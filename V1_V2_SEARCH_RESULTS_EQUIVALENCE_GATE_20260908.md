# V1 to V2 Search-Results Equivalence Gate

**Status:** Required design and test gate before any shared-contract implementation, OpenAI resubmission, or change to the Claude-reviewed contract.  
**Baseline:** Submitted V1 public contract and the existing tested V2 release branch.  
**Scope:** Vehicle-search behaviour only. V3 is excluded. No code change is authorised by this record.

## Governing rule

The public-description redesign may change where a behaviour is expressed, but it may not make vehicle finding less accurate.

“Same results” cannot mean identical VINs because live inventory, price, availability, and provider data change continuously. It means:

1. The same user request reaches the same effective hard constraints.
2. The same practical or electrification intent produces at least the same compatible model/trim candidate scope.
3. Existing V2 field-audit safeguards still control provider mapping, eligibility, and evidence.
4. Any result-set difference is an evidenced improvement, not an accidental loss of precision or recall.

A shorter public description is not accepted as a behavioural replacement on its own.

## What V1 actually did

The submitted V1 description was a 2,767-word operating manual. Some sections were presentation guidance, but several actively shaped search input before the call:

| V1 behaviour | Why it affected vehicle results | Current V2 code ownership | Equivalence status |
| --- | --- | --- | --- |
| Direct-field mapping: price, year, mileage, body style, drivetrain, transmission, colours, cylinders, doors, seating, condition | Determines provider query and local verification inputs. | Query building and post-verification already exist. | Retained, but concise-field host routing must be proven. |
| Practical need to resolved model list | Family, teen-driver, towing, commuter, and large-SUV prompts were resolved into model candidates. The model list is an eligibility filter, while goals is soft context only. | V2 does not derive model lists from goals; it uses the host-supplied model value. | **Open: critical.** |
| Hybrid/PHEV required versus preferred to variant list | Required requests excluded base-gas variants; preferences could include them. This avoided cheapest/budget ranking surfacing a gas variant instead. | V2 receives model/trim candidates and can enrich a final shortlist, but has no type-specific required/preferred input yet. | **Open: critical.** |
| Exact VIN lookup | Prevents a similar-vehicle substitute; checks other criteria against the exact listing. | Dedicated V2 VIN path. | Retained. |
| Required versus preferred trim | Required trim remains eligibility; preferred trim is ranking-only. | Local trim matching and stage-two confirmation. | Retained. |
| Automatic widening | Protects the requested priority dimension and discloses relaxation. | V2 widening ladder, post-verification, and bounded backfill. | Retained. |
| Unknown history/CPO/ownership | Unknown is not false; evidence is disclosed rather than used as a hard exclusion. | V2 evidence handling. | Retained. |
| Body type and vehicle type drift protection | Prevents provider tagging errors from erasing correct E-Class/V90 results. | V2 retry, exclusion, and backfill safeguards. | Retained. |
| City/state/no-location handling | V1 host resolved an unambiguous city to a representative ZIP, used state-wide search where appropriate, and did not guess ambiguous cities. | V2 handles ZIP/state after they are supplied; it does not geocode city text. | **Open: material.** |
| Priority interpretation | Separates best-within-budget from cheapest; protects newest/lowest-mileage/lower-risk intent. | V2 sorting and ranking code. | Retained, but host routing must be proven. |
| Lowest-mileage default | Omitted condition becomes used-only for lowest-mileage intent. | V2 effective-used rule. | Retained. |
| Provider mapping and data trust | Model normalization, no raw trim filter, seats evidence only, provider-fuel display only, null total handling, ZIP control query, local verification. | V2 code and audit safeguards. | Retained; must remain unchanged unless independently revalidated. |

## Critical no-regression requirements

### A. Practical needs must still generate candidate scope

VehicleNeeds replaces the public name goals; it does not give V2 a new capability to infer vehicle models by itself.

For requests such as “reliable car for a teen driver,” “large family SUV,” “commuter,” and “good for towing,” the approved design still relies on AI/host interpretation to provide suitable model/trim candidates. Code then performs stable provider translation and verification.

Therefore, before V1 wording is removed:

- The candidate shared contract must cause each host to provide compatible model/trim input where V1 did.
- VehicleNeeds must be carried as soft intent and not treated as a substitute for that candidate scope.
- Code must accept both goals and vehicleNeeds during migration, retaining the current seat hint and ranking/context semantics.
- No backend lifestyle/model category table is introduced.

If a host cannot reliably provide the model/trim candidates under the shorter contract, that specific minimal cue must be restored or a separate, tested structured hand-off designed. It must not be silently accepted as a generic unanchored search.

### B. Electrification must reproduce V1 selection logic

The proposed fields make an existing V1 distinction explicit:

- Electrification types state which types are acceptable.
- Required means only compatible model/trim candidates are selected before ranking.
- Preferred permits acceptable alternatives but ranks confirmed requested types above them.
- Public hybrid accepts conventional and mild hybrids; plug-in hybrid and electric remain distinct.
- Auto.dev vehicle.fuel is display-only. Gasoline never excludes a hybrid/PHEV candidate.

The V2 feasibility design must preserve V1’s protection against a cheaper gas model outranking a required hybrid/PHEV. It must also use NHTSA evidence without converting an unavailable decode into a false gasoline classification.

### C. Location must not become less capable

V1 supported an unambiguous named city by resolving it to a representative real ZIP. The shorter contract currently exposes ZIP/state but no direct city field or tested city-resolution mechanism.

The feasibility response must choose and test one of these equivalent behaviours:

1. Add a narrow city input and resolve it deterministically in code.
2. Retain a minimal, neutral host-routing cue that an unambiguous city is represented by a valid ZIP, with disclosure.
3. Explicitly narrow the tool’s supported location input to ZIP/state and reject city-only requests.

Option 3 is a regression and is not acceptable for the V1-equivalence target.

## API field-audit invariants

The living Auto.dev audit remains the authority for provider behaviour. The redesign must retain these rules exactly unless a new live validation changes them:

| Area | Required invariant |
| --- | --- |
| Vehicle model | Comma-separated candidate models remain eligible; normalize provider values and use tolerant local matching. |
| Vehicle trim | Never send raw trim as a provider hard filter; enforce required trim locally and treat preferred trim as ranking only. |
| Body style and vehicle type | Use broad body style directly; retain V2 named-model fallback, mismatch handling, and backfill for inconsistent finer type tags. |
| Seats | Evidence/preference only, never an Auto.dev filter. |
| Interior colour and cylinders | Keep direct fields and prove they are routed by both hosts; never replace a real field with manual inspection. |
| CPO, accidents, ownership | Evidence requests only; missing data is unknown, never negative proof. |
| ZIP/state | Retain ZIP validation, non-geographic ZIP control query, scope disclosure, and state-wide behaviour. |
| Vehicle fuel | Display only; never decide hybrid/PHEV eligibility from primary fuel. |
| NHTSA | Preserve raw electrification evidence and distinguish confirmed, unconfirmed, and conflicting evidence. |

## Required evaluation ladder

### 1. Deterministic input-contract tests

For every V1 regression prompt, assert the tool input and effective V2 query—not only the final natural-language response.

At minimum cover:

- Direct price/year/mileage/make/model filters.
- AWD/4WD, manual/automatic, exterior/interior colour, V8/V6/I4, doors, seats, new/used.
- Best-for-budget versus cheapest, newest, lowest-mileage, and lower-risk.
- Required and preferred trim.
- Family, teen-driver, large-SUV, commuter, and towing needs.
- Conventional/mild hybrid, PHEV, and EV as required and preferred.
- RAV4 Hybrid/Prime and F-150 PowerBoost-type variants.
- Exact VIN and unavailable VIN.
- Local ZIP, city-only, state-only, nationwide, invalid ZIP, and non-geographic ZIP.
- CPO, no-accidents, and one-owner unknown evidence.

### 2. Fixture-level candidate and result tests

Use captured provider/NHTSA fixtures to assert:

- The transformed query and local filters preserve V1 candidate eligibility.
- An ineligible gas variant cannot fill a required electrified shortlist.
- A known compatible hybrid is not rejected because provider fuel is Gasoline.
- Body/type drift, trim ambiguity, response-only seats, null totals, and history unknowns retain their V2 behaviour.
- Every returned result reports matching evidence consistently.

### 3. Live same-window A/B host tests

Run the same prompt set in the active V1 contract and the candidate contract, in both ChatGPT and Claude where available.

For each prompt record:

- Host-supplied tool input.
- Effective query and automatic relaxations.
- Candidate/result VIN set, recognizing live inventory drift.
- Whether each stated requirement was actually enforced, preferred, or evidenced.
- Latency and any host-routing omission.

A changed result is accepted only when the evidence shows an improvement or a live-data change—not because the shorter description caused a missing filter, missing model scope, or changed hybrid policy.

### 4. Release gate

No public-contract change proceeds until:

- Every critical V1 search-affecting behaviour above has an equivalent implementation and passing evidence.
- Every API-audit invariant remains covered.
- Both hosts pass their field-routing tests, including interior colour and cylinders.
- Any intentionally improved behaviour is documented with before/after evidence.
- The final description remains user-intent-focused and does not restore the V1 procedure manual.

## Required Claude feasibility response

Claude’s feasibility response must add a V1-equivalence section that answers:

1. How practical-needs prompts still produce model/trim candidate scope without a backend category table.
2. How required versus preferred electrification reproduces V1 candidate selection before price/ranking can prefer gas alternatives.
3. How city-only location is preserved.
4. Which existing V2 protections map to each API-field-audit invariant.
5. The deterministic fixtures and live A/B prompts that prove no behavioural regression.

No implementation should start until this gate is reviewed and approved.

## Sources

- Submitted V1 OpenAI manifest: https://github.com/AndreBro007/carclever-widget/blob/main/openai-submissions/carclever-find-my-car-1-0-0__7_.json
- Living API audit: https://github.com/AndreBro007/carclever-widget/blob/main/specs/Auto_Dev_Field_Audit_v1.md
- Existing V2 feasibility brief: https://github.com/AndreBro007/getcarwise-docs/blob/main/CLAUDE_V2_SHARED_CONTRACT_FEASIBILITY_BRIEF_20260908.md
