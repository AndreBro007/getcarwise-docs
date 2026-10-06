# Handoff to ChatGPT lane — expand three thin guide pages (Oct 6, 2026)

**From:** Claude (Engineering). **To:** ChatGPT (Business/Strategy, content). **Status:** PROPOSED brief; André chose "expand to 1,000+ words" (A5 option 1) on Oct 6, 2026. Content is drafted by ChatGPT; Claude publishes and verifies on the live site. Context: `ANALYSIS_SEO_GEO_DIAGNOSIS_AND_ACTION_PLAN_20261006.md` (section 2c) and the implementation logs of the same date.

## Pages (all non-protected; none is in the Task #78 protected cohort)
| Page | WordPress ID | Words now (Oct 6 crawl) | GSC US impressions, 28d |
|---|---:|---:|---:|
| `/tools/best-hybrid-suv-under-20000/` | 936 | ~158 | 47 |
| `/tools/best-used-electric-car-ev/` | 938 | ~186 | 19 |
| `/tools/best-sedan-under-15000/` | 935 | ~153 | ~8 (parsed from a concatenated GSC row; verify) |
Priority order: hybrid SUV, used EV, then sedan.

## What "good" looks like (acceptance criteria)
- **Length and substance:** at least ~1,000 words of useful, non-repetitive content; unique data or analysis, not generic filler. Name specific models, years, price ranges, known reliability or ownership-cost points, and what a buyer should check.
- **Question-led structure:** H2s phrased as the questions buyers ask, each opening with a 40–60-word direct answer, then detail. This matches the question-style queries the site already ranks for (average position 7.1).
- **Sources and honesty:** cite sources for any statistic; if a figure cannot be sourced, do not include it. No invented numbers, quotes or credentials.
- **Freshness:** include a visible "last updated" date. Author is André Broekman (WordPress user ID 1), never `claude-automation`.
- **Internal links:** link to the relevant pillar guides and tools (e.g. `/tools/best-compact-suv-under-30000/`, `/tools/used-car-true-cost-ownership/`, `/tools/vin-check/`, `/tools/deal-score/`, `/tools/`).
- **Do not** put JSON-LD in the draft text. Claude adds schema as single-line JSON (multi-line JSON-LD was corrupted by WordPress `<br />` insertion on page 827 on Sep 28).
- Keep the existing titles and meta descriptions (rewritten Oct 6) unless a stronger version is proposed in the same document.

## Hand-off process
1. ChatGPT writes each draft as a separate getcarwise-docs file named `DRAFT_<PAGE>_<DATE>.md` (plain markdown, headings as H2/H3, no HTML needed).
2. André reviews and confirms each draft (label: proposed, pending André confirmation, confirmed).
3. Claude publishes the confirmed draft to the live page via WordPress, adds schema, verifies title/H1/links/JSON-LD on the live page, requests re-indexing, and logs it.
4. Measure after about 4 weeks (GSC impressions, position, clicks for each page); do not judge earlier.

## Constraints to respect
- Data limits changed on Oct 1, 2026 (SYS-20261001-001): Auto.dev is now the free Starter plan (about 1,000 calls/month). Check `DECISIONS.md` and `REFERENCE.md` for current limits (I did not re-verify them here) and do not plan content that needs more live-inventory calls than that.
- Do not touch the four protected pages (`/tools/best-compact-suv-under-25000/`, `-under-30000/`, `/tools/best-midsize-sedan-under-40000/`, `/tools/best-3-row-suv-under-50000/`).
