# CarClever V2 / V3 Version Lineage — 2026-09-11

**Status:** CONFIRMED terminology and release-lineage note

## Purpose

This document records the canonical shorthand for the original CarClever V2 incremental work and the V3 split so future notes do not reuse the retired `V2.3` label incorrectly.

## Canonical V2 lineage

The historical V2 work packages should be read as follows:

| Historical label | Scope | Current home |
|---|---|---|
| **V2.1** | Result-count correctness, including the widget/header fix from ambiguous `Top 5 shown` wording to explicit counts such as `Top 5 of 8 shown` when more matches exist | **V2** |
| **V2.2** | Deterministic listing/action URL redesign, including split **Check avail.** / **View similar** CTAs, VIN/listing URL handling, fallback-link behavior, and related link-resolution hardening | **V2** |
| **V2.3** | Separate `check_vehicle` workflow/tool, including NHTSA recall checking and the expanded vehicle-check path | **RETIRED LABEL — MOVED TO V3** |
| **V2.4** | Search/ranking correctness improvements, notably continuous price-proximity scoring plus the modest Used-value tie-break in `matchScore` | **V2** |
| **V2.5** | Result clarity: New / Used / CPO condition surfaced in per-listing text output | **V2** |
| **V2.6** | Malformed-ZIP / unsupported-vehicle-category / input-and-scope robustness was a provisional future bucket, not an established shipped V2 release increment | **Provisional / not canonical release numbering** |

## Canonical rule going forward

- **V2** means improvements to the existing V2 search/listing experience without introducing a new tool surface.
- The active historical V2 work packages incorporated into the V2 lineage are **V2.1, V2.2, V2.4 and V2.5**.
- **Do not call recalls or `check_vehicle` work “V2.3” in new documentation.** The old `V2.3` label is retired; that work is **V3**.
- **V3** is the lane for the additional `check_vehicle` tool/workflow and associated recall/check-vehicle functionality.
- Older historical notes may retain the string `V2.3` for chronology, but they should be interpreted through this mapping rather than treated as current terminology.

## Relationship to current regression work

The September 2026 V2 regression cycle is validating the current combined V2 contract across ChatGPT V2, Claude V2 Cleanroom and V1 baseline. Those regression case numbers are test-case identifiers, not release-version numbers and must not be confused with V2.1/V2.2/V2.4/V2.5.

## Current V3 state

V3 remains a separate paused lane. No V3 work should be described as part of the V2 release solely because older session notes once used the `V2.3` label.
