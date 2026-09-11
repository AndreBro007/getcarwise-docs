# CarClever V2 Submission-Baseline Test — Used Honda CR-V — 2026-09-11

**Status:** CLOSED — CROSS-HOST / CROSS-VERSION PASS WITH MINOR CLAUDE SUMMARY-WORDING WATCH

## Prompt

`Find a used Honda CR-V under $25,000 with less than 60,000 miles near 90210.`

This is an exact prior reviewer-facing submission test prompt.

## ChatGPT V2

Request:

```json
{
  "make": "Honda",
  "model": "CR-V",
  "priceMax": 25000,
  "priceFlexibility": "strict",
  "mileageMax": 60000,
  "used": true,
  "zip": "90210",
  "priorityAxis": "best_for_budget"
}
```

Assessment:
- PASS — all stated constraints mapped correctly.
- No invented year, trim, drivetrain, radius, or history filter.
- Correctly treated a 2021 CR-V with unreported mileage as not verified against the 60,000-mile cap.

## Claude V2 Cleanroom

Request:

```json
{
  "make": "Honda",
  "model": "CR-V",
  "used": true,
  "priceMax": 25000,
  "mileageMax": 60000,
  "zip": "90210"
}
```

Tool response returned 5 closely matching vehicles out of 32 in the area. One 2021 CR-V EX had mileage unknown and was scored lower.

Assessment:
- PASS — clean request mapping with no invented restrictions.
- Tool/result behavior correctly preserved the unknown mileage state.
- Minor host-summary wording watch: Claude's prose said all five were under 60,000 miles even though the 2021 vehicle's mileage was unknown. This is a presentation accuracy issue, not a backend-filtering defect.

## ChatGPT V1 baseline

Request:

```json
{
  "zip": "90210",
  "make": "Honda",
  "model": "CR-V",
  "used": true,
  "priceMax": 25000,
  "priceFlexibility": "strict",
  "mileageMax": 60000,
  "priorityAxis": "best_for_budget"
}
```

Result: 32 matches near 90210. V1 explicitly stated that the 2021 CR-V EX with unreported mileage could not be confirmed against the 60,000-mile limit.

Assessment:
- PASS — exact reviewer-facing intent preserved.
- PASS — unknown mileage handled conservatively and correctly.

## Final conclusion

CLOSED — PASS across ChatGPT V2, Claude V2 Cleanroom, and ChatGPT V1 for the exact prior-submission CR-V prompt.

The only watch is Claude's final prose overstating the unknown-mileage fifth vehicle as satisfying the mileage cap. The underlying request and tool response remained correct.
