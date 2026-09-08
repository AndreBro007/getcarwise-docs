# DRAFT — V1 Tool Contract Redesign for OpenAI Resubmission

**Date:** 2026-09-08  
**Status:** Draft for André's decision — no production code or submission changes authorised by this document  
**Scope:** CarClever - Find My Car V1, submitted OpenAI tool contract  
**Objective:** Preserve accurate AI-led vehicle-listing interpretation while reducing the public MCP contract to the minimum clear, purpose-driven, auditable form required for OpenAI review.

## Executive answer

The rejected V1 contract is not merely verbose. The submitted `find_matching_vehicle` metadata combines four different layers in one public surface:

1. User-facing tool selection.
2. AI interpretation coaching.
3. Auto.dev/provider-specific translation rules.
4. Deterministic search, verification, output, link, and UI instructions.

The submitted main tool description is **2,767 words / 18,154 characters**. Its 29 input-field descriptions add **8,370 characters**. This is a public tool contract carrying a full orchestration manual.

The design direction agreed in discussion is:

> The tool description first explains the vehicle-listing capability. It then gives the AI only the interpretation instructions it genuinely needs. The backend owns translation into Auto.dev fields and all deterministic data-handling behavior.

This does **not** mean replacing AI interpretation with a large lifestyle-category table. AI remains responsible for understanding a request such as “large family SUV” and converting it into a meaningful vehicle-listing intent. Code owns stable normalization, provider-specific conversion, validation, widening, verification, disclosures, and presentation.

## Evidence and review criteria

OpenAI's current plugin guidance requires:

- clear, specific, action-oriented tool names;
- descriptions that accurately state purpose and when to use a tool;
- no overly broad triggering beyond explicit user intent and the plugin's purpose;
- minimal, purpose-driven inputs directly related to the tool's purpose;
- accurate annotations;
- predictable behavior matching the published contract.

Sources:

- [OpenAI Plugin Guidelines](https://developers.openai.com/plugins/app-guidelines)
- [OpenAI: Define Tools](https://developers.openai.com/plugins/plan/tools)
- [OpenAI MCP Server Guidance](https://developers.openai.com/plugins/build/mcp-server)

The rejection names two applicable concerns:

1. Tools request input that is overly broad or unnecessary.
2. Tool naming/description quality is insufficiently clear or contains inappropriate selection language.

The V1 tool name `find_matching_vehicle` is action-oriented and specific. The primary review risk is the oversized, mixed-purpose description and heavily coached schema; the smaller `resolve_dealer_url` description should also be simplified and reviewed before resubmission.

## What already belongs in code

The current V1 backend is not thin in the areas that matter. It already owns substantial deterministic behavior:

| Current backend capability | Existing evidence | Proper public-contract treatment |
|---|---|---|
| Make-prefix normalization | `intent-parser.ts` strips stable manufacturer prefixes from model strings and discloses corrections | Code behavior; do not teach full provider syntax in tool description |
| Query execution and provider mapping | V1 builds the Auto.dev query in server code | Code behavior |
| Post-search verification | `verifyAgainstConstraints` checks returned listings against applied constraints | Brief result guarantee only |
| Widening | `widenSearchIfThin` runs bounded, disclosed retries | Brief limitation/behavior only |
| VIN cross-check | `crossCheckVin` runs on results | Brief result guarantee only |
| Risk classification | `classifyRiskTier` is deterministic over available evidence | Output/ranking behavior, not a long selection prompt |
| Link selection | `resolveLinks` controls affiliate/fallback treatment | Result-generation/UI behavior |
| Hybrid display correction and NHTSA enrichment | Existing fuel/NHTSA helpers | Code/provider behavior |
| Qualifier accounting and constraint evidence | Existing helpers construct verified confirmations/disclosures | Result-generation behavior |
| Trim matching | `trimMatches` and local enforcement exist | Short explanation of required vs preferred intent only |
| Buyer Check construction | `buildBuyerCheck` derives output from result evidence | Candidate separate-tool behavior |

This is important: moving these items out of the public description is not a loss of function. The code already performs them.

## What AI must still do

AI remains necessary for genuine language interpretation before a listing search. It should:

1. Recognise that the user wants vehicles currently for sale, rather than general automotive advice.
2. Extract explicit constraints and priorities from the request.
3. Preserve a user-stated requirement as required; treat a clearly expressed preference as a preference.
4. Interpret vehicle-listing concepts such as “large family SUV,” “teen driver car,” or “vehicle for towing” into a usable vehicle search intent.
5. Resolve ambiguous user language or ask a focused question when no reliable interpretation is possible.
6. Choose the user's explicit optimisation when stated: e.g. lowest price, newest, lowest mileage, lower apparent purchase risk, or best fit within budget.
7. Explain returned, verified results naturally.

AI should **not** need to know the full Auto.dev contract, undocumented field quirks, the widening ladder, link-routing policy, output-card mechanics, or every data-quality exception.

## No lifestyle category-table architecture

The redesign deliberately does **not** create a large maintained taxonomy for “best family cars,” “reliable teen cars,” “good commuter cars,” or “good towing vehicles.”

Those are contextual judgments. AI should continue to interpret them.

Small stable technical lookups remain appropriate where no interpretation is involved:

| Permitted stable lookup | Why it belongs in code |
|---|---|
| Manufacturer aliases and prefix normalization | Closed, slowly changing technical vocabulary |
| Fixed vocabulary conversions such as V8 → 8 cylinders | Mechanical semantic conversion |
| Provider enums and validation | Technical compatibility |
| Known hybrid/PHEV nameplate relationships | Stable vehicle-variant relationship when electrification is explicitly requested |
| ZIP/VIN format validation | Deterministic validation |
| Provider-specific fallback/exception handling | Data-source behavior, not user interpretation |

New entries should be added only when a confirmed bug reveals a stable, non-interpretive mapping. This follows the existing `MAKE_NAMES` pattern in `intent-parser.ts`, which is explicitly separated from lifestyle-to-model mapping.

## Correct ownership of the current description

| Current section or rule | Keep for AI? | Move/retain as | Rationale |
|---|---:|---|---|
| Intro: live US inventory search / shortlist | Yes, compressed | Tool description | Defines the action and scope |
| Explicit constraints (price, make/model, year, mileage, location, body style, drivetrain, transmission, seats, trim, condition) | Yes, compressed | Tool description + concise fields | Tells AI what can be expressed in a listing request |
| Practical listing needs (large family SUV, teen driver, towing) | Yes, carefully bounded | Tool description | Valid if they clearly imply finding vehicles for sale |
| “Do not use” general education / maintenance boundary | Yes | Tool description | Prevents broad non-listing use |
| SEARCH DECOMPOSITION rules | Partly | Compact AI rule + backend | AI extracts intent; code maps/validates provider fields |
| “Model list is a hard filter” | Partly | Short AI rule + backend enforcement | AI needs to preserve interpreted vehicle scope; code owns query mechanics |
| HYBRID AND PHEV coverage | No detailed coaching | Stable code mapping + short limitation | Current detailed variant instructions are provider-specific |
| HARD FILTERS VERSUS DISCLOSURE | No detailed coaching | Backend + result text | Code already verifies and accounts for unknown data |
| HARD-FIELD MAPPING | No detailed coaching | Field definitions + code normalization | Current instruction list is implementation guidance |
| TRIM required vs preferred | Yes, concise | Two short field definitions | This is a real user-intent distinction |
| DIRECT VIN LOOKUP and Buyer Check | Temporarily concise or split | V1 boundary / V3 separate tool option | Current section combines a distinct outcome and can confuse routing |
| RESULT TRUST | No detailed coaching | Code + short tool guarantee | The output is built deterministically |
| PRIORITY AXIS | Yes, concise | Short enum definitions | AI must interpret stated optimisation |
| LOWER RISK RANKING methodology | No detailed coaching | Code + result explanation | The exact evidence/ranking order belongs in backend |
| LOCATION city/ZIP resolution detail | Partly | Concise input boundary + code where feasible | AI may need to ask a question; provider details do not belong in description |
| AUTOMATIC WIDENING | No detailed coaching | Short behavior statement | Code already controls it |
| EMPTY SEARCHES | No detailed coaching | Backend/result behavior | Not a tool-selection issue |
| PRESENTING RESULTS / affiliate links / image markdown | No | Result generation / widget | Public description should not instruct ChatGPT's prose formatting |
| MAPS | No | Separate UI capability or later tool | Not core to inventory search and not required for selection |
| resolve_dealer_url affiliate-routing policy | No detailed coaching | Backend/result behavior | The public description should say it returns an available viewing link for an identified vehicle |

## Proposed V1 contract shape

### 1. Tool purpose and boundary

The main tool should describe only the user-facing listing-search capability.

Proposed intent, not final copy:

> Search current U.S. vehicle listings for a user who wants vehicles for sale or a shortlist. Use it for stated requirements such as vehicle type, make/model, budget, year, mileage, location, drivetrain, transmission, seats, color, trim, condition, or a practical vehicle need that clearly relates to finding listings. Do not use it for general automotive advice that does not require current listings.

This keeps “large family SUV” in scope. It does not make the tool a general advice or recommendation service.

### 2. Minimum AI operating rules

The tool needs a short second layer:

1. Extract only requirements and preferences relevant to the listing search.
2. Preserve explicit requirements; do not silently invent new hard constraints.
3. Treat a clearly stated preference as ranking guidance.
4. When a practical need needs vehicle interpretation, express that interpretation in the search intent.
5. Ask a focused follow-up only when the request is materially ambiguous.
6. Do not treat unreported history or equipment as confirmed.

The current description has many correct rules. The redesign keeps the principles, not the full implementation manual.

### 3. Inputs

The V1 resubmission should retain only inputs that correspond to a real user-stated vehicle-search concept or a necessary compact interpretation.

The detailed schema review should evaluate each input against four tests:

1. **User relevance:** Would a user reasonably state this when asking for listings?
2. **AI need:** Does the host AI need a definition to populate it correctly?
3. **Backend need:** Does the backend need it as an independent input, rather than deriving it deterministically?
4. **Review clarity:** Can its definition be written in one or two plain sentences without implementation instructions?

Likely retain, with short definitions:

- exact VIN;
- make and model;
- budget / price range;
- year and mileage;
- location;
- body style;
- drivetrain and transmission;
- seating;
- color;
- trim requirement or trim preference;
- new/used/CPO preference;
- explicit optimisation;
- accident/owner preferences, provided output remains candid about unknown data.

Likely reduce or redesign:

- `goals`: retain only if it is a brief, task-specific vehicle-listing intent, not a broad contextual field. It must not be a proxy for conversation history.
- `vehicleType`: reconsider whether the user-facing distinction is genuinely needed or whether code can infer/provider-map it.
- `priceFlexibility`: perhaps derive deterministically from explicit language or retain a one-line definition.
- `priorityAxis`: retain, but concise; do not publish the detailed ranking methodology.
- `vin`: keep only for an exact listing lookup in V1, or remove Buyer Check from this contract and split it in V3.

### 4. Output behavior

The tool description should make only high-level, verifiable promises:

- returns current matching listings;
- reports when a stated criterion cannot be confirmed or a search constraint changes;
- does not represent unknown history as clean;
- returns the exact listing when an exact VIN is found, rather than silently substituting a similar vehicle.

It should not tell the host exactly how to render cards, links, maps, photos, count introductions, or ranking caveats. Those are generated from server evidence and UI resources.

## V1 vs V3 decision options

### Option 1 — V1 contract compression, no functional split

Keep `find_matching_vehicle` as one tool, including exact VIN lookup. Strip the Buyer Check coaching and detailed mechanics from the description/schema. The backend can continue returning a Buyer Check as an additive result when it has a VIN.

**Use when:** quickest defensible resubmission is the priority.

**Trade-off:** one tool still serves both discovery and exact-VIN lookup, but the public description can be far cleaner.

### Option 2 — V1 compression plus V3 Buyer Check split

Resubmit a narrowed V1 inventory tool. In V3, move VIN due diligence into a focused `check_vehicle` contract, designed with a card/listing context so it does not repeat the known listing-loss regression.

**Use when:** preserve accurate V1 search now, while creating a clean long-term architecture.

**Trade-off:** requires disciplined version separation and later engineering work.

### Option 3 — V3 intent-first search contract

Redesign search so AI supplies a compact CarClever-level intent and code owns the final provider query construction. Keep AI-led practical-need interpretation; use stable code mappings only for non-interpretive translation.

**Use when:** a material V3 engineering cycle is acceptable.

**Trade-off:** cleanest architecture, but should not be rushed into the V1 resubmission without regression testing.

## Recommended sequence

1. Approve the ownership principle in this document.
2. Perform a field-by-field schema classification using the four input tests.
3. Produce a **V1 minimal contract draft** with no production changes.
4. Produce a **V3 separation brief** for VIN Buyer Check and any intent-first schema redesign.
5. Ask Claude to assess the implementation delta only after the business/design contract is approved.
6. Test the revised contract with direct, indirect, edge-case, and out-of-scope prompts before resubmission.
7. Rescan the live MCP endpoint and verify the exact submitted snapshot—not only the source code.

## Explicit non-decisions

- No claim that every lifestyle need should be replaced by category tables.
- No decision yet to remove exact VIN lookup from V1.
- No decision yet to change V1 tool names.
- No production code change, deployment, app submission, or resubmission is authorised by this document.
- No conclusion that the prior description work was wrong. It solved genuine host-behavior issues; this redesign changes where those rules live.


## Confirmed design directions — André, 2026-09-08

These are confirmed design directions for the V2-baseline OpenAI resubmission analysis. They are not production implementation approvals.

1. **Release baseline:** design the resubmission around V2's existing two-tool surface. Do not include, rely on, or describe V3 tools or capabilities. Custom-domain/release handling is explicitly deferred until the contract redesign is complete.
2. **AI versus code:** AI remains responsible for interpreting a listing request, including practical needs such as a large family SUV, teen-driver car, commuting, or towing. Code owns stable technical translation, normalization, provider quirks, validation, verification, widening, and result generation.
3. **No lifestyle taxonomy:** do not build broad, maintained category tables for concepts such as “best family cars” or “reliable teen cars.” Add code lookups only for stable, non-interpretive mappings or confirmed technical bugs.
4. **Practical needs boundary:** practical needs remain in scope when they clearly mean “find current listings.” The tool must distinguish AI-interpreted fit from listing evidence that actually verifies a specific claim; it must not imply that V1/V2 independently proves reliability, safety, running cost, or vehicle-specific towing suitability.
5. **Hybrid and trim:** AI retains required-versus-preferred interpretation. Code owns hybrid/PHEV variant expansion and verification, provider-specific behavior, model normalization, trim enforcement, and related result disclosures.


## Confirmed Batch 3 directions — André, 2026-09-08

These decisions apply to a **future OpenAI resubmission candidate built from the existing V2 baseline**. They do not redefine V2 or authorise changes to it.

A. **Exact VIN:** retain the already-built V2 exact live-listing lookup. In the future public contract, treat Buyer Check as an additive evidence summary rather than the main public tool trigger; reserve a dedicated VIN-due-diligence contract for later V3 work.

B. **Priority and risk:** retain concise user-intent priorities. Move ranking mechanics and the evidence model to code/result explanations; do not publish the full methodology in the tool description.

C. **Location:** retain AI-led interpretation of a user’s location in the resubmission candidate. Do not create a new deterministic location-resolution subsystem solely for this contract redesign. The tool description need not publish the implementation details.

D. **Widening and empty results:** remove mechanics from the public description; retain only a short transparency commitment that the result explains material changes or limitations.

