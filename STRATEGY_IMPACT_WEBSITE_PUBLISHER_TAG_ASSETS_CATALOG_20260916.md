# GetCarWise Impact/Edmunds Website Monetisation Strategy — Publisher Tag, Assets & Product Catalog

**Date:** 2026-09-16  
**Corrected:** 2026-09-17 after direct Impact support confirmation on Catalog API VIN limitations  
**Owner lane:** ChatGPT — Business/Strategy  
**Status:** **Proposed — pending André approval before website implementation**

## Purpose

Translate the confirmed CJ → Impact.com Edmunds capabilities into a safe, measurable website monetisation design that supports the existing Discovery → Evaluation → Edmunds Lead funnel without compromising SEO/GEO, editorial trust, or active MCP review gates.

Companion records:

- `HANDOFF_EDMUNDS_CJ_TO_IMPACT_MIGRATION_20260916.md`
- `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md`
- `STRATEGY_DISCOVERY_MCP_EDMUNDS_REVENUE_FUNNEL_20260916.md`
- `HANDOFF_WEBSITE_SEO_CTA_OPPORTUNITY_PASS_20260904.md`

## Important correction — Sep 17

An earlier version of this strategy incorrectly treated the Edmunds Product Catalog API as a VIN-search / exact-listing lookup service. That is now **disproven**.

Claude's testing and Impact support ticket **#882346** confirm:

- the Product Catalog API **cannot search or filter by VIN/MPN**;
- exact VIN deep-linking through Impact **does work** when an Edmunds destination URL is already known;
- the app-side CJ → Impact replacement therefore does **not** need the Catalog API for link generation;
- the Catalog API remains potentially useful on the website for **general filtered inventory discovery**, not specific-VIN verification.

The website strategy below has been corrected accordingly. Do not use any older design that says `VIN → Catalog lookup → tracked URL`.

## Executive recommendation

Use the Impact capabilities for different jobs:

1. **Publisher Tag — general editorial/site Edmunds links.** Use a controlled basic-integration pilot to transform clean direct Edmunds URLs into Impact tracking links and add page/link impression measurement. Do **not** enable `identifyUser` initially.
2. **Static Impact deep-linking — exact known Edmunds destinations.** If GetCarWise already knows the precise Edmunds destination URL, including a VIN-specific page, wrap that destination using the confirmed Impact deep-link mechanism. Do not query the Product Catalog by VIN.
3. **Product Catalog API — general current-inventory discovery.** Evaluate it for filtered inventory modules/searches by confirmed searchable dimensions such as model, body-style/category and dealer name, with ready-to-use tracked result links.
4. **Ready-made Assets — broad/fallback CTAs and controlled creative tests.** Use the three text-link assets where they match intent; treat the nine banners as optional experiments, not the default website strategy.

The preferred website hierarchy is:

> **Exact known Edmunds destination when available > relevant filtered catalog inventory > contextual category text CTA > generic banner.**

This preserves the core commercial principle: the website should move an already-qualified shopper toward one of three genuine Edmunds outcomes — used lead, new lead, or trade-in lead — rather than maximize raw affiliate-link exposure.

---

# 1. Publisher Tag — recommendation

## What current Impact documentation confirms

Impact's Publisher Tag is a JavaScript snippet for partner websites. Its basic integration can:

- detect direct links to brands with which the partner is joined;
- transform those direct URLs into Impact tracking links while preserving the specific landing page;
- track impressions for transformed links when supported by the brand/account.

Impact also offers an optional `identifyUser` integration that collects additional user/traffic information for identity/path matching.

Sources:

- https://help.impact.com/partner/platform-features/tracking/tracking-links/create-and-manage-links/publisher-tag-implementation-for-partners
- https://help.impact.com/brand/what-would-you-like-to-learn-about/platform-features/tracking/tracking-explained/publisher-tag-faq

## Critical migration finding

Impact states that Publisher Tag **does not override existing affiliate-tracked links**. It transforms direct brand links that do not already contain affiliate tracking.

Therefore:

> **Installing Publisher Tag does not automatically migrate the existing GetCarWise CJ URLs.**

Existing CJ links still need to be inventoried and replaced. A sensible post-migration editorial workflow is then to store the clean Edmunds destination URL in WordPress and allow Publisher Tag to transform it at runtime.

This is preferable to continuing manual network-specific wrappers for every editorial link because the underlying destination remains readable and network-independent.

## Why it fits GetCarWise

The current website already has contextual Edmunds CTAs on several high-intent pages, including the $30k SUV, used PHEV, 3-row SUV under $50k, compact SUV under $25k, midsize sedan under $40k, and TCO/trade-in work.

Publisher Tag could simplify the website layer while producing better page-level measurement.

Impact's Publisher Tag reporting can capture page/link impressions and referring-page context. Impact's `Overview by Story` / Performance by Story capability can use Publisher Tag page-level attribution to compare content by URL, clicks, conversion rate, commission and related metrics. Impact currently describes this as available through Trackonomics Essentials; account entitlement should be verified rather than assumed from generic help documentation.

Source:

- https://help.impact.com/partner/platform-features/trackonomics/trackonomics-reports/overview-by-story-report

## Recommended rollout: PILOT, not site-wide day one

### Pilot scope

Start on the existing commercial CTA pages only:

1. `/tools/best-compact-suv-under-30000/`
2. `/tools/best-used-phev-plug-in-hybrid/`
3. `/tools/best-3-row-suv-under-50000/`
4. `/tools/best-compact-suv-under-25000/`
5. `/tools/best-midsize-sedan-under-40000/`
6. `/true-cost-of-ownership-explained/` (trade-in path)

Do not add it to the homepage, `/tools/` GEO hub, About/Methodology, or every page merely to increase affiliate exposure during the pilot.

### Integration level

Use the **basic Publisher Tag only** initially:

- transform links;
- impression tracking where available.

Do **not** enable `identifyUser` in phase 1.

Impact documents `identifyUser` as capable of collecting hashed user email/ID plus UUID, session/cookie/device identifiers and hashed IP/geolocation. GetCarWise does not need that additional complexity merely to migrate CJ links and measure page-level affiliate performance.

### Privacy / consent

Even with the basic integration, Publisher Tag transmits page/link and session/UUID information. Impact states its Publisher Tag is designed for privacy/GDPR compliance, but GetCarWise remains responsible for its own cookie/consent/privacy implementation.

Before production use:

- run a Complianz cookie/script scan;
- classify the Impact script appropriately;
- confirm whether the script should load before or after the applicable consent category;
- update the privacy/cookie disclosures if required;
- do not enable advanced identity tracking without a separate decision.

This is operational/privacy review, not legal advice.

### SEO safeguard

Google recommends `rel="sponsored"` for paid/affiliate links.

Source:

- https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links

Acceptance test must confirm Publisher Tag changes the destination `href` without removing the existing `rel="sponsored"` attribute or nearby affiliate disclosure.

### Failure-mode advantage

If Publisher Tag is blocked or fails, a clean direct Edmunds URL can still send the user to the intended Edmunds page; the likely loss is attribution rather than navigation. This graceful degradation is strategically preferable to making the user journey depend on network-specific JavaScript for basic destination correctness.

This should be verified in the actual GetCarWise implementation rather than assumed.

### Performance safeguard

The tag adds third-party JavaScript. It should be tested for:

- LCP/INP/TBT impact;
- duplicate requests;
- impact on CarClever Lite embeds;
- ad/script blocker behavior;
- no console errors;
- no duplicate link transformation.

The site currently has acceptable performance and SEO performance work should not be sacrificed for affiliate convenience.

---

# 2. Existing CJ → Impact website migration model

The current editorial CTAs were deliberately implemented as contextual one-CTA blocks with a nearby affiliate disclosure. Preserve that UX pattern.

The migration should change the tracking layer, not turn those pages into ad pages.

## Proposed website migration pattern

For ordinary editorial/category CTAs:

> Existing CJ tracking URL → clean exact Edmunds destination URL → Publisher Tag transforms to Impact URL

For an exact Edmunds vehicle/VIN destination that is already known:

> Known Edmunds destination URL → confirmed static Impact deep-link wrapper → exact Edmunds page

For general current-inventory discovery:

> Website intent/model/body style/dealer filter → Product Catalog API general search → matching catalog results with ready-to-use tracked links

For a broad asset fallback:

> Impact asset tracking link with approved page/placement reporting parameters

## Important reporting point

Impact supports Sub IDs / Shared IDs and recommends configuring reporting parameters through its supported link-generation mechanisms rather than arbitrarily editing tracking URLs.

Source:

- https://help.impact.com/partner/platform-features/tracking/tracking-links/create-and-manage-links/add-reporting-information-to-your-tracking-links

Publisher Tag page-level attribution may reduce the need to encode page IDs in every basic editorial link. For catalog and asset links, Claude should verify the cleanest reporting mechanism without stripping or corrupting existing tracking parameters.

Do not put PII in affiliate reporting parameters.

---

# 3. The 12 ready-made Edmunds Assets

Confirmed program inventory from Claude research:

- 3 text-link assets: **Sell Your Car**, **New Car Listings**, **Used Car Listings**;
- 9 banner assets across 300×250, 320×50 and 728×90 for the three lead families.

## Recommendation: text links are useful; banners are experiments

### `Used Car Listings`

Good fallback for pages where the reader has chosen a used-car direction but no more specific destination is available.

Candidate contexts:

- used PHEV;
- compact SUV under $25k;
- used EV;
- hybrid SUV under $20k;
- other used-only model/budget guides.

Prefer a more specific deep destination or filtered catalog module whenever it genuinely improves the user's next step.

### `New Car Listings`

Candidate contexts:

- new-car or new-vs-used comparison pages;
- future current-model/incentive guides;
- `$30k SUV` only when the content genuinely concludes that a new-car path is appropriate for the user.

Do not place a generic New Cars CTA on used-only pages just because the lead payout is the same.

### `Sell Your Car`

Strongest natural fit:

- `/true-cost-of-ownership-explained/` depreciation/replacement context;
- future valuation / sell / trade-in content;
- replacement journeys where the user clearly has an existing vehicle.

Because trade-in payout is lower, placement should still be driven by user intent rather than payout amount.

## Banner policy

Do not deploy the nine banners site-wide.

Initial banner rules:

- never on homepage as generic monetisation clutter;
- never inside ChatGPT/Claude MCP apps;
- do not introduce banners into `/tools/` while it is one of the strongest GEO pages;
- do not modify the 3-row/$30k controlled SEO/GEO treatments with banners before the content experiment baseline is established;
- test only one banner treatment at a time against an existing contextual text CTA.

Best first banner experiment if desired: a lower-risk, high-intent trade-in or used-shopping page after Impact tracking is verified, with the banner placed after the useful decision content, not above it.

Primary KPI is **valid lead yield / commission per qualified visitor**, not banner CTR.

---

# 4. Product Catalog — useful complementary website inventory source, with hard limitations

The current verified position is:

- approximately **1.334 million** Edmunds catalog listings;
- catalog updates at least daily based on observed account data;
- **VIN/MPN cannot be searched or filtered** — confirmed both by live testing and Impact support ticket #882346;
- confirmed general search/filtering includes:
  - **dealer name** via the API field labelled `Manufacturer` (despite that field actually holding the dealer name in observed records);
  - **model** via `Text1`;
  - **body style/category** via `Category`;
- matching results include working pre-tracked affiliate links plus current price/stock, photo, dealer information/address, and year/model/trim;
- narrow catalog searches are the intended use; the API cannot page beyond 20,000 results per catalog;
- current endpoint rate limit is 3,600 requests/hour;
- Edmunds coverage is materially smaller than Auto.dev's several-million-listing inventory, so the catalog should be treated as a **complementary subset**, not a replacement merely because it is affiliate-native.

This means the Product Catalog's role is **general current-inventory discovery**, not exact-listing verification against a CarClever VIN.

## Stage 1 — website utility/data-quality audit

Do **not** repeat the disproven VIN lookup work.

Instead evaluate the catalog around the website use cases it can actually support:

- model searches — e.g. current CR-V, RAV4, CX-5, Outlander PHEV inventory;
- body-style/category searches — e.g. current SUV inventory;
- dealer-name searches where useful;
- result quality and relevance;
- new vs used mix and whether condition can be reliably distinguished in returned data;
- geography/location usefulness from returned dealer/address fields;
- live price/stock consistency and update cadence;
- latency and request volume for narrow, real website queries;
- comparison at the **model/category/market-sample level** against Auto.dev, not VIN-for-VIN catalog lookup.

## Stage 2 — potential current-inventory modules, pending rights + product-design gate

The strongest website use is likely a small **filtered current-inventory module** attached to an existing high-value decision page, not millions of new pages.

Examples:

### SUV under $30k

After the independent recommendation section:

> **Current SUVs on Edmunds**  
> Show a small, relevant set from general model/category searches, filtered down using catalog fields the API actually supports.

### Used PHEV

> **Current PHEV inventory on Edmunds**  
> Use confirmed model searches for the PHEV models recommended by the article, then surface a small number of current examples with tracked links.

### Model-specific future guide

> **Current Honda CR-V listings**  
> Model search can supply relevant live Edmunds inventory without pretending it is an exact VIN cross-check against CarClever.

The module should remain subordinate to independent editorial analysis. It should never imply that the Edmunds catalog is the complete U.S. market.

## Stage 3 — proprietary market evidence, only if derivative/publication rights are clear

If the agreement/data-feed terms clearly permit aggregation/publication, catalog data could potentially contribute to:

- listing counts within specific catalog-supported filters;
- price distributions;
- stock/availability trends;
- model-year availability;
- dealer/geographic availability;
- monthly market snapshots.

This could strengthen SEO/GEO and backlink/PR assets.

However, any public statistic must be described accurately as an **Edmunds catalog subset** unless the methodology combines it with broader validated sources. It must not be presented as the full U.S. market simply because the catalog has 1.3M listings.

Do **not** assume public aggregation rights from API access alone. Complete a focused rights/usage review before using catalog-derived statistics in public SEO/GEO content.

## Explicit anti-patterns

Do not:

- attempt VIN lookup via the Catalog API again;
- build website logic that depends on matching a CarClever/Auto.dev VIN to the Edmunds catalog;
- mass-publish one affiliate page per Edmunds listing;
- mechanically republish feed descriptions;
- describe the Edmunds catalog as complete national inventory;
- treat catalog coverage as a replacement for Auto.dev without comparative evidence.

Google's spam guidance calls out thin affiliation where merchant/feed content is republished without original value; high-quality affiliate pages need original analysis, comparison, research or other meaningful additional value.

Sources:

- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content

The GetCarWise advantage should remain independent analysis + current evidence + decision support, with affiliate inventory as the action layer.

---

# 5. How this changes the Discovery → MCP → Edmunds funnel

The existing strategy remains valid but the **Action** layer is now correctly split between exact deep-linking and catalog discovery.

## Discovery

SEO, Google Generative AI, ChatGPT/Claude app awareness, Reddit, referrals, direct/brand.

## Evaluation

Evidence-rich GetCarWise pages, tools and CarClever.

## Intent classification

- Used;
- New;
- Trade-in.

## Action hierarchy

1. **Exact known Edmunds destination** — static Impact deep-link wrapper or Publisher Tag, depending on the surface/use case. This can include a VIN-specific Edmunds page only when that destination URL is already known from another source; the Catalog API does not discover it by VIN.
2. **General live-inventory module** — Product Catalog search by supported general dimensions such as model/body style/dealer, returning tracked Edmunds result links.
3. **Model/category deep destination** — clean Edmunds deep URL + Publisher Tag where suitable.
4. **Broad lead-family destination** — relevant Impact text asset.
5. **Banner** — experiment only.

## Measurement

Add the following fields to the master SEO/GEO/Revenue matrix:

- primary lead path: Used / New / Trade-in;
- CTA type: exact deep link / catalog inventory / deep category / text asset / banner;
- affiliate mechanism: Static Impact Deep Link / Publisher Tag / Catalog / Asset;
- CTA exposure;
- clicks;
- actions/leads;
- commission;
- revenue per visitor;
- revenue per CTA click;
- conversion lag where available.

This turns Impact into the economic measurement layer beneath SEO/GEO rather than a separate affiliate project.

---

# 6. Recommended September migration sequence

## Phase A — research/test in parallel with old-app migration

1. Replace the obsolete VIN-oriented Catalog audit with a **Catalog Website Utility Audit**: model/category/dealer search quality, condition/new-used usefulness, geography, price/stock freshness, latency, coverage versus Auto.dev at aggregate/model level, and public/derived-data rights.
2. Claude tests Publisher Tag basic integration in a non-production or controlled website context.
3. Verify direct Edmunds deep links, including a known VIN destination, transform/resolve correctly without using a Catalog lookup.
4. Verify existing CJ links are not transformed and document the required replacement process.
5. Verify `rel="sponsored"`, disclosure, consent, performance and script-blocker behavior.
6. Verify whether page/story reporting is available in the current Impact account / Trackonomics entitlement.

## Phase B — migrate existing website CTAs

For the six pilot pages:

1. inventory current CJ destination;
2. identify exact equivalent Edmunds destination;
3. replace CJ tracked link with either a clean Edmunds URL + Publisher Tag or an appropriate Impact link method;
4. preserve CTA copy unless the destination/intent changed;
5. preserve disclosure and `rel="sponsored"`;
6. click-test every destination;
7. verify Impact click appears;
8. re-fetch rendered page after every change.

## Phase C — separate catalog experiment

After the core CJ → Impact website migration works reliably:

1. select **one** high-intent page for a catalog-backed inventory experiment;
2. use only supported general filters;
3. show a small number of relevant current results;
4. clearly distinguish editorial recommendation from affiliate inventory;
5. measure module exposure → click → Edmunds action/commission;
6. compare against the existing simpler contextual CTA before scaling.

## Phase D — migration closeout

Before CJ website retirement:

- crawl/search WordPress for all remaining CJ network hostnames / legacy tracking patterns;
- replace or intentionally document every remaining occurrence;
- confirm Impact clicks and lead reporting are functioning;
- keep a rollback/reference inventory until the transition is proven;
- do not remove CJ solely because the Publisher Tag has been installed.

Target remains end of September 2026, with no need to wait for the old Fractal implementation if the website pilot is independently verified.

---

# 7. Decisions recommended now

### Recommend APPROVE

- Publisher Tag **basic-integration pilot** on the six existing commercial CTA pages.
- No `identifyUser` during migration.
- Preserve one-contextual-CTA-per-page philosophy.
- Use confirmed static Impact deep-linking for exact Edmunds destinations already known from another source; **never depend on Catalog VIN lookup**.
- Evaluate Product Catalog only for general model/body-style/dealer current-inventory use cases.
- Use text assets as broad/fallback CTAs when no better destination exists.
- Keep banners in experiment-only status.
- Complete catalog rights/data-quality review before using catalog data as public SEO/GEO evidence.

### Keep PENDING

- site-wide Publisher Tag rollout;
- advanced `identifyUser` integration;
- public catalog-derived market statistics;
- dynamic inventory modules on SEO pages;
- any large-scale banner rollout;
- any mass inventory/programmatic SEO pages.

---

# 8. Bottom line

The corrected Impact architecture is:

> **Publisher Tag for ordinary editorial links → static Impact deep-linking for exact known Edmunds destinations → Product Catalog for general filtered current-inventory discovery → text Assets for broad fallbacks → banners only as measured experiments.**

The Product Catalog remains strategically interesting, but its value is now much more precise: it can help GetCarWise surface **current Edmunds inventory by model/body style/dealer**, not verify whether a specific CarClever VIN exists on Edmunds.

That distinction matters because it keeps the website strategy honest, technically feasible, and separate from the app's exact-link logic.

The biggest near-term win remains operational and measurable: migrate current contextual CTAs cleanly, gain better affiliate performance visibility, and preserve editorial/SEO/GEO quality. The strongest longer-term catalog experiment is a **small, useful, current-inventory module on an existing high-intent page**, not VIN matching and not programmatic page generation.