# CarClever V2 Case 14 — Trim-Preference Toyota RAV4 XLE — 2026-09-11

**Status:** CLOSED — CROSS-HOST / CROSS-VERSION PASS WITH MINOR HOST-WORDING WATCH

## Prompt

`Find me a Toyota RAV4 under $35k in 98101. I'd prefer the XLE trim if possible.`

## ChatGPT V2

Observed request:

```json
{
  "make": "Toyota",
  "model": "RAV4",
  "trimPreference": "XLE",
  "priceMax": 35000,
  "priceFlexibility": "strict",
  "zip": "98101"
}
```

Result: top match was a 2025 Toyota RAV4 XLE at $31,998 with 7,683 miles near 98101.

Assessment:
- Correctly mapped XLE to `trimPreference`, not `trimRequired`.
- Preserved the user's soft preference semantics.
- No invented mileage, year, condition, or radius restrictions.
- Host explicitly explained that XLE remained a ranking preference rather than a hard exclusion.

## Claude V2 Cleanroom

Observed request:

```json
{
  "make": "Toyota",
  "model": "RAV4",
  "priceMax": 35000,
  "zip": "98101",
  "trimPreference": "XLE",
  "priorityAxis": "best_for_budget"
}
```

Result: 371 matches in the area, with five shortlisted XLE vehicles. Top result matched ChatGPT V2: 2025 RAV4 XLE at $31,998 with 7,683 miles.

Assessment:
- Correct `trimPreference:"XLE"` mapping.
- `priorityAxis:"best_for_budget"` is a defensible default for a price-ceiling search with no other optimization.
- All five returned vehicles happened to be XLE, which is a good outcome but not evidence that XLE became a hard filter.
- Minor wording watch: Claude said the vehicles were "perfect matches with the XLE trim you wanted" even though the user stated XLE as a preference. This did not change the request or backend behavior.

## ChatGPT V1 baseline

Observed request:

```json
{
  "zip": "98101",
  "make": "Toyota",
  "model": "RAV4",
  "trimPreference": "XLE",
  "priceMax": 35000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget"
}
```

Result: 3.4 million listings searched → 371 matched near 98101. V1 explicitly stated that the XLE preference worked and all five shortlisted vehicles were XLEs. Top result again matched the V2 hosts: 2025 RAV4 XLE AWD at $31,998 with 7,683 miles.

Assessment:
- Clean baseline consistent with ChatGPT V2 and Claude Cleanroom.
- Confirms the required-versus-preferred trim contract works across versions and hosts.
- Strong alignment on match pool and top candidate.

## Final conclusion

CLOSED — PASS across ChatGPT V2, Claude V2 Cleanroom, and ChatGPT V1.

This case validates the soft trim-preference path: when the buyer explicitly signals a preference such as "I'd prefer the XLE trim if possible," the host should map it to `trimPreference`, not `trimRequired`, so non-XLE inventory remains eligible if needed.

Watch only host prose that overstates a preference as a requirement; no backend or mapping defect was observed.
