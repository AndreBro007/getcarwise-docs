# GetCarWise Documentation Repository

**Purpose:** Persistent storage for session documentation, investigations, strategies, submission records, testing ledgers, and reference materials.

**Organization:** Root-level files with structured naming for easy search and categorization.

---

## File Naming Convention

All documentation follows this pattern: `[TYPE]_[TITLE]_[DATE].md`

Common TYPE categories include:

- **AUDIT_** — infrastructure audits, system reviews, analysis
- **PLAN_** — strategy documents, implementation plans, roadmaps
- **PROTOCOL_** — process SOPs, automation procedures, workflows
- **GUIDE_** — reference guides and how-tos
- **INVESTIGATION_ / RESEARCH_** — research findings
- **TEST_** — manual/automated validation records
- **SUBMISSION_** — platform submission snapshots and status records
- **STATUS_ / CURRENT_** — current operational state
- **DECISION_ / STRATEGY_** — approved or proposed strategic records

DATE uses `YYYYMMDD`.

---

## Cross-Referencing System

Core administrative state remains in `carclever-widget` (`STATE.md`, `TASKS.md`, `DECISIONS.md`, `PLAYBOOK.md`, `REFERENCE.md`). Session research, audits, testing and submission records live here.

Older dated documents are historical evidence. When a newer `CURRENT_`, `STATUS_` or `SUBMISSION_` file explicitly supersedes a stale status statement, use the newer file for current operational state while preserving the older file as history.

---

## Current CarClever / Find My Car state — 2026-09-12

The active submitted release is **V2** from `AndreBro007/carclever-find-my-car` branch `release/v2`, exact SHA:

`b8b07d8542f5d3f2a12e00433e089dde28ae5792`

V2 is now in review on **both platforms** through separate production origins:

- **OpenAI:** `https://carclever-oai.getcarwise.app/mcp` — V2 resubmitted 2026-09-12, status **REVIEW**.
- **Anthropic:** `https://carclever-find-my-car.vercel.app/mcp` — existing production project deliberately promoted to V2 at the exact SHA above; server rescan/listing update saved 2026-09-12, status **IN REVIEW**.

V1/main remains preserved and V3 remains paused.

### Start here

- `CURRENT_V2_STATE_20260909.md` — current operational source of truth, updated Sep 12.
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md` — living release/test ledger, updated through both Sep 12 submissions.
- `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md` — final OpenAI V2 submission record.
- `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md` — Anthropic production cutover, rescan, listing update and current cache-retest item.
- `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md` — current three-app portfolio companion to the older historical `CARCLEVER_3_APPS_STRATEGIC_ANALYSIS.md`.
- `SESSION_CARCLEVER_DUAL_PLATFORM_CLOSEOUT_20260912.md` — Sep 12 session closeout and next-session checklist.

### Current remaining checks

1. Claude connector/cache reset and retest: confirm base connector now advertises V2 (`vehicleNeeds`/electrification fields, no `goals`), then CR-V baseline + exact-VIN Buyer Check.
2. Confirm long-term Vercel production-branch/release behavior for the Anthropic project so a future V1 `main` push cannot silently supersede the manually promoted V2 production release.
3. Freeze V2 during both platform reviews except for platform-requested or evidence-backed corrections.

---

## Session access / closeout

At session start, dynamically list this repository root and fetch every returned file; do not maintain a hardcoded filename list. At session close, write material findings here, re-fetch every changed file, and verify expected content before claiming completion.

See `carclever-widget/PLAYBOOK.md` and `PROTOCOL_SESSION_END_20260826.md` for the broader operating procedure.

---

## Repository Info

- **GitHub:** https://github.com/AndreBro007/getcarwise-docs
- **Managed by:** GetCarWise Business/Strategy + Engineering documentation workflows
- **Strategy:** root-level dated files, structured naming, cross-referenced from core state/admin records
- **Last Updated:** 2026-09-12
