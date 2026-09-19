# Review — Used PHEV SEO/GEO WordPress Rebuild

**Date:** 2026-09-19  
**Reviewer:** ChatGPT — Business/Strategy lane  
**Status:** **IMPLEMENTATION ACCEPTED. PHEV task complete; measurement plan adjusted for overlapping treatment windows.**

## Reviewed

- `HANDOFF_WORDPRESS_USED_PHEV_SEO_GEO_REBUILD_20260919.md`
- `RESEARCH_USED_PHEV_AUTHORITATIVE_SOURCE_PACKAGE_20260919.md`
- `RETURN_WORDPRESS_USED_PHEV_SEO_GEO_REBUILD_20260920.md`
- fresh `STATE.md`, `TASKS.md`, and current repository diffs/commits

Public web fetch of the page was attempted from ChatGPT's web path but returned a cache-miss/internal fetch failure, so this review does **not** claim an independent live-browser render test. Acceptance is based on Claude's authenticated WordPress return, its before/after verification record, the committed return document, and the admin commit diff.

---

# 1. Acceptance decision

The implementation is consistent with the approved handoff.

Accepted outcomes:

- page 937 retained its URL/canonical/robots;
- title/meta/H1 changed to the approved PHEV treatment;
- page expanded from 311 words/no meaningful heading structure into the approved decision framework;
- 8-model dated provider-availability table added;
- 6-model 2024 like-for-like comparison added;
- Prius trim caveat preserved;
- Escape FWD-only distinction preserved;
- Outlander gasoline-mode MPG trade-off preserved;
- Kia warranty wording avoids claiming full ordinary-used 10/100 powertrain transfer;
- recall language remains VIN-specific and scoped to "certain" vehicles;
- no bogus ~$1k provider prices used;
- no unsupported median/average used-price claim introduced;
- existing CJ CTA/disclosure and CarClever Lite preserved;
- editorial source links added without affiliate wrapping;
- no new app/MCP/Vercel/Impact work occurred;
- GSC recrawl/indexing request succeeded.

No rollback or corrective re-edit is required from this review.

---

# 2. T0 baseline accepted

Fresh pre-edit US 28-day baseline:

- Search clicks: **0**
- Search impressions: **124**
- CTR: **0%**
- avg position: **43.4**
- Google Generative AI impressions: **1**

Visible query demand remains concentrated around:

- `best phev`
- `best used phev cars`
- `best used plug in hybrid cars`
- related PHEV-list variants

This is suitable as the page-specific T0.

---

# 3. Same-day deployment deviation — decision

The handoff asked for the PHEV page to deploy on a different calendar date from the Sep 19 $30k treatment. Claude implemented both within the same Sep 19 UTC date.

**Decision: accept the deployment; do not roll back or restart either experiment.**

Reason:

1. the treatments are on different URLs;
2. each treatment has its own fresh immediately-pre-change T0 baseline;
3. GSC Search and Google Generative AI can be measured at page level;
4. the content changes are materially different enough to evaluate independently;
5. rolling back solely to recreate a calendar-day gap would create a second treatment event and make the measurement history worse, not cleaner.

The consequence is that the two pages should be treated as **concurrent page-level treatments**, not perfectly staggered sequential experiments.

---

# 4. Adjusted measurement plan

Measure $30k and PHEV separately at the same checkpoints:

## T+14
Directional only:

- impressions;
- clicks/CTR;
- avg position;
- query breadth;
- Google Generative AI impressions.

Do not declare success/failure from low-volume daily changes.

## T+28
Primary read:

For each treated page, compare:

- its own T0/current 28-day period;
- visible query movement;
- click/CTR movement;
- GEO movement.

Also compare against untreated/control pages to help distinguish a sitewide visibility change from page-treatment movement.

Recommended controls:

- 3-row under $50k — protected GEO benchmark;
- Hybrid SUV under $20k — hold/control;
- Used EV — hold/control.

## T+56
Persistence/confirmation:

- whether gains persist;
- whether query breadth expands;
- whether GEO visibility remains;
- whether any page requires a second treatment.

Do not combine the $30k and PHEV metrics into one blended "SEO experiment" result.

---

# 5. FAQ schema decision

Claude correctly did **not** add FAQPage schema because:

- it did not exist on the page before;
- the handoff said not to add new schema types merely for the experiment.

The visible FAQ content is still useful for readers and retrieval.

FAQ schema can be evaluated later as a separate structured-data decision; it is not a blocker to this treatment.

---

# 6. Kia warranty source caveat

The source package flagged exact 2024 Sportage PHEV hybrid-system transfer language for a final check.

The live treatment avoids making a strong transfer claim. It states the narrower, verified principle:

- Kia's full 10-year/100,000-mile **powertrain** term is an original-owner benefit and does not transfer in full to an ordinary subsequent owner;
- exact hybrid/PHEV-system coverage should be verified by model year/VIN.

This is sufficiently cautious for the treatment. No immediate correction is required.

---

# 7. Process note

Claude reported two recoverable execution near-misses:

- temporary click into Permalink instead of Title, reverted before save;
- first large-body push failed silently, detected by re-fetch and then successfully retried.

No incorrect state was reported as persisted.

The useful operational lesson is valid:

> for large authenticated WordPress REST pushes, use a call pattern that returns HTTP status/content confirmation inline, then independently re-fetch before claiming success.

This is process guidance, not a reason to change the published page.

---

# 8. Next SEO/GEO action

The next prepared treatment is:

`HANDOFF_WORDPRESS_25K_SUV_CONSOLIDATION_20260919.md`

Do **not** launch it tonight.

Use the **Brisbane/AEST calendar** for the next timing boundary and launch it on a later local date after capturing fresh T0 baselines for both $25k URLs.

The $25k package remains:

> retained Search-winning URL + richer comparison/GEO structure + internal-link consolidation + one-hop 301 only after content parity.

The deferred Edmunds/Impact work remains out of scope.

---

# Bottom line

The PHEV rebuild is accepted as complete.

The overlapping $30k/PHEV windows are manageable because measurement is page-specific and both have clean T0 baselines.

No rollback is warranted.

The next implementation is the $25k consolidation, but it should be a separate local-date treatment.
