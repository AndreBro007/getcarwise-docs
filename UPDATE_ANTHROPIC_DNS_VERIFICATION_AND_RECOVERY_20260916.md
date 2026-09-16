# Anthropic DNS Verification and Recovery Note — 2026-09-16

**Owner lane:** ChatGPT — Business/Strategy  
**Status:** FACTUAL UPDATE — recovery pending Engineering action

## User-confirmed Vercel evidence

Andre supplied a Vercel deployment screenshot on 2026-09-16 showing the current Production deployment for project `carclever-find-my-car` as:

- Source branch: `main`
- Commit: `1514ab4` (`Sep 14: add Test Run Log entry for old-CarClever verification round`)
- Environment: Production / Current
- Domain shown: `carclever.getcarwise.app`

This independently confirms the production drift recorded earlier in `UPDATE_ANTHROPIC_MCP_URL_AND_PRODUCTION_DRIFT_20260916.md`.

ChatGPT did not perform this application deployment. Under the standing project boundary, ChatGPT is read-only for `AndreBro007/carclever-find-my-car` and does not perform Vercel production changes. The only ChatGPT write in this workstream on 2026-09-16 was documentation in `AndreBro007/getcarwise-docs`.

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

## Recovery sequence

Engineering should:

1. Restore Anthropic production project `carclever-find-my-car` to the approved V2 release SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.
2. Fix release/production configuration so future `main` pushes cannot silently replace the V2 production release.
3. Attach the confirmed Anthropic branded custom domain `carclever-anth.getcarwise.app` to that project and provide the exact Vercel DNS target to Andre for Porkbun.
4. After DNS propagation/SSL, verify `https://carclever-anth.getcarwise.app/mcp` serves the intended V2 contract and not the legacy V1 contract.
5. Do not change the OpenAI production project or `carclever-oai.getcarwise.app`.
6. Report exact production SHA, live endpoint, and verification evidence before Andre updates Anthropic or replies to Marco with the replacement URL.

No application-code, deployment, Vercel, or DNS changes were performed by ChatGPT in producing this record.
