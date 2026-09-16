# Anthropic MCP URL Update and Production Drift — 2026-09-16

**Owner lane:** ChatGPT — Business/Strategy  
**Status:** FACTUAL UPDATE — incident recovered; branded Anthropic MCP live and verified; support-side listing URL replacement pending confirmation

## Executive conclusion

Anthropic support confirmed that the MCP URL for the currently pending CarClever listing should be updated while review is still pending rather than waiting for approval.

The confirmed GetCarWise architecture remains:

- same CarClever V2 code/release on both platforms;
- separate platform production projects/front doors;
- OpenAI: `https://carclever-oai.getcarwise.app/mcp`;
- Anthropic: `https://carclever-anth.getcarwise.app/mcp`.

A Sep 14 automatic Anthropic production replacement was discovered on 2026-09-16, recovered, and its release-control cause corrected. The new Anthropic branded MCP endpoint has now been created and verified. André has sent the replacement URL to Marco/Anthropic support.

The only remaining Anthropic URL gate is external: **wait for support to confirm that the pending directory listing has been changed to the new branded URL.**

## Anthropic support guidance

Marco at Anthropic confirmed:

1. The April submission made through the old form is not in Anthropic's current review queue and requires no retirement action.
2. Multiple historical submissions for the same connector do not create a conflict; the older path is superseded by the current submission process.
3. The MCP URL may be updated now while the current listing is pending, without a review-cost penalty.
4. Once a listing is approved, the recommended later-edit sequence is to publish first and then edit; editing after approval but before Publish would return it to review.

## Confirmed domain architecture

The 2026-09-11 decision `DECISION_CARCLEVER_PLATFORM_DOMAIN_NAMING_20260911.md` is confirmed by André and sets:

- OpenAI: `carclever-oai.getcarwise.app`;
- Anthropic: `carclever-anth.getcarwise.app`.

The rationale is one product and one tested release line, but separate stable production origins so OpenAI and Anthropic review/deployment lifecycles are not silently coupled.

The older neutral Anthropic alias `carclever.getcarwise.app` remains available during migration but is not the final platform-specific naming target.

## Production drift found on 2026-09-16

### Anthropic project

Project: `carclever-find-my-car`  
Project ID: `prj_AGtLT6n36FwfIida35UUKCYIB3zS`

Expected V2 release after the Sep 12 controlled promotion:

- Branch: `release/v2`
- Exact SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`

Unexpected production deployment found on Sep 16:

- Deployment created Sep 14
- Branch: `main`
- SHA: `1514ab42dd2d4afe20109f02c9cc3930a3ee0789`
- Commit message: `Sep 14: add Test Run Log entry for old-CarClever verification round`

GitHub comparison established that this Sep 14 head was on the older `main` lineage, not V2 plus a harmless documentation-only change.

Root cause of the silent production takeover: Vercel Production had **Auto-assign Custom Production Domains** enabled.

The source of the Sep 14 documentation/test-log commit itself remains unidentified and should not be attributed to a person or AI without evidence.

## Recovery — COMPLETE

1. Exact approved V2 deployment at SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792` was manually promoted back to Anthropic Production.
2. Active Anthropic aliases were verified on production deployment `dpl_9vP17yqXx5fdfV2uTWfAenvfYFD2`.
3. André disabled **Auto-assign Custom Production Domains** on the Anthropic Production environment and saved the setting.
4. Vercel now states that Production deployments require manual promotion.

This closes the production-overwrite safety gate.

## New Anthropic branded endpoint — COMPLETE

New production MCP:

`https://carclever-anth.getcarwise.app/mcp`

Setup/validation:

- custom domain added to Vercel project `carclever-find-my-car`;
- Porkbun DNS added: `CNAME carclever-anth -> c6a2c23ef4265088.vercel-dns-017.com.`;
- Vercel: **Valid Configuration**;
- HTTPS/TLS: valid;
- direct GET `/mcp`: expected HTTP 405 JSON-RPC `Method not allowed` response;
- deployed identity: exact V2 branch `release/v2`, SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`;
- functional MCP-client test using `CarClever - Find My Car`: PASS, confirmed by André.

The old submitted endpoint and neutral alias remain live during transition:

- `https://carclever-find-my-car.vercel.app/mcp`
- `https://carclever.getcarwise.app/mcp`

## Support email — SENT

On 2026-09-16 André replied to Marco requesting that Anthropic replace the pending listing's MCP URL with:

`https://carclever-anth.getcarwise.app/mcp`

The message stated that the new endpoint is live and tested, that the existing endpoint remains active during the transition, and politely asked whether the current listing could be flagged with the review team given the submission history dating back to April.

**Do not mark the directory's stored MCP URL as changed until Anthropic confirms the support-side update.**

## OpenAI production safeguard — COMPLETE

Project: `ccfmc-dev-v2`  
Project ID: `prj_EJRR8xftf6TEIA3QS7jFXjBPr2aX`

OpenAI remained on exact approved V2 SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792` throughout the Anthropic incident.

After Anthropic recovery, André checked the OpenAI Production environment and confirmed:

- tracked branch: `release/v2`;
- **Auto-assign Custom Production Domains: Disabled**;
- setting saved;
- `carclever-oai.getcarwise.app` remains attached to Production.

Both platform production projects now require deliberate manual production-domain promotion.

## Standing release policy

For both platform production projects:

1. Git pushes may create deployments but must not silently take over branded production domains.
2. Production-domain movement requires deliberate **Promote to Production**.
3. Verify intended branch and exact SHA before promotion.
4. Verify branded MCP endpoint and exact production SHA after promotion.
5. Do not use routine documentation/test-log pushes as release mechanisms.

## Deferred housekeeping

After Anthropic confirms the pending listing uses the new branded endpoint and both reviews are stable:

- proposed Vercel display-name cleanup:
  - `ccfmc-dev-v2` -> `carclever-openai`;
  - `carclever-find-my-car` -> `carclever-anthropic`;
- audit old CarClever-related Vercel projects before any retirement;
- re-audit stale GitHub branches before bulk deletion;
- do not rename the shared `AndreBro007/carclever-find-my-car` repository merely to match Vercel display names.

Detailed plan: `PLAN_CARCLEVER_VERCEL_NAMING_AND_RELEASE_HYGIENE_20260916.md`.

## Current gate

**PENDING ANTHROPIC CONFIRMATION ONLY:** support-side replacement of the pending listing's MCP URL with `https://carclever-anth.getcarwise.app/mcp`.

No application-code or deployment changes were performed by ChatGPT in producing this record.

## Source records

- `DECISION_CARCLEVER_PLATFORM_DOMAIN_NAMING_20260911.md`
- `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`
- `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`
- `CURRENT_V2_STATE_20260909.md`
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`
- `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md`
- `UPDATE_ANTHROPIC_DNS_VERIFICATION_AND_RECOVERY_20260916.md`
- `PLAN_CARCLEVER_VERCEL_NAMING_AND_RELEASE_HYGIENE_20260916.md`
- `carclever-widget/ADMIN_RECORD_ANTHROPIC_SUBMISSIONS.md`
- `carclever-widget/ADMIN_RECORD_OPENAI_SUBMISSIONS.md`
- live Vercel/GitHub verification performed 2026-09-16
