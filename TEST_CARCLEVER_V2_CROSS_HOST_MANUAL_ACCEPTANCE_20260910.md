# CarClever V2 Cross-Host Manual Acceptance — 2026-09-10

**Status:** ACTIVE — systematic V2 regression testing, one case at a time  
**Purpose:** Final manual host-level validation of the current V2 contract in ChatGPT and Claude, followed by a single same-prompt V1 baseline comparison after the V2 cross-host baseline is established.  
**Candidate:** current `release/v2`; test current V2 exactly as-is.  
**Method:** Natural user prompts only. Do not change code or descriptions unless completed testing provides concrete defect evidence.

## Locked testing sequence

1. Run one natural-language case on ChatGPT V2 and capture answer/widget evidence plus actual Desktop request JSON when exposed.
2. Run the same case on Claude V2 and capture `Request → Response → Widget` when useful.
3. Compare host interpretation, backend behavior, and UI separately.
4. Run the same prompt once through ChatGPT V1 as the legacy request-semantics baseline. A second V1 host is not required unless a case exposes a material V1 host ambiguity.
5. Record the full case once, after the V1 baseline, before moving to the next test.

**Evidence rule:** ChatGPT Desktop exposed request JSON and Claude Request are primary request evidence. ChatGPT Web/Mobile reconstructed JSON is diagnostic only, not proof of the original MCP request. Full response payloads do not need to be copied when request JSON plus visible result/widget evidence is sufficient; capture full responses when something is surprising, incorrect, geographically odd, or directly relevant to the behavior under test.

## Test #1 — large SUV + strict price ceiling + ZIP

**Prompt:** `Find me a large SUV under 60k in 90210`

**Overall status: CLOSED — PASS.**

ChatGPT V2 actual request:

```json
{
  "priceMax": 60000,
  "priorityAxis": "best_for_budget",
  "zip": "90210",
  "bodyType": "SUV",
  "model": "Tahoe, Expedition, Sequoia, Yukon, Armada, Wagoneer",
  "vehicleNeeds": ["large SUV"]
}
```

Claude V2 actual request:

```json
{
  "model": "Tahoe,Suburban,Yukon,Expedition,Explorer,Highlander,4Runner,Pilot,Ascent,Telluride,Pathfinder",
  "bodyType": "SUV",
  "priceMax": 60000,
  "zip": "90210",
  "priorityAxis": "best_for_budget"
}
```

ChatGPT V1 actual request:

```json
{
  "bodyType": "SUV",
  "model": "Tahoe,Suburban,Yukon,Yukon XL,Expedition,Expedition MAX,Sequoia,Armada,Wagoneer,Grand Wagoneer,Escalade,Escalade ESV,Navigator,QX80",
  "priceMax": 60000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget",
  "zip": "90210",
  "radiusMiles": 50,
  "goals": [
    "large full-size SUV",
    "spacious interior",
    "strong value under budget"
  ]
}
```

**Verdict:** PASS — V2 preserves material V1 behavior for this case. Host candidate breadth varies, but no backend or UI regression was demonstrated. No code or description change recommended.

## Test #2 — hybrid SUV + approximate budget + city location

**Prompt:** `Find me a hybrid SUV around $35k in Austin.`

**Overall status: CLOSED — PASS WITH WATCH ITEMS.**

ChatGPT V2 actual request:

```json
{
  "bodyType": "SUV",
  "electrificationRequirement": "required",
  "electrificationTypes": ["hybrid"],
  "model": "Toyota RAV4 Hybrid, Honda CR-V Hybrid, Hyundai Tucson Hybrid, Kia Sportage Hybrid, Ford Escape Hybrid",
  "priceMin": 30000,
  "priceMax": 37000,
  "priceFlexibility": "flexible",
  "priorityAxis": "best_for_budget",
  "radiusMiles": 50,
  "state": "TX",
  "zip": "78701",
  "vehicleNeeds": ["hybrid SUV around $35,000 in Austin"],
  "transmission": "Automatic"
}
```

Claude V2 actual request:

```json
{
  "bodyType": "SUV",
  "model": "RAV4 Hybrid,Highlander Hybrid,CR-V Hybrid,Venza,Sorento Hybrid,Sportage Hybrid,CX-50 Hybrid",
  "priceMax": 35000,
  "priceFlexibility": "flexible",
  "priorityAxis": "best_for_budget",
  "zip": "78701"
}
```

ChatGPT V1 actual request:

```json
{
  "bodyType": "SUV",
  "model": "RAV4 Hybrid,RAV4 Prime,CR-V Hybrid,Tucson Hybrid,Tucson Plug-In Hybrid,Sportage Hybrid,Sportage Plug-In Hybrid,Escape Hybrid,Escape Plug-In Hybrid,Corolla Cross Hybrid,Venza,Highlander Hybrid,Santa Fe Hybrid,Sorento Hybrid,Sorento Plug-In Hybrid,Niro,Niro Plug-In Hybrid,Hornet Plug-In Hybrid,Grand Cherokee 4xe,Wrangler 4xe",
  "priceMax": 35000,
  "priceFlexibility": "flexible",
  "priorityAxis": "best_for_budget",
  "zip": "78701",
  "radiusMiles": 50,
  "goals": [
    "hybrid or plug-in hybrid SUV",
    "good value around $35k",
    "Austin-area availability"
  ]
}
```

**Assessment:** Core V2 functionality passes. Both V2 hosts preserved hybrid SUV intent, approximate-budget semantics, Austin location and `best_for_budget`. ChatGPT V2 used explicit electrification fields and a flexible band; Claude V2 used an all-hybrid model list plus `priceFlexibility: flexible`. ChatGPT V1 preserved the legacy capability and transparently broadened hybrid to include PHEVs.

**Watch items:**
- ChatGPT V2 used manufacturer-prefixed model entries despite the V2 model naming rule.
- ChatGPT V2 invented `transmission: "Automatic"`.
- Claude V2 surfaced a Sherman, TX listing for an Austin request. Because V1 and V2 differ in radius/default behavior and no backend failure was established, retain this as a geography/result-quality watch item rather than a blocker.

**Verdict:** PASS WITH WATCH ITEMS. No code or description change recommended from Test #2 alone.

## Test #3 — direct make/model + required trim + strict price ceiling

**Prompt:** `Find me a Toyota Camry XSE under $35k in 10001.`

**Overall status: CLOSED — PASS WITH WATCH ITEMS.**

### ChatGPT V2

Actual Desktop request:

```json
{
  "make": "Toyota",
  "model": "Camry",
  "trimRequired": "XSE",
  "priceMax": 35000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget",
  "radiusMiles": 50,
  "state": "NY",
  "zip": "10001",
  "bodyType": "Sedan",
  "transmission": "Automatic",
  "vehicleNeeds": [
    "Toyota Camry XSE under $35,000 near ZIP 10001"
  ]
}
```

Observed result showed two verified Toyota Camry XSE listings near the requested ZIP after filtering, both under $35k. Trim behavior was correct and no unrequested condition/year/mileage limits were applied.

Request assessment:
- **PASS:** explicit `make: Toyota`, `model: Camry`, `trimRequired: XSE`, strict `$35k` ceiling, ZIP `10001`, and `best_for_budget` correctly preserve the prompt.
- **WATCH:** ChatGPT again added `transmission: "Automatic"` without user instruction. This repeats the Test #2 host behavior.
- **WATCH / LOW IMPACT:** `bodyType: "Sedan"` is inferred rather than requested, but for an explicitly named Camry XSE it is redundant and did not materially narrow the intended vehicle identity.
- **PASS:** no invented condition, year, mileage, drivetrain, history, CPO or ownership requirement.

UI observation from André's screenshot: the widget header showed **“Scan 3.4 million → 5 found”** while also showing **“2 shown”** and only two cards. This is a minor count-consistency issue: the distinction may reflect pre-filter candidates versus final display survivors, but the labels do not make that distinction clear to the user. Treat as a non-blocking UI watch item.

### Claude V2

Actual Request:

```json
{
  "make": "Toyota",
  "model": "Camry",
  "trimRequired": "XSE",
  "priceMax": 35000,
  "priorityAxis": "best_for_budget",
  "zip": "10001"
}
```

Claude reported five trim-confirmed, VIN-verified Camry XSE matches under budget. Examples spanned Long Island City, NJ and PA.

Request assessment:
- **PASS:** clean direct identity mapping with `make`, `model` and `trimRequired`.
- **PASS:** strict budget intent preserved via `priceMax: 35000`; no contradictory flexibility was added.
- **PASS:** no invented transmission, body type, condition, year, mileage, drivetrain, history or radius constraint.
- **PASS:** `best_for_budget` is appropriate.

### ChatGPT V1 baseline

Actual request:

```json
{
  "make": "Toyota",
  "model": "Camry",
  "trimRequired": "XSE",
  "priceMax": 35000,
  "priceFlexibility": "strict",
  "priorityAxis": "best_for_budget",
  "zip": "10001",
  "radiusMiles": 50,
  "goals": [
    "Toyota Camry XSE under $35k",
    "good value near 10001"
  ]
}
```

V1 reported the same 677-match universe and returned relevant XSE examples in Long Island City, NJ and PA. This shows the broader geographic result spread seen in Claude V2 is not itself a demonstrated V2 regression.

### V1 ↔ V2 comparison

- **Vehicle identity:** preserved. All three requests encode Toyota + Camry + required XSE trim correctly.
- **Budget:** preserved. V1 explicitly uses `priceFlexibility: strict`; ChatGPT V2 does the same; Claude V2 omits the flag but returns only under-budget results and does not show flexible widening.
- **Location:** all use ZIP `10001`. ChatGPT V1/V2 explicitly use 50 miles; Claude V2 relies on service/default behavior. The result geography is broadly comparable to V1 and therefore not a demonstrated V2 regression.
- **Host inference:** Claude V2 is the cleanest request. ChatGPT V2 adds redundant sedan and unrequested automatic transmission. The repeated automatic inference should remain on the cross-case watch list.
- **Trim enforcement:** PASS. V2 results were explicitly XSE/trim-confirmed.
- **UI:** functional, with one minor count-label consistency issue on ChatGPT V2.

**Verdict:** PASS WITH WATCH ITEMS. V2 preserves the material V1 direct make/model/required-trim behavior. No backend regression demonstrated. No code or description change recommended from this case alone.

## Cross-case watch list after Test #3

1. **ChatGPT V2 repeatedly invents `transmission: "Automatic"`** when not requested (Tests #2 and #3). Continue observing whether this appears in unrelated cases before deciding whether it warrants description/tool-contract action.
2. **ChatGPT V2 model naming** used manufacturer-prefixed cross-brand model candidates in Test #2; watch for recurrence in another broad candidate-resolution case.
3. **Widget count-label consistency:** Test #3 showed “5 found” with “2 shown” and two final cards. Non-blocking, but record recurrence if seen again.
4. **Geographic breadth/default radius:** Claude V2 may return geographically broad results when radius is omitted. Test #3 V1 comparison shows broad geography can also occur in the legacy baseline, so do not classify as a V2 defect without stronger evidence.

## Remaining coverage

Select later cases one at a time. Remaining coverage includes body style vs finer vehicle type; city/state/ZIP/radius; strict vs approximate price; ranking axes; drivetrain/transmission/cylinders/colors/doors; trim preferred vs required; hybrid/PHEV/EV required vs preferred; used/new/CPO/history/one-owner; exact VIN/not-found VIN; thin/zero results and widening; UI/link behavior; practical-needs expansion; and negative non-inventory requests where the connector should not be called.
