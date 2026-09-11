# CarClever V2 Submission-Baseline Test — Low-Risk Used F-150 for Towing — 2026-09-11

**Status:** CLOSED — CROSS-HOST / CROSS-VERSION PASS WITH CLAUDE HARD-FILTER + SUMMARY-WORDING WATCHES

## Prompt

`Find a low-risk used F-150 under $50,000 for towing near Denver.`

This is an exact prior reviewer-facing submission test prompt.

## ChatGPT V2

Request:

```json
{
  "make": "Ford",
  "model": "F-150",
  "used": true,
  "priceMax": 50000,
  "priceFlexibility": "strict",
  "zip": "80202",
  "radiusMiles": 100,
  "priorityAxis": "lower_risk",
  "vehicleNeeds": ["towing"]
}
```

Assessment:
- PASS — exact make/model, explicit used condition, strict budget, lower-risk ranking, and towing need all mapped correctly.
- PASS — towing remained a suitability need rather than being converted into an invented tow-package, engine, axle-ratio, or payload hard filter.
- Positive wording: the host explicitly required VIN-specific tow-package / axle-ratio / payload verification before purchase.
- Minor watch: `radiusMiles: 100` was host-selected from the phrase `near Denver`. This is a reasonable geographic interpretation but still broader than an explicitly stated radius.

## Claude V2 Cleanroom

Request:

```json
{
  "make": "Ford",
  "model": "F-150",
  "used": true,
  "priceMax": 50000,
  "zip": "80202",
  "radiusMiles": 100,
  "bodyType": "Truck",
  "priorityAxis": "lower_risk",
  "vehicleNeeds": ["towing"],
  "noAccidents": true,
  "oneOwner": true
}
```

Assessment:
- PASS on the core requested constraints and `lower_risk` axis.
- WATCH: `noAccidents: true` and `oneOwner: true` were not stated by the user. These are hard history filters, not merely ranking preferences, and can improperly narrow the universe. `low-risk` should normally remain a ranking/evidence concept unless the user explicitly asks for those hard conditions.
- Tool response remained useful and returned eight candidates, so this inference did not collapse the result set in this observed run.
- Summary accuracy issue: Claude stated that all returned trucks had no reported accidents even though one result explicitly had accident history unreported.
- Unsupported wording watch: Claude added trim-level towing, payload, cooling-system, and warranty claims that were not established by the returned listing evidence.

## ChatGPT V1 baseline

Request:

```json
{
  "zip": "80202",
  "make": "Ford",
  "model": "F-150",
  "used": true,
  "priceMax": 50000,
  "priceFlexibility": "strict",
  "goals": [
    "towing suitability",
    "strong payload capability"
  ],
  "priorityAxis": "lower_risk"
}
```

Assessment:
- PASS — cleanest treatment of `low-risk`: ranking/evidence rather than hard `noAccidents` / `oneOwner` filters.
- PASS — towing kept as a practical-need signal, with VIN-specific axle ratio, tow package, trailer-brake controller and payload sticker left for explicit verification.
- Positive wording: V1 clearly stated that stronger reported-history evidence was being prioritized and that this was shortlist guidance rather than a condition guarantee.

## Final conclusion

CLOSED — overall PASS across ChatGPT V2, Claude V2 Cleanroom and ChatGPT V1 for the exact prior-submission F-150 towing prompt.

Best behavior in this case was ChatGPT V1 / ChatGPT V2: `low-risk` remained a ranking/evidence concept. Claude's `noAccidents:true` and `oneOwner:true` should remain a substantive host-inference watch because they convert a soft risk preference into hard eligibility restrictions.
