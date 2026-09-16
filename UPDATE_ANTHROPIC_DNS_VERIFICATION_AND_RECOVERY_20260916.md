# Anthropic DNS Verification and Recovery Note — 2026-09-16

**Owner lane:** ChatGPT — Business/Strategy  
**Status:** FACTUAL UPDATE — V2 runtime recovery confirmed; release-control prevention setting still requires Engineering confirmation; Anthropic branded-domain setup pending

## User-confirmed Vercel evidence

Andre supplied a Vercel deployment screenshot on 2026-09-16 showing the then-current Production deployment for project `carclever-find-my-car` as:

- Source branch: `main`
- Commit: `1514ab4` (`Sep 14: add Test Run Log entry for old-CarClever verification round`)
- Environment: Production / Current
- Domain shown: `carclever.getcarwise.app`

This independently confirmed the production drift recorded earlier in `UPDATE_ANTHROPIC_MCP_URL_AND_PRODUCTION_DRIFT_20260916.md`.

ChatGPT did not perform this application deployment. Under the standing project boundary, ChatGPT is read-only for `AndreBro007/carclever-find-my-car` and does not perform Vercel production changes. The only ChatGPT writes in this workstream on 2026-09-16 were documentation in `AndreBro007/getcarwise-docs`.

## Recovery verification — 2026-09-16

After Engineering recovery work, ChatGPT independently re-checked the live Vercel state.

Resolving the active custom domain `carclever.getcarwise.app` through Vercel now maps to deployment:

- Deployment ID: `dpl_9vP17yqXx5fdfV2uTWfAenvfYFD2`
- Source branch: `release/v2`
- Exact Git SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`
- Commit message: `Make widget origin configurable via NEXT_PUBLIC_WIDGET_ORIGIN env var`
- Target: production
- Action metadata: `promote`
- State: READY
- Active aliases include `carclever.getcarwise.app` and `carclever-find-my-car.vercel.app`

A direct request to `https://carclever.getcarwise.app/mcp` returns an MCP JSON-RPC `Method not allowed` response to GET, confirming that the MCP route is live at the recovered production origin.

Therefore the critical runtime recovery is **confirmed**: the active Anthropic-project aliases are again serving the approved Sep 12 V2 release SHA rather than Sep 14 `main` SHA `1514ab42...`.

### Remaining release-control gate

The available Vercel project metadata does not expose enough production-branch/Git-trigger configuration to independently prove that a future `main` push can no longer replace the promoted V2 release.

Engineering must still explicitly confirm the preventive configuration change and its effect before this incident is considered fully closed. Runtime recovery and future-overwrite prevention are separate gates.

## DNS evidence supplied by Andre

Andre supplied the active Porkbun DNS zone showing, among other records:

- `CNAME carclever-oai.getcarwise.app` -> OpenAI Vercel DNS target
- `CNAME carclever.getcarwise.app` -> legacy/current Anthropic-project Vercel DNS target
- `TXT getcarwise.app anthropic-domain-verification-...`
- `TXT getcarwise.app openai-domain-verification=...`

No `carclever-anth.getcarwise.app` DNS record exists yet.

## Anthropic TXT clarification

Current official Anthropic documentation states that TXT values beginning with `anthropic-domain-verification-` are used in Anthropic's organization/SSO domain-verification flow. This confirms that the existing apex TXT record is an Anthropic identity/domain-control record; it should not be assumed to be a per-MCP-directory subdomain verification record.

Anthropic's current MCP Directory Policy separately requires developers to verify that they own or control API endpoints used by an MCP server. Public directory documentation reviewed today does not specify a separate DNS TXT step for every submitted MCP hostname.

Operational implication:

- Do not remove or replace the existing Anthropic TXT record.
- Creating `carclever-anth.getcarwise.app` requires normal Vercel custom-domain/DNS ownership and SSL validation.
- After the endpoint is live, the Anthropic listing should be updated and its tools re-synced/re-scanned per the current pending-listing workflow and Marco's direct support guidance.
- If Anthropic's portal explicitly asks for an additional verification record for the new hostname, follow the portal-provided value rather than assuming the existing apex TXT covers it.

## Next sequence

Engineering/user should now:

1. Confirm the Vercel/Git release-control fix that prevents future `main` pushes from silently replacing the V2 production release.
2. Attach the confirmed Anthropic branded custom domain `carclever-anth.getcarwise.app` to project `carclever-find-my-car`.
3. Obtain the exact DNS record Vercel requests for that hostname and add it at Porkbun; do not guess the target.
4. After DNS propagation/SSL, verify `https://carclever-anth.getcarwise.app/mcp` resolves to exact V2 SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792` and serves the V2 MCP contract rather than legacy V1.
5. Keep the existing Anthropic aliases alive during migration.
6. Do not change the OpenAI production project or `carclever-oai.getcarwise.app`.
7. Only after endpoint verification, update the pending Anthropic listing, sync/rescan its tools, save, and send Marco the final replacement URL.

No application-code, deployment, Vercel, or DNS changes were performed by ChatGPT in producing this record.
