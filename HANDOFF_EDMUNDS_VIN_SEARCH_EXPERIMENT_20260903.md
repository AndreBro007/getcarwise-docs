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


## Appendix A — Complete 24-vehicle CJ URL fixture list

Claude must check every CJ URL below in Chrome.

### Pool 1 — Southern California used

1. VIN `JF2GUHDC8SH306505` — 2025 Subaru Crosstrek Premium  
   https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fsubaru%2Fcrosstrek%2F2025%2Fvin%2FJF2GUHDC8SH306505%2Ffeatured-listing%2F

2. VIN `5N1BT3BB9TC833441` — 2026 Nissan Rogue SV  
   https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fnissan%2Frogue%2F2026%2Fvin%2F5N1BT3BB9TC833441%2Ffeatured-listing%2F

3. VIN `2T3P1RFV8RC453456` — 2024 Toyota RAV4 XLE  
   https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Ftoyota%2Frav4%2F2024%2Fvin%2F2T3P1RFV8RC453456%2Ffeatured-listing%2F

4. VIN `JM3KKDHA0R1110729` — 2024 Mazda CX-90 PHEV Premium  
   https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fmazda%2Fcx-90%2F2024%2Fvin%2FJM3KKDHA0R1110729%2Ffeatured-listing%2F

5. VIN `2T3J1RFV3RW476504` — 2024 Toyota RAV4 Adventure  
   https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Ftoyota%2Frav4%2F2024%2Fvin%2F2T3J1RFV3RW476504%2Ffeatured-listing%2F

6. VIN `WA1BBAFY3P2179956` — 2023 Audi Q5 Premium Plus  
   https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Faudi%2Fq5%2F2023%2Fvin%2FWA1BBAFY3P2179956%2Ffeatured-listing%2F

7. VIN `5N1BT3BB2SC763599` — 2025 Nissan Rogue SV  
   https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fnissan%2Frogue%2F2025%2Fvin%2F5N1BT3BB2SC763599%2Ffeatured-listing%2F

8. VIN `3MVDMBDM4RM634063` — 2024 Mazda CX-30  
   https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fmazda%2Fmazda-cx-30%2F2024%2Fvin%2F3MVDMBDM4RM634063%2Ffeatured-listing%2F

### Pool 2 — New York/New Jersey used

9. VIN `JM3KFBEMXS0723055` — 2025 Mazda CX-5 Premium Plus  
   https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fmazda%2Fcx-5%2F2025%2Fvin%2FJM3KFBEMXS0723055%2Ffeatured-listing%2F

10. VIN `7FARS6H84SE102229` — 2025 Honda CR-V Sport-L Hybrid  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fhonda%2Fcr-v%2F2025%2Fvin%2F7FARS6H84SE102229%2Ffeatured-listing%2F

11. VIN `1C4RJXN68SW584643` — 2025 Jeep Wrangler Sport S  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fjeep%2Fwrangler%2F2025%2Fvin%2F1C4RJXN68SW584643%2Ffeatured-listing%2F

12. VIN `JF2SLSRD7SH401651` — 2025 Subaru Forester Limited Hybrid  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fsubaru%2Fforester%2F2025%2Fvin%2FJF2SLSRD7SH401651%2Ffeatured-listing%2F

13. VIN `WA1GAAFY0R2009209` — 2024 Audi Q5 Premium S line  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Faudi%2Fq5%2F2024%2Fvin%2FWA1GAAFY0R2009209%2Ffeatured-listing%2F

14. VIN `WBX73EF02S5228598` — 2025 BMW X1 xDrive28i  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fbmw%2Fx1%2F2025%2Fvin%2FWBX73EF02S5228598%2Ffeatured-listing%2F

15. VIN `1C4RJKAG5S8658252` — 2025 Jeep Grand Cherokee L Altitude  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fjeep%2Fgrand-cherokee-l%2F2025%2Fvin%2F1C4RJKAG5S8658252%2Ffeatured-listing%2F

16. VIN `1C4PJXDG9RW330239` — 2024 Jeep Wrangler Willys  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fjeep%2Fwrangler%2F2024%2Fvin%2F1C4PJXDG9RW330239%2Ffeatured-listing%2F

### Pool 3 — Chicago new

17. VIN `1GNEVGKS9VJ113243` — 2027 Chevrolet Traverse LT  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fchevrolet%2Ftraverse%2F2027%2Fvin%2F1GNEVGKS9VJ113243%2Ffeatured-listing%2F

18. VIN `5NMP3DGL2TH219365` — 2026 Hyundai Santa Fe XRT  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fhyundai%2Fsanta-fe%2F2026%2Fvin%2F5NMP3DGL2TH219365%2Ffeatured-listing%2F

19. VIN `WMZ23GA02V7W39566` — 2027 MINI Cooper Countryman  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fmini%2Fcooper-countryman%2F2027%2Fvin%2FWMZ23GA02V7W39566%2Ffeatured-listing%2F

20. VIN `WMZ23GA0XV7W06931` — 2027 MINI Cooper Countryman  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fmini%2Fcooper-countryman%2F2027%2Fvin%2FWMZ23GA0XV7W06931%2Ffeatured-listing%2F

21. VIN `3VVUW7RM6TM141205` — 2026 Volkswagen Tiguan SEL R-Line Turbo  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fvolkswagen%2Ftiguan%2F2026%2Fvin%2F3VVUW7RM6TM141205%2Ffeatured-listing%2F

22. VIN `3VVUW7RM7TM106043` — 2026 Volkswagen Tiguan SEL R-Line Turbo  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fvolkswagen%2Ftiguan%2F2026%2Fvin%2F3VVUW7RM7TM106043%2Ffeatured-listing%2F

23. VIN `1V2KN2CA7TC580603` — 2026 Volkswagen Atlas SE w/Technology  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fvolkswagen%2Fatlas%2F2026%2Fvin%2F1V2KN2CA7TC580603%2Ffeatured-listing%2F

24. VIN `1V2KN2CA9TC576343` — 2026 Volkswagen Atlas SE w/Technology  
    https://www.anrdoezrs.net/click-101637236-17033607?url=https%3A%2F%2Fwww.edmunds.com%2Fvolkswagen%2Fatlas%2F2026%2Fvin%2F1V2KN2CA9TC576343%2Ffeatured-listing%2F

## Claude execution note

Please check all 24 URLs in Chrome. Do not use raw dealer URLs as substitutes for the CJ URLs. The question is whether the CJ redirect reaches an exact Edmunds listing, an Edmunds unavailable page, or a generic/similar Edmunds page. Capture the visible outcome and any exact-VIN/dealer/vehicle match.


## Appendix B — Claude Chrome ground-truth results (24/24)

Claude checked every CJ URL in Chrome.

| Pool | Exact listing | Unavailable with similar grid | Unavailable bare/no similar grid |
|---|---:|---:|---:|
| Southern California used | 5/8 | 2/8 | 1/8 |
| New York/New Jersey used | 6/8 | 2/8 | 0/8 |
| Chicago new | 0/8 | 6/8 | 2/8 |
| **Total** | **12/24** | **10/24** | **2/24** |

The two bare cases are #19 and #20, both 2027 MINI Cooper Countryman VINs:

- `WMZ23GA02V7W39566`
- `WMZ23GA0XV7W06931`

Both were reloaded and screenshot-verified. Edmunds showed “Vehicle no longer available” but no similar-listings module. This is a genuine third destination outcome, not a transient loading issue.

Three exact VIN matches had trim-label differences between the fixture data and the live Edmunds page: #7 SV vs. Rock Creek, #15 Altitude vs. Laredo, and #16 Willys vs. Sport S. VIN, dealer, and vehicle destination matched; treat these as stale trim metadata, not a broken destination.

**Important:** This Claude result does not by itself complete the Google decision gate. The per-VIN Google found/missed and broader-search recovery mapping must be joined to this table. No production classifier is authorized yet.
