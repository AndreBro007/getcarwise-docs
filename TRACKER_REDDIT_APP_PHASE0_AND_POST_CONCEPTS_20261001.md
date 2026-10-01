# CarClever Reddit execution tracker and interactive-post concepts
Date: 1 October 2026 (Brisbane)
Owner: ChatGPT/Codex; account decisions: André
Status: Working execution plan. Research completed; setup and code not yet executed.
Companions: PLAN_REDDIT_CATALOG_APP_BUILD_20261001.md; RESEARCH_REDDIT_BUYER_INTENT_PHASE0_20261001.md

## 1. Decisions and direction

- Proposed human-facing account: Andre_GetCarWise. André proposed this name; availability and account creation have not been checked/performed.
- Position GetCarWise as practical car-buying help; CarClever is the product providing guided decisions. AI is an enabling technology, not the main promise.
- Affiliate referrals drive revenue; Reddit funds are optional.
- Separate app, Impact catalog only; no Auto.dev/Fractal dependency or VIN/radius requirement.
- Start with native interactive-post proof, then iterate with users.
- Edmunds handles ZIP/local refinement and dealer enquiry after the tracked handoff.
- Availability confirmation is a natural, useful next step; do not intentionally retain unavailable cars or invent stock urgency.
- Commission mechanics are already understood: record eligible approved enquiries separately from clicks, without repeatedly revisiting this distinction in strategy discussion.

## 2. Progress states and operating rules

Use Not started, In progress, Waiting on access, Ready to test, Verified, or Deferred. Attach an actual URL/commit/test result when marking Verified. Research is not deployment evidence.

At the next working session, take the next unfinished step, complete or verify it, update this tracker and record the blocker if any. Work through Phase 0 one item at a time; do not present every portal action at once or mark checkboxes from assumptions.

## 3. Phase 0 — groundwork tracker

| ID | Task | Owner | Status | Evidence needed |
| --- | --- | --- | --- | --- |
| R0.1 | Choose developer-owner account; decide whether public presence uses Andre_GetCarWise | André, guided by Codex | Not started | Owner choice; username availability if creating |
| R0.2 | Create private carclever-reddit repository and add to ChatGPT GitHub connector | André; Codex verifies | Waiting on access | Repo URL and connector read/write check |
| R0.3 | Register/select Devvit project from current React starter | André + Codex | Not started | Real app slug and portal ownership |
| R0.4 | Authorize Devvit CLI in the build environment | André OAuth; Codex verifies | Not started | whoami shows correct owner |
| R0.5 | Create/start controlled development installation and native test post | Codex, with owner setup | Not started | Playtest URL opens |
| R0.6 | Define app secrets; securely enter existing Impact SID/token | Codex configuration; André secure entry | Not started | Server-side availability; no client/Git secret exposure |
| R0.7 | Declare api.impact.com and request fetch permission | Codex | Not started | Portal approval and bounded API read |
| R0.8 | Prepare affiliate explanation, privacy/terms scope and app description | Codex drafts; André reviews | Not started | Reviewable documents matching actual data use |
| R0.9 | Add Custom Software promotional property using actual app listing URL | André + Codex | Not started | Property record; no invented listing URL |
| R0.10 | Confirm Edmunds property/source treatment for native Reddit referrals | André; Codex prepares exact details | Not started | Source-specific approval record |
| R0.11 | Review GetCarWise homepage messaging and product-specific claims | Codex | In progress | Homepage read; proposed copy/spec pending; no edits yet |

R0.9–R0.10 proceed alongside development and must be resolved before public monetized rollout. Devvit secret storage follows the first installation. New AI credentials, fund onboarding and paid ads are deferred.

## 4. Build, usability and rollout tracker

| ID | Milestone | Status | Completion test |
| --- | --- | --- | --- |
| R1.1 | Isolated scaffold and safe catalog adapter | Not started | Build/types pass; meaningful input/response tests |
| R1.2 | Interactive launch screen and intent capture | Not started | User click opens intended screen; choices survive transition |
| R1.3 | First real catalog journey | Not started | One supported model/two budgets → three cards |
| R1.4 | Deliberate tracked Edmunds handoff | Not started | User-initiated navigation; manual destination/report checks |
| R2.1 | Curated advice paired with results | Not started | Users understand why choices merit investigation |
| R2.2 | Small usability trial | Not started | Observed use; record confusion and intended next action |
| R2.3 | One-variable design iterations | Not started | Compare behavior after one change, not broad redesign |
| R3.1 | Moderator/own-community distribution variant | Deferred | Working demo, transparent commercial scope, suitable placement |
| R3.2 | Public review/listing | Deferred | Reddit review and commercial setup completed |
| R3.3 | Paid acquisition experiment | Deferred | Accepted ad format/destination; separate approved budget |
| R4.1 | Compare/brief/more models/optional AI | Deferred | Evidence that the addition improves the buyer journey |

The proof does not require a full chatbot, complex scoring, a catalog download or an automated commenting system.

## 5. Brand and website message architecture

Homepage inspected through current public retrieval: prominent AI-led heading, followed by finder/tools and intelligence-engine language. Read-only review; no WordPress edits.

Recommended order:
1. Buyer problem: too many choices, conflicting advice, uncertainty about what to check.
2. Outcome: clearer shortlist, useful tradeoffs, better questions before dealer contact.
3. Actions: choose cars, compare relevant options, inspect listings, take the next step.
4. Technology: CarClever uses available data and AI where helpful to organize information.
5. Transparent commercial explanation and product-specific feature availability.

Possible direction, not final published copy:
- Heading: “Choose your next car with a clearer plan.”
- Supporting line: “Narrow your options, understand the tradeoffs, and know what to ask before contacting a dealer.”
- Technology explanation: “GetCarWise combines practical buying guidance with data and AI-assisted tools to help you make sense of your choices.”

Current site's “Only Independent AI” exclusivity and feature promises should be reviewed against each actual product during the copy task. Do not transfer all legacy-tool features to the Reddit prototype.

## 6. Research burden evidence

A close match for André's remembered 11–14-hour figure exists in Cox Automotive's 2023 Car Buyer Journey study: about 11 hours 45 minutes for new buyers and more than 14 hours for used buyers, from beginning to end. This includes the broader buying process; it is not research-only time.

The original repo location for the remembered figure was not found through the bounded search. Do not claim that this is where our earlier copy came from.

Current 2026 Cox research reports meaningful AI use and continued importance of third-party shopping sites, supporting technology-assisted help as a positioning hypothesis. Neither study measures GetCarWise effectiveness. Avoid “save 10 hours,” “decide in two minutes” or any quantified savings guarantee.

Suggested nonnumeric promise: less research overload, clearer choices and a practical next step. If using the older statistic, label the study year and scope.

## 7. How the app starts

Create an interactive Devvit post with a lightweight inline launch screen. A click opens the expanded app, where we collect the needed choices and call the catalog. It does not read a viewer's mind, scan their comments or launch automatically.

Official current documentation supports HTML preview screens and expansion from a trusted user click. Keep the inline screen simple and feed-friendly.

### Concept A — budget prompt (recommended first)

Post title: “Shopping for an SUV around $25k? Start with a few sensible options.”

Inline preview: one short usefulness statement and a “Explore options” button.

Expanded screen: choose the supported model and one of two budget bands → short buyer guidance and three catalog examples → “View on Edmunds.” Dealer city/state visible; local refinement continues there.

Why first: one clear intent, low implementation effort, easy to explain and measure. The displayed budget is illustrative; do not promise every user has suitable results.

### Concept B — shortlist helper

Post title: “Torn between CR-V and RAV4? What matters most to you?”

Preview launches a simple priority question, then a balanced curated explanation and catalog examples. Useful for advice communities and moderator placements. We need supported factual guidance; no fake community-vote percentages or unsupported model scoring.

### Concept C — buying-discussion starter

Post title: “Before you ask what car to buy, organize your budget and priorities.”

Collect a small set of constraints; return a concise buying brief the user can manually paste into a discussion, with optional catalog exploration. Good candidate for a moderator-approved megathread helper; no automated posting.

### Concept D — ready-to-investigate examples

Post title: “See what these models look like within your budget.”

Minimal input and catalog cards; appropriate for a focused owned-community or acquisition destination. Test whether it gives enough decision help rather than becoming another inventory list.

Use one shared codebase with configurable headlines/defaults/guidance; different entry experiences do not require four separately maintained apps. Initially implement only Concept A.

## 8. Learn before expanding

Measure launch → valid intent selection → usable results → deliberate outbound action. Pair counts with qualitative observation: can the user explain their next step, and did the app resolve uncertainty?

For usability, recruit a small initial group when the prototype exists and ask what they came to decide, where they hesitated and whether the output helped. That group tests comprehension, not statistically proven lead conversion.

Change one variable at a time: title, question order, guidance wording, card count or CTA wording. Judge paid, moderator and owned-community acquisition separately. Full-screen chat and broader personalization can follow observed need.

## 9. Sources

- [Cox 2023 Car Buyer Journey study](https://www.coxautoinc.com/insights/2023-car-buyer-journey-study/)
- [Cox 2026 Car Buyer Journey findings](https://www.coxautoinc.com/insights/cox-automotive-car-buyer-journey-study-finds-efficiency-digital-tools-and-ai-drive-record-satisfaction/)
- [Current GetCarWise homepage](https://getcarwise.app/)
- [Devvit launch-screen customization](https://developers.reddit.com/docs/capabilities/server/launch_screen_and_entry_points/launch_screen_customization)

Next working item: R0.1, followed by R0.2. Decisions, setup and proof evidence are tracked here; no account, repository or app code has been created by this planning session.
