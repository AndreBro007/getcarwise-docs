# CarClever 3-App Portfolio — Current Status 2026-09-12

## Purpose

This is the current-status companion to the older `carclever-widget/CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md`. The older document contains valuable historical analysis from August and should not be read as the current submission state without this update.

## Current portfolio snapshot

| Product / app surface | Hosting | Current role | OpenAI | Anthropic |
|---|---|---|---|---|
| **CarClever / legacy Fractal app** | Fractal production endpoint | Legacy/fallback historical surface | Historical published/submission lineage; not today's V2 submission | Historical Claude submission path; not today's active V2 update |
| **CarClever - New & Used Cars** | Fractal Sky | Separate all-inventory Fractal product/history | Historical OpenAI review/submission lineage | Not the active Anthropic Find My Car submission |
| **CarClever - Find My Car** | Vercel, repo `AndreBro007/carclever-find-my-car` | **Primary active release and current cross-platform submission** | **V2 submitted 2026-09-12 — REVIEW** | **V2 production cutover + listing update 2026-09-12 — IN REVIEW** |

The strategic center of gravity is now **Find My Car V2**, not the Fractal apps.

## Find My Car release lineage inside the active app

Do not confuse the three product surfaces above with Find My Car's internal release branches:

- **V1:** `main`, preserved at `e7c8634...`; historical submitted/production baseline and rollback point. It is no longer the behavior deliberately served behind the Anthropic submitted URL after the Sep 12 controlled cutover.
- **V2:** `release/v2`, exact current submission SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`; active submitted release on both platforms.
- **V3:** paused at `v3.1-3.3/card-first-check-vehicle`, commit `4032feb`; no merge, promotion or submission action authorized while V2 reviews are active.

## OpenAI current state

- Production Vercel project: `ccfmc-dev-v2`.
- MCP URL: `https://carclever-oai.getcarwise.app/mcp`.
- Exact release: V2 `b8b07d8`.
- Domain verification: complete.
- Final Scan Tools: passed with V2 schema, no legacy `goals`, correct custom widget origin/CSP and tool annotations.
- Final positive smoke: normal inventory search, exact VIN Buyer Check, self-contained listing-presence/availability all passed on the custom domain.
- Submission: `CarClever - Find My Car`, version 1.0.0.
- Status: **REVIEW** as of 2026-09-12.

## Anthropic current state

- Existing Vercel project: `carclever-find-my-car`.
- Existing submitted MCP URL retained: `https://carclever-find-my-car.vercel.app/mcp`.
- Production manually promoted from `release/v2` exact SHA `b8b07d8`.
- Production deployment: READY.
- Anthropic server listing: existing `CarClever - Find My Car`, slug unchanged.
- Sync/Rescan from server performed.
- Public description updated to final V2 marketing copy.
- Update saved successfully.
- Status: **IN REVIEW**, Updated `just now` at submission confirmation on 2026-09-12.

## Claude-specific pending item

The first Claude connector attempt after the backend cutover still showed stale V1 tool metadata (`goals`) and an `Unable to reach` banner even though:

- Claude tool discovery could see the connector;
- the V2 Test connector exposed the correct V2 schema; and
- direct GET to the submitted MCP hostname returned the expected JSON-RPC `Method not allowed` response.

Treat this as a **Claude connector/tool-metadata cache refresh issue pending retest**, not proof of server unavailability. The next session should clear/recreate connector state and confirm the base connector now advertises V2 fields before changing code.

## Current strategic decision

1. **Find My Car V2 is the active cross-platform bet.** Both OpenAI and Anthropic now review the same V2 codebase through platform-specific production origins.
2. **Do not merge V2 into main merely to make the submissions work.** The Sep 12 Anthropic cutover proved V2 can be deliberately promoted without changing main.
3. **Freeze V2 during review** unless a platform requests a correction or a concrete reproducible defect appears.
4. **Keep V3 paused.** Do not let V3 work contaminate the submission/review window.
5. The older Fractal portfolio remains historical/fallback context; no new Fractal migration/submission action was authorized in this session.

## Immediate next actions

- Claude: reset connector/cache, verify V2 schema, run CR-V baseline and exact-VIN Buyer Check.
- Vercel: confirm long-term production-branch/release behavior on the Anthropic project so a future V1 `main` push cannot silently supersede the manual V2 production promotion.
- Reviews: monitor OpenAI and Anthropic; no proactive code changes while both are in review.

## Related records

- `CURRENT_V2_STATE_20260909.md`
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`
- `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`
- `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`
- `AUDIT_CARCLEVER_DUAL_PLATFORM_VERCEL_FEASIBILITY_20260911.md`
- historical portfolio analysis: `carclever-widget/CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md`
