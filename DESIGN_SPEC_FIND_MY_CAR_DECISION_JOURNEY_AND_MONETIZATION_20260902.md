# DESIGN_SPEC_FIND_MY_CAR_DECISION_JOURNEY_AND_MONETIZATION_20260902.md

**Status:** Proposed design for Claude engineering investigation and implementation planning. Pending empirical validation and André approval before production behavior changes.

## Purpose

Extend Find My Car from a vehicle shortlist into a lean, evidence-based buying assistant:

1. find suitable vehicles;
2. check a specific VIN/listing;
3. surface recall and purchase-risk evidence;
4. estimate financing;
5. compare shortlisted vehicles;
6. let the user take a clear next action;
7. hand the user to a trustworthy Edmunds destination where listing, finance, or trade-in activity can continue and affiliate attribution can occur.

The frontend should remain lean. Complete evidence stays in structured output for the AI to interpret in natural language.

## Guardrails

- This is a design/investigation brief, not authorization to merge or deploy.
- Find My Car remains under review; preserve the merge freeze until André confirms review has concluded.
- Do not modify the submitted production path without the approval/regression gate.
- Preserve raw provider fields alongside canonical values.
- Unknown is not false, and absence of recall data is not proof of no recalls.
- Do not expose provider internals, raw JSON, numeric risk scores, or affiliate mechanics to users.
- Never send users to a dead, empty, editorial, or materially irrelevant destination.

## A. Buyer Check and recall design

The existing VIN-first Buyer Check remains categorical, not numeric. Natural-language triggers should include:

- “Is this VIN a safe buy?”
- “Would you buy this car?”
- “Any red flags?”
- “Is this vehicle worth considering?”
- “What should I verify before buying?”

“Safe buy” means an evidence-based purchase-risk review, never a safety or mechanical guarantee.

Default card output should be compact:

- Buyer Check status;
- one short explanation;
- one action such as Buyer Check or View listing.

For recalls, display only a vehicle-level status by default:

- no open recall signal found in available data;
- open recall identified;
- recall status unavailable;
- recall status needs verification.

Provide the AI with the complete decision-relevant recall evidence:

- campaign/recall ID;
- title;
- affected component;
- defect/consequence;
- remedy;
- open/resolved/unknown status;
- recall date;
- VIN applicability;
- source;
- raw provider fields;
- conflicts and missing data.

When asked, the AI should explain the relevant recall, whether completion is known, and what to verify with NHTSA, the manufacturer, or the dealer. Do not display a long historical recall catalogue by default.

## B. Affordability design

V1 is a deterministic loan-payment estimate, not an affordability approval or “you can afford it” judgment.

Compact display:

- estimated monthly payment;
- vehicle price;
- term;
- estimated APR;
- down payment assumption.

Structured output should retain:

- all calculation inputs;
- APR source/default;
- term;
- deposit;
- fees/tax treatment;
- amount financed;
- monthly payment;
- total interest;
- rounding;
- missing-input behavior;
- calculation notes.

Before implementation, independently validate amortization math, APR defaults, rounding, zero-down behavior, unknown price/APR behavior, and schema integration.

Keep affordability separate from Buyer Check. The AI may synthesize both, but must not create a false composite score.

## C. AI-driven comparison

Comparison should be adaptive to the user’s stated priorities, not a fixed universal score or table.

The AI should be able to identify:

- best fit for the request;
- best value;
- lowest estimated payment;
- lower apparent purchase risk;
- important trade-offs;
- unknowns requiring verification.

Provide the AI with the complete comparison set:

- identity and listing data;
- hard constraints and preferences;
- match-score breakdown;
- Buyer Check/risk and recall summaries;
- affordability values and assumptions;
- link quality;
- unknowns and conflicts.

The frontend should show only the conclusion and two or three material trade-offs. The AI may say that different vehicles win on different dimensions.

## D. Tap-to-act design

The action row should be compact and context-aware. Candidate actions:

- Buyer Check;
- Compare;
- Estimate payment;
- View actual listing;
- Finance this vehicle;
- Value my trade-in.

Show no more than about three actions at once, selected according to the user’s current intent and the capabilities verified for that result.

A/B/C position labels remain internal routing identity unless user-facing wording makes them useful. Preserve identity across pagination and sorting. Follow-up messages must embed VIN, make, model, year, and price so the next action cannot select the wrong vehicle.

## E. Edmunds website destination resolution

This is a website investigation, not an API assumption.

Current behavior constructs:

- a VIN-specific Edmunds URL;
- a make/model or trim/year fallback;
- a CJ-wrapped affiliate URL.

The critical rule is:

**constructed URL does not equal verified destination.**

For the top monetizable candidates:

1. construct the raw Edmunds URL;
2. validate the raw URL before CJ wrapping;
3. follow redirects;
4. classify the page as exact listing, inventory, editorial, empty, error, or unreachable;
5. verify VIN and vehicle identity where applicable;
6. only then wrap the validated raw URL with CJ;
7. return the CJ URL to the user.

Do not validate the CJ redirect first.

### Fallback hierarchy

- Tier 1: verified VIN-specific listing — “View this vehicle.”
- Tier 2: verified relevant Edmunds inventory — “View similar listings.”
- Tier 3: only if Edmunds’ own website produces a stable, reusable filtered destination — “Find closer matches.”
- None: suppress the listing CTA.

Do not claim year, price, ZIP, trim, or location filtering unless the final page actually proves it. Existing documentation says some URL patterns are live-tested, but those claims must be rechecked because a current year-form URL test redirected to an editorial page.

### Website investigation fixtures

Test a fixed set of existing generated URLs covering:

- common vehicles;
- new and used;
- safe and punctuation-heavy trims;
- rare/discontinued models;
- known Carvana cases;
- live and likely-delisted VINs.

Record:

- original URL;
- final URL;
- HTTP/redirect behavior;
- page type;
- title and visible vehicle identity;
- VIN match;
- inventory presence/count;
- relevant filters shown;
- added latency;
- failure reason.

Test Edmunds’ interactive filters separately for year, type, price, ZIP, and radius. Capture the final URL after filtering, reload it independently, and determine whether the filtered state persists.

## F. Finance, trade-in, and later monetization

The preferred destination is the actual Edmunds listing. Where Edmunds offers a relevant vehicle-specific finance continuation, use it after validation. For trade-in, use a clearly labelled action that may require additional user input.

Do not recreate every Edmunds feature in CarClever. Use CarClever for decision support and Edmunds for deeper listing, finance, and trade-in continuation.

Log outbound opportunities before redirecting:

- session/search ID;
- VIN and vehicle identity;
- result position;
- action type;
- destination tier/type;
- raw destination;
- CJ destination;
- validation result;
- timestamp;
- campaign/click identifier where available.

Log the outbound opportunity, but do not claim a commission until affiliate reporting confirms it. If the user returns to the same conversation, the AI should be able to refer to the previously selected vehicle where the available session context supports it.

## G. Lean frontend contract

Default cards answer:

1. What is this vehicle?
2. Why is it here?
3. What can I do next?

Keep detailed evidence in structured output. Suggested structured fields include:

- recall summary and full recall records;
- Buyer Check evidence;
- affordability assumptions/results;
- comparison attributes;
- available actions;
- destination URL and validation metadata.

Never expose raw provider fields, raw URLs, redirect mechanics, or affiliate identifiers in the normal user experience.

## Required Claude investigation deliverable

Before production implementation, Claude should return:

1. current-flow map and affected files;
2. website-validation feasibility and call/latency measurements;
3. Edmunds fallback test matrix and results;
4. recommended destination classification contract;
5. affordability validation report;
6. proposed test fixtures and regression cases;
7. implementation sequence and risk assessment.

No production behavior change should be promoted until the investigation is reviewed and the approval/regression gate is satisfied.
