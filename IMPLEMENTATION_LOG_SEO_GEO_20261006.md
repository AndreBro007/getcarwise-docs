# SEO/GEO Implementation Log — Oct 6, 2026

**Owner lane:** Claude — Engineering. Implements Tier A items 1–2 of `ANALYSIS_SEO_GEO_DIAGNOSIS_AND_ACTION_PLAN_20261006.md`. Approved by André in chat (schema fix on protected page 827; internal-link rebuild). All edits via WordPress REST in André's logged-in browser session, each guarded by a "page unchanged since read" check and verified by reading the stored content back.

## A1 — JSON-LD repair, page 827 `/tools/best-compact-suv-under-30000/` — DONE
- **Cause:** the ItemList and FAQPage `<script type="application/ld+json">` bodies had `<br />` tags stored in the page content itself, making them invalid JSON (Google: "Unparsable structured data — Incorrect value type").
- **Change:** removed the `<br />` debris and rewrote each body as single-line JSON. Nothing outside the two script bodies changed (verified: stripping the script bodies from old and new content gives identical text). Content length 21,451 → 20,757 chars.
- **Verified:** stored content equals the intended content; the live page now serves 3 valid JSON-LD blocks (ItemList 7 items, FAQPage 4 questions); title, H1, canonical and word count (~2,387) unchanged; no `<br>` inside any JSON-LD.
- **Google:** "Request indexing" submitted in GSC URL Inspection ("Indexing requested", priority crawl queue). GSC's structured-data status will update after the re-crawl (not yet verified).
- **Side effect:** the page's modified date changed to Oct 6 (Rank Math `dateModified`). **Rollback:** WordPress revision of page 827 (pre-change version).

## A2 (part 1) — `/tools/` hub (page ID 452) now links every guide — DONE
- **Change:** appended an "All GetCarWise buying guides" section (H2 + two lists, 28 links: 12 buying guides incl. the $30k and 3-row $50k pages, 16 used-model guides). Existing text untouched (new content = old content + appended section). Anchor text = each page's own H1.
- **Verified (page rendered in browser):** in-content internal links on `/tools/` rose from 8 to 35 unique; all four protected pages plus the PHEV, hybrid, truck and CR-V pages are linked; no stray `<br>` in lists. Rollback: WordPress revision of page 452.
- **No protected page content was edited** — links point TO them from the hub.

## Still to do (not started)
A2 part 2: Guides links in site navigation/footer; blog post to pillar links; vehicle page to pillar links. A3 author byline; A4 titles/metas (~25 pages, protected four excluded); A5 thin pages; A6 llms.txt; A7 own-traffic exclusion; A8 crawler-access check. Strategy items (Tier B) are ChatGPT-lane first.

## Notes
- Mistake logged: fetching 28 pages in parallel from the browser tripped the host's anti-bot challenge ("Checking your browser…" 403) for scripted requests from my sandbox and browser. Normal page navigation passes it. Avoid bursts; space requests.
- STATE.md update is still pending (file too large for the connector; GitHub web-editor save hung). Checkpoints unchanged.
