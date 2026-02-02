# Credit Rebels Archive

> *Preserving invaluable credit knowledge for future generations*

---

## In Memoriam: Birdman (1976 - 2023)

This repository is dedicated to the memory of **Birdman** (also known as Birdman7 and MFBirdman7), the brilliant mind behind the Credit Scoring Primer - widely recognized as the most comprehensive and accurate publicly available resource on FICO credit scoring.

Birdman tragically passed away in a car accident in 2023. His tireless work reverse-engineering FICO scoring algorithms, his willingness to share knowledge freely, and his dedication to helping others improve their financial lives left an indelible mark on the credit community.

> *"The effort he put into the Credit Scoring Primer really shows so much."*
> — Credit Rebels community member

> *"He was the reason I joined this forum. Birdman's encouragement/wisdom along with some of the other members here really helped me dig myself out of a desperate/hopeless credit situation."*
> — Cassie, Credit Rebels member

His work lives on in these pages. May his legacy continue to help people achieve their financial goals.

---

## About This Archive

The original Credit Rebels website (creditrebels.net) has become unreliable/inaccessible. This archive preserves the most valuable educational content from the site, rescued from the Wayback Machine before it could be lost forever.

**This is not a credit repair service.** This is educational material to help you understand how credit scoring works so you can make informed decisions about your own credit.

---

## Contents

### Core Guides

| File | Description |
|------|-------------|
| **Credit_Scoring_Primer_v2.pdf** | The complete FICO Score 8 guide - scorecards, utilization thresholds, age factors, derogatory impacts, and more. This is the crown jewel. |
| **credit_scoring_primer.txt** | Plain text version of the Credit Scoring Primer |
| **Goodwill_Saturation_Technique.pdf** | Strategy for getting late payments removed through volume and timing |
| **CART_Method_Goodwill_Letters.pdf** | Template for writing effective goodwill letters |

### Tools

| File | Description |
|------|-------------|
| **aaoa_calculator.py** | Python recreation of the AAoA Calculator for computing credit age metrics |

---

## The Credit Scoring Primer

The Credit Scoring Primer v2.0 is a comprehensive deep-dive into FICO Score 8 mechanics. Topics covered include:

- **Scorecard Segmentation** - How FICO assigns you to one of 12 scorecards (8 clean, 4 dirty) based on your profile
- **Payment History (35%)** - Delinquencies, collections, charge-offs, and their decay over time
- **Amount of Debt (30%)** - Utilization thresholds (the magic <9.5%), AWB, revolving balance strategies
- **Length of History (15%)** - AoOA, AAoA, AoYA, AoORA, AoYRA and their optimal values
- **New Credit (10%)** - Inquiry impacts and the 12-month decay
- **Credit Mix (10%)** - Account diversity and optimal ratios
- **Scorecard Reassignment** - What happens when you cross thresholds (rebucketing)
- **Mortgage Scores (5/4/2)** - Differences from Score 8
- **Score 9** - Changes and improvements over Score 8

### Key Optimal Values (FICO 8)

| Metric | Optimal Value |
|--------|---------------|
| Payment History | 100%, zero delinquencies |
| Aggregate Utilization | <9.5% (or <4.5% on some scorecards) |
| Retail Utilization | $0 |
| Revolving Balance | <$1000, but never $0 (All-Zero penalty) |
| AAoA (Average Age) | ~90 months for max award |
| AoOA (Oldest Account) | 36+ months for "Mature" scorecard |
| AoYRA (Youngest Revolver) | 12+ months for "No New Revolver" bonus (~10-20 pts) |
| Inquiries | 0 (penalty removed at 365 days) |

---

## Goodwill Saturation Technique

Created by **BrutalBodyShots** in 2016, this technique maximizes your chances of getting negative but accurate items removed through goodwill:

1. **Find multiple addresses** for your target institution (6-12+)
2. **Send identical letters** to all addresses
3. **Vary the mailing days** (Round 1 on Monday, Round 2 on Thursday, etc.)
4. **Wait ~1 month between rounds**
5. **Track responses** and add new addresses to your database
6. **Nurture "nibblers"** - contacts who seem sympathetic

The key insight: it's a numbers game. More letters = more unique eyes = higher probability of success.

---

## CART Method for Goodwill Letters

A simple framework for writing effective goodwill letters:

- **C**ourtesy - Be pleasant, they're doing you a favor
- **A**pologize - Own your mistake sincerely
- **R**easons - Explain why it happened and why it won't again (appeal to emotions)
- **T**hank - Express gratitude for their time and consideration

---

## AAoA Calculator

A Python tool that calculates:

- **AAoA** - Average Age of Accounts
- **AoOA** - Age of Oldest Account
- **AoYA** - Age of Youngest Account
- **AoORA** - Age of Oldest Revolving Account
- **AoYRA** - Age of Youngest Revolving Account
- **Chase 5/24 Status** - Are you over or under Chase's 5-cards-in-24-months rule?
- **FICO 8 Scorecard Estimation** - Which of the 12 scorecards are you likely on?

### Usage

```bash
# Interactive mode
python aaoa_calculator.py

# Load from CSV
python aaoa_calculator.py accounts.csv
```

### CSV Format

```csv
name,open_date,type,closed,close_date,eq,tu,ex
Chase Sapphire,03/15/2019,bankcard,no,,yes,yes,yes
Auto Loan,05/10/2021,auto,no,,yes,yes,yes
```

---

## Important Disclaimers

1. **This is educational material only.** It is not financial advice.
2. **FICO scoring is proprietary.** Much of this information is reverse-engineered and may not be 100% accurate.
3. **Scores vary.** Your mileage may vary based on your specific profile and scorecard.
4. **Laws change.** Credit reporting regulations evolve over time.
5. **Don't dispute accurate information** unless you understand the consequences.

---

## Credits & Attribution

- **Birdman** (MFBirdman7) - Primary author of the Credit Scoring Primer
- **MWGardener19** - Original concept and introduction
- **BrutalBodyShots** - Goodwill Saturation Technique and CART Method
- **Credit Rebels Community** - Collective knowledge and testing
- **MyFICO Forums Contributors** - Thomas_Thumb, Revelate, and many others whose research informed this work

---

## Archive Source

Content archived from [Credit Rebels](https://www.creditrebels.net) via the [Wayback Machine](https://web.archive.org) on February 2, 2026.

If you find this archive valuable, consider:
- Sharing it with others who could benefit
- Contributing corrections or updates via pull request
- Preserving other valuable credit education resources before they disappear

---

*"If you REALLY want to know how it all works, or at least as much as is known, sit back, get comfy, and pack a lunch, because this is going to be a bumpy ride."*
— Birdman, Credit Scoring Primer
