# PLAN_V2_COMPLETION_AND_RELEASE_BUCKETS_20260907.md

**Status:** Proposed V2 completion plan; no engineering authorization implied.

## Executive recommendation

V2 should remain open, but only for contained corrections to the existing search/result contract. New tools and new buyer workflows belong in V3.

The V2 backlog should be grouped into three controlled release buckets, not one version per ticket:

- V2.4 — Search correctness and condition integrity
- V2.5 — Result presentation and action integrity
- V2.6 — Input and scope robustness

Each bucket should ship only after its included items are either fixed and tested or explicitly removed from the bucket. A separate V2.x number is justified when behavior changes are independently testable, user-visible, and likely to require separate regression evidence—not merely because a task exists.

## Evidence base

The source list is the “Consolidated CarClever MCP To-Do List” appended to getcarwise-docs/HANDOFF_RECALLS_INVESTIGATION_20260904.md, cross-referenced with TASKS.md, STATE.md, and the recorded V2/V3 testing history.

The list contains genuine V2 defects, unconfirmed observations, already-completed work, future capabilities, and administrative tasks. They must not be treated as one undifferentiated backlog.

## Proposed V2 buckets

### V2.4 — Search correctness and condition integrity

**Primary candidate: hybrid-result contamination.**

Problem: vehicle.fuel is unreliable enough that gas trims can appear in hybrid-only searches. This directly violates an existing search constraint and affects result correctness.

Recommended design:
- Treat this as the highest-priority V2 candidate.
- Preserve hybrid/PHEV intent as a hard semantic requirement.
- Use the stronger NHTSA electrification signal if empirical testing confirms it remains reliable; otherwise use the cheaper existing-field patch with an explicit verification fallback.
- Do not silently classify unknown as non-hybrid.
- Add fixtures covering hybrid-only, PHEV-only, mixed hybrid/gas model families, ambiguous trims, and unavailable electrification data.

**Conditional candidate: match-score differentiation.**

If structurally different vehicles receive identical matchScore values, include this in V2.4 only if the fix is bounded to ranking/match explanation. If it requires a new scoring philosophy, provider reweighting, or a redesign of the flagship’s deal-scoring role, defer it.

### V2.5 — Result presentation and action integrity

**Conditional candidate: Link/Carfax/photo display consistency.**

Include only after reproducing the defect on the V2 deployment. Treat the card payload and rendered widget as separate verification targets. Do not solve this by adding more prose or exposing provider fields.

**Conditional candidate: VIN Buyer Check widget non-render.**

Observed once and not reproduced. Keep as a verification item, not an implementation item. Promote only with deterministic reproduction.

**Conditional candidate: CarMax failures.**

The earlier 3/3 failure result was unconfirmed and may have been transient. Keep as a test fixture only. Do not ship a special CarMax rule without an independent, generalizable cause.

### V2.6 — Input and result-scope robustness

**Low-priority candidate: malformed ZIP handling.**

The host model intercepted 00000 during one test, so tool-layer behavior remains unknown. Test malformed, missing, non-US, and valid ZIP values directly. If safe already, close as verified; otherwise add a narrow validation/unknown-state fix.

**Low-priority candidate: non-passenger vehicles in broad searches.**

ATVs/trailers may be a provider data-scope characteristic. Include only if the product promise is explicitly passenger vehicles and a deterministic post-filter removes false scope without damaging legitimate results.

**Already resolved: result-count funnel display.**

The count fix is part of V2.1 and should not become another release item unless a new regression appears.

## Items deliberately outside V2

Affordability; adaptive comparison; tap-to-act button row; expanded recalls or check_vehicle routing changes; AI invocation and tool-description redesign; non-Edmunds monetization fallback; cross-session persistence; and facets, VIN anatomy, and qualifier-accounting redesign.

These change product capability or tool behavior and belong in V3 or later.

## Release-numbering recommendation

Do not create V2.4, V2.5, and V2.6 automatically before investigation. Use them as proposed buckets:

1. Investigate hybrid contamination first. If confirmed and fixable within the existing contract, it becomes V2.4.
2. Investigate card/link/image consistency, VIN widget rendering, and CarMax behavior together because they share a presentation/integration verification surface. Ship as V2.5 only if defects reproduce.
3. Investigate malformed ZIP and non-passenger scope separately. Ship V2.6 only if a real tool-layer defect is found; otherwise close or defer without creating a release.

If V2.4 and V2.5 are ready at the same time, they may be combined into one release candidate while keeping internal test suites separate. Avoid one version per bug.

## Required investigation gates

Before promoting any item into V2:
- reproduce it against the V2 deployment;
- establish whether it is an app defect, provider limitation, or host-model behavior;
- define the smallest behavior change;
- test Claude and ChatGPT where routing or rendering is involved;
- run the full V2 regression suite;
- verify V1 remains untouched;
- record the result as confirmed, unconfirmed, provider-limited, or deferred.

## Final rule

V2 is feature-complete but defect-open. V2 may receive contained fixes to existing behavior; V3 receives new tools, new workflows, and invocation-oriented product design.
