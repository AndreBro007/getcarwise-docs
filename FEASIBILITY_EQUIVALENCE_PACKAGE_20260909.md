# V2 Shared Contract — Feasibility/Equivalence Package (Sep 9 2026)

Doc-only. No code touched. Authored by Claude (Engineering lane), for André + ChatGPT review before implementation is authorized.

## 1. Exact schema delta (`route.ts`, proposed — not yet coded)

Remove:
- `goals: z.array(z.string()).optional()` field
- `input.goals` broad-search trigger (`isBroadSearch = !baseQuery.model || (input.goals?.length > 0)`)
- Description text instructing hosts to put qualitative preferences into `goals`

Add:
- `vehicleNeeds: z.array(z.string()).optional()` — same semantic role `goals` played (ranking/context input, not a hard filter), renamed only. No behavior change beyond the name.
- `electrificationTypes: z.array(z.enum(["hybrid","plug_in_hybrid","electric","mild_hybrid"])).optional()` — which electrified types satisfy the request. Open question (#1 below): does `hybrid` implicitly include `mild_hybrid`, or must callers list both?
- `electrificationRequirement: z.enum(["required","preferred"]).optional()` — `required` triggers the bounded 20-VIN NHTSA pool + confirmed-only shortlist (per `SYS-20260909-002/003`); `preferred` affects ranking only, never excludes.

## 2. `goals` retirement

Full removal, no dual-accept, no migration period (locked by André, `SYS-20260909-004`). Any host still sending `goals` gets it silently ignored — **open question #2:** should this be a hard schema-validation rejection instead, so a host relying on the old field fails loudly rather than having its input silently dropped?

## 3. `vehicleNeeds` behavior

Identical to old `goals`: freeform ranking/context signal, never a hard eligibility filter. The existing broad-search trigger logic (currently `input.goals != null && length > 0`) gets a straight rename to `input.vehicleNeeds`. No new logic proposed here — this is the lowest-risk part of the migration.

## 4. Electrification semantics

- `required`: only vehicles confirmed by NHTSA as matching one of `electrificationTypes` are returned. Unconfirmed (`unknown`/`ambiguous` per classifier) are excluded, never backfilled with gas variants — per audit Section C. If fewer than the normal shortlist count confirm, return fewer results with an explicit shortfall flag (not yet coded — this is schema/behavior design only).
- `preferred`: ranking boost only, no exclusion. Vehicles with `unknown`/`ambiguous` electrification are still eligible.
- `mild_hybrid` satisfies `hybrid`, never `plug_in_hybrid` (audit Section D) — **open question #1 above** still needs resolving before this is codeable.

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
5. `mild_hybrid` vehicle against `electrificationTypes: ["hybrid"]` vs `["plug_in_hybrid"]` — confirm satisfies former, not latter (pending open question #1).
6. Host sends legacy `goals` field post-cutover — confirm the chosen behavior (silently ignored vs. rejected, per open question #2) actually happens.
7. City-handling regression (ambiguous city names) — re-run existing fixtures unchanged, confirm this migration doesn't touch that path at all.
8. Full V1/V2 side-by-side on a shared query set (no electrification/vehicleNeeds involved) — confirm zero behavior drift on searches that don't touch the new fields at all.

## 8. Implementation recommendation

Do not implement until: (a) open questions #1 and #2 above are answered, (b) regression cases 1–8 have deterministic fixtures written (not yet started), (c) both tool descriptions (Claude + ChatGPT/OpenAI) are ready to cut over together. Recommend a single atomic PR, not incremental route edits, given the "hard cutover, no dual-accept" constraint in Section 5.

## Explicit blockers

1. `electrificationTypes` array semantics unresolved (see #1) — mild_hybrid/hybrid overlap not yet specified precisely enough to code.
2. Legacy-`goals` post-cutover behavior unresolved (see #2) — silent-ignore vs. hard-reject.
3. Zero regression fixtures exist yet for any of the 8 cases above.
4. No coordinated cutover plan between Claude's and ChatGPT's tool descriptions.
5. `mild_hybrid`/BEV/ambiguous classifier branches still lack real NHTSA fixtures (carried over from `SYS-20260909-003`).
