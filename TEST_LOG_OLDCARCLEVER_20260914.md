# Test Log — Old CarClever Hybrid/PHEV/Electric/Sort/AWD/Diesel Fixes — Sep 14, 2026

Scope: full-day live regression and fix-verification session for old CarClever's `search-used-cars` tool (Fractal-managed). All tests run via direct interaction with the live Claude connector against production (or Fractal's own preview environment where explicitly noted), not Fractal's self-reported unit tests alone.

## Confirmed FIXED and live-verified (production, direct user testing)

| # | Test query | Before | After |
|---|---|---|---|
| 1 | `hybrid SUV under $40k in 90210` (run twice, fresh chats) | Nondeterministic — sometimes gasoline (e.g. Ford Explorer XLT), sometimes hybrid | Identical hybrid-only results (CR-V Hybrid) both runs |
| 2 | `large hybrid SUV under $70k in 90210` | Gasoline vehicles, no hybrid filter applied | Lexus RX 350h, Toyota Highlander Hybrid — hybrid-only |
| 3 | `electric truck under $80k in 90210` | Only SUVs/crossovers (Ioniq 5, Mach-E) | Rivian R1T, Ford F-150 Lightning — trucks only |
| 4 | `compact electric truck under $60k in 90210` | Same as above | Same electric trucks appear; note — no genuine compact/midsize electric truck exists in current inventory, accepted as a data-availability gap, not a routing bug |
| 5 | `large SUV under $70k in 90210` | Acura MDX, Subaru Ascent (not genuinely large) | Toyota Sequoia — genuinely full-size |
| 6 | `large luxury SUV under $80k in 90210` | Lexus NX (compact), Acura MDX | Lincoln Navigator, Audi Q8 — genuinely full-size luxury |
| 7 | `small size suv under 40k in 90210` | Same as midsize (Mazda CX-5, Kia Sportage) | Hyundai Kona — genuine subcompact tier |
| 8 | `compact suv under 40k in 90210` (regression) | — | Unchanged — CX-5/Sportage-class, confirms new subcompact tier didn't disturb existing tier |
| 9 | `plug-in hybrid SUV under 50k in 90210` / `PHEV under 40k in 90210` | Zero PHEVs — only regular hybrids | RAV4 Prime, Wrangler 4xe, Grand Cherokee 4xe, Sorento PHEV correctly surfaced |
| 10 | `hybrid minivan in 90210` | Corolla Hybrid sedans, zero minivans | Toyota Sienna exclusively |
| 11 | `electric sedan under 40k in 90210` | Kia EV6 (misclassified as sedan; actually SUV per Auto.dev) | Tesla Model 3, Hyundai Ioniq 6 now present. Known open gap: Model Y (SUV) can still rank #1 by Deal Score — no strict sedan filter exists yet |
| 12 | `Honda CR-V under 50k in 90210` (no sort specified) | Old default (Best Deal/Deal Score) surfaced $11k-$14k 2014-2018 models on a $50k budget | Recommended now default — surfaces 2025-2026 models correctly using more of the stated budget |
| 13 | Sort dropdown: Best Deal / Price Low-High / Price High-Low / Mileage Low-High, same query | Dropdown appeared to do nothing — same results regardless of selection ("reverts to Best Deal") | All four sorts confirmed to produce genuinely different, correctly-ordered vehicle sets |
| 14 | `Ford F150 under 40k in Dallas` (no hyphen) | Exactly 1 result — 2023 F-150 Lightning at anomalous $499 | Healthy, varied pool — 2023-2025, $31k-$38k |
| 15 | `Ford F-150 under 40k in Dallas` (with hyphen) | Also confirmed broken at one point during the session (small pool) | Healthy, varied pool, consistent with #14 |
| 16 | `Chevrolet Silverado 1500 under 40k in Dallas` (control) | — | Always returned healthy pool — confirmed the F-150 issue was NOT a general truck/named-model bug |
| 17 | `RAV4 Prime under 45k in 90210` | Returned RAV4 Hybrid only, never genuine Prime (pre-existing bug, confirmed present before today's other fixes too) | Genuine RAV4 Prime PHEVs returned (2021-2024, tagged Plug-In Hybrid) |
| 18 | `RAV4 Hybrid under 40k in 90210` (regression) | — | Unchanged, correctly returns plain hybrid trims |
| 19 | `AWD SUV with low mileage under 35k in 90210` | 3 of 6 results were FWD despite explicit AWD request (raw JSON confirmed: FWD, AWD, AWD, FWD, AWD, FWD) | 6 of 6 confirmed AWD |
| 20 | `diesel truck under 50k in 90210` | 100% gasoline substituted silently (evidenced by a 2026 Toyota Tundra — no US diesel Tundra trim exists, ruling out mislabeling) | Genuine diesel filtering confirmed working |

## Confirmed as NOT a defect (working as designed, or genuine market/data limitation)

- **Deal Score's Budget Fit floor** (the root cause behind #12's old behavior) — confirmed mathematically self-consistent by Fractal's own worked example; the *product decision* was to add Recommended as a better default, not to alter Deal Score's own formula (kept fully intact and selectable).
- **Compact electric truck** (#4) — no genuine compact/midsize electric truck exists in current market/model data; accepted, not pursued further.
- **Rivian R1T topping Best Deal-sorted results** in several truck searches — checked, appears to be legitimate high Deal Score (good value-to-market-price ratio), not a recurrence of the old-inventory bug pattern (no "Higher Risk" flags, reasonable years/mileage).

## iOS MCP-app widget rendering — investigated, root cause narrowed, fix NOT yet attempted

Full network-capture investigation via a from-scratch Windows-only rig (Fiddler Classic + Windows Mobile Hotspot + manual iPhone proxy — no Mac available). Confirmed via 3 reproduced failures + 1 successful comparison capture (different, working connector):

- **On failure:** the `search-used-cars` tool call itself succeeds normally (data returns correctly) — matches the long-standing "text works, only the rendering box fails" symptom exactly. Zero request to any `{hash}.claudemcpcontent.com/mcp_apps?platform=ios` path occurs — the iOS client never attempts to fetch the widget resource at all.
- **On the working comparison connector:** this exact request fires and succeeds (200, real HTML widget content).

Fractal's read-only follow-up traced the likely mechanism to the vendored `skybridge` package's conditional `_meta.ui.domain` computation (depends on an exact `User-Agent === "Claude-User"` match; falls back to a malformed raw-origin-URL value otherwise). A directly analogous bug was already solved on the sibling Find My Car project — the working fix there was to **omit** `_meta.ui.domain` entirely (not compute a "correct" value), per SEP-1865 treating it as optional. Next Fractal run (pending, 24hr rate limit) will attempt this same omission approach, with an explicit pre-check that ChatGPT's separate `openai/outputTemplate` mechanism doesn't depend on this field, to avoid any regression there.

## Test infrastructure notes

- iPhone's Fiddler root certificate intentionally left installed (trust toggled OFF, not fully removed) at session end, to avoid redoing the one-time setup pain if another iOS capture round is needed before the fix above is confirmed. **Remove fully once the iOS fix is verified working live.**
- All fixes above were verified via direct interaction with the live production Claude connector, not solely from Fractal's self-reported test output — consistent with this project's standing Rule 9 verification discipline.
