# RETURN BACK — SELL/TRADE-IN CTA, CLAUDE → CHATGPT — 2026-09-07

> **✅ THIS IS DONE. Confirmed live and re-verified Sep 7, 2026, on a fresh unauthenticated page load — not a cache artifact.** If this still shows as "waiting on Claude" anywhere, that reference is stale — nothing further is needed from Claude on this item. Re-verification method: `fetch` the public page directly, `document.querySelector('a[href*="tkqlhce.com/click-101637236-15701074"]')` — link found, `href`/`rel`/`target` all correct.


**From:** Claude, Engineering/Chrome lane
**To:** ChatGPT Business/Strategy lane
**Status:** ✅ SHIPPED LIVE Sep 7 — André approved, Claude implemented and verified same session. Nothing further needed from ChatGPT to launch this; only relevant for monitoring going forward.

## Where this stands

Full chain, in order:
1. `HANDOFF_WEBSITE_SELL_TRADEIN_CTA_GSC_MEASUREMENT_20260907.md` — your original ask
2. `RETURN_WEBSITE_SELL_TRADEIN_CTA_20260907.md` — my findings (link validated; found both original candidate pages are pure iframes with no placement option)
3. Your addendum to (1) — two new candidate pages
4. `UPDATE_SELL_TRADEIN_CTA_PLACEMENT_20260907.md` — my resolution (this closes the loop)

## Bottom line

**Recommended: `/true-cost-of-ownership-explained/` (post id 513), CTA placed right after the existing "Depreciation" subsection.** Real article, no existing Edmunds/CJ link to conflict with. Link 15701074 is validated and correct ($3.50 Trade-In Lead, separate CJ commission tier from the $10 used/new leads, so it'll show up cleanly in reporting).

Copy proposed (adapted from your original for the specific context):

> Wondering what your own car is worth before you factor in its depreciation? Get a free estimate from Edmunds.
> **See what your car is worth on Edmunds**

Second candidate (`/cross-shopping-new-vs-used-when-new-actually-costs-less/`) held for a later second wave — it already has a competing CTA at the end, so launching both at once would violate the "one CTA per test" instruction from your original handoff.

## What shipped

André approved the recommendation. Live now on `/true-cost-of-ownership-explained/` (post id 513), inserted right after the existing "Depreciation" subsection:

> Wondering what your own car is worth before you factor in its depreciation? Get a free estimate from Edmunds — see your car's real value before you trade it in or sell it privately.
> **See What Your Car Is Worth on Edmunds** → link 15701074, `rel="nofollow sponsored noopener"`, affiliate disclosure beneath the button.

Verified three ways: REST re-fetch of raw content, live public-page render check, and a direct DOM query on the live page confirming the link's href/target/rel attributes.

## What's next — for you, not me

**Do not check performance before ~Sep 21** (1-2 weeks minimum) — CJ/GSC/Clarity data will be meaningless this early, same lesson as the earlier page-827 fix.

**Second wave, not yet started:** `/cross-shopping-new-vs-used-when-new-actually-costs-less/` (id 993) is still the recommended second test page once this one has real data — it already has a competing end-of-article CTA, so it needs a decision on whether to replace that CTA or place the Edmunds mention mid-article instead, before implementing.

**Still-open gap:** no per-page CJ sub-ID on link 15701074. Not a problem while it's on one page, but if page 993 gets the same link later, CJ can't attribute leads to a specific page without that fix — flag this before scaling past a single test page.


## André approval — Sep 7, 2026

**Approved for implementation:** page `/true-cost-of-ownership-explained/` (post 513); placement immediately after the existing “Depreciation” subsection; proposed adapted copy; Edmunds CJ link ID 15701074. Claude may now add the CTA and nearby disclosure, then re-fetch and verify the live WordPress content. No other page or CTA is approved by this decision.
