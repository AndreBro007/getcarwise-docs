# CarClever V2 Test #5 — AWD SUV + `vehicleType` Regression — 2026-09-11

**Status:** CLOSED — REGRESSION FIXED AND HOST RETEST PASSED  
**Prompt:** `Find me an AWD SUV under $45k in Denver.`

## Purpose

Validate drivetrain, broad SUV intent, city-only location, strict budget, and parity with Claude V2 plus ChatGPT V1.

## Original ChatGPT V2 failure

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

Observed behavior: ChatGPT V2 reported only 17 local matches and surfaced a weak shortlist dominated by two 2019 Toyota 4Runners and a 2014 GMC Yukon XL with 171k miles. A same-prompt rerun produced materially the same result set.

## Claude V2 baseline

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

## Fix implemented

Claude Engineering pushed two focused fixes to `release/v2`:

1. Commit `15d24bebe5a63893426794bb9f7dddd6e09d8fbb`
   - deterministic provider safety gate: if `vehicleType` equals `bodyType` case-insensitively, `vehicle.type` is not sent to Auto.dev;
   - `vehicleType` schema wording no longer lists SUV as a finer-classification example;
   - transmission field wording was tightened to prevent invented transmission restrictions.

2. Commit `a5d96960792d1de3cd4eaf81ccef0a1515acf04f`
   - added the global semantic instruction: `Direct filter fields should reflect requirements the user stated or clearly implied; leave unstated restrictions unset.`

Both pushes auto-deployed successfully to the V2 Vercel project.

## Post-fix ChatGPT V2 retest

Exact same prompt rerun after deployment:

```json
{
  "bodyType": "SUV",
  "drivetrain": "AWD",
  "priceMax": 45000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget",
  "radiusMiles": 50,
  "state": "CO",
  "vehicleType": "SUV",
  "zip": "80202"
}
```

Observed behavior:

- No invented `used:true` restriction after the global anti-invention wording change.
- ChatGPT still supplied redundant `vehicleType:"SUV"`, but the deterministic provider gate neutralized it before Auto.dev filtering.
- Result set returned 8 strong AWD matches under $45,000 within 50 miles of Denver, including both new and used inventory.
- Strong shortlist included 2026 MINI Countryman S ALL4, 2026 Mercedes-Benz GLB 250 4MATIC, 2025 Audi Q5 Premium, 2026 Subaru Outback Limited XT, 2026 Volkswagen ID.4 AWD Pro, 2026 Nissan Murano SL, 2027 Hyundai Santa Fe SEL, and 2027 MINI Countryman S ALL4 Iconic.
- The result pattern is again consistent with the strong Claude V2 / ChatGPT V1 baseline rather than the original 17-result failure.
- Budget and radius remained strict; no relaxation was reported.

`state:"CO"` was also supplied even though ZIP `80202` already anchors the location. It is semantically consistent and did not create a conflicting restriction in this case, so it is recorded as a non-blocking redundancy rather than a regression.

## Final verdict

**PASS — ORIGINAL MATERIAL REGRESSION FIXED.**

The post-fix evidence confirms both layers are working as intended:

1. the host-facing anti-invention wording stopped the previously observed unstated `used:true` restriction; and
2. the server-side safety gate makes redundant `vehicleType:"SUV"` harmless even when ChatGPT still emits it.

The public `vehicleType` field remains a future data-trust watch item for genuinely finer classifications such as Crossover/Wagon/Hatchback/Coupe because provider `vehicle.type` itself remains undocumented and inconsistently tagged. That broader question is not a release blocker absent a new failing regression case.

## Secondary observations

- Repeated-call / ZIP-recovery behavior remains a host UX watch item and was deliberately not changed in these fixes.
- Auto.dev pricing anomalies remain a provider-data quality issue; existing ranking/output behavior correctly avoids treating implausible flagged prices as credible cheapest results.
