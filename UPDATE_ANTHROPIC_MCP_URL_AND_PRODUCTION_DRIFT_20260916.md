# Anthropic MCP URL Update and Production Drift — 2026-09-16

**Owner lane:** ChatGPT — Business/Strategy  
**Status:** FACTUAL UPDATE — Anthropic URL-change process gate cleared; production-safety gate BLOCKED pending Engineering restoration and verification

## Executive conclusion

Anthropic support has now confirmed that the MCP URL for the currently pending CarClever listing should be updated **while review is still pending** rather than waiting for approval. This clears the previous process uncertainty around whether an in-review URL change would be disruptive.

It does **not** change the confirmed GetCarWise architecture decision from 2026-09-11: OpenAI and Anthropic use the **same CarClever V2 code/release**, but with **separate stable platform production origins**.

The confirmed naming decision remains:

- OpenAI: `https://carclever-oai.getcarwise.app/mcp`
- Intended Anthropic branded origin: `https://carclever-anth.getcarwise.app/mcp`

The current Anthropic submission still records:

- `https://carclever-find-my-car.vercel.app/mcp`

A live Vercel inspection on 2026-09-16 found a material release-control regression on the Anthropic production project: the deliberate 2026-09-12 V2 production promotion at exact SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792` was subsequently replaced by a 2026-09-14 automatic production deployment from `main` at SHA `1514ab42dd2d4afe20109f02c9cc3930a3ee0789`.

A GitHub compare confirms that this Sep 14 `main` head is on the V1/main lineage and is 101 commits behind the V2 release head, rather than being V2 plus a harmless documentation-only change. This is the exact production-overwrite risk previously recorded in the Sep 12 release closeout and validation ledger.

Therefore, **do not send Anthropic a replacement MCP URL until Engineering restores and verifies the correct V2 production release behind the Anthropic project.**

## New Anthropic support guidance

Andre received direct support guidance from Marco at Anthropic confirming:

1. The April submission made through the old form is not in Anthropic's current review queue and requires no retirement action.
2. Two submissions for the same connector do not conflict; the older entry is treated as superseded.
3. The MCP URL should be updated now while the current listing is pending. Anthropic support stated that a pending-listing URL update has no review-cost penalty.
4. Once a listing is approved, the recommended sequence is to **publish first**, then make any later edits. Editing after approval but before Publish would send the listing back to review.

This guidance clears the **review-process/timing gate** for a pending MCP URL update.

## Existing confirmed domain architecture

The 2026-09-11 decision `DECISION_CARCLEVER_PLATFORM_DOMAIN_NAMING_20260911.md` is marked **CONFIRMED BY ANDRÉ** and sets the platform-separated naming convention:

- OpenAI: `carclever-oai.getcarwise.app`
- Anthropic: `carclever-anth.getcarwise.app`

The rationale is one product and one tested release line, but separate stable front doors so OpenAI and Anthropic review/deployment lifecycles are not coupled.

The Sep 12 submission records follow this architecture:

- OpenAI was submitted on `https://carclever-oai.getcarwise.app/mcp` at exact V2 SHA `b8b07d8...`.
- Anthropic retained `https://carclever-find-my-car.vercel.app/mcp` while the same exact V2 SHA was manually promoted into the Anthropic Vercel project.

There is no later documented confirmed decision that both platforms should share one identical MCP URL.

## Existing neutral Anthropic alias

The Anthropic Vercel project currently has both of these domains attached:

- `carclever-find-my-car.vercel.app`
- `carclever.getcarwise.app`

`carclever.getcarwise.app` is an older neutral branded alias associated with the Anthropic/legacy project history. It is **not** OpenAI's current submitted URL, so using it for Anthropic would not place OpenAI and Anthropic on the same URL.

It is also not the Sep 11 confirmed future Anthropic naming target. Choosing `carclever.getcarwise.app` as the permanent Anthropic endpoint would therefore be a **new André decision that supersedes the Sep 11 naming decision**.

At the time of inspection, `carclever-anth.getcarwise.app` is not attached to the Anthropic Vercel project.

## Live production drift found 2026-09-16

### Anthropic project

Project: `carclever-find-my-car`

Expected submitted/reviewed V2 release after Sep 12 promotion:

- Branch: `release/v2`
- Exact SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`

Current production deployment observed on Sep 16:

- Deployment created: 2026-09-14
- Branch: `main`
- SHA: `1514ab42dd2d4afe20109f02c9cc3930a3ee0789`
- Commit message: `Sep 14: add Test Run Log entry for old-CarClever verification round`

GitHub comparison:

- V2 and current main are diverged.
- Current main is ahead by 1 commit on its own lineage and **101 commits behind** V2.
- The shared merge-base is on the preserved V1/main line.

This means the Anthropic production project has materially drifted back to the V1/main release line.

### OpenAI project

Project: `ccfmc-dev-v2`

Current production remains the exact V2 SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792` behind `carclever-oai.getcarwise.app`.

The Sep 14 `main` build appeared only as a non-production preview in the OpenAI V2 project, so the OpenAI submitted endpoint has not suffered the same production overwrite.

## Decision implications

### What has changed

- Anthropic's process gate for changing a pending MCP URL is now clear: **send the change while pending**.
- A previously documented operational risk has become an actual production incident: a V1 `main` push replaced the manually promoted Anthropic V2 production deployment.

### What has not changed

- The confirmed architecture remains same V2 code/release, separate platform production origins.
- There is no confirmed decision to share `carclever-oai.getcarwise.app` between OpenAI and Anthropic.
- The intended branded Anthropic origin remains `carclever-anth.getcarwise.app` unless André explicitly supersedes that naming decision.

## Required Engineering gate before sending the new URL

Claude/Engineering owns these actions on `AndreBro007/carclever-find-my-car` and Vercel:

1. Restore the Anthropic production project to the approved V2 release and verify the exact deployed SHA.
2. Correct the Vercel production-branch/release behavior so a future V1 `main` push cannot silently replace the manually promoted V2 production release.
3. If retaining the confirmed Sep 11 naming decision, attach/configure `carclever-anth.getcarwise.app` to the Anthropic production project.
4. Verify the chosen branded `/mcp` endpoint is reachable and serves the V2 contract, including current V2 schema markers such as `vehicleNeeds` and the V2 electrification fields rather than the legacy V1 `goals` contract.
5. Report the exact verified production URL and SHA before Andre sends the replacement endpoint to Anthropic.

No application-code or deployment changes are authorized or performed by ChatGPT in this record.

## Recommended Anthropic URL after Engineering verification

If the existing confirmed naming decision is retained:

`https://carclever-anth.getcarwise.app/mcp`

Do **not** use `https://carclever-oai.getcarwise.app/mcp` for Anthropic unless André explicitly decides to abandon the separate-platform-origin architecture.

Do **not** send `https://carclever.getcarwise.app/mcp` as the permanent endpoint merely because it is already attached; using that older neutral alias would be a new naming decision and it currently points at the drifted Anthropic production project until Engineering restores V2.

## Source records reviewed

- `DECISION_CARCLEVER_PLATFORM_DOMAIN_NAMING_20260911.md`
- `AUDIT_CARCLEVER_DUAL_PLATFORM_VERCEL_FEASIBILITY_20260911.md`
- `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`
- `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`
- `SESSION_CARCLEVER_DUAL_PLATFORM_CLOSEOUT_20260912.md`
- `CURRENT_V2_STATE_20260909.md` (updated through Sep 12)
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`
- `ADMIN_RECORD_ANTHROPIC_SUBMISSIONS.md`
- `TEST_LOG_OLDCARCLEVER_20260914.md`
- Full dynamically listed root of `getcarwise-docs` as of 2026-09-16
- Live Vercel project/deployment inspection on 2026-09-16
- Read-only GitHub compare of V2 SHA `b8b07d8...` to current `main` SHA `1514ab42...`
- Direct Anthropic support email supplied by André on 2026-09-16
