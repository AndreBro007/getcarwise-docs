# CarClever Cross-Platform Release and Deployment Strategy — 2026-09-10

**Status:** PROPOSED — pending André confirmation before infrastructure or application-repository changes  
**Scope:** Long-term GitHub/Vercel/version/release strategy for CarClever - Find My Car across Claude and OpenAI, including stable MCP origins, V1→V2→V3 promotion, Preview behavior, stale PR disposition, temporary Vercel projects, and final test/release process.  
**Execution boundary:** Business/Strategy guidance only. Claude Engineering owns application code, Git branch/PR mutations in `carclever-find-my-car`, Vercel settings, deployments, domains, connectors, and production cutovers.

## 1. Executive recommendation

The current multi-project setup was a sensible **temporary isolation mechanism** while V1 was frozen in Anthropic review and V2/V3 needed independent testing. It should not become the permanent release model.

Preferred long-term architecture:

1. **One application codebase:** `AndreBro007/carclever-find-my-car`.
2. **Versioned release candidates:** `release/v2`, future `release/v3`, etc.
3. **Two permanent platform production channels:** Claude and OpenAI, because their review/update rules differ and temporary version skew can be legitimate.
4. **One permanent shared release-test harness:** retain the short-named `ccfmc-dev` while its ChatGPT Preview-domain workaround remains useful; make it deliberate/manual rather than broad auto-deploy.
5. **Stable MCP origin per platform:** do not create a new public hostname for every CarClever version.
6. **Sync-first policy:** both platforms serve the same tested release SHA whenever review gates permit. Temporary skew exists only because an external platform has not yet cleared the release.
7. **Previews are test artifacts, never releases.**
8. **Research projects are temporary and inert when finished.**
9. **Every promotion is SHA-driven:** release records identify the exact Git SHA, deployment, MCP origin, contract snapshot, tests, platform status, and rollback point.

Key distinction:

- **Version** = V1, V2, V3 code/release state.
- **Platform channel** = Claude production versus OpenAI production.

A version is promoted through platform channels; it should not require a permanent Vercel project named after every version.

## 2. Preview deployments: what they are and when they merge

A Vercel Preview deployment is an isolated build of a Git branch/commit. It does **not** merge into another Git branch and does **not** later merge itself into Production.

Normal flow:

`feature/release branch push → Vercel Preview → test/review → deliberate Git/release action → Production deployment`

Therefore a V2 Preview appearing inside the V3 Vercel project remains a V2 commit built by the V3 project. It never becomes V3, `main`, or another release branch unless a person/automation explicitly changes Git. Production can also be changed by deliberately promoting a deployment, but that changes Vercel traffic and still does not rewrite Git history.

The observed fan-out is an **environment-isolation/noise problem**, not a hidden merge mechanism.

## 3. Was the current multi-Vercel-project design wrong?

No. It solved real temporary requirements:

- V1 remained frozen while V2/V3 continued;
- V2 had a real production-target test environment;
- V3 had an independent environment;
- the schema probe isolated host-contract research;
- `ccfmc-dev` solved a confirmed ChatGPT/Vercel Preview-domain length problem.

What has become suboptimal is allowing five projects connected to the same application repository to react broadly to unrelated branches. Permanent projects should now be defined by **platform/test purpose**, not version number.

## 4. Did Preview fan-out cause V2's intermittent auto-deployment problem?

**Not proven.** V2 records show production did not reliably update from every intended push: multiple no-op “nudge” commits and later documentation corrections record that a manual deployment/redeployment could be required. Current evidence does not prove other projects' Preview builds caused this.

Fan-out is still worth removing because it adds unnecessary builds, webhook activity, queue/noise, resource use, and dashboard ambiguity.

After branch filtering is installed, Claude Engineering should perform a controlled deployment-trigger test:

1. issue one harmless, deliberate Engineering test commit/change;
2. verify only the intended project reacts;
3. verify target = Production for the production branch;
4. verify the exact expected SHA;
5. repeat once;
6. if it still fails, diagnose Vercel/GitHub integration/webhook/project settings directly.

No reviewed Vercel documentation exposed a per-project “deploy project A before project B” priority control. Build concurrency/queue controls exist, but the correct design is to stop unrelated projects from reacting at all.

## 5. Platform-policy asymmetry drives the permanent architecture

### Claude / Anthropic

The submitted V1 Claude connection is recorded as:

`https://carclever-find-my-car.vercel.app/mcp`

Anthropic's current documentation says a published MCP server is a live API: adding/changing/removing tools is done by deploying the server and **does not require resubmission or scheduled re-review**. Listing metadata is separate; some listing edits require review, and the directory slug is permanent.

The reviewed Anthropic documentation does not explicitly describe a self-service, no-review replacement of the published server hostname/origin. Listing guidance directs “other edits or escalations” to `mcp-review@anthropic.com`.

**Safest Claude strategy:** if V1 is approved/published, keep its MCP URL stable and later deploy the tested V2/V3 release behind that same origin. Do not change Claude's hostname merely to match OpenAI.

### OpenAI

OpenAI's current rules are stricter:

- a public MCP submission uses a production MCP URL and domain verification;
- tool/schema/description/annotation/resource-contract changes require a new reviewed plugin version;
- server-only changes that preserve the published contract can deploy without a new version;
- **the MCP origin (`scheme`, `hostname`, `port`) cannot change between versions of a published plugin; changing it requires a new plugin and full review/publication flow**.

Therefore the hostname selected for the OpenAI V2 resubmission must be treated as permanent infrastructure.

## 6. Recommended permanent MCP URL strategy

### Claude channel

Keep:

`https://carclever-find-my-car.vercel.app/mcp`

This is the submitted Anthropic V1 origin. Retaining it minimizes approval/review risk. V2/V3 become code releases behind the same Claude front door.

### OpenAI channel — revised preferred candidate

**Preferred first choice:**

`https://findmycar.getcarwise.app/mcp`

This is stronger than moving `carclever.getcarwise.app` immediately because:

- the repository/project plan already recorded `findmycar.getcarwise.app` as the intended permanent Find My Car custom domain (“set up once ready to deploy for real”);
- current records identify `carclever.getcarwise.app` as attached to the V1 production project, so moving it while the Anthropic gate is unresolved would touch V1 infrastructure unnecessarily;
- `findmycar.getcarwise.app` is product-specific, platform-neutral, branded under GetCarWise, and avoids coupling the OpenAI origin to the internal Vercel project name `ccfmc-dev-v2`;
- OpenAI origin-lock rules make choosing a long-lived owned hostname now materially safer than submitting a version-labelled `.vercel.app` test hostname.

**Alternative:** `https://carclever.getcarwise.app/mcp` remains a good brand candidate only if a later dependency audit proves it can be reassigned/used without affecting V1, its widget metadata/CSP, website integrations, or any approved connector. It should not be moved while V1 is gated merely for naming consistency.

Using the apex `https://getcarwise.app/mcp` is not recommended because the apex is the main website surface and the website-app architecture is intentionally a separate workstream.

Before any OpenAI production-domain decision is executed, Claude Engineering must verify:

1. DNS/domain ownership and current routing;
2. the subdomain is not already used by another production dependency;
3. V2 accessed through that hostname declares compatible widget/resource/CSP origin metadata — do not assume Vercel's production-domain environment value resolves to the custom domain without live proof;
4. TLS and `/mcp` behavior;
5. OpenAI challenge-token hosting at `/.well-known/openai-apps-challenge`;
6. exact deployed V2 SHA;
7. Scan Tools and complete final acceptance tests against the exact hostname.

### Why two different MCP URLs are preferable

The goal is not one hostname everywhere. The goal is **one code product, two stable platform front doors**. Claude and OpenAI may have different permanent MCP origins while serving the exact same code SHA and behavior. That isolates approval lifecycles without creating separate code products.

## 7. If V1 and V2 are both approved, what happens?

Assuming Claude V1 is approved/published and OpenAI V2 is approved/published:

1. OpenAI serves the tested V2 release through its permanent OpenAI origin.
2. Claude remains on V1 until André authorizes its V2 production upgrade.
3. Re-run V2 acceptance specifically for the Claude production channel.
4. Deploy the **same tested V2 release SHA** behind Claude's existing origin.
5. Keep Claude's MCP hostname unchanged.
6. Smoke-test the live Claude directory connector.
7. Record both channels converged on the same V2 SHA.

If Anthropic V1 is still in review, do not change V1 `main`, its Vercel production, or its submitted endpoint. OpenAI V2 remains independent and can proceed on its own permanent origin.

## 8. Future V3 release strategy

Current V3 should **not** be merged wholesale into current V2. Live Git comparison shows the paused V3 branch is diverged and substantially behind amended `release/v2`.

Future V3 process:

1. freeze the accepted V2 baseline;
2. create fresh `release/v3` from final V2;
3. Claude selectively ports still-valid V3-specific work from the paused branch;
4. run full V2 regression/equivalence tests;
5. run ChatGPT + Claude host acceptance;
6. promote the V3 release separately to each platform channel when that platform's gate permits.

### OpenAI V3 nuance

After V2 is published on OpenAI, the production MCP endpoint remains live while any V3 metadata version is under review. OpenAI explicitly warns that breaking contract changes can break the currently published version immediately. Therefore future V3 changes exposed on the OpenAI production origin must be **backward-compatible during the review transition**: add rather than prematurely remove/rename, keep old contracts working, submit the new metadata snapshot, publish the approved version, and only retire compatibility when platform rules safely permit it. If a truly breaking origin change is required, that is a new plugin.

### Claude V3

At the same existing MCP server, Anthropic currently states tool additions/changes/removals can deploy without resubmission. Still run full regression and production smoke tests; public listing metadata changes may have their own review requirement.

V3 is therefore a new release behind the same two platform front doors, not a new permanent MCP hostname.

## 9. Recommended Git strategy

### Current transition

- `main` remains V1 while the Anthropic status is unresolved.
- `release/v2` remains the V2 release candidate.
- do not merge historical PR #1/#2 into `main` simply because V2 is ready.
- V3 remains paused until this platform/release strategy is confirmed.

### Target release model

- `main` — canonical common stable baseline once a release is accepted as the shared production baseline.
- `release/vN` — next release candidate/integration branch.
- short-lived feature/fix branches — merge into the active release candidate and close/delete after verification.
- if independent platform timing remains common, use lightweight stable deployment pointer branches such as `prod/claude` and `prod/openai`, each advanced only to an already-tested release SHA. This permits one platform to remain on V1/V2 while the other advances, without maintaining separate code forks.

Once that model is adopted, Vercel production projects should react only to their intended production branch; the shared `ccfmc-dev` test harness handles release/feature testing deliberately.

## 10. PR #1 and PR #2 disposition

### PR #1 — `fix/total-matches-count-bug` → `main`

Live Git comparison shows head `6700bbb` is an ancestor of current `release/v2`; V2 is far ahead with none of PR #1 missing from its ancestry. The original **DO NOT MERGE YET** gate protected V1 during review. Today the PR is superseded by the consolidated V2 release.

**Proposed:** close as superseded after André approves strategy and Claude independently verifies ancestry. Do not merge.

### PR #2 — `feature/edmunds-two-button-cta` → `main`

The V2.2 deterministic Edmunds baseline is already in current `release/v2`, while the old PR branch later accumulated V3/check-vehicle-era commits and diverged from current V2. A late merge to `main` would mix already-incorporated V2 history with stale V3 content.

**Proposed:** close as superseded after André approves strategy and Claude independently verifies. Do not merge. Future V3 content is selectively ported onto fresh V3 from final V2.

PR/branch mutations in the application repository belong to Claude Engineering.

## 11. `ccfmc-dev`: keep and repurpose, do not delete yet

`ccfmc-dev` was created to solve a documented ChatGPT Apps SDK Preview-domain problem: long Vercel branch aliases could collapse into an invalid DNS label, while Claude did not have that rendering failure.

That makes it useful as the **one permanent shared release/Preview test harness** if we constrain it properly:

- deny broad automatic Git deployments;
- deploy only explicitly selected release/short test branches;
- keep the short hostname that is known to work with ChatGPT;
- use it for pre-production MCP/widget smoke tests across future releases;
- delete only if a replacement test setup is proven to eliminate the original short-URL need.

This is safer than deleting a known-good platform-specific fallback now.

## 12. `carclever-v2-schema-probe`: purpose complete

The schema probe was explicitly temporary/research-only and its findings have now been incorporated into V2 implementation and connector testing.

**Proposed retirement:** 

1. disable automatic Git deployments / disconnect Git trigger after approval;
2. remove/disconnect the temporary probe connector if one remains;
3. retain Git research branch + documentation as historical evidence;
4. keep the inert Vercel project only through the final V2 smoke/submission window;
5. delete it after confirming no domain/connector/test dependency points to it.

## 13. Proposed Vercel project matrix

| Project | Strategic role | Source | Auto-deployment policy | Long-term disposition |
|---|---|---|---|---|
| `carclever-find-my-car` | Claude production channel | current `main`; later approved Claude deployment branch/release | production-channel only; suppress unrelated previews | **KEEP** — permanent Claude front door; preserve submitted default URL |
| `ccfmc-dev-v2` | current V2 and candidate OpenAI production channel | `release/v2` now; later OpenAI prod pointer/release | OpenAI channel + deliberate release transition only | **KEEP/REPURPOSE** behind permanent owned OpenAI custom domain |
| `ccfmc-dev` | shared short-URL release test harness | explicit release/test branches only | manual/allowlisted only | **KEEP** while short-URL need remains |
| `ccfmc-dev-v3` | paused V3 version-specific project | paused V3 branch | V3-only until migration | **RETIRE** after fresh V3 uses shared release process |
| `carclever-v2-schema-probe` | completed research probe | none once inactivated | disable | **INACTIVATE**, then delete after final V2 dependency check |

`getcarwise-app` / `carclever-widget` is a separate website/widget workstream and remains outside this Find My Car release matrix unless a critical dependency is discovered.

## 14. Testing and release acceptance architecture

The existing V1→V2 equivalence gate is sound. Make it repeatable through six layers.

### A — commit/contract CI

- build, typecheck, unit/custom regression tests;
- MCP initialize and `tools/list`;
- schema/description/annotation/resource snapshots;
- exact version/SHA marker where available;
- deterministic captured provider/NHTSA fixtures.

### B — deployed-environment verification

- intended Vercel project only;
- correct Preview/Production target;
- exact branch + SHA;
- MCP initialize/tools/resources reachable;
- widget resource/CSP/origin behavior;
- verify unrelated projects did not build after isolation rules.

### C — same-window V1 vs candidate A/B

Compare semantics, not identical VINs: user prompt, host arguments, effective hard constraints, relaxations, candidate/result evidence, ordering, latency, routing omissions. Use `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md` as baseline.

### D — cross-host acceptance

Run the same curated high-value/negative prompt pack through ChatGPT and Claude. Host tool selection and argument construction are part of the product and cannot be fully replaced by raw MCP tests.

### E — exact submission endpoint

Immediately before submission/publication: exact hostname, exact SHA, Scan Tools/equivalent, positive + negative submission cases, UI/images/links, release manifest.

### F — post-release monitoring

Runtime errors/latency, connector health, targeted smoke prompts, rollback deployment retained, and explicit record if platform channels temporarily serve different releases.

## 15. ChatGPT/Claude responsibility in testing

ChatGPT Business/Strategy can independently inspect/compare GitHub refs and evidence, inspect Vercel metadata/logs when exposed, verify deployed SHA, design/score regression gates, review Claude implementation claims/diffs, and maintain audit/release docs.

ChatGPT can perform actual CarClever host-level calls only when the relevant CarClever connector is exposed in that ChatGPT test environment. Git/Vercel evidence alone must never be called a passing ChatGPT connector test.

Claude Engineering implements CI/test automation, application changes, deployment settings, release branches, Vercel/domain changes, and production cutovers. ChatGPT independently verifies the resulting evidence and release gate.

## 16. Release manifest required going forward

Every public promotion should record at minimum:

- version + canonical Git SHA + release branch;
- Claude production SHA/MCP URL/status;
- OpenAI production SHA/MCP URL/status;
- Vercel deployment IDs;
- tool/schema/resource fingerprint or scan;
- automated test status/counts;
- ChatGPT live acceptance status;
- Claude live acceptance status;
- previous-release A/B status;
- submission/review version/status;
- exceptions + rollback SHA/deployment.

This becomes the definitive answer to “what code is each platform serving?” rather than inferring from Vercel's newest row.

## 17. Immediate proposed V2 sequence

1. Confirm Anthropic V1 review state.
2. Approve the one-codebase/two-stable-platform-front-doors/sync-first model.
3. Approve `findmycar.getcarwise.app` as first-choice OpenAI V2 permanent-origin candidate, subject to DNS/dependency/live-origin validation.
4. Claude implements Vercel branch isolation without changing frozen V1 production if review remains active.
5. Inactivate schema-probe auto deployments; retain it briefly as inert evidence.
6. Repurpose `ccfmc-dev` as explicit/manual shared short-URL release test harness.
7. Claude rechecks PR #1/#2 ancestry and closes them as superseded after André approval; do not merge.
8. Re-run exact V1/V2 comparison/acceptance testing.
9. Configure and verify permanent OpenAI MCP origin.
10. Run final test pack against that exact origin.
11. Produce release/submission manifest and resubmit V2 to OpenAI.
12. If/when Claude V1 is approved and André wants V2 live there, test then deploy exact V2 SHA behind Claude's existing origin.
13. After V2 stability, create fresh V3 from final V2 and selectively port V3 work.

## 18. Decisions pending André

- **D1:** Current Anthropic V1 state: in review / approved-published / changes requested-rejected / withdrawn.
- **D2:** Approve “one codebase, two stable platform front doors, one shared test harness, sync-first same SHA” as operating model.
- **D3:** Approve `findmycar.getcarwise.app` as preferred OpenAI V2 origin candidate, subject to technical verification; keep `carclever.getcarwise.app` on V1 unless/until separately cleared.
- **D4:** Approve branch-isolation cleanup before final V2 testing.
- **D5:** Approve retaining/repurposing `ccfmc-dev` as manual shared short-URL test harness.
- **D6:** Approve inactivating V2 schema probe now, deletion only after final V2 dependency verification.
- **D7:** Approve closing PR #1/#2 as superseded after Claude independently confirms; do not merge.
- **D8:** Approve future V3 being rebuilt/ported onto final V2 rather than merging paused stale V3 wholesale.
- **D9:** Decide whether to introduce stable `prod/claude` / `prod/openai` deployment-pointer branches during/after the V2 transition. Recommended if platform approval skew becomes a recurring condition.

## 19. References

Internal:

- `AUDIT_CARCLEVER_GITHUB_VERCEL_ENVIRONMENT_MAPPING_20260910.md`
- `CURRENT_V2_STATE_20260909.md`
- `V2_CONNECTOR_TEST_RECORD_20260909.md`
- `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md`
- `CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md`
- `STATE.md`, `DECISIONS.md`, `TASKS.md`, `PLAYBOOK.md`, `REFERENCE.md`, `WORKFLOW_ARCHITECTURE.md`

External policy reviewed 2026-09-10:

- OpenAI: `https://developers.openai.com/plugins/deploy/app-review`
- OpenAI: `https://developers.openai.com/plugins/deploy/submission`
- Anthropic: `https://claude.com/docs/connectors/building/after-publishing`
- Anthropic: `https://claude.com/docs/connectors/building/managing-your-listing`
- Anthropic: `https://claude.com/docs/connectors/building/submission`
- Vercel: current Preview/Git deployment, branch tracking, and build-management documentation.
