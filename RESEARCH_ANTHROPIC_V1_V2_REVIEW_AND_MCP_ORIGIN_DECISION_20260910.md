# Anthropic V1→V2 Review and MCP-Origin Decision — 2026-09-10

**Status:** Decision research complete; execution pending André confirmation and Engineering validation  
**Scope:** Whether to leave the current Anthropic V1 directory submission untouched or amend it to the V2 release, whether to change the submitted MCP URL before approval, and the permanent Claude/OpenAI/test MCP-origin design.  
**Execution boundary:** No application code, Vercel project, DNS, domain, connector, branch, PR, deployment, or Anthropic submission was changed by this research.

## Executive conclusion

The current V1 Anthropic submission has a **material review-risk reason to reconsider waiting**: its `find_matching_vehicle` description is extremely long and instruction-heavy, while Anthropic's current review criteria require narrow, accurate descriptions and explicitly scan for prompt-injection / behavior-instruction patterns. Current V2 is substantially closer to those criteria, but should receive one dedicated Anthropic-compatibility review before it replaces V1 because V2 still contains some host-routing imperative wording.

The preferred infrastructure end state is now three stable owned origins:

- **Claude production:** `https://carclever-claude.getcarwise.app/mcp`
- **OpenAI production:** `https://carclever-openai.getcarwise.app/mcp`
- **Shared release test:** `https://carclever-test.getcarwise.app/mcp`

These names are proposed, not yet configured. `openai` is preferred to `chatgpt` in the infrastructure hostname because the production channel belongs to OpenAI's plugin platform and the hostname should survive future product-surface naming changes.

The shared test origin should front the existing short-name `ccfmc-dev` Vercel project, repurposed as a deliberate release-test harness. Both ChatGPT and Claude test connectors should eventually point at this one stable test URL. Release V2, V3, etc. are deployed behind it one at a time by exact SHA; the test hostname does not change.

## 1. What Anthropic currently documents

Anthropic's current Connector Directory documentation says:

- reviewers functionally test every submitted tool and run policy/compliance checks;
- tool descriptions should be narrow and accurate and match actual behavior;
- descriptions are rejected for several prompt-injection/behavior-instruction patterns;
- review times vary with queue volume;
- after publication, an MCP server is treated as a live API and tool additions/changes/removals can be deployed without a directory resubmission or scheduled re-review;
- post-publication listing metadata is managed separately;
- Anthropic does not currently document a self-service rule saying a published server hostname can be replaced without review.

Official documentation does **not** state whether editing an in-review connector keeps or resets its queue position. Therefore any claim that the existing two weeks are preserved, or definitely lost, would be speculation.

## 2. The pending-submission snapshot matters

A recent issue in Anthropic's own `anthropics/claude-ai-mcp` repository exposed the in-app directory submission request structure and showed a `submission_data.server_snapshot.tools[...]` object being posted when a connector is submitted.

That is strong evidence that the submission stores a snapshot of the tool surface at submission time.

Practical implication: **do not silently switch the current submitted V1 URL to V2 while the V1 submission remains in review and assume Anthropic will automatically treat the submission as V2.** The stored V1 snapshot and the live V2 server could diverge.

If V2 is intentionally substituted while review is active, the submission itself should be amended/refreshed through the in-app Edit flow (or Anthropic support if the portal cannot safely do it) so the recorded submission and live server agree.

## 3. V1 review-risk assessment

The V1 `find_matching_vehicle` description currently contains a large operating manual embedded in tool metadata. Examples of the pattern include instructions such as:

- do not retry a thin search yourself;
- before calling, translate the request using a specified sequence;
- resolve lifestyle needs into model lists every time;
- never rely on manual post-filtering;
- use particular fields in particular ways;
- open the final answer with specified scale wording;
- set ranking axes according to detailed behavioral rules.

Many of these instructions were originally added for good product-quality reasons and helped the host construct accurate calls. However, the current Anthropic review criteria now place much more emphasis on concise functional descriptions and avoiding model-behavior instructions in tool metadata.

**Best assessment:** V1 is not guaranteed to be rejected, but its present description creates a meaningful avoidable review risk. Waiting purely because two weeks have already elapsed is therefore not automatically the lowest-risk decision.

## 4. V2 review-risk assessment

V2's description is drastically shorter and moves much more behavior into structured inputs/code. This is directionally aligned with Anthropic's current review guidance.

However, it still contains several direct host-routing imperatives, for example requiring the host to resolve practical needs and broad electrification requests into real model names before calling the tool.

Those instructions are directly related to correct tool use, so they are less concerning than V1's multi-thousand-word operating manual. Still, before changing the Anthropic submission, V2 should receive a specific **Anthropic Description Compliance Gate**:

1. compare every V2 tool description against current Anthropic review criteria;
2. remove any instruction that can instead be represented by schema, code, or neutral capability wording without causing behavioral regression;
3. preserve the minimum host-routing cues proven necessary by the V1→V2 equivalence testing;
4. run the same prompt pack in Claude and ChatGPT after any description adjustment;
5. freeze the exact V2 SHA only after both hosts pass.

This gate is required before using V2 for the Anthropic submission.

## 5. Should we bite the bullet and edit Anthropic now?

### Option A — wait for the V1 decision

**Advantages**
- preserves whatever review progress/queue position V1 currently has;
- no risk of introducing a portal-edit workflow problem;
- if V1 is approved, Anthropic explicitly permits later live tool-surface updates without resubmission.

**Disadvantages**
- V1 has the material description-review risk described above;
- a rejection means the elapsed review time bought no release progress;
- the submitted origin remains the Vercel-generated hostname rather than a GetCarWise-owned permanent origin;
- after publication, Anthropic does not clearly document a simple self-service server-hostname replacement.

### Option B — amend the pending submission to V2 but keep the old Vercel hostname

**Advantages**
- removes the main V1 description/behavior debt now;
- retains the already submitted hostname;
- least infrastructure change if the Edit flow safely refreshes the server snapshot.

**Disadvantages**
- queue-reset behavior remains undocumented;
- still leaves the permanent Claude channel on the Vercel hostname;
- requires production V2 to be deployed behind that hostname during the edit transition.

### Option C — amend the pending submission to V2 and move to an owned Claude hostname

**Advantages**
- fixes V1 review-risk and permanent-origin design in one controlled change;
- makes Claude and OpenAI symmetric operationally while still having separate approval channels;
- removes long-term dependence on a generated Vercel hostname;
- avoids trying to replace the hostname after Anthropic approval, where the documented self-service path is unclear.

**Disadvantages**
- largest change to an in-review submission;
- may restart review; Anthropic does not document the queue behavior;
- requires domain/DNS/Vercel/widget validation before editing.

### Recommendation

**Preferred: Option C, but only after the Anthropic Description Compliance Gate and exact-domain testing are complete.**

Rationale: the current V1 description presents a real review risk, and if we are going to accept the possibility of resetting review, doing only half the job (V2 code but retaining the temporary/Vercel origin forever) gives up the strongest long-term benefit.

The two weeks already spent are a sunk cost. They matter operationally, but should not outweigh a materially cleaner submission and permanent owned origin if we judge V1 has a meaningful avoidable rejection risk.

## 6. What the Edit button means — what is known and unknown

André currently sees an **Edit** control on the in-review Anthropic submission.

Known:
- the portal clearly supports some modification path for the pending object;
- Anthropic says review timing varies with queue volume;
- submission payloads include a server snapshot;
- post-publication listing editing is a separate workflow.

Unknown:
- whether clicking Edit alone changes status;
- whether saving an edit preserves queue position;
- whether changing the MCP URL specifically triggers a fresh review timestamp;
- whether a new server snapshot is automatically taken when the pending submission is saved;
- whether the portal warns before resetting review.

**Controlled UI rule:** do not blindly save. When this task reaches execution, André/Claude should open Edit, capture the current status and all fields, and inspect the final button/warning text. If the UI says `Resubmit`, `Submit for review`, `restart review`, or otherwise indicates queue reset, record that before committing. If it is ambiguous, stop and use Anthropic's documented escalation contact rather than gambling with the pending submission.

## 7. Recommended permanent URL design

### Claude production

`https://carclever-claude.getcarwise.app/mcp`

### OpenAI production

`https://carclever-openai.getcarwise.app/mcp`

### Shared test

`https://carclever-test.getcarwise.app/mcp`

Why this set:

- every origin is owned under `getcarwise.app`;
- the CarClever product is explicit;
- platform production channels are separate, preventing one platform's review lifecycle from blocking or mutating the other;
- version numbers never appear in permanent hostnames;
- the test origin is stable across V2/V3/V4 and can be used by both host connectors;
- single-label subdomains are operationally simpler than deep nested hostnames;
- `openai` is more durable infrastructure naming than `chatgpt`.

`findmycar.getcarwise.app` remains a valid product/marketing hostname, but the three-role naming above is operationally clearer and avoids using one origin for two different platform approval states.

## 8. Shared test-harness design

Repurpose existing Vercel project `ccfmc-dev` rather than delete it.

Target behavior:

`release/vN exact SHA → shared test project → carclever-test.getcarwise.app/mcp → ChatGPT test connector + Claude test connector`

The project should no longer react broadly to every application branch.

Preferred control model:

- create a pointer-only Git branch such as `test/current`;
- never develop or commit unique code on `test/current`;
- when a release candidate is ready, Engineering moves `test/current` to the exact already-reviewed candidate SHA;
- Vercel production branch for the test project tracks only `test/current`;
- the stable test custom domain automatically serves that project's current production deployment;
- before host tests, verify test project + deployment target + exact Git SHA;
- both ChatGPT and Claude use the same test MCP URL and the same SHA.

Alternative: an explicitly selected production deployment can be promoted/assigned to the stable test domain in Vercel. The pointer-branch method is preferred because the selected SHA remains visible in Git and is easier to audit.

## 9. Production pointer branches

Adopt:

- `prod/claude`
- `prod/openai`

These are deployment pointers, not development branches.

Rules:

- no unique coding on them;
- advance only to a release SHA already passed through the shared test harness;
- each corresponding Vercel production project tracks only its platform pointer branch;
- if external review timing differs, the branches may temporarily point to different release SHAs;
- record the reason for any skew;
- once both platforms converge, both should point to the same release SHA.

`main` then becomes the canonical **shared stable baseline**, not the platform deployment selector.

## 10. When do we actually merge?

To remove the current ambiguity, use these distinct terms:

- **Preview/test deployment:** builds a commit; no Git merge.
- **Release-candidate merge:** feature/fix branch → active `release/vN` after Engineering review/tests.
- **Platform promotion:** move `prod/claude`, `prod/openai`, or `test/current` to an exact tested release SHA; this is not a code-development merge.
- **Canonical release merge:** once the release is accepted as the shared baseline, merge the completed `release/vN` into `main` (or otherwise advance `main` to the exact release history through the agreed Git method), then tag/record it.

Historical PR #1/#2 are not the mechanism for this future canonical merge. They are superseded and remain low-priority cleanup candidates pending Claude's independent ancestry check.

## 11. V3 hard gate before unpausing

**V3 MUST NOT resume from the paused branch as-is.**

Before any new V3 engineering work:

1. V2 final release SHA is frozen;
2. shared test + production-channel architecture is operational;
3. current paused V3 is compared against final V2;
4. a V3 rebaseline/port matrix identifies which V3 changes remain valid;
5. fresh `release/v3` is created from final V2/shared stable baseline;
6. selected V3 functionality is ported deliberately;
7. V2 regression suite passes before adding further V3 scope;
8. both ChatGPT and Claude test the rebased V3 through the shared test URL.

This is a release gate, not a suggestion.

## 12. Controlled infrastructure cleanup

### `carclever-v2-schema-probe`

Task remains approved in principle: inactivate safely first, then delete only after the final V2 dependency check.

Ownership: Claude Engineering for Vercel/connector changes; ChatGPT verifies the before/after topology and records evidence.

Suggested sequence:
1. document current project, branch, domain, connector references and last useful deployment;
2. disable Git auto-deployment / disconnect the trigger;
3. remove the temporary test connector if still present;
4. run dependency searches for the project hostname/name across docs/config;
5. keep inert through final V2 production smoke;
6. delete only after zero dependency is confirmed.

### PR #1 / PR #2

Low priority. Do not merge. Claude independently confirms ancestry/supersession, then close as superseded when convenient after the release design is operating correctly.

## 13. Testing discipline from now on

No release reaches either production channel merely because local tests pass.

Required progression:

`candidate SHA → automated suite → shared test deployment identity check → ChatGPT acceptance → Claude acceptance → release record → platform promotion → exact-production smoke → monitoring`

This applies even when the AI platform does not require a new formal version review.

The release/test ledger in `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md` is the persistent history for this process.

## 14. Immediate next actions

1. ChatGPT: perform the dedicated V2 Anthropic-description compliance review against current Anthropic criteria.
2. ChatGPT + Claude: decide whether any description adjustment is required; if yes, Engineering changes V2 and both hosts re-test it.
3. Claude: validate feasibility of the three proposed GetCarWise subdomains and confirm widget/CSP/origin behavior on the exact test and production hostnames.
4. Claude: design the branch-filter + pointer-branch implementation (`test/current`, `prod/claude`, `prod/openai`) but do not modify the in-review Anthropic V1 until the decision gate is explicitly crossed.
5. ChatGPT/André: inspect the Anthropic pending Edit workflow before saving anything; record whether the portal indicates a queue/review reset.
6. Decision gate: choose whether to amend Anthropic V1 to V2 + `carclever-claude.getcarwise.app/mcp`.
7. Configure and validate `carclever-openai.getcarwise.app/mcp` before the OpenAI V2 submission; never submit the temporary V2 `.vercel.app` origin as the intended permanent production origin.
8. Run the full V1/V2 and cross-host release suite and populate the release-validation ledger.
9. Inactivate the schema probe under the controlled sequence above.
10. Leave PR #1/#2 cleanup until after higher-priority release work.
11. Keep V3 paused until the explicit rebaseline gate in Section 11 is complete.

## Sources

- Anthropic: Submitting to the Connectors Directory — current review process and requirements.
- Anthropic: Pre-submission checklist — current tool-design, description, annotation, functional-quality and prompt-injection review criteria.
- Anthropic: Manage your listing after publishing — MCP server live-update policy and listing-management rules.
- Anthropic `anthropics/claude-ai-mcp` issue #828 — current in-app submission payload evidence containing `submission_data.server_snapshot.tools`.
- OpenAI: MCP server review requirements — origin locking and version/update policy.
- OpenAI: Submit plugins — production MCP URL, domain verification and scan requirements.
- Vercel: Git deployments / production branch — commits to the configured production branch create production deployments.
- Vercel: Custom domains — project custom domains follow the project's latest/current production deployment.
- CarClever V1 source: `carclever-find-my-car/main/app/[transport]/route.ts`.
- CarClever V2 source: `carclever-find-my-car/release/v2/app/[transport]/route.ts`.
- Existing strategy/audit: `STRATEGY_CARCLEVER_CROSS_PLATFORM_RELEASE_AND_DEPLOYMENT_20260910.md`, `AUDIT_CARCLEVER_GITHUB_VERCEL_ENVIRONMENT_MAPPING_20260910.md`.
