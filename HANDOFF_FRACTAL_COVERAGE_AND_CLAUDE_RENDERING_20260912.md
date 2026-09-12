# Fractal legacy CarClever: category search and Claude rendering handoff — corrected 2026-09-12

**Status:** Proposed preview investigation/fix brief. No production deployment or Anthropic submission authorized.

## Corrections from André

- Auto.dev listing fuel is primary fuel. Gasoline can be correct for an HEV/PHEV; the schema lacks secondary fuel/electrification. Preserve model/trim evidence.
- The confirmed remaining category defect is body leakage: electric truck searches return crossovers.
- Inspect the current pair cap rather than assuming it remains fixed at five.
- Explicit large-luxury searches need a real full-size tier.
- Rendering investigation must distinguish Fractal's production MCP endpoint, production origin and preview origin.

## Relevant newer-app precedent

The newer app omitted optional _meta.ui.domain for Claude compatibility, retained OpenAI-specific openai/widgetDomain/CSP, and made the widget origin project/environment-specific through NEXT_PUBLIC_WIDGET_ORIGIN with a runtime fallback. Its OpenAI custom origin and Anthropic Vercel origin were configured separately. The legacy Fractal equivalent must be verified against Fractal's actual MCP_SERVER_URL/PUBLIC_BASE_URL behavior rather than copied mechanically.

## Copyable prompt

Investigate and fix the remaining category-search and Claude rendering issues in this CarClever repository. Use the current code as source of truth, preserve all working ChatGPT behavior, and stop before production deployment.

TASK 1 — Fix body and size constraints for electrified searches

Do not treat Auto.dev fuel_type=Gasoline as proof that a listing is not hybrid. Auto.dev reports the primary fuel and has no secondary/electrification field in its listings schema. Preserve the current model/trim-based HEV/PHEV identification and qualified model-name work. A confirmed hybrid trim may legitimately have Gasoline as primary fuel.

The reproducible defect is that “electric truck under $80k” returns electric SUVs/crossovers. Current logic appears to move truck-tagged candidates to the front and then fills the limited candidate set with other EV body types. That violates the explicit truck requirement.

Trace category detection, bodySignal, model selection, candidate limits, Auto.dev calls, post-filtering, fallback and final display. When the user explicitly asks for a truck, SUV, minivan or size class, apply that as an AND constraint to the candidate models and final results. Do not backfill an electric-truck search with SUVs. If no matching truck inventory exists, return an honest no-exact-match result.

Before changing F-150 handling, compare raw Auto.dev responses for Ford/F-150 and Ford/F-150 Lightning to confirm the provider’s actual model/trim representation. Do not rely on the prior inference alone.

Audit current candidate coverage and add provider-confirmed popular electrified pickups if missing:
- Ford Maverick Hybrid
- Ford F-150 PowerBoost
- Toyota Tacoma i-FORCE MAX
- Toyota Tundra i-FORCE MAX
- Ford F-150 Lightning
- Rivian R1T
- Chevrolet Silverado EV
- GMC Sierra EV
- GMC Hummer EV Pickup
- Tesla Cybertruck

This is an audit list, not a mandatory whitelist. Verify U.S. used inventory, model years and actual Auto.dev make/model/trim strings. Do not add announced vehicles without searchable inventory or classify ordinary trims such as XLT, Lariat, Limited or TRD as electrified by themselves.

Inspect the current make/model-pair limit. The supplied trace showed selectionCount capped at 5 despite an earlier expectation that it had increased. If it is still 5, explain why. Ensure filtering happens before limiting and that the bounded strategy scales enough to query the relevant matching models rather than silently excluding them by list position.

TASK 2 — Correct “large luxury SUV” classification

The current luxury_suv list still mixes sizes. Lexus RX, Acura MDX, BMW X5, Mercedes GLE, Audi Q7/Q8 and similar vehicles can remain candidates for a general “luxury SUV” search, but they must not satisfy an explicit “large luxury SUV” request merely because they are luxurious SUVs.

Implement a separate size-aware route/tag/filter for large luxury SUVs. Verify candidates such as Cadillac Escalade/ESV, Lincoln Navigator/L, Mercedes GLS, BMW X7, Lexus LX, Infiniti QX80, Jeep Grand Wagoneer and full-size Range Rover against provider naming and inventory. Keep midsize and compact luxury SUVs out of the explicit large tier.

Test:
- large luxury SUV under $80k in 90210
- luxury SUV under $80k in 90210
- large SUV under $70k in 90210

For each result show the model and its internal size classification so the difference is auditable.

TASK 3 — Continue the Claude rendering investigation using the correct Fractal origin

Do not repeat the existing fallback as a new fix:
const publicBaseUrl = process.env.PUBLIC_BASE_URL ?? process.env.MCP_SERVER_URL;

That change already made preview resources use the Fractal preview origin instead of localhost. It did not prove Claude rendering.

The newer CarClever app required three related but separate safeguards:
1. optional resource _meta.ui.domain was deliberately omitted because a plain application origin caused Claude iOS to fetch the resource but fail to mount it;
2. OpenAI-specific openai/widgetDomain and CSP resourceDomains were kept and made equal to the actual OpenAI serving origin;
3. the widget origin was environment/project-specific rather than globally hardcoded.

Apply those as diagnostic evidence, not copied code. Inspect what this Skybridge app actually emits.

For this legacy Fractal app, distinguish:
- MCP endpoint: https://f5025062-4d61-4160-95a7-1cc05857c622.usefractal.app/mcp
- serving origin: https://f5025062-4d61-4160-95a7-1cc05857c622.usefractal.app
- preview origin: the corresponding .preview.usefractal.app origin

The widget-domain/CSP value must be an origin, not the /mcp endpoint. Preview must not leak into production. Confirm what MCP_SERVER_URL contains in both environments. If Fractal supports an environment-specific PUBLIC_BASE_URL, assess whether explicitly setting that per environment is safer than relying only on the injected fallback.

Inspect the real public resources/read payload, MIME type, resource URI, _meta, CSP, embedded asset/bootstrap URLs, serverUrl and host postMessage handshake. Check specifically whether _meta.ui.domain is emitted. If it is, test omitting only that optional field through supported application configuration/source; do not edit node_modules and do not remove openai/widgetDomain.

Required evidence:
- tools/list hash before/after
- resources/read metadata and MIME before/after
- asset/bootstrap URLs and successful HTTP retrieval
- confirmation that production values use the production Fractal origin
- fresh ChatGPT regression test
- Claude web/desktop/iOS tests where accessible, with unavailable surfaces marked NOT TESTED and exact manual steps
- text fallback remains usable

A matching schema hash does not prove rendering. Separate fresh-resource behavior from cached connector behavior. Return confirmed findings, minimal changes, test results and remaining risks. Keep the three tasks independently reviewable and stop before production deployment or Anthropic submission.
