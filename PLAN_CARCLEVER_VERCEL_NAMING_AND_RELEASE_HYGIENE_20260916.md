# CarClever Vercel Naming and Release Hygiene Plan — 2026-09-16

**Owner lane:** ChatGPT — Business/Strategy  
**Status:** PROPOSED — pending André confirmation; no Vercel project rename has been performed

## Current verified production map

Both platform endpoints currently serve the same approved V2 release from repository `AndreBro007/carclever-find-my-car`, branch `release/v2`, exact SHA `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.

- OpenAI Vercel project: `ccfmc-dev-v2`
  - Production MCP domain: `https://carclever-oai.getcarwise.app/mcp`
- Anthropic Vercel project: `carclever-find-my-car`
  - Production MCP domain: `https://carclever-anth.getcarwise.app/mcp`
  - Existing migration aliases retained: `carclever.getcarwise.app` and `carclever-find-my-car.vercel.app`

The platform-specific Vercel projects are intentional: one shared codebase/release, separate production front doors and deployment/review lifecycles.

## Proposed production project names

After Anthropic confirms its pending listing has been switched to the new branded MCP URL, rename the two production Vercel projects in one controlled maintenance window:

- `ccfmc-dev-v2` -> `carclever-openai`
- `carclever-find-my-car` -> `carclever-anthropic`

These names are preferred over historical `dev`/version labels because the projects are now production platform endpoints, not temporary development projects.

Do not rename while the Anthropic support-side URL change is still pending. After each rename, re-verify custom domains, production SHA, MCP transport response, and Git connection before treating the rename as complete.

## Release-control hygiene

Anthropic production has already been changed to manual promotion by disabling Vercel's **Auto-assign Custom Production Domains** option.

OpenAI should be checked for the same setting. The desired production-control policy is:

- both platform production projects may continue to build from Git;
- custom production domains must not silently move to a new build after an unrelated push;
- production-domain assignment should require deliberate promotion;
- each promotion must record the intended release branch/SHA and verify the corresponding MCP endpoint afterwards.

The available Vercel connector metadata does not expose the OpenAI project's Auto-assign setting, so this requires an explicit dashboard check rather than assumption.

## Documentation hygiene

Maintain one canonical production map containing, for each platform:

- Vercel project name and immutable project ID;
- public MCP URL;
- Git repository and release branch;
- currently approved production SHA;
- production-promotion policy;
- review/submission status;
- retained legacy aliases and retirement conditions.

Prefer immutable Vercel project IDs in internal runbooks where practical so future display-name changes do not break identification.

## Optional later cleanup

After both OpenAI and Anthropic are stable on their branded production URLs, separately audit the remaining Vercel projects (`ccfmc-dev`, `ccfmc-dev-v3`, `carclever-v2-schema-probe`, etc.) and classify each as active test infrastructure, retained historical reference, or retirement candidate. Do not delete anything solely because its name looks old; first verify whether current test/documentation workflows still reference it.

## Gate

No production Vercel project rename or retirement is confirmed by this document. André confirmation is required before executing any rename/cleanup action.