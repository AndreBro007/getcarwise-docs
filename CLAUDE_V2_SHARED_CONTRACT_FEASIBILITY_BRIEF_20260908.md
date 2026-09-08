# Claude Feasibility Brief — Shared Tool Contract, V2 Baseline

**Status:** Approved design direction for feasibility review. This is not authority to modify code, deploy, or resubmit.  
**Implementation baseline:** Existing tested V2 release branch.  
**Scope exclusion:** No V3 tool or capability is included.

## Decisions already approved

1. **One shared public description** will be attempted for OpenAI and Anthropic. Platform submission metadata may differ, but product semantics and public field definitions should not drift.
2. The description is neutral and declarative: no forced invocation, never-refuse language, mandatory tool chaining, provider implementation manual, or broad context input.
3. The opening retains V1 discovery cues: current listings, shortlists, explicit requirements, lowest price, newest, lowest mileage, best within budget, practical needs, and exact VIN.
4. `goals` becomes public `vehicleNeeds`, retaining the same soft-intent role. During migration, code should accept both names.
5. `bodyType`, `vehicleType`, trim, seating, technical fields, condition/history, priority, and location remain as documented in the shared contract. Existing V2 field-audit safeguards remain code responsibilities.
6. Electrification is first-class: public `hybrid` includes conventional and mild hybrids; plug-in hybrid and electric remain distinct. Requests retain **type(s)** and **required versus preferred** intent.
7. Auto.dev `vehicle.fuel` is display-only. “Gasoline” does not disprove hybrid/PHEV status and must never be used as an electrification filter or exclusion.

## Candidate shared main description

**Measurement:** 282 words / 1,998 characters.  
**Submitted V1 comparison:** 2,767 words / 18,154 characters.  
**Candidate main plus 31 field definitions:** 613 words, approximately 78% shorter than the submitted V1 main description alone.

> Finds current vehicles for sale in the United States and returns a concise shortlist that matches a user’s requirements. It is appropriate for listing requests with explicit criteria, optimisation goals such as lowest price, newest, lowest mileage, or best within a stated budget, practical needs such as a large family SUV or commuter vehicle, or an exact current listing by VIN.
>
> The search can use direct requirements such as make, model, price, year, mileage, location, body style, drivetrain, transmission, trim, seating, colour, condition, electrification, and purchase priority. A stated requirement is evaluated as a matching criterion; an expressed preference informs ranking. Practical listing needs such as a large family SUV, a teen-driver car, a commuter vehicle, or a vehicle for towing can also be represented when the user is seeking vehicles for sale. They help identify and rank suitable candidates, but they do not independently establish reliability, safety, running cost, exact towing suitability, vehicle condition, accident-free history, or certification.
>
> An exact 17-character VIN refers to one specific listing. If that listing is unavailable, the result reports that outcome rather than returning a similar vehicle. Electrification requests identify accepted types—hybrid (including mild hybrid), plug-in hybrid, and electric—and whether they are required or preferred. A primary-fuel label alone does not determine hybrid or plug-in-hybrid status.
>
> Results contain current matching listings, usable viewing links when available, and evidence showing which requested criteria were confirmed, unconfirmed, or changed during the search. Missing history, ownership, certification, equipment, or specification data remains unknown; it is not treated as proof that a vehicle satisfies or fails a request.
>
> This tool is for vehicle-listing searches, not general automotive education, maintenance, financing, leasing, unsupported vehicle categories, or comparisons that do not require current listings.

## Candidate public input contract

All current V2 fields remain unless stated below. Definitions remain concise and user-semantic; provider mapping and verification remain code.

| Field | Definition |
| --- | --- |
| `vin` | Exact 17-character VIN for one current listing. Other criteria are evaluated against that listing; no similar-vehicle substitute is returned. |
| `priceMax` / `priceMin` / `priceFlexibility` | Price range in USD and whether an approximate ceiling may be flexible. |
| `priorityAxis` | best_for_budget, cheapest, lowest_mileage, newest, or lower_risk. Lower risk ranks available purchase-risk evidence and is not a guarantee. |
| `yearMin` / `yearMax` / `mileageMax` | Direct year and odometer bounds. |
| `make` / `model` | Manufacturer and one or more make-free model names; comma-separated models are supported. |
| `bodyType` / `vehicleType` | Broad body style and finer classification when a user expressly distinguishes it. |
| `zip` / `radiusMiles` / `state` | Local or state-wide search scope. |
| `trimRequired` / `trimPreference` | Required trim is a match criterion; preferred trim affects ranking. |
| `seatsMinPreference` | Preferred seating evidence; not a provider hard filter. |
| `vehicleNeeds` | Short, capped listing-relevant practical needs; not a transcript, broad profile, or general-advice channel. |
| `drivetrain` / `transmission` | Requested drivetrain and transmission. |
| `exteriorColor` / `interiorColor` | Requested exterior and interior colour. |
| `doors` / `cylinders` | Requested door count and engine cylinder count; V8=8, V6=6, I4/four-cylinder=4. Displacement is not represented by `cylinders`. |
| `used` | Used only, new only, or omitted for both. |
| `cpo` / `noAccidents` / `oneOwner` | Evidence requests. Results distinguish confirmed/known, reported negative where applicable, and unreported—not false. |
| `electrificationTypes` | One or more accepted electrified types: `hybrid` (including conventional and mild hybrids), `plug_in_hybrid`, and/or `electric`. |
| `electrificationRequirement` | Whether the stated electrification types are `required` or `preferred`. |

## Required implementation ownership

| Topic | Required direction |
| --- | --- |
| `goals` migration | Public schema exposes `vehicleNeeds`; server accepts `goals` and `vehicleNeeds` during compatibility period, with the same soft-intent semantics. |
| Natural-language interpretation | AI identifies practical need, electrification type(s), strength, and applicable model/trim candidates. No large backend category/model table. |
| Provider mapping | Code handles model normalization, stable Auto.dev mapping, existing V2 retries/backfills, and post-verification. |
| Electrification candidate selection | AI continues resolving compatible model/trim variants. A named hybrid/PHEV/EV variant is not discarded merely because provider primary fuel is gasoline. |
| Electrification verification | Code combines model/trim identity with NHTSA VIN evidence for final-shortlist evidence. It must classify hybrid, plug-in hybrid, and electric distinctly; it preserves mild-hybrid evidence internally while treating it as an accepted public `hybrid` result. The current boolean “electrified” helper is insufficient for the full contract. |
| `required` versus `preferred` | Required and preferred must produce demonstrably different selection/ranking behaviour. Do not make NHTSA a new pre-shortlist exclusion gate unless regression evidence shows candidate breadth, latency, and false-negative risk remain acceptable. |
| Result evidence | Return confirmed, unconfirmed, changed, and data-conflict evidence from code. Do not depend on host prose to make those distinctions. |
| Existing audit safeguards | Retain V2 protections for inconsistent `vehicleType`, unsafe raw trim, response-only seats, host-sensitive `interiorColor`/`cylinders`, unknown history/CPO/ownership, ZIP edge cases, and exact VIN. |

## Claude feasibility questions — answer before implementation

1. Does the host reliably route the three new public concepts: `vehicleNeeds`, `electrificationTypes`, and `electrificationRequirement`?
2. What is the minimal safe schema shape for `electrificationTypes` (array/enum limits) and `electrificationRequirement` (required only when types exist)?
3. How should NHTSA `ElectrificationLevel`, primary fuel, and secondary fuel be normalised into hybrid, plug-in-hybrid, and electric evidence while preserving mild-hybrid source evidence distinctly? Public `hybrid` must accept conventional and mild hybrids.
4. Can existing candidate generation supply enough model/trim breadth for a required electrification request before final VIN confirmation?
5. What does “required” do when model/trim identity is compatible but NHTSA is unavailable? Present the evidence-state policy and its user-visible wording; do not use Auto.dev primary fuel as a shortcut.
6. Which existing V2 tests need amended fixtures, and which new deterministic fixtures/live smoke tests are needed?
7. Can `resolve_dealer_url` remain internal/non-public without affecting any host flow?

## Required regression gate

- current inventory / shortlist discovery;
- cheapest, newest, lowest mileage, and best-within-budget intent;
- family, teen-driver, commuter, and towing needs;
- hybrid (including conventional and mild hybrid), PHEV, and EV as required and preferred;
- a hybrid listing whose provider primary fuel is gasoline;
- model/trim hybrid variants, including F-150 PowerBoost;
- exact VIN and unavailable VIN;
- required/preferred trim;
- `bodyType`/`vehicleType` E-Class and V90-style conflicts;
- V8/cylinders and interior-colour routing;
- seats, doors, new/used fairness, condition/history/CPO/ownership unknown handling;
- state, valid ZIP, and non-geographic ZIP;
- returned link and evidence behaviour;
- out-of-scope general advice.

## What Claude should deliver next

A feasibility response only:

1. exact proposed schema/code deltas from V2 baseline;
2. identified regression risks and test plan;
3. any reason a shared common description cannot work in either platform;
4. a recommendation on whether the new fields can be implemented without degrading reliable searches;
5. a V1-equivalence response covering practical-need model/trim scope, required/preferred electrification, city-only location, API-audit invariants, and the proposed deterministic and live A/B tests.

No implementation should start until that response is reviewed and explicitly approved.

## Related design records

- [Shared contract candidate](https://github.com/AndreBro007/getcarwise-docs/blob/main/DRAFT_SHARED_TOOL_CONTRACT_V0_2_20260908.md)
- [Electrification hand-off design](https://github.com/AndreBro007/getcarwise-docs/blob/main/ELECTRIFICATION_HANDOFF_DESIGN_20260908.md)
- [OpenAI/Anthropic compatibility decision](https://github.com/AndreBro007/getcarwise-docs/blob/main/PLATFORM_TOOL_DESCRIPTION_COMPATIBILITY_DECISION_20260908.md)
- [V1 to V2 search-results equivalence gate](https://github.com/AndreBro007/getcarwise-docs/blob/main/V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md)
