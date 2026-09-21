# Handoff — Fractal: Auto.dev Field and Free-Tier Audit

**Use:** Tomorrow's one Fractal code-agent request  
**Purpose:** establish an evidence-based old-CarClever fallback decision before any downgrade, cancellation, or implementation.  
**Mode:** read-only audit. Do not change code, deployment, subscription, credentials, prompts, UI, or app settings.

## Send this prompt to the Fractal code agent

> Perform a **read-only, code-evidence audit** of this old CarClever Fractal project for a possible Auto.dev Growth → Free downgrade. Do not implement or change anything.
>
> The previous report says the app uses Auto.dev Listings and Photos (Free), and Specs, Recalls, APR, Payments and TCO (Growth), with graceful fallbacks. We need to verify that claim from the **actual current code and actual response shape**, not documentation or assumptions.
>
> ### Deliver one complete report in chat
>
> Start with a one-page decision summary:
>
> - **Works on Auto.dev Free unchanged**
> - **Works but becomes an estimate/fallback**
> - **Absent/broken unless changed**
> - **Unknown — state exactly what evidence is missing**
>
> Then provide the following evidence.
>
> #### 1. Exact endpoint and external-service inventory
>
> List every outbound data endpoint/host currently callable by the project. For each: method, exact path/template, code file + function/call-site, Auto.dev plan class (Free/Growth/not Auto.dev), which user tool/action can invoke it, caching, retry/parallel behaviour, and whether it is production-reachable or dead/unused code.
>
> Include all Auto.dev calls and all NHTSA, Zippopotam, and other external calls. Do not omit a call just because it is a fallback.
>
> #### 2. Field-by-field provenance matrix
>
> Cover every response/display field in these user-facing actions/tools:
>
> - search-used-cars
> - get-vehicle-details
> - analyze-deal-risk
> - calculate-affordability
> - vehicle comparison, garage, dealer-resolution, and any other user-facing tool present
>
> For each field, show:
>
> | User-facing field / label | Exact code output path | Primary source endpoint + response path | Plan | Fallback source + condition | Result on Free | Code evidence |
>
> Specifically trace, even if absent:
>
> - price, mileage, year/make/model/trim, photos, dealer, vehicle history, accidents, owners/title;
> - engine, horsepower, torque, displacement, cylinders, drivetrain, transmission, fuel/body style, colour, interior colour, seating;
> - **MPG city, highway and combined**, fuel tank capacity, **EV range**, dimensions, curb weight and payload;
> - safety equipment/features and crash ratings;
> - warranty;
> - recalls, explicitly distinguishing VIN-specific from model-level;
> - APR, taxes, fees, loan amount, out-the-door price, monthly payment;
> - TCO insurance, fuel, maintenance and depreciation.
>
> For MPG and EV range in particular: prove each claimed listing fallback with (a) its exact code property path and (b) a redacted fixture, recorded response, type/schema, or one controlled sample response. If no evidence exists, mark it **not proven/absent**. Do not infer availability from Auto.dev documentation.
>
> Clearly distinguish a field that is merely read internally, declared in a type, or in dead code from one that actually reaches a tool response/UI.
>
> #### 3. Capability guard and 402 behaviour
>
> Audit every Growth endpoint individually:
>
> - startup probe contents, timing, cache/TTL and cold-start behaviour;
> - every caller and guard condition;
> - what happens after 402 FEATURE_NOT_AVAILABLE;
> - whether Specs is included in the probe/guard;
> - whether unsuccessful 402 responses are cached, retried, or repeated for each vehicle request;
> - user-visible wording and whether it correctly says estimate/model-level/VIN-specific.
>
> Call out any path that would create repeat 402s or a misleading user claim on Free.
>
> #### 4. Call-budget calculation
>
> From code, calculate the minimum and realistic worst-case API calls for:
>
> - one cold start;
> - one search;
> - one vehicle-details view;
> - one deal-risk analysis;
> - one affordability calculation; and
> - the website CarClever Lite journey, if this project serves it.
>
> Separate calls by endpoint/plan and include retries, fan-out, probes and cache misses. State how much of a shared 1,000-calls/month Free cap each action consumes. If usage logs are available, report exact 7-day and 30-day counts by app/key/status; otherwise say logs are unavailable rather than estimating from memory.
>
> #### Evidence rules
>
> - Prefer static code inspection, existing fixtures, typed schemas and existing logs.
> - If a vital field cannot be resolved that way, make **at most one** low-volume, read-only verification request per unverified endpoint, with no new credentials or billing changes; redact VINs, keys, user data and dealer identifiers. Do not run bulk tests.
> - Quote code locations/function names and concise relevant excerpts, not just conclusions.
> - No code/config/subscription/API key/UI/deploy changes, and no pull request.
>
> End with:
>
> 1. a prioritized list of the smallest required changes for a truthful Free-tier standby (separate “required” from “optional”);
> 2. a clear recommendation: **safe to downgrade now / safe only after named fixes / not safe**, with reasons; and
> 3. any dependency that would make Fractal cancellation break CarClever Lite or another live website journey.

## Decision use

This audit is not approval to downgrade Auto.dev, change Fractal, or alter the website. It is the evidence gate for André's end-of-month decision.
