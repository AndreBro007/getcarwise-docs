# Google Search Console — US Organic Search Baseline

**Date:** 2026-09-16  
**Owner lane:** ChatGPT — Business/Strategy  
**Status:** Baseline analysis complete from André's US-only 28-day GSC Search Performance export.

## Scope

Source: Google Search Console → Performance → Search results

Filters:
- Search type: Web
- Date: Last 28 days
- Country: United States

## Headline baseline

- **27 clicks**
- **1,529 impressions**
- **1.77% CTR**
- **19.54 average position**

### Trend within the 28-day window

- First 14 days: 6 clicks / 644 impressions
- Most recent 14 days: 21 clicks / 885 impressions
- Click growth between halves: **+250%**
- Impression growth between halves: **+37%**
- Average daily reported position improved from about **23.1** to **16.7** across the two halves

Latest weekly comparison:
- Previous 7 days: 8 clicks / 453 impressions
- Latest 7 days: 13 clicks / 432 impressions
- Clicks increased about **62.5%** while impressions were slightly lower, suggesting better recent click capture rather than simple impression growth.

Treat average-position trends directionally because GSC aggregates many queries, devices and result contexts.

## Device mix

| Device | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| Desktop | 15 | 956 | 1.57% | 23.44 |
| Mobile | 12 | 565 | 2.12% | 13.11 |
| Tablet | 0 | 8 | 0% | 6.88 |

Mobile visibility is materially stronger by average position and CTR than desktop despite fewer impressions.

## Highest-impression pages

| Page | Clicks | Impressions | CTR | Avg position | US GenAI impressions |
|---|---:|---:|---:|---:|---:|
| `/tools/best-used-phev-plug-in-hybrid/` | 0 | 136 | 0% | 43.07 | 1 |
| `/tools/best-compact-suv-under-25000/` | 0 | 122 | 0% | 38.28 | 0 shown |
| `/` | 3 | 48 | 6.25% | 21.08 | 28 |
| `/tools/` | 0 | 44 | 0% | 17.64 | 50 |
| `/tools/best-3-row-suv-under-50000/` | 0 | 41 | 0% | 19.71 | 78 |
| `/tools/best-compact-suv-under-30000/` | 0 | 21 | 0% | 26.05 | 3 |
| `/tools/best-full-size-truck-towing-f150-silverado/` | 0 | 20 | 0% | 65.35 | 1 |
| `we-tested-carclever-against-web-search...` | 0 | 13 | 0% | 9.54 | 0 shown |
| `/tools/best-hybrid-suv-under-20000/` | 0 | 13 | 0% | 32.00 | 0 shown |
| `/tools/best-used-electric-car-ev/` | 0 | 11 | 0% | 53.45 | 1 |

## Key finding 1 — P1 remains justified, but GSC and Ubersuggest measure different things

The under-$30k SUV page has:
- GSC: 21 US impressions, 0 clicks, average page position 26.05 across all queries/devices/dates represented in this export.
- Ubersuggest previously reported the specific query `best suv under 30000` around position #13 with 880 US searches/month.

These figures are not contradictory. GSC's page-level average position blends every query and result context for the page, while Ubersuggest reports an estimated position for one tracked keyword. The exact high-volume query is not visible in the GSC query export, which can occur because Search Console omits/anonymizes some low-volume query data.

P1 should therefore continue to target the specific high-value query cluster while using GSC page-level impressions/clicks as the outcome measure.

## Key finding 2 — the PHEV and $25k SUV clusters have demand but are still too deep

The two highest-impression non-brand content pages are:
- Used PHEV: 136 impressions, position 43.07, 0 clicks
- SUV under $25k: 122 impressions, position 38.28, 0 clicks

This confirms real search demand but also shows why they are not the first optimization target. They need larger content/authority gains than the under-$30k and 3-row pages.

The query export reinforces the pattern:
- `best phev`: 58 impressions, position 38.19
- `best used phev cars`: 27 impressions, position 46.41
- `suv under 25000`: 29 impressions, position 41.83
- `suvs under 25000`: 29 impressions, position 43.72

These remain important P5/P6 opportunities after nearer-page-one wins.

## Key finding 3 — the 3-row page has unusually strong AI exposure relative to organic rank

`/tools/best-3-row-suv-under-50000/`:
- Organic: 41 impressions, 0 clicks, average position 19.71
- Generative AI: 78 impressions

Its AI-feature exposure is substantially stronger than its current conventional organic footprint. This remains the strongest internal GEO case study and should be analysed for reusable content structure, sourcing and intent coverage.

Relevant conventional queries include:
- `best 3 row suv under 50k`: 8 impressions, position 23
- `3 row suv under 50000`: 4 impressions, position 17.75
- `compare 3-row suvs under $50,000`: 4 impressions, position 7.75

## Key finding 4 — the tools hub is strategically valuable

`/tools/`:
- Organic: 44 impressions, position 17.64, 0 clicks
- Generative AI: 50 impressions

This supports preserving and strengthening the hub's descriptive navigation/internal-link role. It is already visible in both conventional and AI search even though click volume has not started.

## Key finding 5 — several page-one/near-page-one queries are emerging

Visible zero-click query opportunities include:
- `automotive evaluation platform`: 18 impressions, position 8.83
- `does cargurus use ai to rank the best deals for me?`: 13 impressions, position 9.54
- `best midsize sedan 2023`: 6 impressions, position 6.67
- `compare 3-row suvs under $50,000`: 4 impressions, position 7.75
- several AI appraisal/finder long-tail queries in positions 2–10 with small volume

These are too small individually to outrank P1, but they are useful evidence that Google is beginning to associate GetCarWise with AI-assisted automotive evaluation/comparison intent.

## Query-export limitation

The visible query table accounts for only **8 clicks and 530 impressions**, compared with the property's total **27 clicks and 1,529 impressions**. This is normal Search Console privacy/anonymization behavior and means the query table is incomplete.

Do not infer that unlisted queries generated zero traffic or that visible query rows fully explain page totals.

## Combined SEO + GEO implications

1. Continue the under-$30k SUV page refresh because it has a specific tracked keyword closer to page one than the site's high-impression PHEV/$25k clusters.
2. Use the 3-row $50k page as an internal GEO architecture case study, but do not assume its AI performance proves causation from any single feature.
3. Preserve and strengthen `/tools/` internal linking because it already has meaningful organic and AI visibility.
4. Keep PHEV and $25k as second-wave content projects: demand is confirmed, but current positions are mostly 35–46.
5. Investigate CTR/title/snippet opportunities for pages/queries already in positions roughly 5–10 once impression volume is sufficient.
6. Re-measure the same US 28-day organic and Generative AI reports after meaningful content changes rather than reacting to daily fluctuations.

## Measurement baseline to retain

Organic US 28-day baseline:
- Clicks: **27**
- Impressions: **1,529**
- CTR: **1.77%**
- Average position: **19.54**
- Latest 14 days: **21 clicks / 885 impressions**
- Previous 14 days: **6 clicks / 644 impressions**

Generative AI US 28-day baseline from companion analysis:
- Total AI impressions: **190**
- `/tools/best-3-row-suv-under-50000/`: **78**
- `/tools/`: **50**
- homepage: **28**
- `/tools/best-compact-suv-under-30000/`: **3**
