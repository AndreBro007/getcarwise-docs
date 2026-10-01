# CarClever Reddit Catalog App — Strategy and Technical Build Plan
Date: 1 October 2026 (Australia/Brisbane)
Owner: ChatGPT/Codex, per André's explicit instruction
Status: Technical research completed; implementation direction authorized. Code has not yet been scaffolded or deployed.
Supersedes: the earlier feasibility review's utility-only recommendation and requirement to complete all commercial setup before any prototype work.

## 1. Confirmed direction

Build a new, separate native Reddit app using the Impact Edmunds catalog as its only inventory API. Edmunds affiliate commissions drive the business case; Developer Funds are optional upside. No Auto.dev or Fractal dependency. No VIN search. ChatGPT/Codex owns research, strategy and this new build; Claude is not a dependency.

The supplied master strategy remains the destination: a native buying co-pilot, catalog results, useful comparison and user-initiated Edmunds referrals. Start with the smallest working inventory journey, then add conversation and deeper buying help. Do not replace it with an advice-only product.

Technical proof can proceed while promotional-property registration and commercial review are completed in parallel. Public distribution and paid traffic are later steps.

## 2. Evidence reviewed

Both original uploaded drafts were reread, and Claude's new Impact Edmunds Vehicle Catalog API — Complete Findings report was read in full. André's screenshot shows Impact's More menu includes Custom Software and Offline/Other promotional channels. Official Impact guidance independently confirms Custom Software registration using a name, public listing URL, description of at most 1,000 characters and optional screenshot. That is a practical setup path; categorizing Devvit as Custom Software is our recommendation, not an explicit Impact endorsement of Devvit.

The existing private prototype source was inspected directly:
- carclever-widget, feature/impact-catalog-prototype, lib/impact-catalog.ts, blob 5f5115ae71f1fc12ae6151e5097deb7f3b2cae1d.
- lib/impact-catalog-shared.ts, blob 36f7041f296d7c7a58b966877c6c8972d97770cb.

The official Reddit React starter's AGENTS, package, manifest, Vite configuration, server entry and API route were inspected. The observed starter currently uses React 19, Hono, Vite and Devvit 0.14.6. Its AGENTS prose mentions Express/tRPC-era structure, while its actual current implementation uses Hono routes: use the current files and schema, not stale prose or the drafts' illustrative snippets.

Local runtime inspection found Node 24.19.0, satisfying the current quickstart's 24.18.0+ requirement. Dependency installation, compilation, Reddit authentication and live integration have not been attempted.

## 3. First product: catalog search and buyer shortlist

Working title: CarClever — Cars Within Your Budget. New project/repository: carclever-reddit (proposed; not yet created).

First flow:
1. Launch from a lightweight native post.
2. Choose a supported model or SUV category and a USD budget.
3. Display three to six catalog cards: year, make, model, trim, price, dealer, city/state and an explicit Edmunds action.
4. Select up to three cards for comparison.
5. Generate a concise discussion brief from the selected criteria and cars.
6. On a deliberate click, use Reddit's navigation API to open the returned tracked link.

The first category and model vocabulary will match the inspected adapter: SUV; CR-V, RAV4, Camry, Accord, Outlander PHEV and Highlander. These are existing adapter allowances, not a claim that every token was independently retested today. Begin live validation with the previously proven CR-V and SUV searches, then validate additions.

Start with existing price bands. Clear loading, thin-results, no-results, timeout, disabled and retry-later states are part of the initial product. Permit users to widen a budget or change a model explicitly rather than silently changing their request.

Use “View on Edmunds” rather than promising a quote form or local dealer when the destination and locality have not established that behavior. A short visible affiliate explanation sits beside the action. Availability is confirmed at Edmunds; no fake live-stock guarantee.

## 4. Architecture

| Layer | Implementation | Role |
| --- | --- | --- |
| Native client | React/TypeScript, Vite | Search inputs, cards, comparison, buying brief |
| Reddit server | Hono, @devvit/web/server | Validate inputs; fetch and normalize catalog results |
| Catalog API | Direct server fetch to api.impact.com | Only inventory source |
| Credentials | Devvit app settings marked isSecret | Account SID and auth token stay server-side |
| Cache | Managed Devvit Redis | Short-lived catalog results and request coordination |
| Outbound navigation | @devvit/web/client navigateTo | User-initiated external link with Reddit confirmation |
| Later AI | Approved provider, behind bounded server interface | Translate free text into supported criteria; explain tradeoffs |

No separate Vercel backend, vector database, daily full-feed sync or paid model subscription is needed for the first proof. Target no new recurring service bill for that stage. Catalog access is already available; this review did not discover a per-call catalog charge. Optional future model usage and advertising require a separate budget.

The frontend calls its own /api/catalog endpoint; only the server calls Impact. Request api.impact.com as an exact fetch hostname through devvit.json and explain it in README. edmunds.sjv.io is a navigation destination, not an API to fetch for automated link checking.

## 5. Concrete reuse

Copy the catalog query builder, bounded fetch behavior, card normalization, host checks, thin/empty states and safe input vocabulary into an independent module. Keep provenance in the new repo. Do not import the current production app at runtime.

Replace:
- Next.js server-only and process.env handling with Devvit server boundaries and settings.get.
- Prototype pageContext with a new Reddit-specific internal context.
- Per-request opaque IDs with suitable session-stable identities for comparison/cache reuse without exposing unneeded raw data.
- Existing raw image rendering with a Devvit-compatible path.

Retain:
- HTTP Basic authentication using full Account SID, not the public numeric partner ID.
- Query expression: Text1 = 'CR-V' AND CurrentPrice <= 25000.
- Catalog 34070; advertiser programme 52125 is separate.
- Returned tracking Url exactly as supplied.
- Dealer name from Manufacturer.
- No inferred condition or VIN fields.

Normalize all ten fetched items before selecting up to six usable cards. The inspected adapter currently slices to six before normalization, so an invalid early item can prevent a valid later item from appearing. Validate missing, zero, negative and malformed prices before budget comparisons.

## 6. Operational design improvements

### Cache and quota

Begin with a configurable 15-minute cache for catalog searches. This is a proposed operating setting, not a measured optimum. Include every supported search constraint in the key. Label the result retrieval time separately from source-feed freshness.

Use a short Redis lock to collapse simultaneous identical misses per installation. Redis is scoped to installations; it does not automatically provide one shared cross-subreddit counter. Start with one test community and a conservative per-installation upstream allowance, inspect Impact quota headers, and design aggregate quota handling before broad rollout.

p-limit alone is a concurrency control, not an hourly limit, and an in-memory queue is not a global serverless limiter. On 429, honor Retry-After without sleeping beyond Reddit's 30-second request window: return retry-later or use a suitable cached response. Use an approximately eight-second upstream timeout and a bounded overall response budget.

### Images

Current Reddit docs require Reddit-hosted displayed media. Start with text cards and a bundled placeholder so photos do not block the first API proof. Then test media.upload for permitted catalog image hosts and cache the returned Reddit media URL. Do not blindly hotlink every ImageUrl or upload the entire catalog.

### Privacy and telemetry

For the first prototype, keep selected cards and preferences in the current browser session; cache public catalog responses without user IDs. Avoid persistent chat history and automated commenting. Add aggregate search/result/cache/error counts.

An outbound-button event is an outbound action, not an approved lead. Reddit's external-link confirmation can be cancelled. Impact remains the source of truth for recorded clicks/actions. Preserve item tracking links initially; only add subIDs after validating Impact's supported syntax and the new-source approval.

## 7. Location path without another inventory API

Show dealer city/state from day one. This is useful even before radius search.

Next, use the already prepared bounded locality probe to inspect usable field names and test one geographic query if justified. If server-side geography works, add it. Otherwise offer a clearly labeled preference/filter within fetched results and measure its usefulness. Do not call a small nationally returned pool “nearby inventory.”

A later permitted catalog download/index is an option if better geography needs it. It is not required for the initial build. No ZIP-to-distance promise, bulk download or paid external geography service is assumed.

## 8. AI and strategy improvements after the core proof

1. Natural-language search can fill the same validated form, for example “CR-V around $25k.” AI may select allowed criteria but never emit an unrestricted Impact query or manufacture listings.
2. Comparison can show advertised price, year, trim and dealer location, with missing-data labels. Explain why a car fits the user's constraints; avoid an unsupported market-value score.
3. A buying brief can summarize budget, choices and open questions for manual sharing. This makes the product contribute to Reddit discussion.
4. A moderator-configured landing screen can emphasize an appropriate category or budget and disable commercial actions if the community requires it.
5. Add curated buyer checklists and questions. Negotiation worksheet parsing and fee research are later, separate capabilities.
6. Keep GetCarWise as the publisher and CarClever as the product to reinforce both brands. Place branding clearly without making the experience a link funnel to another app.

Core commercial measurement: searches with usable results, comparison use, outbound actions, confirmed Impact clicks, approved actions and net revenue. Measure each stage separately; fund metrics remain optional.

## 9. Groundwork and proof milestones

| Step | Owner/action | Evidence of completion |
| --- | --- | --- |
| 1. Separate project | Codex prepares source; new isolated repo access arranged | Own package, manifest and source; no production-app runtime dependency |
| 2. Scaffold and fixtures | Codex uses current official starter and adapts catalog modules | Build/type checks; meaningful input, normalization and failure tests |
| 3. Native runtime | Connect André's selected Reddit account and test community | Interactive post loads; client/server request works in private playtest |
| 4. Live catalog | Set secrets securely; request api.impact.com domain | CR-V and SUV bounded reads return real cards through Devvit |
| 5. Buyer flow | Codex adds compare and buying brief | Mobile/web flow works; empty/timeout/429 paths behave correctly |
| 6. Referral validation | André performs agreed manual clicks | Destination checks and Impact click reporting; no fabricated leads |
| 7. Launch preparation | Promotional property, partner/source approval and Reddit review | Correct source listing, required policy links and review outcome |
| 8. Small community pilot | One willing community, before paid acquisition | Real usage and referral evidence guide further work |

App upload/playtest is distinct from public publishing. Native backend proof requires Reddit runtime; local tests alone cannot establish that Impact is reachable through Devvit. New-app domain approval is part of that integration experiment, not something this report claims has already happened.

## 10. Administrative work in parallel

Recommended Impact property:
- Type: Custom Software, subject to the available form and Impact confirmation if needed.
- Name: CarClever Reddit App — GetCarWise.
- Store URL: actual public Reddit app listing once available; do not invent it.
- Description: A native Reddit car-shopping utility for US buyers, offering budget/model search, catalog comparisons and disclosed Edmunds referral links.
- Screenshot: the working prototype.

The existing approved Edmunds relationship and read-only catalog access can be reused; a new affiliate account is not indicated. The property's registration and Edmunds-specific source permission are separate setup items. Treat them as achievable launch tasks, not reasons to stop technical development. No outreach is authorized merely by this plan.

Fund enrollment, tax/payment onboarding, full-feed synchronization, price-appraisal claims and paid ads do not need to precede the first private prototype.

## 11. Sources and remaining proof

Primary references:
- [Reddit app quickstart](https://developers.reddit.com/docs/quickstart)
- [Devvit Web](https://developers.reddit.com/docs/capabilities/devvit-web/devvit_web_overview)
- [HTTP fetch](https://developers.reddit.com/docs/capabilities/http-fetch)
- [Settings and secrets](https://developers.reddit.com/docs/capabilities/server/settings-and-secrets)
- [Navigation](https://developers.reddit.com/docs/capabilities/client/navigation)
- [Media uploads](https://developers.reddit.com/docs/capabilities/server/media-uploads)
- [Backend test harness](https://developers.reddit.com/docs/guides/tools/devvit_test)
- [Official React starter](https://github.com/reddit/devvit-template-react)
- [Connect custom software in Impact](https://help.impact.com/partner/what-would-you-like-to-learn-about/account-management/account-settings/connect-media-properties/connect-a-browser-extension-and-custom-software)

Claude's attachment supplies historical live Impact evidence; today inspected the implementation and platform sources, not new authenticated Impact calls. Technical architecture is supported by the platform; the full Devvit-to-Impact integration remains to be proven by steps 3–4. Source and domain permissions are launch/integration tasks, not forecasts of rejection.
