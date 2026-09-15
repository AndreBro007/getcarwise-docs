# Edmunds Affiliate Program — CJ → Impact.com Migration & Channel Reference — 2026-09-16

## Why this doc exists

Edmunds moved its affiliate program from CJ Affiliate to Impact.com (as of this
session, exact cutover date not yet confirmed with Edmunds/Impact directly).
André has not received a migration email from Impact — only the original
account-approval email. This doc is a first-pass reconnaissance of the Impact
dashboard (Claude Team Engineering lane, via Claude-in-Chrome against an
already-authenticated `app.impact.com` session) to establish what's actually
available before any code changes are made. **No code has been touched yet.**
No credentials were entered anywhere; no API tokens were generated (confirmed
none exist yet — see API Access section).

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

## Open questions / things this session could NOT confirm

1. **Exact CJ→Impact cutover date and whether the old CJ links
   (`anrdoezrs.net/click-101637236-...`) are still live/paying, or already
   dead.** André hasn't received migration paperwork beyond the original
   approval email — it's possible documentation exists in a menu/tab not yet
   found, or hasn't been sent yet. Worth checking directly with Edmunds/CJ
   support if this isn't resolved soon, since a live site currently pointing
   at dead CJ links would silently lose all commission — this is the most
   time-sensitive open item.
2. Master Program Agreement — not read in full.
3. Reports → More submenu — not expanded.
4. Product Catalog schema — not inspected (no sample row pulled; the
   752 GB figure needs a sanity check).
5. Whether Impact's program record (via the `GET /Mediapartners/{AccountSID}/Campaigns`
   API) exposes deep-linking permissions/allowed domains the way the public
   docs suggest other Impact programs do — not checked for the Edmunds
   program specifically.

## Explicitly NOT done this session (needs sign-off first)

- No API access token created (Impact dashboard confirmed zero tokens exist).
- No FTP account created for the product catalog.
- No code changes to `carclever-find-my-car` (CJ constants in
  `lib/edmunds-cj.ts` are untouched and still live in production).
- No old CJ links removed or replaced anywhere.
- The 4 test Vanity Links created during this session's exploration were not
  deleted (harmless, but flagging for cleanup if desired).

## Recommended next steps (for André's decision, not pre-committed)

1. Confirm with Edmunds/Impact support (or find it doesn't need confirming)
   whether the old CJ link is still tracking — this determines urgency.
2. Decide: pursue Impact API access (create AccountSID/AuthToken) now, or
   continue with manual dashboard-generated Vanity Links short-term while
   evaluating.
3. Decide whether the Edmunds Product Catalog feed is worth a proper
   evaluation against Auto.dev — separate workstream, not blocking the
   tracking-link migration.
4. Once API access exists, Engineering lane can scope the actual
   `lib/edmunds-cj.ts` → Impact replacement as a real implementation task
   (new module, new tests, live-tested before merge — same discipline as the
   original CJ integration).
