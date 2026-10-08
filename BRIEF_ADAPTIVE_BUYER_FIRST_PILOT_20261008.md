# First pilot: an adaptive car-buying conversation

Date: 8 October 2026
Status: proposed pilot design; no prototype, recruitment or deployment completed by this brief.

## Decision

Start with US buyers who already have two or three cars in mind and are stuck choosing. Call the initial offer “Bring your shortlist. Work out what needs to be true before you buy.”

This is a starting audience and promise, not a fixed questionnaire. If the conversation reveals a different problem, change the activity while keeping the buyer's goal and verified evidence.

The commercial outcome is a useful, buyer-chosen dealer enquiry through the eligible Edmunds affiliate journey. The product must first help the buyer make a better decision. A recommendation to wait, reject a car or investigate another option is a legitimate outcome.

This pilot tests whether this specific adaptive experience helps real buyers progress. It does not establish that nobody else has built something similar.

## What a buyer experiences

Initial invitation:

> Bring the two or three cars you are considering, and tell us what is stopping you choosing. We will help you compare the compromises and work out what to check next.

Accept model descriptions or structured listing details when reliable retrieval of supplied URLs is unavailable. Do not promise arbitrary website extraction.

The opening question should use what the buyer already supplied. If their blocker is explicit, begin there instead of asking a generic intake form.

Maintain a small visible buying brief:
- cars being considered;
- buyer priorities and constraints, which they can revise;
- buying conditions: supported by evidence, needs checking, or not met;
- the current unresolved question;
- the next useful action and why it matters.

Evidence labels must distinguish a buyer's statement, catalogue data, another cited source, a calculation, and a dealer's unverified answer. Catalogue specifications do not prove that a particular used vehicle has an option, remains available, or is in a particular condition.

## Three hypothetical conversation paths

| Buyer says | Immediate adaptation | Useful outcome | Possible dealer enquiry |
|---|---|---|---|
| “I prefer A, but I cannot stretch the budget.” | Ask whether the uncertainty is the advertised price or the final total. Show an explicit calculation with known inputs and missing amounts. Reconsider the shortlist if affordability is already ruled out. | A buyer-defined maximum and a clear account of what remains unknown. | Request an itemised out-the-door price for a suitable specific car. |
| “My partner wants the bigger one; I want something easier to park.” | Switch from ranking cars to separate priorities. Identify which compromises each person would accept. Offer a shareable summary with the buyer's consent. | A shared condition such as acceptable passenger space and practical parking fit. | Ask for a test drive to check the specific concern, using the supported Edmunds contact path. |
| “The listing looks right, but I need that exact feature.” | Switch from general comparison to evidence about the particular vehicle. Mark generic model specifications separately from vehicle-level confirmation. | A precise feature requirement and a question the dealer can answer. | Ask the dealer to confirm the equipment and, where appropriate, provide supporting information. |

All examples are hypothetical. Do not fabricate prices, local stock, availability, equipment, quotations or responses.

### Returning with an answer

If the buyer says, “The dealer confirmed that the car lacks the feature,” update the condition to not met, explain the consequence, and reconsider the remaining cars.

If the buyer says, “The total is above my maximum,” update the calculation and ask whether the maximum is firm. Do not silently relax it.

If the answer resolves the buyer's concern, show what is now supported and what still needs checking. Let the buyer decide whether to proceed.

The same conversation should accept a pasted dealer answer. Persistent return sessions and household sharing can follow after the core loop works; cross-session memory needs clear controls.

## Minimum prototype

Build a private web experience with:
1. One shortlist entry point and one conversation.
2. A few useful display formats: comparison, buying conditions, calculation and dealer question.
3. Structured buyer state that can change after each reply.
4. Grounded catalogue/source retrieval where currently available.
5. The existing eligible Edmunds handoff and permitted tracking.
6. Minimal event collection and feedback.

AI chooses the next useful activity and wording from these supported capabilities. It does not need to generate or rewrite production code during a conversation.

Reuse working project infrastructure where feasible. Before implementation, establish what is actually available in the current stack: supported data fields, data freshness, retrieval, model access and the affiliate destination. If one dependency is missing, narrow the first prototype rather than quietly inventing it.

Keep merchant-approved creative and link requirements intact. Dynamic conversation text does not imply blanket permission to modify affiliate assets or tracking links. Confirm the applicable permissions against the current account agreement during implementation.

## Reach buyers while the prototype is being prepared

Use one relevant community as the first proposed source, with Reddit first in the current priority list. Determine whether a moderator or community owner welcomes a limited buyer trial before depending on that channel.

Draft invitation:

> Already choosing between two or three cars? We are trying a tool that helps you compare the compromises and prepare the questions you still need answered before buying. Bring your shortlist and the thing you are stuck on.

Accompany public or participant-facing use with the appropriate affiliate disclosure. Do not claim unbiased rankings unless the ranking behavior supports that claim.

This is draft copy only. No posts, messages or recruitment have been sent.

Find people actively considering a purchase, not only people willing to try an AI demo. Do not make app-directory discovery, native Reddit integration, or a broad SEO campaign prerequisites for the first learning cycle.

## First cohort and live learning

Use the first ten real buyers as a practical qualitative checkpoint, not a statistically meaningful conversion test. Owner and developer sessions are marked as tests and excluded from buyer outcomes.

Within a conversation:
- use explicit corrections immediately;
- let buyers revise priorities and conditions;
- ask a short clarification when an answer changes the task;
- offer a useful next action without making dealer contact mandatory.

Between conversations:
- capture recurring problems and proposed changes;
- version changes to the entry promise, questions and display behavior;
- promote changes based on repeated evidence and review, with rollback available;
- keep factual grounding and affiliate requirements fixed.

One conversation can reveal a defect worth fixing immediately. One success does not establish a winning acquisition or conversion strategy. Silence and lack of clicks do not tell us the reason by themselves.

## Minimum measurement

| Layer | Record | What it tells us |
|---|---|---|
| Access | Source, entry promise, non-test session start | Whether the chosen source and invitation reach the intended buyers. |
| Helpfulness | Starting blocker, changed condition, buyer's short feedback | Whether the interaction resolved something useful. |
| Intent | Selected next action and stated contact reason | Whether the buyer sees a real purpose for a dealer enquiry. |
| Handoff | Eligible outbound click and permitted campaign/session identifier | Whether the buyer reaches the supported Edmunds destination. |
| Commercial result | Available Impact reporting, approved actions and revenue | Whether the affiliate journey produces credited outcomes. |

Do not equate a click with a submitted dealer enquiry or a payable action. Our own site cannot directly observe every merchant-side step. Use reporting actually supplied by the merchant/platform; do not assert person-level attribution where it is unavailable.

Offer an optional return prompt: “Did you get the answer you needed?” Any reminder or follow-up requires the buyer to opt in.

## Budget and progress decisions

The owner's $200/month limit is the total operating ceiling, not an extra allowance for this pilot. Currency and existing recurring charges must be established before committing new spending. Use current services where practical; no paid acquisition in the first pilot.

Continue when there is repeatable evidence that:
- reachable, intended buyers engage with the offer;
- the conversation resolves a meaningful blocker;
- buyers choose a specific next step for a clear reason;
- eligible handoffs are recorded correctly;
- subsequent reporting can establish commercial outcomes.

These are separate milestones. Helpful sessions and handoffs support continued bounded learning; approved affiliate revenue is needed to validate monetization. Define any higher spending decision around observed unit economics, not engagement alone.

If there is little movement, change the failing layer:
- no suitable entrants: source or invitation;
- entrants abandon: opening or interaction;
- useful sessions without contact intent: unresolved need, timing or offer;
- intent without handoff: friction or destination;
- handoffs without credited outcomes: attribution, eligibility or merchant journey.

A ten-person sample cannot distinguish all these causes or validate revenue. Use the cohort to identify the next concrete change, with spending remaining capped.

## Work sequence

1. Review this brief against three realistic buyer cases and the current project capabilities.
2. Produce an implementation brief and a private prototype of the complete conversation-to-handoff loop.
3. In parallel, establish one permitted route to real buyers and prepare recruitment material.
4. Run a short pilot, adapt within conversations, and make documented changes for subsequent buyers.
5. Expand the useful buyer situation into another channel only after there is evidence supporting it.

The immediate deliverable is the first complete buyer experience and a feasibility decision, not twelve platform launches. Once implemented, the next deliverable is observed buyer behavior and the changes it justifies.
