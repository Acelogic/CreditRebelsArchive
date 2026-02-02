#!/usr/bin/env python3
"""
Credit Rebels Toolkit - Comprehensive CLI Credit Scoring Tools

Based on the Credit Scoring Primer by Birdman (1976-2023)

Tools included:
1. AAoA Calculator - Average Age of Accounts, Chase 5/24, Scorecard
2. Utilization Optimizer - Calculate optimal balances
3. AZEO Planner - All Zero Except One strategy
4. Inquiry Tracker - Track inquiry aging
5. Derogatory Tracker - Track negative item aging
6. Scorecard Estimator - Determine your FICO 8 scorecard

Usage:
    python credit_toolkit.py              # Interactive menu
    python credit_toolkit.py --help       # Show help
"""

from datetime import datetime, date, timedelta
from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum
import json
import csv
import sys
import os

# ============================================================================
# Data Classes
# ============================================================================

class AccountType(Enum):
    BANKCARD = "Bankcard"
    RETAIL = "Retail Card"
    CHARGE = "Charge Card"
    HELOC = "HELOC"
    AUTO = "Auto Loan"
    MORTGAGE = "Mortgage"
    STUDENT = "Student Loan"
    PERSONAL = "Personal Loan"
    INSTALLMENT = "Installment"
    OTHER = "Other"

    @classmethod
    def revolving_types(cls):
        return {cls.BANKCARD, cls.RETAIL, cls.CHARGE, cls.HELOC}

    @classmethod
    def card_types(cls):
        return {cls.BANKCARD, cls.RETAIL, cls.CHARGE}

    @classmethod
    def from_string(cls, s: str) -> 'AccountType':
        s = s.lower().strip()
        mapping = {
            'bankcard': cls.BANKCARD, 'credit card': cls.BANKCARD, 'cc': cls.BANKCARD,
            'retail': cls.RETAIL, 'store': cls.RETAIL,
            'charge': cls.CHARGE,
            'heloc': cls.HELOC,
            'auto': cls.AUTO, 'car': cls.AUTO,
            'mortgage': cls.MORTGAGE,
            'student': cls.STUDENT,
            'personal': cls.PERSONAL,
            'installment': cls.INSTALLMENT,
        }
        for key, val in mapping.items():
            if key in s:
                return val
        return cls.OTHER


@dataclass
class Account:
    name: str
    open_date: date
    account_type: AccountType
    closed: bool = False

    def age_months(self, as_of: date = None) -> int:
        as_of = as_of or date.today()
        months = (as_of.year - self.open_date.year) * 12 + (as_of.month - self.open_date.month)
        if as_of.day < self.open_date.day:
            months -= 1
        return max(0, months)

    def age_string(self, as_of: date = None) -> str:
        m = self.age_months(as_of)
        years, months = divmod(m, 12)
        if years == 0:
            return f"{months}mo"
        if months == 0:
            return f"{years}yr"
        return f"{years}yr {months}mo"

    def is_revolving(self) -> bool:
        return self.account_type in AccountType.revolving_types()

    def is_card(self) -> bool:
        return self.account_type in AccountType.card_types()


@dataclass
class CreditCard:
    name: str
    limit: float
    balance: float
    statement_day: int = 1

    @property
    def utilization(self) -> float:
        if self.limit <= 0:
            return 0
        return (self.balance / self.limit) * 100


@dataclass
class Inquiry:
    name: str
    date: date

    def age_months(self, as_of: date = None) -> int:
        as_of = as_of or date.today()
        months = (as_of.year - self.date.year) * 12 + (as_of.month - self.date.month)
        return max(0, months)

    def score_impact_end(self) -> date:
        return self.date + timedelta(days=365)

    def falls_off(self) -> date:
        # Falls off between 24-26 months, use 25
        return date(self.date.year + 2, self.date.month, self.date.day) + timedelta(days=30)


@dataclass
class Derogatory:
    name: str
    date: date
    type: str  # '30late', '60late', '90late', 'collection', 'chargeoff', 'bk7', 'bk13'

    def falls_off(self) -> date:
        years = 10 if self.type == 'bk7' else 7
        return date(self.date.year + years, self.date.month, self.date.day)

    def is_dirty_scorecard(self) -> bool:
        return self.type in ('60late', '90late', 'collection', 'chargeoff', 'bk7', 'bk13')


# ============================================================================
# Utility Functions
# ============================================================================

def format_currency(amount: float) -> str:
    return f"${amount:,.0f}"

def format_date(d: date) -> str:
    return d.strftime("%m/%d/%Y")

def parse_date(s: str) -> Optional[date]:
    for fmt in ['%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d', '%m-%d-%Y']:
        try:
            return datetime.strptime(s.strip(), fmt).date()
        except ValueError:
            continue
    return None

def months_to_string(months: int) -> str:
    years, mo = divmod(months, 12)
    if years == 0:
        return f"{mo} months"
    if mo == 0:
        return f"{years} years"
    return f"{years} years, {mo} months"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# ============================================================================
# Tool 1: AAoA Calculator
# ============================================================================

def aaoa_calculator():
    """Calculate Average Age of Accounts and related metrics."""
    accounts: List[Account] = []

    print("\n" + "=" * 60)
    print("         AAoA CALCULATOR")
    print("=" * 60)
    print("\nCommands: add, list, remove N, calculate, back")

    while True:
        cmd = input("\naaoa> ").strip().lower()

        if cmd == 'back' or cmd == 'q':
            return

        elif cmd == 'add':
            name = input("Account name: ").strip()
            date_str = input("Open date (MM/DD/YYYY): ").strip()
            open_date = parse_date(date_str)
            if not open_date:
                print("Invalid date format")
                continue

            print("Types: bankcard, retail, charge, heloc, auto, mortgage, student, personal")
            type_str = input("Account type [bankcard]: ").strip() or "bankcard"

            account = Account(name=name, open_date=open_date, account_type=AccountType.from_string(type_str))
            accounts.append(account)
            print(f"✓ Added: {name} ({account.account_type.value}) - Age: {account.age_string()}")

        elif cmd == 'list':
            if not accounts:
                print("No accounts added.")
            else:
                for i, a in enumerate(accounts, 1):
                    print(f"{i}. {a.name:<25} {a.account_type.value:<12} Age: {a.age_string()}")

        elif cmd.startswith('remove'):
            try:
                idx = int(cmd.split()[1]) - 1
                removed = accounts.pop(idx)
                print(f"✓ Removed: {removed.name}")
            except (IndexError, ValueError):
                print("Usage: remove N")

        elif cmd == 'calculate' or cmd == 'calc':
            if not accounts:
                print("No accounts to analyze.")
                continue

            today = date.today()
            ages = [a.age_months(today) for a in accounts]
            revolving_ages = [a.age_months(today) for a in accounts if a.is_revolving()]
            card_ages_24mo = [a for a in accounts if a.is_card() and a.age_months(today) < 24]

            aaoa = sum(ages) / len(ages)
            aooa = max(ages)
            aoya = min(ages)
            aoora = max(revolving_ages) if revolving_ages else None
            aoyra = min(revolving_ages) if revolving_ages else None

            print("\n" + "-" * 60)
            print("AGING METRICS")
            print("-" * 60)
            print(f"  AAoA  (Average Age):           {months_to_string(int(aaoa))}")
            print(f"  AoOA  (Oldest Account):        {months_to_string(aooa)}")
            print(f"  AoYA  (Youngest Account):      {months_to_string(aoya)}")
            print(f"  AoORA (Oldest Revolving):      {months_to_string(aoora) if aoora else 'N/A'}")
            print(f"  AoYRA (Youngest Revolving):    {months_to_string(aoyra) if aoyra else 'N/A'}")

            # Chase 5/24
            print("\n" + "-" * 60)
            print("CHASE 5/24 STATUS")
            print("-" * 60)
            chase_count = len(card_ages_24mo)
            status = "OVER" if chase_count >= 5 else "UNDER"
            print(f"  Cards opened in 24 months: {chase_count}")
            print(f"  Status: {status} 5/24")
            print(f"  Slots remaining: {max(0, 5 - chase_count)}")

            # Scorecard estimation
            print("\n" + "-" * 60)
            print("FICO 8 SCORECARD ESTIMATION")
            print("-" * 60)
            thick = len(accounts) >= 4
            mature = aooa >= 36
            no_new_rev = (aoyra is None) or (aoyra >= 12)

            scorecard = f"{'Thick' if thick else 'Thin'} / {'Mature' if mature else 'Young'} / {'No New Revolver' if no_new_rev else 'New Revolver'}"
            print(f"  Scorecard: {scorecard}")

            if not mature:
                print(f"  ⏳ {36 - aooa} months until Mature scorecard")
            if not no_new_rev and aoyra:
                print(f"  ⏳ {12 - aoyra} months until No New Revolver bonus (~10-20 pts)")
            if thick and mature and no_new_rev:
                print("  ⭐ You're on the optimal clean scorecard!")

        else:
            print("Commands: add, list, remove N, calculate, back")


# ============================================================================
# Tool 2: Utilization Optimizer
# ============================================================================

def utilization_optimizer():
    """Calculate optimal credit card balances."""
    cards: List[CreditCard] = []

    print("\n" + "=" * 60)
    print("         UTILIZATION OPTIMIZER")
    print("=" * 60)
    print("\nTarget: <9.5% aggregate (or <4.5% for max points)")
    print("Warning: Never $0 on ALL cards (All-Zero penalty: 10-25 pts)")
    print("\nCommands: add, list, remove N, calculate, back")

    while True:
        cmd = input("\nutil> ").strip().lower()

        if cmd == 'back' or cmd == 'q':
            return

        elif cmd == 'add':
            name = input("Card name: ").strip()
            try:
                limit = float(input("Credit limit: $").strip().replace(',', ''))
                balance = float(input("Current balance: $").strip().replace(',', '') or "0")
            except ValueError:
                print("Invalid number")
                continue

            cards.append(CreditCard(name=name, limit=limit, balance=balance))
            print(f"✓ Added: {name} (Limit: {format_currency(limit)}, Util: {(balance/limit)*100:.1f}%)")

        elif cmd == 'list':
            if not cards:
                print("No cards added.")
            else:
                for i, c in enumerate(cards, 1):
                    print(f"{i}. {c.name:<20} Limit: {format_currency(c.limit):<10} Balance: {format_currency(c.balance):<10} Util: {c.utilization:.1f}%")

        elif cmd.startswith('remove'):
            try:
                idx = int(cmd.split()[1]) - 1
                removed = cards.pop(idx)
                print(f"✓ Removed: {removed.name}")
            except (IndexError, ValueError):
                print("Usage: remove N")

        elif cmd == 'calculate' or cmd == 'calc':
            if not cards:
                print("No cards to analyze.")
                continue

            total_limit = sum(c.limit for c in cards)
            total_balance = sum(c.balance for c in cards)
            current_util = (total_balance / total_limit) * 100 if total_limit > 0 else 0

            target_9 = total_limit * 0.095
            target_4 = total_limit * 0.045
            paydown_9 = max(0, total_balance - target_9)
            paydown_4 = max(0, total_balance - target_4)

            print("\n" + "-" * 60)
            print("CURRENT STATUS")
            print("-" * 60)
            print(f"  Total Credit Limit:    {format_currency(total_limit)}")
            print(f"  Total Balance:         {format_currency(total_balance)}")
            print(f"  Aggregate Utilization: {current_util:.1f}%", end="")
            if current_util < 4.5:
                print(" ✓ Excellent")
            elif current_util < 9.5:
                print(" ✓ Good")
            elif current_util < 30:
                print(" ⚠ Moderate")
            else:
                print(" ✗ High")

            print("\n" + "-" * 60)
            print("OPTIMIZATION TARGETS")
            print("-" * 60)
            print(f"  Target for <9.5%:  {format_currency(target_9)}")
            print(f"  Target for <4.5%:  {format_currency(target_4)}")
            if paydown_9 > 0:
                print(f"  Pay down for 9.5%: {format_currency(paydown_9)}")
            else:
                print(f"  Pay down for 9.5%: ✓ Already there!")
            if paydown_4 > 0:
                print(f"  Pay down for 4.5%: {format_currency(paydown_4)}")
            else:
                print(f"  Pay down for 4.5%: ✓ Already there!")

            print("\n" + "-" * 60)
            print("PER-CARD ANALYSIS")
            print("-" * 60)
            print(f"{'Card':<20} {'Limit':>10} {'Balance':>10} {'Util':>8} {'Status':>10}")
            print("-" * 60)
            for c in cards:
                status = "✓ Good" if c.utilization < 9.5 else ("⚠ High" if c.utilization < 30 else "✗ Very High")
                print(f"{c.name:<20} {format_currency(c.limit):>10} {format_currency(c.balance):>10} {c.utilization:>7.1f}% {status:>10}")

            if total_balance == 0:
                print("\n⚠️  WARNING: All-Zero Balance Detected!")
                print("   Leave a small balance ($5-50) on ONE card to avoid 10-25 point penalty.")

        else:
            print("Commands: add, list, remove N, calculate, back")


# ============================================================================
# Tool 3: AZEO Planner
# ============================================================================

def azeo_planner():
    """Plan statement dates for All Zero Except One strategy."""
    cards: List[CreditCard] = []

    print("\n" + "=" * 60)
    print("         AZEO PLANNER (All Zero Except One)")
    print("=" * 60)
    print("\nStrategy: Pay all cards to $0 before statement EXCEPT")
    print("leave a small balance on ONE card to avoid All-Zero penalty.")
    print("\nCommands: add, list, remove N, plan, back")

    while True:
        cmd = input("\nazeo> ").strip().lower()

        if cmd == 'back' or cmd == 'q':
            return

        elif cmd == 'add':
            name = input("Card name: ").strip()
            try:
                day = int(input("Statement closes on day (1-31): ").strip())
                if not 1 <= day <= 31:
                    raise ValueError
                limit = float(input("Credit limit (optional, for balance suggestion): $").strip().replace(',', '') or "0")
            except ValueError:
                print("Invalid input")
                continue

            cards.append(CreditCard(name=name, limit=limit, balance=0, statement_day=day))
            print(f"✓ Added: {name} (Statement day: {day})")

        elif cmd == 'list':
            if not cards:
                print("No cards added.")
            else:
                for i, c in enumerate(cards, 1):
                    print(f"{i}. {c.name:<25} Statement day: {c.statement_day}")

        elif cmd.startswith('remove'):
            try:
                idx = int(cmd.split()[1]) - 1
                removed = cards.pop(idx)
                print(f"✓ Removed: {removed.name}")
            except (IndexError, ValueError):
                print("Usage: remove N")

        elif cmd == 'plan':
            if not cards:
                print("No cards to plan.")
                continue

            # Sort by statement day
            sorted_cards = sorted(cards, key=lambda c: c.statement_day)

            # Pick card with highest limit to leave balance on
            balance_card = max(cards, key=lambda c: c.limit) if any(c.limit > 0 for c in cards) else cards[0]
            target_balance = min(50, balance_card.limit * 0.01) if balance_card.limit > 0 else 10

            print("\n" + "-" * 60)
            print("YOUR AZEO PLAN")
            print("-" * 60)
            print(f"  Card to leave balance on: {balance_card.name}")
            print(f"  Target balance to leave:  {format_currency(target_balance)} (1-9% of limit)")
            print(f"  All other cards:          Pay to $0 before statement")

            print("\n" + "-" * 60)
            print("MONTHLY PAYMENT SCHEDULE")
            print("-" * 60)
            for c in sorted_cards:
                is_balance_card = c.name == balance_card.name
                action = f"✓ Leave ~{format_currency(target_balance)}" if is_balance_card else "→ Pay to $0"
                print(f"  Day {c.statement_day:2}: {c.name:<25} {action}")

        else:
            print("Commands: add, list, remove N, plan, back")


# ============================================================================
# Tool 4: Inquiry Tracker
# ============================================================================

def inquiry_tracker():
    """Track when inquiries stop affecting score and fall off."""
    inquiries: List[Inquiry] = []

    print("\n" + "=" * 60)
    print("         INQUIRY TRACKER")
    print("=" * 60)
    print("\n• Score impact ends: 12 months")
    print("• Falls off report: 24-26 months")
    print("\nCommands: add, list, remove N, timeline, back")

    while True:
        cmd = input("\ninq> ").strip().lower()

        if cmd == 'back' or cmd == 'q':
            return

        elif cmd == 'add':
            name = input("Creditor name: ").strip()
            date_str = input("Inquiry date (MM/DD/YYYY): ").strip()
            inq_date = parse_date(date_str)
            if not inq_date:
                print("Invalid date format")
                continue

            inquiries.append(Inquiry(name=name, date=inq_date))
            print(f"✓ Added: {name} ({format_date(inq_date)})")

        elif cmd == 'list':
            if not inquiries:
                print("No inquiries added.")
            else:
                today = date.today()
                for i, inq in enumerate(inquiries, 1):
                    age = inq.age_months(today)
                    print(f"{i}. {inq.name:<25} {format_date(inq.date)} ({age} months ago)")

        elif cmd.startswith('remove'):
            try:
                idx = int(cmd.split()[1]) - 1
                removed = inquiries.pop(idx)
                print(f"✓ Removed: {removed.name}")
            except (IndexError, ValueError):
                print("Usage: remove N")

        elif cmd == 'timeline':
            if not inquiries:
                print("No inquiries to show.")
                continue

            today = date.today()
            print("\n" + "-" * 60)
            print("INQUIRY TIMELINE")
            print("-" * 60)

            for inq in sorted(inquiries, key=lambda x: x.date):
                score_end = inq.score_impact_end()
                falls_off = inq.falls_off()
                score_done = today >= score_end
                fallen_off = today >= falls_off

                print(f"\n{inq.name}")
                print(f"  Inquiry date: {format_date(inq.date)}")
                if score_done:
                    print("  ✓ Score impact removed")
                else:
                    days_left = (score_end - today).days
                    print(f"  ⏳ Score impact ends: {format_date(score_end)} ({days_left} days)")
                if fallen_off:
                    print("  ✓ Fallen off report")
                else:
                    days_left = (falls_off - today).days
                    print(f"  ⏳ Falls off report: ~{format_date(falls_off)} ({days_left} days)")

        else:
            print("Commands: add, list, remove N, timeline, back")


# ============================================================================
# Tool 5: Derogatory Tracker
# ============================================================================

def derogatory_tracker():
    """Track when negative items age off."""
    derogs: List[Derogatory] = []

    print("\n" + "=" * 60)
    print("         DEROGATORY TRACKER")
    print("=" * 60)
    print("\n• Most items fall off: 7 years")
    print("• Chapter 7 Bankruptcy: 10 years")
    print("• 60+ day late = dirty scorecard for 7 years")
    print("\nCommands: add, list, remove N, timeline, back")

    while True:
        cmd = input("\nderog> ").strip().lower()

        if cmd == 'back' or cmd == 'q':
            return

        elif cmd == 'add':
            name = input("Account/Item name: ").strip()
            date_str = input("Date of derogatory (MM/DD/YYYY): ").strip()
            derog_date = parse_date(date_str)
            if not derog_date:
                print("Invalid date format")
                continue

            print("Types: 30late, 60late, 90late, collection, chargeoff, bk7, bk13")
            derog_type = input("Type [60late]: ").strip().lower() or "60late"

            derogs.append(Derogatory(name=name, date=derog_date, type=derog_type))
            print(f"✓ Added: {name} ({derog_type})")

        elif cmd == 'list':
            if not derogs:
                print("No derogatory items added.")
            else:
                type_labels = {
                    '30late': '30 Day Late', '60late': '60 Day Late', '90late': '90+ Day Late',
                    'collection': 'Collection', 'chargeoff': 'Charge-Off',
                    'bk7': 'Ch.7 Bankruptcy', 'bk13': 'Ch.13 Bankruptcy'
                }
                for i, d in enumerate(derogs, 1):
                    label = type_labels.get(d.type, d.type)
                    print(f"{i}. {d.name:<25} {label:<15} {format_date(d.date)}")

        elif cmd.startswith('remove'):
            try:
                idx = int(cmd.split()[1]) - 1
                removed = derogs.pop(idx)
                print(f"✓ Removed: {removed.name}")
            except (IndexError, ValueError):
                print("Usage: remove N")

        elif cmd == 'timeline':
            if not derogs:
                print("No derogatory items to show.")
                continue

            today = date.today()
            print("\n" + "-" * 60)
            print("DEROGATORY TIMELINE")
            print("-" * 60)

            type_labels = {
                '30late': '30 Day Late', '60late': '60 Day Late', '90late': '90+ Day Late',
                'collection': 'Collection', 'chargeoff': 'Charge-Off',
                'bk7': 'Ch.7 Bankruptcy', 'bk13': 'Ch.13 Bankruptcy'
            }

            for d in sorted(derogs, key=lambda x: x.date):
                falls_off = d.falls_off()
                fallen_off = today >= falls_off

                print(f"\n{d.name} ({type_labels.get(d.type, d.type)})")
                print(f"  Date: {format_date(d.date)}")

                if fallen_off:
                    print("  ✓ Should have fallen off report")
                else:
                    days_left = (falls_off - today).days
                    years_left = days_left / 365
                    print(f"  ⏳ Falls off: {format_date(falls_off)} ({years_left:.1f} years)")

                if d.is_dirty_scorecard():
                    dirty_end = date(d.date.year + 7, d.date.month, d.date.day)
                    if today < dirty_end:
                        dirty_days = (dirty_end - today).days
                        print(f"  ⚠ On dirty scorecard until: {format_date(dirty_end)} ({dirty_days} days)")
                    else:
                        print("  ✓ Should be back on clean scorecard")

        else:
            print("Commands: add, list, remove N, timeline, back")


# ============================================================================
# Tool 6: Scorecard Estimator
# ============================================================================

def scorecard_estimator():
    """Estimate which FICO 8 scorecard you're on."""
    print("\n" + "=" * 60)
    print("         FICO 8 SCORECARD ESTIMATOR")
    print("=" * 60)

    print("\nDo you have any 60+ day lates, collections, bankruptcy,")
    is_clean = input("or other public records in the last 7 years? (y/N): ").strip().lower() != 'y'

    if is_clean:
        try:
            num_accounts = int(input("How many accounts do you have? ").strip() or "0")
            aooa = int(input("Age of oldest account (months)? ").strip() or "0")
            aoyra = int(input("Age of youngest revolving account (months)? [0 if none] ").strip() or "0")
        except ValueError:
            print("Invalid input")
            return

        thick = num_accounts >= 4
        mature = aooa >= 36
        no_new_rev = aoyra == 0 or aoyra >= 12

        print("\n" + "-" * 60)
        print("YOUR ESTIMATED SCORECARD (Clean)")
        print("-" * 60)
        print(f"  File Thickness:   {'Thick' if thick else 'Thin'} ({num_accounts} accounts)")
        print(f"  File Age:         {'Mature' if mature else 'Young'} ({months_to_string(aooa)})")
        print(f"  Revolver Status:  {'No New Revolver' if no_new_rev else 'New Revolver'}")
        print()
        print(f"  → Scorecard: {'Thick' if thick else 'Thin'} / {'Mature' if mature else 'Young'} / {'No New Revolver' if no_new_rev else 'New Revolver'}")

        print("\n" + "-" * 60)
        print("INSIGHTS")
        print("-" * 60)
        if not thick:
            print(f"  • Add {4 - num_accounts} more accounts to become 'Thick'")
        if not mature:
            print(f"  • {36 - aooa} months until 'Mature' scorecard")
        if not no_new_rev and aoyra > 0:
            print(f"  • {12 - aoyra} months until 'No New Revolver' bonus (~10-20 pts)")
        if thick and mature and no_new_rev:
            print("  ⭐ You're on the optimal clean scorecard!")

    else:
        has_pr = input("Do you have collections, bankruptcy, or foreclosure? (y/N): ").strip().lower() == 'y'
        is_recent = input("Is your most recent negative item within 2 years? (y/N): ").strip().lower() == 'y'

        print("\n" + "-" * 60)
        print("YOUR ESTIMATED SCORECARD (Dirty)")
        print("-" * 60)
        severity = "Public Record" if has_pr else "Delinquency"
        recency = "Recent" if is_recent else "Mature"
        print(f"  Severity: {severity}")
        print(f"  Recency:  {recency}")
        print()
        print(f"  → Scorecard: {severity} / {recency}")

        print("\n" + "-" * 60)
        print("INSIGHTS")
        print("-" * 60)
        print("  • You are on a dirty scorecard - this limits maximum score")
        if is_recent:
            print("  • As negative items age, you may move to 'Mature' dirty scorecard")
        print("  • After 7 years (10 for Ch.7 BK), you return to a clean scorecard")

    input("\nPress Enter to continue...")


# ============================================================================
# Main Menu
# ============================================================================

def main_menu():
    """Display main menu and handle selection."""
    while True:
        clear_screen()
        print("=" * 60)
        print("       CREDIT REBELS TOOLKIT")
        print("       Based on the Credit Scoring Primer")
        print("=" * 60)
        print("\n  In Memory of Birdman (1976-2023)")
        print("\n" + "-" * 60)
        print("  TOOLS:")
        print("-" * 60)
        print("  1. AAoA Calculator       - Account ages, Chase 5/24")
        print("  2. Utilization Optimizer - Optimal credit card balances")
        print("  3. AZEO Planner          - All Zero Except One strategy")
        print("  4. Inquiry Tracker       - Track inquiry aging")
        print("  5. Derogatory Tracker    - Track negative item aging")
        print("  6. Scorecard Estimator   - Which FICO 8 scorecard?")
        print("-" * 60)
        print("  q. Quit")
        print()

        choice = input("Select tool (1-6 or q): ").strip().lower()

        if choice == '1':
            aaoa_calculator()
        elif choice == '2':
            utilization_optimizer()
        elif choice == '3':
            azeo_planner()
        elif choice == '4':
            inquiry_tracker()
        elif choice == '5':
            derogatory_tracker()
        elif choice == '6':
            scorecard_estimator()
        elif choice == 'q' or choice == 'quit':
            print("\nGoodbye!")
            break
        else:
            print("Invalid selection")
            input("Press Enter to continue...")


def main():
    if '--help' in sys.argv or '-h' in sys.argv:
        print(__doc__)
        return

    main_menu()


if __name__ == "__main__":
    main()
