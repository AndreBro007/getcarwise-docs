# CarClever OpenAI V2 Resubmission Record — 2026-09-12

**Status:** SUBMITTED — OPENAI REVIEW  
**Lane:** ChatGPT Business/Strategy  
**App:** CarClever - Find My Car  
**Version:** 1.0.0  
**App ID:** `asdk_app_v_6a85781a44e08191bdf490bb2774b086`

## 1. Submission outcome

André confirmed the edited CarClever - Find My Car submission was successfully resubmitted in the OpenAI dashboard on 2026-09-12. The dashboard shows version `1.0.0` with status `Review`.

This remains the app's initial public release version. The Sep 12 event is a review resubmission after remediation, not a released-version upgrade.

## 2. Final submitted production configuration

- MCP endpoint: `https://carclever-oai.getcarwise.app/mcp`
- GitHub source repo: `AndreBro007/carclever-find-my-car`
- source branch: `release/v2`
- submitted source tip: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`
- OpenAI Vercel project: `ccfmc-dev-v2`
- custom production domain: `carclever-oai.getcarwise.app`
- default Vercel production domain remains attached: `ccfmc-dev-v2.vercel.app`
- production config: `NEXT_PUBLIC_WIDGET_ORIGIN=https://carclever-oai.getcarwise.app`

The default Vercel domain was deliberately retained. The code now uses a project-specific configurable production widget origin so the shared V2 codebase can later serve a separate Anthropic deployment without globally hardcoding the OpenAI hostname.

## 3. Final OpenAI Scan Tools verification

The final exported submission JSON showed:

- MCP URL: `https://carclever-oai.getcarwise.app/mcp`
- safety status: `SCANNED_OK`
- auth: `NONE`
- `openai/widgetDomain`: `https://carclever-oai.getcarwise.app`
- CSP `resourceDomains`: `https://carclever-oai.getcarwise.app`
- tools: `find_matching_vehicle`, `resolve_dealer_url`
- annotations on both tools: `readOnlyHint=true`, `openWorldHint=true`, `destructiveHint=false`
- V2 input schema includes `vehicleNeeds`, `electrificationTypes`, `electrificationRequirement`, and no legacy `goals`

The widget-origin mismatch discovered immediately before submission was fixed by commit `b8b07d8`, which makes `getAppOrigin()` honor the project-specific `NEXT_PUBLIC_WIDGET_ORIGIN` in production while preserving preview behavior and safe fallback logic.

## 4. Final app description

The submitted description is:

> Find My Car searches live U.S. new and used vehicle inventory to help shoppers find the right car for their needs and budget.
> Search by specific or combined requirements, lifestyle needs, and priorities such as cheapest, newest, lowest mileage, or lower-risk options, including detailed criteria such as trim, color, drivetrain, transmission, cylinders, condition, and electrification.
> Requests like “AWD SUV under $35k” and “reliable car for a teen driver” both work, with broader needs translated into relevant real vehicle models before searching current inventory.
> Already found a car? Look up the exact VIN and run a Buyer Check for red flags, good signs, and what to verify before buying.
> Core vehicle identity is VIN-cross-checked, and every returned match is checked against each hard filter applied.
> Unreported accident, ownership, or CPO data is shown as unconfirmed—not assumed clean.
> Each result includes links to check availability and see similar vehicles.

The final edit deliberately preserved existing user-facing marketing language and added only material V2 capability expansion rather than rewriting stable copy.

## 5. Rejection remediation addressed

The prior OpenAI rejection cited two categories:

1. tools requesting input data that was overly broad/unnecessary or included excessive conversation context;
2. tool naming and description quality, including descriptions that must clearly explain correct usage without comparative/biased/preferential wording.

The resubmitted V2 contract addressed those issues through a narrower structured schema, `vehicleNeeds` rather than transcript-like goals/history, explicit anti-invention guidance, first-class electrification fields, clearer tool boundaries, and tighter tool descriptions.

André chose remediation and resubmission rather than replying to the rejection email as an appeal.

## 6. Final positive tests submitted

1. `Find a used Honda CR-V under $25,000 with less than 60,000 miles near 90210.`
2. `Find a reliable hybrid SUV under $50,000 with less than 60,000 miles near 90210.`
3. `Find a low-risk used F-150 under $50,000 for towing near Denver.`
4. `Check VIN 4T1DAACK6SU582551 for red flags before I buy it.`
5. `Check availability for the 2025 Toyota Camry with VIN 4T1DAACK6SU582551.`

Test #5 was changed from the prior context-dependent wording `Click “Check availability” on one of the returned vehicle listings.` to a self-contained reviewer-runnable prompt.

## 7. Final negative tests submitted

1. `How do I replace the brake pads on a 2020 Honda CR-V?`
2. `What is the towing capacity of a 2024 Ford F-150?`
3. `What are the pros and cons of hybrid cars compared with gas cars?`

Expected behavior remains non-invocation for all three.

## 8. Final live ChatGPT smoke tests on the new domain

Before clicking Submit, André deleted the old ChatGPT developer plugin and recreated it against `https://carclever-oai.getcarwise.app/mcp`.

Observed passes:

### Standard inventory search

Prompt: `large suv under 60k in 90210`

- CarClever invoked normally;
- listing carousel rendered;
- result text and cards were coherent;
- current inventory links rendered.

### Exact VIN Buyer Check

Prompt used in the isolated diagnostic run:

`Check VIN 4T1DAACK6SU582551 for red flags before I buy it.`

- exact VIN returned;
- Buyer Check card rendered;
- reported accident concern produced Caution;
- no similar VIN substitution;
- card and text response agreed on core risk state.

### Self-contained availability test in a fresh chat

Prompt:

`Check availability for the 2025 Toyota Camry with VIN 4T1DAACK6SU582551.`

- CarClever invoked;
- exact listing card rendered;
- exact Edmunds destination was returned;
- response appropriately reminded the user that seller availability can change.

These passes establish that the custom OpenAI domain works end-to-end in ChatGPT for normal search, exact VIN Buyer Check, widget rendering, and destination resolution.

## 9. Fixture caveat

VIN `4T1DAACK6SU582551` is live inventory and may change price, trim/reporting detail, availability state, or disappear entirely. It is a validated submission-time fixture, not a permanent deterministic test record.

The existing screenshot using an older VIN remains acceptable as visual evidence only. Historical screenshot VIN status is not expected to remain live indefinitely.

## 10. Tool annotations and justifications

Final annotations for both tools:

- Read Only: `true`
- Open World: `true`
- Destructive: `false`

The submitted justifications correctly state that both tools only search/resolve external vehicle data and do not purchase, reserve, create, update, delete, or otherwise change external state.

## 11. Submission artifacts

The user supplied the final OpenAI JSON export after submission; it was inspected in-session and showed `status: REVIEW` together with the correct custom MCP/widget/CSP configuration.

Repository audit snapshots are stored under `carclever-widget/openai-submissions/` and indexed by `OPENAI_SUBMISSIONS_INDEX.md`.

The screenshot supplied by André visually confirms the OpenAI dashboard row:

- `CarClever - Find My Car`
- version `1.0.0`
- status `Review`

## 12. Current gate

OpenAI lane is now frozen at **REVIEW**.

Do not change the submitted OpenAI MCP endpoint, widget-origin configuration, source branch, or reviewer-facing contract during review unless OpenAI requests a correction or André explicitly authorizes a review-critical change.

## 13. Next lane

Proceed to prepare the Anthropic/Claude submission edit using the same V2 codebase, while treating Anthropic as a separate platform deployment/configuration lane. Do not blindly copy the OpenAI custom-origin environment value into the Anthropic project.

V3 remains paused unless André explicitly reopens it.
