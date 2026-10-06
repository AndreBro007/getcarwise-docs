# SEO/GEO Implementation Log — Part 10 (Oct 6–7, 2026)

**Continues** `IMPLEMENTATION_LOG_SEO_GEO_20261006_PART9.md`. Owner lane: Claude — Engineering. André approved the three upgrades ("3.11 approve yes"). Source drafts (ChatGPT): `DRAFT_UPGRADE_USED_CAR_LISTING_RED_FLAGS_20261006.md`, `DRAFT_UPGRADE_GOOD_DEAL_PRICE_DEAL_SCORE_20261006.md`, `DRAFT_UPGRADE_USED_CAR_TOTAL_COST_OWNERSHIP_20261006.md`.

## Method (all three posts)
Edited the stored post HTML through the DOM: text-only wording changes (proved the tag structure was identical before/after), then added a new sourced section as additive blocks (no existing section restructured), removed the integration notes, added the standard affiliate disclosure before the first Edmunds link, Edmunds links `rel="nofollow sponsored noopener" target="_blank"` with page tags, one blue button per post. URLs, titles and H1s unchanged; WordPress revisions hold the previous versions (rollback: Posts > revisions). Each save verified (stored content equals intended; live page checked for valid JSON-LD, links, disclosure, byline).

## Post 309 — How to Read a Used Car Listing: 5 Red Flags (most-cited page, 173 Bing citations)
- 19 text edits: removed invented statistics (80% of problem cars, "70% of the time", 15–20% / 30%+ below-market thresholds in text and table, $4,000 repair, resale drops 30%, repair and maintenance dollar ranges, $5,000–8,000 total, inspection price); relabelled the 2019 CR-V stories as "illustrative example (hypothetical figures)" with a note under the renamed heading "An Illustrative Scenario"; hidden BlogPosting markup corrected (headline no longer says "Cost Buyers $5,000+").
- New section "Verify Before You Travel or Pay": four sourced Q&As (price vs nearby cars, title and recall checks, history report vs inspection, deposit), FTC video link correctly titled "Buying a Used Car - Consumer Tips video and transcript", VIN Check link, FAQPage JSON-LD (4 questions), sponsored Edmunds text link `red-flags-post_compare` and button `red-flags-post_cta`.
- Verified: 1 embed and 8 tables unchanged; all JSON-LD valid (5 blocks); no invented statistics on the live page.

## Post 412 — The CarClever Deal Score Explained
- Top note: bands, weights, vehicles and prices are simplified illustrative examples, not live market data; the live tool is the authority. Wording fixes: "These sell in 3-5 days" replaced; example "13% underpriced" corrected to about 12% (12,800 vs 14,500 = 11.7%).
- Removed the hidden Dataset JSON-LD "Mid-Size SUV Deal Score Rankings" (unverifiable ranking and price data). No FAQ schema existed, so none added.
- New section "Reading a Good Deal Label From Any Used-Car Site": four sourced Q&As (TrueCar and CarGurus described as company methods, why sites differ, what to match before comparing, strong rating is not a good car), link to the AI-tools guide instead of repeating its comparison, sponsored link `deal-score-post_compare` and button `deal-score-post_cta`.
- Verified: 2 embeds and 1 table unchanged; JSON-LD valid.
- **Open flag:** the post's score bands (RED 0–40, YELLOW 41–70, GREEN 71–100) and weights (20/20/25/20/15) were not verified against the live tool. The Lite app's fallback verdict labels in code (`components/ResultCard.tsx`) use 75+ "Strong Value", 60–74 "Fair Deal", below 60 "Overpriced" (the backend may supply its own verdict). The post now says bands are illustrative; André/ChatGPT should confirm the real bands from the tool before the post states them as fact.

## Post 513 — True Cost of Ownership Explained
- Top note: all dollar figures, percentages and vehicles in the examples are hypothetical, not averages, quotes or predictions. Softened three headline generalizations ("payment is only 40–50% of true cost"; "used cars at 7% APR can cost more over 5 years than new cars at 0% APR"; the "$783/month" example labelled illustrative).
- **Two arithmetic errors fixed (computed with standard amortization on $20,000 over 60 months):** "7% vs 3% APR is $5,000+ more in interest" corrected to roughly $2,200 (interest about $3,761 vs $1,562); "a 1% APR reduction saves thousands over 5 years" corrected to roughly $550 (7% to 6%: $3,761 to $3,199).
- New section "Estimating Your Own True Cost: Sources and Methods": five sourced Q&As (CFPB, FuelEconomy.gov, NAIC, FTC), sponsored trade-in link `tco-post_tradein` in the depreciation answer (Sell Your Car asset 3949601), used-listings link `tco-post_compare`, trade-in button `tco-post_cta`, link to the AI-tools guide and the worked-example page. The post's two older Edmunds links (migrated earlier) have no Shared ID yet.
- **Not audited:** the other worked-example figures (the six-component walkthrough and the new-vs-used comparison table) were not re-computed line by line; they are labelled illustrative. Recommend a full arithmetic check if the post keeps presenting them.

## Still open
Sitemap still stale (new AI-tools post missing; re-check Oct 7); confirm Deal Score bands; optional arithmetic audit of post 513 tables; add Shared IDs to the two older Edmunds links in post 513.
