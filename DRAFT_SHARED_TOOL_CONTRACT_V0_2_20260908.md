# Draft — Shared OpenAI and Anthropic Tool Contract

**Status:** Shared-contract candidate 0.2 for discussion. This document changes no active submission, source code, schema, or deployment.  
**Scope:** One public `find_matching_vehicle` description and concise field definitions that could be used by both OpenAI and Anthropic if approved. Existing V2 code is the future implementation baseline; V3 remains excluded.  
**Purpose:** Replace the current shared V1 public operating manual with a neutral, detailed-but-non-implementation contract.

## Draft 0.2 main description

**Measurement:** **257 words / 1,821 characters**.  
The current submitted V1 main description is **2,767 words / 18,154 characters**. Draft 0.2 is **91% shorter by words** before field definitions.

> Finds current vehicles for sale in the United States and returns a concise shortlist of listings that match the user’s stated requirements. It is appropriate when a user wants available listings, a vehicle shortlist, or an exact current listing by VIN.
>
> The search can use direct requirements such as make, model, price, year, mileage, location, body style, drivetrain, transmission, trim, seating, colour, condition, and purchase priority. A stated requirement is evaluated as a matching criterion; an expressed preference informs ranking. Practical listing needs such as a large family SUV, a teen-driver car, a commuter vehicle, or a vehicle for towing can also be represented when the user is seeking vehicles for sale. They help identify and rank suitable candidates, but they do not independently establish reliability, safety, running cost, exact towing suitability, vehicle condition, accident-free history, or certification.
>
> An exact 17-character VIN refers to one specific listing. If that listing is unavailable, the result reports that outcome rather than returning a similar vehicle. Hybrid, plug-in hybrid, and electric requests retain whether electrification is required or preferred; returned vehicles are identified using the available powertrain evidence.
>
> Results contain current matching listings, usable viewing links when available, and evidence showing which requested criteria were confirmed, unconfirmed, or changed during the search. Missing history, ownership, certification, equipment, or specification data remains unknown; it is not treated as proof that a vehicle satisfies or fails a request.
>
> This tool is for vehicle-listing searches, not general automotive education, maintenance, financing, leasing, unsupported vehicle categories, or comparisons that do not require current listings.

## Why this is a common-platform candidate

- It states purpose, trigger boundary, key inputs, result, and material limits.
- It has no “always invoke,” “never refuse,” “must call another tool,” or post-selection operating script.
- It contains detail Anthropic needs—parameter semantics and caveats—without exposing provider mapping or requiring agent procedure.
- It meets OpenAI’s user-intent and minimum-input direction: no transcript, broad profile, raw context, or implementation terms.
- It does not decide that the platforms must use it. It is the concrete common candidate against which that decision can now be made.

## Proposed concise field definitions

**Measurement:** 29 fields; **320 words** across descriptions.  
**Combined measurement:** Draft 0.2 main description plus field descriptions is **577 words**, an approximately **79% reduction** from the submitted V1 main description alone. This is a directional measurement only: final schema limits, examples, and platform submission metadata are not included.

| Field | Shared concise definition | Status / field-audit guardrail |
| --- | --- | --- |
| `vin` | Exact 17-character VIN for one current listing. Other criteria are evaluated against that listing; no similar-vehicle substitute is returned. | Keep; exact live-VIN path and Buyer Check remain V2-baseline behaviour. |
| `priceMax` | Maximum price in USD. | Keep; strict/flexible handling remains code. |
| `priceMin` | Minimum price in USD. | Keep. |
| `priceFlexibility` | Whether an approximate price ceiling may be treated as flexible; omitted ceilings remain strict. | Keep; concise enum semantics. |
| `priorityAxis` | Ranking objective: best_for_budget, cheapest, lowest_mileage, newest, or lower_risk. Lower risk ranks available purchase-risk evidence and is not a guarantee. | Keep; do not publish scoring mechanics. |
| `yearMin` | Earliest acceptable model year. | Keep. |
| `yearMax` | Latest acceptable model year. | Keep. |
| `make` | Vehicle manufacturer, such as Toyota, Honda, or Ford. | Keep. |
| `model` | One or more vehicle model names, without the manufacturer (for example, E-Class rather than Mercedes-Benz E-Class). Comma-separated models are supported. | Keep; code still normalizes known provider variants. |
| `bodyType` | Broad body style, such as SUV, Sedan, Truck, or Minivan. | Keep; broadly populated provider body-style filter. |
| `mileageMax` | Maximum odometer mileage. | Keep. |
| `zip` | Five-digit US ZIP code for a local search. | Keep; existing ZIP control-query safeguard stays in code. |
| `radiusMiles` | Search radius in miles from the ZIP; the service applies its documented default when omitted. | Keep; code owns widening. |
| `trimPreference` | Preferred trim or variant. It influences ranking and does not require a matching trim. | Keep; code handles unreliable raw trim data. |
| `trimRequired` | Requested trim or variant. A confirmed different trim is not treated as a match. | Keep; local enforcement remains code. |
| `seatsMinPreference` | Preferred minimum seating capacity. Results report whether available seating evidence meets the preference. | Keep; response/ranking evidence, not provider hard filter. |
| `vehicleNeeds` | Proposed replacement for `goals`: a short, capped list of listing-relevant practical needs, not a conversation transcript or broad profile. | **Proposed schema change**; requires Claude feasibility review. |
| `drivetrain` | Requested drivetrain: AWD, 4WD, FWD, RWD, or a comma-separated acceptable set. | Keep. |
| `transmission` | Requested transmission: Automatic or Manual. | Keep; verified hard filter. |
| `exteriorColor` | Requested exterior colour. | Keep; verified hard filter. |
| `interiorColor` | Requested interior colour. | Keep; has host-routing reliability history—must be regression-tested. |
| `vehicleType` | Finer vehicle classification when the user expressly distinguishes it, such as Crossover, Wagon, Hatchback, Coupe, or SUV. | Keep. It is not a duplicate of `bodyType`; retain existing V2 safeguards for inconsistent provider tags. |
| `doors` | Requested door count. | Keep; preserve unknown/null response handling. |
| `cylinders` | Requested engine cylinder count: V8 is 8, V6 is 6, and I4/four-cylinder is 4. Engine displacement is not represented by this field. | Keep; host-routing reliability must be regression-tested. |
| `used` | Vehicle condition: true for used only, false for new only; omitted includes both. | Keep; preserve V2 fairness/default behaviour. |
| `cpo` | Request for certified pre-owned status. Results distinguish confirmed, reported-not-CPO, and unreported evidence. | Keep; unknown is not false. |
| `state` | Two-letter US state code for a state-wide search when no local ZIP is available. | Keep; location interpretation stays AI-led. |
| `noAccidents` | Request for no reported accidents. Results distinguish reported-clean, reported issues, and unreported history. | Keep; never use unknown as a hard failure. |
| `oneOwner` | Request for one-owner history. Results distinguish available ownership evidence from unreported history. | Keep; never use unknown as a hard failure. |

## Deliberate omissions from the public description

These remain necessary product behaviours where applicable, but belong in code, structured result evidence, or the regression suite rather than public description prose:

- Auto.dev provider-field mapping, model cleanup, and hybrid variant expansion;
- retry/widening sequencing, ZIP control queries, provider fallback controls, and post-verification;
- risk score/ranking calculations and data-conflict mechanics;
- card layout, CTA/link labels, maps, image rules, and output formatting;
- instructions to the host to make, repeat, suppress, or chain calls.

## Open feasibility points — not yet decisions

| Topic | What the shared draft assumes | What Claude must confirm before implementation |
| --- | --- | --- |
| `goals` → `vehicleNeeds` | A narrow, capped, listing-specific practical-need input replaces broad free-form goals. | Exact schema shape, cap, current parser/scoring integration, and host routing. |
| Hybrid/PHEV/EV required versus preferred | The distinction appears in the public contract. | Smallest structured representation that preserves the existing V2 behaviour without reintroducing broad prose. |
| Field-routing resilience | Concise definitions retain the needed V8/cylinder and interior-colour signals. | Regression results in both hosts; retain/add only the minimum detail that proves necessary. |
| `resolve_dealer_url` | Main tool returns usable links; resolver stays non-public by default. | Whether any actual host flow still needs public access. |
| Main-description length | 257 words is the current candidate. | Whether the full contract maintains accurate Claude routing and passes OpenAI review. |

## Required regression evidence

No description or schema change should proceed without the existing regression suite plus focused checks for:

- family, teen-driver, commuting, and towing listing requests;
- hybrid/PHEV/EV required versus preferred;
- required versus preferred trim;
- V8/cylinders and interior colour routing;
- `bodyType` and `vehicleType` edge cases;
- exact VIN, condition/history/CPO/ownership unknown semantics;
- ZIP/location edge cases;
- links, evidence statements, and out-of-scope requests.

## Next review questions

1. Is this the right common level of detail for both platforms?
2. Is `vehicleNeeds` the right field name and boundary?
3. Does the concise field table retain every user-visible semantic that should stay public?
4. Which of the open feasibility points should Claude investigate first after approval?



## Shared-review decisions — 2026-09-08

### A. Discovery cues — approved

The shared opening will explicitly mention optimisation requests such as **lowest price, newest, lowest mileage, and best within a stated budget**. These are legitimate user-intent/discoverability cues from V1, expressed declaratively rather than as an instruction to invoke the tool.

### B. `goals` → `vehicleNeeds` — approved direction

`vehicleNeeds` is a narrower public name for the existing `goals` role, not a new category-table system or a behaviour reduction.

- It remains a short array of practical, listing-relevant needs.
- It continues to carry soft intent for AI interpretation and ranking/context; it is not a hard eligibility filter by itself.
- Needs such as reliability, low running cost, family, commuting, and towing remain expressible, but retain the existing evidence/verification boundary.
- The implementation should accept both `goals` and `vehicleNeeds` during migration so that the public-name change does not regress current behaviour.

### C. Electrification — agreed ownership split

Hybrid/PHEV/EV handling remains AI-interpreted, with deterministic translation and verification in code.

- AI identifies the natural-language request and whether electrification is required or preferred.
- Code handles stable model/variant expansion, trim enforcement where the electrified configuration is trim-like, and returned powertrain evidence.
- A small stable structured hand-off from AI to code is preferred over relying only on a prose `vehicleNeeds` phrase. The exact schema shape remains a Claude feasibility question.
- This preserves the V2-baseline model/variant and trim behaviour; no broad changing category table is introduced.


## Auto.dev field-audit re-check — D through G

The living audit was re-read after the D–G review. The proposed concise definitions remain valid; this re-check adds no field removals or new public prose. It confirms the following implementation and regression constraints:

| Area | Audit re-check | Effect on shared contract |
| --- | --- | --- |
| `model` | Trust Class B; provider model strings can span variants and can have runtime type errors. | Keep the concise make-free model semantics; retain ingestion normalization and tolerant matching in code. |
| `bodyType` | Broad `vehicle.bodyStyle` is highly populated and works as a filter. | Keep as the direct broad body-style field. |
| `vehicleType` | `vehicle.type` works mechanically but is undocumented and per-model tagging is inconsistent; live E-Class/V90 failures required V2 retry/backfill safeguards. | Keep the concise user semantic only. Do not claim provider certainty; retain all V2 safeguards and test coverage. |
| `trimRequired` / `trimPreference` | Raw provider trim is not a safe query filter and can be malformed at runtime. | Keep required-versus-preferred semantics; local normalization/matching remains code. |
| `seatsMinPreference` | Seats is response-only, not a provider filter. | Keep as evidence/preference only; no hard filtering. |
| Transmission, drivetrain, exterior colour | Verified working refinements. | Keep concise direct-request definitions. |
| `interiorColor` | Filter works, but host routing has shown real inconsistency. | Keep concise field; require host-routing regression tests before release. |
| `cylinders` | Works as a real filter but is undocumented; host routing has shown real inconsistency. | Keep the V8/V6/I4 semantic cue; require host-routing regression tests before release. |
| `doors` | Refinement works; provider can omit the total-match count while returning valid rows. | Keep direct-request definition; preserve null rather than false-zero totals in code. |
| `used` | Confirmed strict boolean filter; V2 fixed a real lean-projection condition-blindness bug. | Keep direct boolean meaning and preserve V2 condition handling. |
| CPO, accidents, ownership | CPO/history evidence is not safe as hard exclusion; unknown must remain distinct from reported negative. | Keep evidence-request definitions and the unknown-not-false rule. |
| ZIP/state/radius | State is a real filter; ZIP can be non-geographic and silently yield zero results. | Keep concise location inputs; retain validation, scope disclosure, and control-query protection in code. |

**Review outcome:** D–G remain approved as drafted, subject to the already-listed regression gate. The audit strengthens the decision to keep stable user semantics in the shared description while assigning provider quirks and data-trust protections to code.
