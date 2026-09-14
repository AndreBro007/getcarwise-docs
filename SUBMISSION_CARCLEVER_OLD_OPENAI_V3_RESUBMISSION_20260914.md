# Old CarClever (search-used-cars) — OpenAI Resubmission Record — 2026-09-14

**Status:** SUBMITTED — OPENAI REVIEW
**Lane:** Claude Engineering (submission prep) / André (actual submit)
**App:** CarClever (old, `search-used-cars`)
**App ID:** `asdk_app_v_6a995354dd68819185244fab146f4fe6`
**Version:** 3.0.0 (auto-assigned by OpenAI on scan/resubmit; was 2.0.0 in the pre-session export)
**MCP endpoint:** `https://f5025062-4d61-4160-95a7-1cc05857c622.usefractal.app/mcp` (unchanged)

## 1. Trigger

Description/behavior-change resubmission (not a code deploy) for the fixes shipped and live-verified earlier the same session (see `STATE.md`/`TASKS.md` and `getcarwise-docs/TEST_LOG_OLDCARCLEVER_20260914.md`, 20-row live regression table):
- New default sort: **Recommended** (blend of deal quality, budget utilization, recency), replacing Deal Score/"Best Deal" as default. Best Deal remains fully selectable.
- Search-quality fixes: PHEV vs. regular-hybrid disambiguation, hybrid minivan → Sienna, AWD/diesel converted from soft preference to hard filter, F-150 near-empty-pool bug fixed.

## 2. What changed in the submission (confirmed via JSON diff, not assumed)

| Field | Change |
|---|---|
| `mcp.resources[0].description` (search-used-cars tool description) | Auto-updated via **Scan Tools** — pulled live text already reflecting the Recommended-sort paragraph. Verified word-for-word against a live `CarClever:search-used-cars` connector call made earlier this session — matched exactly. No manual edit needed. |
| `description` (public directory description) | **Left unchanged**, deliberate — André's call: sort mechanics belong in release notes / tool description, not user-facing marketing copy. |
| `screenshots` | All 3 replaced: (1) `Honda CR-V under $50k in 90210` — search card showing Recommended sort live; (2) `Analyze deak risk for A` — risk analysis card (top portion: Decision Gate/Risk Score/Title & History box); (3) `Compare A vs B` — comparison card. |
| `test_cases` | 1 new case added: `Find me a Honda CR-V under $50,000 in zip code 90210`, tools_triggered `search-used-cars`, expects Recommended-sorted current-year results using the stated budget. 5 pre-existing cases (risk/affordability/compare/load-more) left unchanged. |
| `release_notes` | Appended: *"CarClever v3.0.0: Results now default to Recommended sort. Best Deal still available. Improved Search"* |
| `version` | `3.0.0` (OpenAI-assigned on scan, not manually set) |
| `negative_test_cases`, `tool_justifications`, all Global/compliance fields (`categories`, `country_filtering`, `commerce_*`, `complies_with_all_laws_and_regulations`, `intended_audience`, `is_health_related`, `plugin_category`, `entity_type`) | Confirmed unchanged via field-by-field diff — none affected by a sort/search-quality change. |

## 3. Known imperfection in the submitted package

**Screenshot 2's prompt text still contains a typo:** submitted as `"Analyze deak risk for A"` (partially fixed — "for" was added, but "deak" → "deal" was never corrected). Flagged mid-session for correction to `"Analyze deal risk for vehicle A"`; the final submitted JSON shows the fix was not fully applied before submit. Not a blocker (app is in REVIEW), but worth fixing on the next resubmission round if one is needed.

## 4. Explicitly out of scope

The iOS MCP-app widget-rendering investigation (root cause narrowed to `skybridge`'s `_meta.ui.domain` computation, fix modeled on the Find My Car precedent but **not yet attempted**) is deliberately excluded from this submission. No related field was touched.

## 5. Verification method

All field comparisons done via structured JSON diff across three sequential exports (`carclever-3-0-0__4_.json` → `__5_.json` → `__6_.json`) rather than visual/manual comparison, catching the screenshot-2 typo gap that a visual-only check likely would have missed.

## 6. Current gate

App status: **REVIEW**. No further submission-package changes should be made until OpenAI responds, per the standing "don't touch a submitted/in-review package" discipline used elsewhere in this project (see V1/V2 Find My Car precedent).
