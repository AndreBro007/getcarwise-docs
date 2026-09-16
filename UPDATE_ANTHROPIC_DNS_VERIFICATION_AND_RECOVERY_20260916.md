# Anthropic DNS Verification and Recovery Note — 2026-09-16

**Owner lane:** ChatGPT — Business/Strategy  
**Status:** FACTUAL UPDATE — V2 runtime recovery and release-control prevention confirmed; Anthropic branded-domain setup pending

## Incident and recovery

Andre supplied Vercel evidence on 2026-09-16 showing that project `carclever-find-my-car` had been silently moved to a Sep 14 `main` deployment at SHA `1514ab42dd2d4afe20109f02c9cc3930a3ee0789`.

ChatGPT independently confirmed the production drift and later independently re-checked the recovered live runtime. The active custom domain `carclever.getcarwise.app` now maps to:

- deployment ID `dpl_9vP17yqXx5fdfV2uTWfAenvfYFD2`;
- source branch `release/v2`;
- exact Git SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`;
- commit `Make widget origin configurable via NEXT_PUBLIC_WIDGET_ORIGIN env var`;
- target `production`;
- state `READY`;
- active aliases including `carclever.getcarwise.app` and `carclever-find-my-car.vercel.app`.

A direct GET to `https://carclever.getcarwise.app/mcp` returns the expected MCP JSON-RPC `Method not allowed` response, confirming that the MCP route is live at the recovered production origin.

## Release-control root cause and fix — confirmed

`carclever-widget/STATE.md` now records the root cause and completed prevention change.

The project's Production environment had **Auto-assign Custom Production Domains** enabled. This allowed a push to the tracked production branch to take over the live custom domain automatically even though the intended V2 release had been deliberately promoted from `release/v2`.

Andre disabled **Auto-assign Custom Production Domains** in Vercel Project Settings → Environments → Production and saved the change. Vercel's UI confirmation states that **Production deployments will need to be manually promoted**.

This closes the release-control gap that caused the incident: future pushes can still create deployments, but they should not automatically replace the live custom production domain without an explicit promotion action.

The source of the Sep 14 `TESTING.md` commit itself remains unidentified and should not be attributed to a specific person or AI without evidence. The operational risk is nevertheless mitigated by the manual-promotion control now in place.

OpenAI's production project and `carclever-oai.getcarwise.app` were not changed during this recovery.

## DNS evidence supplied by Andre

Andre supplied the active Porkbun DNS zone showing, among other records:

- `CNAME carclever-oai.getcarwise.app` → OpenAI Vercel DNS target;
- `CNAME carclever.getcarwise.app` → current Anthropic-project Vercel DNS target;
- `TXT getcarwise.app anthropic-domain-verification-...`;
- `TXT getcarwise.app openai-domain-verification=...`.

No `carclever-anth.getcarwise.app` DNS record exists yet.

## Anthropic TXT clarification

The existing apex `anthropic-domain-verification-...` TXT record is an Anthropic organization/domain-control record and should not be assumed to be a per-MCP-directory subdomain verification record.

Operationally:

- do not remove or replace the existing Anthropic TXT record;
- create `carclever-anth.getcarwise.app` through the normal Vercel custom-domain/DNS/SSL process;
- if Anthropic's portal later explicitly requests another verification record, follow the portal-provided value;
- after the endpoint is live, update the pending Anthropic listing and sync/rescan its tools per Marco's direct guidance.

## Next sequence

1. Add `carclever-anth.getcarwise.app` as a custom domain on Vercel project `carclever-find-my-car`.
2. Obtain the exact DNS record Vercel requests and add it at Porkbun; do not guess the target.
3. Keep existing Anthropic aliases alive during migration.
4. After DNS propagation/SSL, verify `https://carclever-anth.getcarwise.app/mcp` resolves to exact V2 SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792` and serves the V2 contract rather than legacy V1.
5. Do not change OpenAI project `ccfmc-dev-v2` or `carclever-oai.getcarwise.app`.
6. Only after endpoint verification, update the pending Anthropic listing, sync/rescan its tools, save, and send Marco the final replacement URL.

No application-code, deployment, Vercel, or DNS changes were performed by ChatGPT in producing this record.