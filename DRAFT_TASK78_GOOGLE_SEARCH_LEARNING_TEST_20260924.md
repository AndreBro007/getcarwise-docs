# Task #78 — Draft Google Search traffic and lead learning test

**Date:** 2026-09-24. **Status:** Reviewable, unlaunched campaign. This is the preferred acquisition direction after André's Sep 24 correction. No Google Ads account/campaign, spend, WordPress, analytics, outreach, subscription, owner-generated traffic or production change has been made. The passive no-discretionary-testing period remains through the Sep 30 checkpoint. This draft supplements `ADDENDUM_TASK78_DISTRIBUTION_REVENUE_RESET_20260924.md`, replacing partner outreach as the first distribution test.

## Exact outcome

Buy a bounded amount of US search traffic from one clear used-SUV decision intent, and observe ad click → eligible landing → useful action → tagged Edmunds outbound → pending/approved Impact action. The test can measure traffic immediately; it cannot establish profitable lead economics on day one, because Impact approval can lag and the two historical leads have unknown source.

## Campaign prepared for review, not launch

| Setting | Draft |
|---|---|
| Type | Google Search only, one campaign and one ad group. No Display, Performance Max, broad match or Search Partners expansion. |
| Audience | US presence, English; buyer comparing used SUVs around US$30,000. Confirm location/account settings before publication. |
| Existing landing | [Best SUVs Under $30,000 (2026): New vs. Used Picks](https://getcarwise.app/tools/best-compact-suv-under-30000/) (project page 827). Its Used route and existing Impact Used CTA must be rechecked; no new page is needed. The page covers both New and Used, so ad copy must accurately reflect it. |
| Initial keywords | Exact-match candidates: `[best used suv under 30000]`, `[used suv under 30000]`, `[suv under 30000 new vs used]`. Google exact match can include same-meaning variants; inspect actual search terms daily. Use Keyword Planner in the real account to confirm volume/CPC before choosing final set. |
| Exclusions | Exclude irrelevant rental, parts, jobs and wholesale intent. Check the current Impact Edmunds search terms; archived CJ agreement restricted bidding on Edmunds brand and certain car-value/trade-in phrases, plus brand names in ad copy. Do not assume the old CJ wording is the current Impact contract. |
| Ad draft | Headline options: “Compare SUVs Under $30,000”; “New vs. Used Trade-Offs”; “A Clear SUV Buying Checklist”. Description: “Compare practical choices around your budget and see what to check before contacting a dealer. Prices and availability vary.” No claims about live inventory, guaranteed prices, VIN history or platform endorsement. Final character limits, policy and landing-page match to be checked in Ads preview. |
| Proposed test size | **Up to US$150 total equivalent in the Google Ads account currency**, over **7 days**, starting no earlier than after the Sep 30 gates and a separate André launch/spend approval. Use a *campaign total budget* if available in the account: Google says new Search campaigns support it, with a minimum three-day period, and billed spend will not exceed that total. Verify actual account currency, taxes and budget screen before approval. Do not substitute a US$10 average daily budget for a US$150 hard ceiling. |
| Bid | Manual CPC or Maximize Clicks with an explicit CPC limit only if the available settings permit it; confirm in account. No conversion optimization using a low-quality click event as if it were an approved lead. |
| End | Fixed end date/account time zone; review daily for mismatched queries, spend and destination errors. Pause early for broken measurement, disallowed terms, misleading ad/landing match or low-quality traffic. |

## Measurement and economics

**Day-one operational read:** Google Ads impressions, queries, clicks, billed cost and CPC; GA4 consented paid landing sessions; existing qualified action and partner-outbound events if present; Impact source-tagged click count after reporting delay. GCLID/auto-tagging and/or UTM behavior must be confirmed on the existing page; do not put VIN/ZIP or personal data in tags. The GA4–Google Ads link is separate from the already reported GA4–Search Console link.

**Commercial read later:** Impact pending/approved/rejected Used leads and US$10 payout, reconciled to a distinct campaign/placement Sub ID only if the actual link passes it. A click, GA4 key event or outbound is not an approved lead. If source-specific Sub ID or event collection fails, fix the measurement before paying for traffic. Reporting lag makes seven-day revenue results preliminary.

**Break-even before overhead:** US$10 × approved-lead rate per *paid ad click*. At 2%, allowable CPC is US$0.20; at 5%, US$0.50; at 10%, US$1.00. These rates are illustrative, not observed. If Keyword Planner and actual CPC exceed a defensible threshold, do not launch or stop at the cap. Treat US$150 as a possible learning loss; it is not a profit forecast. The point of the test is qualified demand and funnel diagnosis, not scaling by clicks.

## Ordered gate

1. **Now, read-only:** check current Impact Edmunds SEM restrictions and account currency; obtain account Keyword Planner estimates for this exact cluster if an Ads account already exists; map the page's current outbound/GA4 implementation without generating test traffic; finalize ad text and budget screen for review. An Ads account may not exist—do not create one or add billing without approval.
2. **Sep 28:** preserve the protected GSC page/query comparison for page 827. Do not edit it mid-window.
3. **Sep 30:** complete the passive cost/usage decision. Then, with approval for a *specific* consented test, verify destination, GA4 paid session, tagged outbound and Impact reporting without accidentally starting the campaign.
4. **Launch approval:** André reviews exact account currency, Keyword Planner CPC/volume, current affiliate SEM terms, final ad/keywords/negative list, destination, source ID, total budget and end date. Only then create/enable the campaign and authorize spend.
5. **Daily and day 7:** inspect spend, search terms, landing/action/outbound counts and exceptions. Stop at the total budget or earlier; revisit approved actions after Impact maturation before deciding anything about scale.

## Source checks (Sep 24)

- Google: [Search campaign setup](https://support.google.com/google-ads/answer/9510373), [total budgets](https://support.google.com/google-ads/answer/10486938), [auto-tagging](https://support.google.com/google-ads/answer/3095550), [exact match](https://support.google.com/google-ads/answer/7478529), [Keyword Planner](https://support.google.com/google-ads/answer/7337243).
- Project: `carclever-widget/reference/edmunds_cj_program_terms_2025.md` is archived CJ terms and a restriction warning, not proof of current Impact conditions; `getcarwise-docs/STRATEGY_GETCARWISE_MARKETING_REVENUE_GROWTH_20260923.md` provides the baseline and economics.
