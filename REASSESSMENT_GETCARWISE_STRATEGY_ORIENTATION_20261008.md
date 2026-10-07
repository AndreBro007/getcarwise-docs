# GetCarWise strategy reassessment — orientation and questions

Date: 8 October 2026 (Brisbane). Owner: ChatGPT, business/strategy lane.
Status: exploratory; no new strategy, product, spending, renewal, cancellation, public launch or implementation decision approved.

## Scope and verification

This responds to André's attached “New app strategy and brainstorm prompt.txt”. The requested first stage is reconstruction, evidence separation, challenge and questions. Stop before final strategy, roadmap, architecture or build. History is evidence, not a sunk-cost constraint.

Reviewed snapshots:
- getcarwise-docs: `764d36168820edae32eff3e093a4c29b06f99da9`.
- carclever-widget: `6683e9548c02748af3ab438bab2c08dcec9a5c50` (admin and relevant-commit review only).

Fetched all seven required current admin files, without archives. Dynamically listed the complete docs root: 222 entries, comprising 221 files and one scripts directory; complete inventory printed during review. Compared ChatGPT's docs checkpoint with main: 29 commits ahead, 22 added documents, no deleted or renamed files in the net comparison. All 22 added documents were fetched/read, together with the older task-relevant evidence listed below. No comparison fallback was required.

Widget comparison: 15 commits since ChatGPT's checkpoint. Inspected relevant admin changes and net file patches. PR #73's fixed lite_result SharedID and PR #74's removal of the unsupported transaction-volume claim/Dataset schema agree with the code diff. This is a read-only headline verification, not independent live-runtime testing. Other implementation outcomes remain qualified as reported where they were not independently observed. No app code was written or tested.

Relevant task alignment: #78 distribution/revenue reassessment, B2 Reddit reassessment and related SEO/GEO interpretation. Do not act on unrelated tasks. TASKS.md and DECISIONS.md remain above the connector-size threshold; split pending, already mentioned this session.

## Journey reconstructed

The original proposition combined conversational car buying assistance, inventory and decision support, with dealer enquiries monetised through Edmunds. The original distribution expectation included platform discovery from conversational buyer intent.

The legacy Fractal product offered broader used/CPO search, comparison, affordability and risk/cost assistance. Find My Car narrowed the promise around vehicle search and dealer-URL resolution, with a VIN Buyer Check path. MatchScore is not the website Deal Score, and the newer app should not be credited with all legacy functionality.

The project also built an owned WordPress editorial and tool surface, separate Lite/LiteV2 experiences, affiliate destinations, NHTSA/EPA-supported capabilities, and a successful private Impact catalogue prototype. Engineering and host tests established useful functionality and exposed filtering, caching, link and data limitations. They did not establish customer demand or repeatable commercial performance.

The current record shows the new OpenAI app live. The older published app remains distinct from its 3.0.1 review submission. Anthropic and Muse public-review outcomes should not be assumed cleared. The early discovery observation involved a previous CarClever user; clean-account testing demonstrated metadata and explicit invocation, not dependable organic discovery.

Commercial evidence is thin: two historical completed leads were reported over months but remain unattributed. October 7's reviewed SharedID report recorded three clicks, zero actions, including one owner test and two blank-source clicks. Those three clicks are not an all-time lead total. Durable usage attribution remains incomplete; short request snapshots do not identify unique real buyers.

Previous strategy already moved beyond “publish an MCP app and wait”: September second-opinion/owned-site/partner work, late-September catalogue-first local-inventory investigation, and October 1 native Reddit buyer utility planning. Neither the paid Search draft nor a native Reddit deployment has established a distribution result. The Reddit work already considered native guidance, comparison and a buying brief, so that concept is not wholly new.

## Evidence categories

| Category | Current position |
|---|---|
| Known from reviewed records | Working product surfaces; bounded functional tests; a private catalogue prototype manually confirmed by André; two reported historical unattributed leads; small GSC traffic; catalogue field/locality/freshness gaps; current platform/revenue plans and gates. These are dated records, not new dashboard observations. |
| Strongly supported interpretation | Repeatable acquisition and approved-action economics remain unproven. Directory publication alone does not supply an audience. Broad conversational car search needs a sharper advantage. Existing assets make small learning exercises possible without committing to another full app. |
| Assumptions and prior conclusions | Buyers prefer a second opinion; a catalogue-led utility can improve the funnel; narrower questions outperform broad rankings commercially; native Reddit utility will be accepted and used; shareable results will acquire users; Edmunds actions can support the income goal. None is validated merely by being written in a prior strategy. |
| Unknown | Non-test usage and completion; why buyers stop; actual source-to-approved-action conversion; willingness to pay; accessible willing distribution partners; community/moderator acceptance; six-month operating burden; current account-specific Auto.dev allowance/terms; current catalogue availability/freshness. |

October 6 GSC reporting recorded 43 US clicks and about 2,220 impressions for 28 days through October 3. The broad SUV/budget cluster recorded 384 impressions and zero clicks, average position 31.3. A question cluster recorded 105 impressions and zero clicks at average position 7.1. Better question visibility is promising positioning evidence, not proof of a viable acquisition channel. Citations in AI answers likewise do not establish visits or leads. Recent repairs have no demonstrated causal uplift yet.

Cost baseline correction: Growth was cancelled October 1 with expiry October 2; André reported October 3 that both apps worked on the $0/1,000-call tier, called Starter in the record. Do not treat the former A$400-plus Growth charge as current overhead. Remaining quota, exact account tier and production terms were not independently checked.

Current Auto.dev public pricing distinguishes capped Free from grandfathered Starter with metered overages. Its September 16 terms also describe Free allowances as evaluation/development/small-scale rather than production serving end users. This creates an account-specific sustainability question, not a conclusion that André's account is on that Free contract. Confirm actual account terms before assuming a durable free production dependency. Fractal's October 14 renewal remains a separate unresolved owner gate.

## Challenges to the prompt

1. **MCP distribution:** Agree that dependable automatic discovery is not demonstrated. Disagree that this establishes product failure or justifies abandoning every host surface. OpenAI's current rules explicitly make enhanced/proactive distribution selective; Claude's connected-app suggestions depend on the user having connected the relevant app. A channel can remain useful for existing users without being an acquisition engine.
2. **Cost urgency:** Agree on sustainability. Avoid making an urgent quota/renewal decision the product thesis. Cheap infrastructure still has maintenance and founder-time costs.
3. **Impact plus public data:** Plausible cost advantage, not a proven functional replacement. Bounded catalogue tests reported 1,352,716 items, but condition, reliable locality and freshness were not demonstrated. NHTSA cannot supply ownership/title history or current availability. Do not broaden these sample findings into universal feed claims.
4. **Intelligent search:** Useful interface, insufficient differentiation by itself. CarGurus already offers conversational needs, comparison, local listings and persistent conversation URLs. A defensible promise requires a particular outcome and credible evidence.
5. **Distribution first:** Directionally right when it means an identifiable buyer job, credible audience access and a viable commercial handoff. Choosing a popular platform and building for it before checking audience access can recreate the current bottleneck.
6. **Native Reddit:** Better framed than routine promotion, and already explored in project work. Earlier posts show views/engagement, not proven leads. Native utility still needs willing communities and approval. Current Devvit rules require permission in app review for directing users outside Reddit; affiliate continuation is not an assumed native entitlement.
7. **Facebook/Instagram:** Candidate surfaces, not default answers. Car-related interest and reachable buyers at a purchase decision are different. Value, audience access and intent need separate evaluation.
8. **Google:** Specific questions and useful tools are plausible hypotheses; current zero-click evidence is not validation. Google permits useful AI-assisted work but cautions against many pages without added value. An indexable output is not automatically a searchable asset people need.
9. **Acquisition loops:** A result people can share is a feature until there is a reason to share, an audience that receives it, and a reason for recipients to use the product. Many private buying decisions will not create public search demand.
10. **Limited capital/time:** Small reversible learning is appropriate. One engine across many surfaces can still create several support and measurement burdens; cheap data does not remove those.
11. **Sunk cost:** Keep only assets that improve the next learning or customer outcome. Existing functionality does not require its continuation or expansion.
12. **Beyond marketplaces:** Fit, mistake avoidance, comparing alternatives and checking a specific listing are different buyer jobs. Each needs its own evidence, distribution context and payer; do not bundle them into one “better AI car finder” promise.

## Five questions that organise the next discussion

These are strategic questions, not a request for André to research or answer all five now.

1. Which particular buyer, at which decision moment, has a problem a marketplace plus general ChatGPT leaves meaningfully unresolved?
2. What useful outcome can we credibly deliver with the available evidence, without an expensive inventory dependency?
3. Where can those buyers already be reached through a willing intermediary, permitted community or established intent?
4. Who benefits enough to fund the outcome, and can the commercial path reward honest advice even when “do not buy” is the best answer?
5. What smallest reversible observation would distinguish a promising combination of job, access and economics from another technically successful but unused product?

Keep the five layers distinct: product = buyer outcome; data = evidence necessary to deliver it; distribution = actual access; monetisation = who pays and when; defensibility = advantage competitors cannot cheaply reproduce. A strong answer in one layer does not fill the others.

## Missing opportunities and threats — hypotheses only

- A portable decision brief could help the buyer coordinate with a partner, family member or forum adviser. The recipient may have an immediate use for it. This is a possible sharing mechanism, not a demonstrated loop.
- An existing publisher, independent inspector, consumer educator or similar trusted intermediary might distribute useful decision support at the point of need. Whether any will participate or pay is unknown.
- Model/ownership trade-off guidance may retain value longer than an individual stock listing. Live inventory could be a continuation rather than the core product.
- A manual, one-off paid second opinion could reveal willingness to pay before building more software. This is an alternative business-model hypothesis, not authorisation to offer or charge for a service.
- Buying is episodic; personal subscription retention cannot be assumed. General ChatGPT and marketplaces are substitutes. Affiliate-biased coverage can undermine an independent recommendation. A different native platform can introduce another approval dependency. Tool maintenance and keeping recommendations current can outweigh nominally free API savings.

## Only owner inputs requested now

1. What recurring cash ceiling and realistic weekly time ceiling can André sustain for the next six months, and how long can he tolerate no meaningful revenue?
2. Is he open to one-off buyer payment or a partner-funded product alongside Edmunds referrals, or is an affiliate-only business a firm constraint?
3. What has any real, non-test user actually said or done after using CarClever: what decision were they trying to make, what helped, and what remained unresolved? No feedback yet is a valid answer.

Stop here. No product or channel chosen, final strategy approved, catalogue architecture designed, public outreach sent, campaign activated, subscription changed or app code written.

## Principal internal evidence reviewed

- [September marketing/revenue strategy](STRATEGY_GETCARWISE_MARKETING_REVENUE_GROWTH_20260923.md) and September 24 distribution reset addendum.
- [MCP lean holding addendum](ADDENDUM_MCP_DISCOVERY_LEAN_HOLDING_20260923.md).
- [Discovery observations](TEST_CARCLEVER_TOOL_DISCOVERY_INVOCATION_OBSERVATIONS_20260911.md) and clean-account negative invocation baseline.
- [Catalogue C1–C8 tests](RETURN_IMPACT_CATALOG_C1_C8_READ_ONLY_TESTS_20260920.md), [private prototype](RETURN_IMPACT_CATALOG_PRIVATE_PROTOTYPE_20260921.md), and September 30 locality desk audit.
- [Native Reddit feasibility](REVIEW_REDDIT_NATIVE_APP_FEASIBILITY_20261001.md), [buyer-intent research](RESEARCH_REDDIT_BUYER_INTENT_PHASE0_20261001.md), build plan and tracker.
- [October 6 weekly SEO/GEO report](WEEKLY_SEO_GEO_REPORT_20261006.md), diagnosis/action plan, fresh content drafts and implementation logs.
- [October 7 handoff](HANDOFF_CLAUDE_NEW_CHAT_SEO_GEO_MONETIZATION_20261007.md) and the current seven admin files.

## Official external checks

Accessed during this session; account-specific application or performance not inferred:
- OpenAI publication/distribution: https://developers.openai.com/plugins/deploy/app-review
- Claude connected-app suggestions: https://support.claude.com/en/articles/14730684-how-claude-suggests-connected-apps
- CarGurus conversational search announcement, June 9, 2025: https://www.cargurus.com/about/press/ai-search-experience
- Auto.dev pricing: https://www.auto.dev/pricing and terms: https://www.auto.dev/terms
- Reddit Devvit rules: https://developers.reddit.com/docs/devvit_rules
- Google AI-content guidance: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
