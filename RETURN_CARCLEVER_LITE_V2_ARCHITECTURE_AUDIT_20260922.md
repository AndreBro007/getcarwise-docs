# Task #72 — CarClever Lite V2 architecture audit

**Date:** 2026-09-22
**Type:** Read-only repository and architecture review
**Result:** A parallel Lite V2 is technically feasible as a separate web route and API route in `carclever-widget`; the Find My Car repo itself does not currently contain a standalone website frontend.

## Scope confirmed

This audit concerns the actual CarClever Lite web app embedded on WordPress page 239, not the separate Decision Center content page (page 1160). The canonical dependency investigation says page 239 embeds `https://carclever-widget.vercel.app/carclever-lite`, which calls `/api/chat`; that API route currently invokes the Fractal MCP server. Deal Score, Price Check and VIN Check remain independent Auto.dev-backed tools.

## Findings

### 1. There is no standalone Find My Car website UI in its repo

`AndreBro007/carclever-find-my-car` is a Next.js MCP server. Its package and README describe an MCP server on Vercel; the app route is the MCP transport endpoint (`app/[transport]/route.ts`). It exposes an MCP Apps result-card resource for MCP hosts such as Claude/ChatGPT. The repo does not currently expose a regular browser chat page or general-purpose embedded website frontend.

Therefore the phrase “new CarClever frontend” should be implemented as a new Lite web UI powered by the new CarClever backend. Reuse the existing Lite look, responsive chat layout and brand elements as the design starting point; do not assume the host-rendered MCP Apps card can itself be embedded as a normal web page.

### 2. Existing Lite UI can be copied without changing V1

The current Lite UI is in `carclever-widget/app/carclever-lite/page.tsx`; it sends streaming requests to `/api/chat` and uses `app/chat/tool-results.ts` to parse the legacy Fractal names and output shapes. The API route `app/api/chat/route.ts` contains the old Fractal URL and six-tool prompt assumptions.

A V2 can be isolated in the same repo as a new page route (for example `/carclever-lite-v2`) plus a distinct API route (for example `/api/chat-v2`). The current route and current page can remain byte-for-byte untouched. The preview URL can be tested before page 239's iframe is changed.

### 3. Existing card UI cannot be copied as-is

The current `components/ResultCard.tsx` is built around legacy values such as `deal_score`, an estimated loan payment, risk/cost/compare buttons, and the old vehicle registry. The new production `find_matching_vehicle` schema returns a different structure: identity, condition, listing, history, verification, match-ranking, resolved links and other evidence. Its `matchScore` is a search-fit measure, not the old Deal Score; it must not be labeled as the same score.

Build a V2 card/adapter from the current Find My Car output contract. It should display only data actually returned, show New/Used/CPO/unknown distinctly, preserve verification/relaxation notes, and offer only supported actions. Remove or route the legacy Risk, Cost, Compare and Details affordances in V2; the old V1 retains them unchanged. Link to the existing Deal Score, Price Check and VIN Check pages only as separate, clearly labeled continuations where the handoff makes sense.

### 4. Current backend contract and endpoint

The Task #72 dependency record's production probe found two tools on Find My Car: `find_matching_vehicle` and `resolve_dealer_url`. The `check_vehicle` tool belongs to paused V3 and is not part of this V2 contract. The full `find_matching_vehicle` output schema is in `carclever-find-my-car/lib/find-matching-vehicle-output.ts`.

The current portfolio status (updated Sep 22) records the Anthropic production endpoint as `https://carclever-anth.getcarwise.app/mcp`, serving the approved V2 backend release with the Impact link migration. It also records that the Anthropic app's submitted URL is still awaiting support-side replacement and that V2 is under review. Before implementation, independently confirm the exact endpoint's live `initialize` server version and both tool schemas. Do not change either platform submission, endpoint configuration, aliases, V1/V2/V3 branch, or production deployment for this work.

### 5. Feasible server-side call pattern

The existing `carclever-widget` API already uses the Anthropic SDK to stream a chat while attaching a remote MCP server through Anthropic's MCP toolset. That is a feasible pattern for a separate V2 API route: keep the Anthropic API key server-side, call the confirmed Find My Car MCP endpoint from the server-side Anthropic request, expose only the V2 stream to its own page, and provide a V2-specific prompt and result parser.

This keeps browser clients from receiving provider credentials. The existing API route's origin allowlist uses `startsWith` matching and does not include arbitrary Vercel preview hosts. Do not copy that check unchanged. The V2 route needs exact origin validation that supports only the intended production host and the specific protected Vercel preview deployment (or equivalent verified deployment-host mechanism). Keep preview access protection enabled. The MCP endpoint is designed for external MCP clients and has no separate private authorization boundary in the current app configuration; do not call it directly from arbitrary browser JavaScript.

### 6. Provider and cost implications

- Fractal calls stop only for the new V2 path. V1 and the old Fractal service remain available during preview and rollback; there is no immediate Fractal cancellation or cost saving.
- V2 can retain the existing Anthropic API provider pattern. That means Anthropic API/model usage and billing remain part of the V2 cost. A private preview introduces additional test calls.
- Live inventory calls continue through the existing Find My Car backend and its Auto.dev integration. V2 adds demand to the shared production Auto.dev-backed service; it does not justify an Auto.dev tier change by itself. Measure request volume and quotas before any plan decision.
- No Meta approval or OpenAI app submission is needed for a private Vercel-hosted web route. Keep the Anthropic API key, Anthropic MCP endpoint and model usage separate from the review/submission lifecycle; no submission-facing changes are proposed.

## Recommended V2 shape

Use the `carclever-widget` repo and current `carclever-widget` Vercel project, with all work isolated to a feature branch and preview deployment:

1. Add a distinct Lite V2 page route by copying the existing Lite shell as a starting point.
2. Add a distinct V2 server API route; do not alter `/api/chat` or the existing Lite page.
3. Invoke the exact verified Find My Car production MCP endpoint using the existing Anthropic server-side remote-MCP approach.
4. Define a V2 prompt that supports live vehicle discovery and dealer destination resolution only. Explain unsupported intents briefly and route to existing specialist tools where appropriate.
5. Create a parser/card adapter against the live structured schema; do not reuse old Deal Score or estimated-payment fields as if they exist in Find My Car.
6. Keep the page239 iframe on V1. Use an access-protected preview URL to test independently.
7. After the implementation has passed the agreed QA, ask André separately before changing page239's single iframe target. Retain the V1 route and Fractal configuration for one-step rollback.

## Minimum implementation/verification plan after approval

- Confirm endpoint `initialize` version and both tool schemas before coding; make sure the confirmed environment is the expected Anthropic production alias, not a stale alias.
- Implement only new page/API/parser/card files; no changes to the old V1 route, Find My Car backend, submissions, tool schema or WordPress.
- Test a representative local and nationwide search, strict filters, New/Used/CPO labels, relaxed/empty results, provider errors, dealer URL resolution, unsupported affordability/risk/compare requests, and query-to-result rendering.
- Verify preview origin checks and access protection; inspect that secrets never reach client bundles or logs; confirm the preview does not write/persist chat history.
- Compare mobile and desktop layout with the live Lite page and verify keyboard/accessibility basics.
- Record response latency, Anthropic tokens/cost, tool invocations and Auto.dev usage if current reporting supports them; otherwise document the gap and don't claim conversion impact.
- Keep the page-239 embed untouched until a separate cutover approval. On approved cutover, capture the exact old embed and test immediate restoration.

## Risks and unresolved specifics

- The phrase “new CarClever frontend” does not map to a standalone browser UI in the inspected Find My Car repository. The recommended interpretation is a new Lite UI using that backend and its output contract. If André meant another existing web UI/source, its repo or URL was not discoverable in the accessible project inventory.
- The current Lite frontend is tightly coupled to old Fractal tools and old output types. The presentation shell is reusable; the result parser/cards and action affordances need a V2-specific contract.
- The Anthropic production alias and exact schemas must be live-confirmed immediately before implementation because the portfolio status document notes separate platform origins and manual Vercel alias promotion.
- The existing origin guard cannot safely be copied as-is for preview; explicit preview-origin handling is a release requirement.
- During test, V1 and V2 coexist. Monitor preview test use so it does not create unbounded Anthropic or Auto.dev usage.

## Decisions that remain separate

1. Page-239 V1-to-V2 iframe cutover.
2. Retirement of the old Fractal-hosted `@CarClever` ChatGPT app.
3. Fractal subscription cancellation.
4. Auto.dev Free-versus-Growth choice.
5. Public deployment of the Impact Catalog prototype.
6. Decision Center page 1160 launch/indexing/measurement decisions.

## Explicitly unchanged

- Page 239, its V1 iframe, its Fractal prompt/route, and the existing Fractal-backed Lite experience.
- The Find My Car production code, endpoint aliases, V1/V2/V3 branches, active review records, and platform submissions.
- Deal Score, Price Check and VIN Check routes and their Auto.dev integrations.
- Decision Center page 1160 and all active SEO/GEO treatment pages.
- The old `@CarClever` app, Fractal subscription, Auto.dev plan, connectors and Impact Catalog publication state.

## Recommendation status

Architecture Gate 1 is complete at the repository-evidence level. The smallest viable design is a separate V2 page/API route and V2-specific results adapter in `carclever-widget`, previewed independently. Before Claude receives an implementation assignment, André should approve that concrete implementation scope and the interpretation that V2 is a new Lite frontend over the Find My Car MCP backend (not a standalone website UI already present in the Find My Car repo).

