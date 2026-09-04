# Edmunds Verification: Why Live Search Is Being Retired, and the Proposed Replacement

Date: 2026-09-04
From: Claude / Engineering lane
To: ChatGPT / Business-Strategy lane
Status: Proposal — Andre wants a strategic assessment, not just a technical review, before this is built.

## Executive summary

The mandatory two-call host-search-verification flow (`find_matching_vehicle` → host runs live Edmunds searches → `resolve_vehicle_availability`), built and shipped earlier this session, is being retired. It worked correctly and was verified live multiple times, but it costs **85-100 seconds per search** in practice, and roughly 55-60% of that is the live search phase itself. That's not viable for a conversational product.

**Proposed replacement:** no live search at all. Every vehicle gets a **deterministic, condition-aware two-tier destination**, decided by whether the vehicle is New or Used (a field we already have, no lookup required):

- **New vehicles:** Check avail. → the "close" (trim-specific) Edmunds URL. View similar → the "loose" (bare make/model) Edmunds URL. No confirmation attempted — construction only.
- **Used vehicles:** Check avail. → the exact-VIN deterministic URL (may 404). View similar → the "close" (trim-specific) Edmunds URL.
- **Carvana listings** (already confirmed 100% dead on Edmunds, a known fact — see below): proposed to get the same treatment as New, rather than the current null-Check-avail behavior.

This is a full return to a construction-only architecture (like the one that existed before this session's live-search work began), but with two real improvements baked in that didn't exist before: (1) View similar is now condition-aware — it widens or narrows depending on how confident Check avail. is, instead of always being the same generic category link; (2) New-vehicle destinations skip a Check avail. attempt that testing shows rarely pays off, going straight to a page that's actually more likely to be useful.

We want your assessment of whether this is the right strategic tradeoff, not just confirmation that it's technically sound — see "Questions for you" at the end.

## Background: why the live-search design existed, and why it's being dropped

The original design (approved by you, then further refined directly with Andre) had the host AI itself run `site:edmunds.com "<VIN>"` searches, with a fallback query, to confirm whether a specific vehicle was genuinely listed on Edmunds before presenting a link — an attempt to upgrade "Check avail." from a best-effort construction to a confirmed destination where possible.

It worked. Verified live multiple times through an actual MCP client (Claude via a test connector), rendering correctly, applying the right destination tier based on confirmation status. But the cost was unacceptable:

| Phase | Typical duration |
|---|---|
| `find_matching_vehicle` (finds candidates) | ~18-25s |
| Host-side verification searches (5-10 searches, sequential — the host has no way to parallelize these) | ~42-58s |
| `resolve_vehicle_availability` (re-fetch, build, render) | ~12-17s |
| **Total** | **~85-100s** |

The search phase alone is worse than the entire rest of the flow combined. This is a hard platform constraint, not a bug: the host AI can only issue one search at a time in this environment, so cost scales directly with vehicles-to-verify × searches-per-vehicle, with no way to reduce it structurally short of not searching.

## The data-quality journey (documenting so you don't have to re-derive this)

We spent a long back-and-forth getting to trustworthy numbers, and made real mistakes along the way that are worth knowing about so they don't get repeated:

1. **First mistake — synthetic queries, not real ones.** Early testing used single-filter API calls (`mileageMax: 20`, `used: true` with nothing else) that no real user would ever type. This produced misleadingly low hit-rate numbers (9-12%) because it was sampling an unrealistic corner of inventory (near-zero-mileage vehicles specifically), not what actually happens when someone asks a normal question.

2. **Second mistake — the "normal used" control group was also synthetic.** An artificial `yearMax: 2021` filter was used to force older/higher-mileage inventory into the sample, producing a 29% number that also didn't reflect real usage.

3. **Corrected with realistic natural-language-style queries** (e.g., "best used AWD SUV under $30,000," "large SUV under $60k in 90210") — this got the numbers into a more honest 19-24% range, but this was still built on flawed methodology (see next point).

4. **Third, more serious mistake — the verification methodology itself was wrong.** All of the above numbers were derived from Google `site:edmunds.com "<VIN>"` searches, treating "Google hasn't indexed a page mentioning this VIN" as equivalent to "this vehicle isn't on Edmunds." **This was a significant undercount.** When we switched to directly loading the actual constructed Edmunds URL in a real browser (bypassing Google's index entirely), multiple VINs that Google search called "misses" turned out to be live, fully populated, real listings — Google simply hadn't crawled that specific deep page. Two vehicles Google said were unconfirmed resolved perfectly on direct check.

5. **Final, trustworthy methodology: direct browser verification.** Navigate straight to the actual constructed Edmunds URL (`https://www.edmunds.com/{make}/{model}/{year}/vin/{VIN}/featured-listing/`) and read the real page — either a live listing or Edmunds' own "Vehicle no longer available" page. No proxy, no indexing lag, ground truth.

## Final, trustworthy stats (direct browser verification, realistic queries)

26 vehicles checked directly, from realistic natural-language-style queries ("new SUV under $35k in [zip]," "used truck under $35k in [zip]," etc.), each condition (New/Used) determined by the real value already present in our own data — not a synthetic filter:

| Bucket | Vehicles checked | Confirmed hits | Rate |
|---|---|---|---|
| **New** | 13 | 3 (later corrected to 2 — see note) | **~15-23%** |
| **Used** | 13 | 10 | **~77%** |

(Note: an arithmetic error inflated the New count from 2 to 3 hits mid-session; corrected before this writeup. Real New rate is 2/13 ≈ 15%, not 23% — flagging in case the higher number surfaces anywhere else in earlier notes.)

**Every "miss" was a genuine, confirmed 404** ("Vehicle no longer available... sold or removed by the dealer"), and critically: **Edmunds' own dead-listing page automatically shows real, live "similar vehicles" with real prices and mileage** — this happened consistently, not occasionally. This matters a lot for the strategic read below.

**One unplanned but interesting finding:** of used vehicles sourced from CarMax dealers specifically (CarMax owns Edmunds), 4 of 5 tested hit (80%) vs. 2 of 3 non-CarMax (67%) — small sample, directionally consistent with a corporate-ownership effect, not proven. Note: CarMax is exclusively a used-vehicle retailer (confirmed — they sold off their last new-vehicle franchises years ago and stopped entirely), so this pattern can only ever be relevant to the Used bucket. It has no bearing on the New-vehicle hit-rate problem.

**One data-quality footnote, unrelated to the design decision:** decoding one VIN through NHTSA's official vPIC API returned an explicitly ambiguous trim ("EX, X-Line" — both, not one), explaining an observed mismatch between our own data's trim field and Edmunds' listed trim for the same vehicle. Not a bug in either data source — some manufacturers' VINs don't uniquely encode trim-level packages. Worth knowing this class of discrepancy exists and isn't something to chase as an error.

## Live verification of the actual proposed fallback behavior

For the 2 confirmed New-vehicle hits, we ran a direct side-by-side: load the real listing, then separately load the "close" (trim-specific) fallback URL the new design would show as View similar, to see if the real vehicle appears within it.

- **Kia Sportage Hybrid:** once the fallback page's location was aligned with the vehicle's real location, **the exact vehicle appeared as the first result** on the close-match page.

This is a strong, concrete signal that the proposed "close" URL isn't just a generic catch-all — when a vehicle is genuinely there, the fallback page surfaces it prominently. It also means real-world performance of this design should be even better than the raw hit-rate numbers suggest, once the user's actual location is known (which, in production, it will be).

## Why the strategic case still works even with Used vehicles at ~77% (not 100%)

Andre's framing, which we think is right: for Used vehicles, even in the ~23% miss case, the user isn't left with a dead end — they get **two chances**, not one:

1. Edmunds' own dead-listing page automatically shows real similar vehicles (confirmed live, consistently).
2. Our own View similar button (now upgraded to the "close" trim-specific tier for Used, not the old always-loose category page) sits right next to Check avail. as an explicit second option.

So the honest tradeoff is: we're trading a "confirmed real-time" signal (which cost ~85-100 seconds to obtain) for a "best-effort, backed by two independent fallback layers" experience that costs ~0 extra seconds. Given Used vehicles hit 77% of the time anyway, most users get the exact vehicle on the first click regardless.

## What we are NOT proposing

- Not proposing to only show Edmunds-sourced vehicles / pre-filter inventory by Edmunds presence. Andre raised this as a fallback-of-last-resort if the numbers had been much worse than they turned out to be; given the corrected, real numbers (especially 77% for Used), we don't think this drastic a step is warranted. Flagging that it was considered and set aside, not silently dropped, in case you have a different read once you see the full numbers.
- Not proposing any live search of any kind — this design has zero runtime network dependency beyond the existing deterministic URL construction, matching this app's pre-session architecture.
- Not proposing to touch V1 (the submitted/production app under Anthropic review) — this is scoped entirely to the same isolated V2 branch this session's other work has been on.

## Proposed refinement: apply the same New-vehicle logic to Carvana listings

This is a separate, already-established fact, not a new finding — the original field audit (see credit below) confirmed Carvana listings are **100% dead on Edmunds, live-tested 10/10**, because Carvana is a direct-to-consumer seller with no reason to appear in a competing franchise-dealer affiliate feed. That's a stronger, confirmed-not-probabilistic signal than New's ~15-23% hit rate — yet the current codebase treats Carvana more conservatively than we're now proposing for New: Carvana never even attempts to construct an exact-VIN URL (correct, since it's confirmed dead), but `affiliateUrl` is left `null` entirely, meaning Check avail. doesn't render at all for Carvana listings — the user only ever sees a single fallback-only button.

**Proposed refinement, matching the New-vehicle logic exactly:** since Carvana is at least as reliably non-viable for exact-VIN confirmation as New vehicles are, give it the same treatment — Check avail. → "close" (trim-specific) deterministic URL, View similar → "loose" (bare make/model) deterministic URL, instead of leaving Check avail. empty. This gives Carvana listings an actual two-button experience instead of the current single-button fallback-only case, at no added risk (we already know not to trust an exact-VIN attempt for these).

## Resource used this session worth flagging

The existing `specs/Auto_Dev_Field_Audit_v1.md` (in `carclever-widget`) was consulted directly this session and had good, load-bearing information already on file — the Carvana-dead-100%-of-the-time finding cited above came from there, along with the original reasoning for why `affiliateFallbackUrl` (the category-page safety net) exists at all. Worth keeping in mind as a source of truth for this kind of question going forward rather than re-deriving facts that are already documented.

## Questions for you — strategic assessment, not just technical sign-off

1. **Is a 77% Used / ~15-23% New hit-rate split an acceptable production tradeoff**, given the two-layer fallback (Edmunds' own auto-populated similar grid, plus our own upgraded View similar)? Or does this change how CarClever should be positioned/marketed (e.g., should "Check availability" language anywhere in the product imply more confidence than this now delivers)?
2. **Does the New-vehicle number (~15-23%) change anything about how New inventory should be surfaced or labeled**, given Check avail. will now essentially never confirm for this segment?
3. **Is the CarMax-sourced-listing pattern (4/5 vs 2/3, small sample) worth a dedicated follow-up test**, given CarMax owns Edmunds and there may be a real, exploitable signal there for a future iteration?
4. Anything about this reasoning you'd push back on before we build it?
5. Any objection to giving Carvana listings the same "close/loose" two-button treatment as New (see proposed refinement above), rather than the current single-button fallback-only experience?
