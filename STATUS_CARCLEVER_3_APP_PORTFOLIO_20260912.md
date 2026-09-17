# CarClever 3-App Portfolio — Current Status updated 2026-09-16

## Purpose

This is the current-status companion to the older `carclever-widget/CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md`. The older document contains valuable historical analysis from August and should not be read as the current submission state without this update.

## Current portfolio snapshot

| Product / app surface | Hosting | Current role | OpenAI | Anthropic |
|---|---|---|---|---|
| **CarClever / legacy Fractal app** | Fractal production endpoint | Legacy/fallback historical surface | Historical published/submission lineage; not today's V2 submission | Historical Claude submission path; not today's active V2 update |
| **CarClever - New & Used Cars** | Fractal Sky | Separate all-inventory Fractal product/history | Historical OpenAI review/submission lineage | Not the active Anthropic Find My Car submission |
| **CarClever - Find My Car** | Vercel, repo `AndreBro007/carclever-find-my-car` | **Primary active release and current cross-platform submission** | **V2 submitted 2026-09-12 — REVIEW** | **V2 in review; new branded MCP live; support-side URL replacement requested 2026-09-16** |

The strategic center of gravity is now **Find My Car V2**, not the Fractal apps.

## Find My Car release lineage inside the active app

Do not confuse the three product surfaces above with Find My Car's internal release branches:

- **V1/main:** preserved as historical baseline/rollback lineage; no longer the deliberately served cross-platform V2 release.
- **V2/release/v2:** exact current submission SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`; active submitted release on both platforms.
- **V3:** paused at `v3.1-3.3/card-first-check-vehicle`, commit `4032feb`; no merge, promotion or submission action authorized while V2 reviews are active.

## OpenAI current state

- Production Vercel project: `ccfmc-dev-v2` (project ID `prj_EJRR8xftf6TEIA3QS7jFXjBPr2aX`).
- MCP URL: `https://carclever-oai.getcarwise.app/mcp`.
- Reviewed/submitted release: V2 `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.
- **Currently live in production (2026-09-17):** `dd68e15` — the Edmunds CJ→Impact affiliate-link migration, confirmed via raw MCP `initialize` call (`serverInfo.version: "dd68e15"`) and a real end-to-end ChatGPT tool call + click-through to a live Edmunds listing.
- Domain verification: complete.
- Final Scan Tools: passed with V2 schema, no legacy `goals`, correct custom widget origin/CSP and tool annotations.
- Final positive smoke: normal inventory search, exact VIN Buyer Check, self-contained listing-presence/availability all passed on the custom domain.
- Submission: `CarClever - Find My Car`, version 1.0.0.
- Status: **REVIEW**.
- Production branch tracking: `release/v2`.
- **Auto-assign Custom Production Domains: currently ENABLED (temporary, since evening of 2026-09-17)** — re-enabled deliberately to work around a confirmed Vercel behavior where domain reassignment silently fails on manual promotion while this setting is off (see `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md` for full detail). André intends to disable it again to restore the Sep 16 incident-prevention posture — **verify the live setting directly, do not assume from this document.**

## Anthropic current state

- Vercel project: `carclever-find-my-car` (project ID `prj_AGtLT6n36FwfIida35UUKCYIB3zS`).
- Reviewed/submitted release: exact V2 SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`, source `release/v2`.
- **Currently live in production (2026-09-17):** `dd68e15` — the Edmunds CJ→Impact affiliate-link migration, confirmed via raw MCP `initialize` call (`serverInfo.version: "dd68e15"`) and a real end-to-end Claude tool call + click-through to a live Edmunds listing.
- New branded production MCP: `https://carclever-anth.getcarwise.app/mcp`.
- New branded domain is Vercel-valid, HTTPS-valid, resolves to the current live production deployment, and has passed a functional `CarClever - Find My Car` MCP-client test.
- Existing MCP currently recorded by Anthropic remains `https://carclever-find-my-car.vercel.app/mcp` until Anthropic support confirms the replacement.
- Existing aliases remain live during the transition, including `https://carclever.getcarwise.app/mcp` and the submitted Vercel hostname.
- Anthropic server listing remains `CarClever - Find My Car`, slug unchanged.
- Status: **IN REVIEW / SUPPORT-SIDE URL CHANGE PENDING CONFIRMATION**.
- **Auto-assign Custom Production Domains: currently ENABLED (temporary, since evening of 2026-09-17)** — same situation and same caveat as OpenAI above; verify the live setting directly.

## Vercel gotcha discovered and fixed, 2026-09-17

While attempting to promote `dd68e15` to production on both platforms, the dashboard's "Promote to Production" action correctly tagged the new deployment as Production (confirmed via the blue badge) but did **not** reassign either project's actual custom/default domains to it — domains kept serving the prior `b8b07d8` deployment. Confirmed via raw browser-console MCP calls (`x-vercel-cache: MISS` throughout) that this was **not** a caching issue, ruling out the previously-suspected Claude-connector caching bug entirely. Root cause: this is a real, non-obvious Vercel behavior — when **Auto-assign Custom Production Domains** is Disabled, "Promoted" and "domain-assigned/Current" are distinct states (per Vercel's own `/docs/deployments/promoting-a-deployment` documentation), and a preview-deployment promotion does not automatically reach the "Current" state in this configuration.

**Fix applied:** temporarily re-enabled Auto-assign Custom Production Domains on both projects, then re-ran "Promote to Production" on `dd68e15` — this time the domain reassignment worked correctly, confirmed via independent raw MCP calls from fresh browser tabs against both `ccfmc-dev-v2.vercel.app/mcp` and `carclever-anth.getcarwise.app/mcp`.

**Standing lesson:** while Auto-assign is disabled on either project, never trust the dashboard's Production badge alone as proof a release is live — always independently verify via a raw MCP `initialize` call checking `serverInfo.version`. Full investigation detail: `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md`.

## Sep 16 Anthropic support request

The pending Anthropic listing URL cannot be changed by André in the portal, which is why the support thread with Marco was opened.

Marco confirmed that the MCP URL may be changed while the current listing is pending and that the old April submission does not require separate retirement action.

On 2026-09-16 André emailed Marco asking Anthropic to replace the pending listing's MCP URL with:

`https://carclever-anth.getcarwise.app/mcp`

The email stated that the endpoint is live and tested, that the old endpoint will remain active during transition, and politely asked whether the current listing could be flagged with the review team given the submission history dating back to April.

Do not mark the new URL as stored in the Anthropic directory until support confirms the change.

## Sep 16 production incident and release-control outcome

A Sep 14 `main` push temporarily replaced the deliberately promoted Anthropic V2 production deployment because the Anthropic Vercel project's Production environment had **Auto-assign Custom Production Domains** enabled.

Recovery is complete:

1. restored exact approved V2 SHA `b8b07d8...` to Production;
2. verified the production aliases on the correct V2 deployment;
3. disabled **Auto-assign Custom Production Domains** on Anthropic;
4. proactively disabled the same auto-assignment behavior on OpenAI after confirming its tracked Production branch is `release/v2`.

The source of the Sep 14 documentation/test-log commit remains unidentified and should not be attributed without evidence. The operational release-control gap is closed by manual production promotion.

## Current strategic decision

1. **Find My Car V2 is the active cross-platform bet.** Both OpenAI and Anthropic use the same V2 codebase/release through platform-specific production origins.
2. **Do not merge V2 into main merely to make submissions work.** Platform production is controlled through deliberate Vercel promotion.
3. **Freeze V2 during review** unless a platform requests a correction or a concrete reproducible defect appears. **Deliberate, recorded exception (Sep 17), covers BOTH Anthropic and OpenAI reviews:** the Edmunds CJ→Impact affiliate-link swap in `lib/edmunds-cj.ts` was made and promoted to production on this branch despite the freeze — André's explicit decision, reasoning: (a) the Anthropic review may already be "in motion" via the open Marco/support MCP-URL-change thread, so this doesn't introduce a new disturbance where none existed; (b) end-of-September is a hard external deadline independent of review timelines, and applies equally to OpenAI's live Sep 12 resubmission; (c) the edit has zero schema/tool-description/CSP footprint (confirmed by code inspection — this app has no CSP config at all), making it structurally invisible to any automated review scan on either platform. Since both platforms build from the same shared branch/codebase (two separate Vercel projects — `carclever-find-my-car` for Anthropic, `ccfmc-dev-v2` for OpenAI — both auto-build every commit), the code change is unavoidably shared; production promotion was done on **both platforms together**, not staggered. **Now complete and confirmed live** on both platforms via independent raw MCP calls and real end-to-end tool-call/click-through tests, 2026-09-17. Full detail: `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md`.
4. **Keep V3 paused.** Do not let V3 work contaminate the submission/review window.
5. **Production promotion is manual on both platform projects.** Check branch/SHA before promotion, and independently verify the live endpoint's `serverInfo.version` via a raw MCP call after promotion — the dashboard's Production badge alone is not sufficient proof while Auto-assign Custom Production Domains is disabled (see the Vercel gotcha note above).
6. Keep Anthropic legacy aliases live until support confirms the new branded MCP URL is recorded.
7. Defer Vercel project display-name cleanup until the Anthropic URL transition is confirmed.
8. **Added 2026-09-17:** confirm Auto-assign Custom Production Domains has been toggled back to Disabled on both projects — it was temporarily re-enabled to fix the `dd68e15` promotion and must not be left on, or the Sep 14 silent-takeover risk reopens.

## Deferred infrastructure housekeeping

After the current submission transitions stabilize:

- proposed Vercel project display-name cleanup:
  - `ccfmc-dev-v2` -> `carclever-openai`;
  - `carclever-find-my-car` -> `carclever-anthropic`;
- audit remaining CarClever Vercel projects and classify active test infrastructure vs historical reference vs retirement candidates;
- re-audit stale GitHub branches before any bulk deletion;
- do not rename the shared `AndreBro007/carclever-find-my-car` GitHub repository as part of Vercel display-name cleanup.

See `PLAN_CARCLEVER_VERCEL_NAMING_AND_RELEASE_HYGIENE_20260916.md` for the controlled housekeeping plan.

## Immediate next actions

- Anthropic: wait for Marco/support to confirm the pending listing MCP URL has been replaced with `https://carclever-anth.getcarwise.app/mcp` or provide follow-up validation instructions.
- Reviews: monitor OpenAI and Anthropic; no further proactive code changes while both remain in review, beyond the completed Edmunds/Impact migration.
- Infrastructure: no rename/deletion cleanup until the Anthropic support-side URL change is confirmed.
- **Added 2026-09-17:** confirm Auto-assign Custom Production Domains toggled back to Disabled on both projects (see rule 8 above).
- **Added 2026-09-17:** André checking the Impact dashboard (`app.impact.com`) tomorrow for real click/action data on the test tracking links created during Sep 16-17 testing — monitoring only, not a blocker.

## Related records

- `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md` (Edmunds CJ→Impact migration, currently live promoted release, Vercel Auto-assign gotcha)
- `CURRENT_V2_STATE_20260909.md`
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`
- `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`
- `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`
- `UPDATE_ANTHROPIC_MCP_URL_AND_PRODUCTION_DRIFT_20260916.md`
- `UPDATE_ANTHROPIC_DNS_VERIFICATION_AND_RECOVERY_20260916.md`
- `PLAN_CARCLEVER_VERCEL_NAMING_AND_RELEASE_HYGIENE_20260916.md`
- `AUDIT_CARCLEVER_DUAL_PLATFORM_VERCEL_FEASIBILITY_20260911.md`
- historical portfolio analysis: `carclever-widget/CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md`
