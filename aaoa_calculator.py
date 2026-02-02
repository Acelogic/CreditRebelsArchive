#!/usr/bin/env python3
"""
AAoA Calculator - Average Age of Accounts Calculator for Credit Scoring

Recreated from Credit Rebels' calculator. Calculates:
- AAoA (Average Age of Accounts)
- AoOA (Age of Oldest Account)
- AoYA (Age of Youngest Account)
- AoORA (Age of Oldest Revolving Account)
- Chase 5/24 status
- FICO 8 Scorecard estimation

Usage:
    python aaoa_calculator.py                    # Interactive mode
    python aaoa_calculator.py accounts.csv      # Load from CSV
"""

from datetime import datetime, date
from typing import Optional
from dataclasses import dataclass
from enum import Enum
import csv
import sys

class AccountType(Enum):
    BANKCARD = "Bankcard"
    RETAIL = "Retail Card"
    CHARGE = "Charge Card"
    HELOC = "HELOC"
    AUTO = "Auto Loan"
    MORTGAGE = "Mortgage"
    STUDENT = "Student Loan"
    PERSONAL = "Personal Loan"
    INSTALLMENT = "Other Installment"
    OTHER = "Other"

    @classmethod
    def revolving_types(cls):
        """Account types that are considered revolving/open-ended"""
        return {cls.BANKCARD, cls.RETAIL, cls.CHARGE, cls.HELOC}

    @classmethod
    def from_string(cls, s: str) -> 'AccountType':
        s = s.lower().strip()
        mapping = {
            'bankcard': cls.BANKCARD, 'bank card': cls.BANKCARD, 'credit card': cls.BANKCARD, 'cc': cls.BANKCARD,
            'retail': cls.RETAIL, 'store card': cls.RETAIL,
            'charge': cls.CHARGE, 'charge card': cls.CHARGE,
            'heloc': cls.HELOC, 'home equity': cls.HELOC,
            'auto': cls.AUTO, 'car': cls.AUTO, 'vehicle': cls.AUTO,
            'mortgage': cls.MORTGAGE, 'home': cls.MORTGAGE,
            'student': cls.STUDENT, 'student loan': cls.STUDENT,
            'personal': cls.PERSONAL, 'personal loan': cls.PERSONAL,
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
    close_date: Optional[date] = None
    reports_eq: bool = True
    reports_tu: bool = True
    reports_ex: bool = True

    def age_in_months(self, as_of: date = None) -> int:
        """Calculate age in months (FICO uses whole months)"""
        as_of = as_of or date.today()
        # If closed, use close date for age calculation in some models
        # But for AAoA, we typically use current date
        years = as_of.year - self.open_date.year
        months = as_of.month - self.open_date.month
        total_months = years * 12 + months
        # Adjust if day hasn't passed yet this month
        if as_of.day < self.open_date.day:
            total_months -= 1
        return max(0, total_months)

    def age_string(self, as_of: date = None) -> str:
        """Human readable age"""
        months = self.age_in_months(as_of)
        years = months // 12
        remaining_months = months % 12
        if years == 0:
            return f"{remaining_months}mo"
        elif remaining_months == 0:
            return f"{years}yr"
        else:
            return f"{years}yr {remaining_months}mo"

    def is_revolving(self) -> bool:
        return self.account_type in AccountType.revolving_types()

    def opened_within_months(self, months: int, as_of: date = None) -> bool:
        """Check if account was opened within last N months"""
        as_of = as_of or date.today()
        return self.age_in_months(as_of) < months


class AAoACalculator:
    def __init__(self):
        self.accounts: list[Account] = []

    def add_account(self, account: Account):
        self.accounts.append(account)

    def remove_account(self, index: int):
        if 0 <= index < len(self.accounts):
            self.accounts.pop(index)

    def clear(self):
        self.accounts = []

    def get_accounts_for_bureau(self, bureau: str) -> list[Account]:
        """Get accounts that report to a specific bureau"""
        bureau = bureau.upper()
        if bureau == 'EQ':
            return [a for a in self.accounts if a.reports_eq]
        elif bureau == 'TU':
            return [a for a in self.accounts if a.reports_tu]
        elif bureau == 'EX':
            return [a for a in self.accounts if a.reports_ex]
        return self.accounts

    def calculate_aaoa(self, accounts: list[Account] = None, as_of: date = None) -> Optional[float]:
        """Calculate Average Age of Accounts in months"""
        accounts = accounts if accounts is not None else self.accounts
        if not accounts:
            return None
        total_months = sum(a.age_in_months(as_of) for a in accounts)
        return total_months / len(accounts)

    def calculate_aooa(self, accounts: list[Account] = None, as_of: date = None) -> Optional[int]:
        """Age of Oldest Account in months"""
        accounts = accounts if accounts is not None else self.accounts
        if not accounts:
            return None
        return max(a.age_in_months(as_of) for a in accounts)

    def calculate_aoya(self, accounts: list[Account] = None, as_of: date = None) -> Optional[int]:
        """Age of Youngest Account in months"""
        accounts = accounts if accounts is not None else self.accounts
        if not accounts:
            return None
        return min(a.age_in_months(as_of) for a in accounts)

    def calculate_aoora(self, accounts: list[Account] = None, as_of: date = None) -> Optional[int]:
        """Age of Oldest Revolving Account in months"""
        accounts = accounts if accounts is not None else self.accounts
        revolving = [a for a in accounts if a.is_revolving()]
        if not revolving:
            return None
        return max(a.age_in_months(as_of) for a in revolving)

    def calculate_aoyra(self, accounts: list[Account] = None, as_of: date = None) -> Optional[int]:
        """Age of Youngest Revolving Account in months"""
        accounts = accounts if accounts is not None else self.accounts
        revolving = [a for a in accounts if a.is_revolving()]
        if not revolving:
            return None
        return min(a.age_in_months(as_of) for a in revolving)

    def calculate_chase_524(self, as_of: date = None) -> dict:
        """
        Chase 5/24 Rule: Chase will deny most credit cards if you've opened
        5 or more personal credit cards (any issuer) in the last 24 months.
        """
        as_of = as_of or date.today()
        # Count cards opened in last 24 months (bankcards and retail)
        card_types = {AccountType.BANKCARD, AccountType.RETAIL, AccountType.CHARGE}
        recent_cards = [
            a for a in self.accounts
            if a.account_type in card_types and a.opened_within_months(24, as_of)
        ]
        count = len(recent_cards)
        return {
            'count': count,
            'status': 'OVER' if count >= 5 else 'UNDER',
            'slots_remaining': max(0, 5 - count),
            'recent_cards': recent_cards
        }

    def estimate_scorecard(self, bureau: str = None, as_of: date = None) -> dict:
        """
        Estimate FICO 8 scorecard based on known segmentation factors.

        Clean scorecards segmented by:
        - Thick/Thin: 4+ accounts = Thick
        - Mature/Young: 36+ months AoOA = Mature
        - No New Revolver/New Revolver: 12+ months AoYRA = No New Revolver
        """
        accounts = self.get_accounts_for_bureau(bureau) if bureau else self.accounts

        if not accounts:
            return {'scorecard': 'Unknown', 'factors': {}}

        num_accounts = len(accounts)
        aooa = self.calculate_aooa(accounts, as_of)
        aoyra = self.calculate_aoyra(accounts, as_of)

        # Determine factors
        thick = num_accounts >= 4
        mature = aooa >= 36 if aooa else False
        no_new_revolver = aoyra >= 12 if aoyra else True  # No revolvers = no new revolver

        # Build scorecard name
        factors = {
            'file_thickness': 'Thick' if thick else 'Thin',
            'file_age': 'Mature' if mature else 'Young',
            'revolver_status': 'No New Revolver' if no_new_revolver else 'New Revolver',
            'num_accounts': num_accounts,
            'aooa_months': aooa,
            'aoyra_months': aoyra
        }

        scorecard = f"{'Thick' if thick else 'Thin'}/{'Mature' if mature else 'Young'}/{'No New Revolver' if no_new_revolver else 'New Revolver'}"

        return {'scorecard': scorecard, 'factors': factors}

    def full_report(self, as_of: date = None) -> str:
        """Generate a full analysis report"""
        as_of = as_of or date.today()
        lines = []
        lines.append("=" * 60)
        lines.append("         AAoA CALCULATOR - CREDIT AGE ANALYSIS")
        lines.append("=" * 60)
        lines.append(f"Analysis Date: {as_of.strftime('%B %d, %Y')}")
        lines.append(f"Total Accounts: {len(self.accounts)}")
        lines.append("")

        # Account list
        if self.accounts:
            lines.append("-" * 60)
            lines.append("ACCOUNTS")
            lines.append("-" * 60)
            for i, acct in enumerate(self.accounts, 1):
                status = " (CLOSED)" if acct.closed else ""
                bureaus = []
                if acct.reports_eq: bureaus.append("EQ")
                if acct.reports_tu: bureaus.append("TU")
                if acct.reports_ex: bureaus.append("EX")
                bureau_str = ",".join(bureaus) if len(bureaus) < 3 else "All"
                lines.append(f"{i:2}. {acct.name[:20]:<20} {acct.account_type.value:<15} "
                           f"Opened: {acct.open_date.strftime('%m/%d/%Y')}  "
                           f"Age: {acct.age_string(as_of):<10}{status}")

        lines.append("")
        lines.append("-" * 60)
        lines.append("AGING METRICS (All Bureaus)")
        lines.append("-" * 60)

        def months_to_str(m):
            if m is None:
                return "N/A"
            years = int(m) // 12
            months = int(m) % 12
            if years == 0:
                return f"{months} months"
            return f"{years} years, {months} months"

        aaoa = self.calculate_aaoa(as_of=as_of)
        lines.append(f"  AAoA  (Average Age of Accounts):    {months_to_str(aaoa)}")
        lines.append(f"  AoOA  (Age of Oldest Account):      {months_to_str(self.calculate_aooa(as_of=as_of))}")
        lines.append(f"  AoYA  (Age of Youngest Account):    {months_to_str(self.calculate_aoya(as_of=as_of))}")
        lines.append(f"  AoORA (Age of Oldest Revolving):    {months_to_str(self.calculate_aoora(as_of=as_of))}")
        lines.append(f"  AoYRA (Age of Youngest Revolving):  {months_to_str(self.calculate_aoyra(as_of=as_of))}")

        # Per-bureau breakdown
        lines.append("")
        lines.append("-" * 60)
        lines.append("PER-BUREAU BREAKDOWN")
        lines.append("-" * 60)
        lines.append(f"{'Metric':<8} {'All':>12} {'Equifax':>12} {'TransUnion':>12} {'Experian':>12}")
        lines.append("-" * 60)

        for bureau in [None, 'EQ', 'TU', 'EX']:
            accts = self.get_accounts_for_bureau(bureau) if bureau else self.accounts
            aaoa_val = self.calculate_aaoa(accts, as_of)
            # Just show for the header row

        all_accts = self.accounts
        eq_accts = self.get_accounts_for_bureau('EQ')
        tu_accts = self.get_accounts_for_bureau('TU')
        ex_accts = self.get_accounts_for_bureau('EX')

        def fmt(val):
            if val is None:
                return "N/A"
            return f"{val:.1f}mo"

        lines.append(f"{'AAoA':<8} {fmt(self.calculate_aaoa(all_accts, as_of)):>12} "
                    f"{fmt(self.calculate_aaoa(eq_accts, as_of)):>12} "
                    f"{fmt(self.calculate_aaoa(tu_accts, as_of)):>12} "
                    f"{fmt(self.calculate_aaoa(ex_accts, as_of)):>12}")

        lines.append(f"{'# Accts':<8} {len(all_accts):>12} {len(eq_accts):>12} {len(tu_accts):>12} {len(ex_accts):>12}")

        # Chase 5/24
        lines.append("")
        lines.append("-" * 60)
        lines.append("CHASE 5/24 STATUS")
        lines.append("-" * 60)
        chase = self.calculate_chase_524(as_of)
        status_icon = "❌ OVER" if chase['status'] == 'OVER' else "✅ UNDER"
        lines.append(f"  Status: {status_icon} 5/24")
        lines.append(f"  Cards opened in last 24 months: {chase['count']}")
        lines.append(f"  Slots remaining: {chase['slots_remaining']}")
        if chase['recent_cards']:
            lines.append("  Recent cards:")
            for card in chase['recent_cards']:
                lines.append(f"    - {card.name} (opened {card.open_date.strftime('%m/%d/%Y')})")

        # Scorecard estimation
        lines.append("")
        lines.append("-" * 60)
        lines.append("FICO 8 SCORECARD ESTIMATION")
        lines.append("-" * 60)
        sc = self.estimate_scorecard(as_of=as_of)
        lines.append(f"  Estimated Scorecard: {sc['scorecard']}")
        lines.append(f"  File Thickness: {sc['factors'].get('file_thickness', 'Unknown')} ({sc['factors'].get('num_accounts', 0)} accounts)")
        lines.append(f"  File Age: {sc['factors'].get('file_age', 'Unknown')} (AoOA: {sc['factors'].get('aooa_months', 'N/A')} months)")
        lines.append(f"  Revolver Status: {sc['factors'].get('revolver_status', 'Unknown')} (AoYRA: {sc['factors'].get('aoyra_months', 'N/A')} months)")

        # Key insights
        lines.append("")
        lines.append("-" * 60)
        lines.append("KEY INSIGHTS FROM CREDIT SCORING PRIMER")
        lines.append("-" * 60)

        if aaoa:
            if aaoa >= 90:
                lines.append("  ✅ AAoA >= 90 months: Believed to be at/near max AAoA award")
            elif aaoa >= 60:
                lines.append("  📈 AAoA 60-90 months: Good age, approaching optimal")
            elif aaoa >= 36:
                lines.append("  📊 AAoA 36-60 months: Moderate age")
            else:
                lines.append("  ⚠️  AAoA < 36 months: Young file, age will help over time")

        aooa = self.calculate_aooa(as_of=as_of)
        if aooa:
            if aooa >= 36:
                lines.append("  ✅ AoOA >= 36 months: Qualifies for 'Mature' scorecard")
            else:
                months_to_mature = 36 - aooa
                lines.append(f"  ⏳ AoOA < 36 months: {months_to_mature} months until 'Mature' scorecard")

        aoyra = self.calculate_aoyra(as_of=as_of)
        if aoyra is not None:
            if aoyra >= 12:
                lines.append("  ✅ AoYRA >= 12 months: Qualifies for 'No New Revolver' scorecard (~10-20 pts)")
            else:
                months_to_nnr = 12 - aoyra
                lines.append(f"  ⏳ AoYRA < 12 months: {months_to_nnr} months until 'No New Revolver' bonus")

        lines.append("")
        lines.append("=" * 60)

        return "\n".join(lines)

    def load_from_csv(self, filepath: str):
        """Load accounts from CSV file"""
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Parse date - try multiple formats
                date_str = row.get('open_date', row.get('opened', ''))
                for fmt in ['%m/%d/%Y', '%Y-%m-%d', '%m-%d-%Y', '%m/%d/%y']:
                    try:
                        open_date = datetime.strptime(date_str, fmt).date()
                        break
                    except ValueError:
                        continue
                else:
                    print(f"Warning: Could not parse date '{date_str}', skipping")
                    continue

                account = Account(
                    name=row.get('name', 'Unknown'),
                    open_date=open_date,
                    account_type=AccountType.from_string(row.get('type', 'bankcard')),
                    closed=row.get('closed', '').lower() in ('true', 'yes', '1', 'x'),
                    reports_eq=row.get('eq', 'true').lower() not in ('false', 'no', '0'),
                    reports_tu=row.get('tu', 'true').lower() not in ('false', 'no', '0'),
                    reports_ex=row.get('ex', 'true').lower() not in ('false', 'no', '0'),
                )
                self.add_account(account)

    def save_to_csv(self, filepath: str):
        """Save accounts to CSV file"""
        with open(filepath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'open_date', 'type', 'closed', 'close_date', 'eq', 'tu', 'ex'])
            for acct in self.accounts:
                writer.writerow([
                    acct.name,
                    acct.open_date.strftime('%m/%d/%Y'),
                    acct.account_type.value,
                    'yes' if acct.closed else 'no',
                    acct.close_date.strftime('%m/%d/%Y') if acct.close_date else '',
                    'yes' if acct.reports_eq else 'no',
                    'yes' if acct.reports_tu else 'no',
                    'yes' if acct.reports_ex else 'no',
                ])


def parse_date(date_str: str) -> Optional[date]:
    """Parse a date string in various formats"""
    date_str = date_str.strip()
    formats = ['%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d', '%m-%d-%Y', '%m-%d-%y']
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None


def interactive_mode():
    """Run calculator in interactive mode"""
    calc = AAoACalculator()

    print("\n" + "=" * 60)
    print("       AAoA CALCULATOR - Interactive Mode")
    print("=" * 60)
    print("\nCommands:")
    print("  add       - Add a new account")
    print("  remove N  - Remove account #N")
    print("  list      - List all accounts")
    print("  report    - Show full analysis report")
    print("  save FILE - Save accounts to CSV")
    print("  load FILE - Load accounts from CSV")
    print("  clear     - Clear all accounts")
    print("  quit      - Exit")
    print()

    while True:
        try:
            cmd = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not cmd:
            continue

        parts = cmd.split(maxsplit=1)
        action = parts[0]
        arg = parts[1] if len(parts) > 1 else None

        if action in ('quit', 'exit', 'q'):
            print("Goodbye!")
            break

        elif action == 'add':
            print("\nAdd New Account")
            print("-" * 30)

            name = input("Account name (e.g., 'Chase Sapphire'): ").strip()
            if not name:
                name = "Account"

            date_str = input("Open date (MM/DD/YYYY): ").strip()
            open_date = parse_date(date_str)
            if not open_date:
                print("Invalid date format. Please use MM/DD/YYYY")
                continue

            print("Account types: bankcard, retail, charge, heloc, auto, mortgage, student, personal, installment")
            type_str = input("Account type [bankcard]: ").strip() or "bankcard"
            acct_type = AccountType.from_string(type_str)

            closed = input("Is this account closed? (y/N): ").strip().lower() == 'y'

            account = Account(
                name=name,
                open_date=open_date,
                account_type=acct_type,
                closed=closed
            )
            calc.add_account(account)
            print(f"✓ Added: {name} ({acct_type.value}) - Age: {account.age_string()}")

        elif action == 'remove':
            if arg and arg.isdigit():
                idx = int(arg) - 1
                if 0 <= idx < len(calc.accounts):
                    removed = calc.accounts[idx]
                    calc.remove_account(idx)
                    print(f"✓ Removed: {removed.name}")
                else:
                    print("Invalid account number")
            else:
                print("Usage: remove N (where N is account number)")

        elif action == 'list':
            if not calc.accounts:
                print("No accounts added yet.")
            else:
                print(f"\nAccounts ({len(calc.accounts)} total):")
                print("-" * 50)
                for i, acct in enumerate(calc.accounts, 1):
                    status = " (CLOSED)" if acct.closed else ""
                    print(f"{i:2}. {acct.name:<25} {acct.account_type.value:<12} "
                          f"Age: {acct.age_string()}{status}")

        elif action == 'report':
            if not calc.accounts:
                print("No accounts to analyze. Add some accounts first.")
            else:
                print(calc.full_report())

        elif action == 'save':
            if arg:
                try:
                    calc.save_to_csv(arg)
                    print(f"✓ Saved {len(calc.accounts)} accounts to {arg}")
                except Exception as e:
                    print(f"Error saving: {e}")
            else:
                print("Usage: save filename.csv")

        elif action == 'load':
            if arg:
                try:
                    calc.load_from_csv(arg)
                    print(f"✓ Loaded {len(calc.accounts)} accounts from {arg}")
                except FileNotFoundError:
                    print(f"File not found: {arg}")
                except Exception as e:
                    print(f"Error loading: {e}")
            else:
                print("Usage: load filename.csv")

        elif action == 'clear':
            calc.clear()
            print("✓ All accounts cleared")

        else:
            print(f"Unknown command: {action}")
            print("Type 'help' or just press Enter to see commands")


def main():
    if len(sys.argv) > 1:
        # Load from file
        filepath = sys.argv[1]
        calc = AAoACalculator()
        try:
            calc.load_from_csv(filepath)
            print(calc.full_report())
        except FileNotFoundError:
            print(f"File not found: {filepath}")
            sys.exit(1)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
