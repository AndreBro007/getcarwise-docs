# Strategy — Separate CarClever Decision-Center Test Page

**Date:** 2026-09-22  
**Task:** #72  
**Status:** **PROPOSED TEST PLAN — André has directed that page 239 remain as-is and a separate page be prepared for testing. Claude prompt is pending André’s approval.**  
**Scope:** Research, design and a reviewable WordPress draft for a separate test page. No public publication, page-239 change, app change, Fractal change or subscription action is authorized.

## Confirmed direction

Leave the existing CarClever Lite page 239, iframe/embed URL, Fractal endpoint, prompt, and current visitor journey unchanged. Test the proposed CarClever Decision Center concept on a separate new WordPress page.

This isolates the concept from the live Lite experience and preserves a rollback-free control. The experiment should connect visitors to existing GetCarWise tools and to distinct, verified New, Used and Trade-in actions. It should not rebuild those tools or add a new chatbot.

The first deliverable should be a WordPress draft, not a published/indexable page. Claude must first check current Search/GEO evidence, page overlap, approved CTA destinations, traffic acquisition and measurement. The draft can be reviewed visually and editorially. André must separately approve publication, indexing and traffic promotion.

## Governing SEO/GEO and page strategy

The test page must follow the same evidence-led approach used on the recent $25k, $30k, PHEV, $40k and three-row SUV work:

- establish one distinct user job and search/AI question before selecting a title or URL;
- deliver a clear answer first, then useful decision support;
- use original, structured content rather than a thin list of tool buttons;
- explain sources, methodology, data limits, and update date;
- use direct, descriptive headings, a comparison or decision structure where it adds real value, concise FAQs and source links;
- make recommendations conditional on stated user priorities rather than unsupported universal rankings;
- build a Page Funnel Contract: primary/secondary lead family, action timing, link mechanism, fallback, attribution and success metric;
- avoid keyword cannibalization, duplicate content, unsupported facts, fabricated market statistics, or high-volume programmatic variants;
- keep Search, GEO and commercial outcomes distinct in reporting.

An indexable page is justified only if the audit finds a distinct search/GEO intent and the draft offers meaningful original utility. If it is mainly a navigation/router page, keep it as a private or noindex experiment and state plainly that it cannot measure organic discovery while noindex. Do not change the Tools hub or an existing treated page just to drive test traffic.

## Why page 239 stays unchanged

Page 239 is the only website-embedded app identified as directly dependent on Fractal. Its prompt assumes Fractal tools for used-car search, risk, affordability, comparison, vehicle details and dealer URLs. Current production Find My Car exposes only find_matching_vehicle and resolve_dealer_url; a direct MCP URL replacement is not equivalent and would break functions.

The website already has Deal Score, Price Check and VIN Check on separate pages. A separate page lets us evaluate navigation, decision content and funnel clarity without changing Lite or duplicating tool logic. It also allows a separate launch date and measurement record if André later approves publication.

This test does not itself remove the site's Fractal dependency and does not make Fractal cancellable.

## Page concept to investigate

Working concept only: a useful “what should I do next before I buy or replace a car?” decision guide that helps a visitor select among vehicle discovery, vehicle evaluation, price review, VIN review and selling/trading a current vehicle.

Do not assume that phrase is the final title, keyword or URL. Claude must inspect current GSC/Search Console and GEO evidence, live pages and internal links, then identify the most supportable distinct user job. If no defensible gap exists, recommend the best non-indexed usability-test page rather than creating an SEO doorway page.

## Page Funnel Contract

Before drafting, record:

| Contract field | Decision needed |
|---|---|
| User job and trigger | The specific car-buying or replacement decision the page helps with |
| Search/GEO intent | Query families and AI questions supported by current evidence |
| Unique utility | The concrete answer, sequence, checklist or comparison offered on this page |
| Primary lead family | New, Used, Trade-in or none, based on intent evidence |
| Secondary lead family | Only where it naturally follows the visitor's decision |
| Tool continuation | Exact existing site destination for Find My Car, Deal Score, Price Check and VIN Check, when verified |
| Impact mechanism | Existing approved static link; no new or reconstructed tracking URL |
| CTA timing | New/Used after useful decision content; Trade-in as a contextual bridge, not a competing hero CTA |
| Fallback and trust | What remains useful when a tool/link is unavailable; distinguish independent guidance from Edmunds |
| Attribution | Page, module, intent, placement and variant identifiers supported by current systems |
| Success metric | Tool starts/completions, outbound clicks, valid leads and revenue per qualified visit where observable |
| Experiment isolation | Separate URL/date; no edits to page 239, Tools hub, $25k/$40k, or other current treatments |

## Match the established page pattern

The recent pages are not merely a set of buttons. The new page should use the appropriate parts of their shared architecture:

1. Clear, intent-matched title and one H1.
2. Concise answer-first opening.
3. Original explanation of the decision and the order in which the tools help.
4. A structured “which route fits?” decision table or short steps.
5. Existing tool cards that state the user question answered and limitations.
6. New and Used CTAs after the relevant shopping decision; do not blend the two.
7. Trade-in as a separate lower-page action after replacement intent is established.
8. Short methodology/source section and visible affiliate disclosure adjacent to affiliate actions.
9. Useful FAQs drawn from real intent, not filler.
10. Accurate title/meta, self-canonical and schema proposal only if publication/indexing is approved.

Use the relevant current page as a pattern reference, not as copy to duplicate. Page 828's integrated funnel is an example: New primary, Used secondary, Trade-in lower and contextual, tool continuation retained, exact Impact URLs, rel="nofollow sponsored noopener", target="_blank", disclosure and no guarantee of availability/value. The $25k page likewise preserves existing CTA and Lite block. Do not alter any of those pages.

## Known approved commercial links

These exact Impact-managed assets were validated in the site destination audit and used on the $40k page. If used in the draft, use them unchanged and confirm current suitability with the audit; do not recreate or hand-edit them.

| Family | Approved link | Draft placement |
|---|---|---|
| New | https://edmunds.sjv.io/c/7765200/3949597/52125 | Primary only where the page establishes New intent |
| Used | https://edmunds.sjv.io/c/7765200/3949600/52125 | Separate alternative where Used is relevant |
| Trade-in | https://edmunds.sjv.io/c/7765200/3949601/52125 | Contextual lower-page sell/replace bridge |

Use appropriate sponsored/no-follow attributes, clear labels and the existing affiliate disclosure. Do not submit forms or leads. Existing Impact CTA click reporting is not fully confirmed: the $40k completion report says a real consent-granted visitor session is still required to verify GA4 CTA attribution.

## Test and measurement limits

Current records describe two completed leads whose sources are unattributed. The new page has no established traffic baseline. Do not claim a revenue forecast or assert that the page improves conversion before it has evidence.

Before proposing a live pilot, Claude should report:

- page-239 and candidate-page 28/90-day GSC Search and available GEO measures;
- page/session sources and available GA4 engagement/outbound data;
- existing tool-link and CTA performance where available;
- whether the two historic leads can be attributed;
- current Consent/GA4 behavior and whether page-level CTA events actually register;
- a plausible traffic source for the separate page without changing the Tools hub or active treatment pages;
- what a noindex draft can test (content, clarity, usability) and cannot test (organic reach, indexation, real-market conversion).

If analytics/attribution is unavailable, identify the smallest specific check and label it unresolved. Do not add new trackers, Publisher Tag or personal-data collection as a shortcut.

## Active treatment protections

Do not change, add links to, alter canonical/schema, edit CTAs, redirect, update text on, or otherwise disturb:

- page 934: retained $25k compact-SUV page, recently consolidated and under measurement;
- page 828: new $40k midsize-sedan rebuild with integrated New/Used/Trade-in funnel, whose content and CTA effects are bundled in the current treatment;
- the $30k SUV, used PHEV and three-row benchmark pages under their separate measurement plans;
- the Tools hub, which has demonstrated GEO visibility and is treated as a protected router.

Do not drive traffic through these pages without a separately approved experimental design. Record any proposed test-page publication date as its own intervention.

## Options assessment, now applied as a test

- **Reduced two-tool Lite:** not suitable for this test; page 239 remains unchanged.
- **Broader first-party assistant:** not justified; duplicates current tools and adds maintenance/API use.
- **Conversion-focused page:** test as a separate content-led draft with useful unique guidance and existing-tool paths.
- **Hybrid:** if the separate page proves useful, conversational search can be considered later as its own measured follow-up.

The Impact Catalog remains out of scope. Its current data is condition-neutral and lacks supported ZIP/radius filtering; its prototype remains private and unapproved for public use.

## Claude task proposed for André’s approval

1. Perform a fresh read-only audit of current page strategy, GSC/GA4/GEO evidence, candidate query gap, destinations, event/consent behavior, and treatment-page overlap.
2. Return the Page Funnel Contract and recommend whether the test page should be a WordPress draft for a later indexable pilot or remain noindex/private.
3. If the audit finds a safe, non-cannibalizing page concept, create a **new WordPress page in Draft status only** with full evidence-led copy, title/meta proposal, structured decision utility, existing tool destinations and approved CTA links. Do not publish, schedule, add it to menus/sitemaps, or modify internal links from current pages.
4. If there is no defensible page intent, no verified destinations, or a conflict with current measurement, do not create the draft; return the evidence and a revised proposal.
5. Return the page ID, preview route, exact links, page outline, source ledger, SEO/GEO and funnel rationale, risks, measurement plan, and confirmation of untouched assets.
6. Wait for André’s separate approval before publication, indexing, internal-link promotion, analytics changes, widget/code work, or Fractal/Auto.dev decisions.

## Independent decisions remain separate

1. Page 239 / Lite replacement: unchanged; no replacement is selected by this experiment.
2. Old Fractal-hosted @CarClever ChatGPT app retirement: separate distribution/link decision; unchanged.
3. Fractal subscription cancellation: separate cost/account decision; unchanged.
4. Auto.dev Growth-versus-Free: separate shared-use/quota decision; unchanged.
5. Public Impact Catalog deployment: separate pilot authorization; unchanged.

## Explicitly unchanged

- Page 239 and its Fractal-dependent chat remain live as-is.
- The old Fractal @CarClever app and all platform submissions remain unchanged.
- Deal Score, Price Check, VIN Check, Find My Car and their code/routes remain unchanged.
- No existing WordPress page, menu, internal link, CTA, canonical, schema, sitemap or affiliate link is changed.
- No Auto.dev or Fractal plan/account change is made.
- The Impact Catalog remains private, unmerged and unpublished.
- All active SEO/GEO treatment pages remain untouched.

## Approval requested

André’s approval of the Claude prompt authorizes only the read-only audit and, if its stated conditions pass, creation of one new WordPress Draft. It does not authorize publishing, indexing, promoting traffic, changing existing pages, code/deployment, or any platform/subscription change.