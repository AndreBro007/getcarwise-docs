# Independent V2 Feasibility Audit — Electrification Contract

**Status:** Read-only audit of `release/v2` at `fca5013c786dced45272f27f2a227a3ca9453a7a`.  
**Purpose:** Assess whether the approved shared public contract can be implemented from the existing tested V2 baseline without weakening search accuracy.  
**Scope:** No V3 tools or capabilities. No code, deployment, or submission changes.

## Conclusion

The design is feasible, but V2 cannot truthfully support the proposed `required` versus `preferred` electrification contract with its current boolean helper alone.

V2 has strong foundations:

- AI/host already resolves compatible model and trim variants before the server query.
- Auto.dev's `vehicle.fuel` is correctly treated as insufficient for hybrid/PHEV identity.
- NHTSA VIN decode already runs in parallel for the final shortlist and preserves raw `ElectrificationLevel`, `FuelTypePrimary`, and `FuelTypeSecondary`.
- The code already distinguishes a strict required trim from a ranking-only trim preference, and it preserves unknown-versus-false evidence handling.

The missing capability is a bounded, type-specific eligibility and evidence stage. Existing `nhtsaIndicatesElectrified()` returns only `true` / `false`; it cannot distinguish a conventional hybrid, plug-in hybrid, battery electric vehicle, mild hybrid, an unavailable decode, or an ambiguous source value.

## Evidence from V2

| Area | Current V2 behaviour | Feasibility implication |
| --- | --- | --- |
| Public input | `goals: string[]` is the sole practical-needs input. | Add public `vehicleNeeds`; accept both names during migration. |
| Candidate generation | The host resolves relevant model/variant names; V2 queries Auto.dev with those names. | Keep AI/host interpretation. Do not introduce a backend suitability/model table. |
| Auto.dev fuel | Provider fuel is shown but is not reliable hybrid/PHEV evidence. | Never use it to include or exclude an electrification request. |
| Final shortlist | V2 fetches full details and NHTSA decode only for the selected shortlist. | Suitable for evidence, but insufficient on its own for a strict required-type outcome. |
| NHTSA | Raw type-relevant fields are available but reduced to a boolean helper. | Add a canonical classifier with raw-source preservation. |
| Ranking/output | Cards can expose badges, constraint checks, intent confirmations, and data conflicts. | Add structured electrification evidence; do not rely on host prose. |

## Required code design

### A. Input and compatibility

Add:

- `vehicleNeeds?: string[]`
- `electrificationTypes?: ("hybrid" | "plug_in_hybrid" | "electric")[]`, where public `hybrid` includes conventional and mild hybrids
- `electrificationRequirement?: "required" | "preferred"`

During the migration period, accept both `goals` and `vehicleNeeds` and merge/deduplicate them into the existing soft-intent representation. `vehicleNeeds` remains capped and listing-relevant; it is not a transcript or broad profile channel.

`electrificationRequirement` must be rejected or ignored as incomplete when no type is supplied; a strength without a type has no meaning.

### B. Canonical electrification evidence

Replace the boolean-only helper with a classifier that returns both a canonical state and raw NHTSA evidence, for example:

- `hybrid`
- `plug_in_hybrid`
- `electric`
- `mild_hybrid`
- `not_electrified`
- `unknown`
- `ambiguous`

The mapping must be fixture-backed from actual NHTSA responses. It must not infer a type from the Auto.dev primary-fuel label. The raw NHTSA values must remain available for debugging and future drift review.

### C. Candidate selection for required versus preferred

**Preferred:** retain compatible variants, rank confirmed requested types above unconfirmed compatible variants, and disclose the evidence state. A non-electrified result must not be represented as satisfying the preference.

**Required:** preserve the current AI/host model-and-trim resolution, but make the returned shortlist type-safe. A confirmed different type is excluded. A known compatible variant whose NHTSA record is unavailable is not reclassified as gasoline and must be reported as unconfirmed, not confirmed.

The key feasibility question is how V2 gets enough type-confirmed candidates before it takes the final shortlist. Today it decodes only the already-selected 5–8 VINs. A safe approach is a **bounded expanded verification pool** for required requests:

1. use only model/trim variants compatible with the requested type(s);
2. retain the existing full-detail, hard-constraint, trim, and widening safeguards;
3. NHTSA-decode a bounded candidate pool larger than the displayed shortlist;
4. select the final displayed results from confirmed requested types;
5. if confirmation is unavailable, return fewer results or a clear unconfirmed outcome rather than filling the list with gas variants.

The implementation must measure latency, NHTSA availability, and final-candidate breadth before setting the exact pool size. NHTSA must not become an unbounded pre-search gate.

### D. Mild hybrids: resolved public behaviour

Public `hybrid` includes both conventional and mild hybrids. This avoids excluding vehicles that ordinary users reasonably expect in a hybrid search. `plug_in_hybrid` and `electric` remain distinct types.

Internal classification must still keep `mild_hybrid` distinct from conventional hybrid. This is evidence precision, not a separate user-facing taxonomy: a verified mild hybrid may be labelled accurately, and it satisfies a public `hybrid` request. It must not satisfy a `plug_in_hybrid` request.

## Regression gate additions

In addition to the existing V2 suite, add deterministic fixtures and controlled live smoke tests for:

- conventional hybrid, mild hybrid, plug-in hybrid, and battery electric;
- public `hybrid` (covering conventional and mild), plug-in hybrid, and electric as both `required` and `preferred`;
- a hybrid whose Auto.dev primary fuel is Gasoline;
- a confirmed different electrification type;
- compatible named model/trim with unavailable or ambiguous NHTSA response;
- F-150 PowerBoost and another model-family/variant case;
- existing direct VIN, trim-required, exact-price, body/vehicle type, color, cylinders, seats, and location regressions;
- behaviour when fewer than the normal shortlist count can be confirmed.

## Implementation boundary

This audit supports a **feasibility response only**. It does not authorize code changes. Before implementation, Claude should propose the exact schema, classifier mapping, bounded-pool behaviour, result evidence shape, and test fixtures, then we review those choices together.

## Related records

- [Shared contract candidate](https://github.com/AndreBro007/getcarwise-docs/blob/main/DRAFT_SHARED_TOOL_CONTRACT_V0_2_20260908.md)
- [Electrification hand-off design](https://github.com/AndreBro007/getcarwise-docs/blob/main/ELECTRIFICATION_HANDOFF_DESIGN_20260908.md)
- [Claude feasibility brief](https://github.com/AndreBro007/getcarwise-docs/blob/main/CLAUDE_V2_SHARED_CONTRACT_FEASIBILITY_BRIEF_20260908.md)
