# CarClever V2 Cross-Host Manual Acceptance — 2026-09-10

**Status:** ACTIVE — testing one case at a time  
**Purpose:** Final manual host-level validation of the current V2 code/description contract in ChatGPT and Claude, followed by same-prompt V1 comparison, before production/submission decisions.  
**Candidate:** current `release/v2`; exact deployed SHA and endpoint to be captured with results.  
**Method:** Natural user prompts only. No prompt engineering or hints that reveal expected tool arguments. After each host answers, a separate short follow-up requests the JSON values used so the structured call can be compared. Results are reviewed before moving to the next case.

## Test sequence — locked

Testing is deliberately split into two phases so V2 is judged on its own before V1 comparison can bias the review.

### Phase 1 — V2 acceptance first

For each case:

1. Run the natural-language prompt in ChatGPT against `CarClever V2 Test`.
2. Request the JSON values used.
3. Run the equivalent natural-language prompt in Claude using connector `CarClever V2 Test`.
4. Request the JSON values used.
5. Paste both V2 results back for review.
6. ChatGPT records the V2-only verdict and determines whether more information or a retest is needed.

Do **not** run V1 yet while Phase 1 for that case is under review.

### Phase 2 — V1 comparison after V2 verdict

Once the V2 result for the case is accepted/reviewed:

1. Run the same natural user request through the V1 `CarClever - Find My Car` connector in ChatGPT.
2. Request the JSON values if available.
3. Run the same request in Claude explicitly using connector `CarClever - Find My Car`.
4. Request the JSON values.
5. Compare V1 vs V2 separately for each host and then compare cross-host behavior.

The V1 comparison is diagnostic, not an instruction that V2 must return identical listings. Live inventory may change; the primary comparison is effective intent, structured arguments, constraint handling, candidate scope, disclosures, ranking behavior and material result quality.

## Test design rules

- Use realistic user language and vary phrasing, price semantics, geography, body styles, drivetrain, electrification, history, trim and optimization intent across the pack.
- Concentrate coverage on known tricky paths and explicit code/description contracts while minimizing the total number of prompts.
- Compare ChatGPT and Claude on structured intent and actual result behavior; prose need not be identical.
- Do not change code or descriptions during the run unless a completed case demonstrates a concrete defect.
- Record exact host output and JSON where available. If the host reconstructs rather than exposes actual tool arguments, mark that distinction.
- Review each case before proceeding. Any defect becomes either a retest requirement or a candidate code/description issue for end-of-run triage.

## Case 01 — broad size-class SUV + strict price ceiling + ZIP

**Status:** PENDING V2 USER RUN

### Phase 1 — V2 prompts

#### ChatGPT V2 user prompt

`Find me a large SUV under 60k in 90210`

#### Claude V2 user prompt

`Use connector CarClever V2 Test and find me a large SUV under 60k in 90210`

#### JSON follow-up for either host

`Give me the JSON values`

### Phase 2 — V1 prompts — HOLD until V2 verdict

#### ChatGPT V1 user prompt

`Find me a large SUV under 60k in 90210`

#### Claude V1 user prompt

`Use connector CarClever - Find My Car and find me a large SUV under 60k in 90210`

#### JSON follow-up for either host

`Give me the JSON values`

### Why this case exists

This exercises the practical-needs / size-class path where `large` is not a direct hard-filter field, while `SUV`, `$60,000`, and `90210` are directly representable. It checks whether the host resolves a broad size/class need into appropriate real model candidates rather than relying only on `bodyType`, while preserving the explicit price and ZIP constraints.

### Expected structured intent — review criteria, not user-facing prompt guidance

Strong evidence of correct interpretation includes:

- `priceMax: 60000`;
- `zip: "90210"`;
- `bodyType: "SUV"`;
- a sensible comma-separated `model` candidate set representing genuinely large SUVs rather than arbitrary SUVs;
- `vehicleNeeds` carrying the large-SUV/size need, or equivalent structured handling consistent with the current V2 contract;
- no invented year, mileage, drivetrain, fuel type, seating count, make, used/new status, trim, radius, history or other constraint;
- strict price semantics (`under 60k` must not be treated as flexible); explicit `priceFlexibility: "strict"` or omission are both acceptable because omitted ceilings are strict under the schema;
- `priorityAxis` may be omitted/defaulted or `best_for_budget`; it should not become `cheapest` merely because a price ceiling exists.

### Result capture

#### ChatGPT V2

- Full answer: PENDING
- JSON/tool arguments: PENDING
- UI/card behavior: PENDING
- Notes: PENDING

#### Claude V2

- Full answer: PENDING
- JSON/tool arguments: PENDING
- UI/card behavior: PENDING
- Notes: PENDING

#### V2-only verdict

PENDING

#### ChatGPT V1 comparison

- Full answer: HOLD
- JSON/tool arguments: HOLD
- UI/card behavior: HOLD
- Notes: HOLD

#### Claude V1 comparison

- Full answer: HOLD
- JSON/tool arguments: HOLD
- UI/card behavior: HOLD
- Notes: HOLD

#### V1↔V2 comparison verdict

HOLD until V2-only verdict completed.

## Planned coverage after Case 01

Subsequent cases will be selected one at a time based on the prior result, with the minimum set needed to cover: practical/family needs, teen/commuter/towing, direct make/model, body style vs finer vehicle type, city/state/ZIP/radius geography, strict vs approximate price, cheapest vs best-for-budget/newest/lowest-mileage/lower-risk, AWD/transmission/cylinders/colors/doors, trim required vs preferred, conventional hybrid/PHEV/EV required vs preferred, used/new/CPO/history/one-owner evidence, exact VIN/not-found VIN, thin/zero results and widening, cross-brand candidates, UI/widget/link behavior, and negative non-inventory requests where the connector should not be called.
