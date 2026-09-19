# Handoff — WordPress SEO/GEO Batch 1 + Batch 2 Implementation

**Date:** 2026-09-19  
**From:** ChatGPT — Business/Strategy lane  
**To:** Claude — Engineering / authenticated WordPress execution lane  
**Status:** **APPROVED BY ANDRÉ for implementation**  
**Scope:** WordPress content/SEO implementation only.  
**No application/MCP/Vercel/deployment changes.**

## Governing evidence

Read these in full before editing:

1. `STRATEGY_FOUR_PAGE_EDITORIAL_DECISION_PACKAGE_20260919.md`
2. `RESEARCH_WEB_VALUE_CROSSCHECK_20260919.md`
3. `RESEARCH_SEO_GEO_DATA_EVIDENCE_RESULTS_20260919.md`
4. `ANALYSIS_FOUR_PAGE_SEO_GEO_FORENSIC_20260919.md`
5. `HANDOFF_WEBSITE_SEO_CTA_OPPORTUNITY_PASS_20260904.md`

André has approved the four editorial directions. This handoff implements only **Batch 1** and **Batch 2**.

---

# 0. Non-negotiable boundaries

Do **not**:

- edit application code;
- edit MCP tools/prompts;
- touch Vercel;
- change production app routing;
- implement PHEV rebuild yet;
- merge/redirect the $25k comparison URL yet;
- change canonicals yet;
- change Edmunds affiliate network/tracking as part of this content treatment;
- add a dynamic Edmunds inventory module;
- add banners;
- introduce new schema types on the $30k treatment;
- change the existing CarClever Lite embed;
- change the existing $30k Edmunds CTA destination/tracking/disclosure unless a separate approved affiliate-migration task explicitly authorizes it.

**Reason:** this is a controlled SEO/GEO content experiment. Monetization/network changes must remain separately dated so we can attribute effects.

---

# 1. Mandatory preflight and baseline capture

Before any WordPress edit:

## 1.1 Capture live technical state

For each of these URLs:

- `/tools/best-3-row-suv-under-50000/`
- `/tools/best-compact-suv-under-25000/`
- `/tools/best-compact-suv-under-25k-comparison/`
- `/tools/best-compact-suv-under-30000/`
- `/tools/`

Record:

- HTTP status;
- title tag;
- meta description;
- H1;
- canonical;
- robots;
- schema types;
- sitemap `lastmod`;
- current CTA label + destination;
- current affiliate disclosure;
- current word count;
- current heading outline.

Use the sitemap `lastmod`, **not** JavaScript `document.lastModified`; Claude already proved `document.lastModified` reflects site-wide deploy time rather than page edit time.

## 1.2 Capture GSC baseline immediately before Batch 2

For `/tools/best-compact-suv-under-30000/`, save the current US 28-day:

- clicks;
- impressions;
- CTR;
- average position;
- visible top queries;
- Google Generative AI impressions.

Also retain the Sep 16/19 historical baselines from the strategy docs.

Do not wait for Semrush.

## 1.3 Preserve rollback material

Before editing each page:

- save the current WordPress body/content or an exact page export;
- save current Rank Math title/meta values;
- record page/post ID.

This is especially important because earlier WordPress work proved stale editor tabs can overwrite REST edits.

Close/refresh any stale editor tab before saving.

---

# 2. BATCH 1 — low-risk corrections and architecture prep

## 2A. 3-row SUV under $50k — factual correction only

URL:

`https://getcarwise.app/tools/best-3-row-suv-under-50000/`

### Objective

Correct two confirmed factual problems without changing the successful GEO architecture.

Preserve:

- H1/title/meta unless a technical mismatch is discovered;
- recommendation ordering;
- "Best for" labels;
- per-model block structure;
- "Why buy";
- "Watch for";
- comparison table;
- FAQ structure;
- existing CTA/disclosure;
- CarClever prompts;
- URL/canonical/schema.

Do **not** perform a broad rewrite.

---

## 2A.1 Kia Sorento warranty correction

Claude located the problematic wording in the Sorento body copy, the FAQ, and related summary/table language.

### Replace misleading body wording

Any wording equivalent to:

> "The 10-year/100,000-mile powertrain warranty extends well beyond competitors, providing peace-of-mind for 60k+-mile vehicles."

must be replaced with:

> **Warranty note:** Kia’s 10-year/100,000-mile powertrain warranty is an original-owner benefit and does not transfer in full to an ordinary subsequent owner. Qualifying Kia Certified Pre-Owned vehicles have separate CPO limited powertrain coverage. Verify the remaining warranty on the specific vehicle before buying.

### Replace/adjust Sorento "Why buy"

If the current "Why buy" relies on "industry-leading 10yr/100k warranty," replace only that part with:

> **Why buy:** Strong value, family-friendly packaging, and available turbo power; qualifying Kia CPO examples may include separate CPO powertrain coverage.

Do not imply ordinary used vehicles retain the original owner's full 10/100 warranty.

### Comparison table warranty cell

Replace any simple Sorento value such as:

> `10 years / 100,000 miles`

with:

> `Original-owner 10yr/100k; verify used/CPO coverage`

### FAQ warranty wording

Replace any FAQ sentence equivalent to:

> "Kia and Hyundai: 5 years / 60,000 miles (basic) + 10 years / 100,000 miles (powertrain)—industry-leading coverage that protects you to 100k miles on many components."

with:

> **Kia warranty note:** The original 10-year/100,000-mile Kia powertrain warranty does not transfer in full to an ordinary subsequent owner. Qualifying Kia CPO vehicles have separate CPO limited powertrain coverage, so used buyers should verify the specific vehicle’s warranty status rather than assuming the original term applies.

Do not broaden this correction into unsupported Hyundai warranty copy.

### Source

Kia U.S. warranty manual:  
`https://www.kia.com/content/dam/kwcms/pr/es/images/owners/warranty-recalls/kia-warranty-manual-en.pdf`

Kia CPO:  
`https://www.kia.com/us/en/cpo`

---

## 2A.2 Ford Explorer XLT engine correction

The current page associates the 2021–2022 Explorer XLT with a 3.5-liter EcoBoost.

Replace that factual statement with:

> **The 2021–2022 Explorer XLT uses Ford’s turbocharged 2.3-liter EcoBoost four-cylinder, rated at 300 horsepower.**

If the surrounding sentence currently attributes handling/performance to a 3.5L engine, rewrite only enough to make the paragraph grammatical and accurate.

Do not introduce a different trim or V6 claim unless separately verified.

### Sources

Ford 2021 technical specification:  
`https://media.ford.com/content/dam/fordmedia/North%20America/US/product/2021/explorer/21Explorer_Tech_Specs.pdf`

Ford 2021 order guide:  
`https://media.ford.com/content/dam/fordmedia/North%20America/US/product/2021/explorer/2021-Explorer-Order-Guide.pdf`

Edmunds 2021 Explorer:  
`https://www.edmunds.com/ford/explorer/2021/review/`

Edmunds 2022 trims:  
`https://www.edmunds.com/ford/explorer/2022/trims/`

---

## 2A.3 Add one restrained source note

Near the end of the 3-row page, before the FAQ or source-adjacent section, add:

> **How we verify specs:** We check model-year specifications and warranty terms against manufacturer documentation where available. Used-vehicle prices, third-party reliability ratings, recalls, and remaining warranty coverage can change or vary by vehicle, so verify the exact VIN and current records before buying.

Do not add a long methodology section in Batch 1.

---

## 2B. $25k architecture prep — no consolidation yet

URLs:

- retain later: `/tools/best-compact-suv-under-25000/`
- redirect later: `/tools/best-compact-suv-under-25k-comparison/`

### Objective

Prepare the retained page's internal discoverability **without merging or redirecting yet**.

### 2B.1 Capture baseline

Before any edit, record both pages' current:

- title/meta/H1;
- canonical;
- schema;
- sitemap lastmod;
- word count;
- headings;
- GSC conventional Search page metrics if available;
- GSC Generative AI page impressions if available.

### 2B.2 Add a single descriptive link from the Tools hub

On `/tools/`, add one restrained editorial link to:

`https://getcarwise.app/tools/best-compact-suv-under-25000/`

Suggested anchor:

> **Best compact SUVs under $25,000 — compare used picks**

Suggested supporting copy:

> Shopping by budget? See our guide to the best used compact SUVs under $25,000, including the trade-offs between price, age, mileage, and value.

Placement:

- near the end of the Tools page's main content, before the site's footer;
- do not turn the page into a blog index;
- do not remove or demote the existing tools;
- do not add the comparison URL.

### 2B.3 No other $25k changes in Batch 1

Do **not**:

- merge bodies;
- redirect;
- change either canonical;
- noindex either URL;
- alter titles/metas;
- change schema;
- rewrite either page.

Those belong to Batch 4 after the $30k and PHEV experiments are underway.

---

# 3. BATCH 2 — $30k controlled SEO/GEO treatment

Target:

`https://getcarwise.app/tools/best-compact-suv-under-30000/`

This is the primary treatment page.

## 3.1 Keep stable

Keep:

- existing URL;
- current canonical;
- index/follow state;
- existing affiliate CTA destination/tracking;
- existing affiliate disclosure (unless the exact wording is clearly broken);
- existing CarClever Lite embed;
- existing schema types;
- page ID.

Do not add new dynamic inventory.

---

## 3.2 Set Rank Math / rendered metadata

### SEO title

`Best SUVs Under $30,000 (2026): New vs. Used Picks`

### Meta description

`Compare new and used SUVs under $30,000 in 2026. See destination-inclusive new-car prices, live used-market availability, and which path fits you.`

### H1

`Best SUVs Under $30,000 in 2026: New vs. Used Picks`

Ensure Rank Math, rendered title, and H1 all reflect the intended topic. Do not use "Small SUV" as the H1/title.

---

# 4. Publish-ready $30k body copy

Use the following as the **new editorial body**, adapting only Gutenberg/WordPress formatting. Do not make substantive editorial changes without returning to ChatGPT.

---

## INTRO / ANSWER-FIRST BLOCK

**Updated: September 19, 2026**

A $30,000 SUV budget buys two very different kinds of vehicle in 2026.

Buy **new**, and you are mostly shopping smaller crossovers or entry trims with a full new-car warranty and no previous-owner history. Buy **used**, and the same budget opens up larger compact SUVs such as the Toyota RAV4, Mazda CX-5, Subaru Forester and Nissan Rogue.

There is no single best answer for everyone. If warranty coverage, a clean ownership history and predictable first-year costs matter most, start with the new choices. If you want more space, equipment or a larger compact SUV for the same money, used is usually the stronger value path.

### Quick answer

| If you care most about… | Start here |
|---|---|
| Lowest new-car starting price | Chevrolet Trax |
| A new SUV with more budget left for options | Nissan Kicks or Chevrolet Trailblazer |
| A more upscale-feeling small crossover | Mazda CX-30 |
| A simple new-vs-used ownership decision | Honda HR-V vs. a used RAV4/CX-5/Forester |
| Maximum current used-market choice | Nissan Rogue |
| Broad used-SUV availability and resale demand | Toyota RAV4 |
| Standard AWD as a core requirement | Subaru Forester |
| Driving feel and cabin presentation | Mazda CX-5 |

---

## H2 — What $30,000 buys new in 2026

For this guide, a new SUV only counts as **under $30,000** if its starting price remains below the cap **after mandatory destination/freight is included**. Taxes, registration, dealer fees and optional equipment are still extra.

That matters because several SUVs advertise base MSRPs below $30,000 but cross the line once mandatory destination is added.

| New SUV | Starting price incl. destination* | Why it belongs on the list |
|---|---:|---|
| **2026 Chevrolet Trax** | **$23,495** | Lowest verified starting price in this group |
| **2027 Nissan Kicks** | **$24,335** | Leaves substantial room below the $30k cap |
| **2026 Chevrolet Trailblazer** | **$25,095** | Still comfortably below the cap after destination |
| **2027 Kia Seltos** | **$26,485** | A practical small-SUV alternative with room below $30k |
| **2026 Hyundai Kona** | **$27,100** | A current sub-$30k choice even after destination |
| **2026 Mazda CX-30** | **$27,970** | One of the more premium-feeling choices in this price band |
| **2026 Honda HR-V** | **$28,050** | A straightforward new-Honda path that remains under the cap |

*Starting price includes mandatory destination/freight where current sources allow a reliable normalization. It does not include tax, title, registration, dealer fees or options.

### What no longer makes the cut

A headline MSRP below $30,000 is not enough.

- The **2027 Kia Niro Hybrid** starts above $30,000 once destination is included.
- The current **2026.5 Nissan Rogue** also starts above $30,000 after destination.
- The **2026 Hyundai Tucson** has a sub-$30k headline MSRP before freight, but its actual starting sticker exceeds the budget.

A remaining **new 2026 Kia Niro Hybrid** can still fit below $30,000 including destination if unsold 2026 inventory is available, but treat it as a carryover opportunity rather than the baseline current-model choice.

---

## H2 — What the same $30,000 buys used

Used is where the budget opens up.

CarClever's live provider data, checked **September 19, 2026**, reported large nationwide matching pools of used compact SUVs priced at $30,000 or less:

| Used model | Provider-reported matching inventory |
|---|---:|
| **Nissan Rogue** | about **30,100** |
| **Toyota RAV4** | about **17,200** |
| **Subaru Forester** | about **14,000** |
| **Mazda CX-5** | about **12,600** |

These are **CarClever provider-reported matching counts**, not an audited count of every vehicle for sale in the United States. Marketplace coverage, duplicate handling and listing turnover vary, so use them as an availability signal rather than a fixed market-size statistic.

We also consider the **Honda CR-V** a natural used comparison in this budget, but we are not publishing a nationwide CR-V count from this snapshot because the data pull available for this review was not directly comparable with the nationwide queries above.

### Toyota RAV4 — best starting point for broad used-SUV appeal

The RAV4 is the natural benchmark if you want a mainstream compact SUV with a large current used pool and strong buyer demand. At $30,000, the question is less "can I find one?" and more which model year, mileage, drivetrain and history give you the best trade-off.

**Why buy:** broad availability makes it easier to be selective.

**Watch for:** don't pay a premium simply for the badge. Compare age, mileage, trim, accident history and local alternatives.

### Mazda CX-5 — best if driving feel and cabin presentation matter

The CX-5 is a useful contrast to the pure value picks. It gives shoppers a compact-SUV footprint with a more driver-focused feel and cabin presentation while still showing meaningful used availability below $30,000.

**Why buy:** a strong option when you want your budget to buy something that feels less basic.

**Watch for:** compare trim and drivetrain carefully; higher-spec examples can consume the budget quickly.

### Subaru Forester — best if AWD is central to the decision

The Forester belongs on the shortlist when all-wheel drive, visibility and practical SUV use matter more than styling or outright performance.

**Why buy:** a clear fit for buyers who prioritize everyday utility and AWD.

**Watch for:** compare condition and maintenance history rather than assuming two same-year Foresters are equivalent.

### Nissan Rogue — best for raw choice

The Rogue produced the largest matching used pool in this snapshot. That is useful because a buyer can often be more demanding about mileage, trim, location and reported history instead of settling for the first vehicle that fits the budget.

**Why buy:** large current choice.

**Watch for:** large inventory is not the same as best vehicle. Use the extra supply to compare aggressively.

### Honda CR-V — still a core comparison

The CR-V remains one of the first used compact SUVs worth cross-shopping at this budget.

We deliberately excluded it from the nationwide-count table because the available evidence pull for this review used a different geographic scope. That is a limitation of this snapshot, not a claim that CR-V supply is low.

**Why buy:** a well-rounded comparison point for shoppers deciding between a new smaller SUV and a used compact SUV.

**Watch for:** don't treat model reputation as a substitute for checking the specific vehicle's history, mileage, recalls and price.

---

## H2 — New vs. used: which path fits you?

| Choose new if… | Choose used if… |
|---|---|
| You want a full new-car warranty | You want a larger compact SUV for the same budget |
| You prefer no previous-owner history | You want more trim/features for the money |
| Predictable early ownership matters most | You are comfortable comparing mileage and condition |
| A smaller crossover fits your space needs | RAV4/CR-V/CX-5/Forester-size vehicles fit you better |
| You value simplicity over maximizing vehicle size | You are willing to inspect history and condition carefully |

### New is usually the cleaner decision

A Trax, Kicks, Trailblazer, Seltos, Kona, CX-30 or HR-V gives you a known starting point, a current model year and a full new-car warranty. The trade-off is that your $30,000 buys a smaller vehicle or a lower trim than it can on the used market.

### Used usually buys more vehicle

A used RAV4, CR-V, Forester, CX-5 or Rogue puts you in the mainstream compact-SUV class rather than the entry-level end of the new market. The trade-off is that age, mileage, history and remaining warranty now matter much more.

---

## H2 — How we built this comparison

We used two different evidence sets because new and used vehicles require different questions.

### New vehicles

A vehicle only qualifies as "under $30,000" here if the current starting price remains below $30,000 **including mandatory destination/freight** where that figure can be reliably verified.

We cross-checked current pricing against manufacturer pages and independent automotive sources.

### Used vehicles

Used-market availability comes from CarClever's live provider-reported matching inventory on **September 19, 2026**.

The search was used to answer:

- Is there meaningful current supply below $30,000?
- Which mainstream models give a shopper enough choice to compare rather than settle?
- Does the budget support moving from a new small SUV to a used compact SUV?

We do **not** present the tool's five returned examples as an average, median or market-price distribution. The shortlist is a ranking result, not a statistical sample.

### What this guide does not assume

We do not assume that:

- a high listing count makes a model automatically better;
- an advertised base MSRP equals the real starting sticker;
- a famous reliability reputation guarantees a specific used vehicle is clean;
- an affiliate listing determines our recommendation.

The recommendation comes first. Inventory is the next step.

---

## H2 — What to verify before you buy

Whether you choose new or used, verify the exact vehicle rather than relying on the model name alone.

### On a new SUV

Check:

- destination/freight;
- dealer-installed accessories;
- documentation fees;
- trim-specific equipment;
- out-the-door price.

### On a used SUV

Check:

- VIN and exact trim;
- mileage;
- accident/title history;
- open recalls;
- maintenance records;
- CPO status if claimed;
- remaining warranty;
- asking price against comparable vehicles.

A $29,000 used SUV with a weak history can be worse value than a $30,000 example with stronger documentation.

---

## H2 — Best $30k SUV path by buyer type

### Best if you want the lowest-cost new starting point
**Chevrolet Trax**

It gives you the most room below the $30,000 ceiling among the verified current choices in this guide.

### Best if you want a new SUV but still want budget flexibility
**Nissan Kicks or Chevrolet Trailblazer**

Both sit comfortably below the cap after destination, leaving more room than the vehicles clustered near $28,000.

### Best if you want a more premium-feeling new option
**Mazda CX-30**

It sits near the upper end of the verified sub-$30k group but offers a different ownership proposition from the cheapest entries.

### Best if you want more SUV for the same money
**Shop used RAV4, CR-V, Forester, CX-5 and Rogue**

That is where the $30,000 budget starts buying mainstream compact-SUV space instead of an entry-level new crossover.

---

## H2 — Ready to compare real vehicles?

**Keep the existing live Edmunds CTA, its current affiliate destination/tracking, and its current disclosure exactly as implemented unless a separate affiliate-migration task authorizes a change.**

Do not add a second Edmunds CTA.

Immediately after the existing CTA/disclosure, keep the existing CarClever Lite block.

Add one contextual internal link before or after the CTA block:

> If your budget is closer to $25,000, see our **Best Compact SUVs Under $25,000: Used Picks Compared** guide.

Link to:

`https://getcarwise.app/tools/best-compact-suv-under-25000/`

---

## H2 — Frequently asked questions

### Are there really new SUVs under $30,000 in 2026?

Yes. In this review, seven current new SUVs remained below $30,000 after mandatory destination/freight: the Chevrolet Trax, Nissan Kicks, Chevrolet Trailblazer, Kia Seltos, Hyundai Kona, Mazda CX-30 and Honda HR-V.

Taxes, registration, dealer fees and options are extra.

### Is it better to buy a new or used SUV for $30,000?

Neither is automatically better. New gives you a current model year, no previous-owner history and full new-car warranty coverage. Used usually lets the same budget buy a larger compact SUV or more equipment. Your tolerance for mileage, history and warranty trade-offs should decide the path.

### Why don't you count every SUV with a base MSRP under $30,000?

Because mandatory destination/freight is part of the starting cost. A vehicle with a $29,700 headline MSRP can already be above $30,000 before taxes or options. We use destination-inclusive starting prices where they can be reliably verified.

### Are the used inventory counts every vehicle for sale in the U.S.?

No. They are rounded CarClever provider-reported matching counts from a dated live inventory snapshot. Different marketplaces cover different dealers and feeds, so the numbers are an availability signal, not an audited count of the entire U.S. market.

---

# 5. $30k source block

At the end of the article, add a compact source section. Do not reproduce source text; link to sources.

Suggested heading:

## Sources and pricing checks

Suggested intro:

> New-vehicle prices were checked against manufacturer sources and cross-checked against independent automotive references. Used availability reflects a dated CarClever provider inventory snapshot. Prices and inventory change, so recheck the exact vehicle before buying.

Include these editorial links:

- Chevrolet Trax — `https://www.chevrolet.com/suvs/trax`
- Chevrolet Trailblazer — `https://www.chevrolet.com/suvs/trailblazer`
- Chevrolet destination charges — `https://www.chevrolet.com/destination-freight-charges`
- Nissan Kicks — `https://www.nissanusa.com/vehicles/crossovers-suvs/kicks/specs-trims.html`
- Kia Seltos — `https://www.kia.com/us/en/seltos`
- Hyundai Kona — `https://www.hyundaiusa.com/us/en/vehicles/kona`
- Mazda CX-30 — `https://news.mazdausa.com/vehicles-2026-cx-30`
- Mazda destination update — `https://news.mazdausa.com/2026-08-11-Mazda-Adjusts-Destination-and-Handling-Charge%2C-Effective-August-11%2C-2026`
- Honda HR-V — `https://automobiles.honda.com/2026/hr-v`

Independent cross-check references may be included selectively if the page design supports them, but do not turn the source section into a link dump.

Ordinary editorial source links are not affiliate links.

---

# 6. WordPress / Rank Math execution details

## 6.1 Rank Math

Set the exact title/meta in Section 3.2.

Previous work established that Rank Math fields are not reliably writable through core WordPress REST meta. Use the Rank Math snippet/editor UI if required and verify the rendered HTML afterward.

## 6.2 Content editing

Use the safest authenticated WordPress mechanism already documented in:

- `STATE.md`
- `DECISIONS.md` `SYS-20260906-003`

Do not leave a stale Gutenberg editor open while modifying the same page through REST.

## 6.3 Formatting

Use native WordPress blocks:

- Heading blocks for H2/H3;
- accessible tables for comparison data;
- normal paragraphs/lists;
- preserve responsive behavior;
- do not inject a custom JS/CSS component for this content pass.

## 6.4 Links

- Editorial source links: normal editorial links.
- Existing affiliate CTA: preserve its current sponsored/affiliate semantics.
- Internal $25k link: normal internal link.
- Do not add nofollow/sponsored to OEM editorial citations.

---

# 7. Post-implementation verification — mandatory

After Batch 1 and Batch 2, re-fetch and verify the rendered pages.

## 7.1 3-row page

Confirm:

- Sorento ordinary-used warranty text no longer implies full original 10/100 transfer;
- CPO exception is clear;
- no duplicate misleading warranty sentence remains in FAQ/table/body;
- Explorer XLT says 2.3L EcoBoost / 300 hp, not 3.5L;
- H1/title/meta/structure otherwise unchanged;
- CTA/disclosure unchanged;
- canonical/schema unchanged.

## 7.2 Tools page

Confirm:

- one new descriptive link to `/under-25000/`;
- no link to `/under-25k-comparison/` was added;
- existing tool hierarchy remains intact.

## 7.3 $30k page

Confirm:

- exact SEO title;
- exact meta;
- exact H1;
- URL unchanged;
- canonical unchanged;
- robots unchanged;
- schema types unchanged;
- source links work;
- seven current true-under-$30k models use the exact approved prices;
- Rogue/Tucson/2027 Niro are not presented as current true-under-$30k new choices;
- used counts are labeled provider-reported/datetime-specific;
- no CR-V nationwide count is published;
- no median/average/P25/P75 used-price claim was introduced;
- existing Edmunds CTA destination/tracking remains unchanged;
- no duplicate Edmunds CTA;
- affiliate disclosure remains visible;
- CarClever Lite remains present;
- internal $25k link works.

## 7.4 Record sitemap lastmod after save

Use `page-sitemap.xml`.

Do not use `document.lastModified`.

## 7.5 Request recrawl/indexing

For the $30k treatment page, request Google recrawl/indexing through the existing approved Search Console workflow if available.

For the 3-row correction page, a recrawl request is optional; record the update regardless.

---

# 8. Implementation result document

After all work succeeds, create:

`RETURN_WORDPRESS_SEO_GEO_BATCH1_BATCH2_20260919.md`

Include:

1. execution date/time;
2. WordPress page IDs;
3. pre-change title/meta/H1/canonical/schema/lastmod;
4. exact changes made;
5. post-change title/meta/H1/canonical/schema/lastmod;
6. $30k pre-change GSC Search baseline;
7. $30k pre-change Google Generative AI baseline;
8. existing affiliate CTA URL/label before and after — prove it was not changed;
9. source links added;
10. screenshots or textual verification notes where useful;
11. failures/blockers;
12. whether recrawl was requested.

Re-fetch the result document after writing it and verify expected content.

---

# 9. Acceptance criteria

Batch 1 + Batch 2 are complete only when:

- both 3-row factual errors are corrected everywhere they occur;
- $25k retained page gains exactly one intentional Tools-hub internal link;
- no $25k redirect/merge occurred;
- $30k title/meta/H1 match this handoff;
- $30k body contains the approved destination-inclusive new-price logic;
- no unverified median/typical used-price statistics appear;
- existing affiliate CTA/tracking is unchanged;
- rendered pages are re-fetched and verified;
- result doc is committed and re-fetched;
- no app/Vercel/MCP changes occurred.

If WordPress access or Rank Math persistence fails, stop and report the blocker rather than approximating the requested state.
