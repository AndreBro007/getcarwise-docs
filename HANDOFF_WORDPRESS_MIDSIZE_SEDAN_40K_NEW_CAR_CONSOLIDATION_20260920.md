# Handoff — WordPress Midsize Sedan Under $40K New-Car Rebuild and Cluster Consolidation

**Task:** #70  
**Owner:** Claude — authenticated WordPress/GSC implementation lane  
**Authorized scope:** the two named WordPress URLs, their internal links, verified static funnel destinations, GSC inspection/indexing, and the return document  
**Not authorized:** application-code changes; Vercel/MCP work; public Impact Catalog/module work; Publisher Tag; sitewide CJ→Impact migration; unrelated WordPress changes

## Decision already made

Implement **Option A**: rebuild the retained URL as a broad, current, evidence-led guide to **new midsize sedans under $40,000**.

Primary retained URL:

`https://getcarwise.app/tools/best-midsize-sedan-under-40000/`

Adjacent overlap candidate:

`https://getcarwise.app/tools/best-midsize-sedan-under-30k-comparison/`

Default outcome, subject to the evidence gate below: merge unique useful content from the $30k page, then one-hop permanent-301 it to the retained $40k URL.

Read in full before acting:

- `RETURN_WORDPRESS_MIDSIZE_SEDAN_40K_INTENT_AUDIT_20260920.md`
- `REVIEW_WORDPRESS_MIDSIZE_SEDAN_40K_INTENT_AUDIT_20260920.md`
- `STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md`
- `RETURN_TOOL_LED_IMPACT_FUNNEL_FEASIBILITY_20260920.md`
- `STRATEGY_MASTER_SEO_GEO_REVENUE_MATRIX_20260919.md`
- the current repository startup/admin instructions

## Non-negotiable sequence

### 1. Start-of-session verification

Perform the mandatory repository verification. Read all changed/task-relevant files in full. Do not rely on this handoff alone if later repository documents change the decision.

### 2. Preserve both pages before touching either

For **both URLs**, capture and retain:

- exact rendered HTML/content and editable WordPress content;
- page ID/status/modified time;
- title, meta description, H1;
- canonical and robots;
- schema;
- sitemap presence/lastmod;
- all outbound/internal/affiliate links;
- CTA labels, destinations, rel/target attributes and disclosures;
- screenshots sufficient for rollback/visual comparison.

Create explicit rollback copies before any edit or redirect.

### 3. Capture fresh two-URL T0 evidence immediately before changes

For **each URL separately**, capture:

- GSC Search: latest 28 days, previous 28 days and latest 3 months;
- clicks, impressions, CTR and average position;
- complete visible query and page data;
- device split where available;
- Google Generative AI impressions;
- current index/inspection state.

Record the exact capture timestamp and the exact implementation timestamp.

### 4. Mandatory cluster decision gate

Determine whether the $30k URL has a material distinct job.

Proceed with merge/301 only when fresh evidence shows that it:

- substantially overlaps the same category/value/three-model intent;
- lacks a defensible distinct query family;
- is not materially stronger in a way that changes which URL should be retained.

If it has meaningful distinct intent or materially stronger signals, **stop before editing or redirecting**. Write a decision-gate return with the full evidence and proposed alternatives. Do not improvise a second page strategy.

If evidence supports consolidation, document the choice and continue.

### 5. Verify the current eligible model field

Use current official US manufacturer sources immediately before drafting. Verify:

- current model year is actually on sale;
- classification is midsize sedan;
- at least one meaningful configuration qualifies below $40,000 MSRP;
- which trims fall below/above the cap;
- destination-fee treatment;
- powertrain and AWD facts;
- warranty facts only if used.

Expected core candidates to verify:

- Toyota Camry
- Honda Accord
- Hyundai Sonata
- Kia K5
- Nissan Altima

Do not include a model simply because another roundup did. Do not present Civic Si or Prius as midsize without an explicit, defensible classification. Do not present discontinued/non-current Avalon, Legacy or Malibu as current new-car options.

### 6. Build the page around a documented decision method

Required page job:

> Help a US shopper choose among the best current new midsize sedans that can genuinely be configured below $40,000, explain the trade-offs, and give the reader a clear next action.

Required structure:

1. Answer-first summary
2. Dated “how we chose” method and cap definition
3. Scannable comparison table
4. One full section per verified core model
5. Best-for labels and meaningful drawbacks
6. “Which should you buy?” decision paths
7. Funnel continuation block
8. Concise FAQs based on real query language
9. Sources/data notes with current official links

Content rules:

- No unsupported used-mileage, ownership, accident-history or service-history claims.
- No unsourced superlatives about reliability, resale, owner satisfaction or maintenance.
- Clearly separate MSRP from destination, options, incentives and dealer price.
- State the source date.
- Correct the Camry hybrid-only and Altima optional-AWD issues identified by the audit.
- Preserve useful unique facts from the $30k page only after re-verification.
- Make read-time text match actual content.
- Use natural language; no keyword stuffing.

### 7. Make the funnel part of the design

The page must not end with a single mismatched used-car CTA.

Required hierarchy:

| Stage | Role | Placement |
|---|---|---|
| New | Primary conversion path for the page’s job | After the answer/comparison and again after the final recommendation where appropriate |
| Used | Clearly labelled alternative for budget/value shoppers | Secondary to New, not disguised as the primary action |
| Trade-in | Contextual replacement-intent bridge | Later in the decision flow; do not compete with the primary CTA above the fold |
| CarClever | Evaluation/tool continuation | Preserve and place coherently with the decision flow |

Before publication, validate the exact approved destinations and tracking behavior. Requirements:

- New destination is genuinely for new-car shopping;
- Used destination is genuinely for used-car shopping;
- Trade-in destination is genuinely for valuation/trade-in;
- no destination is guessed;
- affiliate disclosure remains clear;
- affiliate links use `rel="nofollow sponsored noopener"` and appropriate `target`;
- final destination/redirect behavior is verified;
- current CJ→Impact **sitewide** migration is not bundled into this task.

If an approved tracked New destination cannot be validated, **stop before publication** and return the blocker. Do not leave “Browse Used Cars” as the sole primary CTA on a new-car page.

Do not add an Impact Catalog inventory widget/module. Task #69 does not authorize public use.

### 8. Analytics/event contract

Verify or implement the approved page event naming available within the existing WordPress setup, without application-code work. At minimum the return must distinguish:

- New CTA clicks
- Used CTA clicks
- Trade-in clicks
- CarClever clicks/engagement where currently measurable
- outbound affiliate destination and page source where currently measurable

If the existing WordPress analytics layer cannot support this without code or global changes, document the exact gap; do not invent events or broaden scope silently.

### 9. SEO/GEO and technical verification

Before any redirect:

- verify title/meta/H1 align with the new broad current-new-car job;
- self-canonical retained URL;
- index/follow;
- one H1 and sensible heading order;
- accurate current primary sources;
- no contradictory old content;
- no orphan state: add/update Tools and Data & Guides links;
- update every internal link that points to the $30k URL;
- verify content parity and unique-content migration;
- validate schema against visible content;
- confirm mobile/desktop rendering and all CTAs.

Suggested direction, not immutable copy:

- Title/H1: “Best New Midsize Sedans Under $40,000”
- Meta: concise answer/value proposition mentioning current comparisons and shopper decision help

Do not force a year into the permanent URL. A current year may appear in visible copy/title only if the maintenance policy can keep it current.

### 10. Redirect only after parity

Only after all prior checks pass:

1. create a one-hop permanent 301 from the $30k URL to the retained $40k URL;
2. verify old URL → exactly one 301 → retained URL 200;
3. verify no loop or intermediate hop;
4. verify canonical and sitemap behavior;
5. confirm no internal link still points to the old URL;
6. inspect/request indexing in GSC for the retained URL and inspect/request recrawl of the redirected URL.

A temporarily stale sitemap entry may be documented, but the old URL must not be intentionally preserved as an indexable duplicate.

### 11. Return document

Create:

`RETURN_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_CONSOLIDATION_20260920.md`

It must include:

- exact timestamps;
- both pages’ complete T0 tables and query evidence;
- cluster decision and reasoning;
- rollback-copy locations;
- before/after title/meta/H1/canonical/robots/schema/read time;
- final verified model set and every primary source;
- factual-claim ledger;
- exact funnel CTA labels, placements, URLs, network/tracking method and verification;
- disclosure/rel/target verification;
- analytics/event verification or exact limitation;
- internal-link and hub changes;
- redirect proof and hop count;
- sitemap/canonical/GSC results;
- screenshots or direct evidence references;
- anything not completed and why;
- confirmation that no app/Vercel/MCP/Catalog/Publisher-Tag/sitewide migration work occurred.

Push the return, re-fetch it from main, and verify it byte-for-byte.

## Measurement

Treat this as its own cluster/content/funnel treatment.

- T+14: directional
- T+28: primary
- T+56: confirmation

Report Search and GEO at the retained URL plus redirect retirement behavior for the old URL. Also report New/Used/Trade-in/CarClever actions separately where available. Do not combine this treatment statistically with the $30k SUV, PHEV or $25k SUV treatments.

## Stop conditions

Stop and return evidence before changing production if:

- the $30k URL has a defensible distinct job or materially changes the retain/redirect choice;
- an approved New destination cannot be verified;
- current manufacturer evidence cannot support the proposed model set/cap;
- rollback copies cannot be made;
- the redirect cannot be guaranteed one-hop/permanent;
- required access fails;
- completing the task would require public Catalog rights, app code, Vercel changes, Publisher Tag or a sitewide affiliate migration.
