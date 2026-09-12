# CarClever Release Validation Ledger — started 2026-09-10

**Status:** ACTIVE living release record  
**Purpose:** Preserve a chronological, exact-SHA record of CarClever validation across local/CI tests, deployed environments, ChatGPT, Claude, OpenAI/Anthropic review gates, production promotion and post-release smoke tests.  
**Rule:** A release is not complete because code was written or because one host passed. Every production change must have a ledger entry, even when the platform itself does not require a new reviewed version.

## 1. Release-control model

Target flow:

`feature/fix → release/vN → exact candidate SHA → host validation → platform-specific production origin → submission/update → post-release smoke → review freeze`

Terms:

- **Preview:** Vercel build only; never a Git merge.
- **Release candidate:** exact SHA on `release/vN` accepted for host testing.
- **Platform production:** exact release SHA deliberately deployed/promoted behind the platform's submitted MCP origin.
- **Canonical merge:** optional later merge into `main`; not required for the current V2 platform releases and explicitly not done in the Sep 12 cutover.

## 2. Mandatory release record fields

Every candidate/release event must record version/release label, exact SHA, source branch, contract fingerprint, automated verification, deployed identity, host tests, exact submission origin, platform review state, production promotion, smoke tests, rollback point, known issues and any André-dependent sign-off.

## 3. Standard test layers

### Layer A — commit/contract tests

Build, typecheck with baseline discrimination, unit/custom regression tests, deterministic fixtures, MCP initialize/tools/resources, schema/description/annotation/resource-contract checks.

### Layer B — deployed identity

Prove correct Vercel project, target, branch, exact SHA, stable MCP URL, widget origin/CSP/resource metadata and isolation from unrelated projects.

### Layer C — baseline vs candidate

Compare effective user intent, tool arguments, hard constraints, preferences, widening/relaxation, evidence, ordering, latency and host omissions. Live inventory VIN identity need not be identical across runs.

### Layer D — AI hosts

Material contract/releases must be exercised in both ChatGPT and Claude because host routing/tool construction is part of the product.

### Layer E — exact production/submission origin

Run critical checks against the exact hostname submitted to each platform.

### Layer F — post-release

Verify production SHA, positive/negative behavior, widget rendering, external links, runtime health, rollback point and any first-seen regression.

## 4. Prompt-pack baseline

The current release pack covers exact make/model/budget/location; practical-needs model resolution; hybrid/PHEV/electric required/preferred; exact VIN; best-for-budget/cheapest/newest/lowest-mileage/lower-risk; direct fields including AWD/transmission/color/cylinders; trim required/preferred; location variants; CPO/history evidence; thin-result widening; widget/link actions; and negative non-inventory questions.

## 5. V2 release identity — FINAL SUBMISSION CANDIDATE

- Branch: `release/v2`.
- Exact release/submission SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.
- Parent: `abb933cc47aa0f093a7f955ac2ae0507ec7f9b08`.
- V1/main remains `e7c8634fdd631c7bb05c83c02daeb1ab7f7bbb6` and was not merged with V2.
- V3 remains paused at `v3.1-3.3/card-first-check-vehicle` commit `4032feb`.
- Public V2 tools: `find_matching_vehicle`, `resolve_dealer_url`.
- V2 contract includes `vehicleNeeds`, `electrificationTypes`, `electrificationRequirement`; legacy `goals` is not part of the V2 schema.

## 6. 2026-09-12 — OpenAI production/submission record

### Production identity

- Vercel project: `ccfmc-dev-v2`.
- MCP URL: `https://carclever-oai.getcarwise.app/mcp`.
- Production widget origin: `https://carclever-oai.getcarwise.app` via `NEXT_PUBLIC_WIDGET_ORIGIN`.
- Exact submitted code: `b8b07d8`.
- OpenAI domain verification completed.

### Final scan/contract verification

PASS:

- custom MCP URL correct;
- `openai/widgetDomain` = `https://carclever-oai.getcarwise.app`;
- CSP resource domain contains the same custom origin;
- auth NONE;
- `vehicleNeeds` and electrification fields present;
- no legacy `goals`;
- both tools readOnly=true, openWorld=true, destructive=false.

### Final OpenAI host smoke

PASS:

1. Normal inventory search: `large suv under 60k in 90210` — CarClever invoked, listing carousel rendered, coherent matches.
2. Exact VIN Buyer Check: `Check VIN 4T1DAACK6SU582551 for red flags before I buy it.` — exact VIN path, Buyer Check card rendered; live status at test time reflected one reported accident/caution.
3. Self-contained listing-presence/availability: `Check availability for the 2025 Toyota Camry with VIN 4T1DAACK6SU582551.` — CarClever invoked, exact VIN/listing flow and Edmunds destination returned.
4. Negative non-inventory cases were included in the submitted test set: brake-pad maintenance, F-150 towing-capacity knowledge and hybrid-vs-gas general comparison.

A prior natural VIN run wandered into host web search and failed to render a card; the later isolated/new-domain tests passed. Recorded as host tool-selection behavior, not an endpoint failure.

### OpenAI submission state

- Submitted 2026-09-12.
- App: `CarClever - Find My Car`, version 1.0.0.
- Current state: **REVIEW**.
- Full record: `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`.

## 7. 2026-09-12 — Anthropic controlled V1→V2 cutover/update

### Production promotion

PASS:

- Existing Vercel project: `carclever-find-my-car`.
- Existing submitted MCP retained: `https://carclever-find-my-car.vercel.app/mcp`.
- Exact promoted source: branch `release/v2`, SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.
- Vercel deployment ID observed: `dpl_9vP17yqXx5fdfV2uTWfAenvfYFD2`.
- State: READY.
- Target: production.
- Deployment metadata records action `promote` and original preview deployment `dpl_GxdqgK2Av4GWnbF8d7Mc8TxCw2hh`.
- Main remained untouched.

### Endpoint liveness

PASS:

Opening `https://carclever-find-my-car.vercel.app/mcp` in a normal browser returned JSON-RPC error `-32000` / `Method not allowed`, which is the expected response to a browser GET and proves DNS/TLS/route reachability.

### First Claude host attempt after cutover

**INCONCLUSIVE / CACHE MISMATCH, not a server failure.**

A new/recreated Claude connector still exposed a stale base-connector `find_matching_vehicle` tool snapshot containing legacy V1 `goals`, while the separately visible `CarClever V2 Test` tool exposed the correct V2 fields (`vehicleNeeds`, electrification fields). Claude displayed `Unable to reach CarClever - Find My Car` around the invocation even though the endpoint was demonstrably reachable and tool discovery could see the connector. This strongly indicates stale host connector/tool metadata after replacing the code behind the existing submitted URL.

No code change was made in response. The historical Claude rendering fix — omission of `_meta.ui.domain` for cross-host compatibility — remains present in V2 and is not the current failure mode.

### Anthropic listing update

PASS:

- Anthropic Edit Server flow opened while listing was already `In review`.
- Sync/Rescan from server run; current server tool count reported as 2.
- Public Description updated to the same final V2 marketing description submitted to OpenAI.
- Name, slug, category, links, branding and other established form answers retained.
- Existing policy decision preserved: do not proactively rewrite the already-tested V2 tool descriptions unless Anthropic gives concrete feedback or a reproducible defect requires it.
- Saved/submitted successfully.
- Directory screen confirmed `In review` and `Updated: just now` on 2026-09-12.
- Full record: `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`.

### Remaining Claude post-update smoke

PENDING USER RETEST after cache reset/fresh connector:

1. Confirm base `CarClever - Find My Car` tool schema now shows V2 fields (`vehicleNeeds`, electrification fields) and no `goals`.
2. Baseline: `Find a used Honda CR-V under $25,000 with less than 60,000 miles near 90210.`
3. Exact VIN: `Check VIN 4T1DAACK6SU582551 for red flags before I buy it.`

Do not interpret changing live VIN status as a regression by itself.

## 8. Current review/release gates

| Gate | State |
|---|---|
| V2 contract/code candidate frozen | PASS — `b8b07d8` |
| OpenAI exact production origin | PASS |
| OpenAI final production smoke | PASS |
| OpenAI submission | REVIEW |
| Anthropic exact production SHA | PASS |
| Anthropic endpoint reachability | PASS |
| Anthropic listing rescan/update | PASS / IN REVIEW |
| Claude refreshed-schema smoke | PENDING cache reset/retest |
| Long-term Anthropic Vercel production-branch safety | PENDING confirmation |
| V1/main protection | PASS — untouched |
| V3 pause | PASS |

## 9. Known issues / follow-up

- Claude can cache connector/tool metadata across a backend cutover. A stale schema must not be mistaken for proof that the production endpoint is serving V1.
- Confirm the Anthropic Vercel project's long-term production branch/release behavior so a future `main` push cannot silently replace the manually promoted V2 production deployment.
- Do not change V2 during either review except for platform-requested corrections or a reproduced evidence-backed defect.
- PR #1/#2 remain stale draft housekeeping and must not be merged.

## 10. Rollback / preservation

- V1 main remains preserved at `e7c8634...`.
- The previous Anthropic V1 production deployment remains a rollback candidate through Vercel deployment history.
- V2 release history remains on `release/v2`; no forced mainline merge was used for this cutover.

## References

- `CURRENT_V2_STATE_20260909.md`
- `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`
- `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`
- `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md`
- `AUDIT_CARCLEVER_DUAL_PLATFORM_VERCEL_FEASIBILITY_20260911.md`
- `AUDIT_V2_ANTHROPIC_SUBMISSION_COMPLIANCE_20260910.md`
- `TEST_CARCLEVER_SUBMISSION_BASELINE_20260911.md`
- `TEST_CARCLEVER_V2_CROSS_HOST_MANUAL_ACCEPTANCE_20260910.md`
