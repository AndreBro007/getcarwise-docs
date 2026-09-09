# CarClever V2 Current State — 2026-09-09

## Purpose

This is the current operational record for the amended V2 shared MCP contract, implementation, validation, and deployment. It supersedes stale “proposed,” “not yet coded,” and pre-cutover status statements in older documents, while preserving those documents as historical design records.

## Current source of truth

- Repository: `AndreBro007/carclever-find-my-car`
- Release branch: `release/v2`
- Merged correction: `5e8735e`
- Current deployed release nudge: `a9d6439`
- V2 production MCP endpoint: `https://ccfmc-dev-v2.vercel.app/mcp`
- Deployment: READY, production target
- V1/Anthropic production endpoint remains separate: `https://carclever-find-my-car.vercel.app/mcp`
- V3 remains excluded from the V2 contract and is not a V2 release target.

The V2 endpoint is the tested internal release endpoint. A final branded submission URL still requires domain routing/verification work; do not assume that `getcarwise.app` is attached to the V2 Vercel project.

## Implemented amended contract

The public input contract now uses:

- `vehicleNeeds` instead of `goals`; legacy `goals` is rejected through the real MCP registration path.
- `electrificationTypes`: `hybrid | plug_in_hybrid | electric`.
- `electrificationRequirement`: `required | preferred`.
- `hybrid` includes the internal `mild_hybrid` classification; callers cannot submit `mild_hybrid`.
- Required electrification uses confirmed NHTSA evidence and preserves shortfall disclosure.
- Preferred electrification changes ranking without excluding non-matches or unknown/ambiguous candidates.
- Practical needs and broad electrification requests require the host to resolve suitable real model names in `model`, alongside `vehicleNeeds`.
- The amended main description and all 31 field descriptions are aligned with `FINAL_DESCRIPTION_20260908.md`, including the approved electrification/model-resolution amendments and the concise `priorityAxis` routing hint.
- `resultsShown` is enforced in code as the final `results.length` and described on the output field, not as procedural narration in the main description.

## Verification completed

- ChatGPT and Claude V2 connector tests passed for practical family-SUV model resolution, hybrid/PHEV required searches, preferred electrification, mixed types, exact VIN/risk flows, priority axes, CPO/AWD/history constraints, legacy-`goals` handling, and the five-card display cap.
- Production build succeeds.
- Full suite: 222 custom checks plus 79 node tests, zero failures.
- One TypeScript error remains in `tests/best-for-budget-ranking.test.ts:105:39`; it was proven pre-existing against the exact `release/v2` baseline and is unrelated to this migration.
- Live NHTSA evidence confirms BEV and PHEV classification. Mild-hybrid real VINs returned blank NHTSA electrification levels; the mild-hybrid branch remains a documented real-world data-availability limitation. The blank-level/secondary-electric ambiguity fixture remains synthetic-only.
- `ELECTRIFICATION_POOL_SIZE = 20` remains provisional and unvalidated; it must not be described as empirically justified.

## Environment boundary

- V2 production is the current tested release.
- The Anthropic-reviewed V1 endpoint is untouched.
- V3 has historically generated preview deployments for V2 branches, but those were preview targets, not proof that V3 production serves V2. V3 branch/deployment filtering should be corrected separately.
- No connector URL should be changed until the final domain-routing decision is made. The MCP path convention is `https://<host>/mcp`.

## Documentation index

- Public contract: `FINAL_DESCRIPTION_20260908.md`
- Design ownership and electrification semantics: `ELECTRIFICATION_HANDOFF_DESIGN_20260908.md`
- Feasibility and equivalence package: `FEASIBILITY_EQUIVALENCE_PACKAGE_20260909.md`
- Equivalence gate: `V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md`
- Live validation record: `VALIDATION_GATES_20260909.md`
- Three-app/host transition: `HANDOFF_CLAUDE_SEO_AND_THREE_APP_TRANSITION_20260902.md`

## Remaining release work

1. Decide and configure the final stable branded MCP domain, including DNS/domain verification and a successful tool scan.
2. Keep the V1/Anthropic endpoint unchanged unless that submission is deliberately updated.
3. Correct V3 preview branch filtering separately.
4. Re-run the final submission smoke test against the exact endpoint submitted to OpenAI.
