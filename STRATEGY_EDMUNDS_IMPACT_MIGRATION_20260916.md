# Edmunds Affiliate Program — CJ → Impact.com Migration & Channel Reference — 2026-09-16

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
5. Decide whether the Edmunds Product Catalog feed is worth a proper
   evaluation against Auto.dev — separate workstream, not blocking the
   tracking-link migration. One specific idea raised: use catalog data as a
   pre-check to confirm a VIN exists in Edmunds' feed before building the
   Check-avail/Similar-options links, improving link reliability rather than
   replacing Auto.dev's live-inventory role.
6. Investigate the Impact marketplace for other relevant affiliate programs
   (vehicle inspection services, auto finance/lending — CJ's LendingTree
   application was never approved/heard back on) — website-first candidate,
   raised by André, not yet started.
7. Look into the Publisher Tag for the website (auto-converts plain Edmunds
   links into tracked ones + impression tracking) — André wants this
   explored now, in parallel with current website/marketing work.
8. Now that the agreement gate is cleared and item 1 (live deep-link test)
   is done, Engineering lane can scope the actual `lib/edmunds-cj.ts` →
   Impact replacement as a real implementation
   task (new module, new tests, live-tested before merge — same discipline
   as the original CJ integration, built on its own branch per point 4).
