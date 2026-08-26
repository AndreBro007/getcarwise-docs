# GetCarWise Documentation Repository

**Purpose:** Persistent storage for session documentation, investigations, strategies, and reference materials.

**Organization:** Root-level files with structured naming for easy search and categorization.

---

## File Naming Convention

All documentation follows this pattern: `[TYPE]_[TITLE]_[DATE].md`

### TYPE Categories

- **AUDIT_** — Infrastructure audits, system reviews, analysis
- **PLAN_** — Strategy documents, implementation plans, roadmaps
- **PROTOCOL_** — Process SOPs, automation procedures, workflows
- **GUIDE_** — Reference guides, how-tos, user documentation
- **INVESTIGATION_** — Research findings, competitive analysis, market research

### TITLE

Descriptive filename in `snake_case` (no spaces, hyphens ok)

### DATE

`YYYYMMDD` format for version control and sorting

---

## Examples

```
AUDIT_WEBSITE_APP_INFRASTRUCTURE_20260826.md
├─ Type: AUDIT
├─ Title: Website App Infrastructure
└─ Date: Aug 26, 2026

PLAN_PRIORITY_3_WEBSITE_REVIEW_20260826.md
├─ Type: PLAN
├─ Title: Priority 3 Website Review
└─ Date: Aug 26, 2026

PROTOCOL_SESSION_END_20260826.md
├─ Type: PROTOCOL
├─ Title: Session End
└─ Date: Aug 26, 2026
```

---

## Cross-Referencing System

All documents are cross-referenced in the **carclever-widget** repository:

- **STATE.md** — Links to active documents by priority/status item
- **TASKS.md** — Links to task-related documentation
- **DECISIONS.md** — Links to decision-supporting documents

**How to find a document:**
1. Search `carclever-widget` STATE/TASKS/DECISIONS for your item
2. Find the doc reference with filename
3. Fetch from `getcarwise-docs` via git

---

## Next Session Access

**Every session:**
1. FILE VERIFICATION fetches state files from `carclever-widget`
2. FILE VERIFICATION fetches documentation from `getcarwise-docs`
3. All state files contain cross-references linking to relevant docs
4. No context loss between sessions

**Document versioning:**
- Latest version only per session (old versions deleted before push)
- Date in filename = session version
- Search by type, title, or date

---

## Session-End Automation

This repository is populated automatically via the **SESSION_END** protocol:

1. Claude creates documentation during a session
2. At session end, only latest version kept
3. Docs pushed to `getcarwise-docs` with cross-references added to state files
4. Next session: FILE VERIFICATION fetches all docs + state

See `carclever-widget` PLAYBOOK.md → TASK: SESSION_END for full protocol.

---

## Repository Info

- **GitHub:** https://github.com/AndreBro007/getcarwise-docs
- **Managed by:** Claude Automation (Session-end protocol)
- **Strategy:** Root-level files, structured naming, cross-referenced in carclever-widget
- **Last Updated:** Aug 26, 2026

---

**First session docs ready to be added:**
- AUDIT_WEBSITE_APP_INFRASTRUCTURE_20260826.md
- PLAN_PRIORITY_3_WEBSITE_REVIEW_20260826.md
- PROTOCOL_SESSION_END_20260826.md
