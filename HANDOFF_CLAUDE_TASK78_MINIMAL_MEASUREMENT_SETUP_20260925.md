# Task #78 — Minimal measurement setup for Claude (Sep 25)
**Status:** a small, reversible analytics setup; no site/app code, campaign, billing, publishing, partner-link, production, subscription or synthetic traffic change. Supersedes the earlier multi-route engineering audit handoff, which ChatGPT completed.

## Decision

The first Google → used page 934 test is a **directional buyer-demand test**. Do not delay it merely to build custom outbound-click events or campaign-to-approved-lead attribution. Measure Google Ads cost/searches, GA4 source/medium landing and engagement, and Impact Used actions/payout separately. These are distinct denominators. The existing page 934 Used link is correct. Without source-specific Impact tagging, do not claim an approved lead came from the ad or compute campaign ROAS.

## Exact Claude task

1. In the existing GA4 property, **read-only verify** the Search Console link and the WordPress web stream/measurement ID. Using existing natural traffic, check that `/tools/best-compact-suv-under-25000/` has page views and that landing-page reports can separate `google / cpc` from organic/direct once a campaign exists. Do not generate a test visit during the no-test window. If GA4 access is unavailable, record the exact missing permission/screen.
2. If GA4 allows it, save a simple exploration or report with date, landing page, session source/medium, sessions and engaged sessions for page 934. This changes only a saved analytics view, not tracking code. Verify it reopens and is filterable. If no natural data is present, demonstrate the report configuration, not fabricated results.
3. In Impact, find or save a report for Edmunds **Used Vehicle Lead** with date, clicks, pending/approved/reversed actions and earnings (and Sub ID only if already present). Verify the report can be reopened. Do not click an affiliate link or generate an action. Record reporting lag and that a page/asset total is **not** proof of Google campaign attribution.
4. Draft the final Google Ads landing URL as the existing page 934 plus non-sensitive UTMs, e.g. `https://getcarwise.app/tools/best-compact-suv-under-25000/?utm_source=google&utm_medium=cpc&utm_campaign=used_suv_decision_g1`. Do not create an Ads account, campaign or billing. Confirm via site configuration/history that the URL shape should serve the same page; no visit solely to test it before Sep 30.
5. Return a one-page readiness note: GA4 property/host and page 934 observation, saved report locations, Impact report fields, proposed URL, anything unverified, and whether **simple directional measurement** is ready. Include the exact evidence viewed. No custom pixels, WordPress edit, link replacement, dynamic UTM-to-Sub-ID logic or Lite V2 event work.

**Acceptance:** existing GA4 report and Impact report are accessible/reopenable, or the missing access is stated precisely; page 934 destination/link remains unchanged; no artificial traffic or production change. If an account/report configuration would require a paid tier or materially affect other users, leave it as a documented setting proposal for André.

**Next gate:** Sep 28 GSC cohort; Sep 30 product/cost and hours/cash; then review exact Google ad, keywords, terms, account offer and spend cap separately. Impact approved-lead attribution may be improved later if an initial directional signal justifies it. Do not report aggregate Impact actions as ad-generated leads.
