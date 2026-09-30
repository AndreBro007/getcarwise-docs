# Phase 1 progress — Catalog-led local inventory desk audit
Date: 2026-09-30
Status: Static evidence and safe diagnostic prepared. **No new live Impact API request or affiliate click performed in this session.**

## Reviewed sources
- `getcarwise-docs/RETURN_IMPACT_CATALOG_C1_C8_READ_ONLY_TESTS_20260920.md`: 20 bounded GETs; 1,352,716 reported items; model/category+price/exact-dealer queries; 10/10 "dealer_location" completeness in one sanitized sample; Condition 0/10; item freshness 0/10; no ZIP/radius test success; no click.
- `getcarwise-docs/RETURN_IMPACT_CATALOG_PRIVATE_PROTOTYPE_20260921.md`: 62 tests, live authenticated six-card CR-V view, condition empty, no VIN field, product links not clicked, preview private and unmerged.
- `carclever-widget` branch `feature/impact-catalog-prototype`: actual adapter, shared types, API and UI. It normalizes `City` and `State` plus dealer name and stock indicator. Its `PageSize=10` national query renders at most six cards. It does not normalize a ZIP, coordinates, condition or item update timestamp.
- `carclever-widget` branch `feature/carclever-lite-v2`: `?q=` prefill and `/api/chat-v2` result flow; can inspire UI but cannot supply Catalog locality by itself.
- Impact's official partner help describes catalog details/Last Updated and platform, FTP or API download options; specific Edmunds download permissions, size and update pattern still need an account check: https://help.impact.com/partner/what-would-you-like-to-learn-about/platform-features/marketing-content/product-marketplace-and-catalogs/download-product-catalogs-as-a-partner

## What is established and what is not

| Topic | Established | Still unproved |
|---|---|---|
| Edmunds origin | Catalog is an Edmunds Product Feed with tracked item URLs. | That every item is currently active at the dealer or exact product link still opens the same vehicle. |
| Dealer location | One ten-item sample had a location field; adapter exposes City/State. | Postal/coordinate completeness, item-versus-dealer location, local recall across ZIPs, distance accuracy. |
| Local retrieval | Exact dealer filtering via feed-specific `Manufacturer` worked in a bounded test. | Discovery of all nearby dealers, scalable query cost, candidate completeness, geographic filter support, feed-index access. |
| Used | Sample Condition empty; no VIN field in sampled schema. | Any reliable authorized used/new source for Catalog cards. Model year and price are insufficient. |
| Stock/freshness | StockAvailability was nonempty in the prior sample; catalog has feed-level update time. | Whether stock value predicts current availability and whether individual rows have reliable timestamps/removals. |
| Product links | Returned tracking URLs structurally valid and displayed in private prototype. | Exact landing success, stale-link rate, verified Impact click/action attribution. |

## Prepared read-only diagnostic

Created branch `feature/catalog-locality-audit` from the private prototype and added `scripts/impact_catalog_phase1_probe.py`. It makes exactly three allowlisted, bounded Item requests (SUV <= $25k; CR-V <= $25k; RAV4 <= $25k, ten rows each). It prints aggregate nonempty location/date field counts, condition buckets, stock and URL presence, and distinct dealer count. It never prints raw item values, URLs, addresses, dealer names, account IDs or credentials; it follows no affiliate links. It is a *field audit*, not five-ZIP local coverage or live inventory validation.

Local checks in this session: `python -m py_compile` passed; a synthetic two-item aggregation/redaction check passed; with no Impact environment variables it exited with the expected missing-configuration message and issued no request. The shell environment here exposes no Impact credential variables. This prevents an honest live result from this workspace.

## Next private execution
1. In Claude's existing credentialed local environment, inspect this audit branch against the previous C1-C8 script and run `python scripts/impact_catalog_phase1_probe.py` once. Record only the redacted JSON output in the return document. Do not paste or log environment values.
2. If no postal/coordinate field is present, evaluate geocoding dealer City/State as a coarse pilot and audit ambiguity; do not claim a true ZIP radius. Check whether a permitted full catalog download or dealer index is available to avoid national ten-row sampling bias. No bulk transfer without capacity and feed-use review.
3. With bounded selected-dealer queries, measure local candidate counts in five representative US areas and how many API calls are needed. Query geographic fields only after confirming the field and syntax supported for this feed.
4. Resolve explicit Used condition from an authorized source or narrow the ad/product promise. No automatic used label from age.
5. Perform a separately recorded small, controlled exact-link landing and Impact attribution check. Classify the exact/similar/error results; do not treat URL shape or a landing redirect alone as current stock proof.
6. Choose API nearby-dealer method, refreshed server-side index or alternate source from measured coverage/latency/freshness. Then implement buyer UI in a separate branch/preview. Keep Google Ads paused.

This audit narrows the work, but **Stage 1 has not passed**. The existing private branch and production remain untouched by the diagnostic branch. The marketing decision remains Approach B as the product priority, with page 934's comparison route retained.
