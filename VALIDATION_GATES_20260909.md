# V2 Validation Gates — Sep 9 2026 (post-commit 0e4a7cc / 134d931)

Doc-only additions except one required disclosure fix (Gate 3, commit `134d931`). No deploy, no resubmission, no V1/V3/production changes.

## Gate 1: Live NHTSA VIN validation

**Method:** real VINs sourced from live dealer/auction listings via web search, decoded directly against `https://vpic.nhtsa.dot.gov` (not the app, not a mock — the same public endpoint `lib/nhtsa-client.ts` calls), then run through the actual `classifyElectrification()` logic to confirm real-world agreement.

### BEV — CONFIRMED with real data
| VIN | Make/Model/Year | Raw `ElectrificationLevel` | Raw `FuelTypePrimary`/`Secondary` | Our classification |
|---|---|---|---|---|
| `5YJ3E1EA7NF153361` | TESLA Model 3 / 2022 | `"BEV (Battery Electric Vehicle)"` | `"Electric"` / `""` | `electric` ✅ |
| `5YJ3E1EA1NF144736` | TESLA Model 3 / 2022 | `"BEV (Battery Electric Vehicle)"` | `"Electric"` / `""` | `electric` ✅ |
| `5YJ3E1EB8NF171506` | TESLA Model 3 / 2022 | `"BEV (Battery Electric Vehicle)"` | `"Electric"` / `""` | `electric` ✅ |

Ran the actual classifier function against the first VIN's raw values: `classifyElectrification("BEV (Battery Electric Vehicle)", "")` → `"electric"`. **Real, live-confirmed.**

**Bonus, unplanned but useful:** also found and decoded 3 real Jeep Wrangler 4xe VINs — all three returned `ElectrificationLevel: "PHEV (Plug-in Hybrid Electric Vehicle)"`, `FuelTypePrimary: "Electric"`, `FuelTypeSecondary: "Gasoline"`, correctly classifying as `plug_in_hybrid`. Reinforces the existing PHEV corpus from `SYS-20260909-002`.

### Mild hybrid — ATTEMPTED, NOT CONFIRMED WITH REAL DATA
Real VINs from 4 different documented mild-hybrid vehicle lines were decoded live:
- Ram 1500 eTorque (WMI `1C6`) ×3 — `1C6RR7PT7GS154751`, `1C6RR7TM4GS186653`, `1C6RR7NM3JS354772`
- Mercedes-Benz E350 4MATIC (EQ Boost 48V mild hybrid, WMI `W1K`) ×4 — `W1KZF8EB7MA911883`, `W1KZF8DB0MA914691`, `W1KZF8EBXMA883142`, `W1KZF8DB5MA913472`
- Audi A6 45/55 TFSI (documented mild hybrid) ×5 — `WAUL2BF25NN046779`, `WAUL2BF20NN035379`, `WAUL2BF28NN022976`, `WAUL2BF25NN039430`, `WAUM2BF28NN030581`
- Hyundai Santa Fe Hybrid ×1 (full hybrid, not mild, decoded for corpus completeness) — `KM8S5DA16NU051118` → correctly `hybrid` (`ElectrificationLevel: "HEV (Hybrid Electric Vehicle) - Level Unknown"`)

**Result: all 12 mild-hybrid-candidate VINs returned a blank `ElectrificationLevel` (`""`) despite the vehicle being a documented, marketed mild hybrid.** This is a real, important finding, not a code defect — NHTSA's `ElectrificationLevel` field is manufacturer-self-reported and appears to be sparsely populated for mild-hybrid systems in practice, even though the vocabulary exists in NHTSA's schema. **Per the explicit instruction not to call synthetic fixtures real validation: the `mild_hybrid` branch of the classifier remains validated only against synthetic/documented-vocabulary test cases (`tests/nhtsa-classifier.test.ts`), not a confirmed live VIN.** This is a genuine open gap, not resolved by this pass, and should be flagged to André/ChatGPT as a real-world data-availability risk for the `mild_hybrid`→`hybrid` implication feature specifically (the code path may simply rarely fire in production, since real mild hybrids often decode as blank/`not_electrified`).

### Ambiguity case (blank level + secondary=Electric) — ATTEMPTED, NOT FOUND IN REAL DATA
Across all 19 real VINs decoded this session (12 mild-hybrid candidates + 3 BEV + 3 PHEV + 1 full hybrid), the blank-level-with-Electric-secondary contradiction pattern did not occur naturally — NHTSA's real data was internally consistent in every case (blank level paired with blank secondary, or populated level paired with a populated, consistent secondary). **This specific ambiguity case remains synthetic-only** (`tests/nhtsa-classifier.test.ts`'s `["", "Electric", "ambiguous", ...]` fixture). Not found despite reasonable real-world sampling effort — flagged, not fabricated as validated.

## Gate 2: V1/V2 equivalence run

**Method:** direct source diff between `release/v2` (pre-migration baseline) and the current branch tip, plus a real executed before/after comparison of `parseIntent()`.

### Search/routing/filtering/ranking/disclosure drift check
Diffed `app/[transport]/route.ts` line-by-line between `release/v2` and this branch. After excluding lines related to the intended scope (goals/vehicleNeeds rename, electrification fields, the lib extraction), grepped the remaining diff for core search-flow function names: `isConfirmedOutsideRadius`, `resolveSort`, `buildQualifierAccounting`, `detectDataConflicts`, `searchListingsLean`, `applyDiversity`, `verifyAgainstConstraints`, `WIDENING_TIME_BUDGET_MS`. **Zero unintended logic changes found** — the only 3 incidental mentions were doc-comments that moved along with the extracted `applyLocalBestForBudgetOrdering`/`applyLocalLowerRiskOrdering` function bodies, not logic changes to the functions they reference. City/ZIP/radius handling code is byte-identical to the V1 baseline.

### `vehicleNeeds` rename equivalence — real executed input/output
Ran the actual `parseIntent()` function from both versions with equivalent input:

**V1** (`goals` field): input `{"priceMax":35000,"goals":["family","reliability"]}` →
```json
{
  "hardConstraints": { "priceMax": 35000 },
  "semantic": { "seatsMin": 5, "goals": ["family", "reliability"] },
  "verificationRequired": ["seating", "identity"],
  "interpretationNotes": ["Goals (family, reliability) influence ranking only — Find My Car does not have reliability, ownership-cost, or history data on the Starter tier to verify these claims."],
  "modelPrefixesStripped": []
}
```

**V2** (`vehicleNeeds` field): input `{"priceMax":35000,"vehicleNeeds":["family","reliability"]}` →
```json
{
  "hardConstraints": { "priceMax": 35000 },
  "semantic": { "seatsMin": 5, "vehicleNeeds": ["family", "reliability"] },
  "verificationRequired": ["seating", "identity"],
  "interpretationNotes": ["Needs (family, reliability) influence ranking only — Find My Car does not have reliability, ownership-cost, or history data on the Starter tier to verify these claims."],
  "modelPrefixesStripped": []
}
```

**Result: structurally identical** — same `hardConstraints`, same `semantic.seatsMin` (5, from the same `GOAL_SEAT_HINTS["family"]` lookup, unchanged), same `verificationRequired`. The only differences are the intentional field rename and the approved wording change ("Goals" → "Needs" in the interpretation note) — not a behavior drift.

### Ambiguous-city handling
Not re-run live (no Auto.dev API credentials available in this session to execute an actual search). Equivalence evidence here is the source-diff proof above: the geo/ZIP/city verification code (`lib/geo-verification.ts`, `isConfirmedOutsideRadius`, the scope-note/widening logic in `route.ts`) shows zero diff lines between V1 and this branch. `tests/geo-verification.test.ts` (21/21 passing, unchanged from before this migration) already covers this path with its own fixtures and passed cleanly in every full-suite run this session.

### Searches without electrification/vehicleNeeds fields
Covered by the real functional test `"no electrification fields preserves existing behavior"` in `tests/electrification-preferred.test.ts` (passing) plus the full existing 287-check regression suite, none of which touches the new fields and all of which pass unchanged.

## Gate 3: Preferred-axis disclosure — DONE, commit `134d931`
`electrificationRequirement`'s field description in `lib/find-matching-vehicle-input.ts` now explicitly states: *"...currently only nudges ordering under the default (best_for_budget) and lower_risk priorityAxis values; it has no effect on cheapest, lowest_mileage, or newest, which always follow their exact stated sort regardless of electrification."* Verified via build+test (clean) and re-fetch/diff (exact match) before this report was written.

## Gate 4: Cutover plan

**Sequence, proposed (not yet executed — no deploy/resubmission has happened):**
1. André confirms final field set is locked (already done: `vehicleNeeds`, `electrificationTypes: hybrid|plug_in_hybrid|electric`, `electrificationRequirement: required|preferred`) — **complete**.
2. Claude's tool description/schema (this branch) is feature-complete and gate-validated as of this document — **complete pending live mild-hybrid/ambiguity data, which may never fully close per Gate 1's findings**.
3. ChatGPT prepares the equivalent OpenAI-side tool description/schema update in lockstep — using this exact field set, this exact enum, this exact "no goals" hard-cutover behavior. **Not yet confirmed done — coordinate before merge.**
4. Both descriptions are reviewed side-by-side (a text diff of the two tool descriptions/schemas) to confirm no drift between what Claude's host sees and what OpenAI's host sees for the same tool.
5. Merge `v2-implementation/schema-and-electrification` to `release/v2` (or equivalent production branch) **only after step 4 is confirmed** — not before, and not by one host alone.
6. Deploy to production.
7. Resubmit to OpenAI (if a separate resubmission step is required for their platform) **only after production deploy is confirmed stable**.

**Hard-cutover risk, explicit:** because `goals` is hard-rejected with no dual-acceptance period, any host (real end user integration, cached prompt, or the other AI platform if not perfectly in sync) that sends `goals` post-cutover gets an immediate schema error, not a degraded-but-working response. This is a deliberate tradeoff (silent-ignore was rejected by André as riskier — it could silently discard a user's stated needs) but it means **both platforms must cut over at effectively the same time** — a staggered rollout where one host still emits `goals` while the schema is already live would break that host's calls entirely, with no fallback.

**Status: gate 4 is a plan, not a completed action.** Actual coordinated execution with ChatGPT/OpenAI has not happened in this session and requires explicit confirmation from both sides before any merge/deploy/resubmit.

## Gate 5: Final verification

- JSON validation: PASS (`contracts/search_intent.schema.example.json`, `package.json`).
- Repo-wide search: `goals` — 9 matches, all intentional (retirement code/comments/test). `powertrains` — 0 matches. Public `electrificationTypes` enum confirmed `["hybrid", "plug_in_hybrid", "electric"]` only.
- Typecheck/build: clean (after the Gate 3 disclosure-fix commit).
- Full test suite: 287/287 passing (221 plain-assertion + 66 node:test), including the 28-check `tests/electrification-preferred.test.ts`.
- Every file changed this pass re-fetched from GitHub and diffed byte-for-byte against the local verified copy: match confirmed for `lib/find-matching-vehicle-input.ts` (commit `134d931`).
- **Not inferred from source inspection alone where a gate required a live/executed check:** Gate 1's BEV/PHEV confirmations and Gate 2's `vehicleNeeds` equivalence were both real executed runs against real data/real code, not source-reading.

## Explicit remaining blockers before deploy/resubmission

1. **Mild-hybrid live confirmation still open** — 12 real-world attempts across 4 manufacturers did not produce a populated `ElectrificationLevel` for any known mild hybrid. This may be a real, hard-to-close gap (manufacturer underreporting), not a code defect — needs an explicit decision from André/ChatGPT on whether to accept this residual risk or invest further in finding a real confirming VIN.
2. **Ambiguity case still synthetic-only** — not found in real data despite sampling 19 real VINs this session.
3. **Coordinated Claude/ChatGPT cutover (Gate 4) has not been executed**, only planned.
4. Standard remaining items from the feasibility package: full production A/B/equivalence test with live Auto.dev traffic (not available in this sandboxed session).
 

## Final release update — 2026-09-09

The amended V2 implementation was merged into `release/v2` at `5e8735e` and manually deployed because Git-connected deployment lagged. The current READY production deployment is release tip `a9d6439`, serving `https://ccfmc-dev-v2.vercel.app/mcp`.

Connector validation subsequently passed through both the ChatGPT and Claude V2 test apps, including practical model resolution, hybrid/PHEV required and preferred searches, mixed electrification types, exact VIN/risk flows, priority axes, legacy-`goals` behavior, and the five-result display cap.

The test suite was rerun after the final description and schema-path corrections: 222 custom checks plus 79 node tests, zero failures. The single TypeScript error in `tests/best-for-budget-ranking.test.ts:105:39` is pre-existing against the exact release baseline and remains separately flagged.

V1/Anthropic remains at `https://carclever-find-my-car.vercel.app/mcp` and was not changed. V3 preview deployments have historically received V2 branch pushes; this is an environment-isolation issue, not evidence that V3 production serves V2, and remains a separate operational cleanup item.