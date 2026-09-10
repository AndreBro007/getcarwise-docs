# Handoff — V2 Contract Gap Fix — 2026-09-11

**Status:** READY FOR CLAUDE — focused engineering pass
**Branch:** `release/v2`
**Known current tip before work:** `a9d6439a31a3e3ad783ead825ae2880cc7aa72ac`
**Purpose:** Fix the two concrete host-contract regressions exposed by the shortened V2 description with the smallest safe patch, run only the required local deterministic checks, then push. ChatGPT/André will take over deployment verification and host regression.

## Read first

Primary audit: `getcarwise-docs/AUDIT_V1_V2_SPECIAL_FIELD_INSTRUCTION_GAPS_20260911.md`.

Do not spend remaining context re-auditing the whole application. The relevant findings have already been source-checked against `release/v2`.

## Confirmed problems to fix

### 1. Broad `bodyType` duplicated into `vehicleType`

Canonical regression: broad SUV request was encoded by ChatGPT V2 with both `bodyType: "SUV"` and `vehicleType: "SUV"`. That reduced the Denver result universe to 17, while Claude V2 and ChatGPT V1 omitted `vehicleType` and both saw 13,617 matches.

Source facts already verified:
- Public schema retains both fields.
- `bodyType` is described as the broad body style.
- `vehicleType` is described as a finer classification "when the user expressly distinguishes it" but still gives `SUV` as an example, creating ambiguity.
- A supplied `vehicleType` becomes the real provider `vehicle.type` filter.
- The provider field is undocumented/inconsistently tagged; prior description-only warnings did not reliably stop hosts from using it.

Required outcome: a normal broad-body request such as "SUV" must not acquire a redundant `vehicle.type=SUV` restriction. Preserve genuine finer-classification capability only if it can be made safe. Do not rely on a description-only warning as the sole protection.

### 2. Host invents hard filters

ChatGPT V2 added `transmission: "Automatic"` to two natural requests that never stated transmission. Claude did not. V1 had an explicit rule not to invent hard filters that the user did not state or clearly imply; that semantic guardrail was weakened in the shorter contract.

Required outcome: restore that semantic guardrail concisely so direct hard-filter inputs represent user-stated or clearly-implied requirements. This is not a request to restore the long V1 manual.

## Secondary wording/recovery check

V1 explicitly told the host not to independently retry thin searches because the service owns automatic widening. V2 still has deterministic widening in code, but Test #4 showed ChatGPT making repeated calls and changing geography. If a very small, declarative wording adjustment can clarify that the service owns bounded search widening/recovery without using Anthropic-problematic "always/must/never invoke" language, include it. Do not redesign recovery logic in this pass unless directly necessary for the two confirmed regressions above.

## Do NOT expand scope

Do not touch V1/main, V3, deployment configuration, Vercel, link logic, NHTSA/electrification logic, ranking, history/CPO semantics, or unrelated tests.

Do not remove `cpo`, `noAccidents`, `oneOwner`, or `seatsMinPreference` merely because they are not safe provider hard filters; their evidence/disclosure semantics are intentional.

Do not rework `interiorColor`/`cylinders` now. They are regression-test watch items for ChatGPT/André after deployment, not confirmed code defects in this patch.

## Minimum verification before push

Use the smallest deterministic verification that still satisfies repository discipline:
1. Add/adjust a regression assertion for the bodyType/vehicleType safety behavior if the chosen implementation has a deterministic boundary that can be tested locally.
2. Run the directly affected test(s), then `npm test` if feasible.
3. Run typecheck/build only as required by the repo's existing release discipline; do not spend time on live host tests or deployment checks.
4. Inspect the final diff for unintended changes.
5. Push the completed patch to `release/v2`.

After pushing, report only:
- commit SHA;
- files changed;
- exact behavior chosen for `vehicleType` (removed, gated, or other safe handling);
- concise anti-invention wording change;
- tests/build run and pass/fail;
- anything ChatGPT/André must know before host regression.

No deployment work and no manual ChatGPT/Claude testing after the push. André will monitor automatic Vercel deployment; ChatGPT will verify the commit/diff and run the post-deploy regression plan.
