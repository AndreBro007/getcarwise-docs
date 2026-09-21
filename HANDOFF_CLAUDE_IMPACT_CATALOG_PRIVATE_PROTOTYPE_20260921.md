# Handoff — Impact Catalog Private Inventory-Continuation Prototype

**Task:** #71  
**Owner:** Claude engineering, only after André supplies this handoff  
**Status:** Ready for a private/noindex engineering prototype; **no public launch or WordPress publication authorized**  
**Governing evidence:** `RETURN_IMPACT_CATALOG_C1_C8_READ_ONLY_TESTS_20260920.md`  
**Governing architecture:** `RETURN_TOOL_LED_IMPACT_FUNNEL_FEASIBILITY_20260920.md`, as corrected by the successful C1–C8 return

## 1. Goal

Build a small reusable private prototype that proves GetCarWise can display a few relevant Edmunds Catalog listings after an independent editorial/tool answer and route clicks through the unchanged Impact item URL.

This is an inventory-continuation component, not a marketplace, local-search engine, SEO page generator or New/Used classifier.

## 2. Mandatory start and stop rules

Perform the repository/checkpoint verification required by `PLAYBOOK.md` before touching code. Read the governing evidence and architecture documents in full.

Stop and return the blocker before implementation if:

- the intended repository/deployment target is not unambiguously confirmed;
- a private/noindex/access-controlled route cannot be guaranteed;
- Impact credentials cannot remain server-only;
- implementation requires Publisher Tag, a bulk Catalog download, arbitrary query passthrough or production WordPress edits;
- a required returned-field mapping differs from the successful C1–C8 evidence;
- the existing repo has concurrent changes that overlap the intended files.

Do not deploy publicly, embed in WordPress, change any existing CTA, alter an active SEO/GEO treatment, create leads, or submit personal information.

## 3. Proven API contract

Use the per-catalog Items endpoint only. The live account proved:

- equality syntax uses a single equals sign, for example `Text1 = 'CR-V'`;
- Boolean `AND` works with category/model plus numeric price expressions;
- `Text1` is the model field;
- `Category` supports the observed body-style value;
- `Manufacturer` is the dealer-name mapping for this feed, not vehicle make;
- `CurrentPrice` supports numeric ceilings;
- `Condition` is an unknown search field and is missing from samples;
- `ItemSearch` is outside the current token scope and must not be called;
- result traversal stops at 20,000 items;
- the item endpoint exposed a 3,000 requests/hour limit in the observed headers;
- returned item URLs use the expected Impact/Edmunds tracking host.

Never accept a raw Impact `Query` string from the browser. Build expressions only from validated allowlisted fields and values.

## 4. Prototype scope

### Inputs

- one allowlisted exact model token **or** one allowlisted observed body-style value;
- maximum price from controlled server-defined bands;
- page/module context identifier from a controlled vocabulary.

Do not include:

- New/Used/CPO selector;
- ZIP/radius/distance;
- VIN input or VIN search;
- free-text dealer, model or query expressions;
- name, email, phone or financial information.

### Output

Return at most 3–6 cards with only validated Catalog-supplied fields:

- year, vehicle make, model and trim;
- current price and USD currency;
- stock indication if present, paired with “availability may change”;
- dealer display name and coarse city/state only if present and approved;
- image URL after host/protocol validation;
- “View on Edmunds” using the returned tracking URL unchanged.

Do not display condition, freshness age, proximity, “near you,” completeness, ranking superiority or any inferred vehicle fact.

### Required states

- loading;
- healthy, 3–6 usable cards;
- thin, 1–2 cards plus transparent fallback;
- empty, explicitly “No matches in this Edmunds feed,” not “No vehicles exist”;
- upstream error/timeout with approved static fallback;
- malformed/missing-field suppression;
- kill-switch state showing only static links.

## 5. NHTSA enrichment spike

Treat NHTSA as optional validation, never as a prerequisite for rendering.

If and only if an Impact record exposes a valid VIN to the server-side adapter:

1. keep the VIN server-side;
2. call NHTSA vPIC through a small isolated adapter;
3. compare returned model year/make/model against the Catalog record;
4. optionally normalize body class and powertrain/electrification clues;
5. mark material mismatches internally and suppress the affected card rather than guessing;
6. do not store or log the VIN, return it to the browser, or send it to analytics;
7. time out quickly and fall back to Catalog-only rendering.

NHTSA must never set or infer New/Used/CPO, ownership, title, accident, mileage, service history, availability or distance. Recall context is a separate vehicle-check concern and is not required on the first inventory card.

Implement NHTSA behind a disabled-by-default feature flag unless the actual Catalog VIN field and completeness are verified privately during this task.

## 6. Server adapter requirements

- credentials only in server-side environment variables;
- strict input schema and allowlists;
- output schema containing only display-approved fields and an opaque result ID;
- URL allowlist for HTTPS `edmunds.sjv.io`/approved Impact/Edmunds hosts;
- no URL rewriting or appended attribution parameters in this prototype;
- timeout, one bounded retry only for retryable failures, and circuit-breaker/kill switch;
- page size no greater than 10 upstream and no pagination traversal;
- in-memory or approved short cache only after checking upstream cache terms; otherwise no cache;
- redact credentials, account/catalog/item IDs, URLs, VINs, dealer street addresses and raw upstream bodies from logs;
- treat zero returned items with upstream total `-1` as a valid empty result;
- never silently broaden model, category or budget constraints.

## 7. Funnel and measurement boundary

The private prototype may emit a local debug event ledger, but must not install Publisher Tag or send production marketing events.

Use the future event names defined in the feasibility return, with test-only output and no PII:

- `inventory_module_view`;
- `inventory_search_submit`;
- `inventory_results`;
- `inventory_outbound_click`;
- `inventory_fallback_click`.

Do not put VIN, ZIP, dealer address, raw URL, credentials, account/catalog/item IDs or free text in events.

Keep the monetization architecture visible in the UI:

- cards continue through their returned item links;
- separate approved static New/Used fallbacks remain available according to host-page intent;
- Trade-in is absent unless the prototype explicitly establishes replacement intent.

## 8. Tests and acceptance gates

Automated tests must cover:

1. allowlisted query construction using live-proven single-equals syntax;
2. injection and arbitrary-field rejection;
3. model and category-plus-price mappings;
4. missing `Condition` never creates a condition label;
5. empty total `-1` normalization;
6. thin/empty/error/timeout rendering;
7. URL host validation and unchanged outbound URL;
8. log/event redaction;
9. NHTSA mismatch, blank decode, timeout and feature-flag-off behavior;
10. mobile, keyboard and basic screen-reader behavior;
11. kill switch and static fallback;
12. noindex/access-control response behavior.

Private live verification may use only a handful of bounded reads. Do not load-test or approach the hourly limit. Do not click more than one ordinary returned tracking URL, and only if André separately authorizes that controlled click.

Acceptance requires:

- all tests and build/type checks pass;
- no secret or prohibited identifier reaches client output, logs or test snapshots;
- no card claims New/Used or local proximity;
- module remains useful when Impact and NHTSA both fail;
- route is confirmed private and noindex;
- no production/domain/WordPress change occurs.

## 9. Return document

Write `RETURN_IMPACT_CATALOG_PRIVATE_PROTOTYPE_20260921.md` with:

- exact repository, branch and files changed;
- architecture and normalized schemas;
- test/build results;
- screenshots at mobile and desktop widths;
- sanitized request count and latency observations;
- NHTSA field/completeness finding, including whether a VIN was actually available;
- confirmation that condition was neither inferred nor displayed;
- security/redaction review;
- private/noindex/access-control evidence;
- rollback instructions;
- explicit list of everything not changed;
- recommendation: stop, revise, or seek separate production-pilot authorization.

## 10. Explicit exclusions

No public page, WordPress edit, SEO/GEO change, CJ/Impact migration, Publisher Tag, bulk feed, production deployment, new lead submission, mass page creation, ZIP/radius claim, VIN search or condition inference.

