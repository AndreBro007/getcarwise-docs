# CarClever V2 Cross-Host Manual Acceptance — 2026-09-10

**Status:** ACTIVE — systematic V2 regression testing, one case at a time  
**Purpose:** Final manual host-level validation of the current V2 code/description contract in ChatGPT and Claude, followed by same-prompt V1 comparison after the relevant V2 baseline is established.  
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
8. Assign PASS / INVESTIGATE / FAIL for the V2 baseline.
9. Run the same prompt through V1 on the available hosts once the V2 baseline is established.
10. Record V1↔V2 differences in intent handling, request semantics, result quality, UI and disclosures; do not require identical live VINs.
11. Only then move to the next test.

Do not revisit architecture unless testing exposes a real issue.

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

**V2 status:** **PASS**

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

### V2 behavior comparison

ChatGPT's candidate interpretation was narrower and more full-size-oriented. Claude's was broader and included some three-row/midsize family SUVs. Both are defensible interpretations of ordinary user language.

The important contract behavior passed on both hosts: the practical phrase was converted into real model candidates and the backend returned matching inventory without a demonstrated constraint failure.

### V2 backend assessment

**PASS.** No backend defect identified.

### V2 UI/widget assessment

**PASS on both platforms.** Verified as working:

- Images
- Buttons
- Risk badges
- Dealer links
- Affiliate links
- Layout

### V2 Test #1 verdict

**PASS — no code changes and no description changes recommended.**

Recommended action: record the host interpretation difference as expected cross-host variance and continue regression testing.

## Test #1 — V1 comparison

### ChatGPT V1 observed result

The same user request was run through the submitted `CarClever - Find My Car` V1 connector in ChatGPT.

Observed V1 behavior:

- Search reported approximately **3.4 million listings**, **1,118 matches**, within **50 miles** of 90210, with **no constraints relaxed**.
- Returned eight large/full-size SUV matches, including Nissan Armada, Jeep Wagoneer, Ford Expedition / Expedition MAX and Chevrolet Tahoe.
- Mix included both new and used inventory.
- Result prices stayed below the stated $60k ceiling.
- Host shortlist emphasized the new Armada for value, a 2024 Tahoe for low-mileage 4WD V8 appeal, and an Expedition MAX for cargo capacity.
- User-facing response surfaced seating, drivetrain, mileage, history/use notes and Carfax/listing links.
- Widget rendered successfully.

### V1 request evidence

**Raw V1 request JSON was not supplied for this run.** Do not infer exact V1 tool arguments from the prose response alone. If ChatGPT Desktop exposes the original V1 request, capture it later only if doing so is convenient; the visible behavior is sufficient for the current high-level V1↔V2 comparison.

### V1 ↔ V2 comparison

**Intent fidelity:** PASS on both. Both interpreted the query as a search for genuinely large/full-size SUVs under $60k in the 90210 area.

**Candidate/result scope:** broadly equivalent. V1 returned Armada, Wagoneer, Expedition, Expedition MAX and Tahoe; V2 also returned those core full-size nameplates, with some host-specific candidate variation. No material evidence that V2 lost the core V1 practical-need capability.

**Condition handling:** V1 visibly included both new and used inventory, which is consistent with the user not specifying condition. V2's actual ChatGPT request also correctly omitted an invented used/new restriction.

**Budget handling:** both respected the under-$60k ceiling. V2's request evidence additionally confirms `best_for_budget` rather than an incorrect `cheapest` mapping.

**Location:** V1 explicitly reported a 50-mile search radius. V2 actual ChatGPT request omitted a radius and allowed the service default. This is not a regression by itself; exact radius behavior should only be treated as a defect if returned geography becomes materially inconsistent with the request or the contract.

**Result count:** V1 reported 1,118 matches versus the V2 ChatGPT widget's smaller count in the earlier run. Live counts are not expected to match because the host-resolved candidate model sets and timing differ. Count difference alone is not evidence of a regression.

**Presentation:** both produced useful ranked lists and functioning widgets. V1's prose surfaced more per-result detail in this run, while V2's widget passed its visual/interaction checks. This is presentation variance, not a demonstrated capability loss.

### Test #1 V1↔V2 verdict

**PASS — V2 preserves the material V1 behavior for this case.**

No regression identified in practical large-SUV intent resolution, strict budget handling, location use, mixed-condition eligibility, result relevance or widget functionality.

**Action:** no code or description change. Test #1 can be considered closed across V2 baseline + V1 comparison, subject only to optional later capture of V1 raw request JSON if convenient.

## Test #2 — hybrid SUV + approximate budget + city location

**Status:** DESIGNED — next test to execute

### Prompt

`Find me a hybrid SUV around $35k in Austin.`

### Why this is a better next test

Test #1 already covered a practical size phrase, an explicit SUV body style, a strict ceiling and a ZIP. Test #2 stays simple and natural while changing three meaningful semantics at once: hybrid requirement, approximate-price language, and city-only geography. It is easier to diagnose than a multi-clause family-needs prompt.

### Expected request behavior

Expected strong signals:

- a sensible Austin ZIP supplied by the host, or otherwise correct city handling allowed by the current contract;
- `bodyType: "SUV"`;
- hybrid/electrification represented consistently with the current V2 contract;
- a sensible comma-separated model candidate list where broad electrification requires model/variant candidates;
- approximate `around $35k` semantics treated as flexible rather than silently hardened into an exact ceiling;
- priority omitted/default or `best_for_budget`, not `cheapest` merely because a budget is present.

Acceptable host variation:

- Different representative Austin ZIPs.
- Different sensible hybrid-SUV candidate models across ChatGPT and Claude.
- Different ranking order among genuinely matching inventory.

Potential investigation triggers:

- Gas-only candidates included while the request is treated as a required hybrid search without disclosed broadening.
- No model candidate resolution for the broad hybrid request.
- Manufacturer-prefixed entries inside the `model` field.
- `around $35k` incorrectly forced into strict ceiling semantics without reason.
- Invented hard constraints for condition, year, mileage, drivetrain, trim, history or seating.
- `cheapest` selected simply because the user stated a budget.
- Location materially wrong for Austin without disclosure.

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
