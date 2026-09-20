# HANDOFF — Impact Catalog C1–C8 read-only API tests

**Date prepared:** 2026-09-20  
**Owner:** Claude (authenticated execution)  
**Task:** #65 — Impact Product Catalog Website Utility Audit + location test  
**Authority:** Evidence collection only. No implementation, deployment, WordPress edit, connector change, Publisher Tag enablement, production traffic, or bulk catalog download.

## 1. Why this test exists

Determine whether the Edmunds product catalog can safely support a small, complementary website utility that returns a few current listings by broad vehicle criteria and sends a user onward through the unchanged Impact tracking URL.

This is **not a VIN-search test**. Prior work already established that VIN/MPN cannot be queried or filtered through the catalog interface. Do not repeat that experiment and do not download the full catalog to work around it.

The decision needed after C1–C8 is narrow:

1. Which filters work server-side?
2. Are New and Used distinguishable reliably?
3. Which useful fields are returned and sufficiently complete?
4. What happens when a query is thin?
5. What pagination ceiling and request limits are observable without load testing?
6. Does the returned tracked URL resolve to an appropriate Edmunds page?
7. Can the result honestly be described without implying local/radius completeness?

## 2. Historical record — do not merge these separate tests

### A. September 3: VIN-to-Edmunds browser experiment

Source: `HANDOFF_EDMUNDS_VIN_SEARCH_EXPERIMENT_20260903.md`.

This was **not an Impact Catalog API test**. It tested constructed CJ-wrapped Edmunds listing URLs and targeted Google discovery for 24 known VINs across Southern California, New York/New Jersey, and Chicago.

Observed outcome:

- 12/24 opened an exact listing.
- 10/24 opened an unavailable-listing page with an Edmunds similar-vehicle grid.
- 2/24 opened an unavailable-listing page without a useful grid.

That experiment established behavior of direct listing destinations, not catalog VIN search capability. Its old CJ mechanism and Google-search fallback must not be revived for C1–C8.

### B. September 16: Impact Catalog VIN/MPN investigation

Source: `STRATEGY_IMPACT_WEBSITE_PUBLISHER_TAG_ASSETS_CATALOG_20260916.md`.

Live account testing plus Impact support ticket **#882346** established:

- The Edmunds catalog was approximately 1.2–1.334 million records.
- VIN/MPN was present in records but could not be searched or filtered.
- Impact support recommended downloading the entire catalog as the workaround.
- That workaround was deliberately rejected for GetCarWise's narrow use case.
- General fields were searchable:
  - dealer name through `Manufacturer` — a misleading feed-specific mapping;
  - model through `Text1`;
  - body style through `Category`.
- Returned records appeared to include current price/stock, image, dealer information/address, year/model/trim, and a pre-tracked affiliate URL.
- Prior account observations indicated a 20,000-result traversal ceiling and 3,600 requests/hour, but both need a fresh, non-destructive confirmation.
- No true vehicle-level ZIP, radius, or distance filter was confirmed.

The support recommendation to download the full feed was a workaround for unsupported VIN lookup. It was **not** a requirement for ordinary catalog reads.

### C. Current test: C1–C8 general catalogue feasibility

C1–C8 tests broad model, condition, category, price, dealer, sparse-result, pagination/rate behavior, and returned URL quality. It must not search by VIN or represent the catalog as a local inventory engine.

## 3. Preconditions and stop conditions

Before starting:

- Use the existing Impact Media Partner account and credentials already stored in the approved secure environment.
- Do not paste credentials, AccountSID, secret values, full authorization headers, or raw tracked URLs into chat, GitHub, screenshots, or the return document.
- Confirm the Edmunds catalog ID through an authenticated list-catalogs call. Redact the ID in the report.
- Use the production Impact API only for read requests.
- Default to one request at a time and `PageSize=10` unless a test below explicitly says otherwise.
- Record timestamps in UTC.
- Do not submit a form, create a lead, call a dealer, or provide personal information.
- Do not request or download a bulk export.

Stop immediately and report the blocker if:

- authentication cannot be completed without exposing a secret;
- Cloudflare or another human-verification challenge blocks access;
- a request would require changing account settings;
- the account/catalog identity cannot be confirmed;
- the API response suggests the wrong advertiser/catalog;
- repeated 401, 403, 429, or 5xx responses occur;
- continuing would require enumerating large portions of the catalog;
- any step appears capable of creating a lead or other user record.

C8 permits at most one controlled open of a returned tracking URL. If that open would materially distort affiliate reporting or the operator is uncertain, record C8 as blocked pending André's confirmation rather than clicking it.

## 4. Relevant endpoints

Use the authenticated Impact API host and the documented version/headers already accepted by the account. The known endpoint shapes are:

```text
GET https://api.impact.com/Mediapartners/{AccountSID}/Catalogs
GET https://api.impact.com/Mediapartners/{AccountSID}/Catalogs/{CatalogId}
GET https://api.impact.com/Mediapartners/{AccountSID}/Catalogs/{CatalogId}/Items?Query={encoded_expression}
GET https://api.impact.com/Mediapartners/{AccountSID}/Catalogs/ItemSearch?Keyword={encoded_keyword}&PageSize={n}&Page={n}
```

Use the account's documented authentication method. In evidence, replace sensitive path/query values with `[REDACTED]`.

Do not assume a query operator. First recover the exact field-query syntax from either:

1. a previously successful request in the authenticated environment; or
2. the current official Impact API documentation available to the account.

Known examples support expressions such as `CurrentPrice > 50` and `Manufacturer == 'Wayne Enterprises'`, but model-string matching and Boolean composition must be verified rather than guessed. URL-encode the complete expression exactly once.

If a field-specific expression is rejected, capture the sanitized error and use `ItemSearch?Keyword=` only where the test permits it. Do not silently treat keyword search as proof of a field-specific filter.

## 5. Discovery preflight D0

D0 is required before C1.

1. Call list catalogs.
2. Identify the Edmunds catalog by returned name/advertiser metadata.
3. Fetch catalog metadata.
4. Fetch one page of 10 items with the least restrictive safe read.
5. Build a field map from the actual response.

For the ten-item sample, record completeness counts for:

- item identifier;
- `Text1` or equivalent model field;
- `Category`;
- `Manufacturer`;
- condition/status;
- year, make, model, trim;
- `CurrentPrice`;
- stock/availability indicator;
- dealer name and city/state;
- ZIP if returned;
- image URL;
- tracked destination URL;
- last-updated or freshness field.

Do not publish raw item payloads. A redacted sample may retain non-sensitive make/model/year/price/category/condition and state, but remove VIN/MPN, exact street address, item IDs, account/catalog IDs, and full tracked URLs.

D0 passes if the Edmunds catalog is positively identified and at least one item page can be read. Otherwise stop; C1–C8 are blocked.

## 6. C1–C8 execution matrix

### C1 — Model discovery: Honda CR-V

**Question:** Can a common model be found predictably, and does `Text1` behave as the prior test indicated?

Procedure:

1. Run a field-specific model query against `Text1` using the account-verified string operator.
2. Request page 1, size 10.
3. Separately run `ItemSearch` with keyword `CR-V`, page 1, size 10.
4. Compare counts and the first ten records.
5. Manually classify every returned item as exact CR-V, related Honda, or false positive.

Pass:

- At least 8/10 sampled results are Honda CR-V records.
- The accepted query syntax and whether matching is exact/contains/tokenized are known.
- Any count difference between field query and keyword search is explained.

Fail/block:

- Model filtering is rejected, overwhelmingly noisy, or only possible through an unbounded client-side scan.

### C2 — Condition split: Mitsubishi Outlander PHEV

**Question:** Can New and Used be separated reliably?

Procedure:

1. Find Outlander PHEV using the successful C1 mechanism.
2. Attempt server-side `Condition == New` combined with the model expression.
3. Repeat for `Condition == Used`.
4. If `Condition` is absent or rejected, fetch a single bounded page of 20 Outlander PHEV results and calculate the condition split from returned fields.
5. Record all distinct condition values exactly as returned, including CPO/unknown variants.

Pass:

- Server-side New/Used filtering works and the ten-result samples contain no contradictory condition values; or
- a bounded response exposes a stable condition field that can safely be split after retrieval, with the limitation documented.

Fail:

- Condition is missing, contradictory, or inferable only from unreliable text.

### C3 — Category plus price: SUV under $30,000 and $25,000

**Question:** Can the catalogue produce a bounded affordable-SUV candidate set?

Procedure:

1. Query `Category` for SUV plus `CurrentPrice <= 30000`.
2. Request page 1, size 10.
3. Repeat with `CurrentPrice <= 25000`.
4. Validate every sampled result:
   - category represents an SUV/crossover;
   - numeric price is present;
   - price is at or below the requested ceiling;
   - currency is USD or clearly identified;
   - no lease/monthly-payment value is masquerading as purchase price.
5. Record total-count metadata if returned.

Pass:

- 10/10 sampled records satisfy the price ceiling.
- At least 8/10 satisfy the intended SUV/crossover category.
- The API performs the price filter server-side.

Fail:

- Prices breach the ceiling, pricing semantics are ambiguous, or category noise makes the result unsafe to describe as SUVs.

### C4 — Dealer filter through `Manufacturer`

**Question:** Does the feed-specific dealer mapping still work?

Procedure:

1. Select one dealer name from a C1–C3 returned item.
2. Query `Manufacturer` using the exact returned dealer string.
3. Request page 1, size 10.
4. Compare the returned `Manufacturer` value and dealer display fields.
5. If exact equality returns zero, try only the documented supported case-insensitive/string operator once.

Pass:

- At least 9/10 returned records belong to the selected dealer.
- The report explicitly says that `Manufacturer` is a feed mapping, not the vehicle make.

Fail:

- Results mix dealers materially or the field cannot be queried.

### C5 — Thin-result and zero-result behavior

**Question:** Does the API fail safely when inventory is sparse?

Procedure:

1. Query `RAV4 Prime` with `CurrentPrice <= 25000`.
2. Record count, latency, response shape, and any spelling/model broadening.
3. Run one deliberately rarer but legitimate combination chosen from observed fields, such as the same model with a lower price or restrictive condition.
4. Stop after these two requests; do not keep tightening until an error occurs.

Pass:

- Zero/thin responses are explicit and structurally valid.
- The API does not silently substitute unrelated models.
- The product can distinguish “no matching catalog items” from an API failure.

Fail:

- The API broadens invisibly, returns materially unrelated inventory, or produces an ambiguous error/empty state.

### C6 — Pagination and 20,000 traversal ceiling

**Question:** What can be confirmed without enumerating the catalog?

Procedure:

1. Use a broad query known to exceed 20,000 results.
2. Record total-count and pagination metadata from page 1, size 20.
3. If direct page access is supported, request only:
   - the last page whose starting offset remains below 20,000; and
   - the immediately following page.
4. Do not traverse intermediate pages.
5. If the API does not allow a direct high-page request, stop after metadata and mark the boundary as not independently reconfirmed.
6. Record whether the response rejects, caps, empties, or serves the beyond-boundary request.

Pass:

- The observed ceiling and behavior are documented with no bulk enumeration.

This is an evidence test, not a requirement that high-page access succeed. Never download 20,000 records to prove the ceiling.

### C7 — Rate headers and resilience

**Question:** What operational signals are visible under tiny, safe request volume?

Procedure:

1. Make five serial identical lightweight requests, waiting for each response.
2. Record status, latency, and rate-related headers for each.
3. If all five succeed, make at most five additional requests with concurrency capped at two.
4. Stop at ten total C7 requests.
5. Do not attempt to trigger 429 and do not approach the previously observed 3,600/hour allowance.
6. If a transient 429/5xx occurs naturally, honor `Retry-After` once, then stop and report.

Pass:

- Median and slowest latency are known.
- Any limit/remaining/reset/retry headers are documented.
- The response to a naturally occurring transient failure is understood.

“No rate headers observed” is a valid finding, not a reason to load-test.

### C8 — Returned tracked URL and landing behavior

**Question:** Does a returned catalog URL preserve tracking and land on an appropriate Edmunds destination?

Procedure:

1. Choose one ordinary item from C1–C4 with a returned tracked URL.
2. Validate the URL structurally without logging it:
   - HTTPS;
   - expected Impact/Edmunds host chain;
   - no obvious malformed or missing destination;
   - no modification to parameters.
3. If authorized for the controlled click, open it once in a clean browser context.
4. Record only:
   - redirect hop hostnames, not full URLs/query strings;
   - final hostname;
   - HTTP/landing outcome;
   - exact listing, unavailable/similar-listings page, generic SRP, or mismatch;
   - whether Impact reporting shows the controlled click, if that can be checked read-only without creating further traffic.
5. Do not submit any lead form or enter any personal information.

Pass:

- The unchanged returned URL resolves through the expected tracking path to Edmunds.
- The landing page is the expected listing or an honest Edmunds unavailable/similar fallback.
- No domain or vehicle mismatch is observed.

Fail:

- Broken redirect, wrong domain, unrelated vehicle, stripped tracking, unsafe destination, or required form submission.

## 7. Evidence ledger

Create one row per request. Use this schema:

| Field | Required content |
|---|---|
| Test ID | D0, C1a, C1b, etc. |
| UTC timestamp | ISO 8601 |
| Endpoint class | Catalogs, Items, or ItemSearch; redact IDs |
| Sanitized query | No AccountSID, catalog ID, VIN, MPN, or tracked URL |
| Page / size | Numeric |
| HTTP status | Numeric |
| Latency ms | End-to-end |
| Count metadata | Page count/total if returned |
| Rate headers | Names and sanitized numeric values |
| Sample validity | e.g. 9/10 exact |
| Field completeness | counts out of sample size |
| Duplicates | count and comparison key, without exposing VIN |
| URL outcome | not tested / exact / unavailable+similar / generic / mismatch |
| Freshness | returned timestamp/age if present |
| Error/fallback | exact sanitized error and action |
| Verdict | pass / qualified pass / fail / blocked |

Also calculate:

- median and maximum latency by test;
- duplicate rate in each sample;
- missing-value rate for price, condition, image, dealer, location, and tracked URL;
- false-positive rate for model/category/dealer filters;
- count of dead or mismatched landing pages;
- count of records with a usable freshness indicator.

Do not put VIN, email, phone, street address, ZIP, AccountSID, credentials, authorization headers, item IDs, catalog IDs, or raw tracked URLs into GA4, chat, or the repository. State and city may be reported in aggregate; omit a record-level ZIP even if returned.

## 8. Interpretation rules

- Catalog presence is not proof of exhaustive market coverage.
- Do not say “near you,” “within X miles,” or “all local inventory” because no vehicle-level ZIP/radius filter has been confirmed.
- Dealer address fields may support a disclosed dealer-location label; they do not prove distance from the user.
- A client-side New/Used split is acceptable only if the returned condition field is stable and the fetched candidate set is tightly bounded.
- `Manufacturer` must be described internally as the dealer-name field for this feed, never as the vehicle manufacturer.
- Do not let catalog availability choose editorial recommendations. The utility is complementary to the evidence-led page.
- A future interface should normally show only 3–6 cards, disclose that availability can change, preserve returned Edmunds/Impact links unchanged, and avoid local-completeness claims.
- Do not infer that the prior 3,600/hour observation is a guaranteed quota.
- Do not infer freshness from “in stock” alone; use returned timestamps or catalog update metadata where available.

## 9. Required return document

Write:

`RETURN_IMPACT_CATALOG_C1_C8_READ_ONLY_TESTS_20260920.md`

If run on a later date, keep the requested filename but put the actual execution date and UTC window inside it.

Required sections:

1. Executive verdict: feasible / feasible with constraints / not feasible / blocked.
2. Historical clarification: September 3 VIN URL test vs. September 16 Catalog VIN limitation vs. current C1–C8.
3. Authenticated environment and catalog identity, sanitized.
4. D0 field map and completeness.
5. C1–C8 results table.
6. Full sanitized request ledger.
7. Latency, pagination, and rate observations.
8. Tracked-URL outcome.
9. Geography and freshness limitations.
10. Security/privacy confirmation.
11. Exact blockers or uncertainties.
12. Recommendation:
    - stop;
    - rerun one named test;
    - proceed to a private/noindex fixture prototype; or
    - proceed to a separately authorized controlled pilot.
13. Explicit confirmation that no code, WordPress, deployment, Publisher Tag, public module, bulk download, lead submission, or production change occurred.

## 10. Completion gate

C1–C8 closes Task #65's evidence gate only if:

- D0 and C1–C5 complete;
- condition and price behavior are known;
- pagination behavior is documented without bulk traversal;
- C7 remains bounded to ten requests;
- C8 is completed or clearly marked blocked for controlled-click authorization;
- the no-ZIP/radius limitation remains explicit;
- the return contains no secrets or prohibited identifiers.

Even a successful run does **not** authorize implementation. A prototype or pilot requires a separate André/ChatGPT decision after review of the return.
