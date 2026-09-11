# CarClever V2 Case 10 — Lower-Risk Used SUV — 2026-09-11

**Status:** CLOSED — CROSS-HOST / CROSS-VERSION PASS WITH HOST-SUMMARY WATCH

## Prompt

`Find me a lower-risk used SUV under $35k in 28202.`

## ChatGPT V2

Observed request:

```json
{
  "model": "RAV4, CR-V, CX-5, Forester",
  "vehicleType": "SUV",
  "used": true,
  "priceMax": 35000,
  "priceFlexibility": "strict",
  "priorityAxis": "lower_risk",
  "zip": "28202",
  "vehicleNeeds": [
    "lower-risk used SUV ownership"
  ]
}
```

Result summary:
- Best match: 2025 Mazda CX-5 2.5 S Preferred AWD at $26,998, 33,130 miles.
- Listing evidence surfaced one owner and no accidents reported.
- Search widened to 100 miles because the local set was thin.
- Four vehicles qualified; the response explicitly advised avoiding one listing with a reported accident.
- Response correctly stated that `lower-risk` is based on available listing-history signals, not an independent inspection or guaranteed clean history.

Assessment:
- `used:true`, price ceiling, ZIP, and `priorityAxis:"lower_risk"` are correct.
- The host-generated model shortlist (`RAV4, CR-V, CX-5, Forester`) is accepted as useful semantic interpretation for this buyer intent rather than treated as a regression. It produced a more sensible lower-risk candidate universe than a completely broad SUV search and aligns with the product goal of having the AI improve search quality rather than merely pass through raw provider filters.
- The model shortlist should remain a watch item rather than a hard rule: future cases should avoid overly narrow or arbitrary model choices when the buyer intent does not support them.
- `vehicleType:"SUV"` is redundant under the current V2 contract; `bodyType:"SUV"` would be cleaner. Existing server-side duplicate handling limits practical impact.
- ChatGPT's user-facing explanation was strong because it tied recommendations to surfaced listing-history evidence and explicitly warned about the accident-reported candidate.

## Claude V2 Cleanroom

Observed request:

```json
{
  "bodyType": "SUV",
  "used": true,
  "priceMax": 35000,
  "zip": "28202",
  "priorityAxis": "lower_risk",
  "vehicleNeeds": [
    "lower-risk purchase"
  ]
}
```

Result: 8 vehicles out of 7,950 in the area, including:
- 2024 Honda CR-V EX-L — $34,999, 5,436 mi
- 2025 Jeep Grand Cherokee L Limited — $34,999, 25,917 mi
- 2024 Tesla Model Y Long Range — $34,999, 26,848 mi
- 2025 Land Rover Range Rover Velar P250 Dynamic SE — $34,999, 48,791 mi
- 2014 Jeep Grand Cherokee SRT — $34,998, 120,439 mi
- 2025 Jeep Grand Cherokee Limited — $34,998, 10,873 mi
- 2021 Toyota 4Runner SR5 — $34,998, 51,915 mi
- 2022 Hyundai Palisade Calligraphy — $34,998, 32,141 mi

Assessment:
- Request mapping is clean and contract-aligned.
- No invented `noAccidents`, `cpo`, `oneOwner`, year, trim, drivetrain, transmission, or mileage restriction.
- The broader search illustrates why some AI-side semantic narrowing can improve practical recommendations for a vague concept like `lower-risk`.
- Claude's final prose introduced claims such as Honda's reliability making the CR-V the "safest bet" and Hyundai's warranty being a reason to prefer the Palisade. Those claims were not established by the CarClever tool response and go beyond the tool's stated role, which explicitly does not independently establish reliability, safety, running cost, or condition. This is a **host-summary wording watch**, not a CarClever backend defect.

## ChatGPT V1 baseline

Observed request:

```json
{
  "zip": "28202",
  "bodyType": "SUV",
  "priceMax": 35000,
  "priceFlexibility": "strict",
  "used": true,
  "priorityAxis": "lower_risk",
  "goals": [
    "lower purchase risk"
  ]
}
```

Result: the same broad 7,950-match pool as Claude V2 Cleanroom. V1 ranked the available evidence more effectively in its final presentation:
- 2024 Honda CR-V EX-L first: one owner, personal use, no accidents reported.
- 2025 Jeep Grand Cherokee Limited second: one owner, corporate use, no accidents reported.
- Known weaker signals were pushed lower, including prior rental use and the 2014 Grand Cherokee SRT with four owners and 120,439 miles.
- Final wording correctly framed lower risk as reported-history/VIN evidence rather than a mechanical guarantee and recommended independent verification.

Assessment:
- V1's request behavior is materially closer to Claude V2 Cleanroom than to ChatGPT V2: broad SUV universe, no AI-generated model shortlist.
- V1 demonstrates that a broad candidate universe can still yield a strong shopper-facing result if post-search ranking and explanation use the available history evidence well.
- This three-way comparison is strategically useful: ChatGPT V2 contributes stronger pre-search semantic narrowing, while V1 contributes a useful baseline for broad-universe ranking behavior.

## Cross-host / cross-version conclusion

PASS. All three environments correctly map the explicit hard criteria and `priorityAxis:"lower_risk"` without turning lower risk into hard `noAccidents`, `cpo`, or `oneOwner` requirements.

The differences are useful rather than defective:
- ChatGPT V2 uses AI semantic interpretation to narrow toward a plausible lower-risk model set and surfaces stronger listing-history signals.
- Claude V2 Cleanroom stays broad and returns a more heterogeneous inventory set.
- ChatGPT V1 also stays broad, but its final evidence-based ranking/presentation is stronger than Claude's summary in this run.

For GetCarWise, the preferred product behavior is not merely to expose raw provider results. AI interpretation that materially improves match quality is acceptable, provided it does not become arbitrary or silently exclude clearly relevant alternatives. Broad-universe behavior remains a valuable baseline because it reveals what ranking and evidence handling accomplish without pre-search semantic narrowing.

Main remaining watch: keep user-facing lower-risk explanations grounded in actual listing evidence and avoid unsupported host claims about reliability, safety, or warranty unless those claims are separately sourced and clearly distinguished from CarClever evidence.

## Regression protocol note

For the remaining regression bank, default to a three-way comparison when practical:
1. ChatGPT V2
2. Claude V2 Cleanroom
3. ChatGPT V1 baseline

V1 is useful not only when a V2 anomaly appears, but also as a behavioral and ranking baseline. It helps distinguish host interpretation, V2 contract behavior, provider/search behavior, and changes in shopper-facing ranking or explanation. Timing observations may also be recorded, but individual runs are not performance benchmarks.
