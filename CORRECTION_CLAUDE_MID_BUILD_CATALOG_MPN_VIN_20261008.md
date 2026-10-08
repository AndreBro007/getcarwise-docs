# Mid-build correction for Claude: Edmunds catalogue VIN is in Mpn

8 October 2026, Australia/Brisbane.
Purpose: amend the data-continuity build already underway. Continue the current isolated branch and preview; no restart or redesign is requested. Read this before making further decisions about VIN support.

## The correction

**The VIN was historically present in the returned `Mpn` field. Searching/filtering by `Mpn` or VIN is unsupported. These are separate capabilities.**

The first continuity handoff inherited an incorrect no-VIN conclusion from the later prototype report. André identified the missed field. The handoff and three related documents have now been corrected and re-fetched to verify.

## Best primary project evidence

[STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md](https://github.com/AndreBro007/getcarwise-docs/blob/main/STRATEGY_EDMUNDS_IMPACT_MIGRATION_20260916.md)

Read these specific subsections:
1. **“Product Catalog schema — CONFIRMED LIVE, major finding (Sep 16, later)”**: three sampled listings explicitly documented **“VIN (in the `Mpn` field)”**, and already-tracked item URLs in `Url`.
2. **“Track A investigation — VIN lookup explored, not resolved (Sep 16, later)”**, including the Sep 17 resolution: `Query=Mpn='{vin}'` returned `400 Unknown search field name: Mpn`; Impact support ticket **#882346** confirmed the search limitation.

The first subsection contains an exploratory proposal to search by VIN and overly strong stock claims. Those proposals were superseded by subsequent findings. Use its returned-field evidence, not its proposed VIN lookup or claims that stock proves current availability.

## Why the later prototype conclusion is unreliable

The Sep 21 prototype return's section 9.3 checked:
- field names resembling VIN;
- VIN-shaped text in Description, Bullets, Name and Text3.

It did not document checking `Mpn`. That probe therefore cannot establish that catalogue records contain no VIN.

The existing prototype's narrow `RawImpactItem` interface and normalizer omit `Mpn`. Its normalized cards consequently lack VIN; that is not proof the upstream field is absent. The NHTSA helper's no-usable-VIN header comment needs correcting when its wiring is revisited.

## Apply this to the build now

1. Inspect `Mpn` explicitly in a small current, read-only sample using the existing Impact credentials. Report aggregate presence, valid-format counts and any year/make/model conflicts; do not print credentials, full upstream bodies or raw VIN lists. Current feed-wide completeness is not yet established.
2. In the new internal source adapter, read `Mpn`, normalize whitespace/case, validate a genuine 17-character VIN, and retain the field's provenance. Shape validation alone does not establish identity correctness.
3. Carry valid VINs from **returned candidates** into the existing identity/verification flow and optional NHTSA enrichment. Keep missing or invalid VIN explicit. Preserve the existing screens/tool schemas wherever compatible.
4. Use the catalogue's supplied `Url` as the tracked destination where applicable; do not wrap it twice. Test the existing `resolve_dealer_url` behavior against candidates that now have real VINs.
5. Do not implement server-side catalogue VIN queries, keyword VIN search, exhaustive pagination or bulk download to find a VIN. For candidate detail/follow-up, reuse the returned normalized candidate or a bounded permitted cache. An arbitrary user-supplied VIN is a different case: NHTSA can decode it, but failure to locate it in the catalogue is not proof sold/unavailable.
6. Test valid, missing and malformed `Mpn`; NHTSA timeout/identity mismatch; correct tracked links; and **zero Auto.dev requests in catalogue-only mode**. Use fixtures for most checks.

A populated VIN does not establish New/Used/CPO, accident history, current availability, mileage or exact local proximity. Continue checking those fields independently. NHTSA is specification/recall support, not substitute dealer inventory.

## Scope remains unchanged

Continue the current private continuity build. Keep the same screen layout and public tool contract as the compatibility target. No production promotion, package submission, broad feature work or extra spending is requested by this correction.

The [updated full handoff](https://github.com/AndreBro007/getcarwise-docs/blob/main/HANDOFF_CLAUDE_EDMUNDS_DATA_CONTINUITY_SPIKE_20261008.md) now contains this mapping. This short note is intended to amend the active build without making you redo completed work.
