# Task #78 — G1 Google Search decision card (Sep 28)

> **Owner timing decision, 2 October closeout:** Lite cutover is deferred pending Fractal's old-CarClever continuation decision, to be resolved before 14 October (Brisbane) and completed before service loss if Fractal stops. Immediate migration is not authorized. G1 remains on hold; whichever Lite path is retained must be functional and accurately described before any future launch. Affiliate creative correction and final campaign/spend approval remain separate. Conditional ten-page inventory: [creative/Lite review](REVIEW_IMPACT_CREATIVE_LITE_CUTOVER_AND_G1_GATES_20261002.md).

> **2 October review — launch remains on hold.** Fresh WordPress REST confirms page 934 still uses custom "Browse Used Cars on Edmunds" text, no supplied pixel in its stored content, no new Find My Car directory anchor, and the legacy Fractal-backed Lite iframe. This page-specific evidence supersedes general rollout-complete assumptions. Recommend current supplied Used Asset Code/exact text and a staged Lite V2 cutover after minimal actual-Free verification; these are pending André confirmation, not completed edits. Missing pixel alone is not proof of broken click attribution or a universal contract requirement. Keep page 934 as G1 destination; final settled-page check, persisted Ads settings/revised future dates and separate preview/spend approval remain required. Full evidence/scope: [2 October creative/Lite review](REVIEW_IMPACT_CREATIVE_LITE_CUTOVER_AND_G1_GATES_20261002.md).

**Status:** Reviewable marketing recommendation. No campaign, ad or spend. André supplied Impact Used asset 3949600 and a screenshot showing getcarwise.app Connected under Promotional Channels. Sep 28 GSC readout recommends no organic page rewrite.

## Recommend one controlled test

Run one seven-day, **A$150 total** US Search pilot to the existing used-SUV-under-$25k guide after the Sep 30 operating/cost decision and separate campaign/spend approval. Sell a clear buyer job: **compare used SUV choices and know what to check before contacting a dealer**. The page offers a GetCarWise shortlist, optional CarClever next step and optional Edmunds inventory handoff. This tests paid buyer demand and engagement; it cannot prove seven-day lead profitability. Keep direct-app awareness and founder-led Reddit Ads as separate later routes rather than splitting A$150 three ways.

| Setting | Proposed final review |
|---|---|
| Audience | US shoppers evaluating used SUVs around US$25k; United States Presence, English. |
| Keywords | One exact-match ad group: [best used suv under 25000], [used suv under 25000]. Each has 100–1K US monthly searches, high competition in the account Planner; inspect actual terms daily. |
| URL | https://getcarwise.app/tools/best-compact-suv-under-25000/?utm_source=google&utm_medium=cpc&utm_campaign=used_suv_decision_g1 |
| Network | Search only; Search Partners and Display expansion off. |
| Budget | A$150 **campaign total** over seven days, fixed end date in Brisbane account time. No promotional credit attached. Do not substitute an average daily budget for this hard ceiling. |
| Bidding | Maximize Clicks with a reviewable CPC ceiling if available. If the final screen predicts negligible delivery or needs poor-intent broadening, return for a decision. |
| Exclusions | Implement the 13 distinct Edmunds phrases as both exact and phrase negatives (26 entries) transcribed in the Search draft; add jobs, rental, parts and wholesale. Review generated assets. No protected brands or manufacturers in ad copy. |

**Ad candidates** (headlines ≤30; descriptions ≤90 characters; final Google preview still required):

- Headlines: “Used SUVs Under $25,000”; “Compare Used SUV Choices”; “Used SUV Buying Guide”; “Know What to Check First”; “GetCarWise SUV Guide”; “Start Your SUV Shortlist”.
- Descriptions: “Compare used SUVs under $25k. See practical trade-offs and what to check before you buy.” / “Start a shortlist with buyer checks, then explore used listings when you're ready.”

This copy promises the actual guide, without claiming verified history, guaranteed savings, automatic app invocation or Edmunds endorsement.


## Sep 28 landing-page reassessment after Claude's SEO/GEO and site fixes

**Keep page 934 for G1.** The two approved ad queries are specifically about *used SUVs under US$25,000*. Page 934 answers that decision directly with six-model trade-offs, a buying checklist, an embedded CarClever Lite step and an Edmunds Used inventory CTA. Page 827 has stronger organic impressions but targets a different US$30,000 *new-versus-used* decision, so sending the $25k used queries there would weaken ad-to-page fit. Decision Center page 1160 is a broad new/used/trade-in route with no $25k SUV answer; it is a better later brand/app test than this search-intent pilot. Organic impressions/SEO scores are not the primary landing-page selection criterion for paid Search.

Claude's Sep 27 weekly scan showed low site authority and the known zero-click $30k SUV cluster, not a new page-934 defect. Tasks #82–84 corrected Semrush monitoring and submitted an 87-domain disavow file, which cannot be expected to improve paid performance by Sep 30. Task #85 *did* change page 934: a page-local script had disabled pointer events on the embedded Lite iframe; Claude removed it and verified a real prompt chip now runs a search on 934. Task #86 made the distinct `carclever-lite-v2` standalone route anonymously accessible in Production; do not conflate that route with the existing embed or assume a page-934 cutover.

The new approved Find My Car directory link is being rolled out site-wide. Its presence on 934 is **not yet confirmed** by the completion records reviewed here. The public page text retrieved Sep 28 still showed the embedded Lite and Edmunds Used handoff, but no visible new ChatGPT directory CTA; public extraction may miss iframe or script-driven UI. Before campaign activation, have the rollout owner confirm the final page-934 destination, a conspicuous new-app CTA if intended, the working Lite prompt and the Used CTA. Keep the paid URL, keywords and ad promise fixed while those edits settle. Do not send a paid visitor to a changing or broken journey. A final post-rollout check is a launch gate, not a reason to replace this better-matched page now.

**Marketing opportunity after G1:** if visitors read but do not proceed, test a nearer-to-top, buyer-specific action (“Find used SUVs near you with CarClever”) and compare app versus inventory handoffs. This is a separate page-change/test decision, not part of the current seven-day baseline or an authorized production edit.

## Economics and decision rule

Edmunds pays **US$10 per approved Used lead**, not per click. At an illustrative 5% approved-lead rate per paid click, media break-even CPC is US$0.50 before overhead; that rate is unobserved. The account Planner's top-of-page bid ranges were A$0.30–3.83 and A$0.86–4.48, not actual CPC. At hypothetical A$2 or A$4 CPC, A$150 buys 75 or 37 clicks if demand delivers. The earlier narrow-keyword forecast showed zero clicks, so volume is uncertain. Treat A$150 as a learning-loss ceiling, not a revenue forecast.

**Daily read:** Ads spend, terms and CPC; GA4 page-934 google / cpc landing and engaged sessions; optional app and partner handoffs only if already measured; Impact Used actions separately as aggregate. Do not assign aggregate Impact actions to the ad or calculate campaign ROAS. A useful first-week signal is relevant query delivery and engaged buyer visits at a repeatable cost.

**Stop:** pause for mismatched queries, destination/GA4 failure, disallowed terms, misleading ad-to-page match or spend approaching A$150. If negligible delivery by day 3, diagnose the auction and bring a revised route decision rather than silently broadening. If visits arrive without meaningful engagement, do not fund a second week. If engagement is promising, choose only one next experiment with a new cap: improve the handoff, test CarClever app awareness, or expand the intent cluster.

## Ordered execution

1. Completed: account and GA4 link, UTM destination, Planner research, Sep 28 GSC no-edit decision, Edmunds terms and owner-supplied Impact asset/profile evidence.
2. Before launch: Sep 30 operating/cash choice; final Google budget/CPC/geo/network/negative-list/creative preview and post-rollout page-934 CTA/Lite/Used-link check. Document exact final settings for André.
3. André separately approves campaign creation/activation and A$150 spend. Then implement, verify live settings and monitor daily. No account campaign or spend is authorized by this document.

**Recommendation:** prepare the final Ads settings now; decide at Sep 30 whether to release one bounded G1 test, revise it or hold media while reducing operating costs.


## Ready-to-enter settings sheet (prepared Sep 28; not entered in Ads)

| Google Ads field | Proposed entry or launch check |
|---|---|
| Account | Existing GetCarWise CID 310-034-4276; AUD, Brisbane time. |
| Campaign | New Search campaign, working name `G1_US_UsedSUV_25k`; Google Search only. Turn off Search Partners and Display expansion. No Performance Max or app-install format. |
| Location/language | United States; location option **Presence** (people in or regularly in the US), not Presence or Interest. English. |
| Ad group | One: `Used SUVs under 25k`. Exact keywords only: `[best used suv under 25000]` and `[used suv under 25000]`. No broad-match or automatic keyword expansion. |
| Destination | The existing page-934 UTM URL in the table above. Display path candidates: `used-suv` / `under-25k`. |
| Budget/dates | **Campaign total budget A$150**, start only after approval, end seven calendar days later in account time. Google says new Search campaigns support total budgets for Maximize Clicks and that billed spend cannot exceed the total, with no daily cap. Verify this exact budget type in the account; do not substitute average daily budget. |
| Bidding | Maximize Clicks, with a maximum CPC bid limit reviewed in the final account preview. No unverified numeric CPC promise: the account's earlier Planner top-of-page ranges were broad and a narrow exact-match forecast returned zero clicks. A suggested limit that prevents delivery must come back for a decision, not be silently relaxed. |
| Goals | Do not optimize to pageviews as if they were approved Edmunds leads. Verify account defaults and any Google-generated assets before activation. |
| Timing | Sep 30 operating/cash gate, completed page-link rollout and final page check, then a separate approval of final Ads preview and spend. No promotional credit currently appears in Billing → Promotions. |

**Responsive Search ad draft** — independent assets may appear in varied combinations; the copy below remains relevant in any order. Headline lengths are 20–28 of Google's 30-character maximum, descriptions 84–88 of 90. Review the final Google preview, including generated text/assets, before approval. Google supports up to 15 headlines and four descriptions; this small test starts with eight and three, leaving room to improve after the first read.

| Headlines | Descriptions |
|---|---|
| Used SUVs Under $25,000; Compare Used SUV Choices; Which Used SUV Fits You?; Find Your Used SUV Shortlist; Know What to Check First; Compare 6 Popular Used SUVs; Start With a Clear Shortlist; GetCarWise SUV Guide | Not sure where to start? Compare six used SUVs under $25k and narrow your shortlist. / See space, AWD and value trade-offs. Know what to check on a real listing before buying. / Choose the SUV that fits your priorities, then explore used listings when you're ready. |

**Campaign-level negatives to enter and verify individually:**

| Match type | Terms |
|---|---|
| Exact | `[car value]`, `[used car values]`, `[trade in value]`, `[what is my car worth]`, `[trade in]`, `[trade in value car]`, `[how much is my car worth]`, `[trade in value of my car]`, `[car value estimator]`, `[appraisal]`, `[used car appraisal]`, `[used car appraisal value]`, `[appraise my car]` |
| Phrase | `"car value"`, `"used car values"`, `"trade in value"`, `"what is my car worth"`, `"trade in"`, `"trade in value car"`, `"how much is my car worth"`, `"trade in value of my car"`, `"car value estimator"`, `"appraisal"`, `"used car appraisal"`, `"used car appraisal value"`, `"appraise my car"` |
| Additional exclusions | Protected Edmunds/Edmonds brand searches and variants; jobs, rental, parts, wholesale. Check the final protected-term list against the current contract and inspect actual search terms daily; negative close-variant coverage is not assumed. |

**First seven days:** inspect spend, CPC, impressions and actual search terms daily. Read the saved GA4 page-934 landing exploration for `google / cpc` sessions and engagement. Read Impact Used actions separately after its reporting delay, without claiming campaign attribution. At day 3, if query quality or delivery is poor, pause and decide whether to revise or end the pilot. At day 7, judge whether the buyer visits were engaged enough to justify a separately capped follow-on. The A$150 is a learning-loss ceiling, not a projected positive return.

Platform documentation checked Sep 28: [campaign total budgets](https://support.google.com/google-ads/answer/10486938), [advanced location options](https://support.google.com/google-ads/answer/1722038), [Maximize Clicks](https://support.google.com/google-ads/answer/6268626), [responsive Search ads](https://support.google.com/google-ads/answer/7684791), [Search campaign setup](https://support.google.com/google-ads/answer/9510373). This sheet is preparation only; it does not authorize campaign creation or spending.
