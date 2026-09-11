# CarClever V2 Case 11 — Manual Mazda MX-5 — 2026-09-11

**Status:** OPEN — CHATGPT V2/V1 PASS; CLAUDE CLEANROOM ANTI-INVENTION WATCH

## Prompt

`Find me a manual Mazda MX-5 under $20k in 90210.`

## ChatGPT V2

Observed request:

```json
{
  "make": "Mazda",
  "model": "MX-5 Miata",
  "transmission": "Manual",
  "priceMax": 20000,
  "priceFlexibility": "strict",
  "zip": "90210",
  "priorityAxis": "best_for_budget"
}
```

Result: five strong manual MX-5 matches under $20,000 near 90210.

Assessment:
- Correct explicit Manual mapping.
- Correct make/model interpretation.
- No invented `used`, radius, year, mileage, trim, or drivetrain restriction.
- Host explicitly stated that `used`, radius, year, and mileage were left unset because the user did not specify them.

## Claude V2 Cleanroom

Observed request:

```json
{
  "zip": "90210",
  "make": "Mazda",
  "used": true,
  "model": "MX-5",
  "priceMax": 20000,
  "priorityAxis": "best_for_budget",
  "transmission": "Manual"
}
```

Result: no matches, including after automatic radius widening.

Assessment:
- `used:true` was not stated or clearly implied and is therefore an anti-invention watch item under the current V2 contract.
- Claude used `model:"MX-5"`; this is not by itself a problem because V1 demonstrated that the service can normalize `MX-5` to `MX-5 Miata` and still return the expected inventory.
- Therefore the model-string difference does not explain the zero-result outcome.
- Working hypothesis: the extra `used:true` materially changed the search and likely caused or contributed to the zero-result outcome.
- Keep this case OPEN until one fresh-chat Claude rerun confirms whether the behavior is reproducible. If it reproduces, re-check the discovery-loaded tool metadata for the current anti-invention marker before attributing it to current Claude behavior.

## ChatGPT V1 baseline

Observed request:

```json
{
  "zip": "90210",
  "make": "Mazda",
  "model": "MX-5",
  "transmission": "Manual",
  "priceMax": 20000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget"
}
```

Result: same expected five-vehicle inventory set. The service normalized `MX-5` to `MX-5 Miata`.

Assessment:
- Confirms that `MX-5` versus `MX-5 Miata` is not the main issue.
- Confirms V1 also avoids inventing `used:true` for this prompt.
- Strongly isolates Claude's extra condition as the current anomaly.

## Current conclusion

ChatGPT V2 and V1 PASS. Claude Cleanroom remains an OPEN host-specific anti-invention watch because it added `used:true` to an unspecified-condition prompt and then returned zero inventory while the other two environments found the expected five matches.

No CarClever backend regression is established from this evidence. One controlled fresh-chat Claude rerun is the next diagnostic step.
