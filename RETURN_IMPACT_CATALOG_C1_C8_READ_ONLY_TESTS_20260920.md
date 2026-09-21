# Return — Impact Catalog C1–C8 Read-Only API Tests

**Task:** #65 — Impact Product Catalog Website Utility Audit + location test  
**Final outcome:** **COMPLETE — feasible with material constraints**  
**Successful execution:** 2026-09-21, 08:23:37–08:23:51 UTC  
**Evidence source:** André’s bounded local Python run using the existing read-only Impact credentials  
**Supersedes:** the earlier same-filename return that stopped at D0 because Claude’s authenticated browser session collided with direct API authentication

## 1. Executive verdict

The Edmunds Product Feed is technically suitable for a small, complementary inventory-continuation module. It is not suitable as a comprehensive local inventory engine, a VIN-search engine, or a reliable New/Used classifier.

The successful run established:

- one accessible Edmunds catalog with 1,352,716 reported items;
- exact server-side model filtering through `Text1`;
- combined category and maximum-price filtering;
- exact dealer filtering through the feed-specific `Manufacturer` mapping;
- safe thin and empty-result behavior;
- a hard 20,000-item result-window boundary;
- stable bounded request behavior and a 3,000 item-requests/hour observed header limit;
- structurally valid partner-specific `edmunds.sjv.io` tracking URLs.

The key negative finding is decisive: `Condition` is absent in the sampled records and rejected as an unknown search field. The module must not label results New, Used or CPO from this feed alone. NHTSA cannot repair that gap because VIN decoding identifies manufacturer-reported vehicle specifications, not sale condition, ownership or title history.

## 2. Historical reconciliation

The earlier Claude attempt remains useful evidence about the dashboard/browser session collision and the disabled `ItemSearch` token scope. It is not evidence that the API itself was unavailable. André’s separate local Python client authenticated successfully and completed the bounded matrix without exposing credentials.

This final return keeps three prior efforts distinct:

1. the September 3 constructed-URL browser test;
2. the September 16 VIN/MPN Catalog investigation and Impact support ticket #882346;
3. this successful C1–C8 general inventory-feasibility run.

No VIN lookup and no bulk catalog download were attempted.

## 3. Decision by capability

| Capability | Decision |
|---|---|
| Model discovery | Approved for prototype, using allowlisted exact model tokens and validation |
| Body style + price ceiling | Approved for prototype, with taxonomy validation and no completeness claim |
| Dealer filtering | Technically viable, but document `Manufacturer` as a feed-specific dealer mapping |
| New/Used/CPO split | **Not supported**; do not infer or display condition |
| ZIP/radius/nearest inventory | **Not supported**; dealer location is not a radius engine |
| VIN Catalog search | **Not supported** and must not be retried |
| NHTSA enrichment | Optional after a valid VIN is already present; never a condition classifier |
| Returned tracking URL | Approved structurally for a private prototype; preserve unchanged |
| Public production module | Not authorized by this evidence run |

## 4. NHTSA boundary

NHTSA vPIC is manufacturer-reported VIN decoding data. Where a returned record contains a valid VIN in an approved server-side field, a later prototype may use NHTSA to validate or enrich:

- model year, make and model;
- body class;
- engine/fuel/electrification clues when returned;
- plant/manufacturer identity;
- inputs needed for separate NHTSA recall-context calls.

It must not be used to claim:

- New, Used or CPO status;
- ownership count;
- title, accident, odometer or service history;
- current sale availability;
- dealer proximity.

VIN must remain server-side, must not be logged or sent to analytics, and NHTSA failure must not break the Catalog fallback.

## 5. Revised prototype recommendation

Proceed only to a separately implemented private/noindex prototype with:

- model or body-style plus price inputs;
- no condition control and no condition label;
- 3–6 neutral “Current Edmunds listings” cards;
- unchanged returned Impact URLs;
- an explicit complementary-feed and changing-availability disclosure;
- separate validated static New and Used CTAs chosen by the host page’s editorial intent;
- optional Trade-in only where replacement intent is present;
- no ZIP/radius or “near you” claim;
- fast static fallback, kill switch, redacted logs and no Publisher Tag.

The prior `RETURN_TOOL_LED_IMPACT_FUNNEL_FEASIBILITY_20260920.md` specification must therefore be read with this correction: remove its user-selectable condition control and all assumptions that `Condition` is returned.

## 6. Security and scope confirmation

The successful run made 20 bounded GET requests. It saved no credentials, AccountSID, catalog ID, item ID, VIN/MPN, street address, dealer name or raw tracking URL. It opened no affiliate link, submitted no lead, downloaded no bulk feed, made no code or WordPress change and created no public module.

## 7. Exact sanitized runner output

The following appendix is the complete sanitized Markdown emitted by the corrected runner. It is retained verbatim as the request ledger and machine-readable result evidence.



# Impact Catalog C1-C8 — Sanitized Local Results

- Started: 2026-09-21T08:23:37+00:00
- Finished: 2026-09-21T08:23:51+00:00
- Requests: 20 bounded GET requests
- Credentials, IDs, VIN/MPN, addresses and raw tracking URLs: not saved
- Affiliate links opened: no

## Test summaries

### D0

```json
{
  "verdict": "pass",
  "catalog_name": "Edmunds Product Feed",
  "catalog_count": 1,
  "reported_number_of_items": "1352716",
  "date_last_updated": "2026-09-21T14:48:18+10:00",
  "currency": "USD",
  "sample_size": 10,
  "field_completeness": {
    "item_identifier": "10/10",
    "model_Text1": "10/10",
    "category": "10/10",
    "dealer_Manufacturer": "10/10",
    "condition": "0/10",
    "year": "10/10",
    "make": "10/10",
    "trim": "10/10",
    "price": "10/10",
    "stock": "10/10",
    "dealer_location": "10/10",
    "image": "10/10",
    "tracked_url": "10/10",
    "freshness": "0/10"
  },
  "duplicates": 0
}
```

### C1

```json
{
  "verdict": "pass",
  "field_query_returned": 10,
  "field_query_exact_crv": 10,
  "field_query_total": 20875,
  "keyword_search_status": "not rerun",
  "keyword_search_returned": null,
  "keyword_search_total": null,
  "keyword_scope_note": "Known token scope limitation: the prior bounded run returned HTTP 403, so this corrected run does not repeat that request.",
  "duplicates": 0
}
```

### C2

```json
{
  "verdict": "qualified/fail",
  "server_side": {
    "New": {
      "status": 400,
      "returned": 0,
      "total": null,
      "condition_values": {},
      "contradictory": 0
    },
    "Used": {
      "status": 400,
      "returned": 0,
      "total": null,
      "condition_values": {},
      "contradictory": 0
    }
  },
  "bounded_fallback": {
    "status": 200,
    "returned": 20,
    "total": 384,
    "condition_values": {
      "[missing]": 20
    }
  }
}
```

### C3

```json
{
  "verdict": "pass",
  "observed_category_value_redacted": "used exactly as returned; value omitted from report",
  "ceilings": {
    "30000": {
      "status": 200,
      "returned": 10,
      "total": 106739,
      "price_at_or_below_ceiling": 10,
      "category_matches_observed_value": 10,
      "missing_or_unparseable_price": 0
    },
    "25000": {
      "status": 200,
      "returned": 10,
      "total": 64321,
      "price_at_or_below_ceiling": 10,
      "category_matches_observed_value": 10,
      "missing_or_unparseable_price": 0
    }
  }
}
```

### C4

```json
{
  "verdict": "pass",
  "returned": 10,
  "total": 301,
  "same_dealer": 10,
  "dealer_name_saved": false
}
```

### C5

```json
{
  "verdict": "pass",
  "cases": [
    {
      "case": "thin",
      "status": 200,
      "returned": 5,
      "total": 5,
      "related_rav4_prime": 5,
      "structurally_valid_empty": false
    },
    {
      "case": "rarer",
      "status": 200,
      "returned": 0,
      "total": -1,
      "related_rav4_prime": 0,
      "structurally_valid_empty": true
    }
  ]
}
```

### C6

```json
{
  "page1_status": 200,
  "page1_returned": 20,
  "reported_total": 1352716,
  "boundary_requests_made": true,
  "page1000_status": 200,
  "page1000_returned": 20,
  "page1001_status": 400,
  "page1001_returned": 0,
  "beyond_boundary_error": "{\n  \"Status\": \"ERROR\",\n  \"Message\": \"Request exceeds the maximum results window of 20000. Please adjust the Page and PageSize parameters.\"\n}"
}
```

### C7

```json
{
  "request_count": 5,
  "statuses": [
    200,
    200,
    200,
    200,
    200
  ],
  "median_latency_ms": 376,
  "maximum_latency_ms": 492,
  "rate_header_names": [
    "x-ratelimit-limit",
    "x-ratelimit-limit-hour",
    "x-ratelimit-remaining",
    "x-ratelimit-remaining-hour",
    "x-ratelimit-reset"
  ],
  "load_test_performed": false
}
```

### C8

```json
{
  "verdict": "qualified structural pass",
  "scheme": "https",
  "hostname": "edmunds.sjv.io",
  "expected_host_family": true,
  "has_query_string": true,
  "raw_url_saved": false,
  "url_opened": false,
  "landing_behavior": "not tested; controlled click deliberately left blocked for separate authorization"
}
```

## Sanitized request ledger

```json
[
  {
    "test_id": "D0-catalogs",
    "utc_timestamp": "2026-09-21T08:23:37+00:00",
    "endpoint_class": "Catalog list",
    "sanitized_query": "none",
    "page": null,
    "page_size": null,
    "http_status": 200,
    "latency_ms": 1505,
    "returned_count": 0,
    "total_count": 1,
    "rate_headers": {
      "x-ratelimit-limit-hour": "1000",
      "x-ratelimit-remaining-hour": "997",
      "x-ratelimit-limit": "1000",
      "x-ratelimit-remaining": "997",
      "x-ratelimit-reset": "2181"
    },
    "error": ""
  },
  {
    "test_id": "D0-metadata",
    "utc_timestamp": "2026-09-21T08:23:38+00:00",
    "endpoint_class": "Catalog metadata",
    "sanitized_query": "none",
    "page": null,
    "page_size": null,
    "http_status": 200,
    "latency_ms": 582,
    "returned_count": 0,
    "total_count": null,
    "rate_headers": {
      "x-ratelimit-limit-hour": "1000",
      "x-ratelimit-remaining-hour": "997",
      "x-ratelimit-limit": "1000",
      "x-ratelimit-remaining": "997",
      "x-ratelimit-reset": "2180"
    },
    "error": ""
  },
  {
    "test_id": "D0-sample",
    "utc_timestamp": "2026-09-21T08:23:39+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "least restrictive safe read",
    "page": 1,
    "page_size": 10,
    "http_status": 200,
    "latency_ms": 545,
    "returned_count": 10,
    "total_count": 1352716,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2981",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2981",
      "x-ratelimit-reset": "2180"
    },
    "error": ""
  },
  {
    "test_id": "C1-field",
    "utc_timestamp": "2026-09-21T08:23:39+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "Text1 = 'CR-V'",
    "page": 1,
    "page_size": 10,
    "http_status": 200,
    "latency_ms": 448,
    "returned_count": 10,
    "total_count": 20875,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2981",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2981",
      "x-ratelimit-reset": "2179"
    },
    "error": ""
  },
  {
    "test_id": "C2-new",
    "utc_timestamp": "2026-09-21T08:23:40+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "Text1 = 'Outlander PHEV' AND Condition = 'New'",
    "page": 1,
    "page_size": 10,
    "http_status": 400,
    "latency_ms": 310,
    "returned_count": 0,
    "total_count": null,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2981",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2981",
      "x-ratelimit-reset": "2179"
    },
    "error": "{\n  \"Status\": \"ERROR\",\n  \"Message\": \"Unknown search field name: Condition\"\n}"
  },
  {
    "test_id": "C2-used",
    "utc_timestamp": "2026-09-21T08:23:40+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "Text1 = 'Outlander PHEV' AND Condition = 'Used'",
    "page": 1,
    "page_size": 10,
    "http_status": 400,
    "latency_ms": 298,
    "returned_count": 0,
    "total_count": null,
    "rate_headers": {
      "x-ratelimit-remaining-hour": "2981",
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2981",
      "x-ratelimit-reset": "2178"
    },
    "error": "{\n  \"Status\": \"ERROR\",\n  \"Message\": \"Unknown search field name: Condition\"\n}"
  },
  {
    "test_id": "C2-bounded-fallback",
    "utc_timestamp": "2026-09-21T08:23:40+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "Text1 = 'Outlander PHEV' (bounded fallback)",
    "page": 1,
    "page_size": 20,
    "http_status": 200,
    "latency_ms": 495,
    "returned_count": 20,
    "total_count": 384,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2979",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2979",
      "x-ratelimit-reset": "2178"
    },
    "error": ""
  },
  {
    "test_id": "C3-30000",
    "utc_timestamp": "2026-09-21T08:23:41+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "Category = [observed CR-V category] AND CurrentPrice <= 30000",
    "page": 1,
    "page_size": 10,
    "http_status": 200,
    "latency_ms": 564,
    "returned_count": 10,
    "total_count": 106739,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2978",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2978",
      "x-ratelimit-reset": "2177"
    },
    "error": ""
  },
  {
    "test_id": "C3-25000",
    "utc_timestamp": "2026-09-21T08:23:41+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "Category = [observed CR-V category] AND CurrentPrice <= 25000",
    "page": 1,
    "page_size": 10,
    "http_status": 200,
    "latency_ms": 2213,
    "returned_count": 10,
    "total_count": 64321,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2975",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2975",
      "x-ratelimit-reset": "2177"
    },
    "error": ""
  },
  {
    "test_id": "C4-dealer",
    "utc_timestamp": "2026-09-21T08:23:44+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "Manufacturer = [REDACTED_DEALER_NAME]",
    "page": 1,
    "page_size": 10,
    "http_status": 200,
    "latency_ms": 1903,
    "returned_count": 10,
    "total_count": 301,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2974",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2974",
      "x-ratelimit-reset": "2175"
    },
    "error": ""
  },
  {
    "test_id": "C5-thin",
    "utc_timestamp": "2026-09-21T08:23:46+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "RAV4 Prime AND CurrentPrice <= 25000",
    "page": 1,
    "page_size": 10,
    "http_status": 200,
    "latency_ms": 525,
    "returned_count": 5,
    "total_count": 5,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2973",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2973",
      "x-ratelimit-reset": "2173"
    },
    "error": ""
  },
  {
    "test_id": "C5-rarer",
    "utc_timestamp": "2026-09-21T08:23:46+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "RAV4 Prime AND CurrentPrice <= 15000",
    "page": 1,
    "page_size": 10,
    "http_status": 200,
    "latency_ms": 440,
    "returned_count": 0,
    "total_count": -1,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2973",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2973",
      "x-ratelimit-reset": "2172"
    },
    "error": ""
  },
  {
    "test_id": "C6-broad-page1",
    "utc_timestamp": "2026-09-21T08:23:47+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "CurrentPrice > 0",
    "page": 1,
    "page_size": 20,
    "http_status": 200,
    "latency_ms": 924,
    "returned_count": 20,
    "total_count": 1352716,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2972",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2972",
      "x-ratelimit-reset": "2172"
    },
    "error": ""
  },
  {
    "test_id": "C6-page1000",
    "utc_timestamp": "2026-09-21T08:23:47+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "CurrentPrice > 0; last 20-item page starting below 20,000",
    "page": 1000,
    "page_size": 20,
    "http_status": 200,
    "latency_ms": 1021,
    "returned_count": 20,
    "total_count": 1352716,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2972",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2972",
      "x-ratelimit-reset": "2171"
    },
    "error": ""
  },
  {
    "test_id": "C6-page1001",
    "utc_timestamp": "2026-09-21T08:23:48+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "CurrentPrice > 0; first 20-item page starting at 20,000",
    "page": 1001,
    "page_size": 20,
    "http_status": 400,
    "latency_ms": 389,
    "returned_count": 0,
    "total_count": null,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2970",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2970",
      "x-ratelimit-reset": "2170"
    },
    "error": "{\n  \"Status\": \"ERROR\",\n  \"Message\": \"Request exceeds the maximum results window of 20000. Please adjust the Page and PageSize parameters.\"\n}"
  },
  {
    "test_id": "C7-1",
    "utc_timestamp": "2026-09-21T08:23:49+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "CurrentPrice > 0; lightweight serial check",
    "page": 1,
    "page_size": 1,
    "http_status": 200,
    "latency_ms": 365,
    "returned_count": 1,
    "total_count": 1352716,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2970",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2970",
      "x-ratelimit-reset": "2169"
    },
    "error": ""
  },
  {
    "test_id": "C7-2",
    "utc_timestamp": "2026-09-21T08:23:49+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "CurrentPrice > 0; lightweight serial check",
    "page": 1,
    "page_size": 1,
    "http_status": 200,
    "latency_ms": 402,
    "returned_count": 1,
    "total_count": 1352716,
    "rate_headers": {
      "x-ratelimit-remaining-hour": "2970",
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2970",
      "x-ratelimit-reset": "2169"
    },
    "error": ""
  },
  {
    "test_id": "C7-3",
    "utc_timestamp": "2026-09-21T08:23:50+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "CurrentPrice > 0; lightweight serial check",
    "page": 1,
    "page_size": 1,
    "http_status": 200,
    "latency_ms": 492,
    "returned_count": 1,
    "total_count": 1352716,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2969",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2969",
      "x-ratelimit-reset": "2169"
    },
    "error": ""
  },
  {
    "test_id": "C7-4",
    "utc_timestamp": "2026-09-21T08:23:50+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "CurrentPrice > 0; lightweight serial check",
    "page": 1,
    "page_size": 1,
    "http_status": 200,
    "latency_ms": 376,
    "returned_count": 1,
    "total_count": 1352716,
    "rate_headers": {
      "x-ratelimit-remaining-hour": "2967",
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2967",
      "x-ratelimit-reset": "2168"
    },
    "error": ""
  },
  {
    "test_id": "C7-5",
    "utc_timestamp": "2026-09-21T08:23:50+00:00",
    "endpoint_class": "Catalog items",
    "sanitized_query": "CurrentPrice > 0; lightweight serial check",
    "page": 1,
    "page_size": 1,
    "http_status": 200,
    "latency_ms": 346,
    "returned_count": 1,
    "total_count": 1352716,
    "rate_headers": {
      "x-ratelimit-limit-hour": "3000",
      "x-ratelimit-remaining-hour": "2965",
      "x-ratelimit-limit": "3000",
      "x-ratelimit-remaining": "2965",
      "x-ratelimit-reset": "2168"
    },
    "error": ""
  }
]
```
