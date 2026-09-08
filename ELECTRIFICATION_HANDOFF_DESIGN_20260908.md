# Electrification Handoff — Shared Tool Contract Design

**Status:** Decision draft. No active submission, schema, code, or deployment is changed.  
**Scope:** Preserve accurate hybrid/PHEV/EV listing searches while moving deterministic field translation and verification out of the public description.  
**Baseline:** Existing V2 code; V3 is excluded.

## What the existing design does

The current V1 description carries the operational logic because Auto.dev does not offer a reliable electrification filter:

- `vehicle.fuel` is not a safe filter for hybrid or PHEV. A hybrid can correctly report primary fuel as gasoline, and the provider has no secondary-electrification field.
- AI currently resolves a natural-language request into model variants. For a named model, a required request sends electrified variants only; a preference may include the base model and electrified variants.
- Trim is relevant for some configurations, notably cases such as F-150 PowerBoost where electrification is represented in a trim/variant rather than a separate model name.
- Current V2 code normalizes provider fuel display, applies a conservative known-hybrid-only override, and decodes shortlisted VINs through NHTSA. NHTSA returns electrification and secondary-fuel evidence and has already corrected real provider misses.
- Today, NHTSA is an informative final-shortlist check. The current helper can answer “electrified or not,” but does not yet expose a complete required-vs-preferred eligibility/ranking contract.

This explains why the long V1 description became detailed: it was compensating for an unreliable provider field and for the absence of a structured hand-off.

## Design constraints

1. AI keeps natural-language interpretation and model/trim knowledge. No broad, changing lifestyle or model-variant table is introduced.
2. Code owns stable translation, verification, and result handling.
3. “Required” and “preferred” remain distinct.
4. The public schema stays small, explicit, and purpose-related.
5. Auto.dev `vehicle.fuel` alone never confirms or rejects an electrification request: a hybrid may correctly report primary fuel as gasoline. Required matching must combine compatible model/trim identity with NHTSA electrification evidence where available.
6. A preference may rank verified electrified results ahead of acceptable non-electrified alternatives.
7. Existing V2 trim semantics remain intact.

## Options

| Option | Shape | Strength | Problem |
| --- | --- | --- | --- |
| H1. No new field | Continue to encode the distinction only in AI-selected `model`, `trimRequired`, and prose `vehicleNeeds` | No schema change | Code cannot reliably know whether electrification was required or merely preferred; too much remains dependent on model procedure. |
| H2. One combined enum | `electrification: hybrid_required | hybrid_preferred | plug_in_hybrid_required | …` | Flat and host-friendly | Becomes awkward when multiple types are acceptable, such as hybrid **or** PHEV. |
| H3. Two flat fields | `electrificationTypes: ["hybrid", "plug_in_hybrid", "electric"]`; `electrificationRequirement: "required" | "preferred"` | Explicit, stable, supports one or several acceptable types, and separates “what” from “how important.” | Requires a small schema/code change and host-routing tests. |
| H4. Nested object | `electrification: { types, requirement }` | Semantically tidy | More complex for host schema routing; no benefit over H3. |

## Recommended candidate — H3

Use two optional, flat fields:

| Field | Candidate definition |
| --- | --- |
| `electrificationTypes` | Acceptable electrified powertrain types: `hybrid`, `plug_in_hybrid`, and/or `electric`. |
| `electrificationRequirement` | Whether the stated electrification types are `required` or `preferred`. |

Examples of the meaning—not instructions to the host:

| User intent | Structured meaning |
| --- | --- |
| “Only a RAV4 Hybrid or Prime” | types: hybrid, plug_in_hybrid; requirement: required |
| “A hybrid would be nice, but show normal RAV4s too” | types: hybrid; requirement: preferred |
| “Cheapest electric SUV” | types: electric; requirement: required |
| “F-150 PowerBoost” | types: hybrid; requirement: required, plus the applicable model/trim intent |

This is a small stable technical taxonomy, not a changing category table. The AI still determines that a phrase refers to a hybrid/PHEV/EV and resolves appropriate model/trim candidates; code receives the durable fact it needs to enforce and explain the result.

## Proposed ownership split

| Stage | Owner | Responsibility |
| --- | --- | --- |
| Natural-language request | AI | Recognise hybrid, PHEV, EV, “only,” “must,” “prefer,” and trim-like configurations. |
| Input hand-off | Shared schema | Carry accepted electrification type(s) and required/preferred strength explicitly. |
| Candidate model/trim selection | AI, with code normalization | Resolve appropriate model/variant names without a giant backend model table. |
| Provider query | Code | Apply stable provider mapping and current V2 query safeguards. |
| Final verification | Code | Use provider data plus NHTSA VIN evidence to classify a returned vehicle’s actual electrification. |
| Required request | Code | Select compatible model/trim candidates and return the evidence state. Auto.dev fuel is display-only, never contrary evidence; any stricter NHTSA-based exclusion needs feasibility and regression proof. |
| Preferred request | Code | Keep acceptable alternatives but rank confirmed matching electrification above them and disclose evidence. |
| User explanation | Result evidence | State confirmed, unconfirmed, or changed powertrain status; do not rely on host prose to infer it. |

## Claude feasibility questions

1. Can `electrificationTypes` and `electrificationRequirement` be added to the V2-baseline schema without reducing host field-routing reliability?
2. Does the query path have enough candidate breadth before final VIN verification to enforce a required request without hiding genuine variants?
3. What normalised result enum should code derive from NHTSA’s `ElectrificationLevel`, primary fuel, and secondary fuel—specifically distinguishing hybrid, PHEV, and EV rather than only “electrified”?
4. Define the evidence states that combine model/trim identity and NHTSA confirmation. NHTSA currently runs only after shortlist selection, so it must not become an exclusion gate without testing candidate breadth, latency, and false-negative risk.
5. How should trim-like electrified variants such as PowerBoost interact with `trimRequired` when the user did not name the trim directly?

## Decision requested

Approve H3 as the intended shared-contract shape, subject to Claude feasibility and regression testing; or select H1/H2/H4 with an explicit rationale.

## Required regression cases

- RAV4 hybrid/PHEV required versus preferred;
- unnamed hybrid SUV required;
- EV required;
- F-150 PowerBoost / other trim-like electrified configuration;
- verified hybrid with provider fuel reported as gasoline;
- Auto.dev gasoline value on a confirmed hybrid;\n- unavailable versus authoritative NHTSA electrification evidence;\n- unambiguous model/trim mismatch;
- hybrid/PHEV plus explicit trim requirement;
- price-priority request where a cheaper gasoline result competes with a required electrified result.

## Evidence consulted

- [Living Auto.dev field audit](https://github.com/AndreBro007/carclever-widget/blob/main/specs/Auto_Dev_Field_Audit_v1.md): `vehicle.fuel` is unsuitable as a hybrid/PHEV filter; model-name resolution and NHTSA evidence are required.
- Existing V2 `fuel-type.ts`, `nhtsa-client.ts`, `trim-match.ts`, and route logic: provider fuel normalization, known-hybrid correction, NHTSA final-shortlist decode, and local trim semantics.


## Audit correction — 2026-09-08

The earlier shorthand “provider gasoline result” was incorrect and must not drive eligibility.

The living field audit establishes that Auto.dev `vehicle.fuel = "Gasoline"` can be technically correct for a hybrid’s **primary** fuel. Auto.dev lacks a secondary/electrification field, so a hybrid and a plain gasoline vehicle are indistinguishable from `vehicle.fuel` alone. It remains display-only.

The correct evidence order is:

1. **Candidate selection:** AI resolves compatible model and, where needed, trim/variant names. This remains the current V2 mechanism.
2. **Provider fuel:** display-only; it neither includes nor excludes an electrified candidate.
3. **NHTSA VIN evidence:** authoritative electrification/secondary-fuel confirmation for the final shortlist, with the existing provider-display override.
4. **Result claim:** a candidate is described from the combined evidence. A bare/ambiguous model with no confirmation must not be described as a confirmed hybrid/PHEV/EV; a known hybrid variant is not rejected merely because Auto.dev says gasoline.

This correction leaves H3's two-field hand-off as an option, but it removes the premature proposal to hard-exclude a candidate solely because provider fuel is gasoline or NHTSA is unavailable. Whether NHTSA should ever become an eligibility gate is a separate Claude feasibility and regression decision.
