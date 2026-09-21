# Comparison — Fractal First-Pass Report vs. Auto.dev Listings Field Audit

**Date:** 2026-09-22  
**Purpose:** compare the Fractal code agent's first-pass API/field claims against the authoritative Auto.dev Listings field audit.  
**Scope limit:** `specs/Auto_Dev_Field_Audit_v1.md` documents the Auto.dev **`/listings`** response and how **Find My Car** uses it. It does not prove what old CarClever on Fractal currently reads, and it does not document Auto.dev's Photos, Specs, Recalls, APR, Payments or TCO response schemas.

## Bottom line

The Fractal report is broadly aligned with the field audit for the basic Listings data: identity, powertrain, price/miles, dealer/location and accident/owner history.

Its listing MPG and horsepower fallback claims do **not** match the field audit. The audit's documented Listings response surface contains no MPG or horsepower fields; earlier field-audit research explicitly records MPG as absent from Listings data/API. The Fractal report must provide code and raw response evidence before those claims can be relied on.

## Endpoint comparison

| Fractal report endpoint/API | Can the Listings field audit validate it? | Comparison |
|---|---|---|
| Auto.dev `GET /listings` | Yes | Directly comparable; see field matrix below. |
| Auto.dev `GET /photos/{vin}` | No | The audit records a Listings `retailListing.primaryImage` field and notes optional extra photo calls in Find My Car, but does not document the Photos endpoint or old Fractal use. |
| Auto.dev `GET /specs/{vin}` | No | The field audit does not cover Specs. Historical submission schemas describe MPG, range, horsepower, warranty and measurements as coming from “Specs,” but that is not a live old-Fractal field trace. |
| Auto.dev `GET /recalls/{vin}`, `/apr/{vin}`, `/payments/{vin}`, `/tco/{vin}` | No | None is documented by the Listings field audit. The Fractal agent must supply actual code paths and response-field mappings. |
| NHTSA vPIC / recalls; Zippopotam | No | Outside the Auto.dev Listings audit. The report needs exact endpoints and current code use. |
| NHTSA Safety Ratings, FRED, DOE/AFDC | No; not current inventory evidence | These are proposed additions only, not evidence of APIs currently used. |

## Listings-field comparison

| Fractal claim about Listings | Field-audit result | Assessment |
|---|---|---|
| Year, make, model, trim | `vehicle.year`, `vehicle.make`, `vehicle.model`, `vehicle.trim` documented and used in Find My Car. | Aligned. Model and trim need runtime type normalization; trim is not a hard filter. |
| Engine, transmission, drivetrain, fuel, body style, colour | `vehicle.engine`, `vehicle.transmission`, `vehicle.drivetrain`, `vehicle.fuel`, `vehicle.bodyStyle`, `vehicle.exteriorColor` and `vehicle.interiorColor` are documented. | Aligned, with caveats: fuel is display-only and unreliable for hybrid/PHEV identification; body/type tags can be inconsistent. |
| Cylinders and seating | `vehicle.cylinders` and `vehicle.seats` are documented/used in the audit. | Aligned. Seats are response/disclosure data, not a dependable hard filter. |
| Price and mileage | `retailListing.price` and `retailListing.miles`. | Aligned. The exact mileage field is **miles**, not `mileage`. |
| Dealer and location | `retailListing.dealer`, `dealerId`, `city`, `state`, `zip`, `vdp`. | Broadly aligned, but the Fractal report omits the exact source paths and important coverage limits (for example, ZIP can be sparse). |
| Accident and owner history | `history.accidents`, `history.accidentCount`, `history.ownerCount`, `history.oneOwner`, `history.usageType`. | Aligned for accidents/owners. `usageType` is parsed but not surfaced in Find My Car. |
| Title status | Audit only records `retailListing.titleStatus` as parsed/displayed but not independently confirmed as a real provider field. | Not yet strong enough to call unaffected/available without old-code evidence. |
| Primary image / photos | `retailListing.primaryImage` is a Listings field; `photoCount` is known unreliable for gallery prediction. | Only partially aligned. It does not prove the separate `/photos/{vin}` route or its field use. |
| MPG city/highway/combined fallback from `listing.vehicle.mpgCity` / `mpgHighway` | No matching Listings field in the field audit or its raw-reference response list; prior audit research says MPG is absent from Listings data/API. | **Mismatch / unproven.** Must not be assumed available. |
| Horsepower fallback from Listings | No `vehicle.horsepower` field documented in the field audit/raw reference. | **Mismatch / unproven.** vPIC `EngineHP` is a separate API claim, not a Listings fallback. |
| EV range, torque, tank capacity, dimensions, safety equipment, warranty | No Listings equivalents documented in the field audit. | Consistent with the report’s claim that these are Specs-derived or absent on Listings, but not a proof of old Fractal code behaviour. |

## Important naming correction

The field audit uses provider paths such as `vehicle.engine`, `retailListing.price` and `history.ownerCount`. The Fractal report uses generic phrases such as “listing field” and writes `listing.vehicle.mpgCity`.

That shorthand is not adequate for an inventory. The next return must give the exact raw response path and code property read, otherwise a type-only field, an invented property or a different endpoint can be mistaken for live data.

## What the current report still omits

Even inside Listings, it does not say whether old CarClever uses fields that the field audit shows are available, including:

- `retailListing.vdp`, `carfaxUrl`, `dealerId`, `primaryImage`, `photoCount`, `used`, `cpo`;
- `vehicle.doors`, `series`, `squishVin`, `confidence`, `type`;
- `history.accidentCount`, `oneOwner`, `usageType`; and
- which fields are only read for a calculation versus returned/displayed.

## Required evidence next time

The proper inventory needs a code-backed row for every API response field old CarClever actually uses:

`provider + endpoint → raw response field path → code property/read site → local calculation/fallback → tool output or UI label`.

Until that exists, the Fractal report can support questions, but cannot settle what data old CarClever actually has.
