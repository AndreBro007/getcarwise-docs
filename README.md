# GetCarWise Documentation Repository

**Purpose:** Persistent storage for session documentation, investigations, strategies, submission records, testing ledgers, and reference materials.

**Organization:** Root-level files with structured naming. Flat by design — no folders, no archive tiers, no manually maintained index.

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
- **DECISION_ / STRATEGY_ / REVIEW_** — approved or proposed strategic records

DATE uses `YYYYMMDD` and records when the file was **created**. It is not a currency signal — several documents have been substantially updated well after their filename date. Use the document's own content and explicit supersession statements to judge authority, never the filename date alone.

---

## Where Current State Lives

**Core administrative state lives in `carclever-widget`** (`STATE.md`, `TASKS.md`, `DECISIONS.md`, `PLAYBOOK.md`, `REFERENCE.md`). Session research, audits, testing and submission records live here.

**This README deliberately does not carry release status, SHAs, endpoints or open checks.** A duplicated status block previously drifted stale here (it listed a superseded Anthropic endpoint for several days). Read `STATE.md` for current state — it is the single source of truth.

Older dated documents are historical evidence. When a newer `CURRENT_`, `STATUS_` or `SUBMISSION_` file explicitly supersedes a stale status statement, use the newer file for current operational state while preserving the older file as history.

---

## Session Startup Rule (effective 2026-09-18)

Agreed by both AI lanes. Full rationale and evidence: `REVIEW_DOCS_ORGANIZATION_AND_SESSION_STARTUP_20260918.md`.

1. **Discover fully, every session.** Dynamically list every file in this repository root via the GitHub API and print the complete inventory. Never hardcode a filename list and never narrow discovery.
2. **Read what you have not seen.** Compare **your own lane's** recorded `getcarwise-docs` checkpoint SHA (in `STATE.md`'s checkpoint table) against `main`, and read every added, modified or renamed file in full. Inspect renames and deletions for affected references.
3. **Read what today's task needs, regardless of age.** Follow references from `STATE.md`/`TASKS.md` and search the full inventory. Age never determines relevance.
4. **Fall back to a full fetch** whenever your checkpoint is missing, empty, uncertain, or the comparison fails. Never guess a lookback window. Never treat the other lane's checkpoint as your own.
5. **At session close,** record the two SHAs you actually reviewed in `STATE.md`'s checkpoint table, updating **only your own lane's row** from a fresh read.

Documents are never moved or archived. Everything stays at a stable, predictable path.

---

## Session Close

Write material findings here, re-fetch every changed file, and verify expected content before claiming completion. See `carclever-widget/PLAYBOOK.md` and `PROTOCOL_SESSION_END_20260826.md` for the broader operating procedure.

---

## Repository Info

- **GitHub:** https://github.com/AndreBro007/getcarwise-docs
- **Managed by:** GetCarWise Business/Strategy (ChatGPT lane) + Engineering (Claude lane)
- **Strategy:** flat root-level dated files, stable paths, cross-referenced from core state/admin records
