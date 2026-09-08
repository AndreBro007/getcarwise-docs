# V2 Shared Contract — Discovery Run Findings (Sep 8, 2026 session)

**Status:** Partial evidence gathered. No implementation done. No production code touched.
Probe: `research/v2-schema-probe` branch, deployed at
`https://carclever-v2-schema-probe.vercel.app/research-probe/mcp`
(Production env on its own isolated Vercel project — no link to carclever-find-my-car.)

## Confirmed findings

### 1. ChatGPT never resolves practical needs into a model list — confirmed regression
Tested across 5 separate prompts (family SUV, teen driver, family-of-five/cargo, cross-brand
hybrid SUV explicitly saying "don't limit me to one model"). ChatGPT never once populated
`model` with resolved candidates — only `bodyType`/`vehicleType` + `vehicleNeeds`. This
reproduces the "Open: critical" risk flagged in the equivalence gate: V1's explicit,
repeated instruction to "resolve into a real comma-separated model list, every time" is
gone from the short description, and ChatGPT does not do this resolution without it.

### 2. Claude DOES resolve practical needs correctly — same description, opposite result
Same prompts run against Claude (via direct model self-report, since Claude's connector
doesn't surface raw structuredContent — see Finding 4): Claude reliably produced real,
sometimes 10-14-item, comma-separated model lists, including for the explicit
"don't limit me to one model" cross-brand hybrid case. This means the regression is
**ChatGPT-specific, not a description-wide defect.** The short description alone is
sufficient to cue this behavior on at least one host.

**Open question, not yet answered:** why does ChatGPT diverge from Claude on identical
input? Worth a direct follow-up to ChatGPT asking what in the tool description it used
(or didn't find) to decide not to resolve models — before touching the description text.
Rewriting the description now risks either reintroducing V1-style verbose prose or fixing
nothing, since the actual cause (wording ambiguity vs. ChatGPT-side interpretation
tendency) isn't established yet.

### 3. Ambiguous city ("Springfield") — confirmed regression on ChatGPT, inconclusive on Claude
ChatGPT silently resolved "Springfield" to a specific state (MO) twice, with no
clarifying question — a real regression against the locked rule.
Claude recognized the ambiguity correctly but the test methodology (forced to run all
calls literally rather than have a real conversation) means it couldn't actually pause
and ask — it instead omitted location and searched nationwide. This is a test artifact,
not evidence Claude would fail this in real use. Needs re-testing in a natural
back-and-forth conversation, not a forced batch run.

### 4. Claude's connector does not surface `structuredContent` — platform-level finding
Confirmed multiple ways: UI inspection, direct instruction to Claude to reproduce raw
JSON, my own direct tool-calling path, and a raw request/response debug view the user
found — none showed a `structuredContent` field, only the plain-text `content` summary.
Adding an `outputSchema` to the probe (commit `ec53d60`) did NOT fix this — ruled out as
the cause. This appears to be a genuine Claude.ai custom-connector platform limitation,
not a probe bug. ChatGPT's connector reliably surfaces `structuredContent`.
**Consequence:** Claude-side evidence for this whole discovery run has to come from
Claude self-reporting field names/values in prose, not raw JSON — lower precision
(no exact character counts) but still usable for behavioral questions (did it resolve
models, did it ask about the ambiguous city).

### 5. Claude used `goals`, not `vehicleNeeds` — unresolved anomaly
In the same self-report round, Claude referred to the field it used as `goals`
(the deprecated, unsupported legacy name) rather than `vehicleNeeds` (what the probe
schema actually exposes — verified in the probe's own code). Two possible explanations,
not yet distinguished:
  (a) Claude pattern-matched a plausible-sounding field name from general/training
      familiarity rather than reading the actual schema it was given this session, or
  (b) something about how the connector or schema was presented to Claude caused it to
      see/prefer a different field name than what's actually registered.
**This needs checking before drawing conclusions** — if (a), it's a caution about
trusting any single-session self-report from Claude as accurately reflecting the real
schema at all, which would affect how much weight Finding 2's positive result should
carry.

## Not yet done
- Diagnosing why ChatGPT and Claude diverge on model-list resolution (Finding 2's open question)
- Re-testing the ambiguous-city case in a natural conversation on both hosts
- Resolving the `goals`/`vehicleNeeds` anomaly (Finding 5)
- The `model` field cap — still no real evidence, though Claude's 14-item hybrid list is
  the first concrete data point (14 items, each a real model/trim name up to ~25 chars,
  well under the current 500-char research ceiling — but one data point isn't a cap)
- Fragile-field (interiorColor/cylinders/vehicleType) retest on Claude specifically
  (only ChatGPT has clean data for these so far)

## Explicitly not done tonight, and shouldn't be rushed
- No description rewrite — premature without knowing root cause of Finding 1/2 divergence
- No schema/cap changes to the locked public contract
- No changes to release/v2, V1, or any production system — all work stayed on the
  isolated research branch and probe deployment

## Next session should start with
1. Decide whether to chase Findings 2/4/5 further, or treat ChatGPT's clean data (fields
   that did work: electrification required/preferred, fragile fields, named variants) as
   sufficient and design the practical-need fix based on ChatGPT's behavior specifically
   (since that's the platform with the confirmed gap).
2. If chasing further: a direct diagnostic prompt to ChatGPT about its own reasoning,
   and a clean re-run of the ambiguous-city case as a real conversation on both hosts.
