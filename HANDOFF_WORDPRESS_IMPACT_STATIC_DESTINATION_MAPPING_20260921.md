# Handoff — Task #63A WordPress Impact Static Destination Mapping

**Date:** 2026-09-21  
**Task:** #63 Phase A  
**Owner:** Claude — authenticated Impact/WordPress evidence lane  
**Authority:** Read-only website/account audit plus controlled destination verification. No WordPress or application changes.

## Objective

Produce an authoritative, usable mapping for the three static Edmunds/Impact destinations required by GetCarWise commercial pages:

1. **New** — current new-vehicle shopping/inventory/lead path;
2. **Used** — current used-vehicle shopping/inventory/lead path;
3. **Trade-in** — current appraisal/trade-in path.

This phase unblocks the redesigned $40k midsize-sedan page and prepares the later sitewide WordPress CJ→Impact migration. It is not the migration itself.

## Mandatory reading

Perform the repository start-of-session procedure, then read in full:

- `REVIEW_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_CONSOLIDATION_DECISION_GATE_20260921.md`
- `RETURN_WORDPRESS_MIDSIZE_SEDAN_40K_NEW_CAR_CONSOLIDATION_20260920.md`
- `STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md`
- `REVIEW_WORDPRESS_IMPACT_LINK_ARCHITECTURE_20260919.md`
- `HANDOFF_EDMUNDS_CJ_TO_IMPACT_MIGRATION_20260916.md`
- `STRATEGY_TOOL_LED_SEO_GEO_MONETIZATION_SYSTEM_20260920.md`
- current `STATE.md`, `TASKS.md`, `DECISIONS.md`, `PLAYBOOK.md` and `REFERENCE.md`

Use the latest repository interpretation: no new rights enquiry is required for the narrow future Catalog-read pattern. Catalog is outside this task.

## Boundaries

Do not:

- edit or publish any WordPress page;
- replace a CJ link;
- create a redirect;
- install or enable Publisher Tag;
- query or test the Product Catalog;
- change an app, MCP connector, repository code, Vercel project or domain;
- submit any New, Used or Trade-in lead form;
- alter an Impact tracking URL manually;
- assume the app’s existing wrapper/base link is automatically the correct WordPress fallback;
- expose credentials, authorization headers, AccountSID or private account data.

A maximum of one controlled destination open per candidate link type is permitted. Do not complete a form.

## Phase A1 — inventory current WordPress commercial links

Using read-only WordPress/API/admin inspection, build a complete inventory of commercial Edmunds/CJ links currently present on published GetCarWise pages.

For each unique link record:

- exact page URL and page ID;
- visible CTA label;
- placement/role;
- CJ hostname and link/ad ID where visible;
- apparent intended action: New, Used, Trade-in or unclear;
- `rel`, `target` and disclosure state;
- whether CarClever is also present;
- duplicate-use count.

Specifically confirm the current state of:

- the $40k midsize-sedan page;
- the $30k midsize-sedan comparison page;
- the $30k SUV page;
- the used-PHEV page;
- the 3-row SUV page;
- the retained $25k SUV page;
- the existing sitewide Trade-in CTA.

Do not edit anything.

## Phase A2 — inspect Impact program and available assets

In André’s existing authenticated Impact session, identify the active Edmunds program/campaign and inspect the currently available:

- text links/assets;
- New Car Inventory destination;
- Used Car Inventory destination;
- Trade-in Tool / Sell My Car destination;
- link-creation/deep-link interface, if visible.

For each candidate, record:

- exact asset/link name;
- intended action class;
- advertiser/campaign confirmation;
- whether it is an existing Impact-managed asset or a user-created deep link;
- destination shown by Impact before clicking;
- applicable action/commission category where the account UI shows it;
- whether it is suitable as a broad WordPress fallback CTA.

Do not create a new link in this phase. If no suitable existing candidate is available for one of the three classes, record that class as **missing — controlled link creation required** and stop short of creating it.

## Phase A3 — controlled destination validation

For at most one candidate in each class—New, Used and Trade-in—perform a controlled open without submitting a form.

Verify and record:

- starting Impact tracking hostname;
- redirect count and final domain;
- final Edmunds page purpose;
- whether the landing page matches the intended class;
- whether obvious tracking parameters remain intact;
- whether the click appears in Impact reporting, if visible without waiting or repeated clicks;
- whether consent/interstitial behavior affects the path;
- any cross-device, login or location assumption.

A landing page that merely mentions the right class but does not provide a credible path toward the corresponding commissionable Edmunds action is not sufficient.

Do not test attribution by submitting personal information or a lead.

## Phase A4 — canonical destination map

Return one row for each class:

| Class | Recommended CTA role | Exact visible label | Approved Impact URL | Final Edmunds destination | Existing asset or creation required | Verification result | Suitable now? |
|---|---|---|---|---|---|---|---|
| New | Primary for new-car pages | | | | | | |
| Used | Secondary/fallback | | | | | | |
| Trade-in | Contextual bridge | | | | | | |

Rules:

- Use the exact Impact-managed URL unchanged.
- Do not synthesize a link by editing publisher, campaign, asset or `u=` parameters.
- Do not place credentials or private identifiers in the repository.
- Affiliate URLs intended for public page use may be recorded; clearly distinguish them from credentials.
- If the account UI does not establish the intended action class, mark it unresolved rather than infer it.

## Phase A5 — migration recommendation

Without making changes, propose:

1. which current CJ link patterns map safely to each approved Impact destination;
2. which links require page-specific treatment rather than bulk replacement;
3. whether the $40k page is now unblocked for a primary New CTA;
4. whether the $30k comparison page should eventually use New, Used or dual continuation;
5. a later controlled Task #63B migration order;
6. how to keep affiliate-change timestamps separate from SEO/GEO treatment timestamps;
7. rollback requirements for the future migration.

Do not authorize or execute #63B.

## Stop conditions

Stop and return the evidence if:

- Impact authentication is unavailable;
- the Edmunds program/campaign cannot be positively identified;
- New/Used/Trade-in purpose is ambiguous;
- a candidate redirects to the wrong class or unrelated destination;
- a required class has no existing managed asset and would require link creation;
- validation would require lead submission;
- any step would require WordPress, Publisher Tag, Catalog, app or code changes.

A blocked or partially complete return is acceptable and preferable to guessing.

## Required return

Create:

`RETURN_WORDPRESS_IMPACT_STATIC_DESTINATION_MAPPING_20260921.md`

Include:

- timestamps and authenticated surfaces used;
- complete current WordPress CJ inventory;
- Impact asset inventory relevant to New/Used/Trade-in;
- controlled redirect/landing evidence;
- the canonical three-row destination map;
- unresolved/missing link classes;
- whether the $40k page is unblocked;
- proposed Task #63B migration order;
- exact confirmation that no WordPress, affiliate-link deployment, Publisher Tag, Catalog, app, Vercel or lead-submission change occurred.

Push the return, re-fetch it, verify it, and update only Claude’s checkpoint row.
