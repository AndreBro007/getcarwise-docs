# GetCarWise Website SEO/GEO Visibility Priority Research — 2026-09-15

**Status:** Research baseline + proposed priority order. No app-release decision and no WordPress publishing approval is implied by this document.
**Lane:** ChatGPT Business/Strategy
**Scope:** getcarwise.app organic search visibility, generative-AI visibility, content depth, structured data, internal duplication, backlinks, and manual-vs-Claude follow-up.

## Executive conclusion

The website is not primarily constrained by speed or a broad technical SEO failure. The highest-leverage work is now:

1. Push the `/tools/best-compact-suv-under-30000/` page from near page one into the top 10 by increasing *unique evidence and authority*, not by adding generic keyword-stuffed copy.
2. Audit and resolve overlapping guide intent, especially the duplicate-looking $25K compact-SUV and 3-row-SUV entries exposed on the Data & Guides hub.
3. Build real authority/backlinks using proprietary or differentiated GetCarWise data rather than generic cold outreach alone.
4. Use Google's new Generative AI Search Console reporting to measure GEO directly.
5. Correct/avoid misleading structured-data recommendations from automated tools before adding schema.

## Evidence reviewed

### Claude / Semrush handoffs supplied Sep 15

- Semrush On-Page SEO Checker: 40 ideas across 6 pages. Claude already shipped title/H1 changes on 4 pages; remaining bucket is mainly content depth/readability, schema suggestions, one manual meta description, and outreach.
- Weekly Engineering Report: no manual action or security penalty; sitemap healthy; Complianz crawl-noise fix shipped; toxic-domain disavow submitted; Semrush Position Tracking corrected from UAE/Arabic to US/English; Google Links report shows almost no real external authority; Semrush keyword portfolio mostly outside top 10.

### Fresh Ubersuggest check (US/English)

Ubersuggest was used because the Semrush API unit balance is exhausted.

- Domain Authority: 9.
- Estimated organic keywords: 35; estimated organic traffic: 2.
- `best suv under 30000`: estimated position **13**, volume **880/month**, landing page `/tools/best-compact-suv-under-30000/`.
- $25K compact-SUV cluster: multiple meaningful terms around positions ~36-47, including `best suv under 25k` (390 volume, position 40) and `best suv under 25000` (320 volume, position 43).
- PHEV page: larger potential demand but materially weaker rankings; examples include `best phev vehicles` (1,900 volume, position 53) and `list of phevs` (1,300 volume, position 73).
- `3rd row suv under 50k`: volume 30, estimated position 28.
- PageSpeed lab data is healthy enough that performance work is not the first priority: desktop LCP ~1.2s / CLS 0; mobile LCP ~2.8s / CLS 0.

Ubersuggest's daily report allowance was then exhausted; do not interpret the inability to run further reports as absence of issues.

## Priority 1 — $30K SUV page: near-page-one opportunity

**URL:** `/tools/best-compact-suv-under-30000/`

This is the clearest immediate organic opportunity because fresh third-party data places the main term around #13, and the page already has substantial useful content (new/used/hybrid comparison, ranked models, comparison table, buying steps and FAQ).

### Do not solve this by simply making it longer

The page already has significant word count. The more defensible gap versus leading competitors is *evidence differentiation*:

- Add a visible **How we ranked these SUVs** methodology block.
- Add/update **author or reviewer attribution** and a visible **last reviewed/updated** date where appropriate.
- Cite sources for price ranges, MPG, reliability and model facts; prefer primary/authoritative sources where practical.
- Add a small **2026 market snapshot** using GetCarWise/CarClever inventory evidence if Claude can produce a reproducible dataset (e.g. sample count, median asking price/mileage by model, date collected). This would create genuinely original content and a linkable data asset.
- Strengthen descriptive internal links from the Data & Guides hub and closely related pages.
- Request/confirm recrawl after the Sep 15 title/H1 change rather than assuming search snippets update immediately.

## Priority 2 — audit overlapping / duplicate-intent guides

The live Data & Guides hub exposes pairs that appear to target nearly the same intent:

- `Best Compact SUV Under $25K — CR-V vs RAV4 vs Tucson vs CX-5 vs Escape`
- `Best Compact SUV Under $25K — Ranked by value`

and:

- `Best 3-Row SUV Under $50K — Highlander and alternatives`
- `Best 3-Row SUV for Families — Highlander and alternatives`

This is not yet proof of harmful cannibalization, but it is enough to require an intent/canonical/internal-link audit before expanding either topic. Google's 2026 generative-AI guidance also recommends reducing duplicate content rather than producing separate pages for every query variation.

**Next check:** resolve each hub link to its exact URL, compare target queries, canonical tags, Search Console impressions/queries and content overlap. Then choose one of: clearly differentiate intent, merge/consolidate, or preserve both with stronger cross-link/canonical logic.

## Priority 3 — $25K SUV cluster

The $25K page has a real query cluster but is not close enough to page one for metadata-only work to be sufficient. After the duplication audit:

- strengthen methodology and current market evidence;
- make new-vs-used intent explicit if Google is surfacing both;
- improve internal links from the #13 $30K page and hub;
- refresh facts/prices only where sourceable;
- avoid creating more near-duplicate $25K variants.

## Priority 4 — PHEV page

The PHEV topic has large potential query volume but weaker rankings. It likely needs a more differentiated guide rather than a minor semantic-word pass.

Potential useful sections, subject to evidence checks:

- real electric-only range by model/model year;
- used price bands and mileage bands;
- charging practicality;
- battery and hybrid-system warranty differences;
- model-year-specific watch-outs;
- reliability / recall context;
- a clear ranking methodology and source list;
- current incentive/tax-credit discussion only if verified against current official rules before publishing.

## Priority 5 — $50K 3-row page

This page is already substantive. The immediate manual item is the Rank Math meta description identified by Claude/Semrush, followed by URL Inspection / recrawl. Light semantic/readability improvement is reasonable; a wholesale rewrite is not currently justified by the evidence.

## Structured-data decisions

Do **not** blindly implement the four Semrush schema suggestions.

### Reject: AutoDealer schema on Deal Score

`AutoDealer` represents a car dealership / local automotive business. GetCarWise's Deal Score tool is not a dealership. Adding this markup would misrepresent the page/site.

### Reject: WebSite schema on the Honda Accord profile

Google's site-name guidance places `WebSite` structured data on the home page. It should not be added to an individual Honda Accord profile simply because an SEO checker suggested it. First inspect existing homepage/Rank Math output to avoid duplicate site-level markup.

### Deprioritize: ItemList schema as a presumed SUV rich-result win

Schema.org `ItemList` can describe a list semantically, but Google's supported rich-result/carousel types are much narrower. There is no evidence that adding ItemList to these editorial SUV rankings will produce the rich-result payoff Semrush implies. Treat this as optional semantics, not a priority visibility lever.

### First schema task

Before adding new schema, isolate and fix the **one existing invalid structured-data item** reported by the cached Semrush Site Audit. The URL was not retrievable because Semrush's report/API was exhausted/unresponsive.

## GEO / Google generative-AI visibility

Google's current documentation says there is no separate GEO/AEO technical recipe or special AI schema required. Normal search eligibility and people-first, original content remain the foundation.

A newly available Search Console **Generative AI performance report** measures impressions from AI Overviews and AI Mode, with page/country/device/date dimensions. It rolled out worldwide by Aug 31, 2026.

### Manual check for André

In Search Console:

1. Open the `getcarwise.app` property.
2. Open the **Generative AI performance** report for Search.
3. Set a meaningful recent date range and open **Pages**.
4. Export the data if present.
5. Also check **Settings → Search generative AI** and confirm the site is included (inclusion is the default, but verify rather than assume).

This should become the primary direct GEO baseline instead of inferring AI visibility only from generic organic rankings.

## Trust / factual-consistency issue to resolve

A live-site wording inconsistency was found:

- The public Tools page says CarClever cross-references official databases including **state title records**.
- The current CarClever User Guide says title status comes from **dealer-provided listing data** and that CarClever does **not independently verify title status**.

Separately, current project investigation records that `title_status`/`titleStatus` is not present in Auto.dev `/listings` responses used in the old CarClever investigation.

This should be treated as a **copy/provenance audit item**, not silently corrected by assumption. Claude/product owner should confirm the exact live data source for each public CarClever surface, then website copy should be reconciled to the truthful narrow claim. Consistent provenance is especially important for trust and AI citation quality.

## Backlink / authority strategy

The authority gap is real; raw referring-domain counts are polluted by spam. Google Search Console's own Links report is the better baseline and currently shows very little genuine external authority.

Semrush's suggested outreach domains are leads, not an outreach strategy. Cold pitching Forbes/Good Housekeeping without a newsworthy data asset is low-probability.

Higher-leverage plan:

1. Produce one proprietary, reproducible GetCarWise data asset around a topic already showing demand — ideally the $30K SUV market.
2. Turn it into a concise public research block/page with methodology and collection date.
3. Pitch realistic automotive/editorial/forum/dealer audiences with a specific finding, not a generic link request.
4. Track earned links by quality and referral traffic, not raw domain count.

Candidate asset: **2026 SUVs Under $30K Market Snapshot** — current listing counts, median asking price, median mileage, used-vs-new split and hybrid availability for the top models, produced from a documented CarClever/Auto.dev sample.

## Division of work

### ChatGPT Business/Strategy

- Research and prioritize content opportunities.
- Draft/rewrite the $30K, $25K and PHEV content improvements.
- Design the methodology/data-asset presentation and outreach angle.
- Audit claims and source quality.
- Draft outreach targets/messages after the data asset exists.

### André manual UI

- Search Console Generative AI report + Search generative AI inclusion control.
- Rank Math meta description for the 3-row-$50K page.
- Rank Math/schema inspection needed to identify existing markup and the invalid item; do not add AutoDealer/WebSite-on-Accord based on the Semrush recommendation.
- URL Inspection/request indexing for pages just changed by Claude where appropriate.

### Claude Engineering / authenticated WordPress work

- Resolve exact URLs/canonicals/content overlap for the duplicate-looking hub entries if authenticated inspection is needed.
- Isolate the invalid structured-data URL when Semrush or site-audit tooling is available.
- Implement approved WordPress content/meta/internal-link changes that require authenticated access.
- If approved, produce the reproducible CarClever/Auto.dev market dataset for the proprietary $30K SUV data asset; ChatGPT should define the business/editorial spec, Claude handles any code/data extraction implementation.
- Confirm the actual title-history data provenance on each CarClever surface before website copy is changed.

## Proposed order of operations

1. André: check/export GSC Generative AI report and inclusion control.
2. ChatGPT + André: inspect exact duplicate-intent pages/hub links; decide consolidate vs differentiate.
3. ChatGPT: prepare the high-value content/evidence upgrade for the #13 $30K page.
4. Claude: implement approved WordPress changes and, if approved, generate the reproducible market-data snapshot.
5. André: fix the $50K 3-row meta in Rank Math and request recrawl as needed.
6. Then move to $25K and PHEV content depth.
7. Build outreach around proprietary data; do not chase raw backlink counts.

## Current limitations of today's tool pass

- Semrush API balance is exhausted, matching Claude's report; no fresh URL-level Semrush issue list could be pulled.
- Ubersuggest supplied useful domain/keyword/PageSpeed data, then hit its account's daily report limit. Fresh Ubersuggest site-audit/backlink-detail reports should be retried on a later day if useful.
- Search-result caches for some pages still show pre-Sep-15 titles, so indexing/recrawl status must be verified in Search Console rather than inferred from cached snippets alone.
