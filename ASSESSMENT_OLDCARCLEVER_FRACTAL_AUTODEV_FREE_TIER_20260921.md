# Assessment — Old CarClever / Fractal: Auto.dev Free-Tier Downshift

**Date:** 2026-09-21  
**Status:** proposed operating decision; no platform, code, plan, submission or deployment change made  
**Scope:** old CarClever hosted on Fractal only. This does not change the primary Vercel-based CarClever – Find My Car product.

## Bottom line

Auto.dev Free is a sensible **standby/decommissioning tier** for old CarClever, not a like-for-like production substitute.

It preserves the core used-car discovery experience—listings, photos and VIN decode—while deliberately downgrading detailed specification, VIN-specific recall, lender/payment and total-cost claims. That is strategically acceptable only if old CarClever is retained as a low-traffic legacy surface rather than developed as a second flagship alongside Find My Car.

The suggested downgrade must not be treated as “zero work.” The reported capability guard is promising, but there is one reported unguarded Growth request (Specifications) and two material facts still require evidence before a plan change:

1. actual Auto.dev call volume by endpoint and cold start; and
2. whether failed/blocked Growth requests count toward the Free plan's 1,000-call cap.

No decision to downgrade, unpublish or retire Fractal is recorded by this assessment.

## Current verified Auto.dev plan boundary

Auto.dev’s current public pricing states that Free provides 1,000 API calls per month at five requests per second, then requests stop at the cap. It includes Global VIN Decode, Vehicle Listings and Vehicle Photos. Specifications, Vehicle Recalls, Total Cost of Ownership, Vehicle Payments and Interest Rates are Growth-only. Growth is currently listed at US$299/month plus data fees.

Source: https://www.auto.dev/pricing (checked 2026-09-21).

This confirms the report's core plan classification. It does **not** independently prove the Fractal code's exact endpoint usage or fallback behavior.

## Assessment of the Fractal code-agent report

| Reported claim | Assessment | Decision consequence |
|---|---|---|
| Search uses listings only | Plausible and aligned with the Free plan. | Core search can remain. |
| Listings, photos and VIN decode remain available | Confirmed by the current Free plan. | Basic cards can remain. |
| Specs, recalls, APR, payments and TCO are Growth-only | Confirmed by the current Free plan. | Detailed vehicle facts and “real” financial outputs cannot be represented as live provider data. |
| Existing capability guards prevent user-facing 402 errors | Not independently code-verified; credible only as a reported implementation detail. | Must be regression-tested after downgrade. |
| No code changes required | **Not accepted.** The report itself identifies an unguarded Specs request. | A small Free-readiness maintenance change is required before relying on Free long term. |
| NHTSA recall fallback is adequate | Appropriate only when visibly labelled as model-level, not VIN-specific. | Keep the disclosure; do not overstate it. |
| vPIC can fully replace the Specs layer | Overstated. vPIC may enrich identity/powertrain facts, but is not a dependable replacement for all equipment, warranty, dimensional, range or safety-feature data. | Treat as a later optional enrichment project, not a prerequisite or substitute. |
| FRED series DTCTHFNM supplies auto-loan rates | **Incorrect.** It is “Total Consumer Loans and Leases Owned and Securitized by Finance Companies, Level,” not an auto-loan-rate series. | Do not implement this workaround. Retain clearly labelled estimate tables unless a separately validated rate source is approved. |

The FRED correction is based on the Federal Reserve Bank of St. Louis series page checked 2026-09-21: https://fred.stlouisfed.org/series/DTCTHFNM.

## User-visible impact

| Function | Free-tier result | Required wording/guardrail |
|---|---|---|
| Used-car search | Retained, subject to the 1,000-call shared cap. | No change in scope; avoid promising exhaustiveness. |
| Listing photos/basic card facts | Retained when available in listings/photos. | Missing fields remain unknown, not inferred. |
| Vehicle details | Core listing identity, price, mileage, dealer and supplied history fields remain; rich specs, warranty and safety-equipment detail can disappear. | Omit unavailable sections rather than display blanks or assumed values. |
| Deal/risk analysis | Listing-based flags and local logic can remain; recall result becomes NHTSA model-level fallback. | State “model-level recall check” wherever Auto.dev VIN recall is absent. |
| Affordability | Payment, out-the-door and five-year ownership figures become estimates based on local assumptions. | Never label these as lender/API/real market calculations; preserve an obvious estimate disclosure. |
| Advanced safety/specification comparisons | No reliable replacement in the proposed scope. | Do not add a pseudo-specs layer just to restore card density. |

## The real Free-tier risk: call budget

The Free allowance is a single shared 1,000-call monthly cap, not 1,000 calls per endpoint. Auto.dev says requests stop once that cap is reached.

The supplied report says four Growth-endpoint probes run at server startup and that Specs is not presently part of that guard. If Fractal's runtime restarts or cold-starts often, those probes and failed Specs calls could consume a meaningful share of the quota. The report does not establish whether 402 responses are counted, nor the lifecycle of the in-memory capability cache. Those are blocking facts for a safe downgrade.

The old app has already been positioned as a non-primary product: the portfolio records Find My Car as the primary Vercel bet, while Fractal carries a longstanding iOS widget-rendering issue. The September 14 direct old-CarClever test log shows strong search/filter behaviour, but it is not a monthly Auto.dev consumption report.

## Recommended operating model

**Recommended: retain old CarClever only as a limited legacy fallback on Free, after the readiness gate below.**

Do not spend effort adding NHTSA Safety Ratings, proactive vPIC enrichment or a new rate-data integration while evaluating a Fractal exit. Those are feature investments in a platform that is being scaled down. The leaner, honest product is more coherent:

- discovery and basic listing cards;
- transparent listing/history-based risk flags;
- NHTSA model-level recall fallback;
- affordability estimates, clearly labelled;
- no rich technical-spec or “real lender data” claims.

If measured demand later exceeds the Free cap, the decision should be **re-upgrade temporarily for a measured business reason or retire/unpublish Fractal**—not quietly rebuild a second full product there.

## Free-readiness gate for Fractal engineering

Before changing the Auto.dev plan, have the Fractal agent return evidence for all of the following. This is a narrow maintenance/verification request, not an authorization for feature work.

1. **Usage baseline:** exact 7-day and 30-day Auto.dev request totals, split by endpoint/status if the dashboard/logs expose them; projected monthly total; number of cold starts/restarts over the same period.
2. **Quota semantics:** written Auto.dev support/dashboard evidence, or an isolated non-production confirmation, of whether 402/feature-unavailable requests count against the 1,000-call allowance.
3. **Free-mode path:** verify that all Growth-only calls—including Specifications—are skipped once Free is known; do not rely on repeatedly discovering unavailable products at runtime.
4. **Probe lifecycle:** show how many Growth probes can occur per hosted instance/start and whether their unavailable state persists long enough to protect the monthly quota.
5. **Output truthfulness:** show the exact fields/labels returned on Free for vehicle details, deal risk and affordability. In particular, no “real” APR, payment, tax/fee, TCO, warranty or VIN-specific recall label may remain where the data is estimated or unavailable.
6. **Regression proof:** run a small live bank through the production-like Fractal surface: a normal used-car search, listing detail, risk check with recalls, affordability, and a VIN-decoding fallback. Capture the user-visible result, not only unit-test output.
7. **Quota monitoring:** identify the dashboard view or alert that will be checked at roughly 50%, 75% and 90% of Free usage. If no alert exists, record a simple owner review cadence rather than claiming automated monitoring.

## Decision thresholds

| Evidence after the readiness check | Recommended action |
|---|---|
| Projected monthly usage comfortably below 700 calls, required fallbacks are honest, and the above regression bank passes | Downgrade to Free and retain as a limited legacy fallback. |
| Projected usage 700–1,000 calls or failure/restart calls are material/unknown | Do not downgrade yet. First reduce avoidable calls and get quota semantics confirmed. |
| Projected usage exceeds 1,000 calls or core results materially degrade | Do not re-invest in Fractal by default. Decide explicitly between a time-bounded Growth renewal tied to demonstrated revenue and retiring/unpublishing the legacy app. |
| The iOS rendering issue remains unresolved and measured use is negligible | Retirement/unpublishing becomes the cleaner strategic choice. |

## Records consulted

- carclever-widget/CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md
- getcarwise-docs/STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md
- getcarwise-docs/SESSION_CARCLEVER_DUAL_PLATFORM_CLOSEOUT_20260912.md
- getcarwise-docs/REVIEW_FRACTAL_ELECTRIFIED_RENDERING_BUILD_20260912.md
- getcarwise-docs/TEST_LOG_OLDCARCLEVER_20260914.md

## Next decision required from André

Choose one of these directions after the readiness evidence returns:

1. **Free standby:** retain old CarClever as a deliberately limited fallback;
2. **Measured renewal:** retain Growth only if usage/revenue evidence justifies it; or
3. **Fractal exit:** unpublish/retire the old legacy surface after preserving the required records.

This assessment does not select one on André's behalf.
