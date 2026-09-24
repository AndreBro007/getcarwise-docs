# Claude handoff — Task #78 multi-route measurement and route readiness
**24 September 2026. Status:** engineering preparation only. Read [the execution plan](PLAN_TASK78_MULTIROUTE_MARKETING_EXECUTION_20260924.md), Task #78 and Task #79 in `carclever-widget/TASKS.md`, and `carclever-widget/STATE.md` using the normal lane checkpoint. Do not redo the completed research phases. Preserve the passive no-discretionary-testing period through September 30 and coordinate with the concurrent Task #79 Free-tier work.

> **Superseded first task (Sep 24):** ChatGPT completed the read-only audit in [AUDIT_TASK78_MULTIROUTE_MEASUREMENT_READINESS_20260924.md](AUDIT_TASK78_MULTIROUTE_MEASUREMENT_READINESS_20260924.md). Do not send Claude the “exact first instruction” at the bottom of this historical brief or duplicate the audit. Claude should continue Task #79 independently; any later Task #78 engineering implementation requires a specific prioritized gap and André's separate approval.

## Historical first-task specification (completed by ChatGPT)

**Perform a read-only audit** of current repository code, deployed configuration already documented in GitHub, analytics/event definitions and existing landing links for the routes below. Produce a concise evidence-backed gap table. No development, testing, ad or production action is requested in this first task.

The outcome is a reviewable answer to: “For a person arriving from a distinct Google, Reddit, organic, app-directory or publisher source, which steps can we actually observe through site, app and Impact approved/rejected action, and where does the chain break?” Do not manufacture clicks or invoke the app to answer it. Mark inaccessible dashboards/config as **unverified**, not broken.

| Route / existing surface | Inspect read-only | Question and acceptance evidence |
|---|---|---|
| Search → used page 934 | Existing page copy, Impact Used href `https://edmunds.sjv.io/c/7765200/3949600/52125`, GA4 consent/event design, CarClever path | Confirm current link in source or public DOM if necessary without clicking; distinguish GA4 page/CTA events from Impact generated click and approved action. The link was already checked live Sep 24; do not propose a blind repair. |
| New/Trade-in → page 828 and Decision Center 1160 | Existing contextual CTAs/assets 3949597, 3949600, 3949601 and app wayfinding | Map which buyer intent has which action, what could be tagged, and what is actually measured. Avoid putting all offers on every page. |
| Search/organic/direct → live old @CarClever | `/try-carclever/` and directory link, known old Used/CPO feature contract, app invocation/log/event availability, dealer/Impact path | State whether a source can survive a direct app handoff through a real approved action. If not, treat paid app route as awareness/use; do not claim install or lead conversion. Old app depends on Fractal; pending newer apps cannot be called live. |
| Reddit paid → GetCarWise or app | Existing destination and source tagging design, end-to-end partner link exposure | Define a brand/app outcome that is valuable and observable without counting social-origin Edmunds commission under supplied §3.B. A site detour cannot disguise source. |
| Publisher/creator → site/app | UTM and permitted disclosed property treatment | Show route-specific source labels without personal data or sub-affiliate/source masking. |
| Partner handoff | Impact asset and link construction, allowable Sub IDs/Shared IDs via Impact UI, action-status report | Identify exact record that would reconcile a *qualified* New, Used or Trade-in click to pending/approved/reversed lead; account access and source visibility may remain unverified. Required tracking link/creative must remain unmodified. |
| Cost/viability Task #79 | Existing Fractal/Auto.dev dependency and Free-tier notes | Reference Task #79's owner and unresolved regression/rollback, do not rerun tests during the quiet window or duplicate its implementation. |

## Deliverable format

1. **Observed vs unverified:** route, source file/config or read-only UI evidence, existing event/link, attribution break, impact on a marketing decision. Do not infer that 17 “no referring domain” Impact clicks came from MCP apps.
2. **Minimum implementation proposal:** the smallest route-specific code/config or page change that would close a material gap, in dependency order. For each, give target file/page, event name and non-sensitive properties, Impact UI-generated tracking parameters where allowed, acceptance evidence, privacy/consent condition and a rollback. Include a “no change needed” row for verified items.
3. **Decision gates:** protect the Sep 28 GSC cohort; at Sep 30 report product/cost/analytics readiness. Flag work requiring André's separate approval: WordPress or production changes, analytics/pixels, ad accounts/billing, publications/outreach, subscription changes, app deployment. Draft PRs/specs can be prepared without merging or deployment if suitable.
4. **Marketing handoff:** one page of route G1, A and R readiness with yes/no/unverified for truthful destination, measurement, permitted handoff and reliable spend stop. State which question can be answered within days and which requires Impact's later action/lock window.

## Guardrails for any later approved implementation

- Follow `STATE.md` lane checkpoint protocol and preserve Claude's Task #79 work. Use a branch/draft PR for code where appropriate; do not change live WordPress, apps, campaign accounts or subscriptions in this first audit.
- Distinguish page 934's existing Used CTA from old CarClever access. Do not promise new inventory in the old app or VIN recall claims the current route does not support.
- No discretionary owner-generated app/API/affiliate clicks before Sep 30; historical Auto.dev usage is not a real-user cohort.
- Capture aggregate, consented events only. No VIN, ZIP, search free text or personally identifying data in UTM, analytics or Impact Sub ID.
- The supplied Edmunds agreement bars direct PPC→Edmunds and social-origin Edmunds traffic without express written permission; do not solve attribution by routing around those rules.
- Do not put a Google/Reddit pixel, create an Ads account, claim credit, set billing or change production simply to test this plan.

**Exact first instruction to Claude:** “For Task #78, perform only the read-only multi-route instrumentation/routing audit defined in `getcarwise-docs/HANDOFF_CLAUDE_TASK78_MULTIROUTE_MEASUREMENT_READINESS_20260924.md`. Use `PLAN_TASK78_MULTIROUTE_MARKETING_EXECUTION_20260924.md`, Task #78/#79 and `STATE.md` as source of truth. Return the observed/unverified gap table, minimum change sequence with acceptance/rollback, and G1/A/R readiness. Do not generate traffic or make production, ad, subscription or publishing changes. Update your GitHub administration lane only for the audit actually completed and verified.” 
