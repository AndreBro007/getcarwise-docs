# Claude and OpenAI Tool-Contract Compatibility Audit

**Status:** Decision draft — no change to the Claude submission currently under review.  
**Scope:** The Claude submission used the same V1 `find_matching_vehicle` contract as the OpenAI submission. This audit decides how to handle that shared starting point after OpenAI’s rejection.  
**Baseline:** Existing tested V2 code remains the prospective implementation baseline. V3 tools and capabilities remain out of scope.

## Executive conclusion

The same V1 description can be defensible for Claude tool performance yet unsuitable for OpenAI submission review. That is not a reason to weaken the product or create two different behaviours.

The sustainable design is:

> One shared product contract, schema semantics, backend mapping, evidence model, and regression suite; platform-specific public tool definitions generated from that contract.

The existing Claude review should remain untouched. Its outcome is valuable evidence about whether the original detailed contract is acceptable to Anthropic and whether it produces useful host behaviour. Do not replace it, appeal it, or resubmit anything while that review is pending.

## What the platforms actually require

| Topic | OpenAI implication | Anthropic implication | Shared design response |
| --- | --- | --- | --- |
| Tool description | Must have a clear, accurate trigger boundary and avoid broad or biased wording. The rejection also flags overly broad input collection. | Calls for a detailed plaintext account of what the tool does, when to use it, how it behaves, parameter effects, and limitations. | The description cannot be identical word-for-word. Keep a concise OpenAI adapter and a more explanatory Claude adapter. |
| Complex inputs | Avoid asking for full history or broad context; request only purpose-related inputs. | Detailed parameter descriptions are important; valid `input_examples` can help for optional/complex inputs. | The schema itself stays narrow. Claude may use a few examples rather than returning to a giant narrative. |
| Tool names | Clear, unique, accurately functional. | Clear names improve selection; fewer related tools reduce ambiguity. | `find_matching_vehicle` remains a strong shared name. |
| Tool selection | Describe user intent, not internal implementation. | Claude selects based on name/description, especially with MCP toolsets. | Keep the explicit listing-search boundary in both adapters; never expose provider mechanics as a trigger rule. |
| Result design | Users must receive important disclosures/evidence from code, not be dependent on description wording. | High-signal result fields help Claude reason about the next step and conserve context. | One structured response contract returns links and confirmed/unconfirmed/changed evidence. |

Official evidence: Anthropic defines a tool description as a detailed explanation of what it does, when it should be used, and how it behaves; it recommends detailed parameter and limitation guidance, and supports schema-valid input examples for complex inputs. It also recommends consolidating related operations rather than exposing many ambiguous tools. OpenAI’s rejection specifically requires narrower input collection and clearer, neutral tool descriptions.

## Responsibility map

| Responsibility | Shared product contract | OpenAI public adapter | Claude public adapter |
| --- | --- | --- | --- |
| Current US vehicle listings / shortlist | Yes | One short scope paragraph | One fuller scope and return-value paragraph |
| Direct requirements: make, model, budget, year, mileage, location, body style, etc. | Yes | Concise field definitions | Field definitions can state material effects/caveats |
| Practical needs: family SUV, teen driver, commute, towing | Yes: AI interprets the need into a vehicle listing search | State the boundary and no-proof caveat | Explain interpretation, ranking role, and verification limitation; use an example if it improves reliability |
| Required versus preferred | Yes | One instruction | Explain its impact in fields/examples where necessary |
| Hybrid/PHEV/EV variants | Yes | State required versus preferred and evidence caveat | Describe variant/verification caveat without documenting Auto.dev internals |
| Make/model cleanup and provider mapping | Code only | Omit | Omit |
| `bodyType` plus `vehicleType` safeguards | Code only | Omit implementation mechanics | Omit implementation mechanics |
| Widening, ZIP control queries, risk calculations, VIN cross-check | Code only | Briefly disclose changed criteria / exact VIN limit | Explain resulting evidence/limitation only if needed |
| Links, CTA, cards, image/map output | Code only | Omit presentation instructions | Omit presentation instructions |
| Reliability, safety, running cost, towing, condition claims | Shared evidence boundary | State that the tool does not independently prove them | Give the same limitation in more concrete terms |

## What should remain shared

These are product rules, not platform prose. A result must behave the same whether it was initiated through Claude or OpenAI:

- The tool searches current US vehicle listings; it is not general automotive, finance, maintenance, or leasing advice.
- Explicit constraints populate relevant inputs; no invented hard constraint.
- Practical needs guide candidate choice and ranking, but do not become unsupported factual guarantees.
- “Required” and “preferred” remain semantically distinct.
- Missing history, ownership, CPO, feature, or specification data remains **unknown**, never an automatic pass or fail.
- Exact 17-character VIN is exact-listing lookup only—no similar-vehicle substitution.
- Returned results carry deterministic listing links and evidence of confirmed, unconfirmed, and altered criteria.
- Backend code owns provider-field translation, normalization, query controls, widening, verification, scoring, and presentation mechanics.
- The field-audit safeguards remain: do not remove `vehicleType`, `cylinders`, or `interiorColor` because a description becomes shorter.

## Where the descriptions should differ

### OpenAI adapter

Use the 414-word Draft 0.1 as the starting point, then write short field definitions. It must:

- ask only for the fields needed to perform the listing search;
- avoid a broad free-text `goals`/conversation-history channel;
- explain when the tool should and should not run;
- retain enough AI guidance for practical needs, required versus preferred, direct constraints, exact VIN, priority, and ambiguity;
- make no provider-specific promise or presentation instruction.

### Claude adapter

Do **not** assume it needs the full 2,767-word V1 description forever. Its detailed guidance can be structurally better:

1. A focused multi-sentence tool description: scope, trigger boundary, what is returned, material limitations.
2. Concise but informative field definitions for parameters where Claude must understand behaviour.
3. A small set of schema-valid `input_examples` if the integration supports them—for example, practical need plus direct constraints; required versus preferred trim; exact VIN.
4. A short limitation block covering evidence versus inference and unknown data.

This preserves the details Claude needs without using tool prose as a second backend implementation.

## Public tool surface

| Tool | OpenAI candidate | Claude position while review is pending | Future default |
| --- | --- | --- | --- |
| `find_matching_vehicle` | Public | Keep exactly as submitted until the review ends | Public on both platforms |
| `resolve_dealer_url` | Not public | Do not change the pending review | Prefer internal/support-only unless Claude’s review or a real host flow demonstrates that it needs separate public access |
| V3 `check_vehicle` | Excluded | Excluded | Separate future decision, not part of this contract work |

This is compatible with Anthropic’s guidance to consolidate closely-related operations where that reduces selection ambiguity. It does not require exposing a second tool merely because it exists internally.

## Options after the Claude review

| Option | Description | Assessment |
| --- | --- | --- |
| A. One short description everywhere | Use the OpenAI adapter unchanged for Claude | Lowest maintenance, but risks losing useful Claude behaviour and ignores Anthropic’s detailed-description guidance. |
| B. One long description everywhere | Retain the V1 description for both | Preserves the current Claude experiment, but directly conflicts with the issue OpenAI raised. |
| C. Two independent hand-written descriptions | Maintain separate prose manually | Can work, but will drift and recreate the same maintenance risk. |
| D. Shared contract with generated platform adapters | Maintain one internal responsibility/field contract; produce a concise OpenAI description and a structured detailed Claude description | **Recommended.** It protects product consistency without pretending the hosts have identical review or tool-use expectations. |

## Decision sequence

1. Leave the submitted Claude contract unchanged while it remains under review.
2. Complete the OpenAI Draft 0.1 field-description pass against the Auto.dev audit.
3. Create the Claude adapter from the same core contract: not yet a submission change, only a comparison draft.
4. Define 3–5 validated Claude input examples if technically supported by its submission path.
5. Give Claude the feasibility package: field/schema deltas, code responsibilities, and the shared regression gate.
6. Review the live/test evidence, then choose Option D formally.
7. Use the platform-appropriate adapter only when a new submission/review action is deliberately initiated.

## Questions that the Claude review can answer

- Does Anthropic accept the existing long V1 contract?
- Does the currently submitted contract show any review concern around input breadth, naming, or inaccurate claims?
- If approved, does that establish only approval—or also reliable real host behaviour?
- Which instructions genuinely need to remain in the Claude-facing definition after code takes over deterministic work?
- Do input examples give the same routing reliability as long prose for difficult fields such as V8/cylinders, interior colour, hybrid status, and required versus preferred trim?

An approval would be useful evidence, but it would not override OpenAI’s separate policy decision. A rejection would not invalidate the core contract; it would tell us which Claude-facing details or submission mechanics need attention.

## Source links

- [Anthropic — Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
- [Anthropic — Tool-use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- [Anthropic — MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
- [OpenAI app guidelines](https://developers.openai.com/plugins/app-guidelines)
- [OpenAI tool planning guidance](https://developers.openai.com/plugins/plan/tools)
