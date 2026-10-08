# Claude handoff: Edmunds-backed data continuity spike

Date: 8 October 2026 (Australia/Brisbane)
Status: proposed urgent engineering scope, prepared from fresh repository/code reads. No application code, live endpoint, deployment or account setting changed.
Owner report: Auto.dev allowance may last only another one or two days. Remaining calls, exact account plan and reset date are not independently checked.


> **VIN correction — 8 October 2026:** The September 16 migration investigation explicitly recorded VIN values in the returned `Mpn` field. It separately established that `Mpn`/VIN cannot be searched or filtered through the Catalog Items API (Impact ticket #882346). The September 21 probe checked VIN-like field names and selected text fields, without documenting a check of `Mpn`; it does not establish that returned records lack VINs. Inspect `Mpn` explicitly in a bounded current read and validate completeness/format before wiring enrichment. Historical returned-field evidence is established; current feed-wide completeness is not. [Source](https://github.com/AndreBro007/getcarwise-docs/blob/main/STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md).

## Recommendation

Prioritize keeping new CarClever usable before building the adaptive buyer pilot. Start from the current deployed release/v2 code, with an isolated branch and private preview. Reuse the existing private Impact catalogue adapter. Keep the existing screen implementation and externally approved tool contract as the target.

This is a bounded substitution/compatibility spike, not a guaranteed equivalent inventory replacement. Establish which actual requests can be fulfilled honestly and which require an explicit limited/unavailable response. Do not downgrade requested hard requirements silently.

The previous September catalogue brief excluded MCP integration; this October proposal intentionally explores that new option. It is not a record that any previous deployment permission covered a production cutover.

## Why this also supports the marketing strategy

The catalogue supplies potential cars, prices, dealer City/State, photos and tracked Edmunds item links. The adaptive experience would later use these candidates to compare compromises and establish useful questions before dealer contact.

The AI conversation and the listing source are separate concerns. A shared, normalized data layer can support the existing MCP app first and the future website/community entry point later. Source differences remain visible to the conversation; richer dialogue does not restore missing evidence.

## Fresh evidence checked

- STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md: returned `Mpn` VIN documented; `Mpn` query rejected, support confirmed limitation. This source was added during the October 8 correction after André identified the missed field.
- carclever-find-my-car release/v2: lib/auto-dev-client.ts, lib/find-matching-vehicle-output.ts, lib/results-card.ts and app/[transport]/route.ts.
- carclever-widget feature/catalog-locality-audit: lib/impact-catalog.ts and lib/impact-catalog-shared.ts.
- Docs: RETURN_IMPACT_CATALOG_C1_C8_READ_ONLY_TESTS_20260920.md; RETURN_IMPACT_CATALOG_PRIVATE_PROTOTYPE_20260921.md; RETURN_CATALOG_LOCALITY_PHASE1_DESK_AUDIT_20260930.md; IMPLEMENTATION_BRIEF_CATALOG_LED_LOCAL_BUYER_JOURNEY_20260930.md; PLAN_V3_REBUILD_FROM_V2_AND_MCP_SHARED_ID_20261008.md.
- STATE.md and TASKS.md fetched fresh. Oct 3 owner-reported tests passed on the then-recorded Starter access. This does not establish access after the monthly allowance is exhausted.
- Existing catalogue prototype: reported 62/62 tests and owner-verified six-card CR-V result. Preview-only, unmerged. Locality probe prepared, with no recorded live execution in the locality return.
- New V3 sync plan was approved separately on Oct 8 and not started in that document. Keep this data-continuity work separate from the V3 feature port.

## Source roles

| Source | Intended role | Boundary |
|---|---|---|
| Edmunds Impact catalogue | Candidate listing data and returned tracked item links | Not established as a full local inventory replacement; sampled condition empty. VIN was historically returned in Mpn, although Mpn/VIN is not a searchable catalogue field. |
| NHTSA vPIC | VIN decoding when a genuine VIN is supplied/available | Not a dealer inventory, sale-condition, price, history or photo source. |
| NHTSA recall endpoints | Recall context at the supported lookup granularity | Model/year campaigns are not proof that a particular vehicle has an outstanding unrepaired recall. |
| Auto.dev | Existing primary until switch, potentially selected enrichment only if allowance remains and the owner chooses it | A supposed no-Auto.dev mode must make zero Auto.dev requests, including photos/details/retries. |

NHTSA is enrichment/fallback for particular data functions, not a fallback search inventory when catalogue requests fail.

## Immediate engineering sequence

### 1. Establish the real baseline without spending listing calls

Read current deployed commits, domain mappings and environment scopes. Confirm the OpenAI build differs, if at all, from release/v2. Create a new feature branch from the verified current baseline; do not start from retired main or the stale V3 branch.

Check the owner's Auto.dev dashboard for remaining allowance and reset date using the existing account session, if accessible. Do not activate a paid plan or assume public pricing matches a legacy account.

Reuse existing catalogue test fixtures. Use no Auto.dev calls for baseline searches. Reserve any remaining calls for essential final comparisons with an explicit bounded request budget.

### 2. Close only the fields necessary for substitution

Inspect the raw catalogue schema safely, using the existing bounded probe/credentialed environment and a handful of catalogue reads. Record field names and aggregate presence, not credentials or upstream payloads.

Look specifically for:
- stable item identity and usable destination;
- genuine VIN from `Mpn`, explicitly documented in the September 16 migration investigation; validate its current presence, completeness and format, and distinguish this returned value from unsupported VIN search. Inspect the existing tracked destination only as a secondary consistency check;
- mileage, New/Used/CPO, equipment/powertrain and location;
- supported geography filters or exact-dealer lookup;
- feed update semantics;
- safe photos usable through the existing image proxy.

Do not bulk-download/index the million-item feed as the first step. Do not scrape destinations speculatively. Never substitute an item ID into a VIN field or infer used status from age or mileage.

If VIN, condition or local search remain unavailable, state the implications immediately and proceed only with requests the data can actually support.

### 3. Implement a normalized source adapter in preview

Keep the same two public tools, input/output schemas, annotations, MCP URL, authentication configuration, resource metadata/CSP and screen source wherever feasible.

Add internal provider selection and source capability checks. A proposed mode switch is auto_dev / edmunds_catalog. Its exact environment name is an implementation choice. Catalogue mode must bypass all Auto.dev calls and enrichment. Test this explicitly with a failing Auto.dev mock.

Do not blindly replace auto-dev-client.ts: the current pipeline refetches by VIN, verifies constraints, widens local searches and derives identity/links from VIN. Route catalogue candidates through the appropriate supported flow.

Use stable catalogue item identity internally for deduplication and follow-up. Output canonicalVehicleId may be a stable catalogue-based key; it must not be represented as a VIN. Determine whether absent VIN can be represented truthfully in the current approved schema and consumers without a schema change. An empty string passing z.string() is insufficient evidence that all downstream consumers are compatible.

Use existing null/unknown states for condition, history and unverified specifications. Maintain real constraint accounting. A required unverified criterion must not be marked satisfied. Do not invent green risk badges, confirmed equipment, local distances, comprehensive totals or current stock.

Retain the existing screen layout. Its renderer already supports missing mileage, images and VIN display. Catalogue condition unknown currently renders as UNKNOWN; test this existing state. If preserving screen source is impossible, return the smallest necessary change proposal rather than redesigning.

### 4. Verify the entire handoff and follow-up contract

Use returned catalogue tracking links as supplied, subject to the current agreement and link checks. Do not wrap an already tracked URL a second time. No link opening or lead submission is needed for fixture tests.

The current resolve_dealer_url input requires VIN. For returned candidates with a validated `Mpn` VIN, test that existing follow-up/tool path and preserve the supplied tracked catalogue link where appropriate. The catalogue still cannot be queried by arbitrary VIN: reuse the candidate already returned or a permitted bounded cache when applicable, and distinguish a direct user VIN request from candidate enrichment. Handle missing/invalid `Mpn` explicitly; never fake a VIN to satisfy the tool.

The catalogue token/prototype proves private access, not blanket permission for every new public channel/use. Check applicable data-display and tracking permissions from the current agreement/account materials before a public cutover. Do not contact Edmunds or Impact without an explicit instruction.

### 5. Run a small compatibility matrix

Use fixtures for most verification and bound any fresh catalogue calls.

| Case | Required result |
|---|---|
| Model + budget, within supported catalogue fields | Correct candidates and current screen render. |
| Broad body style + budget | Valid taxonomy/filtering; no unsupported model or completeness claim. |
| Used-only/CPO, local ZIP/radius, mileage or required hybrid | Fulfill only with evidence; otherwise precise limitation and useful continuation. |
| User-provided VIN | Genuine NHTSA decode/recall behavior remains bounded; catalogue lookup failure is not proof sold or unavailable. |
| Follow-up about displayed candidate | Stable identity, no fabricated evidence, correct supported handoff. |
| Catalogue empty/error/rate limit | Distinguish failure from no matching inventory; existing error/fallback presentation. |
| Missing optional fields | No crash, misleading badge or invented score inputs. |
| Auto.dev exhausted/disabled | Search, photos, detail and all retry paths make zero Auto.dev requests in catalogue mode. |

Check strict output-schema validation, photo-proxy rules and per-tool metadata equivalence against the published definitions. Save baseline hashes and diff, including resource HTML and CSP.

## OpenAI update path: current official documentation

Read on Oct 8:
https://developers.openai.com/plugins/deploy/submission

Current documentation says:
- metadata/assets/bundled skills changes use a new package;
- hosted MCP tool changes are handled separately through scans;
- after publication, daily scans and requested rescans can make eligible updates available after checks without a new package;
- the server must remain compatible with approved schemas while an update is held;
- changing the MCP server URL requires support.

This supports investigating a same-endpoint backend substitution without a new package upload. It is not a guarantee that every behavior change passes checks. Check the actual application's current portal state and scan results at cutover. Screen preservation alone does not establish compatibility. OpenAI's rules do not establish Fractal or Anthropic update behavior.

## Auto.dev time constraint

Fresh public pricing:
https://www.auto.dev/pricing

On Oct 8 the public Free plan states 1,000 calls/month and requests stop at the limit. This differs from the Oct 2 project record describing Starter per-call overages. The owner's actual account may be on a different/legacy contract; dashboard verification remains necessary.

Do not propose a Growth renewal as an assumed solution within the owner's $200/month total ceiling. Do not conflate upstream API calls with AI model tokens or Fractal credits.

## Old CarClever / Fractal

Keep new CarClever first: its two-tool implementation is inspectable in GitHub and the catalogue adapter can be exercised in an isolated preview.

After the shared adapter is proven, assess Fractal separately:
- existing tools, schemas, screens and missing-field handling;
- inventory versus VIN/history/price/affordability feature dependencies;
- ability to call the same server-side catalogue adapter without exposing credentials;
- deployed-code update path while old package 3.0.1 is in review;
- remaining Fractal credits/access and October 14 hosting decision.

Static Growth-to-Free affordability/TCO estimates remain separate from listing-source substitution. No promise of full old-app equivalence before code/access/contract verification. Do not spend the short runway duplicating two unproven adapters.

## Decision at spike exit

Return a concise engineering verdict:
1. Which requests work with unchanged tools/screens.
2. Which requests are limited, why, and the exact user-facing outcome.
3. Whether the catalogue mode truly makes zero Auto.dev requests.
4. Whether links, follow-ups and published contract pass.
5. Cost/access dependencies and rollback.
6. Recommendation: compatible same-endpoint cutover, selective hybrid, or keep catalogue experience isolated until the stated gap is solved.

This brief does not authorize production promotion. Prepare a reviewable preview first. A future cutover keeps existing public endpoints and has a reversible switch, with current aliases/commits inspected before promotion and verified afterward.

Do not delay the answer with a broad marketing report or unrelated V3/SEO work.
