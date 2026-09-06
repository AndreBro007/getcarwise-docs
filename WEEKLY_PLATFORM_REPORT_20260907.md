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
- **🔴 Confirmed, unresolved: the zero-click SUV keyword pattern from Sep 1-2 is still present, largely unchanged:**
  - "best suv under 30000" — 337 impressions, 0 clicks
  - "suv under 30000" — 188 impressions, 0 clicks
  - "best suvs under 30000" — 152 impressions, 0 clicks
  - "suvs under 30000" — 108 impressions, 0 clicks
- Google is surfacing these pages at real volume; the SERP snippet (title/meta) is still the likely blocker, not ranking. **This fix has not been actioned since being identified Sep 1-2.**

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

**The single clearest actionable finding, confirmed independently across GSC, Rank Math, and Semrush:** getcarwise.app ranks for real, high-volume "SUV under $X" style commercial keywords (positions 25-57, hundreds of impressions/month) but converts almost none of that into clicks. This is a title/meta-snippet problem, not a content or ranking problem — and it was already identified and logged as a fix on Sep 1-2 (TASKS.md #49-51) but **has not yet been actioned.**

**Genuine positive movement this week:** AI-assistant discovery (Clarity's AI Visibility) is up meaningfully (18.33%→24.90% SoA), and Semrush's referring-domain count shows a large jump that — if verified — clears the Sep 30 traction gate early.

**Flat/no change:** CJ revenue ($20/2 leads, static), GA4 traffic (broadly consistent with prior reads), 404 monitor (routine scanner noise, not a real problem).

## Recommended Next Actions (not yet actioned, flagging for André/ChatGPT sign-off since this crosses into SEO/business lane)

1. Independently verify the 56-referring-domains Semrush jump before treating the Sep 30 traction gate as met.
2. Action the still-open zero-click SUV title/meta fix (logged Sep 1-2, TASKS.md #49-51) — this is the highest-leverage, lowest-effort item found across two consecutive weekly checks.
3. Continue monitoring Clarity dead-clicks (14.71%) — not urgent but trending up from last week's small sample.
