# Task #72 — CarClever Lite parallel V2 app recommendation

**Date:** 2026-09-22
**Status:** Corrected recommendation after André's clarification; read-only architecture audit complete; implementation not approved.
**Decision requested:** Approve the parallel-app direction before any engineering implementation task is issued.

> This document supersedes the earlier static Decision Center replacement recommendation. That recommendation confused the separate page-1160 funnel pilot with the CarClever Lite web app on page 239.

## Scope — the actual app

The target is the CarClever Lite web app embedded on WordPress page 239. The existing site-wide audit found this Lite app is the web-app consumer that calls the old Fractal CarClever backend. Deal Score, Price Check and VIN Check are separate tools and call Auto.dev directly. The Decision Center page (page 1160) is a separate content/funnel pilot and is not the Lite replacement.

## Recommendation

Keep the current page-239 Lite app and its Fractal-backed V1 intact. Build a separate CarClever Lite V2 web app using the new CarClever frontend and the currently supported production Find My Car tools. Test V2 at a separate preview/staging URL. Once the new app passes agreed checks and André separately approves the cutover, change only page 239's embed target to V2. Keep V1 and its Fractal path available for immediate rollback.

This avoids stripping features out of the current app, gives us a known-good control, and creates a clean place to add capabilities as the new CarClever/V3 contract becomes production-ready. Do not point the old six-tool prompt at a two-tool backend.

## Feature contract for first V2 release

- Reuse the actual new CarClever frontend if it is available and appropriate to embed. A short read-only architecture check must confirm what frontend/source is meant, whether it is reusable, and the supported deployment pattern.
- Initially support only the production tools verified for the intended backend: `find_matching_vehicle` and `resolve_dealer_url`. Confirm endpoint/version and tool schemas during the architecture check.
- Design the prompt and interface around those two tools. Do not imply that affordability, standalone deal-risk, broad vehicle comparison, or vehicle-details tools are available unless the checked production contract confirms them.
- Where useful, link to existing GetCarWise Deal Score, Price Check and VIN Check pages instead of reimplementing them inside V2. Keep their Auto.dev routes independent.
- Keep page-239-specific branding, purpose and conversion cues recognizable. Preserve clear New/Used/CPO condition presentation, dealer link resolution, error handling and a usable mobile layout.
- Add future capabilities only when their API/tool contract is approved, deployed in the intended environment, and separately validated. Maintain a versioned capability list so V2 never promises tools that are only experimental.

## Funnel and product fit

The app's primary job remains helping a visitor discover matching inventory and continue to a relevant dealer/listing action. Its conversion path should be:

1. Visitor describes needs and constraints.
2. V2 searches matching live inventory through `find_matching_vehicle`.
3. V2 presents explainable matches with condition labels and appropriate next actions.
4. V2 resolves the dealer destination through `resolve_dealer_url`.
5. For a specific listing needing additional evaluation, link to the relevant existing GetCarWise tool (Deal Score, Price Check, or VIN Check) where the destination and handoff are verified.
6. Preserve New, Used and Trade-in pathways only where they fit the visitor's intent; do not make the affiliate funnel displace the app's core vehicle-discovery job.

Track app opens, search starts/completions, result-to-dealer actions, existing-tool referrals, and New/Used/Trade-in outbound actions when available. Identify V2 distinctly from V1. Do not add analytics or personal-data collection without separate approval; record current event, consent, and attribution limits before implementation.

## Parallel architecture and release gates

### Gate 1 — read-only architecture check

Confirm:
- exact source/repository and ownership of the 'new CarClever frontend' intended for this Lite experience;
- whether it is a web UI that can be reused/embedded, or whether the Lite interface must be recreated;
- the production endpoint and exact schemas/version for `find_matching_vehicle` and `resolve_dealer_url`;
- safe server-side invocation/authentication, secrets handling, CORS/embed constraints, and allowed model provider/cost if applicable;
- how to isolate V2 deployment/config from Find My Car V1/V2/V3 and from page 239's current V1 app;
- page 239's current embed dimensions/behavior and the exact one-field/one-embed rollback method;
- the current Fractal consumer inventory and whether any old @CarClever distribution is separate.

Return evidence and the smallest implementation proposal. No code or platform changes during this gate.

### Gate 2 — V2 build and isolated verification

After André approves the architecture and implementation scope, Claude may build V2 on a separate branch/project/URL. Verify realistic search requests, correct tool selection and arguments, result rendering, dealer resolution, unsupported-intent handling, empty/error states, mobile layout, privacy/logging behavior, and that page 239/V1 remains unchanged.

Use a private or noindex preview. Do not change the live embed during this gate.

### Gate 3 — page-239 cutover

Only after V2 verification and André's separate approval, switch page 239's embed target to V2. Record the prior embed value and exact rollback steps. Monitor the V2 route and user path. Roll back by restoring the prior V1 embed if the V2 app fails or materially degrades the journey.

### Gate 4 — additive V3 capabilities

Add tools only when the desired capability is present in the approved, deployed backend contract and its costs, UX, safety and failure behavior are understood. Add one capability at a time, update the capability list and test both the new path and existing search behavior.

## Separate decisions — not bundled

1. **Page 239 Lite V1 → V2 embed cutover:** only after separate approval and successful preview verification.
2. **Old Fractal-hosted @CarClever ChatGPT app retirement:** separate distribution decision; page-239 migration does not retire it.
3. **Fractal subscription cancellation:** separate decision after all consumers (including old app distribution) are inventoried and any needed rollback window is complete.
4. **Auto.dev Free vs Growth:** separate shared-key/quota decision; changing Lite does not decide this.
5. **Public Impact Catalog deployment:** separate authorization; prototype stays private.
6. **Decision Center page 1160:** independent funnel/content test, not the replacement Lite app.

Fractal cancellation should not be considered until V2 has replaced the page-239 Fractal call, every other Fractal consumer is accounted for, the old app decision is explicit, and the rollback/retention period has passed.

## Expected impact and limits

The strongest expected benefit is reduced coupling to Fractal for the website app while preserving a working version and allowing capability growth without deleting the legacy implementation. The user journey retains live inventory search and dealer continuation. The main risk is assuming a reusable 'new frontend' exists when the new CarClever may currently be delivered only through MCP/platform integrations; Gate 1 resolves that. The two-tool contract also means V2 should not promise parity with V1's broader Fractal prompt.

Do not forecast lead or revenue lift without baseline and attribution. The current historical lead attribution is limited; collect a distinct V2 baseline before drawing business conclusions.

## Explicitly unchanged

- Page 239 stays on the existing Fractal-backed Lite V1 until the separate cutover approval.
- V1 code/config, Fractal endpoint/prompt, and rollback path stay intact.
- Deal Score, Price Check, VIN Check and Find My Car production behavior remain unchanged.
- No Vercel, WordPress, DNS, connector, Fractal, Auto.dev, Meta, or subscription changes are authorized by this recommendation.
- Decision Center page 1160 and active $25k/$40k SEO measurement treatments remain separate and unchanged.
- The Impact Catalog remains private and unpublished.

## Architecture audit result and next action

The read-only Gate 1 audit is complete. The Find My Car repository contains an MCP server with an in-host result-card resource, not a standalone browser chat website. The recommended minimal V2 is a separate page route and API route in `carclever-widget`, with a V2-specific prompt/parser/card adapter calling the independently verified production MCP endpoint server-side. The old page and API routes remain untouched. Full findings, security boundaries, endpoint/review caveats, dependencies and implementation QA gates are recorded in [the architecture audit return](RETURN_CARCLEVER_LITE_V2_ARCHITECTURE_AUDIT_20260922.md).

Before Claude receives an implementation assignment, André should approve this concrete implementation scope and interpretation of “new CarClever frontend.” No code, deployment or page-239 embed change is authorized yet.

