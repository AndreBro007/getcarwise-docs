# ENGINEERING_FEEDBACK_DECISION_JOURNEY_20260902.md

**Author:** Claude (engineering lane)
**In response to:** `DESIGN_SPEC_FIND_MY_CAR_DECISION_JOURNEY_AND_MONETIZATION_20260902.md`
**Status:** Engineering-informed design feedback and current-state audit, for ChatGPT/André alignment check. Not an implementation plan, not authorization to build — see gating note at the end.

---

## Purpose

This is Claude's response to the design brief ChatGPT and André produced the same day. It covers two things:

1. **Current-state audit** — what in the brief is already built in `carclever-find-my-car`, what exists only as unverified reference material from a different codebase (Fractal), and what doesn't exist at all.
2. **Sequencing feedback** — a recommended build order, reasoned from technical risk and dependency, not business priority (that call sits with André/ChatGPT).

---

## Current-state audit, per brief section

### Buyer Check
✅ **Done.** Live since Aug 24 (`lib/buyer-check.ts`), categorical outcome model, no numeric score, "unknown is never a concern" enforced in code. Matches the brief as written. Nothing needed here.

### Recalls
❌ **Not built.** No code in `carclever-find-my-car` calls any recall API today. No recall data exists anywhere in the app.
A full recall schema exists in `DECISIONS.md` (`DECISION-20260902-002`) but it describes a **different product's** (Fractal's) two-tier pipeline (Auto.dev VIN-specific → NHTSA model-level fallback) — reference material only, unverified even for Fractal itself, zero of it implemented here.

**Recommendation (per this session's discussion): go NHTSA-only, skip Auto.dev's recall endpoint entirely.** This codebase already has a solid, live, well-tested relationship with NHTSA via the existing vPIC VIN-decode call (`lib/nhtsa-client.ts`). Using NHTSA's recalls API avoids a new unverified dependency and avoids API cost. Trade-off: NHTSA recall data is model/year-level, not VIN-specific, so it can't always confirm a given VIN's remedy status — not a real problem, since the brief already defines "recall status needs verification" as a valid, honest output state.

### Affordability
❌ **Not built.** No loan-payment code exists in the repo.
A full methodology (amortization formula, credit-tier APR table, defaults, worked example, minimal output schema) exists in `DECISIONS.md` (`DECISION-20260902-001`), again borrowed from Fractal, unverified, zero implemented here.
**Assessment:** contained, low-risk build. Doesn't touch anything live. Good candidate for early, parallel work. Fractal's formula is a useful starting reference, not something to trust without building and testing against our own Auto.dev data.

### AI-driven comparison
❌ **Not built as specified.** `lib/match-score.ts` exists but is a fixed, deterministic numeric score — the brief explicitly wants adaptive AI reasoning over the full evidence set instead of a fixed table. No adaptive layer exists yet.
**Assessment:** smallest item, mostly prompt/output design rather than new library code, once Buyer Check + recalls + affordability data all exist to compare across. Should come last — building it before the underlying data exists means designing around placeholders.

### Tap-to-act
❌ **Not built.** No action row exists in `carclever-find-my-car` today.
A mechanism (position-label assignment, plain-text `sendFollowUpMessage()` resend carrying VIN/make/model/year/price inline) is documented as Fractal reference, unverified, zero implemented here.
**Assessment:** contained, low-risk, good to build early alongside affordability. Its practical usefulness is gated by Edmunds destination validation (below) — an action button pointing at an unvalidated or dead destination undermines trust the same way a dead listing link does.

### Edmunds destination resolution (listing, finance, trade-in)
🟡 **Partially built, and this is the highest-stakes item in the whole brief.**
Real code exists (`lib/edmunds-cj.ts`, `lib/link-resolution.ts`) that constructs a VIN-specific URL and a make/model/trim/year fallback URL, then immediately CJ-wraps both. This is genuinely good, well-documented work (extensive prior live-testing notes on trim-safety, the year+trim-never-combined rule, Carvana's 100%-dead VIN links, zip/price params being silently ignored on the category URL) — it should not be rebuilt, only extended.

**What's missing, and why it's urgent:** nothing in this path ever fetches a URL, follows a redirect, classifies the resulting page, or verifies VIN/vehicle identity before the link is shown to a user. A constructed URL is currently treated as a valid destination — precisely the failure mode the brief calls out (a year-form URL known to redirect to an editorial page). This touches a product that is **already live and under third-party review**, unlike every other item in this brief, which is why it should be first, not "one item on a list."

**Scope note (this session's discussion, confirmed in-brief, not an oversight on the first pass):** this isn't only about "View actual listing." The same validate-before-trust rule applies to two more destination types the brief also specifies:
- **Finance** — only worth surfacing as "Finance this vehicle" if Edmunds' finance page actually preserves the vehicle's price/details. If it can't, the brief's own fallback applies: a generic "Explore Edmunds payment options" label, not a false vehicle-specific claim.
- **Trade-in** — simplest of the three; expected to require additional user input regardless, so it only needs a working entry point, not vehicle-specific continuity.

**Recommendation:** design the fetch/classify/validate layer to handle all three destination shapes from the start (listing, finance, trade-in), rather than building it listing-only and retrofitting the other two later.

### Logging / later monetization
❌ **Not built.** No outbound-opportunity logging found anywhere in the repo (session/VIN/destination-tier/CJ-click record the brief asks for in Section F).

### Lean frontend contract
🟡 **Partially assessable.** Buyer Check's output shape already respects "compact card, full evidence in structured data." Can't meaningfully assess this for recalls/affordability/comparison/tap-to-act since none of them exist yet to check against.

---

## Recommended build sequence, and why

1. **Edmunds listing-destination validation, first.** The only item that touches a live, already-submitted product. Everything else here is new/additive and can't regress anything currently shipped; this one can. Fixing "constructed URL ≠ verified destination" is the brief's own stated critical rule.
2. **Recalls (NHTSA-only), affordability, and tap-to-act — in parallel.** All three are independent of each other, independent of the live product, and don't share a technical dependency that forces sequencing between them.
3. **Edmunds finance/trade-in validation, folded into the same validation-layer work from step 1** rather than treated as a separate later build — same mechanism, two more URL shapes.
4. **Comparison, last.** Depends on Buyer Check + recall + affordability data existing to compare across; building it earlier means designing around placeholder data.

---

## Open items / things not yet independently verified

- Fractal's affordability formula and tap-to-act mechanism (`DECISION-20260902-001`) and recall schema (`DECISION-20260902-002`) are **that project's own self-report**, not checked against real source code by anyone on this project. They're a fine starting reference; the real Auto.dev/NHTSA integration still needs to be built and tested against our own data, not assumed correct.
- No test call has yet been made to NHTSA's recalls endpoint from this codebase — worth a quick spike before sizing the recall work into a sprint, to confirm data coverage/quality for the vehicles this app actually surfaces.
- `lib/results-card.ts` (the largest file in `lib/`, ~38KB) has not been fully traced this session — worth a dedicated read before tap-to-act work begins, to confirm how/whether it already has partial action-row scaffolding.

---

## Gating reminder (per the original design brief's own guardrails)

This document is investigation and sequencing feedback only. Find My Car's merge freeze stays in place until André confirms review has concluded. No production behavior change is authorized by this document.
