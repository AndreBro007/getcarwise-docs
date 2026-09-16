# Anthropic DNS Verification and Recovery Note — 2026-09-16

**Owner lane:** ChatGPT — Business/Strategy  
**Status:** FACTUAL UPDATE — V2 recovery complete; dual-platform release-control prevention confirmed; Anthropic branded MCP domain live and verified; Anthropic support-side URL update pending

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

`carclever-widget/STATE.md` records the root cause and completed Anthropic prevention change.

The Anthropic project's Production environment had **Auto-assign Custom Production Domains** enabled. This allowed a push to the tracked production branch to take over the live custom domain automatically even though the intended V2 release had been deliberately promoted from `release/v2`.

Andre disabled **Auto-assign Custom Production Domains** in Vercel Project Settings → Environments → Production and saved the change. Vercel's UI confirmation states that **Production deployments will need to be manually promoted**.

This closes the Anthropic release-control gap: future pushes can still create deployments, but should not automatically replace the live custom production domains without an explicit promotion action.

The source of the Sep 14 `TESTING.md` commit itself remains unidentified and should not be attributed to a specific person or AI without evidence.

## OpenAI equivalent safeguard — completed

After the Anthropic recovery, André checked the separate OpenAI Vercel project `ccfmc-dev-v2`.

Confirmed:

- Production branch tracking: `release/v2`;
- **Auto-assign Custom Production Domains: Disabled**;
- setting saved;
- `carclever-oai.getcarwise.app` remains attached to Production.

ChatGPT had independently verified before this settings change that the OpenAI custom domain still served exact approved V2 SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.

Both platform production projects now use deliberate manual production-domain promotion.

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

## Anthropic listing update workflow — support-side action pending

Andre cannot edit the pending Anthropic MCP URL in the portal. This is the reason the support thread with Marco was opened.

Marco's guidance established that the MCP URL can be changed while the listing is pending and that the correct path is to send Anthropic support the replacement URL for the pending submission.

On 2026-09-16 André sent the follow-up email requesting that Anthropic replace the pending listing's current MCP URL with:

`https://carclever-anth.getcarwise.app/mcp`

The email stated that the new endpoint is live and tested, that the existing endpoint will remain active during the transition, and politely asked whether the current listing could be flagged with the review team given the submission history dating back to April.

**Current gate:** wait for Marco/Anthropic to confirm that the pending listing has been updated or provide any required follow-up validation instructions. Do not mark the new URL as the directory's stored URL until that confirmation arrives.

## Anthropic TXT clarification

The existing apex `anthropic-domain-verification-...` TXT record is an Anthropic organization/domain-control record and should not be assumed to be a per-MCP-directory subdomain verification record.

Operationally:

- do not remove or replace the existing Anthropic TXT record;
- keep existing Anthropic aliases alive during the directory migration;
- if Anthropic later explicitly requests another verification record, follow the portal/support-provided value.

## Standing release policy

For both OpenAI and Anthropic production Vercel projects:

1. Git pushes may create deployments but must not silently take over branded production domains.
2. Production-domain movement requires deliberate **Promote to Production**.
3. Verify intended branch/SHA before promotion.
4. Verify branded MCP endpoint and exact SHA after promotion.
5. Do not use routine documentation/test-log pushes as production releases.

## Deferred housekeeping

After Anthropic confirms its new URL and both platform submissions are stable:

- proposed Vercel display-name cleanup:
  - `ccfmc-dev-v2` -> `carclever-openai`;
  - `carclever-find-my-car` -> `carclever-anthropic`;
- audit remaining CarClever-related Vercel projects before any retirement;
- re-audit stale GitHub branches before bulk deletion;
- retain the shared GitHub repository name `AndreBro007/carclever-find-my-car` unless a separate migration decision is made.

See `PLAN_CARCLEVER_VERCEL_NAMING_AND_RELEASE_HYGIENE_20260916.md`.

## Next sequence

1. Wait for Anthropic to confirm the pending listing's MCP URL has been replaced with `https://carclever-anth.getcarwise.app/mcp` or provide follow-up validation instructions.
2. Keep `carclever.getcarwise.app` and `carclever-find-my-car.vercel.app` live during the transition.
3. Keep V2 code frozen except for platform-requested or evidence-backed corrections authorized by André.
4. Do not perform deferred project renames/deletions until the support-side transition is confirmed.

No application-code or deployment changes were performed by ChatGPT in producing this record.