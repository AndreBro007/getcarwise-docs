# SEO/GEO Implementation Log — Part 9 (Oct 6, 2026)

**Continues** `IMPLEMENTATION_LOG_SEO_GEO_20261006_PART8.md`. Owner lane: Claude — Engineering.

## CarClever Lite: Impact Shared ID tagging — DONE (carclever-widget PR #73)
- **Finding:** the Lite tool embedded in the guides is the Next.js app at `carclever-widget.vercel.app/carclever-lite` (WordPress page `/carclever-lite/` iframes it). Every result card already has a full-width "Check Availability ↗" button with an Impact deep link to the exact vehicle's Edmunds listing (`edmunds.sjv.io/c/7765200/3949600/52125?u=<exact VIN listing URL>`) and a "Paid link" disclosure; the vehicle modal has the same link. Missing was a Shared ID, so Lite clicks were not separable in Impact.
- **Change:** `app/chat/utils/affiliate-links.ts` only: `buildEdmundsAffiliateUrl(vehicle, placement='result')` now adds `sharedid=lite_<placement>` before `u=`; `isValidAffiliateUrl` regex accepts the optional prefix. Call sites unchanged (default `lite_result`). Shared ID is a fixed label (sanitized), never user data.
- **Process:** branch `feature/lite-impact-sharedid`; PR #73 created by André (the connector's PR tool requires human confirmation); Vercel preview Ready; Codex bot review completed with no findings; squash-merged by Claude (commit `1e6e4ed`). The Vercel project is not one of the three gated MCP domains.
- **Verified:** after the production build finished, the live bundles at `carclever-widget.vercel.app` contain the `sharedid=lite_` code (a live search run before the build finished still showed no tag; one Auto.dev search call was used for that test).
- **Measure:** Impact > Reports > More Reports > Performance by Sub ID and Shared ID; Shared ID `lite_result` = clicks from the Lite tool.

## AI-tools guide published — DONE (post 1469)
- **URL:** https://getcarwise.app/best-ai-tools-for-buying-a-used-car-2026/ ; title "Best AI Tools for Buying a Used Car in 2026"; Rank Math title 56 chars, description 148 chars; author André Broekman (ID 1); category as the other guides (ID 113); ~1,970 words; 9 question headings with single-line FAQPage JSON-LD; comparison table (8 tools); affiliate disclosure at the top.
- **Source:** ChatGPT's `DRAFT_BEST_AI_TOOLS_USED_CAR_BUYING_2026_20261006.md`, revised twice after Claude's reviews (internal notes removed, links verified, CarGurus fee policy updated to "in effect since July 14, 2026" per the CarGurus dealer update, Lite link changed to `/carclever-lite/`, CarClever product distinctions added). André approved publishing.
- **Claude's checks:** the June test details (prompt, Los Angeles, under $35,000, Auto.dev source, results described) match the published post (published June 21, 2026); CarGurus fee policy confirmed from CarGurus's own update; ChatGPT confirmed the TrueCar, Cars.com, Autotrader, ChatGPT app and CFPB links load (not independently re-checked by Claude).
- **Edits at publish:** removed the "Proposed" line and the production note; both Edmunds links use the Impact Used link, `rel="nofollow sponsored noopener"`, tagged `ai-tools-guide_sources` and `ai-tools-guide_cta`; added a "Browse Used Cars on Edmunds" button at the end.
- **Linked from:** `/tools/` hub (page 452, new list item) and the "We Tested CarClever" post (809, Related buying guides). Removing the added items restores both originals exactly.
- **Live check:** disclosure, byline, table, 2 sponsored Edmunds links, FAQ schema and all JSON-LD valid; no draft labels.
- **Incident:** a first publish attempt failed with a 403 cookie/nonce error (host rate limiting after many requests; cleared by a normal page visit). Nothing was created by the failed attempts; the post was created once.

## Still open
Google re-indexing requests (935, 936, 938 and the new post 1469); review of four remaining strategy drafts (explainer cluster, new-vs-used series, brand/entity plan, Reddit plan); TASKS.md and DECISIONS.md splits.
