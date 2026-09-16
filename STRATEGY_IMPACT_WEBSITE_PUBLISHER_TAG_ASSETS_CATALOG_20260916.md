# GetCarWise Impact/Edmunds Website Monetisation Strategy — Publisher Tag, Assets & Product Catalog

**Date:** 2026-09-16  
**Owner lane:** ChatGPT — Business/Strategy  
**Status:** **Proposed — pending André approval before website implementation**

## Purpose

Translate the confirmed CJ → Impact.com Edmunds capabilities into a safe, measurable website monetisation design that supports the existing Discovery → Evaluation → Edmunds Lead funnel without compromising SEO/GEO, editorial trust, or active MCP review gates.

Companion records:

- `HANDOFF_EDMUNDS_CJ_TO_IMPACT_MIGRATION_20260916.md`
- `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md`
- `STRATEGY_DISCOVERY_MCP_EDMUNDS_REVENUE_FUNNEL_20260916.md`
- `HANDOFF_WEBSITE_SEO_CTA_OPPORTUNITY_PASS_20260904.md`

## Executive recommendation

Use three different Impact mechanisms for three different jobs:

1. **Publisher Tag — general editorial/site Edmunds links.** Use a controlled basic-integration pilot to transform clean direct Edmunds URLs into Impact tracking links and add page/link impression measurement. Do **not** enable `identifyUser` initially.
2. **Product Catalog pre-tracked URL — exact VIN / current-inventory handoffs.** Where the catalog contains a specific VIN, use the catalog-provided pre-tracked URL rather than relying on Publisher Tag transformation.
3. **Ready-made Assets — fallback/category CTAs and controlled creative tests.** Use the three text-link assets where they match intent; treat the nine banners as optional experiments, not the default website strategy.

The preferred hierarchy is:

> **Exact relevant vehicle/deep destination > contextual category text CTA > generic banner.**

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

For exact inventory/VIN modules:

> Exact vehicle/VIN → Edmunds Product Catalog lookup → catalog-provided pre-tracked URL

For a generic asset fallback:

> Impact asset tracking link with approved page/placement reporting parameters

## Important reporting point

Impact supports Sub IDs / Shared IDs and recommends configuring reporting parameters through its supported link-generation mechanisms rather than arbitrarily editing tracking URLs.

Source:

- https://help.impact.com/partner/platform-features/tracking/tracking-links/create-and-manage-links/add-reporting-information-to-your-tracking-links

Publisher Tag page-level attribution may reduce the need to encode page IDs in every basic editorial link. For catalog and asset links, Claude should verify the cleanest reporting mechanism without stripping or corrupting existing catalog tracking parameters.

Do not put PII in affiliate reporting parameters.

---

# 3. The 12 ready-made Edmunds Assets

Confirmed program inventory from Claude research:

- 3 text-link assets: **Sell Your Car**, **New Car Listings**, **Used Car Listings**;
- 9 banner assets across 300×250, 320×50 and 728×90 for the three lead families.

## Recommendation: text links are useful; banners are experiments

### `Used Car Listings`

Good fallback for pages where the reader has chosen a used-car direction but no exact model/VIN destination is available.

Candidate contexts:

- used PHEV;
- compact SUV under $25k;
- used EV;
- hybrid SUV under $20k;
- other used-only model/budget guides.

Prefer a more specific deep destination or exact vehicle link whenever available.

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

# 4. Product Catalog — strongest long-term opportunity, but use in stages

Claude has confirmed:

- 1.3M+ Edmunds listing records;
- exact VIN-level records;
- current price / stock information;
- dealer information / photos;
- ready-to-use pre-tracked affiliate URLs.

Impact's general partner documentation confirms product catalogs are intentionally available to joined partners for product discovery/promotion and may be accessed via platform download, FTP or API. It also provides standardized catalog formats and product-level tracking links.

Sources:

- https://help.impact.com/partner/what-would-you-like-to-learn-about/platform-features/marketing-content/product-marketplace-and-catalogs/download-product-catalogs-as-a-partner
- https://help.impact.com/partner/platform-features/marketing-content/product-marketplace-and-catalogs/set-product-catalog-feed-preferences-as-a-partner
- https://help.impact.com/partner/what-would-you-like-to-learn-about/platform-features/tracking/tracking-links/create-and-manage-links/create-tracking-links

## Stage 1 — approved strategic use: routing / verification research

Use the catalog to investigate:

- VIN coverage overlap with Auto.dev/CarClever;
- current listing presence;
- price/dealer/stock agreement;
- exact Edmunds handoff URL;
- freshness/drift.

This does not require public republication of catalog data.

## Stage 2 — potential public inventory module, pending rights + data-quality gate

If terms and data quality permit, the most valuable website use is **not** millions of new SEO pages.

It is a small current-inventory module on an existing high-value decision page, e.g.:

> **Current examples matching this recommendation**  
> 3–5 currently available vehicles with price, model year, mileage/market context where permitted, location/dealer if appropriate, and exact tracked Edmunds destination.

Potential first candidates:

- $30k SUV;
- used PHEV;
- $25k SUV after canonical architecture is resolved;
- used EV.

The module should be subordinate to independent editorial analysis, not the main content.

## Stage 3 — proprietary market evidence, only if derivative/publication rights are clear

If the agreement/data-feed terms clearly permit aggregation/publication, catalog data could potentially contribute to:

- listing counts;
- price distributions;
- stock/availability trends;
- model-year availability;
- dealer/geographic availability;
- monthly market snapshots.

This could strengthen SEO/GEO and backlink/PR assets.

Do **not** make this assumption from API access alone. Complete the separate Product Catalog Strategic Eligibility Audit before public aggregation.

## Explicit anti-pattern

Do not mass-publish one affiliate page per Edmunds listing or mechanically republish feed descriptions.

Google's spam guidance calls out thin affiliation where merchant/feed content is republished without original value; high-quality affiliate pages need original analysis, comparison, research or other meaningful additional value.

Sources:

- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content

The GetCarWise advantage should remain independent analysis + current evidence + decision support, with affiliate inventory as the action layer.

---

# 5. How this changes the Discovery → MCP → Edmunds funnel

The existing strategy remains valid but the **Action** layer becomes more precise.

## Discovery

SEO, Google Generative AI, ChatGPT/Claude app awareness, Reddit, referrals, direct/brand.

## Evaluation

Evidence-rich GetCarWise pages, tools and CarClever.

## Intent classification

- Used;
- New;
- Trade-in.

## Action hierarchy

1. **Exact VIN/current listing** — catalog-provided pre-tracked URL.
2. **Model/category deep destination** — clean Edmunds deep URL + Publisher Tag where suitable.
3. **Broad lead-family destination** — relevant Impact text asset.
4. **Banner** — experiment only.

## Measurement

Add the following fields to the master SEO/GEO/Revenue matrix:

- primary lead path: Used / New / Trade-in;
- CTA type: VIN / deep category / text asset / banner;
- affiliate mechanism: Catalog / Publisher Tag / Asset;
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

1. Complete the Product Catalog Strategic Eligibility Audit already scoped: coverage, schema, freshness, Auto.dev overlap, public/derived-data rights.
2. Claude tests Publisher Tag basic integration in a non-production or controlled website context.
3. Verify direct Edmunds VIN/deep links transform correctly.
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

## Phase C — migration closeout

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
- Use catalog pre-tracked VIN URLs directly for exact inventory handoffs.
- Use text assets as broad/fallback CTAs when no better deep destination exists.
- Keep banners in experiment-only status.
- Complete catalog rights/coverage audit before using catalog data as public SEO/GEO evidence.

### Keep PENDING

- site-wide Publisher Tag rollout;
- advanced `identifyUser` integration;
- public catalog-derived market statistics;
- dynamic inventory modules on SEO pages;
- any large-scale banner rollout;
- any mass inventory/programmatic SEO pages.

---

# 8. Bottom line

Impact is more than a CJ replacement, but its components should not be treated as interchangeable.

The best GetCarWise architecture is:

> **Publisher Tag for ordinary editorial links → Product Catalog for exact inventory/VIN handoffs → text Assets for broad fallbacks → banners only as measured experiments.**

That architecture supports the larger strategy:

> **Discovery → trusted decision support → the most precise relevant action → one of the three Edmunds lead events.**

The biggest near-term win is operational and measurable: migrate current contextual CTAs cleanly, gain page-level affiliate performance visibility, and preserve editorial/SEO/GEO quality. The biggest longer-term opportunity is catalog-backed decision evidence and current inventory — but only after the separate rights and data-quality gates are answered.