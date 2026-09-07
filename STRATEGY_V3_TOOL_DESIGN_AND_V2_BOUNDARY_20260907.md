# STRATEGY_V3_TOOL_DESIGN_AND_V2_BOUNDARY_20260907.md

**Status:** Proposed strategy; pending André confirmation on the VIN due-diligence routing decision before engineering changes.

## Executive conclusion

V2 should be treated as closed. It is the stable, no-new-tools release on `release/v2`: the count-display fix plus the deterministic Edmunds-link redesign, split CTAs, NHTSA trim decode, and priority-axis improvements.

V3 is the correct home for all remaining app functionality. The one exception is a V3 regression decision that must be resolved before further engineering: when a user asks whether a specific VIN is a good buy or has red flags, should `check_vehicle` also return enough listing context to preserve the listing/card action, should the flow deliberately require a follow-up search, or should the trigger language be narrowed so the request routes back to `find_matching_vehicle`?

## Evidence reviewed

- `STATE.md`, `TASKS.md`, `DECISIONS.md`, `PLAYBOOK.md`, `REFERENCE.md`, `ACCOUNT_MEMORY_TRANSFER.md`, and `WORKFLOW_ARCHITECTURE.md` in `carclever-widget`.
- The dynamically listed and fetched root of `getcarwise-docs` (26 Markdown files).
- `CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md` and the V3 testing record.
- Recent widget commits, including the Sep 7 sell/trade-in CTA shipment; the claimed outcome was verified in the commit diff and task-state transition.

The current record says V3 has passed typecheck/build and 66 total tests, with live Claude coverage for recall states, V2 link behavior, priority axes, trim-required filtering, model correction, and the original VIN Buyer Check path. ChatGPT testing uses `ccfmc-dev-v3`; Claude uses the V3-equivalent test connector. The V1 production path remains untouched and under Anthropic review.

## V2/V3 boundary

Keep in V2:
- Existing search and result-card behavior.
- Deterministic Used/New/Carvana Edmunds destination tiers.
- Split “Check avail.” and “View similar” actions.
- Count correctness, trim decode, and established priority axes.

Do not add to V2:
- New tools.
- Finance, comparison, persistence, or expanded recall workflows.
- Tool-routing changes that alter the submitted production path.

Put in V3:
- The `check_vehicle` tool and all recall/VIN due-diligence behavior.
- Any cross-tool routing correction caused by `check_vehicle`.
- A thin, invocation-friendly action layer around search results (only if it can be implemented without duplicating the listing UI or weakening click-through).
- Later finance/comparison capabilities, each as a separate evidence-backed release rather than a bundle.

## V3 tool portfolio

### 1. `find_matching_vehicle`

Primary discovery tool. It should be selected for requests containing a search intent: find, show, recommend, compare candidates, locate, or search for vehicles. It may also handle a VIN when the user wants the vehicle/listing itself, because it can return the card, image, and outbound actions.

The description should explicitly include realistic user language, including:
- “Find me a used SUV under $30,000.”
- “Show me large SUVs near 90210.”
- “Find this VIN and show me the listing.”
- “Which cars fit these requirements?”

It should state that the result is a shortlist, not a complete market inventory, and that the tool returns the best available matches plus next actions.

### 2. `check_vehicle`

Focused verification tool. It should be selected for a known vehicle/VIN when the user asks about recalls, red flags, purchase risk, or what to verify before buying.

Use plain-language trigger families:
- “Any recalls?”
- “Does this VIN have open recalls?”
- “Is this a good buy?”
- “Any red flags?”
- “What should I check before buying this VIN?”

The output contract should remain compact and categorical:
- vehicle identity when available;
- recall state: none, severe, routine, or unavailable;
- one concise explanation;
- Buyer Check evidence when a VIN is supplied;
- explicit unknown/unavailable handling;
- a next action.

It must never imply that no recall signal is a safety or mechanical guarantee, and it must not expose provider internals or numeric risk scores.

### 3. `resolve_dealer_url`

Destination/action tool. It should be selected only when the user asks for the listing, dealer page, availability, or a link for a selected result. It should not compete with search or recall wording.

Its description should make the required selection explicit: use the vehicle identity/VIN supplied by the preceding result, preserve the selected vehicle, and return the validated destination tier available for that vehicle. The normal user experience should show the action label and destination, not URL-construction details.

## Invocation design rules

1. Describe jobs, not implementation. Start each tool description with “Use this when…” and name the user’s intent.
2. Include natural language synonyms and examples. Models route by semantic fit; “recall,” “red flags,” “good buy,” “listing,” “availability,” and “similar cars” should appear in the relevant descriptions.
3. Make boundaries explicit. State what the tool does not do, especially that search finds candidates, check_vehicle verifies a known vehicle, and resolve_dealer_url supplies a destination.
4. Keep overlap intentional but ordered. VIN + “show me the car/listing” belongs to search; VIN + “recalls/red flags” belongs to check_vehicle. The unresolved regression decision determines whether “is this a good buy?” belongs to check_vehicle alone or a combined path.
5. Make the minimum viable input obvious. A VIN alone should be sufficient for check_vehicle; natural-language vehicle constraints should be sufficient for search; a selected vehicle identity should be sufficient for URL resolution.
6. Return structured evidence that lets the host AI answer naturally, while keeping the rendered card lean and action-oriented.
7. Preserve unknown as unknown. Never convert missing, conflicting, or unavailable provider data into a negative finding.
8. Put the next action in every downstream result. A risk/recall answer should preserve a route back to the selected listing when the product contract permits it.
9. Avoid diagnostic leakage, internal phase labels, raw provider fields, numeric scores, and affiliate mechanics in normal output.
10. Treat invocation rate and click-through as separate metrics. A tool that is called often but removes the reason to visit the listing is not automatically a product win.

## Recommended V3 test matrix

Run the same prompts on Claude and ChatGPT V3 connectors and record: selected tool, arguments, whether a card rendered, whether the selected vehicle stayed consistent, whether the answer preserved unknown states, and whether the expected next action was present.

- Search: “Find a used AWD SUV under $30k near 90210.”
- Search + VIN: “Find this VIN and show me the listing.”
- Recall: “Does this VIN have open recalls?”
- Due diligence: “Is this a good buy? Any red flags?”
- Action: “Open the listing for result A.”
- Ambiguous: “Check this car.”
- Follow-up: “What about the cheaper one?”
- Failure: invalid/partial VIN and unavailable NHTSA response.
- Regression: verify that due-diligence wording does not silently remove listing context unless that behavior is explicitly chosen.

## Recommended sequencing

1. André chooses the VIN due-diligence behavior.
2. Engineering updates the V3 contract and routing only on `feature/v3-check-vehicle`; V1 remains frozen.
3. Re-run the cross-platform regression and the full V2 regression suite.
4. Only after stable invocation behavior, consider the next V3 addition: a thin affordability action or adaptive comparison. Do not add both together.
5. Measure tool selection, completion, listing-action clicks, and downstream affiliate outcomes separately.

## Pending André confirmation

Please choose one for the VIN due-diligence regression:

- **A — preserve context:** `check_vehicle` owns the request and returns a listing/action context when possible.
- **B — keep tools narrow:** `check_vehicle` returns verification only; the host may ask for a follow-up listing action.
- **C — route differently:** narrow `check_vehicle` trigger language so “is this a good buy?” remains on the search/VIN path until a combined experience exists.

Until selected, this document is strategy guidance, not authorization for an implementation change.
