# CarClever V2 Current State — updated 2026-09-12

## Purpose

This is the current operational record for the amended V2 shared MCP contract, implementation, validation, deployment, and platform-review state. It supersedes stale “proposed,” “not yet coded,” V1-production, and pre-cutover status statements in older documents while preserving those documents as historical records.

## Current source of truth

- Repository: `AndreBro007/carclever-find-my-car` (read-only to ChatGPT Business/Strategy lane).
- Release branch: `release/v2`.
- Current V2 tip / exact promoted SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.
- Parent OpenAI verification-endpoint commit: `abb933cc47aa0f093a7f955ac2ae0507ec7f9b08`.
- Main remains V1 at `e7c8634fdd631c7bb05c83c02daeb1ab7f7bbb6`; V2 was not merged into main.
- V3 remains paused at `v3.1-3.3/card-first-check-vehicle`, commit `4032feb`; do not merge or resume as part of V2 release work.

## Platform production state

### OpenAI / ChatGPT

- Vercel project: `ccfmc-dev-v2`.
- Submitted MCP URL: `https://carclever-oai.getcarwise.app/mcp`.
- Production widget origin: `https://carclever-oai.getcarwise.app` via project-specific `NEXT_PUBLIC_WIDGET_ORIGIN`.
- Domain verification and final Scan Tools checks passed.
- OpenAI V2 resubmission completed 2026-09-12.
- Current OpenAI status: **REVIEW**.
- Submission record: `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`.

### Anthropic / Claude

- Existing submitted MCP URL retained: `https://carclever-find-my-car.vercel.app/mcp`.
- Existing Vercel project `carclever-find-my-car` was deliberately promoted to V2 from `release/v2` at exact SHA `b8b07d8` without merging V2 into main.
- Vercel production deployment is READY and records `release/v2`, exact SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`, target `production`.
- Anthropic Edit Server flow used **Sync/Rescan from server** and public listing description was updated to the final V2 marketing description used for OpenAI.
- Anthropic submission update was saved 2026-09-12; directory screen confirmed **In review** and **Updated: just now**.
- Existing connector initially exposed a stale V1 tool snapshot after production cutover (`goals` still visible) and showed “Unable to reach” despite the endpoint being reachable. Direct browser GET to `/mcp` returned the expected JSON-RPC `Method not allowed`, proving the route/hostname was alive. This is currently treated as a Claude connector/tool-metadata cache issue pending a fresh connector/cache reset and retest.
- Submission record: `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`.

## Implemented amended contract

The public V2 input contract uses:

- `vehicleNeeds` instead of legacy `goals`;
- `electrificationTypes`: `hybrid | plug_in_hybrid | electric`;
- `electrificationRequirement`: `required | preferred`;
- required/preferred electrification semantics backed by bounded evidence handling;
- practical-needs/model-resolution guidance;
- direct-filter anti-invention guardrail;
- transmission anti-invention wording;
- `vehicleType` narrowed so it does not duplicate broad `bodyType` intent;
- exact-VIN behavior that never substitutes another vehicle;
- unchanged two-tool public set: `find_matching_vehicle`, `resolve_dealer_url`.

## Validation completed

- Extensive V2 regression and cross-host testing was completed before platform submission; detailed historical cases remain in the `TEST_CARCLEVER_*` documents.
- Final OpenAI production-origin smoke tests passed on the new custom domain for normal inventory search, exact-VIN Buyer Check, and self-contained listing-presence/availability lookup.
- Negative non-inventory prompts were included in the OpenAI submission baseline.
- OpenAI final tool scan confirmed V2 fields (`vehicleNeeds`, electrification fields), no legacy `goals`, read-only/destructive/open-world annotations, and custom widget origin/CSP metadata.
- Anthropic production infrastructure identity is verified: exact V2 SHA is READY in Production and the existing MCP route responds correctly at the submitted hostname.
- Remaining Anthropic validation is host-cache/tool-refresh testing after the saved submission update. This is not evidence of a server outage.

## Known follow-up / gates

1. **Claude cache reset + fresh connector retest:** confirm the base `CarClever - Find My Car` connector now advertises V2 fields (`vehicleNeeds`, electrification fields) and no `goals`; then run the CR-V baseline and exact-VIN Buyer Check.
2. **Do not alter V2 code during either platform review** unless OpenAI/Anthropic requests a correction or a concrete regression is reproduced.
3. **Confirm long-term Vercel production branch/release behavior for the Anthropic project** so a future V1 `main` push cannot silently replace the manually promoted V2 production release.
4. Keep main/V1 untouched and V3 paused.
5. Stale draft PRs #1/#2 remain housekeeping only; do not merge them.

## Current documentation index

- OpenAI submission: `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`
- Anthropic submission update: `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`
- Release validation ledger: `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`
- Current app portfolio: `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md`
- Dual-platform deployment feasibility/history: `AUDIT_CARCLEVER_DUAL_PLATFORM_VERCEL_FEASIBILITY_20260911.md`
- Anthropic compliance audit (historical pre-cutover): `AUDIT_V2_ANTHROPIC_SUBMISSION_COMPLIANCE_20260910.md`
- OpenAI reconciliation/history: `RECONCILIATION_CARCLEVER_OPENAI_V2_SUBMISSION_20260911.md`
- Platform-domain naming decision: `DECISION_CARCLEVER_PLATFORM_DOMAIN_NAMING_20260911.md`

## Current release posture

V2 is now the active submitted release on **both OpenAI and Anthropic**, using separate production origins but the same tested `release/v2` codebase. Both platform submissions are in review. The code/release lane is frozen except for review-requested corrections or evidence-backed defects. V1/main remains preserved as rollback/history rather than the active submitted behavior behind the Anthropic URL.