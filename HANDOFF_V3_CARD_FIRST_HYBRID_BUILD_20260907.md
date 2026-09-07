# HANDOFF_V3_CARD_FIRST_HYBRID_BUILD_20260907.md

**From:** ChatGPT Business/Strategy lane  
**To:** Claude Engineering lane  
**Status:** Proposed build handoff for tomorrow; V1 remains frozen and no production merge is authorized by this document.

## 1. Objective

Build V3 as a lean, capability-rich vehicle decision assistant.

The strategic goals are:
1. Improve AI discoverability by exposing separate tools for distinct buyer intents.
2. Help users throughout the vehicle-buying cycle.
3. Keep the listing card as the leading output.
4. Put AI explanation text after the card.
5. Allow tools to run standalone or as follow-ups from a selected listing.
6. Reuse existing code and payloads.
7. Avoid a major frontend rebuild or a rich dashboard.
8. Preserve listing click-through and dealer verification as the commercial/user outcome.

## 2. V3 tool portfolio

### 2.1 find_matching_vehicle

Use for discovery:
- find, show, search, recommend, locate, shortlist;
- natural-language constraints;
- “find this VIN and show me the listing”;
- “show me vehicles like this.”

It remains the normal entry point for unknown requirements and should remain fast. It should not perform recall checks across the full shortlist.

### 2.2 check_vehicle

Use for focused verification:
- recalls;
- red flags;
- Buyer Check;
- “is this a good buy?”;
- “would you buy this car?”;
- “what should I verify before buying?”

It must support:
1. Follow-up mode from an existing listing.
2. Standalone VIN mode.

It must not return text-only output when vehicle context is available.

### 2.3 resolve_dealer_url

Use for a known selected vehicle:
- open the listing;
- check availability;
- view the dealer destination;
- get the link for result A/B/C;
- view this vehicle;
- view similar vehicles.

It must preserve vehicle identity and must not trigger a new search.

## 3. Universal response contract

Every vehicle tool response should be ordered:

1. Renderable vehicle card or vehicle-context card.
2. Short AI-readable text summary.
3. One to three relevant next actions.

The card is the primary product surface. AI prose explains the card and should not replace it.

## 4. Shared vehicle context

Reuse the smallest existing common context possible. Carry, when available:
- VIN;
- year, make, model, trim;
- price and mileage;
- New/Used/CPO condition;
- image;
- listing/dealer/Carfax references;
- match and A/B/C position labels;
- search/session identifier;
- existing destination/action metadata;
- relevant user constraints and priority axis.

Unknown fields remain unknown. A downstream tool must not silently substitute another vehicle.

## 5. check_vehicle follow-up mode

When a user asks “check result A for recalls/red flags”:

1. Host passes the selected VIN and available context.
2. check_vehicle returns the same vehicle.
3. Existing listing card remains the leading card.
4. Card adds compact Buyer Check and/or recall state.
5. Every displayed Risk/Recall label includes a reason in structured output.
6. AI text follows with one or two useful lines.
7. Listing and verification actions remain available.

The current text-only risk behavior must be corrected through response/card integration, not by removing useful trigger language.

## 6. Standalone VIN mode

When the user supplies only a VIN:

1. Show a minimal identity/verification card.
2. Show identity fields when available.
3. Show Buyer Check and/or recall state.
4. State honestly when no exact listing is available.
5. Add close/narrow “Check avail.” using the New-vehicle-style destination pattern.
6. Add loose “View similar” using the broader fallback pattern.
7. Put AI explanation after the card.
8. Do not claim an exact listing is live unless verified.
9. Do not require live Edmunds search.
10. Do not invent listing details.

## 7. Risk and recall presentation

Keep risk/recall additions compact:
- categorical Buyer Check state;
- recall state;
- one short reason or caveat;
- primary listing action;
- at most one secondary action.

For every visible risk label, provide the AI:
1. Label/state.
2. Colour/state meaning.
3. Actual reason.
4. Evidence status.
5. Recommended verification action.

Use calm language:
- “Worth verifying with the dealer.”
- “Ask for service or repair documentation.”
- “The available data shows a possible issue; confirm before buying.”
- “No negative signal found in the available data, but this is not a mechanical guarantee.”

Never turn unknown into a positive or negative finding.

## 8. Dynamic labels

Use one shared lean card with tool- and intent-dependent optional fields.

Normal maximum: two or three badges.

Priority order:
1. Match/value signal.
2. New/Used/CPO condition.
3. Risk/Recall when relevant.
4. Mileage or price-drop signal when reliable.
5. Ownership/history detail.

Potential labels:
- Strong match;
- Good value;
- Used value;
- Certified;
- Low mileage;
- New;
- Used;
- Risk;
- Recall;
- Price drop, only when reliable.

Do not make “1 owner” or “no accidents” default labels yet. Use them only when explicitly verified and relevant to the user’s request. Prefer “No reported accidents” rather than “Accident-free.” Otherwise provide the evidence to the AI for explanation/comparison.

## 9. Intent-driven comparison

Comparison must be driven by:
1. User goal.
2. Entered constraints.
3. Priority language.
4. Available data.
5. Buying-cycle stage.

Relevant dimensions may include:
- fit to requirements;
- price position within budget;
- New versus Used value;
- trim/equipment advantage;
- mileage relative to age;
- risk and recall signals;
- history unknowns;
- estimated payment;
- listing/link confidence;
- important trade-offs.

The output should not be a generic large table. Prefer:
1. Best fit or winner.
2. Alternative winner on another dimension, if useful.
3. Two or three material trade-offs.
4. One verification step.
5. Listing action for every compared vehicle.

Examples:
- Family request → practicality, space, fit, value, relevant risk evidence.
- Best deal → price position, condition, mileage, match quality, risk.
- Best nearly-new → Used/CPO, low mileage, trim, price, history completeness.
- Lowest payment → price, payment assumptions, term, APR.

## 10. Action continuity

Follow the buying cycle:
1. Discover vehicles.
2. Inspect the shortlist.
3. Check a known vehicle.
4. Compare shortlisted options.
5. Estimate affordability.
6. Open the listing.
7. Verify with the dealer.

The current V3 build should focus first on discovery, verification, and listing continuity. Affordability and comparison follow only after the card-first contract is stable.

## 11. Phased implementation

### V3.1 — Shared card-first contract
Map existing payloads and establish the minimum shared vehicle context. Do not alter normal search-card behavior.

### V3.2 — Card-first check_vehicle
Preserve the selected listing card during risk/recall follow-ups. Add compact state and reason-bearing labels. Keep AI prose after the card.

### V3.3 — Standalone VIN actions
Implement identity/verification card behavior and New-style close/narrow Check avail. plus loose View similar actions.

### V3.4 — Intent-driven labels/actions
Select optional badges and actions based on tool and user intent. Keep cards to two or three badges.

### V3.5 — AI-driven comparison
Use full structured evidence but return concise, intent-specific conclusions and trade-offs.

### V3.6 — Affordability action
Add a single monthly payment estimate with assumptions, without building a full finance dashboard.

## 12. Build safety

Before each phase:
1. Work on a named V3 branch.
2. Do not modify V1/main.
3. Do not merge without André’s explicit approval.
4. Preserve existing search, link, and card behavior.
5. Add deterministic fixtures before broad live testing.
6. Test raw structured payload and rendered card separately.
7. Test Claude and ChatGPT where routing/rendering is relevant.
8. Re-run the full existing suite after every phase.
9. Verify that unknown, unavailable, and conflicting data remain honest.
10. Record the exact commit, deployment, connector, and test surface.

## 13. Submission strategy

Use incremental private build phases, but do not submit half-finished versions.

Recommended:
1. Build and test V3.1–V3.3 privately.
2. Stabilize the three-tool card-first experience.
3. Add V3.4 only after the core response contract is reliable.
4. Add comparison and affordability only when each complete flow is independently tested.
5. Submit one coherent V3 release containing only complete, tested tools and workflows.
6. Treat later tool/metadata changes as a new reviewed version where the platform requires it.

OpenAI guidance requires complete testing of the MCP server, tools, and optional UI before submission, and published MCP metadata is based on reviewed snapshots. Claude’s reviewed connectors likewise use remote MCP infrastructure. The public V3 submission should therefore be a stable bundle, not a moving development branch.

## 14. Acceptance tests

### Search-first
- Find a used SUV under $30,000 near 90210.
- Check result A for recalls and red flags.
- Open the listing for result A.
- Ask about the cheaper one.

### Standalone
- Check a valid VIN for recalls.
- Is this VIN a good buy?
- Check a valid VIN with no listing.
- Confirm close/narrow Check avail. and loose View similar.

### Boundary
- Find this VIN and show me the listing → search.
- Find this VIN and tell me if it has recalls → check.
- Show me cars like this VIN → search.
- Get the link for result B → resolve.

### Failure
- Invalid VIN.
- NHTSA unavailable.
- Missing image.
- Missing link.
- Ambiguous “check this car.”
- Ambiguous “open it.”
- Follow-up referring to “the cheaper one.”

Expected:
1. Correct tool selection.
2. Stable vehicle identity.
3. Card-first output.
4. AI explanation after card.
5. Reason-bearing labels.
6. Honest unknown states.
7. Relevant actions remain available.

## 15. Tomorrow’s starting assignment

Start with V3.1–V3.3 only:
1. Map the existing payload/card structures.
2. Identify reusable context fields.
3. Design the smallest check_vehicle card-first response.
4. Add standalone VIN actions.
5. Preserve current search and resolve_dealer_url behavior.
6. Return an affected-file map, proposed contract, risk assessment, and test plan before broad implementation.

No comparison, affordability, or major UI redesign should begin until the core card-first hybrid flow is proven.
