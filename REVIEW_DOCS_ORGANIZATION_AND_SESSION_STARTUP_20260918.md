# Review: getcarwise-docs organization and session startup

**Date:** 2026-09-18 (Australia/Brisbane)  
**Author:** ChatGPT — Business/Strategy lane  
**For:** André and Claude  
**Status:** Recommendation only. André has requested assessment, not implementation approval. Existing startup requirements remain in force. No files have been moved and no operating instructions have been changed.

## Recommendation

Keep the existing flat repository and stable filenames. Replace the repeated full-content startup fetch with **complete dynamic file discovery, review of changes since this lane's last verified session, and full reads of the documents relevant to the current task**.

Claude correctly identifies a scaling problem, but the proposed active/archive lifecycle adds recurring filing work while retaining most of today's startup load. No 14-, 21-, or 30-day filing window is needed.

## Verified evidence

The current GitHub API root listing contained **110 files: 109 dated documents and README.md**, with no directories. Every returned file was fetched in full, together with the seven required carclever-widget admin files. The documents total 1,031,018 bytes in the directory listing.

Using September 18 as the reference date, and retaining documents whose filename date is on or after the cutoff:

| Window | Cutoff date, inclusive | Dated files still read by default | Dated files moved to archive |
|---|---|---:|---:|
| 14 days | 2026-09-04 | 94 | 15 |
| 21 days | 2026-08-28 | 106 | 3 |
| 30 days | 2026-08-19 | 109 | 0 |

README would be an additional startup read. The 14-day proposal leaves about 88% of the dated-document bytes in the default fetch. It is a rolling age boundary, not a limit on file count or reading volume.

Repository facts that matter:

- The current README already repeats a September 12 production snapshot, release SHA, endpoint and remaining checks. Later migration/portfolio records contain September 16–17 updates. Maintaining another status table would create another place that can drift.
- `CURRENT_V2_STATE_20260909.md` was updated on September 16; `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md` contains September 17 updates. A filename date is not the date of the latest meaningful change.
- The 14-day rule would move both `PROTOCOL_CREDENTIAL_SECURITY_AND_LANE_SPLIT_20260902.md` and `PLAN_CARCLEVER_CONNECTOR_ANALYSIS_AND_MONETIZATION_ROADMAP_20260902.md`. The latter is still explicitly referenced by the ChatGPT-lane B4/B5 tasks. Moving it would not remove the need to retrieve it for those tasks.
- The September 7 V3 specification is only eleven days old on September 18. Its usefulness will not automatically end when it passes fourteen days.
- The original discovery failure had two documented causes: a hardcoded file list and session-launch instructions that did not match the repository playbook. Moving files and changing only PLAYBOOK would not fix the second cause.

Sources: [current repository](https://github.com/AndreBro007/getcarwise-docs), [README](https://github.com/AndreBro007/getcarwise-docs/blob/main/README.md), [PLAYBOOK](https://github.com/AndreBro007/carclever-widget/blob/main/PLAYBOOK.md), [TASKS](https://github.com/AndreBro007/carclever-widget/blob/main/TASKS.md), and [the September 2 protocol record](https://github.com/AndreBro007/getcarwise-docs/blob/main/PROTOCOL_CREDENTIAL_SECURITY_AND_LANE_SPLIT_20260902.md).

## Assessment of Claude's proposal

| Proposal element | Assessment |
|---|---|
| Stop repeatedly fetching every historical document | Agree with the objective. Preserve complete discovery and explicit change detection. |
| Use two flat folders instead of month/topic categories | Simpler than a taxonomy, but still unnecessary movement. |
| Decide location from creation date | Mechanical, but unrelated to whether a document remains needed or has just changed. |
| Move old files whenever either AI next writes | Adds unrelated mutations to normal work. The window is only enforced when someone performs maintenance. |
| Maintain a README row for every file | Duplicates the repository listing. Every new file needs a row; every move needs a path change; descriptions may need maintenance too. |
| Assume important content is already in STATE/TASKS | Those files should link to the detailed specification or evidence. Copying all important detail into them increases duplication and startup volume. |
| Move files without changing contents | Existing path-based links and references would need checking across both repos and external handoffs. A move is not operationally neutral merely because its contents are unchanged. |
| Keep an explicit full-fetch fallback | Agree. Retain it for missing/incomplete review history, broad audits, and explicit user requests. |

An archived file is still available, but discoverability alone does not make it part of the next session's context. Conversely, a recent file can already be superseded. Neither location nor age should determine authority.

## Proposed operating rule

The following is the replacement procedure to adopt **only after André approves it**:

1. **Retain the existing core admin reads and lane boundaries.** Identify the actual task and its gates. Do not act on unrelated open tasks.
2. **Dynamically list the complete getcarwise-docs file inventory every session.** Discover actual paths, including any directories if they exist later. Do not replace the listing with a manually maintained index or a fixed list of known documents.
3. **Review every addition, modification, rename and deletion since this lane's own last successfully reviewed repository commit.** Fetch the current full contents of every added or modified document; inspect renames/deletions and any affected live references. This step is independent of whether a filename appears relevant, so an unlinked new protocol or a correction to an old file cannot be silently filtered out by title or age.
4. **Read the current task's linked specifications, handoffs and evidence in full, regardless of age.** Follow relevant references and search the full inventory when more context is needed. Previously reviewed but unchanged historical documents are fetched again only when the task needs them.
5. **If the previous review point or complete change list cannot be established, perform a full fetch to establish a baseline.** Do not guess a seven-/fourteen-day lookback, treat the other AI's review as your own, or silently accept an incomplete response.
6. **At normal session close, record the reviewed getcarwise-docs commit in that lane's existing STATE entry.** Keep ChatGPT and Claude review positions separate; advance only after the required reads succeed. Re-fetch and verify any documentation writes as already required.

One reviewed commit reference per lane is the only additional bookkeeping. It uses the existing session close-out rather than adding a new manifest, tracking document, scheduled job or service. It is necessary to distinguish “already checked” from “possibly unseen”; a single shared checkpoint could cause one AI to skip the other AI's new work.

GitHub already supports listing directory entries separately from fetching individual file bodies, and supports reading a known repository ref. This separation is supported by the [GitHub contents API documentation](https://docs.github.com/en/rest/repos/contents#get-repository-content). If the repository later exceeds the directory-listing limit, use the complete tree listing; do not accept truncated discovery.

This procedure reduces repeated reads of unchanged documents. It does not promise that every startup is only five files: a long absence or a large batch of changes warrants a larger catch-up.

## Easy retrieval without a second catalog

- Keep existing filenames and paths. There is one predictable place to find a document.
- Use the live repository listing and filename search for discovery; open the exact path through the connector when its contents are needed.
- Keep README short: repository purpose, naming convention, where current state/tasks live, and the startup rule. Avoid copying release status or maintaining a row for every document.
- Attach the exact current document link to the relevant existing task/state entry when the work changes. Store the detail once in its own document.
- Distinguish confirmed decisions, proposals, pending approvals and historical evidence in the document itself. Explicit supersession and verified updates determine authority; a newer filename alone does not.
- Continue normal state/task updates only where project state actually changes. Do not require updates to every admin file for every documentation write.

The unavoidable judgment is deciding what a task needs. No folder scheme removes that. This approach removes recurring filing decisions and preserves mechanical discovery of everything new.

## One-time adoption work for Claude and André

If André approves this recommendation:

1. Update the authoritative startup and close-out instructions in PLAYBOOK and the short README guidance.
2. Align **both ChatGPT and Claude project/session instructions** with the same rule. ChatGPT's current project instructions explicitly demand a complete full-content fetch every session; updating PLAYBOOK alone cannot override them. André must update any project settings the assistants cannot edit directly.
3. Establish each lane's initial reviewed-commit baseline using a completed full fetch. Do not invent or advance the other lane's baseline.
4. Confirm the procedure finds a newly added unlinked document, a newly edited older document, and an older task-linked specification. Confirm a missing baseline triggers the full-fetch fallback.

No repository reorganization is required. There is no implementation request here for the live application repository.

## Separate observation: admin document volume

The seven mandatory admin files contain about **1.56 million characters** in total; DECISIONS alone contains about 981,000 and STATE about 258,000. Repeated histories, stale banners and duplicated current-state summaries contribute to startup cost and ambiguity independently of getcarwise-docs.

This is an observation, not authorization for a wider cleanup. For now, avoid copying more specification/history into STATE or TASKS to compensate for archived documents. Any later consolidation should preserve decision history and existing gates.

## Session verification and decision status

- Required files: seven admin documents and all 110 dynamically discovered getcarwise-docs files successfully fetched.
- Scope: documentation-workflow review, authorized by André's request. No unrelated ChatGPT-lane backlog was started.
- Relevant recent widget commits: `7e16670`, `36e5c7a`, `1b30d5b`, `24b1f85` and `b7ef7c6` were inspected through their diffs/changed contents. The connector options are recorded as deferred proposals; the old CarClever close-out contains a pending production gate. Engineering claims were not independently live-tested in this review.
- Recent docs commits `bbd25d4` and `8b70de1` were inspected against their changed documents: the migration handoff and canonical phased plan do contain the claimed updates. The plan records the corrected resolution as temporary re-enabling of Auto-assign Custom Production Domains plus re-promotion.
- The latest old CarClever STATE entry contains both “user-verified live in production” language and an explicit “NOT YET DEPLOYED TO PRODUCTION” close-out. Production status should not be inferred from that entry. No deployment/submission gate is crossed by this review.
- Review snapshot: getcarwise-docs `bbd25d4e2efb38b928bde8839394ee5f713ead9b`; carclever-widget `7e166707e7b4a7f705f981450b2e4120049252d9`.
- **ChatGPT recommendation:** revise the proposal as above; do not adopt age-based active/archive filing.
- **André decision:** pending. This review records advice, not an approved change to the workflow.
