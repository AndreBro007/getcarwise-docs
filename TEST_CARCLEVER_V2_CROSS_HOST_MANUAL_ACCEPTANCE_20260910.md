# CarClever V2 Cross-Host Manual Acceptance — 2026-09-10

**Status:** ACTIVE — testing one case at a time  
**Purpose:** Final manual host-level validation of the current V2 code/description contract in ChatGPT and Claude, followed by same-prompt V1 comparison, before production/submission decisions.  
**Candidate:** current `release/v2`; exact deployed SHA and endpoint to be captured with results.  
**Method:** Natural user prompts only. No prompt engineering or hints that reveal expected tool arguments. After each host answers, a separate short follow-up requests the exact tool-call JSON so the structured call can be compared. Results are reviewed before moving to the next case.

## Test sequence — locked

### Phase 1 — V2 acceptance first
For each case: ChatGPT V2 → JSON → Claude V2 → JSON → review/record. Do not run V1 until the V2-only result has been reviewed.

### Phase 2 — V1 comparison after V2 verdict
Run the same user request through `CarClever - Find My Car` in ChatGPT and Claude, capture JSON where available, then compare V1 vs V2 by host and cross-host. Live inventory need not return identical VINs; compare intent, arguments, constraints, candidate scope, disclosures, ranking and material result quality.

## Test design rules

- Use realistic user language and vary price semantics, geography, body styles, drivetrain, electrification, history, trim and optimization intent.
- Concentrate on known tricky paths and special code/description contracts with the fewest useful prompts.
- Compare structured intent and actual behavior; prose need not be identical.
- Do not change code/descriptions during the run unless a completed case demonstrates a concrete defect.
- Distinguish **actual tool-call arguments** from host-reconstructed JSON. A follow-up summary that contains results/plugin metadata is not automatically proof of the original call arguments.
- Review each case before proceeding.

## Case 01 — broad size-class SUV + strict price ceiling + ZIP

**Status:** CHATGPT V2 RUN RECEIVED — PROVISIONAL; need exact tool-call args + Claude V2 run

### Intended clean user prompt

ChatGPT: `Find me a large SUV under 60k in 90210`

Claude: `Use connector CarClever V2 Test and find me a large SUV under 60k in 90210`

### Actual ChatGPT prompt used

`@CarClever V2 Test can you see the plugin and what tools does it have, then Find me a large SUV under 60k in 90210`

**Method note:** this run first asked the host to inspect/list the connector tools. That is useful for confirming visibility, but it is not a perfectly clean natural-search-only run because exposing the tool surface may prime the host. Keep the result, but if Case 01 otherwise passes we may later decide whether a clean-search-only repeat is worth doing.

### ChatGPT V2 answer observed

The host saw two tools (`_find_matching_vehicle`, `_resolve_dealer_url`) and returned five plausible full-size/large SUVs under $60k around 90210:

- 2025 Ford Expedition MAX Active — $44,789 — VIN `1FMJK1H84SEA35172`
- 2025 Nissan Armada SV — $49,995 — VIN `JN8AY3AD7S9301089`
- 2025 Jeep Wagoneer 4WD — $50,573 — VIN `1C4SJVAP2SS507259`
- 2025 Chevrolet Suburban Z71 4WD — $59,680 — VIN `1GNS6DRD0SR216215`
- 2025 Ford Expedition Active 4WD CPO — $43,752 — VIN `1FMJU1J81SEA20973`

The host selected the Armada as its shortlist pick and described it as a low-risk/value balance.

### JSON returned after `Give me the JSON values`

The host returned a **composite/reconstructed object**, not clearly the raw original tool-call payload. It included plugin/tool descriptions, a `search` object and full result objects.

Reported `search` values:

```json
{
  "zip": "90210",
  "radiusMiles": 100,
  "priceMax": 60000,
  "priceFlexibility": "strict",
  "vehicleType": "SUV",
  "bodyType": "SUV",
  "used": true,
  "priorityAxis": "best_for_budget",
  "model": "Tahoe, Suburban, Expedition, Yukon, Yukon XL, Sequoia, Armada, Wagoneer, Grand Wagoneer, Escalade, Navigator",
  "vehicleNeeds": [
    "large SUV",
    "three-row family SUV",
    "full-size SUV under $60,000 near 90210"
  ]
}
```

### Provisional ChatGPT V2 review

**Positive:**
- Correct `priceMax: 60000` and strict ceiling semantics.
- Correct ZIP.
- Correct broad SUV body style.
- Strong candidate-model resolution: the model list is materially consistent with large/full-size SUVs.
- `best_for_budget` is appropriate; did not incorrectly map a budget ceiling to `cheapest`.
- Returned results are plausible large SUVs and all reported prices are below the stated ceiling.

**Needs verification before verdict:**
- `radiusMiles: 100` was not stated by the user. The schema explicitly allows radius omission and applies the service default when omitted. If 100 was actually sent by the host, it is an inferred hard constraint rather than a user-stated one.
- `used: true` was not stated. Current V2 schema says omitted condition includes both new and used. If this was in the actual call, this is a material unintended narrowing.
- `vehicleType: "SUV"` is redundant with `bodyType: "SUV"`; `vehicleType` is intended for finer classification when expressly distinguished by the user.
- `vehicleNeeds` added `three-row family SUV`, which the user did not request, and repeats hard constraints in soft context. This may be host reconstruction rather than the actual tool call, so do not diagnose code/description yet.
- The host's statement that the Armada is the best `lowest-risk/value balance` goes beyond the user's request and is not clearly supported as a unique lower-risk winner because several returned vehicles were reported `riskTier: positive`. Treat as minor prose-quality observation unless repeated.

### Required follow-up before Case 01 ChatGPT verdict

Ask ChatGPT:

`Give me only the exact JSON arguments sent to _find_matching_vehicle.`

If the UI exposes the original tool-call details directly, copying those exact arguments is even stronger evidence than a generated follow-up answer.

Also record whether the CarClever card/widget rendered normally (images, buttons/links, no error).

### Expected structured intent — review criteria

- `priceMax: 60000`
- `zip: "90210"`
- `bodyType: "SUV"`
- sensible large-SUV candidate models
- large-SUV need represented without inventing unrelated requirements
- no invented year/mileage/drivetrain/fuel/seating/make/condition/trim/history constraints
- strict price semantics
- priority omitted/default or `best_for_budget`, not `cheapest`

### Result capture

#### ChatGPT V2
- Full answer: RECEIVED
- Composite JSON: RECEIVED
- Exact raw tool-call arguments: PENDING
- UI/card behavior: PENDING
- Provisional verdict: **PROMISING, NOT YET PASS/FAIL**

#### Claude V2
- Full answer: PENDING
- JSON/tool arguments: PENDING
- UI/card behavior: PENDING
- Notes: PENDING

#### V2-only verdict
PENDING

#### V1 comparison
HOLD until V2-only verdict completed.

## Planned coverage after Case 01

Subsequent cases will be selected one at a time based on prior results, covering with the minimum useful set: family/practical needs, teen/commuter/towing, direct make/model, body style vs finer vehicle type, city/state/ZIP/radius geography, strict vs approximate price, cheapest vs best-for-budget/newest/lowest-mileage/lower-risk, AWD/transmission/cylinders/colors/doors, trim required vs preferred, hybrid/PHEV/EV required vs preferred, used/new/CPO/history/one-owner evidence, exact VIN/not-found VIN, thin/zero results and widening, cross-brand candidates, UI/widget/link behavior, and negative non-inventory requests where the connector should not be called.
