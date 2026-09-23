# September scale-down feasibility checkpoint — 2026-09-23

**Task:** narrow read-only review for André's Sep 30 decision. This builds on the existing runway, Fractal Free-tier and field-ledger work. No subscription, production, submission, website, ad or budget change was made. Current charges, renewals and usage are still account-level unknowns.

## Confirmed dependency map

| Surface | Auto.dev | Fractal | Consequence of proposed cuts |
|---|---|---|---|
| Old live ChatGPT @CarClever | Shared key; Free listings/photos/VIN decode, Growth rich specs/recalls/payments/APR/TCO currently used in old code | **Required backend** | Auto.dev Free needs capability guards, honest fallback labels and quota proof; Fractal cancellation ends this live app unless migrated, which is not part of this plan. |
| WordPress page 239, old CarClever Lite | Indirect via old Fractal app | **Required** | It cannot be left pointing at a cancelled backend. Page 239 remains unchanged today; a measured cutover/retirement and rollback need separate approval. |
| Find My Car V2, ChatGPT/Claude submissions | Shared key; documented Free-class listings/VIN decode/photos, Growth specs enrichment off | No | Auto.dev Free should preserve shipped V2 features subject to the shared cap, but must pass a regression and endpoint/cold-start check. |
| Meta Muse connector | Submitted custom Vercel MCP path | No direct Fractal dependency reported | Verify its current data-call path and endpoint health before the account change; do not assume it is insulated from the shared Auto.dev cap. |
| Lite V2 standalone | Vercel live path | No direct Fractal dependency reported | It is a viable separate journey, but does not itself replace page 239 or every old Fractal feature. Verify actual data dependency and capacity. |
| Deal Score, Price Check, VIN Check website pages | Prior infrastructure audit says Auto.dev direct | No | Growth-to-Free may remove data fields these pages expect; exact current endpoint usage and user-visible fallback must be checked, not inferred from V2. |

The current Fractal field ledger proves old app calls to `/listings`, `/photos/{vin}`, `/specs/{vin}`, `/recalls/{vin}`, `/apr/{vin}`, `/payments/{vin}` and `/tco/{vin}`, plus NHTSA/vPIC and ZIP helpers. Its own assessment identifies an unguarded Specs request. Auto.dev [currently lists](https://www.auto.dev/pricing) 1,000 capped Free calls/month across VIN Decode, Listings and Photos; Specifications, Recalls, TCO, Payments and Interest Rates are Growth products. Code-use proof is not a live usage count or safe fallback test.

## Cost scenarios, arithmetic corrected

August bank-recorded run-rate is approximately **A$708/month**: Auto.dev 469, Fractal 58, Claude Team 78, personal Claude Pro 31, ChatGPT Plus 28, Workspace 26, Microsoft 365 10 annualized, hosting/domain/email 8. September charges and cancellation dates must be checked in the actual accounts.

| Scenario | Approx. A$/month | What remains | Blocking proof |
|---|---:|---|---|
| Current stack | 708 | All current services | Confirm current bill/renewal; no change. |
| Auto.dev Free + personal Pro Free; **paid Fractal retained** | 208 | Old ChatGPT app and page 239 may stay hosted | Shared quota and truthful Free behavior; Fractal renewal and production terms. |
| Auto.dev Free + Pro Free + **genuine $0 Fractal production tier** | 150 | Old app/page 239 only if $0 tier really sustains endpoints | Fractal dashboard terms, reliability and quota; not independently verified. |
| Auto.dev Free + Pro Free + **Fractal cancelled** | 150 | V2/Muse/Lite V2 and other Vercel/website paths only | Old app/page 239 exit or approved replacement; direct website tool Free behavior; shared cap. |

The prior runway document's ~A$208 “lean waiting posture” wording says Fractal is retained only if genuinely $0. That precondition conflicts with its arithmetic: A$208 includes the A$58 Fractal bill, whereas $0 Fractal yields about A$150. This table resolves the decision options without changing booked costs. Savings are **not** automatically a marketing budget.

## New evidence: Auto.dev dashboard screenshot supplied Sep 23

The screenshot shows Growth at **US$299/month**, **10,987 total API requests** in the current summary period, **14,965 API requests over the selected last 30 days**, and **US$14.80 estimated usage charges this month**. The $14.80 is not the full subscription bill. The daily chart includes Listings and several Growth-only endpoint families. These are **all-key mixed totals**, heavily affected by building and testing according to André. They cannot identify real users, production call volume, conversion, or which app generated each request. Do not extrapolate 523 requests/day to customer demand.

The mixed 14,965 count exceeds Free's 1,000-call monthly cap by roughly 15×; more than 93% of it would have to disappear or be excluded to fit. That is a sensitivity check, **not** a finding that real use exceeds the cap. If development/testing continues on the same key after a downgrade, those calls themselves can exhaust Free even when real user demand is tiny.

**André's observation rule (Sep 23):** Stop discretionary development and testing now. Keep live services unchanged through the Sep 30 checkpoint and read only the natural daily/weekly dashboard deltas. Do not attempt to reconstruct which historical Auto.dev calls were owner tests. This passive period measures combined live/background usage under a no-test operating posture, **not** unique users; it cannot predict demand if a pending app is approved or if testing resumes. If the period is too short or background probes still dominate, capacity remains uncertain. Any later Free-mode regression or new tagging is a separate technical step after the checkpoint and before an approved plan switch.

## Partner outcome evidence supplied Sep 23

| View/window shown | Observed | Interpretation |
|---|---|---|
| CJ, “This Year” dashboard | 493 clicks, **2 leads**, US$20 commission, 0.41% displayed conversion; André says the two real leads were last month and not his tests. | The only reported non-owner lead outcome so far; source within CJ remains unproven. The 493 clicks include earlier activity and cannot be equated with qualified customers. |
| Impact home snapshot, Aug 25–Sep 23 | 18 clicks, **0 actions**, US$0 earnings. | Impact became the active route only recently; this broad window includes pre-switch dates and test traffic. Too early and too mixed to estimate conversion. |
| Impact “Performance by Referring Domain,” Sep 10–23 | 18 clicks, 0 actions; 1 listed as `getcarwise.app`, 17 “No referring domain.” | “No referring domain” is **not an MCP-app source label**. It could include app handoffs, browser/referrer suppression, redirects and owner tests. André's MCP attribution is a hypothesis, not verified. The report notes some metrics have delay. |

The CJ two-lead outcome and the Impact zero-action snapshot are from different programmes/windows and cannot form a before/after conversion comparison. Do not call the Impact 18 clicks real customer visits or conclude that the switch failed. Revisit action and click details after reporting matures and a period without owner test clicks. Existing Impact work is retained; no repeated monitoring/tool research is needed now.

## Sep 30 readiness test — smallest missing evidence

1. **Billing (André, account views):** September billed amount, next renewal and effective downgrade/cancellation dates for Auto.dev, Fractal and personal Claude Pro; confirm Fractal free production tier and whether published endpoint/review identity survives a plan change.
2. **Passive no-test observation:** record Auto.dev daily totals after André stops discretionary testing; compare with 1,000 shared calls/month and identify any obvious background probe/cold-start pattern only from existing records. Do not classify historical dashboard traffic or run a new test to produce a “clean” number. Record CJ/Impact approved actions separately; no-referrer clicks are unknown source.
3. **Free behavior gate after passive period, before any switch:** review the existing Fractal field/capability audit and identify the unresolved Specs guard, Growth-only labels and direct WordPress dependencies. Any controlled regression test is deferred until André approves the cost path and the observation period ends; then record results and rollback before switching plans.
4. **Fractal exit inventory (technical/editorial owner):** exact page-239 embed and other inbound links; decide retain paid/free vs approved cutover/retirement of old live app and page, with screenshots and rollback. Decision Center and Lite V2 existence do not complete this cutover.
5. **Lead evidence:** reuse prior Impact work; ask only whether the two old approved leads can now be assigned to old Fractal vs other routes. If still unattributed, mark unknown.

**Decision rule:** Choose the cheapest configuration whose live paths still pass functional, truthful-output and quota checks. If passive no-test combined usage projects comfortably below 700 calls/month, that supports a Free proposal **only after** Growth-call guards, direct-tool behavior, a later narrow regression and rollback are verified. It does not estimate approved-app or resumed-QA demand. At 700–1,000 or unknown failed-call semantics, resolve avoidable calls or retain Growth temporarily. Above 1,000, decide between a time-bound paid renewal supported by measured value and a deliberate retirement; never silently break live paths. No downgrade is authorized here.

## Marketing budget handoff

After the cost configuration and André's weekly hours are known, size a separate test budget from an amount he is willing to risk, not from unverified “savings.” With a US$10 approved New/Used lead, paid-media break-even CPC is `US$10 × approved-lead-per-paid-click`; source-specific conversion remains unknown. The first marketing-budget decision should compare no-cash/direct-directory-link and partnership/owned-channel distribution with any capped paid test, including its approved-lead stop rule. Do not launch ads or public promotion from this checkpoint.

**Immediate operating step:** observe unchanged live services without discretionary development/testing through Sep 30. At that checkpoint, review natural Auto.dev deltas, Impact action maturity and Fractal plan/renewal/free-hosting terms. No new tagging or test traffic is part of this step. Marketing-budget allocation follows the confirmed cost and lead picture.