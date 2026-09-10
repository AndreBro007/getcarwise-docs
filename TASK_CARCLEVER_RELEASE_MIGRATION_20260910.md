# CarClever Release Migration Tasks — 2026-09-10

**Status:** ACTIVE controlled task list  
**Scope:** V2 finalization, Anthropic V1→V2 decision, permanent MCP origins, shared test harness, Vercel/Git isolation, production release discipline, cleanup, and V3 rebaseline.  
**Boundary:** ChatGPT owns strategy/research/verification/documentation. Claude Engineering owns application-code changes, `carclever-find-my-car` branch/PR mutations, Vercel configuration/deployments, DNS/domain attachment, connector changes, and production cutovers. André approves gated release/domain/submission decisions.

## Priority 0 — V2 finalization and platform architecture

| # | Task | Owner | Gate / status | Completion evidence |
|---|---|---|---|---|
| 1 | Anthropic-specific V2 tool-description/schema compliance review | ChatGPT | **NEXT / in progress** | Written field-by-field finding against current Anthropic review criteria; minimal proposed changes only |
| 2 | Decide permanent MCP origin set | André + ChatGPT | **Decision today** | Approved Claude/OpenAI/test hostnames recorded as confirmed, not proposed |
| 3 | Validate three owned subdomains technically | Claude | After #2 | DNS/Vercel ownership, TLS, `/mcp`, widget/CSP/origin, exact deployment SHA; no V1 change yet |
| 4 | Design and implement branch/project isolation | Claude | After architecture confirmation | Each Vercel project reacts only to intended pointer/release branch; unrelated branch fan-out blocked |
| 5 | Create pointer-only branches `test/current`, `prod/claude`, `prod/openai` | Claude | After #4 design approval | Branches point to known SHAs; no unique development commits; documented operating rule |
| 6 | Repurpose `ccfmc-dev` as shared test harness | Claude | After #2/#4 | Stable `carclever-test.getcarwise.app/mcp` (or approved equivalent) serves `test/current`; both host test connectors use same URL |
| 7 | Controlled auto-deploy reliability test after isolation | Claude + ChatGPT verification | After #4/#6 | Two deliberate trigger cycles; only intended project reacts; correct target/SHA; record whether prior intermittent behavior persists |
| 8 | Re-run V1↔V2 same-window A/B plus full ChatGPT and Claude acceptance pack | ChatGPT + Claude + André where UI needed | After #1/#6 | Release ledger populated with exact endpoints, SHA, host arguments, deviations, UI behavior, latency |
| 9 | Inspect Anthropic pending-submission Edit flow **without blindly saving** | André + ChatGPT/Claude | After #1/#3 | Current status captured; edit scope, fresh-tool capture behavior, final button/warnings recorded; queue-reset impact recorded if UI states it |
| 10 | Decide Anthropic V1 disposition: wait vs amend to final V2 + owned Claude origin | André | After #1/#3/#9 | Explicit confirmed decision and accepted uncertainty about queue timing |
| 11 | Configure final OpenAI owned origin and submission prerequisites | Claude | After #2/#8 | Exact host, OpenAI challenge endpoint, Scan Tools, domain/CSP/link checks, exact SHA |
| 12 | Submit/promote V2 to OpenAI using permanent owned origin only | André + ChatGPT strategy + Claude technical | After #11 | Submission record, exact snapshot/SHA/origin, status recorded |
| 13 | If #10 chooses amend, update Anthropic pending submission and production channel in one controlled change | André + Claude | After explicit approval | Exact before/after submission fields, tool snapshot, endpoint, SHA, resulting status, full smoke |
| 14 | Post-promotion production smoke and monitoring on every platform change | Claude + ChatGPT review | Mandatory | Ledger entry including last known good, production SHA, host tests, errors/latency, rollback |

## Priority 1 — controlled cleanup

| # | Task | Owner | Status | Completion evidence |
|---|---|---|---|---|
| 15 | Inactivate `carclever-v2-schema-probe` | Claude | Approved in principle; do after dependency capture | Disable Git trigger/auto-deploy, remove temp connector if present, preserve research branch/docs; ChatGPT verifies project is inert |
| 16 | Delete schema-probe Vercel project only after final V2 smoke and zero-dependency verification | Claude + André approval | Deferred safety step | Search shows no domain/connector/config dependency; final V2 smoke complete; deletion confirmed and topology re-audited |
| 17 | Independent ancestry/supersession check for PR #1 and PR #2 | Claude | Low priority | Claude confirms PR #1 contained in current V2 and PR #2 is stale/diverged; no missing required work |
| 18 | Close PR #1/#2 as superseded; do not merge | Claude | Low priority, after #17 | PR state closed with superseded note; no application change merged |
| 19 | Retire version-specific `ccfmc-dev-v3` project after V3 moves to shared release architecture | Claude | Later | V3 uses shared test + platform production channels; no dependency remains |

## Priority 0 hard gate — V3 before any unpause

**NO further V3 feature work, merge, deployment, or connector repointing until every item below is complete.**

- [ ] Final V2 release SHA frozen and recorded.
- [ ] Permanent platform/test origin strategy implemented and verified.
- [ ] `test/current` shared-harness process works in both ChatGPT and Claude.
- [ ] Paused V3 compared against final V2.
- [ ] V3 port/keep/drop matrix written for every V3-specific change.
- [ ] Fresh `release/v3` created from final V2/common stable baseline.
- [ ] Only still-valid V3 work selectively ported; old V3 branch not merged wholesale.
- [ ] Full V2 regression suite passes on rebased V3 **before any new V3 scope begins**.
- [ ] ChatGPT and Claude both pass the V3 shared-test acceptance pack.
- [ ] V3 release entry created in `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`.

## Standing release rules

1. Preview deployments are builds only; they never merge Git.
2. Feature/fix work merges into the active `release/vN`, not directly into platform production pointers.
3. `test/current`, `prod/claude`, and `prod/openai` are pointer-only branches; no unique code is developed on them.
4. Both platforms should serve the same tested SHA whenever external review gates allow it; any temporary skew must be explicit in the ledger.
5. Every platform release or server-only production fix requires both-host regression/smoke evidence, even where the platform does not require a new reviewed version.
6. No cleanup deletion happens merely because a project looks unused: first capture dependencies, inactivate, verify, then delete after an explicit safety gate.
7. `getcarwise-app` / website application work remains a separate workstream and is not part of this task list unless a critical dependency is discovered.

## Primary references

- `RESEARCH_ANTHROPIC_V1_V2_REVIEW_AND_MCP_ORIGIN_DECISION_20260910.md`
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`
- `STRATEGY_CARCLEVER_CROSS_PLATFORM_RELEASE_AND_DEPLOYMENT_20260910.md`
- `AUDIT_CARCLEVER_GITHUB_VERCEL_ENVIRONMENT_MAPPING_20260910.md`
- `CURRENT_V2_STATE_20260909.md`
- `V2_CONNECTOR_TEST_RECORD_20260909.md`
- `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md`
