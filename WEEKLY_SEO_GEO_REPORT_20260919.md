# Weekly SEO/GEO Report — Sep 19, 2026

**Owner lane:** Claude — Engineering (ran this session under André's explicit one-time override; SEO/GEO reporting is normally ChatGPT's lane per the standing split)
**Sources:** Google Search Console (Chrome, authenticated session, no login needed), live site inspection (Chrome + JS console). **Semrush: blocked all session — account had zero API units (`no_api_units` error, non-retryable). No Semrush data of any kind (Site Audit, Position Tracking, Backlinks, Organic Research, Competitors, Traffic Overview, Keyword Research) is in this report.** Needs topping up: https://www.semrush.com/mcp-access
**Window:** 28 days, US-filtered (country=usa) in GSC unless noted otherwise.

---

## 1. Headline numbers (US, 28 days)

| Metric | Value | Trend (GSC Insights, vs. prior 28d) |
|---|---:|---|
| Search clicks | 53 (unfiltered) / 29 (US) | **+165%** |
| Search impressions | 2.94k (unfiltered) / 1.61k (US) | **+57%** |
| Avg CTR | 1.8% | — |
| Avg position | 24.9 (unfiltered) / 18.5 (US) | — |
| Generative AI impressions (US) | **213** | — |
| Indexed pages | 57 | — |
| Not indexed | **83** | — |
| External backlinks (GSC's own count) | **5, from 4 referring sites** | — |

**Caution flagged in the matrix and repeated here:** unfiltered vs. US-filtered GSC numbers differ meaningfully (53 vs. 29 clicks, 24.9 vs. 18.5 avg position). Confirm which convention the Sep 16 baseline actually used before treating this report's US-filtered numbers as directly comparable — this wasn't independently verifiable from the matrix text alone.

---

## 2. Findings against the Sep 16 Master SEO/GEO Matrix

### 🔴 Priority-1 page ($30k SUV) — head-term collapse, needs attention before treatment begins

- `/tools/best-compact-suv-under-30000/` — matrix's #1 priority page, slated for "controlled evidence-led refresh"
- Exact head term **"best compact suv under 30000"**: **1 impression, 0 clicks** in US 28-day window — down sharply from the 21 impressions cited Sep 16
- Page did not appear at all in the US top-24-pages-by-clicks list
- GEO side held steady: 3 AI impressions, matching the Sep 16 figure
- **Live inspection finding:** page's `<title>`, meta description, and `<h1>` all say **"Small SUV"** — but the URL slug, the tracked GSC query, and the matrix's own head term all say **"Compact SUV."** The `/best-compact-suv-under-25000/` sibling page correctly uses "Compact SUV" throughout. This mismatch is a plausible (not confirmed) contributor to the term-level drop.
- **Caveat on timing:** every page checked (this one, the $25k page, the $25k-comparison page, the $50k benchmark, and the PHEV page) shows an identical-pattern `lastModified` timestamp today, all within ~50 seconds of each other (17:04:25 through 17:05:12). This is far more consistent with a **site-wide rebuild/redeploy** than a targeted content edit — so the "Small vs Compact" wording may have been present before today, or may be a byproduct of today's deploy. I could not determine which from the tools available this session.
- Page already has substantial content (1,934 words, has an FAQ section) — supports the matrix's own read that a generic rewrite isn't the fix. No "methodology" section currently present, which the matrix's prescribed treatment explicitly calls for adding.

**Recommendation for ChatGPT lane:** verify the "Small SUV" vs. "Compact SUV" title/H1 mismatch before finalizing the treatment plan — it's a small, low-risk fix that may be worth doing independently of (and before) the larger evidence-led refresh.

### 🟢 3-row SUV under $50k (GEO benchmark) — strengthening

- 86 GEO impressions this window vs. 78 documented Sep 16 — still the site's clear GEO leader
- Page was in the day's redeploy batch but title/H1 unchanged from what the matrix describes

### 🟡 Used PHEV — still flat, weak content depth confirmed

- GEO impressions still ~1, no change from Sep 16 baseline (1)
- Live inspection: page is only **276 words** — thin relative to its 136-impression Search demand and the matrix's own "full evidence-led rebuild" prescription. Title/H1 correctly aligned with intent.

### 🟡 $25k SUV cluster — architecture confirmed live, still unresolved

- Both `/best-compact-suv-under-25000/` (122+ impr, Search) and `/best-compact-suv-under-25k-comparison/` (5 GEO impr) are live, separately indexed
- Live inspection: the comparison-URL page has its **own self-referencing canonical** — this is not an accidental duplicate-content situation; Google is correctly treating them as two distinct pages. The matrix's "Class 4 — Architecture First" call (map intent, decide consolidate-vs-differentiate) is still the right next step; nothing found this session resolves it.

### ⚪ Indexation: 83 not-indexed vs. 57 indexed

Breakdown (GSC "Why pages aren't indexed"):

| Reason | Pages |
|---|---:|
| Page with redirect | 42 |
| Not found (404) | 20 |
| Crawled – currently not indexed | 8 |
| Excluded by noindex tag | 4 |
| Blocked by robots.txt | 4 |
| Redirect error | 3 |
| Blocked (403) | 1 |
| Discovered – currently not indexed | 1 |

Not diagnosed page-by-page this session — flagging the volume (42 redirects, 20 404s) as worth a closer look next session, since redirects/404s at this scale are unusual for a site this size.

### ⚪ Backlinks — thin (GSC's own count, no Semrush cross-check possible)

- 5 total external links, referring sites: vercel.app (2), 2ip.io (1), reddit.com (1), scamadviser.com (1)
- No way to confirm whether this differs from a fuller crawl-based (Semrush) view this session

### ⚪ No manual actions / security issues in GSC. Sitemaps all healthy (3 submitted, all "Success," read within the last 1–2 days). Core Web Vitals: no CrUX field data yet (traffic too low) — expected, not a bug.

---

## 3. What wasn't covered this session

- **All Semrush-based data** — Site Audit, Position Tracking, Backlinks Analytics, Organic Research, Competitors Research, Traffic Overview, Keyword Research, Shopping/Paid Search. Account is out of API units.
- Page-by-page diagnosis of the 42 redirect / 20 404 not-indexed pages
- Any competitor benchmarking
- CJ Affiliate — explicitly excluded per André's instruction this session

## 4. Suggested follow-ups for ChatGPT lane

1. Verify/resolve the "Small SUV" vs. "Compact SUV" title/H1 mismatch on the $30k page before starting the planned combined SEO/GEO treatment
2. Confirm whether today's identical cross-page `lastModified` timestamps reflect a routine redeploy or an unlogged content change — if the latter, the treatment plan's pre-existing baseline assumptions may need re-checking
3. Once Semrush units are available, re-run Site Audit + Backlinks to cross-check the "5 external links" GSC figure and get the redirect/404 detail Semrush's audit tool would normally surface faster than manual GSC page review
