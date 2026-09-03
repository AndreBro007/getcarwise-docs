# Edmunds Live-Search Confirmation — Mechanism Blocked, Routed Back for Redesign

Date: 2026-09-03
Owner: Claude / Engineering lane (found the blocker) → ChatGPT / Business-Strategy lane (owns the redesign decision)
Status: Engineering paused on this sub-feature. Everything else already shipped stays as-is.

## Why this doc exists

`HANDOFF_EDMUNDS_VIN_SEARCH_EXPERIMENT_20260903.md`'s "Final design decision" specified a live Google-search fallback tier (exact VIN `site:edmunds.com` search, then one targeted year+make+model+trim+dealer/location search). Andre corrected this to "approved for implementation, not experimental" and asked for the practical live Google-search mechanism, with credential blockers to be identified rather than treated as undecided.

The code was built completely (see `DECISIONS.md` `SYS-20260903-003` in `carclever-widget`, and PR #2 on `carclever-find-my-car`) behind a configuration boundary, on the assumption that the mechanism would be the Google Custom Search JSON API. Before walking Andre through Google Cloud Console setup, that assumption was checked against current Google documentation and turned out to be wrong in a way that blocks the whole approach, not just a credential detail.

## The actual blocker

Per `developers.google.com/custom-search/v1/overview` (Google's own page, last updated 2026-02-18):

> "The Custom Search JSON API is closed to new customers... Existing Custom Search JSON API customers have until January 1, 2027 to transition to an alternative solution."

Confirmed no existing account/key for this exists on Andre's side (checked the Google Drive secrets folder used for every other credential in this project — nothing there). So this isn't a "your account needs configuring" blocker, it's "this specific product cannot be signed up for anymore," full stop, regardless of platform, subscription tier, or account history.

Google's own suggested replacement, **Vertex AI Search**, is a materially different and heavier product than what was designed around:
- No clear/consistent free tier as of Aug 2026 (some sources describe 10k free queries/month, others describe no free tier at all as of Aug 2026 — conflicting even in current write-ups)
- Usage-based pricing, roughly $1.50–6 per 1,000 queries, plus indexed-data costs
- Requires a GCP billing account enabled from the start, a "data store" + "search app" setup, possibly domain verification
- This is enterprise-shaped tooling for a lightweight per-listing VIN-confirmation lookup — a scope and cost mismatch with what was approved.

## What this means for the approved design

The **behavior** specified in the Sep 3 handoff (exact-VIN search → targeted fallback search → confirmed/targeted-fallback/unconfirmed tiers, no stock/price/mileage/color searches) is unaffected and doesn't need to change. Only the **mechanism** (which live search API actually executes those two queries) needs to be re-picked, since the one assumed isn't available.

## Options identified so far (not yet evaluated for fit — that's the ask below)

1. **Bing Web Search API** (Microsoft/Azure) — similar shape to what was originally planned (API key + query param), has a free tier, straightforward signup, open to new customers as of this check.
2. **SerpApi or Serper.dev** — third-party services that return real Google search results specifically for this kind of use case, typically simple API-key signup with a small free tier, no GCP account needed.
3. **Drop the live-search confirmation tier entirely** — ship everything else already built (split-CTA relabel, the confirm/fallback/fail-open architecture in `lib/link-resolution.ts`) but leave `isGoogleSearchConfigured()` permanently false / remove the search call — i.e. the deterministic exact-VIN URL by default, same as pre-2026-09-03 production behavior, with no live confirmation signal at all.

None of these three were evaluated for cost, reliability, ToS fit, or query-volume behavior against Andre's actual usage pattern — that evaluation is explicitly being handed to the Business-Strategy lane rather than picked unilaterally by Engineering, since it's a vendor/cost/design decision, not a code decision.

## What's needed back from ChatGPT before Engineering resumes on this sub-feature

A short redesign addendum (same handoff-doc pattern as before) that either:
- Names a specific replacement mechanism (from the three above or another one found), with enough detail for Engineering to implement it the same way `lib/edmunds-search.ts` was written (one exact query, one targeted query, no other query types, fail-open on any error) — Engineering will re-check the vendor's current signup/ToS state itself before building, the same way this blocker was caught, rather than trust it secondhand — or
- Explicitly decides to drop the live-confirmation tier for now (option 3), in which case Engineering will simplify `lib/link-resolution.ts` back down and remove the now-unusable `lib/edmunds-search.ts` scaffold rather than leave dead/inert code behind.

## Status of everything else

Unaffected and already shipped, not touched by this blocker:
- Split-CTA relabel ("Check avail." / "View similar") — `carclever-find-my-car` PR #2, draft, tested, `main` untouched.
- The confirm → targeted-fallback → fail-open architecture in `lib/link-resolution.ts` — structurally sound regardless of which search vendor eventually fills in `lib/edmunds-search.ts`; only the vendor-specific query function needs to change once a mechanism is picked.
