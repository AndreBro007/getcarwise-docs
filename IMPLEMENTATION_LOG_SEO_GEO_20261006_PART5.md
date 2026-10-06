# SEO/GEO Implementation Log — Part 5 (Oct 6, 2026)

**Continues** `IMPLEMENTATION_LOG_SEO_GEO_20261006_PART4.md`. Owner lane: Claude — Engineering.

## Visible author byline — DONE (guides); posts already had one
- **Finding:** blog posts already show "by Andre Broekman" via the theme's `post-meta` template part (the one post that had been under `claude-automation` was reassigned earlier). Only pages lacked a visible byline.
- **Change:** new block-theme template **"Guide"** (slug `page-guide`, theme `twentytwentyfour`) created as a copy of the existing "Pages" template plus a centered line "By <post author name>" under the title (author name is not a link, because `/author/` is blocked in robots.txt). The copy keeps the Impact site-verification meta tag that sits inside the page template.
- **Assigned to 26 guide pages:** the 16 used-model guides, the hybrid SUV, used PHEV, used EV, sedan-under-$15k, truck-under-$35k, truck-towing, midsize-sedan-$30K comparison, Highlander comparison, AI-native shopping and true-cost guides. NOT assigned: the four protected Task #78 pages, the `/tools/` hub, the interactive tools (VIN check, Deal Score, price check, CarClever Lite), About, legal pages and Data & Guides.
- **Verified live:** the Camry and hybrid guides show "By Andre Broekman", keep the Impact meta tag, valid JSON-LD, one title/canonical/description, and (Camry) the related-guides block; the $30k protected page has no byline block and is unchanged; the True Cost post shows its byline and no `claude-automation` text anywhere.
- **Rollback:** set the pages' template back to default (empty) or delete the Guide template.
- **Not shown:** the author bio (André's existing bio kept as the stored profile text) and any "last updated" date, to avoid implying fresher content than the real edits.

## Still open
TASKS.md and DECISIONS.md splits (André to decide); confirm whether the AIOSEO install was André's; ChatGPT drafts for the two briefs; token rotation and PLAYBOOK credential revoke (André chose not to now). Protected pages could get the byline later, after the Task #78 observation window.
