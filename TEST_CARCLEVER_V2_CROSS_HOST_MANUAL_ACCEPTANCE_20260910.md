# CarClever V2 Cross-Host Manual Acceptance — 2026-09-10

**Status:** ACTIVE — systematic V2 regression testing, one case at a time  
**Purpose:** Final manual host-level validation of the current V2 contract in ChatGPT and Claude, followed by same-prompt V1 comparison after the relevant V2 baseline is established.  
**Candidate:** current `release/v2`; test current V2 exactly as-is.  
**Method:** Natural user prompts only. Do not change code or descriptions unless completed testing provides concrete defect evidence.

## Locked testing sequence

1. Run one natural-language case on ChatGPT V2 and capture answer, widget, and actual Desktop request JSON when exposed.
2. Run the same case on Claude V2 and capture `Request → Response → Widget`.
3. Compare host interpretation, backend behavior, and UI separately; assign PASS / INVESTIGATE / FAIL.
4. Once the V2 baseline is established, run the same prompt through V1 on the available hosts and compare semantics/results rather than requiring identical live VINs.
5. Record the case fully before moving to the next test.

**Evidence rule:** ChatGPT Desktop exposed request JSON and Claude Request are primary request evidence. ChatGPT Web/Mobile reconstructed JSON is diagnostic only, not proof of the original MCP request.

## Test #1 — large SUV + strict price ceiling + ZIP

**Prompt:** `Find me a large SUV under 60k in 90210`

**Overall status: CLOSED — PASS.**

### ChatGPT V2

Actual Desktop request:

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

Observed results included plausible large/full-size SUVs under $60k such as Expedition/Expedition MAX, Armada, Wagoneer and Suburban. Widget/UI passed for images, buttons, risk badges, dealer/Carfax links, branding and affiliate disclosure. Earlier ChatGPT reconstructed JSON containing inferred `used`, `radiusMiles`, `vehicleType` and extra `vehicleNeeds` is superseded by the actual Desktop request above.

### Claude V2

Actual Request:

```json
{
  "model": "Tahoe,Suburban,Yukon,Expedition,Explorer,Highlander,4Runner,Pilot,Ascent,Telluride,Pathfinder",
  "bodyType": "SUV",
  "priceMax": 60000,
  "zip": "90210",
  "priorityAxis": "best_for_budget"
}
```

Claude resolved “large SUV” more broadly than ChatGPT, including some three-row/midsize candidates. This is host interpretation variance, not a demonstrated backend defect. Backend and widget/UI passed.

### ChatGPT V1

Observed V1 search reported approximately 3.4 million listings, 1,118 matches within 50 miles of 90210 and no constraints relaxed. It returned eight relevant large/full-size SUVs including Armada, Wagoneer, Expedition/Expedition MAX and Tahoe, with both new and used inventory and all prices below $60k. Widget rendered successfully.

Actual V1 Desktop request:

```json
{
  "bodyType": "SUV",
  "model": "Tahoe,Suburban,Yukon,Yukon XL,Expedition,Expedition MAX,Sequoia,Armada,Wagoneer,Grand Wagoneer,Escalade,Escalade ESV,Navigator,QX80",
  "priceMax": 60000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget",
  "zip": "90210",
  "radiusMiles": 50,
  "goals": [
    "large full-size SUV",
    "spacious interior",
    "strong value under budget"
  ]
}
```

### V1 ↔ V2 request comparison

- **Core intent:** equivalent. Both used `bodyType: SUV`, `priceMax: 60000`, `priorityAxis: best_for_budget`, ZIP 90210, and resolved real model candidates.
- **Budget semantics:** V1 explicitly sent `priceFlexibility: strict`; V2 omitted it. Under the V2 contract, an omitted ceiling remains strict, so this is semantically equivalent and V2 is leaner.
- **Location:** V1 explicitly sent `radiusMiles: 50`; V2 omitted radius and allowed the service default. This is a contract simplification, not a regression in this case.
- **Candidate breadth:** V1 sent a broader 14-model full-size list; ChatGPT V2 sent six core models, while Claude V2 used a different broader set. Despite that variation, V2 returned relevant large-SUV inventory and retained the core V1 capability in this case. Continue watching candidate breadth in later practical-needs cases; one passing case does not prove universal equivalence.
- **Soft intent:** V1 added broader inferred `goals` such as “spacious interior” and “strong value under budget”; V2 used the tighter `vehicleNeeds: ["large SUV"]` plus the explicit ranking axis. This is cleaner and avoids turning extra host inference into unnecessary search input.
- **Condition:** neither V1 nor V2 imposed an unrequested new/used condition; both allowed mixed inventory.
- **Results/UI:** both produced useful, relevant lists and working widgets. Different live counts/ranking are not regressions by themselves because candidate sets and inventory timing differ.

### Test #1 verdict

**PASS — V2 preserves the material V1 behavior for this case, with a leaner request contract.**

No regression identified in large-SUV intent resolution, strict budget handling, location use, mixed-condition eligibility, result relevance, or widget functionality. **No code or description change recommended. Test #1 is fully closed.**

## Test #2 — hybrid SUV + approximate budget + city location

**Status:** IN PROGRESS — V2 cross-host evidence captured; same-prompt V1 comparison next

**Prompt:** `Find me a hybrid SUV around $35k in Austin.`

Why: simple real-user wording, distinct from Test #1. It tests broad hybrid model resolution, approximate-price semantics and city-only geography without stacking subjective family/seating/safety requirements.

Expected strong signals: sensible Austin location handling; `bodyType: SUV`; hybrid/electrification represented consistently with the current V2 contract; sensible real model/variant candidates; `around $35k` treated as flexible rather than silently hardened; priority omitted/default or `best_for_budget`, not `cheapest` just because a budget exists.

Investigation triggers: gas-only candidates under a required-hybrid interpretation without disclosed broadening; no candidate-model resolution; manufacturer-prefixed entries in `model`; approximate budget forced to strict without reason; invented hard condition/year/mileage/drivetrain/trim/history/seating constraints; wrong location; or `cheapest` selected solely from the budget phrase.

### Test #2 record

#### ChatGPT V2

Observed response:

- Host chose Austin ZIP `78701`, 50-mile radius, required hybrid, SUV, flexible `$30k–$37k` range, `best_for_budget`, and automatic transmission.
- Reported 79 matches.
- Shortlist shown: 2026 Hyundai Tucson Hybrid SEL ($36,250, AWD, 20 mi), 2026 Kia Sportage Hybrid EX ($36,343, AWD, 10 mi), 2026 Honda CR-V Hybrid Sport ($36,563, FWD, 2 mi), another 2026 Kia Sportage Hybrid EX ($36,465, AWD, 11 mi), and 2027 Kia Sportage Hybrid EX ($36,791, AWD, 6 mi).
- Host stated all five were VIN-verified as hybrids and correctly disclosed that advertised prices may exclude tax/registration/dealer fees/accessories.
- Host appropriately noted that a hard $35,000 ceiling would be a different search and suggested used/CPO as a possible next search rather than silently treating the approximate budget as strict.

Actual Desktop request JSON supplied by André:

```json
{
  "bodyType": "SUV",
  "electrificationRequirement": "required",
  "electrificationTypes": [
    "hybrid"
  ],
  "model": "Toyota RAV4 Hybrid, Honda CR-V Hybrid, Hyundai Tucson Hybrid, Kia Sportage Hybrid, Ford Escape Hybrid",
  "priceMin": 30000,
  "priceMax": 37000,
  "priceFlexibility": "flexible",
  "priorityAxis": "best_for_budget",
  "radiusMiles": 50,
  "state": "TX",
  "zip": "78701",
  "vehicleNeeds": [
    "hybrid SUV around $35,000 in Austin"
  ],
  "transmission": "Automatic"
}
```

ChatGPT-side assessment:

- **PASS:** `bodyType: "SUV"` correctly reflects the explicit body style.
- **PASS:** `electrificationRequirement: "required"` plus `electrificationTypes: ["hybrid"]` correctly preserves the user's hybrid requirement.
- **PASS:** a real hybrid-SUV candidate list was resolved before the call, as required by the V2 tool contract.
- **PASS:** `priceMin: 30000`, `priceMax: 37000`, and `priceFlexibility: "flexible"` preserve approximate-budget semantics rather than silently hardening `$35k` into a strict ceiling. The exact band is host-selected, but its semantics are consistent with “around.”
- **PASS:** `priorityAxis: "best_for_budget"` is correct; the host did not misuse `cheapest`.
- **PASS:** Austin was anchored to ZIP `78701`; `state: "TX"` and `radiusMiles: 50` are redundant but geographically consistent and did not materially change the requested city-local search.
- **INVESTIGATE:** the actual `model` request used manufacturer-prefixed entries (`Toyota RAV4 Hybrid`, `Honda CR-V Hybrid`, etc.). The V2 model-field contract explicitly requires model names **without** manufacturer prefixes, including cross-brand lists. The host's later statement that the plugin “automatically removed manufacturer prefixes” does not change the primary request evidence: the Desktop request shown above contains the prefixes.
- **INVESTIGATE:** the host added `transmission: "Automatic"` although the user did not request a transmission. This is an invented hard search constraint. It may have little practical effect on this hybrid-SUV candidate set, but it is still stronger than the stated user intent.
- **PASS:** no unrequested `used`, year, mileage, drivetrain, trim, history, seating, colour, CPO, accident or ownership constraints were added.
- **RESULT RELEVANCE:** the displayed shortlist is consistent with the required hybrid-SUV request and flexible price band. The fact that the leading listings are new does not itself show an invented condition because `used` was omitted.

**ChatGPT V2 status: INVESTIGATE — request semantics and returned shortlist are broadly correct, but manufacturer-prefixed `model` values and invented `Automatic` transmission are request-quality issues.**

#### Claude V2

Actual Request supplied by André:

```json
{
  "bodyType": "SUV",
  "model": "RAV4 Hybrid,Highlander Hybrid,CR-V Hybrid,Venza,Sorento Hybrid,Sportage Hybrid,CX-50 Hybrid",
  "priceMax": 35000,
  "priceFlexibility": "flexible",
  "priorityAxis": "best_for_budget",
  "zip": "78701"
}
```

Observed response:

- Claude reported 57 area matches and rendered five closely matching vehicles.
- Returned examples were all hybrid SUVs/crossovers: 2025 Honda CR-V Hybrid Sport Hybrid ($27,500, used, Austin), 2025 Mazda CX-50 Hybrid Premium ($25,450, used, Sherman), two 2027 Kia Sportage Hybrid S vehicles ($31,776 and $32,165, new, Austin/Round Rock area), and a 2026 Mazda CX-50 Hybrid Hybrid Preferred ($34,876, new, Leander).
- All five were reported as VIN-verified; one CX-50 carried a disclosed one-accident history warning and Carfax verification direction.
- Widget rendered successfully and Claude summarized the result set rather than duplicating the widget payload.
- Claude explicitly flagged its assumption that it searched established hybrid SUV models and noted Venza as a crossover/SUV hybrid candidate.

Claude-side assessment:

- **PASS:** `bodyType: "SUV"` reflects the explicit body style.
- **PASS:** the `model` field contains real hybrid candidate models **without manufacturer prefixes**, matching the V2 contract better than the ChatGPT request.
- **PASS:** hybrid intent is preserved through an all-hybrid candidate model set and the returned vehicles are hybrid. Claude did not send the dedicated electrification fields, but no gas-only leakage is shown in this result set.
- **PASS / WATCH:** `priceMax: 35000` together with `priceFlexibility: "flexible"` expresses an approximate target differently from ChatGPT's explicit `$30k–$37k` band. The returned vehicles stayed at or below $35k. This does not yet demonstrate incorrect hard-ceiling behavior because the flexibility flag is present, but the V1 comparison should clarify whether material approximate-budget capability is preserved.
- **PASS:** `priorityAxis: "best_for_budget"` is appropriate.
- **PASS:** ZIP `78701` is a sensible Austin anchor.
- **PASS:** Claude did not invent transmission, condition, year, mileage, drivetrain, trim, history, seating, colour, CPO, accident or ownership constraints.
- **INVESTIGATE:** one displayed match is from a dealer in Sherman, TX, which is materially outside the Austin area. The request itself contains no explicit radius, so this may reflect backend default/widening behavior, dealer-location data, or result selection. The supplied evidence does not establish which. Treat this as a geography/result-quality item to compare with V1, not yet as a confirmed server defect.

**Claude V2 status: PASS on request construction, with one result-quality geography item to investigate.**

### V2 cross-host comparison

- Both hosts correctly resolved an Austin ZIP, SUV intent, hybrid candidate models, flexible-price semantics and `best_for_budget` ranking.
- Both returned useful hybrid inventory without evidence of gas-only contamination.
- ChatGPT used explicit electrification fields and an explicit flexible band; Claude encoded hybrid primarily through the candidate list and used `priceMax: 35000` plus `priceFlexibility: flexible`.
- Claude adhered to the model-field naming rule; ChatGPT did not.
- Claude avoided inventing transmission; ChatGPT added `Automatic` without user instruction.
- The request-quality problems are therefore **not required by the backend contract**; they are specific to the ChatGPT host request observed in this case.
- Claude's Sherman listing introduces a separate possible geography/result-quality issue that cannot be attributed from the supplied evidence alone.

### V2 backend assessment

**PROVISIONAL PASS / INVESTIGATE geography.** Both hosts received relevant hybrid-SUV inventory and no backend failure is demonstrated. The strongest unresolved backend/result question is why Claude surfaced a Sherman dealer for an Austin request.

### V2 UI/widget assessment

**PASS based on supplied evidence.** Claude rendered the interactive CarClever widget and its textual summary aligned with the tool response. ChatGPT's response evidence also showed useful matching inventory. No widget defect is demonstrated in Test #2.

### Test #2 V2 verdict

**INVESTIGATE — V2 functionality is materially working, but the case should not close yet.**

Reasons:

1. ChatGPT request construction violated the model naming rule by including manufacturer prefixes.
2. ChatGPT invented an `Automatic` transmission constraint.
3. Claude returned one materially non-Austin dealer result (Sherman), requiring same-prompt V1 comparison before deciding whether this is a V2 geography/result-quality regression or ordinary widening/data behavior.

**No code or description change is recommended yet.** The next step is the same Test #2 prompt through V1, following the locked sequence. Do not move to Test #3 until this comparison is recorded and Test #2 receives a final verdict.

## Remaining coverage

Select later cases one at a time. Remaining coverage includes direct make/model and trim; body style vs finer vehicle type; city/state/ZIP/radius; strict vs approximate price; ranking axes; drivetrain/transmission/cylinders/colors/doors; trim required vs preferred; hybrid/PHEV/EV required vs preferred; used/new/CPO/history/one-owner; exact VIN/not-found VIN; thin/zero results and widening; UI/link behavior; practical-needs expansion; and negative non-inventory requests where the connector should not be called.
