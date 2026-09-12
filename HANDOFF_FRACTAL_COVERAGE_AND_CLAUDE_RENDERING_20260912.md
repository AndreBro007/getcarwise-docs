# Fractal legacy CarClever: category search and Claude rendering handoff — corrected 2026-09-12

**Status:** Fractal implementation and preview-test prompt. Owner performs cross-host acceptance after choosing Deploy to Production.

## Contract and testing boundary

All tool setup is frozen: inventory, registrations, annotations, descriptions, schemas, tool-facing metadata, output-template URI and resource URI must remain unchanged. Fractal can test internal search behavior and preview resource output. It cannot test external ChatGPT or Claude clients, so those checks are explicitly handed to André after production deployment.

## Copyable prompt

Investigate and fix the remaining category-search and Claude-rendering issues in this CarClever repository.

GLOBAL CONTRACT FREEZE

Do not add, remove, rename or re-register any tool. Do not modify any tool title, description, parameter, parameter description, input schema, output schema, annotation, security declaration, tool-facing _meta, output-template URI or resource URI.

Capture the complete tools/list response before editing and again after all work. Compare canonicalized JSON and a raw hash. They must be byte-identical. The search fixes may change which listings are returned, and a confirmed rendering fix may change widget resource metadata, but the tool contract itself must remain unchanged.

TASK 1 — Fix body constraints for electrified searches

Do not treat Auto.dev fuel_type=Gasoline as proof that a listing is not hybrid. Auto.dev reports primary fuel and has no secondary-fuel/electrification field in its listings schema. Preserve the current model/trim-based hybrid and PHEV identification.

The reproducible defect is that “electric truck under $80k” returns electric SUVs/crossovers. Current logic appears to move truck candidates forward and then fill the candidate set with other EV body types.

Trace category detection, bodySignal, model selection, pair limits, Auto.dev calls, post-filtering, fallback and final display. When the user explicitly asks for a truck, SUV, minivan or size class, apply that as an AND constraint to the selected models and final results. Do not backfill an electric-truck search with SUVs. If no matching truck inventory exists, return an honest no-exact-match result.

Before changing F-150 handling, compare raw Auto.dev responses for Ford/F-150 and Ford/F-150 Lightning. Report returned model, trim, fuel type, body style and VIN. Use that evidence to determine the correct query representation.

Audit and add provider-confirmed electrified pickups if missing:
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

This is an audit list, not a required whitelist. Verify actual U.S. used inventory, model years and Auto.dev naming. Do not infer electrification from ordinary trims such as XLT, Lariat, Limited or TRD.

Inspect the current make/model-pair limit. The supplied trace showed selectionCount capped at five. Confirm the current implementation. Apply body/powertrain filtering before the limit and use a bounded strategy that expands enough to search the relevant matching models instead of excluding them by list position.

Run these tests in the Fractal environment:
- electric truck under $80k in 90210
- compact electric truck under $60k in 90210
- hybrid pickup under $50k in 90210
- full-size hybrid truck under $70k in 90210
- ordinary gasoline-truck control
- explicit no-inventory case

Show actual returned year/make/model/trim, body classification and hybrid/EV evidence. An electric-truck test passes only when every returned vehicle is a truck. A no-match response is correct when no matching truck inventory exists.

TASK 2 — Correct “large luxury SUV” classification

The current luxury_suv list mixes sizes. RX, MDX, X5, GLE, Q7/Q8 and similar vehicles may remain in a general luxury-SUV search, but they must not satisfy an explicit “large luxury SUV” request merely because they are luxury SUVs.

Add a size-aware large-luxury route, model tag or filter. Verify full-size candidates such as:
- Cadillac Escalade/ESV
- Lincoln Navigator/L
- Mercedes-Benz GLS
- BMW X7
- Lexus LX
- Infiniti QX80
- Jeep Grand Wagoneer
- full-size Range Rover

Verify provider naming and inventory before adding anything.

Run these tests in the Fractal environment:
- large luxury SUV under $80k in 90210
- luxury SUV under $80k in 90210
- large SUV under $70k in 90210

Report every returned model’s internal size classification and show that general luxury searches still work.

TASK 3 — Prepare the Claude rendering fix for production validation

Do not repeat this existing change as a new solution:

const publicBaseUrl = process.env.PUBLIC_BASE_URL ?? process.env.MCP_SERVER_URL;

That change already made preview resource metadata use the Fractal preview origin instead of localhost. It did not prove Claude rendering.

The newer CarClever app used three separate safeguards:
1. optional resource _meta.ui.domain was omitted because a plain application origin caused Claude iOS to retrieve the resource but fail to mount it;
2. OpenAI-specific openai/widgetDomain and CSP resourceDomains remained and matched the actual OpenAI serving origin;
3. widget origin was environment/project-specific rather than globally hardcoded.

Use these as diagnostic evidence. Inspect what this Skybridge repository actually emits.

Distinguish:
- MCP endpoint: https://f5025062-4d61-4160-95a7-1cc05857c622.usefractal.app/mcp
- production serving origin: https://f5025062-4d61-4160-95a7-1cc05857c622.usefractal.app
- preview serving origin: the corresponding .preview.usefractal.app origin

openai/widgetDomain and CSP domain entries must use an origin, not the /mcp endpoint. Preview values must not be embedded as production constants.

Inspect the preview resources/read response, MIME type, resource URI, resource _meta, CSP, embedded serverUrl, asset/bootstrap URLs and host postMessage handshake. Check specifically whether resource _meta.ui.domain is emitted. If present and the evidence supports the known Claude failure pattern, omit only that optional field through supported application source/configuration. Do not edit node_modules and do not remove openai/widgetDomain.

Confirm from code and environment handling how MCP_SERVER_URL/PUBLIC_BASE_URL will resolve after production deployment. If Fractal supports environment-specific PUBLIC_BASE_URL configuration, report whether it should be set to the production serving origin. Do not hardcode the preview or production domain in source.

Fractal-side evidence required:
- tools/list remains byte-identical
- resources/read metadata and MIME before/after
- preview asset/bootstrap URLs return successfully
- exact source diff
- explanation of the expected production origin
- confirmation that text fallback remains present

End with a short manual acceptance checklist for the owner to run after pressing Deploy to Production:
1. fetch production resources/read and confirm production origin, never preview or localhost;
2. reconnect/create a fresh ChatGPT connector and confirm the widget, photos, links and actions;
3. reconnect/create a fresh Claude connector and test Claude web, desktop and iOS;
4. record any client-specific failure separately from server/resource reachability.

Return confirmed findings, changes, Fractal-side tests, the unchanged tool-contract comparison and the owner’s post-deployment checklist. Keep the three tasks independently reviewable.
