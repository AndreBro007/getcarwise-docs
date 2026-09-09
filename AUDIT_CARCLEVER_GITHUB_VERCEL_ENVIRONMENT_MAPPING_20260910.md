# CarClever GitHub ↔ Vercel Environment Mapping Audit — 2026-09-10

**Status:** VERIFIED read-only audit, reconciled with cross-platform strategy  
**Scope:** `AndreBro007/carclever-find-my-car` Git/Vercel topology, V1/V2/V3 boundaries, Preview fan-out, PR/branch state, temporary-project disposition, and cross-platform release implications before OpenAI V2 resubmission.  
**Execution:** No application code, Vercel setting, domain, connector, PR, branch, or deployment was changed by this audit. Business/Strategy documentation only.

## 1. Executive conclusion

No evidence was found that V2 development contaminated V1 `main` production or replaced V3 production.

The confusing Vercel history is a **Preview-deployment fan-out problem**: several Vercel projects are connected to the same GitHub application repository, and unrelated branches are allowed to build as Previews in multiple projects.

Verified production lines:

- **V1 / Claude submission:** GitHub `main` at `e7c8634...`; Vercel project `carclever-find-my-car`; Anthropic submission connection recorded as `https://carclever-find-my-car.vercel.app/mcp`.
- **V2 / OpenAI resubmission candidate:** `release/v2`; merged correction `5e8735e`; deployed tip `a9d6439...`; Vercel `ccfmc-dev-v2`; tested MCP `https://ccfmc-dev-v2.vercel.app/mcp`.
- **V3 / paused:** `v3.1-3.3/card-first-check-vehicle`; standing V3 production `4032feb...`; Vercel `ccfmc-dev-v3`.

A V2 branch appearing in a V1/V3 Vercel project as a Preview does **not** merge Git, become that project's production branch, or enter `main` automatically.

## 2. Sources checked

Mandatory `carclever-widget` administration files were read at start of session:

- `STATE.md`
- `DECISIONS.md`
- `PLAYBOOK.md`
- `REFERENCE.md`
- `TASKS.md`
- `ACCOUNT_MEMORY_TRANSFER.md`
- `WORKFLOW_ARCHITECTURE.md`

The `getcarwise-docs` root was dynamically listed through GitHub and the full contents of every returned root file were fetched. Current GitHub branches/PRs, relevant commit ancestry, Vercel project/deployment metadata, supplied screenshots, and current OpenAI/Anthropic/Vercel documentation were also reviewed.

Current V2 operational truth is `CURRENT_V2_STATE_20260909.md`; older “proposed/not implemented” V2 statements are historical.

## 3. Verified Vercel project map

| Project | Repository | Current/known purpose | Finding |
|---|---|---|---|
| `carclever-find-my-car` | `carclever-find-my-car` | V1 / Claude production | Production remains V1/main; unrelated V2 branches have generated Previews. |
| `ccfmc-dev-v2` | `carclever-find-my-car` | V2 release/test production | Current V2 target; READY at `a9d6439...`. |
| `ccfmc-dev-v3` | `carclever-find-my-car` | paused V3 | V3 production remains V3; V2/research branches have generated Previews here. |
| `ccfmc-dev` | `carclever-find-my-car` | short-URL ChatGPT Preview workaround / legacy test | Still receives unrelated builds; should be constrained, not deleted yet. |
| `carclever-v2-schema-probe` | `carclever-find-my-car` | temporary V2 schema research | Purpose complete; should be inactivated, retained briefly, then deleted after dependency check. |
| `getcarwise-app` | `carclever-widget` | website/widget application | Separate workstream, excluded from this Find My Car audit unless a critical dependency is found. |
| `car-clever` | old `CarClever` repo | historical | Not part of current V1/V2/V3 release path. |

## 4. Preview semantics

A Vercel Preview is an isolated build of a Git branch/commit. It never merges by itself.

Normal release flow is:

`branch commit → Preview → validation → deliberate Git/release action → Production`

If Vercel explicitly promotes a deployment, production traffic can move to that build, but Git history still does not merge or change automatically.

Therefore the observed V2 Previews inside `ccfmc-dev-v3`, `carclever-find-my-car`, `ccfmc-dev`, and the schema probe are deployment noise/isolation failures, not hidden code merges.

## 5. “main” deployment confusion resolved

Recent Vercel rows with V2-related documentation messages and branch `main` were traced to:

- GitHub repo: `AndreBro007/carclever-widget`
- branch: `main`
- Vercel project: `getcarwise-app`

They were not `carclever-find-my-car/main` application-code deployments. The separate website/widget project will be reviewed later under its own workstream, per André's instruction.

## 6. V2 auto-deployment issue

The repository history contains multiple V2 no-op “nudge” commits used to trigger/retrigger Vercel deployment, and current administration notes correctly warn that the V2 Production deployment may require manual verification/redeploy.

**Finding:** Preview fan-out has not been proven to be the root cause of missed V2 production deploys. It can add build/webhook/queue noise and should be removed, but causation must be tested rather than assumed.

After branch isolation, Claude Engineering should run a controlled two-push deployment-trigger test and verify project, target, branch, and exact SHA. If failures remain, investigate the GitHub↔Vercel integration/project settings directly.

No supported per-project “deploy this Vercel project first” priority mechanism was identified. Correct branch filtering is the appropriate control.

## 7. GitHub PR findings

Two stale draft PRs still target `main`:

### PR #1 — `fix/total-matches-count-bug`

Head `6700bbb` is an ancestor of current `release/v2`. Its V2.1-era work is already incorporated into V2. The historical **DO NOT MERGE YET** gate protected V1 while under review; it is no longer a reason to merge the old branch later.

**Proposed disposition:** close as superseded after André approves strategy and Claude independently verifies ancestry. **Do not merge.**

### PR #2 — `feature/edmunds-two-button-cta`

The V2.2 deterministic Edmunds baseline is represented in current `release/v2`, but the old PR branch later accumulated V3/check-vehicle-era commits and diverged from current V2.

**Proposed disposition:** close as superseded after André approval and Claude verification. **Do not merge.** Future V3 content must be selectively ported from current V2 baseline rather than merged through this old PR.

## 8. V3 branch finding

Current paused V3 is diverged and substantially behind amended `release/v2`. Future V3 should therefore be created fresh from final V2, with still-valid V3-specific changes selectively ported and the full V2 regression suite rerun. Do not merge the stale paused V3 branch wholesale.

## 9. Temporary-project disposition

### `ccfmc-dev`

**Do not delete yet.** Documentation confirms it was created for a real ChatGPT Apps SDK / Vercel Preview-domain issue where long branch aliases produced an unusable sandbox/DNS path. Claude did not have the same issue.

Preferred role now: **one shared short-URL release-test harness**.

- disable broad auto-deploy;
- deploy only explicit release/short test branches;
- keep until a replacement process proves the short-URL workaround is unnecessary.

### `carclever-v2-schema-probe`

The probe was explicitly temporary and its findings are now in the real V2 implementation.

Preferred retirement:

1. stop Git auto-deployment/remove temporary connector after approval;
2. preserve Git research branch/docs;
3. retain inert Vercel project through final V2 submission smoke window;
4. delete after confirming no connector/domain/test dependency points to it.

## 10. Cross-platform policy finding

Anthropic and OpenAI have different maintenance rules, so **platform channel** and **CarClever version** must be treated separately.

### Anthropic

Current Anthropic documentation says a published MCP server is a live API: tools may be added/changed/removed by deploying the server without resubmission or scheduled re-review. Listing metadata is handled separately. A published server-origin replacement is not clearly documented as a routine self-service change, so the safe strategy is to preserve the submitted Claude MCP origin and upgrade code behind it after the gate clears.

### OpenAI

OpenAI requires a production MCP URL and domain verification. For a published plugin, reviewed MCP metadata changes require a new reviewed version; server-only compatible fixes may deploy without a new version. Crucially, the MCP origin (`scheme`, `hostname`, `port`) cannot change between versions; changing it requires a **new plugin**.

This makes the OpenAI V2 hostname a permanent architecture decision.

## 11. Permanent MCP-origin recommendation

### Claude

Preserve the submitted origin:

`https://carclever-find-my-car.vercel.app/mcp`

If/when V2 is approved for Claude production, deploy the exact tested V2 release behind that same URL rather than changing the connector hostname.

### OpenAI

**Preferred permanent candidate:**

`https://findmycar.getcarwise.app/mcp`

Reasoning:

- this subdomain was already documented in the project plan as the intended permanent Find My Car domain once ready for real deployment;
- it is product-specific, platform-neutral, and owned under GetCarWise;
- it avoids submitting a disposable version-labelled `.vercel.app` hostname;
- it avoids moving `carclever.getcarwise.app`, which current records associate with the V1 Vercel project, while the Anthropic gate is unresolved.

`https://carclever.getcarwise.app/mcp` remains an alternative only after a dependency audit proves it can be used/reassigned without affecting V1 or other integrations. The apex `getcarwise.app/mcp` is not recommended because the website architecture is a separate production surface.

Before any OpenAI origin is committed, Engineering must verify DNS/current routing, absence of dependencies, exact V2 SHA, custom-domain widget/CSP/resource origin behavior, TLS/MCP, OpenAI challenge-token hosting, Scan Tools, and final test cases.

## 12. Proposed permanent operating model

**One code product, two stable platform production front doors, one shared release test harness.**

- one GitHub application repo;
- `release/vN` branches for release candidates;
- Claude production channel with stable Claude MCP origin;
- OpenAI production channel with stable OpenAI MCP origin;
- `ccfmc-dev` as deliberate shared short-URL test harness;
- both production channels use the same tested release SHA whenever approval gates permit;
- temporary platform version skew is documented, not treated as separate products;
- optional stable deployment-pointer branches (`prod/claude`, `prod/openai`) can be introduced if independent platform approval timing becomes recurring;
- version-specific Vercel projects such as V3 should be retired once the channel/test model is established.

Future V3 should be built from final V2, validated on the shared harness, then promoted to each platform's stable front door. OpenAI V3 metadata changes require the appropriate new-version review and must remain backward-compatible with the currently published contract during transition; Claude's same-origin live MCP tool changes currently do not require resubmission.

## 13. Testing architecture

Retain `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md` as the core methodology and expand it into a repeatable release acceptance pipeline:

1. **Commit/contract CI:** build, typecheck, tests, MCP initialize/tools/schema/resource snapshots, deterministic fixtures.
2. **Deployment verification:** intended Vercel project, target, exact SHA, MCP/resource/CSP reachability, isolation check.
3. **Same-window A/B:** V1 vs candidate effective constraints, arguments, evidence, ordering, latency — not identical live VINs.
4. **Cross-host acceptance:** same high-value and negative prompt pack on ChatGPT and Claude.
5. **Exact submission-host smoke:** exact hostname + SHA + Scan Tools/equivalent + UI/images/links.
6. **Post-release monitoring:** runtime/connector health plus retained rollback.

Every promotion should produce a release manifest containing version, SHA, branch, both platform endpoints/statuses, Vercel deployments, contract fingerprint/scan, automated tests, live host acceptance, exceptions, and rollback point.

## 14. Strategy reference and next gate

Detailed proposed operating model:

- `STRATEGY_CARCLEVER_CROSS_PLATFORM_RELEASE_AND_DEPLOYMENT_20260910.md`

Supporting current records:

- `CURRENT_V2_STATE_20260909.md`
- `V2_CONNECTOR_TEST_RECORD_20260909.md`
- `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md`
- `CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md`

Current gate requiring André confirmation before V1 changes: **Anthropic V1 status** (in review / approved-published / changes requested-rejected / withdrawn).

All infrastructure and app-repository execution resulting from this audit belongs to Claude Engineering after André approves the strategy/decisions.
