# CarClever V2 Submission-Baseline Test — Reliable Hybrid SUV — 2026-09-11

**Status:** CLOSED — CROSS-HOST / CROSS-VERSION PASS WITH CONDITION-SCOPE + HOST-WORDING WATCHES

## Prompt

`Find a reliable hybrid SUV under $50,000 with less than 60,000 miles near 90210.`

This is an exact prior reviewer-facing submission test prompt.

## ChatGPT V2

Primary request:

```json
{
  "bodyType": "SUV",
  "model": "RAV4, CR-V, Venza, NX, Highlander",
  "priceMax": 50000,
  "priceFlexibility": "strict",
  "mileageMax": 60000,
  "used": true,
  "zip": "90210",
  "electrificationRequirement": "required",
  "electrificationTypes": ["hybrid"],
  "priorityAxis": "lower_risk",
  "vehicleNeeds": ["reliable hybrid SUV"]
}
```

The host also ran a targeted Toyota RAV4 pass with the same core constraints.

Assessment:
- PASS on hybrid handling: `electrificationRequirement: required` plus `electrificationTypes: ["hybrid"]` is the clearest first-class expression of the user's hard powertrain requirement.
- PASS on semantic interpretation of `reliable`: the host used a model shortlist and `lower_risk` rather than fabricating hard `noAccidents`, `oneOwner`, or `cpo` filters.
- Positive wording: the host explicitly said reliability guided model selection and was not independently proven by listing data.
- WATCH: `used: true` was not stated in the prompt. This is a real hard scope restriction and can exclude otherwise valid new hybrid SUVs. Under the current anti-invention rule, condition should remain unset unless stated or clearly implied.

## Claude V2 Cleanroom

Request:

```json
{
  "zip": "90210",
  "bodyType": "SUV",
  "priceMax": 50000,
  "mileageMax": 60000,
  "electrificationTypes": ["hybrid"],
  "electrificationRequirement": "required",
  "model": "RAV4, CR-V, Highlander, Tucson, Escape, Rogue",
  "used": true,
  "priorityAxis": "best_for_budget"
}
```

Assessment:
- PASS on the hard price, mileage, ZIP, body type, and required-hybrid constraints.
- PASS on broad semantic model selection; the model shortlist remained reasonably diverse.
- WATCH: like ChatGPT V2, Claude added `used: true` even though the prompt did not specify used condition.
- HOST-WORDING WATCH: Claude stated that the returned Toyota models were reliable and added broad brand-level claims about dependability, fuel efficiency, resale value, and maintenance costs. Those claims were not established by the CarClever listing evidence itself.

## ChatGPT V1 baseline

Request:

```json
{
  "zip": "90210",
  "bodyType": "SUV",
  "model": "RAV4 Hybrid,CR-V Hybrid,Venza,Highlander Hybrid,Corolla Cross Hybrid,NX 350h,NX 450h+,RX 350h,RX 450h+,CX-90 PHEV",
  "mileageMax": 60000,
  "priceMax": 50000,
  "priceFlexibility": "strict",
  "goals": [
    "reliability",
    "hybrid powertrain",
    "low running costs"
  ],
  "priorityAxis": "best_for_budget"
}
```

Assessment:
- PASS on preserving new + used eligibility: V1 did **not** add `used: true`, which is the cleanest mapping of the exact prompt because the user never specified condition.
- V1's hybrid representation is older/less explicit than V2 because it relies primarily on hybrid-specific model names and goals rather than first-class required-electrification fields.
- Positive wording: V1 also disclosed that reliability informed model selection but listing data did not independently prove mechanical condition.

## Final conclusion

CLOSED — overall PASS across ChatGPT V2, Claude V2 Cleanroom, and ChatGPT V1.

Key finding: V2's first-class electrification contract is stronger than V1's, but both ChatGPT V2 and Claude introduced an unstated hard `used: true` restriction. V1 correctly left vehicle condition unrestricted. This should remain an anti-invention / condition-scope regression watch for V2 hosts.

Semantic model shortlists remain acceptable when they materially improve relevance, remain reasonably broad, and are clearly presented as AI interpretation rather than verified reliability evidence.
