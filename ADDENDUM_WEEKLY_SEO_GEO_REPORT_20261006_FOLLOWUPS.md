# Addendum — Weekly SEO/GEO Report Oct 6, 2026: same-day follow-ups

**Owner lane:** Claude — Engineering. Supplements `WEEKLY_SEO_GEO_REPORT_20261006.md` (which predates these actions; where they differ, this addendum is later).

## 1. Task #67 (ChatGPT follow-up): redirected comparison URL removed from sitemap — DONE
- **Change:** Rank Math → Sitemap Settings → General → "Exclude Posts": added `771` (the field was empty). Nothing else changed.
- **Verified live (Oct 6, after save, cache-busted fetches twice):**
  1. `/tools/best-compact-suv-under-25k-comparison/` is absent from `page-sitemap.xml` (48 → 47 URLs).
  2. It still returns a one-hop 301 (`x-redirect-by: Rank Math`) to `/tools/best-compact-suv-under-25000/`; following it = 1 redirect, final 200.
  3. The retained page returns 200 with 0 redirects and is still listed in the sitemap.
  - `sitemap_index.xml` and `post-sitemap.xml` still return 200.
- **Not done:** WP Rocket cache was not cleared (not needed — the live sitemap already reflected the change).

## 2. Semrush Backlink Audit — disavow recalculation confirmed by André's instruction
- Clicked "Yes, I uploaded the file" (Semrush's prompt referenced its Sep 27 export; the file in Google is André's 87-domain combined file, so the two are not identical).
- **Result:** Overall Toxicity Score High → **Medium**. Referring domains 51 (disavowed excluded), backlinks 63, toxic **25 (49%)**, non-toxic 26 (51%).
- This corrects the earlier reading: of the 51 domains "for review", about half are non-toxic; the genuinely un-disavowed toxic set is ~25 domains, not 108. The 5 spam domains seen earlier are part of it. The other ~20 remain unseen on the current Semrush plan.

## 3. Not done / still open
- STATE.md weekly entry and Claude checkpoint row (widget reviewed through `183554b`, docs held at `4fe2e15`): not written — STATE.md (~425 KB) is too large for a connector write and no GitHub token is available in the sandbox. No checkpoint was advanced.
- Clarity read, GSC redirect/404 drill-down, remaining unread docs, PLAYBOOK.md plaintext WordPress credential revoke/redact.
