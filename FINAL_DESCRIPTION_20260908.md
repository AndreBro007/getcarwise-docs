# V2 Shared Public Tool Description — Final Verified Version

**Source of truth:** this is a direct extraction of the live, currently-deployed
text from `research/v2-schema-probe` branch, `app/research-probe/[transport]/route.ts`,
as of commit `516abc7` (imperative-voice fix) + `7bb5769` (docs-only follow-up,
no wording change). This is the **actual verified-working version** — tested
and confirmed correct on both Claude and ChatGPT, per `FINAL_FINDINGS_20260908.md`.

**If this document and the live code ever disagree, the live code is correct**
— re-extract from source rather than trusting this file blindly, since it can
drift if code changes without this doc being updated. Check `CHANGE_LOG.md`
(same branch) for the full wording history if you need to know what changed
and why.

---

## Main tool description

> Finds current vehicles for sale in the United States and returns a concise shortlist matching a user's stated requirements. Appropriate for listing requests with explicit criteria, optimization goals such as lowest price, newest, lowest mileage, or best within a stated budget, practical needs such as a large family SUV or commuter vehicle, or an exact current listing by VIN.
>
> Search inputs include make, model, price, year, mileage, location, body style, drivetrain, transmission, trim, seating, color, condition, electrification, and purchase priority. Most direct criteria are matched against actual listing data; seating, certification, and history-related requests reflect available evidence, which may be confirmed, unconfirmed, or unreported rather than guaranteed. Practical needs such as a large family SUV, a teen-driver car, or a vehicle for towing are interpreted before the search runs to identify relevant candidates; this tool then searches and ranks them using actual listing data — it does not independently establish reliability, safety, running cost, towing suitability, condition, accident-free history, or certification. When a practical need implies a vehicle class, resolve it into real matching model names yourself and include them in model before calling this tool (for example, a large family SUV might include CR-V, RAV4, or Highlander; a reliable commuter car might include Corolla, Civic, or Mazda3), every time, alongside the related need stated in vehicleNeeds.
>
> An exact 17-character VIN refers to one specific listing; if unavailable, that outcome is reported rather than substituting a similar vehicle. Electrification requests state accepted types — hybrid (including mild hybrid), plug-in hybrid, electric — and whether required or preferred. A vehicle's primary fuel label alone does not determine hybrid or plug-in-hybrid status. For an unambiguous city-only request, a representative ZIP may be supplied as the local search anchor; results disclose the overall local, state-wide, or nationwide scope.
>
> Results include current matching listings, viewing links where available, and available evidence about confirmed, unconfirmed, or changed criteria. Missing history, ownership, certification, or specification data remains unknown and is never treated as proof a vehicle satisfies or fails a request.
>
> This tool is for vehicle-listing searches — not general automotive education, maintenance, financing, leasing, unsupported categories, or comparisons not requiring current listings.

---

## Field-level descriptions

| Field | Type / bounds | Description (verbatim) |
|---|---|---|
| `vin` | string | Exact 17-character VIN for one current listing. Other criteria are evaluated against that listing; no similar-vehicle substitute is returned. |
| `priceMax` | number | Maximum price in USD. |
| `priceMin` | number | Minimum price in USD. |
| `priceFlexibility` | enum: strict, flexible | Whether an approximate price ceiling may be treated as flexible; omitted ceilings remain strict. |
| `priorityAxis` | enum: best_for_budget, cheapest, lowest_mileage, newest, lower_risk | Ranking objective: best_for_budget, cheapest, lowest_mileage, newest, or lower_risk. best_for_budget applies to "best for budget", "best in my budget", or a price ceiling with no other stated optimization. cheapest applies only to explicit lowest-price intent such as "cheapest" or "lowest price" — the word "budget" alone does not imply cheapest. Lower risk ranks available purchase-risk evidence and is not a guarantee. |
| `yearMin` | number | Earliest acceptable model year. |
| `yearMax` | number | Latest acceptable model year. |
| `make` | string, max 200 (research ceiling — see note below) | Vehicle manufacturer, such as Toyota, Honda, or Ford. |
| `model` | string, max 500 (research ceiling — see note below) | One or more real vehicle model names, without the manufacturer (for example, "E-Class" rather than "Mercedes-Benz E-Class"). This applies even in a cross-brand list: "CR-V, RAV4, Outback" is correct; "Honda CR-V, Toyota RAV4, Subaru Outback" is not. Comma-separated for multiple models. When a practical need implies a vehicle class (for example, a large family SUV, or a reliable commuter car), resolve it into real matching model names yourself, using your own knowledge, before calling this tool (for example, CR-V, RAV4, Highlander for a family SUV), every time, alongside the related need stated in vehicleNeeds. |
| `bodyType` | string, max 200 | Broad body style, such as SUV, Sedan, Truck, or Minivan. |
| `vehicleType` | string, max 200 | Finer vehicle classification when the user expressly distinguishes it, such as Crossover, Wagon, Hatchback, Coupe, or SUV. |
| `mileageMax` | number | Maximum odometer mileage. |
| `zip` | string | Five-digit US ZIP code for a local search. |
| `radiusMiles` | number | Search radius in miles from the ZIP; the service applies its documented default when omitted. |
| `state` | string | Two-letter US state code for a state-wide search when no local ZIP is available. |
| `trimRequired` | string, max 200 | Requested trim or variant. A confirmed different trim is not treated as a match. |
| `trimPreference` | string, max 200 | Preferred trim or variant. It influences ranking and does not require a matching trim. |
| `seatsMinPreference` | number | Preferred minimum seating capacity. Results report whether available seating evidence meets the preference. |
| `vehicleNeeds` | array of string, max 5 items, 60 chars each | Short, capped list of listing-relevant practical needs (for example, a large family SUV or a commuter vehicle); not a transcript or broad profile. When a listed need implies a vehicle class, also resolve it into real matching model names yourself and include them in `model` alongside it (for example, a large family SUV need pairs with a model list like CR-V, RAV4, Highlander). |
| `drivetrain` | string, max 200 | Requested drivetrain: AWD, 4WD, FWD, RWD, or a comma-separated acceptable set. |
| `transmission` | enum: Automatic, Manual | Requested transmission: Automatic or Manual. |
| `exteriorColor` | string, max 200 | Requested exterior colour. |
| `interiorColor` | string, max 200 | Requested interior colour. |
| `doors` | number | Requested door count. |
| `cylinders` | number | Requested engine cylinder count: V8 is 8, V6 is 6, and I4/four-cylinder is 4. Engine displacement is not represented by this field. |
| `used` | boolean | Vehicle condition: true for used only, false for new only; omitted includes both. |
| `cpo` | boolean | Request for certified pre-owned status. Results distinguish confirmed, reported-not-CPO, and unreported evidence. |
| `noAccidents` | boolean | Request for no reported accidents. Results distinguish reported-clean, reported issues, and unreported history. |
| `oneOwner` | boolean | Request for one-owner history. Results distinguish available ownership evidence from unreported history. |
| `electrificationTypes` | array of enum: hybrid, plug_in_hybrid, electric — max 3 | One or more accepted electrified powertrain types: hybrid (including conventional and mild hybrids), plug_in_hybrid, and/or electric. |
| `electrificationRequirement` | enum: required, preferred | Whether the stated electrification types are required or preferred. |

**Not in the schema:** `goals` — fully unsupported, no adapter, not accepted even for migration. This was a live decision made in the discovery-run chat (Sep 8, 2026), not written into any dated feasibility doc at the time — see `DISCOVERY_RUN_FINDINGS_20260908.md`/`FINAL_FINDINGS_20260908.md` for the reasoning trail. Docs referencing "accept goals during migration" predate this decision and are stale.

---

## Important caveats before using this as the real production contract

1. **`model` (500 char) and text-field (200 char) ceilings are research-only, not production values.** These were deliberately set generous so the probe wouldn't reject real host output before it could be measured. A real production cap needs to come from a larger evidence sample than this discovery run gathered — see `FINAL_FINDINGS_20260908.md`'s "what's left" section.
2. **Cross-field validation rules** (priceMin≤priceMax, yearMin≤yearMax, electrificationRequirement requires non-empty electrificationTypes, etc.) exist in the probe's handler logic, not enforced at the schema level shown here — see the full `route.ts` source for exact implementation if building real schema-level validation.
3. **This is a schema/description artifact only** — it contains no backend logic (NHTSA classifier, bounded verification pool, Auto.dev query construction). Those are separate, still-open implementation work per the electrification feasibility audit's proposal-and-review gate.
