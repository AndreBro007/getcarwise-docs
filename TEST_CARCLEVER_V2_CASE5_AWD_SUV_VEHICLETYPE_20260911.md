# CarClever V2 Test #5 — AWD SUV + `vehicleType` Regression — 2026-09-11

**Status:** CLOSED — MATERIAL CHATGPT V2 REGRESSION IDENTIFIED  
**Prompt:** `Find me an AWD SUV under $45k in Denver.`

## Purpose

Validate drivetrain, broad SUV intent, city-only location, strict budget, and parity with Claude V2 plus ChatGPT V1.

## ChatGPT V2

Actual request:

```json
{
  "bodyType": "SUV",
  "vehicleType": "SUV",
  "drivetrain": "AWD",
  "priceMax": 45000,
  "priceFlexibility": "strict",
  "zip": "80202",
  "radiusMiles": 50,
  "priorityAxis": "best_for_budget",
  "vehicleNeeds": [
    "AWD SUV in the Denver area under $45,000"
  ]
}
```

Observed behavior: ChatGPT V2 reported only 17 local matches and surfaced a weak shortlist dominated by two 2019 Toyota 4Runners and a 2014 GMC Yukon XL with 171k miles. First card had no photo. A same-prompt rerun produced materially the same result set.

## Claude V2

Actual request:

```json
{
  "bodyType": "SUV",
  "drivetrain": "AWD",
  "priceMax": 45000,
  "priorityAxis": "best_for_budget",
  "zip": "80202"
}
```

Claude reported 13,617 area matches and returned a much stronger shortlist including low-mileage/newer AWD Mercedes-Benz GLA/GLB, Audi Q5, Hyundai Santa Fe, MINI Countryman and Subaru Outback examples around the $44k ceiling.

## ChatGPT V1 baseline

Actual request:

```json
{
  "bodyType": "SUV",
  "drivetrain": "AWD",
  "priceMax": 45000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget",
  "zip": "80202",
  "radiusMiles": 50,
  "goals": [
    "AWD SUV under $45k",
    "good value near Denver"
  ]
}
```

V1 also reported 13,617 local matches and returned essentially the same strong result pattern as Claude V2.

## Field-audit cross-check

The living `carclever-widget/specs/Auto_Dev_Field_Audit_v1.md` confirms that `vehicle.type` — the downstream field represented by `vehicleType` — is mechanically filterable but **not in Auto.dev's official documented Vehicle Filters list** and is known to have inconsistent per-model tagging. The audit records live cases where `vehicle.type=Sedan` or `vehicle.type=Wagon` silently excluded genuine matching inventory, including Volvo V90 records tagged as `Crossover` despite real body style. The document explicitly distinguishes this from `vehicle.bodyStyle`, which is the broader body-style field behind `bodyType` and has been live-confirmed as suitable for broad cross-brand body searches.

This means `vehicleType` is not safe as a redundant hard filter for ordinary broad SUV intent.

## Comparison and diagnosis

- ChatGPT V2 is the only tested request that adds `vehicleType: "SUV"`.
- Claude V2 omits `vehicleType` and returns 13,617 area matches.
- ChatGPT V1 omits `vehicleType` and returns the same 13,617-match universe.
- ChatGPT V2 returns only 17 matches, and the same-prompt rerun reproduces the poor result pattern.
- Other differences (`priceFlexibility`, `radiusMiles`, `vehicleNeeds`) exist, but V1 also carries strict flexibility, 50-mile radius and goal context while still returning 13,617 matches. That materially narrows the causal difference to the extra `vehicleType` filter.
- The living field audit independently documents exactly the failure mode expected from `vehicleType`: silent recall loss caused by inconsistent provider classification.

## Verdict

**FAIL / MATERIAL REGRESSION ON CHATGPT V2 REQUEST CONSTRUCTION.**

The evidence strongly supports `vehicleType: "SUV"` as the regression trigger. This is stronger than a host-variance watch item because:

1. the same ChatGPT V2 behavior reproduced on rerun;
2. Claude V2 and ChatGPT V1 independently converge on the same 13,617-match universe and similar strong results while omitting `vehicleType`; and
3. the pre-existing field audit documents `vehicle.type` as an unreliable, undocumented classification field capable of silently excluding valid inventory.

A fully isolated server A/B with identical payloads differing only by `vehicleType` would be the final mechanical proof, but it is not necessary to classify this manual acceptance case as a real regression.

## Required action / boundary

This is implementation work in `carclever-find-my-car`, therefore **Claude's engineering lane**. ChatGPT should not modify application code. The engineering handoff should preserve the existing field-audit rule: broad SUV/body-style intent should not be redundantly constrained through unreliable `vehicleType`; `bodyType`/`vehicle.bodyStyle` is the appropriate broad body-style path. Any change should be regression-tested against this exact Denver case before promotion.

## Secondary observations

- Missing photo on the first ChatGPT V2 listing is a separate data/UI quality watch item, not the primary failure.
- ChatGPT V2's repeated poor shortlist was not explained by random retrieval variance because the rerun reproduced it.
