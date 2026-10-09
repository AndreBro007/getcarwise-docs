# RETURN: Edmunds/Impact catalogue data-continuity spike — INTERIM (Claude, Engineering lane)

**Date:** Oct 8, 2026 (Brisbane) · **Status:** INTERIM, spike NOT exited, nothing promoted · **Owner:** Claude (Lane 1), directed by André
**Responds to:** `HANDOFF_CLAUDE_EDMUNDS_DATA_CONTINUITY_SPIKE_20261008.md` (ChatGPT brief)
**Scope decided by André:** OpenAI app only (same MCP URL). Anthropic and Meta are under review and untouched. Separate copy of V2 (not V3).

## UPDATE — Oct 9, 2026 (Claude): corrections to this record (the Oct 8 text below is kept as history)

1. **Statuses:** Anthropic is APPROVED and PUBLISHED (Community connector, Oct 9). OpenAI’s new app is PUBLISHED (Version 1.0.0, RELEASED; `DECISIONS.md` `SYS-20260924-007`; no review pending per André’s Oct 9 screenshot). Statements below that these reviews are in progress are out of date for those two; Meta was not re-checked.
2. **Cutover route in section 7 is WITHDRAWN.** The idea of a dedicated production branch for `carclever-openai` contradicts the documented strategy (all three platforms on `release/v2`; test on `staging`, merge into `release/v2`, promote per domain; `carclever-widget` TASKS.md #116 item 2). Documented route for the catalogue code: test on `staging`, merge into `release/v2`, promote on `carclever-openai` only, with behaviour switched per project by environment variables (`LISTING_SOURCE` and the Impact variables exist only on the OpenAI project).
3. **Branch state:** the spike head is now `8c71b89` (102/102 tests), after adding to the Oct 8 build: year-by-year queries (`Name ~`), nearest-city dealer queries, model lists in `IN` chunks, the large-SUV fallback, no condition label when unknown, VIN from `Mpn`, and the year, mileage and dealer-ZIP mapping now confirmed (20/20 on the diagnostics; André verified one card against Edmunds), no longer “inferred”. `carclever-oai-test` still points at the spike branch (temporary). Nothing has been promoted.
4. **Auto.dev:** André is over 1,000 calls and still being served (Oct 9). ChatGPT’s `REASSESSMENT_..._20261008` says Auto.dev’s public pricing has a “grandfathered Starter with metered overages”; the pricing page and llms.txt Claude read on Oct 9 list only Free (capped), Growth, Scale and Enterprise. Unreconciled: confirm on André’s Auto.dev billing page (TASKS.md #113, #116).
5. **Files check (André, Oct 9):** the catalogue Files endpoint returned 0 files; Impact documents three bulk routes (platform download, FTP, Items API); next step is the catalogue details page in the Impact platform (TASKS.md #118).
6. **Other Oct 9 changes:** the version banners in six admin files were corrected (`release/v2` tip `cac7028`); STATE.md was split a second time (`STATE_ARCHIVE_2026-09-19_to_2026-09-29.md`); document audit and updates are recorded in TASKS.md #114–#117.

## 1. Headline
- A working Edmunds/Impact catalogue listing source exists as a **separate, tested branch** and is running on the OpenAI **test** domain only. It returns real Edmunds listings with VIN, year, mileage, dealer city/state, photos and tracked links, with **zero Auto.dev requests** in catalogue mode.
- **No production domain, branch setting or live deployment was changed.** Live domains verified unchanged repeatedly: `carclever-oai` and `carclever-meta` -> `cac7028` (release/v2); `carclever-anth` and `carclever` -> `dd68e15` (deliberate pin).
- Decision on cutover is **pending André (morning of Oct 9)**. André may renew Auto.dev for a month to buy time for a better fallback (daily extraction of the catalogue).

## 2. What was built (repo `carclever-find-my-car`, branch `spike/edmunds-catalog-mode`, head `7f66b8a`, from `release/v2` `cac7028`)
- Additive only; no existing code removed. Same two tools, schemas, MCP URL and screen source (one small change to `results-card.ts`, see below).
- `lib/source-mode.ts` — `LISTING_SOURCE` = `auto_dev` | `edmunds_catalog` | `auto` (default `auto`). Breaker trips on Auto.dev 401/402/403 (15 min), 429 and repeated 5xx (2 min). With no Impact credentials every mode behaves exactly like today.
- `lib/catalog-source.ts` — Impact catalogue adapter that outputs the existing listing shape. Includes year-by-year queries (`Name ~ 'YYYY'`), nearest-city dealer queries for ZIP searches, `IN (...)` model lists (up to 24), distance from the user's ZIP, price bands for price-only searches, and an aggregate-only diagnostics function.
- `lib/listing-source.ts` — facade with the four function names the route used. Route changes are an import swap plus small guards (no fair-pool duplicate query, no false "used only" note, no blank VIN text, `canonicalVehicleId` falls back to `catalog:<item id>`, scope reported `local` only when distance was actually applied).
- `lib/vehicle-class.ts` — safety net: when no model is supplied and the request describes a large / three-row SUV, expand to a curated model list (catalogue source only; explicit models always respected). Approximation from market knowledge, not feed data.
- `lib/link-resolution.ts` — catalogue tracking link used exactly as supplied, never re-wrapped.
- `lib/corpus-count.ts` — the cosmetic corpus-count call (one Auto.dev call per cold start) is now opt-in (`CORPUS_COUNT_REFRESH=true`). **This changes live Auto.dev behaviour if merged.**
- `lib/results-card.ts` — (a) non-production builds honour `NEXT_PUBLIC_WIDGET_ORIGIN` when set; (b) no condition pill when condition is unknown (known USED/NEW/CPO render as before). **The shared screen is therefore no longer byte-identical to live.**
- Temporary: `app/api/catalog-diag/route.ts` (aggregate-only diagnostics, 404 unless `CATALOG_DIAG_KEY` matches). **Must be removed before any cutover.**
- Tests: 101/101 pass (existing 79 plus new, including a failing-Auto.dev mock proving zero Auto.dev calls, failover, link rules, real-feed-shape end-to-end, and a no-leak diagnostics test). One pre-existing type error in `tests/best-for-budget-ranking.test.ts` (not from this work).

## 3. Catalogue feed facts (live diagnostic, 20-item sample, Oct 8)
**Confirmed:**
- `Mpn` = VIN (20/20 VIN-shaped). `Text1` = model, `Text2` = trim, `CurrentPrice` = price, `Manufacturer` = dealer name, `Url` = partner tracking link.
- `Numeric1` = model year (20/20 equals year in `Name`), `Numeric2` = mileage (20/20 plausible; André verified one card against its Edmunds page), `ShippingLabel` = dealer ZIP (20/20 valid US ZIP; leading zero dropped upstream).
- No `Make`, `Year`, `City`, `State` fields; `Condition` empty on every item. `Description` and `Name` start with the model-year, make and model; `Description` also carries the dealer name; `Text3` is a title-like string, not an address.
- **Queryable (HTTP 200):** `Text1`, `Category`, `CurrentPrice`, `Manufacturer` (exact), `Name ~ '...'` and `Description ~ '...'` (contains), `OR`, `IN`, `PageSize=100`.
- **Not queryable (HTTP 400):** `State`, `City`, `Year`, `Make`, `Condition`, `Mpn`, `Numeric1`, `Numeric2`, `ShippingLabel`, `Colors`.
- `Category` vocabulary is inconsistent across dealers ("SUV", "Sport Utility", "4D Sport Utility", ...), so it under-recalls.
- Photos: 9 dealer CDN hosts; 8 fetch fine server-side; `img2.carmax.com` times out for most photos even with browser-style headers (not fixable from our side). 3/18 sampled photo URLs were plain http (now accepted, served via our HTTPS proxy); 2/20 had no photo.
- `Description ~ '<city>'` returns cars whose dealers are in/near the city (Santa Monica, Pasadena, Austin: 20/20 within 15 mi; San Diego 7/7 within 30) but is incomplete (Beverly Hills returned 2 far-away cars). Used as an additive candidate source only; every row is still filtered/ordered by its real dealer-ZIP distance.

**Cannot be known from this feed:** new vs used, accident history, CPO, seats, drivetrain, transmission, body size class. `used: true/false` is ignored in catalogue mode (André decided: no mileage-based guessing; keep as is).

## 4. ChatGPT test evidence (André, test connector on the test domain)
- "honda crv under 30k near 90210": 8 local results, newer years, photos, two buttons ("Check avail." / "View similar"), correct mileage/location. First card verified against Edmunds by André.
- "large suv under 60k in 90210": exposed two defects, both fixed in `7f66b8a`: (1) caller sent only `bodyType: SUV` + vehicleNeeds + `seatsMinPreference: 7` with no model list, so every SUV came back; (2) a cap of 3 models silently dropped most of a caller's model list (first call listed 10 models and returned nothing). Retest with a 10-model list returned 8 plausible large SUVs near LA.
- Known remaining quality limits: candidate pool is a bounded sample, not the whole feed; accuracy for requests with no make/model/known class is inherently limited (André's position: catalogue-only searches should be driven by make/model).
- Pending André retest: UNKNOWN pill removal (likely ChatGPT caching the old card template per connector; re-add connector to refresh).

## 5. Environment and setting changes made this session (all Preview/test only)
- **Impact:** André created a new read-only token "CarClever catalog read" with scopes items, item, files, search (retrieve catalogs / retrieve catalog unticked). Credentials entered by André only; never seen or stored by Claude.
- **Vercel project `carclever-openai`, Preview scope:** `IMPACT_ACCOUNT_SID`, `IMPACT_AUTH_TOKEN`, `IMPACT_CATALOG_ID` (by André); `LISTING_SOURCE=edmunds_catalog`; `NEXT_PUBLIC_WIDGET_ORIGIN=carclever-oai-test.getcarwise.app`; `CATALOG_DIAG_KEY` (temporary, sensitive). Production scope: unchanged (still has its own `NEXT_PUBLIC_WIDGET_ORIGIN`).
- **Test domain** `carclever-oai-test.getcarwise.app`: git branch changed `staging` -> `spike/edmunds-catalog-mode` (André approved). ChatGPT sandbox needs the widget host label <= 63 chars (`SYS-20260906-002`): the branch preview URL (74) cannot work; the test domain (33) does. Needs a fresh connector after changes (template caching).
- Several preview redeploys of the spike branch. `autoAssignCustomDomains` untouched (OFF on the three live projects).

## 6. Outage assessment (Auto.dev allowance ends; reset Nov 2)
- Auto.dev pricing page (read Oct 8): Free = 1,000 calls/month, **capped, requests stop at the limit**; listings/photos/VIN decode only; 5 req/s. Growth = $299/month + data fees (listings $0.0015, photos $0.0009, VIN decode $0.0025), unlimited volume, 10 req/s, 7-day trial (billing terms not verified). The Oct 2 record of a pay-per-call "Starter" no longer matches the page. Prior Growth month (screenshot, STATE): 14,965 requests, ~US$14.80 data fees.
- **One Auto.dev key is shared by six Vercel projects** (`carclever-openai`, `carclever-meta`, `carclever-find-my-car`, `getcarwise-app`, `ccfmc-dev`, `ccfmc-dev-v3`) and the Fractal apps: one pool.
- **Breaks at the cap:** all three live MCP apps (search errors; platform reviews are in progress, so reviewers could see failures — inference); the 9 tool pages that embed `getcarwise.app/carclever-lite/` (legacy Lite -> Fractal old CarClever); 6 pages that embed `carclever-widget.vercel.app` (`/carclever-lite`, `/tools/deal-score`, `/tools/price-check`, `/tools/vin-check`, 2 blog posts); Lite V2 (backend hard-coded to `https://carclever-anth.getcarwise.app/mcp` in `carclever-widget` `app/api/chat-v2/route.ts`). Static content keeps working.
- The Google Search paid test targets `/tools/best-compact-suv-under-25000/`, which embeds the old app: **hold paid traffic until it works**.
- Code parity check: Anthropic `dd68e15` vs OpenAI/Meta `cac7028` differ only by one 24-line disclosure note in `route.ts` (SYS-20260924-008). The three apps are in sync; none of them has the failover (it exists only on the spike branch).
- Unknown: the HTTP status Auto.dev returns at the cap; how the Fractal apps behave.

## 7. Options and pending decisions (André, morning Oct 9)
- A. Do nothing until Nov 2. B. Renew Auto.dev Growth (~$299 + fees; exceeds the stated $200/month ceiling; buys time for the daily-extraction fallback). C. Cut the OpenAI app over to the catalogue (production safety gate in `PLAYBOOK.md`). D. Repoint Lite V2 to the OpenAI backend after C. E. Swap the 9 tool pages from legacy Lite to Lite V2 (WordPress change; page-239 cutover previously "unauthorized"). F. The 6 old-widget pages cannot be fixed from our code.
- Cutover route for OpenAI only: shared tracked branch `release/v2` also feeds Meta; proposal is a dedicated production branch for `carclever-openai` (project setting change, needs André's confirmation), then merge, promote, verify live. Nothing done.
- Longer term (André's direction): extract the catalogue daily, enrich (NHTSA etc.), search our own database. Gates not yet checked: permitted use/storage under the Edmunds/Impact terms (an Impact email already told André to extract the data when VIN search failed), file size/format/refresh pattern, and where a daily job and database would run. A read-only "catalog files" detail check (counts, sizes, formats; no download) was offered, not yet approved.

## 8. Before ANY cutover (cleanup list)
1. Remove `app/api/catalog-diag/route.ts` and the `CATALOG_DIAG_KEY` variable.
2. Set test domain `carclever-oai-test.getcarwise.app` back to `staging`; remove the Preview `NEXT_PUBLIC_WIDGET_ORIGIN` if not needed.
3. Decide `LISTING_SOURCE` for Production and add the three Impact variables to Production scope (André enters values).
4. Decide whether the `corpus-count.ts` change and the `results-card.ts` pill change go live; review the shared-screen diff.
5. Follow `VERCEL PRODUCTION SAFETY`: show live commit + aliases for all 3 domains before and after; verify on the live domain with a real search.
6. Check OpenAI's current update/scan path in the portal (docs: tool changes are handled through scans; not guaranteed).

## 9. Deviations and risks (recorded plainly)
- The Vercel API token and the GitHub PAT were passed inline in sandbox commands (no env vars in the sandbox), so both are visible in that chat's tool-call log. Temp scripts were deleted. André was advised to rotate and declined; the Vercel token expires Nov 16, 2026.
- The GitHub PAT was used for a read-only clone and for pushes of the spike branch (large multi-file writes; documented fallback). `release/v2` and `main` were never pushed to.
- Early advice to use the Vercel branch preview URL for ChatGPT testing was wrong (sandbox label length) and wasted a test; corrected after reading `DECISIONS.md`. Early ChatGPT test runs on the test domain hit Auto.dev before forcing catalogue mode (a few dozen calls).
- Not done this session: STATE/TASKS/DECISIONS updates beyond a pointer to this file; review checkpoints were **not advanced** (docs held at `4fe2e15`; ~45 added docs, `WORKFLOW_ARCHITECTURE.md` and full `TASKS.md`/`DECISIONS.md` not read). `TASKS.md` and `DECISIONS.md` are over the ~200 KB split size; a split is pending André's OK.
- The PLAYBOOK.md "Mode C" example contains a plaintext WordPress application password; not used; recommend rotating and redacting.
