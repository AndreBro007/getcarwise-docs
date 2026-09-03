# Edmunds VIN Search Validation Experiment

Date: 2026-09-03
Owner: ChatGPT / Business-Strategy lane
Status: Test in progress; no implementation authorized

## Why this test exists

Find My Car already does the important front-end work: it interprets the user's intent and returns a small set of best-matched vehicles. We must preserve that value and monetize every outbound vehicle action through the existing CJ Edmunds affiliate URL construction. The problem is that an exact VIN Edmunds page may be unavailable, stale, or difficult to discover through Google. We need evidence before changing the product.

## Confirmed UX and commerce design

Every result—new or used—keeps the same simple buttons:

- **Check avail.** — CJ-wrapped exact Edmunds VIN listing when available; otherwise a targeted CJ-wrapped Edmunds search for the same vehicle.
- **View similar** — CJ-wrapped similar-vehicle search. For an unverified exact listing, this may be broader; for a verified listing, it can remain close.

New vehicles are not excluded. They are expected to use targeted similar-new Edmunds searches more often because individual new-car VIN inventory appears less consistently indexed. Exact VIN checking still matters for new cars because the user may want the precise color, options, or dealer unit.

Never expose a raw Google URL, raw dealer URL, or non-CJ destination as the user-facing monetized link.

## Test protocol

1. Obtain a fresh mixed pool of result VINs.
2. Run an exact VIN-only Google search for every VIN.
3. If Google does not surface an Edmunds result, immediately run broader searches using year/make/model/trim, dealer and location, stock number, price, mileage, color, and freshness/listing terms.
4. Record whether the broader search identifies the exact Edmunds listing—not merely the same vehicle on a dealer or third-party website.
5. Provide Claude the CJ affiliate URL for every VIN, including positives and negatives. Claude checks each URL manually in Chrome and records: exact Edmunds listing, Edmunds unavailable page, or similar/search destination.
6. Use Claude's browser results as ground truth to decide whether the validation process is useful and whether the conditional broader search belongs in production.

The key measurement is: **Google VIN miss → broader-search recovery → Claude confirms exact Edmunds listing.**

## Pools tested so far

- Original Southern California used pool: 8 vehicles.
- New York/New Jersey used pool: 8 vehicles.
- Chicago new-vehicle pool: 8 vehicles.
- Total: 24 vehicles.

## Findings so far

The original five-vehicle screenshot case was corrected after review: 3/5 Edmunds pages were active and Google found those three; Nissan and Mazda showed unavailable pages. The Toyota RAV4 Adventure marked “New Arrival” was a newly added used/CPO listing, not a new vehicle, and was one of the Google positives.

In the fresh New York/New Jersey used pool, Google exact VIN search missed at least one vehicle that broader searching recovered as an exact Edmunds listing. This is a positive signal for conditional broader search.

In the Chicago new-vehicle pool, exact Edmunds indexing was weaker. Broader searches frequently found the exact new vehicle on dealer or third-party inventory pages, but did not consistently produce an exact Edmunds result. This is not evidence that new vehicles should be dropped; it indicates that new inventory will more often rely on targeted new Edmunds search fallback and must be checked in Chrome.

A direct automated attempt to open one CJ URL was inconclusive: the web session rejected it as an unsafe URL, and a command-line request could not run because network approval was unavailable. This does not establish that CJ or Edmunds blocks the URL. Claude Chrome remains the relevant browser test.

## What Claude must check

Claude should check all 24 CJ URLs from the three pools, not only Google misses. This supplies positive controls and negative testing. For each URL, record:

- VIN
- Google VIN result: found / not found
- Wider-search result, if run: exact Edmunds / non-Edmunds only / none
- CJ browser outcome: exact listing / unavailable / similar or generic search / redirect or error
- Whether the exact VIN, dealer, and vehicle details match
- Any “New Arrival” or listing-date clue

## Current decision gate

Do not implement a Google-based availability classifier yet. First compare all Google results and wider-search recoveries against Claude's CJ browser results. If wider search repeatedly recovers genuine Edmunds listings missed by VIN search, add it conditionally. If misses remain misses in Claude, use VIN-only evidence plus the existing targeted fallback and avoid unnecessary search complexity.
