# DESIGN_V3_HYBRID_TOOL_INTEGRATION_AND_CARD_FIRST_20260907.md

**Status:** Proposed V3 product and architecture design for Claude engineering review. No implementation authorization yet.

## Executive goal

V3 should expand CarClever beyond a listing app without becoming a heavy dashboard.

The strategy is:
- keep the listing card as the leading output;
- expose separate, semantically distinct tools so AI hosts can discover and invoke additional capabilities;
- allow every tool to run standalone or as a follow-up from a selected listing;
- reuse the existing search, card, VIN, Buyer Check, recall, and dealer-link machinery;
- keep detailed evidence in structured output and concise interpretation in AI text.

## Core UX rule

Every vehicle-related tool response should follow this order:

1. Renderable vehicle card or vehicle-context card.
2. Short AI-readable text summary.
3. One to three context-appropriate next actions.

The card is the anchor. AI prose explains the card; it must not replace it.

For a search, use the existing lean listing card. For a follow-up risk or recall check, preserve the same vehicle card and add a compact risk/recall state. For a standalone VIN check with no listing available, use a minimal identity/verification card and state clearly that listing data is unavailable.

## Hybrid integration model

Use a shared vehicle-context envelope across the tools. This is the minimum common shape needed for composability, not a new large orchestration layer.

Carry, when available:
- VIN;
- year, make, model, trim;
- price and mileage;
- New/Used/CPO condition;
- image;
- existing listing, dealer, and Carfax references;
- match and position labels such as A/B/C;
- search/session identifier where already available;
- existing action metadata;
- relevant user constraints and priority axis.

Unknown fields remain unknown. A downstream tool must never silently replace the selected vehicle.

### Follow-up from listings

When the host AI has a selected result:
- check_vehicle accepts the VIN and available vehicle context;
- it returns that same vehicle as the leading card;
- the card adds a compact Buyer Check/recall state;
- the AI text explains the result in one or two useful lines;
- listing and verification actions remain available.

resolve_dealer_url remains the action/destination tool and must not trigger a new search.

### Standalone use

When the user supplies only a VIN:
- check_vehicle runs independently;
- it returns identity and recall/Buyer Check evidence;
- if listing context cannot be recovered cheaply and reliably, it must say so;
- it uses a minimal vehicle-context card and offers a clearly labelled route to find a listing;
- find_matching_vehicle can then be called if the user asks to locate that vehicle or comparable listings.

When the user supplies natural-language constraints, find_matching_vehicle remains the entry point.

When the user asks only for a link, resolve_dealer_url runs on selected vehicle context. If no selected vehicle exists, the host should ask which vehicle the user means.

## Tool responsibilities

### find_matching_vehicle

Discovery and listing-card tool. Use for find, show, search, recommend, locate, shortlist, natural-language constraints, or “find this VIN and show me the listing.”

### check_vehicle

Focused verification tool. Use for recalls, red flags, Buyer Check, “is this a good buy?”, and “what should I verify before buying?”

Its description should explicitly support follow-up mode and standalone VIN mode. Its output must be card-first: existing listing card when context exists, minimal identity/verification card otherwise. It must not become text-only.

### resolve_dealer_url

Selected-vehicle action tool. Use for open the listing, check availability, view the dealer destination, or get the link for result A/B/C. It is not a general search or verification tool.

## Routing boundaries

Descriptions should state both positive triggers and boundaries:

- Search finds candidates and supplies listing context.
- Check verifies a known vehicle and preserves context when available.
- Resolve supplies an action destination for a known selected vehicle.

Assign ownership by object:
- unknown requirements: search;
- known VIN or selected result plus risk/recalls: check;
- known selected result plus link/action: resolve.

The “is this a good buy?” regression is best handled by making check_vehicle preserve the listing card when context is passed, not by removing the useful trigger language.

## Lean card design

Do not create a new rich risk dashboard.

The card should remain:
- identity;
- price, mileage, and location;
- condition;
- image;
- match/risk or recall state;
- one primary listing action;
- at most one or two secondary actions.

Risk/recall additions should be compact: categorical Buyer Check state, recall state, one short reason or caveat. Do not expose raw campaigns, provider fields, numeric scores, or long history by default. Keep full evidence in structured output.

## Reuse and implementation shape

Reuse the existing result-card renderer, VIN identity fields, Buyer Check/risk-tier logic, NHTSA recall result, deterministic Edmunds-link resolution, and position-label/follow-up conventions.

The likely work is contract and response-envelope alignment, not a new frontend or general orchestration engine. A shared internal formatter is acceptable if it reduces drift.

## Test matrix

Test Claude and ChatGPT, explicitly attaching the connector on ChatGPT.

Search-first:
- Find a used SUV under $30,000 near 90210.
- Follow up: check result A for recalls and red flags.
- Follow up: open the listing for result A.
- Follow up: what about the cheaper one?

Standalone:
- Check a valid VIN for recalls.
- Is this VIN a good buy?
- Any red flags with this vehicle?

Boundary tests:
- Find this VIN and show me the listing -> search/listing card.
- Find this VIN and tell me if it has recalls -> check/verification card.
- Show me cars like this VIN -> search.
- Get me the link for result B -> resolve action.

Failure tests:
- invalid VIN;
- valid VIN with no listing;
- NHTSA unavailable;
- missing image or link;
- ambiguous “check this car” follow-up.

Expected in every case: stable vehicle identity, card-first output where possible, honest unknown states, and no invented listing.

## Success criteria

V3 succeeds if additional tools are invoked for intended buyer intents, check_vehicle never degrades into text-only output when context exists, standalone checks remain useful, follow-ups preserve the selected vehicle, cards remain lean and action-oriented, and AI text adds interpretation instead of duplicating the card.

## Engineering handoff

1. Map existing response and card payloads for all three tools.
2. Identify the smallest shared vehicle-context fields already available.
3. Implement card-first output for check_vehicle while preserving standalone VIN behavior.
4. Verify action and link continuity through resolve_dealer_url.
5. Run the cross-platform matrix before adding affordability, comparison, or more tools.

The tools remain separate for invocation and capability discovery, but share a card-first vehicle-context contract.


## André clarification — standalone VIN card and Edmunds actions (Sep 7, 2026)

For a standalone VIN check, the intended compact response is:

1. Minimal identity/verification card.
2. Honest indication when no exact listing is available.
3. Close/narrow “Check avail.” action, using the same condition-aware close destination pattern used for New vehicles.
4. Loose “View similar” action, using the same broader fallback pattern used for New vehicles.
5. AI explanation text after the card, not instead of it.

This gives a standalone VIN user useful next actions without requiring the tool to perform live listing search or invent an exact listing. The exact-VIN destination should not be presented as confirmed when the tool does not have verified listing context.
