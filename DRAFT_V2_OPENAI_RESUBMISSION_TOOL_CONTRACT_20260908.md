# Draft — OpenAI Resubmission Tool Contract

**Status:** Discussion draft 0.1 — not code-ready and not an OpenAI submission.  
**Scope:** A future OpenAI resubmission candidate built from the existing tested V2 baseline. This is not a redefinition of V2, and it adds no V3 tools or capabilities.  
**Owners:** ChatGPT owns this contract/design. Claude must assess feasibility and implement any approved code or schema changes in `carclever-find-my-car`.

## Purpose

The rejected V1 public description tried to make the host understand the product, interpret a buyer's request, map it to Auto.dev, control deterministic search behaviour, and prescribe result presentation. Its main description was **2,767 words / 18,154 characters**.

This draft keeps the AI work that genuinely needs AI—interpreting practical vehicle needs into a listing search—but moves deterministic translation, verification, widening, and presentation responsibilities to code. It is deliberately conservative: field count is not reduced just to make the contract shorter.

The agreed rule is:

> The description first explains the vehicle-listing capability. It then gives the AI only the interpretation instructions it genuinely needs. Code owns the translation into Auto.dev fields and all deterministic data-handling behaviour.

## Proposed public tool surface

| Public surface | Draft decision | Reason |
| --- | --- | --- |
| `find_matching_vehicle` | Keep public, with the same clear, accurate name | It directly describes the action: finding current matching vehicle listings. |
| `resolve_dealer_url` | Do not expose publicly | It is a deterministic support operation. The primary result already returns usable listing links. |
| V3 `check_vehicle` or other V3 tools | Excluded | The current candidate is based on the existing V2 baseline only. |

The public search tool must request only concise, purpose-related data. It must not request a conversation transcript or a broad free-form profile.

## Candidate main description — Draft 0.1

**Measurement:** **414 words / 2,774 characters**. This is 2,353 words and 15,380 characters shorter than the submitted V1 main description (about 85% shorter by words). Field descriptions remain to be written and measured separately.

> Use this tool when the user wants current vehicles for sale in the United States or a shortlist of matching vehicles. It supports stated requirements such as make or model, budget, year, mileage, location, body style, drivetrain, transmission, seating, colour, trim, condition, and purchase priority.
>
> It also supports practical vehicle-listing needs such as a large family SUV, a teen-driver car, a commuter vehicle, or a vehicle for towing, when the user is asking to find suitable listings. Interpret those needs into a vehicle search while preserving the user's actual requirements and preferences. A practical need helps choose and rank candidates; it is not proof that a returned vehicle is reliable, safe, inexpensive to run, or suitable for a particular trailer or payload. Confirm only the listing evidence that is actually returned, and identify anything that still needs independent verification.
>
> Do not use this tool for general automotive education, maintenance, financing or leasing advice, unsupported vehicle categories, or comparisons that do not require current listings.
>
> Prepare the search as follows:
>
> - Put explicit requirements into the matching input fields. Do not invent hard constraints the user did not state or clearly imply.
> - Treat a named requirement as required. Treat a clearly signalled preference as ranking guidance.
> - When a practical need requires vehicle interpretation, resolve it into suitable candidate models and retain the short need in `vehicleNeeds`. If a reliable interpretation is not possible and would materially change the search, ask a focused follow-up question.
> - Use available constraint fields for explicit requirements rather than manually post-filtering returned listings.
> - For hybrid, plug-in hybrid, or electric requests, preserve whether electrification is required or preferred. Returned results must be described according to their actual available powertrain evidence.
> - Use `vin` only for an exact 17-character VIN. It finds that one current listing if available and never substitutes a similar vehicle.
> - Use the user's stated priority: best fit within budget, lowest price, lowest mileage, newest, or lower apparent purchase risk. Lower risk is a ranking preference based on available evidence, not a guarantee of safety, condition, or accident-free history.
> - Use the stated location. If a location is materially ambiguous, ask a focused question rather than guessing.
>
> The tool returns a concise set of current matching listings, available viewing links, and clear evidence about which requested criteria were confirmed, unconfirmed, or changed during the search. It does not treat missing history, ownership, certification, equipment, or specification data as proof that a vehicle fails—or meets—a request.

## Input contract boundaries

The goal is not to turn every interpretation into a category table. AI should still understand a phrase such as “large family SUV” or “good first car for my teenager” in the context of a request for listings. Code then maps selected candidates to provider fields, applies stable normalization, verifies the results, and returns the evidence.

| Input group | Public contract | Code responsibility | Field-audit position |
| --- | --- | --- | --- |
| Identity: make, model, year, VIN | Direct, concise requirements | Normalize make/model forms; exact live VIN lookup and verification | Keep. `model` is provider-variant-prone, so code normalization is required. |
| Budget, mileage, location | Direct numeric/location constraints | Build provider query; existing ZIP safeguards and widening logic | Keep. Location remains AI-led; do not add a new resolver solely for this redesign. |
| Body shape: `bodyType`, `vehicleType` | Both can be sent when the user expresses the relevant constraint | Preserve the existing V2 drop/retry, hard-exclude, and backfill safeguards | Keep both for now. They are not duplicates: `bodyType` maps the broadly-populated body-style field; `vehicleType` maps a distinct, inconsistently-tagged provider field. |
| Trim | Required versus preferred is intent | Normalize and enforce/relax locally as the current design requires | Keep. Raw provider trim is not a reliable hard filter. |
| Powertrain: fuel, drivetrain, transmission, cylinders | Direct technical requirements; hybrid/PHEV/EV requirement versus preference remains visible to the AI | Variant expansion, provider quirks, and evidence verification | Keep. `fuel` is structurally unreliable for hybrid/PHEV. Keep the concise V8-to-`cylinders` cue until routing tests prove it is unnecessary. |
| Equipment: interior colour, seats, doors | Direct request where the user states it | Preserve null/unknown semantics and existing post-verification behaviour | Keep. `interiorColor` has real filtering value but unreliable host routing; `seats` is evidence/ranking, not a provider hard filter. |
| Condition, history, ownership, CPO | User requirement or preference | Never infer pass/fail from missing data; return evidence state | Keep. Unknown must not become false. |
| Purchase priority | Short user priority | Deterministic scoring/risk classification and result explanation | Keep, but do not publish mechanics. |
| Practical need | Proposed narrow `vehicleNeeds` list: short listing-relevant phrases only; no prose history or transcript | Candidate/model selection, provider mapping, verification, and result evidence | Proposed rename/restriction; requires Claude feasibility review. |

## Explicit non-changes and safeguards

- Do not remove `vehicleType` simply to reduce apparent overlap. It must first pass equivalence testing against the previous E-Class, V90, and other problematic body/type cases.
- Do not remove the current `cylinders` or `interiorColor` guidance merely because it is concise. Both had host-routing reliability issues in prior testing.
- Do not turn practical needs into a static lifestyle-category table. The AI remains responsible for interpreting the request; code handles stable mapping and verification.
- Do not advertise the tool as independently proving reliability, safety, running cost, towing capability, condition, accident history, or certification.
- Do not place link labels, CTA rules, images, maps, Buyer Check, widening mechanics, risk calculations, or Auto.dev field mappings in the public description. If a user needs to see it, return it from code; if the AI should explain it, return structured evidence.

## Changes requiring Claude’s feasibility assessment

These are proposed contract changes, not instructions to alter the existing V2 code yet.

| Change | Proposed direction | What Claude must confirm |
| --- | --- | --- |
| `goals` → `vehicleNeeds` | Replace broad free-form goals with a short capped list of listing-relevant needs | Whether the host reliably sends the new field; cap/shape; how current intent parsing and scoring consume it. |
| Hybrid/PHEV/EV required vs preferred | Retain the distinction | The smallest schema representation that preserves current behaviour without adding broad prose. |
| Public `resolve_dealer_url` | Remove from the published surface | Whether it is needed for any host flow, and whether internal use can remain unchanged. |
| Main description compression | Replace the 2,767-word V1 main description with the Draft 0.1 candidate | Behavioural regression risks from removed instructions; which outcomes are already code-enforced versus still host-dependent. |
| Field descriptions | Rewrite as concise user-input definitions | Required wording for difficult fields without recreating the old routing manual. |
| Annotations and manifest metadata | Do not change by assumption | Confirm the existing values against the current OpenAI submission rules and actual read-only external-data behaviour. |

## Regression gate before any submission

Claude should run the existing automated/live tests and add focused cases before accepting any contract change. At minimum:

| Case | Expected protection |
| --- | --- |
| “Large family SUV” | AI interpretation produces listings; returned evidence does not claim independently-proven safety/reliability. |
| “First car for my teenager” | Practical need informs candidate choice; no unsupported safety or reliability guarantee. |
| Towing request | Requirement/preference remains visible; actual listing/spec evidence and verification gap are clear. |
| Hybrid/PHEV/EV, required and preferred | No accidental downgrade; returned powertrain status reflects available evidence. |
| Required versus preferred trim | Required trim is enforced where possible; a preference ranks rather than silently excludes. |
| V8 / cylinders and interior colour | Shorter descriptions do not cause the host to stop routing those fields. |
| `bodyType` plus `vehicleType` cases | Existing V2 retry/backfill safeguards preserve prior search quality. |
| Seats and doors | No false hard filtering; missing total doors stays unknown rather than wrong. |
| ZIP edge case | Existing control query prevents a non-geographic ZIP from collapsing the search. |
| Condition/history/CPO/ownership | Missing data remains unknown—not an automatic pass or fail. |
| Exact VIN | Only exact 17-character VIN lookup; no similar-car substitution. |
| Link/result rendering | Code returns required listing links and disclosure evidence without relying on description wording. |
| Out-of-scope advice | No tool call for general maintenance, financing, leasing, or non-listing comparisons. |

## Decision path

1. Review and amend this draft as a contract, without touching code.
2. Give Claude the approved contract plus the feasibility table.
3. Claude identifies exact V2-baseline schema/code deltas and runs the regression gate.
4. Review the implementation diff and live results.
5. Only then prepare the resubmission manifest and revisit the custom-domain decision.

## Open items for the next discussion

- Is `vehicleNeeds` the right public name, or is a clearer narrow label preferable?
- What is the minimum structured representation for “hybrid/PHEV/EV is required versus preferred”?
- Which concise field descriptions preserve host routing for `cylinders`, `interiorColor`, `vehicleType`, trim, and history without returning to a long manual?
- After Claude’s feasibility assessment, what should the measured full contract length (main description plus all field descriptions) be?

---

**Evidence consulted:** the submitted V1 manifest; the existing V2 baseline’s tool route and intent parser; prior discoverability/description review and regressions; the living Auto.dev field audit; and the current OpenAI app and MCP tool guidance. This draft preserves the earlier work’s hard-won behaviours while changing where the responsibility lives.