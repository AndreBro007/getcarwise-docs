# Review — Fractal API, Field and Logic Ledger

**Date:** 2026-09-22  
**Input reviewed:** Fractal code agent's tables A–F supplied by André.  
**Scope:** current old CarClever code evidence, compared with the authoritative Auto.dev Listings Field Audit in `carclever-widget/specs/Auto_Dev_Field_Audit_v1.md`. No source, account, deployment or plan change is authorised.

## Verdict

This is the first Fractal return that substantially answers the inventory question.

It identifies the user-facing tools, 19 call-path rows (including four startup probes and one dead legacy route), every current external provider/endpoint, request parameters, response paths, local logic and output destinations. It also identifies fields stored but not subsequently used.

The one incomplete part is table E: the Fractal environment could not retrieve the Listings Field Audit and therefore marked every audit comparison “cannot verify.” This review completes the material comparison below.

## Current external API inventory established by the ledger

| Provider | Current callable endpoints |
|---|---|
| Auto.dev | `/listings`, `/photos/{vin}`, `/specs/{vin}`, `/recalls/{vin}`, `/apr/{vin}`, `/payments/{vin}`, `/tco/{vin}` |
| NHTSA vPIC | `/api/vehicles/decodevinvalues/{vin}?format=json` |
| NHTSA Recalls | `/recalls/recallsByVehicle?make=&model=&modelYear=` |
| Zippopotam.us | `/us/{zip}` for validation; `/us/{state}/{city}` for live city lookup |

The local dealer/affiliate resolver constructs URLs but makes no outbound HTTP call. Garage functions use local SQLite. A second Zippopotam ZIP helper is dead inside a commented deprecated block.

## What the code now proves

### Listings fields genuinely read in old CarClever

The code reads and traces to output or logic:

- identity: `vehicle.vin/year/make/model/trim`, plus top-level fallbacks;
- commercial/listing: `retailListing.used/cpo/price/miles/primaryImage/dealer/trim/vdp/city/state/status/carfaxUrl/daysOnMarket/stockNumber/description`;
- powertrain/display: `vehicle.fuel/mpgCity/mpgHighway/drivetrain/bodyStyle/engine/transmission/cylinders/doors/seats/exteriorColor/color/interiorColor/horsepower/titleStatus/photos`;
- dealer/location fallbacks: `dealer.name/phone/website/address.*`, `seller.name`, `location.*`;
- history: `history.accidents` and `history.ownerCount`.

It also documents the exact local logic: used-stock exclusion, hybrid override, fuel/EV handling, deal-risk changes (accident true −10, false +5; 3+ owners −5; one owner +5), warranty parsing, payment and TCO formulas, photo fallback order and dealer-name sanitation.

### Important correction to the earlier review

The old Fractal code **does read** `vehicle.mpgCity`, `vehicle.mpgHighway` and `vehicle.horsepower` from Listings. My earlier position was narrower: these fields were not documented in the Find My Car Listings audit. The new Fractal ledger resolves the code-use question.

What remains unresolved is provider population: code reading a property does not establish that Auto.dev currently returns it. A single controlled Listings response would settle that later if needed.

## Comparison with the Listings Field Audit

| Fractal old-CarClever code/API use | Listings field-audit position | Assessment |
|---|---|---|
| `vehicle.year/make/model/trim` | Documented Listings fields. | Match. The audit records type-normalisation risks for model/trim. |
| `vehicle.engine/drivetrain/transmission/fuel/bodyStyle/exteriorColor/interiorColor/cylinders/seats/doors` | Documented/audited Listings fields. | Match, subject to the audit’s field-specific reliability rules—especially fuel not being reliable for hybrid/PHEV eligibility, and seats being disclosure data. |
| `retailListing.price/miles/used/cpo/dealer/city/state/vdp/carfaxUrl/primaryImage` | Documented/audited Listings fields. | Match. The exact mileage source is `retailListing.miles`. |
| `history.accidents/accidentCount/ownerCount/oneOwner` | Audited Listings history fields. | Match for the fields read; old CarClever visibly uses accidents and ownerCount. |
| `vehicle.mpgCity`, `vehicle.mpgHighway`, `vehicle.horsepower` | Not present in the Listings audit or raw-reference response surface; prior field-audit research records MPG as absent from Listings data/API. | **Code use is proved; provider availability is not.** Do not call these dependable Listing fallbacks without one live response check. |
| `vehicle.titleStatus` | The audit only notes an unconfirmed `retailListing.titleStatus`, not `vehicle.titleStatus`. | **Path mismatch / unverified.** |
| `retailListing.trim` | Audit documents `vehicle.trim`; old code accesses retailListing trim through an `as any` cast. | **Not documented / unverified.** It may simply fall through to `vehicle.trim`. |
| `vehicle.photos`, top-level `photos`, `retailListing.status/daysOnMarket/stockNumber/description` | Not part of the audit’s documented core field surface. | Current code use is proved, but audit does not corroborate provider availability. |
| `/photos/{vin}` response `data.retail[]` | Outside Listings audit scope. | Code use is proved; separate endpoint schema not compared. |
| Specs, Recalls, APR, Payments, TCO, vPIC, NHTSA Recalls, Zippopotam response paths | Outside Listings audit scope. | Current code use is proved by the ledger; the Listings audit cannot validate these schemas. |

## Two current request-field mismatches worth retaining

These are facts from old CarClever code compared with the Listings audit. They are not a change request.

| Old CarClever request parameter | Field-audit documented parameter/field | Why it matters |
|---|---|---|
| `vehicle.mileage=-{max}` | `retailListing.miles` | The audit records `retailListing.miles` as the verified mileage field and notes a prior Find My Car bug caused by using the wrong name `retailListing.mileage`. Old CarClever's `vehicle.mileage` needs a later isolated provider-behaviour check before it can be trusted as a mileage filter. |
| `vehicle.color={color}` | `vehicle.exteriorColor` | The audit documents `vehicle.exteriorColor` for colour. Old CarClever's different query name needs a later isolated provider-behaviour check before it can be trusted. |

## Other material logic clarifications

- The Auto.dev Payments response's `loanMonthlyPayment` is read only to set `using_real_data`; old CarClever calculates its displayed monthly payment locally. The Payments endpoint does directly supply taxes/fees and loan amount.
- Combined MPG comes from Specs only; old CarClever does not read a combined-MPG Listings field.
- vPIC's `BodyClass`, `DisplacementL`, `FuelTypeSecondary` and `ElectrificationLevel` are stored in intermediate values but are not subsequently used in an output or calculation.
- The code agent did not find NHTSA Safety Ratings, FRED or DOE/AFDC calls. Those are not current dependencies.

## Next evidence boundary

The API/field/logic inventory is now sufficient for architecture and data-source comparison. The only unresolved field questions requiring a later targeted read-only provider check are the code-used but undocumented Listings properties (`mpgCity`, `mpgHighway`, `horsepower`, `vehicle.titleStatus`, `retailListing.trim`) and the two mismatched Listing filter names above.

## Explicit non-decisions

- No endpoint, field, prompt, code, subscription, host or Auto.dev plan has been changed.
- No conclusion is made about provider population where static code alone cannot prove it.
