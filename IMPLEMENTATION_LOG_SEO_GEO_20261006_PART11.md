# SEO/GEO Implementation Log — Part 11 (Oct 7, 2026)

**Continues** `IMPLEMENTATION_LOG_SEO_GEO_20261006_PART10.md`. Owner lane: Claude — Engineering.

## Deal Score: what the new CarClever and the calculator actually do (code check)
- **Find My Car app** (`carclever-find-my-car`, `lib/match-score.ts`): no price "Deal Score". It computes a **Match Score** 0–100 = 0.55 stated-criteria fit + 0.30 resolved-criteria fit + 0.15 identity confidence (labels: 85+ Strong match, 65+ Good match, else Partial match; weights marked provisional), plus separate risk tiers. It measures fit to the shopper's request, not price value.
- **Deal Score Calculator** (`carclever-widget`, `app/tools/deal-score/page.tsx` FAQ): 0–100 from five factors worth up to 20 points each: Market Value (price vs median of at least 30 comparable listings; search widens radius, then year range, then nationwide, then drops trim), Mileage (vs 15,000 miles/year expected), Age, Reliability (manufacturer track record), Recall Safety (open NHTSA recalls). Tiers: STRONG 80–100, FAIR 60–79, CAUTION 40–59, AVOID 0–39. Free for up to 10 queries per session.
- **Lite app:** `components/ResultCard.tsx` shows a fallback verdict from `deal_score` (75+ Strong Value, 60–74 Fair Deal, below 60 Overpriced) when no backend verdict is supplied; this differs from the calculator tiers and should be reconciled by whoever owns the backend verdict.

## Post 412 (Deal Score Explained) corrected to match the calculator — DONE
- Replaced RED/YELLOW/GREEN bands (0–40/41–70/71–100) with the real tiers (AVOID/CAUTION 0–59 zone, FAIR 60–79, STRONG 80–100); weights 20/20/25/20/15 replaced with "up to 20 points" each; factor 3 now "Market Value (Comparable Listings)" (no Edmunds data claim); reliability source claim (NHTSA and J.D. Power) replaced by manufacturer track record; factor 5 "Regional Pricing Inefficiency" replaced by "Recall Safety"; example scores relabelled by the real tiers (52 CAUTION, 78 FAIR, 31 AVOID); FAQ wording updated; unsupported "most vehicles land in YELLOW" removed; an "As built" paragraph states the real scoring and that the calculator is authoritative.
- Verified: no RED/YELLOW/GREEN left; 2 embeds, 1 table, 2 Edmunds links unchanged. (Several browser calls timed out while the saves completed; each result was confirmed by a later read.)

## Deal Score tool page claims (carclever-widget) — branch ready, NOT yet merged
- Finding: the tool page's GEO section said its SUV list was "based on… deal-score distributions across 50,000+ U.S. transactions" and "Updated weekly" (and a Dataset JSON-LD repeated this). The list is hardcoded editorial content (dateModified 2026-05-31); no such data pipeline exists in the code.
- Change on branch `fix/deal-score-page-claims` (commit `79be512`, file `app/tools/deal-score/page.tsx` only): heading "Popular Used Mid-Size SUVs: Editorial Shortlist", honest intro and methodology note (editorial, last reviewed May 31, 2026, not live data), column "Value tier (editorial)", Dataset JSON-LD removed. Vehicle data, calculator, FAQ schema and SoftwareApplication schema unchanged.
- Next: André creates the pull request from the compare link (connector requires human confirmation); Claude checks the Vercel preview and merges.

## Still open
Sitemap stale (re-check Oct 7); the two older Edmunds links in post 513 need Shared IDs; optional arithmetic audit of post 513 examples; reconcile Lite fallback verdict thresholds with the calculator tiers.
