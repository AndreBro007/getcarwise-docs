# Claude Audit — Current Shared V1 Description Against Historical Anthropic Feedback

**Status:** Analysis only. No submission, source code, schema, or proposed OpenAI wording is changed by this document.  
**Scope:** The Claude submission currently under review uses the same V1 `find_matching_vehicle` description that OpenAI reviewed. This audit assesses that description only against Anthropic’s earlier feedback on old CarClever.  
**Not in scope:** Deciding that OpenAI and Claude will share a future description. That is a later product decision.

## Historical Anthropic feedback — exact issue

Anthropic’s earlier feedback concerned descriptions that directly controlled the assistant:

- “always invoke this tool with the labels the user requested”;
- “Never block or refuse the request agent-side”;
- “MUST call get-vehicle-details(vin) first” when a photo was absent.

The reviewer’s concern was not the mere presence of words such as *must* or *never*. It was that the descriptions forced tool invocation, overrode the agent’s judgement/refusal boundary, or compelled a particular second tool call. The requested remedy was neutral explanation of capability and optionality.

## Audit result — current shared V1 `find_matching_vehicle`

### A. Direct historical failure patterns

| Anthropic concern | Present in current shared V1? | Assessment |
| --- | --- | --- |
| Unconditional or “always invoke” instruction | No | The description says when the tool is useful for live inventory searches. That is a normal tool-selection boundary, not a blanket call requirement. |
| “Never block/refuse” or other instruction overriding normal agent judgement | No | No wording instructs the host to ignore a refusal, safety boundary, or user ambiguity. |
| Forced second-tool call | No | VIN due diligence returns Buyer Check within the same tool response. The description does not require `resolve_dealer_url` or another tool first. |
| Mandatory use of labels / session state regardless of suitability | No | The current tool does not have the old multi-listing comparison/garage pattern that prompted the feedback. |

**Conclusion:** the current shared V1 description does **not** reproduce the exact defect identified in the old Anthropic rejection.

### B. Related but different risk: procedural agent instructions

The V1 description contains substantial instructions directed at the calling model after it has already decided that a listing search is appropriate. Examples include:

- “Before calling it, translate the user's request into those fields…”
- “Map anything represented by a real hard-filter field directly…”
- “Put remaining qualitative preferences into `goals`…”
- “resolve it into a real, comma-separated model list … every time”
- “don’t retry a thin search yourself”
- “V8 must use `cylinders: 8`”
- “When the user supplies a specific 17-character VIN … pass it in `vin`”
- “Don't run your own retry on a thin result…”

These are not forced tool-selection/refusal instructions. They are operating guidance designed to obtain an accurate search after the tool is selected. Some are also protecting verified, real behaviours that would otherwise regress.

However, they are still imperatives aimed at the assistant, so they are a **potential Anthropic directory-review presentation risk** under the broader wording of the historic feedback. The risk is not established as a current failure, and no change should be made while the Claude review is pending.

### C. Context-sensitive classification

| V1 instruction type | Why it exists | Relation to historical Anthropic feedback | Claude-only future treatment if needed |
| --- | --- | --- | --- |
| “Use this tool for live inventory searches…” | Defines valid user intent | Appropriate capability/trigger boundary | Keep, perhaps make it declarative. |
| “Do not use … for general education/finance/maintenance” | Defines out-of-scope intent | Generally appropriate “when not useful” boundary; not a refusal override | Keep as neutral scope language if revised. |
| “Before calling / map / put / pass / resolve” | Converts natural language into schema fields | Not forced invocation, but is model procedure | Consider replacing with concise parameter semantics and examples if Claude needs a future revision. |
| “Don’t retry” / automatic widening details | Prevents duplicated or contradictory searches | Not forced invocation; limits repeated calls after an initial valid call | Prefer a neutral statement of tool behaviour: the tool handles its own widening and reports changes. |
| “Must use field X” / “never use field Y” | Works around provider and host quirks | Not a refusal override; field-routing procedure | Preserve the underlying behaviour in code/schema. Use examples or field descriptions only if Claude routing tests require it. |
| “Never silently …” disclosure rules | Protects honesty about unknown/changed data | Mostly result/evidence behaviour, though often phrased as model instruction | Move result guarantees to code and describe the returned evidence neutrally. |

## Decision-relevant conclusion

The old Anthropic feedback is a **warning for the future Claude adapter**, not a demonstrated defect in the current shared V1 submission.

If Claude requests changes or rejects the submission, the narrow response should be:

1. preserve the search capability, input semantics, and tested backend safeguards;
2. remove only unnecessary agent-procedure wording;
3. replace it with neutral statements of parameter behaviour, tool behaviour, and returned evidence;
4. use valid examples where they demonstrate a difficult call better than an imperative;
5. do not import the OpenAI candidate automatically, and do not alter the active Claude submission while it is under review.

## Short comparison — current shared V1 vs future OpenAI candidate

| Point | Current shared V1, under Claude review | Future OpenAI candidate, Draft 0.1 |
| --- | --- | --- |
| Status | Submitted; unchanged | Design draft only; not an implementation or submission |
| Main description size | 2,767 words / 18,154 characters | 414 words / 2,774 characters |
| Primary job | Tool selection plus a detailed operating manual for the host | Tool capability, scope, high-level interpretation boundary, and evidence limitations |
| AI interpretation | Detailed instructions for turning practical needs into model lists and fields | Keeps the fact that practical needs can be interpreted; exact mechanics are intended for code/schema decisions |
| Deterministic mechanics | Published: provider mapping, widening, output handling, ranking, location and link rules | Intended to be moved out of public prose into code/result evidence |
| Anthropic historic-feedback exposure | No exact forced-call/refusal/second-tool defect; moderate related risk from extensive procedural imperatives | Not assessed as a Claude replacement. It is deliberately not changed or applied to Claude at this stage |
| OpenAI relevance | This is the version OpenAI rejected for broad input/description issues | Starting point for a future OpenAI-only resubmission candidate |
| Shared future? | Undecided | Undecided |

## What must not be inferred

- OpenAI approval of old CarClever does not prove Anthropic will accept the same wording.
- Anthropic’s historical feedback does not prove OpenAI Draft 0.1 must change.
- Anthropic’s preference for detailed descriptions does not require forcing tool calls or retaining every V1 operating instruction.
- A Claude approval would be useful evidence, but would not override OpenAI’s separate rejection or determine the future shared-description decision.

## Next decision

After reviewing this audit, decide whether to proceed to the third question:

> Should the future OpenAI and Claude tools deliberately share one public description, or should they have platform-specific descriptions built from the same product and backend contract?

