# AUDIT_WEBSITE_APP_INFRASTRUCTURE_20260902.md — WordPress Endpoint Audit (Technical Facts Only)

**Status:** Technical facts only — no messaging/strategy recommendation (that's ChatGPT's lane per lane split)
**Prepared by:** Claude Team (engineering lane), Sep 2, 2026
**For:** André, to bring to ChatGPT for design/strategy pass on Items 2-5 + website messaging
**Source checklist:** TASKS.md WordPress Endpoint Audit section, referencing `AUDIT_WEBSITE_APP_INFRASTRUCTURE_20260826.md` (getcarwise-docs)
**Method:** WordPress.com MCP connector returned all read/write ops disabled (site lacks a paid Jetpack plan). Fell back to public page fetches (web_search to locate URL, then web_fetch) for 7 of 8 pages. Reads live rendered HTML, not the WP REST API/draft content.

---

## Findings by page

| Page | ID | Question from TASKS.md | Finding |
|---|---|---|---|
| CarClever Lite | 239 | Already Vercel Find My Car? | **No.** Embeds `carclever-widget.vercel.app/carclever-lite`. Still on old Fractal backend. |
| Deal Score | 453 | Widget or standalone tool? | Embeds `carclever-widget.vercel.app/tools/deal-score`. Same app family as Lite. |
| Price Check | 527 | Widget or standalone tool? | Embeds `carclever-widget.vercel.app/tools/price-check`. Same app family. |
| VIN Check | 1023 | Confirm Vercel endpoint | Embeds `carclever-widget.vercel.app/tools/vin-check`. Same app family. |
| Tools Hub | 452 | Check for embeds/links | Links to all 4 web apps above, plus 3x "@CarClever on ChatGPT" links (old Fractal ChatGPT app). Zero mentions or links to Find My Car or Claude anywhere on the page. |
| Try CarClever | 38 | Endpoint TBD, stale copy? | Confirmed stale, matches the Aug 26 audit exactly: "⚠️ App Status: Live on ChatGPT @CarClever", "Claude (Coming soon)". No update since Find My Car was submitted to Anthropic. |
| Homepage | 7 | Check for CarClever mentions | **New since Aug 26 audit:** headline already reads "The Only Independent AI Evaluating **Cars**" — the word "Used" has already been dropped (Aug 26 doc quoted it as "...Evaluating Used Cars"). Someone made this edit between Aug 26 and Sep 2; not reflected in the prior audit doc. Homepage links go to the ChatGPT app + `/try-carclever/` — no Claude/Find My Car link. |
| CarClever Guide | 1053 | Repoint to Find My Car once ready | **Not verified this session** — could not reach via web_search + web_fetch. Still open for a future session with direct WP access (or once Jetpack plan is active for MCP connector use). |

## Bottom line (facts only)

All four web-app tools (Lite, Deal Score, Price Check, VIN Check) run on `carclever-widget`'s own Vercel deployment. None of the 8 audited pages link to Find My Car or provide a Claude entry point anywhere on the site. The homepage headline has already changed since the Aug 26 audit in a way that document didn't anticipate — worth checking with André whether that edit was intentional/who made it.

---

## Related: CarClever Lite backend-switch code investigation

André separately asked whether CarClever Lite's code could be switched from the old Fractal MCP server to Find My Car. Full findings logged in `carclever-widget/DECISIONS.md` DECISION-20260902-011. Summary:

- Only Lite is MCP-backed (`app/api/chat/route.ts`, hardcoded to Fractal's `carclever` server). Deal Score/Price Check/VIN Check call Auto.dev directly — no MCP involved, correcting an earlier assumption.
- Find My Car's live MCP server exposes only 2 tools (`find_matching_vehicle`, `resolve_dealer_url`) vs. Fractal's 7+ (`search-used-cars`, `analyze-deal-risk`, `calculate-affordability`, `vehicle-comparison`, `get-vehicle-details`, `garage-*`).
- Lite's system prompt is written entirely around Fractal's tool contract. A URL swap alone would break it — the prompt references tools that don't exist on Find My Car.
- This ties directly to the paused Items 2-5 (DECISION-20260902-010): Lite can't cleanly move to Find My Car until risk/affordability/comparison exist there, or until Lite's scope is deliberately reduced to search + dealer-link only. Flagging as a factor for the ChatGPT design conversation, not resolving it here.

**Next step:** André to take this + the DECISIONS.md entries to ChatGPT for the design/strategy pass on Items 2-5, which will also inform what Lite's future backend contract needs to look like.
