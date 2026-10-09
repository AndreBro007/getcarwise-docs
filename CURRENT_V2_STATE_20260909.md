# CarClever V2 Current State — updated 2026-09-16 (Oct 9 update below)

## UPDATE — Oct 9, 2026 (Claude, Engineering lane): supersedes the statuses below where they differ

- **Anthropic:** APPROVED and PUBLISHED as a Community connector (André, Oct 9). The listing URL is still `carclever-find-my-car.vercel.app/mcp`; the portal’s Change URL button does not allow the change, so Anthropic must change it. Full record: `carclever-widget/ADMIN_RECORD_ANTHROPIC_SUBMISSIONS.md`.
- **OpenAI:** the new app is published (Version 1.0.0, RELEASED; `DECISIONS.md` `SYS-20260924-007`) with no review pending (André’s Oct 9 screenshot of the plugin list).
- **Project name:** the OpenAI Vercel project `ccfmc-dev-v2` was renamed `carclever-openai` on Sep 24 (older mentions below are historical).
- **What each domain serves** (Vercel API and raw MCP `serverInfo.version`, Oct 9): `carclever-oai` and `carclever-meta` serve `cac7028` (`release/v2` tip); `carclever-anth`, `carclever` and `carclever-find-my-car.vercel.app` serve the pinned `dd68e15`. The only code difference is one 24-line disclosure note in `route.ts` (`SYS-20260924-008`).
- **Freeze rule:** the “freeze V2 / no further proactive code changes while both remain in review” rule below no longer applies to Anthropic or OpenAI. Changes to the published URLs are public changes under VERCEL PRODUCTION SAFETY.
- **Current work and status document:** a catalogue continuity build on a separate branch, not promoted (`RETURN_CLAUDE_EDMUNDS_CATALOGUE_SPIKE_INTERIM_20261008.md`). The current status document is `carclever-widget/CARCLEVER_3_APPS_CURRENT_STATUS_20260912.md` (read its Oct 2–9 section first).

## Purpose

This is the current operational record for the amended V2 shared MCP contract, implementation, validation, deployment, and platform-review state. It supersedes stale “proposed,” “not yet coded,” V1-production, and pre-cutover status statements in older documents while preserving those documents as historical records.

## Current source of truth

- Repository: `AndreBro007/carclever-find-my-car` (read-only to ChatGPT Business/Strategy lane).
- Release branch: `release/v2`.
- Exact approved V2 production/submission SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.
- Parent OpenAI verification-endpoint commit: `abb933cc47aa0f093a7f955ac2ae0507ec7f9b08`.
- `main` remains the historical V1 lineage and is not the intentionally served V2 production line.
- V3 remains paused at `v3.1-3.3/card-first-check-vehicle`, commit `4032feb`; do not merge or resume as part of V2 release work.

## Platform production state

### OpenAI / ChatGPT

- Vercel project: `ccfmc-dev-v2`.
- Immutable Vercel project ID: `prj_EJRR8xftf6TEIA3QS7jFXjBPr2aX`.
- Submitted MCP URL: `https://carclever-oai.getcarwise.app/mcp`.
- Production widget origin: `https://carclever-oai.getcarwise.app` via project-specific `NEXT_PUBLIC_WIDGET_ORIGIN`.
- Exact production release: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.
- Domain verification and final Scan Tools checks passed.
- OpenAI V2 resubmission completed 2026-09-12.
- Current OpenAI status: **REVIEW**.
- Production branch tracking: `release/v2`.
- **Auto-assign Custom Production Domains: Disabled** as of 2026-09-16; Production custom-domain movement now requires deliberate manual promotion.
- Submission record: `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`.

### Anthropic / Claude

- Vercel project: `carclever-find-my-car`.
- Immutable Vercel project ID: `prj_AGtLT6n36FwfIida35UUKCYIB3zS`.
- Exact approved production release: `b8b07d8542f5d3f2a12e00433e089dde28ae5792` from `release/v2`.
- Approved production deployment: `dpl_9vP17yqXx5fdfV2uTWfAenvfYFD2`, READY, target `production`.
- New branded production MCP endpoint: `https://carclever-anth.getcarwise.app/mcp`.
- New branded hostname is Vercel-valid, HTTPS-valid, reaches the MCP transport, resolves to exact approved V2 SHA, and has passed a successful functional `CarClever - Find My Car` MCP-client test.
- Existing MCP currently recorded in the pending Anthropic listing remains `https://carclever-find-my-car.vercel.app/mcp` until support confirms the replacement.
- Existing migration aliases remain live, including `https://carclever.getcarwise.app/mcp` and the submitted Vercel hostname.
- Anthropic submission update saved 2026-09-12 and remains **IN REVIEW**.
- On 2026-09-16 André emailed Marco/Anthropic support requesting replacement of the pending listing MCP URL with `https://carclever-anth.getcarwise.app/mcp`; the support-side URL change is **pending confirmation**.
- **Auto-assign Custom Production Domains: Disabled**; Production custom-domain movement now requires deliberate manual promotion.
- Submission record: `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`.

## 2026-09-16 Anthropic production incident — resolved

A Sep 14 push to `main` silently became the active Anthropic production deployment because Vercel's Production environment had **Auto-assign Custom Production Domains** enabled.

Git history showed that this was an older `main` lineage deployment, not the approved V2 release plus a harmless documentation-only change.

Recovery and prevention completed:

1. manually promoted exact approved V2 SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792` back to Anthropic Production;
2. verified active production aliases on the correct V2 deployment;
3. disabled **Auto-assign Custom Production Domains** on Anthropic and saved the setting;
4. proactively disabled the same setting on OpenAI after confirming OpenAI Production tracks `release/v2`.

The source of the Sep 14 documentation/test-log commit itself remains unidentified and should not be attributed to a person or AI without evidence.

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
- Final OpenAI production-origin smoke tests passed on the custom domain for normal inventory search, exact-VIN Buyer Check, and self-contained listing-presence/availability lookup.
- Negative non-inventory prompts were included in the OpenAI submission baseline.
- OpenAI final tool scan confirmed V2 fields (`vehicleNeeds`, electrification fields), no legacy `goals`, read-only/destructive/open-world annotations, and custom widget origin/CSP metadata.
- Anthropic new branded hostname `carclever-anth.getcarwise.app` passed Vercel configuration, TLS/HTTPS, MCP transport reachability, exact-production-SHA validation, and a functional MCP-client test.
- The older Sep 12 Claude stale-metadata/cache symptom is not an active server defect unless it can still be reproduced against the current branded V2 endpoint.

## Current production policy

Both platform production projects now use manual production-domain promotion.

Standing rules:

1. Git pushes may build deployments, but must not silently take over branded production domains.
2. Before **Promote to Production**, verify intended branch and exact SHA.
3. After promotion, verify branded MCP endpoint and exact production SHA.
4. Do not use routine documentation/test-log pushes as release mechanisms.
5. Do not merge V2 into `main` merely to simplify platform deployment.

## Known follow-up / gates

1. **Anthropic support-side URL replacement:** wait for Marco/Anthropic to confirm the pending listing now uses `https://carclever-anth.getcarwise.app/mcp` or provide follow-up validation instructions.
2. **Do not alter V2 code during either platform review** unless OpenAI/Anthropic requests a correction or a concrete regression is reproduced.
3. Keep old Anthropic aliases live until the support-side URL transition is confirmed and no dependency remains.
4. Keep `main` untouched as historical/rollback lineage and V3 paused.
5. Stale draft PRs #1/#2 remain housekeeping only; do not merge them.
6. Defer Vercel display-name cleanup until submission transitions stabilize:
   - `ccfmc-dev-v2` -> `carclever-openai`;
   - `carclever-find-my-car` -> `carclever-anthropic`.
7. Later audit old Vercel projects and stale GitHub branches before any retirement/deletion action; verify dependencies first.

## Current documentation index

- OpenAI submission: `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`
- Anthropic submission update: `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`
- Release validation ledger: `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`
- Current app portfolio: `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md`
- Anthropic URL/recovery update: `UPDATE_ANTHROPIC_DNS_VERIFICATION_AND_RECOVERY_20260916.md`
- Vercel/GitHub housekeeping plan: `PLAN_CARCLEVER_VERCEL_NAMING_AND_RELEASE_HYGIENE_20260916.md`
- Dual-platform deployment feasibility/history: `AUDIT_CARCLEVER_DUAL_PLATFORM_VERCEL_FEASIBILITY_20260911.md`
- Anthropic compliance audit (historical pre-cutover): `AUDIT_V2_ANTHROPIC_SUBMISSION_COMPLIANCE_20260910.md`
- OpenAI reconciliation/history: `RECONCILIATION_CARCLEVER_OPENAI_V2_SUBMISSION_20260911.md`
- Platform-domain naming decision: `DECISION_CARCLEVER_PLATFORM_DOMAIN_NAMING_20260911.md`

## Current release posture

V2 is the active submitted release on **both OpenAI and Anthropic**, using separate platform production origins but the same tested `release/v2` codebase and exact production SHA. Both platform submissions remain in review. OpenAI already uses its branded submitted MCP URL; Anthropic's new branded endpoint is live and tested while the pending listing's support-side URL replacement awaits confirmation. Production-domain promotion is manual on both Vercel projects. The code/release lane remains frozen except for review-requested corrections or evidence-backed defects.