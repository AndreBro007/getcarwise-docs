# Handoff — V2 Shared Tool-Contract Feasibility

**From:** ChatGPT business/strategy lane  
**To:** Claude engineering lane  
**Status:** Investigation only. No implementation, deployment, connector change, or submission is authorised.  
**Priority:** Active, separate lane. V3 pause is requested pending Claude’s safe-state confirmation.

## Why this handoff exists

OpenAI rejected the submitted CarClever - Find My Car V1 app because the tool surface requested overly broad or unnecessary input and the tool description/name metadata did not meet the required quality bar.

The current V1 description is a 2,767-word operating manual. It was carefully developed because some of its content genuinely drives correct search input and results. The goal is not simply to shorten it. The goal is to move stable provider mapping, verification, and safeguards into code or structured result evidence while retaining the same or better vehicle-search results.

The active V1 contract is also still under Anthropic review. Do not change it, its MCP URL, its code, its Vercel project, its connector, or its review submission. This handoff is preparation for a later, separate decision about a future shared OpenAI/Anthropic contract.

## Workstream boundary

This is a future OpenAI resubmission candidate built from the existing tested V2 baseline. It is not a new V2 release and it does not redefine V2.

V3 pause is requested while this feasibility investigation runs. Before beginning this work, record and confirm the current V3 safe state; do not then continue, merge, repoint a connector, deploy, or start another V3 phase. André will separately instruct the V3 agent to stop.

Use no V3 tool or capability in this workstream.

## Product decisions already made

1. Try one shared public tool description for OpenAI and Anthropic. Platform submission metadata may differ, but public semantics should not drift.
2. Keep the description neutral and user-intent-focused. Do not reproduce the V1 procedure manual, forced invocation, never-refuse language, mandatory tool chaining, broad context collection, or provider implementation instructions.
3. Preserve V1 discovery cues: current listings, explicit criteria, lowest price, newest, lowest mileage, best within budget, practical needs, and exact VIN.
4. Public vehicleNeeds replaces goals. The server must accept both during migration, with the same soft-intent role.
5. AI/host retains natural-language interpretation and appropriate model/trim candidate selection. Code owns stable Auto.dev translation, field-audit safeguards, verification, ranking, and result evidence. Do not build a changing lifestyle/model category table.
6. Electrification is first-class. Public hybrid includes conventional and mild hybrids; plug-in hybrid and electric remain distinct. Required and preferred must behave differently.
7. Auto.dev vehicle.fuel is display-only. Gasoline never disproves or excludes a hybrid/PHEV candidate.
8. The user-facing product remains accurate matching. Internal data-trust machinery should remain invisible unless uncertainty materially affects the decision.

## V1-equivalence gate

The redesign is blocked until Claude can show how the V2 baseline preserves:

1. Practical-need prompts producing the same model/trim candidate scope as V1.
2. Required versus preferred electrification before price/ranking can select a cheaper gas alternative.
3. City-only location handling.
4. Every existing Auto.dev field-audit safeguard.
5. Deterministic and live same-window A/B evidence in both hosts.

The precise requirements and test ladder are in the V1 to V2 search-results equivalence gate linked below.

## Required Claude response

Return a feasibility response only. Do not modify code.

1. Exact proposed schema and code deltas from the existing V2 baseline.
2. How each V1 search-affecting rule is retained, moved, or improved.
3. The minimal safe implementation for practical needs, electrification, and city-only location without a broad category table.
4. A mapping from every relevant API-field-audit rule to V2 code ownership and regression coverage.
5. Deterministic fixtures, host-routing tests, and live A/B tests required before implementation.
6. Any reason the common public contract cannot work for OpenAI or Anthropic.
7. A clear recommendation: proceed, revise the design, or retain a platform-specific variation.

## Explicitly out of scope

- Any source-code change, branch operation, merge, deployment, Vercel configuration, connector repoint, or test run that changes an external service.
- Any OpenAI resubmission or Anthropic submission/review change.
- Any V3 work.
- Applying the proposed GetCarWise custom domain. The custom domain is a later V2 resubmission decision, after this design and feasibility work is approved.

## Source records

- Shared-contract feasibility brief: https://github.com/AndreBro007/getcarwise-docs/blob/main/CLAUDE_V2_SHARED_CONTRACT_FEASIBILITY_BRIEF_20260908.md
- V1 to V2 search-results equivalence gate: https://github.com/AndreBro007/getcarwise-docs/blob/main/V1_V2_SEARCH_RESULTS_EQUIVALENCE_GATE_20260908.md
- Independent V2 electrification audit: https://github.com/AndreBro007/getcarwise-docs/blob/main/INDEPENDENT_V2_ELECTRIFICATION_FEASIBILITY_AUDIT_20260908.md
- Shared contract candidate: https://github.com/AndreBro007/getcarwise-docs/blob/main/DRAFT_SHARED_TOOL_CONTRACT_V0_2_20260908.md
- OpenAI/Anthropic compatibility decision: https://github.com/AndreBro007/getcarwise-docs/blob/main/PLATFORM_TOOL_DESCRIPTION_COMPATIBILITY_DECISION_20260908.md
- Current V1 Anthropic feedback audit: https://github.com/AndreBro007/getcarwise-docs/blob/main/CLAUDE_CURRENT_V1_ANTHROPIC_FEEDBACK_AUDIT_20260908.md
- Living Auto.dev field audit: https://github.com/AndreBro007/carclever-widget/blob/main/specs/Auto_Dev_Field_Audit_v1.md

## Handoff discipline

Keep this workstream distinct from V3 in branch names, notes, test results, and discussions. First confirm and record V3's safe stopping point. If a question would require changing an active review, a deployed connector, or V3 work, stop and return it for André’s decision.
