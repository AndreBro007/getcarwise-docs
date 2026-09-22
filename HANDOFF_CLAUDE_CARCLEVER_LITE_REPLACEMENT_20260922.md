# Claude Prompt — Separate CarClever Decision-Center Test Page

**Task #72 — pending André’s approval before execution**  
**Engineering/content lane:** Claude  
**Reference strategy:** getcarwise-docs/STRATEGY_CARCLEVER_LITE_FRACTAL_EXIT_REPLACEMENT_20260922.md

## Objective

Investigate and prepare a **separate new test page** for the CarClever Decision Center concept. Keep existing WordPress page 239 and its Fractal-backed CarClever Lite experience completely unchanged.

The goal is to test a content-led journey that helps a car shopper choose the right next step, routes them to existing GetCarWise tools, and then presents relevant Edmunds New, Used or Trade-in actions. This page must follow the evidence-led SEO/GEO and page-funnel approach already used across GetCarWise. Do not create a thin page made only of buttons or tool links.

## Required repository reading

Before work, follow the fresh repository verification procedure and inspect current main state. Read in full:

- carclever-widget: STATE.md, DECISIONS.md, PLAYBOOK.md, REFERENCE.md, TASKS.md, ACCOUNT_MEMORY_TRANSFER.md, WORKFLOW_ARCHITECTURE.md, and current CARCLEVER_3_APPS status.
- getcarwise-docs:
  - STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md
  - STRATEGY_MASTER_SEO_GEO_REVENUE_MATRIX_20260919.md
  - STRATEGY_FOUR_PAGE_EDITORIAL_DECISION_PACKAGE_20260919.md
  - ANALYSIS_FOUR_PAGE_SEO_GEO_FORENSIC_20260919.md
  - RESEARCH_SEO_GEO_DATA_EVIDENCE_RESULTS_20260919.md
  - REVIEW_WEEKLY_SEO_GEO_REPORT_20260919.md
  - REVIEW_WORDPRESS_IMPACT_STATIC_DESTINATION_MAPPING_20260921.md
  - RETURN_WORDPRESS_25K_SUV_CONSOLIDATION_20260919.md
  - RETURN_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_REBUILD_20260921.md
  - current strategy and handoff documents for Task #72.

Read other live-page, SEO/GEO and funnel documents that are relevant to your proposed target page. Use current contents, not the filename date or old page drafts, as the source of truth.

## Phase A — read-only audit

Do not make edits during this phase.

1. Inspect current live GetCarWise page strategy and page structures. Include the recent $25k consolidation, $40k new-sedan rebuild, $30k SUV work, used-PHEV rebuild, three-row SUV benchmark and Tools hub. Identify the patterns that should carry into this test: answer-first content, distinct buyer job, factual source ledger, methodology, useful decision structure, FAQs, contextual funnel, disclosures and measurement.
2. Inspect current U.S. GSC Search and available GEO/query evidence for a candidate user job. Identify existing competing URLs and internal links. Recommend one page intent, title/H1 direction and slug only if evidence shows a distinct gap. Do not assume the working label “Decision Center” is an SEO keyword.
3. Complete the Page Funnel Contract:
   - user job and search/GEO intent;
   - unique user utility and answer;
   - primary and secondary lead family;
   - primary/secondary action and CTA placement;
   - exact target page for each existing tool;
   - existing Impact asset type and link;
   - disclosure and fallback;
   - consent-aware attribution dimensions and events;
   - success measures;
   - experiment isolation from existing treatments.
4. Verify destination links and current labeling. Known validated Impact links are:
   - New: https://edmunds.sjv.io/c/7765200/3949597/52125
   - Used: https://edmunds.sjv.io/c/7765200/3949600/52125
   - Trade-in: https://edmunds.sjv.io/c/7765200/3949601/52125
   Use each unchanged only if still suitable; do not create or edit links, submit forms or leads, or claim GA4 attribution works without evidence.
5. Check GA4/GSC/GEO and the Impact reports for any baseline that exists. Confirm whether the two historical completed leads are attributable. Check the actual Consent/GA4 event path and whether clicks can be separated by page, tool, lead family and placement. Identify a traffic source for a later pilot that does not alter protected pages. Mark unavailable evidence plainly.
6. Recommend one of:
   - **Distinct indexable page candidate:** only if it has a distinct search/GEO job, unique content utility, no material cannibalization and measurable funnel path; or
   - **Private/noindex usability test only:** if demand or attribution is insufficient. State that this cannot test organic discovery or indexation.
7. Check page 239 only as a control/dependency reference. Do not edit or repoint it.

Deliver the audit and draft outline first. If no safe, distinct page concept or verified destinations exist, stop and return the audit without creating a page.

## Phase B — create one WordPress draft only

Proceed only if Phase A supports a separate test page without cannibalization or interference with active work.

Create one new WordPress page with **Draft** status. This is the only WordPress write authorized by this prompt. Do not publish, schedule, index, add to a menu, add to sitemap, or add links from existing pages. Do not edit any existing page, including page 239.

Use WordPress-native content blocks and existing site conventions where practical. Do not add an app, iframe, MCP call, model API, Impact Catalog query, Publisher Tag, new code or new lead form. If the intended user experience cannot be achieved without code or a production analytics change, stop and return the limitation instead of expanding scope.

The draft should be complete enough for André to review: intent-matched title/meta/H1 proposal, answer-first opening, original decision guidance, genuinely useful tool-choice structure, exact verified destinations, concise FAQs, methodology/source notes, adjacent affiliate disclosure, and accessibility-minded labels. Do not invent market statistics or unsupported vehicle/financial/safety claims.

## Content and funnel rules

- Keep GetCarWise recommendations and editorial guidance independent of affiliate compensation.
- Link to existing Find My Car, Deal Score, Price Check and VIN Check destinations only after verifying the current public destination and truthful capability. Do not point visitors to a platform-review app while implying approval or availability that has not been confirmed.
- Present New and Used as separate actions based on the visitor’s stated intent. Do not imply the Edmunds links represent all available U.S. inventory.
- Place Trade-in as a distinct contextual action after replacement intent is established; it must not compete with the primary New action above the fold.
- Use the exact approved Impact links unchanged. Use rel="nofollow sponsored noopener", target="_blank", clear labels and the current affiliate disclosure pattern.
- Any event plan must distinguish page view, tool-path selection, tool outbound click, New/Used/Trade-in outbound clicks and confirmed affiliate actions where reports support them. Do not send VINs, precise budgets, credit data, names, emails or other unnecessary personal data to analytics.
- Do not install Publisher Tag or claim attribution functionality that is unverified.

## Protected assets and exclusions

Do not change or link from:

- Page 239 / CarClever Lite, its embed, prompt or Fractal backend.
- The current Tools hub or Try CarClever pages.
- Page 934, the consolidated $25k SUV page.
- Page 828, the $40k new midsize-sedan page and its active bundled content/funnel measurement.
- The current $30k SUV, used-PHEV, three-row SUV and other active treatment pages.
- Deal Score, Price Check, VIN Check or Find My Car code/routes.
- The old Fractal-hosted @CarClever app, connector submissions, platform status or app links.
- Fractal subscription, Auto.dev Growth/Free plan, credentials, Vercel or DNS.
- The private Impact Catalog prototype.

No internal-link promotion or visitor acquisition campaign is authorized. Do not claim that a draft has tested conversion or SEO performance.

## Return and verification

Re-fetch the new WordPress page through the available authenticated interface and confirm:

- status is Draft, not Published or Scheduled;
- the page has a unique draft URL/page ID and is absent from public navigation/sitemap;
- title/meta/H1 and all planned source/disclosure text are correct;
- every CTA destination is exact and its link attributes are correct;
- no existing page or affiliate asset was changed;
- no lead form was submitted;
- no code, Vercel, DNS, connector, Fractal, Auto.dev, Catalog or analytics configuration changed.

Return:

1. the complete Phase A audit and Page Funnel Contract;
2. the candidate intent, competing-page check and indexability recommendation;
3. page ID, preview link and full draft copy/outline;
4. verified tool and Impact destinations;
5. baseline, attribution and traffic limitations;
6. proposed publish/measurement plan, with SEO/GEO and funnel outcomes separated;
7. rollback/removal instructions for the draft;
8. an exact scope confirmation.

Stop after the draft is re-fetched and verified. André must separately approve publication, indexing, internal-link promotion, analytics changes or any later implementation.