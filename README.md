# Credit Rebels Archive

> *Preserving invaluable credit knowledge for future generations*

## [Launch the Credit Toolkit](https://acelogic.github.io/CreditRebelsArchive/)

---

## In Memoriam: Birdman (1976 - 2023)

This repository is dedicated to the memory of **Birdman** (also known as Birdman7 and MFBirdman7), the brilliant mind behind the Credit Scoring Primer - widely recognized as the most comprehensive and accurate publicly available resource on FICO credit scoring.

Birdman tragically passed away in a car accident in 2023. His tireless work reverse-engineering FICO scoring algorithms, his willingness to share knowledge freely, and his dedication to helping others improve their financial lives left an indelible mark on the credit community.

> *"He was the reason I joined this forum. Birdman's encouragement/wisdom along with some of the other members here really helped me dig myself out of a desperate/hopeless credit situation."*

His work lives on in these pages.

---

## Quick Start

**New to credit?** Start with the [Credit 101 Beginner's Guide](docs/Credit_101_Beginners_Guide.md)

**Ready to optimize?** Use the [Credit Toolkit](https://acelogic.github.io/CreditRebelsArchive/)

**Want the deep dive?** Read the full [Credit Scoring Primer](docs/Credit_Scoring_Primer_v2.pdf)

---

## Repository Structure

```
CreditRebelsArchive/
├── index.html                              # Web-based Credit Toolkit
├── README.md                               # You are here
├── docs/
│   ├── Credit_101_Beginners_Guide.md       # Simplified intro for newcomers
│   ├── Credit_101_Beginners_Guide.pdf      # PDF version
│   ├── Credit_Scoring_Primer_v2.pdf        # The complete technical guide
│   ├── credit_scoring_primer.txt           # Plain text version
│   ├── Goodwill_Saturation_Technique.pdf   # Strategy for removing late payments
│   ├── goodwill_saturation_technique.txt   # Plain text version
│   ├── CART_Method_Goodwill_Letters.pdf    # Letter writing template
│   └── cart_method_goodwill_letters.txt    # Plain text version
└── tools/
    └── aaoa_calculator.py                  # Python CLI tool for developers
```

---

## The Credit Toolkit (Web App)

A free, privacy-focused web app with everything you need:

| Tool | Description |
|------|-------------|
| **AAoA Calculator** | Calculate average age, Chase 5/24 status, scorecard estimation |
| **Utilization Optimizer** | Find target balances for optimal utilization |
| **AZEO Planner** | Plan statement dates for "All Zero Except One" strategy |
| **Inquiry Tracker** | Countdown to score recovery and report removal |
| **Derogatory Tracker** | Track when negative items age off |
| **Scorecard Estimator** | Identify which FICO 8 scorecard you're on |
| **Quick Reference** | Key thresholds and optimal values |

**Privacy:** All data stored locally in your browser. No servers, no tracking, no cookies.

---

## Documentation

### For Beginners
- [**Credit 101 Beginner's Guide**](docs/Credit_101_Beginners_Guide.md) - Start here if you're new to credit

### Core Guides
- [**Credit Scoring Primer v2.0**](docs/Credit_Scoring_Primer_v2.pdf) - The complete technical deep-dive
- [**Goodwill Saturation Technique**](docs/Goodwill_Saturation_Technique.pdf) - How to get negative items removed
- [**CART Method**](docs/CART_Method_Goodwill_Letters.pdf) - Template for writing effective goodwill letters

---

## Key Concepts at a Glance

### The Five Categories (FICO 8)

| Category | Weight | What It Means |
|----------|--------|---------------|
| Payment History | 35% | Pay on time, every time |
| Amounts Owed | 30% | Keep utilization below 9.5% |
| Length of History | 15% | Older accounts = better |
| New Credit | 10% | Don't apply too often |
| Credit Mix | 10% | Have different account types |

### Magic Numbers

| Metric | Target | Why |
|--------|--------|-----|
| Utilization | <9.5% | Major threshold for max points |
| Utilization (aggressive) | <4.5% | Extra points on some scorecards |
| AoOA (Age of Oldest) | 36+ months | Moves you to "Mature" scorecard |
| AoYRA (Youngest Revolver) | 12+ months | "No New Revolver" bonus (~10-20 pts) |
| Revolving Balance | >$0 | Avoid "All Zero" penalty (10-25 pts) |
| Inquiries | 0 | Impact removed at 12 months |

### Common Traps

| Trap | What Happens | How to Avoid |
|------|--------------|--------------|
| All-Zero Balances | Lose 10-25 points | Keep small balance on ONE card |
| Closing Old Cards | Hurts average age + utilization | Keep old cards open |
| Too Many Applications | Hurts score + triggers denials | "Garden" for 6-12 months |
| Paying After Statement | Balance already reported | Pay BEFORE statement date |

---

## CLI Tool for Developers

For those who prefer command-line tools:

```bash
# Interactive mode
python tools/aaoa_calculator.py

# Load from CSV
python tools/aaoa_calculator.py accounts.csv
```

Features: AAoA calculation, Chase 5/24, scorecard estimation, CSV import/export.

---

## Contributing

Found an error? Have additional research? Contributions welcome!

- Open an issue or pull request
- Help preserve other valuable credit education resources
- Share this archive with others who could benefit

---

## Disclaimer

This is **educational information only**, not financial advice. FICO scoring is proprietary - this information is based on reverse-engineering and community research. Your actual scores may vary. Always verify important financial decisions with a qualified professional.

---

## Credits

- **Birdman** (MFBirdman7) - Credit Scoring Primer author
- **MWGardener19** - Original concept
- **BrutalBodyShots** - Goodwill Saturation Technique, CART Method
- **Credit Rebels Community** - Collective knowledge and testing
- **MyFICO Forums Contributors** - Research that informed this work

---

## Source

Content archived from [Credit Rebels](https://www.creditrebels.net) via the [Wayback Machine](https://web.archive.org) in February 2026.

---

*"If you REALLY want to know how it all works, sit back, get comfy, and pack a lunch, because this is going to be a bumpy ride."* — Birdman
