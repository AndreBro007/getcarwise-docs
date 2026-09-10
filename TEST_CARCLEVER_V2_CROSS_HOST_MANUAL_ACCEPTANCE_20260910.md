# CarClever V2 Cross-Host Manual Acceptance — 2026-09-10

**Status:** ACTIVE — systematic V2 regression testing, one case at a time  
**Purpose:** Final manual host-level validation of the current V2 code/description contract in ChatGPT and Claude, followed by same-prompt V1 comparison only after the V2 baseline is established.  
**Candidate:** current `release/v2`; test current V2 exactly as-is.  
**Method:** Natural user prompts only. Test like real users. Do not change code or descriptions unless a completed test provides concrete evidence of a defect.

## Locked testing sequence

1. Run one natural-language test on ChatGPT V2.
2. Capture the response, actual request JSON from ChatGPT Desktop when available, screenshot, and notes.
3. Run the same natural-language test on Claude V2.
4. Capture Claude's Request, Response, screenshot/widget, and notes.
5. Compare host behavior.
6. Assess backend behavior separately from host interpretation.
7. Assess UI/widget behavior separately.
8. Assign PASS / INVESTIGATE / FAIL.
9. Record the recommended action.
10. Only then move to the next test.

Do not compare against V1 until the V2 baseline for the relevant behavior has been established. Do not revisit architecture unless testing exposes a real issue.

## Evidence hierarchy for tool requests

### ChatGPT Desktop

When the Desktop client exposes the tool request, treat that displayed request JSON as the strongest evidence of what ChatGPT actually sent to the MCP tool. Copy it exactly where practical.

Do **not** replace actual Desktop request JSON with a later model-generated reconstruction.

### ChatGPT Mobile/Web

A JSON object reconstructed by the host in a follow-up answer can be useful for diagnosis, but it is not proof of the actual MCP request. Label it as reconstructed/composite unless the UI explicitly shows the original tool request.

### Claude

Claude exposes a useful three-part debugging surface:

`Request → Response → Widget`

Use the Request view as the primary Claude request evidence, then compare the Response payload and rendered Widget. Claude is therefore the primary MCP debugging platform when tracing request/response/widget behavior end to end.

## Test #1 — large SUV + strict price ceiling + ZIP

**Prompt:** `Find me a large SUV under 60k in 90210`

**Status:** **PASS**

### ChatGPT V2

ChatGPT interpreted “large SUV” primarily as full-size/large nameplates such as Tahoe, Expedition, Yukon, Sequoia, Armada and Wagoneer.

Actual ChatGPT Desktop request JSON:

```json
{
  "priceMax": 60000,
  "priorityAxis": "best_for_budget",
  "zip": "90210",
  "bodyType": "SUV",
  "model": "Tahoe, Expedition, Sequoia, Yukon, Armada, Wagoneer",
  "vehicleNeeds": ["large SUV"]
}
```

Assessment:

- Correct strict price ceiling.
- Correct ZIP.
- Correct broad SUV body style.
- Correct `best_for_budget` interpretation; “under 60k” was not misread as “cheapest.”
- Practical need was resolved into a real cross-brand model list.
- No manufacturer names leaked into the comma-separated `model` field.
- No invented used/new condition, radius, drivetrain, fuel, year, mileage, trim, seating or history constraints appeared in the actual request.

The earlier composite/reconstructed ChatGPT JSON that contained inferred `used`, `radiusMiles`, `vehicleType`, and extra `vehicleNeeds` must not be treated as the actual MCP request. The Desktop request above supersedes it as request evidence.

### Claude V2

Claude interpreted “large SUV” more broadly, including candidates such as Tahoe, Suburban, Explorer, Highlander, Pilot, Ascent, Telluride and Pathfinder.

Assessment:

- The broader model set is a host interpretation difference, not evidence of a server defect.
- The server handled the supplied request correctly.
- No code or description change is justified by this difference.

### Behavior comparison

ChatGPT's candidate interpretation was narrower and more full-size-oriented. Claude's was broader and included some three-row/midsize family SUVs. Both are defensible interpretations of ordinary user language.

The important contract behavior passed on both hosts: the practical phrase was converted into real model candidates and the backend returned matching inventory without a demonstrated constraint failure.

### Backend assessment

**PASS.** No backend defect identified.

### UI/widget assessment

**PASS on both platforms.** Verified as working:

- Images
- Buttons
- Risk badges
- Dealer links
- Affiliate links
- Layout

### Test #1 verdict

**PASS — no code changes and no description changes recommended.**

Recommended action: record the host interpretation difference as expected cross-host variance and continue regression testing.

## Test #2 — family/practical-needs model resolution without explicit vehicle class

**Status:** DESIGNED — next test to execute

### Prompt

`I've got three kids and need something practical for school runs and family trips. Find me something under $35k in 78701.`

### Why this is a different test

Test #1 supplied an explicit vehicle class (`SUV`) plus the phrase “large SUV.” Test #2 deliberately supplies **no make, model, body type, drivetrain, fuel, condition, year, mileage, trim or vehicle class**. It tests whether each host can turn ordinary family/practical-needs language into sensible real model candidates without inventing unrelated hard constraints.

### Expected request behavior

Expected strong signals:

- `priceMax: 35000`
- `zip: "78701"`
- `vehicleNeeds` carrying concise family/practical-use intent
- a sensible comma-separated `model` list containing real model names without manufacturer prefixes
- priority omitted/default or `best_for_budget`

Acceptable host variation:

- Different sensible candidate models across ChatGPT and Claude.
- Different mixes of sedan, hatchback, SUV or minivan candidates where each is defensible for three children, school runs and family trips.
- A seating preference if the host interprets three children as a practical seating need, provided it is not represented as stronger than the user actually stated.

Potential investigation triggers:

- No model list despite the practical-needs instruction in the current V2 contract.
- Manufacturer-prefixed entries in `model`.
- An invented hard body type, drivetrain, fuel type, new/used condition, year, mileage, trim or history requirement with no basis in the prompt.
- `cheapest` selected merely because the user supplied a price ceiling.
- Family/practical intent present only as prose while candidate scope remains effectively unconstrained.
- Returned results materially violating the actual price/location request without a disclosed relaxation.

### Test #2 record template

#### ChatGPT
- Response: PENDING
- Actual Request JSON (Desktop if available): PENDING
- Screenshot: PENDING
- Notes: PENDING

#### Claude
- Request: PENDING
- Response: PENDING
- Screenshot/widget: PENDING
- Notes: PENDING

#### Behavior comparison
PENDING

#### Backend assessment
PENDING

#### UI assessment
PENDING

#### Verdict
PENDING — PASS / INVESTIGATE / FAIL

#### Recommended action
PENDING

## Remaining coverage

Select later cases one at a time after Test #2 is fully analysed. The remaining suite should eventually cover direct make/model, body style versus finer vehicle type, city/state/ZIP/radius geography, strict versus approximate price, cheapest versus best-for-budget/newest/lowest-mileage/lower-risk, AWD/transmission/cylinders/colors/doors, trim required versus preferred, hybrid/PHEV/EV required versus preferred, used/new/CPO/history/one-owner evidence, exact VIN/not-found VIN, thin/zero results and widening, UI/widget/link behavior, and negative non-inventory requests where the connector should not be called.
