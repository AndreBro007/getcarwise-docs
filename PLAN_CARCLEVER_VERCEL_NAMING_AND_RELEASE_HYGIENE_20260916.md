# CarClever Vercel Naming and Release Hygiene Plan — 2026-09-16

**Owner lane:** ChatGPT — Business/Strategy  
**Status:** ACTIVE HOUSEKEEPING PLAN — production safety controls complete; renames/retirements deferred pending Anthropic URL-change confirmation

## Current verified production map

Both platform endpoints currently serve the same approved V2 release from repository `AndreBro007/carclever-find-my-car`, branch `release/v2`, exact SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.

- OpenAI Vercel project: `ccfmc-dev-v2`
  - Immutable project ID: `prj_EJRR8xftf6TEIA3QS7jFXjBPr2aX`
  - Production MCP domain: `https://carclever-oai.getcarwise.app/mcp`
- Anthropic Vercel project: `carclever-find-my-car`
  - Immutable project ID: `prj_AGtLT6n36FwfIida35UUKCYIB3zS`
  - New production MCP domain: `https://carclever-anth.getcarwise.app/mcp`
  - Existing migration aliases retained: `carclever.getcarwise.app` and `carclever-find-my-car.vercel.app`

The platform-specific Vercel projects are intentional: one shared codebase/release, separate production front doors and deployment/review lifecycles.

## Production safety controls — completed 2026-09-16

Both production projects now use deliberate/manual production-domain promotion.

### Anthropic

Following the Sep 14 silent production replacement incident, André disabled Vercel **Auto-assign Custom Production Domains** on the Production environment and saved the setting. Vercel's UI states that Production deployments must be manually promoted.

The approved V2 deployment was restored and independently verified at exact SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.

### OpenAI

André then checked project `ccfmc-dev-v2` and confirmed:

- Production branch tracking: `release/v2`;
- **Auto-assign Custom Production Domains: Disabled**;
- setting saved;
- `carclever-oai.getcarwise.app` remains attached to Production.

The OpenAI custom domain was independently verified to remain on the approved V2 SHA before this settings change. The settings change itself does not require a redeploy.

### Standing production policy

- Git pushes may create deployments, but custom production domains must not silently move to a new deployment.
- A production cutover requires an explicit **Promote to Production** action.
- Before promotion, verify intended branch and exact SHA.
- After promotion, verify the branded MCP endpoint and exact production SHA.
- Do not use a routine documentation/test-log push as a production-release mechanism.

## Proposed production project names — DEFERRED

After Anthropic support confirms the pending listing has been switched to the new branded MCP URL, rename the two production Vercel projects in one controlled maintenance window:

- `ccfmc-dev-v2` -> `carclever-openai`
- `carclever-find-my-car` -> `carclever-anthropic`

These names are preferred over historical `dev`/version labels because the projects are now production platform endpoints, not temporary development projects.

Do **not** rename while Anthropic's support-side URL change is still pending. Custom domains are the public contract and should remain unchanged.

After each rename, verify:

1. immutable Vercel project ID is unchanged;
2. GitHub repository link is still `AndreBro007/carclever-find-my-car`;
3. Production branch/release-control setting remains correct;
4. custom platform domain remains attached;
5. exact production SHA remains `b8b07d8542f5d3f2a12e00433e089dde28ae5792` unless a later approved release supersedes it;
6. `/mcp` remains reachable;
7. no platform submission URL changed as a side effect.

## Anthropic migration cleanup — DEFERRED

Current state:

- `https://carclever-anth.getcarwise.app/mcp` is live, TLS-valid, Vercel-valid and functionally tested.
- The old submitted endpoint remains live during the support-side transition.
- André emailed Marco/Anthropic support on 2026-09-16 requesting replacement of the pending listing MCP URL with the new branded endpoint.

Do not remove legacy Anthropic aliases until Anthropic confirms the pending listing has been updated and there is no remaining operational dependency on them.

## Remaining Vercel housekeeping backlog

After both OpenAI and Anthropic are stable on their branded production URLs:

1. Audit remaining CarClever-related Vercel projects, including at minimum `ccfmc-dev`, `ccfmc-dev-v3`, `carclever-v2-schema-probe`, `car-clever`, and any newer test projects discovered at that time.
2. Classify each as:
   - active test infrastructure;
   - retained historical/reference infrastructure; or
   - retirement candidate.
3. Verify current documentation/test workflows before deleting or disconnecting anything.
4. Record the final project map using immutable Vercel project IDs, not display names alone.
5. Check that any active test project has intentional branch tracking, deployment protection, and authentication settings appropriate to its use.

No Vercel project should be deleted solely because its display name looks obsolete.

## Remaining GitHub housekeeping backlog

Known low-priority GitHub cleanup should be handled separately from production-submission work:

1. Re-audit the stale branches previously identified in `carclever-widget` before bulk deletion. Eighteen branches were earlier confirmed fully merged (`ahead_by: 0`), but the live branch list must be rechecked immediately before deletion.
2. Keep stale `carclever-find-my-car` PR #1/#2 as housekeeping only; do not merge them into the active V2 line.
3. Audit old/duplicate feature branches in `carclever-find-my-car` only after current review/submission stability is confirmed; do not delete rollback/reference branches without checking documentation references.
4. Keep the separate `AndreBro007/CarClever` repository decision parked until a deliberate keep/integrate/retire review is performed; do not infer retirement from age or naming.
5. Do **not** rename the `AndreBro007/carclever-find-my-car` GitHub repository as part of the Vercel display-name cleanup. The repository is shared by both production platform projects and is widely referenced in documentation and integrations.

## Documentation hygiene

Maintain one canonical production map containing, for each platform:

- Vercel project display name and immutable project ID;
- public MCP URL;
- Git repository and release branch;
- currently approved production SHA;
- production-promotion policy;
- review/submission status;
- retained legacy aliases and retirement conditions.

Prefer immutable Vercel project IDs in internal runbooks where practical so future display-name changes do not break identification.

## Gate

- **Completed:** dual-platform manual production-domain promotion policy.
- **Pending external confirmation:** Anthropic support-side MCP URL replacement.
- **Deferred:** Vercel production project renames, legacy alias cleanup, old Vercel-project audit, and GitHub branch/repository housekeeping.
- André confirmation is required before executing any rename, deletion, retirement, or bulk branch cleanup action.