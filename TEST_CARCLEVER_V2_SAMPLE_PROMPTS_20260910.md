# CarClever V2 Sample Prompt Bank — 2026-09-10

**Status:** ACTIVE REFERENCE — candidate prompts only; not a locked sequence.  
**Use:** Pick one prompt at a time after the previous case has been fully reviewed and recorded.  
**Principle:** Natural user language, minimal complexity, fewest prompts needed to exercise distinct contract paths. Do not tell the host which fields or arguments to send.

## Locked testing method

- Run each selected prompt on ChatGPT V2 and Claude V2.
- Capture ChatGPT Desktop actual Request JSON when exposed; do not substitute reconstructed follow-up JSON.
- Capture Claude `Request → Response → Widget`.
- Review host interpretation, backend behavior and widget behavior separately.
- Assign PASS / INVESTIGATE / FAIL before selecting another prompt.
- Do not change code or descriptions without concrete test evidence.
- V1 comparison comes only after the relevant V2 behavior has a baseline.

## Completed baseline

### Test #1 — broad size phrase + strict ceiling + ZIP

`Find me a large SUV under 60k in 90210`

**Result:** PASS.

## Recommended next case

### Test #2 — hybrid + approximate budget + city

`Find me a hybrid SUV around $35k in Austin.`

Why: simple real-user wording, but distinct from Test #1. It tests broad hybrid model resolution, approximate-price semantics and city-only location without adding family/seating/safety ambiguity.

## Later candidate prompts

These are deliberately short. Choose based on what remains untested; do not run as a batch.

### Direct make/model + trim

`Find me a Toyota Camry XSE under $35k in 10001.`

Primary paths: direct model, trim handling, strict price, ZIP.

### Explicit cheapest ranking + used condition

`Find me the cheapest used pickup under $40k near 30301.`

Primary paths: `cheapest` intent, used condition, truck/body style, ZIP/local search.

### Drivetrain

`Find me an AWD SUV under $45k in Denver.`

Primary paths: drivetrain, city-only location, strict budget.

### Required plug-in hybrid

`I only want a plug-in hybrid SUV under $50k in 98101.`

Primary paths: required PHEV semantics, model/variant candidate resolution, strict budget.

### Preferred electrification, gas allowed

`I'd prefer a hybrid, but gas is okay. Keep it under $30k in 60601.`

Primary paths: preferred rather than required electrification, strict budget, no explicit body style.

### CPO + history evidence

`Find me a CPO SUV with no accidents under $40k in 75001.`

Primary paths: CPO, accident-history evidence, strict budget.

### Lowest mileage

`Find me the lowest-mileage used Honda CR-V under $32k in 85001.`

Primary paths: direct model, used condition, `lowest_mileage`, strict budget.

### Newest

`Find me the newest Mazda CX-5 under $35k in 98101.`

Primary paths: direct model, `newest` ranking, strict budget.

### Lower-risk ranking

`Find me a lower-risk used SUV under $35k in 28202.`

Primary paths: lower-risk priority, used condition, broad body style.

### Exact VIN

`Find this VIN: 1HGCV1F39MA000000.`

Primary path: exact-VIN routing. Replace with a real known VIN from prior test evidence before execution if the placeholder is not known to exist.

### Thin/zero-result behavior

`Find me a manual Mazda MX-5 under $20k in 90210.`

Primary paths: model correction, transmission, thin/zero-result handling and any disclosed widening. Use only after normal-path cases are stable because this intentionally stresses a historically tricky path.

### Negative invocation case

`What's the difference between leasing and financing a car?`

Primary path: connector should normally not be needed for a general non-inventory explanation.

## Prompt-design guardrails

Prefer prompts with one or two new concepts plus ordinary location/budget context. Avoid piling together family size, safety, seating, cargo, fuel, drivetrain, condition and ranking in one case because a failure becomes hard to attribute. Practical-needs prompts are still important, but use them later as deliberate intent-expansion tests rather than as the immediate second case.
