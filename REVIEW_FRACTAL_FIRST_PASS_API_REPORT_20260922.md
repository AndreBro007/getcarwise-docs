# Review — Fractal First-Pass API Report

**Date:** 2026-09-22  
**Scope:** assessment of the Fractal code agent's supplied “Auto.dev Free Plan Impact Assessment.” This review does not inspect the old Fractal source directly and does not authorise any downgrade or implementation.

## Bottom line

The report is useful as a **preliminary architecture hypothesis**. It identifies the likely endpoint families, expected fallbacks and a potentially material Specs-call issue.

It is **not** the requested current API-and-field inventory. It contains no code locations, no raw response paths, no complete field matrix and no source-to-output trace. Its statements about individual listing fields—especially MPG and EV range—are therefore not verified.

## What can be retained as a working hypothesis

| Report statement | Assessment | Reason |
|---|---|---|
| Old CarClever calls Auto.dev Listings, Photos, Specs, Recalls, APR, Payments and TCO. | Plausible but unverified inventory. | The report names endpoints and related tools, but gives no call sites or proof that none are missing. |
| NHTSA vPIC, NHTSA recalls and Zippopotam are external fallbacks/helpers. | Plausible but incomplete. | No exact paths, code locations or field mappings are supplied. |
| Search relies on Listings and photos can be independently retrieved. | Plausible. | Still requires code/output tracing before it can be treated as a complete description. |
| NHTSA vPIC can return VIN-derived manufacturer specification variables. | Broadly supported. | vPIC's official documentation describes VIN decoding into key-value vehicle variables; it is not proof that this project reads any particular value. |
| NHTSA model/year safety ratings may be useful later. | A potential future addition only. | It is not evidence of an API currently used by old CarClever. |

## Important findings that need follow-up

| Finding | Why it matters | Current status |
|---|---|---|
| Specs appears absent from the stated capability probe/guard, while every other Growth route is said to be guarded. | A details request may still make a Specs call and receive 402. | Plausible defect; needs code evidence. |
| The report simultaneously says all Growth endpoints are guarded and says Specs is not guarded. | The “zero code changes required” conclusion does not follow. | Internally inconsistent. |
| Listing MPG fallbacks are asserted as `listing.vehicle.mpgCity` / `mpgHighway`. | This was the exact question André raised. | **Not proven**: no code path, response sample or output trace. |
| EV range is said to be lost. | Could be correct, but a complete inventory needs to establish whether another source/local field is used. | Not proven. |
| Affordability fallback figures and `usingRealData` wording are described. | These may be useful, but require output/schema and UI call-site evidence. | Plausible, not verified. |
| Recalls are described as VIN-specific in Auto.dev and model-level in NHTSA. | User wording must accurately distinguish the two. | Needs exact request parameters and output label evidence. |

## Claims to reject

### FRED series DTCTHFNM is not an auto-loan rate

The report proposes FRED series `DTCTHFNM` as an auto-loan-rate fallback. FRED identifies it as **Total Consumer Loans and Leases Owned and Securitized by Finance Companies, Level**, measured in millions of dollars—not an interest-rate series. It must not be used as an APR substitute.  
Source: [FRED DTCTHFNM](https://fred.stlouisfed.org/series/DTCTHFNM).

### vPIC is not a drop-in Specs replacement

NHTSA vPIC can decode VIN-related manufacturer data and exposes flat decode output, but that does not establish a consistent replacement for EPA economy figures, EV range, warranty, equipment feature lists, retail-price data or ownership-cost models. It can only be evaluated field by field after the project’s actual usage is known.  
Source: [NHTSA vPIC API](https://vpic.nhtsa.dot.gov/api/).

### Safety Ratings and DOE/AFDC are not current dependencies

The report presents NHTSA Safety Ratings and the Department of Energy's AFDC as possibilities. They should not be included in the current API inventory unless the code audit finds actual calls to them.

## Correct next step

The next Fractal request remains the read-only inventory in `HANDOFF_FRACTAL_AUTODEV_FIELD_AND_FREE_TIER_AUDIT_20260922.md`:

1. every API actually called by current production-reachable code;
2. every response field actually read and/or surfaced;
3. exact code and raw response paths;
4. source-to-output tracing per tool; and
5. clear separation of live, fallback/internal, and dead/type-only code.

Only after that inventory is reviewed can a reliable Free-tier or Fractal-retention assessment be made.

## Explicit non-decisions

- No subscription, Auto.dev plan, Fractal plan, code, deployment, API key, UI or website change is authorised.
- No conclusion is drawn that the stated endpoint/field list is complete.
