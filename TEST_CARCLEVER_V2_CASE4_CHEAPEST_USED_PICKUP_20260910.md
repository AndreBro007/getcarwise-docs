# CarClever V2 Test #4 — Cheapest Used Pickup + Invalid ZIP — 2026-09-10

**Status:** CLOSED — PASS WITH HOST/UI WATCH ITEMS  
**Prompt:** `Find me the cheapest used pickup under $40k near 30301.`

## Purpose

Validate `used`, pickup/truck body intent, strict price ceiling, `priorityAxis: cheapest`, ZIP handling, retry/widening behavior, and parity with the ChatGPT V1 baseline.

## ChatGPT V2

The original search against ZIP `30301` returned no usable local result. ChatGPT retried multiple times, rendered the CarClever V2 widget three times, then substituted nearby Atlanta ZIP `30303` and widened the radius to 100 miles. The successful request was:

```json
{
  "bodyType": "pickup",
  "used": true,
  "priceMax": 40000,
  "priceFlexibility": "strict",
  "priorityAxis": "cheapest",
  "zip": "30303",
  "radiusMiles": 100,
  "vehicleNeeds": [
    "pickup truck"
  ]
}
```

The resulting cheapest match was a 1997 Ford F-150 at $7,485. ChatGPT disclosed that `30301` could not be resolved and that it had switched to `30303` and widened to 100 miles.

Assessment:
- **PASS:** `used: true`, strict `$40k` ceiling and `priorityAxis: "cheapest"` correctly preserve the explicit request.
- **PASS:** pickup/truck intent was preserved.
- **WATCH:** ChatGPT changed the requested ZIP from `30301` to `30303` without first asking the user.
- **WATCH:** ChatGPT widened radius to 100 miles as part of the retry flow.
- **UI/HOST WATCH:** three widget instances were rendered because unsuccessful/retry calls each produced another card. This is confusing even though the final search succeeded.

## Claude V2

Actual request:

```json
{
  "zip": "30301",
  "used": true,
  "model": "F-150,Silverado,Ram 1500,Tundra,Tacoma,Colorado,Canyon,Gladiator",
  "bodyType": "Truck",
  "priceMax": 40000,
  "priorityAxis": "cheapest"
}
```

Claude received no matches and reported that a broader check also found zero listings of any kind near `30301`, indicating the ZIP itself was probably not resolving as a searchable inventory location. Claude stopped and asked the user whether to retry using a nearby standard Atlanta ZIP such as `30303`, `30305`, or `30308`.

Assessment:
- **PASS:** Claude preserved the original ZIP rather than silently substituting it.
- **PASS:** Claude did not widen radius, price, year, condition or other criteria without permission.
- **PASS:** `used`, strict budget intent and `cheapest` ranking were preserved.
- **WATCH:** the candidate list included `Ram 1500`; the service explicitly corrected this to model `1500`, showing another manufacturer-name/model-field formatting issue.
- **HOST BEHAVIOR:** Claude's recovery flow is cleaner than ChatGPT's for an unresolvable ZIP because it asks before changing geography.

## ChatGPT V1 baseline

ChatGPT V1 showed very similar retry behavior. It rendered the V1 widget repeatedly, attempted multiple structured requests against `30301`, then invoked a separate older CarClever app as a fallback. Because that last fallback crossed app boundaries, its nationwide result is not clean evidence of the V1 Find My Car contract and should not be treated as a V1 inventory-quality baseline.

Actual V1 structured requests:

First attempt:

```json
{
  "bodyType": "Truck",
  "used": true,
  "priceMax": 40000,
  "priceFlexibility": "strict",
  "priorityAxis": "cheapest",
  "zip": "30301",
  "radiusMiles": 50,
  "goals": [
    "cheapest used pickup under $40k near 30301"
  ]
}
```

Second attempt correcting body label:

```json
{
  "bodyType": "Pickup",
  "used": true,
  "priceMax": 40000,
  "priceFlexibility": "strict",
  "priorityAxis": "cheapest",
  "zip": "30301",
  "radiusMiles": 50,
  "goals": [
    "cheapest used pickup under $40k near 30301"
  ]
}
```

Fallback older-CarClever request:

```json
{
  "keywords": "cheapest used pickup truck under $40k near 30301",
  "price_max": 40000,
  "zip": "30301",
  "distance": 50,
  "sort_by": "price_low"
}
```

Later stricter model-list retry:

```json
{
  "model": "F-150,Silverado 1500,Ram 1500,Sierra 1500,Tundra,Tacoma,Colorado,Ranger,Frontier,Canyon,Ridgeline,Maverick,Gladiator,Titan",
  "used": true,
  "priceMax": 40000,
  "priceFlexibility": "strict",
  "priorityAxis": "cheapest",
  "zip": "30301",
  "radiusMiles": 50,
  "goals": [
    "cheapest used pickup under $40k near 30301"
  ]
}
```

## V1 ↔ V2 comparison

- **Core search semantics:** preserved. V1 and both V2 hosts correctly represented used inventory, pickup/truck intent, the `$40k` maximum and `cheapest` ranking.
- **ZIP behavior:** both V1 and V2 demonstrated that `30301` is problematic for this inventory search. This is therefore not a V2-only regression.
- **Retry behavior:** ChatGPT retries aggressively and can produce repeated widget cards. This occurred in both V1 and V2, indicating a ChatGPT host/retry presentation issue rather than a new V2 regression.
- **Recovery quality:** Claude V2 was the cleanest host behavior because it stopped and asked before changing geography.
- **Cross-app fallback:** ChatGPT V1 eventually invoked another older CarClever app. This is a host-routing/fallback issue and invalidates that later result as a pure V1 comparison point; it is not evidence of a V2 backend defect.
- **Model formatting:** Claude V2 and a V1 retry both used manufacturer-prefixed `Ram 1500`, reinforcing the existing model-format watch item across hosts/versions.

## Verdict

**PASS WITH HOST/UI WATCH ITEMS.** No material V2 regression is demonstrated. The important issue exposed by this case is recovery behavior around an unresolvable ZIP, especially ChatGPT's repeated widget rendering and automatic geography substitution/widening. These are worth tracking, but the V1 baseline shows the retry/presentation problem predates V2.

**No code or description change recommended from this case alone.** Continue testing and look for recurrence before escalating.

## Watch items carried forward

1. ChatGPT repeated widget rendering on retry/fallback flows.
2. ChatGPT may substitute ZIP/radius automatically rather than asking before changing geography.
3. Manufacturer-prefixed model values continue to appear in some host-generated candidate lists (`Ram 1500`).
4. ChatGPT V1 can cross-route into another CarClever app during fallback; treat such mixed-app results as invalid for clean V1 baseline comparison.
