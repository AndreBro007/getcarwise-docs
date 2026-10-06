# Proposed monthly data series: new versus used availability and asking-price gap

**Status: proposed, pending André confirmation. Not for publication.**  
**Author: André Broekman**  
**Decision requested:** Approve or revise the research design before any inventory calls are made. This document contains no findings, market statistics, or sampled inventory data.

## What would the new-versus-used data series measure?

The series would track how many eligible new and used listings are visible in a defined inventory sample and compare their advertised prices over time. It would publish observed listing counts and asking-price distributions with a clear method, date, market definition, and limitations. It would not claim to represent every car for sale or the final price buyers pay.

The working editorial question is: “How does the advertised price gap between comparable new and used vehicles change in the markets we can consistently observe?” That framing is more useful than a broad claim about the entire U.S. used-car market unless the data coverage can support that claim.

## What should count as “availability”?

For this project, availability should mean a listing returned by the selected source at a specified snapshot time that passes the documented filters. It should not mean that a car is still available at a dealer unless availability is independently confirmed. Listings can be duplicated, stale, removed, or changed after collection.

Before collecting anything, verify what fields the current provider returns and what its terms allow us to store, analyze, and publish. Do not assume that a listing ID, VIN, price, location, trim, or condition field is present or reliable until the current API documentation and sample response confirm it. If the data cannot support stable deduplication, label the measure “returned listings,” not unique vehicles.

## How should new and used vehicles be compared fairly?

Compare vehicles within matched groups rather than pooling unlike vehicles. A group could be defined by make, model, model year, trim, body style, powertrain, market, and snapshot date, but include only fields the provider supports consistently. “New” and “used” should follow the provider’s condition field, with certified-pre-owned handled separately or excluded under a rule set before collection.

The price comparison should use advertised listing prices, not describe them as transaction prices. Show the distribution selected for publication and how the group was constructed. Do not combine a low-mileage recent-year used vehicle with a different new trim and call the difference a like-for-like gap. If the sample is sparse or changes definition between months, omit the comparison or flag the break in method.

A geographic sample should be selected for continuity and described plainly. Avoid calling selected metros “national” or “representative” unless the sampling design and evidence justify those terms. Any map or market label should describe where listings were searched, not where all buyers or vehicles are located.

## What data would each monthly release need?

Each release should preserve a dated record of its source, filters, query definitions, coverage, excluded records, and calculations. The research log should include:

- Snapshot date and time, source, and retrieval method.
- Search geography and vehicle-matching rules.
- Condition definitions and treatment of certified vehicles.
- Rules for duplicate or incomplete listings, price anomalies, and unavailable records.
- Number of records returned and retained, with any exclusions explained.
- The exact advertised-price measure and any summary statistic used.
- Known coverage gaps and changes from the previous release.

These are method requirements, not observed results. Do not publish counts, percentages, averages, medians, or price gaps until they have been computed from saved source records and independently checked. Every value in a public chart or paragraph should be traceable to that release’s retained data and method notes.

## How should API usage be controlled?

Do not make research calls until André approves the design and the current subscription status, remaining allowance, rate limits, and permitted use have been checked against the provider’s live account and current documentation. Project records note that Auto.dev usage is shared by multiple product surfaces and that discretionary testing should be monitored; see the current [Auto.dev operating decisions](https://github.com/AndreBro007/carclever-widget/blob/main/DECISIONS.md) and [provider reference notes](https://github.com/AndreBro007/carclever-widget/blob/main/REFERENCE.md). Those internal records are operating context, not a substitute for checking the provider dashboard before a new collection.

The research owner should estimate the full call plan, reserve capacity for product operations, and define a stop condition before collection. If the remaining allowance cannot be established, do not collect. If the API returns unexpectedly large, incomplete, or duplicate-heavy results, stop and revise the design rather than expanding calls ad hoc. Keep credentials out of research drafts and published material.

## What could the first release say?

Nothing about the current price gap or the number of cars available until a real sample has been collected and checked. The first release can make a narrow claim about the sample it actually observed, for example: “In the listings returned by this defined search on this snapshot date, matched new examples had a different advertised-price distribution from matched used examples.” The sentence should be filled only with verified values and must identify the sample and comparison.

If the data does not produce a reliable match, publish a methods note or postpone the result. An honest “not enough comparable listings to report this month” is better than filling the chart with weak or non-comparable records.

## How could the series earn useful citations?

Publish a short article alongside a downloadable or inspectable methodology note, a clear chart, and a plain-language explanation of what the sample can and cannot establish. Offer reporters, researchers, and consumer educators a stable page to cite. A reusable monthly format makes changes in definitions visible and lets readers compare like with like.

The editorial angle should focus on a useful buyer question, such as whether a shopper’s shortlist has new and used alternatives at different asking prices. The series should not promise “the cheapest car,” “the best time to buy,” or savings unless the observed data and method actually support those conclusions. Any outreach or media pitch should link to the published methods and disclose the source, snapshot date, and limitations.

## What must be approved before the first release?

André should confirm the vehicle groups, geographic scope, source and permitted use, snapshot schedule, operational call budget, storage plan, and who reviews the calculations. Product and technical owners should verify the current API fields and the data’s permitted retention and publication. The first release should be reviewed against its saved source records before any chart or headline is approved.

Until that review is complete, this is a research proposal only. No API calls, inventory sampling, or public market claims are part of this draft.
