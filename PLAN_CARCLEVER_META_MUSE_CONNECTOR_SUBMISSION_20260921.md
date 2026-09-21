# Plan — CarClever Meta Muse Connector Submission

**Date:** 2026-09-21  
**Status:** PROPOSED — ready for André’s approval; no Meta submission, code, Vercel, DNS or production change is authorised by this document  
**Product:** CarClever - Find My Car  
**Owner split:** ChatGPT — submission strategy, listing copy and review evidence; Claude — read-only technical confirmation, then any approved Vercel/DNS/configuration work

## Executive conclusion

Meta has opened the **Muse Connector Platform** for reviewed directory connectors. Its public platform page confirms a three-step path: describe the product, Meta reviews functional/security/legal requirements and completes end-to-end testing, then approved connectors appear in the Muse directory. The submission form, independently recorded by a first submitter, accepts an **Existing MCP** connection type with a hosted MCP endpoint and documentation.

CarClever’s current V2 production contract is already an existing remote MCP server. It therefore does **not** need a Meta-specific API integration, new tool, OAuth implementation, or application-code change merely to submit.

It does need an independent Meta production front door. The proposed contract is:

https://carclever-meta.getcarwise.app/mcp

Meta’s public materials do not state that each connector must have a unique URL. This is a GetCarWise release-control requirement: it prevents Meta review/testing and any later repair from being silently coupled to the OpenAI or Anthropic public endpoints.

## Account, availability and subscription preflight

This must happen before infrastructure work.

1. Open https://muse.ai in a normal browser and create or sign in to one controlled GetCarWise owner account. Use an inbox André controls and can retain for review correspondence; the connector form has been reported to prefer a work email.
2. Do not use a VPN or attempt to bypass a regional rollout. Meta’s launch announcement says Muse is rolling out in the United States. André is operating from Australia, so the first outcome may be a normal availability restriction even though GetCarWise serves the U.S. market.
3. If access is available, complete only the minimal profile/account steps and enable account security, including two-factor authentication if offered. Do not connect email, calendar, social accounts, payment methods, Link, or any other personal service merely to submit CarClever.
4. Review privacy settings before testing. Meta says users can opt out of having Muse interactions used to train its models; choose the appropriate setting intentionally.
5. Keep the free tier initially. Meta says Muse is free for most use, with subscription plans for people who want to do more. Meta does not currently publish the free limits, paid price, or whether a paid plan is required for connector review/testing. The subscription page is login-gated. No plan or payment method should be purchased until the live account shows a concrete limit that blocks this submission or its acceptance tests.
6. From the same account, open https://muse.ai/platform and click Submit a connector. Confirm the account can reach the form, the exact live terms, authentication choices, and whether any verified-business requirement appears. Stop there; do not submit before the Meta endpoint exists and the later gates pass.

**Decision rule:** a free account with form access is sufficient to continue the preflight. A regional/access block is an external gate to record and revisit; it is not a reason to create a different identity or circumvent availability controls.

## What Meta currently requires or asks for

### Publicly confirmed by Meta

- A product description and user-use explanation.
- Meta review for functional, security and legal requirements, including end-to-end testing.
- An approved connector becomes discoverable in Muse; featured placement is editorial.

### Form fields reported by an independent existing-MCP submitter

The September 19 form report is not Meta documentation, but is the best current field-level evidence. It reports:

- connector name; company/developer; product website; example prompts;
- 512 × 512 PNG or SVG icon;
- payment status; submitter name and work email;
- support email or URL; Privacy Policy URL; Terms of Service URL;
- connection type **Existing MCP**; hosted MCP endpoint; documentation;
- access requirements; authentication checkboxes: API keys, OAuth with PKCE, or Other;
- submission authority, no-guarantee/editorial-discretion, and connector-terms confirmations.

No public Meta documentation currently sets a review timeframe, developer fee/revenue share, SDK, or published connector terms. Treat all of those as unknown until the live form or Meta reply says otherwise.

## CarClever readiness assessment

| Area | Current evidence | Submission position |
|---|---|---|
| MCP model | Current production is a remote MCP server with find_matching_vehicle and resolve_dealer_url. | Fits Existing MCP. |
| User authentication | The current OpenAI submission scanned as NONE; the product is free and requires no CarClever account or API key. | No OAuth work should be added just for Meta. If the form requires an auth choice, select **Other** and state “public, unauthenticated MCP; no user account, API key or credential is collected.” Confirm this against the live form. |
| Functional review | The app already has live cross-host MCP smoke evidence and a visual-card/text fallback. | A dedicated Meta endpoint test is still required. |
| Visual card origin | Current code derives the card CSP/resource origin and openai/widgetDomain from NEXT_PUBLIC_WIDGET_ORIGIN in production. | A Meta host should receive a matching carclever-meta origin, not an OpenAI/Anthropic origin. |
| Legal URLs | Live Privacy Policy and Terms of Service URLs exist. | Re-check both and align any stale feature claims before submit. |
| Payments | CarClever is free; it may earn outbound Edmunds affiliate commission but takes no connector payment. | Mark **does not accept payments**. Do not enable Stripe Link. |
| Geography | Product searches U.S. dealer inventory only. | State this explicitly in access requirements and examples. |

## Engineering/operations scope

### Required, no application-code change expected

Claude should create a separate Meta production channel from the same approved release line:

1. Create a Vercel project for the Meta channel, proposed display name carclever-meta, from the shared carclever-find-my-car repository and the already-approved V2 release SHA.
2. Add carclever-meta.getcarwise.app to that project and create the required DNS CNAME at Porkbun.
3. Set the project’s production NEXT_PUBLIC_WIDGET_ORIGIN to https://carclever-meta.getcarwise.app. Copy only the existing required server-side environment variables; never expose their values in documentation or the submission form.
4. Keep automatic custom-domain movement disabled; use the existing deliberate promotion and post-promotion verification procedure.
5. Confirm live raw MCP initialize, tools/list, and resources/read. The resource response must declare the Meta origin in its CSP resource domains. Confirm the live server version is the intended SHA.
6. Run Meta-compatible end-to-end acceptance once Meta’s submission/review flow exposes a test path. Confirm that a normal search and an exact-VIN search return usable text/structured results; visual-card rendering is additive and must never block the text fallback.

This is a new Vercel/DNS/configuration channel, so it is Claude’s engineering lane. The existing code inspection supports a **configuration-only** path; it does not replace the required live checks above.

### Not required unless Meta rejects or testing proves a defect

- No new MCP tools or schema changes.
- No OAuth or API-key layer.
- No changes to OpenAI or Anthropic URLs/projects.
- No changes to affiliate link behaviour or payments.
- No V3 resumption or merge.
- No Meta Model API work; that is separate from the Muse directory.

## Submission pack to prepare

### Overview

- **Connector name:** CarClever - Find My Car
- **Company/developer:** GetCarWise
- **Product website:** verify immediately before submission; preferred product page is https://getcarwise.app/carclever-find-my-car/ if it accurately describes the current V2 contract.
- **Support:** info@getcarwise.app or a stable GetCarWise support URL.
- **Privacy:** https://getcarwise.app/privacy-policy/
- **Terms:** https://getcarwise.app/terms-of-service/
- **Payments:** Does not accept payments.
- **Icon:** reuse a verified CarClever brand asset in 512 × 512 PNG or SVG format; confirm ownership and that it exactly represents the connector.

### Draft neutral directory description

> Search current U.S. dealer vehicle listings in plain language. CarClever returns a concise shortlist using stated budget, location, vehicle, condition and feature preferences, with clear evidence when a requested detail is unconfirmed. It can also look up an exact 17-character VIN when that listing is available. Results may include links to Edmunds or dealer listings for the user to continue their research. Inventory and prices change frequently; verify final availability, condition and terms with the seller.

This deliberately avoids unsupported claims about independent reliability, title verification, financing offers, dealer affiliation, or purchase completion.

### Example prompts

1. “Find a used Honda CR-V under $30,000 near 90210.”
2. “Show me hybrid SUVs under $40,000 near 98101.”
3. “Find the lowest-mileage Toyota Camry under $25,000 near Dallas.”
4. “Check VIN 4T1DAACK6SU582551 for the current listing.”

Re-run all examples immediately before submit; replace the VIN prompt if that inventory record is no longer available.

### Technical fields

- **Connection type:** Existing MCP.
- **Hosted MCP endpoint:** https://carclever-meta.getcarwise.app/mcp — only after live verification.
- **Documentation:** a current product guide that accurately reflects the submitted V2 capability.
- **Access requirements:** “Free public tool; no account, sign-in, API key or payment is required. Searches cover U.S. dealer inventory only. Listings, prices, availability and third-party links can change. The tool provides research shortlists, not purchase, financing, title, condition or history guarantees.”
- **Authentication:** confirm actual form behaviour; if a selection is required, use Other with the unauthenticated explanation above.

## Pre-submission gates

1. **André approval:** approve this Meta channel and proposed domain before infrastructure work.
2. **Contract freeze:** pin the exact shared release SHA. No unreviewed code/schema change may ride with the Meta setup.
3. **URL/domain verification:** HTTPS, direct MCP transport, intended SHA and widget resource origin all pass.
4. **Listing truthfulness review:** product page, guide, Terms and Privacy must not describe legacy Fractal-only tools as though they belong to the submitted Find My Car contract. Correct or scope the Meta listing and supporting pages before legal review.
5. **Brand/legal proof:** icon ownership, website, support, privacy and terms URLs are live and accurate.
6. **Live smoke evidence:** four example prompts plus a negative/unsupported request, with raw MCP and Muse-host evidence where available.
7. **Form review:** check the live Meta Connector Terms, any fees/revenue share, data-use requirements and the actual authentication choices before pressing Submit.

## Execution sequence

| Phase | Owner | Deliverable | Gate |
|---|---|---|---|
| 1. Submission preflight | ChatGPT | Final field pack, current website/legal consistency check, test prompt pack | André approval to create Meta channel |
| 2. Meta front door | Claude | Separate Vercel project, DNS, production env, pinned deployment | No code change; domain and SHA verified |
| 3. Independent technical acceptance | Claude, reviewed by ChatGPT | Raw MCP trace and host-facing smoke results | Resource origin and text fallback pass |
| 4. Submit | André with ChatGPT guidance | Completed Meta form and acknowledgement capture | Live terms/form checked |
| 5. Review handling | ChatGPT | Log status, respond to Meta evidence requests | No reactive code change without a reproducible requirement |
| 6. Post-approval | André/Claude/ChatGPT | Directory discovery test and light monitoring | Separate decision before any future platform-specific release |

## Decision requested

Approve or reject the proposed Meta submission track and the carclever-meta.getcarwise.app domain. Approval authorises Phase 1 preparation and asks Claude for the configuration-only feasibility/preflight; it does **not** authorise a production change or Meta submission until the later gates pass.

## Sources

- Meta’s Muse Connector Platform: https://muse.ai/platform — read 2026-09-21.
- Meta launch background: https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/ — read 2026-09-21.
- Form-field evidence from a September 19 existing-MCP submitter: https://stacktr.ee/blog/muse-connector-platform — corroborative, not official policy.
- Current platform/domain architecture: DECISION_CARCLEVER_PLATFORM_DOMAIN_NAMING_20260911.md and STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md.
