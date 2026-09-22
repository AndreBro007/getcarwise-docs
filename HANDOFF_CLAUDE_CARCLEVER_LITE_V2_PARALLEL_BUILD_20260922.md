# Claude Engineering Handoff — Parallel CarClever Lite V2

**Task:** #72 — build a separate CarClever Lite V2 using the new Find My Car backend
**Date:** 2026-09-22
**Authorization:** André approved the parallel V2 direction and the method: copy the existing CarClever Lite web-app approach into a separate V2. Implement on a feature branch only. This handoff does not authorize merging, production deployment, WordPress edits, page-239 cutover, endpoint changes, connector changes, or subscription actions.

## Engineering assignment

This is an engineering task. Build a parallel CarClever Lite web experience in `AndreBro007/carclever-widget` that follows the current Lite's working interaction pattern and visual language, but calls the new Find My Car MCP backend. Preserve the existing V1 files and behavior as the rollback version.

Create isolated V2 page and API routes (proposed `/carclever-lite-v2` and `/api/chat-v2`). Keep V1's `/carclever-lite`, `/api/chat`, Fractal URL, prompt, parser and WordPress embed unchanged. Work on a new feature branch; do not commit to `main`.

## Mandatory startup and stop/go gate

1. Complete the standard start-of-session verification in `carclever-widget/PLAYBOOK.md` before editing: fresh-check the seven admin files, dynamically inventory the complete `getcarwise-docs` root, compare checkpoint state with `main`, read every changed file in full, review relevant repo commits, and read the Task #72 records cited below.
2. Read current `carclever-widget/STATE.md`, `TASKS.md`, `PLAYBOOK.md`, `CLAUDE.md`, `CARCLEVER_3_APPS_CURRENT_STATUS_20260912.md`, `app/carclever-lite/page.tsx`, `app/api/chat/route.ts`, `app/chat/tool-results.ts`, the old Lite card/modal/widget components, `carclever-find-my-car/lib/find-matching-vehicle-output.ts`, `lib/results-card.ts`, and the relevant registered tool code.
3. Before writing code, perform a raw read-only MCP `initialize` and `tools/list` against exactly `https://carclever-anth.getcarwise.app/mcp`, using the established MCP HTTP procedure. Confirm the returned server version matches the current portfolio record and confirm the live tools are exactly `find_matching_vehicle` and `resolve_dealer_url` with schemas compatible with current source.
4. If the endpoint, `serverInfo.version`, or schemas do not match; if the production alias is stale; or if the required current files disagree, stop before code and return the evidence. Do not silently try another production alias, switch to the OpenAI project, alter a submission, or change Vercel aliases.

Live evidence already obtained by ChatGPT on Sep 22: GET of the Anthropic endpoint returned Vercel `405 Method Not Allowed` from the MCP transport route (expected for GET), and the connected production CarClever integration successfully completed one inventory search and one dealer-URL resolution. Those checks verify route/tool usability at a high level but did not expose MCP `serverInfo.version`; your raw initialize check remains required.

## V2 interaction and capability contract

Copy the useful web-app method from Lite V1:

- branded responsive chat experience, welcome state and starter prompts;
- streaming assistant response and visible tool-working status;
- session-only conversation context and New Search reset;
- current useful query prefill behavior (`?q=` pre-fills but never auto-submits);
- mobile-first layout, keyboard use, affiliate disclosure, and clear loading/error/empty states;
- vehicle result cards and selected-vehicle follow-up within the same session.

Build the UI as a **new browser-facing Lite app route**. The `carclever-find-my-car` repository currently contains an MCP server and an MCP-host result-card resource, not a standalone browser chat UI that can simply be embedded. Use the existing Lite shell as the visual/interaction reference, then build V2 result handling against the live Find My Car contract.

V2 may use only:

1. `find_matching_vehicle` for inventory searches and exact VIN searches. Its result already contains structured candidate data, condition, history/risk evidence, identity verification, match fit, constraint checks, and available links. A direct VIN search may return the supported `buyerCheck` fields.
2. `resolve_dealer_url` for a selected vehicle when an explicit link resolution call is needed.

Respect the current tool descriptions and schemas as the contract. Do not port V1's six-tool system prompt as-is. In particular:

- Do not claim standalone affordability calculation, standalone Deal Score, general listing comparison, full vehicle-details lookup, load-more pagination, garage persistence, or a separate recall tool. They are not in the current two-tool contract.
- The existing `find_matching_vehicle` result may include a simple risk tier/reasons and a VIN Buyer Check. Display only evidence actually returned, with its limitations. Do not present it as equivalent to V1's full `analyze-deal-risk` output, a safety determination, or an NHTSA recall check.
- Show condition using the returned New/Used/unknown and CPO evidence fields; do not infer missing condition/history data.
- `ranking.matchScore` is match fit, not the old Deal Score. Label it only as a match score (or omit it); never present it as a deal-value score.
- Do not reuse `components/ResultCard.tsx` unchanged: it presents legacy Deal Score, estimated loan payment and unsupported Risk/Cost/Compare actions. Build a V2-specific result card from actual Find My Car fields. Never calculate or invent payment, deal score, market value, condition or history.
- A search result already supplies `links.affiliateUrl` and `links.affiliateFallbackUrl` when available. Use those exact returned destinations with accurate labels such as “Check availability” and “View similar options.” Do not substitute `dealerListingUrl` for the affiliate action, strip Impact parameters, hand-edit tracking, or emit a link when the relevant returned URL is null. Use the resolver tool only where the contract warrants a selected-vehicle resolution; do not call it once per card unnecessarily.
- Follow the current Find My Car prompt guidance for required fields, intent interpretation, hard filters, nationwide searches, automatic widening disclosure, empty results, unknown evidence and VIN handling. The old Lite prompt's mandatory-location rule is not the new contract: Find My Car supports nationwide search when no location is given, with scope disclosure.

## Funnel, tool and site boundaries

- Primary journey: visitor describes their needs → Find My Car searches live New/Used/CPO inventory according to the visitor's intent → V2 presents transparent matches → visitor uses the returned Edmunds/dealer action where available.
- Preserve New/Used choice and condition clarity. Keep New and Used distinct as returned; never force a condition that the visitor did not request.
- If a visitor needs a separate price, deal-score or VIN workflow, offer the verified existing GetCarWise destinations (`/tools/price-check/`, `/tools/deal-score/`, `/tools/vin-check/`) only where appropriate. Do not imply these tools are integrated into V2 or that listing data transfers automatically.
- Do not add a Trade-in affiliate CTA in this implementation unless a page-239-specific approved destination and attribution identifier are already documented. Do not reuse page 1160's pilot Sub IDs on page 239. If there is no approved Lite trade-in link, record that as a future funnel gap.
- Keep page 239's surrounding WordPress copy, canonical, SEO metadata, schema, menus, links, measurement and iframe untouched. Do not edit the Decision Center page (1160) or any active $25k/$40k SEO treatment page.
- Keep the V2 preview access-controlled or noindex. Do not add it to WordPress navigation, sitemap, or internal links.

## Implementation isolation and security

- Add new V2 files only; shared components may be reused only if they do not change V1 behavior. If a shared change would affect V1, copy the component for V2 instead.
- Use the existing server-side Anthropic SDK/remote-MCP approach for streaming, with the confirmed Anthropic endpoint fixed server-side. Never accept an MCP endpoint from browser input.
- Reuse the existing server-side `ANTHROPIC_API_KEY`; do not expose it in client code, logs, errors or `NEXT_PUBLIC_*` variables. Do not change Vercel environment variables.
- Keep the current model/provider pattern unless the existing project state proves it cannot call the MCP endpoint; if it cannot, stop and report the blocker rather than changing providers or billing.
- Do not copy the current `/api/chat` `startsWith` origin validation as-is. Implement exact normalized-origin validation for the V2 route, with a narrowly constrained method for the intended Vercel preview origin. Preserve preview deployment access protection; do not disable SSO/auth.
- Do not persist chat history or add analytics, cookies, identifiers, external tracking, or data collection. Keep session history in memory in the browser as V1 does. Document any event/attribution limitations.
- No changes to the Find My Car backend/repo, MCP tool contract, V1/V2/V3 releases, Anthropic/OpenAI/Meta submissions, production aliases, Fractal or Auto.dev settings.

## Scope limits and return

- Implement the V2 code on a new feature branch only. Do not merge, deploy to Vercel, change page 239's embed, publish a WordPress page, or alter a subscription.
- Do not run a public/live visitor test. Local verification only is within this assignment. Do not make extra live inventory calls beyond the required preflight; one live inventory search and one resolver call were already used on Sep 22.
- Follow the repository's documented engineering validation workflow for changed code. If a gate fails, report it; do not bypass it.
- Return a numbered, structured report: branch and base SHA; changed files; V1 files confirmed untouched; architecture/data-flow summary; confirmed endpoint version and tools; validation results; unsupported functionality removed from V2; security and origin handling; remaining preview/deployment prerequisite; exact rollback; and any blockers.
- Stop before Vercel preview deployment and page-239 cutover. Those require separate approval.

## Task #72 records

- `getcarwise-docs/RECOMMENDATION_CARCLEVER_LITE_PAGE239_EXIT_20260922.md`
- `getcarwise-docs/RETURN_CARCLEVER_LITE_V2_ARCHITECTURE_AUDIT_20260922.md`
- `getcarwise-docs/INVESTIGATION_CARCLEVER_LITE_FRACTAL_EXIT_DEPENDENCY_20260921.md`
- `getcarwise-docs/PLAN_SEPTEMBER_RUNWAY_COST_AND_PLATFORM_CONTINGENCIES_20260921.md`
- `getcarwise-docs/ASSESSMENT_OLDCARCLEVER_FRACTAL_AUTODEV_FREE_TIER_20260921.md`
- `getcarwise-docs/STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md`
- `getcarwise-docs/RETURN_TOOL_LED_IMPACT_FUNNEL_FEASIBILITY_20260920.md`
- `getcarwise-docs/RETURN_IMPACT_CATALOG_PRIVATE_PROTOTYPE_20260921.md`
- `carclever-widget/CARCLEVER_3_APPS_CURRENT_STATUS_20260912.md`

## Independent decisions that remain separate

- Old Fractal-hosted `@CarClever` ChatGPT app retirement.
- Fractal subscription cancellation.
- Auto.dev Free-versus-Growth decision.
- Public deployment of the private Impact Catalog prototype.
- Page 239's V1-to-V2 embed switch.
- Decision Center page 1160 SEO/indexing/traffic experiment.

