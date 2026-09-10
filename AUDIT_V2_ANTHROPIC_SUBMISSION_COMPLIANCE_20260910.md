# V2 Anthropic Submission Compliance Audit — 2026-09-10

**Status:** COMPLETE read-only compliance/design audit; one material policy clarification blocker found  
**Scope:** Current `release/v2` MCP tool descriptions, input-field descriptions, annotations, functional behavior relevant to Anthropic review, and the existing Anthropic V1 submission answers.  
**No code, Vercel configuration, domain, connector, branch, PR, deployment, or Anthropic submission was changed.**

## 1. Executive result

V2 is **materially better positioned than V1** for Anthropic's current tool-description review criteria, but it is **not yet ready to replace the pending V1 submission unchanged**.

Two separate issues exist:

1. **Description/schema wording — fixable:** V2 still contains direct instructions to the host model in the main tool description and several field descriptions. Anthropic's current rule is explicit: descriptions should state what the tool does and when to invoke it; "Describe what the tool does. Do not tell Claude how to behave." The current V2 wording can be made more neutral without changing the tested contract.
2. **Commercial-content classification — potentially blocking and more important:** Anthropic's current Software Directory Policy says directory software may not serve advertisements, sponsored content, paid product placements, or primarily promotional content unless expressly permitted by Anthropic. Current V2 deliberately routes user-facing vehicle links through Edmunds/CJ affiliate URLs, and existing source comments describe the design as providing a path to "Edmunds/CJ revenue." The existing Anthropic submission record simultaneously says "no sponsored content" and says an Edmunds affiliate disclosure was provided. That combination needs clarification before any resubmission/amendment.

**Release recommendation:** do not amend the Anthropic submission to V2 until (a) the minimal description cleanup has been implemented and re-tested in both hosts, and (b) Anthropic confirms whether CarClever's affiliate-link model is permitted and how the portal's sponsored-content question should be answered. Do not guess or preserve the existing "no sponsored content" answer without clarification.

## 2. Current Anthropic criteria used

Current Anthropic documentation says:

- tool descriptions must narrowly and accurately state what the tool does and when it should be invoked;
- descriptions must match actual behavior;
- descriptions are rejected for specified prompt-injection / behavior-instruction patterns;
- Anthropic's concise rule is: describe the tool's function rather than telling Claude how to behave;
- all tools need title plus applicable safety annotations;
- tools must return functional, actionable responses and validate invalid inputs;
- the MCP server must call first-party APIs or APIs legitimately proxied;
- directory software may not serve ads, sponsored content, paid product placements, or primarily promotional content unless expressly permitted;
- submission data handling explicitly asks whether the connector surfaces sponsored content.

## 3. `find_matching_vehicle` main description

### Good / retain

The opening and closing purpose statements are substantially improved from V1. They explain:

- the tool searches current US vehicle inventory;
- it returns a concise shortlist;
- supported search dimensions and optimization goals;
- exact VIN behavior;
- evidence/unknown handling;
- the tool is for live listing search rather than general automotive education/finance/maintenance.

These are exactly the kinds of "what it does / when to invoke" statements Anthropic asks for.

### Needs neutralization

The following V2 concepts are valid but are expressed as direct model instructions:

- "resolve it into real matching model names yourself and include them in model before calling this tool ... every time";
- "For a broad hybrid ... likewise resolve suitable real model or variant names and include them in model before calling the tool";
- required/preferred instructions are partly phrased as commands to the host rather than contract semantics.

The underlying behavior is important because the V1→V2 equivalence gate proved practical-needs/electrification candidate resolution must survive. The fix should therefore change **wording, not behavior**.

### Recommended neutral form

Use capability/contract language such as:

> Practical-needs searches use `model` for resolved real-world candidate models and `vehicleNeeds` for soft need context. The server does not infer vehicle classes from `vehicleNeeds`; model-scoped eligibility therefore depends on candidate model names supplied with the request. Broad electrification searches similarly use compatible real model/variant candidates together with the structured electrification fields. `required` restricts eligibility to compatible electrification evidence; `preferred` keeps alternatives eligible while ranking compatible results higher.

This tells Claude how the inputs function without imperative phrases such as "yourself," "before calling," or "every time."

## 4. Input-schema description audit

### `model` — CHANGE

Current wording directly instructs the host to "resolve ... yourself ... before calling ... every time." Replace with neutral contract semantics. Preserve:

- real model names;
- no manufacturer prefix;
- comma-separated candidates;
- practical-needs/electrification searches require candidate model scope because the server does not infer it from soft need text.

### `vehicleNeeds` — CHANGE

Current wording again tells the host to resolve needs into model names. Keep this field described as soft, capped listing-relevant context and cross-reference that candidate models determine model eligibility. Avoid a direct imperative.

### `electrificationTypes` — CHANGE

Current wording says to "pair this field" and "do not use ... alone." Rephrase descriptively: electrification fields express acceptable powertrain evidence, while broad/model-agnostic electrification searches require compatible model/variant candidate scope because these fields do not independently create a vehicle-class/model search universe.

### `priorityAxis` — MINOR CHANGE

Most of the description correctly defines semantics, but "Use lower_risk for requests such as..." is a direct instruction. Rephrase as examples of intent represented by the enum: `lower_risk` represents lower-risk/safer-looking/cleaner-history ranking intent. Keep the non-guarantee language.

### Other input fields — PASS

The remaining fields are generally narrow, factual parameter descriptions: VIN, price, year, make, body type, mileage, ZIP/radius, trim required/preferred, seats, drivetrain, transmission, colors, vehicle type, doors, cylinders, used, CPO, state, no-accidents, one-owner. No material Anthropic behavior-instruction issue was found in them.

## 5. `resolve_dealer_url` description

**Description-form verdict: PASS with optional simplification.**

It describes the tool's actual deterministic behavior: inputs, preferred Edmunds link, fallback behavior, and the fact direct dealer URLs are not returned as the user-facing resolved link. It does not materially instruct Claude to modify unrelated behavior.

However, the description and underlying link behavior are directly relevant to the commercial-content blocker below.

## 6. Tool annotations / structure

Current V2 registration includes short tool names and the relevant `title`, `readOnlyHint`, `openWorldHint`, and `destructiveHint` annotations. No tool-name-length or obvious read/write annotation defect was found in this audit.

The app is authless and uses Streamable HTTP in the existing submission record. Functional regression tests and custom error handling are already extensive. These areas are not the current blocker.

## 7. Critical commercial-content finding

### Current Anthropic policy

Anthropic's Software Directory Policy currently states that, unless expressly permitted in writing, directory software may not serve:

- advertisements;
- sponsored content;
- paid product placements;
- software primarily operating as an advertising/promotional vehicle.

The current submission portal's data-handling step explicitly asks whether the connector surfaces sponsored content.

### What CarClever currently does

Current V2 source is explicit that link resolution gives each result an Edmunds/CJ revenue path. User-facing result links use `affiliateUrl` / `affiliateFallbackUrl`, while the dealer listing URL is retained only for internal/diagnostic use and deliberately not surfaced as the resolved user-facing destination.

This is not a hypothetical future monetization feature; it is current application behavior.

### Existing submission-record inconsistency

The existing Anthropic V1 submission record in `carclever-widget/STATE.md` says:

- Data Handling: proxied Auto.dev API, no health data, **no sponsored content**;
- Compliance: all seven boxes checked, **Edmunds affiliate disclosure provided**.

Those two statements may be reconcilable if Anthropic does not classify ordinary affiliate links as sponsored/promoted content, but Anthropic's public policy does not define that boundary. We therefore cannot safely assume the current "no" answer is correct.

### Risk assessment

**Material / release-blocking until clarified.**

It would be irresponsible to recommend editing V1 to V2, re-attesting to the current form, and hoping reviewers interpret affiliate routing as outside the sponsored-content prohibition. The risk is at least as important as the tool-description issue and may be more likely to produce a policy rejection.

### Required clarification

Before the Anthropic V1→V2 decision is executed, ask Anthropic review support a narrow factual question:

> CarClever ranks vehicle listings independently from payment and does not sell ranking placement, but its user-facing outbound vehicle links are CJ/Edmunds affiliate links and may generate commission when a user follows/converts. Does Anthropic classify this as prohibited "sponsored, promoted, or advertising content" for a Connectors Directory MCP server? If permitted, should the Data Handling sponsored-content answer be Yes, and is written permission/another disclosure required?

Until answered, treat the Anthropic commercial-content gate as **OPEN**.

## 8. Impact on the V1-vs-V2 decision

The earlier decision research preferred amending the pending Anthropic submission to V2 + a permanent owned Claude origin after description/domain validation.

**This audit adds a new prerequisite and changes that recommendation to CONDITIONAL.**

Do not change the pending Anthropic submission yet. Sequence:

1. perform the minimal V2 description/schema wording cleanup through Claude Engineering;
2. run both-host regression tests to prove no host-routing loss;
3. obtain Anthropic clarification on affiliate-link eligibility/sponsored-content classification;
4. validate the permanent Claude custom origin;
5. inspect the pending Edit workflow without saving and determine what the UI says about resubmission/review status;
6. only then choose wait vs amend.

If Anthropic says the affiliate model is not allowed in directory connectors, the Claude production channel will need a compliant link-output policy/configuration before any amended submission. That engineering design must preserve unbiased search/ranking and be re-tested; it should not be improvised in the submission form.

## 9. Queue/edit finding

Anthropic's public docs say review times vary with queue volume and explain that reviewer-requested changes can be addressed and resubmitted from the same submission page. They do **not** state whether a voluntary edit to an already-in-review submission retains or resets its place in the queue.

A current third-party translation of Claude's own UI strings contains text indicating an edit may be reviewed against a previously captured tool list unless the connector is reconnected to attach a fresh capture. This is corroborative, not authoritative. The current Anthropic GitHub issue #828 independently confirms the submission request contains `submission_data.server_snapshot.tools`.

Therefore:

- a tool snapshot exists;
- a V1→V2 change should intentionally refresh/reconnect the snapshot if the UI supports it;
- queue position after a voluntary pending edit remains unknown until the actual Edit workflow or Anthropic support says otherwise.

## 10. Final audit verdict

| Area | Verdict | Action |
|---|---|---|
| V2 overall functional design | PASS / already well tested | retain |
| Main `find_matching_vehicle` description | CHANGE | neutralize direct host instructions |
| `model` field description | CHANGE | neutral contract semantics |
| `vehicleNeeds` field description | CHANGE | neutral contract semantics |
| `electrificationTypes` description | CHANGE | neutral contract semantics |
| `priorityAxis` description | MINOR CHANGE | remove imperative "Use..." phrasing |
| Other input descriptions | PASS | retain |
| `resolve_dealer_url` description form | PASS | optional simplification only |
| Tool names/annotations | PASS | retain |
| Existing Anthropic "no sponsored content" answer | **UNRESOLVED / MATERIAL RISK** | obtain Anthropic clarification before re-attesting |
| V1→V2 Anthropic amendment | **BLOCKED FOR NOW** | complete description + commercial-content + domain + Edit-flow gates first |

## 11. Ownership

- ChatGPT: this audit, policy research, wording/design recommendation, release-gate verification.
- Claude Engineering: any V2 description/schema code edits and all deployment/domain/branch/connector work.
- André: Anthropic contact/submission decision and final permanent-origin confirmation.

## References

- Anthropic, `Submitting to the Connectors Directory`.
- Anthropic, `Pre-submission checklist`.
- Anthropic, `Manage your listing after publishing`.
- Anthropic Software Directory Policy, current 2026 policy.
- Anthropic `anthropics/claude-ai-mcp` issue #828, server-snapshot submission evidence.
- `carclever-find-my-car/release/v2/app/[transport]/route.ts`.
- `carclever-find-my-car/release/v2/lib/find-matching-vehicle-input.ts`.
- `carclever-find-my-car/release/v2/lib/link-resolution.ts`.
- `carclever-widget/STATE.md` current Anthropic submission record.
- `RESEARCH_ANTHROPIC_V1_V2_REVIEW_AND_MCP_ORIGIN_DECISION_20260910.md`.
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`.
