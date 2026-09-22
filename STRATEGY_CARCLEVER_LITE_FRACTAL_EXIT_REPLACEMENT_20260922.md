# Strategy — CarClever Lite Fractal Exit Replacement

**Date:** 2026-09-22  
**Task:** #72  
**Status:** **PROPOSED — pending André’s approval; no engineering task authorized**  
**Scope:** Page 239 / CarClever Lite product and funnel design. No code, WordPress, Vercel, DNS, Fractal, connector, subscription or production changes are authorized.

## Recommendation

Replace the Fractal-dependent chat experience embedded at WordPress page 239 with a **conversion-focused CarClever Decision Center** in the existing Lite embed. Keep the page URL and embed contract stable. The first release should help visitors choose the next useful task and route them into existing GetCarWise tools or an approved, attributable Edmunds action.

Do not rebuild Lite as a two-tool chatbot in the first release. That would preserve an open-ended prompt but still depend on a model/API layer, and its vehicle-search capability substantially overlaps Find My Car. It would remove the Fractal MCP dependency only after a deliberate rewrite; a URL swap would break unsupported risk, affordability, comparison and detail flows. Build conversational search later only if measured page use justifies its ongoing cost and maintenance.

The first release should not call the Impact Catalog. Its verified data is condition-neutral, has no supported ZIP/radius behavior and is still a private, preview-only prototype. It cannot support a trustworthy local New/Used selector. Retain it as a separately gated future inventory-continuation module.

**Decision status:** recommendation only, pending André’s approval. Do not give Claude an implementation task until André approves the product direction.

## Why this is the strongest first move

The current Lite route calls Fractal and assumes six Fractal tools. Current production Find My Car exposes only find_matching_vehicle and resolve_dealer_url; changing the endpoint alone would break separate risk, affordability, comparison and detail flows.

The website already has standalone Deal Score, Price Check and VIN Check experiences that call Auto.dev directly. Recreating them inside Lite would duplicate behavior and maintenance. A decision page can instead connect each visitor’s job to the appropriate existing tool and make the revenue action explicit.

The wider strategy is a useful decision layer followed by a relevant action: Discover → answer/utility → confidence → New, Used or Trade-in action → Edmunds lead. A focused router is more consistent with that funnel than a general chat surface whose feature coverage and lead attribution are unclear.

## Option assessment

| Option | Customer value and differentiation | Functionality and monetization | Cost, risk and durability | Assessment |
|---|---|---|---|---|
| **A. Reduced two-tool Lite** | Flexible vehicle discovery remains; useful for open-ended needs. Similar search exists in Find My Car and large marketplaces. | Retains search and dealer resolution. Risk, affordability, comparison and detail flows are lost unless linked elsewhere. New/Used actions possible; Trade-in needs a distinct path. | Requires an actual prompt/flow rewrite, retains model/API cost and orchestration, and overlaps the primary product. | Not first release; reconsider if measured page use shows demand for conversational search. |
| **B. Broader first-party assistant** | A complete owned decision journey could be useful if every function is reliable and distinct. | Could combine search, risk, price, VIN, affordability and Impact actions, but overlaps four existing tools. | Highest build/maintenance effort; duplicates integrations and may increase Auto.dev calls. LLM and model dependency remain. | Reject for first release. Link to existing tools instead. |
| **C. Conversion-focused page** | Makes the next step clear and connects independent decision tools. | Routes to Find My Car, Deal Score, Price Check and VIN Check; offers separate New, Used and contextual Trade-in actions once verified. | Lowest new runtime complexity; no Fractal MCP, LLM or Catalog dependency. Main risk is link, consent and measurement readiness. | **Recommended first release.** |
| **D. Hybrid** | Conversion page first, with a conversational search module only if validated. | Clear routing now; optional search later. | A gated roadmap avoids duplicating chat capability before evidence. | Recommended roadmap: C now, measured search as optional later phase. |

## Recommended page and user journey

Keep the WordPress page 239 URL and current embedded widget URL stable. Replace the embedded chat experience with a simple decision center: “What are you trying to do?”

1. **Find a vehicle** → existing website Find My Car destination, if verified.
2. **Evaluate a vehicle I found** → Deal Score, with separate Price Check and VIN Check paths.
3. **Check a VIN** → VIN Check, with source and scope limits.
4. **Check whether the price is fair** → Price Check.
5. **Sell or trade my current vehicle** → a distinct Trade-in action.
6. **Not sure?** → short guidance and a route to the right tool, not free-form chat in release one.

Show which tool answers which question. Distinguish independent advice/tools from Edmunds inventory or lead destinations. Never imply that Edmunds Catalog cards represent all U.S. inventory or local inventory.

### New, Used and Trade-in placement

- **Used:** primary commercial action after a used-car selection/evaluation task.
- **New:** separate action only when the visitor selects New or the relevant page has New intent. Do not infer New/Used from Catalog records.
- **Trade-in:** primary for sell/valuation/replacement intent; secondary after a buying journey only when the visitor has a vehicle to replace.
- Leave existing CTA links untouched until each destination, approval and attribution parameter is audited. Do not substitute CJ links blindly or invent Impact URLs.

## First-release feature contract

### In scope

- Stable page-239 and embed URLs, after a pre-change inventory and rollback copy.
- Clear routes into existing Find My Car, Deal Score, Price Check and VIN Check experiences.
- A distinct sell/trade-in route shown in the right context.
- Concise, evidence-based tool descriptions and material data limits.
- Exact approved existing links only, with distinct event/placement identifiers where supported.
- Navigation still works when JavaScript or affiliate tracking is unavailable.
- Consent-compliant measurement for page view, path selection, tool outbound click, lead-family CTA click and confirmed Impact action/revenue where available. Do not send VINs or personal financial inputs to analytics.
- No changes to the $25k and $40k SEO treatment pages.

### Out of scope

- Fractal MCP calls or a replacement MCP URL swap.
- New free-form chat or a new risk/price/affordability engine.
- Rebuilding Deal Score, Price Check or VIN Check inside Lite.
- Impact Catalog query/display.
- New VIN intake, accounts, saved garages, lead capture or personal-data collection.
- Publisher Tag, identifyUser or Trackonomics Essentials dependency.
- Any change to the old Fractal-hosted @CarClever app, its links, app submission or subscription.

## Legacy function disposition

| Legacy Lite function | First-release disposition |
|---|---|
| Search used cars | Route to the current website Find My Car destination if verified. Otherwise leave for a later phase; do not use an MCP URL swap. |
| Deal-risk analysis | Relocate to existing Deal Score. Do not claim equivalent Lite analysis. |
| VIN / vehicle details | Relocate to VIN Check with source and scope limits. |
| Price evaluation | Relocate to Price Check. |
| Affordability | Retire from Lite release one unless an existing tool offers a clearly labeled, supportable estimate. Never label estimates as lender quotes. |
| Comparison | Retire as a separate Lite function in release one; use Find My Car for discovery. |
| Free-form automotive Q&A | Retire from Lite release one; retain relevant editorial content on the site. |
| Edmunds actions | Retain only after a current inventory confirms destination, lead family, tracking validity and attribution. |

## Impact Catalog decision

**Do not include Catalog in release one.**

The completed C1–C8 work verified model and category/price filtering, safe thin/empty results, a 20,000-item traversal window, an observed 3,000 requests/hour item endpoint allowance and structurally valid partner tracking URLs. Sampled records lacked Condition, Condition was rejected as a query field, ZIP/radius is unsupported, and the prototype is private, unmerged and not authorized for public use. It cannot label cards New/Used/CPO or claim local inventory.

A future public pilot requires separate production-pilot approval, current-main reconciliation, security and measurement review, and a host-page decision. If later approved, describe results as neutral complementary Edmunds listings, use returned tracking URLs unchanged, keep static New/Used destinations separate and make no geographic or condition claim.

## Monetization and attribution

The page is a router, not a lead-generation form. Users complete leads on Edmunds.

1. New and Used use separate approved Impact destinations aligned to selected intent.
2. Trade-in is distinct on the sell/replace path and optional after a buying decision.
3. Prefer the exact approved destination; otherwise use an approved category/model destination; show a clear fallback if unavailable.
4. Before implementation, define page/module/lead-family/placement identifiers that can be carried through allowed tracking or reporting fields. Do not assume Publisher Tag or a report dimension exists.
5. Distinguish outbound clicks from valid leads, approved actions and commission; report separately by lead family and placement where dashboards permit.
6. Identify Edmunds inventory as partner inventory; keep CarClever analysis distinct and disclose the affiliate relationship near the action.
7. Respect consent. Do not send VINs, detailed budget/credit inputs, names, emails or unnecessary identifiers to GA4, SubIDs or logs.

## Operating cost and review dependencies

- **Fractal:** the first release removes page 239’s runtime dependency after the replacement is verified. It does not authorize Fractal cancellation.
- **Anthropic API:** the proposed deterministic page has no per-message model/API usage. Actual savings require checking current Lite API usage and cost.
- **Auto.dev:** existing tool pages keep their current usage. Do not duplicate endpoint calls in the router.
- **Impact:** exact link availability and event/report support must be confirmed; do not predict revenue without a baseline.
- **Platform review:** no OpenAI/Anthropic/Meta approval is needed for an independent website router, unless a later stage changes a reviewed assistant endpoint. The page must not imply pending apps are approved.
- **Catalog:** no production dependency in release one.

## Measurement and evidence gap

There is not enough evidence to quantify revenue: the records report two completed leads with no source attribution and no verified page-239 conversion/CTA baseline. Expected impact is directional: fewer broken-tool paths, lower runtime complexity, direct routing to existing useful tools, and measurable New/Used/Trade-in actions.

Before build, complete one bounded page-239 audit:

- GA4/GSC sessions, sources, engagement and outbound clicks over available recent 28- and 90-day windows;
- current WordPress page and embedded-widget link/CTA inventory, destination and lead family;
- whether either historic completed lead can be attributed to page 239 or the old app;
- current approved Impact New/Used/Trade-in links and supported attribution dimensions;
- existing consent/event behavior across WordPress and the embedded app;
- current Lite Anthropic API use/cost and exact Fractal dependency path.

This is the smallest evidence package to freeze the feature contract and quantify a business case. If attribution is unavailable, mark it as such; do not invent a baseline.

### Success measures

- Each job reaches its intended existing tool in one clear action.
- Each outbound click has a stable, consent-compliant page/module/lead-family label where supported.
- New, Used, Trade-in clicks and confirmed actions are reported separately.
- Tool routing errors and broken destinations are zero in acceptance checks.
- Compare the first 28/90 days after release to the recorded page-239 baseline. Report outbound click rate and valid action/revenue per page session; treat small counts as directional.
- Keep $25k/$40k page text, links, canonical data, structured data and treatment unchanged. Record page-239 widget release as a separate intervention.

## Staged plan

### Stage 0 — André approval and evidence audit
Approve/reject the direction, then complete the bounded page-239 audit. No implementation.

### Stage 1 — engineering design
Claude checks current page/widget links and embed inventory, confirms target destinations, defines events/consent, and returns a minimal same-URL UI and rollback plan. No production edits.

### Stage 2 — isolated build and acceptance
If separately authorized, build on an isolated branch/preview. Remove Fractal assumptions only from page 239. Test every route, family label, consent state, screen size, keyboard path, empty/offline state and rollback. Do not alter other widgets or reviewed MCP apps.

### Stage 3 — controlled publish
After preview review, André separately authorizes publication. Preserve page 239 URL and embed URL unless separately approved. Keep $25k/$40k treatments unchanged and measure from the recorded launch date.

### Stage 4 — Fractal-exit gate
Only after all Fractal dependencies are inventoried and the live page-239 replacement is verified may André decide whether to retain a verified $0 tier, keep a time-bounded paid tier or cancel. Verify old-app links, account retention, shared Auto.dev usage/credentials and rollback independently.

### Stage 5 — optional search
Consider a two-tool first-party search experience only if page-239 usage demonstrates conversational search demand. Compare incremental completed search/actions against LLM/API, Auto.dev and maintenance costs. Requires separate scope approval.

### Stage 6 — optional Catalog pilot
Separate from release one; requires explicit production-pilot authorization and its own gates. No condition/locality claims.

## Rollback

- Preserve current page/embed URLs and deployment while replacement is in preview.
- Capture current widget deployment/config and WordPress embed/copy before authorized release.
- Use a reversible feature switch or retain the old experience as a redeployable release artifact.
- If routing, consent, analytics or approved destinations fail, restore the prior page-239 widget; do not change Fractal or other tools as rollback.
- Verify restored experience and links.
- Keep Fractal endpoint, old app and credentials intact through the rollback window.

## Independent decisions — do not bundle

1. **Page 239 replacement:** proposed decision center; pending André approval.
2. **Old Fractal-hosted @CarClever app retirement:** separate links and app-status decision; unchanged.
3. **Fractal subscription cancellation:** separate account/renewal decision, gated by dependency, safe replacement and billing/account facts; unchanged.
4. **Auto.dev Growth vs Free:** separate shared-usage/quota/cold-start/guard decision; unchanged.
5. **Impact Catalog public deployment:** separate pilot/production authorization; unchanged.

## Explicitly unchanged

- Find My Car remains the primary active app and under platform review unless André reports a new status.
- Task #70 remains live/complete; Task #71 remains a private preview prototype; Task #73 remains submitted and awaiting Meta review.
- No code, WordPress, Vercel, DNS, Fractal, app, connector, subscription or affiliate-link changes.
- Old Fractal app and its links are not retired.
- Auto.dev Growth is not downgraded; Fractal is not cancelled.
- Catalog stays unmerged, private and unpublished.
- Active $25k and $40k SEO measurement treatments stay untouched.

## Approval gate

André’s approval is required for the product direction before Claude receives an implementation task. Approval would authorize only the bounded audit/engineering-design step, not production implementation or account/platform changes.