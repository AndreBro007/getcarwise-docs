# Review — WordPress Batch 1+2 + Edmunds/Impact Link Architecture

**Date:** 2026-09-19  
**Reviewer:** ChatGPT — Business/Strategy lane  
**Status:** Implementation review complete; affiliate architecture clarification recorded  
**Reviewed sources:**  
- `RETURN_WORDPRESS_SEO_GEO_BATCH1_BATCH2_20260919.md`
- `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md`
- `STRATEGY_IMPACT_WEBSITE_PUBLISHER_TAG_ASSETS_CATALOG_20260916.md`
- `HANDOFF_EDMUNDS_CJ_TO_IMPACT_MIGRATION_20260916.md`
- current `STATE.md`

## Implementation review

Claude's return is internally consistent with the approved Batch 1+2 handoff.

Confirmed from the return/admin record:

- 3-row factual corrections completed without broad structural changes.
- Tools hub now contains one link to the retained $25k URL.
- $30k page received the approved content/metadata treatment.
- $30k T0 baseline captured: 0 clicks / 22 impressions / avg pos 25.2 / 3 Google Generative AI impressions.
- Google recrawl requested.
- No app/MCP/Vercel changes.
- No $25k consolidation yet.
- No PHEV rebuild yet.

Direct public-page fetching was not available to ChatGPT's current web fetch path, so this review relies on Claude's verified return plus STATE/commit evidence rather than claiming an independent live-browser click test.

---

# Critical affiliate-link clarification

## Current WordPress state

The website CTAs are **still CJ**, not Impact.

### $30k page

Current CTA:

`https://www.jdoqocy.com/click-101637236-15700851`

Label:
`Browse SUVs on Edmunds`

There are two instances on the page.

### 3-row page

Current CTA:

`https://www.anrdoezrs.net/click-101637236-15701072`

Label:
`Browse Used Cars on Edmunds`

These were deliberately preserved byte-identical during Batch 1+2 to keep affiliate migration separate from the SEO/GEO content-treatment date.

Therefore the current website CTAs are:

- **not Impact links**;
- **not Publisher Tag links**;
- **not Product Catalog API result links**;
- **not dynamically narrowed per model on the page**;
- **not confirmed as ZIP/radius/location-aware GetCarWise-generated searches**.

They are legacy CJ affiliate destinations.

The app/MCP migration to Impact on Sep 17 did **not** migrate WordPress.

---

# Current app/MCP link architecture — separate from WordPress

The Find My Car applications are already on Impact.

They do **not** use the Impact Product Catalog API for runtime link generation.

Current app path:

> Auto.dev/CarClever finds/evaluates the vehicle → GetCarWise already has/builds the intended Edmunds destination → static Impact affiliate wrapper → `edmunds.sjv.io` → Edmunds.

Known exact VIN destinations can deep-link to the exact VIN page through Impact.

The Product Catalog API is **not** queried by VIN and is **not** a dependency for app search/result links.

---

# Product Catalog API — current website status

## What it can do

Confirmed searchable dimensions include:

- model (`Text1`);
- body style/category (`Category`);
- dealer name (`Manufacturer`, despite the misleading field label).

Returned catalog results include:

- current price;
- stock status;
- photo;
- dealer information/address;
- year/model/trim;
- ready-to-use Impact tracked URL.

VIN/MPN is present in item data but **cannot be searched/filter directly**.

## What it does NOT yet do

The WordPress site currently makes **no Product Catalog API calls** to pull vehicles.

There is currently:

- no live-inventory module;
- no per-model catalog widget;
- no catalog-fed cards on the $30k/3-row/PHEV/$25k pages;
- no confirmed catalog ZIP/radius search.

Location/geography is not yet established as a supported catalog search dimension. Dealer/address fields are returned, so geography may be useful for post-filtering/selection, but this requires a specific utility test before public deployment.

---

# Publisher Tag — current status

Publisher Tag is available but **not implemented on WordPress**.

It can convert clean direct Edmunds links into Impact tracked links and collect page/link attribution.

Important:

> Publisher Tag does not rewrite existing CJ affiliate links.

Therefore website migration requires replacing/inventorying the CJ URLs first.

---

# Approved future website architecture

The corrected strategy remains:

> **Publisher Tag for ordinary editorial Edmunds links → static Impact deep-linking for exact known Edmunds destinations → Product Catalog for general filtered current-inventory discovery → Impact text assets for broad fallbacks → banners only as measured experiments.**

For SEO/GEO high-intent pages, the strongest catalog concept remains:

> Independent GetCarWise recommendation → small “current inventory” module → narrow model/category catalog query → 3–5 relevant live Edmunds listings with price/photo/dealer/stock + tracked links.

This should be tested on **one page only** after the basic WordPress CJ→Impact migration succeeds.

---

# Location-aware / “narrow” search question

The current WordPress CTAs do **not** implement a GetCarWise-controlled “model + user location” narrow search.

Two possible future mechanisms must not be conflated:

1. **Clean Edmunds model/category destination + Publisher Tag**  
   Edmunds may apply its own location/user context after landing, but GetCarWise is not currently passing a validated ZIP/radius search in these CTAs.

2. **Product Catalog API module**  
   GetCarWise could query by supported model/category/dealer fields and potentially use returned dealer geography to select relevant results. A true ZIP/radius API filter has **not** been confirmed and should not be promised.

If location-sensitive inventory is important, the next Catalog Website Utility Audit should explicitly test:

- whether any supported geographic search parameter exists;
- whether state/city/dealer-address post-filtering is practical;
- whether location can be inferred/selected without privacy/consent issues;
- fallback behavior when local Edmunds catalog coverage is thin.

---

# Recommended next sequence

## 1. Website CJ → Impact migration — next

This is now the clearest immediate commercial gap.

For the existing commercial WordPress CTAs:

- inventory every remaining CJ hostname/link;
- map each CTA to its intended Edmunds destination;
- replace with either:
  - clean Edmunds destination + Publisher Tag basic integration, or
  - direct/static Impact link where that is simpler/more deterministic;
- preserve `rel="sponsored"` and disclosures;
- verify Impact click attribution;
- record migration date separately from Sep 19 SEO/GEO treatment.

Do **not** change $30k editorial content during the affiliate migration.

## 2. Catalog utility pilot — after basic migration

Choose one high-intent page and test a small current-inventory module.

Best candidates after the content program matures:

- Used PHEV page after rebuild;
- $30k page after initial T+14/T+28 content read;
- later $25k canonical page.

Do not launch catalog modules simultaneously on multiple pages.

## 3. Location/narrow-search behavior — test explicitly

Before calling any future module “near you” or location-aware, verify actual Catalog API geography behavior.

---

# Bottom line

There are **three separate systems**:

1. **Website today:** legacy broad CJ CTAs.
2. **Apps today:** Impact `edmunds.sjv.io` static/deep links; no catalog dependency.
3. **Future website catalog module:** not implemented yet; planned as a separate model/category/dealer filtered inventory experiment.

The current website is therefore **not yet using the new Impact affiliate codes and is not currently pulling vehicles from Impact's Catalog API**.
