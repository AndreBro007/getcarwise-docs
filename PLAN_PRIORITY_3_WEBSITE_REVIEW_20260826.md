# Priority #3: Coordinated Website Review Plan
## Executive Recommendation + Proposed Website Alignment for New+Used MCP Apps

**Prepared:** Aug 26, 2026, 10:15 AEST  
**For:** André approval before implementation  
**Status:** Investigation complete, recommendations ready for review

---

## EXECUTIVE SUMMARY

**Current state:** Website messaging assumes used-only scope (homepage, web apps, navigation). This reflects the old CarClever (Fractal, used-only, OpenAI-approved) which is still live.

**New reality:** Two new+used MCP apps submitted to both OpenAI and Anthropic:
- **CarClever — New & Used Cars** (Fractal/Sky, in Anthropic review, blocked by Fractal deployment issues)
- **CarClever - Find My Car** (Vercel, in OpenAI + Anthropic review, no blockers)

**Decision pending:** Which app(s) become primary? Drop Fractal apps? Timeline?

**Website alignment strategy:** Until the new apps are approved and go live, the website messaging should remain accurate to the current live product (used-only). Once approved and live, messaging must pivot to new+used. This document proposes HOW to make that pivot cleanly when ready.

---

## CURRENT WEBSITE MESSAGING AUDIT

### ✅ ALREADY CORRECT (No changes needed)

**Pages that are already aligned with Anthropic requirements:**
- `/carclever-guide/` (ID 1053) — ✅ Assistant-agnostic user guide (meets Anthropic doc requirement)
- `/carclever-find-my-car/` (ID 1071) — ✅ Find My Car specific guide (accurate, current)
- `/privacy-policy/` (ID 3) — ✅ Reviewed, retention section OK
- `/terms-of-service/` (ID 33) — ✅ Reviewed, VIN wording kept broad/unchanged
- `/contact-us/` (ID 64) — ✅ Support contact live

**Pages with scope already verified as used-only (accurate NOW):**
- `/tools/vin-check/` (ID 1023) — VIN decoder, works for any vehicle (new or used)
- `/tools/deal-score/` (ID 453) — Deal score assumes used-car listing data
- `/tools/price-check/` (ID 527) — Price check assumes used-car listings
- `/carclever-lite/` (ID 239) — Evaluation tool for used cars (calls old CarClever backend)

---

### 🔴 MESSAGING CONFLICTS TO RESOLVE (When New+Used Apps Go Live)

#### 1. HOMEPAGE (ID 7) — Headline & Core Copy

**Current:**
- Headline: "The Only Independent AI Evaluating **Used Cars**"
- FAQ says: "GetCarWise is an AI-powered **used car** research platform"
- Copy: "evaluate a vehicle's price against the market, flag risk factors like **title** and **accident history**"

**Conflict:** When Find My Car (new+used) or Sky (new+used) go live on Claude/ChatGPT, this messaging becomes wrong.

**Proposed changes (phase 2, when new apps go live):**
- Headline option A: "The Only Independent AI for Car Shopping" (neutral)
- Headline option B: "Independent AI for New & Used Car Shopping" (explicit)
- Recommendation: Option B (clearer, more defensible)
- FAQ update: "GetCarWise is an AI-powered **new and used car** research platform"
- Copy update: "evaluate a vehicle's value, flag risk factors, and research **new and used** vehicles..."

**Why wait:** Homepage is currently accurate. Changing it before new apps are live creates false promises. Change only when the new+used capability is actually live.

#### 2. TRY-CARCLEVER PAGE (ID 38) — App Reference

**Current:**
- Status message: "⚠️ App Status: Live on ChatGPT **@CarClever**" (old app name)
- Links: Reference to "CarClever" but doesn't distinguish old vs. new

**Conflict:** When Find My Car approved, users clicking "Try CarClever" might be confused if they land on the old app vs. new.

**Proposed change (phase 2):**
- Option A: Update to "Live on ChatGPT and Claude as **CarClever - Find My Car**" (direct)
- Option B: Add sub-heading "New & Used Cars" to clarify scope
- Recommendation: Option A + link to `/carclever-find-my-car/` guide

**Why wait:** Old app is still the live one. Switching this before new app approval creates confusion.

#### 3. WEB APP PAGES (Deal Score, Price Check, VIN Check, Lite)

**Current messaging:**
- "CarClever Lite: Free AI **used car** evaluation"
- "Deal Score: AI deal evaluation... **used car deals**"
- "Price Check: pricing analysis for **used car listings**"
- "VIN Check: any vehicle VIN... reveals specs... [works for new or used]"

**Conflict:** These pages are accurate now (they do evaluate used cars). But when website messaging shifts to new+used, these need review:
- Deal Score: Can it evaluate new cars? Or used-only? → **Needs product clarification**
- Price Check: Can it evaluate new cars? Or used-only? → **Needs product clarification**
- VIN Check: Already agnostic (decodes any VIN, new or used) → **No change needed**
- CarClever Lite: Calls old CarClever backend → Will need backend update to new+used support

**Proposed change (phase 2, conditional on product scope):**
- IF Deal Score/Price Check can/should support new cars: Update FAQs
- IF Deal Score/Price Check are used-only by design: Keep messaging as-is, clarify on web app pages
- VIN Check: No changes needed (already works for any vehicle)
- CarClever Lite: Update backend integration to call new+used MCP app when available

**Why wait:** Product capability not yet confirmed for web apps. Don't change messaging until design is locked.

---

## IMPLEMENTATION ROADMAP (Two Phases)

### PHASE 1: NOW (Before New+Used MCP Apps Go Live)
**Action:** No changes. Verify existing pages remain accurate.

**Checklist:**
- ✅ Keep homepage used-only messaging (correct)
- ✅ Keep web app pages used-only messaging (correct)
- ✅ Keep `/carclever-guide/` and `/carclever-find-my-car/` as-is (correct, guides are live)
- ✅ Monitor OpenAI + Anthropic review progress (no action)
- ✅ Document what WILL change when apps go live (this plan)

**Deliverable:** This plan document (ready for André)

### PHASE 2: WHEN NEW APPS APPROVED & LIVE
**Trigger:** Either Find My Car (Vercel) or Sky (Fractal) gets final approval + is deployed to production

**Actions (waiting for André decision on which app is primary):**

**A. Homepage alignment**
- Update headline to "Independent AI for New & Used Car Shopping" (or equivalent per André)
- Update FAQ to reflect new+used scope
- Maintain professional tone, avoid "submitted"/"in review"/"coming soon" copy

**B. Try CarClever page**
- Update app reference to primary approved app name
- Link to correct guide (already built)
- Clarify new+used scope in intro

**C. Web app pages (conditional)**
- Review Deal Score + Price Check capability (new vs. used scope)
- Update FAQs if they support new cars
- Keep VIN Check as-is (already agnostic)

**D. CarClever Lite backend update**
- If new+used backend becomes standard, update Lite to call it
- Keep web app messaging aligned with actual backend

**E. Navigation audit**
- Ensure all app references point to live, approved versions
- Remove references to old/deprecated apps (if applicable)
- Confirm no "coming soon" or ambiguous copy exists

---

## ALREADY COMPLETE (Per Earlier Review)

**No further action needed on:**
1. ✅ Affiliate disclosure (Commission Junction references verified across pages)
2. ✅ Complianz contact-data cleanup (already done, per TASKS.md)
3. ✅ Terms VIN wording (reviewed, deliberately broad, no change)
4. ✅ Privacy retention section (reviewed, no change)
5. ✅ Legal pages (`/privacy-policy/`, `/terms-of-service/`)

---

## CONDITIONAL ITEMS (Require André Decision)

**Before proceeding with Phase 2, clarify:**

1. **Which app(s) are primary going forward?**
   - Find My Car only? Or find a way to keep Sky (Fractal)?
   - Timeline for deprecating old CarClever?

2. **Web app scope (Deal Score, Price Check):**
   - Can they evaluate new cars, or are they used-only by design?
   - Should web app messaging change if Find My Car becomes primary?

3. **CarClever Lite backend:**
   - Should it call old CarClever (Fractal), or switch to new MCP app?
   - Can/should Lite support new cars?

4. **Platform-availability wording:**
   - André stated preference: avoid "submitted"/"in review"/"coming soon" copy
   - When apps go live, how should availability be communicated?
   - Example: "Live on Claude and ChatGPT" vs. "Now available on..." vs. other?

---

## PROPOSED TODO LIST (Phase 2, When Approved)

**After André approves this plan and new apps go live:**

1. Update homepage headline (new+used positioning)
2. Update homepage FAQ (new+used scope)
3. Update Try CarClever page (app reference + link)
4. Review + update Deal Score page (if new-car capable)
5. Review + update Price Check page (if new-car capable)
6. VIN Check page: No changes (already agnostic)
7. CarClever Lite: Update backend integration (if scope changes)
8. Audit navigation: Ensure no old app references remain
9. Verify affiliate disclosures consistent across all pages
10. SEO audit: Check focus keywords, meta descriptions align with new+used messaging
11. Test all external links (submission guides, privacy, support) still resolve
12. Document final state in website audit log

---

## SUMMARY FOR ANDRÉ

**Status:** Website is currently accurate to live product (used-only).

**What's ready:** Two new+used MCP apps submitted, awaiting approval.

**What we're waiting for:** Final approval from OpenAI/Anthropic, decision on which app(s) become primary.

**Next step:** Approval of this plan. Once new apps go live, follow Phase 2 changes above.

**No urgent changes needed now.** Site messaging is honest and correct. When apps go live, this plan provides a clean path to align the website with the new reality.

---

**Prepared by:** Claude  
**For approval by:** André  
**Ready for Phase 2 implementation when:** New+used MCP app goes live (OpenAI or Anthropic approval + production deployment)
