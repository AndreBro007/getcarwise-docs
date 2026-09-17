# Audit: Edmunds/Impact Production Alias Drift — 2026-09-17

## Finding

The CJ→Impact code is present in the promoted deployment dd68e15cd34d2cbc13c29de698beb657c3b2d1ae, but the public production aliases are still serving the prior production build b8b07d8.

This is not a CDN-cache explanation.

## Evidence

- GitHub commit a2372d0 contains the substantive migration: edmunds.sjv.io base link and wrapWithImpact.
- Follow-up commits d62a3ab, 342796f, 5fb2bbf, and dd68e15 preserve the Impact base link. dd68e15 itself only changes a comment.
- Vercel project ccfmc-dev-v2 has READY Production deployment dpl_4zkjgLsr8tT88PYiEsc8mS24G4Gs, commit dd68e15, branch edmunds-impact-swap.
- Vercel project carclever-find-my-car has READY Production deployment dpl_HEA4yQevEh9psX3zpGtY7jJsRiJg, commit dd68e15, branch edmunds-impact-swap.
- Direct MCP POST to the deployment-specific V2 URL returned serverInfo.version dd68e15 and an edmunds.sjv.io URL.
- Direct MCP POST to all public aliases returned serverInfo.version b8b07d8 and the old anrdoezrs.net CJ URL: ccfmc-dev-v2.vercel.app, carclever-oai.getcarwise.app, carclever-anth.getcarwise.app, and carclever-find-my-car.vercel.app.
- The live MCP responses returned Cache-Control: no-cache, no-transform and x-vercel-cache: MISS. Preliminary GET checks also returned max-age=0, must-revalidate and x-vercel-cache: MISS.

## Diagnosis

The dashboard promotion created a new READY Production deployment, but the public aliases were not moved to it. The live result is deployment/alias drift. The likely operational interaction is that Auto-assign Custom Production Domains was disabled as a safety control; after that change, a promotion can leave custom domains attached to the prior deployment unless the intended aliases are explicitly reassigned. The exact Vercel alias state should be checked in the dashboard/API before any further action.

The canonical .vercel.app aliases also need explicit verification; they are demonstrably still serving b8b07d8.

## Required Claude Engineering action

1. Inspect the aliases/domains attached to dpl_HEA4yQevEh9psX3zpGtY7jJsRiJg and dpl_4zkjgLsr8tT88PYiEsc8mS24G4Gs.
2. Explicitly assign the intended public production aliases to the dd68e15 deployment, or use the Vercel-supported production promotion flow that moves those aliases. Do not change code.
3. Because production-domain auto-assignment is intentionally disabled, confirm exactly which domains must be manually reassigned and preserve rollback to b8b07d8.
4. Verify with raw MCP initialize and resolve_dealer_url POSTs against every intended public URL. Expected identity: dd68e15; expected affiliate prefix: https://edmunds.sjv.io/.
5. Only after alias identity is correct, repeat connector tests. A CDN purge is not the primary remedy.

## Vercel cache answers

1. A cached response would normally be indicated by a cache hit/revalidation signal, but these MCP responses are explicitly MISS and no-cache. More importantly, the response identity differs by hostname: public aliases consistently run b8b07d8, while the immutable deployment URL runs dd68e15.
2. This session provides a concrete yes: the deployment is tagged Production, yet the public aliases still resolve to the older build. The issue is alias/domain assignment or promotion semantics, not stale content at the MCP route.
3. For this route, no purge should be needed. The reliable operational fix is explicit alias/domain reassignment to the intended deployment, followed by raw MCP identity and link-output verification. If a future static/CDN response is intentionally cached, use Vercel's purge mechanism or cache tags; that is separate from this MCP failure.
