# CarClever V2 Case 9 — Newest Mazda CX-5 — 2026-09-11

**Status:** CLOSED — CROSS-HOST PASS

## Prompt

`Find me the newest Mazda CX-5 under $35k in 98101.`

## ChatGPT V2

Observed request:

```json
{
  "make": "Mazda",
  "model": "CX-5",
  "priceMax": 35000,
  "priceFlexibility": "strict",
  "priorityAxis": "newest",
  "zip": "98101"
}
```

Result: five 2026 Mazda CX-5 matches under $35k, including both used and new inventory. ChatGPT explicitly noted that both new and used vehicles were included because condition was not specified.

Assessment:
- Correct make/model parsing.
- Correct strict price ceiling.
- Correct `priorityAxis:"newest"`.
- No invented `used`, year, trim, drivetrain, transmission, mileage ceiling, radius, bodyType, or vehicleType restriction.
- Mixed new/used search behavior is correct because condition was unspecified.

## Claude V2 Cleanroom

Observed request:

```json
{
  "make": "Mazda",
  "model": "CX-5",
  "zip": "98101",
  "priceMax": 35000,
  "priorityAxis": "newest"
}
```

Result: the same five vehicles, in the same order, as ChatGPT V2:
1. 2026 Mazda CX-5 2.5 S Select — used, 390 mi, $30,733
2. 2026 Mazda CX-5 2.5 S Preferred — used, 3,029 mi, $30,955
3. 2026 Mazda CX-5 2.5 S Select — new, 1 mi, $32,645
4. 2026 Mazda CX-5 2.5 S Select — new, 1 mi, $32,880
5. 2026 Mazda CX-5 2.5 S Select — new, 1 mi, $32,980

Assessment:
- Same essential request semantics as ChatGPT V2.
- No invented condition or other restrictions.
- Identical result ordering strongly indicates backend ranking consistency rather than host-specific behavior.

## Conclusion

PASS. The `newest` path behaves consistently across ChatGPT V2 and Claude V2 Cleanroom. Both hosts preserve unspecified condition, correctly search across new and used inventory, and produce the same five-result ordering.

No V1 baseline is required for this case because there is no anomaly to isolate. Continue regression testing.
