# Handoff — Tool-Led Impact Funnel Technical Feasibility

**Date:** 2026-09-20  
**From:** ChatGPT — Business/Strategy lane  
**To:** ChatGPT — Business/Strategy feasibility review; Claude reserved for any later implementation  
**Status:** **FEASIBILITY AND ARCHITECTURE ONLY — NO PRODUCTION IMPLEMENTATION**

## Objective

Translate the newly approved tool-led SEO/GEO and monetization strategy into a technically credible, reusable implementation plan.

Read the governing strategy in full:

`STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md`

The intended system is:

> Evidence-led landing page → useful decision tool → relevant New, Used or Trade-in continuation → Impact-tracked Edmunds lead → measurable revenue/learning loop.

This is not a request to add more generic affiliate buttons. It is a request to determine how GetCarWise can build reusable interactive modules that create differentiated user value and then route the appropriate next action.

## Mandatory boundary

Do not:

- modify production WordPress;
- modify `carclever-find-my-car`;
- deploy anything;
- change existing CJ or Impact links;
- install Publisher Tag;
- expose credentials;
- create indexable pages;
- build multiple tool pages;
- change the active $30k/PHEV/$25k SEO treatments;
- interfere with the separate Task #68 midsize-sedan audit.

Return evidence and a recommended build plan only.

## Required reads

Read in full:

1. `STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md`
2. `STRATEGY_DISCOVERY_MCP_EDMUNDS_REVENUE_FUNNEL_20260916.md`
3. `STRATEGY_IMPACT_WEBSITE_PUBLISHER_TAG_ASSETS_CATALOG_20260916.md`
4. `REVIEW_WORDPRESS_IMPACT_LINK_ARCHITECTURE_20260919.md`
5. `DESIGN_SPEC_FIND_MY_CAR_DECISION_JOURNEY_AND_MONETIZATION_20260902.md`
6. `STRATEGY_MASTER_SEO_GEO_REVENUE_MATRIX_20260919.md`
7. This handoff.

Use repository and live-account evidence rather than relying on memory.

## Workstream A — existing technical surface inventory

Map the current website/app components that could support reusable tools.

Record:

- WordPress theme/builder constraints;
- existing CarClever Lite embed mechanism;
- available REST/custom-plugin/shortcode options;
- any existing Vercel-hosted widget or API that can safely support a WordPress module;
- current analytics/event instrumentation;
- consent/Complianz interaction;
- current CTA implementation;
- mobile/responsive constraints;
- CSP/CORS/domain restrictions;
- secret-storage options.

Do not recommend putting Impact credentials or private API keys in browser-delivered JavaScript.

## Workstream B — Impact action mechanisms

Validate the exact role and current usability of:

1. static Impact deep linking;
2. Publisher Tag basic integration;
3. Product Catalog API;
4. Impact text assets;
5. Impact Sub IDs / Shared IDs / page-story attribution.

For each, return:

- confirmed capability;
- confirmed limitation;
- authentication requirement;
- client-side versus server-side suitability;
- attribution available;
- graceful-failure behavior;
- consent/privacy impact;
- page-performance implications;
- best-fit tool/page use cases.

Do not repeat the disproven VIN-to-Catalog design. Catalog cannot search by VIN.

## Workstream C — Catalog utility and geography

Using controlled, read-only tests, establish what the Edmunds Catalog can actually support for a website module.

Test representative queries for:

- model;
- make + model;
- body style/category;
- New versus Used condition if available;
- price/budget if supported;
- dealer;
- electrification if supported;
- location, ZIP, radius or geographic fields;
- post-filtering by returned dealer address/city/state;
- sort order;
- pagination;
- freshness/stock;
- image availability;
- tracked URL;
- empty/thin results;
- latency and rate limits.

Use at least:

- one high-volume mainstream model;
- one hybrid/PHEV model;
- one body-style/budget intent;
- one deliberately thin-market query.

For each test, record exact request shape, response fields, count/coverage, latency and limitations.

Do not publish or write returned inventory to the website.

## Workstream D — rights and data-use boundary

Determine from available Impact/Edmunds terms or support evidence:

- whether individual catalog listings may be displayed publicly;
- whether images, price, dealer, stock and tracked links may be shown;
- whether caching is allowed and for how long;
- whether derived counts/aggregates may be published;
- required attribution/disclosures;
- prohibited transformations;
- whether the data may be combined with Auto.dev output.

If the terms are unclear, mark the question unresolved and identify the exact support question required. Do not assume API access equals publication or aggregation rights.

## Workstream E — reusable architecture options

Compare at least three implementation patterns:

### Option 1 — WordPress-native plugin/shortcode

Assess:

- maintenance;
- security;
- caching;
- editor reuse;
- performance;
- analytics;
- deployment/rollback.

### Option 2 — Vercel-hosted embedded module

Assess:

- reuse of existing widget infrastructure;
- isolation from WordPress;
- API/secret handling;
- iframe or script integration;
- CSP/CORS;
- mobile behavior;
- analytics and consent;
- SEO visibility of surrounding content versus module output.

### Option 3 — server-rendered WordPress/Vercel hybrid

Assess:

- crawlability;
- freshness;
- caching;
- operational complexity;
- fallback behavior;
- attribution.

Recommend one pattern and explain why.

Do not write code in this feasibility task.

## Workstream F — first reusable module specification

Specify, but do not build, this prototype:

### Budget + condition + body-style inventory continuation

Purpose:

> After GetCarWise independently explains the decision, let the user see a small, relevant Edmunds inventory subset and continue toward a valid New or Used lead.

Candidate inputs:

- budget;
- New / Used / either;
- body style;
- make/model optional;
- electrification optional;
- location only if supported honestly.

Required output behavior:

- 3–5 results maximum;
- price;
- vehicle/model label;
- condition;
- dealer/location where returned;
- image where permitted;
- freshness/availability caveat;
- Impact-tracked destination;
- empty/thin coverage message;
- broad category fallback;
- affiliate disclosure;
- no claim of complete U.S. inventory.

The module must remain subordinate to the independent recommendation.

## Workstream G — trade-in bridge

Define a reusable secondary component for pages where replacement intent is natural.

It must:

- explain why valuing the current vehicle affects the purchase decision;
- route to the valid Edmunds Trade-in lead;
- remain optional;
- never displace the primary New/Used action;
- be primary only on valuation, sell, depreciation or keep-versus-replace tools;
- carry separate attribution.

Return recommended language and placement rules, not production copy for every page.

## Workstream H — measurement architecture

Specify the full event and attribution flow:

`landing → tool_view → tool_start → tool_result → CTA impression → CTA click → Impact action/lead → commission`

Return:

- event names;
- required properties;
- prohibited/sensitive properties;
- GA4/Clarity/Impact ownership;
- how page, module, lead family, placement and variant are identified;
- confirmed Impact Sub ID / Shared ID handling;
- Publisher Tag page/story reporting availability;
- deduplication approach;
- reporting table needed to calculate:
  - valid leads;
  - revenue per visitor;
  - revenue per qualified tool completion;
  - revenue per outbound click;
  - lead mix;
  - conversion lag.

Do not log full VINs, exact personal finance inputs or unnecessary personal data.

## Workstream I — tool-led page/template implications

Return a technical assessment of the proposed page families:

- budget/inventory finder;
- new-versus-used decision tool;
- model comparison;
- affordability/TCO;
- VIN/listing risk;
- trade-in/replace/keep.

For each, state:

- reusable components;
- required backend/data;
- primary and secondary lead paths;
- SEO/indexability approach;
- what must remain static/editorial;
- what should be dynamic;
- cannibalization/thin-page risk;
- estimated engineering complexity: low/medium/high;
- recommended sequence.

Do not propose automatically indexable parameter pages.

## Workstream J — pilot recommendation

Recommend:

1. the safest unindexed/non-production prototype environment;
2. the first reusable module;
3. the first eventual production pilot page;
4. why that page should be used;
5. how to avoid contaminating current treatment measurement;
6. rollback and kill-switch approach;
7. acceptance tests;
8. what requires André approval.

Do not assume the Tools hub should host the monetization module. Its role is routing and it currently has strong GEO visibility.

## Required return

Create:

`RETURN_TOOL_LED_IMPACT_FUNNEL_FEASIBILITY_20260920.md`

Include:

1. executive recommendation;
2. current technical surface inventory;
3. Impact mechanism matrix;
4. exact Catalog test ledger;
5. geography findings;
6. rights/data-use findings;
7. architecture comparison;
8. recommended architecture;
9. first-module specification;
10. trade-in bridge specification;
11. measurement/event contract;
12. tool-page family feasibility matrix;
13. pilot recommendation;
14. risks and blockers;
15. decisions requiring André;
16. explicit confirmation that no production/code/WordPress/deployment changes were made.

Re-fetch and verify the return after writing it.

## Decision gate

ChatGPT and André will review the return before authorizing:

- code;
- WordPress changes;
- Publisher Tag installation;
- a Catalog module;
- a new tool page;
- a production pilot.

The goal is not to maximize affiliate exposure. The goal is to build a differentiated decision-tool system whose useful next actions create measurable New, Used and Trade-in leads.
