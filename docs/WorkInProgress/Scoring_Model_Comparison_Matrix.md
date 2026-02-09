# Scoring Model Comparison Matrix

**A comprehensive side-by-side reference for all FICO and VantageScore models**

Companion document to the *Credit Scoring Primer v2.0* (Birdman / Credit Rebels).
Last updated: February 2026.

> This reference is written for a credit-savvy audience that already understands
> the basics of FICO scoring (scorecards, segmentation factors, scoring factors,
> AZEO, utilization, etc.). If any of those terms are unfamiliar, read the
> Credit Scoring Primer first.

---

## Table of Contents

1. [Complete Model Inventory](#1-complete-model-inventory)
2. [Key Feature Comparison -- General Purpose Models](#2-key-feature-comparison----general-purpose-models)
3. [Optimization Strategy Differences by Model](#3-optimization-strategy-differences-by-model)
4. [Which Score Matters? Decision Tree](#4-which-score-matters-decision-tree)
5. [Where to Check Your Scores](#5-where-to-check-your-scores)
6. [Glossary of Abbreviations](#6-glossary-of-abbreviations)

---

## 1. Complete Model Inventory

Every commercially deployed FICO and VantageScore model, organized by family.
A dash (--) means the model is not available at that bureau.

### 1a. General Purpose FICO Scores (Range 300--850)

| Model | Experian | Equifax | TransUnion | Base Year | Status |
|---|:---:|:---:|:---:|:---:|---|
| FICO Score 2 (a.k.a. Experian/Fair Isaac Risk Model V2) | Yes | -- | -- | 1998 | Legacy -- mortgage only |
| FICO Score 3 (Experian/Fair Isaac Bankcard Risk Score V3) | Yes | -- | -- | 2004 | Legacy -- Experian bankcard |
| FICO Score 4 (TransUnion FICO Risk Score 04) | -- | -- | Yes | 2004 | Legacy -- mortgage only |
| FICO Score 5 (Equifax Beacon 5.0) | -- | Yes | -- | 2004 | Legacy -- mortgage only |
| FICO Score 8 | Yes | Yes | Yes | 2009 | **Most widely used** |
| FICO Score 9 | Yes | Yes | Yes | 2014 | Current -- limited adoption |
| FICO Score 10 | Yes | Yes | Yes | 2020 | Newest general -- growing adoption |
| FICO Score 10 T | Yes | Yes | Yes | 2020 | Newest general -- trended data |

### 1b. FICO Auto Scores (Range 250--900)

| Model | Experian | Equifax | TransUnion | Base Year | Notes |
|---|:---:|:---:|:---:|:---:|---|
| FICO Auto Score 2 | Yes | -- | -- | 1998 | Legacy -- Experian only |
| FICO Auto Score 4 | -- | -- | Yes | 2004 | Legacy -- TransUnion only |
| FICO Auto Score 5 | -- | Yes | -- | 2004 | Legacy -- Equifax only |
| FICO Auto Score 8 | Yes | Yes | Yes | 2009 | Widely used for auto |
| FICO Auto Score 9 | Yes | Yes | Yes | 2014 | Current auto |
| FICO Auto Score 10 | Yes | Yes | Yes | 2020 | Newest auto |

### 1c. FICO Bankcard Scores (Range 250--900)

| Model | Experian | Equifax | TransUnion | Base Year | Notes |
|---|:---:|:---:|:---:|:---:|---|
| FICO Bankcard Score 2 | Yes | -- | -- | 1998 | Legacy -- Experian only |
| FICO Bankcard Score 4 | -- | -- | Yes | 2004 | Legacy -- TransUnion only |
| FICO Bankcard Score 5 | -- | Yes | -- | 2004 | Legacy -- Equifax only |
| FICO Bankcard Score 8 | Yes | Yes | Yes | 2009 | Widely used for cards |
| FICO Bankcard Score 9 | Yes | Yes | Yes | 2014 | Current bankcard |
| FICO Bankcard Score 10 | Yes | Yes | Yes | 2020 | Newest bankcard |

### 1d. VantageScore Models (Range varies by version)

| Model | Experian | Equifax | TransUnion | Base Year | Score Range | Notes |
|---|:---:|:---:|:---:|:---:|:---:|---|
| VantageScore 1.0 | Yes | Yes | Yes | 2006 | 501--990 | Retired |
| VantageScore 2.0 | Yes | Yes | Yes | 2010 | 501--990 | Retired |
| VantageScore 3.0 | Yes | Yes | Yes | 2013 | 300--850 | **Most widely distributed free score** |
| VantageScore 4.0 | Yes | Yes | Yes | 2017 | 300--850 | Current -- trended data; limited adoption |

### 1e. Quick Reference: Score Ranges

| Model Family | Score Range | Key Difference |
|---|:---:|---|
| FICO General Purpose (2, 3, 4, 5, 8, 9, 10, 10T) | 300--850 | Standard range |
| FICO Auto Scores | 250--900 | Wider range; emphasizes auto-lending risk factors |
| FICO Bankcard Scores | 250--900 | Wider range; emphasizes revolving risk factors |
| VantageScore 1.0 / 2.0 | 501--990 | Retired; non-standard range |
| VantageScore 3.0 / 4.0 | 300--850 | Same range as FICO general purpose |

---

## 2. Key Feature Comparison -- General Purpose Models

This section compares the six general-purpose models that consumers are most
likely to encounter: FICO Score 8, FICO Score 9, FICO Score 10, FICO Score 10 T,
VantageScore 3.0, and VantageScore 4.0.

### 2a. Architecture and Scoring Categories

| Feature | FICO Score 8 | FICO Score 9 | FICO Score 10 | FICO Score 10 T | VantageScore 3.0 | VantageScore 4.0 |
|---|---|---|---|---|---|---|
| **Score range** | 300--850 | 300--850 | 300--850 | 300--850 | 300--850 | 300--850 |
| **Developer** | Fair Isaac | Fair Isaac | Fair Isaac | Fair Isaac | EX/EQ/TU joint venture | EX/EQ/TU joint venture |
| **Base year** | 2009 | 2014 | 2020 | 2020 | 2013 | 2017 |
| **Number of scorecards** | 12 (8 clean, 4 dirty) | 13 (includes high-util card) | Not publicly confirmed; believed similar to 8/9 with refinements | Same as Score 10 plus trended overlays | Not disclosed; uses a single model across bureaus | Not disclosed; single model, trended overlays |
| **Payment History weight** | ~35% | ~35% | ~35% (refined) | ~35% (refined) | ~40% (most influential) | ~41% |
| **Amounts Owed weight** | ~30% | ~30% | ~30% | ~30% | ~20% | ~20% |
| **Length of History weight** | ~15% | ~15% | ~15% | ~15% | ~21% | ~20% |
| **New Credit weight** | ~10% | ~10% | ~10% | ~10% | ~5% | ~5% (includes "available credit") |
| **Credit Mix weight** | ~10% | ~10% | ~10% | ~10% | ~11% | ~11% |
| **Trended data** | No | No | No | **Yes** -- uses 24-month balance trajectory | No | **Yes** -- uses 24-month trended data |

### 2b. Collections and Derogatory Treatment

| Feature | FICO Score 8 | FICO Score 9 | FICO Score 10 | FICO Score 10 T | VantageScore 3.0 | VantageScore 4.0 |
|---|---|---|---|---|---|---|
| **Paid collections** | Still penalized (balance irrelevant) | **Excluded from scoring** | **Excluded from scoring** | **Excluded from scoring** | **Excluded from scoring** | **Excluded from scoring** |
| **Medical collections** | Penalized same as other collections | **Reduced weight** | **Excluded if paid; reduced weight if unpaid** | Same as Score 10 | **Excluded if paid** | **Excluded entirely** (per National Credit Assistance Plan and VS 4.0 update) |
| **Nuisance collections (<$100)** | Excluded | Excluded | Excluded | Excluded | Excluded (<$250 in later updates) | Excluded (<$500 in later updates) |
| **Dirty scorecard threshold** | 60-day late or worse | 60-day late or worse | 60-day late or worse (believed) | 60-day late or worse (believed) | Not scorecard-based; uses continuous penalty curve | Not scorecard-based |
| **CFA (Consumer Finance Account) penalty** | Yes -- negative scoring factor | Yes -- believed present | Yes -- believed present | Yes -- believed present | Not specifically penalized as a category | Not specifically penalized as a category |
| **Loan modification treatment** | May flag as derogatory depending on furnisher reporting | May still penalize if reported as modified | Improved handling; modifications less penalized if current | Same as Score 10 | Does not penalize loan modifications if account is current | Does not penalize loan modifications if account is current |

### 2c. Authorized User and Inquiry Handling

| Feature | FICO Score 8 | FICO Score 9 | FICO Score 10 | FICO Score 10 T | VantageScore 3.0 | VantageScore 4.0 |
|---|---|---|---|---|---|---|
| **AU (Authorized User) handling** | Anti-abuse algorithm may discount AU tradelines that appear to be piggybacking | Same anti-abuse logic as Score 8 | Believed to have refined anti-abuse detection | Same as Score 10 | AU accounts are included; no known anti-abuse filter | AU accounts are included; no known anti-abuse filter |
| **AU cards on mortgage scores** | N/A (mortgage uses 2/4/5) | N/A | N/A | N/A | N/A | N/A |
| **Inquiry buffer** | 30 days (recent installment HPs ignored) | 30 days | 30 days | 30 days | Soft-pull model; HPs from last 14 days excluded | Soft-pull model; HPs from last 14 days excluded |
| **Inquiry de-duplication window** | 45 days (same type) | 45 days | 45 days | 45 days | 14 days (rolling) | 14 days (rolling) |
| **Inquiry scoring impact duration** | 12 months | 12 months | 12 months | 12 months | 12 months | 12 months (some evidence of faster decay) |
| **Inquiry report removal** | 24--26 months | 24--26 months | 24--26 months | 24--26 months | 24 months | 24 months |

### 2d. Segmentation and Scorecard Thresholds

| Feature | FICO Score 8 | FICO Score 9 | FICO Score 10 | FICO Score 10 T | VantageScore 3.0 | VantageScore 4.0 |
|---|---|---|---|---|---|---|
| **Scorecard model** | 12 discrete scorecards | 13 discrete scorecards | Discrete scorecards (number not publicly confirmed) | Same as Score 10 plus trended overlays | Single unified model; no publicly known scorecard segmentation | Single unified model |
| **Clean/Dirty threshold** | 60-day late within 7 years | 60-day late within 7 years | 60-day late within 7 years (believed) | Same | No discrete clean/dirty split | No discrete clean/dirty split |
| **Thick/Thin threshold** | 4 tradelines (confirmed for Score 9) | 4 tradelines (confirmed) | Believed ~4 tradelines | Same as Score 10 | Can score with as few as 1 tradeline (even <6 months old) | Can score with as few as 1 tradeline |
| **Mature/Young AoOA threshold** | 36 months (3 years) | 36 months (3 years) | Not publicly confirmed; believed similar | Same as Score 10 | No discrete threshold; continuous curve | No discrete threshold |
| **New Revolver segmentation threshold** | 12-month AoYRA | 12-month AoYRA | Not publicly confirmed; believed similar | Same as Score 10 | No discrete threshold | No discrete threshold |
| **AAoA max benefit** | ~90 months (7.5 years) | ~90 months (believed) | Not publicly confirmed | Same as Score 10 | Longer history is always better (no confirmed cap) | Longer history is always better |

### 2e. Utilization and Balance Metrics

| Feature | FICO Score 8 | FICO Score 9 | FICO Score 10 | FICO Score 10 T | VantageScore 3.0 | VantageScore 4.0 |
|---|---|---|---|---|---|---|
| **Aggregate revolving utilization** | Scored; thresholds at ~5%, 10%, 30%, 50%, 70%, 90%, 100% | Same threshold structure as Score 8 | Same threshold structure (believed) | Same thresholds, **but also evaluates 24-month utilization trajectory** | Scored; thresholds not publicly confirmed but ~10%, 30%, 50%, 75%, 100% believed | Same as VS 3.0 plus trajectory analysis |
| **Individual card utilization** | Scored; thresholds at ~30%, 50%, 70%, 90%, 100% | Same as Score 8 | Same (believed) | Same, plus trajectory | Scored; less granular threshold detail available | Same as VS 3.0 plus trajectory |
| **Optimal aggregate utilization** | <9.5% (some scorecards <4.5%) | <9.5% | <9.5% + declining trajectory ideal on 10T | <9.5% + declining trajectory ideal | <10% | <10% + declining trajectory ideal |
| **AWB (Accounts with Balance) sensitivity** | Moderate (less weighted than on mortgage scores) | Moderate | Moderate to High (believed) | Moderate to High (trended adds context) | Not confirmed as a discrete metric; utilization-focused | Not confirmed as discrete metric |
| **All Zero point loss** | 10--25 points if all revolvers report $0 | 10--20 points (same mechanism) | Present (believed) | Reduced impact; trended data provides context that $0 is intentional if history shows balances | Present but generally smaller (~5--15 points) | Smaller; trended data mitigates |
| **Revolving balance dollar amount** | Scored independently of utilization; <$1,000 optimal | Same as Score 8 | Same (believed) | Same, plus trajectory | Not confirmed as independent factor | Not confirmed |
| **Retail utilization** | Scored; optimal at $0 | Same | Same (believed) | Same | Not separately broken out publicly | Not separately broken out |

### 2f. Thin File and Minimum Requirements

| Feature | FICO Score 8 | FICO Score 9 | FICO Score 10 | FICO Score 10 T | VantageScore 3.0 | VantageScore 4.0 |
|---|---|---|---|---|---|---|
| **Minimum tradelines to generate a score** | 1 tradeline, open at least 6 months (or any tradeline updated in last 6 months) | Same as Score 8 | Same as Score 8 | Same as Score 8 | **1 tradeline, any age** (can score within days of first account) | **1 tradeline, any age** |
| **Deceased notation** | Cannot score if deceased notation present | Same | Same | Same | Same | Same |
| **Thin-file handling** | Thin scorecard (<4 TLs); may produce volatile scores | Same as 8; thin scorecard | Same general approach | Same as Score 10 | Designed for thin files; machine-learning model handles sparse data | Same as VS 3.0; improved thin-file predictiveness |

### 2g. Trended Data and Advanced Features

| Feature | FICO Score 8 | FICO Score 9 | FICO Score 10 | FICO Score 10 T | VantageScore 3.0 | VantageScore 4.0 |
|---|---|---|---|---|---|---|
| **Trended / time-series data** | No | No | No | **Yes** -- 24-month payment and balance history | No | **Yes** -- 24 months |
| **Distinguishes transactors from revolvers** | No (snapshot only) | No | No | **Yes** -- rewards consistent pay-in-full behavior | No | **Yes** -- rewards transactor behavior |
| **Personal loan consolidation re-spend tracking** | No | No | No | **Yes** -- penalizes consumers who consolidate debt then re-accumulate revolving balances | No | **Yes** -- can detect re-spend patterns |
| **AZEO effectiveness** | High -- snapshot model sees current $0 balances | High | High | **Moderate** -- model can see that balances were recently paid to zero (less "gaming" value) | Moderate -- less sensitive to single-month manipulation | **Moderate to Low** -- trended data sees the pattern |
| **Rent / utility / telecom data** | Not scored | Not scored | Not scored | Not scored | Not scored (unless reported as tradeline) | **Scored if reported** via FCRA-compliant furnisher (positive data only in some implementations) |

### 2h. Mortgage Score Specifics (FICO 2 / 4 / 5)

These are the legacy scores mandated by FHFA for GSE (Fannie Mae / Freddie Mac)
mortgage originations. They are being replaced -- FHFA announced a transition
to FICO Score 10 T and VantageScore 4.0, with implementation timelines subject
to change.

| Feature | FICO Score 2 (EX) | FICO Score 4 (TU) | FICO Score 5 (EQ) |
|---|---|---|---|
| **Score range** | 300--850 | 300--850 | 300--850 |
| **Base year** | 1998 | 2004 | 2004 |
| **Bureau** | Experian only | TransUnion only | Equifax only |
| **Key debt factor** | AWB (Accounts with Balance) is most heavily weighted | AWB | AWB |
| **AU cards** | Always count (no anti-abuse algorithm) | Always count | Always count |
| **Mature AoOA threshold** | 24 months (2 years) | 24 months | 24 months |
| **New account segmentation** | 18 months (any account type, not just revolvers) | 18 months | 18 months |
| **High-CL exclusion** | CLs >$31,000--$34,900 excluded from revolving utilization | CLs >=$35,000 excluded | CLs >=$35,000 excluded |
| **Inquiry de-dup window** | 14 days (EX2 specifically) | 45 days | 45 days |
| **Paid collections** | Still penalized | Still penalized | Still penalized |
| **Medical collections** | Penalized same as other collections | Penalized same | Penalized same |
| **Tri-merge usage** | Lender pulls all 3; uses middle score for single borrower, lower-middle for co-borrowers | Same | Same |

---

## 3. Optimization Strategy Differences by Model

How the same optimization strategy performs across different model families.

### 3a. Core Strategies

| Strategy | Score 8 | Score 9 | Score 10 / 10T | Mortgage (2/4/5) | Auto Scores | Bankcard Scores | VantageScore 3.0 / 4.0 |
|---|---|---|---|---|---|---|---|
| **Revolving utilization target** | <9.5% aggregate; <30% individual | <9.5% aggregate; <30% individual | <9.5% + declining trajectory rewards on 10T | <9.5%; AWB matters more than util here | Less critical than general; still helps | **Most critical** -- revolving behavior is primary risk factor | <10%; VS 4.0 rewards declining trajectory |
| **AZEO effectiveness** | **High** -- snapshot sees only current month | **High** -- same snapshot logic | Score 10: **High**; Score 10T: **Moderate** (sees 24 months of balance history) | **Highest** -- these legacy snapshot models respond most dramatically | Moderate -- auto risk factors dominate | **High** -- revolving balance behavior is key | VS 3.0: **Moderate**; VS 4.0: **Moderate to Low** (trended data) |
| **AWB target** | <20% of accounts carrying a balance | <20% | <20%; 10T may add trajectory context | **<20% is most critical here** -- AWB is the primary debt metric on mortgage scores | Less critical | Important but secondary to utilization | Not confirmed as discrete metric; keep balances low generally |
| **Inquiry cooling period** | 12 months for score recovery | 12 months | 12 months | 12 months (most impactful for mortgage qualification) | Rate-shop window (45-day de-dup) is key; individual inquiry weight is lower | 12 months | 12 months (may decay faster on VS 4.0) |
| **New account cooling period** | 12 months (revolver-specific via AoYRA segmentation) | 12 months (revolver-specific) | 12 months (believed similar) | **18 months (any account type)** -- most conservative | Less critical than general; focus on auto-specific factors | 12 months (revolver-focused) | No confirmed discrete threshold; longer is better |
| **Paid collections impact** | **Still penalized** -- paying does not help the score | **Excluded** -- paying removes the penalty | **Excluded** | **Still penalized** -- these pre-date the paid-collections fix | Varies by version (Auto 8 penalizes; Auto 9+ excludes) | Varies by version (Bankcard 8 penalizes; Bankcard 9+ excludes) | **Excluded on 3.0+** |
| **SSL/SSLT effectiveness** | Works if it is your only loan on file (drives loan util <9.5%) | Same as Score 8 | Same -- works if only loan | Same -- works if only loan | Less relevant (auto loan itself is the primary tradeline) | Not relevant (bankcard scores focus on revolving) | Less data on effectiveness; loan util is lower-weight |
| **Medical debt strategy** | Treat same as any collection; PFD or dispute | Less impactful but still scored if unpaid | Paid medical excluded; unpaid reduced weight | Treated same as any collection; no special handling | N/A for industry scores | N/A for industry scores | VS 3.0: paid medical excluded; VS 4.0: all medical collections excluded |

### 3b. Trended Data Strategies (Score 10T and VantageScore 4.0 Only)

These strategies only matter for models that use trended (time-series) data.

| Strategy | Score 10T | VantageScore 4.0 | Impact |
|---|---|---|---|
| **Pay in full every month (transactor behavior)** | Rewarded -- model sees 24 months of $0 post-statement balances | Rewarded -- similar trajectory analysis | Builds a "transactor" profile that scores higher than a "revolver" profile at the same utilization snapshot |
| **Gradually pay down debt** | Rewarded -- declining balance trajectory is positive | Rewarded | Better than stable high balances even if current snapshot looks the same |
| **Consolidate then re-spend** | **Penalized** -- model detects when revolving balances climb back after a consolidation event | **Penalized** -- similar detection | A consumer who takes a personal loan to pay off cards, then runs the cards back up, will score lower than one who keeps the cards low |
| **AZEO month-before-app manipulation** | **Less effective** -- model sees 23 months of higher balances behind the one $0 month | **Less effective** -- same issue | Still worth doing, but the benefit is smaller than on Score 8; best combined with consistently low balances |
| **Balance surfing / cycling** | Detected -- model can see high-low-high patterns | Detected | May be interpreted as revolver behavior even if snapshot util is low |

### 3c. Mortgage Preparation Timeline

Because mortgage scores (2/4/5) are the most sensitive to optimization, here is a timeline:

| Months Before Application | Action | Why |
|---|---|---|
| **18+ months** | Stop opening any new accounts (cards, loans, anything) | Mortgage scores segment on 18-month new account threshold |
| **12+ months** | Eliminate all hard inquiries (stop applying) | Allow all inquiry penalties to fully recover |
| **6+ months** | Begin gardening; verify all tradelines reporting correctly | Build payment history; allow scores to settle |
| **3 months** | Pay down all revolving balances; aim for AZEO | Let low-balance statements cycle through to all 3 bureaus |
| **1 month** | Final AZEO positioning: $5--$20 on ONE national bankcard with CL <$31,000 | Mortgage scores exclude high-CL cards from util calculation |
| **Application month** | Pull your own scores via myFICO to verify; do NOT open anything new | Lender pulls tri-merge and uses middle score |

---

## 4. Which Score Matters? Decision Tree

Different lenders and scenarios use different scoring models. This section maps
common credit activities to the model most likely used.

### 4a. By Application Type

| You Are Applying For | Most Likely Score(s) Used | Notes |
|---|---|---|
| **Conventional mortgage (Fannie/Freddie)** | EX2, TU4, EQ5 (tri-merge, middle score) | FHFA mandated. Transitioning to Score 10T and VS 4.0 (timeline TBD, originally targeted Q4 2025). |
| **FHA / VA / USDA mortgage** | EX2, TU4, EQ5 | Same as conventional for now. |
| **Jumbo / portfolio mortgage** | Varies -- may use Score 8, 9, 10, or mortgage scores | Lender discretion; not sold to GSEs so not bound by FHFA mandate. |
| **Credit card (major issuer)** | FICO Bankcard Score 8 or 9; some use general Score 8 | Varies by issuer. Some use bankcard-specific; others use general. |
| **Credit card (credit union)** | FICO Score 8 or 9 | Credit unions often use general-purpose scores. |
| **Auto loan (dealership)** | FICO Auto Score 8 or 9; some use older Auto 2/4/5 | Varies by lender. Auto-specific scores emphasize auto payment history. |
| **Auto loan (credit union / bank)** | FICO Score 8 or Auto Score 8 | Some use general-purpose; others use auto-specific. |
| **Personal loan (bank / online lender)** | FICO Score 8 or 9 | Most common. Some fintechs use proprietary models alongside FICO. |
| **Student loan (private)** | FICO Score 8 or 9 | Varies by lender. |
| **Apartment rental application** | VantageScore 3.0 (most common); sometimes FICO 8; sometimes no score (report review only) | Landlords and screening companies often use free/cheap VantageScore. |
| **Insurance (auto / home)** | FICO Insurance Score (separate model, not covered in this document) | Not the same as any lending score. Range varies. |
| **Employment screening** | No score used. Report review only. | Employers see a modified credit report with no score. Some states restrict this. |
| **Utility / cell phone** | VantageScore 3.0 or no score (report review) | Varies widely. |
| **Business credit card (personal guarantee)** | FICO Score 8 or Bankcard 8/9 | Personal credit is checked for the guarantor. |

### 4b. Free Score Monitoring -- What Are You Actually Seeing?

| Service | Score Model Provided | Bureau | Cost |
|---|---|---|---|
| **Credit Karma** | VantageScore 3.0 | TransUnion and Equifax | Free |
| **Credit Sesame** | VantageScore 3.0 | TransUnion | Free |
| **NerdWallet** | VantageScore 3.0 | TransUnion | Free |
| **Discover Scorecard** | FICO Score 8 | TransUnion | Free (even for non-customers) |
| **Experian app (free tier)** | FICO Score 8 | Experian | Free |
| **Chase Credit Journey** | VantageScore 3.0 | TransUnion | Free (Chase customers) |
| **Capital One CreditWise** | VantageScore 3.0 | TransUnion | Free (Capital One customers) |
| **Bank of America** | FICO Score 8 | TransUnion | Free (BoA customers) |
| **Wells Fargo** | FICO Score 8 | Experian (or TU for some products) | Free (WF customers) |
| **Citi** | FICO Score 8 | Equifax | Free (Citi customers) |
| **American Express** | FICO Score 8 | Experian | Free (Amex customers) |
| **US Bank** | FICO Score 8 | TransUnion | Free (USB customers) |
| **IdentityIQ** | All 28 FICO scores (all bureaus, all versions) | All 3 | ~$1 trial, then ~$30/month |

**Key takeaway:** Most free monitoring services show VantageScore 3.0, which can
differ significantly (sometimes 50--100+ points) from the FICO scores that
lenders actually use. Do not treat VantageScore 3.0 as a reliable proxy for
FICO 8, and especially not for mortgage scores. It is useful for trend-watching
and catching reporting errors, but the number itself should not be taken at
face value for lending decisions.

---

## 5. Where to Check Your Scores

### 5a. Comprehensive Score Access

| Score(s) | Source | Cost | Notes |
|---|---|---|---|
| **FICO Score 8 (all 3 bureaus)** | myFICO.com (3-Bureau plan) | ~$40/month subscription | All 3 bureau FICO 8 scores updated monthly or on-demand |
| **All 28 FICO scores** | myFICO.com (Premier plan) | ~$40/month | Includes general 8/9/10, mortgage 2/4/5, auto, and bankcard scores for all 3 bureaus |
| **All 28 FICO scores** | IdentityIQ ($1 trial) | ~$1 for 7-day trial; ~$30/month after | Same 28 scores as myFICO; popular for one-time score checks |
| **FICO Score 8 (single bureau)** | Experian.com (free tier) | Free | Experian FICO 8 only |
| **FICO Score 8 (single bureau)** | Discover Scorecard | Free | TransUnion FICO 8; available to non-customers |
| **FICO Score 8 (single bureau)** | Most bank/card apps (see table above) | Free | Bureau varies by institution |

### 5b. Specific Score Types

| Score | Where to Get It | Cost | Notes |
|---|---|---|---|
| **Mortgage scores (EX2, TU4, EQ5)** | myFICO.com, IdentityIQ | Paid subscription or trial | Essential before mortgage shopping |
| **Auto scores** | myFICO.com, IdentityIQ | Paid subscription or trial | Useful before auto loan shopping |
| **Bankcard scores** | myFICO.com, IdentityIQ | Paid subscription or trial | Useful before credit card applications |
| **FICO Score 9** | myFICO.com, IdentityIQ | Paid subscription or trial | Limited free sources |
| **FICO Score 10 / 10T** | myFICO.com (where available), some bank apps beginning to roll out | Varies | Adoption is growing but still limited for consumer access |
| **VantageScore 3.0** | Credit Karma, Credit Sesame, NerdWallet, many bank apps | Free | Widely available; NOT the same as FICO |
| **VantageScore 4.0** | Limited consumer availability; some lenders provide it | Varies | Not yet widely available through free monitoring |

### 5c. Free Credit Reports (No Score)

| Source | What You Get | Frequency |
|---|---|---|
| **AnnualCreditReport.com** | Full credit reports from all 3 bureaus; no scores | Free weekly (made permanent after COVID-era policy) |
| **Experian.com** | Experian report | Free (updated monthly) |
| **Credit Karma** | TransUnion and Equifax reports | Free (updated weekly) |

---

## 6. Glossary of Abbreviations

Terms used throughout this document and the Credit Scoring Primer.

| Abbreviation | Meaning |
|---|---|
| AAoA | Average Age of Accounts |
| AAoRA | Average Age of Revolving Accounts |
| ABORT | Average Balance on Revolving Tradelines |
| AoOA | Age of Oldest Account |
| AoORA | Age of Oldest Revolving Account |
| AoYA | Age of Youngest Account |
| AoYRA | Age of Youngest Revolving Account |
| AU | Authorized User |
| AWB | Accounts with Balance |
| AZ | All Zero (all revolvers report $0 balance) |
| AZEO | All Zero Except One |
| BC | Bankcard |
| B/L | Balance to Limit ratio |
| BK | Bankruptcy |
| BWB | Bankcards with Balance |
| CA | Collection Agency |
| CFA | Consumer Finance Account |
| CL | Credit Limit |
| CMS | Credit Monitoring Service |
| CO | Charge-off |
| CRA | Credit Reporting Agency |
| DOFD | Date of First Delinquency |
| EQ | Equifax |
| EX | Experian |
| FCRA | Fair Credit Reporting Act |
| FHFA | Federal Housing Finance Agency |
| GSE | Government-Sponsored Enterprise (Fannie Mae, Freddie Mac) |
| HP | Hard Pull (hard inquiry) |
| PFD | Pay for Delete |
| PR | Public Record |
| SP | Soft Pull (soft inquiry) |
| SSL | Share Secured Loan |
| SSLT | Share Secured Loan Trick |
| TCL | Total Credit Limit |
| TL | Tradeline |
| TPOD | Total Period of Delinquency |
| TU | TransUnion |
| VS | VantageScore |

---

*This document is part of the Credit Rebels Archive. Information is based on
publicly available FICO documentation, hobbyist data-point research compiled in
the Credit Scoring Primer, and community knowledge. FICO's algorithms are
proprietary; some details are inferred from data points rather than confirmed
by Fair Isaac. Always verify current lender practices before making financial
decisions.*
