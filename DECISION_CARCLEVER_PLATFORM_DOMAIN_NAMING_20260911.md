# CarClever Platform Domain Naming Decision — 2026-09-11

**Status:** CONFIRMED BY ANDRÉ

## Decision

Use this naming convention for branded GetCarWise MCP production front doors:

`<product>-<platform>.getcarwise.app`

For CarClever:

- OpenAI target: `https://carclever-oai.getcarwise.app/mcp`
- Future Anthropic branded target: `https://carclever-anth.getcarwise.app/mcp`

## Current Anthropic exception

Anthropic must remain on the MCP URL already used for its current submission until the Anthropic review/change gate is explicitly cleared:

`https://carclever-find-my-car.vercel.app/mcp`

When/if a future Anthropic migration to the branded domain is approved, `carclever-anth.getcarwise.app` is the intended naming target. No Anthropic domain/deployment change is authorized by this decision alone.

## OpenAI implementation sequence

The OpenAI branded target is now confirmed as `carclever-oai.getcarwise.app`. Before it is placed into the resubmission, Claude Engineering must:

1. map/configure the branded hostname in the appropriate Vercel production channel;
2. configure the required DNS record under `getcarwise.app`;
3. serve the exact tested V2 release behind the new origin;
4. verify the deployed SHA and MCP metadata, not merely URL reachability;
5. run a production-origin smoke covering MCP initialize/tools, widget/resource/CSP loading, representative live search, exact-VIN Buyer Check, link resolution, and at least one negative-invocation check;
6. complete any OpenAI domain-verification / Scan Tools checks required by the resubmission flow.

Only after those checks pass should the OpenAI resubmission MCP URL be changed to:

`https://carclever-oai.getcarwise.app/mcp`

## Scope boundary

This decision records naming and release architecture only. Application code, Vercel/DNS implementation, production deployment, and connector changes remain Claude Engineering work. The existing OpenAI resubmission reconciliation document should not be treated as updated until the new origin is actually configured and verified.