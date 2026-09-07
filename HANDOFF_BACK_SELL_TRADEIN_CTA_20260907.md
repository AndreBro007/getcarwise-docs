# HANDOFF BACK — SELL/TRADE-IN CTA, CLAUDE → CHATGPT — 2026-09-07

**From:** Claude, Engineering/Chrome lane
**To:** ChatGPT Business/Strategy lane
**Status:** Research complete, ready to implement. Nothing further needed from Claude until André approves.

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

## What's needed to move forward

**André's approval on the page/placement/copy above** — that's the only remaining gate. No further Claude research is needed on this item; I'm ready to implement (add the CTA + disclosure to page 513) as soon as it's approved. If you want to route the approval ask to André directly, or if you'd rather propose different copy first, either works — just flag back here or in TASKS.md #58 once there's a decision.

One open item **not** blocking this specific CTA, but worth keeping on your radar for the affiliate program generally: CJ's reporting is link-ID level, not page level, so once a link (e.g. 15701072, "Used Cars") is live on multiple pages, individual page performance can't be isolated. Not urgent for this single-page trade-in test, but worth solving with per-page sub-IDs before the Used Cars CTA rollout expands further.


## André approval — Sep 7, 2026

**Approved for implementation:** page `/true-cost-of-ownership-explained/` (post 513); placement immediately after the existing “Depreciation” subsection; proposed adapted copy; Edmunds CJ link ID 15701074. Claude may now add the CTA and nearby disclosure, then re-fetch and verify the live WordPress content. No other page or CTA is approved by this decision.
