# CarClever V2 Cross-Host Manual Acceptance — 2026-09-10

**Status:** ACTIVE — testing one case at a time  
**Purpose:** Final manual host-level validation of the current V2 code/description contract in ChatGPT and Claude before production/submission decisions.  
**Candidate:** current `release/v2`; exact deployed SHA and endpoint to be captured with results.  
**Method:** Natural user prompts only. No prompt engineering or hints that reveal expected tool arguments. After each host answers, a separate short follow-up requests the JSON values used so the structured call can be compared. Results are reviewed before moving to the next case.

## Test design rules

- Use realistic user language and vary phrasing, price semantics, geography, body styles, drivetrain, electrification, history, trim and optimization intent across the pack.
- Concentrate coverage on known tricky paths and explicit code/description contracts while minimizing the total number of prompts.
- Compare ChatGPT and Claude on structured intent and actual result behavior; prose need not be identical.
- Do not change code or descriptions during the run unless a completed case demonstrates a concrete defect.
- Record exact host output and JSON where available. If the host reconstructs rather than exposes actual tool arguments, mark that distinction.
- Review each case before proceeding. Any defect becomes either a retest requirement or a candidate code/description issue for end-of-run triage.

## Case 01 — broad size-class SUV + strict price ceiling + ZIP

**Status:** PENDING USER RUN

### ChatGPT user prompt

`Find me a large SUV under 60k in 90210`

### Claude user prompt

`Use connector CarClever V2 Test and find me a large SUV under 60k in 90210`

### JSON follow-up for each host

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

#### ChatGPT

- Full answer: PENDING
- JSON/tool arguments: PENDING
- UI/card behavior: PENDING
- Notes: PENDING

#### Claude

- Full answer: PENDING
- JSON/tool arguments: PENDING
- UI/card behavior: PENDING
- Notes: PENDING

### Case verdict

PENDING

## Planned coverage after Case 01

Subsequent cases will be selected one at a time based on the prior result, with the minimum set needed to cover: practical/family needs, teen/commuter/towing, direct make/model, body style vs finer vehicle type, city/state/ZIP/radius geography, strict vs approximate price, cheapest vs best-for-budget/newest/lowest-mileage/lower-risk, AWD/transmission/cylinders/colors/doors, trim required vs preferred, conventional hybrid/PHEV/EV required vs preferred, used/new/CPO/history/one-owner evidence, exact VIN/not-found VIN, thin/zero results and widening, cross-brand candidates, UI/widget/link behavior, and negative non-inventory requests where the connector should not be called.
