# Audit — V1 Special Field Instructions vs Short V2 Contract — 2026-09-11

**Status:** COMPLETE — read-only audit; no application code, deployment, connector, or submission changed  
**Scope:** Compare the submitted long V1 `find_matching_vehicle` description/schema with the current `release/v2` public contract and relevant implementation safeguards, specifically looking for behavior that may have been lost when the description was shortened.

## Executive conclusion

The shorter V2 contract did not simply drop the V1 operating manual. Most of the important provider/data-trust safeguards were deliberately moved into deterministic code or retained in concise field descriptions. However, this audit found **two concrete host-contract gaps already supported by live regression evidence, plus two additional areas that deserve focused testing before V2 is promoted**.

1. **`vehicleType` is the clearest material gap.** V1 explicitly separated broad body style (`bodyType`) from finer classification (`vehicleType`). V2 retained `vehicleType`, but its concise description still lists `SUV` as an example. ChatGPT Test #5 therefore sent both `bodyType: "SUV"` and `vehicleType: "SUV"`. The living Auto.dev audit already says provider `vehicle.type` is undocumented/inconsistently tagged and that description-only warnings historically failed. Claude V2 and ChatGPT V1 omitted `vehicleType` and both returned the same 13,617-match Denver universe; ChatGPT V2 repeatedly returned only 17. This is a real release-blocking contract/implementation issue, not just description polish.
2. **The V1 “do not invent hard filters” rule was materially weakened.** V1 explicitly told the host not to invent price/year/mileage/body-style/history/other hard filters not stated or clearly implied. The short V2 main description says it matches stated requirements but does not carry the same explicit anti-invention instruction. In current manual testing ChatGPT V2 invented `transmission: "Automatic"` in Tests #2 and #3. Claude did not. That recurrence is consistent with a missing host guardrail and should be treated as a second real contract-quality gap.
3. **Thin-search/retry ownership is now mostly code-owned, but host behavior is not fully constrained.** V1 explicitly said the tool automatically widens and told the host not to retry a thin search itself. V2 correctly moved bounded widening into code, but the short public description no longer clearly states that recovery is service-owned. Test #4 showed ChatGPT retrying repeatedly, rendering multiple widgets, substituting ZIP, and later V1 even cross-routing to another CarClever app. Re-adding coercive “don’t retry” language is not recommended because of Anthropic review concerns; a concise declarative contract signal and/or stronger structured terminal/recovery state should be considered by Engineering.
4. **`interiorColor` remains a known host-routing reliability risk.** The filter itself is proven, but historic repeated ChatGPT runs did not consistently send it. The short V2 field definition is now only “Requested interior colour,” whereas V1 explicitly mapped named interior colour to the field. `cylinders` is better preserved because V2 still contains the V8/V6/I4 mapping. Interior colour therefore merits one focused host test before release.

## Schema inventory check

The current `release/v2` schema contains the intended V2 field set: `vin`, price min/max/flexibility, priority, year min/max, make/model, `bodyType`, mileage, ZIP/radius/state, trim required/preferred, seating preference, `vehicleNeeds`, electrification types/requirement, drivetrain, transmission, exterior/interior color, `vehicleType`, doors, cylinders, used, CPO, no-accidents, and one-owner. Legacy `goals` is hard-rejected by `.strict()`.

No unrelated legacy field was found to have silently crept back into the public input schema. The problem is instead that **one deliberately retained field — `vehicleType` — is not safe under the current host-facing semantics for ordinary broad body-style requests.** The current source also directly maps supplied `vehicleType` to Auto.dev `vehicle.type`, so an unnecessary host-generated value becomes a real provider hard filter.

The Auto.dev client still has internal query capabilities such as CPO/history-related fields for lower-level use, but the public V2 semantics are not supposed to treat CPO/accident/ownership evidence as guaranteed hard exclusions. Current qualifier-accounting and route comments confirm `cpo`, `noAccidents`, `oneOwner`, and seating are deliberately handled as disclosed/evidence-based rather than exclusionary criteria.

## V1 special-instruction reconciliation

| V1 special behavior | Current V2 state | Code / design ownership | Audit verdict |
| --- | --- | --- | --- |
| Do not invent hard filters not stated or clearly implied | Only indirectly conveyed by “stated requirements”; no equally explicit field-use guardrail | Host-dependent | **GAP — live recurrence:** ChatGPT invented Automatic in Tests #2/#3 |
| Broad body style → `bodyType`; finer distinction → `vehicleType` | Both fields retained; `vehicleType` says “expressly distinguishes” but still gives `SUV` as example | Supplied `vehicleType` maps directly to provider `vehicle.type`; historical named-model fallback exists | **FAIL / GAP:** Test #5 proves recall loss on broad SUV request |
| Practical/lifestyle need → resolve real model list, not goals/body alone | Retained in main description + `model` + `vehicleNeeds` field descriptions | Host resolves; code normalizes model names | **PRESERVED**; prior discovery regression was fixed |
| Model values must omit manufacturer names | Retained with cross-brand example | Code strips known make prefixes and discloses correction | **PRESERVED WITH DEFENCE-IN-DEPTH**; hosts can still send bad values but code protects search |
| Hybrid/PHEV required vs preferred requires different candidate scope | Replaced with dedicated `electrificationTypes` + `electrificationRequirement`; main/model descriptions still require model/variant resolution | Deterministic NHTSA classification/verification + ranking | **PRESERVED / IMPROVED structurally**; continue required/preferred regression cases |
| Fuel label alone is insufficient for hybrid/PHEV | Explicitly retained | NHTSA classifier rather than raw fuel field | **PRESERVED** |
| Named trim defaults to required; soft wording uses preference | V2 has separate `trimRequired` / `trimPreference` definitions | Trim is not trusted as provider filter; required trim is locally enforced, preference ranks | **PRESERVED in schema/code**, though host interpretation should remain in regression suite |
| CPO/no-accidents/one-owner are evidence/disclosure, missing ≠ false | Retained in main/field semantics | `buildCpoSummary`, `buildHistorySummary`, qualifier accounting; never exclusion on missing evidence | **PRESERVED** |
| Minimum seating is not a trustworthy provider hard filter | `seatsMinPreference` explicitly calls itself preferred | Response evidence + disclosure only | **PRESERVED** |
| V8/V6/I4 maps to cylinder count, not displacement | Explicit mapping retained in `cylinders` definition | Provider filter is mechanically verified though undocumented | **PRESERVED**, but still a known host-routing watch item |
| Named interior/exterior colours map to dedicated fields | Dedicated fields retained; explicit mapping example removed | Provider filters work; historical ChatGPT routing inconsistency exists for interior colour | **PARTIAL / TEST NEEDED**, especially interiorColor |
| New/used condition explicit; unspecified searches both | Retained in `used` field | Provider condition filtering + local verification | **PRESERVED** |
| `lowest_mileage` defaults to used unless user states otherwise | No longer stated in the short public field description | Existing project state/field audit and Sep 6 V2 live test record confirm server behavior still defaults `lowest_mileage` to `used: true` and discloses it | **PRESERVED IN CODE**; do not rely on host to invent `used` |
| Budget ≠ cheapest; “best for budget” → best_for_budget | Initially lost in short-contract discovery, then explicitly restored | `priorityAxis` description + deterministic sort/ranking | **PRESERVED** |
| Approximate price only → flexible; otherwise strict | Concise `priceFlexibility` definition retained | Widening code raises price only when flexible | **PRESERVED** |
| Automatic widening protects explicit priority and never silently changes constraints | Main procedural prose removed | `loosening-ladder.ts` owns bounded radius/mileage/year/price widening, priority-axis protection, strict-price protection and disclosures | **PRESERVED IN CODE**, but host self-retry behavior is a contract/presentation watch |
| ZIP/location edge cases and scope disclosure | City-ZIP anchor and scope disclosure retained concisely | Existing ZIP validation/control-query and geo logic; invalid-ZIP behavior observed in Test #4 | **MOSTLY PRESERVED**, with host retry UX watch |
| Every applied hard constraint is checked/reported | Short description says confirmed/unconfirmed/changed criteria | Post-verification + constraint evidence + qualifier accounting | **PRESERVED**, although provider-stage false negatives such as `vehicleType` cannot be recovered merely by checking survivors |
| Exact VIN must not substitute a similar vehicle | Explicitly retained | Exact-VIN path | **PRESERVED** |
| Result links/trust/disclosure rules | Much V1 presentation prose removed | Link resolution, card/output schema, risk/history summaries | **DELIBERATELY CODE/OUTPUT-OWNED** |

## Why `vehicleType` escaped the Sep 8 discovery run

`FINAL_FINDINGS_20260908.md` recorded “vehicleType” among direct fields that tested clean. That result was too broad as a conclusion. The current failure is a different semantic shape: the user asked only for the broad category “SUV,” and ChatGPT duplicated that into both broad `bodyType` and finer `vehicleType`. The earlier discovery work did not establish that `vehicleType` is safe as a redundant broad filter; the living field audit already documented the opposite risk for provider `vehicle.type`.

The short-contract design itself also said `vehicleType` should be used only when the user **expressly distinguishes** a finer classification, but retained “SUV” as one of the examples. Those two ideas conflict in practice. Test #5 is strong evidence that ChatGPT interpreted the example more strongly than the qualifier.

## Recommended release-blocking actions before further broad regression

These are **requirements for Claude's engineering lane**, not line-level implementation instructions:

1. Treat Test #5 as the canonical regression fixture. Broad “SUV” must not acquire a redundant provider `vehicle.type=SUV` restriction merely because `vehicleType` exists in the public schema.
2. Re-evaluate whether `vehicleType` needs to remain a public input at all. If retained, its semantics and server-side safeguards must make broad-body duplication harmless; a description-only warning is insufficient because that approach already failed historically.
3. Restore the **semantic effect** of V1's anti-invention rule in the shortest compliant form: direct hard-filter fields should represent constraints the user actually stated or clearly implied. This should specifically prevent unrequested transmission/body/condition/etc. constraints. Do not simply restore the entire V1 procedural manual.
4. Make thin-result/recovery ownership clear without recreating Anthropic's prohibited “always/must/never call” style. The service already owns bounded widening; the host should have enough declarative information not to independently retry/change geography unless the returned state calls for user input.
5. Add focused host checks for `interiorColor`, `cylinders`, required/preferred trim, and a lowest-mileage request **without explicitly saying used**, because these are exactly the areas where V1 carried special instructions or server defaults that a shorter contract can conceal.
6. After any fix, rerun the exact Denver Test #5 on ChatGPT V2 and Claude V2, then continue the existing regression bank only after parity is restored.

## Schema decision status

- **Confirmed problem:** current public `vehicleType` semantics are unsafe for broad-body requests on ChatGPT.
- **Proposed, not yet André-confirmed:** remove `vehicleType` from the public schema entirely versus retain it with stronger deterministic gating. Engineering should assess the smallest safe option; this audit does not make that product decision final.
- **No evidence of other accidental schema reintroduction:** `goals` remains rejected and the remaining public fields correspond to the approved V2 contract.
- **Do not remove evidence-only fields merely because they are not provider hard filters:** seating/CPO/history fields deliberately exist to express user intent and report evidence without treating unknown as false.

## Sources reviewed

- Submitted V1 OpenAI manifest: `carclever-widget/openai-submissions/carclever-find-my-car-1-0-0__7_.json`
- Living provider audit: `carclever-widget/specs/Auto_Dev_Field_Audit_v1.md`
- Short V2 contract: `getcarwise-docs/FINAL_DESCRIPTION_20260908.md`
- Shared-contract design: `getcarwise-docs/DRAFT_SHARED_TOOL_CONTRACT_V0_2_20260908.md`
- Discovery findings: `getcarwise-docs/FINAL_FINDINGS_20260908.md`
- Current V2 state / validation: `CURRENT_V2_STATE_20260909.md`, `VALIDATION_GATES_20260909.md`
- Read-only current `release/v2` source reviewed: `lib/find-matching-vehicle-input.ts`, `lib/auto-dev-client.ts`, `lib/intent-parser.ts`, `lib/loosening-ladder.ts`, `lib/local-ranking.ts`, `lib/qualifier-accounting.ts`, `lib/constraint-evidence.ts`, `lib/post-verify.ts`, and `app/[transport]/route.ts`.

## Bottom line

The short description strategy is still sound, but **shortening cannot remove semantic guardrails that only the host can enforce unless those guardrails are moved into deterministic code**. Test #5 exposed exactly that boundary. The next engineering pass should focus on making the public schema safe-by-construction where possible, then leaving the description to explain user semantics rather than provider quirks.