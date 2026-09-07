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


## Independent live-page review — Sep 7, 2026

ChatGPT reviewed publicly rendered pages directly while Claude's browser work is pending.

### Findings

- The homepage is already broadly neutral: “The Only Independent AI Evaluating Cars,” with current-car-shopping CTAs and an affiliate disclosure at the bottom.
- The Tools page remains explicitly used-car-focused (“Verification Tools for Used Car Buyers,” “used car” repeated across tool descriptions). This is not automatically wrong, but it creates a homepage/Tools-page scope split that should be reviewed only after actual web-tool product scope is confirmed.
- The live Deal Score page is extremely thin in the rendered view: title, one calculator link, and global navigation/footer. It does not expose a visible contextual Edmunds CTA in the crawled output. This makes it a possible monetisation surface, but also suggests a content/SEO quality issue that should be verified in WordPress and against the intended page design.
- The live PHEV page has a clear above-the-fold Used Cars CTA before the CarClever Lite embed, with disclosure. This confirms the placement pattern used in the September handoff.
- The live 3-Row SUV page has a substantial comparison article, a Used Cars CTA after the FAQ section, and a second “Next Steps” section. Its current CTA placement is serviceable, but a sell/trade-in CTA would be more naturally tested after the ownership/budget discussion or near the final next steps—not near the opening recommendations.
- The live page-827 SUV article has the new title/meta-aligned content and a prominent SUV-specific Edmunds CTA immediately after the opening context. It should be treated as the completed control/example, not edited again without new evidence.

### Page-placement recommendation

1. First candidate: `/tools/price-check/` — inspect through WordPress/Chrome because public crawling was intermittently rate-limited. Place one Sell Your Used Car CTA after the valuation explanation/result and before the embedded tool or next steps.
2. Second candidate: `/tools/deal-score/` — first verify whether the sparse public rendering reflects genuinely thin WordPress content or an embed/rendering limitation. If genuinely thin, improve the page's explanatory content before adding a commercial CTA.
3. Existing SEO articles — do not add another CTA to PHEV or page 827. The 3-Row SUV page could receive a sell/trade-in CTA only after avoiding duplication and confirming the page's traffic/conversion role.

### Access and ownership update

- Public page inspection and strategic recommendations can be done by ChatGPT.
- Authenticated GSC and Clarity extraction still requires Claude Chrome or an André export.
- WordPress content inspection and changes require Claude/Chrome or the authorised WordPress workflow.
- No live changes were made by ChatGPT in this review.


## Additional public-site review — Sep 7, 2026

### New findings

- The public Blog index lists 9 guides and provides useful links to Price Check, Deal Score, CarClever Lite, and Try CarClever. This is a potential internal-link distribution channel for future CTA tests.
- `/cross-shopping-new-vs-used-when-new-actually-costs-less/` is a strong contextual candidate for a valuation/sell CTA because it discusses replacing a vehicle, trade-offs, residual value, and uses Edmunds/KBB as valuation references. Its current conversion path points mainly to CarClever Lite/ChatGPT and does not show a dedicated sell/trade-in CTA in the rendered content.
- `/true-cost-of-ownership-explained/` is another strong contextual candidate, especially near the “residual value” section or before the final tool CTA. Its primary current CTA is the ChatGPT affordability tool; no dedicated sell/trade-in CTA was visible in the rendered content.
- The 3-Row SUV page already has a substantial article and one Used Cars CTA. It should not receive a second commercial CTA without a specific test rationale.
- The live Deal Score page renders as a thin page with only a calculator link and global navigation in the public crawl. This is a potential SEO/conversion issue independent of the sell/trade-in experiment and needs WordPress/Chrome verification.

### Revised CTA test candidates

1. Price Check: best direct intent; requires Claude/WordPress inspection because public fetch was rate-limited.
2. Cross-Shopping New vs Used article: best editorial replacement/upgrade intent; proposed secondary test after Price Check.
3. True Cost of Ownership article: good financial-decision context; secondary candidate.
4. Deal Score: only after confirming whether the sparse rendering is real content or a crawl/embed limitation.

Do not add sell/trade-in CTAs to every article. Use one controlled page first, then expand only if the first test produces measurable eligible leads.


## Claude resolution — Sep 7, 2026

Claude completed the browser/WordPress investigation documented in `HANDOFF_BACK_SELL_TRADEIN_CTA_20260907.md`.

- Link ID **15701074** is validated as the Edmunds sell/trade-in appraisal flow and reports a distinct **$3.50 Trade-In Lead** commission tier, separate from the $10 used/new vehicle leads.
- `/tools/price-check/` and `/tools/deal-score/` are pure iframe embeds with no separate WordPress content area for a normal CTA placement. Deal Score's sparse public rendering is architectural, not a confirmed page defect.
- Recommended first test: `/true-cost-of-ownership-explained/` (WordPress post ID 513), immediately after the existing **Depreciation** subsection. It is a real long-form article with no existing Edmunds/CJ link conflict.
- Hold `/cross-shopping-new-vs-used-when-new-actually-costs-less/` (post ID 993) for a second wave because it already has a competing end-of-article CTA.

**Recommended adapted copy:**

> Wondering what your own car is worth before you factor in its depreciation? Get a free estimate from Edmunds.
> **See what your car is worth on Edmunds**

**Approval gate:** No WordPress change is authorised until André approves the page, Depreciation-section placement, and adapted copy. Once approved, Claude can implement and live-verify the CTA and disclosure.

**Measurement caveat:** CJ reporting is link-ID level. If the same link is used on multiple pages, page-level attribution is not isolated; use per-page sub-IDs or another attribution method before scaling beyond the first test.
