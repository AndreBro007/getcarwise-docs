# STATUS_V2.4_MATCH_SCORE_IMPLEMENTATION_20260907.md

**From:** Claude / Engineering lane
**Re:** Implementation of the V2.4 scope ChatGPT specified (André-approved) in the Sep 7 message following `HANDOFF_V2_BACKLOG_INVESTIGATION_20260907.md`

## What was built

`lib/match-score.ts`:
1. **Continuous price-proximity scoring** — `statedCriteriaFit`'s `priceMax`/`priceMin` checks changed from binary (in/out of range) to graded (0 / 0.85–1.0), differentiating candidates that previously scored identically for both satisfying the same price constraint at different distances from the ceiling/floor. Year/mileage/make/model checks are untouched, still plain booleans.
2. **Modest Used-value tie-break** — `resolvedCriteriaFit` gains a small bonus (+0.04, +0.02 more if clearly low-mileage/"nearly-new") for a reported-Used candidate, structurally a no-op when `CardIntentInput.used === false` (explicit New-only). CPO and explicit-Used intent are unaffected in correctness, just receive the same modest nudge uniformly.

Weights (0.55/0.30/0.15), match-score labels, and `penalizedByRelaxation`'s deliberate deferral are all explicitly unchanged.

## Where it lives

**Branch `v2.4/match-score-price-proximity`**, branched off `release/v2`'s tip — **not merged into `release/v2`**, and `release/v2`/`main` (V1) are both confirmed untouched (re-verified against GitHub directly after push, not assumed). Commit `18ae2a2`, `carclever-find-my-car` repo.

## Validation status against ChatGPT's required list

| Requirement | Status |
|---|---|
| Full existing V2 regression suite re-run | ✅ 54/54 pass, 0 regressions (local run) |
| New unit coverage: mixed New/Used/CPO | ✅ `tests/match-score.test.ts`, V2.4-6 |
| High-budget searches | ✅ V2.4-7 |
| Explicit New requests | ✅ V2.4-8 (confirmed structural no-op) |
| Explicit Used requests | ✅ V2.4-9 |
| CPO searches | ✅ V2.4-10 |
| Equal and near-equal prices | ✅ V2.4-2, V2.4-3 |
| Lower-priced Used with better trim | ✅ V2.4-11 (trim held equal via existing `trimPreference` mechanism — a true independent trim-value model was out of scope for a bounded fix, noted explicitly) |
| New clearly best/only fit | ✅ V2.4-12 |
| Typecheck | ✅ `tsc --noEmit` clean |
| **Claude rendered-output confirmation** | ⏳ **Not yet done** — needs a live pass via the `CarClever V2 Test` Claude connector once this branch (or a preview deployment of it) is reachable there |
| **ChatGPT rendered-output confirmation** | ⏳ **Not yet done** — same, via ChatGPT's `CarClever V2 Test` connector |

**12 new unit tests, 66/66 total passing, 0 regressions — but the two live cross-platform rendering checks are still outstanding.** The current `ccfmc-dev-v2` connectors both point at `release/v2` itself, not this new branch, so a live check requires either a temporary deployment of this branch or merging it into `release/v2` first (André's call on order of operations).

Full code and commit detail: `carclever-find-my-car`, branch `v2.4/match-score-price-proximity`.
