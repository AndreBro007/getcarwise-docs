# Edmunds Affiliate Program — CJ → Impact.com Migration — Phased Plan

**Last updated:** 2026-09-17
**Status:** Track A (application code) complete, live, and independently verified on both platforms. Tracks B/C and Phases 5-7 remain open.

This is the canonical phased structure for this migration. It supersedes the narrative session-log format previously used in this document; that detailed log is preserved below under "Full session history" for anyone who needs the blow-by-blow investigation record, but this phased summary is the one to read first.

---

## Phase 1 — Business and Impact setup — ✅ COMPLETE

- Confirmed Edmunds is moving its affiliate program from CJ Affiliate to Impact.com.
- Confirmed CJ remains live in parallel — this was a planned transition, not an emergency cutover.
- Confirmed the Impact "media partner" account (Broekman Consulting Pty Ltd, Account ID `7765200`) and that the Edmunds program under it is Approved.
- Confirmed commission amounts are unchanged from the CJ-era program ($10 used/new vehicle lead, $3.50 trade-in lead) and that Impact's referral window (30 days) is actually an improvement over CJ's (14-15 days).
- Read the Impact Master Program Agreement in full. Section 4.2 ("Promotional Methods") is the only clause that actually constrains this work — it prohibits fabricated/automated/incentivized actions, not destination-URL specificity. VIN deep-linking, and reading the Product Catalog API to build better links, are both clear under this agreement.
- Confirmed via the Assets screen's "Deeplinking: Supported" filter that Edmunds has deep linking enabled for this program, no assets excluded.
- Created a read-only Impact Catalogs API token ("GetCarWise Engineering - Read Access") for research purposes. The actual secret was never viewed or transcribed by Claude, per credential-handling rules.

## Phase 2 — Link migration design — ✅ COMPLETE

- Confirmed Impact's tracking-link format via live testing:
  ```
  https://edmunds.sjv.io/c/7765200/3949600/52125?u={encodeURIComponent(destinationUrl)}
  ```
  This is functionally the same shape as CJ's `?url=` wrapper (Impact uses `u=` instead), which meant the app's existing URL-building logic could be reused rather than rebuilt.
- Investigated a more ambitious "look up VIN in Impact's Product Catalog, use its pre-tracked URL" design. **Ruled out**, confirmed directly by Impact support (ticket #882346): VIN cannot be searched or filtered by, via the Catalog Items API, under any field. **Decision, final: use the same static-formula approach as old CarClever** — no catalog/API dependency for link generation at request time.
- Confirmed the design preserves all existing behavior: exact VIN links for used vehicles, trim-specific/category fallback links, CPO handling, new/used/Carvana link logic, and the "similar vehicles" fallback link.
- Live-tested a real VIN-specific Impact link end-to-end (2026 Honda CR-V EX-L, VIN `2HKRS3H79TH322650`): clicked manually by André (not Claude, to avoid looking like automated traffic per the Master Agreement's Section 4.2), resolved correctly to the exact listing with Impact's tracking parameters (`irpid=7765200`, `utm_source=impact`) present and correct.

## Phase 3 — Application code change — ✅ COMPLETE

- Branch `edmunds-impact-swap` created off the exact reviewed SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792` (not off `main`), so the diff is measured against precisely what's live in review.
- The substantive code migration (CJ wrapper → Impact wrapper) was introduced in commit `a2372d0`. Final promoted commit is `dd68e15`, which includes this plus later cleanup (generic naming, cosmetic comment removal, test assertion fixes).
- Changes: `lib/edmunds-cj.ts` (3 old CJ constants consolidated into 1 generic `AFFILIATE_BASE_LINK`; `wrapWithCJ()` renamed to the network-generic `wrapWithAffiliateNetwork()`), `lib/link-resolution.ts` (3 real call sites updated — not 2 as first assumed, corrected by direct inspection), `tests/stable-boundaries.test.ts` (domain constant renamed; 6 places fixed for the `u=` vs `url=` parameter-name difference between Impact and CJ — a real functional fix, not cosmetic; if missed, the test suite would have failed even though production code would have worked).
- Naming deliberately made network-generic (zero occurrences of "CJ" or "Impact" in any touched code) so a future network change needs no renaming, only a value update.
- Total diff: 46 lines across 3 files.
- Build/test validation: 79/79 tests pass (confirmed in an isolated sandbox clone of the branch), clean production build on both Vercel projects. One pre-existing, unrelated TypeScript error confirmed to predate this work (verified against a fresh clone of the unmodified reviewed SHA).
- Manually verified on a live preview deployment (real search, real Impact-tracked result) before promotion.
- **Promoted `dd68e15` to production on both platforms together** (`carclever-find-my-car` for Anthropic, `ccfmc-dev-v2` for OpenAI), not staggered — both projects build from the same shared branch/commit.

## Phase 4 — Production deployment correction — ✅ COMPLETE

- Immediately after promotion, discovered a real discrepancy: the Vercel dashboard showed `dd68e15` tagged "Production" on both projects, but live raw MCP calls to both public domains (`ccfmc-dev-v2.vercel.app`, `carclever-anth.getcarwise.app`, and others) returned `serverInfo.version: "b8b07d8"` — the old commit.
- **Ruled out CDN/edge caching** as the cause: confirmed via raw browser-console `fetch()` calls that every response showed `x-vercel-cache: MISS`, not `HIT` or `STALE`. Also ruled out the previously-suspected Claude-connector caching bug (`SYS-20260831-001` series) on this basis.
- **Attempted and ruled out two other fix paths before finding the real one:**
  - Vercel CLI `vercel promote <sha>` — failed; the CLI requires a full deployment ID or URL, not a bare short SHA, and using it without a local project checkout proved impractical in this session.
  - **Vercel's Instant Rollback dashboard feature — attempted, did NOT work as the fix.** On the Hobby plan, Instant Rollback only offers the single immediately-previous deployment as an option, and that option was itself the old `b8b07d8` build, not `dd68e15` — so Instant Rollback could not reach the deployment we actually needed. This rules out Instant Rollback as the mechanism that fixed this issue, correcting an earlier mischaracterization.
- **Actual root cause, confirmed:** on both projects, **Auto-assign Custom Production Domains was Disabled** (a deliberate setting from the Sep 16 incident response, meant to prevent silent branch-push takeovers). With this setting off, "Promote to Production" correctly tags a new deployment as Production but does **not** automatically reassign the project's actual domains to it — per Vercel's own documentation, "Promoted" and "Current" (domain-assigned) are genuinely distinct states in this configuration, not the same action.
- **Actual fix:** temporarily **re-enabled Auto-assign Custom Production Domains** on both projects, then re-ran "Promote to Production" on `dd68e15` on each. This time the domain reassignment completed correctly.
- **Confirmed live via independent raw MCP `initialize` calls** (fresh browser tabs, bypassing all connector/client caching): both `https://ccfmc-dev-v2.vercel.app/mcp` and `https://carclever-anth.getcarwise.app/mcp` report `serverInfo.version: "dd68e15"`.
- **Confirmed working end-to-end via real tool calls**, not just raw protocol checks: both the standing Claude connector (`CarClever - Find My Car`) and the standing ChatGPT connector (`CarClever V2 Test`) return real search results with `edmunds.sjv.io` links (not the old `anrdoezrs.net`). Manual click-throughs on real listings confirmed working — one VIN hit Edmunds' documented "vehicle no longer available, see similar" fallback page (expected, correct behavior, not a bug), the rest landed on live listings with correct price/dealer/photos.
- **Auto-assign Custom Production Domains confirmed re-disabled** on both projects afterward, restoring the Sep 16 incident-prevention posture.

**Current production URLs:**
- OpenAI: `https://carclever-oai.getcarwise.app/mcp`
- Anthropic: `https://carclever-anth.getcarwise.app/mcp` (also still reachable at the original submitted URL and other legacy aliases during the separate, still-pending Anthropic support URL-change request)

**Standing lesson for any future promotion while Auto-assign is disabled on either project:** the dashboard's blue "Production" badge is not sufficient proof a release is actually live. Always independently verify via a raw MCP `initialize` call checking `serverInfo.version` against the exact expected commit.

## Phase 5 — Website and other CarClever surfaces — ⬜ NOT STARTED

- WordPress website CTAs still use CJ links — not yet migrated.
- Old CarClever (Fractal-managed, separate codebase/team) still needs its own CJ→Impact swap. A separate Fractal code agent already investigated this and confirmed it's safe and ready to implement using the same static-formula approach — but one flagged gap (an unconfirmed 5th CSP array location) was sent back for confirmation and has not yet been resolved. Not this session's direct responsibility (Track A/Engineering owns the main app; old CarClever's migration is a separate decision).
- Website implementation needs a decision between two real options, not yet made:
  1. Replace each CTA with a direct Impact deep link (same approach as the app).
  2. Use Impact's **Publisher Tag** (a JS snippet, account-scoped ID already identified: `P-A7765200-5940-4415-8561-...`) to auto-rewrite plain Edmunds links into tracked Impact links client-side, with basic impression tracking. This is website-only — not applicable to the app's server-rendered MCP tool responses, but relevant here.
- Once implemented, website links need testing for: correct Impact redirect, correct Edmunds destination, tracking attribution, disclosure wording, and no broken or leftover CJ links.
- This is a separate workstream from the Find My Car application switch (Phases 1-4 above), owned by ChatGPT's Business/Strategy lane per the existing handoff (`HANDOFF_EDMUNDS_CJ_TO_IMPACT_MIGRATION_20260916.md`), not blocked by or blocking it.

## Phase 6 — Monitoring after launch — ⬜ TO BE DONE

- Monitor the Impact dashboard for real click/action/referral/commission data — André checking tomorrow (2026-09-18) as the first real data point. As of the last check, balance and pending were both $0.00, with zero real clicks/actions recorded (expected, since no live traffic had gone through Impact links yet at that point).
- Confirm the first real attributed activity appears correctly in Impact once live traffic starts flowing through the new links.
- Compare early Impact performance against the former CJ baseline (referenced in `STRATEGY_EDMUNDS_CJ_AFFILIATE_PARTNERSHIP_20260902.md`) once there's enough data to compare meaningfully.
- Spot-check that VIN links, fallback/similar-vehicle links, and any category links all attribute correctly under real traffic, not just the manual tests already done.
- Watch for any unexpected redirects or rejected Edmunds destinations under real-world volume/variety of listings.
- Keep CJ active during this entire monitoring period as a safety fallback — no reason to disable it yet.

## Phase 7 — Final CJ retirement — ⬜ TO BE DONE (after Phase 6 proves Impact is working)

- Decide a formal CJ retirement date once Impact's performance is proven at real volume — not before.
- Remove remaining CJ-specific application links, website links, and documentation references once retirement is decided.
- Update any disclosures or affiliate-network wording that names CJ specifically, if any exist.
- Remove or archive obsolete CJ constants/tests in the codebase (note: `lib/edmunds-cj.ts`'s filename itself still contains "cj" — deliberately left unchanged during Phase 3 due to the cost of renaming every import across the repo for marginal accuracy gain; revisit this decision if/when CJ is fully retired and the filename's history becomes purely legacy).
- Confirm no `anrdoezrs.net` links remain live anywhere in production surfaces (app or website) before considering this phase complete.
- Keep historical CJ records/data for reporting and comparison purposes even after retirement — do not delete.

---

## Separate, related, but non-blocking gates

These are real open items tracked elsewhere that touch the same infrastructure but are not blockers to this migration specifically:

- Anthropic support (Marco) still needs to confirm the pending CarClever listing has been changed to the new branded MCP URL (`carclever-anth.getcarwise.app`) — a separate request, tracked in `ADMIN_RECORD_ANTHROPIC_SUBMISSIONS.md` and `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`.
- Proposed Vercel project renames (`ccfmc-dev-v2` → `carclever-openai`, `carclever-find-my-car` → `carclever-anthropic`) remain deferred until the above is confirmed.
- Old/duplicate Vercel project cleanup (`ccfmc-dev`, `ccfmc-dev-v3`, `carclever-v2-schema-probe`, `car-clever`, and any others found) remains deferred, tracked in `PLAN_CARCLEVER_VERCEL_NAMING_AND_RELEASE_HYGIENE_20260916.md`.
- Both platforms' app-review status (OpenAI, Anthropic) must continue to be monitored each session per `STATE.md`'s standing instruction.

---

## Bottom line

**The core Find My Car application CJ→Impact migration (Phases 1-4) is complete, live, and independently verified on both platforms** — not just claimed via dashboard state, but confirmed via raw protocol calls, real tool calls through both standing connectors, and real manual click-throughs to live Edmunds listings.

**What's genuinely left:** website/old-CarClever migration (Phase 5, a separate workstream), real-traffic monitoring (Phase 6, starts tomorrow), and eventual CJ retirement once Impact is proven (Phase 7, not time-sensitive).

---

## Full session history (detailed investigation log, preserved for reference)

*The material below is the original, detailed, chronological session-by-session record of this investigation — kept for anyone who needs the full reasoning, dead ends, troubleshooting detail, or exact evidence trail behind the phased summary above. The phased summary above is the canonical current-status reference; this log is supporting detail, not a competing source of truth.*

## Why this doc exists

Edmunds moved its affiliate program from CJ Affiliate to Impact.com. André
has not received a migration email from Impact — only the original
account-approval email — but confirmed directly (Sep 16) that **CJ is still
live**, so this is a planned transition, not an emergency one: **target is
fully moved over before end of September 2026.** This doc is a first-pass
reconnaissance of the Impact dashboard (Claude Team Engineering lane, via
Claude-in-Chrome against an already-authenticated `app.impact.com` session)
to establish what's actually available before any code changes are made.
**No code has been touched yet.** No credentials were entered anywhere; no
API tokens were generated (confirmed none exist yet — see API Access
section).

Companion technical doc (code-side findings, CJ implementation detail): see
`lib/edmunds-cj.ts` / `lib/link-resolution.ts` in `carclever-find-my-car`,
summarized below under "Current code state."

## Account structure

- **Impact "media partner" account:** Broekman Consulting Pty Ltd (Account ID
  7765200). This is the umbrella publisher account — Edmunds is one advertiser
  program under it. The account is not Edmunds-specific, so other affiliate
  programs (other automotive brands, or unrelated verticals) could be added
  under this same account/API credential later without a separate signup.
- **Edmunds program status:** Approved. Can generate tracking links and
  promote immediately.
- **Master Program Agreement** link exists in the account menu (Settings menu
  → footer) — not yet read in full; worth reviewing for terms that supersede
  the informal understanding carried over from CJ.

## Commission terms — confirmed unchanged from CJ

| Lead type | Rate | Referral window |
|---|---|---|
| Used Vehicle Lead | $10.00 | 30 days |
| New Vehicle Lead | $10.00 | 30 days |
| Trade-in Offers Lead | $3.50 | 30 days |

Same dollar amounts as the CJ-era program record
(`getcarwise-docs/STRATEGY_EDMUNDS_CJ_AFFILIATE_PARTNERSHIP_20260902.md`).
**Referral window is now uniformly 30 days** — an improvement over CJ's
14 days (new/used) / 15 days (trade-in).

Current account balance: $0.00 earned, $0.00 pending — no clicks/actions
recorded yet on this Impact account (expected, since it's newly approved and
no links are live on the site/app yet).

## Tracking link mechanism — different from CJ, this changes the code approach

**CJ's model** (what the app currently does, in `lib/edmunds-cj.ts`) is a
static, computable URL template:
```
https://www.anrdoezrs.net/click-{pubId}-{adId}?url={encodeURIComponent(destinationUrl)}
```
No API call needed — pure string concatenation, computed per-request.

**Impact's model is not a static template.** Confirmed via live testing in
the dashboard's "Create a link" tool: pasting a landing page URL and clicking
Create issues a **new, distinct, persistent short link** per destination URL
(e.g. `edmunds.sjv.io/0G56VV` for one URL, `edmunds.sjv.io/6k16mr` for
another — not a predictable function of the input). These are called **Vanity
Links** internally and are visible/manageable under Content → Vanity Links,
each with metadata fields (subId1-3, sharedid, partnerpropertyid) and
Last Updated/Date Created timestamps. Four were created during this session's
testing (visible in the account, harmless, no clicks sent) — flagged in case
André wants them removed.

This means **`wrapWithCJ()` cannot be swapped for a simple `wrapWithImpact()`
string-builder.** The app currently constructs a fresh Edmunds URL per
listing (VIN-specific or category fallback) and wraps it inline, at request
time, for every search result — a pattern that assumed a static wrap
function. Two real paths forward, neither built yet:

1. **Impact Partner API — Tracking Links endpoint.** Impact's public REST API
   (`api.impact.com`) has a documented Tracking Links resource (see
   "Partner API Reference v16" — publicly readable at
   `integrations.impact.com/partner-api-reference`) that can create these
   links programmatically. This would let the app call the API per-listing
   instead of using the dashboard UI. Requires an API token (AccountSID +
   AuthToken) — **none exists yet on this account** (confirmed: Settings →
   API showed "You don't have any access tokens yet," only options were
   "Create Access Token" / "Enable Legacy Tokens" — did not click either,
   token generation needs André's explicit go-ahead).
2. **Publisher Tag (client-side link transformation).** Under Content → Ad
   Tools, Impact offers a JS snippet ("Publisher Tag," account-scoped ID
   embedded: `P-A7765200-5940-4415-8561-...`) that can be installed on a
   website to auto-detect direct Edmunds links and rewrite them into tracked
   Impact links client-side, plus basic impression tracking. This is a
   **website-only** mechanism (WordPress pages), not applicable to the
   `carclever-find-my-car` app's server-rendered/tool-response links, but
   relevant for the GetCarWise WordPress site's existing Edmunds CTAs (the
   ones ChatGPT/Claude added per `HANDOFF_WEBSITE_SEO_CTA_OPPORTUNITY_PASS`).

**Neither path is built. This needs a decision, not just an implementation.**

## Major finding: Edmunds Product Catalog / Inventory Feed via Impact

Under Content → Product Catalogs, there is a live, large, structured data
feed:

- **Name:** Edmunds Product Feed (Catalog ID 34070)
- **1,334,554 products**, file size ~752.6 GB uncompressed (752,675,851 kB
  per the dashboard — likely means the feed is genuinely enormous or this
  figure needs sanity-checking; worth re-verifying before relying on it)
- **Format:** Custom (XML/TXT/CSV/PSV available); current Data-Feed default
  configured as `txt` + `gz` compression (Settings → Data Feeds → Product
  Feed — currently not enabled/piping anywhere; Daily Action Feed and Daily
  Promotional Ad Feed are both present but disabled too)
- **Label:** "inventory," Type: "Retail"
- **Last updated:** live/rolling (Sep 15, 2026 14:49:58 at time of check —
  i.e. updates at least daily)
- **Access methods offered directly in the dashboard:**
  - Download via Browser (Advertiser Submitted Format or Impact Standardized
    Format)
  - Download via FTP (requires creating an FTP account first — a button
    exists: "Create and Email Product Catalog FTP Username and Password" —
    **not clicked**, this creates real credentials and needs André's sign-off)
  - **Access via API** — links to Impact's public Catalogs API
    (`GET/POST/PUT api.impact.com/Advertisers/{AccountSID}/Catalogs/{CatalogId}/Items`),
    documented at `integrations.impact.com/brand-api-reference/reference/catalogs`
    and `.../catalog-items`. Supports keyword search, filtering, sorting per
    the public docs.

**This could be a genuinely different data source than what the app uses
today.** The app currently sources live vehicle inventory from Auto.dev
(see `lib/auto-dev-client.ts`) and only uses Edmunds for affiliate
destination URLs. An Edmunds-native inventory feed — over 1.3M listings,
apparently daily-updated — raises real questions worth a deliberate
evaluation, not an assumption either way:

- Does this feed overlap with, complement, or potentially replace parts of
  the Auto.dev dependency?
- Is it US used+new inventory, or something narrower (needs inspection of an
  actual sample row/schema)?
- Same authentication model (AccountSID + AuthToken) as the Tracking Links
  API, so one API credential would unlock both if pursued.

**Not evaluated further this session** — this is a scope/priority decision,
not something to pursue unilaterally. Flagging clearly as its own item.

## Other Impact account resources (breadth check, not deeply evaluated)

- **Assets (Content → Assets):** 12 pre-made ad assets for Edmunds — 3 text
  links (Sell Your Car, New Car Listings, Used Car Listings) and 9 banner
  images across sizes (300x250, 320x50, 728x90) for three campaigns: New Car
  Inventory, Trade-in Tool, Used Car Inventory. All generate the same
  short-vanity-link style tracking URL when a tracking link is pulled for
  them. These map fairly directly to the CJ-era "Tier 1" opportunities
  already identified in `STRATEGY_EDMUNDS_CJ_AFFILIATE_PARTNERSHIP_20260902.md`
  (Used Cars, Sell Your Car, Used Car Listings, etc.) — same use cases,
  different asset IDs now.
- **Content Widgets:** none available (0 rows) for Edmunds currently.
- **Promo Codes:** none active (0 rows); a "Request Promo Code" button exists
  if this becomes worth pursuing with Edmunds.
- **Requests:** no open requests to/from Edmunds via Impact.
- **Reports menu:** Overview, Performance by Brand, Performance by Day,
  Advanced Action Listing, Saved Reports, Scheduled Reports, Performance
  Bonus Progress, plus a "More" submenu (not expanded this session). All will
  read $0 until real traffic flows through Impact links.

## CJ status — confirmed live (André, Sep 16)

**CJ is still live as far as André can see.** This is not a hard cutover —
both programs can run in parallel. André's plan: **transition from CJ to
Impact before end of month (Sep 2026)**, not urgently/immediately. This
changes the priority of the migration from "urgent, might already be broken"
to "planned, has a few weeks of runway." Worth still spot-checking a live CJ
link on the site periodically before end of month, but this is no longer the
most time-sensitive open item.

## Context: three app submissions currently in review (André, Sep 16)

Relevant background for sequencing this migration against other in-flight
work — three separate app review processes are open at once:

1. **ChatGPT — old CarClever** (the original/legacy app)
2. **ChatGPT — new CarClever** (the OpenAI resubmission candidate, see
   `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md` and related)
3. **Claude — new CarClever** (this is `carclever-find-my-car`, V1 in
   `STATE.md` terminology — the Anthropic review referenced throughout
   `STATE.md` as "pending, confirm each session")

Any CJ→Impact code change to `lib/edmunds-cj.ts` touches the live V1 app that
is *itself* mid-review with Anthropic. Given V1 is frozen per repeated
`STATE.md` entries ("V1 is frozen... do not alter its code"), this affiliate
migration likely needs to land on a non-`main` branch first (V2/dev) and
only reach `main`/production once a decision is made about whether touching
V1 mid-review is acceptable — that's André's call, not assumed here.

## Trackonomics Essentials (seen in Impact dashboard, not yet evaluated)

`Content` area also surfaces an upsell page for **Trackonomics Essentials**
(`app.impact.com/secure/mediapartner/fr/trackonomics-essentials-upgrade.ihtml`)
— an Impact **add-on product**, not a feature already active on this account.
Marketing framing: "Grow your entire affiliate channel in one platform... create
links and track performance across all your networks in one place," with
multi-network link generation as a headline feature. This is relevant only if
GetCarWise ends up running Edmunds-via-Impact alongside other affiliate
programs on *different* networks simultaneously (i.e. a genuine multi-network
management need) — not needed for a straight CJ→Impact swap of a single
program. Flagging for awareness, not recommending action; it's a paid upgrade
and the page's full feature/pricing detail wasn't fully read this session
(page did not scroll further via automation — worth a direct look if this
becomes relevant).

## Open questions / things this session could NOT confirm

1. Master Program Agreement — not read in full.
2. Reports → More submenu — not expanded.
3. Product Catalog schema — not inspected (no sample row pulled; the
   752 GB figure needs a sanity check).
4. Whether Impact's program record (via the `GET /Mediapartners/{AccountSID}/Campaigns`
   API) exposes deep-linking permissions/allowed domains the way the public
   docs suggest other Impact programs do — not checked for the Edmunds
   program specifically.
5. Full Trackonomics Essentials feature/pricing detail — page didn't scroll
   past the hero section via automation this session.

## Explicitly NOT done this session (needs sign-off first)

- No API access token created (Impact dashboard confirmed zero tokens exist).
- No FTP account created for the product catalog.
- No code changes to `carclever-find-my-car` (CJ constants in
  `lib/edmunds-cj.ts` are untouched and still live in production).
- No old CJ links removed or replaced anywhere.
- The 4 test Vanity Links created during this session's exploration were not
  deleted (harmless, but flagging for cleanup if desired).

## Session 2 (Sep 16, later) — deep-linking confirmed, API token created, agreement NOT yet read

### Terminology correction from earlier in this session

André's "catalog options" question turned out to mean the **API token
scope picker** (Accounts, Actions, Ads, Catalogs, Clicks, Contracts,
Tracking Links, Programs, etc.) — not the Product Catalog itself. Recorded
here so the earlier confusion in this doc/conversation doesn't get
misread later. Separately: **before creating this token, the available
scope options and the reasoning for picking specific ones were not
explained to André first** — a real process miss, corrected going forward:
scope/credential choices get laid out for a decision before being created,
not after.

### API token created

One token exists: **"GetCarWise Engineering - Read Access"**, API Version
16, status Enabled. Scopes granted: **Catalogs only** (two GET endpoints —
`Retrieve catalogs` and `Retrieve catalog`). All other scope categories were
explicitly cleared. This token **cannot** create tracking links or read
program/deep-linking settings (no Tracking Links or Programs scope) — those
would need a separate scope grant, deliberately not added yet pending a
clearer sense of what the app vs. the website actually each need (likely
two separate purpose-built tokens rather than one shared one — not decided).

**The actual secret (AccountSID + AuthToken) was never viewed, copied, or
transcribed by Claude** — per credential-handling rules, that value must
come from André directly from the dashboard, never through this chat.

### Priority 1 — Edmunds VIN/deep-linking — CONFIRMED WORKING AT THE PERMISSION LEVEL

This was flagged as the single most important open question: can we point
a tracking link at a specific vehicle (VIN) page, since VIN-level linking is
the most direct path to the two highest-value commissionable events (new
and used vehicle leads, $10 each)?

**Confirmed via the Assets screen's own "Deeplinking" filter** (Content →
Assets → filter sidebar → Deeplinking: Supported / Not Supported):
- Filtering to **Supported** → all 12/12 Edmunds assets shown.
- Filtering to **Not Supported** → 0/12 shown.

This proves Edmunds has deep linking enabled for our program, with no
assets excluded. Mechanically (per Impact's public Help Center docs, not
this account specifically): a tracking link is deep-linked by appending
`u={percent-encoded destination URL}` to it — e.g.
`https://edmunds.sjv.io/xyz?u=https%3A%2F%2Fwww.edmunds.com%2F...%2Fvin%2F...`.
This is functionally the same shape as CJ's `?url=` wrapper, which is good
news for reusing `lib/edmunds-cj.ts`'s existing URL-building logic once the
base domain/format changes to Impact's.

**Still NOT confirmed — two real gaps before this is production-ready:**
1. **Permitted domains/paths for deep linking specifically.** The general
   capability is on, but Impact's docs describe a separate, more granular
   allow-list (domains, with wildcard support) that a brand can restrict
   deep links to. No dashboard location was found this session that shows
   *our* Edmunds program's specific permitted-domains list (the "Details"
   tab / "Discover → My Brands" path described in Impact's own docs isn't
   reachable in this account's current single-brand dashboard layout — it
   may require the broader marketplace view, not yet located).
2. **A real, live click-through test has not been done.** Confirming the
   permission is on is not the same as confirming an actual Edmunds
   VIN-specific URL, wrapped as a `u=` deep link, resolves correctly through
   Impact's redirect rather than erroring or falling back to a generic page.
   This is the next concrete task — build one real test link from an
   existing VIN URL shape the app already generates, and manually verify it
   lands correctly.

### Master Program Agreement — NOT YET READ, flagged honestly

André asked directly whether this had been read before touching anything
further, specifically to avoid inadvertently breaking Impact's rules
(e.g. around scraping the catalog, deep-linking limits, or link
cloaking/obscuring — a known common clause in affiliate agreements
generally). **Honest answer: no, not read in full, and here's exactly why:**
the PDF (`https://impact.com/legal/impact.com_Master_Program_Agreement.pdf`)
blocks automated fetching via its own robots.txt, and web-search snippets
only surface fragmentary sections (indemnification, confidentiality,
liability caps — standard boilerplate, nothing found yet about deep-linking
or catalog-use restrictions specifically). A related but distinct public
document, Impact's "Partner User Agreement" (found via a third-party SEC
filing, not impact.com directly), has a "Restrictions" section that
explicitly prohibits "cookie stuffing or other means" of manipulating
attribution — relevant in spirit but not the same document, and the
available snippet cuts off before the full restriction list.

**This is a real, acknowledged gap, not a checked-off task.** The only
reliable path forward: André reads the PDF directly (already open in an
account-authenticated tab this session), or shares the actual text so
Claude can search it properly. Nothing that could plausibly conflict with
this agreement (API automation beyond read-only research, catalog scraping,
building the actual Impact link-replacement code) should proceed until this
is genuinely resolved — not assumed clear.

### Overall plan status — still being built, not finalized

There is not yet a finished, written step-by-step plan — this doc is
presently a running record of the *investigation* phase, which is exactly
where things should stay until: (1) the Master Program Agreement is
confirmed clear, (2) the deep-link click-through test passes, (3) André has
decided on the token/scope structure for app vs. website use. Once those
three land, the next version of this doc should convert from "investigation
notes" into an actual phased plan with concrete tasks, owners, and
sequencing — deliberately not written yet, to avoid planning around
unconfirmed assumptions.

### Master Program Agreement — READ IN FULL, GATE CLEARED (Sep 16, later)

André supplied the actual PDF directly (uploaded to chat) after the earlier
robots.txt block prevented automated fetching. Full document read.

**The one clause that actually constrains what we build — Section 4.2,
"Promotional Methods".** Unless Edmunds authorizes in writing, Partner must
not:
- (a) provide leads obtained other than through genuine End User action
  (e.g. scraping End User info, or submitting End User data on their
  behalf instead of the End User doing so personally);
- (b) use fake redirects, automated software, or other mechanisms to
  generate Actions;
- (c) generate Actions not in good faith — automated devices, robots,
  iframes, hidden frames, or interference with another Partner's referrals;
- (d) incentivize End Users to procure Actions (e.g. offering a reward for
  completing an Edmunds lead form).

**How this maps to the plan:**
- VIN deep-linking — **clear.** A real user clicking a real link to a real
  page is exactly the intended use; nothing restricts destination-URL
  specificity, only fabricated/automated/incentivized actions.
- Using the Product Catalog API to verify a VIN exists in Edmunds' own feed
  before constructing a link — **clear.** This is reading data to build a
  better link, not generating or submitting a lead on anyone's behalf.
- **Hard lines to remember for any future feature/marketing idea:** never
  auto-submit any Edmunds form on a user's behalf; never fire an Action
  without a real person actually completing it themselves; never offer an
  incentive (discount, reward, etc.) specifically for completing an Edmunds
  lead — this would violate 4.2(d) directly regardless of good intent.

**Other clauses of note, not blocking:**
- 4.1 (IP license): ad creative use is revocable, non-exclusive, and
  limited to "solely to the extent necessary to perform the Services" —
  fine for using Edmunds' provided banners/text links as intended, not a
  license to repurpose their assets elsewhere.
- 6.3 (Audit rights): either party can request compliance records for up
  to 1 year after the agreement ends — supports keeping this documentation
  trail as a matter of practice, not just convenience.
- No clause found restricting Product Catalog data use, deep-link
  destination domains, or link formatting/cloaking beyond what 4.2(b)/(c)
  already cover.

**Gate status: CLEARED.** Nothing in the agreement blocks VIN deep-linking,
Catalog API reads, or the plan as currently scoped. The live click-through
test (next item below) can proceed.

### Live VIN deep-link test — PASSED (Sep 16, later)

André manually clicked the test link (not Claude — deliberately, to avoid
looking like automated/bot traffic to Edmunds/Impact, consistent with
Section 4.2's prohibition on non-genuine End User actions).

**Test setup:** Real, currently-live Edmunds listing — 2026 Honda CR-V
EX-L, VIN `2HKRS3H79TH322650`, AutoNation Honda Valencia, $34,985. André
supplied a real CJ tracking link to this same listing as the comparison
baseline. Claude built the Impact equivalent by entering the clean
(CJ-params-stripped) Edmunds URL into the dashboard's "Create a link" tool:
`https://www.edmunds.com/honda/cr-v/2026/vin/2HKRS3H79TH322650/featured-listing/`
→ Impact returned `https://edmunds.sjv.io/k4vqR0`.

**Result:** André clicked `edmunds.sjv.io/k4vqR0` manually. It resolved to:
```
https://www.edmunds.com/honda/cr-v/2026/vin/2HKRS3H79TH322650/featured-listing/
  ?afsrc=1&im_ref=3b41-OT1MxyZRMh1dFUhBUHkUkr26YUgxRROx80&irgwc=1
  &irpid=7765200&sharedid=&utm_account=edmunds_affiliate
  &utm_adgroup=3880547&utm_campaign=edmunds_affiliate&utm_content=7765200
  &utm_medium=affiliate&utm_source=impact
```
Confirmed: `irpid=7765200` and `utm_content=7765200` both match our Impact
account ID; `utm_source=impact` (not `commission_junction`) confirms this
is genuinely Impact's tracking, not a leftover CJ redirect. The page shown
was the correct, exact VIN listing — same price, same dealer, same photo as
the CJ-link comparison. **VIN-specific deep linking through Impact is
confirmed working end-to-end, not just enabled at the permission-setting
level.** This is the single most important open question for the entire
migration, and it's now answered: yes, this works.

One near-miss worth recording: André initially pasted a link that still
carried CJ's tracking parameters (`AID`, `PID`, `cjdata`, `cjevent`,
`utm_source=commission_junction`) rather than the resolved Impact one,
which looked like a same-page result and briefly suggested the test might
have failed to differentiate. Re-confirmed with the correct link — real
pass, not a false positive from two links coincidentally landing on the
same page (they're the same VIN by design, so that alone wasn't proof of
which mechanism was used; the query parameters were the actual tell).

**Priority 1 — CLOSED.** VIN deep-linking via Impact works, is permitted
under the Master Program Agreement, and has been live-verified against a
real listing.

### Product Catalog schema — CONFIRMED LIVE, major finding (Sep 16, later)

After extensive troubleshooting (network egress, token scopes, persona path,
session conflicts — all resolved; see "API access troubleshooting log"
below), a real, successful `GET /Mediapartners/{AccountSID}/Catalogs/34070/Items`
call returned live data. **This is a significantly bigger finding than
originally expected — it changes the recommended implementation approach.**

**Per-item fields confirmed present** (sample: a 2026 Toyota Corolla Cross,
a 2024 Mazda CX-90, a 2024 Subaru Outback — three real, in-stock listings):
- **VIN** (in the `Mpn` field)
- **A complete, pre-built, already-tracked Impact URL** in the `Url` field —
  e.g.
  `https://edmunds.sjv.io/c/7765200/3913681/52125?prodsku=...&u=https%3A%2F%2Fwww.edmunds.com%2Ftoyota%2Fcorolla-cross%2F2026%2Fvin%2F7MUDAABG8TV206611%2Ffeatured-listing%2F...&intsrc=APIG_34070`.
  This already contains our account ID, the Edmunds campaign ID, a per-item
  `prodsku`, and a `u=` deep link to the exact VIN listing page — fully
  formed and ready to use as-is.
- Dealer name (`Manufacturer`) and dealer street address (`Text3`)
- Real-time price (`CurrentPrice`) and stock status
  (`StockAvailability`: confirmed `InStock` on all three sampled)
- Photo URL (`ImageUrl`)
- Year / Make / Model / Trim, split across `Category`, `SubCategory`,
  `Text1`, `Text2`, `Numeric1`
- **1,334,554 total items** — confirmed via the real API response
  (`@total`), not just the earlier unverified dashboard figure

**Why this matters more than originally scoped:** the original plan was to
build `lib/edmunds-impact.ts` to call Impact's Tracking Links API and
construct a `u=` deep link per listing at request time (mirroring
`wrapWithCJ()`'s current CJ-era logic). **This catalog data makes that
unnecessary in cases where the VIN already exists in Edmunds' feed** — the
`Url` field is already a complete, pre-tracked, ready-to-use affiliate link.
The revised, simpler design worth evaluating: look up the VIN in this
catalog (via `Query=Mpn='{vin}'` or similar on the Items endpoint) and use
its `Url` field directly, falling back to constructing a deep link
ourselves only for VINs not present in the feed. This is both simpler and
more robust than always constructing links client-side, since Edmunds'
own feed is the authoritative source for which listings are actually live
right now (the `StockAvailability` field alone solves the "is this VIN
still for sale" problem that motivated the app's existing deterministic
CJ-fallback logic).

**Not yet done:** no code changes reflecting this have been made. This is a
design-shifting finding to bring to the actual implementation task, not
something to build unilaterally mid-investigation.

### API access troubleshooting log (Sep 16, later) — for future sessions

This took considerably longer than expected and is recorded in detail so a
future session doesn't repeat the same dead ends:

1. **Network egress**: this environment's own sandboxed bash tool cannot
   reach `api.impact.com` even after `api.impact.com` was added to the
   account's Additional Allowed Domains in Claude's Capabilities settings —
   the block persisted in-session regardless (a known class of platform
   issue per public bug reports, not something fixable mid-session). **All
   further API calls in this investigation were run directly by André**, on
   his own machine, outside Claude's sandbox — this is the durable
   workaround until/unless the egress setting reliably applies.
2. **Credential handling**: the first credential file uploaded as a `.txt`
   attachment was inadvertently exposed in full, in plain text, in this
   chat's transcript — Claude's assumption that a `.txt` upload stays
   file-path-only (as other file types do) was wrong; **`.txt` and other
   text-like uploads are inlined directly into the conversation as visible
   document content.** This is an important lesson for this project:
   **never upload credential files as chat attachments, in any format** —
   share only command output/responses, never the credential itself,
   copy-pasted directly between the dashboard and a local terminal.
3. **403 "Access Denied" (first occurrence)**: caused by calling
   `/Advertisers/{AccountSID}/Catalogs/.../Items` — the **Brand-persona**
   endpoint (for Edmunds to manage their own catalog), not the
   **Partner-persona** endpoint we needed
   (`/Mediapartners/{AccountSID}/Catalogs/.../Items`). Impact publishes
   fully separate "Brand API Reference" and "Partner API Reference" docs;
   easy to conflate since both exist for "Catalogs."
4. **403 "Access Denied" (second occurrence, correct persona path)**:
   caused by the token missing the specific "Retrieve catalog items" scope
   — a distinct checkbox from "Retrieve catalogs"/"Retrieve catalog," which
   the original token-creation session enabled without realizing "Items"
   was a separate, unchecked endpoint.
5. **"You are already authenticated as another user" (XML error)**:
   occurred consistently regardless of credential correctness while calling
   from André's machine with `curl.exe -u`. Root cause not fully confirmed,
   but resolved by switching to Python's `requests` library with credentials
   passed as environment variables (matching Impact's own documented Python
   example) rather than curl with inline `-u` — possibly a
   curl/PowerShell/corporate-proxy session-cookie interaction specific to
   that machine, not an Impact-side account issue. If this recurs, try
   Python/requests first before assuming it's a token problem.
6. **401 Unauthorized**: occurred once when the `AccountSID` environment
   variable held the plain numeric account ID (`7765200`) rather than the
   token's actual full Account SID value
   (`IRjibDkYVJPf7765200xMYBSd2WBDBPtF1`). **The numeric ID and the full
   Account SID are not interchangeable** — always copy the exact Account
   SID string from the token's card, not the number visible in dashboard
   URLs.
7. Final working call, confirmed 200:
   ```
   GET https://api.impact.com/Mediapartners/IRjibDkYVJPf7765200xMYBSd2WBDBPtF1/Catalogs/34070/Items?PageSize=3
   -u {full AccountSID}:{current AuthToken}
   ```

### MCP connector — attempted, not currently viable from claude.ai web

Impact.com has a hosted MCP server (`https://mcp.impact.com/mcp`, OAuth 2.1)
that would eliminate credential-handling entirely (Impact issues tokens
straight to the connecting AI client, never exposing them in chat). MCP
access is already enabled on this Impact account. **Attempted to connect it
as a custom connector from claude.ai web — failed**: Impact's server
returned "Automatic client registration isn't supported by Impact,"
meaning it doesn't support the auto-registration handshake claude.ai web's
custom-connector flow uses. Impact's own documentation confirms only three
specific clients are supported: **Cursor, VS Code, and Claude Desktop /
Claude Code** — not claude.ai's web browser interface. **This is worth
revisiting via Claude Desktop specifically** (a different application from
claude.ai web) in a future session, since Impact's guide is written
specifically for it and should work following their documented steps.
Likely a better long-term integration path than manual curl/Python calls,
once set up.

### Track A investigation — VIN lookup explored, not resolved (Sep 16, later)

Following the catalog-schema finding above, investigated whether a
VIN-based lookup could work for Track A's design (look up VIN in
catalog → use pre-tracked `Url` if found → fall back to constructed
`?u=` link otherwise, same formula as old CarClever).

**Confirmed, directly, not inferred: VIN cannot be searched or filtered
by, in any way, through this API.**
- `Query=Mpn='{vin}'` → `400 "Unknown search field name: Mpn"` (tested
  live, exact error)
- `Keyword={vin}` (free-text search) → empty result, no match (tested
  live)
- `Mpn` (the field VIN is stored in) is not on Impact's documented
  `Query`-eligible-fields list (`CatalogItemId, Name, Description,
  Labels, Manufacturer, CurrentPrice, StockAvailability, Gtin, Category,
  DiscountPercentage, Gender, Color, Size`)

**A workaround was tested and partially works, but is NOT yet a
validated solution — this needs to be stated carefully, an earlier
draft of this section overstated it as "validated" before being
corrected:**
- `Manufacturer` (confirmed to actually store *dealer name*, not car
  make) IS queryable — confirmed live, `Query=Manufacturer='AutoNation
  Honda Valencia'` returned 161 items for that one dealer
- Scanning that 161-item set client-side found an exact VIN match for
  one specific real car (`2HKRS3H79TH322650`) — same VIN tested earlier
  in this session's live deep-link click-through test
- The app's own dealer-name string for that same car (confirmed from a
  real `carclever-find-my-car` result card, screenshot) matched
  Impact's `Manufacturer` value exactly, byte-for-byte

**Real, unresolved problems with this workaround — why it is NOT
recommended as the design yet:**
1. **Unverified match rate.** One dealer matching exactly proves
   nothing about the hundreds/thousands of other dealers — independent
   dealers, abbreviations, franchise-naming differences could easily
   cause Auto.dev's dealer string and Impact's `Manufacturer` field to
   diverge. Not tested across a real sample.
2. **Latency.** A live query returning up to ~100s of items, then a
   client-side scan, adds real request time to what should presumably
   feel instant — not measured.
3. **Rate limits.** Catalogs endpoint: 3,600 requests/hour (confirmed
   from docs). Calling this per-listing, per-search, at request time
   could exhaust this under real traffic — not modeled against actual
   expected volume.
4. **Also discovered: Impact's documented `Query`-eligible-fields list
   is itself unreliable** — `Text1` (model) worked despite not being
   listed as eligible; `Numeric1` (year) failed with the same "Unknown
   search field name" error as `Mpn`. This means nothing about this API
   can be assumed correct from docs alone going forward — only
   live-tested.

**RESOLVED — Impact support confirmed (Sep 17), ticket #882346 closed.**
Reply from Emma, Impact support: *"filtering or searching directly by
Mpn (or VIN) is unfortunately not supported via the Catalog Items API
search endpoint. Only specific predefined fields are supported."*
Confirms exactly what our own live testing found — not a gap in our
testing, a genuine platform limitation. Their suggested workaround:
download the full product catalog and search the file locally by VIN —
noted as a heavier option, not pursued now (see Track C addition below).

**Decision, final: Track A uses the static-formula approach, same as
old CarClever.** No catalog lookup, no live API dependency for link
generation:
```
https://edmunds.sjv.io/c/7765200/3949600/52125?u={encodeURIComponent(destinationUrl)}
```
The dealer-name workaround explored earlier this session is shelved —
not disproven, just unnecessary complexity for an unproven, marginal
benefit once the "proper" API-based lookup was confirmed unsupported by
Impact directly.

**Real underlying issue, worth stating plainly:** the actual limiting
factor for how many listings get a working Edmunds link was never really
the search mechanism — it's the **coverage gap between Edmunds' catalog
(1.3M) and Auto.dev's inventory (source of the app's ~3-4M listings)**.
No amount of clever API querying fixes a listing that simply isn't in
Edmunds' catalog at all. This is not something to solve via engineering
against Impact's API — see Track C addition below for the real lever
(exploring other affiliate programs/data sources beyond Edmunds alone).

## Session 3 (Sep 17) — implementation: branch created, edits made, naming genericized

Following the plan agreed above, work began on `carclever-find-my-car`.

**Branch created:** `edmunds-impact-swap`, off the exact reviewed SHA
`b8b07d8542f5d3f2a12e00433e089dde28ae5792` (not off `main` — deliberate,
so the diff is measured against precisely what's live in review).

**Edits made, then revised once, based on real-time review discussion:**

*First pass:* renamed `wrapWithCJ()` → `wrapWithImpact()`, consolidated
3 CJ constants into 1 Impact-named constant, added explanatory comments
referencing the CJ→Impact migration by name. Diff: +26/−24 across 3
files.

*André's review, mid-session:* flagged that this exceeded the originally
agreed scope ("3 constants + 1 function body") — a fair, correct catch.
Assessment done before deciding what to do about it:
- Measured actual diff size precisely (git compare, not estimated)
- Confirmed: renaming carries no additional *review* risk (no schema/
  CSP/manifest footprint either way; TypeScript compiler catches any
  missed call site, so no silent-bug risk)
- Real issue was process (scope not confirmed before acting), not the
  code itself

**Second pass, informed by André's further observation:** naming the
function/constants after "Impact" specifically was itself worth
reconsidering — if the network changes again in future, generic naming
means zero renames needed next time, only value updates. Also noted:
`edmunds.sjv.io` (the new domain) is arguably *more* recognizable/
legitimate-looking than CJ's old `anrdoezrs.net`, softening any
"suspicious domain" concern in the *good* direction regardless of naming.

**Final naming, applied:**
- `wrapWithAffiliateNetwork()` (generic, was briefly `wrapWithImpact()`,
  originally `wrapWithCJ()`)
- `AFFILIATE_BASE_LINK` (generic, replaces all 3 old CJ constants)
- `AFFILIATE_PREFIX` in the test file (same pattern)
- Zero occurrences of "CJ" or "Impact" remain in any code this session
  touched, confirmed via full-file grep sweep after each change

**Comments:** reduced to the minimum useful. One purely cosmetic label
comment deleted entirely (no functional value). One file-purpose comment
kept but genericized (was "Edmunds/CJ revenue," now "Edmunds/affiliate
revenue") since it explains what the file does, not which network is
used. No migration-history comments left in code — that context lives in
this doc, not inline.

**Filename `lib/edmunds-cj.ts` deliberately left unchanged** — contains
"cj" but renaming it would require updating every import across the repo
(confirmed: at least `link-resolution.ts` + 3 test files reference it by
path), a meaningfully larger and riskier change than the value/name swap
already done, for a marginal accuracy gain. Decision: leave as-is.

**Final diff, confirmed via `git compare` against the reviewed SHA:**

| File | Lines changed |
|---|---|
| `lib/edmunds-cj.ts` | +5 −7 |
| `lib/link-resolution.ts` | +4 −4 |
| `tests/stable-boundaries.test.ts` | +13 −13 |
| **Total** | **46 lines, 3 files** |

**A genuine, non-optional fix found along the way:** while editing the
test file, discovered it hardcodes parsing on `url=` (CJ's param name) in
6 separate places. Impact's deep-link parameter is `u=`, not `url=` — had
this not been caught, the test suite would have failed after the swap
even though production code itself would have worked correctly. Also
discovered `link-resolution.ts` has 3 real call sites to `wrapWithCJ()`,
not the 2 originally assumed from an earlier, now-stale reading of the
file — corrected by re-fetching and diffing directly against the reviewed
SHA before editing, rather than trusting memory from earlier in the
session.

**Status: all edits pushed to the branch, verified byte-identical against
what was intended. Test suite has not been run. No build has been run. No
Vercel preview deployment has been triggered. No production-promotion
decision made.**

## Recommended next steps (for André's decision, not pre-committed)

1. **DONE.** ~~Build and manually verify one real VIN deep-link test
   through Impact~~ — passed Sep 16, see "Live VIN deep-link test" above.
   Priority 1 closed.
2. **Target: CJ→Impact fully transitioned before end of September 2026**
   (André's stated timeline, Sep 16). CJ confirmed still live, so no
   emergency cutover needed — this can be sequenced deliberately.
3. Decide how to sequence this against the three in-review app submissions
   — corrected understanding (see Session 2 notes elsewhere in
   `getcarwise-docs`): the ChatGPT resubmission and the Claude review are
   **the same V2 codebase** (`release/v2`, SHA `b8b07d8`), not separate
   code. `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md`'s own rule is to
   freeze `release/v2` during review absent a platform-requested fix — an
   Impact migration touching `lib/edmunds-cj.ts` should build/test on its
   own branch and hold there, not merge into `release/v2` or `main` while
   review is open.
4. Decide token/scope structure: likely separate purpose-built tokens for
   app (server-side, Tracking Links scope) vs. any future website API use,
   rather than one shared broad token — not yet built.
5. **Revised based on today's live catalog finding:** the Edmunds Product
   Catalog isn't just a side data source — the Items endpoint returns
   fully pre-tracked Impact affiliate URLs per VIN, already containing the
   correct deep link, plus real-time stock status and price. Next
   engineering step should evaluate using catalog lookups as the primary
   link-generation mechanism (VIN → catalog `Url` field), with constructed
   deep-linking as the fallback for VINs not present in the feed — the
   reverse of the original plan. Separately still worth comparing against
   Auto.dev for inventory-sourcing purposes, but that's now a secondary
   question to the link-generation one.
6. Investigate the Impact marketplace for other relevant affiliate programs
   (vehicle inspection services, auto finance/lending — CJ's LendingTree
   application was never approved/heard back on) — website-first candidate,
   raised by André, not yet started. **New (Sep 17): given the confirmed
   Edmunds (1.3M) vs. Auto.dev (~3-4M) coverage gap, and that this gap is
   the real limiting factor on affiliate revenue (not a technical/search
   problem), explore other automotive affiliate programs or data sources
   beyond Edmunds alone that might cover listings Edmunds doesn't have —
   this is the actual lever for improving coverage, not further Impact API
   work.**
7. Look into the Publisher Tag for the website (auto-converts plain Edmunds
   links into tracked ones + impression tracking) — André wants this
   explored now, in parallel with current website/marketing work.
8. Now that the agreement gate is cleared and item 1 (live deep-link test)
   is done, Engineering lane can scope the actual `lib/edmunds-cj.ts` →
   Impact replacement as a real implementation
   task (new module, new tests, live-tested before merge — same discipline
   as the original CJ integration, built on its own branch per point 4).

## Session 3 continued (Sep 17, later) — production promotion, post-promotion caching question, and a corrected OpenAI test-branch note

**Both platforms promoted to production together, same commit `dd68e15`,
confirmed via dashboard screenshots.** See the updated status in the
"Chosen implementation method" checklist above (steps 5-6, now marked
done) and the new open item logged there about a post-promotion link
domain discrepancy (old `anrdoezrs.net` links still showing via the
Claude connector immediately after promotion) — not yet resolved as of
this entry, pending a fresh-chat re-test André will run later.

### Correction: the OpenAI/ChatGPT-side branch-testing URL — RESOLVED, corrected twice this session

This session repeatedly guessed at the wrong URL for testing against
ChatGPT, wasting real time — recording the final, confirmed-correct
answer here so this isn't re-derived badly again.

**Confirmed correct method (via direct screenshot of the connector's own
settings, Sep 17):** ChatGPT's standing **`CarClever V2 Test`** connector
is already configured against:

```
https://ccfmc-dev-v2.vercel.app/mcp
```

This is `ccfmc-dev-v2`'s own default Vercel production domain — a real,
permanent, stable, short(ish) URL, not a per-deployment preview link and
not a branch alias. It tracks whatever commit is currently promoted to
that project's Production slot (confirmed: this is the exact same
"Production" concept as `carclever-oai.getcarwise.app` on the branded
side — same project, same promotion mechanism, just the plain Vercel
domain instead of the custom branded one). Connector settings confirm:
"Review status: development," "Version name: dev mode," connected
Sep 6, 2026 — this is a genuine standing dev/test connector, already
correctly wired, requiring no new setup.

**Practical implication:** since this URL always reflects whatever is
promoted to `ccfmc-dev-v2` Production, testing a new commit here means
promoting it to that project's Production first (exactly what this
session already did for the Edmunds/Impact commit) — there is no
separate "preview-only" test step needed on the OpenAI side beyond that
promotion. The standing connector picks it up automatically.

**Superseded/incorrect leads explored this session, kept here only so a
future session doesn't waste time on them again:**
- A raw per-deployment preview URL with a random hash
  (`ccfmc-dev-v2-1zlwzi323-...vercel.app`) — valid but not the intended
  reusable pattern.
- `ccfmc-dev-v2`'s own git-branch alias
  (`ccfmc-dev-v2-git-<branch>-...vercel.app`) — also valid, but not what
  the standing connector actually uses, and did not resolve the
  ChatGPT-rendering problem when tried live.
- The older, separate `ccfmc-dev` project (no `-v2`) and its documented
  short-throwaway-branch method (`STATE.md`/`DECISIONS.md`
  `SYS-20260906-002`) — this was a real, correctly-documented method from
  an earlier point in the project's history, but **appears superseded by
  the simpler fact that `ccfmc-dev-v2.vercel.app` itself is already
  short and stable enough** for the standing `CarClever V2 Test`
  connector's actual needs. Not confirmed dead/retired, just not the
  answer to today's question — don't assume it still needs to be used
  for this purpose without checking first.

**Recommendation for future sessions:** before guessing at any new URL
for OpenAI/ChatGPT-side testing, check the `CarClever V2 Test`
connector's own settings/Information panel in ChatGPT first (URL field)
— it already shows the actual, currently-working answer directly, no
need to reconstruct it from Vercel or from doc history.
