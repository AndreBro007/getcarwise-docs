# Post-launch verification and remaining website fixes — 9 October 2026

Status: public verification COMPLETE; live repairs NOT APPLIED. Checked about 21:52–21:55 Brisbane. Owner authorised ChatGPT to continue while Claude was out of tokens.

## Verified from fresh public reads
- 49 published pages + 11 posts = 60 sources.
- Old CarClever directory anchors: 32 (same total as before; Claude's full unchanged-link comparison is separately in its log). New ChatGPT anchors: 48. Claude directory anchors: 52 across 43 sources. Counts describe stored published content; page 771 redirects, so do not interpret 43 as 43 distinct visitor destinations.
- Launch post 1546 is published and returns HTTP 200. Public rendered text matches the latest approved HTML draft after HTML removal/entity decoding/whitespace normalisation. This is a text-content comparison, not a byte-identical raw Gutenberg check.
- Post has six Claude links and three new ChatGPT links. Title, description, canonical, index/follow robots and publication metadata are present.
- Live /blog/ includes the announcement. Guide 1071, Tools 452, Decision Center 1160 and historical post 952 include announcement links.
- Homepage retains two old-app links, Tools retains three, historical post 952 retains one.
- Post has no featured media. Its actual Open Graph fallback is the site's 512×512 car icon; sharing is not image-less, but a launch-specific 1200×630 graphic remains preferable.
- Page 937 has three tables and three scroll wrappers. Pages 828/830/934 have respectively 2/1/2 tables and zero overflow-x wrappers. Claude's browser-confirmed mobile overflow remains unresolved; no new independent visual/mobile preview was available in ChatGPT.
- GA4 tag G-HNN7CS0Z4L and MonsterInsights appear on the article and blog. Installation presence does not establish click-event collection. Owner-parked click capture and logged-out Claude-listing checks were not performed.

## Sitemap diagnosis
Plain /post-sitemap.xml contains 10 entries and omits both post 1546 and post 1469. Same missing entries at:
- /post-sitemap.xml?review=20261009-evening
- /?sitemap=post
- /index.php?sitemap=post

XML requests returned 200 and the plain/query-string responses advertised Cache-Control: no-cache, no-store, must-revalidate, max-age=0. /page-sitemap.xml contains 47 entries. These observations favour an origin/plugin-generation or internal-cache issue rather than a simple browser cached copy, but do not isolate the actual cause; content exclusion/settings remain possible.

## Smallest next repair: sitemap (authenticated admin required)
Primary source read Oct 9: https://rankmath.com/kb/exclude-sitemaps-from-caching/ (Next Steps).
1. In Rank Math SEO → Sitemap Settings, record the existing Links Per Sitemap value and inclusion/exclusion settings. Confirm published, indexable posts 1546 and 1469 are not intentionally excluded.
2. Follow Rank Math's documented cache regeneration: change Links Per Sitemap by one and Save Changes. Record the value used, then restore the original value and save so the setting returns to its previous state.
3. Settings → Permalinks → Save Changes without changing the permalink structure, as the vendor documents.
4. Fresh unauthenticated fetch of the ordinary post sitemap must contain BOTH actual post URLs; a query-string-only success is insufficient. Check the page sitemap now reflects the latest guide changes, then check sitemap index and a representative live page.
5. If still stale, inspect the actual hosting/cache layers and sitemap exclusions. Do not edit .htaccess, deactivate SEO, disable site-wide caching or add a theme filter as a speculative first fix.
No cache/settings changes have been made by ChatGPT.

## Smallest next repair: five tables on three pages
| ID | Page | Tables |
|---|---|---:|
| 828 | /tools/best-midsize-sedan-under-40000/ | 2 |
| 830 | /tools/best-3-row-suv-under-50000/ | 1 |
| 934 | /tools/best-compact-suv-under-25000/ | 2 |

Use the same scoped wrapper already applied by Claude on 937:
```html
<div style="overflow-x: auto; -webkit-overflow-scrolling: touch;">
  <!-- existing table markup, unchanged -->
</div>
```
Fetch fresh authenticated edit-context RAW source, capture rollback content/revision, preserve Gutenberg block structure, wrap only the unwrapped comparison tables, and abort if the page changed since reading. Never POST the public rendered content as a substitute for raw source. Preserve all original text, table contents, links, iframes, scripts and schema. Read back raw content exactly; verify at 390px and desktop that tables scroll within the page without clipping or whole-page overflow. Record another dated Task #78 intervention if applied. Live table fixes have NOT been applied.

## Access limitation and work completed
Local runtime failed to start; no authenticated browser, WordPress connector or current WordPress application password exists in this ChatGPT lane. PLAYBOOK confirms the NEW credential is exclusively in Claude's project instructions; the old repository credentials were revoked and redacted. No credential was requested, guessed, printed or copied from older records. A one-CPU nonpersistent Vercel Sandbox fetched public pages/XML and was stopped. No secrets were placed in it.

Corrected the earlier ChatGPT audit/handoff with prominent superseded-policy notices; keep old toolkit links where relevant and preserve existing explanations. Publication is now recorded on the Markdown draft and editorial checklist. No WordPress content, production deployments, subscriptions, affiliate redirects or lead forms changed in this follow-up.

Remaining: authenticated sitemap/table repairs, launch share image, owner-parked measurement and logged-out listing checks. Directory indexing is pending observation; propagation timing is unconfirmed.
