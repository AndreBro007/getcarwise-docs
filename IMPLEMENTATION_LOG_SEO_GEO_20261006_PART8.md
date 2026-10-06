# SEO/GEO Implementation Log — Part 8 (Oct 6, 2026)

**Continues** `IMPLEMENTATION_LOG_SEO_GEO_20261006_PART7.md`. Owner lane: Claude — Engineering. André approved "stronger buttons" for the Edmunds links.

## Edmunds primary link turned into a button on 19 pages — DONE
- **Pages:** the 16 used-model guides (WordPress IDs 755, 749, 757, 741, 742, 752, 751, 756, 739, 740, 750, 738, 769, 758, 753, 754) and the hybrid SUV, used EV and sedans-under-$15k guides (936, 938, 935).
- **Change:** the first Edmunds link on each page (placement tag `_top` / `cta-top`) is now a centered button using the exact style already on the site's CarClever button (blue `#2563eb`, white text, 14px/28px padding, 6px radius, bold) with a lead line above it ("Ready to see what is for sale?") and an arrow after the label. The disclosure sentence still appears before it. The closing links stay plain text. Link addresses, tags and `rel="nofollow sponsored noopener" target="_blank"` unchanged: every page keeps the same number of Edmunds links (3 on model guides; 6, 5 and 7 on the hybrid, EV and sedan guides), all sponsored.
- **Verified:** stored content equals intended for all 19 pages; live render checked on the 2022 Camry guide (button directly after the first section) and the hybrid SUV guide (button directly below the CarClever tool; all 6 Edmunds links present). A transient browser error page appeared once on the hybrid guide; the page itself returned HTTP 200 with correct content and recovered on reload.
- **Rollback:** WordPress revisions of each page; or replace the two centered paragraphs with the earlier single paragraph.
- **Measure:** compare click counts by Shared ID in Impact (Reports > More Reports > Performance by Sub ID and Shared ID) for `_top` versus `_end-used` links; the button change date is Oct 6, 2026, so compare before and after it.

## Not done / next
- Edmunds link inside CarClever Lite results (app change in the widget code; needs a separate look at the app's existing CTAs) — proposed.
- Google re-indexing requests for 935, 936, 938; review of four remaining strategy drafts; revised AI-tools guide from ChatGPT; TASKS.md and DECISIONS.md splits.
