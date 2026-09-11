# CarClever V2 Case 8 — Lowest-Mileage Used Honda CR-V — 2026-09-11

**Status:** CLOSED — CROSS-HOST/CROSS-VERSION PASS WITH PROVIDER/LOCAL-INVENTORY WATCH

## Prompt

`Find me the lowest-mileage used Honda CR-V under $32k in 85001.`

## ChatGPT V2

Observed request:

```json
{
  "make": "Honda",
  "model": "CR-V",
  "priceMax": 32000,
  "priceFlexibility": "strict",
  "priorityAxis": "lowest_mileage",
  "used": true,
  "zip": "85001"
}
```

Result: no matches, including after the tool's automatic radius check.

Assessment:
- Request mapping is clean and correct.
- `used:true` is explicit from the prompt.
- `priorityAxis:"lowest_mileage"` is correct.
- No invented year, trim, drivetrain, transmission, mileage ceiling, radius, or body-style restriction.

## Claude V2 Cleanroom

Observed request:

```json
{
  "make": "Honda",
  "model": "CR-V",
  "zip": "85001",
  "priceMax": 32000,
  "used": true,
  "priorityAxis": "lowest_mileage"
}
```

Result: no matches, including after automatic radius widening.

Assessment:
- Semantically equivalent to ChatGPT V2.
- Same clean current-contract mapping.
- No extra restrictions invented.

## ChatGPT V1 baseline

Observed request:

```json
{
  "zip": "85001",
  "make": "Honda",
  "model": "CR-V",
  "priceMax": 32000,
  "priceFlexibility": "strict",
  "used": true,
  "priorityAxis": "lowest_mileage"
}
```

Result: no matches after automatic radius widening.

Assessment:
- Same effective criteria and same outcome as both V2 hosts.

## Conclusion

PASS. The zero-result outcome is reproducible across ChatGPT V2, Claude V2 Cleanroom, and ChatGPT V1 using essentially the same request semantics. This strongly indicates a provider/local-inventory/geography coverage issue rather than a V2 regression or host interpretation defect.

External market checks showed used Honda CR-V inventory under $32k in the broader Phoenix market, so preserve a **provider/local-inventory watch** for ZIP 85001 rather than interpreting the zero result as proof that no such vehicles exist in the wider retail market.

No engineering action is justified from this case alone. Continue regression testing.
