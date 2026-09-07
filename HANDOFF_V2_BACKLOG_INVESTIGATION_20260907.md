# V2 Backlog Investigation — Engineering Findings (Sep 7, 2026)

From: Claude / Engineering lane
To: ChatGPT / Business-Strategy lane
Re: `PLAN_V2_COMPLETION_AND_RELEASE_BUCKETS_20260907.md`, investigating against `release/v2` (commit `e2ffe66`)

**Note on release-numbering:** this doc uses "V2.4/V2.5/V2.6" only as ChatGPT's own proposed bucket labels, per the plan's own framing ("do not create these automatically"). These are not new canonical version identities — they remain sub-groupings within V2 per `STATE.md`'s canonical V1/V2/V3 mapping (Sep 6, 2026).

**Method:** direct source review against `release/v2`'s actual deployed code (`ccfmc-dev-v2`), not black-box guessing. Several items turned out to already have embedded historical live-test evidence in the code's own comments (dated, pre-existing) — cited below where used instead of a fresh live repro, with an honest note on which items would benefit from an additional live pass before final promotion.

---

## 1. Hybrid-result contamination in hybrid/PHEV searches

- **Reproduces against V2?** Not as a bug — reproduces as **designed behavior**, confirmed by direct code read.
- **Classification: host-model behavior + provider data limitation, NOT an application defect.** `route.ts`'s own tool description states this explicitly (lines 77-81): *"there's no dedicated fuel-type filter"* — hybrid/PHEV inclusion is deliberately delegated to the host model constructing the right comma-separated model-name list (e.g. `"RAV4 Hybrid,RAV4 Prime"`, not `"RAV4"`) and verifying each individual result's model field. There is a real normalization/override layer (`lib/fuel-type.ts`: `normalizeFuelType`, `applyKnownHybridOverride`, a conservative whitelist of ~18 confirmed hybrid-only nameplates) — but confirmed by full-repo search, **it only affects display text (`fuelTypeDisplay`), never filters or excludes a vehicle from results.** No fuel-based `filter()` call exists anywhere in the codebase.
- **Smallest safe correction:** none required for V2 as currently scoped — the architecture is intentional and documented. If a hard-filter enforcement backstop is wanted (e.g., a `fuelRequired: "hybrid"` parameter that hard-excludes confirmed-gas listings), that's new tool-contract surface, not a contained correction — recommend **defer to V3**, not V2.4.
- **Affected files:** `lib/fuel-type.ts`, `app/[transport]/route.ts` (tool description + `normalizedFuel` usage, lines 654-850). No tests currently target this path directly (no dedicated hybrid-filter test exists because no hard filter exists).
- **Bucket recommendation:** none — not a defect to fix within V2's existing contract. If André/ChatGPT still want a hard-filter guardrail as a genuinely new capability, that belongs in V3 planning, not V2.4.
- **Regression coverage needed:** none for V2 (no code change proposed). If deferred work proceeds in V3: fixtures for hybrid-only, PHEV-only, mixed families, ambiguous trims, and unavailable electrification data, tested on both Claude and ChatGPT.

## 2. Link, Carfax, photo, and result-card consistency

- **Reproduces against V2?** No specific defect found on direct review. `lib/photos.ts` already does per-photo independent HEAD-request validation (`isReachable()`) with graceful degradation — a single broken image (real observed pattern, `SYS-20260812-014`) never invalidates the gallery or the result. `lib/link-resolution.ts` is deterministic and condition-aware (used/new/CPO/Carvana all handled distinctly), replacing an earlier live-search design that was verified working but too slow (85-100s/search) — this whole subsystem was already redesigned and live-tested this cycle (`SYS-20260904-002`).
- **Classification:** no defect found; existing design already addresses the failure modes this item was worried about (broken photos, dead links).
- **Smallest safe correction:** none identified. If André has a specific reproduction (a particular VIN/listing where a link, Carfax, or photo actually failed to render), that would change this — currently there's no concrete repro to work from, only the general category from the original backlog.
- **Affected files:** `lib/photos.ts`, `lib/link-resolution.ts`, `lib/edmunds-cj.ts`.
- **Bucket recommendation:** hold as a verification-only item, not a fix. Do not include in V2.5 without a concrete reproduction case.
- **Regression coverage needed:** if a real case surfaces — reproduce on both the raw tool payload and the rendered widget separately (per the plan's own instruction), on both Claude and ChatGPT.

## 3. VIN Buyer Check widget non-render

- **Reproduces against V2?** This has a **known, documented root cause already fixed once on this exact branch** — not the unconfirmed mystery the original backlog entry suggested. `lib/results-card.ts`'s own header comment (dated 2026-09-04, `SYS-20260904-003`) describes exactly this incident: André reported the widget not rendering/updating after a full connector cache clear and a brand-new chat. Root cause: client/connector-side widget caching keyed by the resource's URI string (`ui://carclever-find-my-car/results-card-vN`) — a content change without a URI bump doesn't reliably propagate. The fix (bump the version suffix, `v2` → `v3`) was already applied on `release/v2` in response to this exact report.
- **Classification:** confirmed application-level issue (widget caching), **already fixed** on the branch under investigation.
- **Smallest safe correction:** none needed beyond what's already shipped — but this is a "bump the URI again" class of fix that will recur any time the widget's rendered content changes without a version bump. Worth a standing reminder in `PLAYBOOK.md`/`TESTING.md` rather than a one-off code fix.
- **Affected files:** `lib/results-card.ts` (the `RESULTS_CARD_RESOURCE_URI` constant).
- **Bucket recommendation:** close as resolved for this specific incident; add a process note (not a release item) — "bump `RESULTS_CARD_RESOURCE_URI`'s version suffix on any widget content change" — to the release checklist.
- **Regression coverage needed:** confirm live on both Claude and ChatGPT that the current `results-card-v3` URI renders correctly after a fresh connector cache clear, since that's the exact scenario that broke last time.

## 4. CarMax failures

- **Reproduces against V2?** No CarMax-specific code path exists anywhere in the repo (confirmed by full-repo search across `link-resolution.ts`, `edmunds-cj.ts`, `route.ts`) — CarMax listings get exactly the same generic dealer-link handling as any other retail listing, no special-casing, no separate logic that could uniquely fail for CarMax.
- **Classification:** cannot classify as an application defect — there's no CarMax-specific code to be defective. If failures are real and reproducible, they're either a provider (Auto.dev) data issue specific to how CarMax listings are represented, or were transient (matches the plan doc's own caution: "may have been transient").
- **Smallest safe correction:** none proposed. Per the plan's own instruction, do not ship a special CarMax rule without an independent, generalizable cause — none found.
- **Affected files:** none identified.
- **Bucket recommendation:** keep as a test fixture only (retest CarMax listings periodically), not a release item, unless a fresh, reproducible, generalizable failure is found.
- **Regression coverage needed:** a standing test-fixture re-run (not a code change) — retest a CarMax listing on both Claude and ChatGPT next testing pass; only escalate if it fails again with a diagnosable pattern.

## 5. Malformed ZIP behavior at the tool layer

- **Reproduces against V2?** No — **already fixed, predates V2 entirely.** `route.ts` (lines ~1295-1311) contains a two-check validation (5-digit format regex, plus an explicit all-same-digit rejection specifically because `"00000"` passes a naive regex) with a detailed dated comment describing the exact original bug (`zip=00000` returned real, unfiltered nationwide Camrys with no error/signal) and confirming the first, single-check version of the fix reproduced the same bug before the second check was added.
- **Classification:** confirmed, already-resolved application defect (fixed before V2 existed).
- **Smallest safe correction:** none needed — already shipped, already tested against the exact original failure mode.
- **Affected files:** `app/[transport]/route.ts` (`zipFormatValid`, `zipNotAllSameDigit`, `zipIsValid`, `scopeNote` logic).
- **Bucket recommendation:** close as already-resolved, not a release item. Original open question ("host model intercepted 00000 during one test, so tool-layer behavior remains unknown") is now answered directly from source — the tool layer independently validates and gracefully falls back to a disclosed nationwide scope, it does not depend on host-model interception.
- **Regression coverage needed:** none beyond what's presumably already in the test suite for this — worth confirming `tests/` includes a direct case for `zip: "00000"` and a few other all-same-digit values if not already covered; not found in the current `tests/` directory listing, so recommend adding one as low-effort insurance, not because a defect was found.

## 6. Non-passenger vehicles appearing in broad searches

- **Reproduces against V2?** Plausible, not independently reproduced this pass. The tool description explicitly states motorcycles/ATVs are out of scope for the tool's *intended use* (line 52), but confirmed by code read: **no code-level exclusion filter exists** for non-passenger `bodyType`/`vehicleType` values — enforcement is instructional (tool description text) only, same pattern as item 1.
- **Classification:** provider data-scope characteristic + host-model behavior, not an application defect — same category as hybrid contamination (item 1), for the same underlying reason (no dedicated code-level filter exists for this axis either).
- **Smallest safe correction (if wanted):** a narrow, deterministic denylist on `vehicleType`/`bodyType` values (e.g. explicitly exclude "ATV", "Trailer", "Motorcycle" outright, regardless of search terms) — this is a small, bounded, testable change unlike item 1's broader hybrid-filter question, since it's a hard category exclusion rather than a soft preference axis.
- **Affected files:** would touch `app/[transport]/route.ts`'s result-building/filtering stage; no existing file owns this logic today.
- **Bucket recommendation:** reasonable **V2.6 candidate** if André wants it — small, contained, testable. Needs a real reproduction (a broad search that actually returns an ATV/trailer) before committing to build it, per the plan's own gate.
- **Regression coverage needed:** fixtures with a genuine non-passenger listing in the provider data (if one can be found/confirmed) plus a normal broad SUV/truck search to confirm no legitimate results get excluded; test on both Claude and ChatGPT since result-set changes affect both.

## 7. Match-score differentiation

- **Only if a contained correction — assessed as such, and appears containable.**
- **Reproduces against V2?** Yes, by design, confirmed via full read of `lib/match-score.ts`. `statedCriteriaFit` is a simple ratio of boolean-satisfied hard constraints — many structurally different candidates that all satisfy the same price/year/mileage/make/model filters score identically (e.g. all `1.0`). `resolvedCriteriaFit` is a flat `0.7` (or `0.6` with an unverifiable seat-count preference) regardless of how well a candidate actually fits semantic intent — not a bug, an explicitly-labeled "v1... intentionally simple" placeholder. `identityConfidence` is typically `1.0` for any VIN-verified listing. Identical inputs to a coarse, mostly-boolean formula naturally produce identical outputs — this is the actual root cause of the "identical `matchScore: 91`" observation.
- **Classification:** application design limitation (deliberately coarse v1 formula, already flagged in the code's own comments as provisional — `SYS-20260812-012`/`013`), not a hidden bug.
- **Smallest safe correction (bounded, does not touch scoring philosophy or weights):** replace binary threshold checks in `statedCriteriaFit` with continuous partial-credit terms where a natural continuous signal already exists (e.g. price proximity to `priceMax`/`priceMin` as a graded 0-1 value instead of a binary pass/fail) — this alone would differentiate otherwise-identical candidates without redesigning the 0.55/0.30/0.15 weighting or introducing a new philosophy. **Do not touch** the still-deliberately-unimplemented `penalizedByRelaxation` field (`SYS-20260812-013`) — that's explicitly out of scope, a separate, already-deferred design question.
- **Affected files:** `lib/match-score.ts` (`statedCriteriaFit` function only). Tests: none currently exist for this file specifically (not in the `tests/` listing) — would need new fixtures.
- **Bucket recommendation:** reasonable **V2.4 candidate**, bounded as described. Confirm with André/ChatGPT the graded-price-proximity approach specifically (vs. any broader rescoring) before implementing, since "bounded" is doing a lot of work in this classification.
- **Regression coverage needed:** fixtures with several candidates satisfying the same hard constraints at different price points within range, confirming differentiated (not identical) scores; confirm existing `Strong/Good/Partial` label thresholds still make sense against the new continuous values; test on both Claude and ChatGPT since match scores appear in both platforms' rendered output.

---

## Summary table

| # | Item | Reproduces? | Classification | Bucket |
|---|---|---|---|---|
| 1 | Hybrid contamination | As designed, not a bug | Host-model/provider, by design | None (or defer to V3 if a hard filter is wanted) |
| 2 | Link/Carfax/photo consistency | No defect found | N/A | Hold, verification-only |
| 3 | VIN Buyer Check widget non-render | Yes, historically — already fixed on this branch | App defect (widget caching), already resolved | Close; add process note |
| 4 | CarMax failures | No code path exists to fail | Cannot classify — no CarMax-specific code | Test-fixture only |
| 5 | Malformed ZIP | No — already fixed, predates V2 | App defect, already resolved | Close as resolved |
| 6 | Non-passenger vehicles | Plausible, not reproduced | Provider/host-model, by design (same as #1) | V2.6 candidate if reproduced |
| 7 | Match-score differentiation | Yes, by design (coarse formula) | App design limitation, bounded fix available | V2.4 candidate |

**Net effect: of the 7 items, only #7 (match-score) and conditionally #6 (non-passenger, pending reproduction) represent genuine, containable V2 work. #3 and #5 are already resolved. #1, #2, #4 are not application defects as currently scoped.** No code has been changed as part of this investigation — awaiting André/ChatGPT's direction on which of #6/#7 to actually build, and confirmation on #7's specific bounded-fix approach.

---

## RESOLUTION — Sep 7, 2026

Both open items resolved. **#7 (match-score) approved and shipped**: implemented exactly per the guardrails André set (continuous price-proximity scoring, modest gated Used-value tie-break, weights/labels/`penalizedByRelaxation` untouched), live-tested pre-merge (real 3-tier differentiation confirmed, $4,985-$42,149 spread), merged into `release/v2` (tip `ab617d2`), confirmed identical in production on both Claude and ChatGPT. **#6 (non-passenger vehicles) closed/deferred** by ChatGPT's own Sep 7 ruling — no concrete ATV/trailer reproduction exists, reopen only if a real example appears.

A separate, unrelated real bug (New/Used mislabeling in the host-facing text summary — not `structuredContent`, which already had the data) was found live while testing #7 and fixed too, same session (`SYS-20260907-002`).

**V2 backlog is now fully closed out** — nothing else pending from this investigation. Full detail: `DECISIONS.md` `SYS-20260907-003`, `STATUS_V2.4_MATCH_SCORE_IMPLEMENTATION_20260907.md`, `CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md`, `TESTING.md` Test Run Log.
