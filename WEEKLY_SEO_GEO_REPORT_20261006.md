# Weekly SEO/GEO Report — Oct 6, 2026

**Owner lane:** Claude — Engineering (run at André's request; SEO/GEO reporting is normally ChatGPT's lane)
**Prior reports:** `WEEKLY_SEO_GEO_REPORT_20260919.md`; Sep 27 weekly scan (STATE.md)
**Mode:** read-only. No site, Semrush-setting, GSC, Ads or code change was made, except the Semrush Backlink Audit re-crawl André explicitly requested.

## Source status
| Source | Status |
|---|---|
| GSC (domain property `sc-domain:getcarwise.app`) | Read via Chrome |
| GA4 (property 532413608) | Read via Chrome |
| Semrush connector | Blocked: `no_api_units` (same as Sep 19) |
| Semrush via Chrome UI | Read: Domain Overview, Position Tracking, Site Audit, Backlink Audit (re-crawled Oct 6) |
| Clarity | NOT read — blank page in Chrome (login/render unresolved) |
| Impact / CJ | Not read (login-gated; CJ retired) |

## 1. Headline numbers (windows differ between reads — directional only)
| Metric | This week | Prior reference |
|---|---|---|
| GSC US 28d (Sep 6–Oct 3) clicks / impressions / avg position | 43 / 2.22k / 17.2 | 29 / 1.61k / 18.5 (Sep 19); ~41 / ~1.83k (Sep 28) |
| GSC all countries 28d | 66 / 3.39k / 15.1 | 53 / 2.94k / 24.9 (Sep 19) |
| GSC generative-AI impressions (US 28d) | 338 | 213 (Sep 19) |
| GA4 last 7 days | 30 users (+16.7%), 35 sessions (+18.6%), 5 key events | 26 users, 33 sessions (Sep 27) |
| Semrush AI Visibility | 14, 1 mention, 4 cited pages | 14, 1, 3 (Sep 25) |
- An exact previous-28-day GSC pull failed (date-range URL returned no data), so there is no like-for-like comparison.
- The GSC generative-AI query table looked identical to the normal web table; only its total (338) is reported.

## 2. GA4 (28 days, 117 sessions)
| Channel | Sessions | Engagement rate | Key events |
|---|---:|---:|---:|
| Direct | 51 | 29% | 0 |
| Organic Search | 51 | 61% | 4 |
| Referral | 12 | 100% | 0 |
| AI Assistant | 2 | 100% | 1 |
| Unassigned | 1 | 0% | 0 |
- Revenue $0. Top pages by views: `/` 61; `/carclever-lite-v2` 53 (4 users, 7m32s); `/tools/` 42; `/carclever-lite/` 27; `/tools/best-compact-suv-under-25000/` 17 (5 users, 5m08s, 5 key events).
- Likely André's own testing on the `/carclever-lite-v2` and $25k page rows — UNCONFIRMED.
- 7-day geography: US 22, Australia 5, 1 each Germany / Sri Lanka / Russia.

## 3. GSC detail
- **Pages (US 28d, clicks/impressions):** `/try-carclever/` 3/39; `/` 2/118; `/carclever-live-in-chatgpt/` 2/16; best-3-row-suv-under-50000 1/77; best-compact-suv-under-25000 1/76; best-compact-suv-under-30000 0/305; best-used-phev 0/107; best-midsize-sedan-under-40000 0/130 (pos 18.2); `/blog/` 0/120 (pos 65.8). Rows below the top 10 were parsed from concatenated strings.
- **Queries:** brand ("carclever" 4 clicks/21 impr; "car wise" 1/10; "getcarwise" 0/39); zero-click head terms ("ai car finder" 62 impr; "best suvs under 30k" 48; "best suv under 30000" 39).
- **Question-style queries ranking well (US):** "tools that use ai to compare used cars?" pos 3.5; "do hybrid suvs hold their value better than gas suvs?" 3.5; "does cargurus use ai to rank the best deals for me?" 9.3; several long AI-appraisal / used-car-sourcing questions at positions 2–5.
- **Indexing (report last updated Sep 21 — stale):** 57 indexed / 84 not indexed (was 83). Redirect 43, 404 19, robots-blocked 5, noindex 4, redirect error 3, 403 1, crawled-not-indexed 8, discovered-not-indexed 1. Not diagnosed page by page.
- **Manual actions: none. Security issues: none** (checked Oct 6).
- **Messages (5, 4 unread):** none are manual-action or security. Notable: "New Unparsable structured data issues" (Sep 27). The Unparsable structured data report (updated Oct 4) now shows 0 invalid pages, with a 1-page "Incorrect value type" blip around Sep 27. Breadcrumbs: 0 invalid / 9 valid.

## 4. Semrush (Chrome UI)
- **Domain Overview (Oct 5):** organic keywords 117 (Sep 25 snapshot: 77), referring domains 145 (118), backlinks 173 (137), Authority Score 2.
- **Position Tracking (10 keywords, US Google desktop, tracking restarted Sep 28):** visibility 27.58%, avg position 39.0. Positions: best midsize sedan under 40000 = 1; carclever = 1; car clever = 2; getcarwise = 2; best compact suv under 30000 = 27; best used phev plug in hybrid = 27; best suv under 30000 = 30 (vol 1,300); best 3 row suv under 50000, best suv under 30k, vin check (vol 90,500) = not ranking. The "+27.58%" is largely a baseline artifact (no earlier data).
- **Site Audit (crawl ~1 week old, 100 pages):** health 93%, AI Search health 85%. 1 error (invalid structured data item — may be stale given GSC shows 0); warnings: 52 low text-HTML ratio, 15 long titles, 9 internal nofollow, 1 missing meta description; notices: 39 permanent redirects, 34 links without anchor text, 23 pages with one internal link.
- **Backlink Audit (re-crawled Oct 6):**
| Metric | Sep 27 | Oct 6 |
|---|---:|---:|
| Referring domains | 105 | 134 |
| Toxic | 83 (79%) | 108 (80.6%) |
| Non-toxic | 22 | 26 |
| Backlinks analysed | 115 | 149 |
| Mirror pages / link networks (by IP) | 45 / 15 (Oct 6) | prev 15 / 8 |
  - The toxic count still includes the already-disavowed set because Semrush has not been told the file reached Google (André was shown, and did NOT click, the "Yes, I uploaded the file" recalculation prompt).
  - "For review": 63 backlinks / 51 domains (not yet disavowed). The free plan shows only 5 (`sidarma88gacor.shop`, `pamto.shop`, `corvio.shop`, `nuxlo.shop`, `bestirishcasinoonline.online`): guest-post-farm spam, toxicity 100, homepage targets. The other 46 are not visible; same campaign is an inference.
  - Semrush's disavow list shows 82 domains (all "Exported"); the file André uploaded to Google had 87. Counts (108 toxic vs 82 + 51) do not reconcile.
  - Domain Overview (145 ref domains) and Backlink Audit (134) are different Semrush datasets; the gap is unexplained.

## 5. Live site checks (Oct 6, sandbox)
- `$30k` page title/H1 now "Best SUVs Under $30,000 (2026): New Vs. Used Picks" — the Sep 19 "Small SUV" mismatch is gone; "compact" no longer appears in title/H1 though slug and tracked keyword still say compact.
- Used PHEV page ~3,300 words (was 276 on Sep 19). All five key pages: 200, self-canonical, index, JSON-LD present.
- `robots.txt` blocks `/tag/`, `/author/`, `/category/…`, Complianz uploads; sitemap index → post + page sitemaps (58 URLs). 57 return 200; 1 returns 301: `/tools/best-compact-suv-under-25k-comparison/` (WP page ID 771, Rank Math redirect → page 934). Both 771 and 934 are listed in `page-sitemap.xml` (Rank Math). See Task #67 follow-up.

## 6. GEO spot-checks (2 web searches only)
- "getcarwise.app CarClever AI car finder": the ChatGPT app directory listing for CarClever – Find My Car appeared; getcarwise.app itself did not.
- "getcarwise": results were unrelated Carwise / beCarWise entities (collision repair, leasing, a dealer, a car-sourcing service) — brand-name collision.
- Not tested: Perplexity, ChatGPT, Gemini directly.

## 7. Recommendations
- **Backlinks:** not urgent; no manual action or security issue found. Disavow (if desired) as a monthly batch; a new Google upload REPLACES the old file, so include the existing 87 + new domains. Recalculate in Semrush once after the next upload. Watch new-domains-per-week (79 → 94).
- **Hold protected pages** (Sep 28 no-change decision still applies).
- **Verify before claiming a win:** $40k sedan page 828 (GSC 130 impr at pos 18.2 vs Semrush keyword position 1).
- **Sitemap:** exclude page ID 771 via Rank Math → Sitemap Settings → General → Exclude Posts (does not touch the redirect, retained page or page content).

## 8. Open / to-do
- Clarity read (login/render); GSC index drill-down for 43 redirects / 19 404s; confirm the Semrush structured-data error is stale; Site Audit minor warnings; brand-collision and Q&A-content ideas for ChatGPT lane; Semrush API-unit top-up decision; Fractal decision due before Oct 14 (STATE.md).
- Admin: getcarwise-docs checkpoint NOT advanced (25 added + 1 modified docs unread since `4fe2e15`; only `CHECKPOINT_TASK78_GSC_PROTECTED_COHORT_20260928.md` and `WEEKLY_SEO_GEO_REPORT_20260919.md` read). PLAYBOOK.md still contains a plaintext WordPress application password (revoke, then redact).
