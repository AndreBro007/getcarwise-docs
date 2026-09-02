# HANDOFF: Edmunds Live-Fetch Probe + srp.html Discovery (2026-09-02, Claude Engineering Lane)

**For:** ChatGPT (business/strategy/roadmap lane)
**Context:** Follow-up to `PLAN_CARCLEVER_CONNECTOR_ANALYSIS_AND_MONETIZATION_ROADMAP_20260902.md`'s "Required next test — Edmunds raw-fetch/redirect spike" item. Full technical detail lives in `carclever-widget/DECISIONS.md` (two new entries, both dated 2026-09-02, search for "SYS-20260902" + "Edmunds"). This doc is the condensed, roadmap-relevant summary.

## 1. The original open question is answered

**Question was:** does the real, deployed Vercel app's server-side fetch to Edmunds work reliably enough to validate listing destinations automatically?

**Answer: No — and it never can, as currently architected.** Edmunds runs Akamai bot-detection that blocks plain server-side fetches (confirmed via response headers: `server: AkamaiGHost`, explicit branded `403 - Access Denied | Edmunds` page) while allowing real browser requests through untouched. This was cross-checked two ways: a live Vercel preview deployment got 403 on every URL shape tested, while André's manual browser check of the identical URLs all rendered correctly.

**Practical implication:** any feature idea that depends on "check live whether this Edmunds link actually resolves before showing it to the user" **cannot be built as a serverless/API-route feature**. It would need either (a) a browser-automation step (slow, not viable for real-time user-facing latency), or (b) accepting we don't live-validate and rely on the already-good fallback design (category URL never dead-ends, per existing `SYS-20260817-001` work). This is an architectural ceiling, not a bug to fix — worth factoring into any monetization-funnel feature that assumed live validation was cheap/easy.

## 2. Unexpected upside: a better Edmunds URL exists

While testing, found that Edmunds' own filter UI redirects to a second, different, more powerful URL format (`edmunds.com/inventory/srp.html?...`) once certain filters are touched — this takes real query params, unlike the current SEO-style category URL (`/used-{make}-{model}-{trim}/`) the codebase builds today.

**Confirmed real and working:** `mileage` (e.g. `0-50000`) and `drivetrain` (e.g. `four wheel drive`) — both genuinely filter results and combine correctly with each other.

**Confirmed NOT working via the native Edmunds UI itself:** price range and year range — the *same limitation the codebase already worked around* for the old URL shape, now confirmed to also apply to Edmunds' own filter UI on this newer shape. Not a codebase bug; an Edmunds limitation.

**Untested:** engine type, seating count, accident/history flags, exterior color, body type — several of these are real facets in Edmunds' own sidebar (see the screenshots André captured this session) and could plausibly be wired in, but need the same careful click-and-observe verification method before anyone builds against them.

## 3. Why this might matter for your side of the roadmap

If "closer match to what a user actually wants" is a monetization/UX goal you're scoping — e.g. a user says "I want a 4WD Tahoe under 50k miles" — today's link-building code can't express mileage or drivetrain as filters, only make/model/trim/year/used-new. This `srp.html` discovery is a real, confirmed path to closing part of that gap. It's not built yet and shouldn't be treated as ready — engineering flagged concrete next steps (confirm the real year-param name, verify color/other facets via network inspection rather than guesswork, decide whether to migrate the URL-building function to this shape entirely) before any implementation starts.

**Not a decision, not committed work — a scoping input for whatever roadmap conversation you're having about search-quality/personalization features.**

## References
- Full technical write-up: `carclever-widget/DECISIONS.md`, two SYS-20260902 entries (search "Akamai" and "srp.html")
- Vercel/GitHub identifiers now recorded in `carclever-widget/REFERENCE.md` if needed for any cross-lane verification
- Branch `probe/edmunds-live-fetch` on `carclever-find-my-car` still exists (diagnostic only, never merged, `main` untouched throughout)
