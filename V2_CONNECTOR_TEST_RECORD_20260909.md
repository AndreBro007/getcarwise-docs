# V2 Connector Test Record — 2026-09-09

## Release under test

- Endpoint: `https://ccfmc-dev-v2.vercel.app/mcp`
- Branch: `release/v2`
- Merge: `5e8735e`
- Deployed tip: `a9d6439`
- Deployment: READY, production target

## Connector tests passed

The amended V2 release was exercised through both the ChatGPT and Claude V2 test applications:

- Practical family-SUV request with explicit real model-name resolution.
- Hybrid SUV required search.
- Plug-in-hybrid SUV required search.
- Preferred hybrid search, confirming non-matches remain eligible.
- Mixed hybrid/PHEV request with OR semantics.
- Exact model/variant searches.
- Budget, cheapest, newest, lowest-mileage, lower-risk, AWD, CPO, history, and family-needs requests.
- Exact VIN lookup and risk/buyer-check flows.
- Legacy `goals` wording, confirming the host used `vehicleNeeds` rather than the retired field.
- Five-result display behavior.

## Contract checks

- `vehicleNeeds` is the public replacement for `goals`.
- Public electrification inputs are `hybrid | plug_in_hybrid | electric`.
- Internal `mild_hybrid` is not caller-selectable.
- Required/preferred semantics are visible in the live schema and behavior.
- Practical and broad electrification requests resolve real model names into `model`.
- `resultsShown` remains code-derived from final `results.length`.

## Local verification

- Production build: passed.
- Custom checks: 222 passed.
- Node tests: 79 passed.
- Typecheck: one pre-existing unrelated error at `tests/best-for-budget-ranking.test.ts:105:39`, proven against the release baseline.
- Live NHTSA: BEV/PHEV confirmed; mild-hybrid candidates returned blank electrification levels; ambiguity case remains synthetic-only.

## Remaining work

This record does not authorize changing V1/Anthropic or V3. Final OpenAI submission still requires choosing and verifying a stable submission domain; the V2 Vercel URL is the tested release endpoint, not necessarily the final branded endpoint.
