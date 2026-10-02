# OpenAI submission process and screens — session checkpoint
Date: 2 October 2026 (Australia/Brisbane)
Status: Official documentation and owner screenshots reviewed; corrected package draft and reusable ZIP builder prepared, not uploaded.
Owner: ChatGPT Business/Strategy.

## Session verification
Fetched all seven required widget administrative files fresh. Dynamically listed the complete getcarwise-docs root inventory. Docs comparison from ChatGPT checkpoint 196097e4a09a5265ebb81d88392a36a432d65a8a to main was identical. Widget comparison from 3e139eceb19cd9c20b1ffc68651abb3ad3be5a74 found one STATE-only closeout commit, 1be947a278f018698cb61e7ee3ec07c0f46199bb. Read its diff and spot-verified the linked Reddit tracker in full. Read both OpenAI submission records, V2 reconciliation and portfolio status report in full.

Current administrative evidence records Find My Car as published. The older submission and portfolio reports retain historical REVIEW labels; these do not override the later confirmed publication in STATE/DECISIONS. Anthropic/Muse outcomes have not been newly confirmed. Auto.dev cancellation/2 October expiry and Fractal 14 October renewal are recorded owner facts; no new subscription decision made.

## Current official workflow

| Screen/action | Documented role |
| --- | --- |
| Upload new or existing plugin | Upload a ZIP and select verified publisher identity. |
| Metadata & Skills | Package version, listing/skill findings; package changes require another ZIP. |
| MCPs | Server connection, domain verification, tools and scan findings. |
| Review information → Review details | Test materials and private reviewer access. Initial MCP review requires five positive and three negative cases plus a video. |
| Submit for review / Publish plugin | Review and publication are separate actions. |
| Published version → … → Download release ZIP | Starting point for updating an existing submission created through the previous form. |
| MCPs → Issues → Rescan | Hosted tool changes are checked separately; eligible changes also receive daily scans. |
| Live definition / Held update | Previously approved metadata remains active while an existing tool update is held; new tools await approval. |

Source: [Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission), fetched 2 October Brisbane time. Imported ZIP test cases are read-only; revise them in the package. Only one review can be active.

## CarClever application and limits
Recommendation: inspect the existing CarClever entry first. For a future listing/assets update, start from its published release ZIP and preserve identity/configuration. No replacement plugin or immediate resubmission has been justified by this read.

Actual account screens, migration status, warnings and current legacy-app review status remain unobserved. Next: André supplies the current Plugins overview/detail screenshot; inspect one screen at a time.

The dedicated submission guide says server-URL changes require support, while the MCP review page retains older origin/path restrictions. Treat the dedicated guide as the current workflow; do not authorize an endpoint change from these mixed instructions. Relevant source: [MCP review requirements](https://developers.openai.com/plugins/deploy/app-review).

The historical OPENAI_SUBMISSIONS_INDEX.md reference returned 404 at widget root; no archive contents or missing assets inferred. No required session-start read failed.

No portal action, submission, scan, package creation, code, deployment, public communication or spending occurred.

## Owner evidence and ZIP inspection — 2 October, later in same session

### Confirmed dashboard observations
André supplied five screenshots and the v3 rejection email:
- Old CarClever: publication v2.0.0; package v3.0.0 Changes required. MCP configured/domain verified; nine listed tools Live; latest MCP scan reports no issues, last checked two days ago.
- Find My Car: publication v1.0.0; no active package review; Metadata & Skills reports no issues. MCP configured/domain verified; both tools Live. Orange/red tab dot accompanies Complete MCP setup, with no last-checked dates.
- New & Used Cars: not published; v1.0.0 not submitted.

A clean current tool scan does not retrospectively approve the rejected v3 package. Publication, package review and MCP checks are separate states. Find My Car's dot is an observed setup/discovery warning, not evidence of an annotation rejection. Stale migration state is a hypothesis only.

### Independent live annotation check
Read tools/list from https://carclever-oai.getcarwise.app/mcp successfully (HTTP 200); no vehicle search or Auto.dev call initiated.

| Tool | readOnlyHint | destructiveHint | openWorldHint |
| --- | --- | --- | --- |
| find_matching_vehicle | true | false | true |
| resolve_dealer_url | true | false | true |

These match read-only public listing retrieval/link resolution. No null or omitted values in either annotation object. Future V3/check_vehicle metadata was not tested or approved by this check.

Old Fractal endpoint metadata request returned HTTP 403 from this environment. Its current annotations were not independently fetched. André supplied the Fractal fix report: search-used-cars, analyze-deal-risk and calculate-affordability now openWorldHint true. Screenshot confirms clean current scan, but not every individual boolean.

### Annotation audit cautions
The current guidelines distinguish public/open-ended entities from bounded private accounts/catalogs; merely calling an externally hosted API does not automatically mean openWorldHint true. The three reported fixes are reasonable for public vehicle/recall data.

Garage save/remove/list may be closed-world, but persistence still requires readOnlyHint false for save/remove and destructiveHint true for deletion. The historical v2 export already has those write/delete annotations. Review get-vehicle-details if it fetches public vehicle/recall information; it was not among the three reported fixes. Review resolve-dealer-url according to whether it resolves arbitrary public destinations or only transforms bounded cached values. Do not infer these two are correct solely from “local” or “URL builder.”

Current plugin guidelines say annotation justifications are no longer required, unlike the pasted rejection email and some older review-page wording. Preserve factual explanations for any appeal/field that still requests them; explicit accurate booleans remain essential.

### Tool-description diagnosis — likely targets, not a confirmed reviewer explanation
Current connector-exposed old search description includes “Highest Priority,” “Very High Priority,” and “Call this first.” These are strong candidates for the rejection because they prescribe tool preference rather than simply describing matching user intent.

The archived v2 submission also labels comparison “Compare Listings & Find the Best Option,” search “Find & Compare Used Cars for Your Situation,” and the read-only list “View & Manage Your Saved Cars.” These titles should be checked against the current endpoint: the first is promotional; the second may imply comparison beyond the search operation; the third may imply editing. These are historical titles, not verified v3/current ones. Technical identifiers shown in the screenshots are already understandable; no mass rename is proposed.

The affordability connector description claims “current APR rates” and “accurate results”; risk description claims “title brand verification.” Check those against the current Free-tier paths before reuse. Estimates and reported/unavailable evidence should remain explicit.

Proposed search description, for André/Fractal review:
> Searches current U.S. used-vehicle listings when a user requests vehicles for sale matching a budget, location, make/model, vehicle category, features or practical buying needs. Returns listing details, available history/certification evidence, Deal Scores and viewing links. Default Recommended sorting combines deal score, budget fit and recency; other supported sorts include price and mileage. If the search expands beyond the requested area, disclose that scope. Use offset for additional results. Missing history or specifications remain unconfirmed. This tool does not independently establish safety, reliability, physical dealer availability or final sale price. Do not use for general automotive research, repair instructions, new-car configurators, lease quotes or non-U.S. inventory.

Proposed titles, preserving technical identifiers:
- search-used-cars: Search Used Vehicle Listings
- vehicle-comparison: Compare Vehicle Listings
- garage-list: List Saved Vehicles

Find My Car annotations pass the current check, but its live resolver description says “Prefers the Edmunds” and “never dead-ends.” The first can describe routing rather than promotion, but neutral wording and removal of the absolute guarantee would be clearer at its next metadata review. No change authorized/performed.

Proposed resolver description for later review:
> Returns an Edmunds vehicle-page link for the supplied VIN, make, model and year when available; otherwise returns a make/model search link. The dealer listing URL is not the resolved destination. This tool only returns a link and does not reserve a vehicle, confirm physical dealer availability or complete a purchase.

### What the downloaded ZIPs actually contain
Inspected both archives directly:
- app-698c1e794a3481918fad0affa7757784-3.0.0.zip
- app-6a85781882508191b1794888c5bbf728-1.0.0.zip

Each has exactly one file: .codex-plugin/plugin.json. It includes package name/version, author, description, listing interface text, four policy/support URLs, category, empty capabilities and three starter prompts. Neither contains tool definitions/annotations, .mcp.json, assets, skills or review/publication extensions. These exports are not complete backups of the MCP app or its review materials. Icons shown in the portal are not embedded in these ZIPs.

For an existing app update: retain its package identity; extract, edit the manifest/version and intended listing changes, include needed assets, then compress the contents with .codex-plugin at archive root. Upload through that existing entry's Upload new version. Validate its attached MCP, assets, countries/commerce, reviewer materials and checks before submission. Whether the migration export preserves existing server association/assets must be verified in a draft; not assumed.

For a new MCP-backed submission: create a complete supported package, including remote MCP configuration and referenced images, listing URLs and review materials. Portable root plugin.json + mcp.json is the recommended new-package layout; the exported compatibility .codex-plugin/plugin.json layout remains supported. Hosted application code stays on its existing server and is not put in the submission ZIP. Do not add unsupported .app.json app references/hooks to a public-submission ZIP.

Initial MCP review requires five positive/three negative cases and video; copy nothing untested from historical VIN fixtures. The Find My Car exported starter VIN is an old inventory fixture, so review its usefulness before an eventual listing update. This is not an instruction to run inventory tests now.

### Practical next steps
1. Find My Car: owner already rescanned and confirmed no tool issues. This step is complete. Application V2 is approved/live; exported package version is 1.0.0. Any remaining Complete MCP setup dot is a separate portal-state question. Do not request another scan or conflate it with old CarClever's rejected package 3.0.0.
2. Old CarClever: verify current titles/descriptions and the two annotation cautions, then have Fractal apply approved wording. No priority-tier language; preserve functional scope.
3. Prepare a complete updated package/draft for review when André chooses to proceed. No upload, scan, reconnection, appeal, submission or publication was performed here.

### Source and access limits
Read current official plugin guidelines, submission/package guides, MCP review and submission-errors pages. The email's tracked Help Center link did not resolve; searches did not establish its exact target. Do not claim that article was read. Use these direct official sources:
- https://developers.openai.com/plugins/plugin-guidelines
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/app-review
- https://developers.openai.com/plugins/deploy/submission-errors

Corrected archive discovery: OPENAI_SUBMISSIONS_INDEX.md exists under openai-submissions/, not widget root. Read it and fetched the historical v2 export for title/annotation evidence. Historical statuses remain superseded by today's dashboard screenshots.

No application code, deployment, portal setting, package upload, lead/affiliate click, appeal, public message or spend changed. Original ZIPs remain unchanged.

## Concrete package preparation — owner clarification, later 2 October

Owner clarified Find My Car application V2 was submitted and is live, not V3. Owner already supplied/extracted ZIPs and completed the clean rescan; repeated requests to do those steps were incorrect. Find My Car application V3 remains paused/unsubmitted. Old CarClever package 3.0.0 is the rejected version, with package 2.0.0 published and application code 3.0.0 already live including Recommended sort.

Current submission guide explicitly says rejected packages need a corrected ZIP; update package contents and version. Prepared old-carclever-3.0.1-draft.zip from the supplied old 3.0.0 export, preserving identity/publisher/URLs/category/capabilities and compatibility path. Updated factual listing text/subtitle/prompts and version only. Reopened and verified ZIP integrity, JSON, field lengths and unchanged fields. No server code bundled or changed. Draft not submitted-ready: existing portal icon/review materials and connection need checking on import; URLs preserved, not newly reverified. No portal action performed.

Prepared carclever-zip-toolkit.zip with a reusable Python 3 ZIP builder, factual old listing JSON, instructions for both old/new identities and a concrete Fractal description task. Toolkit is not the portal upload. Both artifacts saved successfully as user-facing files. No special OpenAI generator is needed; Python json/zipfile recreate the exported compatibility format. No new Find My Car package was generated. Future package version is independent of application V3.

Recommended next: remove old search priority directives on server, then upload the 3.0.1 draft to existing old CarClever, verify saved draft/retained connection/assets/review information, submit corrected package and publish after approval. No need to submit solely to deploy compatible Recommended sorting: hosted changes use MCP scans independently. Leaving rejected package unresolved retains published 2.0.0 metadata. No guarantee of future approval implied.


## Session closeout — 2 October 2026, 13:39 Brisbane — corrected package submitted

This dated update supersedes earlier same-session statements that the draft had not been uploaded or submitted and that server-description work remained pending.

André ran the Fractal agent's small description/AI-visible URL-suppression changes, passed preview testing and deployed to production. He rescanned the old MCP; screenshot showed all nine tools Live and no issues. Independent old-plugin tests: search (six listings), comparison (two), risk and affordability succeeded with dealer_vdp_url absent; temporary garage save/list/remove succeeded, garage-list returned null and final garage was restored empty. Private get-vehicle-details and resolve-dealer-url were not callable in this session; raw Fractal metadata remained 403-blocked. Full all-nine-tool independent verification is not claimed. Session connector descriptions remained cached; they were not treated as current deployed metadata. Internal affiliate resolution was preserved per Fractal's report/owner preview, not independently destination-clicked.

Uploaded 3.0.1 initially reported App icon required: original export had no icon. Corrected ZIP adds root interface.logo and interface.composerIcon pointing to ./assets/carclever-icon.png plus actual image bytes. André selected his existing blue square 128 × 128 PNG; it meets documented ≥48px requirement and portal accepted it. Metadata screen showed No Issues. Original manifest identity, URLs and other fields were preserved; version/listing/release notes reflect the correction.

André submitted on 2 October; final screenshot confirms old CarClever Version 3.0.1 · In review, Publication Version 2.0.0, MCP Configured. Package 3.0.0 remains rejected history. Approval/publication of 3.0.1 is pending. Hosted Fractal application code 3.0.0 was already live, including Recommended sort. New Find My Car application V2 remains approved/live, exported published package 1.0.0; new application V3 paused/unsubmitted.

Documentation says rejected submissions need a corrected ZIP and updates change package version; it does not explicitly promise overwriting a rejected same-version entry. This session used 3.0.1 successfully; same-version uploads corrected its unsubmitted draft. Only one active review allowed; wait for outcome before another upload unless deliberately cancelling review.

Saved reusable [guide](GUIDE_OPENAI_SUBMISSION_ZIP_20261002.md) and [Python 3 builder](scripts/build_openai_submission_zip.py), plus user-facing toolkit containing guide/script/square icon/old listing example/final submitted reference ZIP. Builder now bundles icon assets, validates required image references, preserves unrelated entries, supports explicit same-version draft correction and verifies ZIP integrity. Tested next-version build, same-version draft build, extra-component preservation and missing-icon rejection. Portal/server/policy review remains separate.

Current submission-error reference still asks for annotation justifications; guideline wording differs. Retain factual justifications wherever requested by portal/reviewer. Earlier guideline-only interpretation must not be read as grounds to ignore the rejection email.

No ChatGPT application code or deployment, affiliate click/lead, new Find My Car submission, publication, subscription or spend change. Remaining action: review outcome, remedy any specific new feedback, publish approved 3.0.1 when André chooses.


### New CarClever annotation check — owner closeout clarification, 2 October 2026

New CarClever – Find My Car's two live tools, find_matching_vehicle and resolve_dealer_url, were checked independently: readOnlyHint=true, destructiveHint=false and openWorldHint=true, explicitly set on both and consistent with their current public-data/link-resolution behavior. Owner already completed a clean scan. The submission screen still shows a red/orange MCP-tab dot; no annotation defect was found and the dot alone is not evidence of one. Leave the current live application V2/published package 1.0.0 unchanged. Reassess actual portal findings at the next new-app package submission; do not speculate that a stricter future review has already failed. Future application V3 annotations were not checked and remain outside this live two-tool verification.
