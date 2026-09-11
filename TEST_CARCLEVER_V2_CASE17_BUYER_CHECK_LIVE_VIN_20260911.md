# CarClever V2 Case 17 — Buyer Check / Live VIN — 2026-09-11

**Status:** CLOSED — CROSS-HOST / CROSS-VERSION PASS WITH CLAUDE HOST-INFERENCE WATCH

## Prompt

`Check VIN 4T1DAACK6SU582551 for red flags before I buy it.`

## Fixture selection

The prior submission VIN `4T1BF3EK7BU748352` no longer had a current live listing in V2, so it is no longer suitable as the positive reviewer-facing Buyer Check fixture. The live VIN used for this case, `4T1DAACK6SU582551`, had just appeared in the interior-color regression case and carried a reported accident, making it a stronger current Buyer Check fixture.

## ChatGPT V2

Observed request:

```json
{
  "vin": "4T1DAACK6SU582551"
}
```

Result: exact 2025 Toyota Camry SE Hybrid FWD, $29,995, 25,803 miles, Sunland CA. Buyer Check verdict was **Caution**. The response surfaced one reported accident, unreported title status, not reported as Toyota CPO, relatively high mileage for model year, and unverified recall completion. It also surfaced positive signals such as VIN identity consistency and one-owner/personal-use history, then recommended Carfax review, repair documentation, title verification, and independent inspection before purchase.

Assessment:
- Ideal exact-VIN request shape with no invented make/model/price/history restrictions.
- Correctly used the live exact-VIN path for Buyer Check/red-flag assessment.
- Strong uncertainty handling: unknown title/recall/CPO evidence was not converted into false claims.
- Clear caution outcome tied to the reported accident.

## Claude V2 Cleanroom

Observed request:

```json
{
  "vin": "4T1DAACK6SU582551",
  "noAccidents": true,
  "oneOwner": true,
  "cpo": true
}
```

Result: exact same live vehicle was returned and the Buyer Check correctly produced **Caution**, explicitly surfacing the reported accident and recommending Carfax review, dealer documentation, independent inspection, and trim/spec verification.

Assessment:
- Exact VIN resolution: PASS.
- Buyer Check outcome and accident disclosure: PASS.
- Claude inferred `noAccidents:true`, `oneOwner:true`, and `cpo:true` from the buyer's request to check for red flags. Those fields were not literally requested and are not the cleanest semantic representation of a pure exact-VIN inspection.
- In this observed case, the extra fields did **not** suppress, alter, or sanitize the result: the exact VIN was still returned and the reported accident was still exposed correctly.
- Per André's assessment, this is therefore recorded as a non-blocking **host-inference watch**, not a release defect.

## ChatGPT V1 baseline

Observed request:

```json
{
  "vin": "4T1DAACK6SU582551"
}
```

Result: exact 2025 Toyota Camry SE Hybrid, $29,995, 25,803 miles, Sunland CA. Buyer Check verdict was **Caution** with the same core issue: one reported accident. V1 also surfaced VIN identity consistency, one-owner/personal-use signals, uncertainty about accident severity/repair quality, and recommended Carfax review, repair documentation, independent inspection, and trim confirmation.

Assessment:
- Cleanest possible exact-VIN request mapping.
- Same core caution outcome as ChatGPT V2 and Claude V2 Cleanroom.
- Confirms the live VIN fixture is suitable for current Buyer Check regression and likely stronger than the stale prior-submission VIN.

## Related stale-VIN observation

When the old submission VIN `4T1BF3EK7BU748352` was tested on ChatGPT V2, the exact VIN request returned no current live listing and rendered a blank/no-match card. The host correctly explained that inventory-backed title/accident/owner/mileage evidence could not be substantiated from a live listing. That behavior is best treated as:
- stale positive fixture: retire for final reviewer-facing tests;
- empty-state widget UX: minor watch;
- not evidence of a VIN-routing or Buyer Check backend defect.

## Final conclusion

CLOSED — PASS across ChatGPT V2, Claude V2 Cleanroom, and ChatGPT V1 on the live exact-VIN Buyer Check outcome.

Recommended current reviewer-facing VIN fixture: `4T1DAACK6SU582551`, while it remains live and continues to return the accident-linked **Caution** outcome.

Preferred exact-VIN request shape remains the VIN alone unless the buyer explicitly adds other constraints. Claude's extra history/CPO fields are recorded as a host-inference watch because they were semantically broader than necessary, but they did not change the observed result in this case.
