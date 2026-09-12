# Review of Fractal electrified-search and rendering build — 2026-09-12

## Verdict

**Partially correct; not ready to call complete.** The body constraint fix for electric truck searches appears correctly implemented and the large-luxury route is directionally correct. The report contains one explicit test failure that was misclassified, omits requested hybrid pickup additions, and cannot establish ChatGPT/Claude rendering compatibility from inside Fractal.

## Confirmed strengths

- Tool-contract hash was reported byte-identical before/after.
- Electric truck requests now set a strict truck body mode and apply a final body filter instead of filling with electric SUVs.
- Live electric truck output was reported as 10/10 Rivian R1T trucks, which is valid truck output.
- large_luxury_suv was separated from general luxury_suv.
- The large-luxury sample (Escalade, Navigator, LX) is semantically plausible.
- Skybridge’s Claude user-agent path was inspected rather than assuming the plain-origin _meta.ui.domain behavior. It produced a hashed claudemcpcontent.com domain.

## Defects or incomplete evidence

1. The reported compact electric truck under $60k test returned Rivian R1T. R1T is a midsize pickup, so this is a body/size failure, not a test assertion problem. The implementation appears to enforce truck but not compact.
2. The requested hybrid pickup audit was not completed in the report. Only Rivian R1T was added to the electric list. No evidence shows Ford Maverick Hybrid, F-150 PowerBoost, Toyota Tacoma i-FORCE MAX or Toyota Tundra i-FORCE MAX were added or provider-validated.
3. The report’s all tasks complete wording is too strong. Hybrid pickup and full-size hybrid truck acceptance tests were not shown.
4. The Fractal process cannot test external ChatGPT or Claude clients. Byte-identical tools/list and preview resources are necessary but do not prove rendering.
5. Claude’s hashed claudemcpcontent.com metadata may be intentional Skybridge behavior, but production origin and actual Claude rendering remain owner tests after deployment.
6. The report says nine tools are unchanged, but the required proof should include actual before/after artifacts or hashes from the same canonical response, not only a summary sentence.

## External classification checks

Rivian’s own site identifies R1T as an electric truck, while independent vehicle classification describes it as a midsize pickup. Therefore it is valid for electric truck but not compact electric truck. Toyota’s official Tacoma and Tundra pages identify i-FORCE MAX hybrid powertrains, and Ford’s Maverick materials identify a full hybrid powertrain; these remain important audit candidates, subject to Auto.dev naming and inventory verification.

## Required next response from Fractal

Ask it to correct or explicitly document compact/midsize/full-size truck classification, run hybrid pickup/full-size hybrid tests, and report exact current category tables and provider evidence. Treat Claude rendering as preview-ready only until production resources/read and real ChatGPT/Claude tests are completed.


## Owner preview test result — large hybrid SUV

André's preview test for “large hybrid SUV under $70k in 90210” returned six Lexus RX 350h listings. The hybrid identification is plausible, but the size constraint failed: RX is a midsize luxury SUV, not a large SUV. This demonstrates that the hybrid body filter is working only at the broad SUV level; the large-size signal is still being discarded on the hybrid category path. The result must be treated as a reproducible defect requiring another Fractal correction before production deployment.


## Additional owner preview observations

- “Hybrid pickup under $70k in 90210” returned no results.
- Variants adding “truck,” using “hybrid truck,” and using “truck” alone also returned no results.

The hybrid-pickup result may indicate missing candidate coverage or provider availability. The plain “truck” failure is a separate higher-priority regression because the earlier build reported ordinary truck searches returning F-150/Silverado/Ram/Sierra/Tundra results. Fractal must reproduce the plain truck case before assuming this is only an inventory gap. The large-hybrid-size failure remains separately queued because only one Fractal request can be sent per day.


## Further owner preview observation

The electric-truck test returned no results. Changing the prompt to “Full-size truck under $70k in 90210” returned results. Ordinary full-size truck search therefore works, while the electric-plus-truck path remains broken or has no verified matching candidate. This does not validate the previous Fractal claim that electric-truck behavior was complete.


## Further owner preview observation — successful electric truck rerun

A rerun of “Electric truck under $80k in 90210” returned Rivian R1T listings. These are valid electric trucks. This shows the electric-truck path can work, although the earlier empty run remains unexplained and should be considered intermittent/provider or parsing variance until repeated deterministically. The compact electric truck failure and missing hybrid-pickup coverage remain open.
