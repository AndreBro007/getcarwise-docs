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


## 23. André-approved refinement — intent-driven comparison

Comparison must be driven by:
1. The user’s stated goal.
2. The constraints entered.
3. The priority language used.
4. The data available for each vehicle.
5. The point reached in the buying cycle.

Do not produce a generic table every time.

Examples:
- “Best SUV for my family” → space, practicality, safety-related evidence, value, and fit.
- “Which is the best deal?” → price position, condition, mileage, match quality, and risk signals.
- “Which should I buy?” → overall fit, material trade-offs, unknowns, and next verification.
- “Cheapest monthly payment” → price, payment assumptions, and condition.
- “Best nearly-new option” → Used/CPO, low mileage, trim, price proximity, and history completeness.

The AI should explain why the winner fits the user’s request and identify the most important trade-off. The comparison card should show only the decision-relevant fields for that request.

## 24. V3 phased build plan

### V3.1 — Card-first tool contract

Goal: establish the shared vehicle-context and response order without adding a new user workflow.

Scope:
1. Map current payloads for find_matching_vehicle, check_vehicle, and resolve_dealer_url.
2. Define the minimum shared vehicle context.
3. Ensure every vehicle response can lead with a card/context card.
4. Preserve current search card behavior unchanged.
5. Keep V1 and V2 branches untouched.

Gate:
- existing V3 recall and search tests pass;
- no card regression;
- standalone and follow-up response shapes are documented.

### V3.2 — Card-first check_vehicle integration

Goal: fix the current risk/recall experience.

Scope:
1. Follow-up check from a listing preserves the selected listing card.
2. Add compact Buyer Check and recall states to that card.
3. Provide reason-bearing risk labels.
4. Keep AI explanation after the card.
5. Preserve unknown/unavailable states.
6. Keep listing actions available.

Gate:
- known VIN/listing follow-up;
- standalone VIN;
- no listing available;
- recall unavailable;
- risk reason matches displayed label;
- exact vehicle identity preserved.

### V3.3 — Standalone VIN action flow

Goal: make VIN-first use useful without requiring a previous search.

Scope:
1. Minimal identity/verification card.
2. Honest no-listing state.
3. Close/narrow Check avail. button using the New-vehicle pattern.
4. Loose View similar button.
5. AI explanation after the card.
6. No live Edmunds search or unverified exact-listing claim.

Gate:
- valid VIN;
- invalid VIN;
- valid VIN with no listing;
- Used, New, and CPO examples;
- Claude and ChatGPT rendering.

### V3.4 — Intent-driven labels and action selection

Goal: make the compact card adapt to the user’s stage in the buying cycle.

Scope:
1. Search cards prioritize match/value and condition.
2. Risk cards prioritize Risk/Recall and verification action.
3. Listing-action cards prioritize Check avail./View similar.
4. Comparison cards prioritize only fields relevant to the stated question.
5. Cap default badges at two or three.
6. Never hide the primary listing action.

Gate:
- labels change appropriately by tool and intent;
- no crowded cards;
- action remains clear at a glance;
- no loss of listing click-through.

### V3.5 — AI-driven comparison

Goal: answer “which one should I choose?” with adaptive reasoning rather than a generic table.

Scope:
1. Accept selected result labels, VINs, or the current shortlist.
2. Return complete structured evidence to the host AI.
3. Let the AI select comparison dimensions from user intent.
4. Return a compact card/conclusion for each compared vehicle.
5. Provide one winner, one alternative where useful, key trade-offs, and verification steps.
6. Keep a listing action for every compared vehicle.

Gate:
- family/practicality comparison;
- best value;
- cheapest payment;
- best nearly-new option;
- risk/unknown trade-off;
- explicit user priorities that conflict.

### V3.6 — Affordability action

Goal: add a useful purchase-cycle step without creating a full financial dashboard.

Scope:
1. Single monthly-payment estimate.
2. Show price, term, APR, and down-payment assumptions.
3. Keep affordability separate from risk.
4. Return the same vehicle card plus payment line.
5. Preserve listing action.

Gate:
- known and unknown price;
- different terms;
- zero down payment;
- APR assumptions;
- clear disclaimer;
- no claim that the user can afford the vehicle.

## 25. Build and release strategy

Use incremental engineering phases internally, but do not submit every phase as a separate public app version.

Recommended approach:
1. Build and test V3.1 through V3.3 privately first.
2. Stabilize the core three-tool experience.
3. Add V3.4 only after card-first behavior is reliable.
4. Add comparison and affordability only when each is independently complete.
5. Submit one coherent V3 release containing the tools and workflows that are fully tested.
6. Keep later capabilities for V3.1/V3.2-style post-launch updates or the next reviewed release, depending on platform requirements.

The reason is that separate tools increase capability and discoverability, but submitting too early with half-finished hybrid behavior creates a poor review and user experience. Conversely, waiting to build every possible feature creates unnecessary scope and delays useful validation.

The public release should be a coherent bundle:
- find_matching_vehicle;
- check_vehicle;
- resolve_dealer_url;
- card-first standalone/follow-up behavior;
- tested descriptions and starter prompts;
- stable lean UI.

Comparison and affordability should not be included merely because they exist in the roadmap. Include them only if their complete user flow, card output, evidence handling, and regression coverage are ready.

OpenAI’s current guidance says to thoroughly test the MCP server, tools, and optional UI across scenarios before submission, and that published MCP metadata uses reviewed snapshots; metadata changes require a new reviewed version. [OpenAI submission guidance](https://developers.openai.com/plugins/deploy/submission), [OpenAI review guidance](https://developers.openai.com/plugins/app-guidelines), [OpenAI connection guidance](https://developers.openai.com/plugins/deploy/connect-chatgpt)

For Anthropic, maintain the same discipline: test the remote MCP server and real Claude user experience privately, then submit the stable tool set rather than a moving development target. Anthropic documents reviewed connectors as remote MCP servers using the same MCP infrastructure. [Anthropic MCP documentation](https://docs.anthropic.com/en/docs/claude-code/mcp)

## 26. Recommended immediate next step

Give Claude the V3.1–V3.3 handoff:
1. Map existing payloads.
2. Define the smallest shared vehicle-context contract.
3. Make check_vehicle card-first for listing follow-ups.
4. Add standalone VIN card actions.
5. Preserve existing search and link behavior.
6. Test Claude and ChatGPT before considering comparison or affordability.

No production or V1 change is authorized by this design alone.
