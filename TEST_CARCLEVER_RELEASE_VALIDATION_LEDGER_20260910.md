# CarClever Release Validation Ledger — started 2026-09-10

**Status:** ACTIVE living release record  
**Purpose:** Preserve a chronological, exact-SHA record of CarClever validation across local/CI tests, deployed environments, ChatGPT, Claude, OpenAI/Anthropic review gates, production promotion and post-release smoke tests.  
**Rule:** A release is not complete because code was written or because one host passed. Every production change must have a ledger entry, even when the platform itself does not require a new reviewed version.

## 1. Release-control model

Target flow:

`feature/fix → release/vN → exact candidate SHA → test/current → carclever-test.getcarwise.app/mcp → ChatGPT + Claude acceptance → prod/openai and/or prod/claude → exact production smoke → main/shared baseline when appropriate`

Terms:

- **Preview:** Vercel build only; never a Git merge.
- **Release-candidate merge:** feature/fix work intentionally merged into `release/vN`.
- **Test promotion:** `test/current` points at an exact candidate SHA and the stable shared test host serves it.
- **Platform promotion:** `prod/openai` or `prod/claude` points at an exact candidate/release SHA already accepted through the shared test host.
- **Canonical merge:** completed release becomes the common stable baseline in `main` after the agreed release gate. Historical PR #1/#2 are not the future canonical merge mechanism.

## 2. Mandatory release record fields

Every candidate/release event must record:

| Field | Required evidence |
|---|---|
| Version / release label | V1, V2, V3, hotfix identifier, etc. |
| Candidate Git SHA | Full SHA preferred; short SHA allowed in summary only |
| Source branch | `release/vN` or approved hotfix branch |
| Contract fingerprint | tools, descriptions, input/output schemas, annotations, resource URIs |
| Automated verification | build, typecheck status, unit/custom tests, fixtures, MCP initialize/tools/resources |
| Test deployment | Vercel project, deployment ID/URL, target, Git branch, exact SHA |
| Shared test MCP | exact stable URL used |
| ChatGPT host test | date/time, connector, prompt pack version, pass/fail, deviations |
| Claude host test | date/time, connector, prompt pack version, pass/fail, deviations |
| Same-window A/B | baseline release, candidate release, material differences and justification |
| Submission endpoint check | exact final production hostname, TLS, MCP, widget/CSP/resources, links, domain verification |
| Platform review state | OpenAI / Anthropic current status |
| Production promotion | platform, Vercel project, branch/pointer, deployment ID, exact SHA |
| Production smoke | exact production URL, positive/negative checks, host behavior |
| Monitoring window | error/latency observations and duration |
| Rollback point | previous known-good SHA/deployment |
| Known issues | open defects, accepted limitations, follow-up tasks |
| Sign-off | André decision/gate where required |

## 3. Standard test layers

### Layer A — commit/contract tests

- build;
- typecheck, with any pre-existing failure proven against baseline rather than silently accepted;
- unit/custom regression tests;
- deterministic provider/NHTSA fixtures;
- MCP initialize;
- tools/list and resources where applicable;
- schema, description, annotation and resource-contract snapshots.

### Layer B — deployed identity

Before testing behavior, prove:

- correct Vercel project;
- correct target (Preview/Production as intended);
- correct branch/pointer;
- exact Git SHA;
- stable MCP URL reaches that deployment;
- widget origin/CSP/resource metadata match the actual host;
- unrelated Vercel projects did not react once isolation rules are installed.

### Layer C — baseline vs candidate

Use the same prompt window where possible. Compare effective user intent, tool arguments, hard constraints, preferences, widening/relaxation, evidence, ordering, latency and host omissions. Do not require identical VINs from changing live inventory.

### Layer D — both AI hosts

Every material contract/release must be exercised in both ChatGPT and Claude. Host routing is part of the product. A server-only test cannot prove that each host chooses the tool and constructs arguments correctly.

### Layer E — exact production/submission origin

Run the critical suite against the exact hostname that will be submitted or promoted. A passing temporary `.vercel.app` environment is not proof that a custom-domain widget/MCP path behaves identically.

### Layer F — post-release

Immediately after promotion:

- verify exact production SHA;
- smoke positive and negative cases;
- verify UI/widget rendering;
- verify external links;
- check runtime errors/latency;
- record rollback deployment;
- monitor and record any first-seen regression with timestamp.

## 4. Prompt-pack versioning

Maintain a reusable release prompt pack. Each ledger entry records the pack version.

Minimum categories:

1. exact make/model/budget/location;
2. family/practical need requiring model resolution;
3. conventional hybrid required;
4. PHEV required;
5. electrification preferred with alternatives;
6. exact VIN / unavailable VIN;
7. best-for-budget vs cheapest;
8. newest / lowest mileage / lower risk;
9. AWD/transmission/color/cylinder/direct fields;
10. trim required vs preferred;
11. city-only / ZIP / state / nationwide / invalid location;
12. CPO/history/one-owner unknown evidence;
13. zero/thin results and automatic widening;
14. UI/widget render and link actions;
15. negative non-inventory questions where the connector should not be invoked.

Any production bug discovered later should add a permanent regression case to the pack with a reference to the incident and first bad/last good release if known.

## 5. Existing baseline records

### V1 — current Anthropic submission baseline

- Git branch: `main`.
- Current production SHA verified by the Sep 10 infrastructure audit: `e7c8634...`.
- Anthropic submitted MCP: `https://carclever-find-my-car.vercel.app/mcp`.
- Status as confirmed by André on 2026-09-10: still in Anthropic review.
- Current concern: V1 `find_matching_vehicle` description is very long/instruction-heavy relative to Anthropic's current review criteria.
- Do not mutate this production/submission until the pending V1→V2 Anthropic decision gate is crossed.

### V2 — current amended release candidate

Existing recorded evidence from `V2_CONNECTOR_TEST_RECORD_20260909.md`:

- branch: `release/v2`;
- merge: `5e8735e`;
- deployed tip: `a9d6439`;
- endpoint tested: `https://ccfmc-dev-v2.vercel.app/mcp`;
- deployment READY / production target;
- production build passed;
- custom checks: 222 passed;
- Node tests: 79 passed;
- typecheck: one pre-existing unrelated baseline error recorded;
- exercised in both ChatGPT and Claude across practical model resolution, required/preferred hybrid/PHEV, mixed electrification, exact VIN/risk, priority axes, CPO/history and five-card behavior.

This evidence is strong but **does not close the final release gate**. Remaining work includes Anthropic-specific description review, permanent custom-domain validation, controlled branch isolation, exact-host final A/B/host tests and production-channel promotion records.

## 6. Current open validation sequence — V2 finalization

| Step | Owner | Status | Evidence required |
|---|---|---|---|
| Anthropic V2 description-compliance review | ChatGPT | NEXT | Written pass/fail against current Anthropic criteria; identify only necessary changes |
| Any resulting V2 description/code change | Claude | gated | Exact diff + tests; no V1 mutation |
| Re-run ChatGPT V2 host pack | ChatGPT/André | pending | prompt pack + tool args + outputs + UI notes |
| Re-run Claude V2 host pack | Claude/André | pending | same pack/version and deviation notes |
| Configure stable shared test host | Claude | pending architecture implementation | `carclever-test.getcarwise.app/mcp` or final approved equivalent; exact SHA verified |
| Branch/project isolation cleanup | Claude | pending | unrelated push no longer fans out |
| Controlled Vercel auto-deploy trigger test | Claude + ChatGPT verification | after isolation | two deliberate trigger cycles with exact SHA/target evidence |
| Validate Claude production custom origin | Claude | pending decision | `carclever-claude.getcarwise.app/mcp` or final approved equivalent |
| Inspect pending Anthropic Edit workflow | André + ChatGPT/Claude | pending | capture current status, edit fields, final button/warning; do not save blindly |
| Anthropic V1→V2 decision | André | gated | wait vs amend; queue impact acknowledged as unknown unless UI/support resolves it |
| Validate OpenAI production custom origin | Claude | pending | `carclever-openai.getcarwise.app/mcp` or final approved equivalent; challenge endpoint + Scan Tools ready |
| Final same-window V1↔V2 A/B | ChatGPT + Claude | pending | both hosts where possible, exact endpoints/SHA recorded |
| OpenAI V2 submission | André/ChatGPT strategy + Claude technical execution | pending | exact permanent origin + final test record |
| Anthropic change if approved by André | André + Claude | pending | exact submission change/deployment + status after action |
| Production smoke + monitoring | both lanes | pending | exact production URLs/SHA, pass/fail and rollback |

## 7. V3 rebaseline gate — NO UNPAUSE BEFORE COMPLETE

Current paused V3 must not receive new feature work until all of the following are recorded:

- [ ] final V2 candidate/release SHA frozen;
- [ ] cross-platform release architecture and branch isolation operating correctly;
- [ ] paused V3 compared against final V2;
- [ ] explicit port/keep/drop matrix for every V3-specific change;
- [ ] fresh V3 release branch created from final V2/common stable baseline;
- [ ] selected V3 functionality ported rather than wholesale stale-branch merge;
- [ ] V2 regression suite passes on rebased V3 before new V3 scope;
- [ ] ChatGPT and Claude both pass the shared test-host acceptance suite;
- [ ] exact V3 test record added to this ledger.

## 8. Incident/regression chronology rule

Whenever something breaks, add an incident row immediately:

| First observed | Symptom | Last known good | First known bad | Host | Endpoint | SHA/deployment | Root cause | Permanent regression test |
|---|---|---|---|---|---|---|---|---|

Do not rely on memory such as “it used to work last week.” The purpose of this ledger is to make the first-bad/last-good interval progressively smaller over time.

## 9. Cleanup actions tracked by release gate

- Schema probe: inactivate safely after dependency capture; retain inert through final V2 smoke; then delete after zero dependency is confirmed.
- `ccfmc-dev`: retain and repurpose as shared stable test harness; do not delete while it is the known solution to ChatGPT's long Preview-domain problem.
- V3-specific Vercel project: retire after V3 is rebased onto the shared release architecture.
- PR #1/#2: low priority; Claude independently verifies supersession/ancestry, then close rather than merge.

## References

- `V2_CONNECTOR_TEST_RECORD_20260909.md`
- `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md`
- `CURRENT_V2_STATE_20260909.md`
- `AUDIT_CARCLEVER_GITHUB_VERCEL_ENVIRONMENT_MAPPING_20260910.md`
- `STRATEGY_CARCLEVER_CROSS_PLATFORM_RELEASE_AND_DEPLOYMENT_20260910.md`
- `RESEARCH_ANTHROPIC_V1_V2_REVIEW_AND_MCP_ORIGIN_DECISION_20260910.md`
