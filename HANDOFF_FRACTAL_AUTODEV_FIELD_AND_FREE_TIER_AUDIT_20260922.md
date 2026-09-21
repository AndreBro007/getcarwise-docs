# Handoff — Fractal: Current API and Field Inventory

**Use:** Tomorrow's one Fractal code-agent request  
**Purpose:** create a factual inventory of every API the current old CarClever project uses and every field it actually uses.  
**Mode:** read-only. Do not change code, deployment, subscription, credentials, prompts, UI, or app settings.

## Send this prompt to the Fractal code agent

> Perform a **read-only, code-evidence inventory** of the current old CarClever Fractal project.
>
> This is **not** a Free-tier, subscription, pricing, downgrade, call-budget, capability-guard, or implementation task. Do not assess plans or recommend changes. We first need one factual answer: **which APIs does the current project use, and which fields from each does it actually use?**
>
> ### Deliver one complete report in chat
>
> #### 1. Every API currently used
>
> Find every outbound API/service call that can be reached by the currently deployed project, including direct calls, helper/client wrappers, server routes, background/startup work, and fallback paths.
>
> For each API, provide:
>
> | Provider / host | Method | Exact endpoint/path template | Code file and function/call-site | Triggering user tool/action | Current status |
> |---|---|---|---|---|---|
>
> “Current status” must say **used in the live execution path**, **fallback path**, **startup/background path**, or **present but not called/dead code**.
>
> Include every provider, not just Auto.dev: NHTSA, Zippopotam, and any other external data/service API. Enumerate the actual user-facing tools/actions from the code rather than relying on a previous list.
>
> #### 2. Every field actually used
>
> For each API response, list every field that the current project reads, maps, calculates from, returns through a tool, or displays to the user.
>
> Use this matrix:
>
> | Provider / endpoint | Raw response field path | Code file + exact usage | Used for / user-facing label or output path | Direct, derived, fallback, or internal-only | Notes |
> |---|---|---|---|---|---|
>
> Cover all fields, not only headline vehicle fields. In particular, verify whether the current code uses:
>
> - price, mileage, year/make/model/trim, VIN, photos, dealer and location;
> - vehicle history, accident history, owner count and title status;
> - engine, horsepower, torque, displacement, cylinders, drivetrain, transmission, fuel, body style, colours and seating;
> - **MPG city/highway/combined**, fuel-tank capacity, **EV range**, dimensions, curb weight and payload;
> - safety features/ratings, warranty and recalls;
> - APR, taxes, fees, loan amount, out-the-door price, payment and all TCO components.
>
> For **MPG and EV range**, do not infer that a field exists from documentation or a TypeScript type. Show the actual response-path reference in current code and say whether it reaches a user output. If the code never reads it, state **not used**. If it is only declared in a type, state **declared but not used**.
>
> #### 3. Complete source-to-output tracing
>
> For each user-facing tool/action currently available, provide a compact source map:
>
> | Tool/action | Output field/section | Source API + response path, or local/static calculation | Code evidence |
> |---|---|---|---|
>
> Distinguish:
>
> - API fields actually used in a live result;
> - API fields read only for an internal calculation;
> - locally derived/static/default fields;
> - fallback-only fields; and
> - fields/types/endpoints present in the repository but not reached by current execution.
>
> #### Evidence rules
>
> - Base conclusions on the current code, not memory or provider documentation.
> - Quote concise code locations/excerpts or give exact function and property paths.
> - Use existing fixtures, logs or schemas where available. If a raw response shape is essential and unavailable, make at most one low-volume read-only verification request; redact keys, VINs and personal/dealer data.
> - Do not make any code, configuration, data, subscription, UI, deployment, key, prompt, or pull-request change.
>
> End with only:
>
> 1. the complete API list;
> 2. the complete field-use matrix;
> 3. the fields that were claimed previously but are **not actually used**; and
> 4. any uncertainty that cannot be resolved from the project.

## Decision use

This inventory is factual groundwork only. Any later assessment of plans, fallbacks, or Fractal retention will be a separate request after the inventory is reviewed.
