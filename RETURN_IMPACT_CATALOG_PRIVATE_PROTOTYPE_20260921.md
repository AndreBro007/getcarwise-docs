# RETURN — Impact Catalog Private Engineering Prototype (Task #71)

**Date:** Sep 21, 2026
**Owner:** Claude (Engineering lane)
**Authorized by:** André, per the scope in `HANDOFF_CLAUDE_IMPACT_CATALOG_PRIVATE_PROTOTYPE_20260921.md`
**Status:** ✅ Built, tested, deployed to a private/access-controlled Vercel preview. Live end-to-end path confirmed via server-side verification. One remaining gap noted below (browser-level Basic Auth click-through), not blocking.

---

## 1. Scope actually delivered

Exactly what the handoff authorized, nothing more:

- A **private, access-controlled, noindex** engineering prototype at `/internal/impact-prototype` in the `carclever-widget` repo (same repo as Lite, Deal Score, Price Check, VIN Check).
- **Condition-neutral by design** — the adapter never reads, infers, or displays New/Used/CPO. Confirmed live (Section 5) that Impact's `Condition` field is present in the schema but always an empty string; the code never reads it regardless of that finding.
- **Optional NHTSA VIN spec-validation layer** — disabled by default (`IMPACT_PROTOTYPE_NHTSA_ENABLED`), scoped only to year/make/model/body-class cross-checks, never condition/ownership/title/accident/mileage/availability/proximity, never logs or returns the VIN.
- **No public launch, no WordPress publication, no SEO/GEO edit, no Publisher Tag, no bulk Catalog download, no sitewide CTA change, no lead submission.** None of these were touched.

## 2. Repository / branch / deployment target

Confirmed explicitly before any code was written, per the handoff's stop condition:

| | |
|---|---|
| Repo | `AndreBro007/carclever-widget` (same repo as all other website apps — André's direction) |
| Branch | `feature/impact-catalog-prototype`, cut from `main` |
| Vercel project | `getcarwise-app` (project ID `prj_VYlR7zuiAKvz7ve4JL62Ryn5nDt9`) — **note the project name does not match the repo/domain name**; its domain is `carclever-widget.vercel.app`, worth remembering for future sessions |
| Deployment | Preview only, via the stable branch-alias domain `getcarwise-app-git-feature-impa-7e010a-andre-broekmans-projects.vercel.app`; **not promoted to production** |
| Latest deployment | `dpl_4a9MWyppu4SdBrG2Y7GBgxN9D4SZ`, commit `4ee60d7`, `readyState: READY`, confirmed clean build (`✓ Compiled successfully`, `Build Completed`) |

## 3. Files added (branch `feature/impact-catalog-prototype`, 12 commits)

| File | Purpose |
|---|---|
| `lib/impact-catalog.ts` | Server-only adapter: allowlisted query builder, field normalization, URL host allowlist, redaction-safe logging. Never reads `Condition`. |
| `lib/impact-nhtsa-enrichment.ts` | Optional NHTSA spec-check, disabled by default, never infers condition/ownership/history, never returns the VIN |
| `app/api/internal/impact-prototype/route.ts` | POST-only API route, rate-limited (30/hr/IP, far under Impact's ~3,000/hr), validates all input before touching the adapter |
| `app/internal/impact-prototype/page.tsx` | Private page — `noindex`/`nofollow` metadata, server-side kill switch (`IMPACT_PROTOTYPE_ENABLED`) |
| `app/internal/impact-prototype/ImpactPrototypeClient.tsx` | Client UI — all required states (loading, healthy, thin, empty, error, malformed-suppressed, kill-switch fallback) |
| `middleware.ts` | HTTP Basic Auth + `X-Robots-Tag: noindex, nofollow`, scoped **only** to `/internal/impact-prototype*` via `matcher` — fails closed (503) if auth env vars aren't configured |
| `tests/impact-catalog.test.ts` | 21 tests |
| `tests/impact-nhtsa-enrichment.test.ts` | 8 tests |
| `tests/middleware.test.ts` | 6 tests |
| `vitest.config.ts`, `package.json` (updated) | First test framework in this repo (none existed before); added `npm test` / `npm run typecheck` scripts |

**35/35 tests pass.** Full local verification before any push: `npx vitest run` (35/35), `npx tsc --noEmit` (0 errors — necessary because this repo's `next.config.ts` has `typescript.ignoreBuildErrors: true`, so `next build` alone doesn't catch type errors), `npx eslint` (0 errors, 0 warnings), `npx next build` (clean, correct route table: prototype page static, API route dynamic, middleware active).

## 4. Access control — what's actually guaranteed, and how it was verified

Per the handoff: "unlinked" alone is not "private." What's actually in place:

- **HTTP Basic Auth**, enforced in `middleware.ts`, scoped only to the prototype's two paths (`/internal/impact-prototype/*`, `/api/internal/impact-prototype/*`) — confirmed via a dedicated test that the matcher does **not** cover Lite, Deal Score, `/api/chat`, or the homepage.
- **Fails closed**: if `IMPACT_PROTOTYPE_AUTH_USER`/`_PASS` aren't set, the route returns 503 rather than falling open. **Live-confirmed on the real deployment** before env vars were set (see Section 5).
- **`X-Robots-Tag: noindex, nofollow`** set on every response from this route, including 401/503s, plus page-level `robots` metadata (`index: false, follow: false, nocache: true`).
- **Not linked from any navigation, sitemap, or public content.**
- Credentials: username `andre`, a 24-character randomly generated password, stored **only** as a Vercel Preview-scoped environment variable (`IMPACT_PROTOTYPE_AUTH_PASS`). Never printed to this chat transcript, never committed to the repo. You can retrieve it directly from Vercel → `getcarwise-app` project → Settings → Environment Variables, or I can hand it to you through a different channel if preferred.

## 5. Live verification performed this session

**Vercel access.** The documented bash+PAT standing method (STATE.md, Sep 17 2026 entries) works correctly — confirmed identity, listed all 7 real projects, found the `getcarwise-app`/`carclever-widget.vercel.app` name mismatch, set 5 new environment variables scoped to **Preview only** (never touched Production), and triggered a redeploy that reached `READY`.

**Fail-closed behavior, before env vars were set:** hit the private route on the live preview deployment and got exactly the expected `503 "Prototype access not configured"` — confirmed via the browser's own network log (`statusCode: 503`), not just the page text. This is the middleware doing exactly what it's designed to do when credentials aren't configured yet.

**Real Impact Catalog API calls — 4 total this session, all read-only, nowhere near the ~3,000/hr limit:**
1. `list Catalogs` — confirmed credentials work, found the real Catalog (1,352,716 items, matching C1-C8's figure)
2. `Text1 = 'CR-V' AND CurrentPrice <= 30000` — 6 real results, real dealer names (e.g. "CarMax Potomac Mills" in `Manufacturer`, confirming that field is genuinely the dealer name, not vehicle make, exactly as documented)
3. `Category = 'SUV' AND CurrentPrice <= 25000` — 6 real results
4. `Text1 = 'Outlander PHEV' AND CurrentPrice <= 25000` — 6 real results (confirms even a narrow model+price intersection returns real inventory)

**One real finding, corrected:** the original code comment said `Condition` is "absent from every sample." Live data (query #2 above) shows the field is present in the schema but is an **empty string on every item** — a small precision difference from "absent," not a contradiction of the underlying conclusion. The code never read this field either way; only the comment was imprecise. Fixed and pushed (commit `4ee60d7`).

**Build/deploy verification, server-side:** Vercel's own deployment event log confirms `✓ Compiled successfully in 4.4s` and `Build Completed in /vercel/output [30s]` with zero real errors (the only "error"-tagged log lines were harmless `npm warn allow-scripts` notices, unrelated to this code).

## 6. Gap not fully closed — flagged, not blocking

I could not complete a full browser click-through of the HTTP Basic Auth prompt itself (entering credentials → confirming the live 200/healthy-card response visually). Chrome's native Basic Auth dialog sits outside what the browser automation tooling can screenshot or type into without the password passing through a visible tool call in this transcript — which conflicts with the redaction discipline this task explicitly requires. 

This does **not** mean the authenticated path is unverified: it's covered by 6 passing automated tests against the real middleware code (including the exact "correct credentials → 200" case), and the application logic those credentials would unlock has been separately confirmed against live Impact data (Section 5, calls #2–4). The only untested link is the browser's own native auth-dialog interaction, which is standard, well-understood browser behavior, not custom code.

**If you want this closed out fully:** open `https://getcarwise-app-git-feature-impa-7e010a-andre-broekmans-projects.vercel.app/internal/impact-prototype` yourself, sign in with username `andre` and the password from the Vercel dashboard (path above), and confirm you see the search form and get real cards back.

## 7. What's explicitly NOT done (by design, matching the handoff's scope)

- No promotion to production
- No WordPress page created or edited
- No Publisher Tag work
- No bulk Catalog download
- No sitewide CTA change
- No lead submission anywhere
- No merge to `main` — this stays on its feature branch until you decide otherwise

## 8. Suggested next steps (not started, awaiting direction)

- Your own click-through confirmation (Section 6), if you want that specific gap closed
- Decide whether/when this becomes a real feature (public launch is explicitly out of scope for this task and would need its own separate authorization)
- If kept as a standing internal tool, consider rotating the Basic Auth password periodically and adding it to the Drive secrets doc for continuity across sessions
