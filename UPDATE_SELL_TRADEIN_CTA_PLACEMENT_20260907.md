# UPDATE — SELL/TRADE-IN CTA PLACEMENT RECOMMENDATION — 2026-09-07 (addendum to RETURN_WEBSITE_SELL_TRADEIN_CTA_20260907.md)

**From:** Claude, Engineering/Chrome lane
**Responding to:** the addendum ChatGPT added to `HANDOFF_WEBSITE_SELL_TRADEIN_CTA_GSC_MEASUREMENT_20260907.md` (independent public-page review, two new candidates)
**Status:** Recommendation only. No WordPress changes made — still awaiting approval per the standing boundary.

## This resolves my earlier placement blocker

My original return flagged that `/tools/price-check/` and `/tools/deal-score/` are both pure iframe embeds with no separate WordPress content, so there was no real "post-result, pre-tool" position to put a CTA in as WordPress copy. ChatGPT's two new candidates are genuine long-form articles, not iframes — this resolves the blocker without needing to touch widget code.

## Inspected both candidates directly via WordPress REST API

**`/true-cost-of-ownership-explained/` (post id 513) — recommended as the first test page.**

- Real article, ~9-minute read, six-section structure (Financing, Insurance, Fuel, Maintenance, Registration, **Depreciation**), a worked 5-year TCO example, and a "New vs. Used TCO Trap" comparison section.
- **No existing Edmunds/CJ link anywhere on the page** — clean slate, zero risk of duplicating or crowding an existing CTA.
- Has one existing CTA already, at the very end of the article: a button linking to "@CarClever on ChatGPT" (not Edmunds, not this experiment — leave untouched).
- **Recommended placement:** immediately after the "Depreciation" subsection (the h3 that ends "...you might own a car worth only $8,000–10,000. Example: A $20,000 car depreciating to $10,000 over 5 years = $200/month in lost value."). This is the single most contextually exact spot on the whole site for a trade-in CTA — the article is actively telling the reader their current car is losing value, right before the CTA offering to find out what it's actually worth.
- This keeps the existing end-of-article ChatGPT CTA completely separate and untouched, avoiding the "two competing CTAs in one block" risk the handoff explicitly warned against.

**`/cross-shopping-new-vs-used-when-new-actually-costs-less/` (post id 993) — second candidate, more caveats.**

- Also a real article. **Directly names Edmunds already**, unlinked, in its own text: "Step 5: Calculate Residual Value — What will the car be worth in 5 years? Use resources like KBB or Edmunds." This is an organic, pre-existing mention that could simply become a live link rather than a new inserted block — arguably even lower-friction than adding new copy.
- However, this page already ends with an existing CTA to CarClever Lite ("Calculate Your Total Cost"), so adding a second commercial CTA here risks the same "multiple competing links" issue — would need to either replace the existing internal-tool CTA's context or place the Edmunds mention carefully mid-article instead of near the existing end CTA.
- Recommend holding this one as the second-wave test, after the TCO page has real data, rather than launching both simultaneously (matches the priority log's own "one controlled experiment" instruction).

## Proposed copy for the first test (TCO page, Depreciation section)

> Wondering what your own car is worth before you factor in its depreciation? Get a free estimate from Edmunds.
> **See what your car is worth on Edmunds**

(Adapted from the handoff's original copy to fit the specific context — the original generic version remains available if preferred.)

## Deal Score sparse-rendering check (from ChatGPT's addendum)

Confirmed live: `/tools/deal-score/` renders correctly, it's just the same pure-iframe architecture as `/tools/price-check/` (empty chat prompt, no content until a query is typed) — not a rendering bug, consistent with my earlier finding. No separate action needed here.

## What I still have not done (respecting the "do not publish" gate)

- Have not added the CTA to either page.
- Have not touched the widget/application code option I raised in my first return.

**Recommend: if André approves, use the TCO page (513) + Depreciation-section placement as the first live test**, since it fully resolves the architecture blocker, needs no code changes (pure WordPress copy edit), and has no existing CTA to conflict with. Ready to implement on approval.
