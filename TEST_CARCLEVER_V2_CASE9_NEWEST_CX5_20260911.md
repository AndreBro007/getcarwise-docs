# CarClever V2 Case 9 — Newest Mazda CX-5 — 2026-09-11

**Status:** CLOSED — CROSS-HOST / CROSS-VERSION PASS

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

## ChatGPT V1 baseline

V1 returned the same 424-match pool near 98101 and the same five 2026 vehicles in the same order, including the same lowest-priced used CX-5 and the same best new option.

Observed wall-clock time reported by André for this single V1 run: **14 seconds**. The corresponding ChatGPT V2 run was reported at **26 seconds**.

Timing assessment:
- Record this as a single-run qualitative observation only, not a benchmark.
- Host latency, tool cold/warm state, network conditions, rendering, and inventory response time can all vary between runs.
- Do not infer that V1 is generally faster from this one comparison; repeated controlled runs would be needed for a performance conclusion.

## Conclusion

PASS. The `newest` path behaves consistently across ChatGPT V2, Claude V2 Cleanroom, and ChatGPT V1. All preserve unspecified condition, correctly search across new and used inventory, and produce the same five-result ordering.

The one observed V1 timing was faster than V2 (14s vs 26s), but this remains a non-controlled single-run observation rather than evidence of a systematic performance difference.
