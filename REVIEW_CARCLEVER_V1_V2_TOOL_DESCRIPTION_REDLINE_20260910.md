# CarClever V1→V2 Tool Description Review — 2026-09-10

**Status:** REVISED — DESCRIPTION CHANGES DEFERRED; no application code changed  
**Purpose:** Compare Anthropic's actual prior CarClever feedback with current V1/V2 MCP descriptions and determine whether any change is actually necessary before final V2 testing.  
**Owners:** ChatGPT = review/test design; Claude = implementation only after an explicit approved change; André = final approval and manual host testing where required.

## 1. Exact context of Anthropic's prior objection

The archived 2026-08-01 Anthropic MCP Directory email was re-read directly. Anthropic had re-tested the previous CarClever server and said the server itself was in good shape. Their wording objection was specifically to descriptions that **instruct the assistant in a way that can force unwanted invocation or override normal host judgment**.

Their examples were:

- `always invoke this tool ...`
- `Never block or refuse ...`
- `MUST call ... first`

Anthropic's explanation was that descriptions should describe what a tool does and when it is useful; **imperatives aimed at the assistant — especially never-refuse language — can force unwanted invocations and are not allowed in directory listings**.

### Revised interpretation

This is materially narrower than a blanket prohibition on clear usage guidance. Ordinary schema/contract instructions are not automatically equivalent to `MUST`, `always invoke`, or `never refuse` language.

That distinction matters for CarClever because the host must understand several non-obvious contract requirements — especially practical-needs candidate-model resolution and broad electrification searches. Removing or making these instructions vague can create a real search regression.

## 2. Current V1 risk

Current V1 (`main`) still contains substantially more assistant-directed mandatory language than V2, including `don't retry ... yourself`, `Before calling`, repeated `Never`, `Do not`, `every time`, and multiple answer-presentation instructions.

**Conclusion:** V1 remains more likely than V2 to attract the same category of review feedback Anthropic previously raised. That does not prove V1 will be rejected, but the risk is credible.

## 3. Current V2 risk — revised down

V2 is dramatically shorter and more capability-led than V1. The previously flagged phrases — for example `resolve ... yourself`, `before calling this tool`, `every time`, and `do not use ... alone` — are directive, but they are used to explain a genuine schema/host contract rather than to force tool invocation, suppress refusal, or override user intent.

The proposed neutralized alternatives were also judged by André to be less clear and more vague. That is a serious downside because these instructions exist specifically to prevent known host-routing/search failures.

### Current recommendation

**Do not change the V2 tool or field descriptions before the next testing phase.**

Treat the earlier redline as a contingency only. Re-open wording changes only if one of the following occurs:

1. Anthropic explicitly flags the current V2 wording or gives a narrower rule that clearly applies to it;
2. testing shows a specific description-induced host failure that can be improved safely;
3. a final compliance review identifies genuinely coercive language equivalent to the old `MUST` / `always invoke` / `never refuse` problem.

Do not change wording merely to make it less imperative if the replacement becomes harder for the host or humans to understand.

## 4. Why testing now has priority

V2 has already undergone extensive contract and equivalence work. The highest-value remaining evidence is whether the current V2 description/schema produces the right behavior in both ChatGPT and Claude across real host calls.

The testing phase should therefore use **current V2 wording unchanged** as the candidate unless a concrete defect appears.

Key checks:

- practical-needs requests still resolve to sensible real model candidates;
- broad hybrid/PHEV/EV requests include appropriate model/variant scope;
- required vs preferred electrification is preserved;
- manufacturer names are excluded from `model` values where expected;
- hard user constraints are preserved;
- no invented constraints appear;
- `best in my budget` does not collapse to `cheapest`;
- exact VIN, trim-required/preferred, lower-risk, radius/location and other high-value paths behave correctly;
- both hosts produce materially equivalent structured intent even if their prose differs.

## 5. Manual host test plan

Manual testing will be run in a fresh ChatGPT session because the current Claude session is token-constrained. Use a stable candidate endpoint and the current V2 wording. At minimum test:

1. family SUV with no named model;
2. reliable teen-driver car with no named model;
3. commuter car with no named model;
4. towing vehicle with no named model;
5. broad hybrid request with no named model;
6. hybrid required;
7. hybrid preferred;
8. PHEV required;
9. broad EV request;
10. explicit cheapest intent;
11. `best in my budget`;
12. lower-risk request;
13. required vs preferred trim;
14. exact VIN;
15. cross-brand multi-model request.

Record endpoint, exact deployed SHA, host/model, host-generated arguments where visible, results, UI/card behavior, latency, and any divergence.

## 6. Separate endpoint/hostname test

Before approving a permanent shared-test hostname, perform the clean A/B/C endpoint experiment using the same application SHA/configuration:

- A: long Vercel Preview/branch alias with Vercel Authentication confirmed off;
- B: short existing `ccfmc-dev` hostname;
- C: short temporary owned `getcarwise.app` hostname.

Test connector creation, tool discovery, MCP calls, widget/resource loading, and CSP/origin behavior in ChatGPT. This determines whether the historical Preview-hostname issue still exists and whether a custom short domain actually improves reliability.

## 7. Anthropic V1→V2 path — current leaning

After V2 passes the testing gates, the current preferred operational path is:

1. keep the **currently submitted Anthropic MCP URL** rather than attempting an immediate hostname change;
2. deliberately deploy the exact final tested V2 SHA behind that submitted URL;
3. immediately use the Anthropic submission UI's **Rescan tools** action and save/submit the listing update as one controlled operation;
4. record the exact before/after server SHA, tool scan state, submission state and any warning/queue text;
5. run a production smoke test against the same submitted URL;
6. treat any later move to an owned Anthropic hostname as a separate Anthropic-managed migration decision, informed by the support email already sent.

Important: do not silently replace the server while the review is active. If this path is chosen, deploy + rescan + save + verification are one controlled cutover.

Because the MCP URL is not self-service editable, saving an ordinary listing/tool rescan update should not be expected to trigger a URL-change discussion by itself. If Anthropic does not respond to the support email, the safest near-term choice is to leave the submitted URL unchanged through this V2 upgrade and revisit hostname ownership separately.

## 8. Decision status

- Exact production/test hostnames: **NOT APPROVED**.
- V2 description redline: **DEFERRED / contingency only**.
- Current V2 wording: **PREFERRED for next testing round**.
- Application implementation: **NO DESCRIPTION CHANGE REQUESTED**.
- Anthropic pending submission: **UNCHANGED / IN REVIEW**.
- Anthropic likely next path after testing: **same submitted URL + exact tested V2 SHA + Rescan Tools + controlled save**, pending André's final explicit approval.
- V3: **HARD PAUSED pending final V2 baseline/rebaseline work**.
