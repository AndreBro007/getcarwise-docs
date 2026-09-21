# Handoff — Fractal: Current API, Field and Logic Inventory

**Use:** Tomorrow's one Fractal code-agent request  
**Purpose:** establish exactly which APIs old CarClever currently calls, which request/response fields it uses, and what logic is applied to each field.  
**Mode:** read-only. Do not change code, deployment, subscription, credentials, prompts, UI, or app settings.

## Send this prompt to the Fractal code agent

> Perform a **read-only, code-evidence inventory** of the current old CarClever Fractal project.
>
> Do **not** produce another Free/Growth assessment, subscription discussion, call-budget calculation, capability-guard review, list of suggested APIs, or implementation recommendation. Do not repeat the prior impact report.
>
> We need one factual, auditable answer:
>
> **For every API the deployed project can call, which request fields does it send; which response fields does it actually read; and what filter, fallback, transformation, calculation or output logic uses each field?**
>
> A field is “used” only when current executable code reads it, passes it into logic, returns it in a tool result, or displays it. A property mentioned only in a type, comment, schema, old test, dead file or provider documentation is **not used**—list it separately as such.
>
> ### Required method
>
> 1. Search the whole current project for outbound HTTP clients/calls (including 'fetch', API wrappers, URL construction, startup work, server routes, background work and fallback paths), and for environment/configured base URLs.
> 2. For every live/reachable call, trace its response object through every property read until its final tool response/UI use.
> 3. Do not infer a field from an endpoint name, a type definition or API documentation. Give the exact raw response property path used in code.
> 4. Treat current deployed/reachable code separately from dead, test-only or superseded code.
>
> ### Return format — use these tables exactly
>
> #### A. User-facing tool/action map
>
> Enumerate the actual current user-facing tools/actions from code.
>
> | Tool/action | Entry file/function | APIs it can invoke | Notes |
> |---|---|---|---|
>
> #### B. Complete API call registry
>
> Include **every** external API/service provider—not only Auto.dev—including NHTSA, Zippopotam, Edmunds/affiliate or other HTTP services if callable.
>
> | Provider | Host | Method | Exact endpoint/path template | Code file + function | Triggering tool/action | Execution status |
> |---|---|---|---|---|---|---|
>
> 'Execution status' must be exactly one of: **live execution path**, **fallback path**, **startup/background path**, **test/development only**, or **dead/not called**.
>
> #### C. Request-field ledger
>
> For every row in table B that is live, fallback or startup/background:
>
> | Provider endpoint | Request parameter/body/header field (redact values/secrets) | Built from which user input/local value | Code file + expression | Purpose/logic |
> |---|---|---|---|---|
>
> This must include listing filters, VINs, ZIP/distance, credit/loan inputs and any model/year/make values sent to an external API.
>
> #### D. Response-field and logic ledger
>
> This is the essential table. Include **every response property actually read by current executable code**, including fields read only to calculate another result.
>
> | Provider endpoint | Exact raw response field path | File + function/property read | Logic applied (filter, validation, fallback condition, transformation, calculation) | Final use: tool output/UI field or internal-only | Execution status |
> |---|---|---|---|---|---|
>
> Use the actual raw source paths—for example 'vehicle.engine', 'retailListing.price' and 'history.ownerCount'—not generic phrases such as “listing data.”
>
> Include every field in use, particularly:
>
> - identity/location: VIN, year, make, model, trim, dealer, city/state/ZIP, price, miles, photos/images;
> - listing/powertrain: engine, drivetrain, transmission, fuel, body style/type, colours, doors, cylinders, seats;
> - history: accident fields, owner fields, usage, title, CPO, Carfax/VDP;
> - specifications: horsepower, torque, displacement, MPG city/highway/combined, EV range, fuel tank, dimensions, weight, safety equipment, warranty;
> - recalls, APR, taxes, fees, loan/OTD/payment and every TCO component.
>
> For every field with logic, name the condition/formula/threshold. For example: “if missing, use X”; “adds/subtracts Y to risk score”; “used in OTD calculation”; “displayed unchanged”; “only used to choose a fallback.” Do not merely say “used for analysis.”
>
> If a response object is passed wholesale to another function, continue tracing inside that function until the individual fields and final output are identified.
>
> #### E. Listings-audit comparison
>
> Read this authoritative reference for Auto.dev '/listings' fields only:
>
> https://github.com/AndreBro007/carclever-widget/blob/main/specs/Auto_Dev_Field_Audit_v1.md
>
> It describes the provider's Listings field surface and Find My Car’s use; it does **not** prove old Fractal use or cover Auto.dev’s other endpoints.
>
> For every '/listings' response field found in table D, compare it:
>
> | Old CarClever raw field path | Old CarClever logic/final use | Status in Listings field audit | Match / mismatch / not documented | Evidence |
> |---|---|---|---|---|
>
> Explicitly resolve these previously claimed fields:
>
> - 'listing.vehicle.mpgCity', 'listing.vehicle.mpgHighway' and combined MPG;
> - any Listings horsepower fallback;
> - 'vehicle.seats', 'vehicle.interiorColor', 'vehicle.cylinders';
> - 'history.accidents', 'history.accidentCount', 'history.ownerCount', 'history.oneOwner';
> - 'retailListing.price', 'retailListing.miles', 'retailListing.dealer', 'retailListing.vdp', 'retailListing.carfaxUrl', 'retailListing.titleStatus', 'retailListing.primaryImage'.
>
> If a claimed field does not occur in code, write **not used**. If it occurs only in a TypeScript type/schema/comment/test, write **declared only—not runtime use**. If it occurs in code but is never returned/displayed, write **internal-only** and name the logic.
>
> #### F. Field claims that do not survive the code audit
>
> List only:
>
> 1. previously claimed fields that are not read in current reachable code;
> 2. fields that are type/schema-only;
> 3. code paths whose exact provider field cannot be resolved; and
> 4. any API call that is unreachable/dead.
>
> ### Evidence rules
>
> - Cite the precise file, function and property path for every row.
> - Prefer static code evidence. Do not make live API calls unless a field path is impossible to resolve from code; if essential, use at most one read-only call and redact all sensitive values.
> - Do not change anything and do not open a pull request.
> - Do not include pricing, plans, downgrade advice, alternatives or recommendations.
>
> End after tables A–F. No executive summary or conclusion.

## Decision use

This inventory is factual groundwork only. It lets us compare old CarClever’s true provider usage against the established Listings audit before any later platform or subscription decision.
