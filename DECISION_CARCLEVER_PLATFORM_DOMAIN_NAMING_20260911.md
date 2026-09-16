# CarClever Platform Domain Naming Decision — 2026-09-11, implementation updated 2026-09-16

**Status:** CONFIRMED BY ANDRÉ — platform naming implemented; Anthropic support-side listing URL replacement pending confirmation

## Decision

Use this naming convention for branded GetCarWise MCP production front doors:

`<product>-<platform>.getcarwise.app`

For CarClever:

- OpenAI: `https://carclever-oai.getcarwise.app/mcp`
- Anthropic: `https://carclever-anth.getcarwise.app/mcp`

The two platform front doors intentionally serve the same approved CarClever V2 release from the shared repository while remaining on separate Vercel production projects. This keeps platform review/deployment lifecycles from silently coupling.

## Implementation state

### OpenAI

Implemented before the 2026-09-12 resubmission:

- branded MCP: `https://carclever-oai.getcarwise.app/mcp`;
- Vercel project: `ccfmc-dev-v2`;
- exact approved V2 SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`;
- production widget origin and Scan Tools/domain verification completed;
- OpenAI submission remains in REVIEW.

### Anthropic

The earlier temporary exception—keeping the existing submitted Vercel URL while the review/change gate was unresolved—has now been operationally superseded.

On 2026-09-16:

- Anthropic support confirmed the pending listing MCP URL may be changed while review is still pending;
- `carclever-anth.getcarwise.app` was added to Vercel project `carclever-find-my-car`;
- Porkbun DNS was configured;
- Vercel shows Valid Configuration;
- HTTPS/TLS and MCP transport reachability passed;
- the new hostname resolves to exact approved V2 SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`;
- André completed a successful functional MCP-client test using `CarClever - Find My Car`;
- André emailed Marco/Anthropic support requesting replacement of the pending listing's current MCP URL with `https://carclever-anth.getcarwise.app/mcp`.

The old submitted endpoint remains live during migration:

`https://carclever-find-my-car.vercel.app/mcp`

The neutral alias `https://carclever.getcarwise.app/mcp` also remains live during transition.

**Directory-record gate:** do not state that Anthropic's stored listing URL has changed until support confirms the replacement.

## Production release controls

As of 2026-09-16 both platform production Vercel projects have **Auto-assign Custom Production Domains disabled** and therefore require deliberate manual promotion for production-domain movement.

Standing policy:

1. verify intended release branch and exact SHA before promotion;
2. use deliberate **Promote to Production** rather than allowing a routine Git push to take over a branded domain;
3. verify the branded MCP endpoint and exact production SHA after promotion.

This policy was introduced after a Sep 14 `main` deployment silently replaced the manually promoted Anthropic V2 production deployment. The incident was recovered and the approved V2 SHA restored.

## Vercel project display names

Current display names remain historical:

- OpenAI: `ccfmc-dev-v2`
- Anthropic: `carclever-find-my-car`

Proposed later housekeeping, after Anthropic confirms the support-side URL replacement and current reviews stabilize:

- `ccfmc-dev-v2` -> `carclever-openai`
- `carclever-find-my-car` -> `carclever-anthropic`

These are display-name cleanups only; the public branded MCP URLs above remain the production contracts. No rename has been performed yet.

## Scope boundary

This document records the confirmed naming/release architecture and its implementation status. It does not authorize application-code changes, project deletion, branch cleanup, or review-critical submission changes beyond the already-requested Anthropic URL replacement.

Detailed current records:

- `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md`
- `SUBMISSION_CARCLEVER_ANTHROPIC_V2_UPDATE_20260912.md`
- `UPDATE_ANTHROPIC_DNS_VERIFICATION_AND_RECOVERY_20260916.md`
- `PLAN_CARCLEVER_VERCEL_NAMING_AND_RELEASE_HYGIENE_20260916.md`
