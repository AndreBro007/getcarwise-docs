# SEO/GEO Implementation Log — Part 7 (Oct 6, 2026)

**Continues** `IMPLEMENTATION_LOG_SEO_GEO_20261006_PART6.md`. Owner lane: Claude — Engineering. André's instruction: make Edmunds affiliate click-through the priority and follow `STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md` and `STRATEGY_IMPACT_WEBSITE_PUBLISHER_TAG_ASSETS_CATALOG_20260916.md` (action hierarchy: exact known destination > catalog > model/category deep destination > broad text asset).

## Mechanism tested in Chrome (one controlled click each; no forms, no leads)
- **Appraisals asset 4051015** (`https://edmunds.sjv.io/c/7765200/4051015/52125`) redirects to `https://www.edmunds.com/sell-car/` with `utm_adgroup=4051015`, `utm_matchtype=tradein`, `irpid=7765200` — the same destination as the Sell Your Car asset (3949601) already used on the pages. No change needed for the "see what it could be worth" links. (The Impact asset's listed landing page is `/appraisal/`; the live redirect lands on `/sell-car/`.)
- **Impact deep link with page tag works:** `https://edmunds.sjv.io/c/7765200/3949600/52125?sharedid=<tag>&u=<URL-encoded Edmunds page>` landed on `https://www.edmunds.com/used-toyota-camry/` ("Used Toyota Camry for Sale Near Me", about 1,833 listings) with `irpid=7765200`, `utm_source=impact` and the `sharedid` value passed through intact.
- **Test clicks made by Claude (will appear in Impact):** one Appraisals click (no sharedid), one Camry deep-link click with `sharedid=claude-test`. Earlier-session validation clicks are documented in `RETURN_WORDPRESS_IMPACT_STATIC_DESTINATION_MAPPING_20260921.md`.

## Edmunds destination pages verified in a real browser (Akamai blocks automated fetches)
All load with live listings: used-chevrolet-equinox, used-toyota-rav4, used-ford-escape, used-ford-f-150, used-honda-civic, used-mazda-cx-5, used-chevrolet-silverado-1500, used-honda-cr-v, used-nissan-altima, used-honda-accord, used-hyundai-tucson, used-kia-sportage, used-subaru-outback, used-toyota-highlander, used-toyota-corolla, used-toyota-camry, used-kia-niro (82 listings), used-chevrolet-bolt-ev (68), used-nissan-leaf (173). Pattern: `https://www.edmunds.com/used-{make}-{model}/`. The Silverado page is the Silverado 1500 page (the guide covers the Silverado line).

## Tag convention (Shared ID, no personal data; visible to Edmunds as well as to GetCarWise)
- Model guides: `model_<year>-<make>-<model>_top`, `_end-used`, `_end-tradein` (e.g. `model_2022-toyota-camry_top`).
- New guides: `hybrid-suv_*`, `used-ev_*`, `sedan-15k_*` with placements `cta-top`, `cta-end-used`, `cta-end-tradein`, and `model-<name>` for the per-model links inside the "compare first" section.

## Pages changed (all verified: stored content equals intended, every Edmunds link `rel="nofollow sponsored noopener" target="_blank"`)
- **16 used-model guides** (755, 749, 757, 741, 742, 752, 751, 756, 739, 740, 750, 738, 769, 758, 753, 754): disclosure sentence plus "Ready to see what is for sale? See current used {Model} listings on Edmunds" (model-specific deep link) right after the first section (verdict); closing line with a second model link and the strategy's trade-in bridge ("Trading or selling your current vehicle may change the budget available for this choice, so check its value on Edmunds…"). 3 links per page. Live check on the 2020 Equinox page: three links, correct `sharedid` and destination, disclosure shown before the link, byline and JSON-LD intact.
- **Hybrid SUV (936), used EV (938), sedans under $15k (935):** the three existing links now carry page tags, and a "See current used listings on Edmunds" line with model-specific deep links (Escape, RAV4, Niro; Bolt EV, LEAF; Corolla, Civic, Camry, Accord) was added after the first paragraph of the "compare first" section. 6, 5 and 7 tagged links respectively; tool iframe and single-line FAQ JSON-LD intact.
- Not changed: the four protected Task #78 pages, `/tools/` hub, the Task #63B CJ-to-Impact migration of the five older guides (separate task), interactive tool pages.

## What André checks in Impact (documented path; exact report URL not recorded)
Impact partner login `https://app.impact.com/login.user` (session was logged out in Claude's browser). Then **Reports → More Reports → Performance by Sub ID and Shared ID**, show the Shared Id column and filter Shared Id; or **Reports → More Reports → Click Data** (per-click detail, filter by Shared Id). Expect rows named as above once real visitors click, plus `claude-test`. Actions (leads) lag clicks; Edmunds window is 30 days.

## Open
Google re-indexing requests for 935, 936, 938; stronger button-style CTAs and tool-embedded Edmunds links as a next conversion test (changes visual design; needs André's yes); Publisher Tag pilot and Catalog module (strategy: pending); review of four remaining strategy drafts; revised AI-tools guide; TASKS.md and DECISIONS.md splits.
