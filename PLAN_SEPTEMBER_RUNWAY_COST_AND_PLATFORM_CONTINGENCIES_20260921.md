# Plan — September Runway: Cost and Platform Contingencies

**Date:** 2026-09-21  
**Status:** proposed; awaiting André’s end-of-month decision  
**Decision date:** on or before 2026-09-30, unless Anthropic/Claude approval changes the evidence sooner  
**Scope:** recurring-cost runway, old CarClever/Fractal fallback, and the website consequences of a Fractal exit. No plan, subscription, app, website, code, deployment or submission has been changed.

## Trigger

Old CarClever has been live for months and has produced only two completed leads. Their source is not currently attributable between the ChatGPT app and website links. This is not sufficient evidence to sustain the existing cost base by default.

The next nine days should preserve the in-review Vercel Find My Car path, avoid automatic Growth/hosting renewals, retain only the smallest viable stack, and make Fractal removable without leaving a broken CarClever Lite experience.

## Verified current architecture

The one Auto.dev key is shared by three consumers:

1. Vercel Find My Car — currently in review with Anthropic/Claude;
2. old CarClever — Fractal production; and
3. CarClever – New & Used Cars — Fractal.

Auto.dev is therefore not an old-Fractal-only cost.

Find My Car is deliberately built with the Free/Starter endpoint family only: Listings, VIN Decode and Photos. Its declared Growth Specs enrichment is off. Free does not remove a currently shipped Find My Car feature; it creates a **shared 1,000-call monthly cap** across all remaining consumers.

## Current documented recurring cost base

The current Tool Stack Reference was last bank-verified on 2026-08-28 and records approximately A$708/month. Some older sections conflict, so amounts and renewal dates must be confirmed in each billing dashboard before any change.

| Service | Documented monthly cost (AUD) | Position through 30 Sep | Proposed fallback |
|---|---:|---|---|
| Auto.dev Growth | 469 | Do not assume another Growth renewal. | Downgrade to Free if the shared-cap readiness gate passes. |
| Fractal | 58 | Freeze new Fractal work. | Prefer a genuine $0 plan if available and safe; otherwise retire after website handling. |
| Claude Team | 78 | Keep while review is open. | Keep the minimum two-seat Team plan for now. |
| Claude Pro personal backup | 31 | Candidate for immediate reduction after account/connector check. | Downgrade to Free. |
| ChatGPT Plus | 28 | Keep. | Live @CarClever distribution and operations workspace. |
| Google Workspace | 26 | Keep. | Company email, Drive and operating records. |
| Microsoft 365 | 10 annualised | Do not renew in October unless a real dependency is identified. | Remove at annual renewal. |
| Porkbun / WordPress / domain / email | 8 | Keep. | Revenue, SEO/GEO and email asset. |
| Vercel, Impact, CJ, Brevo, GA4, GSC, Bing, Clarity, Semrush | 0 | Keep. | Core free distribution, attribution and web infrastructure. |

## Run-rate scenarios

| Scenario | Approx. monthly run-rate | Preconditions / trade-off |
|---|---:|---|
| Current | 708 | Existing position; not justified by the observed lead evidence alone. |
| Immediate non-product cuts | 677 now, then 667 after Microsoft renewal | Claude Pro → Free; Microsoft 365 does not renew. |
| Lean waiting posture | about 198 | Auto.dev Free; Fractal either retained at $0 or exit decision remains pending. |
| Fractal-exit survival posture | about 140 | Auto.dev Free, Fractal cancelled only after website dependencies are handled, Claude Pro Free, Microsoft 365 non-renewed. |

The A$140 figure is a target run-rate, not an assertion that every downgrade is currently safe. It retains Claude Team, ChatGPT Plus, Google Workspace and the website/domain. Potential reduction from the current documented base: approximately A$568/month once conditional changes are safely in effect.

## What must stay

1. **Website/domain/email:** the owned revenue and SEO/GEO asset.
2. **ChatGPT Plus:** @CarClever remains the only confirmed live assistant distribution channel.
3. **Claude Team minimum:** keep through review and the immediate post-decision period. Current Anthropic pricing says Team serves 2–150 seats, so reducing only the QA seat is not available.
4. **Google Workspace:** do not disrupt company email, Drive records or operating identity during a transition.
5. **Vercel and free analytics/affiliate services:** low-cost path to keep testing.
6. **Auto.dev at Free, if safe:** remove Growth cost rather than shut off inventory.

## What can be reduced or stopped

### Auto.dev Growth — highest-priority reduction

Auto.dev Free provides 1,000 calls/month and includes Listings, Photos and VIN Decode. Growth-only products include Specifications, Vehicle Recalls, TCO, Vehicle Payments and Interest Rates.

Find My Car uses only Free/Starter-class endpoints. Old CarClever has reported fallbacks but needs one small guard for Specs and a combined usage/cold-start check.

**Recommendation:** plan Growth → Free at the existing end-of-month review unless the shared-call evidence proves the cap would be breached immediately. If real post-approval traffic consumes the cap, that is evidence for a measured re-upgrade—not a reason to retain A$469/month without demand.

Source checked 2026-09-21: https://www.auto.dev/pricing.

### Fractal — not critical if website is safe

Fractal hosts old CarClever, including the backend used by website page 239, CarClever Lite. It is not required for Vercel Find My Car.

A public Fractal free-tier/cancellation policy could not be independently verified. Treat any $0 tier as dashboard/support-confirmed only.

- If Fractal confirms a real $0 retention tier and old CarClever plus Lite work safely on Auto.dev Free, keep it as a passive fallback.
- If there is no true $0 tier, do not pay A$58/month merely to preserve an unverified source of two historical leads.
- Do not cancel before the website contingency is complete.

### Claude Pro personal account

The stack records Claude Pro at A$30.91/month as still active, while Team is the working production account. Current official pricing confirms Free retains web/desktop/mobile chat, memory, Projects, connectors, web search and code execution; it loses Claude Code and higher usage.

**Recommendation:** after checking the personal account’s connector/project count and confirming Team has needed access, downgrade personal Pro to Free.

Source checked 2026-09-21: https://claude.com/pricing.

### Microsoft 365

It is documented as a backup service, A$125/year due in October. Set it not to renew unless a real business dependency is identified.

## Fractal exit: website consequences and safe fallback

The infrastructure audit identifies CarClever Lite (page 239) as a website app calling old Fractal CarClever. Cancelling Fractal without changing this path will leave a live, broken user journey. Related old-CarClever references may also remain on Try CarClever and embedded website-tool journeys.

This must be handled by Claude as authorised website/widget work.

### Recommended low-cost CarClever Lite fallback

Do **not** automatically repoint Lite chat to Find My Car. Find My Car does not yet reproduce old Lite deal-risk/affordability behaviour and remains under review.

Preserve the existing URL and replace the Fractal-dependent experience with a lightweight owned conversion page:

- practical used-car evaluation checklist and source notes;
- independent/research positioning;
- a clear continuation to live ChatGPT @CarClever;
- after approval, a clearly labelled continuation to Claude Find My Car;
- approved contextual affiliate routes where appropriate; and
- no claim that an unavailable live chat or VIN analysis is still operating.

This preserves page equity and avoids a 404 or broken widget.

### Required pre-cancellation inventory

Claude must first verify, current not historical:

1. every WordPress page/embed that calls Fractal or old CarClever;
2. the exact CarClever Lite backend path and all inbound CTAs;
3. Try CarClever published assistant links/copy;
4. Deal Score, Price Check and VIN Check dependencies;
5. whether either completed lead can be attributed to an old-CarClever/Fractal path;
6. rollback copies for every changed page/widget; and
7. the order for Fractal environment removal and shared Auto.dev credential rotation after actual retirement.

## Evidence required before 30 Sep

### A. Revenue/source ledger — André / affiliate dashboards

For each of the two completed leads, capture if available: event date, programme/network, action type and value/status, tracking link/asset or sub-ID, referrer/device data, and reversal/approval status. Until this exists, treat both leads as **unattributed**, not evidence for retaining Fractal or any single channel.

### B. Auto.dev Free readiness — Claude / Fractal engineering

Return the exact combined 7-day and 30-day calls across Vercel Find My Car, old Fractal CarClever and any remaining Fractal app; status codes; cold starts; and a monthly projection.

Also prove:

- Specs and every Growth-only call are skipped on Free;
- whether feature-unavailable responses count toward quota;
- expected calls for a basic Find My Car search, drill-down and old Lite interaction;
- a clear usage-cap message rather than an indistinct service error;
- old-CarClever labels remain truthful; and
- a small real regression bank passes.

### C. Fractal account — André / dashboard

Confirm exact plan, renewal date, cancellation timing/data-retention consequence, availability of a genuinely free production tier, endpoint/environment survival, and reversibility without new review/submission implications.

### D. Website exit readiness — Claude

Return the dependency inventory and a small implementation plan for either keeping Lite on $0 Fractal or replacing it with the lightweight fallback above.

## Decision tree at end of month

1. **Claude approved and early traffic is real:** keep Vercel Find My Car, use Auto.dev Free if capacity permits, and re-upgrade only if real traffic proves the cap is a constraint. Simplify rather than fund parallel Fractal products.
2. **Claude approved but traffic remains negligible:** retain the low-cost Vercel/web path; retire Fractal after the website fallback is live.
3. **Claude still pending:** maintain the lean waiting posture—Vercel ready, Auto.dev Free capped, no Fractal feature work, $0 Fractal standby or prepared exit.
4. **Claude rejected/no credible path:** complete Fractal exit, preserve website/domain and static conversion assets, retain ChatGPT @CarClever while live, and stop paying for Growth data/duplicate hosting.

## Proposed sequence

| Timing | Action | Owner | Requires André confirmation? |
|---|---|---|---|
| Now | Freeze new Growth-only and Fractal feature work; record billing renewal dates. | André | No for inspection; yes for changes. |
| Now | Obtain two-lead attribution records. | André | No. |
| Next 2–4 days | Complete Auto.dev shared-cap readiness and Fractal-plan facts. | Claude / Fractal agent | No for investigation; yes for modifications. |
| Next 2–4 days | Produce current website dependency inventory and Lite fallback scope. | Claude | No for audit; yes for implementation. |
| By 30 Sep | Select Free standby, measured Growth renewal or Fractal exit; select Lite retain/replace path. | André | Yes. |
| After decision | Execute only selected subscriptions and authorised website/app transition; verify each. | André / Claude | Yes. |

## Records consulted

- Tool Stack Reference, Reference, CarClever 3 Apps Strategic Analysis and Find My Car Phase-Out Decision Record in carclever-widget.
- Old CarClever Auto.dev Free-Tier Assessment and Website & App Infrastructure Audit in getcarwise-docs.
- Current read-only Find My Car source: auto-dev-client and capabilities modules.

## Explicit non-decisions

- No subscription has been downgraded, cancelled or renewed.
- No Fractal app has been unpublished or altered.
- No website endpoint, widget, page, affiliate link or app code has been changed.
- No conclusion is drawn about where the two leads originated.
- Claude/Anthropic approval remains pending unless André confirms a new status.
