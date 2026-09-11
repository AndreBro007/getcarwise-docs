# CarClever Dual-Platform Vercel Feasibility Audit — 2026-09-11

**Status:** VERIFIED READ-ONLY FEASIBILITY AUDIT

**Purpose:** confirm whether the exact tested V2 release can back both the new OpenAI branded MCP origin and, later, the existing Anthropic-submitted MCP origin without merging V2 into `main` or changing the Anthropic URL.

**No deployment, DNS, domain, Git branch, PR, connector, or submission state was changed.**

## Executive conclusion

Yes — the intended two-channel architecture is technically feasible with the current repository/Vercel setup.

Target steady state:

- OpenAI: `https://carclever-oai.getcarwise.app/mcp` → exact tested V2 release
- Anthropic: `https://carclever-find-my-car.vercel.app/mcp` → the same exact tested V2 release, only after the Anthropic review/change gate is explicitly cleared

The two channels do not require separate codebases or a V2 merge into `main`.

Current immutable release candidate unless André separately authorizes a code change:

`a5d96960792d1de3cd4eaf81ccef0a1515acf04f`

## Verified Vercel topology

The linked Vercel account/team currently contains separate projects connected to the same GitHub repository `AndreBro007/carclever-find-my-car`, including:

- `ccfmc-dev-v2` — V2 test/release project
- `carclever-find-my-car` — existing V1/Anthropic production project
- `ccfmc-dev-v3` — paused V3 project
- `ccfmc-dev` — historical short-URL test project
- `carclever-v2-schema-probe` — temporary schema-research project

The current V2 project `ccfmc-dev-v2` has a READY **production** deployment at exact SHA `a5d96960792d1de3cd4eaf81ccef0a1515acf04f`, branch `release/v2`.

## Critical feasibility evidence for the Anthropic URL

The existing Vercel project `carclever-find-my-car` is already receiving/building `release/v2` as Preview deployments because it is connected to the same GitHub repository.

Most importantly, it already has a READY Preview deployment of the exact final tested V2 SHA:

- project: `carclever-find-my-car`
- deployment: `dpl_24BPVwbCwhjxmAk1zQjtAiqUu4Dd`
- Git ref: `release/v2`
- Git SHA: `a5d96960792d1de3cd4eaf81ccef0a1515acf04f`
- state: READY
- target: Preview (`target: null`), **not Production**

Therefore the exact V2 source already builds successfully inside the very Vercel project that owns the submitted Anthropic hostname `carclever-find-my-car.vercel.app`.

This proves that a later same-hostname Anthropic cutover does not require moving repositories, renaming the Vercel project, changing the submitted URL, or merging V2 into GitHub `main`.

When André clears the Anthropic gate, Engineering can deliberately make the exact V2 deployment the Production deployment for that existing project (for example by a controlled promotion or equivalent production-branch/release action), then verify that `https://carclever-find-my-car.vercel.app/mcp` serves the intended SHA and current MCP contract.

Do **not** perform that promotion while the active Anthropic review/change gate remains closed.

## Why a manual preview promotion alone is not enough as the permanent operating model

Vercel supports promoting a Preview deployment to Production. That is useful for a controlled cutover, but the project’s future Git/Production-branch behavior must also be reconciled so a later V1 `main` push cannot silently replace the V2 production deployment.

Before the Anthropic cutover, Engineering must inspect and explicitly set/confirm the project’s intended long-term Production branch or release process. `main` should remain untouched as the preserved V1 Git line unless André separately authorizes a Git merge.

## OpenAI branded-origin feasibility

The V2 project `ccfmc-dev-v2` currently serves the exact tested SHA as Production. A custom domain can be assigned to a Vercel project, so `carclever-oai.getcarwise.app` can be attached to the V2 production channel without changing the Git release source.

Vercel documents `VERCEL_PROJECT_PRODUCTION_URL` as the project production domain and, in framework variants, as the shortest production custom domain or `vercel.app` domain. Current V2 code uses this variable in `getAppOrigin()` when `VERCEL_ENV === "production"` for widget/CSP origin metadata and image-proxy URLs.

This means the custom-domain step must include an explicit runtime verification after the domain is attached: inspect the MCP widget/resource metadata and prove that the deployed production origin resolves to the intended `carclever-oai.getcarwise.app` value (or otherwise remains valid for the host). Do not assume this from DNS success alone.

If the runtime origin metadata does not resolve correctly after domain attachment, that is a real release blocker requiring a narrowly-scoped Engineering fix and re-test before submission. Do not submit around it.

## Important current code behavior

`lib/results-card.ts` on `release/v2` contains:

- Production: `https://${VERCEL_PROJECT_PRODUCTION_URL ?? "carclever-find-my-car.vercel.app"}`
- Preview: `https://${VERCEL_BRANCH_URL ?? VERCEL_URL ?? "carclever-find-my-car.vercel.app"}`

That design is favorable for the later Anthropic cutover because the production project’s canonical Vercel domain is already `carclever-find-my-car.vercel.app`.

For OpenAI, the custom-domain smoke must specifically verify `openai/widgetDomain`, CSP `resourceDomains`, and proxied-image URLs after `carclever-oai.getcarwise.app` is attached.

## Recommended two-stage execution

### Stage A — OpenAI now

1. Keep Git release source fixed at `release/v2` SHA `a5d9696...`.
2. Use `ccfmc-dev-v2` as the current V2 production project unless Engineering identifies a concrete reason a separate permanent OpenAI Vercel project is safer.
3. Attach `carclever-oai.getcarwise.app` and configure DNS exactly as Vercel instructs.
4. Verify TLS/domain status.
5. Verify exact deployed SHA.
6. Verify MCP initialize/tools/schema and widget/resource-origin metadata through the custom hostname.
7. Run the minimal production-origin smoke bank.
8. Only then put the new hostname into the OpenAI resubmission.

### Stage B — Anthropic later, only after André clears the gate

1. Keep the submitted URL unchanged: `https://carclever-find-my-car.vercel.app/mcp`.
2. In the existing `carclever-find-my-car` Vercel project, use the already-proven V2 build path and deliberately make the exact tested V2 release the Production deployment.
3. Confirm the long-term Production-branch/release setting so a subsequent V1 `main` push cannot overwrite V2 unexpectedly.
4. Verify exact SHA and MCP metadata at the unchanged submitted URL.
5. Run a short Claude smoke bank.
6. Preserve a documented rollback point to the current V1 production deployment.

## What Claude Engineering must NOT do

- Do not merge `release/v2` into `main` just to serve the Anthropic URL.
- Do not change the Anthropic MCP hostname.
- Do not touch paused V3.
- Do not merge or clean the two stale PRs as part of this release operation.
- Do not make opportunistic V2 code changes during domain/deployment work.
- Do not assume a custom domain is safe because DNS resolves; verify MCP/widget origin metadata.
- Do not promote V2 into the Anthropic production alias until André explicitly clears the Anthropic review/change gate.

## Platform evidence

Vercel documentation confirms:

- custom domains can be assigned to a specific project;
- Preview deployments can be promoted to Production;
- Production deployments serve the project production domain;
- `VERCEL_PROJECT_PRODUCTION_URL` exposes the project production domain.

Anthropic’s current remote-MCP documentation confirms that Claude connects to the exact configured remote MCP URL from Anthropic cloud infrastructure. Keeping the submitted URL stable while changing which tested release the server serves is technically compatible with that remote-MCP model; directory-review policy remains a separate governance gate and is why no Anthropic production change is authorized yet.

## Decision implication

The architecture does **not** require us to choose between the OpenAI branded domain and preserving the Anthropic submitted domain. Both can point to the same V2 release through separate Vercel production channels.

The next Claude handoff should therefore be extremely narrow: **OpenAI front-door implementation only**, while explicitly reminding Claude that the same V2 SHA must later be promoted behind the existing Anthropic project/URL after its gate clears.