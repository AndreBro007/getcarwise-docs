# Addendum — Sep 30 checkpoint: new CarClever's App Directory approval isn't factored in

**Date:** Sep 27, 2026. **Owner:** Claude, Engineering lane (flagged during a session review/cleanup pass; no decision made here).

**What this addendum does:** points out a gap in `CHECKPOINT_SEPTEMBER_SCALE_DOWN_FEASIBILITY_20260923.md` — it does not change that document's numbers, dependency map, or recommendation.

## The gap

The Sep 23 checkpoint frames old CarClever/Fractal retention purely as a **cost/dependency** question: what breaks if Fractal is cancelled, what Auto.dev Free-tier guards are needed, what the resulting monthly cost is. That framing was accurate on Sep 23.

One day later (Sep 24), "CarClever - Find My Car" — the new, Vercel-hosted app — was approved and published to the **ChatGPT App Directory** (`SYS-20260924-007`, live public listing, "Connected on Sep 26"). This is a genuinely new fact: a public, working, approved replacement for old CarClever's core "find/check a car via ChatGPT" use case now exists, independent of Fractal or Auto.dev Growth-tier data.

The Sep 23 checkpoint was written before this happened and has not been revisited since. It still treats old CarClever's exit purely as a hosting-cost decision ("cheapest configuration whose live paths still pass functional checks"), not as a **replacement-driven** decision ("do we still need old CarClever/page 239/Fractal running at all, now that a public alternative exists, regardless of what it costs to keep them alive?").

## What this doesn't change

- The dependency map, cost table, and partner-outcome evidence in the Sep 23 checkpoint are all still accurate as far as they go — nothing here contradicts them.
- The Auto.dev Free-tier downgrade prep (Task #79/#80) is unaffected either way — that work stands regardless of whether old CarClever is ultimately kept or retired.
- No lead-attribution, cost, or usage evidence changes as a result of the Directory approval — it's a distribution fact, not a measurement fact.

## What's worth doing before Sep 30

Fold this fact into the actual decision conversation — not necessarily a rewrite of the checkpoint doc, but at minimum an explicit acknowledgment that "keep Fractal, but free" (the option currently favored) is being weighed against "the new app already does this, does old CarClever still earn its keep at any price" — a question the current checkpoint doesn't ask.

**References:** `CHECKPOINT_SEPTEMBER_SCALE_DOWN_FEASIBILITY_20260923.md`; `DECISIONS.md` `SYS-20260924-007` (carclever-widget); this session, Sep 27, 2026.
