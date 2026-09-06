# WEBSITE SEO, AFFILIATE LINK INVENTORY AND PRIORITY LOG — 2026-09-07

**Status:** Proposed priorities; implementation pending validation and André approval where required  
**Scope:** GetCarWise website SEO, affiliate monetisation, and conversion optimisation  
**Source documents:**  
- `links(3).csv` supplied in this session; analysed directly from the attached CSV  
- `getcarwise-docs/WEEKLY_PLATFORM_REPORT_20260907.md`  
- `getcarwise-docs/HANDOFF_WEBSITE_SEO_CTA_OPPORTUNITY_PASS_20260904.md`  
- `carclever-widget/TASKS.md` items #49–#53  
- `carclever-widget/STATE.md`

## Executive finding

The website's clearest current opportunity is not a demonstrated technical-speed defect. It is the combination of:

1. Organic impressions that are not yet converting into clicks;
2. Pages ranking mostly outside page one;
3. Affiliate CTAs that have been deployed on selected pages but are not yet measured at page level; and
4. A high-value Edmunds sell/trade-in destination that has not yet been tested on a relevant existing page.

The attached CSV confirms that the strongest untested sell/trade-in destination is **Sell Your Used Car**, link ID **15701074**, with a three-month EPC of **$241.11 USD** and seven-day EPC of **$310.00 USD**.

## Affiliate link inventory relevant to the website

| Link ID | Destination | 3-month EPC | 7-day EPC | Strategic use |
|---|---|---:|---:|---|
| 15701074 | Sell Your Used Car | $241.11 | $310.00 | Highest-priority sell/trade-in experiment |
| 15701076 | Sell My Car | $152.29 | N/A | Backup/alternative sell CTA |
| 15701072 | Used Cars | $163.69 | $239.50 | Current deployed shopping CTA |
| 15701080 | Used Car Listings | N/A | $85.71 | Page-specific used-listing alternative |
| 15734470 | Evergreen Edmunds link | $30.47 | $65.94 | Generic fallback only |
| 15700865 | Car Incentives & Rebates | $42.16 | N/A | Relevant to incentives/rebates content |
| 14387442 | How Much is My Car Worth? | N/A | N/A | Valuation CTA candidate; EPC not reported |
| 17071978 | New Trade In Banner 300x250 | N/A | N/A | Banner option; no EPC reported |

**Interpretation caution:** EPC is a program/publisher performance metric, not a guaranteed payout for a particular GetCarWise page or click. The CSV confirms relative opportunity, not forecast revenue.

## Current website performance evidence

- GSC: 5.36k impressions, 60 clicks, 1.1% CTR over three months.
- Semrush: target organic keywords generally rank positions 25–57; no page-one presence among the reported examples.
- Page 827's title/meta/CTA fix shipped Sep 3; the three-month GSC aggregate is too old to judge its effect.
- Five pages from the Sep 4 SEO/CTA handoff were updated with title/meta work and/or above-the-fold Used Cars CTAs and disclosures.
- CJ: $20 from two historical leads; no confirmed sell/trade-in leads.
- Clarity: 14.71% dead-click rate over seven days, below the historical 42.86% baseline but worth monitoring.
- 404 monitor entries are scanner noise, not evidence of genuine site breakage.
- Semrush referring-domain growth from 27 to 56 was diagnosed as low-quality spam/PBN noise and should not count toward the traction gate.

## Ranked priority order

### Priority 1 — Validate the high-value sell/trade-in destination

Before publishing, verify that link ID 15701074:

- Resolves to the intended Edmunds sell/trade-in offer flow;
- Is active and permitted under current program terms;
- Produces the intended eligible lead event;
- Does not redirect to a generic editorial or shopping page; and
- Can be distinguished in CJ reporting from ordinary vehicle-shopping leads.

### Priority 2 — Run one controlled CTA experiment on Price Check

Proposed first placement: `/tools/price-check/`, because the user intent is already valuation-adjacent.

Use one CTA, one disclosure, and no new article required. Proposed copy:

> Thinking about trading in your current car? Get an Edmunds estimate before you negotiate your next purchase.  
> **See what your car is worth on Edmunds**

The CTA should be reviewed for duplication, placed in a natural post-analysis position, and tracked separately from the existing Used Cars CTA.

### Priority 3 — Complete the post-Sep-3 GSC zero-click audit

Pull a date-filtered GSC range from Sep 3 onward and identify:

- Pages with meaningful impressions and near-zero clicks;
- Queries producing those impressions;
- Current CTR and average position; and
- Pages ranking closest to page one.

Apply the established page-827 pattern only to qualifying pages: title/meta improvement plus a prominent, intent-matched affiliate CTA.

### Priority 4 — Measure existing CTA performance at page level

Create a simple record of page URL, CTA label, CJ link ID, impressions, outbound clicks, leads, EPC, date range, and disclosure status. This prevents the site from optimising on network-wide EPC alone.

### Priority 5 — Improve pages ranking positions 10–30

For the closest organic opportunities, review search-intent alignment, internal links, comparison depth, above-the-fold clarity, FAQs/schema where appropriate, and commercial CTA placement.

### Priority 6 — Investigate Clarity dead clicks

First identify the affected elements and pages. Fix only recurring, attributable issues involving CTA styling, embeds, mobile navigation, or misleading interaction affordances.

### Priority 7 — Defer broad homepage/product-positioning changes

Keep current used-only messaging until the relevant new-and-used product is approved and live. Do not make a broad positioning change based on pending app status.

## Decisions and ownership

- **Business/SEO lane:** validate link selection, select page placement, define experiment, audit GSC, and document results.
- **Claude/engineering lane:** implement WordPress changes only when the copy/link decision is approved and perform any code, deployment, or infrastructure work.
- **Decision status:** this log records a proposed priority order; it does not constitute approval to publish the new sell/trade-in CTA.
- **Existing implementation:** link ID 15701072 (“Used Cars”) remains the current deployed shopping CTA on the pages documented in the Sep 4 handoff.

## Success criteria for the first experiment

After an agreed observation period or traffic threshold, compare:

- CTA impressions;
- CTA click-through rate;
- CJ outbound clicks;
- eligible sell/trade-in leads;
- revenue/EPC; and
- performance against the existing Used Cars CTA.

Do not declare the experiment successful from EPC alone.
