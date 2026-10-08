# PLAN: Rebuild V3 on top of current release/v2, then tag the MCP app's Edmunds links

**Date:** Oct 8, 2026 | **Lane:** Claude Engineering | **Status:** APPROVED BY ANDRÉ, NOT STARTED. To be executed in a separate, new session.
**Trigger phrase (André will say):** "sync CarClever V3 code"

## Why this exists (confirmed from the repo, Oct 8, 2026)
- `carclever-find-my-car` branch `v3.1-3.3/card-first-check-vehicle` (tip `4032feb`) is **26 commits and 54 files BEHIND `release/v2`** (tip `cac7028`) and has **6 commits of its own** (9 files, +1,048/-24): check_vehicle port (recalls / Buyer Check), V3.2 card-first check_vehicle, V3.3 standalone identity card, tests, TESTING.md.
- V3 lacks: the V2 contract rewrite and schema validation fix, the electrification fix, the OpenAI domain-verification endpoint, local-ranking changes, and the **Impact migration**. Its `lib/edmunds-cj.ts` still builds old CJ links (`anrdoezrs.net`), which are dead. Any V3 test connector (`ccfmc-dev-v3`) therefore returns dead Edmunds links today.
- Likely cause (INFERRED from history, not stated in any document): V3 was cut from the older v2.4/v2.5 development line; `release/v2` was then assembled from separate correction branches (Sep 9) and received the Impact swap (Sep 16-25) and the electrification fix (Sep 25); V3 was frozen during the platform reviews and never received them.
- The MCP app (OpenAI, Anthropic and Meta front doors, all on `release/v2`) builds every Edmunds link in `lib/edmunds-cj.ts` (`wrapWithAffiliateNetwork`): `https://edmunds.sjv.io/c/7765200/3949600/52125?u=<encoded Edmunds URL>` with **no `sharedid`**. Lite V2 displays these backend links, so it is untagged too.

## Approved approach
1. **Do NOT continue from the old V3 branch.** Create a NEW branch from the current tip of `release/v2` and re-apply the 6 V3 commits (cherry-pick). V3 becomes "V2 + its own changes".
2. Expected conflict files: `app/[transport]/route.ts`, `lib/find-matching-vehicle-output.ts`, `package.json`, tests (`stable-boundaries`, others). Resolve in favour of V2 for everything V2 changed; keep V3's check_vehicle additions.
3. **First commit on the new branch: Shared ID tagging** of MCP Edmunds links (see below).
4. Add a **test guard**: every URL produced by the MCP link builder must (a) use the Impact base `edmunds.sjv.io`, (b) contain `sharedid=`, (c) not contain `anrdoezrs.net`.
5. Do NOT touch `release/v2`, `main`, `staging`, or any production domain. Do NOT promote anything. V2 live and submitted (OpenAI, Anthropic, Meta reviews) must be unaffected.

## Shared ID design (André decision Oct 8)
- Goal for now: separate web-page clicks from app clicks. Use **one generic tag for all MCP app links** in V3; per-platform tags (OpenAI / Anthropic / Meta, possibly Lite V2) later, when there is volume.
- **Impact documentation (verified Oct 8):** Shared IDs are "letters and numbers only; no spaces or special characters", 255 characters max; all tracking links including vanity links support them. Use an alphanumeric tag such as `mcpapp`. Existing website/Lite tags use hyphens/underscores (`claude-test` was confirmed to appear in Impact's report; underscore tags such as `lite_result` are NOT yet confirmed to survive). See open item below.
- Where V3 sets it: in the link builder, not in the model-facing text, so links the model writes in chat also carry it.

## Guard-rails for the executing session (Vercel safety, PLAYBOOK hard gate applies)
- Before any Vercel promotion or `autoAssignCustomDomains` change: fetch and SHOW current live commit + alias list for all 3 domains. Not expected to be needed: this work should only produce a branch and preview/dev builds.
- Check which branch the `ccfmc-dev-v3` project tracks (read-only Vercel API) before pushing, so the new branch name cannot match a production-tracked branch.
- Pushes to non-tracked branches create previews only. Do not push this work to `staging` (it feeds the three `-test` domains for all platforms) unless André approves.
- Verify with a real `find_matching_vehicle` call against the V3 dev endpoint (uses Auto.dev calls from the shared Free cap: ask André first) and confirm the live URL contains the Impact base and the tag.
- Log everything in STATE.md / TASKS.md; re-fetch to verify.

## Preventing drift (approved in principle; each item needs André's OK when executed)
1. One trunk: `release/v2` is the trunk; V3 is always "trunk plus a small delta". Fixes to links, disclosures or security go to the trunk first, then V3 syncs.
2. Drift check at session start: V3 ahead/behind `release/v2`, recorded in STATE.md.
3. The link test guard above.
4. Branch hygiene, DEFERRED until V3 is rebuilt: 14 branches exist; default branch `main` is the retired V1 line. Proposal: set default branch to `release/v2` and archive stale branches. Both need André's explicit approval; do not do either in the V3 session without it.

## Open items
- Impact underscore/hyphen question: does a real visitor click on an existing underscore tag (for example `lite_result`) appear in Impact's Shared ID report? If not, existing tags need normalising to letters and numbers. Needs one labelled test click or the first real tagged click.
- Per-platform MCP tags (and whether Lite V2 should be split from the Claude app): later, after volume.
- Old CarClever (Fractal) links are not in GitHub and untagged; revisit after the Oct 14 Fractal decision.
