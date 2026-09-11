# CarClever V2 Case 18 — Listing Presence / Availability Flow — 2026-09-11

**Status:** CLOSED — CROSS-HOST / CROSS-VERSION PASS WITH WORDING + HOST-ROUTING WATCHES

## Prompt

`Check availability for VIN 4T1DAACK6SU582551.`

## Capability contract

CarClever can verify that an exact VIN is still present in current inventory/listing data and can resolve the dealer/listing URL. This is not the same as proving real-time dealer availability, because feeds can lag and a vehicle may already be sold or under deposit. Preferred wording is therefore **currently listed / present in current inventory**, followed by a direct-dealer confirmation caveat.

## ChatGPT V2

Observed flow:

Availability-link resolution request:

```json
{
  "vin": "4T1DAACK6SU582551",
  "make": "Toyota",
  "model": "Camry",
  "year": 2025
}
```

Live inventory confirmation request:

```json
{
  "vin": "4T1DAACK6SU582551"
}
```

Result: the exact 2025 Toyota Camry SE listing remained present in current inventory. The host surfaced a **Check availability** action and warned that feeds can lag. André clicked through and confirmed that the dealer/listing destination still showed the vehicle as available at that moment.

Assessment:
- PASS on exact listing/dealer-link resolution.
- PASS on current-inventory/listing confirmation.
- PASS on end-to-end clickthrough for this observed vehicle.
- Wording refinement: prefer "currently listed" or "present in current inventory" over treating CarClever itself as a real-time dealer availability oracle.

## Claude V2 Cleanroom

A same-chat run used the prior VIN context to resolve the exact listing directly with:

```json
{
  "vin": "4T1DAACK6SU582551",
  "make": "Toyota",
  "year": 2025,
  "model": "Camry"
}
```

It returned the exact VIN-specific Edmunds listing URL.

A fresh-chat rerun removed the prior-context effect and used:

```json
{
  "vin": "4T1DAACK6SU582551"
}
```

The exact live listing was found again and the host surfaced the accident-linked Buyer Check context and listing URL.

Assessment:
- PASS on fresh-chat VIN lookup.
- PASS on exact listing URL / current listing presence.
- Minor wording watch when Claude says "currently available"; the safer contract is current-listing presence plus dealer confirmation.
- Separate data watch: Claude labeled the vehicle LE in the fresh run while ChatGPT V2/V1 labeled the same VIN/listing SE. Claude correctly warned that trim should be independently verified, so this remains a provider/listing trim-consistency issue rather than an availability-flow failure.

## ChatGPT V1 baseline

Valid V1 request:

```json
{
  "vin": "4T1DAACK6SU582551"
}
```

Tool/operation:

`carclever_find_my_car_find_matching_vehicle`

Result: V1 stated that the VIN **is currently listed for sale**, returned the exact 2025 Toyota Camry SE Hybrid listing, surfaced dealer/location/price/mileage and accident history, provided a **Check current availability** action, and recommended dealer confirmation before traveling.

Assessment:
- Clean exact-VIN request with no extra location, price, model, or condition filters.
- PASS on listing-presence confirmation and availability/dealer-action flow.
- Wording appropriately includes dealer-confirmation caveat.

## Host-routing incident

One attempted V1 run unexpectedly invoked `carclever_v3_test_check_vehicle` even though the intended V1 connector had been selected. A subsequent rerun correctly used `carclever_find_my_car_find_matching_vehicle`.

This is recorded as a **host connector/tool-routing watch**, not a CarClever V1 application defect. The invalid run should not be used as V1 regression evidence.

## Final conclusion

CLOSED — PASS across ChatGPT V2, Claude V2 Cleanroom, and ChatGPT V1 on the core capability: exact VIN current-listing presence plus dealer/listing resolution.

The final product/reviewer wording should distinguish **currently listed / present in current inventory** from guaranteed real-time dealer availability. In the observed ChatGPT V2 run, André's clickthrough independently confirmed that the vehicle still showed as available at the dealer/listing destination at that moment.
