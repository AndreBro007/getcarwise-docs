# CarClever Dual-Platform V2 Session Closeout — 2026-09-12

## Session outcome

This session completed the controlled V2 submission/update path for both OpenAI and Anthropic using the same tested `release/v2` codebase while keeping platform-specific production origins separate.

## Frozen release identity

- Repo: `AndreBro007/carclever-find-my-car`
- Branch: `release/v2`
- Exact release/submission SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`
- V1/main remains untouched at `e7c8634fdd631c7bb05c83c02daeb1ab7f7bbb6`
- V3 remains paused at `v3.1-3.3/card-first-check-vehicle`, commit `4032feb`

## OpenAI — complete for review handoff

- Vercel project: `ccfmc-dev-v2`
- MCP: `https://carclever-oai.getcarwise.app/mcp`
- Domain verification complete.
- Final Scan Tools passed with V2 contract, no legacy `goals`, correct widget origin/CSP and annotations.
- Final production-origin smoke passed for normal search, exact-VIN Buyer Check and self-contained listing-presence/availability.
- V2 resubmitted 2026-09-12.
- Current status: **REVIEW**.
- Review freeze applies.

## Anthropic — production cutover and submission update complete

- Existing submitted MCP retained: `https://carclever-find-my-car.vercel.app/mcp`
- Existing Vercel project retained: `carclever-find-my-car`
- Exact V2 SHA `b8b07d8` manually promoted from `release/v2` to Production.
- Verified Vercel deployment `dpl_9vP17yqXx5fdfV2uTWfAenvfYFD2`: READY, production, exact V2 SHA.
- Direct MCP browser probe returned expected JSON-RPC `Method not allowed`, confirming route reachability.
- Anthropic Edit Server → Sync/Rescan completed; portal reported 2 tools.
- Public Description updated to final V2 marketing copy.
- Existing form answers/name/slug/branding retained.
- Update saved successfully.
- Current status: **IN REVIEW**; submission page confirmed `Updated: just now` after save.

## Claude cache observation — open test, not a release blocker

The first recreated Claude connector after the backend cutover still exposed stale V1 base-tool metadata (`goals`) and displayed `Unable to reach`, while the endpoint was independently reachable and the separate V2 Test connector exposed the correct V2 schema.

Current classification: **Claude connector/tool-metadata cache mismatch pending retest**. No code change was made. Historical cross-host rendering protection (`_meta.ui.domain` omitted) remains present in V2.

## Next-session test — first action after cache reset

1. Confirm base `CarClever - Find My Car` now exposes V2 fields (`vehicleNeeds`, `electrificationTypes`, `electrificationRequirement`) and no `goals`.
2. Run: `Find a used Honda CR-V under $25,000 with less than 60,000 miles near 90210.`
3. Run: `Check VIN 4T1DAACK6SU582551 for red flags before I buy it.`
4. Only investigate code if the refreshed connector still shows a reproducible defect.

Live VIN/listing status can change and is not itself a regression.

## One infrastructure follow-up not to lose

Confirm the Anthropic Vercel project's long-term Production branch/release behavior. The Sep 12 manual promotion is correct now, but a future V1 `main` push must not be allowed to silently replace the V2 production deployment behind the submitted Anthropic URL.

## Documentation reconciled this session

Updated/created current records:

- `CURRENT_V2_STATE_20260909.md` — updated to Sep 12 dual-platform state.
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md` — updated with final OpenAI + Anthropic release/submission evidence.
- `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md` — created.
- `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md` — created as current companion to the older historical three-app analysis.
- `README.md` — updated current-status index.
- `carclever-widget/ADMIN_RECORD_ANTHROPIC_SUBMISSIONS.md` — created.
- `carclever-widget/CARCLEVER_3_APPS_CURRENT_STATUS_20260912.md` — created current portfolio pointer.

Existing OpenAI records created earlier on Sep 12 remain current.

## Session-close posture

- OpenAI: **REVIEW**.
- Anthropic: **IN REVIEW**.
- V2 code: frozen.
- V1/main: preserved.
- V3: paused.
- No new strategic decision is pending.
- Remaining operational items: Claude cache/schema retest and Anthropic Vercel production-branch safety confirmation.
