# HANDOFF: Edmunds Affiliate Program Moving from CJ to Impact.com — 2026-09-16

**For: ChatGPT (SEO/website/marketing lane), André**
**From: Claude (Engineering lane)**
**Companion doc (full research log, engineering detail):**
`STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md`

## What's changing, in one paragraph

Edmunds moved its affiliate program from CJ Affiliate to Impact.com.
**Update (Sep 17): the Find My Car app's CJ→Impact migration is now
complete, live, and independently verified in production on both
platforms** (Anthropic and OpenAI) — see the status table below for
detail. **Website links (WordPress) and old CarClever (Fractal) are
still on CJ, not yet migrated** — that work remains open, per Phase 5
in the companion research doc. CJ affiliate tracking overall is being
kept active as a fallback during a monitoring period — no reason to
retire it yet.

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

## Engineering finding: VIN deep-linking confirmed working, end-to-end

For the app side specifically: Impact's Assets screen has a "Deeplinking"
filter (Supported / Not Supported). Filtering our Edmunds assets to
"Supported" returns all 12/12; "Not Supported" returns 0/12. This confirms
Edmunds has deep linking enabled for our program with no assets excluded.
Mechanically this works by appending `u={encoded destination URL}` to a
tracking link — similar in shape to how the app's existing CJ integration
wraps URLs today (`lib/edmunds-cj.ts` / `lib/link-resolution.ts` in
`carclever-find-my-car`), which is encouraging for reusing that logic once
the base link format changes.

**Update: live-tested and confirmed, Sep 16.** André manually clicked a
real Impact tracking link built for a genuine, currently-live Edmunds
listing (2026 Honda CR-V, a real VIN). It resolved correctly to the exact
VIN-specific page, with Impact's own tracking parameters attached — not a
generic fallback, not an error. This is the single most important open
question for the whole migration, and it's now answered conclusively: yes,
VIN-level deep linking works through Impact.

## Blocking gate: Master Program Agreement — READ, CLEARED

Update (Sep 16, later): André supplied the agreement PDF directly; it has
now been read in full. **Gate cleared — nothing in it blocks the plan.**
The one relevant clause (Section 4.2, "Promotional Methods") prohibits
fake/automated actions, scraped or user-submitted-on-their-behalf leads,
and **incentivizing users to complete an Edmunds lead** — worth keeping in
mind for any future marketing idea (e.g. never offer a reward specifically
for filling out an Edmunds form). VIN deep-linking and using the Product
Catalog API to verify listings are both clearly fine — real users clicking
real links, no fabrication or incentive involved. Full clause-by-clause
detail in the companion research doc.

## Correction + important update: VIN lookup is NOT possible — but general catalog search is, and may be useful for the website

**Correcting an earlier update in this doc.** An earlier version of this
handoff said the Product Catalog API could look up a specific VIN and
return a pre-tracked link. **That was wrong, and has since been
disproven** — both by our own live testing and by direct confirmation
from Impact support (ticket #882346): **VIN cannot be searched or
filtered by, in any way, through this API.** If any website design work
started from the earlier (incorrect) claim, it should be revisited —
there is no way to check "is this specific VIN on Edmunds" via this API.

**What the API genuinely CAN do — and this may still be useful for the
website, separate from the VIN question:**

The Catalog API supports **general search/filtering** across the Edmunds
inventory (1,334,554 listings, updated at least daily) by these confirmed
fields:
- **Dealer name** (field is called `Manufacturer` in the API, but
  actually holds the dealer's name, e.g. "AutoNation Honda Valencia" —
  not the car's make)
- **Model** (field `Text1`, e.g. "CR-V" — confirmed working despite not
  being in Impact's own documented list of searchable fields)
- **Body style / category** (field `Category`, e.g. "4WD Sport Utility
  Vehicles")
- Likely also: price, stock status (listed as supported, not yet tested
  live)

Each matching result includes: **a ready-to-use pre-tracked affiliate
link, current price, stock status, photo, dealer name and address, and
year/model/trim.**

**Possible website use, worth considering separately from the app work:**
a page or widget that pulls real, current Edmunds inventory by a general
filter — e.g. "used SUVs near you," "current Honda CR-V listings," a
dealer-specific page — would get back genuinely live data with working
tracked links already attached, no link-building needed on our side for
that specific use case. This is different from (and doesn't require) any
VIN-specific lookup.

**Caveats to know before designing anything around this:**
- Hard cap: cannot page beyond 20,000 results per catalog (irrelevant for
  narrow/filtered searches, relevant if ever browsing broadly)
- Rate limit: 3,600 requests/hour on this endpoint specifically
- Coverage: Edmunds' 1.3M listings vs. Auto.dev's ~3-4M — a real gap, so
  this only ever covers a subset of the full market either way

Full technical detail, every field tested, and the exact API responses
are recorded in the companion research doc — no need to redo this
research or testing.

## Current status snapshot

| Area | Status |
|---|---|
| CJ links (website only) | Still live — website (WordPress) and old CarClever (Fractal) not yet migrated |
| Impact account | Approved, one API token created (Engineering research only, read-only, Catalogs scope) |
| VIN deep-linking | **Confirmed working end-to-end** — live-tested by André against a real listing, resolved correctly through Impact's tracking |
| Product Catalog API | **Confirmed live, works for general search** (dealer, model, category) — does NOT support VIN lookup (confirmed by Impact support). Possible website use, not an app-side VIN solution — see above |
| Master Program Agreement | **Read in full, gate cleared** — one relevant constraint (no incentivized/automated leads), doesn't block VIN deep-linking or catalog reads |
| Website Publisher Tag / assets | Available now, not yet implemented anywhere |
| App code (`lib/edmunds-cj.ts`) | **Live in production on both platforms** (commit `dd68e15`) — independently verified via raw MCP calls and real connector tests on both Anthropic and OpenAI. See `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md` Phase 3/4 for full detail. |
| Target completion | End of September 2026 |

## Full detail

Every finding, screenshot-by-screenshot navigation note, and the raw
research log lives in `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md` in
this same repo — this handoff doc is the summary/why; that one is the
how/what-was-checked.
