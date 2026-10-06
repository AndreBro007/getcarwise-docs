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

## A3 — Author reassigned (Oct 6, later) — DONE (schema author); visible byline NOT yet added
- **Change:** author of all 32 published items previously attributed to the `claude-automation` WordPress user (31 pages incl. the four protected pages and the `/tools/` hub, plus 1 post) set to André Broekman (user ID 1) via REST, one item at a time; every response returned author = 1. Result: 0 items left on `claude-automation`; 58 items under André. Only the author field was sent. Page modified dates changed to Oct 6 (no content changed).
- **Verified:** live `/tools/best-compact-suv-under-30000/` JSON-LD names Andre Broekman (Person + author), 3 of 3 blocks valid, no `claude-automation` anywhere in the page.
- **Bio:** André's existing WordPress bio (257 chars: founder of GetCarWise, built CarClever, "research and transparency, not selling cars") was left unchanged; his approved alternative text was NOT applied. His choice which to use.
- **Open:** the theme shows no visible byline/author box on these pages; adding one is a theme/block task (not started).
- **Mistake logged:** the REST saves are slow (~4 s each); two long scripts timed out mid-batch and the host's anti-bot challenge appeared. All 32 were verified afterwards by re-querying the author filter, not by trusting the responses.

## STATE.md split (Oct 6, later) — DONE
- STATE.md (430,126 bytes) split on André's instruction (Option 1: PAT used once in bash, visible in that tool call; the local token file was deleted afterwards and no file contains it). **Rotate the carclever-widget PAT.**
- Archive `STATE_ARCHIVE_2026-08-02_to_2026-09-18.md` (266,181 bytes) holds original lines 743–774 and 834–2772 verbatim; live STATE.md is 180,555 bytes (keeps banner, checkpoints, 🔴 gate section, everything from Sep 19). Archive and live file were byte-verified against local copies after upload.
- **Nothing lost:** rebuilding the original from the repo's live file + archive reproduces the pre-split file byte-for-byte (blob `1d8664c209873ca81a13a59550f56d8cefd17d78`), proven twice (local build and repo copies). An archive notice in STATE.md lists older open items carried forward (status not re-verified).
- PLAYBOOK.md: one line added (startup item 2b about the archive); diff confirms nothing else changed.
- STATE.md now also holds the Claude Oct 6 entry and the Claude widget checkpoint `183554b` (docs checkpoint held at `4fe2e15`).
