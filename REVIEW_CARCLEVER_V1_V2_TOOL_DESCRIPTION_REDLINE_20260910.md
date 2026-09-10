# CarClever V1→V2 Tool Description Review and Minimal Redline — 2026-09-10

**Status:** REVISED PROPOSAL — no application code changed  
**Purpose:** Compare Anthropic's actual prior CarClever feedback with current V1/V2 MCP descriptions and define the smallest wording change that removes forceful assistant-directed imperatives without weakening host routing.  
**Owners:** ChatGPT = review/redline/test design; Claude = implementation only after André approves; André = final approval and manual host testing where required.

## 1. Exact context of Anthropic's prior objection

The archived 2026-08-01 Anthropic MCP Directory email was re-read directly. Anthropic had re-tested the previous CarClever server and said the server itself was in good shape. Their wording objection was specifically to descriptions that **instruct the assistant in a way that can force unwanted invocation/behavior**.

Their examples were:

- `always invoke this tool ...`
- `Never block or refuse ...`
- `MUST call ... first`

Anthropic's explanation was that descriptions should describe what a tool does and when it is useful; **imperatives aimed at the assistant — especially never-refuse language — can force unwanted invocations and are not allowed in directory listings**.

### Revised interpretation

This is more specific than a blanket rule that every word such as `use`, `when`, or ordinary enum-selection guidance is prohibited. The primary risk is **coercive/mandatory host behavior language**, especially `must`, `always`, `never refuse`, `before calling`, `every time`, and equivalent commands directed at the model.

That distinction matters because CarClever needs enough semantic guidance for the host to build the right structured search. We should remove coercive phrasing, not strip useful contract semantics.

## 2. Current V1 risk

Current V1 (`main`) is still high-risk against that exact prior-feedback pattern. Its main `find_matching_vehicle` description contains many assistant-directed commands, including `don't retry ... yourself`, `Before calling`, `Do not invent`, `resolve ... every time`, `Never rely`, `Use trimRequired`, `Never translate a VIN`, repeated `never`/`must`/`do not`, and answer-presentation instructions.

**Conclusion:** waiting for V1 review is not risk-free. V1 contains substantially more assistant-directed mandatory language than the older CarClever descriptions Anthropic already asked us to rewrite.

## 3. Current V2 risk — narrower than V1

V2 is dramatically better. Most of its description is capability/contract language and should remain untouched.

The remaining concern is concentrated in four places:

1. a small section of the main `find_matching_vehicle` description;
2. the `model` field description;
3. the `vehicleNeeds` field description;
4. the `electrificationTypes` field description.

The phrases of concern are specifically constructions such as `resolve ... yourself`, `before calling this tool`, `every time`, and `do not use ... alone`.

### `priorityAxis` revised verdict

**Leave unchanged in this pass.** `Use lower_risk for requests such as ...` is ordinary enum/intention mapping and does not force the tool to be invoked or tell the host to override/refuse user intent. Changing it provides little compliance benefit and adds avoidable regression surface.

## 4. Revised minimal redline — exact changed text

The goal is now **surgical neutralization**, not paragraph rewriting.

### 4.1 Main tool description — sensitive sentences only

**Current:**

> When a practical need implies a vehicle class, **resolve it into real matching model names yourself and include them in model before calling this tool** (...) **every time**, alongside the related need stated in vehicleNeeds. For a broad hybrid, plug-in hybrid, or electric request, **likewise resolve suitable real model or variant names and include them in model before calling the tool**. For required hybrid or plug-in hybrid searches, **use electrified variants only**; for preferred searches, acceptable base-model alternatives may also be included.

**Proposed:**

> When a practical need implies a vehicle class, **real matching model names are supplied in `model`** (...) **alongside the related need stated in `vehicleNeeds`**. Broad hybrid, plug-in hybrid, or electric searches **similarly use suitable real model or variant names in `model`**. For required hybrid or plug-in hybrid searches, **candidate model scope contains electrified variants only**; for preferred searches, acceptable base-model alternatives may also be included.

**Effect:** same examples and candidate-model/electrification contract; removes `yourself`, `before calling`, `every time`, and direct `use ... only` command.

### 4.2 `model`

**Current risky portion:**

> When a practical need implies a vehicle class (...) **resolve it into real matching model names yourself, using your own knowledge, before calling this tool** (...) **every time**, alongside the related need stated in vehicleNeeds. For broad hybrid, plug-in hybrid, or electric requests, **also resolve suitable real electrified model or variant names and include them here**.

**Proposed full field description:**

> One or more real vehicle model names, without the manufacturer (for example, `E-Class` rather than `Mercedes-Benz E-Class`). This applies even in a cross-brand list: `CR-V, RAV4, Outback` is correct; `Honda CR-V, Toyota RAV4, Subaru Outback` is not. Comma-separated for multiple models. **For a practical need that implies a vehicle class, this field carries the real matching model candidates** (for example, CR-V, RAV4, Highlander for a family SUV), **alongside the related need in `vehicleNeeds`**. Broad hybrid, plug-in hybrid, or electric searches **similarly use suitable real electrified model or variant names here**.

### 4.3 `vehicleNeeds`

**Current risky portion:**

> When a listed need implies a vehicle class, **also resolve it into real matching model names yourself and include them in `model` alongside it** (...).

**Proposed full field description:**

> Short, capped list of listing-relevant practical needs (for example, a large family SUV or a commuter vehicle); not a transcript or broad profile. When a listed need implies a vehicle class, **corresponding real matching model candidates are represented separately in `model`** (for example, CR-V, RAV4, Highlander for a large family SUV).

### 4.4 `electrificationTypes`

**Current risky portion:**

> For a broad request without a named model, **pair this field with resolved model/variant names in model; do not use electrification fields alone** for a generic body-style search.

**Proposed full field description:**

> One or more accepted electrified powertrain types: hybrid (including conventional and mild hybrids), plug_in_hybrid, and/or electric. For a broad request without a named model, **corresponding real model or variant candidates are represented in `model`; the electrification fields alone do not define a generic body-style candidate universe**.

## 5. Length impact

The revised proposal is **shorter overall**, not longer.

| Area | Current | Proposed | Change |
|---|---:|---:|---:|
| Main sensitive sentences | 673 chars / 103 words | 590 chars / 86 words | **-83 chars / -17 words** |
| `model` | 758 chars / 115 words | 613 chars / 90 words | **-145 chars / -25 words** |
| `vehicleNeeds` | 379 chars / 63 words | 335 chars / 51 words | **-44 chars / -12 words** |
| `electrificationTypes` | 309 chars / 44 words | 339 chars / 46 words | **+30 chars / +2 words** |
| **Total changed text** | **2,119 chars / 325 words** | **1,877 chars / 273 words** | **-242 chars / -52 words** |

Only `electrificationTypes` becomes slightly longer because the direct prohibition is converted into an explicit statement of what the field does *not* define. The total MCP description surface becomes smaller.

## 6. What does NOT change

This proposal does not change:

- tool behavior or search/ranking code;
- schema fields or enum values;
- candidate-model requirement for practical needs;
- required/preferred electrification semantics;
- VIN behavior;
- price flexibility;
- trim required/preferred behavior;
- ZIP/radius handling;
- history/CPO semantics;
- `resolve_dealer_url`;
- annotations/tool names;
- `priorityAxis` wording in this revised pass.

## 7. No-regression gate

Treat even these wording changes as behavioral until tested. Baseline the existing V2 description and exact SHA, implement only the approved text diff on a test/release branch, then run the high-risk prompt suite in both ChatGPT and Claude.

Compare host-generated arguments, not just final prose. Critical checks: practical-needs model resolution, hybrid/PHEV/EV candidate scope, required vs preferred behavior, model values without manufacturer prefixes, hard-filter preservation, priority-axis mapping, and no invented constraints.

Reject/revise the redline if either host materially worsens.

## 8. Anthropic V1→V2 implication

The precise old-review context strengthens two conclusions simultaneously:

1. V1 has credible risk because it contains large amounts of exactly the kind of forceful assistant-directed language Anthropic previously objected to.
2. We should **not over-correct V2**. The current V2 issue is limited and can be addressed with a small neutralization pass that is shorter overall and preserves the semantic cues needed for correct searches.

Pending Anthropic submission remains unchanged until André explicitly chooses the path after testing and any Anthropic support response.

## 9. Manual host test plan

Manual testing will be run in a fresh ChatGPT session because the current Claude session is token-constrained. Use a stable candidate endpoint and compare current V2 wording with candidate wording against at least: family SUV, teen driver, commuter, towing, broad hybrid, hybrid required, hybrid preferred, PHEV required, broad EV, cheapest, best-in-budget, lower-risk, required/preferred trim, exact VIN, and cross-brand multi-model requests.

The separate A/B/C endpoint test remains required before approving the permanent test hostname: long Vercel Preview alias with Vercel Authentication off vs short `ccfmc-dev` vs short owned-domain candidate, all on the same application SHA/configuration.

## 10. Decision status

- Exact production/test hostnames: **NOT APPROVED**.
- Revised V2 description redline: **PROPOSED for André review**.
- Application implementation: **NOT STARTED**.
- Anthropic pending submission: **UNCHANGED / IN REVIEW**.
- V3: **HARD PAUSED pending final V2 baseline/rebaseline work**.
