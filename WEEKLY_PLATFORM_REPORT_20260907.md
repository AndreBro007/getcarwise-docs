# Weekly Platform Report — Sep 7, 2026 (Brisbane)

**Run by:** Claude, Engineering lane (via MCP tools + Chrome, per André's explicit routing this session — ChatGPT lacks these direct tool/API/browser connections). Reddit excluded per instruction (AI-restricted).

**Baseline for comparison:** the Sep 1-2, 2026 full marketing/admin check recorded in STATE.md.

---

## 1. Google Analytics 4 (28 days, Aug 10–Sep 6, 2026)

- **Active users:** 34 US, 6 AU, 5 Spain, 2 Canada, 1 Brazil, 1 India, 1 Iraq — 50 total across 7 countries.
- **Top city:** Brisbane (6), then Ashford (3), Los Angeles (3).
- **Events:** page_view 106, user_engagement 74, session_start 71, first_visit 50, scroll 38, click 23, form_start 5.
- **Engagement:** avg 26s/active user, 0.69 engaged sessions/active user.
- **Top pages:** "Used Car Research & AI Deal Scoring" (21), "Car Research & Deal Scoring" (14), "CarClever User Guide" (9), "Used Car Research Tools" (9).

No red flags. Broadly consistent with the Sep 1-2 read (that was a 7-day window showing 10 active users; this 28-day window naturally shows more).

## 2. Google Search Console (3 months)

- **Totals:** 60 clicks / 5.36k impressions / 1.1% CTR / avg position 27.9.
- **Top queries:** carclever (3 clicks/51 impr), getcarwise (3/40), car clever (3/16), best small suv under 30k (1/20).
- **Correction to an initial read of this data:** the zero-click pattern below was flagged Sep 1-2 and looked unresolved in this 3-month GSC pull — **but TASKS.md #49/#51 confirm the fix (new title + meta + CJ link) was already shipped live Sep 3** on the single page these 4 queries all resolve to (`/tools/best-compact-suv-under-30000/`, id 827):
  - "best suv under 30000" — 337 impressions, 0 clicks (3-month aggregate)
  - "suv under 30000" — 188 impressions, 0 clicks
  - "best suvs under 30000" — 152 impressions, 0 clicks
  - "suvs under 30000" — 108 impressions, 0 clicks
- These are 3-month rolling totals, so they're still dominated by the ~2.5 months of pre-fix history; a handful of post-Sep-3 days can't move the aggregate yet. **This is not a missed fix — it's too early to read click impact from the aggregate view.** Next check should pull a Sep 3-onward date-filtered range specifically to see if the new snippet is earning clicks.
- **What's genuinely still open:** TASKS.md #50, the site-wide audit for other pages with the same pattern — sent to ChatGPT Sep 3, still marked "awaiting audit list" as of this check.

## 3. Microsoft Clarity (7 days)

- **Sessions:** 34, unique users 22 (67.65% new / 32.35% returning).
- **Dead clicks:** 14.71% (5 sessions) — up from the Sep 1-2 reading (6.67%, small sample) but still well under the historical 42.86% baseline flagged back in Aug. Not urgent, worth watching.
- **Rage clicks:** 0%. **Quick backs:** 5.88%.
- **AI Visibility (Copilot + partners):** Share of Authority **24.90%** (61 citations vs. 184 others) — **up from 18.33% at the Sep 1-2 check.** Top grounding queries: "ai-powered car shopping how it works" (6 citations, 37.5% SoA), "vehicle total cost of ownership components" (4, 14.29%), "suv with 3 rows and costs under 50k in wi" (4, 100%).
  - This is a genuine positive trend worth flagging to André/ChatGPT — AI-assistant discovery is growing faster than traditional search clicks.

## 4. CJ Affiliate (This Year)

- **Commission: $20, 2 leads, 0 sales** — unchanged since Sep 1-2. Both leads are historical (Aug 14: $10/12 clicks/8.30% conv; Aug 27: $10/4 clicks/25% conv). **No new commission activity in the past week.**
- Confirms the CJ Program Terms finding: leads (not sales) are the paying event.

## 5. WordPress / Rank Math (30 days)

- **SEO totals:** 971 impressions, 6 clicks, 276 tracked keywords (+74 vs. prior period), CTR 0.62% (+0.39), avg position trend: 1 in top-3, 3 in positions 4-10, 30 in positions 10-50 (+21 — the "positions improving but not converting to clicks" pattern, consistent with GSC).
- **404 Monitor:** 19 logged entries, all identifiable as bot/vulnerability-scanner probes (`wp-content/plugins/pwnd.php`, `staging/phpinfo.php`, `worksec.php`, `.well-known/security.txt`) — **not real broken internal/external links.** No action needed; this is normal background scanner noise for any public WordPress site.

## 6. Semrush

- **Semrush Rank:** 14,762,795 (improved from 15,006,413 at last check).
- **Organic keywords:** 44 (up from 35).
- **🟢 Referring domains: 56** (via Backlinks Overview, `domains_num`) — **up from 27 at the Sep 1-2 check, and past the Sep 30 traction-gate target of 40.** Authority Score 6, 70 total backlinks, 41 referring IPs.
  - **Flagging for verification, not treating as certain:** this is a large jump (27→56) in about a week. Worth an independent sanity check (e.g., pull the actual referring-domains list next session) before formally declaring the Sep 30 traction gate met — could be a real link-building win or a Semrush re-crawl/counting change.
- **Top organic keywords** (by traffic rank) all sit in position 25-57 — e.g. "best small suv under 30k" (pos 31), "compact suv under 25000" (pos 29), "suv under 25000" (pos 44). None are page-1. This corroborates the GSC zero-click finding: the site is indexed and ranking in the 20s-50s for its target terms, but not high enough yet to earn clicks, and where it is ranking well enough to get impressions, the snippet isn't converting.

---

## Cross-Platform Synthesis

**The single clearest pattern, confirmed independently across GSC, Rank Math, and Semrush:** getcarwise.app ranks for real, high-volume "SUV under $X" style commercial keywords (positions 25-57, hundreds of impressions/month) but converts almost none of that into clicks in the 3-month aggregate. The flagship instance of this (the "SUV under $30k" cluster, page 827) was already diagnosed and fixed Sep 3 (TASKS.md #49/#51) — new title/meta + CJ link live. Too soon to see the click-rate effect in a 3-month rolling window. **The genuinely open item is TASKS.md #50** — the site-wide audit for other pages with the same signature, sent to ChatGPT Sep 3, still pending a returned list.

**Genuine positive movement this week:** AI-assistant discovery (Clarity's AI Visibility) is up meaningfully (18.33%→24.90% SoA), and Semrush's referring-domain count shows a large jump that — if verified — clears the Sep 30 traction gate early.

**Flat/no change:** CJ revenue ($20/2 leads, static), GA4 traffic (broadly consistent with prior reads), 404 monitor (routine scanner noise, not a real problem).

## Recommended Next Actions (flagging for André/ChatGPT sign-off since this crosses into SEO/business lane)

1. Independently verify the 56-referring-domains Semrush jump before treating the Sep 30 traction gate as met.
2. Chase TASKS.md #50 — ChatGPT's site-wide zero-click page audit, still pending since Sep 3.
3. Next weekly check: pull a Sep 3-onward date-filtered GSC range (not the 3-month rolling default) to see whether page 827's Sep 3 fix is actually lifting clicks yet.
4. Continue monitoring Clarity dead-clicks (14.71%) — not urgent but trending up from last week's small sample.
