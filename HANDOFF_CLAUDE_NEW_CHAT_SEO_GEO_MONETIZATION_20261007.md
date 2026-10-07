# Handoff to a new Claude chat — SEO/GEO and Edmunds monetization (Oct 7, 2026)

**From:** Claude (Engineering lane), long Oct 6–7 session. **For:** the next Claude chat in the "GetCarWise Engineering" project. Run the normal start-of-session verification from the project instructions first (SHA-check gate, getcarwise-docs inventory), then work the priority list below. No secrets are recorded here; never repeat tokens, passwords or André's IP address in chat or documents.

## How André wants to work (keep doing this)
- Short replies, everything numbered, each item clearly marked ACTION / QUESTION / DECISION for André. Give a ready-to-paste prompt whenever work goes to ChatGPT (its instruction field is limited to 8,000 characters).
- Check our own documentation (getcarwise-docs, carclever-widget) for Edmunds/Impact products, pages and links BEFORE asking him; he has supplied them many times. Edmunds affiliate links are the only monetization path: use them wherever relevant, and propose monetization yourself from the strategy docs.
- Explain options and get confirmation before changing account/admin/API settings. Verify click-paths from documentation instead of guessing. State plainly what is confirmed vs not.
- Protected pages (Task #78): never edit the four protected pages: `/tools/best-compact-suv-under-25000/`, `/tools/best-compact-suv-under-30000/`, `/tools/best-midsize-sedan-under-40000/`, `/tools/best-3-row-suv-under-50000/` (the $30k page had only the approved schema fix). Byline on them: WAIT until the observation window ends.

## What was done Oct 6–7 (details in the logs)
Logs in getcarwise-docs: `IMPLEMENTATION_LOG_SEO_GEO_20261006.md` and `_PART2.md` to `_PART11.md`. Reports: `WEEKLY_SEO_GEO_REPORT_20261006.md`, `ADDENDUM_WEEKLY_SEO_GEO_REPORT_20261006_FOLLOWUPS.md`, `ANALYSIS_SEO_GEO_DIAGNOSIS_AND_ACTION_PLAN_20261006.md`. Summary:
- STATE.md split (live 181 KB + `STATE_ARCHIVE_2026-08-02_to_2026-09-18.md`); PLAYBOOK size rule and WORKFLOW_ARCHITECTURE updated; both lane prompts updated. TASKS.md has Tasks #104, #105, #106 (appended at the end; TASKS.md about 351 KB, DECISIONS.md about 368 KB; both editable via the GitHub web editor; splitting not needed).
- Schema repair on `/tools/best-compact-suv-under-30000/`; tools hub (page 452) and 16 model guides, 9 posts and the footer now link to guides; 32 titles and 21 descriptions rewritten (Rank Math `rankmath/v1/updateMeta`); 58 items re-attributed to André (WordPress user 1); template "Guide" (`page-guide`) adds a visible byline on 26 guide pages.
- All-in-One SEO was installed by André by mistake, caused duplicate tags, and was removed; Rank Math's "LLMs.txt" module now serves `/llms.txt`. GA4 internal-traffic rule and Clarity IP blocks use a range (home IP changes).
- Thin pages expanded and published (hybrid SUV 936, used EV 938, sedans under $15k 935); AI-tools guide published (post 1469); red-flags (309), Deal Score (412) and total-cost (513) posts upgraded with invented statistics removed and corrected to the real calculator; two arithmetic errors fixed in 513.
- Deal Score tool page claims fixed (carclever-widget PR #74); Lite tool now tags Edmunds links `lite_result` (PR #73). Find My Car has a Match Score, not a price Deal Score; the Deal Score Calculator is five factors up to 20 points each, tiers STRONG 80–100, FAIR 60–79, CAUTION 40–59, AVOID 0–39.

## Edmunds / Impact facts (verified)
- Impact account 7765200, Edmunds program 52125. Assets: Used Car Listings 3949600, New Car Listings 3949597, Sell Your Car 3949601 (trade-in), Appraisals 4051015 (lands on `edmunds.com/sell-car/`). Source of truth: `RETURN_WORDPRESS_IMPACT_STATIC_DESTINATION_MAPPING_20260921.md`; strategy: `STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md` and `STRATEGY_IMPACT_WEBSITE_PUBLISHER_TAG_ASSETS_CATALOG_20260916.md`.
- Deep link (tested): `https://edmunds.sjv.io/c/7765200/3949600/52125?sharedid=<tag>&u=<URL-encoded Edmunds page>` (in HTML use `&amp;`). Model pages verified in a real browser: `https://www.edmunds.com/used-{make}-{model}/` (e.g. used-toyota-camry, used-honda-cr-v, used-ford-f-150, used-chevrolet-silverado-1500, used-chevrolet-bolt-ev, used-nissan-leaf, used-kia-niro). Edmunds blocks automated fetches (Akamai): verify in Chrome.
- Markup on every Edmunds link: `rel="nofollow sponsored noopener" target="_blank"`; standard disclosure paragraph before the first link: "Some links on this page are affiliate links. If you use one, GetCarWise may receive compensation at no additional cost to you. Our recommendations remain independent." Button style: centered, `background-color:#2563eb;color:#ffffff;padding:14px 28px;text-decoration:none;border-radius:6px;display:inline-block;font-weight:600;`.
- Shared ID tags: `model_<year>-<make>-<model>_top|_end-used|_end-tradein` (16 model guides), `hybrid-suv_*`, `used-ev_*`, `sedan-15k_*` (with `_cta-top`, `_cta-end-used`, `_cta-end-tradein`, `_model-<name>`), `ai-tools-guide_sources|_cta`, `red-flags-post_compare|_cta`, `deal-score-post_compare|_cta`, `tco-post_compare|_tradein|_cta`, Lite tool `lite_result`. Test tag from Claude: `claude-test`. Impact report: Reports > More Reports > Performance by Sub ID and Shared ID (or Click Data). Never put personal data in a Shared ID.
- Publisher Tag pilot and Product Catalog module: PARKED by recommendation (pilot pages are the protected pages; our deep links already give per-page attribution).

## Working notes and gotchas (save time)
- Edit WordPress through André's logged-in Chrome session using REST: get a nonce from `/wp-admin/admin-ajax.php?action=rest-nonce`, then `/wp-json/wp/v2/posts|pages/<id>` (use `context=edit` for raw content). Heavy admin pages freeze the browser: run scripts from the lightweight page `https://getcarwise.app/wp-admin/admin-ajax.php?action=rest-nonce`. After a CDP timeout, re-read the post: saves usually completed.
- Request bursts trigger the host's "Checking your browser" 403 challenge; space requests and use normal page navigation to clear it. Every long script must stay under about 40 seconds.
- Edit existing posts at the DOM text-node level and prove the tag structure is unchanged before saving; WordPress keeps revisions (rollback). JSON-LD must be single-line (multi-line JSON was corrupted by `<br />` earlier). Posts and guides show the byline "by Andre Broekman" (posts via the theme, guides via the Guide template).
- GitHub: connector is the standing method. Pull requests: create a branch and commit, then André must click "Create pull request" (the connector's PR tool needs human confirmation; give him the compare link); then check the Vercel preview and the Codex review comment, and merge with `merge_pull_request`. The widget repo's Vercel project is `getcarwise-app` (not one of the three gated MCP domains); production host `carclever-widget.vercel.app`. Large files (TASKS.md, STATE.md) can be edited with the GitHub web editor via the CodeMirror view and a JS-triggered commit.
- A web `search_code` result often comes back empty (index incomplete): browse the repo tree instead.

## Priority list for the new chat
**P1 — decisions and actions waiting on André**
1. DECISION: park the Publisher Tag pilot and Product Catalog module (Claude recommends yes).
2. DECISION: approve the next monetization wave: add Edmunds links (disclosure, tags, one button) to pages that have none: guides 829 (truck under $35k), 773 (truck towing), 772 (midsize sedan $30K comparison), 774 (Highlander comparison), 541 (AI-native shopping), 540 (true-cost worked example); posts 1011 (new vs used math), 1008 (title brands), 993 (cross-shopping), 952 (CarClever live in ChatGPT), 666 (depreciation and APR trap), 809 (We Tested CarClever); optionally the `/tools/` hub (452). Not the four protected pages.
3. ACTION (André, in a few days): check Impact clicks by Shared ID; report what appears.
4. DECISION (André, by Oct 14): the Fractal decision.
**P2 — Claude tasks**
5. Re-check the sitemap: the new post `/best-ai-tools-for-buying-a-used-car-2026/` was missing from `/post-sitemap.xml` and page lastmods were stale after three safe flushes (Rank Math transients, unchanged sitemap-settings save, WP Rocket clear). Hosting dashboard shows "Hosted on unknown" and has no cache button. If still stale, options: wait, or briefly switch Rank Math's sitemap module off and on (small risk; ask André first).
6. Add Shared IDs to the two older Edmunds links in post 513.
7. Verify Task #63B (CJ-to-Impact) leftovers in the older guides and the legacy widget without touching protected pages.
8. Diagnose the slow page-loading score (Clarity LCP 4.6 s, INP 250 ms).
9. Verify Search Console's structured-data error clears for the $30k page after recrawl.
10. Read the roughly 25 unread getcarwise-docs files, then advance the Claude row of STATE.md's SESSION REVIEW CHECKPOINTS (docs row was held at `4fe2e15`; widget row recorded as `183554b` before ChatGPT's later commits).
11. Reconcile the Lite tool's fallback verdict labels (`components/ResultCard.tsx`: 75+ Strong Value, 60–74 Fair Deal) with the calculator tiers (80+ STRONG).
12. Optional: audit the remaining worked-example arithmetic in post 513.
**P3 — later or parked**
13. LATER (Task #104): LinkedIn company page, social accounts and app-marketing research (no official profiles exist; André creates accounts; ChatGPT researches; Claude adds verified `sameAs` links afterwards). Brand plan approved but unpublished.
14. PARKED: new-vs-used data series (needs Auto.dev calls from a shared ~1,000 per month allowance and publication-rights check); Reddit buyer-help plan (the separate Reddit app task is the active Reddit work).
15. Declined for now by André: rotating the GitHub token (it appeared in an earlier chat), plaintext credentials in PLAYBOOK.md and REFERENCE.md (WordPress application password, REST key, Auto.dev token), a narrower Vercel token, splitting TASKS.md/DECISIONS.md. Do not nag; mention only if something breaks.
16. Low priority: 25 toxic backlink domains not disavowed (monthly batch), Bing AI-citation gaps (Jul 27–Aug 6, Aug 20–22), Search Console legacy redirect and 404 drill-down; V3 development paused pending Anthropic review; two Lite versions exist (`carclever-lite` used by the guides, `carclever-lite-v2`).

## ChatGPT lane
- ChatGPT is idle. Project tasks belong in `carclever-widget/TASKS.md`; getcarwise-docs holds only named documents (ChatGPT once created a stray `TASKS.md` there; it was moved and deleted). ChatGPT's drafts are `DRAFT_*` files in getcarwise-docs; Claude reviews facts and format, André confirms, Claude publishes. Lessons: verify statistics, bands and weights against code or sources; check math; link only to opened URLs.
