# Return — Task #70 Revised: $40K Midsize-Sedan New-Car Rebuild With Integrated Impact Funnel

**Task:** #70 revised implementation
**Outcome: COMPLETE — page 828 rebuilt and published**
**Executed by:** Claude — Engineering lane (authenticated WordPress + GSC + Impact.com sessions)
**Handoff executed:** `HANDOFF_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_REBUILD_20260921.md`
**Target:** `https://getcarwise.app/tools/best-midsize-sedan-under-40000/` (WordPress page 828)
**Governing docs read in full at session start:** `RETURN_WORDPRESS_MIDSIZE_SEDAN_40K_INTENT_AUDIT_20260920.md`, `RETURN_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_CONSOLIDATION_20260920.md`, `REVIEW_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_CONSOLIDATION_DECISION_GATE_20260921.md`, `RETURN_WORDPRESS_IMPACT_STATIC_DESTINATION_MAPPING_20260921.md`, `REVIEW_WORDPRESS_IMPACT_STATIC_DESTINATION_MAPPING_20260921.md`, `STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md`, `STRATEGY_MASTER_SEO_GEO_REVENUE_MATRIX_20260919.md`

Page 772 (the $30k Camry/Accord/Altima comparison) was **not edited, not redirected, not canonicalized**. No other WordPress CJ link was migrated. No Publisher Tag, Impact Catalog/C1-C8, app, MCP, code, or Vercel work occurred.

---

## 1. Exact T0 and implementation timestamps

**Fresh T0 captured immediately before editing** (2026-09-21, approximately 03:00-03:05 UTC):

| Window | Clicks | Impressions | CTR | Avg. position |
|---|---:|---:|---:|---:|
| Latest 28 days | 0 | 7 | 0% | 8.0 |
| Latest 3 months | 0 | 65 | 0% | 42.7 |

Both figures identical to every prior capture (Task #68, Task #70 original attempt) — confirmed stable, no drift. This is a fresh capture for this implementation, not a reuse of the earlier decision-gate T0 (which the handoff explicitly said was evidence, not the implementation baseline).

**Complete visible query list, latest 28 days:** "best midsize sedan 2023" (6 impressions), "best sedans under $40k" (1 impression) — unchanged from all prior captures.

**GEO impressions:** 1 (consistent with the Task #70 original-attempt finding; negligible either way).

**Evidence limitation — T0 completeness:** the previous-28-day metrics and device split were **not captured** as part of this implementation session's fresh T0 pull. Only latest-28-day and latest-3-month figures were captured at implementation time (Section above). This is recorded here as a genuine gap in the T0 evidence for this specific implementation pass, not filled in retroactively from other sessions' captures, since doing so would misrepresent when that data was actually gathered relative to this edit. Comparable previous-28-day (avg. position 27.9) and device-split figures do exist from the Task #68 audit two days earlier, but are not substituted here as if they were captured as part of this session's T0.

**Pre-edit URL Inspection/index condition:** not separately captured as part of this implementation session's T0 pull. The page's indexed/crawled state was checked only after publication (Section 14 below: "URL is on Google," page indexed, 2 valid breadcrumb items), not immediately before this edit. This is recorded as an evidence gap for the same reason as above.

**Implementation timestamps:**
- Content + title pushed via WordPress REST: 2026-09-21T03:16:48 UTC
- Rank Math title/meta/schema saved via editor: approximately 2026-09-21 03:20 UTC
- Tools hub link added: 2026-09-21T03:30:42 UTC
- Data & Guides link added: 2026-09-21T03:31:29 UTC
- Data & Guides stale duplicate removed: 2026-09-21T03:32:00 UTC
- GSC indexing requested: approximately 2026-09-21 03:35 UTC
- Single post-publication validation click (New CTA): approximately 2026-09-21 03:38 UTC
- **Corrective pass (this amendment) — Accord/Legacy/threshold content fixes pushed via WordPress REST: 2026-09-21T03:52:18 UTC**

---

## 2. Rollback locations

- **Page 828 rollback — corrected durable location.** The pre-edit editable content/HTML was originally captured during Task #68 (2026-09-19) as a local file (`rollback_page_828_pre_audit.html`) inside Claude's ephemeral bash container. That location is **not durable** — it does not persist across sessions or survive independently of this conversation. As part of this corrective pass, that exact file was pushed, unmodified, into the `getcarwise-docs` repository at:

  **`getcarwise-docs/ROLLBACK_WORDPRESS_PAGE_828_PRE_TASK70_REBUILD_20260919.html`**

  Pushed as commit `4292f87f0aff41805aabcc3665e456915d9f8425` and re-fetched to confirm a byte-for-byte match with the original local file. This is now the durable rollback reference for page 828's pre-rebuild state. Before this edit was made, the page's WordPress `modified` timestamp and content length were re-verified identical to this capture, confirming the file was still an accurate representation of the page immediately prior to the rebuild.
- A fresh pre-edit screenshot was also taken this session as an additional visual record; this remains local only, since the HTML capture is the substantive durable artifact.
- **No rollback was needed for page 772**, since it was not edited.
- **Tools hub (page 452) and Data & Guides (page 899):** the exact pre-edit marker strings used for each surgical insertion/removal are recorded in **Section 13 ("Tools/Data & Guides changes")** of this document, not Section 8 as an earlier version of this document incorrectly stated (Section 8 covers the CTA labels/URLs/placements, not the internal-link edits). This is corrected here: see Section 13 below for the actual before/after marker strings used for both pages' edits.

---

## 3. Final verified model set and exclusion decisions

All five candidates named in the handoff were checked against current official US manufacturer sources (Toyota, Honda, Hyundai, Kia, Nissan) immediately before drafting. All five qualified and were included:

| Model | Current on sale? | Midsize sedan? | Trim under $40k MSRP? |
|---|---|---|---|
| Toyota Camry | Yes, 2026 MY | Yes | Yes — hybrid-only, ~$29,000-$37,525 across trims |
| Honda Accord | Yes, 2026 MY | Yes | Yes — $28,395-$39,495 across trims |
| Hyundai Sonata | Yes, 2026 MY | Yes | Yes — ~$25,650-$38,100 across trims |
| Kia K5 | Yes, 2026 MY | Yes | Yes — ~$27,490-$37,275 across trims |
| Nissan Altima | Yes, 2026 MY | Yes | Yes — $27,580-$30,980 across trims |

**Excluded, with reasons stated in the page copy itself:**
- **Toyota Prius, Honda Civic Si** — compact-class cars, not midsize sedans; excluded on classification grounds.
- **Toyota Avalon, Chevrolet Malibu** — discontinued as of the current model year; excluded on availability grounds.
- **Subaru Legacy** — production ended after the 2025 model year (Subaru's own official announcement, media.subaru.com/pressrelease/2165/117/subaru-announces-legacy-production-end-2025, verified reachable this session); it is not a current 2026 model and is excluded on that basis, not on a scoping decision. **Correction note: an earlier version of this return document and the live page both incorrectly stated the Legacy "remains on sale" and treated it as a candidate for future review. This was factually wrong and has been corrected on the live page and in this document as part of the corrective pass documented below.**

No model was padded into the list without evidence, and no candidate was silently dropped without explanation.

---

## 4. Source ledger

Base MSRP, trim, and powertrain figures for all five models were checked against each manufacturer's own current pricing/specification pages during this session (2026-09-21) and, for the three US brands not previously checked this week, freshly verified via web search against official and near-official sources:

- Toyota Camry — toyota.com/camry (also cross-checked via TrueCar/KBB aggregator figures in the Task #68 audit)
- Honda Accord — automobiles.honda.com/accord
- Hyundai Sonata — hyundaiusa.com/us/en/vehicles/sonata (newly verified this session)
- Kia K5 — kia.com/us/en/k5 (newly verified this session)
- Nissan Altima — nissanusa.com/vehicles/cars/altima.html

All five source URLs are cited inline in the published page's "Sources" section.

---

## 5. Before/after title/meta/H1/canonical/robots/schema/read time

| Field | Before | After |
|---|---|---|
| Post title | Best Midsize Sedan Under $40,000: Camry vs Accord vs Altima | Best New Midsize Sedans Under $40,000 in 2026 |
| Rendered title tag | Best Midsize Sedan Under $40,000: Camry Vs Accord Vs Altima - GetCarWise | Best New Midsize Sedans Under $40,000 In 2026 - GetCarWise |
| Meta description | Compare the Camry, Accord, and Altima under $40k. See which wins on reliability, driving feel, and value before you buy. | Compare 2026 Camry, Accord, Sonata, K5 and Altima trims under $40,000. See MSRP, powertrain, AWD and warranty by model, plus new, used and trade-in options. |
| H1 | Best Midsize Sedan Under $40,000: Camry vs Accord vs Altima | Best New Midsize Sedans Under $40,000 in 2026 |
| Canonical | self-referencing (`/tools/best-midsize-sedan-under-40000/`) | unchanged, self-referencing |
| Robots | follow, index, max-snippet:-1, max-video-preview:-1, max-image-preview:large | unchanged |
| Permalink slug | best-midsize-sedan-under-40000 | unchanged — no year forced into the URL |
| Schema | site-wide 8-item `@graph`, Article headline stale (referenced old title) | same 8-item `@graph`; Article headline and BreadcrumbList item name both confirmed live to dynamically match the new title exactly, via Rank Math's `%seo_title%`/`%seo_description%` bindings, re-saved this session to force refresh |
| Read-time badge | "Essential Guide · 8 min read" (hardcoded `<p>` element in old content, inconsistent with the page's actual ~540-word length) | **absent** — the badge was part of the old body content, not a theme-computed field; since the new body never included it, the mismatch is resolved by removal rather than by re-computing a new estimate. Page is confirmed ~1,925-2,010 words by two independent counts (WordPress block-editor count and a live-page word-count script) |

---

## 6. Factual-claim corrections made

All issues identified in the Task #68 audit's claim ledger were corrected in the rebuild:

- **Camry hybrid-only fact corrected.** The old page implied a "hybrid adds a small premium" framing; the new page states plainly that the 2026 Camry is hybrid-only across every trim, with no non-hybrid option to compare against.
- **Altima AWD corrected.** The old page's self-contradictory "standard all-wheel drive available" wording is replaced with the accurate "AWD is available (Intelligent AWD) as an option, adding roughly $1,400... AWD is optional, not standard" — stated twice (model section and FAQ) for clarity.
- **Unsupported 2019-2023 used-market framing removed entirely.** The new page makes no claims about used-market model years, mileage ranges, ownership history, or accident/service records, since the page is now explicitly a new-car guide.
- **Unsupported reliability/resale/maintenance/"segment leader" claims removed.** No claim in the new page states or implies a reliability or resale ranking without a named, defensible basis; comparative statements (e.g., "Kia's warranty includes the same... term structure as Hyundai") are stated as verifiable facts (warranty terms), not subjective quality judgments.
- **Subjective judgments labeled as such.** Statements like "Why it might fit" are framed as conditional recommendations tied to a stated buyer priority (e.g., AWD, warranty length, price), not as unqualified rankings.
- **Inline citations and a dated source section added.** The old page had zero outbound editorial links; the new page cites all five manufacturers directly and states the check date (September 2026) in both the methodology section and the sources section.

**Corrective pass (2026-09-21T03:52:18 UTC) — three additional errors introduced in the original rebuild, identified and fixed:**

- **Accord "only gas/hybrid choice" claim corrected.** The original rebuild stated "The 2026 Accord is the only car on this list that still offers a genuine choice between gas and hybrid power in the same model line," which directly contradicted the page's own Sonata section (which correctly describes the Sonata as also offering both gas and hybrid trims). Changed sentence, exactly as specified:
  - **Before:** "The 2026 Accord is the only car on this list that still offers a genuine choice between gas and hybrid power in the same model line. LX and SE trims use a turbocharged 1.5L gas engine; Sport, EX-L, Sport-L and Touring trims switch to a 2.0L hybrid powertrain."
  - **After:** "The Accord is one of two cars here, alongside the Sonata, offering both gas and hybrid powertrains. Unlike the Sonata, the Accord does not offer AWD. LX and SE trims use a turbocharged 1.5L gas engine; Sport, EX-L, Sport-L and Touring trims switch to a 2.0L hybrid powertrain."
  - Verified via full-content search that no other passage on the page repeats the retracted "only car" gas/hybrid claim (the K5 section's separate "only car here with a genuine performance option" statement is about performance trims, not gas/hybrid choice, and was not affected).

- **Subaru Legacy exclusion corrected.** The original rebuild stated the Legacy "remains on sale," which is factually wrong — Subaru officially ended Legacy production after the 2025 model year.
  - **Before:** "The Legacy remains on sale but was not part of this comparison's original scope; we may revisit it separately."
  - **After:** "The Subaru Legacy ended after the 2025 model year, so it is not a current 2026 candidate."
  - The official Subaru source (`https://media.subaru.com/pressrelease/2165/117/subaru-announces-legacy-production-end-2025`) was verified reachable this session and added to the page's Sources section under a new "Excluded model" heading, so the exclusion is now cited, not just asserted.

- **$40,000 threshold / destination-charge framing corrected in two places.** The original rebuild implied every listed trim, including the Accord Touring Hybrid ($39,495 base MSRP), remains under $40,000 even after destination — this is not necessarily true once a roughly $1,100-$1,300 destination charge is added to a trim already within a few hundred dollars of the cap.
  - **Before (methodology section):** "Adding destination does not push any base trim listed here over $40,000, but destination plus options can push a heavily equipped trim close to or over the cap — check the build for the specific trim you want."
  - **After (methodology section):** "Each included model has at least one configuration below $40,000 base MSRP. Entry trims remain below the cap after typical destination charges, but some upper trims — including the Accord Touring Hybrid — can exceed $40,000 once destination, packages or options are included. Check the build for the specific trim you want."
  - **Before (Accord "Why it might fit" list):** "every trim, including the range-topping Touring Hybrid at $39,495, stays under the $40,000 cap at base MSRP;"
  - **After (Accord "Why it might fit" list):** "every trim lists a base MSRP under $40,000, though the range-topping Touring Hybrid at $39,495 base MSRP can exceed $40,000 once destination, packages or options are included;"
  - Base MSRP figures themselves were not altered — only the claim about what happens once destination/options are added.

All three corrections were verified present on the live public page after publication (Section 20, below). No other content, heading, CTA, schema binding, or internal link was touched during this corrective pass.

---

## 7. Complete final heading outline

1. H1: Best New Midsize Sedans Under $40,000 in 2026
2. H2: Quick answer
3. H2: How we chose these five
4. H2: 2026 midsize sedans under $40,000: reference table
5. H2: Toyota Camry (H3: Why it might fit, H3: What to check before buying)
6. H2: Honda Accord (H3: Why it might fit, H3: What to check before buying)
7. H2: Hyundai Sonata (H3: Why it might fit, H3: Warranty note, H3: What to check before buying)
8. H2: Kia K5 (H3: Why it might fit, H3: What to check before buying)
9. H2: Nissan Altima (H3: Why it might fit, H3: What to check before buying)
10. H2: Which should you buy? (5 x H3 buyer-priority sub-sections)
11. H2: Ready to shop? (New + Used CTA block)
12. H2: Already have a car to sell or trade? (Trade-in CTA block)
13. H2: Frequently asked questions (5 x H3 questions)
14. H2: Sources

One H1, logical nested heading structure throughout, matches the required 11-section structure from the handoff (answer-first summary, dated methodology, comparison table, one section per model, decision guide, integrated New/Used funnel, contextual Trade-in bridge, CarClever continuation, FAQs, sources).

---

## 8. Exact New/Used/Trade-in CTA labels, URLs and placements

All three CTAs use the exact Impact-managed URLs validated in Task #63A, unchanged:

| Role | Label | URL | Placement |
|---|---|---|---|
| Primary New | Shop New Midsize Sedans on Edmunds | `https://edmunds.sjv.io/c/7765200/3949597/52125` | "Ready to shop?" section, immediately after the decision-guide content, styled with `<strong>` for visual primacy |
| Secondary Used | Browse Used Midsize Sedans on Edmunds | `https://edmunds.sjv.io/c/7765200/3949600/52125` | Same section, immediately below the New CTA, introduced with "Prefer to consider a used option instead?" |
| Contextual Trade-in | See What Your Current Car May Be Worth | `https://edmunds.sjv.io/c/7765200/3949601/52125` | Separate, lower "Already have a car to sell or trade?" section, positioned after the New/Used block, before the disclosure and CarClever block |

All three links use `rel="nofollow sponsored noopener"` and `target="_blank"`, confirmed via live DOM inspection after publication. No CTA implies guaranteed availability, price, valuation, or lead acceptance — both the New/Used section and the Trade-in section include an explicit disclaimer sentence to this effect.

**Ordering correction made during drafting:** the first draft placed the Trade-in block before the New/Used block, which the handoff and its associated review both prohibit ("Trade-in must not compete with New above the fold... belongs later in the page"). This was caught and corrected before publication — verified via string-index comparison of the final content before pushing, confirming the New/Used section appears earlier in the document than the Trade-in section.

---

## 9. CJ removal proof (page 828 only)

Confirmed via live DOM inspection of the published page: zero anchors matching `anrdoezrs.net` are present anywhere on page 828. The legacy CJ link (`https://www.anrdoezrs.net/click-101637236-15701072`, "Browse Used Cars on Edmunds") that was present on the pre-rebuild page is fully absent from the rebuilt page.

**No other page's CJ link was touched.** The 4 remaining `anrdoezrs.net` placements (3-row SUV, $25k SUV, PHEV) and the 2 `jdoqocy.com` placements ($30k SUV comparison page, a different page from the $30k *sedan* comparison) inventoried in Task #63A were not modified in any way this session.

---

## 10. Disclosure/rel/target proof

Live DOM inspection confirms:
- All three CTA links carry `rel="nofollow sponsored noopener"` and `target="_blank"`, exactly matching the pattern used on every other GetCarWise affiliate link.
- The affiliate disclosure sentence ("Some links on this page are affiliate links. If you use one, GetCarWise may receive compensation at no additional cost to you. Our recommendations remain independent.") is present, extended with an additional no-guarantee clause ("These links do not guarantee vehicle availability, price, trade-in value, or loan/lead acceptance — confirm current details directly with the dealer or lender."), and positioned adjacent to the funnel per the handoff's requirement.

---

## 11. GA4/Impact verification, or exact limitations

**GA4: firing and outbound-event capture could not be verified in the observed automated/consent state.** Live inspection of the published page found `window.gtag` undefined and no `dataLayer` array present at page-load time; a page-source search found a Google Site Kit-inserted "Google tag (gtag.js) consent mode dataLayer" comment block present but with no actual gtag/measurement-ID script executing during this session's page load. This is consistent with the site's Complianz consent-management plugin gating analytics behind cookie consent, which did not register as accepted in this automated browsing session. **This finding is specific to the observed session state and should not be read as a conclusion that GA4 is globally inactive on the site** — a real visitor who accepts the consent banner may see gtag load and fire normally; that path was not tested here. **Per the handoff's explicit instruction ("If existing analytics cannot provide page-level CTA reporting without global code/GTM changes, document the limitation; do not broaden scope"), no GTM change, consent-bypass, or new tracking code was added.** Whether GA4 enhanced measurement captures these three outbound clicks with page location and link URL, for a real consenting visitor, remains unverified and is recorded here as an open question for the T+14 measurement window, not resolved in this session.

**Impact: confirmed working at the account level; page-level attribution to page 828 is not established.** Authenticated into the Impact.com Edmunds media-partner dashboard (same session used for Task #63A). The account's own Sep 1-21 snapshot shows **9 total clicks recorded, 0 actions, $0.00 earnings** across the whole account. This demonstrates account-level click tracking is active and functioning, but it is **not evidence of clicks attributed specifically to page 828** — Impact's account-level snapshot does not break clicks down by referring page or sub-ID, and no such breakdown was pulled or is available in the dashboard views used this session. **The earlier version of this document speculated that these 9 clicks were generated by Task #63A's validation clicks and that Impact's redirect chain caused multiple tracked events per click; that speculation is retracted here, since it was not verified and cannot be confirmed from the account-level total alone.** The correct, narrower claim is simply that Impact registers *some* click activity on this account; the composition of those 9 clicks (which asset, which page, which session) was not established. Confirmed the account's contract terms independently: Used Vehicle Lead $10.00/30-day, New Vehicle Lead $10.00/30-day, Trade-in Offers Lead $3.50/30-day — matching prior documentation exactly.

**One permitted post-publication validation click was made** on the New CTA's exact URL (`https://edmunds.sjv.io/c/7765200/3949597/52125`). This confirmed that **the link resolves successfully** — one hop to `edmunds.com/new-cars/` with all tracking parameters intact (`irpid=7765200`, `utm_source=impact`, `utm_matchtype=inventory`, `utm_adgroup=3949597`). **This is a destination/redirect verification only. It is not a claim that Impact's reporting attributed this specific click to page 828**, since no page-level or sub-ID evidence was pulled to confirm that attribution — doing so was outside what this session's dashboard views could show. No lead was submitted. Used and Trade-in CTAs were not re-clicked this session, since they were already validated in Task #63A with the same exact URLs and no change was made to either link.

---

## 12. CarClever verification

Confirmed via live DOM inspection: the CarClever Lite `<iframe>` block (`src="https://getcarwise.app/carclever-lite/"`) is present on the published page, positioned after the CTA/disclosure block per the handoff's requirement ("position it coherently after the editorial decision path"). Watched it load live in-browser during the desktop verification pass, confirming it is functionally active, not just present in the HTML. The click-handler script making the surrounding container clickable (routing to `/tools/deal-score/`) is also present, unchanged from the pre-rebuild page.

---

## 13. Tools/Data & Guides changes

**Tools hub (page 452):** did not previously link to either sedan page. Added one new entry, "Best new midsize sedans under $40,000 — 2026 model comparison," linking to the rebuilt page 828, inserted immediately after the existing $25k SUV entry using the site's established list-item pattern. Verified live.

**Data & Guides (page 899):** found a more complex pre-existing state than initially expected. The page had one correct-format entry for the $30k page (`/best-midsize-sedan-under-30k-comparison`, "Best Midsize Sedan Under $30K") but **no entry at all for the $40k page under its expected search pattern** — and, on closer inspection, a separate, differently-formatted stale entry (`/best-midsize-sedan-under-40000`, missing the `/tools/` path prefix, labeled "Best Midsize Sedan Under $40K — Camry vs Accord vs Altima") that an earlier DOM query had missed. Two changes were made:
1. Added a new, correctly-labeled entry: "Best New Midsize Sedans Under $40,000" linking to `/tools/best-midsize-sedan-under-40000` with a description naming all five models.
2. Removed the stale duplicate entry with the old three-model label and malformed URL.

Verified live: exactly two sedan-related entries now exist on Data & Guides, clearly distinguishable by name and destination, with no implication that either page was merged, redirected, or superseded.

**Exact before/after marker strings used for these edits (for rollback reference):**

*Tools hub (page 452) — insertion anchor, existing content immediately preceding the new entry (unchanged, used only as an insertion point):*
```
<p>Shopping by budget? See our guide to the best used compact SUVs under $25,000, including the trade-offs between price, age, mileage, and value.</p>
```
*New entry inserted immediately after that anchor:*
```
<p><a href="https://getcarwise.app/tools/best-midsize-sedan-under-40000/"><strong>Best new midsize sedans under $40,000 — 2026 model comparison</strong></a></p>
<p>Shopping for a new midsize sedan? Compare the Camry, Accord, Sonata, K5 and Altima by price, powertrain and AWD, with new, used and trade-in options.</p>
```

*Data & Guides (page 899) — insertion anchor, existing content immediately preceding the new entry (unchanged, used only as an insertion point):*
```
<li><a href="/best-midsize-sedan-under-30k-comparison">Best Midsize Sedan Under $30K</a> — Accord vs Camry vs Altima</li>
```
*New entry inserted immediately after that anchor:*
```
<li><a href="/tools/best-midsize-sedan-under-40000">Best New Midsize Sedans Under $40,000</a> — Camry, Accord, Sonata, K5 and Altima compared for new-car buyers</li>
```
*Stale entry removed entirely (this exact string was deleted, nothing was inserted in its place):*
```
<li><a href="/best-midsize-sedan-under-40000">Best Midsize Sedan Under $40K</a> — Camry vs Accord vs Altima</li>
```

Reversing either page's edit is a matter of removing the "inserted" string above (and, for Data & Guides, re-adding the removed stale-entry string if a full revert is ever wanted) from that page's current content.

---

## 14. Sitemap/GSC result

- **Sitemap lastmod for page 828:** confirmed updated to 2026-09-21 03:27 UTC, matching the fresh publish.
- **Sitemap lastmod for page 772:** confirmed unchanged at 2026-06-21 08:37 UTC — independent proof the $30k page was not touched.
- **GSC URL Inspection for page 828:** confirmed "URL is on Google," page indexed, 2 valid breadcrumb items detected.
- **GSC indexing requested** for page 828 via URL Inspection → Request Indexing; confirmed "Indexing requested" status with the URL added to Google's priority crawl queue.

---

## 15. Mobile/desktop verification

**Desktop (1600x900):** full scroll-through of the published page performed; hero, comparison table, all five model sections, decision guide, CTA block, Trade-in block, CarClever (confirmed loading live), FAQ, and sources all rendered cleanly with no broken HTML observed.

**Mobile (390x844, iPhone-class viewport):** page reloaded fresh at mobile width and scrolled through; text reflow confirmed clean with no horizontal overflow, warranty-note and "what to check" list sections readable, sources section links tappable and correctly formatted at the bottom of the page.

---

## 16. Confirmation that page 772 was untouched

**Confirmed, independently, three separate ways:**
1. WordPress REST API: page 772's `modified` timestamp (2026-06-21T08:37:52) and content length (5,126 characters) are byte-identical to the values recorded during Task #70's original inspection the previous day.
2. Sitemap: page 772's `lastmod` entry (2026-06-21 08:37 UTC) is unchanged.
3. No tool call, fetch, or write request targeting page 772's ID was made at any point in this session — confirmed by reviewing the session's own action log; every WordPress write this session targeted page 828 (content/title), page 452 (Tools hub), or page 899 (Data & Guides).

---

## 17. Confirmation that no other WordPress affiliate link, Publisher Tag, Catalog, app, Vercel or code change occurred

**Confirmed.** This session's WordPress writes were limited to exactly three pages: 828 (the target page's content, title, Rank Math meta, and schema), 452 (Tools hub, one insertion), and 899 (Data & Guides, one insertion and one removal, both related solely to distinguishing the two sedan pages). No other page's content, CTA, or affiliate link was read, opened for editing, or modified. No Impact Publisher Tag was installed or enabled. No Impact Product Catalog query (C1-C8 or otherwise) was made. No app, MCP connector, repository code, Vercel project, or domain configuration was opened or changed at any point in this session.

---

## 18. Unresolved issues

1. **GA4 page-level CTA click attribution cannot be confirmed working** without a real (non-automated, consent-granted) visitor session, per the documented limitation in Section 11. This should be checked with real traffic during the T+14 measurement window rather than assumed either way.
2. **The "Appraisals" text link** (Impact asset 4051015, a newer, narrower trade-in-adjacent asset identified in Task #63A) remains unused; "Sell Your Car" was used instead per the handoff's exact specification. No action needed unless a future page specifically wants the narrower appraisal-only flow.
3. **The Subaru Legacy is not a live model-set question.** This document's original version incorrectly stated the Legacy "remains on sale" and framed it as a candidate for future review. That was factually wrong: Subaru officially announced Legacy production ended after the 2025 model year (source: media.subaru.com/pressrelease/2165/117/subaru-announces-legacy-production-end-2025, verified reachable and cited on the page). This has been corrected on the live page and in this document (Section 3, Section 6, and the page's own Sources section). There is no remaining open question about the Legacy to revisit.
4. **T+14/T+28/T+56 measurement** must report Search, GEO, and each of the three CTA classes separately per the handoff's measurement section, but cannot claim causal separation between the content rebuild and the funnel integration, since both launched together as one bundled treatment.
5. **Previous-28-day metrics, device split, and pre-edit URL Inspection state were not captured** as part of this implementation's T0 pull (Section 1). This is a genuine evidence gap for this specific session, not reconstructed after the fact. Future sessions referencing this page's T0 should note that only latest-28-day and latest-3-month figures are available from the exact implementation-adjacent capture.

---

## 19. Explicit confirmation of scope boundaries held

**Confirmed.** This session:
- Rebuilt WordPress page 828 only — content, title, meta, schema, and its three affiliate CTAs.
- Made two small, directly related internal-link edits (Tools hub, Data & Guides) solely to correctly distinguish the two sedan pages, as explicitly authorized by the handoff's scope section.
- Did not edit page 772, did not create any redirect, did not migrate any other CJ link.
- Did not run Impact Catalog or C1-C8 of any kind.
- Did not install or touch Publisher Tag.
- Did not change any app, MCP connector, repository code, Vercel project, or domain.
- Made exactly one permitted post-publication validation click per CTA class requirement (only the New CTA was re-clicked; Used and Trade-in were not re-validated since no change was made to either underlying link versus their Task #63A validation).
- Did not submit any lead, quote, or form on any destination page.

**Corrective pass (2026-09-21, this amendment) additionally confirmed:**
- Made only the three narrow content corrections specified (Accord opening, Legacy exclusion, $40,000/destination threshold wording in two places), plus the one directly related citation addition (Subaru source) and the one durable-rollback preservation action.
- Did not alter any URL, title, meta, schema architecture, CTA URL, CTA ordering, CarClever block, page 772, any other affiliate link, Catalog, Publisher Tag, app, Vercel, or code.
- Did not capture or designate a new T0, and did not start any other task.

This return document is being written to `getcarwise-docs` for ChatGPT and André's review.

---

## 20. Corrective-pass verification evidence (2026-09-21T03:52:18 UTC)

**Pre-correction state confirmed** via WordPress REST fetch immediately before editing: page 828's `modified` timestamp (2026-09-21T03:27:20) and content length (16,356 characters) matched the state recorded when the page was originally published in this same Task #70 session — confirming no other change had occurred to the page between original publication and this corrective pass.

**All three target passages confirmed present, exactly once each, before editing:**
- Accord "only car" claim: 1 occurrence
- Legacy old wording: 1 occurrence (found only after correcting for WordPress's HTML-entity-encoded apostrophe, `&#8217;`, in the original string)
- Touring Hybrid "stays under the cap" claim: 1 occurrence

**All three corrections applied via a single WordPress REST `POST` to page 828,** confirmed `status: 200`, resulting content length 16,797 characters (16,356 original + 441 net characters added across all corrections, the Subaru source addition, and the threshold-wording expansion).

**Live public-page verification performed immediately after publication:**
- `document.title` unchanged: "Best New Midsize Sedans Under $40,000 In 2026 - GetCarWise"
- Live page text confirmed to contain all four corrected passages: the new Accord opening, the new Legacy sentence, the new methodology threshold sentence, and the new Accord "Why it might fit" threshold bullet.
- **All three exact Impact CTA URLs, labels, `rel` and `target` attributes confirmed unchanged** via live DOM query: New (`edmunds.sjv.io/c/7765200/3949597/52125`, "Shop New Midsize Sedans on Edmunds"), Used (`edmunds.sjv.io/c/7765200/3949600/52125`, "Browse Used Midsize Sedans on Edmunds"), Trade-in (`edmunds.sjv.io/c/7765200/3949601/52125`, "See What Your Current Car May Be Worth") — all three still carry `rel="nofollow sponsored noopener"` and `target="_blank"`, byte-identical to the original rebuild.
- **Old CJ URL (`anrdoezrs.net`) confirmed still absent** from the page.
- **CarClever Lite `<iframe>` confirmed still present** in the live DOM.
- **Page 772 confirmed untouched**, independently, via a fresh WordPress REST fetch during this corrective pass: `modified` timestamp (2026-06-21T08:37:52) and content length (5,126 characters) both byte-identical to every prior check this week.

**GSC indexing was not re-requested** for this corrective pass. The changes are narrow textual corrections, not a structural or metadata change (title, meta, H1, canonical, and schema bindings were all left untouched), so a fresh indexing request was judged not necessary; the page's existing "Indexing requested" status from the original rebuild stands. If ChatGPT or André judge a fresh request appropriate given the factual nature of the corrections, that can be done as a one-line follow-up without further content changes.

**Durable rollback preserved:** the pre-rebuild page-828 HTML capture was pushed to `getcarwise-docs/ROLLBACK_WORDPRESS_PAGE_828_PRE_TASK70_REBUILD_20260919.html` (commit `4292f87f0aff41805aabcc3665e456915d9f8425`) and re-fetched to confirm a byte-for-byte match with the original local file, resolving the durability gap identified in the corrective instructions.

**No new T0 was captured, and no new task was started**, per the explicit instruction that this is a corrective continuation of the same bundled Task #70 treatment.
