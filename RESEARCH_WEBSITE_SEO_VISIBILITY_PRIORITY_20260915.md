# GetCarWise Website SEO / GEO Visibility Priority Research — 2026-09-15

**Status:** Research complete; implementation decisions remain page-specific.
**Lane:** ChatGPT Business/Strategy
**Scope:** GetCarWise website visibility, content, schema, internal linking, authority and manual WordPress/Rank Math work. No application-code changes.

## Executive finding

The Sep 15 engineering report and Semrush On-Page Checker findings are directionally consistent: the major remaining visibility constraint is not a hidden technical penalty. It is weak page-one coverage, insufficient content depth on ranking pages, and very low real external authority.

The highest-leverage near-term opportunity is `/tools/best-compact-suv-under-30000/`. A second SEO source (Ubersuggest, US database) currently estimates `best suv under 30000` at approximately position 13 with search volume about 880. This makes it the clearest near-page-one opportunity and justifies concentrating content, internal-link and link-earning effort there rather than distributing work evenly across all Semrush pages.

Semrush API extraction is currently blocked by zero API units, consistent with the engineering report. Treat its current UI/report snapshot as the latest available Semrush evidence until quota resets.

## Priority order

### P0 — Do not implement inaccurate schema suggestions

1. **Do not add `AutoDealer` schema to `/tools/deal-score/`.** `AutoDealer` represents a car dealership/local automotive business. GetCarWise is not a dealership, and the page is a calculator/tool.
2. **Do not add `WebSite` schema to the Honda Accord article as a page-level fix.** Google's site-name guidance requires `WebSite` structured data on the site's home page. Check the homepage for an existing WebSite node before adding or changing anything.
3. **Do not assume ItemList = Google carousel eligibility.** Google's documented host-carousel ItemList rich result is limited to supported content types such as Course, Movie, Recipe and Restaurant; a generic vehicle recommendation list does not automatically qualify. ItemList may still be semantically valid if it truthfully matches visible page content, but it should not be sold as a guaranteed rich-result opportunity.
4. Validate any added schema against visible page content and Google's Rich Results Test / Schema validator. Do not add schema solely because Semrush suggests a type.

### P1 — Best SUVs Under $30,000 page

URL: `/tools/best-compact-suv-under-30000/`

Why first:
- Prior GSC evidence showed hundreds of impressions and zero clicks across the core $30k SUV query family before the recent title/H1 work.
- Ubersuggest now estimates the head term `best suv under 30000` around position 13 (US; volume ~880).
- Claude already corrected title and H1. Rewriting them again immediately would create unnecessary churn before Google has fully reprocessed the change.

Next work:
- Deepen the body content rather than changing title/H1 again.
- Add genuinely useful comparison information: new vs used trade-offs at $30k, real model-year/trim context, hybrid availability, fuel economy, cargo/passenger fit, warranty/CPO implications, and a concise buying checklist.
- Make the page answer the decision question directly: which SUV under $30k is best for which buyer.
- Add a compact comparison table near the top and scannable sections below it.
- Add natural variants of the ranking query in visible copy without stuffing.
- Strengthen internal links from relevant high-context pages (Tools hub, SUV/$25k page, 3-row pages, PHEV page where relevant, related ownership-cost content).
- After substantive content changes, inspect/request recrawl in GSC.
- Use this page as the first link-earning asset because it is already close to page one.

### P2 — Best 3-Row SUVs Under $50,000

URL: `/tools/best-3-row-suv-under-50000/`

Current external directional signal: Ubersuggest estimates `3rd row suv under 50k` around position 28.

Next work:
- Manually correct the Rank Math meta description if still outstanding.
- Expand useful body content and improve readability.
- Cover 3-row practicality, cargo trade-offs with all rows up, fuel economy, hybrid choices, towing where relevant, family-safety/use-case differences and ownership-value considerations.
- Use `3-row SUV`, `fuel efficiency` and related language naturally.
- Recheck indexed title/snippet after Google recrawls; current search index may lag the live title change.

### P3 — Best Compact SUVs Under $25,000

URL: `/tools/best-compact-suv-under-25000/`

This page was not the main focus of the Sep 15 40-idea list, but the second SEO source shows a broader ranking footprint than several listed pages: multiple $25k SUV variants are around positions 36–47, with estimated volumes up to ~390.

Next work:
- Preserve the Sep 6 title/meta/CTA work.
- Audit content depth and whether the page clearly distinguishes realistic new vs used availability under $25k.
- Improve decision usefulness and internal linking; this is a stronger content-upgrade candidate than lower-evidence pages.

### P4 — Used PHEV page

URL: `/tools/best-used-phev-plug-in-hybrid/`

Directional rankings include multiple relevant terms in roughly the 40s–70s, including `best used plug in hybrid suv` and broader PHEV-list terms.

Next work:
- Keep used-only intent clear unless a separate page is deliberately created for all/new PHEVs.
- Expand model comparison depth, EV range, charging practicality, reliability/warranty considerations and used-PHEV battery/inspection guidance.
- Avoid broad keyword expansion that weakens the page's used-car intent.

### P5 — Highlander alternatives and Honda Accord pages

Proceed with content-quality upgrades after the pages above unless GSC shows stronger impression opportunity.

Highlander page:
- Expand alternatives by buyer use case, including hybrid-powertrain context and Ford Explorer where genuinely relevant.
- Focus on comparative differences rather than adding semantic phrases mechanically.

Honda Accord page:
- Add accurate EPA-style fuel-economy/trim context only when verified from reliable sources.
- Improve trim comparison, real-world buyer guidance, comfort and efficiency trade-offs.
- Use Article/BlogPosting-style page semantics if appropriate; do not add WebSite schema to the article as a substitute for homepage WebSite markup.

### P6 — Deal Score tool page

The public page is thin because it is a pure iframe/tool surface; prior WordPress investigation confirmed the sparse rendered content is architectural rather than a missing article block.

If organic ranking for Deal Score is strategically important, the correct fix is to add useful crawlable explanatory HTML around/outside the iframe (what Deal Score measures, how to interpret it, example factors, limitations, FAQ). This is more important than adding an unrelated LocalBusiness/AutoDealer schema type.

Ownership:
- ChatGPT: content specification/copy.
- André/manual: WordPress/Rank Math if editable in the page builder.
- Claude: implementation only if the iframe/page architecture requires engineering work.

## Homepage

The Semrush `car search` semantic suggestion is low priority compared with the ranking pages above. Check whether homepage already contains a correct WebSite node and Organization/brand markup before adding schema. If WebSite markup is absent, the homepage—not an internal vehicle article—is the correct location for site-name WebSite structured data.

## Authority / backlinks

Google's own Links report (per Sep 15 engineering audit) shows only five real external links from four domains. This is the clearest authority gap.

Prioritise quality and relevance over raw referring-domain count. The recent rise in Semrush referring domains is largely spam/link-farm noise and must not be reported as traction.

Best first link-earning approach:
1. Turn the $30k SUV page into a genuinely citeable asset with explicit methodology and a useful comparison table.
2. Pursue realistic automotive/dealer/editorial outreach where the page adds value (for example relevant dealer resource pages and automotive publishers), rather than assuming large publishers will link because Semrush listed them.
3. Pitch data/methodology or expert commentary, not generic reciprocal-link requests.
4. Track earned links by source quality, relevance, target page and resulting impressions/rank movement.

## Manual work queue for André + ChatGPT

1. `/best-3-row-suv-under-50000/`: Rank Math meta description check/fix.
2. Homepage: inspect existing Rank Math schema; confirm whether WebSite + Organization/brand nodes already exist. Do not add duplicates.
3. Target pages: inspect current schema types before adding anything; reject AutoDealer on Deal Score and internal-page WebSite markup.
4. GSC URL Inspection after major page changes to confirm canonical, crawl/index state and request recrawl where appropriate.
5. GSC performance pull when convenient: compare the post-Sep-3 period and identify pages/queries closest to positions 8–20 with meaningful impressions.

## ChatGPT content work queue

1. Draft the `$30k SUV` page content expansion first.
2. Draft the `$50k 3-row SUV` expansion second.
3. Audit and draft `$25k compact SUV` content expansion third.
4. Prepare internal-link map and anchor suggestions for these clusters.
5. Prepare backlink outreach targets and tailored pitches once the first linkable page is strengthened.

## Claude handoff queue

Only after content/manual decisions are settled:
- Implement page/content changes that require WordPress/Chrome or engineering access.
- If Deal Score needs crawlable static HTML but the current pure-iframe architecture prevents a normal WordPress content block, implement the approved page architecture change.
- Re-run the Semrush Site Audit URL-level issue list once quota/UI access returns; isolate the one structured-data error, long-title pages, nofollow internal links and missing meta page.
- Verify rendered output after each change.

## Monitoring

- Recheck GSC indexing approximately 1–2 weeks after the Complianz crawl-noise fix, as already recommended in the Sep 15 engineering report.
- Do not over-read Core Web Vitals/Clarity or week-to-week traffic until volume is sufficient.
- Allow Google time to reprocess the Sep 15 title/H1 changes before judging CTR/rank effects.
- When Semrush quota returns, rerun organic research and URL-level Site Audit rather than relying indefinitely on the cached Aug 3 audit.

## Decision status

This document records prioritised research and recommended sequencing. It does not authorise unrelated application changes, does not change any in-review app package, and does not make any pending app retirement/migration decision final.
