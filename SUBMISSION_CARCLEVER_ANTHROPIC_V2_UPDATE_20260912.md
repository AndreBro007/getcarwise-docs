# CarClever Anthropic V2 Submission Update — 2026-09-12, updated 2026-09-16

## Status

**Current status: IN REVIEW.** The 2026-09-12 Anthropic directory screen confirmed `CarClever - Find My Car`, slug `carclever-find-my-car`, status `In review`, and `Updated: just now` immediately after saving the V2 update.

As of 2026-09-16, the V2 production release remains unchanged, a new branded Anthropic MCP endpoint is live and verified, and Anthropic support has been asked to replace the pending listing's existing MCP URL with that new endpoint. The support-side URL change is **pending Anthropic confirmation**.

## Original 2026-09-12 controlled update

This was a controlled update of the existing Anthropic submission, not a new server/slug.

- Existing MCP URL retained at that time: `https://carclever-find-my-car.vercel.app/mcp`.
- Existing Vercel project retained: `carclever-find-my-car`.
- Production was deliberately promoted from V1 to the exact tested V2 release without merging V2 into `main`.
- Promoted source: `release/v2`.
- Exact promoted SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.
- Vercel production deployment verified READY; deployment metadata records target `production`, branch `release/v2`, exact SHA above, and action `promote`.

## Vercel evidence

Approved production deployment:

- Project: `carclever-find-my-car`
- Project ID: `prj_AGtLT6n36FwfIida35UUKCYIB3zS`
- Deployment ID: `dpl_9vP17yqXx5fdfV2uTWfAenvfYFD2`
- State: READY
- Target: production
- Git branch: `release/v2`
- Git SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`
- Commit: `Make widget origin configurable via NEXT_PUBLIC_WIDGET_ORIGIN env var`
- Original promoted preview: `dpl_GxdqgK2Av4GWnbF8d7Mc8TxCw2hh`

No OpenAI-specific `NEXT_PUBLIC_WIDGET_ORIGIN` value was copied into the Anthropic project.

## Original Anthropic listing update

Actions completed on 2026-09-12:

1. Opened **Edit server**.
2. Used server **Sync/Rescan tools**; portal reported the server's current list as 2 tools.
3. Updated the public Description to the final V2 marketing description used for the OpenAI resubmission.
4. Kept established name, slug, category, links, branding, access/data-handling answers and policy acknowledgements unchanged unless already set.
5. Preserved the prior decision not to proactively rewrite current V2 tool descriptions solely for Anthropic; change them only if Anthropic gives concrete feedback or a reproducible defect demonstrates a need.
6. Saved/submitted the edit.
7. Returned to **Your MCP servers** and verified status `In review`, Updated `just now`.

## Final public description

Find My Car searches live U.S. new and used vehicle inventory to help shoppers find the right car for their needs and budget.
Search by specific or combined requirements, lifestyle needs, and priorities such as cheapest, newest, lowest mileage, or lower-risk options, including detailed criteria such as trim, color, drivetrain, transmission, cylinders, condition, and electrification.
Requests like “AWD SUV under $35k” and “reliable car for a teen driver” both work, with broader needs translated into relevant real vehicle models before searching current inventory.
Already found a car? Look up the exact VIN and run a Buyer Check for red flags, good signs, and what to verify before buying.
Core vehicle identity is VIN-cross-checked, and every returned match is checked against each hard filter applied.
Unreported accident, ownership, or CPO data is shown as unconfirmed—not assumed clean.
Each result includes links to check availability and see similar vehicles.

## Tool set expected

- `find_matching_vehicle`
- `resolve_dealer_url`

V2 `find_matching_vehicle` is expected to expose `vehicleNeeds`, `electrificationTypes` and `electrificationRequirement`, and not expose legacy `goals`.

## 2026-09-16 production drift incident and recovery

A Sep 14 push to `main` silently became the active Anthropic production deployment because the Vercel Production environment had **Auto-assign Custom Production Domains** enabled.

The Sep 14 deployment was not V2 plus a harmless documentation change; Git history showed it was on the older `main` lineage rather than the approved V2 release.

Recovery completed on 2026-09-16:

1. Exact approved V2 deployment at SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792` was manually promoted back to Production.
2. The active production aliases were verified back on that exact V2 deployment.
3. André disabled **Auto-assign Custom Production Domains** in Vercel's Production environment and saved the change.
4. Vercel now states that Production deployments must be manually promoted.

The source of the Sep 14 documentation/test-log commit itself remains unidentified and should not be attributed to a person or AI without evidence.

## 2026-09-16 branded Anthropic MCP endpoint

The confirmed platform-domain decision has now been implemented on the Anthropic Vercel project.

New branded endpoint:

`https://carclever-anth.getcarwise.app/mcp`

Setup completed:

- Added `carclever-anth.getcarwise.app` to Vercel project `carclever-find-my-car`.
- Vercel requested DNS:
  - Type: `CNAME`
  - Host: `carclever-anth`
  - Target: `c6a2c23ef4265088.vercel-dns-017.com.`
- André added the CNAME at Porkbun with note `CarClever - Anthropic MCP URL`.
- Vercel showed **Valid Configuration**.
- HTTPS/TLS is valid.
- Direct GET to `/mcp` returns the expected MCP JSON-RPC `405 Method Not Allowed` response.
- Vercel resolves the new hostname to exact approved V2 SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.
- André completed a successful functional MCP-client test using **`CarClever - Find My Car`** against the new endpoint.

Existing aliases remain live during the transition:

- `https://carclever-find-my-car.vercel.app/mcp`
- `https://carclever.getcarwise.app/mcp`

No alias should be removed until Anthropic confirms the pending listing has been switched and there is no remaining dependency.

## Anthropic support-side URL change

The MCP URL on the pending listing cannot be changed by André in the portal. This is the reason the support thread with Marco was opened.

Marco confirmed that:

- the old April submission through the older process is not the current review-queue item and does not require separate retirement action;
- the current pending submission can have its MCP URL changed while still pending;
- updating it while pending does not create a review-cost penalty;
- after approval, the correct sequence for later edits is to publish first, then make edits.

On 2026-09-16 André emailed Marco asking Anthropic to replace the pending CarClever listing's MCP URL with:

`https://carclever-anth.getcarwise.app/mcp`

The message stated that the endpoint is live and tested, that the existing endpoint remains active during transition, and politely asked whether the current listing could be flagged with the review team given the submission history dating back to April.

**Current gate:** wait for Marco/Anthropic to confirm that the support-side URL change has been applied or provide any follow-up validation instructions. Do not state that the directory already stores the new URL until this confirmation is received.

## Functional validation status

The older Sep 12 Claude cache symptom—stale V1 metadata on the base connector despite the server being reachable—should no longer be treated as an active defect by itself.

The Sep 16 branded endpoint has now passed:

- Vercel/domain validation;
- TLS/HTTPS validation;
- direct MCP transport reachability;
- exact production-SHA verification; and
- a successful functional MCP-client test using `CarClever - Find My Car`.

Do not change code solely because of the historical cache symptom unless it can still be reproduced against the current branded V2 endpoint.

## Review freeze and production policy

While Anthropic and OpenAI are both in review, do not change V2 code/contract unless:

- a platform requests a correction; or
- a concrete reproducible defect is demonstrated and André authorizes the correction path.

Production-domain assignment on the Anthropic project is now manual. A future release requires deliberate **Promote to Production**, with intended branch/SHA checked before promotion and endpoint/SHA verified afterward.

The same manual-promotion safeguard was also applied proactively to the separate OpenAI production project on 2026-09-16.

## Deferred housekeeping

Do not rename the Vercel project while the Anthropic support-side URL change remains pending.

Proposed later display-name cleanup:

- Anthropic: `carclever-find-my-car` -> `carclever-anthropic`
- OpenAI: `ccfmc-dev-v2` -> `carclever-openai`

See `PLAN_CARCLEVER_VERCEL_NAMING_AND_RELEASE_HYGIENE_20260916.md` for verification gates and broader Vercel/GitHub cleanup tasks.

## Related records

- `CURRENT_V2_STATE_20260909.md`
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`
- `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`
- `AUDIT_CARCLEVER_DUAL_PLATFORM_VERCEL_FEASIBILITY_20260911.md`
- `AUDIT_V2_ANTHROPIC_SUBMISSION_COMPLIANCE_20260910.md`
- `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md`
- `UPDATE_ANTHROPIC_MCP_URL_AND_PRODUCTION_DRIFT_20260916.md`
- `UPDATE_ANTHROPIC_DNS_VERIFICATION_AND_RECOVERY_20260916.md`
- `PLAN_CARCLEVER_VERCEL_NAMING_AND_RELEASE_HYGIENE_20260916.md`
