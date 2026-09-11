# CarClever V2 Case 13 — Trim-Required Ford F-150 Raptor — 2026-09-11

**Status:** CLOSED — CROSS-HOST / CROSS-VERSION PASS WITH MATCH-COUNT VARIANCE WATCH

## Prompt

`Find me a Ford F-150 Raptor under $70k in 75001.`

## ChatGPT V2

Observed request:

```json
{
  "make": "Ford",
  "model": "F-150",
  "trimRequired": "Raptor",
  "priceMax": 70000,
  "priceFlexibility": "strict",
  "zip": "75001"
}
```

Result: valid F-150 Raptor inventory under $70,000 near 75001. The top clean-history lead was a 2023 F-150 Raptor at $58,675; a lower-mileage 2023 Raptor at $65,395 had one reported accident.

Assessment:
- Correctly parsed `Raptor` as `trimRequired`, not as part of the model string and not as a soft preference.
- No invented mileage, year, radius, condition, or ranking optimization.
- Presentation appropriately distinguished clean-history/value from lower-mileage inventory with a reported accident.

## Claude V2 Cleanroom

Observed request:

```json
{
  "make": "Ford",
  "model": "F-150",
  "trimRequired": "Raptor",
  "priceMax": 70000,
  "zip": "75001",
  "bodyType": "Truck",
  "priorityAxis": "best_for_budget"
}
```

Result: five returned F-150 Raptors, with the same core vehicles and same $58,675 2023 Raptor at the top. Claude reported 3,149 matches in the area.

Assessment:
- Correct `trimRequired:"Raptor"` mapping.
- `bodyType:"Truck"` is a reasonable implication from F-150 and does not conflict with the request.
- `priorityAxis:"best_for_budget"` is a defensible default for a price-ceiling search with no other optimization.
- Every shown vehicle was confirmed as Raptor.

## ChatGPT V1 baseline

Observed request:

```json
{
  "zip": "75001",
  "make": "Ford",
  "model": "F-150",
  "trimRequired": "Raptor",
  "priceMax": 70000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget"
}
```

Result: 3.4 million listings searched → 3,178 matched near 75001. V1 explicitly stated that the Raptor trim was enforced as a hard requirement and returned the same core five Raptor candidates, headed by the 2023 Sherman truck at $58,675.

Assessment:
- Strong cross-version agreement on the trim semantics and top candidate set.
- V1 reported 3,178 matches versus Claude V2's 3,149. Treat this as a match-count variance watch, not a failure, because ranking and returned inventory remained materially aligned.

## Final conclusion

CLOSED — PASS across ChatGPT V2, Claude V2 Cleanroom, and ChatGPT V1.

This case validates the required-versus-preferred trim contract: when a buyer explicitly names a trim such as `Raptor`, the host should send the base model separately and map the variant to `trimRequired` as a hard eligibility requirement.

Watch only the small pool-size variance across hosts/versions; there is no evidence here of incorrect trim filtering or result substitution.
