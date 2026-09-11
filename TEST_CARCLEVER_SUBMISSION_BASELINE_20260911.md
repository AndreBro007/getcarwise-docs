# CarClever Submission Baseline — 2026-09-11

Source: the actual prior OpenAI submission JSON supplied by André for CarClever - Find My Car v1.0.0.

## Purpose

Use this as the authoritative baseline for the user intents and negative-invocation cases explicitly declared in the last submission. Do not blindly copy old architecture/tool-description text into the next submission; reuse the test intents and expected product behavior, then update tool names, schemas, descriptions, screenshots, and URLs to match the final V2 production build.

## Prior positive submission test cases

1. `Find a used Honda CR-V under $25,000 with less than 60,000 miles near 90210.`
   - Expected: current used Honda CR-V listings; budget, mileage, and location preserved; no silent hard-constraint violation.

2. `Find a reliable hybrid SUV under $50,000 with less than 60,000 miles near 90210.`
   - Expected: shopping intent recognized; relevant hybrid SUV shortlist; price, mileage, location preserved; explain why results are strong matches.

3. `Find a low-risk used F-150 under $50,000 for towing near Denver.`
   - Expected: current used F-150 inventory; lower-risk ranking; preserve budget and towing intent; stronger reported history evidence ranked ahead of unknown/concerning history where available.

4. `Check VIN 4T1BF3EK7BU748352 for red flags before I buy it.`
   - Expected: exact VIN only; Buyer Check; reported accident concern and caution outcome; no similar-vehicle substitution.

5. `Click “Check availability” on one of the returned vehicle listings.`
   - Expected: resolve selected vehicle to the correct live availability destination; fallback to similar vehicles if the exact listing is gone.

## Prior negative submission test cases

These explicitly expected CarClever not to invoke:

1. `How do I replace the brake pads on a 2020 Honda CR-V?`
2. `What is the towing capacity of a 2024 Ford F-150?`
3. `What are the pros and cons of hybrid cars compared with gas cars?`

## Submission screenshots used last time

The prior submission included screenshots for these user prompts:

- `reliable hybrid SUV under $40k in 90210`
- `low risk used F150 < $50k for towing in Denver`
- `check VIN 4T1BF3EK7BU748352 for red flags`

These are useful candidates for final V2 screenshot/demo validation because they exercise semantic model resolution, lower-risk ranking, and exact-VIN Buyer Check.

## Important architecture note

The prior submission exposed `find_matching_vehicle` and `resolve_dealer_url` with the V1 production MCP origin `https://carclever-find-my-car.vercel.app/mcp`. The final V2 submission must be generated from the final V2 production MCP contract and endpoint. Do not carry forward stale V1 schema/description text merely because it appeared in the last submission.

## Remaining V2 regression implication

Before final submission, the regression bank should include:

- all remaining specialist-field checks already planned;
- at least one or two mainstream/popular buyer prompts;
- the four search-oriented positive submission cases above that remain relevant to the current V2 architecture;
- exact-VIN Buyer Check using the prior known VIN if still live, otherwise another verified current VIN with the same exact-lookup behavior;
- the three exact negative-invocation prompts above;
- availability/dealer-link behavior after at least one live result is returned.

Default comparison protocol remains ChatGPT V2 → Claude V2 Cleanroom → ChatGPT V1 where practical, with V1 serving as a behavioral baseline rather than only an anomaly diagnostic.
