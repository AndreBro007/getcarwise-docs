# Review — Midsize Sedan Under $40K Intent Audit

**Reviewed:** 2026-09-20  
**Audit return:** `RETURN_WORDPRESS_MIDSIZE_SEDAN_40K_INTENT_AUDIT_20260920.md`  
**Decision:** **Accept Option A with mandatory two-URL consolidation preflight and a built-in monetization funnel.**  
**Next task:** #70 — implement the new-car rebuild/consolidation only after the preflight gates in the handoff close.

## Executive decision

Rebuild the retained page as a broad, current, evidence-led guide to **new midsize sedans under $40,000**. Do not preserve the existing implicit-used, three-model job.

The audit supports this decision because:

- The visible query set is category/value-led, not model-specific: the dominant three-month query is “best sedans under $40k” (27 of 65 impressions).
- No observed query names Camry, Accord or Altima.
- No observed query expresses used-car intent.
- Current winners for the price-cap query are broad current/new-car roundups.
- The present body contains unsupported used-market assumptions and current factual errors.
- The URL and $40,000 cap already fit the recommended job, so the retained URL can preserve accumulated signals.

This is not approval to copy competitor model lists. The rebuilt page must define and source its own inclusion method.

## Modification 1 — treat this as a two-URL cluster

The audit correctly flagged the adjacent page:

`https://getcarwise.app/tools/best-midsize-sedan-under-30k-comparison/`

A public inspection confirms that it uses the same Accord/Camry/Altima comparison and substantially overlaps the same “affordable midsize sedan” decision. Leaving both pages live unchanged would repeat the duplicate-intent pattern just resolved in the $25k SUV cluster.

The implementation must therefore capture fresh Search/GEO baselines and rollback copies for both URLs before editing. Default architecture:

- **Retain:** `/tools/best-midsize-sedan-under-40000/`
- **Rebuild:** broad new midsize sedans under $40,000
- **Merge and 301 the $30k URL:** only if fresh evidence confirms it has no defensible distinct query job or stronger independent signal
- **Do not redirect automatically:** if the $30k URL has a material, distinct search job, stop and return the evidence for a new architecture decision

The reason to retain the $40k URL is evidence-led, not arbitrary: it already receives the dominant under-$40k query family and its cap can include the complete current midsize field. The $30k page is narrower and presently duplicates the same three-car structure.

## Modification 2 — monetization is part of the page contract

The old “Browse Used Cars on Edmunds” CTA cannot remain the page’s sole or primary action after a new-car rebuild. It would contradict the page job.

Required funnel hierarchy:

1. **Primary — New:** move a reader from the ranked guide into shopping current new midsize sedans.
2. **Secondary — Used:** preserve a clearly labelled alternative for readers who decide the new-car budget/value trade-off is not right.
3. **Contextual — Trade-in:** offer a trade-in/value bridge only after replacement intent is established, not as a competing hero CTA.
4. **CarClever:** remain a useful evaluation path, with its role and event tracking preserved.

The affiliate-network migration remains separate from the editorial architecture. This task must not invent an Impact URL or silently run the sitewide CJ→Impact migration. However, it also must not publish a mismatched used-only primary CTA. Before publication, Claude must validate an approved tracked New destination and the intended Used and Trade-in destinations. If that cannot be done, stop at the CTA decision gate and return the exact blocker.

The public Catalog/inventory module is not authorized here. Task #69 found it conditionally feasible but blocked on rights, authenticated testing and geographic limitations. Use static, approved, properly disclosed destinations only.

## Modification 3 — model scope

The page should cover current US-market midsize sedans that genuinely qualify under the cap, using official manufacturer evidence immediately before drafting. The likely core field is:

- Toyota Camry
- Honda Accord
- Hyundai Sonata
- Kia K5
- Nissan Altima

This is a **verification list, not a pre-approved factual claim**. Claude must verify current model-year availability, segment fit and MSRP under $40,000 immediately before publication.

Do not add compact cars merely because competing pages rank them for the broader word “sedans.” Specifically, Honda Civic Si and Toyota Prius should not be treated as midsize sedans without an explicit classification rationale. Do not include discontinued/non-current models such as Avalon or Legacy as current new-car recommendations.

## Content and GEO direction

The rebuild should provide:

- an answer-first summary and transparent “how we chose” method;
- a current price/trim qualification table;
- one evidence-led section per included model;
- explicit best-for labels and trade-offs;
- “which one should you buy?” decision logic;
- concise, answerable FAQs based on observed query language;
- inline primary sources and a dated source/methodology section;
- accurate title, meta, H1, canonical, robots, read-time and schema;
- internal links from Tools and Data & Guides;
- no unsupported reliability, resale, owner-satisfaction, accident-history or used-market generalizations.

## Measurement decision

Treat the publication as one documented **cluster + content + funnel treatment**, because the search architecture and conversion path are being fixed together. Preserve component-level analytics so we can still distinguish:

- Search/GEO discovery
- New CTA clicks
- Used alternative clicks
- Trade-in bridge clicks
- CarClever engagement
- Affiliate outbound clicks where observable

Measure at T+14, T+28 and T+56 from the exact implementation timestamp. Record both old URL baselines even if the $30k URL is redirected.

## Review verdict

Claude’s audit is accepted as complete. Option A is approved with the safeguards above. The implementation handoff is `HANDOFF_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_CONSOLIDATION_20260920.md`.
