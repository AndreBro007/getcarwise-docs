# Fractal CarClever coverage and rendering handoff — 2026-09-12

Status: proposed preview investigation/fix brief; no deployment or Anthropic submission authorized. Latest build report was not attached, so no exact coverage delta is claimed.

Verification: fetched seven required administrative files, dynamically listed getcarwise-docs and fetched all 90 root files. Read current submission/portfolio records and relevant rendering decisions; checked latest relevant administrative commit diffs against current documents. Historical engineering behavior is documented evidence, not independently reproduced in this session. No application code accessed or changed.

Current state: Sep 12 records supersede older STATE opening sections: Find My Car V2 is in review on both platforms; separate legacy Fractal work does not authorize changing it. Legacy resubmission remains proposed. This handoff supports the user-requested legacy investigation; unrelated ChatGPT-lane tasks remain untouched.

Rendering findings:
- DECISIONS.md Aug 28 batch: omission of resource _meta.ui.domain recorded as confirmed by Claude iOS A/B; OpenAI namespaced domain retained separately.
- DECISION-20260902-003: legacy Skybridge serving-origin fallback fix recorded as preview-only, tools/list unchanged. TASKS records deliberate production pause due to serving-domain/review risk. Current build/deployment inclusion unknown.
- Sep 12 closeout records separate Find My Car stale connector metadata; not proof of legacy root cause.

Sources: carclever-widget/DECISIONS.md, TASKS.md, CODE_AGENT_PROMPT_CONVENTIONS.md; getcarwise-docs/REVIEW_CARCLEVER_LEGACY_ANTHROPIC_RESUBMISSION_20260912.md and STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md. Candidate OEM references: https://www.toyota.com/tacoma/ ; https://www.toyota.com/tundra/ ; https://www.toyota.com/electrified-vehicles/ ; https://www.ford.com/trucks/maverick/ ; https://www.kia.com/us/en/ev9 ; https://www.chrysler.com/pacifica-hybrid.html . Candidate list is not a measured popularity ranking or verified missing inventory list.

## Copyable prompt

Investigate and fix two issues in this CarClever project. ChatGPT is live and working: preserve that experience. Work in an isolated preview; do not deploy to production or change the live endpoint. First establish the current code and reproduce each defect; only fix confirmed problems. If a hypothesis is disproved, report it and leave that behavior alone.

TASK 1 — Complete hybrid/PHEV/EV search coverage
Combined searches previously lost body/size requirements: “large hybrid SUV under $70,000 in 90210” returned Prius listings. The latest build reportedly improves this. Verify the current implementation rather than assuming that defect or a five-model cap still exists.

Audit supported U.S. used-market make/model/year/powertrain variants and search aliases. Priority candidates to check, adding only genuinely missing coverage:
- Hybrid pickups: Ford F-150 PowerBoost, Maverick Hybrid; Toyota Tundra and Tacoma i-FORCE MAX. Distinguish full-size, midsize and compact pickups. Do not identify hybrids from XLT, Lariat, Limited or TRD badges alone.
- Hybrid family vehicles: Highlander/Grand Highlander Hybrid, Sequoia, Sienna, RAV4/CR-V Hybrid, Tucson/Santa Fe Hybrid, Sportage/Sorento Hybrid.
- PHEVs: RAV4 Prime/Plug-in Hybrid, Prius Prime/Plug-in Hybrid, Escape PHEV, Pacifica Hybrid, Outlander PHEV, Wrangler/Grand Cherokee 4xe, Tucson/Santa Fe/Sportage/Sorento PHEV, Lexus NX 450h+/RX 450h+, Volvo Recharge/T8, BMW X5 xDrive45e/50e, Mazda CX-70/CX-90 PHEV.
- EVs: Tesla Model 3/Y/S/X, Mustang Mach-E, Ioniq 5/6, Kia EV6/EV9/Niro EV, Bolt EV/EUV, Nissan Leaf, VW ID.4; pickups F-150 Lightning, Rivian R1T, Silverado EV, Sierra EV, Cybertruck; larger SUVs Rivian R1S and Model X.

This is an audit seed list, not a required hardcoded whitelist or a claim these are missing. Verify U.S. model years and aliases from manufacturer sources and actual provider data. Preserve discontinued used-market models. Distinguish HEV, PHEV, BEV and mild hybrid; do not let Ram eTorque silently satisfy a full-hybrid requirement. Do not invent available plug-in pickups from announcements.

Trace request parsing → model candidates → caps/API requests → listing verification → ranking/fallback → displayed vehicles. Preserve all explicit constraints together, including price, location, size/body, drivetrain and powertrain. Check whether caps, ordering or fallback drop valid candidates or reintroduce mismatches. Mixed-powertrain models require listing-level evidence; unknown is not confirmed hybrid/PHEV/EV. Keep “large SUV” distinct from “three-row SUV,” with a documented classification.

Acceptance: test hybrid pickup, full-size hybrid pickup, Maverick Hybrid AWD, PHEV SUV, PHEV minivan, large electric SUV, electric pickup, and the original large-hybrid-SUV query, plus ordinary petrol controls and a no-match case. Show actual returned year/make/model/trim and powertrain evidence, not merely category labels. Record effective price/location filters. No silent relaxation or invented inventory.

TASK 2 — Claude rendering without ChatGPT regression
Inspect current widget registration, emitted resource metadata, HTML/bootstrap URL, CSP, MIME type and host bridge. Diagnostic leads to verify:
1. A plain application origin in resource _meta.ui.domain can cause Claude to fetch the resource successfully but fail to mount it. Test whether omitting that optional field resolves this while preserving the working namespaced openai/widgetDomain and OpenAI output-template behavior. These fields are not interchangeable.
2. Search for PUBLIC_BASE_URL, MCP_SERVER_URL, registerWidgetResource and Skybridge's serverUrl generation. A known failure pattern is missing forwarded-host/origin headers causing localhost:3000 or an incorrect serving origin to enter widget metadata/HTML. Check whether the PUBLIC_BASE_URL fallback to MCP_SERVER_URL already exists and what each value actually contains. Use the correct external origin for each environment; never leak preview or localhost URLs into production resources.
3. Separate server defects from cached connector metadata/resources. Verify the running build, tools/list and resources/read before treating a stale client view as fresh evidence.

Use current official MCP Apps/host documentation if needed. Keep changes minimal and durable; avoid transient node_modules edits, broad dependency upgrades or CSP weakening.

Acceptance: capture before/after tools/list and resource metadata/HTML URL differences; keep tool names, descriptions, schemas and annotations unchanged. Verify ChatGPT and Claude web/desktop/iOS rendering, photos, links and existing interactive actions where accessible. Preserve useful text fallback. Mark unavailable host tests NOT TESTED and provide exact manual steps—unit tests/schema hashes do not prove host rendering.

Return confirmed causes, coverage added, minimal changes, evidence and remaining risks. Keep both fixes independently reviewable. Stop before production deployment; identify any serving-domain or published-configuration change requiring review.
