# CarClever GitHub ↔ Vercel Environment Mapping Audit — 2026-09-10

**Status:** Verified read-only infrastructure audit; strategy follow-up added 2026-09-10  
**Scope:** GitHub repository/branch/PR topology, Vercel project/deployment topology, current V1/V2/V3 boundaries, preview-deployment fan-out, and release-isolation recommendations before final OpenAI resubmission testing.  
**No application code, Vercel settings, branches, pull requests, connectors, domains, or deployments were changed by this audit.**

## 1. Executive conclusion

The V2 work has **not** been shown to have contaminated either the V1 `main` production deployment or the V3 production deployment.

The confusing deployment pattern is real, but it is a **Vercel preview-deployment fan-out problem**, not a Git merge/production-branch problem:

- Several Vercel projects are connected to the same GitHub repository, `AndreBro007/carclever-find-my-car`.
- Pushes to V2 and research branches are currently allowed to generate **Preview** deployments in multiple connected Vercel projects, including the V1, V3, schema-probe, and legacy dev projects.
- In Vercel deployment records, these cross-project branch builds have `target = null`, while actual production deployments have `target = production`.
- The current V1 production remains tied to GitHub `main` at `e7c8634...`.
- The current V2 production remains tied to `release/v2` at `a9d6439...`.
- The current V3 production remains tied to `v3.1-3.3/card-first-check-vehicle` at `4032feb...`.

This matches the current project record in `CURRENT_V2_STATE_20260909.md`: V3 has historically generated preview deployments for V2 branches, but those preview deployments are not proof that V3 production serves V2.

The immediate infrastructure issue is therefore **environment isolation and branch filtering**. It should be fixed before final OpenAI submission testing so that the test host, deployed commit, and intended release branch are unambiguous.

## 2. Sources checked

This audit was based on:

- all mandatory `carclever-widget` administrative files: `STATE.md`, `DECISIONS.md`, `PLAYBOOK.md`, `REFERENCE.md`, `TASKS.md`, `ACCOUNT_MEMORY_TRANSFER.md`, and `WORKFLOW_ARCHITECTURE.md`;
- a dynamic GitHub API root listing of `getcarwise-docs`, followed by full retrieval of every root file returned by that listing;
- current GitHub branch metadata for `AndreBro007/carclever-find-my-car`;
- current open pull requests in that repository;
- current Vercel team/project metadata and deployment histories for all relevant CarClever projects;
- supplied GitHub/Vercel screenshots;
- current Vercel documentation for Git branch deployment filtering.

Older documents that still describe V2 as proposed, feasibility-only, or not implemented were treated as historical. `CURRENT_V2_STATE_20260909.md` is the current V2 operational record.

## 3. Verified environment map

| Environment / purpose | GitHub repository | Intended production branch | Verified production commit | Vercel project | Current role / observation |
|---|---|---|---|---|---|
| **V1 submitted app** | `AndreBro007/carclever-find-my-car` | `main` | `e7c8634...` | `carclever-find-my-car` | Production remains V1/main. Newer V2/feature pushes seen here are Preview deployments, not production. V1 remains frozen while its Anthropic review status is unresolved. |
| **V2 OpenAI resubmission candidate** | `AndreBro007/carclever-find-my-car` | `release/v2` | `a9d6439...` | `ccfmc-dev-v2` | Current tested V2 production endpoint: `https://ccfmc-dev-v2.vercel.app/mcp`. READY production deployment verified. |
| **V3 paused work** | `AndreBro007/carclever-find-my-car` | `v3.1-3.3/card-first-check-vehicle` | `4032feb...` | `ccfmc-dev-v3` | V3 production remains the paused V3 branch. V2/research pushes are nevertheless generating Preview deployments in this project. |
| **V2 schema/research probe** | `AndreBro007/carclever-find-my-car` | `research/v2-schema-probe` | research branch state | `carclever-v2-schema-probe` | Research-only project. It is also receiving unrelated V2 branch Preview deployments. |
| **Legacy dev/test** | `AndreBro007/carclever-find-my-car` | historical setup | historical | `ccfmc-dev` | Documented as legacy/retired, but it still receives new Preview builds from current branches. This is deployment noise/cost, not an active release target. |
| **Widget/admin deployment** | `AndreBro007/carclever-widget` | `main` | current widget/admin main | `getcarwise-app` | Separate repository and separate Vercel project. Current documentation/admin commits to `carclever-widget/main` create actual production deployments here. This explains the recent Vercel rows that say `main` and have V2-related commit messages. |
| **Old CarClever project** | `AndreBro007/CarClever` | old project | historical | `car-clever` | Unrelated to the current Find My Car V1/V2/V3 release path; ignore for current resubmission work unless later cleaning up old infrastructure. |

## 4. The key “main branch” confusion

The Vercel deployment rows titled **“Record final amended V2 contract and release status”** that show `main` are not V2 application-code deployments to `carclever-find-my-car/main`.

Live Vercel metadata identifies those deployments as:

- Vercel project: `getcarwise-app`
- GitHub repository: `AndreBro007/carclever-widget`
- GitHub branch: `main`

Those commits are administrative/documentation changes in `carclever-widget`. Because that repository is connected to `getcarwise-app`, they trigger production deployments of that separate project.

The application repository's `main` branch remains at `e7c8634...`, and the verified V1 production deployment also remains on that commit.

## 5. What is happening in V3

The concern about V2 appearing in the V3 project is valid as an isolation problem.

The V3 project currently contains many Preview deployments triggered by branches including:

- `release/v2`
- `v2-correction/description-and-citation-cleanup`
- `v2-implementation/schema-and-electrification`
- `research/v2-schema-probe`
- older V2.4/V2.5 branches

However, those cross-branch deployments are Preview targets. The verified V3 production deployment remains `v3.1-3.3/card-first-check-vehicle` at `4032feb...`.

So the correct interpretation is:

> **V2 branches are building inside the V3 Vercel project, but they are not replacing V3 production.**

That distinction is operationally important because Vercel's newest/latest deployment can be a Preview deployment; the newest row alone must not be used to infer what production is serving.

## 6. GitHub branch and PR state

The current application repository has distinct active/historical branches, including:

- `main` — V1 production
- `release/v2` — V2 release
- `v3.1-3.3/card-first-check-vehicle` — paused current V3 work
- `research/v2-schema-probe` — research
- `v2-correction/description-and-citation-cleanup` — V2 correction work
- `v2-implementation/schema-and-electrification` — V2 implementation work
- older `feature/v3-check-vehicle`, `feature/edmunds-two-button-cta`, V2.4/V2.5, and test/fix branches

There are two open draft PRs against `main`:

1. PR #1 — `fix/total-matches-count-bug` → `main`
2. PR #2 — `feature/edmunds-two-button-cta` → `main`

Both are old, explicitly marked **DO NOT MERGE YET**, and predate the current `release/v2` release path. They are cleanup candidates, not evidence of an active merge into `main`. They should not be closed or merged without André's confirmation.

## 7. Root cause

The root architectural cause is that multiple Vercel projects are connected to the same GitHub application repository, while automatic Git deployments are currently permissive enough that unrelated branches can build as Previews in those projects.

That creates four practical problems:

1. **Release ambiguity** — the newest deployment shown for a project may not be that project's production release.
2. **Testing risk** — a connector or tester can accidentally use the wrong branch alias/preview URL.
3. **Build noise and cost** — one push can fan out into several Vercel builds that have no testing purpose.
4. **Operational confusion** — V2 commit messages appear under V1/V3 projects even though their production targets remain unchanged.

No production cross-contamination was found in this audit.

## 8. Proposed target isolation policy

**Status: proposed only. No settings were changed. Actual Vercel configuration work belongs to the Engineering lane.**

| Vercel project | Keep as production branch | Proposed automatic-deployment scope |
|---|---|---|
| `carclever-find-my-car` (V1) | `main` | While review is active, freeze tightly: production from `main`; suppress unrelated branch previews unless a deliberate V1 preview is required. |
| `ccfmc-dev-v2` | `release/v2` | Allow `release/v2` and only deliberate V2 development/correction branches required for testing. Deny V3 and unrelated research branches. |
| `ccfmc-dev-v3` | `v3.1-3.3/card-first-check-vehicle` | Allow only the current V3 branch/family. Deny V2 and research branches. |
| `carclever-v2-schema-probe` | `research/v2-schema-probe` | Allow only schema-probe/research work while the project is still needed. |
| `ccfmc-dev` | legacy | Disable broad automatic Git deployments. Later strategy review determines whether it remains as the short-URL ChatGPT test harness or is decommissioned. |
| `getcarwise-app` | `carclever-widget/main` | Separate website/widget workstream; excluded from the current Find My Car release audit unless a critical dependency is found. |

Vercel currently supports per-branch Git deployment rules through `git.deploymentEnabled`, including glob/minimatch patterns. Unspecified branches default to enabled, so a reliable isolation configuration must be designed carefully rather than assuming only the production branch deploys.

## 9. Recommended sequence before OpenAI resubmission

1. **Confirm the V1/Anthropic review status with André before any V1 infrastructure change.** Current project governance says V1 remains frozen while that review is active.
2. Agree the branch allow/deny matrix above.
3. Hand the approved Vercel filtering/configuration change to the Engineering lane for implementation.
4. Re-audit each relevant Vercel project after the change: production branch, production SHA, domain, and one deliberate allowed Preview; confirm an unrelated branch no longer fans out.
5. Decide and configure the final stable OpenAI V2 MCP submission origin.
6. Run the final OpenAI smoke/regression test against the **exact MCP endpoint that will be submitted**, and record the deployed SHA used for that test.
7. Only then proceed with the resubmission package.

## 10. Cleanup candidates after the release path is stable

These are **not authorized actions**, only candidates for a later explicit cleanup decision:

- close stale draft PR #1 and PR #2 if confirmed superseded;
- delete obsolete historical feature/test branches after confirming no rollback/reference need;
- retain `ccfmc-dev` only if the known short-URL ChatGPT test need remains, otherwise decommission after a replacement is proven;
- inactivate and later remove the schema-probe Vercel project after dependency verification;
- review the old `car-clever` project separately;
- review `getcarwise-app` production-build behavior separately under the website-app workstream.

## 11. Governance / ownership

- **André:** confirms review status, approves environment-isolation policy, domain choice, and any cleanup/deletion decisions.
- **ChatGPT Business/Strategy lane:** audits, documents, verifies topology, defines the intended release/isolation policy, and reviews resulting evidence.
- **Claude Engineering lane:** implements Vercel/Git deployment filtering, code/config changes, deployments, connector changes, and production infrastructure changes.

## 12. Current gate status

The V2 shared-contract implementation and connector validation are already recorded as complete. The relevant remaining operational items are:

- final stable OpenAI submission origin/domain;
- V3/V2 preview branch isolation;
- exact-endpoint final smoke testing before resubmission.

No evidence found in this audit requires reverting V2 application work.

## 13. Strategy follow-up — 2026-09-10

Further investigation after André's review of the initial audit produced the following additional findings. The detailed proposed operating model is now recorded in `STRATEGY_CARCLEVER_CROSS_PLATFORM_RELEASE_AND_DEPLOYMENT_20260910.md`.

### 13.1 Preview semantics confirmed

Vercel Preview deployments are isolated builds of branch commits. They do not merge Git and do not later merge themselves into V1, V2, V3, or `main`. A production change still requires a deliberate Git/release action or deployment promotion. The cross-project V2 builds observed in V3 remain deployment noise/isolation failures, not hidden merges.

### 13.2 Auto-deploy root cause remains unproven

Preview fan-out has **not** been proven to be the cause of V2's intermittent production auto-deployment behavior. It is still worth eliminating because it creates unnecessary builds and ambiguity. After branch isolation, Engineering should run a controlled deployment-trigger test to determine whether V2 production now updates deterministically. No supported per-project “deploy this project first” priority mechanism was identified; correct branch filtering is the primary control.

### 13.3 Platform policy changes the permanent architecture

Anthropic's submitted V1 connection is recorded as `https://carclever-find-my-car.vercel.app/mcp`. Current Anthropic documentation says published MCP tool-surface changes can be deployed to the live server without a new directory submission, while listing changes are managed separately. Because changing the published server hostname is not clearly documented as a self-service no-review operation, the safest strategy is to retain Claude's submitted MCP origin and upgrade code behind it after the review gate clears.

OpenAI's current published-plugin maintenance rules are stricter: changing the MCP origin (`scheme`, `hostname`, or `port`) requires a **new plugin**, while tool/schema/description/annotation/resource-contract changes require a new reviewed plugin version. Consequently the OpenAI V2 submission hostname should be treated as permanent before resubmission. `https://carclever.getcarwise.app/mcp` is the preferred branded candidate, subject to a complete dependency/domain verification before any move or attachment.

### 13.4 PR #1 and PR #2 are now verified as superseded, not pending production merges

Git comparison shows PR #1 head `6700bbb` is an ancestor of current `release/v2`; current V2 contains that work and is far ahead of it. PR #1's original DO-NOT-MERGE gate protected V1 during review, but the old PR is no longer the correct release vehicle.

For PR #2, the V2.2 portion is also already represented in current `release/v2`, while the PR branch later accumulated V3/check-vehicle-era commits and diverged from current V2. It should therefore not be merged into `main` as a route to V2 production.

**Proposed disposition for both:** close as superseded after André approves the release strategy and Claude independently rechecks the ancestry; do not merge either old PR.

### 13.5 V3 must be rebased conceptually onto final V2

Live Git comparison shows paused V3 has diverged and is substantially behind current `release/v2`. Future V3 should be created from the final V2 baseline and have still-valid V3-specific work selectively ported and fully retested. The old V3 branch should not be merged wholesale.

### 13.6 Temporary Vercel-project disposition refined

- `ccfmc-dev`: **do not delete yet**. It solved a documented, real ChatGPT Preview-domain/DNS-length problem. Convert it to a dormant/manual short-URL ChatGPT test harness, block broad auto-deployments, and delete only after a replacement test process is proven.
- `carclever-v2-schema-probe`: its temporary research purpose is complete. Proposed path is inactivate first (stop Git auto-deploy / remove temporary connector after approval), retain briefly through final V2 smoke testing, then delete after confirming no dependency points to it.

### 13.7 Long-term release model proposed

Use one application codebase and versioned `release/vN` candidates, but treat Claude and OpenAI as two permanent production channels with stable MCP origins. Default to both channels serving the exact same tested SHA. Temporary platform version skew is permitted only when submission/review timing forces it. V2/V3 should be releases promoted through channels, not permanent hosting identities.

### 13.8 Testing architecture expanded

The V1→V2 equivalence method remains the baseline. Future releases should add automated commit/contract CI, exact-SHA deployed-environment verification, same-window V1/candidate A/B tests, cross-host ChatGPT/Claude acceptance, exact-submission-host smoke tests, and post-release monitoring. A release manifest should record the exact SHA, deployments, MCP origins, contract snapshot, platform status, tests, and rollback point for every promotion.

### 13.9 New strategy reference

Primary follow-up strategy document:

- `STRATEGY_CARCLEVER_CROSS_PLATFORM_RELEASE_AND_DEPLOYMENT_20260910.md`

Existing supporting references remain:

- `CURRENT_V2_STATE_20260909.md`
- `V2_CONNECTOR_TEST_RECORD_20260909.md`
- `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md`
- `CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md`

No application, Vercel, domain, connector, PR, or branch changes were made by this follow-up. All execution remains gated on André's decisions and belongs to Claude Engineering where applicable.
