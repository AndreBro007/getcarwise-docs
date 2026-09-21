# Investigation — CarClever Lite Fractal Exit Dependency

**Date recorded:** 2026-09-21  
**Status:** Parked for later decision; investigation only  
**Source:** Claude read-only repository, live MCP and WordPress embed investigation reported by André  
**Authority:** Record findings only. No code, WordPress, Vercel, connector, Fractal, app or subscription change is authorized.

## Executive finding

CarClever Lite is the only one of the four website-embedded apps currently dependent on Fractal. It cannot be moved to the production Find My Car MCP server through a URL-only swap because the two servers expose materially different tool contracts.

The dependency should be resolved before Fractal is cancelled, but it is deliberately parked while Task #71 proceeds.

## Verified dependency map reported by Claude

All four website apps live in `AndreBro007/carclever-widget` and are served by the `carclever-widget` Vercel project.

| Website app | WordPress page | Backend | Fractal dependency |
|---|---:|---|---|
| CarClever Lite | 239 | `app/api/chat/route.ts` → Anthropic API with `mcp_servers` pointed at the Fractal MCP URL | **Yes** |
| Deal Score | 453 | `app/api/deal-score/route.ts` → Auto.dev directly | No |
| Price Check | 527 | `app/api/price-check/route.ts` → Auto.dev directly | No |
| VIN Check | 1023 | `app/api/vin-check/route.ts` → Auto.dev directly | No |

WordPress page 239 currently embeds:

`https://carclever-widget.vercel.app/carclever-lite`

That frontend calls `/api/chat`. The route currently hardcodes the Fractal MCP server and contains system-prompt assumptions for multiple Fractal tools, including:

- `search-used-cars`;
- `analyze-deal-risk`;
- `calculate-affordability`;
- `vehicle-comparison`;
- `get-vehicle-details`;
- `resolve-dealer-url`.

Claude’s live raw MCP check reported that the current Find My Car production deployment (`dd68e15`) exposes only:

- `find_matching_vehicle`;
- `resolve_dealer_url`.

The paused V3 `check_vehicle` tool is not part of the current production contract.

## Consequence

A direct replacement of the Fractal MCP URL with the Find My Car MCP URL would leave CarClever Lite’s prompt calling tools that do not exist. This would be a functional regression, not a configuration-only migration.

The September 2 dependency finding therefore remains materially current despite later V2 scoring, condition-label and Impact-link work.

## Separate old-app dependency

The Tools Hub and Try CarClever pages do not directly embed the Fractal MCP server. They link to the old `@CarClever` ChatGPT app, which is itself Fractal-hosted. That app retirement/link-routing issue is related to the Fractal exit but is separate from the page-239 embedded CarClever Lite backend migration.

Do not merge these two work items silently:

1. website page 239 / CarClever Lite backend replacement;
2. old `@CarClever` ChatGPT app retirement and replacement links.

## Future options — not yet selected

### Option A — two-tool Lite rewrite

Rewrite CarClever Lite’s system prompt and supported flows around the current production Find My Car contract:

- `find_matching_vehicle`;
- `resolve_dealer_url`.

This is likely the fastest clean Fractal exit but deliberately removes separate risk, affordability, comparison and detail-tool flows unless equivalent behavior is designed elsewhere.

### Option B — wait for a broader production contract

Resume and complete the relevant V3/later capabilities first, then rewrite Lite against the expanded production server contract. This may preserve more feature breadth but is blocked on a separate product decision and engineering sequence.

### Possible third path to assess later

Keep the Lite frontend but move selected non-search functions to direct first-party server routes rather than requiring every flow to exist as an MCP tool. This was not evaluated in Claude’s reported investigation and is not an approved direction; it should be compared explicitly when the task resumes.

## Required future decision package

Before implementation, return:

1. current-vs-target user journeys and feature-loss table;
2. whether page 239 remains a chat interface or becomes a narrower guided finder;
3. exact target tool/API contract;
4. handling of risk, affordability, comparison and vehicle details;
5. old `@CarClever` app link-retirement plan;
6. Auto.dev/Anthropic usage and cost implications;
7. rollback and live verification plan;
8. SEO/GEO and analytics implications for page 239;
9. confirmation that no active submitted/reviewed app is modified unintentionally.

## Current decision

Record and park. Do not change the Fractal URL, CarClever Lite prompt, page 239 iframe, production Find My Car server, Tools Hub links, Try CarClever links, V3 status or any subscription now.

Resume only after André explicitly selects this task following the Task #71 work or as part of the September Fractal-exit decision.
