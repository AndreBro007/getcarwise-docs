# Reddit buyer intent, Edmunds funnel and Phase 0 setup
Date: 1 October 2026 (Brisbane)
Owner: ChatGPT/Codex
Status: Research and setup specification complete. Account selection, repository provisioning, CLI authorization and authenticated catalog integration remain to be performed.
Companion: PLAN_REDDIT_CATALOG_APP_BUILD_20261001.md

## 1. Strategic fit

The existing GetCarWise strategy's “clear second opinion before contacting a dealer” fits this channel. Reddit can host the useful decision step itself. GetCarWise is the publisher, CarClever the product, Edmunds the outside shopping/dealer destination. Affiliate income drives the project; Reddit funding remains optional.

The new direction is a native community utility, not another campaign that merely posts app links. Help a buyer resolve uncertainty, show relevant catalog choices, then offer an explicit tracked continuation. ZIP matching is unnecessary for the initial value proposition: Edmunds handles local search after handoff.

## 2. What the research supports

Read the current overall marketing strategy and relevant multiroute/Impact addendum; examined public Reddit buying discussions, the r/cars weekly buying template and Reddit's own current audience/business guidance.

This is exploratory qualitative evidence, not a representative sample or proof of conversion. The inspected individual threads include a buyer comparing Tucson/CR-V/RAV4 hybrids and asking about years/trims, and another comparing four luxury SUVs with maintenance and feature concerns. The r/cars template asks for location, price, vehicle type and other buying needs; it directs buying questions to its megathread rather than the main queue.

Reddit's May 2026 survey, published in August, emphasizes human validation of AI recommendations and firsthand experience. It is platform-sponsored, covers general shoppers and is not a forecast for our app. Its useful implication is that the app should support a discussion and a decision, rather than claim to replace owner experiences.

Reddit's business guidance recommends genuine helpful participation, a clear business profile and respect for each community's promotion rules. It supports André's preference for a human account voice without suggesting concealed ownership.

## 3. Match the product to buyer intent

| Buyer question | Value we can provide | Natural Edmunds continuation |
| --- | --- | --- |
| What can I get for this budget? | A manageable set of catalog examples and the tradeoffs to consider | Browse matching cars near the buyer |
| I am choosing between these models | Short, balanced explanation and a simple factual comparison | Compare available examples locally |
| Does this choice fit my needs? | Clarify use case, priorities and what remains to check | Inspect trim/details and contact a dealer |
| Is this advertised car worth investigating? | Organize known listing facts and questions for the seller | View the actual listing and confirm availability |
| I am ready to contact someone | A short checklist: stock, out-the-door price, history/inspection | Submit the relevant dealer enquiry |

The first proof should focus on a budget/model choice, not attempt to serve every intent. Reliability claims and model-year recommendations require curated evidence; do not generate unsupported technical assertions from the catalog. User priorities can guide the advice, but do not pretend the catalog has verified seating, hybrid type or condition filters when it does not.

## 4. The commercial funnel

Reddit question or discovery → useful native guidance → sensible shortlist/catalog examples → explicit tracked Edmunds click → local search/availability/details → qualifying enquiry → Impact approval and commission.

The click need not lead to an immediate enquiry or the precise example vehicle. The recorded Edmunds programme has a 30-day referral window and last-click attribution. A later eligible enquiry can potentially count within that window, subject to the applicable action terms and tracking. Do not promise cross-device continuity, every subsequent enquiry or all purchases; attribution can be superseded.

A user browsing a listing, checking availability visually or clicking a contact control is not automatically a payable lead. The commercial event is an eligible submitted enquiry approved by the programme. Track app progress, outbound actions, recorded clicks, pending/approved/declined actions and commission separately.

There is no need to force a ZIP field into the app or to manufacture urgency. Show known dealer city/state and explain that the user can check local availability at Edmunds. The catalog is useful evidence of advertised examples; live inventory freshness remains unproven, but it need not block this decision-and-handoff product. Availability confirmation is a sensible next action, not a reason to intentionally surface stale listings.

Initially preserve returned item links. A model/category continuation using an approved separate tracked destination may be useful when examples are distant or unavailable; validate the fallback once and label it “Browse this model near you.” No round-robin destination rotation.

## 5. Account and positioning

André identifies the existing account as u/CarClever_GPT. A new human-led public presence is an option, not an implementation prerequisite. Do not infer that account is suspended from older notes naming a different account.

Recommended account style: a real founder identity, for example Andre_CarWise if available. Availability has not been checked. Keep AI/GPT out of the headline promise; disclose the owner and relevant automation clearly in the profile/app.

Possible bio: “André, founder of GetCarWise. Building practical tools to help US car buyers compare options and know what to ask before contacting a dealer.”

The Devvit app identity and a founder's community account are different roles. Choose a stable developer owner; it need not determine the public-facing marketing username. A new account cannot be used to bypass an existing community/site suspension.

Offer a useful answer before suggesting the tool; do not fabricate US residence, dealership expertise, owner experience or independent endorsement. Honest tradeoffs, short explanations and the ability to take a buying brief back to the community are more credible than an AI-first pitch.

## 6. Distribution experiments

1. Controlled app playtest: technical validation, then a small usability trial in a community we control. Creating it does not create an audience automatically.
2. Willing moderator pilot: present a working utility and disclose affiliate actions. Ask for one suitable placement, not blanket promotion.
3. Own community/app directory: an alternative controlled destination when a large community is unsuitable; outside discovery still needs work.
4. Permitted founder participation: useful responses in relevant discussions, following the actual community rules.
5. Paid acquisition later: test an accepted ad format and destination. The draft's interactive promoted-post format has not been established; a conventional ad pointing to an allowed app post/demo is an experiment to confirm, not a promised capability.

No account creation, moderator messages, posts or ad spend occurred in this research. Public rollout and the desired social-origin affiliate treatment remain subject to source-specific review. These are setup tasks alongside development.

## 7. Tools and execution ownership

| Tool/system | Our use | Current setup implication |
| --- | --- | --- |
| GitHub | Source history, tests, reviewable changes and documentation | New private carclever-reddit repo proposed; add it to the ChatGPT GitHub connector's selected repos |
| Codex workspace, Node/npm and TypeScript | Edit, install, compile and test | Node 24.19.0 observed earlier; dependencies not installed yet |
| Devvit project-local CLI | Login, playtest, upload and eventually publish | Reddit OAuth must be connected in the environment that executes these commands |
| Reddit developer portal | App ownership, domain requests and app details | Select owner; create/register the React project |
| Devvit server, secrets and Redis | Runtime, credential storage and cache | Managed by Reddit; separate Vercel project not required |
| Browser/device testing | Native web/mobile behavior and outbound confirmation | Starts once there is a playtest URL |
| Existing Impact account/API | Read catalog and supply tracked URLs | Secure full SID/token handoff; no credentials in chat or Git |
| getcarwise-docs | Strategy, setup log and outcome record | Already writable by the connector |

Current GitHub tools can write the existing authorized repos but expose no repository-creation action. Creating/connecting the new repo is an owner setup task; it does not need Claude. No new OpenAI/Gemini account, key or payment setup is required for the initial structured prototype.

## 8. Phase 0 — minimum setup

| Step | André/account owner | Codex | Completion evidence |
| --- | --- | --- | --- |
| 0.1 Ownership | Choose existing/new developer owner account | Explain separation from public founder identity; record choice | Selected account can access Reddit developer portal |
| 0.2 Source repository | Create private carclever-reddit and grant connector access | Verify read/write access and establish project README | New repo reachable and an isolated change re-fetched |
| 0.3 Devvit registration/auth | Complete Reddit sign-in/OAuth personally | Prepare current starter/CLI; verify whoami | Correct owner authenticated in build environment |
| 0.4 Test community | Confirm controlled test destination when prompted | Follow starter's development-community/playtest setup | Native test post opens |
| 0.5 Impact secrets | Provide existing full SID/token through secure secret entry; confirm current token | Define Devvit secret settings and bounded adapter | Secrets available server-side; no browser/Git leakage |
| 0.6 Network request | Review intended API use if needed | Declare api.impact.com and README purpose | Domain approval recorded; bounded server fetch succeeds |
| 0.7 Launch groundwork, parallel | Register Custom Software property when real listing URL exists; obtain source approval | Prepare description, screenshots and clear app disclosures | Correct property/source record and approval outcome |
| 0.8 Prototype checks | Perform agreed manual destination checks later | Record mobile/web behavior and Impact outcomes | Real click reporting checked without dummy lead submissions |

Devvit secret storage requires an installation first, so do not insist on finishing secrets before the first playtest installation. Devvit handles Reddit app authentication; no separate legacy Reddit Data API key is needed. OAuth in a browser alone is not proof that the build CLI is authenticated.

Phase 0 is complete for build purposes when repository access, correct CLI identity, a test post and secure configuration are established. Live-catalog proof additionally requires the fetch-domain grant and successful bounded calls. Commercial setup proceeds in parallel; fund tax/bank onboarding is deferred.

## 9. Keep the proof small

First technical proof: one supported model (CR-V), one or two budgets, three catalog cards, one clear Edmunds action, loading/empty/error handling. No chat, VIN, radius lookup, feed download, persistent user history or advanced scoring.

First user-fit trial: add a short curated explanation of what to compare and questions to ask. Then change one thing at a time: guidance wording, input order, card count or CTA wording. Comparison, copyable buying brief, more models and optional AI follow only when the observed buyer journey benefits.

Technical success means native render + client/server request + real catalog results + deliberate functioning handoff. Buyer-fit success means users understand their choices and take an appropriate next step. Commercial success is a traceable approved action, which may arrive later inside the referral window.

## 10. Primary sources

- [Hybrid shortlist discussion](https://www.reddit.com/r/whatcarshouldIbuy/comments/1jb1n4l/all_around_best_hybrid_suv/)
- [Luxury SUV shortlist discussion](https://www.reddit.com/r/whatcarshouldIbuy/comments/1fdumg7/im_trying_to_decide_between_the_glc_xc60bmw_x3_or/)
- [r/cars weekly buying template, September 14](https://www.reddit.com/r/cars/comments/1wg2sy2/what_car_should_i_buy_a_weekly_megathread/) — search excerpt; full page retrieval failed.
- [Reddit Path to Purchase research](https://www.business.reddit.com/blog/path-to-purchase)
- [Reddit SMB participation guidance](https://www.business.reddit.com/learning-hub/articles/smb-how-to-use-reddit)
- [Devvit quickstart](https://developers.reddit.com/docs/quickstart)
- [Devvit FAQ](https://developers.reddit.com/docs/guides/faq)
- [Settings and secrets](https://developers.reddit.com/docs/capabilities/server/settings-and-secrets)

Internal programme evidence: STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md and ADDENDUM_TASK78_MULTIROUTE_CREDITS_REDDIT_IMPACT_20260924.md. The recorded 30-day window/last-click terms were not independently re-read from a new live account contract today.
