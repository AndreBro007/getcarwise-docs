# Can CarClever Use One Tool Description Across OpenAI and Anthropic?

**Decision purpose:** determine whether the future CarClever listing-search tool should use one shared public description, or separate OpenAI and Anthropic descriptions.  
**Scope:** description and public input guidance only. The current Claude review remains unchanged. The future OpenAI candidate remains a draft. This does not approve a resubmission or any code change.  
**Evidence:** current OpenAI and Anthropic first-party tool documentation, the historic Anthropic directory feedback supplied by André, and the submitted CarClever V1 contract.

## Executive answer

**Yes: one shared future tool description is feasible. The two platforms are not too far apart to attempt it.**

The shared description cannot be the current 2,767-word V1 operating manual, and it should not be the current OpenAI Draft 0.1 unchanged. It needs a deliberate common middle: a neutral, sufficiently detailed explanation of capability, user-intent boundary, material input semantics, returned evidence, and limitations.

The real split is not “short for OpenAI versus long for Anthropic.” It is:

- OpenAI: describe **user intent**, request only the minimum purpose-related input, and do not expose implementation.
- Anthropic: provide **enough detail** about tool behaviour, parameters, and limitations for reliable tool use.
- Historic Anthropic directory feedback: do not use tool descriptions to force calls, override judgement/refusal, or compel tool chains.

Those requirements are compatible. A neutral declarative description can satisfy all three.

## Side-by-side requirements and fit

| Decision area | OpenAI requirement | Anthropic requirement | Can one description fit? | Shared formulation |
| --- | --- | --- | --- | --- |
| Purpose and trigger | State the user goal and conditions that trigger the tool; describe user intent, not implementation. | Explain what the tool does and when it should and should not be used. | **Yes — direct overlap.** | “Finds current US vehicle listings when a user wants vehicles for sale or a shortlist; it is not for general vehicle advice.” |
| Detail level | Be clear/accurate, but do not use overly broad triggering or internal terminology. | Detailed description is the strongest tool-performance factor; include parameter meaning/effects and important limitations. | **Yes — with disciplined detail.** | Give user-visible parameter semantics and limits; exclude Auto.dev mapping, retry ladders, scoring formulas, and UI mechanics. |
| Inputs | Request only the minimum information directly related to the stated purpose; no broad context, transcript, or “just in case” inputs. | Explain each parameter’s meaning and how it affects behaviour. | **Yes — direct complement.** | Keep a narrow schema; give concise descriptions for the fields retained. A narrow `vehicleNeeds` field can work only if it is task-specific and bounded. |
| Practical needs | The trigger must remain a vehicle-listing request; avoid broad “general advice” triggering. | Detail can help Claude interpret optional/complex inputs and caveats. | **Yes.** | A practical need can guide listing selection, but it is not proof of reliability, safety, running cost, or towing capability. |
| Tool-selection control | Tool descriptions decide selection; do not manipulate selection beyond explicit user intent. | Historic directory feedback prohibits “always invoke,” “never refuse,” or forced multi-tool sequences in a description. | **Yes — shared prohibition.** | Describe conditions and outcomes neutrally. Do not tell the model to always call, never refuse, or call another tool first. |
| Input-construction procedure | Explicit inputs are needed for correctness, but the description should not expose implementation. | Detail improves tool use, but the historic review distinguishes detail from agent-control instructions. | **Yes — move procedure down a level.** | Field descriptions state semantics; code performs stable mapping/normalization. Use neutral examples only if the actual platform path supports them. |
| Result/evidence | Return structured, reusable information and explain important limitations. | Return high-signal information useful for reasoning; avoid unnecessary context. | **Yes — direct overlap.** | Return listing links plus confirmed/unconfirmed/changed evidence; keep deterministic disclosure in code. |
| Tool count/name | Clear, unique, accurate names; avoid overlapping descriptions. | Fewer related operations reduce selection ambiguity; clear names help selection. | **Yes.** | One public `find_matching_vehicle` remains compatible. `resolve_dealer_url` can remain internal unless a real host flow proves it needs public access. |

## The actual differences

### 1. Detail is the only meaningful description-level tension

OpenAI’s instruction is to describe the user intent rather than the implementation. Anthropic asks for detailed tool behaviour, parameter effects, and limitations.

That does **not** require two descriptions. It requires a description that is detailed about the product contract, not the backend algorithm.

| Detail type | One shared description? | Reason |
| --- | --- | --- |
| What users can ask for | Keep | Required by both. |
| What counts as in scope/out of scope | Keep | Required by both. |
| What each retained field means to the search | Keep, concise | OpenAI needs explicit inputs; Anthropic benefits from parameter semantics. |
| Required versus preferred | Keep | User-visible behaviour, not internal implementation. |
| Practical need versus verified fact | Keep | Material limitation and trust boundary. |
| Exact-VIN limitation | Keep | Material input behaviour and limitation. |
| Provider-specific field mapping | Remove from shared public description | Implementation detail; code owns it. |
| Auto.dev quirks, query fallbacks, model-prefix cleanup | Remove | Implementation detail. |
| Widening ladder, risk formula, scoring mechanics | Remove from description; return outcomes/evidence from code | Both platforms benefit more from deterministic results than model procedure. |
| Links, CTA wording, maps, card formatting | Remove | Presentation logic, not tool selection or parameter semantics. |

### 2. Anthropic-only enrichment is possible, but not required for a shared description

Anthropic’s client-tool documentation supports optional `input_examples` for complex inputs, but it says this feature is not supported for server tools or client toolsets. A remote MCP submission therefore should **not** depend on Anthropic examples as the mechanism that makes the tool work.

If the exact Claude submission path later supports a platform-specific example mechanism, examples could be an enrichment. They would be metadata around the shared description—not evidence that the base description must fork.

### 3. Platform-specific metadata is unavoidable, but is not a second description

Submission forms, annotations, test cases, privacy declarations, icons, and review explanations differ by platform. That is normal. The decision here concerns the tool’s public capability description and field semantics.

## Where the two existing texts sit

| Text | Fit with a single shared future description | Why |
| --- | --- | --- |
| Current shared V1 (2,767 words) | **Too implementation-heavy as a shared final form** | It includes valuable behaviour, but mixes user intent, agent procedure, Auto.dev mapping, widening, ranking, output/presentation, and host workarounds. It is more than either platform needs in the public tool description. |
| Future OpenAI Draft 0.1 (414 words) | **Closer, but not yet a common description** | It has the right responsibility split and evidence boundary, but it was written for the OpenAI redesign. It needs a conscious common-contract review—not automatic adoption by Claude. |
| Proposed common description | **Viable** | Neutral, declarative, materially detailed, narrow input contract; field semantics and code own the rest. |

## What a single shared description must contain

A common description can be structured in five short sections:

1. **Capability and trigger**  
   Current US vehicle listings or a shortlist; direct requirements and practical vehicle needs are in scope only when the user is seeking listings.

2. **Inputs and semantics**  
   Direct constraints, required versus preferred, practical needs, and exact VIN behaviour. Only fields needed for the search are requested.

3. **Interpretation boundary**  
   Practical needs guide candidate selection; they do not independently establish reliability, safety, running cost, exact towing suitability, condition, or accident-free history.

4. **Returned result and evidence**  
   Current listings, usable viewing links, and clear confirmed/unconfirmed/changed criteria.

5. **Limits and exclusions**  
   Not general automotive/finance/maintenance advice; missing provider data is unknown rather than a pass/fail conclusion.

This is enough to meet Anthropic’s requirement for a meaningful behavioural description while meeting OpenAI’s emphasis on explicit user intent, minimal inputs, and no implementation detail.

## What it must not contain

A shared description should avoid:

- “always invoke,” “never refuse,” “must call [other tool] first,” or comparable agent-control language;
- instructions that make the calling model repeat, avoid, or chain calls as a procedure;
- Auto.dev terminology, raw mapping rules, fallback ladders, scoring formulas, or diagnostic data;
- broad free-text / conversation-history inputs;
- claims that CarClever independently proves buyer-outcome facts that the listing evidence cannot prove.

These exclusions align with both platforms. They do not create a reason to fork.

## Decision options

| Option | What it means | Assessment |
| --- | --- | --- |
| One shared description now | Deliberately write one neutral common contract; use platform-specific metadata only | **Recommended next experiment.** Requirements are compatible, and it minimizes drift. |
| Separate descriptions now | Maintain an OpenAI-specific and Claude-specific prose contract | Premature. It adds maintenance and can hide behavioural drift before testing proves a need. |
| One common core plus optional Claude enrichment later | Same description and field semantics; add supported Claude-only examples or submission text only if evaluation shows a benefit | **Good fallback.** This is not two competing descriptions. |

## Evidence gate before deciding to fork

Do not fork merely because the documentation uses different emphasis. First evaluate the same common description in both environments against the existing regression suite:

- practical needs: family, teen driver, commuting, towing;
- hybrid/PHEV/EV required versus preferred;
- required versus preferred trim;
- V8/cylinders and interior colour routing;
- `bodyType` plus `vehicleType`;
- exact VIN;
- unknown history/CPO/ownership;
- ZIP/location edge cases;
- out-of-scope advice;
- returned links and evidence statements.

**Fork only if a real platform-specific test fails and the smallest neutral, shared clarification cannot fix it.**

## Recommendation

Treat a single shared description as **achievable and preferable to attempt first**. The documents do not show a hard policy conflict.

The next decision is not “which platform gets the better description?” It is whether we approve the common-contract principles above, then write one candidate description and test it. If it does not give Claude sufficient routing quality or fails OpenAI review, use a narrow platform-specific enrichment as the evidence-based exception.

## Sources and limits

- [OpenAI — Plugin guidelines](https://developers.openai.com/plugins/app-guidelines): purpose-accurate descriptions, no overly broad triggering, minimum purpose-driven inputs.
- [OpenAI — Define tools](https://developers.openai.com/plugins/plan/tools): describe user intent, not implementation; state purpose, use conditions, limits, and explicit schemas.
- [OpenAI — Build an MCP server](https://developers.openai.com/plugins/build/mcp-server): tool metadata is user-facing behaviour; tool descriptions explain when to use a tool; results should be useful and structured.
- [Anthropic — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools): detailed descriptions, parameter meaning/effects, caveats, and limitations; optional input examples for supported tool types.
- [Anthropic — MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector): MCP selection relies on names and descriptions.
- Historic Anthropic directory feedback supplied by André: used as the authoritative record of the earlier directory-review concern. No public current Anthropic directory-policy page was available in the reviewed sources, so this report does not infer additional directory rules beyond that feedback.

