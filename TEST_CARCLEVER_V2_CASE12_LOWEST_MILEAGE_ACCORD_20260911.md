# CarClever V2 Case 12 — Lowest-Mileage Honda Accord — 2026-09-11

**Status:** CLOSED — CROSS-HOST / CROSS-VERSION PASS WITH MINOR HOST-WORDING WATCH

## Prompt

`Find me the lowest-mileage Honda Accord under $30k in 10001.`

## ChatGPT V2

Observed request:

```json
{
  "make": "Honda",
  "model": "Accord",
  "priceMax": 30000,
  "priceFlexibility": "strict",
  "priorityAxis": "lowest_mileage",
  "zip": "10001"
}
```

Result: 1,249 local matches; top result 2025 Honda Accord LX at $22,733 with 178 miles.

Assessment:
- Clean mapping of make, model, strict budget, ZIP, and `priorityAxis:"lowest_mileage"`.
- Host did not itself add `used:true`.
- Service correctly interpreted `lowest_mileage` as a used-only search per contract and disclosed that behavior.
- This is an intentional semantic exception to the normal anti-invention rule, not an unstated-condition error.

## Claude V2 Cleanroom

Observed request:

```json
{
  "make": "Honda",
  "model": "Accord",
  "priceMax": 30000,
  "priorityAxis": "lowest_mileage",
  "radiusMiles": 50,
  "used": true,
  "zip": "10001"
}
```

Result: same 1,249-match pool and same top result/order pattern, headed by the 2025 Accord LX at 178 miles and $22,733.

Assessment:
- `used:true` is correct here because `lowest_mileage` explicitly defaults to used inventory.
- `radiusMiles:50` is harmless because 50 miles is the documented default local radius.
- Minor host wording watch: calling the 178-mile used Accord "essentially a brand-new car" is looser than ideal because the listing condition is explicitly Used. Not a mapping/backend failure.

## ChatGPT V1 baseline

Observed request:

```json
{
  "zip": "10001",
  "make": "Honda",
  "model": "Accord",
  "priceMax": 30000,
  "priceFlexibility": "strict",
  "priorityAxis": "lowest_mileage"
}
```

Result: 3.4 million listings searched → 1,249 matched near 10001. Same lowest-mileage result: 2025 Accord LX, 178 miles, $22,733. V1 explicitly disclosed that lowest-mileage ranking searched used vehicles only.

Assessment:
- Clean baseline consistent with ChatGPT V2.
- Confirms the used-only behavior belongs to the `lowest_mileage` semantic, not to host invention.
- Strong cross-version consistency on pool size, ranking, and top result.

## Final conclusion

CLOSED — PASS across ChatGPT V2, Claude V2 Cleanroom, and ChatGPT V1.

This case validates the intentional `lowest_mileage` exception: when the buyer asks for the lowest-mileage vehicle without explicitly stating condition, the search may default to used inventory. That behavior should be disclosed rather than treated as an unstated hard-filter error.

Main watch is limited to host prose: avoid describing an explicitly used vehicle as effectively or essentially new solely because mileage is extremely low.
