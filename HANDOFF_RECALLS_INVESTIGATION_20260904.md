# Recalls Feature (V3, formerly "V2.3") — STATUS UPDATE Sep 6, 2026: Built, Shipped, Live-Tested — Real Regression Found, Decision Needed

**This handoff has moved past "investigation only" — the feature described below was built and shipped since this doc was last written. Read this update section first, the rest of the file below is the original Sep 4 investigation, kept as historical record.**

## Canonical version terminology (effective Sep 6, 2026 — supersedes this doc's own Sep 4 "V2.1/V2.2/V2.3" note below)

- **V1** = production `main`. Untouched.
- **V2** = `release/v2` branch (commit `e2ffe66`). Combines what this doc's Sep 4 note called "V2.1" (count-display fix) + "V2.2" (Edmunds CTA/link redesign) into one shipped release. No new tools.
- **V3** = `feature/v3-check-vehicle` branch (commit `719fc13`, branched from V2). **This is what this doc's Sep 4 note called "V2.3" — that label is retired.** Adds the `check_vehicle` tool described below.

Full canonical mapping (GitHub branch / Vercel project / connector name, for all three versions): top of `STATE.md`, `DECISIONS.md`, and every other admin doc in `carclever-widget`, plus `CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md` in the same repo.

## What actually got built (matches this doc's proposed design almost exactly)

`check_vehicle` shipped with the NHTSA-only mechanism this doc proposed, the 4-state model largely as proposed (none/severe/routine/unavailable), and Buyer Check integration exactly as described (own concern line for severe, `needsVerification` for routine/unavailable). Full source: `lib/nhtsa-recalls-client.ts`, `lib/buyer-check.ts`, `app/[transport]/route.ts` on branch `feature/v3-check-vehicle`.

## Real regression found, live-tested on both Claude and ChatGPT, decision still not made

`check_vehicle` is **text-only** — no listing/photo/link — so a VIN due-diligence question ("is this a good buy? any red flags?") that used to get a full one-shot answer (listing + link + Buyer Check, all from `find_matching_vehicle`'s old VIN path) now silently loses the listing/photo/link half of that answer, because it correctly routes to `check_vehicle` instead per that tool's own description. Confirmed cross-platform (Claude and ChatGPT both reproduce it identically) — this is a real design consequence of the four-tool split, not a host quirk or a bug in the recall logic itself. Full detail: `DECISIONS.md` `SYS-20260906-001`/`SYS-20260906-002`.

**Three options laid out, not yet decided — this needs ChatGPT's business/design call, not just an engineering fix:**
1. Give `check_vehicle` its own listing-resolution capability when a VIN produces one — restores the old one-shot experience, but blurs the tool's original lean/text-only design intent.
2. Leave as-is — the listing is retrievable via a natural follow-up, already confirmed working through `resolve_dealer_url`. Cheapest, but a real UX regression from before the split.
3. Narrow `check_vehicle`'s own tool description so it stops winning this specific phrasing ("is this a good buy? any red flags?") when a listing/link response would actually be preferred — pushes ambiguous due-diligence questions back toward `find_matching_vehicle`'s VIN path instead.

## New: a "risk reasons" field also shipped in V2, worth knowing before designing anything V3-adjacent

Not part of `check_vehicle` — this landed in **V2** (the NHTSA-trim-decode commit chain), but it's directly relevant to any future recall/risk-explanation design: `lib/risk-tier.ts` gained `explainRiskTier()`, a companion to the existing `classifyRiskTier()`, returning a `reasons: string[]` array (e.g. "VIN identity check failed...", "A reported accident or history issue is on file...") explaining *why* a card got an amber/red tier — not just the bare tier. Fully wired into the API output schema (`RiskSchema.reasons`) and used for every card `find_matching_vehicle` produces.

**Overlap with V3:** since V3 branches directly from V2's tip, `check_vehicle` inherits and uses the exact same `classifyRiskTier()`/`explainRiskTier()` functions for any card it resolves — this is shared code, not duplicated. What's genuinely new and separate in V3 is the recall-specific handling in `buildBuyerCheck()` (a different function, feeding `BuyerCheck.concerns`/`needsVerification`/`nextSteps`, not `RiskSchema.reasons`). Both follow the same underlying "explain the flag, don't just show a bare state" principle (`DECISION-20260902-008`), but they're sibling mechanisms feeding different output shapes, not competing or overlapping work — worth knowing as existing precedent if V3 planning extends further into risk-explanation design.

## Test/dev infrastructure now exists for both platforms (didn't exist Sep 4)

Permanent Vercel dev projects `ccfmc-dev-v2`/`ccfmc-dev-v3`, with matching ChatGPT and Claude connectors (`CarClever V2 Test`, `CarClever V3 Test`), all live-tested end-to-end as of Sep 6. Full setup, gotchas, and connector URLs: `CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md` (this repo). Full pass/fail test log for both platforms across all three versions: `TESTING.md`'s Test Run Log, in `carclever-find-my-car` (present on both `release/v2` and `feature/v3-check-vehicle` branches).

---

# Original Sep 4, 2026 investigation (historical — terminology below is superseded by the update above; content otherwise still accurate)

# Recalls Feature (V2.3) — Engineering Investigation, Ready for ChatGPT's Final Design/Spec Pass

Date: 2026-09-04
From: Claude / Engineering lane
To: ChatGPT / Business-Strategy lane
Status: Investigation only — no code written. Per the design brief's own process (`DESIGN_SPEC_FIND_MY_CAR_DECISION_JOURNEY_AND_MONETIZATION_20260902.md`), this is the "current-flow map, feasibility, and implementation sequence" deliverable for Section A (Buyer Check/recalls) specifically, so a final spec can be written before any build starts.

## Terminology note (locked this session)

**V1** = the submitted/production app (`main`), under Anthropic review, untouched. **V2** = everything since, numbered sequentially against actual app-submission versions: **V2.1** (count-display/domain fix), **V2.2** (Edmunds CTA/link redesign, just shipped), **V2.3** = this — recalls, the next scoped piece.

## What's already decided, not up for re-litigation

Checked `DECISIONS.md` before starting fresh — a decision already exists on the mechanism (`DECISION-20260902-007`, confirmed with Andre): **recalls go NHTSA-only, not Auto.dev's `/recalls/{vin}` endpoint.** Reasoning already recorded: `carclever-find-my-car` already has a live, tested NHTSA vPIC relationship (`lib/nhtsa-client.ts`), so this avoids a new unverified dependency and API cost. Accepted trade-off: NHTSA's recall data is **model/year-level, not VIN-specific**, so exact remedy status per individual VIN can't always be confirmed — already judged acceptable, since the design brief itself defines "recall status needs verification" as a valid, honest state rather than a gap to work around.

This investigation does not revisit that decision — it confirms feasibility against it and fills in what wasn't yet tested.

## Live-tested today, real data, real latency

**Endpoint:** `https://api.nhtsa.gov/recalls/recallsByVehicle?make={make}&model={model}&modelYear={year}` — public, no API key, no rate-limit wall encountered.

**Latency:** 308ms for a real query (2026 Ford Bronco), consistent with the existing NHTSA vPIC call already made per-shortlist-vehicle for electrification data (~350-500ms, per the field audit). Comparable added cost, nothing alarming.

**Real example response** (2026 Ford Bronco, live, current as of today):
```json
{
  "Count": 8,
  "results": [{
    "Manufacturer": "Ford Motor Company",
    "NHTSACampaignNumber": "25V788000",
    "parkIt": false,
    "parkOutSide": false,
    "overTheAirUpdate": false,
    "ReportReceivedDate": "14/11/2025",
    "Component": "ELECTRICAL SYSTEM: INSTRUMENT CLUSTER/PANEL",
    "Summary": "Ford Motor Company (Ford) is recalling certain 2025-2026 Bronco and Bronco Sport vehicles. The Instrument Panel Cluster (IPC) may fail at startup.",
    "Consequence": "An instrument panel display that does not show critical information...increases the risk of a crash.",
    "Remedy": "The instrument panel cluster software will be updated...free of charge...",
    "Notes": null,
    "ModelYear": "2026", "Make": "FORD", "Model": "BRONCO"
  }, ...]
}
```
This maps cleanly onto every field the design brief (Section A) and the earlier Fractal-derived schema (`DECISION-20260902-002`) both asked for: campaign ID, title/summary, component, defect/consequence, remedy, date, make/model/year. `parkIt`/`parkOutSide` (the two "stop driving immediately" severity flags) are present and usable exactly as Fractal's reference material described them.

**What this endpoint does NOT give us, confirmed:** VIN-level applicability or remedy-completion status — matches the already-accepted trade-off above, not a new finding.

## Tool-boundary decision (settled architecture)

Recalls are part of the **check_vehicle tool**, not find_matching_vehicle and not a new standalone recalls tool. For V1, check_vehicle owns the known VIN/listing Buyer Check and recall result. The normal search remains fast and should not perform recall lookups for every search result. If recalls cannot be retrieved, check_vehicle must still return the rest of the Buyer Check with an honest partial result and the recall state set to **“Recall status unavailable.”**

This follows settled architecture decision DECISION-20260902-008: four tools (find_matching_vehicle, check_vehicle, calculate_affordability, resolve_dealer_url), with comparison remaining AI-led and tap-to-act handled through natural-language follow-up prompts. Architecture is settled; implementation remains subject to the documented review, probe, regression, and approval gates.

## Proposed integration point (mirrors the existing NHTSA electrification call exactly)

Same stage as `decodeNhtsaElectrification()` — called on the final shortlist (5-8 vehicles) only, never the full candidate pool, so it can never thin out or delay the search itself. One genuine efficiency opportunity this endpoint's shape enables that the electrification call doesn't: **since this is make/model/year-keyed rather than VIN-keyed, multiple shortlisted vehicles sharing the same make/model/year (a common case — e.g. two same-trim listings from different dealers) only need one recall lookup, not one per vehicle.** Worth deduplicating before firing the calls.

## Mapping to the design brief's compact 4-state display (Section A), confirmed buildable as specified

- "No open recall signal found in available data" — NHTSA returned `Count: 0`, or all returned recalls are old/resolved (no per-recall completion flag exists in this API, so "resolved" can't be independently confirmed either — see the state below).
- "Open recall identified" — `Count > 0`, at least one with `parkIt` or `parkOutSide` true (a currently-serious one), or just any non-empty result if the brief wants all counts treated as "open" absent completion data.
- "Recall status unavailable" — the API call itself failed/timed out.
- "Recall status needs verification" — the honest default for the common case: recalls exist in the response but individual-VIN remedy completion can't be confirmed (this is where the model/year-vs-VIN trade-off surfaces to the user, framed honestly rather than hidden).

**Open question for ChatGPT's spec, not resolved here:** exactly which of "open recall identified" vs. "needs verification" should be the default when NHTSA returns 1+ recalls but none are flagged `parkIt`/`parkOutSide` — that's a business/tone call (how alarming should a routine, non-critical recall look by default?), not a technical one.

## Proposed test fixtures / regression cases

1. A real vehicle with zero recalls (`Count: 0`) → "no open recall signal found."
2. A real vehicle with a `parkIt`/`parkOutSide` recall (the Bronco example above, or find a cleaner park-it example) → "open recall identified," with the severity flags surfaced distinctly.
3. A real vehicle with only routine, non-severity-flagged recalls → tests the open-question boundary above.
4. API failure/timeout (mocked) → "recall status unavailable," fails open, never blocks the card the same way every other NHTSA-derived signal in this codebase already fails open.
5. Deduplication test: two shortlisted vehicles, same make/model/year → exactly one NHTSA recall call fired, both cards get the same (correct) result.

## Recommended sequencing (technical-risk basis only, business priority stays Andre/ChatGPT's call, per the already-recorded build sequence)

This slots into the already-recorded plan (`DECISION-20260902-007`): "Recalls (NHTSA-only) + affordability + tap-to-act, in parallel — independent, low-risk, additive." Nothing found in this investigation changes that — recalls remains low-risk and can proceed independently of the affordability/comparison work.

## What's needed back from ChatGPT before implementation starts

1. Final resolution on the open question above (default state when recalls exist but aren't severity-flagged).
2. Exact compact-display wording/format for the 4 states (the design brief gives the states, not the literal user-facing copy).
3. Confirmation this is the actual next priority, or whether affordability/tap-to-act should go first given they're already listed as "ready to build" from the original roadmap methodology-extraction work.

---

## Consolidated CarClever MCP To-Do List (compiled Sep 6, 2026 — Find My Car focus, individual items sourced from TASKS.md, cross-referenced here for ChatGPT's convenience)

### 🔴 Immediate open decisions (blocking or near-blocking)
1. **`check_vehicle` listing-loss regression** — see the 3 options above. This is the most direct thing for this ChatGPT session to resolve.
2. **V1 Anthropic review status** — still pending as of last check, confirm each session.
3. **Hybrid-result contamination** (`vehicle.fuel` unreliable, gas trims leak into hybrid-only searches) — root-caused, Option A (cheap, patch existing field) vs Option B (NHTSA `ElectrificationLevel`, stronger, Claude's own lean) — not decided. `DECISIONS.md` `SYS-20260817-027`.

### 🟡 Find My Car Roadmap (pre-existing prioritized list, `TASKS.md`)
| # | Item | Status |
|---|---|---|
| 1 | Re-test directory discoverability once approved | Pending approval |
| 2 | VIN-first risk/"Buyer Check" tool | Already live (categorical, not numeric — deliberately rejects Fractal's old numeric model) |
| 3 | Single hard-number affordability line (loan payment only, not full TCO) | Methodology extracted (`DECISION-20260902-001`), not yet built |
| 4 | AI-driven adaptive comparison (not a fixed table) | Design ready, not started |
| 5 | Tap-to-act button row (position-label A/B/C, re-send mechanism) | Mechanism confirmed (`DECISION-20260902-001`), not built |
| 6 | Cross-session persistence | Backlog, low priority |

### 🔴 Other known bugs/gaps, not started
- Result-count funnel display ("X indexed → Y matched → shown") — needs V2's count-fix as prerequisite (done)
- Link/Carfax/photo display consistency — real fix is a rendered UI card, not more prose tuning
- Match-score differentiation (identical `matchScore: 91` on structurally different vehicles) — scope question first, risks crossing into flagship's deal-scoring job. `SYS-032` (TASKS.md)
- Non-passenger vehicles (ATVs/trailers) appearing in unfiltered searches — data-scope characteristic, low priority (Finding B)
- VIN Buyer Check widget non-render — one observed instance, never reproduced (Finding C)
- CarMax retest (3/3 failures once, likely transient, unconfirmed)

### 🧹 Housekeeping / infra
- 18 stale merged branches on `carclever-widget` — safe bulk-delete, no urgency
- `AndreBro007/CarClever` (Codex-built, live at car-clever.vercel.app) — real keep/integrate/retire decision, not urgent
- WordPress page repointing once Find My Car is fully live (CarClever Guide, Try CarClever, Tools Hub, etc.) — see `AUDIT_WEBSITE_APP_INFRASTRUCTURE_20260826.md`
- Vercel MCP connector account-visibility bug (`list_projects` returns empty) — re-check each session, don't re-attempt project creation via it blind
