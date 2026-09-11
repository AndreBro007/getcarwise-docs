# CarClever OpenAI V2 Submission Reconciliation — 2026-09-11

**Status:** SUBMISSION CONTENT READY; TWO GATES REMAIN BEFORE ACTUAL SUBMISSION  
**Lane:** ChatGPT Business/Strategy  
**Execution:** documentation/reconciliation only. No app code, deployment, Vercel, DNS, connector, or submission state changed.

## 1. Executive conclusion

The V2 regression and reviewer-facing QA bank is now strong enough to move from testing into final OpenAI submission preparation.

Current tested V2 source is `AndreBro007/carclever-find-my-car` branch `release/v2` at:

`a5d96960792d1de3cd4eaf81ccef0a1515acf04f`

Current tested V2 MCP endpoint:

`https://ccfmc-dev-v2.vercel.app/mcp`

That `.vercel.app` endpoint is a test/release endpoint, **not the recommended permanent OpenAI production origin**.

Two gates remain before an actual submission should be made:

1. **André must confirm the permanent OpenAI MCP origin.** Preferred existing strategy recommendation: `https://findmycar.getcarwise.app/mcp`. No DNS/Vercel/domain work is authorized merely by this document.
2. **The final production-origin smoke must be run after Engineering maps that approved origin to the exact tested V2 release.** Verify exact SHA, MCP initialize/tools metadata, widget/resource/CSP behavior, links, current VIN fixture, Scan Tools/equivalent, and the final submission prompts.

Until both gates are satisfied, status is **READY TO PREPARE, NOT READY TO CLICK SUBMIT**.

## 2. What changed versus the prior OpenAI submission

The prior submission artifact (`carclever-find-my-car-1-0-0`) used the V1 production MCP URL and a substantially older `find_matching_vehicle` contract.

The final V2 submission must not copy the old resource metadata/schema. The submission flow should populate MCP metadata from the final V2 endpoint itself.

Material V2 contract differences now include:

- `goals` is no longer accepted; the schema is strict and rejects it.
- `vehicleNeeds` is the short listing-relevant practical-needs context field.
- electrification is first-class through `electrificationTypes` (`hybrid`, `plug_in_hybrid`, `electric`) plus `electrificationRequirement` (`required`, `preferred`).
- `used` means used-only when true, new-only when false, and **must remain unset when condition was not stated or clearly implied**.
- `transmission` should only be supplied when stated or clearly implied.
- `vehicleType` is only for a finer classification than `bodyType`; it should not duplicate a broad body style.
- `lower_risk` is a ranking objective, not a promise of safety or clean history.
- `cpo`, `noAccidents`, and `oneOwner` express requested evidence; missing/unreported evidence remains unknown rather than being treated as false or clean.
- exact VIN lookup remains inside `find_matching_vehicle`; V2 does not expose the paused V3 `check_vehicle` tool.
- `resolve_dealer_url` now resolves to an Edmunds VIN-specific affiliate URL where possible, otherwise an Edmunds similar-vehicle fallback. Dealer URLs remain diagnostic/internal rather than the user-facing resolved destination.

The current V2 public description includes the explicit anti-invention rule:

> Direct filter fields should reflect requirements the user stated or clearly implied; leave unstated restrictions unset.

## 3. Recommended final app metadata copy

### Display name

Keep:

`CarClever - Find My Car`

### Subtitle

Current prior value is acceptable:

`Live car search, made smart`

Safer alternative if André wants to eliminate any possible ambiguity around the word "live":

`Current car search, made smart`

**Recommendation:** keep the existing subtitle unless OpenAI specifically flags "live" as an availability claim. The long description below clearly defines the capability boundary.

### Recommended description

> Find My Car searches current U.S. vehicle listings to help shoppers find cars that fit their stated requirements, practical needs and buying priorities. Search by make/model, price, year, mileage, location, body style, drivetrain, transmission, trim, color, condition and electrification, with priorities such as best for budget, cheapest, newest, lowest mileage or lower-risk options. For broader needs such as family use, commuting, towing or reliability, CarClever can identify relevant models and then search and rank current listings using available listing evidence. Already found a car? Look up an exact VIN and run a Buyer Check that summarizes reported good signs, concerns and items to verify before buying. Missing accident, ownership, CPO or specification data stays unknown rather than being assumed. Listing links show where a vehicle is currently listed; dealer inventory can change, so physical availability, final condition and out-the-door pricing should be confirmed directly.

Why this replaces the prior wording:

- preserves the strong product story;
- accurately reflects V2's first-class electrification and practical-needs architecture;
- keeps Buyer Check inside exact-VIN search;
- avoids implying CarClever independently proves reliability/towing suitability;
- avoids treating current listing presence as guaranteed physical dealer availability.

## 4. Commerce / affiliate disclosure reconciliation

Commerce should remain enabled because CarClever directs users to external marketplace pages and may earn affiliate revenue.

Recommended commerce explanation:

> CarClever is a vehicle-research and listing-discovery utility. It links users to Edmunds pages for specific vehicles when available, or to similar Edmunds vehicle pages when an exact listing link is unavailable. CarClever does not sell vehicles, process payments, broker transactions or independently verify physical dealer availability. Any vehicle purchase or availability confirmation occurs outside CarClever with the marketplace, dealer, retailer or seller. CarClever may earn affiliate revenue from qualifying traffic to Edmunds.

This replaces the older phrasing that could be read as CarClever itself performing a definitive availability check.

## 5. MCP/tool contract for the submission

Final V2 should expose exactly the current V2 tools:

### `find_matching_vehicle`

Use for current U.S. vehicle-listing searches and exact-current-listing VIN lookups. The live V2 description is the source of truth and should be discovered from the final MCP endpoint rather than pasted from the old submission JSON.

Key reviewer-facing contract:

- direct fields reflect stated/clearly implied requirements;
- unstated hard restrictions stay unset;
- broad practical needs may be interpreted into relevant model candidates before search;
- required/preferred electrification is explicit;
- exact VIN means exact VIN only, never a similar substitute;
- history/CPO/ownership may be confirmed, contradicted or unreported;
- general automotive education, repair, financing/leasing and non-listing comparisons are out of scope.

### `resolve_dealer_url`

Use to resolve a selected vehicle to a usable Edmunds destination.

Current V2 behavior:

- prefers the VIN-specific Edmunds affiliate URL;
- otherwise returns the Edmunds make/model fallback where possible;
- does not present the dealer's own URL as the resolved user-facing destination;
- is read-only and does not reserve, purchase or confirm dealer stock.

## 6. Recommended final positive test cases

### Test 1 — explicit used CR-V constraints

**Prompt**

`Find a used Honda CR-V under $25,000 with less than 60,000 miles near 90210.`

**Expected output**

> Returns current used Honda CR-V listings matching the stated $25,000 ceiling, mileage cap and 90210 location as closely as current inventory allows. It does not add unstated year, trim, drivetrain or history restrictions. A vehicle with unreported mileage must not be presented as verified under the 60,000-mile limit.

**Validated:** ChatGPT V2 PASS; Claude V2 Cleanroom PASS with minor prose watch; V1 baseline PASS.

### Test 2 — reliable used hybrid SUV

**Recommended stabilized prompt**

`Find a reliable used hybrid SUV under $50,000 with less than 60,000 miles near 90210.`

This deliberately adds the word **used** compared with the prior submission prompt.

Reason: the exact older prompt omitted condition, but both ChatGPT V2 and Claude V2 inferred `used:true` during the final regression. That inference was useful in the observed results but is still an unstated hard restriction. Adding `used` makes the submission prompt deterministic and aligned with the tool contract rather than knowingly submitting an ambiguity that current hosts may resolve inconsistently.

**Expected output**

> Treats hybrid as required, searches relevant used hybrid SUVs, preserves the $50,000 price cap, 60,000-mile cap and 90210 location, and uses available listing/history evidence plus sensible model interpretation to rank useful options. Reliability may guide model selection but must not be presented as independently proven by the listing data.

**André confirmation needed:** approve this one-word submission-test change (`used`) or deliberately retain the prior ambiguous prompt.

### Test 3 — low-risk used F-150 for towing

**Prompt**

`Find a low-risk used F-150 under $50,000 for towing near Denver.`

**Expected output**

> Returns current used Ford F-150 listings under $50,000 near Denver, uses lower-risk ranking to prioritize stronger available purchase-risk evidence, and treats towing as a suitability need rather than inventing a specific tow package, axle ratio, engine or payload requirement. It should state that VIN-specific towing configuration still needs verification.

**Validated:** ChatGPT V2 PASS; V1 baseline PASS. Claude remained useful but added unstated `noAccidents:true` and `oneOwner:true`, so that behavior stays a host-inference watch rather than the intended contract.

### Test 4 — exact VIN Buyer Check

The old fixture `4T1BF3EK7BU748352` is no longer a current live listing and should be retired from the final test case.

**Current recommended fixture:**

`4T1DAACK6SU582551`

**Prompt**

`Check VIN 4T1DAACK6SU582551 for red flags before I buy it.`

**Expected output**

> Looks up that exact VIN only, returns the current listing if still present, and presents a Buyer Check using the available evidence. In the validated Sep 11 run, the vehicle produced a Caution outcome with one reported accident. Missing title/CPO/recall-completion evidence stayed unreported or unverified rather than being invented. No similar vehicle is substituted if the VIN disappears.

**Critical:** re-run this exact VIN immediately before submission. Live listing state can change; if it is no longer present or no longer carries the needed accident evidence, replace it with a freshly validated current VIN rather than weakening the test.

### Test 5 — listing presence + destination resolution

The old label "Check availability" can remain an interface action, but the test description must not claim CarClever knows physical dealer availability.

**Recommended self-contained prompt**

`Check whether VIN 4T1DAACK6SU582551 is still listed and open its listing.`

**Expected output**

> Checks whether the exact VIN is present in current inventory data. If present, it can resolve/open the VIN-specific Edmunds listing destination; if an exact Edmunds destination is unavailable, it clearly offers a similar-vehicle Edmunds fallback. It does not guarantee that the vehicle is physically unsold, unreserved or still on the dealer lot, and the user should confirm with the seller.

This wording is more reviewer-safe than claiming a definitive "availability check."

## 7. Final negative-invocation test cases

Keep the same three prior prompts; they passed 3/3 on both ChatGPT V2 and Claude V2 Cleanroom:

1. `How do I replace the brake pads on a 2020 Honda CR-V?`
2. `What is the towing capacity of a 2024 Ford F-150?`
3. `What are the pros and cons of hybrid cars compared with gas cars?`

**Expected behavior for all three:** answer without invoking CarClever.

V1 does not need to be rerun for this negative set.

## 8. Tool justifications — recommended submission wording

### `find_matching_vehicle`

**Read-only**

> Queries current third-party vehicle inventory/listing data and returns matching evidence; it does not create, update, reserve, purchase or delete anything.

**Open-world**

> Reads current external vehicle inventory/listing and vehicle-evidence sources outside CarClever's own closed system.

**Destructive**

> No destructive or irreversible action is available; the tool only searches and returns information.

### `resolve_dealer_url`

**Read-only**

> Resolves and returns an Edmunds destination URL for a selected vehicle or similar-vehicle fallback; it does not change external state.

**Open-world**

> Builds/resolves links to external Edmunds marketplace pages outside CarClever's own closed system.

**Destructive**

> Pure lookup/link resolution; no destructive or irreversible action is available.

## 9. Screenshots

The existing three-screen story remains strategically strong:

1. discovery / reliable hybrid SUV;
2. lower-risk used F-150 for towing;
3. exact-VIN Buyer Check.

Existing screenshots were previously declared locked unless a genuine blocker emerged.

**Current recommendation:** do not automatically redo all three.

Before submission, compare each existing image against the final V2 widget and submission metadata:

- if the visual experience is still representative, reuse it;
- if V2 materially changed the visible widget, recapture the affected screenshot only;
- the old Buyer Check screenshot uses the now-stale VIN `4T1BF3EK7BU748352`. This is **not automatically a visual blocker**, because the screenshot captured a genuine prior app result, but it is a reviewer replay risk. If the submission UI associates/replays that prompt or André wants every public screenshot tied to a currently reproducible fixture, recapture screenshot #3 with the current live Buyer Check VIN. Otherwise preserve the locked screenshot.

OpenAI screenshot export requirements already documented in the project guide remain: 706 px wide, 400–860 px high, PNG/JPG, with 706×860 preferred for the carousel-style export.

## 10. Demo recording

The prior submission references an existing Google Drive demo recording.

Before reuse, manually verify the recording still represents the final V2 user experience and does not teach stale V1-only behavior such as the old schema or overstate definitive availability.

- If it remains visually/product accurate, reuse it.
- If it materially demonstrates stale contract behavior, record a short V2 replacement after the final production-origin smoke.

This is a verification gate, not an assumption that a new video is required.

## 11. Branding and policy URLs

The prior submission used:

- website: `https://getcarwise.app/`
- customer support: `https://getcarwise.app/contact-us/`
- privacy policy: `https://getcarwise.app/privacy-policy/`
- terms: `https://getcarwise.app/terms-of-service/`
- auth: NONE

No regression evidence from this test cycle requires changing those values. They should still receive a final browser reachability check immediately before submission.

## 12. Remaining host watches — not submission blockers by themselves

### ChatGPT V2

- On the older ambiguous `reliable hybrid SUV` prompt, ChatGPT added unstated `used:true` despite the current anti-invention description. Recommended mitigation for the reviewer test is to explicitly say `used` if that is the intended condition.
- ChatGPT may choose semantic model shortlists for practical-needs requests. This is acceptable product behavior when broad enough and transparently framed as AI interpretation rather than verified reliability/safety evidence.
- Host-selected radius may appear for phrases like `near Denver`; reasonable, but not a user-stated exact radius.

### Claude V2 Cleanroom

- Sometimes converts `low-risk` into hard `noAccidents:true` / `oneOwner:true`. This is not the intended contract and remains a host-inference watch.
- Has produced a few overconfident prose claims (e.g. treating unknown accident history as clean, or asserting trim-level towing/reliability facts not established by returned evidence).

These are host-layer observations. They did not establish a V2 backend regression in the validated runs and should not trigger a code change without a demonstrated user-impact failure.

## 13. Regression evidence completed for submission

Completed final reviewer-facing bank:

- exact used CR-V baseline — closed pass;
- reliable hybrid SUV baseline — closed overall pass, condition-scope watch;
- low-risk used F-150/towing baseline — closed overall pass, Claude hard-filter watch;
- exact live VIN Buyer Check — closed cross-host/cross-version pass with minor host-inference watch;
- listing-presence / link-resolution path — closed cross-host/cross-version pass with wording/routing watches;
- negative invocation bank — 3/3 pass on both active V2 hosts.

The broader specialist regression bank also covered required/preferred electrification, trim required/preferred, interior color, cylinder/V8, manual transmission, lowest-mileage/newest/lower-risk axes, CPO/history disclosure, and provider/geographic edge behavior.

## 14. Final go/no-go checklist

### Ready now

- V2 release branch regression bank completed.
- Current release source verified at `a5d96960792d1de3cd4eaf81ccef0a1515acf04f`.
- Current V2 tool description contains the anti-invention guardrail.
- Current V2 schema includes first-class electrification and rejects legacy `goals`.
- Exact VIN Buyer Check remains available through `find_matching_vehicle`.
- Negative-invocation boundary is clean on ChatGPT V2 + Claude V2 Cleanroom.
- Submission metadata/test-case copy reconciled in this document.

### Must happen before submit

- André confirms the permanent OpenAI MCP origin.
- Engineering maps that approved origin to the exact final V2 release without touching V1/Claude production.
- Final origin/SHA is verified.
- MCP initialize/tools metadata and widget resources are smoke-tested on the permanent origin.
- Current Buyer Check VIN is revalidated immediately before submission.
- Final positive and negative submission prompts are rerun on the actual submission origin.
- Scan Tools/equivalent passes on the final origin.
- Screenshot compatibility is checked; only affected images are recaptured if genuinely needed.
- Existing demo recording is checked for V2 accuracy; replace only if materially stale.
- website/support/privacy/terms URLs are reachable.
- final submission JSON is generated from the current MCP endpoint, not copied from V1 metadata.

## 15. André confirmations required

### Confirmation A — permanent OpenAI origin

**Proposed:** `https://findmycar.getcarwise.app/mcp`

This is a permanent architecture decision and requires André's explicit confirmation before Engineering performs DNS/Vercel/domain work.

### Confirmation B — reviewer hybrid prompt

**Recommended:** change the positive reviewer test from:

`Find a reliable hybrid SUV under $50,000 with less than 60,000 miles near 90210.`

to:

`Find a reliable used hybrid SUV under $50,000 with less than 60,000 miles near 90210.`

This removes the exact ambiguity that caused both active hosts to add `used:true` during regression. If André prefers to preserve the older prompt exactly, keep it and accept the documented host condition-scope watch.

## 16. Go/no-go judgment

**Current judgment: CONDITIONAL GO.**

The product/contract/test evidence is submission-grade. The remaining work is release-channel finalization and final-origin smoke testing, not another broad regression cycle.

Do **not** submit the disposable/test `ccfmc-dev-v2.vercel.app` origin as the permanent OpenAI plugin origin unless André explicitly reverses the standing permanent-domain strategy.
