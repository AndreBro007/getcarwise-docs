# CarClever MCP Connector Analysis & Monetization-Aware Roadmap

### Comparing "CarClever – New & Used Cars" vs "CarClever – Find My Car" as Claude connectors, plus a monetization-aware roadmap

This review is based on live behavior observed across a working session: what got found via search_mcp_registry, what got loaded via tool_search, how each tool's schema is written, what came back in tool results, and — added in this revision — how each connector's *rendered UI* behaves once real screenshots were reviewed. It's an assessment of these connectors as MCP surfaces for an LLM and its UI layer to reason over and render, not a general code review.

**v2 changes:** incorporates the "Find My Car" connector's actual business model (drive clicks to dealer listings, don't replicate the listing/Carfax content in Claude), corrects several v1 recommendations that would have undermined that model, and adds a dedicated strategy section on how tool design should serve monetization rather than compete with it.

## 1. Evaluation criteria (why these, specifically for MCP)

Unlike a human browsing an app store, Claude never "sees" a UI on its own — but its *host surface* (the MCP App widget) can render one, and that widget is itself part of the product. So the criteria here span both the model-facing contract and the human-facing render:

1. **Directory discoverability** — does search_mcp_registry surface the connector on natural-language keywords, not just its exact name? (Caveat, addressed in §2: a connector still under review may reasonably not appear yet — this isn't necessarily a defect.)
2. **Tool-level discoverability** — once in scope, does tool_search match the connector's tools to the user's phrasing?
3. **Schema/prompt engineering quality** — does the tool description teach Claude how to decompose a fuzzy request ("large SUV," "reliable teen car") into correct structured parameters, including edge cases?
4. **Output design for LLM consumption** — is the tool result something Claude can summarize cleanly, or does it leak internal implementation detail / fight Claude's own formatting instincts?
5. **Reliability** — do calls actually succeed against their own declared schema?
6. **Functional depth vs. business-model fit** — how much of the buyer's decision journey does the connector cover, *and does covering more of it help or cannibalize the actual monetization event* (the dealer click-through)? This is the criterion most revised in this version.
7. **UI/UX render quality** — does the widget teach users the interaction model (labels, buttons) without requiring memorized commands?
8. **Consistency of trust/opt-in tagging** — are tools correctly marked [third_party_mcp_app], and are write-actions (save/persist) held to a confirm-before-acting standard regardless of tagging?

## 2. Connector A: "CarClever – New & Used Cars"

**Tools:** search-vehicles-for-sale, analyze-deal-risk, calculate-affordability, vehicle-comparison, garage-save, garage-list

### What stood out (good)

- **Full-journey coverage.** Only this connector can do 5-year TCO math, structured deal-risk gating, and remember a saved vehicle across turns via garage-save/garage-list.
- **Excellent slot-filling rules** on search-vehicles-for-sale — 14 numbered rules for size-class → model-list translation, hybrid/PHEV mistagging workarounds, and proxy translations ("reliable," "luxury"). Best-in-class prompt engineering for turning fuzzy requests into structured filters.
- **Active output steering.** Tool results embed a literal CRITICAL INSTRUCTION directive controlling Claude's summary length — a deliberate technique, and it worked.
- **The rendered detail view (Images 4-5) is a genuinely well-built decision-support screen** — tabbed Vehicle Info/Details, a reasoned Deal Score Breakdown (+21 Budget Fit, +17 Age, +22 Mileage, +16 Market Value, +13 Reliability), inline NHTSA recall text, a 69-photo carousel, and a "NEXT STEPS" button row (Risk A, Safe To Buy A, Cost A, Ownership Cost A, Save A, View Garage, What Else Can I Check?) that solves the exact "how does a user discover they can type Risk A" problem flagged in v1 — it's already solved here.

### What stood out (weak)

- **vehicle-comparison is broken** — failed twice in this session with an output-validation error, with and without search_id.
- **Diagnostic leakage** in search results (phase=diversity, DIAG: pool=707..., emv_basis=insufficient_comparables) — implementation detail bleeding into the model-facing contract.
- **Inconsistent opt-in tagging** — garage-save/garage-list aren't tagged [third_party_mcp_app] while the other four tools are.
- **The monetization risk, now visible in the UI:** the detail screen in Images 4-5 is thorough enough that a user could get everything they need and never click "Check Avail." The connector's own decision-support surface competes with its own paid link. This wasn't visible from the tool schema alone — it only became clear once the rendered card was reviewed.

### Rating: 7.0 / 10

Deepest functionality, best risk/afford/persistence coverage, but a broken comparison tool and a UI that arguably over-serves the user at the expense of the click-through that actually generates revenue. (Lowered slightly from v1 once the business-model tension became visible.)

## 3. Connector B: "CarClever" (submitted as "CarClever – Find My Car," pending directory review)

**Tools:** find_matching_vehicle, resolve_dealer_url

### What stood out (good)

- **One tool covers search, VIN lookup, and an inline Buyer Check** in a single call — no second tool needed for a basic risk read.
- **priorityAxis is a clean, well-designed abstraction** (best_for_budget vs cheapest vs lowest_mileage vs newest vs lower_risk), with an explicit guard against the common LLM mistake of treating "budget" as a signal for "cheapest."
- **Best-in-class location handling** — ambiguous city disambiguation, state-only search, nationwide fallback, disclosed auto-widening.
- **The rendered card (Image 6) is deliberately thin, and this is the correct design, not a gap** — one strong-match badge, price/mileage/location/VIN, a Carfax link, and two outbound buttons ("View listing," "View similar"). Nothing invites the user to linger; everything invites a click-through. Given the stated business model (drive engagement to the dealer listing, since that's where the money is), this is the right shape and shouldn't be "fixed" toward Connector A's richer card.
- **Zero errors observed** in this session, including the VIN-specific Buyer Check path.
- **Strict, well-reasoned link/monetization contract** — mandatory Edmunds affiliate link as primary, distinctly labeled fallback, embedded top-result image, explicit rule never to substitute a raw dealer URL (including for Carvana listings).

### What stood out (weak)

- **No persistence, no dedicated financial tooling, no comparison tool** — real gaps in the buyer's next-step journey, addressed in the roadmap below with monetization-safe designs (not straight ports of Connector A's versions).
- **No button row yet.** The card links out, but doesn't yet offer the tappable "Risk A / Cost A / Save A" pattern Connector A has already proven works.
- **Naming/registry status.** "CarClever – Find My Car" wasn't found by search_mcp_registry under any phrasing tried — most likely explained by the submission still being under review rather than a metadata problem (see §4 below). Worth re-testing once approved.

### Rating: 7.6 / 10

Narrower scope, but a UI and link discipline that are already correctly aligned with the business model — the harder thing to retrofit, and the thing Connector A would need to walk back, not add.

## 4. On discoverability and the "under review" explanation

If this is a custom connector with a submission still pending, its absence from search_mcp_registry results is expected, not a metadata defect — that registry most plausibly indexes approved/live entries only. This changes the diagnosis but not the eventual test: once approved, re-run the same keyword searches ("SUV," "used car," "find a car," "car near me"). If it still doesn't surface on generic terms at that point, that's the moment to treat it as a real optimization task — tightening the top-level name/description to match how buyers actually phrase requests, and resolving the "CarClever" vs "CarClever – Find My Car" naming gap so the name intended and the name that's indexed are the same string.

## 5. Side-by-side

| Dimension | New & Used Cars | Find My Car |
|---|---|---|
| Directory discoverability | Not observed (likely pending review) | Not observed (likely pending review) |
| Tool-level discoverability | Good | Good |
| Search schema sophistication | Excellent | Excellent, arguably more edge-case coverage |
| Risk/history assessment | Dedicated tool, but UI over-discloses | Folded into search/VIN lookup, thinner |
| Affordability/TCO | Full 5-yr breakdown (false-precision risk) | None yet |
| Comparison | Dedicated tool — broken | None yet |
| Persistence | Yes, cross-turn only | None |
| Location edge cases | Zip-centric | Ambiguity, state-only, nationwide, widening |
| Detail-card design | Rich, replicates the listing | Thin, drives outbound clicks |
| Button-row / tap-to-act UX | Yes, already solved | Not yet present |
| Link/monetization discipline | Present, looser | Strict, explicit |
| Reliability observed | One tool errored twice | No errors observed |
| Fit with a click-through business model | Tension — own UI competes with the CTA | Aligned by design |

## 6. Design philosophy: build tools that create reasons to click, not reasons to stay

This is the organizing principle that should govern every future addition to Find My Car:

**A tool's job is to supply just enough decision-relevant signal to make clicking through feel safe and worthwhile — never enough to substitute for the listing or the Carfax report itself.**

Concretely, that means for every new tool:

- **End every result with a live link back to the listing** — not just on the initial search result, but on every downstream tool's output too (risk check, comparison, affordability). Right now that discipline exists at the search step; nothing downstream exists yet to test whether it survives as more tools get added. Write it into the tool-output contract now, as a shared rule, rather than leaving each future tool author to remember it independently.
- **Prefer one strong verdict line over a breakdown table.** Connector A's Deal Score Breakdown (five reasoned line items) is well-built, but it's also the thing most likely to let a user feel "done" without clicking. A single sentence ("Strong deal — priced under market, no reported accidents") carries most of the same confidence with much less surface area to linger on.
- **Never reproduce what the Carfax report or listing page already shows.** Recall status, full history, and detailed spec sheets belong one click away, not rebuilt inline.
- **Measure new tools by click-through rate, not just usage rate.** A risk or compare tool that gets called often but reduces clicks to listings is a net negative for the business model even though it looks like a successful feature from a usage dashboard.

## 7. Priority roadmap for enhancing "Find My Car"

Ranked by expected impact on (a) getting invoked more often, and (b) usefulness once invoked, with the monetization principle above applied to each item.

**1. Re-test directory discoverability once the submission clears review.** If it still doesn't surface on generic buyer phrasing after approval, tighten the registry name/description then — not before.

**2. Add a thin risk/"Buyer Check" tool, VIN-first.** Accept a VIN alone as sufficient input rather than requiring make/model/year/price re-entry. Return one verdict line, 1-2 concrete flags, and end with the listing link and Carfax link — not a breakdown tab. **STATUS: Already live via buyer-check.ts + risk-tier.ts (shipped Aug 24) — see §10 for the critical build-order correction.**

**3. Add a single hard-number affordability line — not a full TCO tool.** Loan payment from price + APR + term + down payment is real, deterministic math — safe to state as a number. Anything beyond that (insurance, fuel, maintenance, resale) should stay a disclosed range in at most one extra line, not a compounded 5-year total. **STATUS: Methodology extracted, ready to build — see §8.**

**4. Add an AI-driven comparison, not a fixed-schema table tool.** Keep the tool itself thin: given labels or VINs, resolve and return each vehicle's full available data with no formatting or fixed-row logic. Let Claude build the actual comparison adaptively.

**5. Add the tap-to-act button row — proven pattern, straightforward to adopt.** Per-vehicle buttons (Risk A, Cost A, Save A) and a "next steps" row after search results. **STATUS: Mechanism confirmed — see §8.**

**6. [DROPPED — see §9]**

**7. Apply the link/output contract from Find My Car to every new tool, not the reverse.** As items 2-5 get built, they should inherit Find My Car's existing discipline (mandatory affiliate link, distinctly labeled fallback, never a raw dealer URL) rather than drifting toward Connector A's looser pattern.

**8. Decide write-action confirmation policy before building persistence.** A write action generally warrants an explicit confirm-before-acting step, the same way sending an email or deleting a file does.

*Caveat: this assessment is based on one session's worth of observed tool-call behavior, rendered screenshots, and the schemas as currently written — not exhaustive testing, and not visibility into either connector's backend implementation, registry review status, or actual click-through/revenue data.*

## 8. Update — Fractal Extraction (Sep 2, 2026): Items #3 and #5 resolved

Item #3 (affordability) methodology extracted from Fractal's own calculate-affordability implementation. Monthly loan payment is deterministic math (standard amortization: price + APR + term + down payment), requiring zero Auto.dev calls. Fractal uses a single authoritative credit-tier APR table (not the real per-VIN APR lookup, which is fetched but deliberately unused, kept as reference metadata only) — this keeps displayed numbers internally consistent. Worked example: 2021 Honda CR-V, $27,500, good credit -> ~$549/mo at 7.4% APR, 60mo, 10% down. Fractal's own limitations guidance independently confirms this document's original recommendation in §7 item 3: show loan payment only, never an inline insurance/fuel/maintenance range, because a wrong-for-most-users range erodes trust faster than omitting it.

Item #5 (button row) — the one open blocker is now resolved. Position labels (A/B/C...) are assigned by sorting results by deal score descending (highest = A), with a VIN-pin exception when a searched VIN takes label A. The firing mechanism is a plain-text follow-up message re-send (not a structured callback) with VIN/make/model/year/price embedded directly in the text, e.g. "Call calculate-affordability for A [VIN:... make:... model:... year:...]". Find My Car's own button row should replicate this same mechanism.

Full response text and the GitHub-side task log for both live in DECISIONS.md (DECISION-20260902-001) and TASKS.md in the carclever-widget repo.

## 9. Item #6 dropped — new monetization gap identified

Item #6 (cross-session persistence) — dropped per André's decision (Sep 1-2 session). Standing principle going forward for all roadmap items: lean frontend, leverage AI over fixed schema, adapt to user intent, and drive to dealer-listing click-through as fast as possible.

New gap identified, not in the original roadmap — non-Edmunds dealer-link fallback. When a matched vehicle has no Edmunds affiliate listing, there is currently no defined behavior. This is a real hole in the monetization funnel: a result with no monetizable link is a dead end. Needs scoping: whether a live per-result existence check is feasible without hurting latency/quota, and what to do when a vehicle isn't listed (labeled non-affiliate fallback link, suppress the result, or flag differently in the UI). Not yet scoped or built.

Source: two Fractal code-agent prompts run in parallel Sep 1-2 (one in the "CarClever - New & Used Cars" project for this affordability/button extraction, one in the original "CarClever" project investigating the Claude iOS rendering blocker).

## 10. Recovered Aug 31 Fractal Exchange (Item #2 full detail, never persisted until now)

A separate Aug 31 Fractal exchange (different chat session, discovered via a handoff document on Sep 2) produced a full extraction of analyze-deal-risk (Item #2) that was never persisted anywhere until now. Recorded in full in DECISIONS.md DECISION-20260902-002. See that entry for the complete output schema and Auto.dev field mappings.

Critical build-order correction, most important part of this update: Find My Car does NOT need this numeric risk model built. It already has its own, deliberately different, live categorical system (buyer-check.ts + risk-tier.ts, shipped Aug 24) that explicitly rejects numeric scoring and unverified titleStatus — a considered design choice, not a gap. This full extraction is reference-only, in case a specific piece (repair-reserve dollar amounts, the recall two-tier VIN-specific-then-model-level pipeline) is worth borrowing later. Do not treat "Item #2 methodology fully extracted" as "Item #2 needs building against this schema."

Worked example (2016 Honda Accord, 95,000mi, VIN provided, title_status unconfirmed, 1 recall): Start 85 -> title unverified forces gate GREEN to YELLOW (no score change) -> 1 recall -5 (80) -> mileage 95k tier -10 (70) -> age 10yr -5 (65) -> usage rate normal, no change (65) -> final score 65, "Moderate", gate YELLOW. A flag can only downgrade the gate, never upgrade it back to GREEN.

Only three genuinely open Fractal questions remain across both exchanges: (1) what raw data/signals feed the hardcoded make/model risk items, since Find My Car wants to hand the AI the evidence rather than hardcode a table; (2) whether the payments endpoint loan-term bug found independently on Aug 11 (36/60/84mo all returning a fixed 72mo calc) is still present on Fractal's side, low priority since client-side amortization is used regardless; (3) BEV affordability fallback behavior when /tco/{vin} returns RESOURCE_NOT_FOUND, low priority. Draft prompt for these three: NEXT_FRACTAL_PROMPT_THIRD_ROUND.md in the carclever-widget GitHub repo.

## 11. Migration note (Sep 2, 2026)

This document was originally a Google Doc (`carclever-connector-analysis.md`, Drive file ID `1gag-E3acUgt4lCejLhyK229d34y3oJe184QcMpPUsX4`), maintained as a deliberate exception to the GitHub-is-primary architecture from Aug 30 to Sep 2. Migrated into `getcarwise-docs` once that repo's naming convention and dynamic-fetch mechanism made the exception no longer worth maintaining — see `DECISIONS.md WORKFLOW-20260902-002` and `ARCHIVE_INDEX.md` for the full reasoning. The original Drive doc is archived, not deleted, with a pointer back here.
