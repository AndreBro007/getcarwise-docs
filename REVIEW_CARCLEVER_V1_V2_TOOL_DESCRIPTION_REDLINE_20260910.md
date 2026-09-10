# CarClever V1→V2 Tool Description Review and Minimal Redline — 2026-09-10

**Status:** PROPOSED — no application code changed  
**Purpose:** Compare Anthropic's actual prior CarClever feedback with the current V1 and V2 MCP descriptions, identify only the wording that creates review risk, and define a minimal no-regression redline before Claude Engineering changes anything.  
**Owners:** ChatGPT = review/redline/test design; Claude = implementation only after André approves the redline; André = final approval and manual host testing where required.

## 1. Authoritative prior Anthropic feedback

On 2026-08-01 Anthropic's MCP Directory team said the previous CarClever server was technically healthy and specifically objected to **tool descriptions that instruct the assistant**. Their examples were imperative phrases such as:

- `always invoke this tool ...`
- `Never block or refuse ...`
- `MUST call ... first`

Their stated rule was that descriptions should describe **what a tool does and when it is useful**; assistant-directed imperatives can force unwanted invocations and are not allowed in directory listings.

This is the most relevant precedent for Find My Car. The earlier review also requested a listing icon and assistant-agnostic documentation, but those are listing/presentation issues rather than MCP contract wording.

## 2. Current V1 risk assessment

Current V1 (`main`) is high-risk against that exact prior feedback pattern. Its main `find_matching_vehicle` description is a long operating manual containing many direct instructions to the calling model, including constructions such as:

- `Use this tool ...`
- `don't retry ... yourself`
- `Before calling it, translate ...`
- `Do not invent ...`
- `resolve it ... and pass it ... every time`
- `Never rely ...`
- `Use trimRequired whenever ...`
- `Never translate a VIN ...`
- `Set priorityAxis ...`
- repeated `never`, `must`, `do not`, and presentation instructions.

**Conclusion:** waiting for V1 review is not risk-free. V1 contains the same class of assistant-directed wording Anthropic already rejected on the older CarClever submission, only at substantially greater volume.

## 3. Current V2 assessment

V2 is a major improvement. Its main description is much shorter, capability-led, and mostly states what the tool does. However, several phrases still cross into direct host instruction and should be neutralized carefully.

The underlying semantics are important and must not be weakened: practical-needs and broad electrification searches depend on the host supplying real candidate models/variants because the server itself does not create that candidate universe from soft need text alone.

## 4. Minimal proposed redline — main tool description

### 4.1 Current V2 paragraph at issue

The sensitive section currently says, in substance:

`When a practical need implies a vehicle class, resolve it into real matching model names yourself and include them in model before calling this tool ... every time ... For a broad hybrid ... likewise resolve suitable real model or variant names and include them in model before calling the tool. For required hybrid or plug-in hybrid searches, use electrified variants only; for preferred searches, acceptable base-model alternatives may also be included.`

### 4.2 Proposed replacement

> Practical-needs searches use `model` for real candidate models and `vehicleNeeds` for soft need context. The server does not infer a complete candidate model universe from `vehicleNeeds`; model-scoped eligibility therefore depends on real candidate model names supplied with the request. For example, a large family SUV request may use candidates such as CR-V, RAV4, or Highlander, while a commuter-car request may use Corolla, Civic, or Mazda3. Broad hybrid, plug-in-hybrid, and electric searches similarly use compatible real model or variant candidates together with the structured electrification fields. When electrification is required, candidate scope is limited to compatible electrified variants; when it is preferred, acceptable base-model alternatives can remain eligible.

### Why this is safer

It preserves every important contract fact but removes:

- `resolve ... yourself`
- `before calling this tool`
- `every time`
- `use ... only` as a direct command

It describes **how the contract works** rather than commanding the host.

## 5. Minimal proposed redline — input field descriptions

### 5.1 `model`

**Current risk:** directly tells the host to resolve practical needs into real model names `yourself`, `before calling`, `every time`.

**Proposed:**

> Vehicle model name, without the manufacturer (for example, `E-Class` rather than `Mercedes-Benz E-Class`). Comma-separated values represent multiple accepted candidate models. Practical-needs searches and broad electrification searches use this field to define the real candidate-model scope because `vehicleNeeds` and electrification fields do not independently create a complete model universe.

**Preserves:** no manufacturer prefix; multi-model support; candidate-model dependency.

### 5.2 `vehicleNeeds`

**Current risk:** tells the host to resolve needs into model names and include them.

**Proposed:**

> Short, capped list of listing-relevant practical needs, such as family use, commuting, towing, or teen-driver suitability. This is soft context used for relevance and disclosure; it is not a hard model-eligibility filter. Real candidate models for a need are represented separately in `model`.

**Preserves:** soft-context role; separation from hard model eligibility.

### 5.3 `electrificationTypes`

**Current risk:** imperative `pair this field ... do not use ... alone` wording.

**Proposed:**

> Accepted electrified powertrain types: hybrid (including conventional and mild hybrids), plug-in hybrid, and/or electric. These values express acceptable electrification evidence. For broad searches without a named model, compatible real model or variant candidates are represented in `model`; this field does not independently define a complete vehicle-model search universe.

**Preserves:** accepted enum semantics; broad-search candidate dependency.

### 5.4 `priorityAxis`

**Current risk:** `Use lower_risk for requests such as ...`

**Proposed:**

> Ranking objective: `best_for_budget`, `cheapest`, `lowest_mileage`, `newest`, or `lower_risk`. `best_for_budget` represents best-fit/value intent within a budget; `cheapest` represents explicit lowest-price intent; `lower_risk` represents requests for lower-risk, safer-looking, or cleaner-history candidates. Lower-risk ranking uses available purchase-risk evidence and is not a guarantee of safety or clean history. Data conflicts remain separate verification notes rather than purchase-risk evidence.

**Preserves:** intent mapping and non-guarantee semantics without a direct command.

## 6. Areas that should NOT be changed in this pass

To minimize regression risk, do not use this exercise as general copy cleanup. Leave unchanged unless testing finds a real defect:

- VIN semantics;
- price flexibility semantics;
- required/preferred trim behavior;
- ZIP/radius semantics;
- drivetrain/transmission/color/doors/cylinders/condition/CPO/history field definitions;
- `resolve_dealer_url` description;
- annotations and tool names;
- result text behavior;
- any ranking/search code.

This is a wording-only change with a deliberately tiny blast radius.

## 7. No-regression acceptance plan

The redline is accepted only if **both ChatGPT and Claude** continue to create materially equivalent correct calls and results.

### A. Baseline capture before change

Record:

- current V2 SHA;
- exact current main tool description;
- exact current input-schema descriptions;
- exact test MCP endpoint;
- date/time and host/model used.

### B. High-risk intent set

Run old wording and candidate wording against the same prompt set. At minimum include:

1. family SUV with no named model;
2. reliable teen-driver car with no named model;
3. commuter car with no named model;
4. towing vehicle with no named model;
5. broad hybrid request with no named model;
6. hybrid **required**;
7. hybrid **preferred**;
8. PHEV required;
9. EV broad request;
10. explicit cheapest intent;
11. `best in my budget` to ensure it does not become `cheapest`;
12. lower-risk request;
13. explicit trim required vs preferred;
14. exact VIN request;
15. cross-brand multi-model request.

### C. Compare host-generated arguments

For each host and prompt, record whether the candidate wording preserves:

- correct tool selection;
- real candidate model resolution where required;
- manufacturer-free model values;
- correct `vehicleNeeds` soft context;
- correct electrification types;
- correct required/preferred electrification behavior;
- correct priority axis;
- hard constraints from the user's prompt;
- no invented constraints.

### D. Fail criteria

Reject or revise the redline if either host materially worsens on any critical behavior, especially:

- omits candidate models for practical-needs searches;
- sends broad electrification without viable model/variant scope;
- includes gas variants when electrification was required;
- maps `best in my budget` to `cheapest`;
- drops an explicit hard field;
- starts inventing constraints;
- chooses a wrong tool or fails to call the tool where current V2 succeeds.

### E. Acceptance

Only after both-host comparison passes:

1. Claude commits the approved wording-only diff to the V2 release line;
2. automated schema/contract tests pass;
3. exact deployed SHA is verified;
4. the accepted description snapshot and results are recorded in `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`;
5. then the Anthropic V1-vs-V2 submission decision is revisited.

## 8. Anthropic submission implication

Because V1 contains the same assistant-directed-imperative class Anthropic previously rejected, there is a credible risk that simply waiting preserves time in queue but ends with predictable description feedback.

However, V2 should not replace V1 until the minimal redline above passes both-host testing. The pending submission must remain untouched until André explicitly chooses the Anthropic path.

## 9. Manual test plan for the next ChatGPT session

Claude token limits mean host testing can be driven manually by André in a fresh ChatGPT conversation. Prepare one stable candidate MCP endpoint and run the numbered prompt pack above twice where practical: first against the current V2 wording baseline and then against the candidate wording. Capture screenshots/tool-call arguments/results and add them to the release ledger. Claude can perform the parallel Claude-host run when a fresh Claude session is available.

## 10. Related infrastructure test

Separately from description testing, perform the clean ChatGPT endpoint experiment before locking the permanent shared-test hostname:

- A: long Vercel Preview/branch alias, Vercel Authentication confirmed off;
- B: short `ccfmc-dev` Vercel hostname;
- C: short temporary owned `getcarwise.app` hostname;

Use the same application SHA and configuration for all three. Test connector creation, MCP tool invocation, widget/resource loading, and origin/CSP behavior. This distinguishes a true hostname-length/sandbox issue from Vercel Authentication or historical platform behavior.

## 11. Decision status

- Exact production/test hostnames: **NOT APPROVED**.
- V2 description redline: **PROPOSED for André review**.
- Application implementation: **NOT STARTED**.
- Anthropic pending submission: **UNCHANGED / IN REVIEW**.
- V3: **HARD PAUSED pending V2 baseline/rebaseline work**.
