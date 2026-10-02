# Review — Impact creative, Lite cutover and Google Search gates

**Date:** 2 October 2026, Australia/Brisbane.
**Lane:** ChatGPT business/strategy.
**Status:** Recommendations pending André confirmation. Review complete; implementation and live functionality checks not performed.

## Recommendation

1. Replace fixed website affiliate CTAs with the exact relevant Edmunds-supplied Impact asset text and current Asset Code, including its supplied impression pixel where present. Start with page 934, then audit the other live fixed placements, including post 513. Do not leave custom creative unresolved or make an Edmunds response a prerequisite for using existing supplied creative.
2. Move the nine website guide embeds to the already-built Lite V2 in stages, after a small Claude verification on the actual Free plan. Start with page 934, then the remaining eight guides. Adjust adjacent feature promises to Lite V2's actual discovery/link-resolution scope. Page 239 is an additional legacy entry point requiring its own explicit cutover/content decision.
3. Keep Google Ads activation/spend on hold until the selected page's affiliate creative, Lite path, feature copy and final campaign settings are verified and André approves the concrete campaign/spend preview.
4. Await Fractal's reply for the separate old ChatGPT app/hosting decision before the recorded 14 October renewal. Website migration need not wait for that reply. No cancellation, retirement, export or self-hosting decision is made here.

## Evidence and verification

All seven required widget administration files fetched fresh. Complete getcarwise-docs root inventory discovered and printed: 190 entries. Docs checkpoint and main both 8aae7889c37a9beb4b052d01a4966c58e7d7813d: compare identical; no added/modified/renamed/deleted files since the ChatGPT checkpoint. No full-fetch fallback required.

Widget checkpoint ae72bf2c31cb5cfc58f22ffad03084b2bb53b202 to reviewed tip 7b19c420a9249f9f4bab7e602b312e290d1926b3: one commit, STATE.md only (8 additions, 2 deletions). Inspected patch and spot-verified the package/application-version correction and concrete ZIP preparation against the current linked OpenAI review document. This is documentation evidence; ZIP bytes were not independently re-audited this session.

Read task-relevant G1, paid-search contract, Impact website architecture, Lite recommendation/architecture/strategy and old-Free API/field reports. Historical proposals are not new implementation authority. Read the current stored 13-page supplied agreement, Edmunds terms(1).pdf (Library identity libfile_f624e44140188191a490ef3c7f134479), in full.

Fresh public WordPress REST reads (no affiliate navigation, no vehicle search):
- Page 934 last modified 2026-09-27T22:21:36; href https://edmunds.sjv.io/c/7765200/3949600/52125, visible affiliate text "Browse Used Cars on Edmunds", sponsored/nofollow/noopener attributes present. No imp.pxf.io in stored rendered content. No ChatGPT directory anchor in that content. Iframe points to https://getcarwise.app/carclever-lite/.
- Post 513 last modified 2026-09-30T23:40:08; both Trade-in hrefs now https://edmunds.sjv.io/c/7765200/3949601/52125; text "See what your car is worth on Edmunds" / title-case variant; no imp.pxf.io in stored content. New Find My Car and old CarClever directory anchors both present.
- Fresh public pages listing confirms all nine guide embeds still target the legacy WordPress Lite page. Page 239 itself embeds https://carclever-widget.vercel.app/carclever-lite.

The older Sep 29 general rollout-complete note does not establish page-934 coverage; this page-specific check takes precedence for G1. Stored-content absence does not exclude a global/plugin-injected pixel; no full browser network audit was performed. This review did not repeat Claude's sitewide CJ scan. Post-513 href repair was independently verified; broader Task #98 completion remains Claude/owner-reported evidence.

Read-only widget source checks:
- app/api/chat/route.ts uses the Fractal endpoint and old risk/affordability/comparison assumptions.
- app/api/chat-v2/route.ts uses https://carclever-anth.getcarwise.app/mcp and the two tools find_matching_vehicle and resolve_dealer_url; it expressly excludes standalone affordability, deal-risk, comparison and full vehicle-details tools.
- The current Anthropic deployment pin dd68e15 is recorded by Claude; not independently queried through Vercel in this review.

## 1. Fixed Impact creative

The supplied agreement §4.A restricts affiliate creative/text links to supplied Approved Ads and requires express prior Edmunds email authorization for modifications. §4.B requires designated unaltered Impact links. A correct href alone does not establish approval of custom anchor wording.

**Recommendation:** choose the supplied creative option now. For page 934 use the exact Used asset wording reported in the supplied evidence: **Used Car Listings at Edmunds.com**. Obtain its current Asset Code from Impact rather than reconstructing a pixel URL. For New/Trade-in use each asset's exact current copy/code; do not guess their wording from asset names. Include the supplied impression element when supplied, preserve disclosure, and have the implementation owner verify consent handling and the rendered placement.

The agreement read here does not explicitly impose an impression pixel on every link. Impact's public asset guide offers both Asset Code and a Tracking Link. Therefore missing pixel alone is not proof of unpaid clicks, broken attribution or a contractual breach. Deploying the supplied full code removes the omission question for these fixed placements; it does not prove lead attribution or universal compliance.

This fixed-asset recommendation is not blanket approval for dynamic vehicle-card links, catalog links, custom deep links or arbitrary tracking parameters. Review those against their actual asset/API permissions separately. Do not insert pixels or rewrite generated links across the MCP apps as part of a WordPress CTA correction.

Optional follow-up: ask Edmunds for written authorization of desired custom website anchor/button text and presentation, and whether tracking-link-only placements may omit the impression pixel. That outreach is not authorized or sent in this review. Until permission exists, use the supplied asset. No guarantee of partner acceptance or payout is made.

Official platform reference checked today:
https://help.impact.com/partner/what-would-you-like-to-learn-about/platform-features/marketing-content/brand-assets/manage-assets-as-a-partner

## 2. Website Lite migration

| Page ID | Guide | Current embedded route |
|---|---|---|
| 934 | Compact SUV under $25,000 / G1 | Legacy Lite |
| 937 | Used PHEV | Legacy Lite |
| 938 | Used EV | Legacy Lite |
| 935 | Sedan under $15,000 | Legacy Lite |
| 936 | Hybrid SUV under $20,000 | Legacy Lite |
| 830 | Three-row SUV under $50,000 | Legacy Lite |
| 829 | Full-size truck under $35,000 | Legacy Lite |
| 828 | New midsize sedan under $40,000 | Legacy Lite |
| 827 | SUV under $30,000, new vs used | Legacy Lite |

Lite V2 already exists; no replacement build is recommended. Its main website job—find matching inventory and continue toward a vehicle/dealer—is suitable for these buyer guides. Its new/used/CPO support also fits page 828 more naturally than a legacy used-only route.

It has fewer dedicated tools. Page 830 currently tells visitors to compare the top three using a comparison tool and inspect Deal Score, estimated monthly cost, warranty and recalls. Those promises cannot simply accompany a V2 embed. Inspect each embed's surrounding text and prompt chips, and retain only verified capabilities. Separate existing specialist tools can be linked only where their current Free-plan functionality is verified.

**Staged sequence for André to approve:**
1. Claude verifies a minimal Lite V2 search/render/dealer-link path on the actual post-Growth plan, including anonymous access and embedded interaction. Avoid a broad regression campaign while quota is limited. Record outcome and request count where available.
2. Capture page-934 rollback content; replace its iframe target with https://carclever-lite.getcarwise.app/carclever-lite-v2, adjust local prompt handling/feature copy if needed, and add a clear optional new Find My Car directory CTA using its existing approved directory destination. Keep the buyer guide and Edmunds Used path intact.
3. Verify the settled page on desktop/mobile and a small purposeful interaction. Do not assume the previous pointer-event fix proves a new cross-origin embed works.
4. Repoint the remaining eight guides and adjust capabilities copy. Record cutover dates as measurement interventions; preserve titles, canonical URLs and core editorial content.
5. Decide page 239 separately so it does not remain an overlooked live Fractal dependency. Old route/code retention remains available for reference, but rollback to Fractal only works while that service remains active and functional.

Auto.dev Growth cancellation and approximately 2 October expiry are owner-recorded; actual plan transition and live Free results not verified here. The 1,000 monthly calls are shared across Auto.dev consumers, not an allowance per app and not 1,000 visitor sessions. Lite V2 removes Fractal dependence for migrated website use but retains Auto.dev and Anthropic API/model usage. It does not establish lower total request use or zero running cost.

Await Fractal's free/lower-plan/export reply for the old ChatGPT app independently. Repointing guides neither retires that app nor makes Fractal immediately cancellable. Before the recorded 14 October renewal, André must choose the old app's hosting/retention direction with current plan and demand evidence.

## 3. Google Ads hold

Retain page 934 as the proposed exact-intent G1 landing page; no new landing-page selection or larger media experiment is justified by this review.

Required before activation:
- supplied affiliate asset placement verified;
- final Lite route works on actual Free access and accurately described capabilities;
- optional new app CTA verified if included in the final page design;
- current saved Ads draft completed and persisted, US Presence/network settings/SEM negatives/ad copy and revised future dates checked;
- separate André approval of concrete preview and A$150 total spend.

Earlier Oct 1–7 draft dates are historical, not an automatic launch schedule. Correcting these blockers does not authorize spend. Direct Google PPC to Edmunds remains prohibited under supplied §3.A.IV.

## Completion and boundaries

Completed: business review, supplied agreement read, public page/embed evidence, source-level dependency spot checks and recorded recommendation. Remaining: André selection of website cutover/creative implementation scope, current Free verification, actual WordPress edits, campaign completion/approval, and Fractal reply/hosting decision.

No application edits, live searches, deployments, subscriptions, Ads activation, affiliate clicks, lead submissions or outbound partner message performed.
