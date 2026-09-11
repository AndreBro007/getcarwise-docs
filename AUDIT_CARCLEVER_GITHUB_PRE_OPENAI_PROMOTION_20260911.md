# CarClever GitHub Pre-OpenAI Promotion Audit — 2026-09-11

**Status:** VERIFIED READ-ONLY AUDIT  
**Purpose:** establish the exact GitHub state immediately before any OpenAI production-origin/domain work.  
**Execution:** no application code, branch, PR, deployment, Vercel setting, connector, or DNS state changed.

## Executive conclusion

The current OpenAI V2 release candidate is:

- Repository: `AndreBro007/carclever-find-my-car`
- Branch: `release/v2`
- HEAD: `a5d96960792d1de3cd4eaf81ccef0a1515acf04f`

The prior Sep 10 infrastructure audit recorded V2 at `a9d6439a31a3e3ad783ead825ae2880cc7aa72ac`.

GitHub comparison now proves `release/v2` is **exactly 2 commits ahead and 0 behind** that audited baseline. Those are the two Sep 11 regression fixes produced by the subsequent cross-host testing. No additional application-repository commits have landed after them.

## The two post-audit V2 commits

### 1. `15d24bebe5a63893426794bb9f7dddd6e09d8fbb`

Claimed outcome: prevent `vehicleType` from duplicating broad `bodyType`, and restore the anti-invention guardrail on `transmission`.

Spot verification of the actual diff confirms:

- `buildListingsParams()` omits `vehicle.type` when `vehicleType` equals `bodyType` case-insensitively;
- a genuinely different finer classification such as `Crossover` remains supported;
- `transmission` description now says to supply it only when explicitly stated or clearly implied and not to invent a value;
- `vehicleType` description no longer uses `SUV` as an example and explicitly says not to duplicate `bodyType`;
- a dedicated five-case regression test was added.

This is a real implementation + contract correction, not a documentation-only commit.

### 2. `a5d96960792d1de3cd4eaf81ccef0a1515acf04f`

Claimed outcome: add a general anti-invention instruction to the public `find_matching_vehicle` tool description.

Spot verification confirms the only source change is the added description line:

`Direct filter fields should reflect requirements the user stated or clearly implied; leave unstated restrictions unset.`

No search/ranking/link/VIN logic changed in this commit.

## Current principal branch heads

- `main` (V1 / submitted Anthropic production line): `e7c8634fdd631c7bb05c83c02daeb1ab7f7bbb6d` — unchanged since Aug 25.
- `release/v2` (OpenAI V2 candidate): `a5d96960792d1de3cd4eaf81ccef0a1515acf04f`.
- `v3.1-3.3/card-first-check-vehicle` (paused V3 safe point): `4032feb7b67879ba2aa3230c8c3bc7f546a525f1` — unchanged.

This preserves the intended separation: V1 `main` is untouched, V2 is isolated on `release/v2`, and V3 remains paused on its separate branch.

## Current open PRs

Two old draft PRs remain open against `main`:

1. PR #1 `fix/total-matches-count-bug`, head `6700bbb...`
2. PR #2 `feature/edmunds-two-button-cta`, head `719fc13...`

The earlier Sep 10 audit recommended closing both as superseded rather than merging them, subject to André approval / engineering ancestry verification.

Current comparison strengthens that conclusion for PR #1: `release/v2` is 93 commits ahead and 0 behind `fix/total-matches-count-bug`, so the old branch is an ancestor of the current V2 line.

PR #2 is different: its old branch accumulated V3-era work and is now diverged from `release/v2`. It must **not** be merged into `main` or used as the OpenAI production source. The current V2 source of truth is `release/v2` only.

## Other remaining branches

Current repository branch listing still contains historical/research/test branches including:

- `feature/edmunds-two-button-cta`
- `feature/v3-check-vehicle`
- `fix/total-matches-count-bug`
- `research/v2-schema-probe`
- `t1`
- `v2-correction/description-and-citation-cleanup`
- `v2-implementation/schema-and-electrification`
- `v2.4/match-score-price-proximity`
- `v2.5/condition-label-in-summary-text`
- `v3.1-3.3/card-first-check-vehicle`

Verified examples:

- `v2-implementation/schema-and-electrification` is an ancestor of current `release/v2` (V2 is 13 commits ahead, 0 behind).
- `v2-correction/description-and-citation-cleanup` is an ancestor of current `release/v2` (5 ahead, 0 behind).
- V2.4 and V2.5 topic branches are each ancestors of current `release/v2` (48 ahead, 0 behind).
- `research/v2-schema-probe`, `t1`, and the old `feature/edmunds-two-button-cta` line are diverged historical/test lines and must not be mistaken for the release source.

Branch/PR cleanup remains valid housekeeping for later, but it is **not required to construct the OpenAI production front door**. It should not be mixed into the production-origin task unless André deliberately chooses to do cleanup first.

## Release-candidate rule for the next Claude handoff

For the OpenAI production-origin/domain task, Claude Engineering must treat this exact commit as immutable input unless André separately approves a new code change:

`a5d96960792d1de3cd4eaf81ccef0a1515acf04f`

The task is infrastructure/release-channel work, not another V2 feature or code-cleanup pass.

Claude must not:

- merge either old PR;
- merge V2 into `main`;
- touch the paused V3 branch;
- use `feature/edmunds-two-button-cta`, `research/v2-schema-probe`, `t1`, or a historical topic branch as the release source;
- bundle branch deletion/cleanup into the production-origin change;
- modify the Anthropic V1 production line or submitted MCP origin.

## Next technical step

Once André accepts this audit as the correct GitHub baseline, prepare a narrowly scoped Claude Engineering handoff to create and validate the OpenAI production front door:

`https://carclever-oai.getcarwise.app/mcp`

The handoff should require exact-SHA verification before and after deployment and must preserve the established two-channel architecture:

- OpenAI branded channel → exact tested V2 release;
- Anthropic existing submitted URL remains untouched until its separate review/change gate is cleared.
