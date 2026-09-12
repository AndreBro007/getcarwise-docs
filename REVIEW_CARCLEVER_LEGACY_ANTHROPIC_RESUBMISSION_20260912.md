# Legacy CarClever Anthropic Resubmission Review — 2026-09-12

**Status:** PROPOSED / PREPARE-ONLY — no new Anthropic submission authorized or made by this document.  
**Decision owner:** André.  
**Scope:** Legacy Fractal `CarClever` used-car product, not `CarClever - Find My Car` V2 and not `CarClever - New & Used Cars`.

## Why this review exists

André is considering submitting the legacy used-car `CarClever` Fractal MCP to Anthropic again using the current submission flow, shortly after the Sep 12 `CarClever - Find My Car` V2 Anthropic update returned to **IN REVIEW**.

This document reconstructs the prior legacy-CarClever Anthropic submission from Google Drive records, compares it with the current portfolio, and sets a safe go/no-go path. It does **not** treat historical form answers or capability claims as current until re-verified against the live legacy MCP.

## Historical Anthropic submission record recovered from Google Drive

Primary source documents recovered:

- `020_ANTHROPIC_MCP_SUBMISSION_JUNE21_2026.md`
- `020_ANTHROPIC_MCP_CONNECTOR_SUBMISSION.md`
- `020_ANTHROPIC_MCP_SUBMISSION_STEPBYSTEP_20260825.md` (later Find My Car form guide, useful for form structure/process rather than legacy-CarClever content)

### Legacy CarClever identity used in the June 21 submission

- MCP server name: `CarClever`
- Product focus: used-car search plus evaluation/risk/cost workflow
- Hosting: Fractal production
- Historical MCP URL: `https://f5025062-4d61-4160-95a7-1cc05857c622.usefractal.app/mcp`
- Company / brand: GetCarWise
- Support: `info@getcarwise.app`
- Website: `https://getcarwise.app/`

**Important:** the URL above is historical submission evidence, not a current-live verification in this review. Re-test the endpoint and current tool discovery before any resubmission.

### Historical tagline

> Find used cars, analyze risk, true cost, buy smarter

### Historical public description

The June 21 submission positioned legacy CarClever as a complete used-car buying workflow rather than a listing-only search product. It emphasized live inventory, Deal Scores, risk analysis, repair/recall/title/odometer signals, affordability / ownership-cost calculations, side-by-side comparison, and transparent analysis.

Do not reuse that copy unchanged until each substantive capability claim has been re-verified on the current live MCP.

### Historical use cases

1. Search, Score and Rank Deals.
2. Pre-Purchase Risk Analysis.
3. True Cost of Ownership / affordability.
4. Side-by-Side Comparison.

The historical example prompts included a budget/risk-oriented SUV search, an affordability calculation, a deal-risk analysis, and multi-vehicle comparison.

### Historical tool inventory

The June 21 record listed nine tools:

1. `search-used-cars`
2. `analyze-deal-risk`
3. `calculate-affordability`
4. `vehicle-comparison`
5. `garage-save`
6. `garage-list`
7. `garage-remove`
8. `get-vehicle-details`
9. `resolve-dealer-url`

Historical records said user-friendly titles/annotations were set and that the server had been tested in Claude.ai / Claude Code. Those are historical assertions only; the current server must be rescanned and exercised again.

### Historical support / compliance material

The prior submission referenced:

- documentation on GetCarWise;
- GetCarWise Privacy Policy;
- GetCarWise Terms of Service;
- `info@getcarwise.app` support;
- public/no-auth connectivity;
- production readiness and live U.S. inventory;
- screenshots for search/results, affordability/TCO, and risk analysis;
- policy, technical, documentation and testing checklists.

The prior submission history recorded:

- Apr 29, 2026 — initial submission; outcome unclear in the surviving record;
- May 19, 2026 — resubmission with V1.3 enhancements / updated MCP URL, awaiting review;
- Jun 21, 2026 — moat-focused copy and refreshed screenshots prepared for resubmission.

## Later Anthropic form/process reference

The Aug 25 Find My Car guide documented an Anthropic web-form flow with sections covering introduction, connection, tools, listing, use cases, company, authentication, data handling, test/launch, compliance, and review.

The current Sep 12 Anthropic portal also demonstrably supports server editing plus Sync/Rescan tools for the existing Find My Car listing. Therefore, for a new legacy-CarClever listing, use the **current live form as authoritative** and treat the historical section labels as a preparation checklist only.

## Current portfolio context — Sep 12

Current canonical status places `CarClever - Find My Car` V2 at the center of the product strategy:

- OpenAI: V2 submitted, REVIEW.
- Anthropic: existing Find My Car listing updated to exact tested V2, IN REVIEW.
- Legacy `CarClever` Fractal app: historical/fallback surface.
- `CarClever - New & Used Cars`: separate historical Fractal surface.
- V3 remains paused.

No new Fractal submission action had been authorized before this review.

## Strategic assessment of submitting legacy CarClever as a second Anthropic app

### Potential upside

A second Anthropic listing can be defensible **if it is clearly a different job-to-be-done** from Find My Car:

- **Find My Car:** streamlined live new/used inventory discovery and matching, with Buyer Check support.
- **Legacy CarClever:** specialist **used-car evaluation / risk / affordability / comparison** workflow.

That differentiation could make the portfolio broader without merely cloning the same search experience. The legacy product's richer risk/cost/comparison capabilities are the strongest reason to keep it distinct.

### Main risks

1. **Reviewer and user confusion.** Two GetCarWise automotive connectors with similar `CarClever` branding and overlapping inventory search could look duplicative unless the listing name, tagline, description and use cases make the distinction immediate.
2. **Portfolio-focus risk.** Current strategy deliberately centers Find My Car V2 and labels the Fractal products historical/fallback. A new submission changes that strategy and should be explicit rather than accidental.
3. **Broader tool surface = more review surface.** Nine historical tools are materially more complex than Find My Car's two-tool V2 surface. Every tool description, annotation, authentication/data claim and capability statement should be current and defensible.
4. **Historical claims may be stale.** Do not reuse claims about title brands, repair reserves, ownership cost, comparison, garage behavior or "all tools functional" until reproduced on the live server now.
5. **Timing.** Find My Car V2 was just resubmitted/updated to Anthropic on Sep 12 and is in review. There is no documented Anthropic rule found here prohibiting another related submission, but introducing another overlapping CarClever listing immediately could add avoidable reviewer context/confusion.

## Recommendation

**PREPARE NOW; DO NOT CLICK SUBMIT YET.**

The idea is worth pursuing, but only as a deliberately differentiated specialist product and only after a short live submission-readiness audit. The safest timing is to prepare the complete current-form package now, then make an explicit go/no-go decision once:

- the legacy Fractal MCP has passed fresh tool discovery and smoke tests; and
- we have decided whether to wait for the newly updated Find My Car Anthropic review to settle or intentionally run the two reviews in parallel.

This is a strategic recommendation, not an Anthropic policy prohibition.

## Required pre-submit audit

Before any new legacy-CarClever Anthropic submission:

1. Verify the exact current legacy MCP URL and HTTPS reachability.
2. Rescan/discover the current tool list; compare it to the historical nine-tool list.
3. Capture the exact current tool names, descriptions, annotations and input schemas.
4. Run at minimum:
   - one normal used-car inventory search;
   - one VIN/deal-risk analysis;
   - one affordability/TCO flow;
   - one vehicle-comparison flow;
   - garage save/list/remove if those tools are still exposed.
5. Verify every user-facing link and affiliate disclosure.
6. Verify current documentation, privacy, terms and support URLs.
7. Re-check data handling/authentication answers against the actual live architecture.
8. Create fresh screenshots from the current UI; do not automatically reuse June assets.
9. Rewrite the listing around the distinct value proposition: **used-car evaluation, risk and ownership-cost decision support**, not generic car finding.
10. Review the current Anthropic form field-by-field and only reuse historical answers that remain true.

## Proposed positioning if the audit passes

**Working listing name:** `CarClever — Used Car Buyer` or similarly differentiated wording. Final name requires André approval and should be checked against the current form/directory conventions.

**Working tagline direction:** `Evaluate used-car risk, cost and value before you buy.`

**Positioning rule:** inventory search is an entry point, not the lead message. Lead with used-car due diligence, risk, affordability / true cost and comparison so it is clearly complementary to `CarClever - Find My Car`.

## Decision gate

**Pending André confirmation:**

- A. Prepare only, wait for Find My Car Anthropic review before submitting legacy CarClever; or
- B. Prepare and submit in parallel once the legacy live-readiness audit passes.

Until André chooses A or B, this remains a proposal and no current portfolio/admin status should say that legacy CarClever has been resubmitted.

## Related current records

- `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`
- `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md`
- `AUDIT_V2_ANTHROPIC_SUBMISSION_COMPLIANCE_20260910.md`
- `carclever-widget/ADMIN_RECORD_ANTHROPIC_SUBMISSIONS.md`
- `carclever-widget/CARCLEVER_3_APPS_CURRENT_STATUS_20260912.md`
