# CarClever V2 Case 11 — Manual Mazda MX-5 — 2026-09-11

**Status:** CLOSED — CHATGPT V2/V1 PASS; CLAUDE CLEANROOM HOST-SEMANTIC WATCH

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

Initial observed request:

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

Follow-up attempts continued to preserve `used:true` while changing radius, price flexibility, and even removing the transmission restriction. Those Mazda searches still returned no results. Claude then proposed alternative lightweight/manual sports cars and found valid Subaru BRZ and Toyota 86 inventory under $20k using the same general location and `used:true` assumption.

Assessment:
- `used:true` was not stated or clearly implied and remains a host-semantic anti-invention watch item under the current V2 contract.
- Claude used `model:"MX-5"`; this is not by itself a problem because V1 demonstrated that the service can normalize `MX-5` to `MX-5 Miata` and return the expected inventory.
- The repeated Mazda attempts make the extra condition the most meaningful observed request difference versus ChatGPT V2/V1, but the exact causal mechanism for the zero-result outcome is not proven.
- Claude's fallback behavior was useful from a shopper perspective: once the requested Mazda search exhausted, it offered nearby alternatives and successfully found manual BRZ/86 inventory.
- This is therefore a host interpretation/recovery watch rather than a CarClever backend regression.

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
- Provides a clean baseline against Claude's extra condition.

## Final conclusion

CLOSED. ChatGPT V2 and V1 PASS. Claude Cleanroom shows a minor host-semantic quirk by repeatedly inserting `used:true` when condition was unspecified. That behavior is imperfect but not release-blocking in this case, especially because Claude eventually recovered by offering and successfully searching reasonable alternatives.

No CarClever V2 backend regression is established from this case. Preserve the Claude `used:true` behavior as a regression watch for future unspecified-condition prompts, but no additional MX-5 diagnostic is required before continuing the bank.
