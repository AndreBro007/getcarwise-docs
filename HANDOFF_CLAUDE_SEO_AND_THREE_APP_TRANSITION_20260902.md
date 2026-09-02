# CLAUDE HANDOFF — SEO Conversion and Three-App Transition Plan — 2026-09-02

## Purpose

Execute the next business/website work during the transition from the legacy Fractal apps to Find My Car. This is a copy, SEO, and content brief. Do not change application code or remap production endpoints from this brief.

## Product status to use in all copy

- **Legacy CarClever:** used/CPO-only Fractal app, currently published in the ChatGPT Directory. Keep its existing access path available during transition.
- **CarClever – New & Used Cars:** broader Fractal app, review withdrawn by André on Sep 1, 2026. Treat as being phased out. Do not promote it as the future product or send new website traffic to it.
- **CarClever – Find My Car:** Vercel replacement covering new/used/CPO/demo inventory. Submitted for Claude and ChatGPT review; not yet approved or ready for public endpoint remapping.

Never describe the legacy CarClever app as Claude-approved or as a Claude fallback. Its old Claude submission was not approved; an email response was received through the former submission process.

## Workstream 1 — SEO title/meta conversion pass

Target the pages and queries with real impressions but zero clicks:

- “best suv under 30000” — 337 impressions / 0 clicks
- “suv under 30000” — 188 impressions / 0 clicks
- “best suvs under 30000” — 152 impressions / 0 clicks
- “suvs under 30000” — 108 impressions / 0 clicks
- Also inspect /tools/best-compact-suv-under-25000/, flagged for a significant impression increase.

Deliverables:

1. Draft an improved SEO title and meta description for each target page.
2. Preserve the page’s actual product promise; do not imply live Find My Car availability.
3. Make the title clearly match the search intent and price ceiling.
4. Make the meta description useful and action-oriented without unsupported claims.
5. Add appropriate Edmunds/CJ links from the existing affiliate inventory where contextually relevant.
6. Identify other pages with the same pattern: meaningful impressions, weak CTR, and no obvious ranking failure.

Do not publish copy without André’s review.

## Workstream 2 — Transition-aware website messaging

Prepare copy recommendations for the following pages:

### Try CarClever — Page 38

- Remove or revise stale “Claude coming soon” wording.
- Do not claim Find My Car is available before approval.
- Explain that the next-generation all-inventory experience is moving through platform review.
- Keep a clear path to the currently live legacy CarClever ChatGPT experience if the page still directs users there.

### CarClever Guide — Page 1053

- The current guide already explains new/used scope and Claude setup.
- Its issue is status/link clarity, not a wholesale rewrite.
- Recommend wording that distinguishes:
  - the currently live legacy ChatGPT app;
  - the withdrawn New & Used Cars app;
  - the pending Find My Car replacement.
- Do not add a live Find My Car or Claude link until approval and the correct public URL are confirmed.

### Tools Hub — Page 452

- Avoid presenting New & Used Cars as an active destination.
- Keep existing web tools accurate.
- Decide whether the legacy ChatGPT app should remain labelled as the current live car-search experience during the transition.
- Reserve a clearly labelled future slot for Find My Car only after approval.

### Homepage — Page 7

- Review whether the current homepage wording overstates or understates the transition.
- Do not add an unavailable app link.
- Keep the messaging centred on independent car evaluation and useful tools until Find My Car is approved.

## Sequencing and gates

1. Draft the SEO copy and transition copy first.
2. André reviews and approves the copy.
3. Claude/André applies approved WordPress changes.
4. Re-test page links and rendered copy.
5. Do not remap production endpoints to Find My Car until:
   - Find My Car is approved and live on at least one platform;
   - roadmap prerequisites are complete;
   - zero regressions are confirmed.
6. After approval, run a separate launch/remapping brief. Do not combine that implementation with this copy pass.

## Success measures

For SEO pages:

- increased CTR for target queries;
- increased organic clicks;
- stable or improved rankings;
- qualified outbound affiliate/dealer clicks.

For transition messaging:

- no dead or misleading app links;
- no promotion of the withdrawn New & Used Cars app;
- no claim that Find My Car is already publicly available;
- clear continuity for users relying on the current ChatGPT legacy app.

## Source records

- CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md — corrected legacy Claude status
- CARCLEVER_SUBMISSION_SUMMARY_FINAL.md — corrected legacy Claude status
- AUDIT_WEBSITE_APP_INFRASTRUCTURE_20260902.md — current page findings
- DECISION_RECORD_FIND_MY_CAR_PHASE_OUT.md — transition decision and gate
- RECOMMENDATION_WEEKLY_MONITORING_EFFORT_ALLOCATION_20260902.md — effort allocation
