# CarClever Anthropic V2 Submission Update — 2026-09-12

## Status

**Submitted update: IN REVIEW.** Anthropic directory screen confirmed `CarClever - Find My Car`, slug `carclever-find-my-car`, status `In review`, and `Updated: just now` immediately after saving the V2 update on 2026-09-12.

## What changed

This was a controlled update of the existing Anthropic submission, not a new server/slug.

- Existing MCP URL retained: `https://carclever-find-my-car.vercel.app/mcp`.
- Existing Vercel project retained: `carclever-find-my-car`.
- Production was deliberately promoted from V1 to the exact tested V2 release without merging V2 into `main`.
- Promoted source: `release/v2`.
- Exact promoted SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`.
- Vercel production deployment verified READY; deployment metadata records target `production`, branch `release/v2`, exact SHA above, and action `promote`.
- Main/V1 remains preserved at `e7c8634fdd631c7bb05c83c02daeb1ab7f7bbb6`.

## Vercel evidence

Verified production deployment:

- Project: `carclever-find-my-car`
- Deployment ID: `dpl_9vP17yqXx5fdfV2uTWfAenvfYFD2`
- State: READY
- Target: production
- Git branch: `release/v2`
- Git SHA: `b8b07d8542f5d3f2a12e00433e089dde28ae5792`
- Commit: `Make widget origin configurable via NEXT_PUBLIC_WIDGET_ORIGIN env var`
- Original promoted preview: `dpl_GxdqgK2Av4GWnbF8d7Mc8TxCw2hh`

No OpenAI-specific `NEXT_PUBLIC_WIDGET_ORIGIN` value was copied into the Anthropic project. V2 production therefore uses its project-specific Vercel production-domain fallback as designed.

## Endpoint reachability

A direct normal-browser GET to:

`https://carclever-find-my-car.vercel.app/mcp`

returned JSON-RPC error `-32000` / `Method not allowed`, which is expected for an ordinary browser GET to the MCP route. This confirmed DNS, TLS and route reachability after the V2 promotion.

## Anthropic listing update

The existing Anthropic entry was edited while already in review.

Actions completed:

1. Opened **Edit server**.
2. Used server **Sync/Rescan tools**; portal reported the server's current list as 2 tools.
3. Updated the public Description to the final V2 marketing description used for the OpenAI resubmission.
4. Kept established name, slug, category, links, branding, access/data-handling answers and policy acknowledgements unchanged unless already set.
5. Preserved the prior decision not to proactively rewrite current V2 tool descriptions solely for Anthropic; change them only if Anthropic gives concrete feedback or a reproducible defect demonstrates a need.
6. Saved/submitted the edit.
7. Returned to **Your MCP servers** and verified status `In review`, Updated `just now`.

## Final public description

Find My Car searches live U.S. new and used vehicle inventory to help shoppers find the right car for their needs and budget.
Search by specific or combined requirements, lifestyle needs, and priorities such as cheapest, newest, lowest mileage, or lower-risk options, including detailed criteria such as trim, color, drivetrain, transmission, cylinders, condition, and electrification.
Requests like “AWD SUV under $35k” and “reliable car for a teen driver” both work, with broader needs translated into relevant real vehicle models before searching current inventory.
Already found a car? Look up the exact VIN and run a Buyer Check for red flags, good signs, and what to verify before buying.
Core vehicle identity is VIN-cross-checked, and every returned match is checked against each hard filter applied.
Unreported accident, ownership, or CPO data is shown as unconfirmed—not assumed clean.
Each result includes links to check availability and see similar vehicles.

## Tool set expected after refresh

- `find_matching_vehicle`
- `resolve_dealer_url`

V2 `find_matching_vehicle` is expected to expose `vehicleNeeds`, `electrificationTypes` and `electrificationRequirement`, and not expose legacy `goals`.

## Claude cache issue observed during cutover

Before saving the Anthropic rescan/update, a newly recreated Claude connector still showed stale V1 metadata for the base `CarClever - Find My Car` connector, including legacy `goals`, while a separate `CarClever V2 Test` entry exposed the correct V2 schema. Claude also displayed `Unable to reach CarClever - Find My Car` even though tool discovery could see the connector and the MCP endpoint was independently reachable.

This is currently classified as **host connector/tool-metadata cache mismatch pending retest**, not server unavailability and not the historical Claude widget-rendering defect.

The historical Claude cross-host rendering fix remains in V2: `_meta.ui.domain` is intentionally omitted. No code change was made in response to the cache symptom.

## Pending post-submission retest

After clearing/recreating Claude-side connector/cache state:

1. Confirm the base connector now advertises V2 schema (`vehicleNeeds`, electrification fields; no `goals`).
2. Run: `Find a used Honda CR-V under $25,000 with less than 60,000 miles near 90210.`
3. Run: `Check VIN 4T1DAACK6SU582551 for red flags before I buy it.`
4. Record any remaining host-specific deviation before changing code.

The test VIN is live inventory and its reported status may change; a status change alone is not a regression.

## Review freeze

While Anthropic and OpenAI are both in review, do not change V2 code/contract unless:

- a platform requests a correction; or
- a concrete reproducible defect is demonstrated and André authorizes the correction path.

## Remaining infrastructure check

Confirm the Anthropic Vercel project's long-term production branch/release behavior so a future push to V1 `main` cannot silently replace the manually promoted V2 production deployment.

## Related records

- `CURRENT_V2_STATE_20260909.md`
- `TEST_CARCLEVER_RELEASE_VALIDATION_LEDGER_20260910.md`
- `SUBMISSION_CARCLEVER_OPENAI_V2_RESUBMISSION_20260912.md`
- `AUDIT_CARCLEVER_DUAL_PLATFORM_VERCEL_FEASIBILITY_20260911.md`
- `AUDIT_V2_ANTHROPIC_SUBMISSION_COMPLIANCE_20260910.md`
- `STATUS_CARCLEVER_3_APP_PORTFOLIO_20260912.md`
