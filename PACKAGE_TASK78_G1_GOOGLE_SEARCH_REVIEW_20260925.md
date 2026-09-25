# Task #78 — G1 Google Search launch package for review
**Prepared 25 September 2026. Status:** copy/settings draft only; no Ads account, campaign, billing, keyword upload, page change, affiliate click, owner-generated traffic or spend. This packages the already selected Google → existing used-only page 934 route while Claude checks simple reports. It does not launch it.

## 1. Objective and buyer

One US Search experiment for a person asking which **used compact SUV under US$25,000** to consider. The ad promises a useful comparison/checklist on GetCarWise, not a live listing search or an Edmunds-sponsored experience. The landing page is [Best Compact SUVs Under $25,000: Used Picks Compared](https://getcarwise.app/tools/best-compact-suv-under-25000/) (project page 934). Existing labelled Impact Used link remains unchanged. This route tests buyer demand for the page; it does not test old @CarClever invocation or establish ad-specific approved lead ROI.

## 2. Campaign configuration to review, not enter yet

| Setting | Proposed value | Validation before activation |
|---|---|---|
| Type | One Search campaign, one ad group, one responsive Search ad | Search only; Display, Search Partners, broad match, Performance Max and automatically applied expansions off if settings permit. |
| Geography/language | United States, English; presence targeting | Confirm Ads account setting and actual geographic report; do not include Australians searching about US cars. |
| Landing URL | `https://getcarwise.app/tools/best-compact-suv-under-25000/?utm_source=google&utm_medium=cpc&utm_campaign=used_suv_decision_g1` | Claude checks existing GA4 report and URL pattern read-only; after quiet period verify final rendered destination as part of separately approved setup. No Impact redirect as final URL. |
| Keyword selection | Start with 2–3 exact-match candidates below | Check Keyword Planner demand and CPC in the real account, close-variant search terms and current Edmunds SEM restrictions. Do not create an account early merely to check credits. |
| Bidding | A bounded click-learning setup with a CPC control if the available account settings allow | Do not optimize to a page view or partner click as if it were an approved lead. Record setting visible in review screen. |
| Dates/cash | Proposed **US$150 total equivalent** over seven days, after Sep 30 and separate approval | Verify account currency, taxes, genuine campaign total-budget option and fixed start/end dates/account time zone. If a hard total cap is unavailable, present an alternative with actual maximum risk before approval; do not substitute a daily average and call it a hard cap. |
| Credit | Do not include any assumed Google promotional credit in the cap | Show the actual account-specific eligibility, qualifying cash spend and timing only if available without premature account creation. |
| Landing/affiliate | Existing page 934 and its already verified Impact Used asset 3949600 | Keep published page and tracking link unchanged for this first directional test. Direct PPC→Edmunds prohibited under supplied agreement. |

**Keyword candidates:** `[best used suv under 25000]`, `[used compact suv under 25000]`, `[compare used suvs under 25000]`. Choose a narrow subset once actual volume/CPC is visible. Exact match can include close intent variants; inspect search terms, not just the entered words.

**Exclusions:** Apply the Edmunds agreement's exact and phrase negative list for specified valuation/trade-in terms, plus protected Edmunds/trademark terms. Do not use Edmunds, automaker or competitor names in ad copy. Also exclude clearly irrelevant `rental`, `parts`, `jobs`, `wholesale`, `repair`, `lease` and `free car` intent where the account's matching behavior supports it. The precise agreement schedule must be transcribed and checked against the selected keywords/negative match types before activation; this draft is **not** a complete contractual negative list. Review the search-terms report daily and add only evidenced irrelevant terms.

## 3. Proposed responsive Search ad

All headlines below are at most 30 characters; descriptions at most 90 characters. No Edmunds, manufacturer or competing brand appears. Do not pin without a demonstrated reason.

| Headlines | Characters |
|---|---:|
| Used SUVs Under $25,000 | 23 |
| Compare Used SUV Choices | 24 |
| See the Trade-Offs | 18 |
| Used SUV Buying Guide | 21 |
| Start With a Shortlist | 22 |
| Check Before Dealer Contact | 27 |
| GetCarWise Used SUV Guide | 25 |
| Compare Cost and Risk | 21 |

| Descriptions | Characters |
|---|---:|
| Compare used SUVs under $25,000. Review price, mileage and trade-offs before contact. | 85 |
| A practical used SUV comparison and checklist to help you narrow your choices. | 78 |

**Editorial check:** If page 934 does not actually discuss a specific promise (for example “risk”), drop that headline rather than changing the page during the protected GSC window. Do not assert verified vehicle histories, live inventory, guaranteed pricing, financing or official platform/Edmunds endorsement. Final combinations, character handling and policy/landing match must be reviewed in the actual Ads preview before launch.

## 4. Simple measurement and decision rule

- **During an approved seven-day run:** Google Ads spend, actual queries, clicks and CPC; GA4 page-934 sessions and engaged sessions from `google / cpc`. Read Impact Used pending/approved/reversed actions separately as background, not as ad conversions.
- **Directional question:** Did relevant US used-SUV searches deliver engaged buyers to this page at a cost and volume that justify a second, better-attributed or app-focused test? Do not manufacture a target conversion rate from two historic CJ leads. If, illustratively, CPC is US$2–5, a US$150 cap buys only about 30–75 clicks before any nonlanding or nonengagement; this is a learning sample, not a profitability estimate.
- **Stop:** hard spend cap/end date; prohibited/irrelevant queries, misleading ad/page fit, broken destination, GA4 paid landing absent after normal reporting delay, or abnormal spend. Check daily. If few clicks occur because demand is too narrow, record that result rather than broadening silently.
- **After:** review Search terms, cost per engaged landing, page behavior visible in GA4 and Impact actions separately. Only source-specific accepted actions support an ad CPA/ROAS claim. A later Impact Sub ID/event project needs a concrete reason and separate approval.

## 5. Dependencies and explicit approval screen

1. Sep 28 GSC cohort review for page 934.
2. Sep 30 actual hours/cash/Fractal/app viability gate and Claude's GA4/Impact report setup.
3. Exact Edmunds SEM/negative schedule, page copy and asset permission, account Keyword Planner CPC/volume, account-specific credit, Google location/budget/settings preview.
4. André approves the **exact** ad, keywords/negative list, final URL, geography, dates, account/currency and maximum cash loss. Only then set up/enable paid campaign.

**No parallel Google→app or Reddit ad is included in this cap.** They are separate experiments with different success measures and approvals. This package is based on the [execution plan](PLAN_TASK78_MULTIROUTE_MARKETING_EXECUTION_20260924.md), [Google draft](DRAFT_TASK78_GOOGLE_SEARCH_LEARNING_TEST_20260924.md), [Impact terms brief](BRIEF_TASK78_EDMUNDS_IMPACT_PAID_SEARCH_ROUTES_20260924.md), and [minimal measurement handoff](HANDOFF_CLAUDE_TASK78_MINIMAL_MEASUREMENT_SETUP_20260925.md).
