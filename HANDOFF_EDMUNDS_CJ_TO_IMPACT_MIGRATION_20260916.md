# HANDOFF: Edmunds Affiliate Program Moving from CJ to Impact.com — 2026-09-16

**For: ChatGPT (SEO/website/marketing lane), André**
**From: Claude (Engineering lane)**
**Companion doc (full research log, engineering detail):**
`STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md`

## What's changing, in one paragraph

Edmunds has moved (or is moving) its affiliate program from the CJ Affiliate
network to Impact.com. André's Impact account is already approved for
Edmunds. CJ is still live as of this session, so this is a planned,
unhurried migration — **target: fully transitioned by end of September
2026** — not an emergency fix. This affects every Edmunds affiliate link
across the website and the app(s), plus opens up monetization options that
didn't exist under CJ. Nothing has been changed in production yet anywhere
— website links are still the old CJ links, the app's code still uses CJ.

## Why this matters beyond "swap the link format"

This is not a like-for-like swap. Three real differences change how we
should think about monetization strategy, not just implementation:

1. **Same commission rates, better terms.** $10/used lead, $10/new lead,
   $3.50/trade-in lead — unchanged from CJ. But the referral/attribution
   window is now a flat **30 days** on every lead type, up from CJ's
   14–15 days. That alone modestly improves conversion credit on longer
   consideration cycles (which describes most car buying).
2. **A genuinely different, larger toolset than CJ ever offered**, some of
   which is directly relevant to marketing work already underway:
   - 12 ready-made ad assets (3 text links + 9 banners) available
     immediately — no design/setup needed.
   - A live Edmunds inventory data feed (1.3M+ listings, updated daily) —
     unexplored territory, potential relevance to both the app and future
     website content.
   - A "Publisher Tag" — a website JS snippet that auto-converts any plain
     Edmunds link into a tracked one, plus impression tracking. Directly
     relevant to the website CTA work already in progress.
   - Access to Impact's broader marketplace — meaning other affiliate
     programs (vehicle inspection services, auto finance/lending) may be
     reachable through the same account. CJ's old LendingTree application
     was never approved; this could be a fresh path to finance-adjacent
     revenue, especially for the website.
3. **VIN-level deep linking is confirmed enabled for our program** (verified
   this session — see Engineering Finding below). This is the mechanism
   that lets us point a link directly at a specific vehicle listing rather
   than a generic category page — it's the most direct route to the two
   highest-value events (new/used vehicle leads, $10 each), because it lets
   the app hand a user straight to "this exact car" on Edmunds rather than
   "search results that might include it."

## The strategic frame: everything drives toward 3 events

Worth stating plainly since it reframes how to think about every Edmunds
placement, on the website or in the app: **Impact/Edmunds only pays on
three commissionable events** — a new-vehicle lead, a used-vehicle lead, or
a trade-in lead, each completed on Edmunds' own site. There is no display-ad
revenue, no per-click payment, nothing else. Every asset, every link, every
piece of content is purely a *funnel mechanism* toward one of those three
outcomes. This means:

- We cannot capture a lead ourselves and hand it to Edmunds — the user must
  complete the actual form on Edmunds' domain for it to count.
- The real marketing question for every placement is: **does this
  meaningfully increase the odds a user completes one of the 3 forms on
  Edmunds**, not "does this get a click." A high-traffic but low-intent
  placement is worth less than a lower-traffic, high-intent one (e.g. a
  used-SUV buying guide with a "see comparable listings" link, versus a
  generic homepage banner).
- Trade-in leads pay less ($3.50 vs $10) but may have a lower bar to
  complete (a valuation form vs. an actual purchase-intent lead) — worth
  factoring into which funnel to prioritize where.

## What this means for the website (ChatGPT's lane) — flagging, not deciding

These are raised for ChatGPT/André to evaluate and own, not things Claude
is deciding or building:

- The 12 ready-made assets and the Publisher Tag are both usable *now*,
  independent of any app code changes — genuinely "easy wins" that fit
  directly into the marketing push already underway. André specifically
  wants the Publisher Tag looked into further as a way to reduce manual
  link-wrapping work on the website.
- Worth testing on the website first, before the app — André's own
  instinct, and a reasonable one: lower risk, faster iteration, and it
  surfaces real click/lead data before committing to app-side engineering
  effort.
- The other-affiliate-programs angle (inspections, finance) is worth
  browsing in Impact's marketplace as a website monetization avenue,
  especially since CJ's LendingTree application went nowhere.
- Whether/how the Edmunds product catalog feed could feed into future SEO
  content (e.g. real inventory-backed pages) is an open idea, not yet
  scoped — would need its schema inspected first.

## Engineering finding: VIN deep-linking confirmed possible

For the app side specifically: Impact's Assets screen has a "Deeplinking"
filter (Supported / Not Supported). Filtering our Edmunds assets to
"Supported" returns all 12/12; "Not Supported" returns 0/12. This confirms
Edmunds has deep linking enabled for our program with no assets excluded.
Mechanically this works by appending `u={encoded destination URL}` to a
tracking link — similar in shape to how the app's existing CJ integration
wraps URLs today (`lib/edmunds-cj.ts` / `lib/link-resolution.ts` in
`carclever-find-my-car`), which is encouraging for reusing that logic once
the base link format changes.

**Not yet confirmed:** the specific list of domains/paths Edmunds permits us
to deep-link to (a separate, more granular setting than the general
capability), and a real live click-through test of an actual VIN URL. Both
are the immediate next engineering steps, gated on the item below.

## Blocking gate: Master Program Agreement not yet read

Before any further Impact API automation or code changes, the Impact
Master Program Agreement needs to be read and confirmed clear — specifically
around deep-linking limits, catalog-use restrictions, and link-cloaking
rules (a common clause in affiliate agreements generally). This has **not**
been done yet — the PDF blocks automated fetching, so André is retrieving
it directly. Nothing website- or app-side that goes beyond what's already
described here (i.e., beyond using the pre-made assets and reading
documentation) should be built until this is confirmed.

## Current status snapshot

| Area | Status |
|---|---|
| CJ links (website + app) | Still live, unchanged, still the production mechanism |
| Impact account | Approved, one API token created (Engineering research only, read-only, Catalogs scope) |
| VIN deep-linking | Permission confirmed enabled; live test not yet done |
| Master Program Agreement | Not yet read — blocking gate |
| Website Publisher Tag / assets | Available now, not yet implemented anywhere |
| App code (`lib/edmunds-cj.ts`) | Untouched, still CJ-based |
| Target completion | End of September 2026 |

## Full detail

Every finding, screenshot-by-screenshot navigation note, and the raw
research log lives in `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md` in
this same repo — this handoff doc is the summary/why; that one is the
how/what-was-checked.
