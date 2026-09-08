# V2 Shared Contract — Discovery Run Final Findings

**Status:** Discovery complete. Public contract wording verified working on both
hosts. No production code touched throughout — all work stayed on
`research/v2-schema-probe` branch and its isolated Vercel project. `release/v2`
confirmed untouched at `fca5013` at every checkpoint.

## Summary

Three real regressions were found, root-caused, fixed, and verified against
V1-equivalent or better behavior on both ChatGPT and Claude. One additional
finding (Claude connector platform limitation) is documented as a permanent
testing-tooling constraint, not a contract defect.

## Finding 1 — Practical-need → model-list resolution (RESOLVED)

**Symptom:** Under the original short candidate description, ChatGPT never
resolved a practical need (e.g. "large family SUV") into real model names —
it only populated `bodyType`/`vehicleNeeds`, unlike V1 and unlike Claude
(which did this correctly from the start).

**Root cause, in order of discovery:**
1. The description didn't say *who* does the resolving (tool vs. calling
   assistant) — ChatGPT read it as the tool's job.
2. Field-level descriptions were entirely missing on the probe (structural
   gap, unrelated to wording).
3. Abstract principle statements (even field-level, even cross-referenced)
   didn't reliably trigger the behavior — needed concrete worked examples.
4. Concrete examples alone got the behavior working but revealed a second bug
   (Finding 2).
5. The examples-with-passive-voice wording was itself unreliable — imperative
   voice, matching V1's actual working pattern, was needed for consistent
   triggering.

**Fix (v8, commit `516abc7`):** Imperative-voice instruction in the main
description, the `model` field, and the `vehicleNeeds` field, all pointing at
each other, with worked examples. Full wording history in `CHANGE_LOG.md` on
the research branch.

**Verification:** 2/2 clean raw-JSON-verified passes on ChatGPT, 1/1 clean
self-reported pass on Claude (see Finding 4 for why Claude can't be raw-JSON
verified). Natural, unprompted phrasing ("I need a reliable large SUV for my
family") — no coaxing required.

## Finding 2 — Manufacturer names leaking into cross-brand model lists (RESOLVED)

**Symptom:** Once Finding 1's fix started working, `model` came back as
`"Chevrolet Tahoe, Ford Expedition, Toyota Sequoia..."` — every entry
prefixed with the manufacturer, violating the field's own no-manufacturer
rule. Per the field audit, a make-prefixed model string silently returns zero
real results on Auto.dev, not an error — this would have been a worse
regression than Finding 1's original bug.

**Root cause:** The `model` field's only worked example was a single-model
case ("E-Class" vs. "Mercedes-Benz E-Class") — never demonstrated in the
comma-separated, cross-brand shape that actually broke.

**Fix (v7, commit `4ad8453`):** Added an explicit cross-brand example to the
`model` field description: *"'CR-V, RAV4, Outback' is correct; 'Honda CR-V,
Toyota RAV4, Subaru Outback' is not."*

**Verification:** Both confirmed ChatGPT passes and the Claude self-report
show zero manufacturer names across 19 total resolved model entries.

## Finding 3 — priorityAxis budget-vs-cheapest disambiguation (RESOLVED)

**Symptom:** The candidate schema's `priorityAxis` field description dropped
V1's explicit warning that the word "budget" alone does not mean `cheapest`
— a real, identified gap, not yet observed failing but untested and known-risky.

**Fix (v7, commit `4ad8453`, same push as Finding 2):** Restored V1's
disambiguation language in the field description.

**Verification:** Confirmed correct — "$30,000 budget" → `best_for_budget`;
"cheapest" → `cheapest`, correctly distinct.

## Finding 4 — Claude connector doesn't surface structuredContent (DOCUMENTED, not fixable)

**Symptom:** Claude's chat UI/client never displays or gives Claude access to
a called tool's `structuredContent`, regardless of `outputSchema` presence
(tested explicitly — adding `outputSchema` did not fix it). ChatGPT's client
reliably surfaces it.

**Status:** Confirmed platform-level limitation, not a probe bug. Documented
here so future sessions don't re-investigate it. Practical consequence:
Claude-side evidence in this whole discovery run relies on self-report
(asking Claude to state what fields/values it sent), which is directionally
useful but not byte-exact verifiable the way ChatGPT's raw JSON is.

## Also tested and confirmed clean (no fix needed)

- Electrification required/preferred split — clean on both hosts throughout.
- Named hybrid/PHEV variants (RAV4 Prime, F-150 PowerBoost) — clean.
- Fragile direct fields (interior/exterior color, cylinders, vehicleType) —
  clean on both hosts.
- Ambiguous city clarification ("Springfield") — clean in natural
  conversation on both hosts; earlier apparent failures were forced-call
  test-methodology artifacts, not real regressions.
- Hybrid/PHEV variant-name string manipulation (V1's most fragile mechanism)
  — architecturally eliminated in V2's design (dedicated `electrificationTypes`
  + backend NHTSA classifier replace host-side string tricks). Confirmed the
  host no longer attempts V1's approach; the backend classifier itself is
  unverified pending real implementation (out of scope for this schema-only
  probe by design).

## Anthropic historic-feedback compliance check

The v8 imperative-voice wording was checked against
`CLAUDE_CURRENT_V1_ANTHROPIC_FEEDBACK_AUDIT_20260908.md` before being locked
in. The actual documented concern is narrow: descriptions that force tool
invocation, override refusal, or compel a second tool call — not imperative
language generally. V1's own field-routing imperatives were explicitly
assessed as NOT falling into that category, only a minor, non-blocking
"presentation risk." v8's wording is in the same benign category. Full
reasoning recorded in `CHANGE_LOG.md`.

## What's left before this can be called a locked public contract

1. The `model` field cap — still no real evidence-based number. Real host
   output so far: max observed length ~74 characters, 8-11 items. The
   generous 500-char research ceiling was never actually tested against a
   real limit; a production cap should come from a larger sample, not this
   handful of runs.
2. The provisional 50-char text-field caps (trimRequired, colors, etc.) —
   still provisional, never boundary-tested against real host output.
3. A second, independent round of testing (not run by the same person who
   iterated the fixes) would strengthen confidence before submission,
   given how much run-to-run variance was observed throughout this process.
4. Decide whether v8's imperative-voice trade-off is acceptable for the
   actual Anthropic/OpenAI submission, given the minor style-risk noted above
   — this is a judgment call for André/ChatGPT to confirm, not something this
   probe can settle.

No implementation of the real V2 schema begins until these are explicitly
signed off, per the locked two-gate sequence from earlier in this process.
