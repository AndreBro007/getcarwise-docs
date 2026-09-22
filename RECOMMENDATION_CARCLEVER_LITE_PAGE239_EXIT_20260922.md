# Recommendation — CarClever Lite Fractal Exit (Page 239)

**Date:** 2026-09-22  
**Task:** #72  
**Status:** Business/strategy recommendation prepared; no implementation approved  
**Decision sought:** Approve or reject the recommended replacement product before any Claude engineering task is issued.

## Recommendation

Replace the Fractal-backed CarClever Lite chat embedded on WordPress page 239 with a **first-party, content-led decision and conversion page**, using the newly published CarClever Decision Center (page 1160) as the tested starting point.

Keep page 239 live and unchanged while page 1160 is observed. If the Decision Center proves to be the clearer route and its content is ready to become the canonical page, consolidate the final content onto page 239 (preserving its existing URL) and retire or redirect page 1160 in a separate SEO-reviewed change. Do not leave two near-duplicate indexable pages. Do not remove the page-239 embed or redirect either page until André separately approves that implementation.

Do **not** preserve a general-purpose chat merely to preserve the old interface, and do not swap the Fractal MCP URL under the existing prompt. The value of the replacement is a reliable route to existing specialist tools and monetized actions, not another layer that repeats those tools.

## Why this is the best fit

The existing Lite /api/chat route assumes six Fractal tools: used-car search, deal risk, affordability, comparison, vehicle details and dealer URL resolution. Production Find My Car currently exposes only find_matching_vehicle and resolve_dealer_url. A URL-only swap would break Lite's unsupported flows.

The website already has separate Deal Score, Price Check and VIN Check pages. The Decision Center links visitors to those tools, Find My Car, and distinct Edmunds New, Used and Trade-in destinations. Its three affiliate CTAs have been verified live and carry distinct Impact Sub IDs. This produces a clear tool-to-lead path without duplicating calculations, adding an AI layer, or increasing Auto.dev calls.

The runway plan reports only two historical completed leads, with no attribution to Fractal or another channel, and identifies Auto.dev as a shared dependency. This supports reducing unnecessary Fractal-specific complexity; it does not establish that Fractal generated those leads or that any particular replacement will earn more.

## Options

| Option | Benefit | Main cost or loss | Assessment |
|---|---|---|---|
| A. Rewrite Lite as a two-tool chat | Retains conversational vehicle discovery and can use the current Find My Car contract | Removes integrated risk, affordability, comparison and detail flows; still needs a maintained chat/API path and model-provider usage | Viable fallback only if visitors clearly value chat/search on page 239 |
| B. Build a broader first-party conversational replacement | Could preserve selected capabilities in one interface | Rebuilds or duplicates existing tools; raises API, Auto.dev quota, consent, support and maintenance burden | Not justified for first release |
| C. Replace the Lite chat with a decision/funnel experience | Uses the already-built Decision Center and existing tools; simplest Fractal exit and clearest New/Used/Trade-in funnel | Gives up open-ended chat; page 1160 needs observation and final SEO consolidation planning | **Recommended** |
| D. Hybrid page plus two-tool chat | Offers guidance and interactive search | Combines the maintenance of A and content upkeep of C before evidence shows the chat is needed | Defer unless the pilot shows demand for both |

## Page 239 replacement contract

The replacement should:

1. Explain the visitor's next step in plain language.
2. Route vehicle discovery to Find My Car when available; retain useful alternatives if its platform review changes availability.
3. Route a specific listing to Deal Score, Price Check or VIN Check according to the visitor's question.
4. Offer New and Used Edmunds actions as separate choices after useful guidance.
5. Show Trade-in as a lower, contextual action for someone replacing a current vehicle.
6. Preserve clear affiliate disclosure, the validated Impact destinations and sponsored/nofollow attributes.
7. Avoid making an unsupported “best car,” market coverage, valuation or lead-acceptance promise.
8. Remain useful if any one tool is unavailable: provide static links and a graceful explanation.

The Impact Catalog prototype does not belong in this first release. Its prototype remains private; condition-neutral inventory and unsupported ZIP/radius filtering make it unnecessary and potentially misleading for this page.

## Funnel and measurement

Measure the sequence: Decision Center visit → tool-path click or search continuation → New/Used/Trade-in outbound click → Impact action → valid lead → commission. The primary business outcome is attributable valid leads and revenue per qualified visit, not Rank Math score or raw clicks.

Page 1160 has distinct Impact Sub IDs for New, Used and Trade-in. Its earlier verification found no GA4 outbound-click event in MonsterInsights Lite. Use the Impact click/action reports for affiliate outcomes; report GA4 pageviews only where consent and collection permit. Do not claim a conversion or revenue lift without attributable actions.

Observe page 1160 at the 14-day directional and 28-day primary checkpoints. The last user-provided Rank Math screenshot showed **Index checked** and **No Index unchecked**, but the current live robots directive and sitemap inclusion have not been independently re-verified after the user's edits. Confirm those before interpreting organic exposure. No Search Console impressions are guaranteed; without sufficient impressions, the test cannot establish organic demand.

Before replacing page 239, compare its current 28/90-day Search Console and available analytics data with page 1160; check query overlap and internal links. Keep active $25k/$40k and other treatment pages unchanged.

## Costs, approvals and maintenance

- **Fractal:** A static first-party replacement removes page 239's live Fractal call only after that embed/route is actually retired. Subscription cancellation remains a separate decision after every Fractal consumer is inventoried and removed or intentionally retained.
- **Anthropic/OpenAI/Meta:** No conversational model is required for the recommended first release, so the replacement does not depend on new model approval. Existing tool/platform availability should be stated accurately.
- **Auto.dev:** The static funnel adds no Auto.dev calls. Auto.dev Free/Growth remains a separate decision because the key is shared with other consumers.
- **Catalog:** No public Catalog call or deployment.
- **Maintenance:** Low; review destination links, disclosure and tool availability periodically. Avoid new code unless an essential interaction requirement emerges and is approved.

## Staged plan

1. **Now — observe page 1160.** Keep page 239 untouched. Confirm its current robots directive, sitemap status, live snippet, and Impact Sub ID reporting. Review at day 14 and day 28. No paid or external traffic acquisition is assumed.
2. **Decision gate — verify intent and page overlap.** Review page 239 and 1160 query/page data, existing protected treatments, visitor paths and whether the current Decision Center provides enough distinct utility.
3. **If approved — prepare one reversible page-239 replacement.** Capture a restorable copy of the current page content/embed and widget/backend references. Use the Decision Center contract above, preserve page 239's URL, and keep page 1160 from becoming a competing duplicate (appropriate consolidation/redirect decision must be approved).
4. **Verify before closing Fractal.** Confirm page 239 no longer requests the Fractal-backed endpoint, tool links still work, New/Used/Trade-in links retain their exact tracking and attributes, mobile/accessibility behavior is acceptable, and rollback is practical.
5. **Only then consider Fractal account cancellation.** Re-inventory all Fractal-hosted apps and references, including old @CarClever distribution. Treat its retirement and subscription cancellation as separate approvals. Rotate/remove shared credentials only after actual dependencies are understood.

## Rollback

Before any future page-239 edit, save the exact existing page content, embed URL, relevant widget version and date. If the new route fails or causes a material SEO/user-path problem, restore the original page-239 content/embed while the Fractal service is still available. Do not cancel Fractal as part of that page edit; cancellation needs its own dependency and reversibility check.

## Explicitly unchanged

- Page 239 and its Fractal-backed Lite experience remain unchanged pending separate approval.
- Page 1160 remains a separate live pilot; this recommendation does not authorize further WordPress/Rank Math changes.
- Old Fractal-hosted @CarClever retirement remains separate.
- Fractal subscription cancellation remains separate.
- Auto.dev Growth-versus-Free remains separate.
- The Impact Catalog remains private and unpublished.
- No code, deployment, Vercel, connector, DNS, subscription, or existing SEO-treatment change is authorized by this recommendation.

## Sources

- [Task #72 dependency investigation](INVESTIGATION_CARCLEVER_LITE_FRACTAL_EXIT_DEPENDENCY_20260921.md)
- [September runway and platform contingencies](PLAN_SEPTEMBER_RUNWAY_COST_AND_PLATFORM_CONTINGENCIES_20260921.md)
- [Old CarClever Auto.dev Free-tier assessment](ASSESSMENT_OLDCARCLEVER_FRACTAL_AUTODEV_FREE_TIER_20260921.md)
- [Tool-led SEO/GEO monetization strategy](STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md)
- [Impact funnel feasibility return](RETURN_TOOL_LED_IMPACT_FUNNEL_FEASIBILITY_20260920.md)
- [Task #72 separate-page test strategy](STRATEGY_CARCLEVER_LITE_FRACTAL_EXIT_REPLACEMENT_20260922.md)
- User/Claude live pilot report pasted Sep 22, 2026

## Approval gate

André must approve the recommended page-239 replacement product before Claude receives any implementation task. Approval of this recommendation does not approve page edits, code, deployment, model/API changes, platform submissions, or subscription actions.
