# B1 — SEO Title/Meta and Edmunds CTA Drafts — 2026-09-02

## Status

Approved by André on Sep 2, 2026. Claude may proceed with the page preflight and WordPress implementation, subject to the checks and safeguards below.

## Target page 1 — Best SUVs under $30,000

**Suggested SEO title:** Best SUVs Under $30,000: Top Picks for Your Budget

**Suggested meta description:** Shopping for an SUV under $30,000? Compare practical new and used options, key trade-offs, ownership considerations, and where to continue your search.

**Suggested Edmunds CTA:** Browse SUVs on Edmunds

**CTA context:** Place after the page’s recommendations and buying criteria. The CTA should take the reader to the approved Edmunds SUV destination from the current CJ inventory.

**Affiliate rationale:** This is a natural next step for a user who has finished the editorial shortlist and wants to browse current inventory or research specific SUVs.

## Target page 2 — SUVs under $30,000

**Suggested SEO title:** SUVs Under $30,000: Compare New and Used Options

**Suggested meta description:** Find SUVs under $30,000 by comparing new and used choices, pricing, mileage, features, and the compromises that matter before you buy.

**Suggested Edmunds CTA:** Compare SUVs and listings on Edmunds

**CTA context:** Use once after the comparison section, not repeatedly throughout the page.

## Target page 3 — Best SUV under $30,000

**Suggested SEO title:** Best SUV Under $30,000: What to Buy and What to Check

**Suggested meta description:** See which SUVs offer the best value under $30,000, including practical checks for price, mileage, reliability, features, and ownership costs.

**Suggested Edmunds CTA:** Research SUVs and current listings on Edmunds

**CTA context:** Link after the “what to check” section so Edmunds is positioned as the next research action.

## Target page 4 — Best SUVs under $30,000

**Suggested SEO title:** Best SUVs Under $30,000: Value Picks Compared

**Suggested meta description:** Compare the best SUV choices under $30,000 with a practical look at value, space, fuel economy, condition, mileage, and buying risk.

**Suggested Edmunds CTA:** See SUV research and listings on Edmunds

**CTA context:** Use a single contextual CTA near the end of the page.

## Target page 5 — Best Compact SUV Under $25,000

**Known URL:** /tools/best-compact-suv-under-25000/

**Suggested SEO title:** Best Compact SUVs Under $25,000: Smart Used-Car Picks

**Suggested meta description:** Looking for a compact SUV under $25,000? Compare practical used-car choices by price, mileage, reliability, features, and everyday value.

**Suggested Edmunds CTA:** Browse used SUVs on Edmunds

**CTA context:** This page should favour the used-car destination unless the page is specifically updated to include new inventory.

## Recommended Edmunds CTA map

| Page intent | Preferred destination | Why |
|---|---|---|
| Used SUV shopping | Used Cars / Used Car Listings | Closest match to the user’s purchase intent |
| New SUV shopping | New Cars / New Car Listings | Keeps the destination aligned with inventory type |
| SUV research | SUVs at Edmunds | Useful when the user is still comparing models |
| New-car affordability | Car Incentives & Rebates / New Car Quotes | Matches a user moving from research to purchase |
| Valuation or sell intent | How Much is My Car Worth? / Sell Your Used Car | Separate funnel from buyer traffic |
| Trade-in intent | Sell My Car / trade-in destination | Use only where the page explicitly discusses selling or trading |

Use the exact active CJ tracking URL from the supplied inventory. Do not copy a raw Edmunds URL into a monetized CTA if the CJ link is the approved tracking mechanism.

## Affiliate disclosure draft

“Some links on this page are affiliate links. If you use one, GetCarWise may receive compensation at no additional cost to you. Our recommendations remain independent.”

Place the disclosure near the first commercial CTA and keep it visible enough to be understood before the click.

## Site-wide audit pattern

After these pages are updated, audit pages with:

- meaningful Google impressions;
- low or zero click-through rate;
- rankings high enough that the result is visible;
- titles that do not clearly match the query;
- meta descriptions that do not communicate a useful reason to click.

Prioritise pages where the query expresses a budget, vehicle type, location, valuation, selling, or buying action. These are more likely to produce both organic clicks and measurable Edmunds downstream activity.

## Measurement requirements

For every Edmunds CTA, record:

- source page;
- page intent;
- destination type;
- CJ link ID;
- clicks;
- valid leads;
- rejected/invalid leads where available;
- revenue;
- date range.

Recommended naming convention for internal analytics:

- edm_used_suv_page
- edm_new_suv_page
- edm_suv_research
- edm_incentives
- edm_sell_vehicle
- edm_trade_in

Do not claim that these labels are passed to CJ unless the tracking implementation supports it. They are first-party reporting labels unless confirmed otherwise.

## Claude/WordPress handoff checklist

1. Confirm the exact WordPress URL and current title for each target page.
2. Confirm whether each page covers new cars, used cars, or both.
3. Apply the approved title and meta description.
4. Add one relevant Edmunds CTA using the supplied CJ tracking URL.
5. Add the affiliate disclosure.
6. Verify the CTA opens the intended Edmunds destination.
7. Verify mobile layout and link behaviour.
8. Confirm no withdrawn New & Used Cars app link or premature Find My Car claim is introduced.
9. Record the page, CTA, CJ link ID, and date in the measurement log.
10. Re-check Search Console after the next meaningful reporting period.

## Approval gate

André should now review:

- the five title/meta pairs;
- the Edmunds destination chosen for each page;
- whether the pages should say “new and used” or “used”;
- the disclosure wording.

After André approves, this document is ready to hand to Claude for WordPress implementation. No application-code work is required for this task.
