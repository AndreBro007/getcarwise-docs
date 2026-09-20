# Review — Task #63A WordPress Impact Static Destination Mapping

**Reviewed:** 2026-09-21  
**Return:** `RETURN_WORDPRESS_IMPACT_STATIC_DESTINATION_MAPPING_20260921.md`  
**Verdict:** **Accepted. Phase A complete; all three destination classes validated.**

## Accepted destination map

| Class | Impact-managed URL | Verified final purpose |
|---|---|---|
| New | `https://edmunds.sjv.io/c/7765200/3949597/52125` | Edmunds new-car shopping |
| Used | `https://edmunds.sjv.io/c/7765200/3949600/52125` | Edmunds used-car shopping |
| Trade-in | `https://edmunds.sjv.io/c/7765200/3949601/52125` | Edmunds sell/trade-in path |

All three are existing Impact-managed assets. Nothing was created or manually reconstructed. Claude verified one-hop redirects, correct Edmunds destinations and intact tracking without submitting a lead.

## WordPress inventory accepted

The live site currently has six CJ placements across five pages, using two unique Used-only CJ links. No existing WordPress New or Trade-in CTA was found. The $30k midsize-sedan comparison page has neither an Edmunds CTA nor a CarClever Lite embed.

## Decision for the $40k page

The Task #70 CTA gate is closed. The revised page may use:

- New as its primary conversion action;
- Used as a secondary alternative;
- Trade-in as a contextual replacement-intent bridge;
- CarClever as the evaluation/tool continuation.

Trade-in must not compete with New above the fold. It belongs later in the page after the reader has established purchase/replacement intent.

## Scope decision

The revised Task #70 implementation is authorized to make the page-specific CJ→Impact change on the $40k URL as part of its integrated content/funnel rebuild.

This does not authorize the remaining sitewide Task #63B migration. The other CJ placements remain unchanged until a separately dated page-by-page migration is approved.

## Measurement

Because content and funnel architecture will launch together on the $40k page, they form one bundled page treatment. Search/GEO and funnel actions must be reported separately, but the content and CTA contributions cannot be causally isolated from one another within this treatment.
