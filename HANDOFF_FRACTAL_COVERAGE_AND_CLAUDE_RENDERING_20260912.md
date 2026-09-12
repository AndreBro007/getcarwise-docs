# Fractal legacy CarClever: electrified search and Claude rendering handoff — revised 2026-09-12

**Status:** Proposed preview investigation/fix brief. No production deployment or Anthropic submission authorized.

## Assessment of the supplied latest build

The latest build made useful progress, but its report itself confirms unresolved correctness:

- strictHybridMode retains gasoline results when zero verified hybrid items survive.
- A fuel=Gasoline item was accepted because the returned/requested label contained “Hybrid.”
- electric truck returned only non-trucks; body matching reordered candidates but did not constrain the final set.
- The F-150/Lightning provider taxonomy was inferred and then described as confirmed without raw provider evidence.
- The five-pair cap remains order-sensitive.
- Large luxury taxonomy still mixes midsize models into a query whose explicit word is “large.”

The next pass therefore needs constraint enforcement and raw provider validation, not another category-routing-only test.

## Rendering evidence reconciled

The supplied rendering transcript confirms the prior Fractal change from PUBLIC_BASE_URL alone to a fallback on MCP_SERVER_URL. It normalized openai/widgetDomain and embedded serverUrl in preview while leaving tools/list unchanged. It did not include a successful Claude rendering test.

A separate documented Find My Car incident provides a narrower diagnostic lead: omission of optional _meta.ui.domain fixed Claude iOS after successful resource retrieval, while OpenAI-specific domain metadata was retained. This is a hypothesis to verify in this codebase, not permission to copy code between repositories.

## Copyable prompt

Investigate and fix the remaining electrified-search and Claude widget issues in this repository. Work from current code and live provider evidence. Keep the existing ChatGPT behavior and every tool name, description, schema and annotation unchanged. Do not deploy to production.

TASK 1 — Make combined electrified searches true AND searches

The current build improved category routing and hybrid model names, but its own live evidence still exposes these defects:

1. Strict hybrid filtering falls back to unfiltered gasoline results when zero verified hybrids survive. Remove that behavior for an explicit/required hybrid or PHEV request. Return an honest no-exact-match result or use an existing explicit relaxation mechanism; never silently return gasoline.
2. A listing reported as fuel=Gasoline was accepted because its model/title contained “Hybrid.” A requested candidate label is not proof of the listing’s powertrain. For mixed-powertrain nameplates, require trustworthy listing-level evidence. Treat unknown as unknown. Keep HEV, PHEV, BEV and mild hybrid distinct.
3. Body signals currently reorder candidates but do not constrain final results: “electric truck under $80k” returned only crossovers and was called correct because all were electric. That is incorrect. Explicit truck/SUV/minivan/size requirements must filter candidates and final listings before any cap; if no matching inventory remains, say so rather than filling with another body type.
4. The claim that Auto.dev stores Lightning as model=F-150, trim=Lightning was not proven with raw provider responses. Compare raw results for Ford/F-150 and Ford/F-150 Lightning, including model, trim, fuel_type, bodyStyle and VIN, before choosing the query representation. Do the same for ambiguous qualified names such as RX 350h, 4xe, PowerBoost and i-FORCE MAX.
5. Remove the positional failure caused by selecting only the first five pairs. Filter by all detected dimensions first, then apply a documented bounded query strategy. Do not let list order decide whether a valid body/powertrain class is searched.

Audit and add missing high-demand U.S. used-market coverage where provider evidence supports it. Prioritize:
- Hybrid pickups: Ford Maverick Hybrid; Ford F-150 PowerBoost; Toyota Tundra i-FORCE MAX; Toyota Tacoma i-FORCE MAX.
- Other high-value hybrid gaps: Toyota Grand Highlander Hybrid, Corolla Cross Hybrid, Venza, Sequoia and 4Runner i-FORCE MAX; Ford Escape Hybrid; Kia Niro Hybrid; Mazda CX-50 Hybrid; Lexus NX/UX hybrid variants.
- PHEV: RAV4 Prime/Plug-in Hybrid, Prius Prime/Plug-in Hybrid, Escape PHEV, Outlander PHEV, Pacifica Hybrid, Wrangler/Grand Cherokee 4xe, Sorento/Sportage/Tucson/Santa Fe PHEV, Mazda CX-70/CX-90 PHEV, BMW X5 xDrive45e/50e, Volvo Recharge/T8 and Lexus “h+” variants.
- Electric pickups: F-150 Lightning, Rivian R1T, Silverado EV, Sierra EV, GMC Hummer EV Pickup and Cybertruck; also verify large EV SUVs such as EV9, R1S and Model X.

This is an audit list, not a mandatory whitelist. Verify actual Auto.dev naming and U.S. model years. Retain discontinued models for used searches. Do not add announced vehicles with no searchable inventory. Do not infer electrification from ordinary trims such as Limited, XLT, Lariat or TRD. Remember that older Siennas and mixed-year nameplates may be gasoline even if current versions are hybrid-only.

Acceptance tests must inspect actual returned listings, not category labels:
- large hybrid SUV under $70k in 90210
- hybrid pickup under $50k in 90210
- full-size hybrid truck under $70k in 90210
- plug-in hybrid SUV under $50k in 90210
- plug-in hybrid minivan under $45k in 90210
- electric truck under $80k in 90210
- large electric SUV under $80k in 90210
- ordinary gasoline truck control
- explicit no-match case

For every returned item show year/make/model/trim, provider fuel evidence, body/size classification and which hard constraints passed. No gasoline in required HEV/PHEV results, no HEV in required PHEV results, and no crossover/SUV in required truck results. If inventory is absent, the correct result is no exact matches.

TASK 2 — Continue the Claude rendering investigation from the already-attempted fix

Do not repeat this completed change as the solution:
const publicBaseUrl = process.env.PUBLIC_BASE_URL ?? process.env.MCP_SERVER_URL;

That change already made Skybridge’s resource openai/widgetDomain/serverUrl use the Fractal preview origin instead of localhost, and tools/list stayed byte-identical. It did not by itself prove the widget renders in Claude.

Inspect the exact current resources/read payload and widget HTML served through the real preview/public MCP URL. Compare it with the payload that currently works in ChatGPT. Trace resource URI, MIME type, _meta fields, CSP, asset URLs, embedded serverUrl, postMessage/host handshake and any host-specific metadata.

A relevant independently confirmed precedent from another MCP app: Claude iOS failed after a successful resources/read when the optional resource field _meta.ui.domain contained the app’s plain serving origin; omitting _meta.ui.domain fixed Claude, while the separate OpenAI-specific openai/widgetDomain remained for ChatGPT. Check whether this repository or Skybridge emits _meta.ui.domain. If present, test omitting only that optional field through supported source/configuration—not by editing node_modules. Do not remove or repurpose openai/widgetDomain merely because the names look similar.

Also verify whether production would emit its production MCP origin rather than the preview origin; MCP_SERVER_URL may be environment-specific. Do not hardcode either domain.

Evidence required:
- current tools/list hash before/after
- current resources/read metadata and MIME before/after
- extracted asset/bootstrap URLs and proof they return successfully
- exact change and why it affects Claude mounting
- ChatGPT live regression test
- Claude web, desktop and iOS test where accessible; mark unavailable surfaces NOT TESTED with exact manual steps
- useful text fallback remains available

A schema hash proves tool-contract safety, not widget rendering. If code and resources are correct but only an existing Claude connector remains stale, prove fresh connector/resource behavior before changing code again.

Return confirmed findings, raw evidence, changes, tests and remaining risks. Keep search and rendering changes independently reviewable. Stop before production deployment or Anthropic submission.
