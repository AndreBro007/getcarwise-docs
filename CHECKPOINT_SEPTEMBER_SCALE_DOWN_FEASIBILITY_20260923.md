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

## Sep 30 readiness test — smallest missing evidence

1. **Billing (André, account views):** September billed amount, next renewal and effective downgrade/cancellation dates for Auto.dev, Fractal and personal Claude Pro; confirm Fractal free production tier and whether published endpoint/review identity survives a plan change.
2. **Auto.dev shared usage (dashboard/logs):** 7- and 30-day calls by endpoint/status across old Fractal, V2/Lite/Muse and direct WordPress tools; daily peaks and starts; forecast against a practical <700-call comfort zone. Confirm whether blocked Growth/probe calls consume Free quota and whether the unguarded Specs call was fixed.
3. **Free behavior (technical owner, controlled test):** run one old search, detail, VIN/risk and affordability path plus one V2/Lite V2/Muse route and each direct WordPress tool. Record missing fields, labels, status codes and link destination. No “real” financing or VIN-specific recall claim if only estimates/model-level checks remain. Keep rollback.
4. **Fractal exit inventory (technical/editorial owner):** exact page-239 embed and other inbound links; decide retain paid/free vs approved cutover/retirement of old live app and page, with screenshots and rollback. Decision Center and Lite V2 existence do not complete this cutover.
5. **Lead evidence:** reuse prior Impact work; ask only whether the two old approved leads can now be assigned to old Fractal vs other routes. If still unattributed, mark unknown.

**Decision rule:** Choose the cheapest configuration whose live paths still pass functional, truthful-output and quota checks. If Free usage projects comfortably below 700 calls/month with guards and regression passing, a reversible Auto.dev downgrade can be proposed for approval. At 700–1,000 or unknown failed-call semantics, resolve avoidable calls or retain Growth temporarily. Above 1,000, decide between a time-bound paid renewal supported by measured value and a deliberate retirement; never silently break live paths. No downgrade is authorized here.

## Marketing budget handoff

After the cost configuration and André's weekly hours are known, size a separate test budget from an amount he is willing to risk, not from unverified “savings.” With a US$10 approved New/Used lead, paid-media break-even CPC is `US$10 × approved-lead-per-paid-click`; source-specific conversion remains unknown. The first marketing-budget decision should compare no-cash/direct-directory-link and partnership/owned-channel distribution with any capped paid test, including its approved-lead stop rule. Do not launch ads or public promotion from this checkpoint.

**Immediate next input:** account-level Auto.dev usage/plan and Fractal plan/renewal views (with keys and billing identifiers hidden), plus whether Fractal offers a true free hosted production endpoint. These three facts determine which A$150/A$208 option is real; the remaining controlled tests then establish safety.