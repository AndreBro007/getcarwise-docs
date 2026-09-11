# CarClever V2 Negative-Invocation Baseline — 2026-09-11

**Status:** CLOSED — CHATGPT V2 + CLAUDE V2 CLEANROOM PASS 3/3

## Purpose

Verify that CarClever is **not invoked** for general automotive questions that do not require live vehicle inventory/search behavior.

These prompts come from the prior reviewer-facing negative test set.

## Test 1 — Brake-pad replacement

Prompt:

`How do I replace the brake pads on a 2020 Honda CR-V?`

### ChatGPT V2

Observed behavior: answered the repair/maintenance question directly. CarClever was not invoked.

Assessment: **PASS**.

### Claude V2 Cleanroom

Observed behavior: answered the repair/maintenance question directly. CarClever was not invoked.

Assessment: **PASS**.

Separate host-content note: Claude's repair guidance was less conservative around rear electronic parking-brake handling and included generic torque guidance. This is outside the CarClever invocation test and is not classified as a connector defect.

## Test 2 — F-150 towing-capacity factual question

Prompt:

`What is the towing capacity of a 2024 Ford F-150?`

### ChatGPT V2

Observed behavior: answered the general towing-capacity question directly and discussed configuration-specific limits. CarClever was not invoked.

Assessment: **PASS**.

### Claude V2 Cleanroom

Observed behavior: answered the general factual/specification question directly. CarClever was not invoked.

Assessment: **PASS**.

## Test 3 — Hybrid vs gas pros/cons

Prompt:

`What are the pros and cons of hybrid cars compared with gas cars?`

### ChatGPT V2

Observed behavior: answered the general explanatory comparison directly. CarClever was not invoked.

Assessment: **PASS**.

### Claude V2 Cleanroom

Observed behavior: answered the general explanatory comparison directly. CarClever was not invoked.

Assessment: **PASS**.

## Final conclusion

The full negative-invocation set is clean across both active V2 host environments:

- Brake-pad replacement — ChatGPT V2 PASS; Claude V2 Cleanroom PASS.
- F-150 towing-capacity question — ChatGPT V2 PASS; Claude V2 Cleanroom PASS.
- Hybrid-vs-gas comparison — ChatGPT V2 PASS; Claude V2 Cleanroom PASS.

**Overall:** 3/3 negative prompts behaved correctly on both hosts. CarClever remained out of scope for general repair, factual specification, and educational comparison questions.

Per current regression protocol, V1 was intentionally skipped for this final negative-invocation set after André confirmed it was unnecessary.