# Handoff to ChatGPT lane — SEO/GEO content and brand strategy (Oct 6, 2026)

**From:** Claude (Engineering). **To:** ChatGPT (Business/Strategy). **Status:** PROPOSED brief; André approved handing this lane's items to ChatGPT on Oct 6, 2026. Each item below needs André's confirmation before publishing. Claude implements on the live site once an item is confirmed.
**Read first:** `ANALYSIS_SEO_GEO_DIAGNOSIS_AND_ACTION_PLAN_20261006.md`, `IMPLEMENTATION_LOG_SEO_GEO_20261006.md` plus `_PART2` and `_PART3`, and `HANDOFF_CHATGPT_THIN_PAGES_EXPANSION_BRIEF_20261006.md` (separate task).

## Evidence to build on (all from Oct 6 reads; windows differ, treat as directional)
- **Head terms are unwinnable for now:** "SUV under $X" queries average position about 31 with 0 clicks; the top results are JD Power, KBB, Road & Track, Jalopnik, USA Today. Semrush Authority Score is 2.
- **Question and AI-tool queries are where we rank:** 39 natural-language queries average position 7.1 (e.g. "tools that use ai to compare used cars?" at 3.5).
- **Bing/Copilot cites us heavily:** about 1.1K citations since Jul 6. Most-cited pages: the True Cost of Ownership post (200), the used-car-listing red-flags post (173), the old $25k comparison URL (144, now a 301), the $30K sedan comparison (100), the `/tools/` hub (89). Top cited queries: "red flags in used car listings" (65), "AI tools to compare used cars" (26), "how car listing sites calculate good deal price" (23), "vehicle total cost of ownership components" (21).
- **Brand collision:** a web search for "getcarwise" returns unrelated Carwise/beCarWise businesses; the ChatGPT app directory listing for CarClever does rank for the brand.
- **Real Google search traffic is tiny** (about 55 Google sessions in 30 days). Judge success by AI citations and impressions first, clicks later.

## Items (priority order) — each is a content/strategy decision for ChatGPT to draft
1. **"Best AI tools for buying a used car (2026)" pillar.** Honest comparison of CarGurus, TrueCar, Cars.com, Edmunds, Autotrader and CarClever, built on the existing "We Tested CarClever" post. Question-led headings, direct answers first, sourced claims only.
2. **Explainer expansion in the style that earns citations.** New posts or sections on: red flags in listings, how deal prices are calculated, total cost of ownership components (insurance, maintenance, depreciation, financing). Reuse the format of the two most-cited posts.
3. **Original data series.** A monthly "new vs used availability and price gap" analysis from live inventory, pitched for links. Respect data limits (Auto.dev Starter about 1,000 calls/month; check `DECISIONS.md` and `REFERENCE.md` for current limits).
4. **Brand and entity plan.** Decide the naming rule (CarClever = product, GetCarWise = publisher); list real profiles for Organization `sameAs`; directory listings that are genuinely applicable. Claude adds the schema once the profile list is confirmed.
5. **Reddit plan** (existing ChatGPT-lane item) aligned with items 1–3.

## Hand-off process
- ChatGPT writes each item as a separate getcarwise-docs file `DRAFT_<TOPIC>_<DATE>.md`, labelled "proposed, pending André confirmation". No code, no publishing.
- André confirms; Claude publishes, adds schema, links it from the hub/related guides, verifies live, requests indexing and logs it.
- Measure at about 4 weeks: Bing AI Performance citations, GSC impressions and position, Clarity/GA4 usage.

## Rules for drafts
- Every statistic needs a source; unsourced figures are left out. No invented quotes or credentials. Author is André Broekman.
- Do not touch the four protected Task #78 pages (`/tools/best-compact-suv-under-25000/`, `-under-30000/`, `/tools/best-midsize-sedan-under-40000/`, `/tools/best-3-row-suv-under-50000/`).
- Do not put JSON-LD in drafts; Claude adds it as single-line JSON.
