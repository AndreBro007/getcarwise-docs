# V2 Shared Contract — Feasibility/Equivalence Package (Sep 9 2026)

Doc-only. No code touched. Authored by Claude (Engineering lane), for André + ChatGPT review before implementation is authorized.

## 1. Exact schema delta (`route.ts`, proposed — not yet coded)

**Open questions #1 and #2 answered by André, Sep 9 2026:**
1. `electrificationTypes: ["hybrid"]` implicitly includes `mild_hybrid` — callers never list it separately. `plug_in_hybrid` stays distinct, never implied by `hybrid`.
2. Legacy `goals` is hard-rejected post-cutover (schema/contract error stating `vehicleNeeds` is now required), not silently ignored — silent-ignore risked discarding practical needs and producing misleading results.

Remove:
- `goals: z.array(z.string()).optional()` field
- `input.goals` broad-search trigger (`isBroadSearch = !baseQuery.model || (input.goals?.length > 0)`)
- Description text instructing hosts to put qualitative preferences into `goals`

Add:
- `vehicleNeeds: z.array(z.string()).optional()` — same semantic role `goals` played (ranking/context input, not a hard filter), renamed only. No behavior change beyond the name.
- `electrificationTypes: z.array(z.enum(["hybrid","plug_in_hybrid","electric","mild_hybrid"])).optional()` — which electrified types satisfy the request. `hybrid` implicitly includes `mild_hybrid` (André, Sep 9); `plug_in_hybrid` never implied.
- `electrificationRequirement: z.enum(["required","preferred"]).optional()` — `required` triggers the bounded 20-VIN NHTSA pool + confirmed-only shortlist (per `SYS-20260909-002/003`); `preferred` affects ranking only, never excludes.

## 2. `goals` retirement

Full removal, no dual-accept, no migration period (locked by André, `SYS-20260909-004`). Any host still sending `goals` post-cutover gets a hard schema/contract error stating `vehicleNeeds` is now required (André, Sep 9 — silent-ignore rejected as risking discarded practical needs and misleading results).

## 3. `vehicleNeeds` behavior

Identical to old `goals`: freeform ranking/context signal, never a hard eligibility filter. The existing broad-search trigger logic (currently `input.goals != null && length > 0`) gets a straight rename to `input.vehicleNeeds`. No new logic proposed here — this is the lowest-risk part of the migration.

## 4. Electrification semantics

- `required`: only vehicles confirmed by NHTSA as matching one of `electrificationTypes` are returned. Unconfirmed (`unknown`/`ambiguous` per classifier) are excluded, never backfilled with gas variants — per audit Section C. If fewer than the normal shortlist count confirm, return fewer results with an explicit shortfall flag (not yet coded — this is schema/behavior design only).
- `preferred`: ranking boost only, no exclusion. Vehicles with `unknown`/`ambiguous` electrification are still eligible.
- `mild_hybrid` satisfies `hybrid`, never `plug_in_hybrid` (audit Section D; confirmed by André Sep 9 — resolved, codeable).

## 5. Host-routing risks

- Any host already deployed against the current `goals`-based tool description breaks immediately on this schema change (no dual-accept). This is a breaking API change for every existing integration, not additive.
- Both ChatGPT's own OpenAI-side tool description and Claude's own tool description need simultaneous updates, or hosts calling one before the other get inconsistent behavior mid-rollout.
- No feature-flag/versioned-endpoint mechanism currently exists to stage this — it's a hard cutover.

## 6. Preserved safeguards (confirmed unaffected by this migration)

- Model-list resolution for practical needs (unchanged, doesn't touch `goals`/`vehicleNeeds`)
- No lifestyle taxonomy tables
- Unknown data stays unknown (`unknown != false` standing principle, extended to `ambiguous` this session)
- No unsupported safety/reliability/towing/running-cost claims
- Auto.dev field-audit safeguards (make/model/cylinder conflict surfacing) — untouched by this delta, lives in `lib/nhtsa-client.ts` already merged

## 7. Regression cases required before implementation

1. Every existing `goals`-based test/fixture re-run against `vehicleNeeds` — same input semantics, renamed field, expect identical output.
2. `electrificationRequirement: "required"` with 0, 1, and 20 confirmed matches in the pool — verify shortfall flag behavior at each.
3. `electrificationRequirement: "preferred"` — verify no exclusion occurs even when 0 vehicles confirm.
4. Mixed `electrificationTypes` array (e.g. `["hybrid","electric"]`) — verify OR semantics, not AND.
5. `mild_hybrid` vehicle against `electrificationTypes: ["hybrid"]` vs `["plug_in_hybrid"]` — confirm satisfies former, not latter (semantics locked, needs fixture).
6. Host sends legacy `goals` field post-cutover — confirm hard schema/contract error returned (not silent-ignore).
7. City-handling regression (ambiguous city names) — re-run existing fixtures unchanged, confirm this migration doesn't touch that path at all.
8. Full V1/V2 side-by-side on a shared query set (no electrification/vehicleNeeds involved) — confirm zero behavior drift on searches that don't touch the new fields at all.

## 8. Implementation recommendation

Semantics now locked (André, Sep 9). Do not implement until the three release gates below are cleared. Recommend a single atomic PR, not incremental route edits, given the "hard cutover, no dual-accept" constraint in Section 5.

## Release gates (blockers) — confirmed valid by André, Sep 9

1. Add real BEV, mild-hybrid, and ambiguity NHTSA fixtures (carried over from `SYS-20260909-003`).
2. Define one coordinated Claude/ChatGPT tool-description cutover and refresh plan (no staged/partial rollout given hard-cutover constraint).
3. Write full regression fixtures for all 8 cases in Section 7 before implementation authorization.

**Status: semantics resolved, package ready for review. Implementation remains blocked on the three gates above.**
