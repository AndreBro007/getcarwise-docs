# Handoff — Task #70 Revised: $40K Midsize-Sedan New-Car Rebuild With Integrated Impact Funnel

**Date:** 2026-09-21  
**Task:** #70 revised implementation  
**Owner:** Claude — authenticated WordPress/GSC implementation lane  
**Target:** `https://getcarwise.app/tools/best-midsize-sedan-under-40000/` (WordPress page 828)

## Decision

Rebuild only the $40k page as a broad, current, evidence-led guide to **new midsize sedans under $40,000**.

Do not edit, merge, canonicalize or redirect:

`https://getcarwise.app/tools/best-midsize-sedan-under-30k-comparison/`

That URL has a distinct Camry/Accord/Altima comparison job and remains separately live.

## Mandatory reading

Perform the repository startup procedure, then read in full:

- `RETURN_WORDPRESS_MIDSIZE_SEDAN_40K_INTENT_AUDIT_20260920.md`
- `RETURN_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_CONSOLIDATION_20260920.md`
- `REVIEW_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_CONSOLIDATION_DECISION_GATE_20260921.md`
- `RETURN_WORDPRESS_IMPACT_STATIC_DESTINATION_MAPPING_20260921.md`
- `REVIEW_WORDPRESS_IMPACT_STATIC_DESTINATION_MAPPING_20260921.md`
- `STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md`
- `STRATEGY_MASTER_SEO_GEO_REVENUE_MATRIX_20260919.md`
- current admin instructions and relevant changed files

## Authorized scope

- page 828 content, title/meta/H1 and existing Article-compatible schema bindings;
- page 828’s integrated New/Used/Trade-in affiliate funnel;
- preservation/repositioning of the existing CarClever Lite block;
- Tools hub and Data & Guides internal links needed to distinguish the two sedan pages;
- GSC inspection/indexing for page 828;
- implementation return document.

## Not authorized

- any edit to page 772 or its URL;
- any redirect or canonical change involving the $30k page;
- any other WordPress CJ→Impact migration;
- Publisher Tag;
- Impact Product Catalog or C1–C8;
- app, MCP, repository application code, Vercel or domain changes;
- creation or manual alteration of Impact links;
- lead submission.

## Mandatory sequence

### 1. Capture a new immediate T0

The prior Task #70 T0 was decision evidence and is not the implementation baseline.

Immediately before editing page 828, capture:

- GSC Search, US: latest 28 days, previous 28 days and latest 3 months;
- clicks, impressions, CTR and average position;
- complete visible query list;
- device split where available;
- Google Generative AI impressions;
- URL Inspection/index state;
- exact timestamp.

Do not use page 772 as a redirect candidate or edit it. Its prior evidence may be retained as a context/control reference.

### 2. Create rollback evidence

Before editing page 828, save:

- exact editable WordPress content;
- rendered HTML/screenshot;
- title, meta, H1;
- canonical, robots and schema;
- current CJ CTA HTML including label, URL, rel and target;
- CarClever Lite block;
- page modified timestamp and sitemap lastmod.

Record the rollback location.

### 3. Verify the current model field

Use current official US manufacturer sources immediately before drafting.

Expected candidates to verify:

- Toyota Camry;
- Honda Accord;
- Hyundai Sonata;
- Kia K5;
- Nissan Altima.

For each included model verify:

- current US model year is on sale;
- it is defensibly classified as a midsize sedan;
- at least one meaningful configuration has MSRP below $40,000;
- which relevant trims cross or remain under the cap;
- whether destination is included or excluded;
- powertrain, drivetrain/AWD and warranty facts used on the page.

Do not pad the list with compact or discontinued models. Specifically, do not present Civic Si, Prius, Avalon, Legacy or Malibu as current qualifying midsize-sedan recommendations without compelling current official evidence and a documented classification rationale.

If one expected candidate is no longer current or cannot be sourced, exclude it and explain why rather than forcing five models.

### 4. Apply a transparent selection method

The page job is:

> Help a US shopper choose among the strongest current new midsize sedans that can genuinely be configured below $40,000, explain the trade-offs, and provide clear New, Used and Trade-in next actions.

Define:

- US market;
- source date;
- MSRP treatment, including destination/options caveat;
- inclusion threshold;
- editorial comparison dimensions;
- how “best for” labels are assigned.

Do not claim that every trim/configuration is under $40,000 unless official evidence proves it.

### 5. Rebuild the page

Required structure:

1. Answer-first summary
2. Dated “how we chose” methodology
3. Scannable comparison table
4. One complete section per verified model
5. Clear best-for labels plus meaningful drawbacks
6. “Which should you buy?” decision guide
7. Integrated New/Used funnel
8. Contextual Trade-in bridge
9. CarClever continuation
10. Concise FAQs based on observed query language
11. Sources/data notes

Content rules:

- remove the unsupported 2019–2023 used-market, mileage, ownership, accident-history and service-history framing;
- correct Camry hybrid-only and Altima optional-AWD facts;
- no unsupported reliability, resale, maintenance, owner-satisfaction or “segment leader” claims;
- label subjective judgments as editorial;
- use inline official citations and a dated source section;
- keep copy useful and natural rather than inflating word count;
- make the read-time badge match the final content.

### 6. Implement the exact funnel

Use these Impact-managed URLs unchanged:

| Role | Exact CTA label | Exact URL |
|---|---|---|
| Primary New | **Shop New Midsize Sedans on Edmunds** | `https://edmunds.sjv.io/c/7765200/3949597/52125` |
| Secondary Used | **Browse Used Midsize Sedans on Edmunds** | `https://edmunds.sjv.io/c/7765200/3949600/52125` |
| Contextual Trade-in | **See What Your Current Car May Be Worth** | `https://edmunds.sjv.io/c/7765200/3949601/52125` |

Placement:

- Do not create a large affiliate CTA above the answer-first content.
- Place the primary New and secondary Used actions after the comparison/decision content, with New visually primary.
- Place Trade-in in a separate, lower contextual block introduced with replacement intent, such as “Already have a car to sell or trade?”
- Preserve CarClever as the evaluation/tool continuation and position it coherently after the editorial decision path.
- Do not imply guaranteed availability, price, valuation or lead acceptance.

All three affiliate links must use:

- `rel="nofollow sponsored noopener"`;
- `target="_blank"`;
- the exact Impact URL unchanged.

Remove page 828’s legacy CJ Used CTA only after the replacement funnel is fully inserted and verified.

Keep a visible affiliate disclosure adjacent to or immediately following the funnel:

> Some links on this page are affiliate links. If you use one, GetCarWise may receive compensation at no additional cost to you. Our recommendations remain independent.

Do not add these three links to other pages in this task.

### 7. Analytics/attribution check

Without adding application code:

- determine whether existing GA4 enhanced measurement records outbound link clicks with page location and link URL;
- verify whether the three CTA classes can be distinguished through their unique link URLs;
- record the implementation timestamp separately from earlier content treatments;
- verify Impact registers the controlled clicks if reporting is visible.

At most one post-publication validation click per CTA is permitted. Do not submit a lead.

If existing analytics cannot provide page-level CTA reporting without global code/GTM changes, document the limitation; do not broaden scope.

### 8. SEO/GEO and internal architecture

Implement and verify:

- a broad current-new-car title/meta/H1 aligned to “best new midsize sedans under $40,000”;
- self-canonical page 828;
- index/follow;
- one H1 and logical heading structure;
- accurate Article graph/schema bindings matching visible content;
- no unsupported FAQ schema addition;
- Tools hub link to page 828 with a broad $40k/new-car label;
- Data & Guides retains separate, distinguishable links for:
  - the broad $40k new-car guide;
  - the $30k Camry/Accord/Altima comparison;
- no internal-link change that implies page 772 was merged or superseded;
- mobile and desktop rendering;
- no broken source or affiliate link.

Do not force a year into the permanent URL. A current year may appear in visible metadata only if it can be maintained.

### 9. Publish and verify

After publication:

- re-fetch page 828 through WordPress REST and the public URL;
- compare intended vs saved content;
- verify title/meta/H1/canonical/robots/schema;
- verify all three exact Impact URLs, labels, rel and target;
- verify the old CJ URL is absent from page 828;
- verify CarClever still loads;
- verify Tools/Data & Guides links;
- verify sitemap lastmod;
- inspect/request indexing in GSC;
- capture exact implementation timestamp.

No redirect testing is required because no redirect is authorized.

### 10. Return document

Create:

`RETURN_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_REBUILD_20260921.md`

Include:

- exact T0 and implementation timestamps;
- rollback locations;
- final verified model set and exclusion decisions;
- source ledger;
- before/after title/meta/H1/canonical/robots/schema/read time;
- factual-claim corrections;
- complete final heading outline;
- exact New/Used/Trade-in CTA labels, URLs and placements;
- CJ removal proof for page 828 only;
- disclosure/rel/target proof;
- GA4/Impact verification or exact limitations;
- CarClever verification;
- Tools/Data & Guides changes;
- sitemap/GSC result;
- mobile/desktop verification;
- confirmation that page 772 was untouched;
- confirmation that no other WordPress affiliate link, Publisher Tag, Catalog, app, Vercel or code change occurred;
- unresolved issues.

Push, re-fetch and verify the return. Update only Claude’s checkpoint row.

## Measurement

This is one bundled page treatment: editorial rebuild + SEO/GEO architecture + funnel integration.

- T+14: directional
- T+28: primary
- T+56: confirmation

Report separately:

- Search clicks/impressions/CTR/position;
- GEO impressions;
- New CTA clicks;
- Used CTA clicks;
- Trade-in clicks;
- CarClever engagement where available;
- affiliate activity where observable.

Do not claim causal separation between the content and CTA components launched together.

## Stop conditions

Stop before publication if:

- current official evidence cannot support a defensible model set;
- rollback capture fails;
- any approved Impact URL differs from the Task #63A verified link;
- required CTA destination or tracking behavior fails;
- preserving page 772 would be compromised;
- completing the task requires Publisher Tag, Catalog, global analytics code, another page’s migration, app/Vercel work or lead submission.
