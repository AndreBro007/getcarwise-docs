# CarClever V2 Case 15 — Interior-Color Toyota Camry — 2026-09-11

**Status:** CLOSED — CROSS-HOST / CROSS-VERSION PASS WITH MINOR PRESENTATION WATCH

## Prompt

`Find me a Toyota Camry with a black interior under $35k in 90210.`

## ChatGPT V2

Observed request:

```json
{
  "make": "Toyota",
  "model": "Camry",
  "interiorColor": "black",
  "priceMax": 35000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget",
  "zip": "90210"
}
```

Result: five local matches with verified black interiors, all under $35,000. Top options included 2026 Camry Nightshade, 2026 Camry SE, 2025 Camry SE, and 2026 Camry XLE AWD.

Assessment:
- Correctly mapped black interior to the dedicated `interiorColor` field.
- The field operated as a real structured filter rather than a broad search followed by manual post-filtering.
- No invented condition, mileage, model year, radius, exterior color, or drivetrain restrictions.
- Lowercase `"black"` was accepted and worked correctly.
- Host also surfaced a trim/dealer-page inconsistency on one result rather than silently ignoring it.

## Claude V2 Cleanroom

Observed request:

```json
{
  "make": "Toyota",
  "model": "Camry",
  "priceMax": 35000,
  "interiorColor": "black",
  "priorityAxis": "best_for_budget",
  "zip": "90210"
}
```

Result: 961 matches in the area and the same five core vehicles, all explicitly confirmed with black interiors.

Assessment:
- Correct `interiorColor:"black"` mapping.
- Confirms cross-host use of the dedicated structured field.
- Same core inventory, prices, mileages, and accident note as ChatGPT V2.
- Differences were presentation/ranking emphasis only.

## ChatGPT V1 baseline

Observed request:

```json
{
  "zip": "90210",
  "make": "Toyota",
  "model": "Camry",
  "interiorColor": "Black",
  "priceMax": 35000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget"
}
```

Result: 3.4 million listings searched → 961 matched near 90210. V1 explicitly stated that black interior was enforced as a hard filter.

Assessment:
- Clean baseline consistent with V2.
- Confirms case-insensitive color handling (`Black` vs `black`).
- Match pool aligns with Claude V2 at 961.
- Minor presentation watch: V1 noted that all shortlisted cars were hybrids even though hybrid powertrain was not part of the user's request. This did not change filtering or eligibility.

## Final conclusion

CLOSED — PASS across ChatGPT V2, Claude V2 Cleanroom, and ChatGPT V1.

This case validates the dedicated interior-color path: a stated interior color should be passed through `interiorColor` and enforced by the search rather than approximated with post-search inspection.

Watch only incidental host prose that introduces unrelated characteristics; no backend or mapping defect was observed.
