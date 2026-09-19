# Four-Page SEO/GEO Editorial Decision Package — Sep 19, 2026

**Owner:** ChatGPT — Business/Strategy lane  
**Status:** **APPROVED BY ANDRÉ — 2026-09-19. Values cross-checked before implementation; see `RESEARCH_WEB_VALUE_CROSSCHECK_20260919.md`.**  
**Evidence inputs:**  
- `ANALYSIS_FOUR_PAGE_SEO_GEO_FORENSIC_20260919.md`
- `RESEARCH_SEO_GEO_DATA_EVIDENCE_RESULTS_20260919.md`
- `STRATEGY_MASTER_SEO_GEO_REVENUE_MATRIX_20260919.md`
- `REVIEW_WEEKLY_SEO_GEO_REPORT_20260919.md`

André approved the four editorial directions on 2026-09-19. WordPress implementation should use the value-normalization rules and corrected figures in `RESEARCH_WEB_VALUE_CROSSCHECK_20260919.md`; no application/MCP/Vercel changes are authorized by this document.

---

# 1. Executive decisions proposed

## Decision A — $30k SUV

Proceed with a **controlled evidence-led refresh**, not a generic rewrite.

Core editorial promise:

> **With a $30,000 SUV budget today, when is a new small SUV the better choice, and when does a used compact SUV give you more vehicle for the money?**

Use current OEM MSRP evidence for the new-car side and **dated, rounded provider-reported availability counts** for the used side.

Do **not** publish fabricated median/P25/P75 market statistics. The current CarClever V1 tool cannot produce them.

## Decision B — Used PHEV

Proceed with a **full evidence-led rebuild**.

The page should stop being a short ranked list and become a decision guide answering:

> **Does a used PHEV make sense for how you actually drive, and which current used models best fit different buyer jobs?**

Use validated model-name populations for market availability. Do not use the provider electrification filter alone to define the PHEV population.

## Decision C — $25k cluster

**Recommend consolidation into:**

`/tools/best-compact-suv-under-25000/`

The stronger conventional-Search URL should become the single long-term page. Merge the richer comparison page's useful structure, methodology and unique evidence into it **before** redirecting anything.

After content parity, propose:

- 301 redirect `/tools/best-compact-suv-under-25k-comparison/` → `/tools/best-compact-suv-under-25000/`;
- update internal links to the retained URL;
- add the retained page to `/tools/`;
- preserve/migrate useful Article/Breadcrumb structured data;
- monitor conventional Search and Google Generative AI separately.

This is proposed, not implemented.

## Decision D — 3-row $50k benchmark

**Protect the page architecture.**

Make only a factual/source correction pass initially:

- correct Kia used-owner warranty wording;
- correct Ford Explorer XLT engine wording;
- remove or source unsupported precision where practical;
- add a short methodology/source note;
- preserve the entity → facts → best-for → why-buy → watch-for → comparison → FAQ architecture.

Do not broadly rewrite this page while it remains the site's strongest GEO benchmark.

---

# 2. Evidence-quality review of Claude's package

Claude's evidence package is useful and sufficient for the editorial decisions above, with four limitations that must remain visible.

## 2.1 No medians or percentiles

`find_matching_vehicle` is a shortlist/ranking tool, not a bulk statistical endpoint.

Therefore the current evidence supports:

- availability/pool counts;
- illustrative live examples;
- model-name population validation;
- technical page audits.

It does **not** support:

- median asking price;
- median mileage;
- P25/P75;
- national price distributions.

Do not invent those statistics.

## 2.2 CR-V is not comparable to the other $30k counts

Claude's CR-V run was California-only.

Do not publish the 1,682 CR-V figure beside the nationwide RAV4/CX-5/Rogue/Forester counts.

Either omit the CR-V availability count in the first treatment or obtain a clean nationwide count later.

This missing count is **not a blocker** to the page refresh.

## 2.3 Reproducibility requirement was only partially met

The handoff asked for exact-query reruns on at least two $30k candidates.

Claude reran only RAV4 and obtained identical results. The report then treats general stability observations as satisfying the two-candidate requirement.

That does not literally satisfy the requested two-candidate rerun.

It is a methodology gap, but not large enough to invalidate the editorial use proposed here because:

- the page will use rounded availability counts, not financial/statistical medians;
- the figures will be dated;
- the claims will be labeled as live provider-reported inventory counts;
- no ranking winner will be determined solely by those counts.

## 2.4 The old V1 `totalMatches` bug does not by itself invalidate the pool counts

ChatGPT independently checked the current read-only application repo.

The headline fix on branch `fix/total-matches-count-bug` (commit `ce161fc`) addresses a real display/interpretation bug:

- `totalMatches` = broader matching pool;
- `resultsShown` = number of actual returned cards.

The calling model had previously narrated the pool-scale count as if it were the number of results shown.

That fix does **not** say that ordinary `totalMatches` pool values for simple make/model/price queries are inherently invalid.

Separate known Auto.dev total-count edge cases still exist for particular filters, so all counts below remain described as **provider-reported live matching pools**, not independently audited U.S.-market totals.

---

# 3. $30k SUV — final editorial treatment

## 3.1 URL

Keep:

`/tools/best-compact-suv-under-30000/`

No URL change.

## 3.2 Proposed title / H1

**Title:**  
`Best SUVs Under $30,000 (2026): New vs. Used Picks`

**H1:**  
`Best SUVs Under $30,000 in 2026: New vs. Used Picks`

Reason:

- the proven head demand is broader `best suv under 30000`;
- the article genuinely compares small new SUVs against used compact SUVs;
- "Small SUV" alone is narrower than the article's actual job;
- "Compact SUV" alone also undersells the new-small-SUV side.

Use **SUV** as the headline category, then explain the size-class trade-off clearly in the opening.

## 3.3 Proposed 30-second answer

The opening should communicate this logic, with the exact model winners finalized after full source QA:

> Around $30,000, buying new usually means choosing a smaller crossover or a base trim. Buying used opens the door to larger compact SUVs such as the RAV4, CX-5, Forester and Rogue with more space or equipment. The better choice depends on whether you value a full new-car warranty and zero-owner history more than size, features and depreciation value.

Do not pick a single universal winner.

## 3.4 Current new-SUV evidence — web cross-checked

The value cross-check changed the eligibility rule:

> For a page promising **new SUVs under $30,000**, eligibility is based on the starting price **including mandatory destination/freight**, not merely the OEM headline MSRP before destination.

Full evidence and source disagreements: `RESEARCH_WEB_VALUE_CROSSCHECK_20260919.md`.

### Core current choices genuinely under $30k including destination

| Model | Publication-safe starting price | Cross-check status |
|---|---:|---|
| 2026 Chevrolet Trax | **$23,495** | OEM base + OEM destination; independently corroborated |
| 2027 Nissan Kicks | **$24,335** | OEM base + OEM destination; Cars.com corroborated |
| 2026 Chevrolet Trailblazer | **$25,095** | OEM base + OEM destination; C/D/Cars.com corroborated |
| 2027 Kia Seltos | **$26,485** | OEM base + destination; KBB/C&D corroborated |
| 2026 Hyundai Kona | **$27,100** | OEM base; KBB + Edmunds agree on destination-inclusive sticker |
| 2026 Mazda CX-30 | **$27,970** | Current OEM base + Aug 11, 2026 destination charge; live Edmunds inventory corroborates |
| 2026 Honda HR-V | **$28,050** | OEM base + OEM destination; C/D corroborated |

### Optional / inventory-dependent

- **2026 Kia Niro Hybrid — $28,885** including destination. Use only if meaningful remaining 2026 new inventory exists at publication time.

### Do not classify as true current new “under $30k”

- **2027 Kia Niro Hybrid — $31,385 including destination**
- **2026.5 Nissan Rogue — about $31,035 including destination**
- **2026 Hyundai Tucson — current OEM base MSRP $29,700 excludes freight; independent current sticker sources place it above $30k**

### Source-normalization cautions

- Mazda's current CX-30 destination charge is **$1,595** effective Aug 11, 2026; older third-party pages may still show the previous lower destination charge.
- Niro must always carry a model year: 2026 can fit under $30k; 2027 does not once destination is included.
- Tucson pricing has moved during 2026. Use the current OEM base price and avoid a falsely precise destination-inclusive figure unless rechecked immediately before publication.
- Recheck all new-car prices immediately before WordPress publication.

## 3.5 Used-market evidence format

Claude's nationwide Sep 19 provider-reported matching pools under $30k:

- Nissan Rogue: about **30.1k**
- Toyota RAV4: about **17.2k**
- Subaru Forester: about **14.0k**
- Mazda CX-5: about **12.6k**
- Honda CR-V: **do not publish a national figure from this package** — its run was CA-only

Recommended public presentation:

> **Live-market availability, checked Sep 19, 2026:** CarClever's provider-reported nationwide matching pool found roughly 30,100 used Rogues, 17,200 RAV4s, 14,000 Foresters and 12,600 CX-5s listed at $30,000 or less. Inventory changes continuously, and these counts are availability signals rather than audited market totals.

Do **not** publish the tool's top-five prices as "typical," "median" or "average." The ranking mode deliberately selects near the budget ceiling.

## 3.6 Methodology

Use transparent selection criteria, but avoid an invented numeric score.

Recommended factors:

1. **Budget fit** — can a shopper genuinely find the model under the cap?
2. **Current availability** — is the model available in meaningful volume?
3. **Age/mileage trade-off** — what vehicle age/mileage does the budget typically buy, where sourced reliably?
4. **Fuel/ownership efficiency** — EPA/OEM-backed.
5. **Safety / recall context** — NHTSA/IIHS-backed where appropriate.
6. **Reliability/repair evidence** — only if the source is named and appropriate.
7. **Buyer fit** — space, AWD, family use, commuting, etc.

Do not publish arbitrary unexplained "9.2/10 reliability" style scores.

## 3.7 Content architecture

1. Updated/reviewed date
2. 30-second answer
3. "What $30k buys new vs. used today"
4. Current new-SUV table
5. Current used-market availability snapshot
6. Used candidate blocks — standardized
7. New-vs-used decision table
8. Best choices by buyer job
9. Methodology
10. Source notes
11. Buyer watch-outs
12. Natural CarClever / Edmunds next action
13. FAQs

## 3.8 Monetization

Do not add a dynamic Edmunds inventory module during the content treatment.

Migrate affiliate tracking operationally if required, but keep the **content treatment date** separate from any later inventory/CTA experiment.

---

# 4. Used PHEV — final editorial treatment

## 4.1 URL

Keep:

`/tools/best-used-phev-plug-in-hybrid/`

## 4.2 Proposed title / H1

**Title:**  
`Best Used Plug-In Hybrids (PHEVs) in 2026: What to Buy`

**H1:**  
`Best Used Plug-In Hybrids in 2026: Which PHEV Fits You?`

## 4.3 Core decision question

The page should lead with:

> **A used PHEV is most valuable when you can charge regularly and its electric range covers a meaningful share of your normal driving. If you rarely plug in, the extra battery and powertrain complexity may deliver less benefit than a conventional hybrid.**

This is a decision framework, not a model ranking.

## 4.4 Validated live-availability evidence

Sep 19 provider-reported used matching pools:

| Model | Live matching pool | Role to evaluate |
|---|---:|---|
| Toyota Prius Prime | ~940 | Efficiency / commuter |
| Chrysler Pacifica Plug-In Hybrid | ~623 | Family / minivan |
| Toyota RAV4 Prime | ~488 | All-round SUV |
| Mitsubishi Outlander PHEV | ~315 | AWD / family crossover |
| Kia Sportage Plug-In Hybrid | ~257 | Newer compact SUV |
| Ford Escape Plug-In Hybrid | ~146 | Value/commuter crossover |
| Hyundai Tucson Plug-In Hybrid | ~128 | Newer compact SUV alternative |
| Kia Niro Plug-In Hybrid | ~111 | Efficient small crossover |

The availability counts are useful.

The shortlist prices from this session are **not safe as representative price evidence** because:

- Prius Prime included a likely bad $1,028 listing;
- Niro PHEV included a likely bad $1,199 listing;
- provider anomaly detection did not flag those cases consistently.

Therefore the first rebuild should use availability counts but **not claim typical/median used pricing from this dataset**.

## 4.5 Proposed primary comparison set

Use six main candidates to keep the page decision-focused:

1. Toyota RAV4 Prime
2. Toyota Prius Prime
3. Chrysler Pacifica Plug-In Hybrid
4. Mitsubishi Outlander PHEV
5. Ford Escape Plug-In Hybrid
6. Kia Sportage Plug-In Hybrid

Keep Tucson PHEV and Niro PHEV as "also consider" alternatives unless the source/fact pass reveals a stronger user-job reason to elevate one.

This set covers materially different shopper jobs rather than eight near-identical cards.

## 4.6 Mandatory fields to source before copy is finalized

For the relevant model years of every primary candidate:

- EPA electric-only range;
- EPA charge-depleted/gas-only efficiency;
- battery/hybrid-system warranty;
- powertrain warranty;
- transfer rules for a second owner;
- seating/cargo where decision-relevant;
- AWD/FWD configuration;
- NHTSA recall/safety context;
- reliability/repair evidence only from a named source;
- materially different model-year changes.

Do not use the provider's electrification filter as the population definition.

Use the validated PHEV model-name strings.

## 4.7 PHEV page architecture

1. Updated/reviewed date
2. "Does a used PHEV make sense for you?"
3. 30-second answer
4. Current used-PHEV availability snapshot
5. What matters when buying a used PHEV
6. Six standardized model blocks
7. One comparison table
8. Decision tree:
   - longest electric commuting
   - family/3-row
   - AWD/SUV
   - lower used-price path
   - efficiency-focused
9. Warranty-transfer section
10. Used-PHEV inspection/watch-outs
11. Methodology/source notes
12. Natural used-inventory CTA
13. FAQs

---

# 5. $25k architecture decision

## 5.1 Evidence

`/under-25000/`:

- 122 conventional Search impressions in the Sep baseline;
- 248 words;
- no meaningful H2 structure;
- self-canonical;
- current title explicitly used-focused;
- updated Sep 6;
- no link from `/tools/`.

`/under-25k-comparison/`:

- 5 recent Google Generative AI impressions;
- 822 words;
- structured model sections;
- comparison table;
- Data & Methodology section;
- Article schema;
- self-canonical;
- lastmod Jun 21;
- no link from `/tools/`.

Four of five core models overlap.

Both target essentially the same budget and used-compact-SUV decision.

## 5.2 Recommendation

**Consolidate.**

Retain:

`/tools/best-compact-suv-under-25000/`

Why retain this URL rather than the richer comparison URL:

1. it is already the conventional Search winner;
2. it has the stronger measured demand signal;
3. it is the currently maintained/updated URL;
4. the richer comparison content can be migrated without changing the user's destination;
5. the second page has only a small GEO signal and can be redirected once its useful evidence is transferred.

## 5.3 Required order

Do not redirect first.

1. Capture both current pages.
2. Move the useful comparison structure/methodology into `/under-25000/`.
3. Decide the candidate set and remove contradictory Rogue-vs-Escape split.
4. Add Article/Breadcrumb metadata if accurate.
5. Add `/under-25000/` to the `/tools/` hub.
6. Update other relevant internal links.
7. Verify content parity and source/fact quality.
8. Record GSC SEO/GEO baseline for both URLs.
9. 301 `/under-25k-comparison/` to `/under-25000/`.
10. Request indexing and monitor both Search and Generative AI visibility.

Do not keep two pages merely because both currently index.

---

# 6. 3-row $50k benchmark — minimum correction package

## 6.1 Kia Sorento warranty

Current wording incorrectly/misleadingly implies that a used buyer can rely on the original 10-year/100,000-mile powertrain warranty deep into used ownership.

Kia's U.S. warranty manual defines the 120-month/100,000-mile Power Train Limited Warranty as an **Original Owner** benefit and states it is **not transferable to subsequent owners**.

Authoritative source:
https://www.kia.com/content/dam/kwcms/pr/es/images/owners/warranty-recalls/kia-warranty-manual-en.pdf

### Replacement principle

Replace every "used buyer gets 10/100" implication with wording such as:

> **Warranty note:** Kia's 10-year/100,000-mile powertrain warranty is an original-owner benefit and does not transfer in full to a subsequent owner. Used buyers should verify the remaining warranty coverage for the specific vehicle.

Apply this correction in:

- the Sorento body section;
- the "Why buy" wording if it relies on 10/100;
- the FAQ warranty summary;
- any comparison-table cell that implies the full term transfers.

## 6.2 Ford Explorer XLT engine

The page currently associates the 2021–2022 Explorer XLT with a 3.5-liter EcoBoost.

Ford's official 2021 technical specifications list Base/XLT/Limited with a **2.3-liter EcoBoost I-4**. Ford's 2022 product guide also identifies the Explorer ST-Line with the 2.3-liter EcoBoost and does not support the page's 3.5-liter XLT claim.

Authoritative sources:
- https://media.ford.com/content/dam/fordmedia/North%20America/US/product/2021/explorer/21Explorer_Tech_Specs.pdf
- https://media.ford.com/content/dam/fordmedia/North%20America/US/product/2022/Ford-2022MY-Whats-New-Product-Guide.pdf

### Replacement principle

Replace the XLT engine statement with:

> The 2021 Explorer XLT uses Ford's turbocharged 2.3-liter EcoBoost four-cylinder, rated at 300 horsepower.

For 2022 wording, verify the exact XLT spec in the final page-level source pass rather than extrapolating unsupported trim detail.

## 6.3 Other unsupported claims

Do not mass-delete the other 23 ledger items.

Instead:

- verify sourceable specs during the implementation prep;
- keep claims that can be sourced accurately;
- soften/remove unsourced precision;
- avoid broad reliability scores unless the source and scope are visible.

## 6.4 Protect architecture

Do not change:

- "Best for" labels;
- repeated evidence-card structure;
- Why buy / Watch for pattern;
- comparison table;
- FAQs;
- next-step structure,

except where factual corrections require it.

---

# 7. Internal-link finding — fix regardless of the $25k redirect decision

Neither $25k page currently appears in the main `/tools/` hub's on-page links.

That is a clear discoverability/internal-authority weakness.

Even before any redirect, the final retained $25k guide should have:

- a descriptive link from `/tools/`;
- contextual links from $30k;
- links from relevant used SUV/value content;
- one clear reverse link where it helps the reader.

Do not create sitewide footer spam.

---

# 8. PHEV provider quirk — engineering follow-up decision

The PHEV model-name result is now empirically clear:

- base model + required PHEV filter returned zero for RAV4, Sportage and Tucson;
- explicit model variants (`RAV4 Prime`, `Sportage Plug-In Hybrid`, etc.) returned real populations.

This is relevant to CarClever's future PHEV behavior, but it does **not** require interrupting the current SEO/GEO work.

The existing V1 tool description already contains special hybrid/PHEV model-name handling.

Recommendation:

> **Do not open a new app-engineering task solely from this SEO investigation unless real user testing shows the existing model-resolution instructions fail.**

Record it as a known provider/query semantic constraint, not an urgent defect.

---

# 9. What to implement first after André approves

## Batch 1 — low-risk factual/architecture prep

1. Correct 3-row Sorento warranty wording.
2. Correct Explorer XLT engine wording.
3. Add the final retained $25k page to `/tools/`.
4. Capture both $25k page baselines before consolidation.

## Batch 2 — primary content experiment

5. Refresh $30k page using the evidence-first structure.
6. Request recrawl.
7. Start T+14 / T+28 / T+56 measurement.

## Batch 3 — full rebuild

8. Rebuild PHEV after the authoritative EPA/OEM source table is complete.
9. Request recrawl.
10. Measure separately.

## Batch 4 — $25k consolidation

11. Merge the richer comparison content into `/under-25000/`.
12. Verify.
13. Redirect the comparison URL.
14. Monitor Search and Generative AI movement.

Keep monetization/inventory UI experiments on separate dates.

---

# 10. Approval status

André explicitly approved the four editorial directions on 2026-09-19:

- $30k controlled evidence-led refresh;
- PHEV evidence-led rebuild;
- $25k consolidation into `/tools/best-compact-suv-under-25000/`;
- minimal factual/source correction of the 3-row benchmark.

The subsequent multi-source value cross-check is complete and did not overturn those directions. It **did** tighten the $30k new-vehicle eligibility rule to require starting price including destination.

Implementation should now be prepared in controlled batches, with pre-change baselines preserved and new monetization/inventory-module experiments kept on separate dates.

