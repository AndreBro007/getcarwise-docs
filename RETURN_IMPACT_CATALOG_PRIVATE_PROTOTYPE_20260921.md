# RETURN — Impact Catalog Private Engineering Prototype (Task #71)

**Date:** Sep 21, 2026 (original build), continued same-day for a corrective closeout pass
**Owner:** Claude (Engineering lane)
**Authorized by:** André, per the scope in `HANDOFF_CLAUDE_IMPACT_CATALOG_PRIVATE_PROTOTYPE_20260921.md`
**Status:** 🟡 **PARTIALLY COMPLETE — engineering corrections done and verified (62/62 tests, clean build, confirmed client/server isolation); live browser verification and screenshots blocked by tooling; a Vercel project-level setting (`ssoProtection`) was disabled mid-session with André's approval and not yet restored. See Section 14 for the explicit recommendation: REVISE, not stop or promote.**

---

## 1. Scope actually delivered

Exactly what the handoff authorized, nothing more:

- A **private, access-controlled, noindex** engineering prototype at `/internal/impact-prototype` in the `carclever-widget` repo (same repo as Lite, Deal Score, Price Check, VIN Check).
- **Condition-neutral by design** — the adapter never reads, infers, or displays New/Used/CPO. Confirmed live (Section 5) that Impact's `Condition` field is present in the schema but always an empty string; the code never reads it regardless of that finding.
- **Optional NHTSA VIN spec-validation layer** — disabled by default (`IMPACT_PROTOTYPE_NHTSA_ENABLED`), scoped only to year/make/model/body-class cross-checks, never condition/ownership/title/accident/mileage/availability/proximity, never logs or returns the VIN. **Confirmed in the closeout pass (Section 9.3): no VIN field exists in this feed at all — stays disabled and uninvoked.**
- **No public launch, no WordPress publication, no SEO/GEO edit, no Publisher Tag, no bulk Catalog download, no sitewide CTA change, no lead submission.** None of these were touched.

## 2. Repository / branch / deployment target

Confirmed explicitly before any code was written, per the handoff's stop condition, and **re-confirmed at the start of the closeout pass** (Section 12):

| | |
|---|---|
| Repo | `AndreBro007/carclever-widget` (same repo as all other website apps — André's direction) |
| Branch | `feature/impact-catalog-prototype`, cut from `main` |
| Vercel project | `getcarwise-app` (project ID `prj_VYlR7zuiAKvz7ve4JL62Ryn5nDt9`) — **note the project name does not match the repo/domain name**; its domain is `carclever-widget.vercel.app`, worth remembering for future sessions |
| Deployment | Preview only, via the stable branch-alias domain `getcarwise-app-git-feature-impa-7e010a-andre-broekmans-projects.vercel.app`; **not promoted to production** |
| Latest deployment | `dpl_CFSHHwnTxAzZvWWkXZAAFiahLv2R`, commit `d966f53`, `readyState: READY`, confirmed clean build (`✓ Compiled successfully in 6.3s`, `Build Completed in /vercel/output [47s]`) |

## 3. Files added (original build, branch `feature/impact-catalog-prototype`, 12 commits — see Section 9 for the 10 closeout-pass commits on top of these)

| File | Purpose |
|---|---|
| `lib/impact-catalog.ts` | Server-only adapter: allowlisted query builder, field normalization, URL host allowlist, redaction-safe logging. Never reads `Condition`. |
| `lib/impact-nhtsa-enrichment.ts` | Optional NHTSA spec-check, disabled by default, never infers condition/ownership/history, never returns the VIN |
| `app/api/internal/impact-prototype/route.ts` | POST-only API route, rate-limited (30/hr/IP, far under Impact's ~3,000/hr), validates all input before touching the adapter |
| `app/internal/impact-prototype/page.tsx` | Private page — `noindex`/`nofollow` metadata, server-side kill switch (`IMPACT_PROTOTYPE_ENABLED`) |
| `app/internal/impact-prototype/ImpactPrototypeClient.tsx` | Client UI — all required states (loading, healthy, thin, empty, error, malformed-suppressed, kill-switch fallback) |
| `middleware.ts` | HTTP Basic Auth + `X-Robots-Tag: noindex, nofollow`, scoped **only** to `/internal/impact-prototype*` via `matcher` — fails closed (503) if auth env vars aren't configured |
| `tests/impact-catalog.test.ts` | 21 tests originally, +4 in the closeout pass (Section 9.4) |
| `tests/impact-nhtsa-enrichment.test.ts` | 8 tests |
| `tests/middleware.test.ts` | 6 tests |
| `vitest.config.ts`, `package.json` (updated) | First test framework in this repo (none existed before); added `npm test` / `npm run typecheck` scripts |

**See Section 9.4 for the current, post-closeout test total (62/62).**

## 4. Access control — what's actually guaranteed, and how it was verified

Per the handoff: "unlinked" alone is not "private." What's actually in place:

- **HTTP Basic Auth**, enforced in `middleware.ts`, scoped only to the prototype's two paths (`/internal/impact-prototype/*`, `/api/internal/impact-prototype/*`) — confirmed via a dedicated test that the matcher does **not** cover Lite, Deal Score, `/api/chat`, or the homepage.
- **Fails closed**: if `IMPACT_PROTOTYPE_AUTH_USER`/`_PASS` aren't set, the route returns 503 rather than falling open. **Live-confirmed on the real deployment** before env vars were set (see Section 5).
- **`X-Robots-Tag: noindex, nofollow`** set on every response from this route, including 401/503s, plus page-level `robots` metadata (`index: false, follow: false, nocache: true`).
- **Not linked from any navigation, sitemap, or public content.**
- Credentials: username `andre`, a 24-character randomly generated password, stored **only** as a Vercel Preview-scoped environment variable (`IMPACT_PROTOTYPE_AUTH_PASS`). Never printed to this chat transcript, never committed to the repo. Retrieve it directly from Vercel → `getcarwise-app` project → Settings → Environment Variables.
- **Note (Section 11): Vercel's own project-level `ssoProtection` was additionally in front of all of this, and is currently disabled** — see Section 11 for full detail and the required follow-up decision.

## 5. Live verification performed in the original build session

**Vercel access.** The documented bash+PAT standing method (STATE.md, Sep 17 2026 entries) works correctly — confirmed identity, listed all 7 real projects, found the `getcarwise-app`/`carclever-widget.vercel.app` name mismatch, set 5 new environment variables scoped to **Preview only** (never touched Production), and triggered a redeploy that reached `READY`.

**Fail-closed behavior, before env vars were set:** hit the private route on the live preview deployment and got exactly the expected `503 "Prototype access not configured"` — confirmed via the browser's own network log (`statusCode: 503`), not just the page text.

**Real Impact Catalog API calls — see Section 10 for the full accounting across both sessions (8 total).**

**One real finding, corrected:** the original code comment said `Condition` is "absent from every sample." Live data showed the field is present in the schema but is an **empty string on every item** — a small precision difference from "absent," not a contradiction of the underlying conclusion. Fixed in the code comment.

**Build/deploy verification, server-side:** Vercel's own deployment event log confirmed a clean build with zero real errors in the original session.

## 6. Gap noted in the original build — since re-examined in the closeout pass (Section 9.4/11)

The original build session could not complete a full browser click-through of the HTTP Basic Auth prompt. The closeout pass attempted to resolve this and found a second, compounding factor (Vercel's `ssoProtection`) — see Sections 9.4 and 11 for the full, current status of this gap, which remains open.

## 7. What's explicitly NOT done (by design, matching the handoff's scope) — still true after the closeout pass

- No promotion to production
- No WordPress page created or edited
- No Publisher Tag work
- No bulk Catalog download
- No sitewide CTA change
- No lead submission anywhere
- No merge to `main` — this stays on its feature branch until you decide otherwise
- No model/category allowlist broadened
- No ZIP/radius or condition claims added
- No work performed on Task #72 or Meta Muse during this closeout pass

## 8. Suggested next steps from the original build (superseded by Section 14's recommendation)


---

## 9. Corrective closeout pass (Sep 21 2026, continued session) — items 1–4 fixed and re-verified

André requested a corrective closeout on six specific gaps found in the original build. Status of each:

### 9.1 — Kill switch not enforced in the API route — FIXED, verified

`IMPACT_PROTOTYPE_ENABLED` was previously checked only in `page.tsx`, meaning the API route could be hit directly to bypass it. Moved the check into `queryCatalog()` itself in `lib/impact-catalog.ts` (new `isPrototypeEnabled()` function), so both the page and the route share a single source of truth. When disabled: returns `{ state: "disabled" }` with `X-Robots-Tag: noindex, nofollow`, and **fetch is never called** — confirmed by a dedicated test asserting zero `fetch` invocations, both at the `queryCatalog()` level and the route level (`tests/impact-catalog.test.ts`, `tests/route.test.ts`).

### 9.2 — Client/server separation — FIXED, verified two independent ways

Split into `lib/impact-catalog-shared.ts` (pure types, allowlists, input validation — no credentials, no fetch, safe for the client) and `lib/impact-catalog.ts` (now `import "server-only"` at the top, holds all credential handling and the actual Impact fetch call). The client component (`ImpactPrototypeClient.tsx`) now imports exclusively from the shared file.

Verified two ways, not just by code review:
1. **A real `next build`** compiled cleanly both locally and on Vercel's own infrastructure — if the client component had pulled in server-only code, this build would fail outright (`server-only`'s entire purpose).
2. **Direct inspection of the compiled client bundle.** Grepped all 15 JS chunks produced by the build for `IMPACT_ACCOUNT_SID`, `IMPACT_AUTH_TOKEN`, `IMPACT_CATALOG_ID`, `queryCatalog`, `buildQueryExpression`, and the literal string `api.impact.com/Mediapartners` — **zero matches across every chunk.** The allowlisted model names (`"CR-V"`, `"RAV4"`, etc.), which are meant to be client-visible since they populate the search dropdown, were confirmed present, proving the grep methodology actually works and isn't just missing content due to minification.

### 9.3 — NHTSA/VIN ambiguity — RESOLVED: no VIN field exists in this feed

Ran the minimum bounded read required to answer this: **one** live Catalog item (`PageSize=1`), field **names** inspected only. Findings:
- No field name resembling "VIN" exists anywhere in the schema (70 fields total on the sampled item).
- Checked the free-text fields (`Description`, `Bullets`, `Name`, `Text3`) for a 17-character VIN-shaped substring — none found.
- **No VIN value of any kind was printed, logged, stored, or otherwise handled** — only a boolean presence/pattern-match result was ever produced or recorded.

**Conclusion, per the handoff's explicit instruction for this exact outcome: NHTSA stays disabled and uninvoked.** `lib/impact-nhtsa-enrichment.ts` remains a complete, tested, ready-to-wire adapter that is never called from any live code path — kept in the repo for a future Catalog or feed version that might expose a usable VIN, with this finding now documented directly in the module's own header comment.

### 9.4 — Acceptance evidence — test suite substantially expanded, live evidence partially blocked

Added:
- 4 kill-switch tests in `tests/impact-catalog.test.ts` (disabled state, enabled-by-default, explicit "true", disabled-wins-over-missing-credentials ordering)
- New `tests/route.test.ts` — 5 tests covering the API route's kill-switch enforcement, response hygiene (noindex headers), and confirming validation still runs even while disabled
- New `tests/ImpactPrototypeClient.test.tsx` — **18 tests** covering every one of the 7 required UI states (initial, loading, healthy, thin, empty, error [both reasons], malformed-suppressed, disabled/kill-switch, client-side fetch failure), plus dedicated accessibility tests: every form control has an accessible name, the whole flow is operable via keyboard alone (Tab + Enter, no mouse), `aria-live="polite"`/`aria-atomic="true"` on the results region, `role="alert"` on error states, `role="status"` (not alert) on the disabled state, descriptive per-card link accessible names (not just "View on Edmunds"), and decorative images correctly using empty `alt=""`.

**Current total: 62/62 tests pass** (up from 35), clean `tsc --noEmit`, clean `eslint` (0 errors, 0 warnings), clean `next build` — all re-verified after every change, not assumed.

**Not completed — a real, unresolved live-verification gap:** desktop/mobile screenshots of the authenticated prototype, and a full browser click-through of the live 200/healthy-card path, were not obtained. Two blockers compounded:
1. Chrome's native HTTP Basic Auth dialog sits outside what the browser automation tooling can screenshot or type into without the password appearing in a visible tool call — the same redaction-discipline conflict noted in Section 6 of this document.
2. **The `getcarwise-app` Vercel project had `ssoProtection: { deploymentType: "all_except_custom_domains" }` enabled**, which very likely intercepted every preview request before my own middleware even ran, producing an unauthenticated **503** on every attempt regardless of credentials — the middleware's own "not configured" 503 and Vercel's own SSO-wall 503 are not distinguishable from the status code alone, and I could not inspect the actual response body before the browser automation tool itself became unresponsive partway through this session. **André approved disabling this setting** to unblock further diagnosis; **it is currently OFF as of this document's writing** and needs a decision on whether to restore it (see Section 11).

Given this, item 4's UI/logic-level tests are complete and passing, but the specific "capture sanitized desktop and mobile screenshots of the authenticated prototype" requirement is **not fulfilled** — genuinely blocked by tooling, not skipped.

### Files changed in this closeout pass (10 additional commits, `feature/impact-catalog-prototype`)

| File | Change |
|---|---|
| `lib/impact-catalog-shared.ts` | **New.** Client-safe types/allowlists/validation, extracted from the original `impact-catalog.ts`. |
| `lib/impact-catalog.ts` | Marked `import "server-only"`; re-exports shared types for backward compatibility; kill switch (`isPrototypeEnabled()`) now enforced inside `queryCatalog()` itself. |
| `lib/impact-nhtsa-enrichment.ts` | Marked `import "server-only"`; header comment updated with the confirmed VIN-absence finding. |
| `app/api/internal/impact-prototype/route.ts` | Comment updated to reflect the single-source-of-truth kill switch (no code-logic change needed here — the fix lives in `queryCatalog()`). |
| `app/internal/impact-prototype/page.tsx` | Now calls the shared `isPrototypeEnabled()` instead of reading the env var directly, so page and route can never drift out of sync. |
| `app/internal/impact-prototype/ImpactPrototypeClient.tsx` | Imports only from `impact-catalog-shared.ts`; added a `disabled` state renderer (`role="status"`, not `alert`); added `useId()`-based `aria-live` region id, `role="list"`/`role="listitem"` on results, descriptive per-card link labels, empty `alt=""` on images. |
| `tests/impact-catalog.test.ts` | +4 kill-switch tests. |
| `tests/route.test.ts` | **New**, 5 tests. |
| `tests/ImpactPrototypeClient.test.tsx` | **New**, 18 tests. |
| `tests/setup.ts` | **New** — Testing Library cleanup after each test (required for vitest, unlike Jest which does this automatically). |
| `tests/stubs/server-only-noop.ts` | **New** — a vitest-only alias target for the `server-only` package (see `vitest.config.ts` comment for why: vitest runs plain Node, not webpack, so it can't resolve `server-only`'s bundler-conditional export the way `next build` does; this alias lets logic tests run without tripping an unrelated resolution difference, while the *real* enforcement is verified separately via the actual `next build` and the bundle grep in 9.2 above). |
| `vitest.config.ts` | Switched default test environment to `jsdom` (needed for the new UI tests); added the `server-only` alias; server-side logic test files each carry a `// @vitest-environment node` docblock override. |
| `package.json` | Added `server-only`, `@testing-library/react`, `@testing-library/jest-dom`, `@testing-library/user-event`, `@vitejs/plugin-react`, `jsdom`. |

## 10. Latency and bounded-request accounting

**Total live Impact Catalog API calls across both sessions: 8.** Well under the observed ~3,000/hour limit (roughly 0.27% of one hour's budget, spread across two separate sessions on the same day).

| # | Session | Query | Purpose |
|---|---|---|---|
| 1 | Original | `list Catalogs` | Confirm credentials, find the real Catalog ID |
| 2 | Original | `Text1 = 'CR-V' AND CurrentPrice <= 30000` | Confirm model-search query shape |
| 3 | Original | `Category = 'SUV' AND CurrentPrice <= 25000` | Confirm category-search query shape |
| 4 | Original | `Text1 = 'Outlander PHEV' AND CurrentPrice <= 25000` | Confirm narrow model+price intersection |
| 5 | Original | `Text1 = 'CR-V' AND CurrentPrice <= 30000` (re-run) | Precision correction on the `Condition` field finding |
| 6 | Closeout | `Text1 = 'CR-V'` (`PageSize=1`) | VIN field-presence probe (Section 9.3) |
| 7 | Closeout | `Text1 = 'CR-V'` (`PageSize=1`, re-run for field-name verification) | Confirmed field list and VIN-shape substring check |

(Two calls in the original session shared the same query; both counted since each was a separate live HTTP request.)

**No latency instrumentation was added to the adapter itself** — this was not requested in either the original handoff or the closeout instructions, and adding timing/observability code was outside the explicitly authorized scope. Rough, unscientific observation from manual testing: individual Impact API calls returned in well under 1 second each; Vercel preview builds took 30–47 seconds end-to-end (queue + build), consistent across all 5 deployments triggered this session.

## 11. Vercel SSO protection — currently disabled, needs a decision

**Current state, as of this document: `ssoProtection` is OFF** on the `getcarwise-app` project (André approved disabling it mid-session to unblock diagnosis of an unexplained 503). This setting, when on, gates **every** preview deployment on this project behind Vercel's own account-level SSO wall — not specific to this prototype.

This was turned off to test a hypothesis (that Vercel's SSO wall, not my own middleware, was the source of a 503 seen when testing the live authenticated path) — **that hypothesis was never actually confirmed**, because the browser automation tool became unresponsive before the test could be completed with SSO off.

**Recommendation: before restoring `ssoProtection`, complete the blocked verification first** (Section 9.4) — turning it back on before confirming whether it was the real cause would recreate the exact same blocker for the next session. Once verified either way, decide whether the project-wide SSO wall should be restored (likely yes, since my own middleware's Basic Auth is what's actually meant to gate this specific route regardless).

## 12. Branch / main divergence status (re-confirmed at start of the closeout pass)

Re-ran the mandatory repository/checkpoint verification before starting the closeout pass, as required. Result: `main` had advanced 5 commits past the branch's fork point (all admin-doc changes — DECISIONS.md/STATE.md/TASKS.md, including two of Claude's own earlier pushes and unrelated Meta Muse work from ChatGPT); the feature branch was 12 commits ahead. **Zero overlapping application-code files** between the two — confirmed via `git compare`, not assumed. Safe to continue without any merge-conflict risk to real code.

## 13. Rollback instructions

If this prototype needs to be fully removed or the branch abandoned:

1. **Immediate kill switch (no deploy needed):** set `IMPACT_PROTOTYPE_ENABLED=false` as a Vercel Preview env var on the `getcarwise-app` project and trigger any redeploy — the module goes fully inert (no Impact calls from either the page or the API route) while the branch/deployment itself keeps existing.
2. **Remove the preview deployment:** delete the Vercel deployment(s) via the dashboard or `DELETE /v13/deployments/{id}` — the branch alias domain stops resolving.
3. **Remove the branch entirely:** `git push origin --delete feature/impact-catalog-prototype` (or the GitHub UI) — since nothing was ever merged to `main`, this is a clean, total removal with zero impact on any other code.
4. **Revoke credentials:** delete the 5 `IMPACT_*`/`IMPACT_PROTOTYPE_*` environment variables from the `getcarwise-app` Vercel project (Settings → Environment Variables). The Impact Account SID/Auth Token themselves are shared account-wide credentials (used elsewhere per REFERENCE.md) — do not rotate those without checking for other dependents first; only the prototype-specific Basic Auth password is safe to discard outright.
5. **Restore `ssoProtection`** if it was left off (see Section 11) — re-enable via `PATCH /v9/projects/{id}` with `{"ssoProtection": {"deploymentType": "all_except_custom_domains"}}` (or the dashboard) once no longer needed for diagnosis.

## 14. Explicit recommendation

**Recommendation: REVISE, not stop or seek production authorization.**

The core engineering work is sound and thoroughly verified: 62/62 tests, clean build, confirmed client/server isolation via two independent methods, a conclusive and correctly-handled NHTSA/VIN finding, and real live Impact API calls confirming the query logic against production data. This is not a design that needs to be abandoned.

What's needed before this can be called fully closed out:
1. Complete the blocked live browser verification (authenticated 200 path, screenshots) — needs working browser automation tooling, or André's own manual click-through per Section 6's instructions.
2. Resolve whether `ssoProtection` was the real cause of the observed 503, and restore it if appropriate once that's settled.

Neither of these reflects a problem with the underlying engineering — they reflect two tooling/infrastructure obstacles encountered near the end of this session. **No production-pilot authorization request is being made** — that remains a separate, later decision per the original handoff's scope, unaffected by this closeout pass.
