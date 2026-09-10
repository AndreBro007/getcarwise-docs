# V2 Anthropic Submission Compliance Audit — 2026-09-10

**Status:** COMPLETE read-only compliance/design audit, revised after live pending-submission UI inspection  
**Scope:** Current `release/v2` MCP tool descriptions and input-field descriptions, Anthropic review criteria, the live pending-submission Edit flow, previous CarClever Anthropic review precedent, and implications for a V1→V2 decision.  
**No code, Vercel configuration, domain, connector, branch, PR, deployment, or Anthropic submission was changed.**

## 1. Executive result

V2 is **materially better positioned than V1** for Anthropic's current tool-description review criteria, but any description/schema wording change is release-sensitive and must be treated as a behavioral change until both Claude and ChatGPT prove otherwise.

The live pending-submission UI materially clarifies the V1→V2 options:

- the submission remains `In review`, `Not live`, created/last updated about two weeks ago;
- listing details are editable and changes are submitted for review;
- the current MCP connector URL is **not exposed as a self-service editable field**;
- the UI explicitly says the connector URL and authentication settings are managed by Anthropic and directs other changes/escalations to `mcp-review@anthropic.com`;
- the Tools & prompts section has a live **Rescan tools** action which replaces the listed tool names with the server's current list and refreshes the annotation summary reviewers see;
- the UI does not state whether saving/submitting a voluntary edit preserves or resets review-queue position.

Therefore, changing the Anthropic submission to an owned MCP hostname is not a normal self-service edit. If André ultimately wants an owned Claude production origin, that requires Anthropic involvement unless their process changes.

The earlier affiliate/sponsored-content concern is **downgraded from a release blocker to a watch item**. André confirms the previous CarClever Anthropic review already included affiliate disclosure and the reviewers did not flag affiliate routing. Repository history independently records the actual prior blockers as assistant-directed imperatives in tool descriptions, a missing listing icon, and a ChatGPT-specific documentation link. That precedent materially reduces the practical likelihood that unchanged, transparently disclosed affiliate behavior is the issue Anthropic will focus on. Current policy language should still be monitored and the disclosure must remain accurate, but no separate Anthropic-policy clarification is required before continuing the description/release analysis unless the commercial behavior or form answer changes.

## 2. Current Anthropic description issue

The strongest known review-risk area is the same class of problem Anthropic previously raised on the older CarClever submission: **assistant-directed imperatives inside tool descriptions**.

Current V2 is dramatically shorter and cleaner than V1, but several phrases still tell the calling model what to do rather than only describing contract semantics. The sensitive areas are:

- the main `find_matching_vehicle` description;
- `model` field description;
- `vehicleNeeds` field description;
- `electrificationTypes` field description;
- a smaller imperative phrase in `priorityAxis`.

Examples include wording such as `resolve ... yourself`, `before calling this tool`, and `every time`.

These instructions exist for a real reason: V1→V2 equivalence work proved that practical-needs and electrification searches depend on the host supplying suitable real model/variant candidates. Removing those cues carelessly can create a genuine search regression even though the text becomes more policy-compliant.

**Required principle:** change wording only where the same behavior can be expressed as neutral contract semantics. Never trade away search correctness merely to shorten the description.

## 3. Safe description-change gate

No V2 description/schema wording change should be treated as cosmetic. Before it is eligible for Anthropic or OpenAI production use:

1. preserve the current V2 source as the baseline and capture the exact description/schema snapshot;
2. Claude Engineering makes the smallest possible wording-only diff on the V2 release line — no unrelated code change;
3. deterministic schema/contract tests pass;
4. the established V1→V2 high-value prompt pack runs against the old and candidate wording;
5. compare the host-generated arguments, especially model resolution for family/teen/towing/commuter requests and hybrid/PHEV/EV required-vs-preferred requests;
6. run the same candidate wording through both ChatGPT and Claude;
7. reject or restore any wording whose removal causes worse tool selection, missing model scope, missing hard fields, or materially worse results;
8. record the exact accepted SHA and description snapshot in the release validation ledger.

This is a **no-regression gate**, not a copy-edit exercise.

## 4. Input-schema audit summary

| Area | Verdict | Required treatment |
|---|---|---|
| Main `find_matching_vehicle` description | CHANGE CAREFULLY | neutralize direct model instructions without losing routing behavior |
| `model` | CHANGE CAREFULLY | express candidate-model dependency as contract semantics, not an imperative |
| `vehicleNeeds` | CHANGE CAREFULLY | preserve that it is soft context and not a substitute for model eligibility |
| `electrificationTypes` | CHANGE CAREFULLY | describe accepted evidence and candidate-scope dependency neutrally |
| `priorityAxis` | MINOR WORDING CHANGE | remove direct `Use...` phrasing while keeping intent definitions |
| Remaining direct input fields | PASS | retain unless testing identifies a real defect |
| `resolve_dealer_url` description form | PASS | do not change merely for cleanup |
| Tool names/annotations | PASS | retain |

## 5. Live Anthropic Edit-flow evidence — Sep 10

The pending submission page supplied by André shows:

- Review state: `In review`.
- Health: `Not live` / available after publishing.
- Last updated: approximately two weeks ago.
- `Edit server` says listing details can be updated and changes submitted for review.
- `Tools & prompts` says the listing's tool/prompt names were populated from a live probe at submission time.
- `Rescan tools` replaces the advertised tool list with the server's current list and refreshes the annotation summary reviewers see.
- Under `Name`, the page states: **the connector URL and authentication settings are managed by Anthropic; contact `mcp-review@anthropic.com` to change them.**
- The slug is locked after submission, though the display name can change.

### Implications

1. **We cannot assume the MCP URL can be changed from the Edit page.** The live UI says it cannot.
2. An owned Claude custom domain remains strategically attractive, but changing to it requires Anthropic coordination unless a different supported flow is provided.
3. `Rescan tools` provides a supported mechanism to refresh at least the advertised tool names and reviewer annotation summary after a server change.
4. The UI wording does **not** prove that Rescan Tools refreshes every captured tool description/schema field in the underlying submission snapshot. We should not assume more than the UI states.
5. The UI also does **not** disclose what happens to queue position when an in-review listing is voluntarily edited and resubmitted.

## 6. V1→V2 Anthropic options after this finding

### Option A — leave pending V1 untouched until Anthropic decides

**Pros:** preserves the existing two-week review state and introduces no submission uncertainty.  
**Cons:** Anthropic may return exactly the type of description feedback already seen on the older CarClever review; V1 remains behind the better V2 implementation.

### Option B — keep the currently submitted Anthropic MCP origin, deliberately deploy final V2 behind it, then refresh/resubmit the listing metadata/tool capture in one controlled operation

**Pros:** does not require an MCP-origin change; gets Anthropic onto final V2; preserves the current platform channel.  
**Risks:** the live server and stored submission snapshot must not be allowed to drift; queue impact is unknown; changing the live endpoint while review is active must be coordinated with the Edit/Rescan flow rather than done silently.

**Important:** do not simply deploy V2 behind the submitted URL and walk away. If this option is chosen, the deployment, Rescan Tools, listing review and exact resulting review state must be treated as one controlled release operation.

### Option C — ask Anthropic to replace the submitted MCP origin with an owned GetCarWise domain and simultaneously move the submission to final V2

**Pros:** strongest long-term infrastructure ownership and consistency.  
**Risks:** not self-service; could trigger a fresh review or other process; queue impact unknown. Anthropic must tell us how they handle the change.

### Current recommendation

Do **not** pick A/B/C solely because of the two weeks already elapsed. First finish the V2 wording/no-regression analysis and determine whether the present V1 description is likely enough to fail that waiting is a poor trade-off. In parallel, preserve the current submission unchanged until André explicitly chooses the Anthropic path.

## 7. Affiliate/sponsored-content finding — revised

Current Anthropic policy/form language remains strict about sponsored/promoted content, so this topic cannot be erased from the compliance record.

However, the practical evidence now matters more:

- André confirms the previous CarClever Anthropic review already disclosed the affiliate arrangement and reviewers did not raise it as an issue;
- repository history records the three actual Anthropic blockers from that review as: assistant-directed imperatives in two tool descriptions, missing listing icon, and ChatGPT-specific documentation;
- the current Find My Car submission also records an Edmunds affiliate disclosure.

**Revised risk:** WATCH / consistency check, **not a current V2 release blocker**.

Required discipline:

- do not make ranking/pay-to-play dependent on affiliate economics;
- keep affiliate disclosure transparent and consistent with the implementation;
- if the commercial model materially changes, re-open the policy assessment;
- if Anthropic raises the issue in the current review, treat their direct feedback as authoritative for the next submission step.

## 8. Queue-position uncertainty

No authoritative source reviewed so far states whether a voluntary edit/resubmission of an already `In review` server keeps or resets its queue position.

The live page's `Last updated` field and `submit changes for review` wording show that submission updates are tracked, but they do not answer the queue question.

Therefore the operating rule remains:

**Never tell André that an edit definitely preserves or definitely loses the existing two weeks. That is unknown unless the UI produces an explicit warning/result or Anthropic confirms it.**

If we choose to inspect the final save/resubmit step, capture the exact warning/button text before committing any edit. Do not save merely to discover what happens.

## 9. Final audit verdict

| Area | Verdict | Action |
|---|---|---|
| V2 overall functional design | PASS / already extensively tested | retain |
| V1 Anthropic description risk | MATERIAL | compare against known prior Anthropic description feedback before deciding whether waiting is sensible |
| V2 description/schema wording | CHANGE CAREFULLY | minimal neutralization + both-host no-regression testing |
| Tool names/annotations | PASS | retain |
| Affiliate routing | WATCH, not blocker | preserve disclosure/independent ranking; react only to new evidence or Anthropic feedback |
| Pending-submission MCP URL | NOT SELF-SERVICE EDITABLE | Anthropic manages URL/auth changes; support contact required |
| Rescan Tools | AVAILABLE | use only as part of controlled release if server tool surface changes |
| Queue impact of voluntary edit | UNKNOWN | do not guess; capture UI/support evidence |
| Exact Claude production custom domain | UNDECIDED | no hostname approved yet |
| V1→V2 Anthropic amendment | DECISION PENDING | description/no-regression assessment + URL strategy + edit-flow evidence first |

## 10. Ownership

- **ChatGPT:** policy/review analysis, description redline strategy, cross-platform release gate, independent verification and documentation.
- **Claude Engineering:** any source description/schema edits, branches, deployments, Vercel/domain changes, test-harness implementation.
- **André:** Anthropic submission/edit decision and any request to Anthropic to change the MCP origin.

## References

- Live Anthropic pending-submission Edit page supplied Sep 10, 2026.
- Current Anthropic Connectors Directory submission/review documentation and Software Directory Policy.
- Anthropic `anthropics/claude-ai-mcp` issue #828 for evidence that submission payloads contain `server_snapshot.tools`.
- `carclever-widget/TASKS.md` historical prior-review blockers.
- `carclever-widget/STATE.md` current Find My Car submission record.
- `carclever-find-my-car/release/v2/app/[transport]/route.ts`.
- `carclever-find-my-car/release/v2/lib/find-matching-vehicle-input.ts`.
- `carclever-find-my-car/release/v2/lib/link-resolution.ts`.
- `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md`.
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`.
