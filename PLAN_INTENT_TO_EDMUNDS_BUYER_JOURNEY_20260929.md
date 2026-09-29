# GetCarWise intent-to-listing growth system — research and blueprint
Date: 2026-09-29
Status: Strategy and implementation brief. No campaign publication, production change, catalog promotion, or spend authorised by this document.

## Decision
Build a buyer decision and inventory handoff experience for US shoppers, starting with used SUVs under US$25,000. A Google query, organic article, or AI app invocation becomes an explicit, editable intent capsule (vehicle type, condition, budget, location, priorities). The product returns evidence-based choices, then routes to the exact Edmunds vehicle when a valid tracked link exists. An approved tracked Edmunds category destination remains a bypass/fallback. Optimize for approved partner actions, with useful result and outbound click as diagnostic stages.

Differentiation is a fast, honest "which actual car should I inspect and why?" decision, not a generic best-cars list, a clone of a marketplace, or an empty AI chat.

## Evidence and limits
- Cox Automotive's 2025 Car Buyer Journey summary: 77% of used buyers visited third-party automotive websites; 41% of vehicle buyers used search engines; used buyers visited 4.8 sites on average. This supports a decision-to-marketplace journey, not a GetCarWise conversion forecast. https://www.coxautoinc.com/wp-content/uploads/2026/03/2025-Cox-Automotive-Car-Buyer-Journey-Study-Summary.pdf
- Ubersuggest connected US/English estimates obtained Sep 29: "best used suv under 25000" 590 monthly, SEO difficulty 22, estimated CPC US$1.15; "best used compact suv under 25000" 50 monthly, SD25, CPC US$1.66; "used suv under 25000" seed 390 monthly, SD23, CPC US$1.58; "used suv near me" seed 18,100 monthly, SD23, CPC US$2.20. The provider marked paid competition/difficulty high. These are directional estimates, not Google Ads clearing prices. Further overview calls returned INVALID_ARGUMENT; no other volumes are asserted. Google Keyword Planner and Search Console should govern account decisions.
- Google ValueTrack {keyword} returns the matched account keyword, not the user's exact query. We know the ad group/creative intent and can pass an explicit intent ID; we cannot promise to capture the full search phrase. https://support.google.com/google-ads/answer/6305348
- Exact match still includes searches of same meaning/intent; inspect search terms after launch. https://support.google.com/google-ads/answer/7478529
- Current CarClever Lite V2 uses ?q= to show a prepared search button; it does not auto-run. It uses Find My Car MCP, parses narration into lean vehicle cards, and offers a full-listing link or separately labelled similar-listings fallback. It is a useful technical base, not the finished campaign page.
- Edmunds has a used-SUV-under-$25,000 category destination: https://www.edmunds.com/used-suv-under-25000/ . A tracked deep link to this exact page is a proposal only; generate/validate it through Impact and the active agreement.
- Internal Impact Catalog C1-C8 tests on Sep 21 found about 1.35m reported items, working category+price and exact-model filters, dealer mapping, partner-specific tracking URLs, a 20,000-item traversal window and observed 3,000 requests/hour. They also found no usable Condition (empty in sampled records), no VIN field, no proven ZIP/radius, and no item-level freshness in the sample. It cannot independently prove used, near me, currently in stock, or exact same vehicle as an Auto.dev card. See RETURN_IMPACT_CATALOG_C1_C8_READ_ONLY_TESTS_20260920.md and RETURN_IMPACT_CATALOG_PRIVATE_PROTOTYPE_20260921.md.
- Current recorded Impact agreement says US$10 per approved Used/New lead, US$3.50 per approved Trade-in lead, subject to current agreement and reversals. Paid CPC ceiling before costs = US$10 × approved-lead-per-ad-click for Used/New. At 5%, US$0.50 CPC; at 10%, US$1.00. The Google Ads UI's forecast and Ubersuggest CPC are not observed profit.
- Google Ads landing pages need useful original value; link-only bridge pages can violate destination requirements. https://support.google.com/adspolicy/answer/16427718
- Google Search's existing people-first SEO practices apply to AI Overviews/AI Mode; avoid thin, indexed dynamic filter variants. https://developers.google.com/search/docs/appearance/ai-features and https://developers.google.com/crawling/docs/faceted-navigation

## Product: Intent-to-listing engine
Create a reusable Intent Capsule with schema version, campaign/page intent ID, condition, body type, price cap, optional model, optional ZIP/radius, optional must-haves, optional trade-in interest, and source metadata. Ad links pass curated intent IDs and UTMs/GCLID; do not infer precise ZIP from an ad click or put personal details in tracking URLs. The user can edit all constraints. Keep source context in a privacy-conscious first-party session; GA4 receives only coarse intent and event IDs, not ZIP/VIN.

Screen 1: search-specific answer and one action. Example: "Find a used SUV under $25,000 that fits your life." Visible chips: Used / SUV / Up to $25,000. Ask an optional ZIP for nearby vehicles; offer "Search nationwide" explicitly. Ask at most one optional priority (space / AWD / fuel economy / lowest ownership concern) before search. Primary button: "Show matching vehicles." Secondary informational link: "How we choose." Do not gate on email, login, or chat composition.

Screen 2: three to five useful matches, not an endless generic inventory grid. Each card has identity, price, miles, dealer/location, evidence that the listing meets verified constraints, uncertainty to check, and "View full listing on Edmunds" only when a verified specific tracked link exists. Support edits and a transparent empty/thin result state. Use comparison at a glance for model trade-offs. No invented Deal Score or unverified reliability/history claim.

Screen 3: optional buyer check for a selected VIN/listing, where evidence exists, followed by the same listing action. Do not force this stage before handoff. Never claim an inspected car or guaranteed availability.

The AI role is to interpret natural-language needs into a structured capsule, explain match and trade-offs grounded in fields we actually possess, and ask a focused clarification when necessary. Filtering, price cap, condition, location, data provenance and outbound URL integrity remain deterministic. Log why each candidate passed, failed, or lacks evidence. Ranking is buyer-fit, not affiliate payout.

## Inventory architecture and the Catalog decision
Use two explicitly identified result lanes during development:
1. Find My Car / Auto.dev for used-condition, model, price and locality when its data confirms them. Verify whether each full-listing link genuinely reaches that vehicle on Edmunds with valid Impact attribution; suppress or relabel failures.
2. Impact Edmunds Catalog as an Edmunds-sourced complementary lane for category+budget/model discovery and pretracked product URLs. Display it condition-neutral and location-neutral unless a different verified source confirms a particular item. Never fuzzy-join Catalog and Auto.dev cards and claim they are the same car without a stable identity key. Do not silently broaden the budget to fill slots.

The Catalog alone cannot power a "used SUV near me" promise. To improve it, investigate an authorised richer Edmunds data path with condition, VIN/stock ID, last-updated, ZIP/dealer coordinates, live stock status and exact destination. Treat this as a partner/data-development workstream, not a dependency for the first useful experience. Validate tracked product URL redirects and Impact clicks; a working redirect does not prove current dealer availability. Preserve returned tracking URLs unchanged except permitted reporting parameters.

Always offer a truthful alternative: a valid tracked Edmunds under-$25k category continuation if generated and verified, or an existing approved Used destination clearly labelled as a broader browse. This bypass should not displace the decision tool's primary CTA. The live category page is not proof that an arbitrary deep link is permitted or tracks.

## Site and SEO/GEO architecture
- Build one indexable, server-rendered intent page for the curated theme at a stable GetCarWise URL. Above the fold: useful answer to the query and embedded buying flow; below: original comparison/selection method, six-model trade-offs, what is verified, where feed coverage ends, US pricing caveat, update date/editorial ownership, common buyer questions and links to related research. It must stand alone if the interactive API fails.
- Assess page 934 against this role. Preserve its observed SEO cohort and canonical unless the new page makes it redundant. It may become the comparison article linked to the new buying page, or be carefully revised into the combined intent page after GSC baseline and redirect/canonical review. Avoid two pages targeting the same phrase with near-identical text.
- Keep generated ZIP, filter and listing-result URLs nonindexable/canonicalized as appropriate. Curate additional landing pages only for materially different intents with demand and distinctive evidence, e.g. AWD under $25k, 3-row family SUV under $30k, specific model versus alternatives.
- Use visible, accurate structured data if eligible, but do not mark GetCarWise as the seller of Edmunds inventory. Google merchant listings require the merchant to be the seller: https://developers.google.com/search/docs/appearance/structured-data/merchant-listing .

## Paid Search design
Paused existing campaign stays unpublished. Treat the current three exact keywords as the comparison/budget cohort:
[best used suv under 25000]
[best used compact suv under 25000]
[used suv under 25000]
After product readiness, separate "best/compare" from "find listings" into distinct ad groups with distinct copy and preloaded intent. Start US presence, English, Google Search only, controlled spend and search-term review. Do not enable AI Max expansion or broad match until observed economics and term quality justify it. The broad head term "used SUV near me" is a later, likely expensive cohort; do not chase its volume.
Example comparison ad: "Compare Used SUVs Under $25K" / "Find One That Fits Your Needs" / "See Matching Vehicles." Example description: "Compare the trade-offs, then see used SUVs that fit your budget. Add ZIP for nearby results."
Example inventory ad: "Used SUVs Under $25K" / "Search Near Your ZIP" / "View Full Listings." Description: "Set your budget and location. See matching vehicles, then open the full listing."
Ad copy cannot claim live local Edmunds inventory or exact current availability until the displayed lane proves it. Site links can lead to the comparison method, buyer checks and the confirmed tracked Edmunds browse route. Do not use competitor brands as ad text casually.

## Measurement and unit economics
Event chain: landing_view (intent/source/ad group) → intent_edit → search_start → results_success/empty/error (source and counts) → partner_cta_view → partner_outbound (item-versus-category, source, immutable click key, link type) → Impact pending/approved/rejected/reversed action and USD payout. No ZIP, VIN, street address, email or phone in analytics. Reconcile browser/server events and GA4 across WordPress and Vercel with consent; preserve GCLID/UTMs without leaking them into vehicle data. Use permitted Impact Sub IDs to distinguish placement and source, and verify reporting, not just URL shape.

Dashboard cuts: query-intent cluster, ad group/keyword, device, ZIP-provided versus nationwide (aggregate only), results coverage, exact-listing-link rate, partner click-through, accepted lead per click, revenue per click, spend and variable tool cost. An outbound click is a diagnostic milestone, not the payout. Set bid ceiling from the mature approved-action rate in the same currency with a contribution-margin reserve.

Pre-spend acceptance gate: mobile page loads and gives value without API; five representative US ZIP/city scenarios and nationwide search produce truthful constraints and reasonable fallbacks; several returned Edmunds item links land on the same vehicle and record clicks; valid category bypass resolves; result errors do not dead-end; cross-domain attribution works; editorial statements match the tool; one real approved action or partner confirmation validates post-click reconciliation. If approved-action reporting lags, report the stage as unverified and hold scaling.

## Sequence and decision rights
1. Research and prioritise with current US GSC query/page export plus Google Keyword Planner; assess SERPs and the true Search Terms report after launch. Do not treat Ubersuggest estimates as actual paid CPC.
2. Engineer and QA the exact listing/Impact handoff and data provenance. Determine whether the current Find My Car links truly satisfy the promised specific-Edmunds-listing outcome.
3. Build the intent capsule, single-screen guided search and curated server-rendered page on top of existing Vercel/WordPress infrastructure. Keep the Catalog private until its public contract is truthful and link QA is complete.
4. Publish useful organic entrance and monitor GSC/indexing and tool outcomes. Prepare matching ad groups, copy, URLs and measurement.
5. Launch only a capped paid cohort after the path works; review terms and cost daily. Expand intents only when accepted-lead contribution and tool reliability justify it. Negotiate stronger data/partner economics if US$10 approved lead cannot support acquisition.
No live website, ad, app, or partner account changes are made by this plan.


## Addendum — catalog-card-to-Edmunds narrow continuation (Sep 30)

André proposed a two-stage handoff: the GetCarWise page shows a broad set of relevant vehicle examples, and a click on a chosen vehicle carries that narrower preference into Edmunds. This is a useful product pattern, with a precise hierarchy:

1. **Exact product link:** When an Impact Catalog item has a returned tracked product URL and a controlled check confirms it lands on that same Edmunds vehicle, keep that URL unchanged and label the CTA "View this vehicle on Edmunds." The Catalog prototype has shown URLs structurally valid and VIN-shaped strings embedded in their destinations, but did not click them, so the exact landing claim needs the separate click QA.
2. **Narrow similar-search link:** If the exact destination is absent, stale, or demonstrably wrong, generate an Impact-approved tracked continuation to the narrowest Edmunds search URL that has been verified to work for that combination. Preserve only supported filters: make/model; condition/year/trim as separately validated; ZIP, price and sort only when the actual Edmunds route applies them. Label "See similar [model] on Edmunds." Do not imply the clicked record will be on the results page, appear first, or still be available.
3. **Curated category link:** If a tested narrow route cannot be generated or has no useful matches, use a valid tracked Edmunds used-SUV-under-$25k page when that deep link is approved and tested, else the existing approved broader Used destination. Label the actual scope. The live untracked category page currently displays Used/CPO, SUV, up to $25,000 and offers ZIP input; it does not establish that a particular affiliate wrapper deep-links there.
4. **No dead end:** If no tracked partner route is valid, show useful on-site alternatives and an explicitly non-affiliate direct destination where appropriate. Do not create a fake product URL.

The choice of a catalog card gives us *preference information* (year/make/model/trim, price band, perhaps dealer if the record supplies it), even when the exact car no longer exists. That information can produce a helpful narrower search. However, we cannot guarantee that a result from the separate Catalog feed is Used or near the buyer: its Condition is empty, VIN is absent, item-level freshness was absent in the sample and ZIP radius is unsupported. For a paid "used SUV near me" page, only present cards as confirmed Used/local if another verified source or the actual Edmunds destination supplies that evidence. A condition-neutral catalog card may be labelled an Edmunds option with its limitations, but should not silently masquerade as a used local match.

Existing CarClever historical work supports *part* of the fallback pattern: an always-available make/model Edmunds category route was deployed, and later changes corrected condition/year handling; decorative ZIP/price URL parameters were removed because they did not apply the filters, and year+trim together was observed broken. Reuse the validated route-builder and its regression tests rather than inventing URL query parameters. See carclever-widget TASKS.md entries for Aug 17 and Aug 23–24 (SYS-20260817-001/002, SYS-20260823-002, SYS-20260824-001). Verify the current implementation before porting it to a new site flow.

A web click cannot be recovered after the browser has already left for an Edmunds dead page. Perform bounded link checks before offering the exact CTA (at fetch, cache refresh or pre-click where technically viable), and still state that dealer availability can change. Never crawl or scrape Edmunds to assert availability without a permitted, reliable method. Do not alter a Catalog-returned Impact URL to build the fallback; generate a separate approved tracking link for the fallback and inspect its real redirect.

The current Edmunds agreement review recorded a bar on *direct PPC to Edmunds* and specific negative-keyword/copy rules. The paid destination remains a substantive GetCarWise buying experience; the buyer chooses the outbound partner link from it. See getcarwise-docs DRAFT_TASK78_GOOGLE_SEARCH_LEARNING_TEST_20260924.md and the Sep 28 contract review in carclever-widget TASKS.md.

### Click acceptance cases
- Catalog item URL resolves to same actual vehicle: exact CTA, record item-level outbound.
- Item URL resolves to a generic page, wrong vehicle, or error: no "this vehicle" promise; offer a validated similar-search CTA.
- Narrow route preserves model but drops unsupported trim/ZIP/price: the button and landing context reveal the broader scope, and the buyer can set filters on Edmunds.
- Empty/thin local result: state that coverage is incomplete, show what was found, and offer the verified category/nearby alternative; never silently change a hard budget or condition.
- Tracking: each tier has a distinct link type and permitted Sub ID/context, and Impact reports clicks/actions; assess exact versus similar versus category conversion separately.

Evidence: live Edmunds category page https://www.edmunds.com/used-suv-under-25000/ ; account tests RETURN_IMPACT_CATALOG_C1_C8_READ_ONLY_TESTS_20260920.md and RETURN_IMPACT_CATALOG_PRIVATE_PROTOTYPE_20260921.md.
