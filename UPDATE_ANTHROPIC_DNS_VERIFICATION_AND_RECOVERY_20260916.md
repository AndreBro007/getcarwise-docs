# Anthropic DNS Verification and Recovery Note — 2026-09-16

**Owner lane:** ChatGPT — Business/Strategy  
**Status:** FACTUAL UPDATE — V2 recovery complete; release-control prevention confirmed; Anthropic branded MCP domain live and verified; Anthropic support-side URL update pending

## Incident and recovery

Andre supplied Vercel evidence on 2026-09-16 showing that project `carclever-find-my-car` had been silently moved to a Sep 14 `main` deployment at SHA `1514ab42dd2d4afe20109f02c9cc3930a3ee0789`.

ChatGPT independently confirmed the drift and later re-checked the recovered live runtime. The approved production deployment is:

- deployment ID `dpl_9vP17yqXx5fdfV2uTWfAenvfYFD2`;
- source branch `release/v2`;
- exact Git SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`;
- commit `Make widget origin configurable via NEXT_PUBLIC_WIDGET_ORIGIN env var`;
- target `production`;
- state `READY`.

The existing aliases `carclever.getcarwise.app` and `carclever-find-my-car.vercel.app` remain live.

## Release-control root cause and fix — confirmed

`carclever-widget/STATE.md` records the root cause and completed prevention change.

The project's Production environment had **Auto-assign Custom Production Domains** enabled. This allowed a push to the tracked production branch to take over the live custom domain automatically even though the intended V2 release had been deliberately promoted from `release/v2`.

Andre disabled **Auto-assign Custom Production Domains** in Vercel Project Settings → Environments → Production and saved the change. Vercel's UI confirmation states that **Production deployments will need to be manually promoted**.

This closes the release-control gap: future pushes can still create deployments, but should not automatically replace the live custom production domains without an explicit promotion action.

The source of the Sep 14 `TESTING.md` commit itself remains unidentified and should not be attributed to a specific person or AI without evidence.

OpenAI's production project and `carclever-oai.getcarwise.app` were not changed during this recovery.

## Anthropic branded-domain setup — completed and verified

Andre added the Vercel custom domain:

`carclever-anth.getcarwise.app`

Vercel requested the Porkbun DNS record:

- Type: `CNAME`
- Host: `carclever-anth`
- Target: `c6a2c23ef4265088.vercel-dns-017.com.`

Andre added the record at Porkbun with note `CarClever - Anthropic MCP URL`.

Vercel subsequently showed **Valid Configuration** for `carclever-anth.getcarwise.app`.

ChatGPT independently verified the hostname against Vercel. It resolves to the same approved production deployment:

- deployment ID `dpl_9vP17yqXx5fdfV2uTWfAenvfYFD2`;
- branch `release/v2`;
- exact SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`;
- state `READY`;
- target `production`.

A direct HTTPS request to:

`https://carclever-anth.getcarwise.app/mcp`

completed successfully at the TLS/HTTP layer and returned the expected MCP JSON-RPC GET response:

- HTTP `405 Method Not Allowed`;
- JSON-RPC error `Method not allowed`;
- `content-type: application/json`;
- `strict-transport-security` present;
- response served by Vercel.

This confirms that DNS, SSL/HTTPS routing, Vercel aliasing, and the MCP route are live on the new Anthropic hostname.

Andre also confirmed a successful functional MCP-client test using **`CarClever - Find My Car`** against the new branded endpoint. This provides an additional end-to-end confirmation beyond the browser/HTTP transport check.

## Anthropic listing update workflow — corrected

Andre cannot edit the pending Anthropic MCP URL in the portal. This is the reason the support thread with Marco was opened.

Marco's guidance established that the MCP URL can be changed while the listing is pending and that the correct path is to send Anthropic support the replacement URL for the pending submission.

Therefore the next action is **not** a portal Edit Server / Sync / Rescan step by Andre. The next action is to reply to Marco with the verified replacement MCP URL:

`https://carclever-anth.getcarwise.app/mcp`

Anthropic/support must apply the URL change to the pending listing on their side. Any follow-up sync/rescan or review action should be performed according to the instructions Anthropic provides after making that change.

## Anthropic TXT clarification

The existing apex `anthropic-domain-verification-...` TXT record is an Anthropic organization/domain-control record and should not be assumed to be a per-MCP-directory subdomain verification record.

Operationally:

- do not remove or replace the existing Anthropic TXT record;
- keep existing Anthropic aliases alive during the directory migration;
- if Anthropic later explicitly requests another verification record, follow the portal/support-provided value.

## Next sequence

1. Reply to Marco with `https://carclever-anth.getcarwise.app/mcp` and ask Anthropic to replace the pending listing's current MCP URL with this verified endpoint.
2. State that the new endpoint is already live and tested, including a successful `CarClever - Find My Car` MCP-client test.
3. Wait for Anthropic to confirm the pending listing has been updated or provide any required follow-up validation instructions.
4. Keep `carclever.getcarwise.app` and `carclever-find-my-car.vercel.app` live during the transition; no cleanup is required before Anthropic confirms the new endpoint is recorded.
5. Do not change OpenAI project `ccfmc-dev-v2` or `carclever-oai.getcarwise.app`.

No application-code or deployment changes were performed by ChatGPT in producing this record.