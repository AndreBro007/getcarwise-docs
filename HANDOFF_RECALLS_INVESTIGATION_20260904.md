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
