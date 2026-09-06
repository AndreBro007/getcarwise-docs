# HANDOFF — WEBSITE SELL/TRADE-IN CTA, GSC AUDIT AND MEASUREMENT — 2026-09-07

**From:** ChatGPT Business/Strategy lane  
**To:** Claude Engineering/Chrome lane  
**Status:** Ready for execution of browser-dependent validation and implementation; publication remains pending approval

## Context already completed

ChatGPT reviewed the weekly platform report, the September website SEO/CTA handoff, the current admin tasks, the live website pages, and the attached `links(3).csv`.

The full strategy record is:
`getcarwise-docs/LOG_WEBSITE_SEO_AFFILIATE_PRIORITY_20260907.md`

The previously completed September 4 handoff remains the record for the five pages already updated with Used Cars CTAs. Do not duplicate those CTAs.

## Confirmed affiliate inventory

| Link ID | Destination | 3-month EPC | 7-day EPC |
|---|---|---:|---:|
| 15701074 | Sell Your Used Car | $241.11 | $310.00 |
| 15701076 | Sell My Car | $152.29 | N/A |
| 15701072 | Used Cars | $163.69 | $239.50 |
| 15701080 | Used Car Listings | N/A | $85.71 |
| 15734470 | Evergreen Edmunds link | $30.47 | $65.94 |
| 14387442 | How Much is My Car Worth? | N/A | N/A |
| 17071978 | New Trade In Banner 300x250 | N/A | N/A |

EPC is directional network/publisher data, not a guaranteed page-level forecast.

## Claude actions requested

### A. Validate link 15701074

Using the browser/CJ or other authorised live method:

1. Confirm the link is active.
2. Confirm it opens the intended sell/trade-in or valuation flow.
3. Confirm the intended eligible lead event and current program terms.
4. Confirm it is suitable for a contextual website CTA.
5. Record the final URL/redirect behaviour without exposing credentials.

If 15701074 is unsuitable, evaluate 15701076 as the backup. Do not substitute a generic Used Cars link for this experiment without recording why.

### B. Inspect candidate pages and recommend exact placement

First candidate: `/tools/price-check/`.  
Second candidate: `/tools/deal-score/`.

Inspect the complete rendered pages and WordPress content for:

- Existing Edmunds/CJ links;
- Duplicate or buried CTAs;
- The main analysis/result boundary;
- The CarClever Lite embed;
- The best natural point for one commercial CTA;
- Mobile presentation and disclosure visibility.

Preferred placement is after the core valuation/evaluation explanation or result, before the embedded tool or next-steps section.

### C. Do not publish until approval

Proposed copy:

> Thinking about trading in your current car? Get an Edmunds estimate before you negotiate your next purchase.  
> **See what your car is worth on Edmunds**

Use one CTA and a nearby affiliate disclosure. Do not add a banner or multiple links in the first test. Report the recommended page, exact placement, final copy, link ID, and destination before implementation if approval is still required.

### D. Run the GSC zero-click audit

ChatGPT cannot access the authenticated GSC account directly in this session. Use Claude Chrome or obtain an export from André.

Pull a date-filtered range beginning **Sep 3, 2026**, not only the rolling three-month view. Return:

- Page;
- query;
- impressions;
- clicks;
- CTR;
- average position.

Identify pages with meaningful impressions, near-zero clicks, commercial intent, and rankings closest to page one. The five pages in the Sep 4 handoff have already been handled and should be treated as post-fix monitoring candidates, not automatically reworked.

### E. Return a page-level CTA measurement baseline

For existing and proposed CTAs, record:

- Page URL;
- CTA label;
- CJ link ID;
- date live;
- page impressions;
- CTA/outbound clicks;
- CJ clicks if available;
- eligible leads;
- revenue/EPC;
- disclosure verified.

### F. Check Clarity dead clicks

Use Clarity to identify the actual pages/elements behind the current 14.71% seven-day dead-click rate. Do not recommend a broad redesign unless dead clicks cluster around a repeatable component. Check CTA buttons, embeds, mobile navigation, and text styled as clickable.

### G. Product messaging

Do not broadly rewrite homepage or web-tool positioning yet. Confirm actual new-vehicle support and app approval status first. Record any live mismatch between homepage-neutral messaging and used-car-specific Tools-page copy for a later decision.

## Return package

Please return:

1. Link validation result for 15701074;
2. Recommended first CTA page and exact placement;
3. GSC zero-click page/query list;
4. CTA measurement baseline;
5. Clarity dead-click findings;
6. Any WordPress changes made, with live re-fetch verification;
7. Any remaining approval or engineering blockers.

## Boundary

This handoff authorises research, browser inspection, and preparation. It does not authorise production application changes, Vercel changes, MCP changes, Find My Car merges, or publication of the new CTA without the required approval.
