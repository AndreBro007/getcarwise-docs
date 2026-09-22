# Gated Claude Handoff — CarClever Lite Page 239 Replacement

**Task:** #72  
**Status:** **DRAFT / DO NOT START — requires André’s explicit approval of the product direction**  
**Target repository if approved:** AndreBro007/carclever-widget (widget/admin repo only)  
**Engineering lane:** Claude  
**Reference design:** getcarwise-docs/STRATEGY_CARCLEVER_LITE_FRACTAL_EXIT_REPLACEMENT_20260922.md

## Gate

Do not modify code, WordPress, Vercel, DNS, Fractal, connectors, subscriptions, reviewed app endpoints or production. Do not begin unless André explicitly approves the recommended CarClever Decision Center direction and authorizes this handoff.

After approval, the first authorized work is a read-only evidence and engineering-design return. Production implementation still requires separate explicit authorization after design review.

## Proposed product direction

Replace the Fractal-dependent chat UI embedded at WordPress page 239 with a conversion-focused decision center at the existing widget/embed URL. Route people into existing Find My Car, Deal Score, Price Check and VIN Check experiences, plus separate New, Used and contextual Trade-in actions using verified approved destinations.

Do not do a URL-only MCP swap. Do not build a broader assistant or duplicate existing tools in the initial release. Do not include the private Impact Catalog prototype. Do not modify the old Fractal-hosted @CarClever app or any other page/tool.

## Phase 0 — bounded read-only audit (first return; no code edits)

1. Verify current page 239 WordPress content, iframe/embed URL and relevant inbound/outbound links. Record the exact widget route and present Fractal dependencies.
2. Inventory approved destination URLs and map each to New, Used, Trade-in, tool destination or editorial content. Record source/owner, link type, destination and tracking values that must remain unchanged. Do not create/edit links.
3. Identify current website destinations for Find My Car, Deal Score, Price Check, VIN Check, New inventory, Used inventory and Trade-in. Flag unavailable/unverified targets; do not guess.
4. Return available GA4/GSC page-239 baseline for recent 28- and 90-day periods, outbound events and any page/widget lead data. Check whether either historic completed lead can be attributed to page 239 or old-app route. Mark missing evidence unavailable.
5. Record current Lite Anthropic API use/cost if observable and the precise Fractal call path. Do not infer savings from code removal alone.
6. Inspect consent behavior across WordPress and embedded Vercel widget, GA4 events and affiliate click measurement. Propose a minimal event contract with no VIN, credit, precise budget, identity or other unnecessary personal data.
7. Confirm whether page 239/embed is included in the active $25k or $40k SEO measurement windows. If uncertain, leave page/copy/SEO changes out of scope and report uncertainty.
8. Return only a proposal: user-flow map, component/function list, exact verified destinations, missing dependencies, event schema, estimate/risk, preview acceptance plan and rollback. Do not implement.

## Proposed first-release interaction contract (subject to verified destinations)

- “Find a vehicle” → existing website Find My Car destination, if verified.
- “Evaluate a vehicle I found” → Deal Score, with separate Price Check and VIN Check routes.
- “Check a VIN” → VIN Check.
- “Check whether the price is fair” → Price Check.
- “Sell or trade my current vehicle” → verified Trade-in destination.
- New and Used actions remain distinct and appear only where relevant.
- Explain each existing tool’s role and material data limits.
- Use exact approved URLs confirmed in Phase 0; preserve required tracking values unchanged.
- No free-form chat, new API call, Catalog search, account, VIN collection or new lead form in release one.

## Future implementation scope (not authorized by this handoff)

Only after André reviews Phase 0 and separately authorizes implementation:

1. Create an isolated branch and preview. Do not push to production or change the live WordPress page.
2. Keep page-239 embed URL stable unless separately approved.
3. Implement the decision-center interface without calling Fractal or a new model API.
4. Link to existing tools instead of duplicating data logic.
5. Add only measurement approved in the Phase 0 design and supported by current consent/Impact behavior.
6. Disclose affiliate destinations and distinguish GetCarWise tools from Edmunds destinations.
7. Provide keyboard access, mobile layout, clear failure states and navigation when analytics/affiliate scripts are unavailable.
8. Retain a reversible route/configuration flag or documented release artifact.
9. Leave $25k/$40k page copy, links, canonical data, structured data and SEO treatment untouched.
10. Do not touch old ChatGPT app, Fractal account, Auto.dev plan, Catalog prototype, production MCP endpoints or other tools.

## Preview acceptance gates (only after separate build authorization)

- Every route goes to the exact Phase 0 verified destination.
- New, Used and Trade-in are distinct and contextually appropriate.
- No unsupported local-inventory, condition, lender or VIN-analysis claims appear.
- No new Fractal MCP request occurs from page 239.
- No duplicate Deal Score, Price Check or VIN Check behavior is introduced.
- Analytics respects consent and contains no VIN or sensitive inputs.
- Mobile, desktop, keyboard, consent-denied, offline/empty and link-fallback states are checked.
- Original page/embed and rollback artifact remain recoverable.
- No edit touches active $25k/$40k SEO treatments.
- André reviews preview and explicitly authorizes publication.

## Explicitly not authorized

- Any code change before André approves the product direction.
- WordPress edits, production deployment, DNS or configuration changes.
- Fractal endpoint/account/subscription change or old-app retirement.
- Auto.dev Growth/Free change.
- Impact link creation/modification or Catalog publication.
- Changes to Find My Car or Anthropic/OpenAI/Meta submissions.