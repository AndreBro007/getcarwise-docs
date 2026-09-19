# Four-Page SEO/GEO Forensic Comparison — GetCarWise

**Date:** 2026-09-19  
**Owner lane:** ChatGPT — Business/Strategy  
**Status:** Research/analysis complete. No implementation approval implied.  
**Pages:** SUV under $30k, Used PHEV, $25k SUV cluster, 3-row SUV under $50k.

## Executive finding

The four-page comparison supports a stronger hypothesis than “add more content”:

> **GetCarWise’s best combined SEO/GEO pattern is a narrow decision question, answered immediately, followed by standardized comparison evidence, explicit trade-offs, transparent methodology/sourcing, and a relevant action path.**

The current 3-row page is the clearest **GEO architecture benchmark**, but it is **not** a safe copy template because factual QA found material errors/ambiguities. The $30k page has enough content and strong head-keyword relevance already; its biggest gap is evidence/freshness/coherence, not length. The PHEV page has real demand but lacks the PHEV-specific evidence depth visible in the current SERP. The $25k cluster presents the strongest architecture risk because two closely related URLs are being surfaced differently by conventional Search and Google Generative AI.

Google’s 2026 guidance is consistent with this: SEO remains foundational to generative AI visibility, query fan-out retrieves related evidence across subtopics, Google prefers unique/non-commodity content, and unnecessary separate pages for query variations are discouraged.

Primary Google references:
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/appearance/ai-features

---

# 1. Measured four-page baseline

| Case | Conventional Search — US 28d | Google Generative AI — US 28d | Current Ubersuggest / SERP evidence | Commercial path |
|---|---|---|---|---|
| **SUV under $30k** | 21 impressions, 0 clicks, avg pos 26.05 | **3 AI impressions** | `best suv under 30000`: **#13**, vol 880, SD 27 in latest available page data; AI Overview present | **New + Used** |
| **Used PHEV** | **136 impressions**, 0 clicks, avg pos 43.07 | **1 AI impression** | `best used phev` ~#46, vol 210; `best used plug in hybrid` ~#52, vol 390; `best used plug in hybrid suv` ~#43, vol 320; `best phev vehicles` ~#53, vol 1,900; AI Overview present | **Used** |
| **SUV under $25k** | **122 impressions**, 0 clicks, avg pos 38.28 on `/under-25000/` | Exact Search URL absent; **different `/under-25k-comparison/` URL has 4 AI impressions** | `best suv under 25k`: ~#40, vol 390; `best suv under 25000`: ~#43, vol 320; `new suvs under 25k`: ~#37, vol 320; AI Overview present | **Used currently; intent split needs resolution** |
| **3-row SUV under $50k** | 41 impressions, 0 clicks, avg pos 19.71 | **78 AI impressions — site leader** | Current exact-query SERP is dominated by Car and Driver, Reddit, MotorTrend, U.S. News/TrueCar/KBB; AI Overview present | **New + Used potential; current page used-focused** |

### Ubersuggest page authority evidence

For the three pages where the daily page-report quota was still available on Sep 19:

| Page | Page Authority | Backlinks | Referring domains | Estimated organic traffic |
|---|---:|---:|---:|---:|
| $30k SUV | 14 | 0 | 0 | 1 |
| Used PHEV | 14 | 0 | 0 | 1 |
| $25k SUV | 14 | 0 | 0 | 0 |

The Ubersuggest daily report quota was exhausted before the 3-row page overview could be refreshed. Do not infer a value for that page.

**Strategic implication:** GetCarWise is competing against domains commonly in the DA 65–93 range with almost no page-level link authority. On-page work alone is unlikely to create a durable top-3 position. The content treatment should therefore be designed to create **original evidence worth citing/linking**, not merely a better article.

### Semrush note

A fresh Position Tracking pull was attempted on Sep 19. The connected Semrush project exists (`getcarwise.app`, project 30351889, Position Tracking enabled), but Semrush returned **“not enough api units to perform this action.”** Therefore this forensic pass uses the already-recorded Semrush on-page findings plus current GSC/Ubersuggest/web evidence; it does not pretend a new Semrush ranking pull succeeded.

---

# 2. Case A — SUV under $30k

URL: `/tools/best-compact-suv-under-30000/`

## What is already working

The page is not thin. The currently indexed page contains:

- an answer-first new-vs-used introduction;
- a new-SUV section;
- hybrid options;
- five ranked used picks;
- repeated price / MPG / cargo / reliability information;
- a side-by-side comparison table;
- practical “how to get a good deal” steps;
- FAQs;
- CarClever / Deal Score action path.

That explains why a DA-9 domain can still appear around #13 for `best suv under 30000` in Ubersuggest’s available dataset despite major authority disadvantages.

The current SERP contains an AI Overview and top organic competitors including Car and Driver, Edmunds, KBB, Reddit and inventory marketplaces. Car and Driver explicitly explains a roughly 200-data-point testing methodology; Edmunds’ ranking comes from a nine-vehicle comparison test. These pages have both authority and a clearly explained evidence base.

Competitor references:
- https://www.caranddriver.com/rankings/best-suvs/under-30k
- https://www.edmunds.com/car-news/small-suv-comparison-test-video-feature.html

## What is holding it back

### A. The evidence is presented as fact, but the method is mostly invisible

The page gives precise price bands, mileage ranges, reliability scores and “best” labels, but the visible content does not explain:

- which inventory dataset produced the price ranges;
- sample size;
- retrieval date;
- geography;
- how candidate years were chosen;
- how “value” was calculated;
- how reliability and resale claims were weighted.

That leaves the page closer to a polished editorial list than a reproducible GetCarWise analysis.

### B. The page mixes three user jobs without a formal decision framework

It covers:

1. new subcompact SUVs;
2. used compact SUVs;
3. used hybrids/PHEVs.

The mixed scope is useful, but the page does not yet make the comparison itself the organizing method. The page should answer:

> **With $30,000 today, when is new better, when is used better, and which models give the strongest value in each path?**

That single decision question would make the mixed scope coherent rather than diluted.

### C. Freshness has a confirmed factual problem

The page currently says a new Ford Escape Hybrid exists “in this price range.” Ford’s current official 2026 pricing shows:

- base Escape: **$30,350**
- Escape Hybrid: **$33,890**

Source: https://shop.ford.com/showroom/

That statement should be removed or reframed. This is exactly the kind of stale factual detail that weakens both user trust and AI citation reliability.

### D. Several absolute claims should either be sourced or softened

Examples include broad long-term failure/resale statements and price ranges presented without date/sample context. Even where directionally true, they are weaker than a dated, sourced market snapshot.

## Best treatment

**Do not add more generic prose.**

Build a visible **September 2026 GetCarWise Market Snapshot** and make it the evidence layer beneath the existing answer architecture.

The page should ultimately have three explicit winners:

- **Best new SUV path under $30k**
- **Best used compact-SUV path under $30k**
- **Best hybrid value under $30k**

Then explain who should choose each.

---

# 3. Case B — Used PHEV

URL: `/tools/best-used-phev-plug-in-hybrid/`

## What the data says

This is the strongest conventional-demand / weakest-GEO contrast:

- **136 GSC Search impressions** — highest measured content page;
- avg position ~43;
- only **1 Google Generative AI impression**.

Ubersuggest confirms meaningful query breadth:

- `best phev vehicles` — vol ~1,900, page ~#53;
- `list of phevs` — vol ~1,300, page ~#73;
- `best used plug in hybrid` — vol ~390, page ~#52;
- `best used plug in hybrid suv` — vol ~320, page ~#43;
- `best used phev` — vol ~210, page ~#46.

The current `best used phev cars` SERP has an AI Overview and is led by Consumer Reports, CarMax, Car and Driver, WIRED and KBB.

## What competitors answer that GetCarWise does not yet answer deeply enough

### Consumer Reports

CR’s current used-PHEV article is organized around the **actual decision mechanics**:

- will a used PHEV save money?
- are PHEVs reliable?
- electric-only range;
- gas-only fuel economy;
- long-range vs short-range older PHEVs;
- how PHEV capability changed by model year;
- whether the owner will actually charge frequently.

It is backed by CR testing and owner survey experience.

Reference:
https://www.consumerreports.org/cars/plug-in-hybrids/used-plug-in-hybrids-best-worst-ev-range-fuel-economy-a9601102060/

### CarMax

CarMax uses recent first-party sales/inventory behavior:

- recent six-month data window;
- popularity ranking;
- price range;
- owner rating;
- fuel economy;
- RepairPal reliability where available;
- pros/cons;
- direct current inventory.

Reference:
https://www.carmax.com/research/plug-in-hybrids/best-overall

## GetCarWise’s current gap

The retrievable indexed content is primarily:

- RAV4 Prime as the standout;
- Tucson PHEV / Sportage PHEV cross-shopping;
- Outlander PHEV;
- a CarClever Lite prompt.

That is useful, but it does not yet expose a PHEV-specific analytical framework comparable to the top SERP.

### Confirmed trust issue: warranty-transfer wording

The current page says the Hyundai Tucson PHEV and Kia Sportage PHEV offer Korean-brand warranty coverage that “transfers well to a second owner.”

That wording is too broad.

Hyundai’s official current warranty language says the 10-year/100,000-mile powertrain warranty applies to the original owner; subsequent owners receive powertrain coverage under the 5-year/60,000-mile New Vehicle Limited Warranty.

Kia’s warranty manual likewise states that the 120-month/100,000-mile Powertrain Limited Warranty is **not transferable to subsequent owners**.

Sources:
- https://www.hyundaiusa.com/ (current warranty language surfaced across model comparison pages)
- https://www.kia.com/content/dam/kwcms/pr/es/images/owners/warranty-recalls/kia-warranty-manual-en.pdf

This is a good example of why the PHEV rebuild needs **model-year and ownership-state-specific warranty evidence**, not generic “long warranty” copy.

## Best treatment

This page should become:

> **A used-PHEV decision guide based on how people actually use a PHEV, not simply a ranked model list.**

Core comparison dimensions should include:

- current used-market price;
- typical mileage / model-year availability;
- EPA electric-only range;
- gas-only MPG after battery depletion;
- charging frequency/use-case fit;
- transferred warranty / battery warranty;
- cargo/passenger compromise;
- reliability/repair evidence;
- current market availability;
- “best for” use case;
- specific used-buyer watch-outs.

This is the page where a genuinely differentiated GetCarWise dataset could move both SEO and GEO.

---

# 4. Case C — SUV under $25k cluster

Primary Search URL:
`/tools/best-compact-suv-under-25000/`

GEO URL:
`/tools/best-compact-suv-under-25k-comparison/`

## Why this is the clearest architecture problem

The Data & Guides hub currently exposes two entries with almost the same core intent:

- **Best Compact SUV Under $25K — CR-V vs RAV4 vs Tucson vs CX-5 vs Escape**
- **Best Compact SUV Under $25K — Ranked by value**

The GSC surfaces are already splitting:

- conventional Search: `/under-25000/` — **122 impressions**, avg pos ~38;
- Google Generative AI: separate `/under-25k-comparison/` — **4 AI impressions**.

Ubersuggest shows the `/under-25000/` page ranking for a broad cluster that already spans both “best” and “new” interpretations:

- `best suv under 25k` ~#40, vol 390;
- `best suv under 25000` ~#43, vol 320;
- `best suv under $25 000` ~#46, vol 320;
- `new suvs under 25k` ~#37, vol 320;
- `new suvs under 25000` ~#47, vol 260.

Its current Search Console/WordPress handoff describes the page as **used-focused** and the Sep 6 metadata was deliberately rewritten to:

- title: `Best Compact SUVs Under $25,000: Used Picks Compared`
- meta: compare used CR-V, RAV4, Tucson, CX-5 and Rogue by price, mileage, reliability and value.

## What the current SERP tells us

The `best suv under 25k` SERP has an AI Overview and mixes:

- editorial rankings (U.S. News, KBB);
- community advice (Reddit);
- used-focused editorial (Autotrader);
- new-focused ranking/product pages (TrueCar);
- inventory pages (CarGurus/Cars.com).

This means one strong page can legitimately answer the broad intent, with clear sections for “new at this budget” versus “used value,” if GetCarWise wants a broad page.

## Provisional conclusion

**Consolidation is more likely than keeping two near-duplicate pages**, unless a full audit proves the second URL has a genuinely different user job and independent query demand.

This is not yet a redirect instruction.

Before any merge/redirect, collect:

- full body of both URLs;
- title/H1/meta;
- canonical tags;
- GSC page-level query sets for each URL if available;
- internal-link sources;
- backlinks/referring domains;
- index status;
- historical traffic/clicks;
- whether one page is explicitly “comparison of five used models” and the other “broader current budget market.”

Google’s current AI guidance explicitly recommends reducing duplicate content and warns against creating separate pages for every query/fan-out variation.

## Best treatment

**Architecture first, content second.**

Do not spend time strengthening two URLs until we know which one should own the intent.

---

# 5. Case D — 3-row SUV under $50k: the GEO benchmark

URL:
`/tools/best-3-row-suv-under-50000/`

## Why this page matters

Measured baseline:

- 41 Search impressions;
- avg conventional position ~19.71;
- **78 Google Generative AI impressions** — the strongest measured GEO page on the site.

The exact `best 3 row suv under 50k` SERP is highly competitive: Car and Driver, Reddit, MotorTrend, U.S. News/TrueCar/KBB and an AI Overview. GetCarWise does not need to rank #1 for this exact head term to be useful to Google’s generative systems; Google’s own documentation explains that AI search uses query fan-out across related subtopics and pages.

## The architecture that is worth copying

This page repeatedly gives the model a predictable unit of evidence:

- model + model years;
- “best for” label;
- best trim;
- price range;
- cargo;
- fuel economy;
- reliability;
- warranty;
- explanatory paragraph;
- **Why buy**;
- **Watch for**.

Then it adds:

- one comparison table;
- deal-shopping guidance;
- FAQs;
- concrete next steps.

That architecture maps extremely well to likely fan-out questions:

- best overall?
- best for space?
- fuel economy?
- towing?
- warranty?
- reliability?
- cargo?
- what should I watch for?

This is the strongest site-specific evidence that **standardized, extractable trade-off blocks** are worth preserving.

## What must NOT be copied blindly

The factual layer needs work.

### Kia warranty claim

The page presents the Kia Sorento’s 10-year/100,000-mile powertrain warranty as protection that extends well into used ownership and says the coverage protects to 100k on many components.

Kia’s own warranty manual states that the 120-month/100,000-mile Powertrain Limited Warranty is **not transferable to subsequent owners**.

Source:
https://www.kia.com/content/dam/kwcms/pr/es/images/owners/warranty-recalls/kia-warranty-manual-en.pdf

### Ford Explorer engine claim

The page says the 2021–2022 Explorer XLT pairs a “turbocharged 3.5-liter EcoBoost” with its driving characteristics.

Ford’s official 2021 Explorer technical/order documentation says Base/XLT/Limited use the **2.3-liter EcoBoost I-4**; the 3.0-liter EcoBoost V6 is used for ST/Platinum variants.

Source:
https://media.ford.com/content/dam/fordmedia/North%20America/US/product/2021/explorer/21Explorer_Tech_Specs.pdf

This proves an important point:

> **The GEO winner’s structure appears strong enough to earn AI visibility despite factual weaknesses. Our opportunity is to preserve the structure and upgrade the evidence/trust layer.**

## Best treatment

Do not perform a broad rewrite during the first experiment.

1. Correct verified factual errors.
2. Add/clarify source provenance.
3. Add an updated/reviewed date and methodology note.
4. Preserve the repeated entity/attribute blocks, comparison table and FAQ/next-step structure.
5. Use it as the benchmark against which the $30k and PHEV treatments are evaluated.

---

# 6. Cross-page forensic conclusions

## Finding 1 — GEO success is not simply “rank higher in classic Search”

The 3-row page is the strongest internal proof:

- middling conventional Search visibility;
- disproportionate Google Generative AI visibility.

Therefore GEO should be measured separately, even though the foundational work overlaps with SEO.

## Finding 2 — “extractable comparison architecture” appears to matter

The 3-row page gives the clearest repeatable structure:

> **entity → standardized facts → best-for label → why buy → watch for → table → FAQs → action**

The page naturally answers multiple fan-out subquestions without needing separate URLs.

This is a stronger working hypothesis than “write FAQs for AI” or “make content longer.”

## Finding 3 — evidence/provenance is the biggest shared SEO/GEO upgrade

The top competitors repeatedly expose their evidence:

- Car and Driver: extensive instrumented tests / ~200 data points;
- Edmunds: explicit multi-vehicle comparison testing;
- Consumer Reports: purchased/tested vehicles + owner research;
- CarMax: recent six-month customer/sales data.

GetCarWise needs its own equivalent:

> **current market inventory analysis + transparent methodology + authoritative vehicle facts + buyer-specific trade-offs**

That is the shared layer that can improve SEO, GEO, authority/link earning and conversion trust at once.

## Finding 4 — the page should answer one decision, even when it contains many subtopics

- $30k currently contains useful new/used/hybrid material, but the central decision framework is implicit.
- PHEV needs the “does a used PHEV fit how you drive?” framework.
- $25k needs one clear URL/job.
- 3-row already has a coherent family/value comparison job.

## Finding 5 — authority is a real ceiling

GetCarWise’s low authority means we should not expect title/meta/body optimization alone to consistently beat DA-80+ publishers.

The highest-value content change is therefore one that is simultaneously:

- useful to a shopper;
- unique enough for AI systems to cite;
- useful enough for journalists/forums/sites to reference;
- tied naturally to CarClever and the New/Used/Trade-in funnel.

## Finding 6 — factual QA must become a formal pre-publication step

The live 3-row and PHEV pages contain warranty-transfer wording that is materially misleading for used buyers; the 3-row page also contains a confirmed Explorer engine error. The $30k page contains a stale new Escape Hybrid pricing claim.

A repeatable SEO/GEO system must include **fact/source QA before optimization**, not after.

---

# 7. GetCarWise evidence-first page blueprint v1

Do not make every page visually identical. Standardize the **evidence architecture**.

## 1. Fresh identity

- clear title/H1;
- visible updated/reviewed date;
- author/reviewer;
- one-sentence scope: new, used, or mixed.

## 2. 30-second answer

Answer the actual decision immediately.

Examples:

- “At $30k, buy used if you need compact-SUV space; buy new if warranty/zero-owner history matters more.”
- “A used PHEV makes sense if you can charge most days and buy enough electric range for your normal commute.”

## 3. Current market snapshot

Where validated and reproducible:

- retrieval period/date;
- qualifying listing count;
- median price;
- median mileage;
- useful distribution/range;
- model-year availability;
- sample limitations.

## 4. Methodology

Explain:

- candidate inclusion;
- data source;
- ranking factors;
- how missing data is treated;
- what is not independently verified.

## 5. Standardized candidate blocks

Use repeated attributes appropriate to the decision.

Common:
- price;
- mileage/year availability;
- reliability;
- ownership cost;
- safety;
- best for;
- why buy;
- watch for.

PHEV-specific:
- electric range;
- gas-only MPG;
- battery/transfer warranty;
- charging-use fit.

3-row-specific:
- seating;
- third-row/cargo;
- towing;
- fuel economy.

## 6. One comparison table

Keep the most decision-relevant fields in one extractable table.

## 7. Decision tree

Explicitly tell different buyer types which path fits.

## 8. Evidence and source notes

Prefer:
- OEM;
- EPA;
- NHTSA;
- IIHS where relevant;
- GetCarWise/Auto.dev validated market evidence;
- clearly attributed third-party reliability evidence.

## 9. Buyer watch-outs

Negative/limiting information is valuable. Do not make every candidate sound good.

## 10. Natural action path

Only after the decision:

- CarClever research/evaluation;
- appropriate New/Used Edmunds action;
- Trade-in where contextually relevant.

Do not let affiliate inventory determine the recommendation.

---

# 8. Exact data requirements for the next Claude brief

The forensic comparison now narrows the engineering/data request.

## $30k dataset

Need a reproducible U.S. market snapshot for a controlled candidate set:

- model / relevant year range;
- qualifying listing count under $30k;
- median asking price;
- median mileage;
- P25/P75 price if practical;
- model-year distribution;
- condition/new-used classification;
- retrieval date and filter logic;
- duplicate handling;
- geography definition.

New-model MSRP/availability should come from OEM sources, not inferred from used inventory.

## Used PHEV dataset

For selected PHEV models:

- used listing count;
- model-year distribution;
- median asking price;
- median mileage;
- current availability;
- EPA electric-only range by relevant model year;
- gas-only/charge-depleted MPG where authoritative;
- OEM battery / powertrain warranty and transfer rules;
- validated reliability/repair evidence if available;
- clear null/unknown handling.

## $25k cluster

**No large dataset yet.** First retrieve both page bodies and SEO/index/canonical/query evidence so André can make the URL architecture decision.

## 3-row benchmark

No major new market dataset is required for the first pass.

Need:
- factual/source audit of current repeated fields;
- correction list;
- source map;
- no structural rewrite initially.

---

# 9. Experiment design after implementation approval

### Treatment 1
$30k — evidence/freshness/methodology upgrade.

### Treatment 2
Used PHEV — full decision-framework rebuild.

### Architecture treatment
$25k — consolidate/differentiate first; optimize after.

### Protected comparator
3-row $50k — factual QA only.

### Untreated controls
Hybrid SUV under $20k, Used EV, F-150 vs Silverado.

Measure:
- T0 baseline;
- T+14 directional;
- T+28 primary;
- T+56 confirmation.

Keep content-treatment dates separate from future dynamic Edmunds inventory-module experiments.

---

# 10. Bottom line

The strongest repeatable hypothesis is not “SEO content” versus “GEO content.”

It is:

> **A single decision-focused page with current proprietary evidence, transparent sourcing, standardized comparison blocks, explicit trade-offs and a natural next action can serve classic Search, generative retrieval, human decision-making and commercial conversion at the same time.**

The 3-row page shows the architecture.  
The $30k page is the best combined treatment.  
The PHEV page is the best rebuild test.  
The $25k cluster is the architecture warning.

The next engineering handoff should request **only the data/evidence needed to build these treatments**, not broad website implementation.
