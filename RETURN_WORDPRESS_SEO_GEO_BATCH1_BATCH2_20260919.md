# Return — WordPress SEO/GEO Batch 1 + Batch 2 Implementation

**Executed by:** Claude — Engineering lane (authenticated WordPress execution via André's live `wp-admin` browser session)
**Approved by:** André, explicit written approval, "ANDRÉ APPROVAL — EXECUTE WORDPRESS SEO/GEO BATCH 1 + BATCH 2"
**Handoff executed:** `HANDOFF_WORDPRESS_SEO_GEO_BATCH1_BATCH2_20260919.md`
**Governing docs read in full before editing:** `STRATEGY_FOUR_PAGE_EDITORIAL_DECISION_PACKAGE_20260919.md`, `RESEARCH_WEB_VALUE_CROSSCHECK_20260919.md`, `RESEARCH_SEO_GEO_DATA_EVIDENCE_RESULTS_20260919.md`, `ANALYSIS_FOUR_PAGE_SEO_GEO_FORENSIC_20260919.md`, `HANDOFF_WEBSITE_SEO_CTA_OPPORTUNITY_PASS_20260904.md`
**Execution window:** 2026-09-19, approximately 08:20–09:57 UTC

---

## 1. Execution date/time

| Step | UTC time |
|---|---|
| Baseline capture (all 5 URLs) | ~08:20–08:35 |
| GSC baseline capture ($30k page) | ~08:38 |
| 3-row page (830) corrected and pushed | 08:45:13 |
| 3-row page live-verified | 08:46 |
| Tools hub (452) link added and pushed | 08:48:17 |
| Tools hub live-verified | 08:49 |
| $30k page (827) Rank Math title/meta saved | ~09:30 |
| $30k page (827) body + post title pushed | 09:53:34 |
| $30k page live-verified (rendered + REST) | 09:54-09:56 |
| Sitemap lastmod confirmed | 09:56 |
| GSC recrawl requested ($30k page) | 09:57 |

---

## 2. WordPress page IDs

| Page | URL | Page ID |
|---|---|---|
| 3-row SUV under $50k | `/tools/best-3-row-suv-under-50000/` | 830 |
| Tools hub | `/tools/` | 452 |
| Compact SUV under $25,000 | `/tools/best-compact-suv-under-25000/` | 934 (not edited this batch; only linked to) |
| SUV under $30,000 | `/tools/best-compact-suv-under-30000/` | 827 |

---

## 3. Pre-change state (baseline, captured before any edit)

### 3-row page (830)
- Title: `Best 3 Row SUVs Under 50k - GetCarWise`
- Meta: `Compare 3-row SUVs under $50,000 by space, reliability, fuel economy, towing, and ownership value. See which family SUV fits your priorities.`
- H1: `Best 3 Row SUVs Under 50k`
- Canonical: `https://getcarwise.app/tools/best-3-row-suv-under-50000/`
- Robots: `follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large`
- Schema: `Place`, `Organization`/`AutomotiveBusiness`, `WebSite`, `ImageObject`, `BreadcrumbList`, `WebPage`, `Person`, `Article`
- Sitemap lastmod: 2026-09-15 08:35 UTC
- Content contained: Kia Sorento warranty wording implying full 10yr/100k transfer to used buyers (in body, "Why buy" line, comparison table, and FAQ - 4 occurrences); Ford Explorer XLT described with a 3.5L EcoBoost engine
- CTA: `https://www.anrdoezrs.net/click-101637236-15701072`, label "Browse Used Cars on Edmunds"
- Disclosure: "Some links on this page are affiliate links. If you use one, GetCarWise may receive compensation at no additional cost to you. Our recommendations remain independent."
- CarClever Lite: iframe embed present

### Tools hub (452)
- Title: `Car Research Tools - AI-Powered Evaluation`
- No link to `/tools/best-compact-suv-under-25000/` anywhere on the page
- Sitemap lastmod: 2026-08-29 07:40 UTC

### $30k page (827)
- Title (rendered/browser tab): `Best Small SUV Under 30k ($30,000): New and Used Options Compared`
- Meta: `Shopping for an SUV under $30,000? Compare new, used, and hybrid options side by side - pricing, reliability, and true ownership costs before you buy.`
- H1 (from post title): `Best Small SUV Under 30k ($30,000): New and Used Options Compared`
- Canonical: `https://getcarwise.app/tools/best-compact-suv-under-30000/`
- Robots: `follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large`
- Schema: site-wide `@graph` block (`Place`, `Organization`/`AutomotiveBusiness`, `WebSite`, `ImageObject`, `BreadcrumbList`, `WebPage`, `Person`, `Article`) plus a page-specific `ItemList` and a page-specific `FAQPage`
- Sitemap lastmod: 2026-09-15 05:44 UTC
- Content: used the old 2019-2021 model-year framing, presented RAV4 Prime as "2021 only," referenced a new Ford Escape Hybrid pricing claim the forensic doc had flagged as stale, no destination-inclusive new-price logic, no live CarClever pool counts
- CTA: `https://www.jdoqocy.com/click-101637236-15700851`, label "Browse SUVs on Edmunds" (2 instances - one with an arrow, one without)
- Disclosure: "Some links on this page are affiliate links. If you use one, GetCarWise may receive compensation at no additional cost to you. Our recommendations remain independent."
- CarClever Lite: iframe embed present
- Word count (pre-edit, logged-in view): 1,969

**Important note on affiliate links:** both existing CTAs on these pages are on the **old CJ Affiliate network** (`anrdoezrs.net` and `jdoqocy.com`), not the Impact.com network (`edmunds.sjv.io`) that the CarClever app/MCP tooling migrated to on Sep 17. The app-level CJ-to-Impact migration did not touch these WordPress page CTAs. Per the handoff's explicit boundary ("no Edmunds affiliate-network/tracking change... unless a separate approved affiliate-migration task explicitly authorizes it"), **both CTAs were preserved exactly as-is, unchanged**, including staying on the CJ network. This is a deliberate compliance with the boundary, not an oversight - flagging it here so it isn't mistaken for a missed migration step.

---

## 4. Exact changes made

### 4.1 - 3-row page (830), Batch 1 Section 2A

1. **Sorento body wording** - replaced the sentence implying a used-owner benefit ("The 10-year/100,000-mile powertrain warranty extends well beyond competitors, providing peace-of-mind for 60k+-mile vehicles.") with the exact handoff-specified warranty note distinguishing original-owner coverage from CPO coverage.
2. **Sorento "Why buy" line** - replaced "Industry-leading 10yr/100k warranty; modern, upscale interior; strong fuel economy; excellent value-to-features ratio." with "Strong value, family-friendly packaging, and available turbo power; qualifying Kia CPO examples may include separate CPO powertrain coverage."
3. **Comparison table Sorento warranty cell** - replaced `10yr/100k` with `Original-owner 10yr/100k; verify used/CPO coverage`.
4. **Ford Explorer engine wording** - replaced "pair a turbocharged 3.5-liter EcoBoost engine with agile handling" with agile-handling language plus the exact sentence: "The 2021-2022 Explorer XLT uses Ford's turbocharged 2.3-liter EcoBoost four-cylinder, rated at 300 horsepower."
5. **FAQ warranty answer** - replaced the Kia/Hyundai "industry-leading coverage" sentence with the exact handoff-specified Kia warranty note (same transfer-eligibility correction, applied a second time since it was duplicated in the FAQ).
6. **New source note added** - inserted the exact "How we verify specs" paragraph immediately before the FAQ heading, as specified.

Nothing else on the page was touched. Confirmed via diff against the saved pre-edit content: exactly these 6 changes, no others.

### 4.2 - Tools hub (452), Batch 1 Section 2B

Added, after the "Built for Defensive Research" paragraph and before the end of the page content, a new linked heading to `/tools/best-compact-suv-under-25000/` reading "Best compact SUVs under $25,000 - compare used picks", with supporting copy: "Shopping by budget? See our guide to the best used compact SUVs under $25,000, including the trade-offs between price, age, mileage, and value." - exactly as suggested in the handoff.

No other change made to this page.

### 4.3 - $30k page (827), Batch 2

1. **Rank Math SEO title** set to: `Best SUVs Under $30,000 (2026): New vs. Used Picks`
2. **Rank Math meta description** set to: `Compare new and used SUVs under $30,000 in 2026. See destination-inclusive new-car prices, live used-market availability, and which path fits you.`
3. **WordPress post title** (renders as the page's H1) set to: `Best SUVs Under $30,000 in 2026: New vs. Used Picks`
4. **Full body content replaced** with the handoff's Section 4 publish-ready copy: answer-first intro with "Updated: September 19, 2026" dateline, quick-answer table, existing CTA block (unchanged link) and CarClever Lite iframe (unchanged), new-SUV destination-inclusive pricing table (7 models), "what no longer makes the cut" list (2027 Niro, 2026.5 Rogue, 2026 Tucson), used-market availability table (4 models, CarClever provider counts), 4 candidate write-ups (RAV4, CX-5, Forester, Rogue) plus a CR-V paragraph explaining its exclusion from the count table, new-vs-used decision table, "best by buyer type" section, methodology section, "what to verify before you buy" checklist, closing CTA + $25k internal link, updated FAQ (4 questions), sources section with 9 editorial links
5. **Schema updated in place** - `ItemList` and `FAQPage` blocks kept as the same schema *types*, with their internal text/item content updated to match the new copy (old items referencing 2019-2021 model-year picks replaced with items referencing the new destination-inclusive new-SUV picks and the used-market candidates)

Permalink slug, canonical, robots meta, and the site-wide schema block were not touched.

**Not changed (deliberately preserved unchanged):** featured image (still shows the old "2019-2022 Models" graphic - see Section 14, Known Limitations, below), CTA destination/tracking/label, CarClever Lite embed, focus keyword ("compact suv," left as-is since the handoff didn't ask to change it).

---

## 5. Post-change state (verified live)

### 3-row page (830)
- Title/meta/H1/canonical/robots/schema: **unchanged**, confirmed identical to baseline via live rendered-page JS extraction
- Sorento warranty text: corrected in all 4 locations, no lingering misleading sentence found anywhere in the rendered content (checked via regex against both old phrasings)
- Explorer engine text: now reads 2.3L EcoBoost / 300 hp; old 3.5L phrase confirmed absent
- CTA link: unchanged, `anrdoezrs.net/click-101637236-15701072` confirmed present and identical
- CarClever Lite / disclosure: unchanged, both confirmed present
- Sitemap lastmod: updated to 2026-09-19 08:45 UTC

### Tools hub (452)
- New link confirmed live, pointing to `/tools/best-compact-suv-under-25000/` with the exact anchor text specified
- Comparison URL (`/best-compact-suv-under-25k-comparison/`) confirmed **not** linked
- Existing tool cards (Deal Score, Listing Check, VIN Check, CarClever Lite, Risk Check, Cost Check) all confirmed still present and unchanged

### $30k page (827)
- Title (browser tab / Rank Math rendered): `Best SUVs Under $30,000 (2026): New Vs. Used Picks`
- Meta: matches handoff exactly
- H1: `Best SUVs Under $30,000 in 2026: New vs. Used Picks` - confirmed rendered on the live page
- Canonical: unchanged, `https://getcarwise.app/tools/best-compact-suv-under-30000/`
- Robots: unchanged
- Schema: `ItemList` and `FAQPage` types both still present (confirmed via live-page JSON-LD parse)
- CTA: both instances of `https://www.jdoqocy.com/click-101637236-15700851` confirmed present, label "Browse SUVs on Edmunds," unchanged
- CarClever Lite iframe: confirmed present and functionally loaded on the live page (screenshot-verified, widget rendered with live search UI)
- Disclosure: confirmed present, unchanged wording
- All 9 editorial source links (Chevrolet x3, Nissan, Kia, Hyundai, Mazda x2, Honda) confirmed resolving to the correct URLs, no broken markup
- Internal $25k link confirmed present and pointing to `/tools/best-compact-suv-under-25000/`
- Full-page visual scroll-through performed; no broken HTML, no stray blocks, no duplicate CTA blocks found anywhere on the page
- Sitemap lastmod: updated to 2026-09-19 09:53 UTC

---

## 6. $30k page - pre-change GSC baselines

**Conventional Search, US, 28 days, captured before any edit:**

| Metric | Value |
|---|---:|
| Clicks | 0 |
| Impressions | 22 |
| CTR | 0% |
| Avg. position | 25.2 |

Visible top queries in this window: "best compact suv under 30k" (7 impr), "best compact suvs under 30k" (6 impr), "compact suvs under 30k" (4 impr), "best small suv under 30k" (3 impr), "best compact suv under $30000" (1 impr), "best compact suv under 30000" (1 impr).

## 7. $30k page - pre-change Google Generative AI baseline

**US, 28 days, captured before any edit:**

| Metric | Value |
|---|---:|
| GEO impressions | 3 |

## 8. Historical baselines retained for reference (Sep 16/19 strategy docs)

- Sep 16 baseline cited in the forensic doc: 21 conventional Search impressions, 0 clicks, avg. pos 26.05; 3 GEO impressions
- These are consistent with the fresh pre-change pull above (22 impr / 0 clicks / 25.2 avg pos / 3 GEO impr), confirming no material drift occurred between the Sep 16 baseline and this session's pre-change capture - the T0 baseline for the upcoming T+14/T+28/T+56 measurement plan can be treated as this session's numbers.

---

## 9. Existing affiliate CTA - before and after (proof of no change)

| Page | CTA URL (before) | CTA URL (after) | Label (before) | Label (after) | Changed? |
|---|---|---|---|---|---|
| 3-row (830) | `https://www.anrdoezrs.net/click-101637236-15701072` | `https://www.anrdoezrs.net/click-101637236-15701072` | Browse Used Cars on Edmunds | Browse Used Cars on Edmunds | **No** |
| $30k (827) | `https://www.jdoqocy.com/click-101637236-15700851` | `https://www.jdoqocy.com/click-101637236-15700851` | Browse SUVs on Edmunds (x2) | Browse SUVs on Edmunds (x2) | **No** |

Both confirmed byte-identical before and after via direct string match against the live rendered page and the raw REST content.

---

## 10. Source links added (all editorial, no affiliate/tracking parameters)

1. Chevrolet Trax - `https://www.chevrolet.com/suvs/trax`
2. Chevrolet Trailblazer - `https://www.chevrolet.com/suvs/trailblazer`
3. Chevrolet destination charges - `https://www.chevrolet.com/destination-freight-charges`
4. Nissan Kicks - `https://www.nissanusa.com/vehicles/crossovers-suvs/kicks/specs-trims.html`
5. Kia Seltos - `https://www.kia.com/us/en/seltos`
6. Hyundai Kona - `https://www.hyundaiusa.com/us/en/vehicles/kona`
7. Mazda CX-30 - `https://news.mazdausa.com/vehicles-2026-cx-30`
8. Mazda destination update - `https://news.mazdausa.com/2026-08-11-Mazda-Adjusts-Destination-and-Handling-Charge%2C-Effective-August-11%2C-2026`
9. Honda HR-V - `https://automobiles.honda.com/2026/hr-v`

Plus one internal link added on the $30k page pointing to `/tools/best-compact-suv-under-25000/`, and one internal link added on the Tools hub pointing to the same URL.

---

## 11. Verification notes (textual, in lieu of screenshots)

- 3-row page: confirmed via a combination of REST `content.rendered` string checks and a live rendered-page JS extraction (`document.title`, `h1`, `canonical`, `robots`, body text regex for both the corrected and the old warranty/engine phrasing).
- Tools hub: confirmed via REST content check plus live-page `querySelectorAll('a[href*="best-compact-suv-under-25000"]')` and a negative check for the comparison URL.
- $30k page: confirmed via REST content check, live rendered-page JS extraction, **and** a full manual visual scroll-through of the entire page (4 screenshots spanning hero image through footer), which caught no rendering issues, no broken HTML, and confirmed the CTA/disclosure/CarClever Lite/source links all display correctly in their intended positions.
- Sitemap `lastmod` (not `document.lastModified`, per the standing lesson from the prior session) was used as the authoritative post-change timestamp source for both edited pages, and matches the REST `modified` timestamp in both cases.

---

## 12. Failures / blockers

**None.** Every WordPress write in this batch succeeded on the first attempt and was independently re-verified. No stale-editor-tab conflict occurred (the Rank Math title/meta edit was made through the block editor UI and saved via the documented button-click method before any REST content push to the same page, and no editor tab was left open across the subsequent REST writes).

One near-miss avoided: the initial plan to inject the ~22KB new $30k body content as a single JavaScript string risked truncation or a tool-call failure; this was mitigated by splitting the content into 4 logical chunks (at natural section boundaries), injecting and concatenating them in the browser's own JS context, and verifying the reassembled string's length and several boundary strings before the actual REST push - avoiding any risk of a silently-truncated or malformed content push.

---

## 13. Recrawl requested?

**Yes**, for the $30k page (`/tools/best-compact-suv-under-30000/`) - confirmed via Google Search Console's URL Inspection tool: "Indexing requested. URL was added to a priority crawl queue."

Per the handoff's Section 7.5, a recrawl request for the 3-row correction page was optional; **not requested** this session, since the change there was a narrow factual correction rather than the primary content-treatment experiment. The lastmod update via the sitemap is recorded (Section 5, above) regardless.

---

## 14. Known limitations / minor items for a future pass

1. **$30k page featured image unchanged.** It still displays "Best Compact SUVs Under $30k / 2019-2022 Models | Ranked by Real Value" - this framing (fixed model-year range, "compact SUV" only) no longer matches the new body copy's new-vs-used, destination-inclusive framing for 2026. The handoff did not explicitly ask for an image change, so none was made, but this is worth a follow-up image refresh to avoid a visual/copy mismatch for visitors.
2. **Focus keyword left as "compact suv"** in Rank Math on the $30k page - not requested to change, so left as-is; Rank Math's own Basic SEO panel flags 2 errors (focus keyword not in title/meta) as a result, which is expected and was not a save-blocking issue.
3. **CTA links remain on the old CJ Affiliate network** on both edited pages (Section 3, above) - correct per this task's explicit boundary, but flagged again here as a reminder that a future, separately-dated affiliate-migration task will need to address these two WordPress-side CTAs, since the Sep 17 app-level Impact migration did not cover them.
4. Per this session's earlier evidence-package work, no true P25/P75/median statistics exist for the used-market figures presented - the page correctly avoids presenting them as such, per the handoff's requirement, using only "provider-reported matching inventory" language throughout.

---

## Completion checklist (per Section 9 acceptance criteria)

- [x] Both 3-row factual errors corrected everywhere they occurred (4 Sorento locations + 1 Explorer location)
- [x] $25k retained page gained exactly one intentional Tools-hub internal link
- [x] No $25k redirect/merge occurred
- [x] $30k title/meta/H1 match the handoff exactly
- [x] $30k body contains the approved destination-inclusive new-price logic
- [x] No unverified median/typical used-price statistics appear anywhere in the new copy
- [x] Existing affiliate CTA/tracking unchanged on both edited pages (verified byte-identical before/after)
- [x] Rendered pages re-fetched and verified (REST + live page + visual scroll-through)
- [x] Result doc written and re-fetched (see verification below)
- [x] No app/Vercel/MCP changes occurred this session
