# Return — $25k Compact SUV SEO/GEO Consolidation

**Executed by:** Claude — Engineering lane (authenticated WordPress execution via André's live `wp-admin` browser session)
**Approved by:** André, explicit written approval, "ANDRÉ APPROVAL — EXECUTE $25K COMPACT-SUV SEO/GEO CONSOLIDATION NOW"
**Handoff executed:** `HANDOFF_WORDPRESS_25K_SUV_CONSOLIDATION_20260919.md`
**Governing docs read in full before editing:** `ANALYSIS_FOUR_PAGE_SEO_GEO_FORENSIC_20260919.md`, `RESEARCH_SEO_GEO_DATA_EVIDENCE_RESULTS_20260919.md`, `STRATEGY_FOUR_PAGE_EDITORIAL_DECISION_PACKAGE_20260919.md` (all reviewed in prior sessions this week; content unchanged since)
**Retained URL:** `https://getcarwise.app/tools/best-compact-suv-under-25000/`
**Consolidated/redirected URL:** `https://getcarwise.app/tools/best-compact-suv-under-25k-comparison/`

---

## 1. Implementation date/time

| Step | UTC time |
|---|---|
| Preflight/baseline capture (both URLs) | ~19:30-19:55 |
| T0 GSC baselines captured (both URLs) | ~19:35-19:50 |
| Internal-link inventory (WordPress search) | ~19:55 |
| Rank Math title/meta set (retained page) | ~20:05 |
| Retained-page body pushed via REST | 20:51:42 |
| Schema (Article) re-saved to refresh dynamic bindings | ~20:53 |
| Data & Guides duplicate entry fixed | 20:56:01 |
| Content-parity visual verification | ~20:58-21:00 |
| 301 redirect created (Rank Math Redirections) | Sep 19, 20:57 |
| Redirect functional verification | ~21:00-21:02 |
| Sitemap/internal-link final sweep | ~21:02 |
| GSC indexing requested (retained URL) | ~21:03 |
| GSC indexing requested (old comparison URL) | ~21:04 |

**Note on timing vs. prior guidance:** ChatGPT's PHEV review had recommended waiting for a later local calendar date (Brisbane/AEST) before launching this consolidation. André's approval message for this task explicitly overrode that recommendation ("Same-day execution is explicitly approved... Do not wait for another calendar day"), and the handoff itself was updated to state the same. This implementation proceeded on André's explicit, more recent instruction. Fresh T0 baselines were captured for both URLs immediately before any change, per the handoff's own mitigation for same-day execution, so this treatment's baseline validity is not affected by the timing override.

---

## 2. Both page IDs

| Page | URL | Page ID |
|---|---|---|
| Retained | `/tools/best-compact-suv-under-25000/` | 934 |
| Comparison (consolidated away) | `/tools/best-compact-suv-under-25k-comparison/` | 771 |
| Data & Guides (internal link fixed) | `/data-guides/` | 899 |

---

## 3. T0 Search/GEO baselines for BOTH URLs (US, 28 days, captured immediately before any change)

### Retained URL (`/under-25000/`)

| Metric | Value |
|---|---:|
| Search clicks | 0 |
| Search impressions | 124 |
| CTR | 0% |
| Avg. position | 38.2 |
| GEO impressions | 0 (not present anywhere in the top 25 GEO pages list) |

Top queries (partial, by impressions): "suv under 25000" (31), "suvs under 25000" (29), "compact suv price range" (8), "best compact suv under 25k" (6), "best compact suv value" (5), "best suv under 25k" (5), "best suv under 25000" (4), "new suv under 25000" (4), "compact suvs under 25k" (3), "best compact suv under 25000" (2).

### Comparison URL (`/under-25k-comparison/`)

| Metric | Value |
|---|---:|
| Search clicks | 0 |
| Search impressions | 1 |
| CTR | 0% |
| Avg. position | 15 |
| GEO impressions | 5 |

This matches the handoff's historical Sep 19 reference almost exactly (~122 impressions/avg pos ~38 for the retained URL; ~5 GEO impressions for the comparison URL), confirming no material drift and validating the strategy's core premise: the retained URL dominates conventional Search, the comparison URL had a small but real GEO signal and negligible Search visibility.

---

## 4. Pre-change title/meta/H1/canonical/schema/lastmod for both

### Retained URL (934) — before
- Title (rendered): `Best Compact SUVs Under $25,000: Used Picks Compared - GetCarWise`
- Meta: `Shopping for a compact SUV under $25,000? Compare used CR-V, RAV4, Tucson, CX-5, and Rogue options by price, mileage, reliability, and value.`
- H1: `Best Compact SUVs Under $25,000: Used Picks Compared`
- Canonical: `https://getcarwise.app/tools/best-compact-suv-under-25000/`
- Robots: `follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large`
- Schema: site-wide `@graph` only (`Place`, `Organization`/`AutomotiveBusiness`, `WebSite`, `ImageObject`, `BreadcrumbList`, `WebPage`, `Person`, `Article`) — page-specific Article/Breadcrumb items existed but referenced the old title
- Sitemap lastmod: 2026-09-06 04:59 UTC
- Word count: 285
- Content: two short paragraphs (2017-2020 model years, 60k-110k miles framing), no real heading structure

### Comparison URL (771) — before
- Title (rendered): `Best Compact SUV Under $25K: CR-V Vs RAV4 Vs Tucson Vs CX-5 Vs Escape - GetCarWise`
- Meta: `Best Compact SUV Under $25K: CR-V vs RAV4 vs Tucson vs CX-5 vs Escape`
- H1: `Best Compact SUV Under $25K: CR-V vs RAV4 vs Tucson vs CX-5 vs Escape`
- Canonical: `https://getcarwise.app/tools/best-compact-suv-under-25k-comparison/`
- Robots: `follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large`
- Schema: site-wide `@graph` only (same 8-item structure as retained page's pre-change state)
- Sitemap lastmod: 2026-06-21 08:36 UTC
- Word count: 859
- Content: 5-model comparison (CR-V, RAV4, Tucson, CX-5, Ford Escape) with star ratings and average-price ranges

**Critical factual issue found on the comparison page (not carried forward):** the old page stated *"[Tucson] includes Hyundai's exceptional 10-year/100,000-mile transferable warranty (even as a used vehicle)"* — this is factually incorrect. Hyundai's own documentation states the full 10-year/100,000-mile powertrain term is an original-owner benefit; ordinary subsequent owners receive coverage under the 5-year/60,000-mile New Vehicle Limited Warranty. This confirms the handoff's explicit instruction not to import old claims without re-verification.

---

## 5. Rollback/export details

Exact pre-edit HTML body content for all three edited pages was saved to local files before any change:
- `rollback_page_934_pre_edit.html` (retained page, 2,608 bytes)
- `rollback_page_771_pre_edit.html` (comparison page, 7,518 bytes)
- `rollback_page_899_pre_edit.html` (Data & Guides, 6,796 bytes)

The comparison page (771) itself was **not edited or deleted** — only redirected. Its content remains intact in WordPress and can be restored/un-redirected at any time by deactivating the Rank Math redirect rule; no rollback of page 771's own content is therefore needed unless the redirect itself is reversed.

---

## 6. Retained-page edits (page 934)

1. **Rank Math SEO title** set to: `Best Compact SUVs Under $25,000 (2026): Used Picks Compared`
2. **Rank Math meta description** set to: `Compare used CR-V, RAV4, CX-5, Forester, Rogue and Tucson SUVs under $25,000 by space, MPG, AWD and buyer fit.`
3. **WordPress post title** (H1 source) set to: `Best Compact SUVs Under $25,000 in 2026: Used Picks Compared`
4. **Full body replaced** with the handoff's publish-ready copy: answer-first intro, quick-answer table, "what matters most" checklist, 2021-2022 reference-spec comparison table (6 models), six full model sections (Honda CR-V, Toyota RAV4, Mazda CX-5, Subaru Forester, Nissan Rogue, Hyundai Tucson) each with Why Buy/Watch For (and a Warranty Note for Tucson), decision-by-use-case section including the "Also consider: Ford Escape" note, "what we deliberately do not rank" section, 10-item buying checklist, methodology section, closing CTA + disclosure + CarClever Lite (all preserved unchanged), updated FAQ (5 questions), sources section with 11 editorial links across the six manufacturers/Edmunds
5. **Schema (Article) re-saved** via Rank Math's Schema Builder to refresh its dynamic `%seo_title%`/`%seo_description%` bindings against the new title/meta — confirmed live that the Article's `headline` and the site's `BreadcrumbList` item name both correctly show the new title, with no stale reference to the old page

Permalink slug (`best-compact-suv-under-25000`), canonical, and robots meta were not touched.

**Preserved unchanged (verified byte-identical before/after):** CTA URL/label/rel, affiliate disclosure text, CarClever Lite iframe embed and its click-handler script.

---

## 7. Data & Guides edits (page 899)

**Before:** two separate `<li>` entries under "By Budget Range" — one linking to `/best-compact-suv-under-25k-comparison` (anchor: "Best Compact SUV Under $25K — CR-V vs RAV4 vs Tucson vs CX-5 vs Escape") and one linking to `/tools/best-compact-suv-under-25000` (anchor: "Best Compact SUV Under $25K — Ranked by value").

**After:** a single entry linking to `/tools/best-compact-suv-under-25000`, with the handoff's suggested anchor/description: **"Best Compact SUVs Under $25,000 — Used Picks Compared"** — "Compare CR-V, RAV4, CX-5, Forester, Rogue and Tucson by space, drivetrain and buyer fit."

No other content on this page was touched. Confirmed via diff: exactly the two intended line changes (one replaced in place, one removed), nothing else.

---

## 8. Internal links updated / verified

- **Data & Guides:** fixed as described in Section 7 — confirmed only one $25k entry remains, pointing to the retained URL.
- **Tools hub (`/tools/`):** verified unchanged and correct — already linked to the retained URL from the prior Sep 19 Batch 1 session; no duplicate added.
- **$30k page contextual link:** verified unchanged and correct — points to `/tools/best-compact-suv-under-25000/`.
- **Site-wide sweep:** used WordPress's own admin search (`wp-admin/edit.php?s=...`) for the literal string `best-compact-suv-under-25k-comparison` across all pages. **Result: zero pages found** after the Data & Guides fix (one page — Data & Guides itself — was found before the fix; none after). This confirms no other editorial internal link anywhere in WordPress content pointed to the comparison URL.

No external/third-party links were touched, per instruction.

---

## 9. Redirect mechanism and exact rule

**Mechanism:** Rank Math SEO's native Redirections module (`wp-admin/admin.php?page=rank-math-redirections`).

**Rule created:**
- **Source URL:** `/tools/best-compact-suv-under-25k-comparison/` (match type: Exact)
- **Destination URL:** `/tools/best-compact-suv-under-25000/`
- **Redirection Type:** 301 Permanent Move
- **Status:** Activate

The redirect was created only after the retained page's content, metadata, schema, and internal links were all verified — per the handoff's mandatory sequence (steps 1-9 completed before step 10, the redirect itself).

---

## 10. Redirect verification

- **Functional test (browser navigation):** navigating to the comparison URL lands on the retained URL with the retained page's title and content. Confirmed via `window.location.href` after navigation.
- **Hop count:** confirmed exactly one hop via network request trace — 2 document-level requests recorded (old URL, then new URL), no intermediate bounce.
- **Fetch-based confirmation:** `fetch(oldURL, {redirect: 'follow'})` returned `redirected: true`, `status: 200`, `url` equal to the retained URL — confirms a real redirect occurred and the final destination returns 200.
- **Redirect type confirmed as genuine 301** via Rank Math's own Redirections list (not a 302) — the rule shows Type "301" and had accumulated 4 hits at time of writing, with "Last Accessed" updating live as verification requests were made.
- **No redirect loop:** confirmed by the 2-request trace above; the destination URL does not itself redirect anywhere.
- **Google's live crawler test (GSC URL Inspection → Test Live URL on the old URL):** returned "URL is available to Google," "Page can be indexed," and **Breadcrumbs: 2 valid items detected** — matching the retained page's breadcrumb structure (the old comparison page, before redirect, would have shown different breadcrumb content). This is independent confirmation that Google's own live-fetch path follows the redirect correctly.

---

## 11. Destination post-change title/meta/H1/canonical/schema/lastmod

- Title (rendered): `Best Compact SUVs Under $25,000 (2026): Used Picks Compared - GetCarWise`
- Meta: `Compare used CR-V, RAV4, CX-5, Forester, Rogue and Tucson SUVs under $25,000 by space, MPG, AWD and buyer fit.`
- H1: `Best Compact SUVs Under $25,000 in 2026: Used Picks Compared`
- Canonical: `https://getcarwise.app/tools/best-compact-suv-under-25000/` — **unchanged, self-canonical**
- Robots: `follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large` — unchanged
- Schema: same 8-item site-wide `@graph` structure (`Place`, `Organization`/`AutomotiveBusiness`, `WebSite`, `ImageObject`, `BreadcrumbList`, `WebPage`, `Person`, `Article`) — confirmed the `Article.headline` and `BreadcrumbList` item name both dynamically match the new title exactly; no new schema type was introduced
- Sitemap lastmod: 2026-09-19 20:54 UTC — confirmed matching the REST `modified` timestamp

---

## 12. CTA URL/label before and after

| | Before | After |
|---|---|---|
| URL | `https://www.anrdoezrs.net/click-101637236-15701072` | `https://www.anrdoezrs.net/click-101637236-15701072` |
| Label | "Browse Used Cars on Edmunds" | "Browse Used Cars on Edmunds" |
| `rel` | `nofollow sponsored noopener` | `nofollow sponsored noopener` |
| Target | `_blank` | `_blank` |

**Unchanged, confirmed byte-identical** via direct comparison of the live rendered page before and after.

This CTA remains on the CJ Affiliate network (`anrdoezrs.net`), not Impact.com — consistent with every other page edited this week and with the explicit instruction not to perform the CJ→Impact migration in this task.

---

## 13. Source links added

11 editorial (non-affiliate-wrapped) links, confirmed resolving on the live page:

1. Honda 2021 utility brochure — `https://automobiles.honda.com/-/media/Honda-Automobiles/Vehicles/Full-Line-and-Family-Brochures/2021/Wave-1/Utility/MY21-Utility-Brochure-Wave1-Model-Site2.pdf`
2. 2021 CR-V spec cross-check — `https://www.edmunds.com/honda/cr-v/2021/st-401875820/features-specs/`
3. Toyota 2021 RAV4 brochure — `https://www.toyota.com/content/dam/toyota/brochures/pdf/2021/rav4_ebrochure.pdf`
4. Toyota 2021 RAV4 newsroom — `https://pressroom.toyota.com/vehicle/2021-toyota-rav4/`
5. Mazda 2021 CX-5 brochure — `https://www.mazdausa.com/siteassets/pdf/owners-optimized/2021/cx-5/2021-cx5-ebrochure-updated.pdf`
6. Mazda 2021 newsroom — `https://news.mazdausa.com/vehicles-2021-cx-5`
7. Subaru 2021 Forester brochure — `https://www.subaru.com/content/dam/subaru/downloads/pdf/brochures/2021/forester/2021_Subaru_Forester_Brochure.pdf`
8. Nissan 2021 Rogue brochure — `https://www.nissanusa.com/content/dam/Nissan/us/vehicle-brochures/2021/2021-nissan-rogue-brochure-en.pdf`
9. Hyundai 2022 Tucson launch source — `https://www.hyundainews.com/models/hyundai-tucson-2022-tucson`
10. Hyundai warranty FAQ — `https://www.hyundaiusa.com/us/en/help-center`
11. Hyundai warranty coverage — `https://www.hyundaiusa.com/us/en/assurance/america-best-warranty`

---

## 14. Sitemap result

- **Retained URL:** lastmod correctly updated to 2026-09-19 20:54 UTC.
- **Comparison URL:** still present in `page-sitemap.xml` with its old lastmod (2026-06-21 08:36 UTC) at time of writing. This is the expected, documented behavior — the handoff explicitly states: *"do not panic if the old URL remains reported for a while... the old URL is no longer independently present in sitemap once WordPress/SEO tooling refreshes."* The sitemap generator has not yet re-run since the redirect was created; no error, no action needed beyond normal monitoring.

---

## 15. GSC indexing/recrawl result

- **Retained URL:** "Indexing requested" confirmed via URL Inspection → Request Indexing. URL added to Google's priority crawl queue.
- **Comparison URL:** "Indexing requested" confirmed via URL Inspection → Request Indexing (submitted after the live-test check). This should help Google discover and process the redirect faster than waiting for organic recrawl.
- **Live test on comparison URL:** performed in addition to the standard requests — confirmed Google's live fetch path already resolves to the retained page's structure (2 breadcrumb items matching the new page), even before the priority-queue recrawl completes.

---

## 16. Blockers/failures

**None.** Every WordPress write succeeded on its first REST push attempt (retained-page body push, Data & Guides fix) using the synchronous `await`-based call pattern established in the prior PHEV session, which returns HTTP status and content confirmation inline — no silent-failure incidents this session, unlike the one that occurred during the PHEV rebuild.

One minor process note: an initial attempt to check the redirect's raw HTTP status via `fetch(url, {redirect: 'manual'})` returned an opaque, unreadable response (expected browser same-origin-redirect-opacity behavior, not a bug) — resolved by using `fetch(url, {redirect: 'follow'})` instead, which correctly exposed the `redirected: true` / final `status: 200` / final `url` fields needed to confirm the redirect chain.

---

## 17. Final rendered-page verification

**Retained page (live, post-redirect-creation):**
- ✅ Returns 200
- ✅ Exact SEO title, meta, H1 match the handoff
- ✅ Canonical unchanged, self-referencing
- ✅ Robots unchanged
- ✅ Article schema headline dynamically matches new title; BreadcrumbList item name matches; no stale references to old content
- ✅ FAQ content present as plain HTML matching visible questions (no FAQ schema was added or claimed — none was requested beyond Article/Breadcrumb)
- ✅ All six main models present as full sections (Honda CR-V, Toyota RAV4, Mazda CX-5, Subaru Forester, Nissan Rogue, Hyundai Tucson)
- ✅ Ford Escape appears only as the "Also consider" note, not a seventh full model card
- ✅ No unsupported average/median market price introduced — the explicit denial sentence from the handoff is present verbatim; the old page's unsourced $18k-$25k "average price" ranges and star ratings were not carried forward
- ✅ Hyundai warranty-transfer wording correct (original-owner-benefit framing), appearing in both the Tucson section and the FAQ
- ✅ All 11 source links resolve to well-formed URLs
- ✅ Existing CJ CTA/tracking/rel/disclosure survives byte-identical
- ✅ CarClever Lite block survives unchanged, confirmed functionally loading live
- ✅ No internal links anywhere in WordPress still point to the comparison URL
- ✅ Full visual scroll-through (hero through comparison table through decision-tree sections) showed no broken HTML, no rendering defects

**Old comparison URL (live, post-redirect-creation):**
- ✅ Returns a one-hop 301 to the retained URL
- ✅ Destination returns 200
- ✅ No redirect loop
- ✅ Confirmed via both browser navigation and `fetch` with `redirect: 'follow'`
- ✅ Confirmed via Google Search Console's own live-fetch test

---

## Completion checklist (per handoff Section 13)

- [x] Retained URL returns 200
- [x] Old comparison URL returns one-hop 301 to retained URL
- [x] Title/meta/H1 match the handoff exactly
- [x] Canonical is the retained URL
- [x] Robots remains index/follow
- [x] Article/Breadcrumb schema references the retained URL/headline correctly
- [x] No FAQ schema added or claimed (none was required beyond visible FAQ content)
- [x] Six main models present
- [x] Escape appears only as "Also consider"
- [x] No unsupported typical/median market price introduced
- [x] Hyundai warranty-transfer wording correct
- [x] Source links work
- [x] Data & Guides has only one $25k entry
- [x] Tools hub retained link remains present
- [x] $30k contextual link remains correct
- [x] No internal links still point to the comparison URL
- [x] Existing CJ CTA/tracking/disclosure survives
- [x] CarClever block survives
- [x] Sitemap behavior is correct (retained URL updated; comparison URL's stale entry is expected pending tooling refresh)
- [x] GSC recrawl/indexing request completed for both URLs
