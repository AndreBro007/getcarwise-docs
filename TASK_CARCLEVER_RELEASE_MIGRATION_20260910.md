# CarClever Release Migration Tasks — 2026-09-10

**Status:** ACTIVE controlled task list  
**Scope:** V2 finalization, Anthropic V1→V2 decision, permanent MCP origins, shared test harness, Vercel/Git isolation, production release discipline, cleanup, and V3 rebaseline.  
**Boundary:** ChatGPT owns strategy/research/verification/documentation. Claude Engineering owns application-code changes, `carclever-find-my-car` branch/PR mutations, Vercel configuration/deployments, DNS/domain attachment, connector changes, and production cutovers. André approves gated release/domain/submission decisions.

## Priority 0 — V2 finalization and platform architecture

| # | Task | Owner | Gate / status | Completion evidence |
|---|---|---|---|---|
| 1 | Anthropic-specific V2 tool-description/schema compliance review | ChatGPT | ✅ **COMPLETE / REVISED Sep 10** | Exact old Anthropic feedback re-read; current conclusion is that V2 guidance is materially less coercive than old rejected wording and should remain unchanged for the next test phase |
| 2 | Decide permanent MCP origin set | André + ChatGPT | **UNDER DISCUSSION — NO HOSTNAME APPROVED** | Final Claude/OpenAI/test origins recorded as confirmed only after architecture + technical validation |
| 3 | Determine Anthropic production-origin strategy | André + ChatGPT | **OPEN / SUPPORT QUESTION SENT Sep 10** | Current UI says URL/auth are Anthropic-managed. Email sent to `mcp-review@anthropic.com` asking whether an in-review URL can move to owned domain, queue/review impact, what Rescan Tools refreshes, and whether active review has started |
| 4 | Clean retest of historical ChatGPT Preview-domain failure before approving shared test hostname | Claude + ChatGPT verification | **PLAN DEFINED; MANUAL EXECUTION IN FRESH CHAT** | Same-SHA A/B/C test: long branch alias with Vercel Auth off vs short `ccfmc-dev` vs short owned-domain candidate; test connector creation, MCP calls, widget/resource origin/CSP |
| 5 | Design and implement branch/project isolation | Claude | After architecture confirmation | Each Vercel project reacts only to intended pointer/release branch; unrelated branch fan-out blocked |
| 6 | Create pointer-only branches `test/current`, `prod/claude`, `prod/openai` | Claude | After #5 design approval | Branches point to known SHAs; no unique development commits; documented operating rule |
| 7 | Repurpose `ccfmc-dev` as shared test harness | Claude | After #4/#5 | Stable short test origin TBD serves `test/current`; both ChatGPT and Claude test connectors use the same URL |
| 8 | Controlled auto-deploy reliability test after isolation | Claude + ChatGPT verification | After #5/#7 | Two deliberate trigger cycles; only intended project reacts; correct target/SHA; record whether prior intermittent behavior persists |
| 9 | V2 description/schema review and contingency redline | ChatGPT | ✅ **COMPLETE Sep 10 — CHANGE DEFERRED** | `REVIEW_CARCLEVER_V1_V2_TOOL_DESCRIPTION_REDLINE_20260910.md`; exact old-feedback context reviewed; current V2 wording retained unless testing or Anthropic feedback creates a concrete reason to change |
| 10 | Implement V2 description wording change | Claude | **NOT CURRENTLY REQUESTED** | Only activate if testing finds a description-caused defect or Anthropic explicitly flags the current V2 wording; then use minimal wording-only diff + both-host re-test |
| 11 | Re-run V1↔V2 same-window A/B plus full ChatGPT and Claude acceptance pack using current V2 wording | ChatGPT + Claude + André where UI needed | **NEXT MAJOR TASK** | Release ledger populated with exact endpoint, SHA, host arguments, deviations, UI behavior, latency; manual fresh-chat execution acceptable due Claude token constraint |
| 12 | Anthropic pending-submission Edit-flow inspection | André + ChatGPT/Claude | 🟡 **PARTIALLY COMPLETE / SUPPORT QUESTION SENT Sep 10** | Confirmed URL not self-service editable, Rescan Tools available, listing fields editable. Support asked what Rescan refreshes, queue impact, URL change process, and whether active assessment has started |
| 13 | Affiliate/sponsored-content consistency watch | ChatGPT | 🟢 **NOT A CURRENT BLOCKER** | Prior CarClever Anthropic review disclosed affiliate arrangement and did not flag it; historical blockers were descriptions/icon/docs. Keep implementation/disclosure consistent and reopen only on new evidence or Anthropic feedback |
| 14 | Decide Anthropic V1 disposition | André | **CURRENT LEAN: after #11, use exact final V2 behind existing submitted URL + Rescan Tools + controlled save; final approval still required** | Explicit decision recorded with before/after SHA, submission state and rollback. Owned Anthropic-domain move treated separately unless support gives a better supported process |
| 15 | Configure final OpenAI owned origin and submission prerequisites | Claude | After #2/#11 | Exact owned host, OpenAI challenge endpoint, Scan Tools, domain/CSP/link checks, exact SHA |
| 16 | Submit/promote V2 to OpenAI using permanent owned origin only | André + ChatGPT strategy + Claude technical | After #15 | Submission record, exact snapshot/SHA/origin, status recorded |
| 17 | If #14 is approved, execute Anthropic V2 change as one controlled operation | André + Claude | After explicit approval | Exact final V2 SHA deployed behind existing submitted MCP URL; immediate Rescan Tools + listing save/submit; resulting review state captured; smoke test and rollback point recorded |
| 18 | Post-promotion production smoke and monitoring on every platform change | Claude + ChatGPT review | **MANDATORY** | Ledger entry including last known good, production SHA, both-host tests where applicable, errors/latency, rollback |

## Priority 1 — controlled cleanup

| # | Task | Owner | Status | Completion evidence |
|---|---|---|---|---|
| 19 | Inactivate `carclever-v2-schema-probe` | Claude | Approved in principle; do after dependency capture | Disable Git trigger/auto-deploy, remove temp connector if present, preserve research branch/docs; ChatGPT verifies project is inert |
| 20 | Delete schema-probe Vercel project only after final V2 smoke and zero-dependency verification | Claude + André approval | Deferred safety step | Search shows no domain/connector/config dependency; final V2 smoke complete; deletion confirmed and topology re-audited |
| 21 | Independent ancestry/supersession check for PR #1 and PR #2 | Claude | Low priority | Claude confirms PR #1 contained in current V2 and PR #2 is stale/diverged; no missing required work |
| 22 | Close PR #1/#2 as superseded; do not merge | Claude | Low priority, after #21 | PR state closed with superseded note; no application change merged |
| 23 | Retire version-specific `ccfmc-dev-v3` project after V3 moves to shared release architecture | Claude | Later | V3 uses shared test + platform production channels; no dependency remains |

## Priority 0 hard gate — V3 before any unpause

**NO further V3 feature work, merge, deployment, connector repointing, or new V3 scope until every item below is complete.**

- [ ] Final V2 release SHA frozen and recorded.
- [ ] Permanent platform/test origin strategy implemented and verified.
- [ ] `test/current` shared-harness process works in both ChatGPT and Claude.
- [ ] Paused V3 compared against final V2.
- [ ] V3 port/keep/drop matrix written for every V3-specific change.
- [ ] Fresh `release/v3` created from final V2/common stable baseline.
- [ ] Only still-valid V3 work selectively ported; old V3 branch **not merged wholesale**.
- [ ] Full V2 regression suite passes on rebased V3 **before any new V3 feature work begins**.
- [ ] ChatGPT and Claude both pass the V3 shared-test acceptance pack.
- [ ] V3 release entry created in `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`.

## Standing release rules

1. **Preview deployments are builds only; they never merge Git.** A merge/promotion occurs only through an explicit Git/release action.
2. Feature/fix work merges into the active `release/vN`, not directly into platform production pointers.
3. `test/current`, `prod/claude`, and `prod/openai` are pointer-only branches; no unique code is developed on them.
4. Both platforms should serve the same tested SHA whenever external review gates allow it; any temporary skew must be explicit in the release ledger.
5. Every material release, production hotfix, or server-only behavior change requires the defined validation/smoke process even where an AI platform does not require a new reviewed version.
6. Tool/field descriptions are changed only for a concrete reason. Clear contract guidance is not rewritten merely because it is directive; genuinely coercive `MUST` / `always invoke` / `never refuse` behavior remains disallowed. Any description change is treated as behavioral until both hosts show no regression.
7. No cleanup deletion happens merely because a project looks unused: first capture dependencies, inactivate, verify, then delete after an explicit safety gate.
8. `getcarwise-app` / website application work remains a separate workstream and is not part of this task list unless a critical dependency is discovered.
9. Exact MCP hostnames remain **unapproved** until André confirms them. Existing strategy-document hostname examples are proposals only.
10. Any Anthropic V1→V2 server replacement during active review must be one controlled operation: exact SHA deployment → Rescan Tools → save/submit → capture resulting review state → smoke test. Never silently change the submitted server and leave the listing untouched.

## Primary references

- `REVIEW_CARCLEVER_V1_V2_TOOL_DESCRIPTION_REDLINE_20260910.md`
- `AUDIT_V2_ANTHROPIC_SUBMISSION_COMPLIANCE_20260910.md`
- `RESEARCH_ANTHROPIC_V1_V2_REVIEW_AND_MCP_ORIGIN_DECISION_20260910.md`
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`
- `STRATEGY_CARCLEVER_CROSS_PLATFORM_RELEASE_AND_DEPLOYMENT_20260910.md`
- `AUDIT_CARCLEVER_GITHUB_VERCEL_ENVIRONMENT_MAPPING_20260910.md`
- `CURRENT_V2_STATE_20260909.md`
- `V2_CONNECTOR_TEST_RECORD_20260909.md`
- `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md`
