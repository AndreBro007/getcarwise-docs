# CarClever Cross-Platform Release and Deployment Strategy — 2026-09-10

**Status:** PROPOSED — pending André confirmation before any infrastructure or application-repository changes  
**Scope:** Long-term GitHub/Vercel/version/release strategy for CarClever - Find My Car across Claude and OpenAI, including stable MCP origins, V1→V2→V3 promotion, Preview behavior, stale PR disposition, temporary Vercel projects, and the final test/release process.  
**Execution boundary:** This document is Business/Strategy guidance. Claude Engineering owns application code, Git branch/PR mutations in `carclever-find-my-car`, Vercel settings, deployments, domain moves, connector changes, and production cutovers.

## 1. Executive recommendation

The current multi-project setup was a sensible **temporary isolation mechanism** while V1 was frozen in Anthropic review and V2/V3 needed independent testing. It should not become the permanent release model.

The preferred long-term architecture is:

1. **One application codebase:** `AndreBro007/carclever-find-my-car`.
2. **Versioned release candidates:** `release/v2`, future `release/v3`, etc.
3. **Two permanent platform production channels:** one for Claude and one for OpenAI, because the two platforms have different submission/review/update rules and can legitimately be on different approved versions temporarily.
4. **Stable MCP origin per platform:** do not create a new public MCP hostname for every CarClever version.
5. **Sync-first release policy:** both platform channels should serve the same tested release SHA whenever their review gates permit. Temporary skew is acceptable only because one platform may approve before the other.
6. **Previews are test artifacts, never releases:** no Preview deployment merges Git or becomes another branch automatically.
7. **Temporary/research Vercel projects are inert by default:** no broad automatic Git fan-out.
8. **Every promotion is SHA-driven and evidence-driven:** a release manifest records exact Git SHA, Vercel deployment, MCP URL, contract fingerprint, tests, and platform status.

This architecture separates two concepts that have become mixed together in the current setup:

- **Version** = V1, V2, V3 code/release state.
- **Platform channel** = Claude production versus OpenAI production.

A version is promoted through platform channels; it should not require a permanent Vercel project named after every version.

## 2. Preview deployments: what they are and when they merge

A Vercel Preview deployment is an isolated build of a Git branch/commit. It does **not** merge into another Git branch and it does **not** later merge itself into Production.

The normal flow is:

`feature/release branch push → Vercel Preview → test/review → deliberate Git merge or release promotion → Production deployment`

Therefore:

- A V2 Preview that appears inside the V3 Vercel project is still just a build of a V2 Git commit.
- It never becomes V3 code by itself.
- It never enters `main` by itself.
- It never enters `release/v2` by itself.
- Git changes only when somebody explicitly merges, rebases, cherry-picks, or moves a branch ref.
- Vercel Production changes when the configured production branch is deployed or when a deployment is explicitly promoted; promoting a deployment still does not rewrite Git history.

The current cross-project Preview fan-out is therefore an **isolation/noise problem**, not an automatic merge mechanism.

## 3. Was the current multi-Vercel-project design wrong?

No. It solved a real temporary problem: V1 `main` was under review and needed to stay frozen, while V2 and V3 needed live environments and connectors.

However, the design has now accumulated five Vercel projects connected to the same application repository, and branch filtering is permissive enough that unrelated branch pushes generate Preview builds in several projects. That is no longer the cleanest permanent operating model.

### What is good about the current design

- V1 production remained isolated while V2/V3 work continued.
- V2 could be tested as a real production-target deployment without changing V1.
- V3 had an independent test target.
- The schema probe could investigate host-contract behavior without touching release branches.
- `ccfmc-dev` solved a confirmed ChatGPT/Vercel Preview-domain length problem.

### What should change

- Keep permanent projects based on **platform purpose**, not CarClever version number.
- Apply explicit Git branch deployment filtering.
- Stop obsolete/research projects from reacting to every branch push.
- Retain only one deliberate short-URL Preview harness if ChatGPT still needs it.
- Treat `release/vN` branches as candidate versions, not permanent hosting identities.

## 4. Did Preview fan-out cause the intermittent V2 auto-deployment problem?

**Not proven.** The evidence is sufficient to say the V2 production deployment did not reliably update from every intended push — several no-op “nudge” commits and later administrative corrections document that manual deployment/redeployment was sometimes needed. But the current evidence does not prove that other projects' Preview builds caused that behavior.

Cross-project fan-out can still be a contributing operational risk because it creates unnecessary builds, webhook activity, queue/noise, and ambiguous dashboard state. Removing it is worthwhile even if it turns out not to be the root cause.

The correct next diagnostic is controlled, after branch filtering is applied:

1. Push a deliberate harmless test change/commit through the approved Engineering workflow.
2. Verify only the intended Vercel project reacts.
3. Verify the correct deployment target is `production` for the production branch.
4. Verify deployment metadata points to the exact expected SHA.
5. Repeat once to establish whether automatic deployment is now deterministic.
6. If a production deploy still fails, investigate Vercel/GitHub integration/webhook/project settings directly rather than attributing it to Preview fan-out.

There is no documented Vercel feature in the reviewed material that assigns an arbitrary **project A before project B deployment priority** to several projects responding to one Git push. Build concurrency/queue controls exist, but they are not a substitute for correct branch scoping. The strategic fix is to prevent unrelated projects from building in the first place.

## 5. Platform-policy asymmetry is the key design constraint

Claude and OpenAI should normally run the same CarClever release, but their publication rules differ enough that they should not be forced to share one deployment lifecycle.

### Claude / Anthropic

The submitted V1 Claude connection was recorded as:

`https://carclever-find-my-car.vercel.app/mcp`

Anthropic's current documentation states that a published MCP server is a live API: adding, changing, or removing tools is done by deploying the server change and **does not require resubmission or scheduled re-review**. Listing metadata is managed separately; some listing edits require review, and the published directory slug is permanent.

Anthropic's public documentation reviewed on 2026-09-10 does **not** explicitly document a self-service procedure for replacing the published MCP server hostname/origin. Its listing-management guidance says other edits/escalations should go through `mcp-review@anthropic.com`.

**Safest strategy:** if V1 is approved/published, keep the Claude MCP URL stable and upgrade the code behind that same endpoint from V1 to V2 after the V2 release is accepted for Claude production. Do not change Claude's hostname merely to make it match OpenAI.

### OpenAI

OpenAI's current plugin documentation is stricter about the MCP origin:

- public MCP submissions use a production MCP URL and require domain verification;
- tool/schema/description/annotation/resource-contract changes require a new plugin version review;
- server-only fixes that preserve the published contract can deploy without a new version;
- **the MCP origin — scheme, hostname, or port — cannot change between versions of an existing published plugin; changing it requires creating and reviewing a new plugin**.

Therefore the hostname chosen for the V2 OpenAI resubmission is a long-term architectural decision, not a disposable test URL.

## 6. Recommended permanent MCP URL strategy

### Claude channel

Keep the already-submitted Vercel origin:

`https://carclever-find-my-car.vercel.app/mcp`

Reason: it is the URL Anthropic reviewed/submitted for V1. If V1 becomes approved/published, retaining that origin minimizes platform-change risk. V2/V3 are then code upgrades behind the existing Claude endpoint.

### OpenAI channel

Do **not** submit the long-term OpenAI plugin on a hostname we expect to discard, such as a version-labelled temporary test origin, if a permanent branded origin can be safely established first.

Preferred candidate:

`https://carclever.getcarwise.app/mcp`

This is proposed, not yet approved for execution. Before using it, Claude Engineering must verify:

1. the domain's current Vercel ownership/routing;
2. that moving/attaching it to the intended OpenAI production project does not break V1, widget CSP/resource metadata, any website integration, or an existing connector;
3. production TLS/DNS and `/mcp` behavior;
4. OpenAI domain-challenge hosting at the required `/.well-known/openai-apps-challenge` location;
5. the exact V2 SHA is what the hostname serves;
6. all final submission tests pass against that exact branded hostname.

Using the apex `https://getcarwise.app/mcp` is **not recommended** for this release because the apex is the main website surface and the website-app architecture is intentionally a separate workstream. A dedicated CarClever subdomain gives cleaner ownership and fewer accidental dependencies.

### Why two different MCP URLs are acceptable and preferable

The goal is not “one hostname everywhere.” The goal is **one code product, two stable platform front doors**.

The two platforms may have different permanent MCP origins while still serving the exact same Git SHA and behavior. This preserves platform approval independence while avoiding code drift.

## 7. If V1 and V2 are both approved, what happens?

Assuming Claude V1 is approved/published and OpenAI V2 is approved/published:

1. OpenAI serves the tested V2 release through its permanent OpenAI MCP origin.
2. Claude initially remains on V1 through its existing MCP origin until André authorizes the Claude upgrade.
3. Re-run the V2 acceptance suite specifically for the Claude production channel.
4. Advance the Claude production deployment to the exact same tested V2 release SHA.
5. Keep the Claude MCP hostname unchanged.
6. Smoke-test the live Claude directory connector.
7. Record that both platform channels now converge on the same V2 SHA.

This is safer than changing Claude's MCP URL to the OpenAI URL after approval.

If Anthropic review is still active, do **not** change V1 `main`, its Vercel production, or its submitted endpoint. OpenAI V2 remains independently deployable and submittable through its own channel.

## 8. Future V3 release strategy

Current V3 work should **not** be merged wholesale into current V2. Live Git comparison shows the paused V3 branch has diverged and is substantially behind the now-amended `release/v2` line.

The future V3 process should be:

1. Finalize/freeze the accepted V2 release baseline.
2. Create a fresh `release/v3` (or equivalent approved release candidate) **from the final V2 baseline**.
3. Claude selectively ports the still-valid V3-specific work from the paused V3 branch.
4. Run the complete regression/equivalence suite so V2 fixes cannot be silently lost.
5. Test V3 on both ChatGPT and Claude hosts.
6. Promote to each platform channel separately when that platform's rules/gates permit.

Platform behavior:

- **OpenAI:** if V3 changes tools, schemas, descriptions, annotations, resource metadata, or other reviewed MCP metadata, create a new version of the existing plugin, scan, submit for review, then publish after approval. Keep the same OpenAI MCP origin.
- **Claude:** at the same existing MCP server, Anthropic currently says tool additions/changes/removals can deploy without resubmission. Still run full production compatibility/smoke testing and follow any listing-review requirement if public listing metadata also changes.

Thus V3 should be “new release behind the same platform front doors,” not “new permanent MCP hostname.”

## 9. Recommended Git strategy

### Near term while V1 Anthropic status is unresolved

- `main` stays untouched as V1.
- `release/v2` remains the current V2 release candidate.
- do not merge old PR #1 or #2 into `main` merely because V2 is now ready;
- V3 remains paused until the V2 platform strategy is settled.

### Long-term model

Recommended lightweight release model:

- `main` — canonical stable baseline after a release has been accepted as the common production baseline.
- `release/vN` — immutable-ish release candidate/integration line for the next public version.
- short-lived feature/fix branches — merge into the active release candidate, then close/delete after verification.
- optional platform deployment pointer branches (`deploy/claude`, `deploy/openai`) should be introduced **only if** platform approval timing repeatedly makes `main` insufficient. They are not required immediately.

The objective is to avoid permanent branch proliferation while still allowing platform version skew when needed.

## 10. PR #1 and PR #2 disposition

### PR #1 — `fix/total-matches-count-bug` → `main`

Live Git comparison shows PR #1 head `6700bbb` is an ancestor of current `release/v2`; current V2 is 91 commits ahead with no commits behind relative to that head. Its work has therefore already been absorbed into V2.

The original **DO NOT MERGE YET** instruction was valid because V1 `main` was under review and had to remain frozen. That does not mean the old PR should now be merged. Its correct successor is the current consolidated `release/v2` release, not a late merge of this historical branch into V1.

**Proposed disposition:** close as superseded after André approves the release strategy; preserve the PR/history. Do not merge.

### PR #2 — `feature/edmunds-two-button-cta` → `main`

The V2.2 deterministic Edmunds work through its earlier V2 baseline is already incorporated into current `release/v2`. The PR branch later accumulated additional V3/check-vehicle-era commits and now diverges from current V2.

That makes the PR especially unsuitable for a late merge into `main`: it mixes an already-incorporated V2 history with stale V3-specific work.

**Proposed disposition:** close as superseded after André approves the release strategy; preserve the PR/history. Do not merge. Future V3-specific content should be selectively ported onto a fresh V3 branch based on final V2.

Any PR close/branch cleanup in the application repository must be executed by Claude Engineering, not ChatGPT.

## 11. `ccfmc-dev`: do not delete yet

`ccfmc-dev` was not arbitrary clutter. Project documentation records a confirmed ChatGPT Apps SDK Preview-domain problem: long Vercel preview/branch-alias hostnames could be transformed into an invalid DNS label, while Claude did not hit the same rendering mechanism. The short-named `ccfmc-dev` project plus short throwaway branches was created as the ChatGPT test workaround.

Because that solved a real platform-specific failure, immediate deletion is not justified.

**Proposed safe state:** convert it from “legacy project that auto-builds everything” into a **dormant/manual ChatGPT Preview Test Harness**:

- block unrelated automatic Git deployments;
- allow only explicitly chosen short test branches or manual deployments;
- confirm no current production/domain dependency;
- keep it through the final V2 submission and first post-release cycle as fallback;
- delete only after the replacement automated test process proves the short-URL workaround is no longer needed.

## 12. `carclever-v2-schema-probe`: purpose is complete

The schema-probe project was explicitly temporary/research-only. Its purpose was to test the V2 shared-contract design without Auto.dev/NHTSA/search behavior and without affecting V1/V2/V3 production.

That discovery has now been folded into the real V2 implementation and connector validation, so the probe has fulfilled its purpose.

**Proposed safe retirement:** 

1. stop automatic Git deployments / disconnect its Git trigger after André approval;
2. disconnect/remove any temporary probe connector;
3. keep the Git research branch and documentation as historical evidence;
4. retain the inert Vercel project through the final V2 submission smoke test in case evidence needs to be reproduced;
5. then delete the Vercel project once a dependency check confirms no connector/domain/test process points to it.

Vercel does not need a permanent version-specific schema project after this investigation.

## 13. Proposed Vercel project matrix

| Project | Strategic role | Production branch / source | Automatic deployment policy | Long-term disposition |
|---|---|---|---|---|
| `carclever-find-my-car` | Claude production channel | `main` for current V1; later exact approved common release | Production only from deliberate Claude production branch; suppress unrelated V2/V3 previews | KEEP — permanent Claude front door |
| `ccfmc-dev-v2` | Current V2 / candidate OpenAI production channel | `release/v2` now | Only active V2/release testing branches until cutover | KEEP/REPURPOSE as OpenAI production channel if permanent branded origin is attached and verified |
| `ccfmc-dev-v3` | Current paused V3 test project | paused V3 branch | V3-only while retained | RETIRE after new release-channel model is working; future V3 should not require a permanent version-specific Vercel project |
| `ccfmc-dev` | ChatGPT short-URL Preview test harness | manual/short test branch | Deny broad auto-deploy; explicit test only | KEEP temporarily, then delete only after replacement proven |
| `carclever-v2-schema-probe` | Completed research probe | none once inactivated | Disable | INACTIVATE now after approval; delete after final V2 smoke/dependency check |

`getcarwise-app` / `carclever-widget` is outside this matrix and remains a separate website/widget workstream, per André's instruction.

## 14. Testing and release acceptance architecture

The existing V1→V2 equivalence gate is sound. The next improvement is to make it repeatable and increasingly automated.

### Layer A — commit/contract CI

Run for every release-candidate SHA:

- build;
- typecheck;
- unit/custom regression suite;
- MCP initialize and `tools/list`;
- schema/description/annotation snapshots;
- exact server/version SHA marker where available;
- deterministic fixtures for V1/V2 search semantics.

### Layer B — deployed-environment verification

Before host testing:

- confirm the intended Vercel project received the deployment;
- confirm deployment target (Preview versus Production);
- confirm Git branch and exact SHA;
- confirm MCP initialize/tools/resources are reachable;
- confirm widget resource/CSP/origin behavior;
- confirm no unrelated Vercel project built the branch after isolation rules are installed.

### Layer C — same-window V1 vs candidate A/B

Because live inventory changes, compare semantics rather than requiring identical VINs:

- same user prompt;
- host-supplied tool input;
- effective hard constraints;
- relaxations;
- candidate/result set and evidence;
- priority ordering;
- latency;
- any host routing omission.

Use the current `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md` as the baseline methodology.

### Layer D — cross-host acceptance

Run the same curated prompt pack through both ChatGPT and Claude:

- direct filters;
- practical needs/model resolution;
- required/preferred electrification;
- hybrid/PHEV/EV mixed cases;
- price/budget/cheapest/newest/lowest-mileage/lower-risk axes;
- VIN/Buyer Check;
- CPO/history/unknown evidence;
- location modes;
- zero/thin-result widening;
- negative/out-of-scope prompts;
- result-card rendering and links.

Host-model behavior cannot be fully replaced by raw MCP unit tests; actual ChatGPT and Claude connector tests remain a release gate because tool selection and argument construction are part of the product.

### Layer E — exact submission endpoint

Immediately before submission:

- test the exact hostname submitted to that platform;
- verify it serves the intended SHA;
- rerun Scan Tools / equivalent metadata read;
- run the platform submission test cases;
- inspect UI/images/links;
- record a release manifest.

### Layer F — post-release monitoring

After publication/cutover:

- Vercel runtime error/latency checks;
- connector health;
- targeted smoke prompts;
- rollback SHA/deployment retained;
- compare platform channels and alert/document if they are intentionally on different releases.

## 15. What ChatGPT can and cannot do in this test model

ChatGPT Business/Strategy can independently:

- inspect and compare GitHub branches, commits, PRs, and release evidence read-only;
- inspect Vercel project/deployment metadata and logs when exposed through the connector;
- verify whether the intended SHA was deployed;
- design the regression/equivalence suite;
- review Claude's implementation claims and diffs independently;
- compare platform test records and decide whether a release gate is satisfied;
- maintain the strategy/audit/release documentation.

ChatGPT can directly exercise CarClever through a live connector only when that connector is exposed in the current ChatGPT tool environment. It should never claim a host-level test passed merely from Git/Vercel evidence.

Claude Engineering should implement CI/test automation, change Vercel/Git settings, create/deploy release candidates, and run Engineering-owned deployment procedures. ChatGPT then independently verifies the evidence and business/release gate.

## 16. Release manifest — required going forward

For every V2/V3/... promotion, create one release record containing at minimum:

- release version;
- canonical Git SHA;
- release branch;
- Claude production SHA + MCP URL + status;
- OpenAI production SHA + MCP URL + status;
- Vercel deployment IDs;
- tool/schema/resource fingerprint or captured scan;
- automated test counts/status;
- live ChatGPT acceptance status;
- live Claude acceptance status;
- V1/previous-release A/B result if applicable;
- submission/review version/status;
- known exceptions;
- rollback deployment/SHA.

This should become the definitive answer to “what code is each platform serving?” rather than inferring from the newest Vercel row.

## 17. Immediate proposed sequence for V2

**No execution until André confirms the relevant decisions.**

1. Confirm current Anthropic V1 review state.
2. Approve the two-platform/stable-origin strategy.
3. Decide whether `carclever.getcarwise.app` is the preferred permanent OpenAI origin, subject to dependency verification.
4. Have Claude implement Vercel branch isolation without touching the frozen V1 production state if review is still active.
5. Inactivate schema-probe auto deployments; retain it briefly as inert evidence.
6. Convert `ccfmc-dev` to explicit/manual short-URL test-harness status rather than deleting it.
7. Verify PR #1/#2 ancestry/supersession in Claude's own Engineering review and close them as superseded — do not merge — after André approves.
8. Re-run exact V1/V2 comparison/acceptance testing.
9. Configure and verify the permanent OpenAI MCP origin.
10. Run the final test pack against that exact origin.
11. Generate the OpenAI submission/release manifest and resubmit V2.
12. If/when Claude V1 is approved and André wants V2 live there, test then deploy the exact V2 SHA behind Claude's existing MCP origin.
13. Only after V2 is stable on the intended platform channels, restart V3 from a fresh V2-based branch.

## 18. Decisions still pending André

- **D1:** Current Anthropic V1 state: in review / approved-published / changes requested-rejected / withdrawn.
- **D2:** Approve “one codebase, two stable platform front doors, sync-first same SHA” as the operating model.
- **D3:** Approve `carclever.getcarwise.app` as the preferred OpenAI V2 origin candidate, subject to technical dependency validation.
- **D4:** Approve branch-isolation cleanup before final V2 testing.
- **D5:** Approve keeping `ccfmc-dev` temporarily as a dormant/manual short-URL ChatGPT test harness.
- **D6:** Approve inactivating the V2 schema probe now, with deletion only after final V2 smoke/dependency verification.
- **D7:** Approve closing PR #1 and PR #2 as superseded after Claude independently confirms the ancestry findings; do not merge either PR.
- **D8:** Approve future V3 being rebuilt/ported onto the final V2 baseline rather than merging the paused stale V3 branch wholesale.

## 19. Current references

Internal project records:

- `AUDIT_CARCLEVER_GITHUB_VERCEL_ENVIRONMENT_MAPPING_20260910.md`
- `CURRENT_V2_STATE_20260909.md`
- `V2_CONNECTOR_TEST_RECORD_20260909.md`
- `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md`
- `CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md`
- `STATE.md`, `DECISIONS.md`, `TASKS.md`, `PLAYBOOK.md`, `REFERENCE.md`, `WORKFLOW_ARCHITECTURE.md`

Current external policy references reviewed 2026-09-10:

- OpenAI MCP server review / maintenance: `https://developers.openai.com/plugins/deploy/app-review`
- OpenAI submission flow: `https://developers.openai.com/plugins/deploy/submission`
- Anthropic post-publication connector management: `https://claude.com/docs/connectors/building/after-publishing`
- Anthropic directory listing management: `https://claude.com/docs/connectors/building/managing-your-listing`
- Anthropic submission flow: `https://claude.com/docs/connectors/building/submission`
- Vercel Preview/Git deployment documentation and current Git configuration guidance.
