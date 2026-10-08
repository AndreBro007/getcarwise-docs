# Implementation brief — Catalog-led local buyer journey (Approach B)
Date: 2026-09-30
Status: Build-ready research and private engineering brief. The Google Ads draft remains paused. No public site, campaign, or partner-account change is made by this document.


> **VIN correction — 8 October 2026:** The September 16 migration investigation explicitly recorded VIN values in the returned `Mpn` field. It separately established that `Mpn`/VIN cannot be searched or filtered through the Catalog Items API (Impact ticket #882346). The September 21 probe checked VIN-like field names and selected text fields, without documenting a check of `Mpn`; it does not establish that returned records lack VINs. Inspect `Mpn` explicitly in a bounded current read and validate completeness/format before wiring enrichment. Historical returned-field evidence is established; current feed-wide completeness is not. [Source](https://github.com/AndreBro007/getcarwise-docs/blob/main/STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md).

## Product decision
Create a substantive GetCarWise website journey for a US buyer with an SUV budget and optional location. The promise is a short, useful decision plus Edmunds-fed vehicle options and a transparent handoff. The buyer should be able to act within one or two interactions, edit the intent, and understand exactly what is verified. The Impact Catalog is the first candidate source of website inventory. CarClever's narrow Edmunds route is a labelled fallback when an exact item link is absent or stale. The Catalog is **not** added to the MCP apps.

The eventual paid cohort is local inventory intent, distinct from page 934's existing "best/compare" cohort. Do not buy "used SUVs near me" traffic until the returned cards have verified used classification and local coverage. A condition-neutral "SUVs under $25k" version is a separate candidate if its copy and actual results are truthful.

## Evidence from existing code and tests
- `carclever-widget` branch `feature/impact-catalog-prototype` has a private Basic Auth/noindex prototype, server-only adapter, validated allowlisted query, kill switch and unchanged `edmunds.sjv.io` item links. It passes 62/62 tests and André verified six CR-V cards. It is unmerged.
- The adapter `lib/impact-catalog.ts` currently queries `Text1` (model) or `Category` (SUV), optional `CurrentPrice`, `PageSize=10`, and normalizes at most six cards. Its public card exposes dealer name, `City`, `State`, stock indicator, price and tracked URL. It does **not** expose dealer ZIP, coordinates, street address, condition, listing ID or item freshness. The C1–C8 report marked dealer location 10/10 in ten records; this does not establish ZIP completeness or distance accuracy.
- `Manufacturer` is mapped to dealer name for this Edmunds feed, not vehicle make. Exact dealer filtering worked in the bounded test; 301 reported rows for one dealer. Traversal window 20,000 and observed rate header 3,000 item requests/hour. No bulk download or true local retrieval test has been run.
- `Condition` exists but was empty in sampled items. VIN was historically documented in `Mpn`; it is not searchable through the catalogue API and is not normalized by the current prototype. The later no-VIN probe did not account for that mapping. A Used label cannot be inferred from year/price. A `StockAvailability` value existed in the sample but was not validated against live dealer stock. Catalog Last Updated is feed-level. Partner docs say catalog details expose Last Updated and offer platform/FTP/API download where the partnership permits it: https://help.impact.com/partner/what-would-you-like-to-learn-about/platform-features/marketing-content/product-marketplace-and-catalogs/download-product-catalogs-as-a-partner
- Lite V2 `app/carclever-lite-v2/page.tsx` is a standalone chat client whose `?q=` prefills without automatic submission and whose `/api/chat-v2` calls Find My Car. Reuse its result-card ideas only after mapping data provenance; this website experience should have typed intent controls and server-prepared results, not an empty chat landing.
- Relevant source reports: `RETURN_IMPACT_CATALOG_C1_C8_READ_ONLY_TESTS_20260920.md`, `RETURN_IMPACT_CATALOG_PRIVATE_PROTOTYPE_20260921.md`, `PLAN_INTENT_TO_EDMUNDS_BUYER_JOURNEY_20260929.md`.

## Stage 1 — bounded private data and destination spike

Run under the existing private/noindex protection and read-only credentials. Do not expose secrets, raw dealer addresses, item IDs, raw link lists or upstream bodies in reports. Keep requests bounded and record exact counts, dates, field presence and aggregate outcomes. Check with Claude's earlier field audit before repeating any test.

1. **Location schema:** inspect field *names* and safe aggregate completeness across a stratified sample (e.g. 5 US metros, SUV under $25k and several exact models/dealers). Determine whether dealer ZIP or lat/lon actually exists, whether city/state is unambiguous, and whether item location may differ from dealer location. Sample more than ten items without walking broad result pages.
2. **Local retrieval options:** test any documented/authorized filter on city/state/postal field with a handful of bounded queries; if unsupported, test nearby-dealer discovery and exact `Manufacturer` plus price/category query shape. Estimate dealer coverage, number of API calls, duplicate rows and missing candidate bias in a few ZIPs. Do not treat the first ten national results as the local universe.
3. **Feed index feasibility:** inspect this partnership's permitted catalog download formats, compressed size, synchronization frequency and applicable use limits without downloading the 1.35m-item file in this first spike. If feasible, design a server-side refreshed index with dealer geocodes and category/price/condition fields. Account for removals and stale rows. No client-side credentials or raw feed.
4. **Used truth:** search for an explicit, reliable condition value from an authorized source/field, not a model-year heuristic. Check contradictions on a bounded sample. If absent, define a separate product promise or partner source before a used-only inventory CTA.
5. **Link outcomes:** with an authorized controlled check, sample a small, stratified set of returned tracked item links. Record same exact active car / unavailable with alternatives / generic page / wrong car / error. Confirm click attribution separately from landing correctness. Preserve the returned item URL unchanged; never rewrite it to create a search URL.
6. **Fallback:** verify an independently generated, permitted Impact-tracked narrow Edmunds search for make/model (and only those filters actually honored). Then a verified broader Used category route. A stale item is labelled "See similar vehicles on Edmunds", never "View this vehicle."

**Spike exit:** a short decision table showing field completeness by sample stratum, 5-ZIP local coverage and latency/cost, used-condition evidence, exact-link success and fallbacks. Recommend API-nearby-dealer lookup, refreshed feed index, hybrid, or another source. Mark unknowns plainly. Do not build or advertise a proximity claim if location is only city/state without validated coordinates.

## Stage 2 — product architecture after spike

**Source pipeline:** server-only Impact adapter -> normalized candidate rows with field provenance and feed observed time -> server-side dealer geocode/index -> hard filters (budget/body/condition only if verified) -> proximity and buyer-fit ranking -> small result set -> exact/similar/category continuation. Deduplicate by stable feed item key inside the server, never fuzzy-join to Auto.dev and claim the same vehicle without a stable verified identity. Refresh/index and query separately. Cache dealer geocodes; no geocoding per page impression. Use a distributed rate limit and cache because the prototype's in-memory per-IP Map is not a production-wide limiter on Vercel.

**Intent contract:** `intentId=used-suv-25k-local-v1`, budget 25000 USD, body SUV, optional user ZIP and radius, optional priority (space/AWD/fuel economy/value), condition Used only when source confirms it. UTMs and campaign IDs identify creative, not the exact user's query. Do not put ZIP/VIN in URL tracking or GA4. The visitor can change budget/location; nationwide is an explicit choice. A paid URL may open a prepared state but must not fabricate a ZIP or automatically claim local results.

**Ranking:** hard verified constraints first; then proximity, price/value proxy only if defensible, preference fit, data completeness and freshness/validity. Show why each option appears, plus what must be checked at Edmunds/dealer. Do not claim AI has verified mechanical reliability, clean title, stock availability or the cheapest market price.

**UI state contract:** initial/ZIP prompt, loading, useful results, thin coverage, no verified Used result, stale exact link, upstream unavailable. Each has a helpful next action and truthful partner route. Feature flag public Catalog cards independently of the editorial page.

## Stage 3 — landing-page design and SEO

Choose one stable GetCarWise URL for the inventory-intent product after assessing page 934's GSC/canonical role. Proposed above-the-fold copy when the data gates pass:

- H1: "Find a used SUV under $25,000 near you"
- Deck: "Tell us your ZIP and what matters most. Compare a few options, then open the full vehicle listing on Edmunds."
- Visible intent: Used / SUV / Up to $25,000; editable.
- ZIP with "Search nationwide" alternative; one optional priority choice.
- CTA: "Show matching SUVs."
- Result card: year/make/model/trim, price, dealer city/state and validated approximate distance, source/availability caveat, a concise fit/trade-off reason, and "View this vehicle on Edmunds" only after exact destination QA. If stale: "See similar [model] on Edmunds."
- After results: comparison of six sensible SUV models, which compromises matter, practical inspection questions, method and date, partner disclosure, FAQ and links to page 934's independent comparison if it remains a separate page.

For a **condition-neutral** interim product, remove "used" from the H1/ad and do not imply all results are used. For a city/state-only pilot, remove "near you"/distance and let the buyer explicitly choose a region. Server-render the useful explanatory content so the page is helpful without the inventory API. No indexable ZIP/filter permutations or thin city doorway pages. Do not claim to be Edmunds or a dealer.

## Stage 4 — measurement and channel readiness

Events: `landing_view`, `intent_edit`, `search_start`, `results_success/thin/empty/error`, `partner_cta_view`, `partner_outbound` with tier exact/similar/category, `impact_action_pending/approved/rejected/reversed`. Aggregate by intent ID, source, ad group and geography *band* only. Keep ZIP, VIN, dealer street address, raw tracking URL and credentials out of analytics/logs. Verify Impact Sub ID/click reconciliation before buying traffic; the US$10 payout is per approved lead, not outbound click.

Page 934 remains the comparison route for the paused three-keyword exact Search draft unless deliberate SEO review combines/replaces it. The inventory ad group is separate and cannot launch until its actual page promise is satisfied. US presence, Google Search only, no expansion, capped spend, negative terms and agreement-approved on-page creative remain draft controls. Direct PPC to Edmunds is not the route. Reddit can use the same substantive buyer experience later but needs its own creative, account cost/targeting review and separate source measurement.

## Implementation order and acceptance

| Gate | Deliverable | Pass condition |
|---|---|---|
| 1 | Private data/location/link spike | Evidence table resolves local retrieval, Used truth and exact link success; no fabricated claims |
| 2 | Server search and indexed source | Five representative ZIPs plus nationwide return relevant results or honest thin states within measured latency/cost; no secrets in client |
| 3 | Buyer UI and editorial page | Mobile buyer can edit intent, understand why results appear and reach exact/similar Edmunds route; page useful when API fails |
| 4 | Attribution | Test journeys from source to click and Impact reporting; approved-action stage marked unverified until observed/confirmed |
| 5 | Paid decision | One reviewable campaign/ad/landing package with daily and total cash cap and stop rules; no automatic publication |

**Immediate next execution:** commission Stage 1 on the existing private branch, using this brief and Claude's previous audit as input. Its result determines whether the first build uses API dealer queries or a permitted refreshed feed. If neither gives acceptable local/Used coverage, keep B as the product direction but change the inventory data source or narrow the advertised promise; do not spend to discover a known data gap.
