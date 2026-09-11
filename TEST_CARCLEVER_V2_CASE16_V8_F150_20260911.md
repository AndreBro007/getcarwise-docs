# CarClever V2 Case 16 — V8 Ford F-150 — 2026-09-11

**Status:** CLOSED — CYLINDERS PASS ACROSS HOSTS/VERSIONS WITH 30301 GEO-RESOLUTION WATCH

## Prompt

`Find me a V8 Ford F-150 under $45k in 30301.`

## ChatGPT V2

Observed initial request:

```json
{
  "make": "Ford",
  "model": "F-150",
  "cylinders": 8,
  "priceMax": 45000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget",
  "zip": "30301"
}
```

Because 30301 returned zero searchable inventory, ChatGPT retried with nearby ZIP 30303 using the same filters.

Assessment:
- Correctly mapped `V8` to the dedicated hard-filter field `cylinders: 8`.
- Did not rely on engine-text inspection or manual post-filtering.
- Good trust behavior: three candidate vehicles were excluded because their cylinder data conflicted with VIN-decoded six-cylinder configurations.
- Geo watch: the host substituted 30303 after 30301 failed. It disclosed the substitution, so this is not a silent change, but asking before changing the user’s ZIP is cleaner behavior.

## Claude V2 Cleanroom

Observed request:

```json
{
  "zip": "30301",
  "make": "Ford",
  "model": "F-150",
  "priceMax": 45000,
  "cylinders": 8,
  "priorityAxis": "best_for_budget"
}
```

Result: no vehicles matched and a broader check found zero listings of any kind near 30301. Claude explained that the ZIP might not resolve to a searchable street location and asked the user before trying a nearby ZIP.

Assessment:
- Correct `cylinders: 8` mapping.
- Preserved the exact user ZIP.
- Better host handling of the geo issue than the ChatGPT V2 retry because it requested user confirmation before changing location.

## ChatGPT V1 baseline

Observed request:

```json
{
  "zip": "30301",
  "make": "Ford",
  "model": "F-150",
  "cylinders": 8,
  "priceMax": 45000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget"
}
```

Result: no matches because 30301 did not resolve as a searchable street location. V1 kept the Ford F-150, V8, and $45,000 filters strict and suggested nearby geographic ZIPs such as 30303 or 30309.

Assessment:
- Clean baseline confirming the same `cylinders: 8` behavior.
- Preserved the user’s ZIP rather than substituting another one automatically.
- Reinforces that the 30301 behavior is a location/provider-resolution issue rather than a cylinders-filter defect.

## Final conclusion

CLOSED — PASS on the V8/cylinder requirement across ChatGPT V2, Claude V2 Cleanroom, and ChatGPT V1.

This case validates that a stated V8 requirement must map to the dedicated `cylinders: 8` structured field and should be enforced as a real search filter. It also independently re-confirms the known 30301 geo/provider-resolution watch.

Preferred host behavior when the supplied ZIP cannot resolve is to preserve the user’s location and ask before substituting a nearby ZIP. ChatGPT V2 disclosed its 30303 retry, so this is a host-location-handling watch rather than a backend or cylinders regression.
