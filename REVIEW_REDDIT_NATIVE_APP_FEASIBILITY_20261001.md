# Review: Reddit native automotive app feasibility
Date: 1 October 2026
Status: Research review complete; feasibility, permissions and implementation remain unapproved.

## Judgment

A native Reddit buying helper is worth investigating as another GetCarWise distribution channel. It could let people choose a useful interactive tool within their community instead of encountering repeated promotional bot replies. The supplied documents are substantial concept drafts, but their dual-income forecast and implementation claims are not yet reliable enough to authorize a build.

Treat community utility, affiliate revenue and Developer Funds as three separate hypotheses. Community value can be tested first. Neither affiliate permission nor fund eligibility follows automatically from an app being native to Reddit.

## Documents reviewed

Both uploaded drafts were read in full:
- End-to-End Operational Execution Plan for Reddit Automotive App.
- Master Strategy & Technical Specification: Reddit Native Automotive Co-Pilot & Inventory Inspector (v2).

Startup review refreshed all seven widget admin files, generated the complete current docs inventory, reviewed all nine changed documents across the 21-commit docs delta, and reviewed the 112-commit widget delta with relevant patches and targeted source reads. Additional relevant multiroute, partner and catalog reports were reviewed. This was a strategy and documentation review, not a live-site audit or a retest of previously reported engineering results.

Reviewed pre-session repository snapshots:
- Docs: 778db9f34704a762c5d646bf6650a236a36c54ee.
- Widget: 3acc78d14229955d8a1052c2f327493d44a51253.

No writes to carclever-find-my-car, deployments, account creation, outbound messages, affiliate clicks or spending occurred.

## Current operating context

The fresh admin record says Auto.dev Growth was cancelled and expires on 2 October. The prospective Free Starter allowance is 1,000 calls per month shared across surfaces; post-expiry behavior still needs checking. Fractal's future remains unresolved ahead of its 14 October renewal. The existing website catalog journey and the unfinished Google Search draft remain separate workstreams. This review does not supersede them.

The prior GetCarWiseAdvisor Reddit account is recorded as banned. The distinction between a subreddit ban and a sitewide suspension, and the current appeal/status outcome, is not established here. It matters to Developer Funds eligibility. Do not open an alternative account to evade a suspension.

## Corrections to the revenue case

### Developer Funds

The current H2 2026 terms apply from 1 August through 31 December 2026. The first one-time engagement milestone requires a seven-day average of 5,000 qualified daily engagers and pays US$4,000. Recurring payments require a separate application and qualifying monthly averages: the published examples give US$0 at 5,000, US$555.56 at 10,000 and US$5,000 at 50,000. Install payments require qualifying communities and holding periods. These are contingent incentives, not a guaranteed recurring baseline or a commitment for 2027.

The drafts' 500-user threshold comes from the expired H1 scheme. Their income forecasts need rebuilding around current rules, actual acquisition and repeat use.

Source: [H2 2026 Developer Funds terms](https://support.reddithelp.com/hc/en-us/articles/50860336905108-Reddit-Developer-Funds-H2-2026-Terms).

Australia appears on the supported-country list, but participation still requires good standing and enrollment checks. Reddit's earning-money policy excludes advertisements from eligible content. Whether this proposed affiliate-enabled utility is eligible therefore needs a specific Reddit determination.

Source: [Earning money on Reddit](https://support.reddithelp.com/hc/en-us/articles/37760672112660-Earning-money-on-Reddit).

### Edmunds affiliate income

The current internal partner record states US$10 for approved New and Used actions and US$3.50 for trade-in. The drafts' older US$3 / US$5–8 figures and a supposed negotiated US$10 rate are inconsistent with that record.

More importantly, the supplied agreement as recorded in ADDENDUM_TASK78_MULTIROUTE_CREDITS_REDDIT_IMPACT_20260924.md includes social restrictions in section 3.B.I and requires express written Edmunds approval for social commissions in section 3.B.II. Native placement or an intermediate GetCarWise page does not automatically remove the originating social source.

Obtain property- and source-specific written approval before treating organic Reddit, paid Reddit or a Devvit app as commissionable. No such approval was established in this review.

## Reddit platform implications

Official Devvit rules require app review and permission for third-party destinations. Their approved LLM list currently names OpenAI and Google Gemini. They also restrict using apps to promote external app versions and require privacy, terms and deletion handling. A native app must deliver useful functionality itself; an affiliate destination requires explicit review rather than assumed permission.

Source: [Devvit rules](https://developers.reddit.com/docs/devvit_rules).

Server HTTP requests use reviewed domain allowlists, HTTPS and runtime limits. Network approval does not substitute for partner permission. The proposed inventory service and any custom backend must be assessed within those limits.

Source: [Devvit HTTP fetch](https://developers.reddit.com/docs/capabilities/http-fetch).

The proposed paid promoted interactive-app format, moderator installation demand, competitor absence and guaranteed moderation advantages were not verified. Claims of zero bounce, no competition and automatic exemption from commercial restrictions should be removed. Checked onboarding boxes in a planning draft are not evidence of completed enrollment.

## What can actually be reused

| Existing asset | Reuse assessment |
| --- | --- |
| Car-buying knowledge, intent questions, comparison explanations | Strong conceptual reuse; adapt to community needs and native UI. |
| Typed search inputs, result-card patterns and deterministic link decisions | Useful implementation references, subject to technical and permission review. |
| Current Lite V2 orchestrator | Not a direct port: the reviewed route uses Anthropic, outside the current Devvit approved LLM list. |
| Existing ChatGPT/Claude MCP product | Separate distribution surface; a Reddit app is not another connector installation. |
| Website Impact catalog prototype | Possible later data adapter; current locality, freshness and permission gaps persist. |
| Deal Score, TMV valuation, affordability and recall features in the drafts | Not established as available components of the reviewed Lite V2 route. |

The current chat-v2 route exposes two tools, find_matching_vehicle and resolve_dealer_url. Its existing origin restrictions also mean direct reuse cannot be assumed. This does not establish the feature inventory of every other repository or version.

## Catalog evidence and limitations

The recorded September tests observed approximately 1.35 million feed rows at that time. That count is not proof of current active stock. The catalog ID is distinct from advertiser programme 52125.

The tested feed used Text1 for model, Category and CurrentPrice for filtering, and Manufacturer for dealer names rather than vehicle makes. Condition was absent/empty in the tested samples; no reliable VIN field was established. Sample location data was city/state, with ZIP-radius support unresolved. A feed timestamp does not prove per-item stock freshness.

The C1–C8 report recorded bounded API tests and URL-shape inspection, not clicked affiliate destinations. The private prototype's reported 62 passing tests are historical evidence, not a retest in this session. The September 30 locality desk audit prepared additional queries but did not run them.

Therefore do not promise VIN-level checks, condition precision, TMV appraisal, nearby live inventory or valid round-robin vanity destinations from this feed. Do not broaden the website-only catalog scope into MCP or Reddit without a separate decision.

## Smallest sensible product

A CarClever community buying helper could ask for budget, intended use, seating and priorities, then return two or three model tradeoffs, buyer questions and a copyable discussion brief. It should be useful without an outbound click.

Inventory can follow only after source permissions and data quality support the promise. An approved LLM can follow if structured rules and existing content are insufficient. No new US$500 monthly model budget is justified by the current evidence.

A buying decision is episodic. The fund forecast needs a credible reason for sustained community use, such as useful comparisons and discussion support, rather than assuming each shopper returns daily. At 5,000 daily engagements, even one Auto.dev call per engagement would be roughly 150,000 monthly calls against a shared 1,000-call allowance. That is an illustrative one-call-per-engagement calculation, not a measured workload; caching and an inventory-free first product could reduce calls.

## Recommended decision gates

1. Establish the existing Reddit account's status and eligibility; confirm the proposed utility, commercial destinations and funding treatment with Reddit.
2. Obtain Edmunds' written approval for the specific Reddit property and intended organic/paid traffic source before forecasting affiliate income.
3. Prepare a read-only engineering feasibility assessment: reusable deterministic components, Devvit architecture, approved AI options, deletion obligations, source quality and a bounded operating-cost estimate.
4. Validate moderator interest and user utility before commissioning a build. Do not assume permission to contact moderators from this review request.
5. If those gates pass, authorize a small native prototype with explicit success measures: meaningful uses, repeat use, community adoption, approved outbound conversion and operating cost.

The next deliverable should be a corrected feasibility brief. No code or deployment is authorized by this review.
