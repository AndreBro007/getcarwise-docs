# Return — Task #63 Phase A: WordPress Impact Static Destination Mapping (Complete)

**Task:** #63 Phase A
**Outcome: COMPLETE — all three destination classes identified and validated**
**Executed by:** Claude — Engineering lane (WordPress read-only inspection + authenticated Impact.com read-only inspection, both complete)
**Handoff executed:** `HANDOFF_WORDPRESS_IMPACT_STATIC_DESTINATION_MAPPING_20260921.md`
**Supersedes:** the earlier same-day return of the same filename, which stopped at Phase A2 due to an unauthenticated Impact session. André subsequently authenticated the session and authorized continuation; this document reflects the completed task.
**Governing docs read in full at session start:** `REVIEW_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_CONSOLIDATION_DECISION_GATE_20260921.md`, `RETURN_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_CONSOLIDATION_20260920.md`, `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md`, `REVIEW_WORDPRESS_IMPACT_LINK_ARCHITECTURE_20260919.md`, `HANDOFF_EDMUNDS_CJ_TO_IMPACT_MIGRATION_20260916.md`, `STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md`

**All five phases (A1-A5) are now complete.** No WordPress page was edited. No CJ link was replaced. No new Impact link was created (all three validated links are existing Impact-managed assets, opened read-only). No Publisher Tag, Catalog, app, Vercel, or lead-submission action occurred at any point, including during the controlled validation clicks in Phase A3.

---

## 1. Timestamps and authenticated surfaces used

- Session start / mandatory repository verification: 2026-09-20, approximately 22:20 UTC
- Phase A1 (WordPress inventory): 2026-09-20, approximately 22:30-22:40 UTC, using André's existing authenticated wp-admin session
- First Phase A2 attempt: 2026-09-20, approximately 22:42 UTC - blocked, app.impact.com unauthenticated (documented in the superseded prior return)
- André authenticated the Impact.com session between sessions.
- Phase A2 (Impact asset inspection, this session): 2026-09-20, approximately 22:52-22:58 UTC, confirmed authenticated as "Broekman Consulting Pty..." on the Edmunds media-partner dashboard
- Phase A3 (controlled destination validation): 2026-09-20, approximately 22:58-23:00 UTC
- Return document finalized: 2026-09-20, approximately 23:05 UTC

**Authenticated surfaces used:** WordPress admin (wp-admin, via André's existing session); Impact.com partner dashboard (app.impact.com, via André's freshly authenticated session, confirmed as the Edmunds media-partner account for Broekman Consulting Pty Ltd).

---

## 2. Complete current WordPress CJ inventory (Phase A1)

### 2.1 - anrdoezrs.net links (4 pages found)

| Page URL | Page title | Visible label | Placement | rel/target | CarClever present |
|---|---|---|---|---|---|
| /tools/best-3-row-suv-under-50000/ | Best 3 Row SUVs Under 50k | "Browse Used Cars on Edmunds" | After "Which Should You Buy?" section, before disclosure/CarClever block | rel="nofollow sponsored noopener", target="_blank" | Yes |
| /tools/best-compact-suv-under-25000/ | Best Compact SUVs Under $25,000 | "Browse Used Cars on Edmunds" | Same relative placement | Same | Yes |
| /tools/best-midsize-sedan-under-40000/ | Best Midsize Sedan Under $40,000 | "Browse Used Cars on Edmunds" | Same relative placement | Same | Yes |
| /tools/best-used-phev-plug-in-hybrid/ | Best Used Plug-In Hybrids | "Browse Used Cars on Edmunds" | Same relative placement | Same | Yes |

**Exact URL on all 4 pages:** https://www.anrdoezrs.net/click-101637236-15701072 - byte-identical across every page.

### 2.2 - jdoqocy.com links (1 page found, 2 instances)

| Page URL | Page title | Visible label | Placement | rel/target | CarClever present |
|---|---|---|---|---|---|
| /tools/best-compact-suv-under-30000/ | Best SUVs Under $30,000 | "Browse SUVs on Edmunds →" and "Browse SUVs on Edmunds" | Two placements in the page | rel="nofollow sponsored noopener", target="_blank" | Yes |

**Exact URL on both instances:** https://www.jdoqocy.com/click-101637236-15700851.

### 2.3 - Sitewide Trade-in CTA

**Not found.** WordPress admin search for "trade-in" returned zero results; a homepage DOM scan for trade/sell-related links also returned zero matches. No sitewide Trade-in CTA exists on the live site today.

### 2.4 - $30k midsize sedan comparison page

/tools/best-midsize-sedan-under-30k-comparison/ has no Edmunds/CJ/Impact link and no CarClever Lite embed (documented in the Task #70 return; not re-inspected this session).

### 2.5 - Complete link-record summary

| Unique CJ URL | Hostname | Pages using it | Total instances | Apparent intended action |
|---|---|---|---:|---|
| click-101637236-15701072 | anrdoezrs.net | 4 (3-row SUV, $25k SUV, $40k sedan, PHEV) | 4 | Used |
| click-101637236-15700851 | jdoqocy.com | 1 ($30k SUV) | 2 | Used |

**Total commercial CJ link placements sitewide: 6, across 5 unique pages, using only 2 distinct CJ tracking IDs. Every existing placement is Used-only; none is New or Trade-in.**

---

## 3. Impact asset inventory relevant to New/Used/Trade-in (Phase A2 - complete)

**Authenticated successfully** at app.impact.com, confirmed as the "Broekman Consulting Pty..." Edmunds media-partner account. Navigated Content -> Assets. The Edmunds program currently shows **13 assets** (an increase of 1 from the "12 assets" recorded in the Sep 16 strategy document - see Section 3.4 below):

### 3.1 - Text links (4)

| Asset name | Asset ID | Landing page | Available since | Last updated |
|---|---:|---|---|---|
| Appraisals | 4051015 | https://www.edmunds.com/appraisal/ | Sep 19, 2026 | Sep 19, 2026 (new this week) |
| Sell Your Car | 3949601 | https://www.edmunds.com/sell-car/?utm_matchtype=tradein | Jun 25, 2026 | Sep 1, 2026 |
| New Car Listings | 3949597 | https://www.edmunds.com/new-cars/?utm_matchtype=inventory | Jun 25, 2026 | Sep 1, 2026 |
| Used Car Listings | 3949600 | https://www.edmunds.com/used-cars-for-sale/?utm_matchtype=inventory | Jun 25, 2026 | Sep 1, 2026 |

### 3.2 - Banner images (9), by campaign

| Campaign | Sizes available |
|---|---|
| New Car Inventory | 300x250, 320x50, 728x90 |
| Trade-in Tool | 300x250, 320x50, 728x90 |
| Used Car Inventory | 300x250, 320x50, 728x90 |

Banner assets were identified by name/campaign in the Assets grid but not individually opened for tracking-link detail, since Phase A3's scope is destination validation for the CTA classes (text links are the direct fit for WordPress inline CTAs; banners are a separate future consideration for image-based placements, not needed to unblock the $40k page's text CTA).

### 3.3 - Landing-page parameters confirm class unambiguously

Each of the three primary text-link candidates carries a utm_matchtype query parameter on its landing page that independently confirms its class, without relying on the asset's display name alone:

- New Car Listings -> utm_matchtype=inventory (new-inventory context, confirmed by the destination page itself)
- Used Car Listings -> utm_matchtype=inventory (same parameter value as New; the class distinction comes from the base URL path - /new-cars/ vs. /used-cars-for-sale/ - not from this parameter)
- Sell Your Car -> utm_matchtype=tradein (distinctly different parameter value, confirming this is Impact's own trade-in classification, not an inference)

### 3.4 - Correction to the prior-session (Sep 16) asset count

The Sep 16 strategy document recorded 12 assets (3 text links + 9 banners). This session found **13 assets: 4 text links + 9 banners** - one new text link, "Appraisals," was added to the account on Sep 19, 2026 (2 days before this session), landing on https://www.edmunds.com/appraisal/. This is a genuinely new finding, not a discrepancy in the prior record. "Appraisals" is closely related to but distinct from "Sell Your Car" - both point at trade-in-adjacent journeys, but "Sell Your Car" carries the explicit utm_matchtype=tradein classification and matches the named "Trade-in Tool" banner campaign, making it the cleaner primary candidate. "Appraisals" is recorded here as a secondary, not separately validated in Phase A3, per the handoff's "at most one candidate per class" limit.

---

## 4. Controlled redirect/landing evidence (Phase A3 - complete)

One candidate per class was opened in a fresh browser tab (no form fields completed, no lead submitted). All three resolved correctly in a single hop.

### 4.1 - New (asset 3949597, "New Car Listings")

- Starting URL: https://edmunds.sjv.io/c/7765200/3949597/52125
- Final URL: https://www.edmunds.com/new-cars/?afsrc=1&im_ref=...&irgwc=1&irpid=7765200&sharedid=&utm_account=edmunds_affiliate&utm_adgroup=3949597&utm_campaign=edmunds_affiliate&utm_content=7765200&utm_matchtype=inventory&utm_medium=affiliate&utm_source=impact
- Redirect count: 1 (single hop, edmunds.sjv.io -> www.edmunds.com)
- Landing page purpose: "New Cars - Know what to buy, know what to pay," a live, functional new-car search page (Make/Model/Type/Price search, ZIP field, links to Price Checker, Loan Calculator, Compare Cars, Trade-In Calculator)
- Class match: confirmed - unambiguously a new-car shopping page with a credible path toward a new-vehicle lead
- Tracking parameters intact: irpid=7765200 (matches the account ID), utm_source=impact, utm_matchtype=inventory all present and correctly formed
- No consent/interstitial behavior observed blocking the path
- No cross-device, login, or location assumption beyond a standard ZIP-based location field pre-filled with a generic default, which did not require any user input to view the page

### 4.2 - Used (asset 3949600, "Used Car Listings")

- Starting URL: https://edmunds.sjv.io/c/7765200/3949600/52125
- Final URL: https://www.edmunds.com/used-cars-for-sale/?afsrc=1&im_ref=...&irpid=7765200&...&utm_matchtype=inventory&utm_medium=affiliate&utm_source=impact
- Redirect count: 1
- Landing page purpose: "Shop Used Cars for Sale - 1M+ Listings Near Me," a live search page with Buy In-store/Buy Online/Buy Private Party options, Make/Model/Type/Price search, and links to Sell My Car, Car Appraisal, Certified Pre-owned Cars
- Class match: confirmed - unambiguously a used-car shopping page
- Tracking parameters intact: same pattern as Section 4.1, correctly formed for this asset ID

### 4.3 - Trade-in (asset 3949601, "Sell Your Car")

- Starting URL: https://edmunds.sjv.io/c/7765200/3949601/52125
- Final URL: https://www.edmunds.com/sell-car/?afsrc=1&im_ref=...&irpid=7765200&...&utm_matchtype=tradein&utm_medium=affiliate&utm_source=impact
- Redirect count: 1
- Landing page purpose: "Sell my car online - Selling your car has never been easier," with License Plate/VIN/Year-Make-Model lookup tabs leading to a "See your car's value" action, plus a secondary private-sale listing option
- Class match: confirmed - unambiguously the trade-in/valuation class, and the utm_matchtype=tradein parameter independently confirms Impact's own classification agrees
- Tracking parameters intact
- **No form field was completed and no lookup was submitted** - the landing page's existence and correct framing was confirmed by observation only, per the boundary against lead submission

---

## 5. Canonical destination map (Phase A4)

| Class | Recommended CTA role | Exact visible label | Approved Impact URL | Final Edmunds destination | Existing asset or creation required | Verification result | Suitable now? |
|---|---|---|---|---|---|---|---|
| New | Primary for new-car pages | "New Car Listings" (Impact asset name; WordPress-facing label can be authored separately, e.g. "Browse New Cars on Edmunds," to match site voice) | https://edmunds.sjv.io/c/7765200/3949597/52125 | https://www.edmunds.com/new-cars/ (plus Impact tracking parameters) | Existing Impact-managed asset (ID 3949597); no creation needed | Verified: one hop, correct domain, functional new-car search page, tracking parameters intact | **Yes** |
| Used | Secondary/fallback | "Used Car Listings" (current WordPress CJ labels - "Browse Used Cars on Edmunds" / "Browse SUVs on Edmunds" - can be retained verbatim once the underlying URL is swapped) | https://edmunds.sjv.io/c/7765200/3949600/52125 | https://www.edmunds.com/used-cars-for-sale/ (plus Impact tracking parameters) | Existing Impact-managed asset (ID 3949600); no creation needed | Verified: one hop, correct domain, functional used-car search page, tracking parameters intact | **Yes** |
| Trade-in | Contextual bridge | "Sell Your Car" (Impact asset name; WordPress-facing label could read e.g. "See Your Car's Value" or "Sell or Trade Your Car") | https://edmunds.sjv.io/c/7765200/3949601/52125 | https://www.edmunds.com/sell-car/ (plus Impact tracking parameters) | Existing Impact-managed asset (ID 3949601); no creation needed | Verified: one hop, correct domain, functional trade-in/valuation entry page, utm_matchtype=tradein confirms class, tracking parameters intact | **Yes** |

**All three classes are resolved and suitable for use.** No destination requires controlled link creation. No class is ambiguous.

---

## 6. Unresolved/missing link classes

**None.** All three classes (New, Used, Trade-in) were successfully identified, validated, and mapped in this session.

One secondary finding, not a gap: the "Appraisals" text link (asset 4051015, https://www.edmunds.com/appraisal/) is a second, newer trade-in-adjacent asset not separately validated in Phase A3, per the "at most one candidate per class" limit. It is noted in Section 3.4 for future reference should a narrower "just get an appraisal number" flow (distinct from the fuller "Sell Your Car" listing/sale flow) ever be wanted for a different page context.

---

## 7. Whether the $40k page is unblocked

**Yes - the CTA/monetization gate from Task #70 is now resolved.** A validated, WordPress-facing, Impact-tracked New destination exists: https://edmunds.sjv.io/c/7765200/3949597/52125, confirmed via controlled validation to land correctly on Edmunds' functional new-car shopping page with intact tracking.

This does not itself authorize implementation. Per the Task #70 review's own "Next dependency" note, a revised, $40k-only implementation handoff should now be written once this mapping is accepted, and per the same review's "Measurement note," a fresh T0 baseline must be captured immediately before any production edit - the T0 captured during the stopped Task #70 attempt was decision evidence, not the implementation baseline.

---

## 8. Proposed Task #63B migration order (proposed only, not authorized or executed)

1. **Migrate the 5 existing Used-labeled CJ placements first** (Section 2.5), since the validated Used destination (https://edmunds.sjv.io/c/7765200/3949600/52125) now exists and this is the lowest-risk change - no page content or CTA role changes, only the underlying tracking URL. The 4 anrdoezrs.net placements (3-row, $25k, $40k sedan, PHEV) can be treated as one pattern; the 2 jdoqocy.com placements on the $30k SUV page should be migrated together as their own unit, since they share an identical destination and page.
2. **Add a primary New CTA to the $40k midsize-sedan page specifically**, once its content rebuild is otherwise ready (per the still-open cluster/content decisions from Task #70), using the validated New destination (https://edmunds.sjv.io/c/7765200/3949597/52125). This is page-specific treatment, not a bulk pattern, since no other current page has new-car content framing.
3. **Trade-in remains net-new sitewide infrastructure.** No current page has Trade-in content or context; per the Tool-Led Monetization strategy's own guidance, it should not be added as a generic CTA to every page, but placed contextually on a future page with genuine replacement/ownership framing, using the validated destination (https://edmunds.sjv.io/c/7765200/3949601/52125) when that page is built.
4. **Do not bulk-migrate all 6 current Used placements in a single pass.** Each of the 5 affected pages is an active or recently-active SEO/GEO content-treatment subject with its own T0 measurement window; migrate page-by-page, each with its own logged timestamp, per Section 9.

---

## 9. Keeping affiliate-change timestamps separate from SEO/GEO treatment timestamps

No affiliate change occurred this session. For the future migration, continue the existing, already-established convention (confirmed in REVIEW_WORDPRESS_IMPACT_LINK_ARCHITECTURE_20260919.md as current practice): log each page's CJ->Impact link swap with its own commit/edit timestamp, separate from that page's most recent content-treatment timestamp.

---

## 10. Rollback requirements for the future migration

For each page's future CJ->Impact swap, the Task #63B implementer should capture beforehand:

- the exact pre-swap CTA HTML (URL, label, rel, target) - the granularity already captured in Section 2 of this document for all 6 current placements;
- the page's WordPress modified timestamp immediately before the swap;
- the page's sitemap lastmod immediately before the swap;

so any single page's CTA can be reverted independently if a problem is found with one specific Impact destination after rollout.

---

## 11. Blockers/failures

**None remaining.** The single blocker recorded in the earlier same-day return (Impact authentication unavailable) was resolved by André authenticating the session between sessions. This session completed successfully once that access was restored, with no further blockers encountered.

---

## 12. Explicit confirmation: no changes made

**Confirmed.** This session performed exclusively:

- Read-only inspection of the Impact.com Edmunds media-partner account (Content -> Assets), viewing 4 text-link assets' detail panels (name, ID, landing page, availability dates) and their "Get Tracking Link" tabs
- Three controlled, read-only navigations to existing Impact tracking URLs, observing the resulting redirect and landing page; no form field was completed and no lookup, quote, or lead of any kind was submitted on any landing page
- No changes to WordPress this session (Phase A1 was read-only inventory only, as in the prior return)

**No WordPress page was edited. No CJ link was replaced or modified. No new Impact tracking link was created - all three validated links are pre-existing Impact-managed assets, opened as-is. No Publisher Tag was installed or enabled. No Impact Product Catalog query was made. No app, MCP connector, repository code, Vercel project, or domain was changed. No lead form, appraisal lookup, or sale listing of any kind was submitted or completed. No Impact tracking URL was manually altered - all three URLs used are exactly as generated by Impact's own "Get Tracking Link" interface. No credentials, authorization headers, AccountSID, or private account data are recorded anywhere in this document.**

This return document is being written to getcarwise-docs for ChatGPT and André's review. Task #63 Phase A is complete. The $40k midsize-sedan page's CTA gate is resolved pending a revised implementation handoff.
