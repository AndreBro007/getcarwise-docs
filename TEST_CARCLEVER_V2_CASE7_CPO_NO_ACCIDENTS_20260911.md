# CarClever V2 Case 7 — CPO + No Accidents — 2026-09-11

**Status:** CLOSED — CROSS-HOST PASS WITH UI DISCLOSURE WATCH

## Prompt

`Find me a certified pre-owned SUV with no accidents under $40k in 75001.`

## ChatGPT V2

Observed request:

```json
{
  "bodyType": "SUV",
  "cpo": true,
  "noAccidents": true,
  "priceMax": 40000,
  "priceFlexibility": "strict",
  "priorityAxis": "lower_risk",
  "radiusMiles": 50,
  "used": true,
  "vehicleType": "SUV",
  "zip": "75001",
  "vehicleNeeds": [
    "certified pre-owned SUV",
    "no accidents",
    "under $40,000 near 75001"
  ]
}
```

Assessment:
- Core semantics correct.
- `used:true` is justified because CPO clearly implies used/pre-owned.
- `lower_risk` is defensible because the request includes both CPO and accident-history intent.
- `vehicleType:"SUV"` is redundant but neutralized by the current exact-duplicate server gate.
- `radiusMiles:50` is redundant/default-like but did not narrow beyond documented local behavior.
- Text response correctly stated that none of the returned listings were confirmed CPO and treated them as vehicles requiring CPO verification.
- Watch item: listing cards did not visibly communicate CPO evidence/status as clearly as the text response. For a user who scans cards only, this could make unconfirmed vehicles look more like direct CPO matches than intended.

## Claude V2 Cleanroom 20260911

The second-account cleanroom connector loaded the current V2 metadata and was invoked from the same natural-language prompt without explicitly naming the connector. Discovery search query was `find vehicle cars for sale`, and the host loaded only the cleanroom connector tools.

Observed request:

```json
{
  "bodyType": "SUV",
  "cpo": true,
  "noAccidents": true,
  "priceMax": 40000,
  "zip": "75001",
  "used": true,
  "priorityAxis": "best_for_budget"
}
```

Assessment:
- Clean request under the current contract.
- `used:true` justified by CPO.
- No invented transmission, year, mileage, radius, make/model, or vehicleType restriction.
- `best_for_budget` differs from ChatGPT's `lower_risk`, but is still contract-valid because the user did not explicitly ask to optimize for lower risk; CPO/no-accidents remain evidence requests rather than guaranteed exclusions.
- Tool response correctly distinguished `Not reported as CPO` from definitive non-CPO status and disclosed accident-history evidence per listing.
- Claude's summary correctly excluded accident-reported vehicles from its recommended subset and warned that CPO status still needed confirmation.

## Cross-host conclusion

PASS. Both current V2 hosts translated the user request correctly and preserved the evidence model:

- CPO and no-accident requests are represented directly.
- Missing CPO evidence remains unknown/unreported rather than silently treated as confirmed or false.
- Accident evidence is disclosed rather than overclaimed as a provider-guaranteed hard exclusion.
- `used:true` is a valid implication of CPO, not an invented restriction.

The main remaining issue is presentation rather than search correctness: the result card should make CPO evidence/state sufficiently visible when CPO is part of the user's request.

## Claude invocation note

On the second-account cleanroom setup, Claude successfully discovered and invoked the sole connected automotive tool from the same plain natural-language prompt used on ChatGPT. For current regression testing, prompts can therefore remain identical across ChatGPT V2 and Claude Cleanroom V2 unless tool-selection ambiguity appears later. Explicit connector naming remains a fallback, not a requirement for every cleanroom case.
