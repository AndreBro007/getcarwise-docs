# Website & App Infrastructure Audit — Aug 26, 2026

**Status:** Baseline audit complete. Ready for Priority #3 coordinated website review planning.

**Current Time:** Wednesday, Aug 26, 2026, 09:45 AEST (Tuesday 19:45 EDT)

---

## SUMMARY: 3 Categories of Apps

### ✅ CATEGORY 1: WEB APPS (Website-only, I built these, code in hand)

| App | URL | ID | Purpose | Integration | Status |
|-----|-----|-----|---------|-------------|--------|
| **CarClever Lite** | /carclever-lite/ | 239 | Free AI used car evaluation (deal score, risk, TCO) | Uses old CarClever (Fractal) backend | 🟢 Live |
| **VIN Check** | /tools/vin-check/ | 1023 | Free VIN decoder + risk score (NHTSA recalls, Auto.dev specs) | Direct to Auto.dev + NHTSA API | 🟢 Live |
| **Deal Score** | /tools/deal-score/ | 453 | AI deal evaluation (0-100 scale, 5-factor analysis) | Integrated tool, used-car focused | 🟢 Live |
| **Price Check** | /tools/price-check/ | 527 | AI pricing analysis (fair/good/overpriced) | Market data analysis, used-car focused | 🟢 Live |
| **Try CarClever** | /try-carclever/ | 38 | Landing page → links to ChatGPT/Claude AI assistants | Links to MCP apps | 🟢 Live |

---

### 🤖 CATEGORY 2: MCP APPS (AI Assistants, for ChatGPT/Claude)

| App Name | Platform | Scope | Status | Blocker |
|----------|----------|-------|--------|---------|
| **CarClever** (original) | Fractal | Used-only | 🔄 Anthropic IN REVIEW (feedback received, can't deploy fix) | Fractal PRD deployment blocked |
| **CarClever — New & Used Cars** (formerly "Sky") | Fractal | New + Used | 🔄 Anthropic IN REVIEW (never deployed to PRD) | Fractal PRD deployment blocked |
| **CarClever - Find My Car** | Vercel/GitHub | New + Used | 🔄 OpenAI IN REVIEW (SEP-1865), submitted to Anthropic | None (Vercel works fine) |

---

### 📊 CATEGORY 3: SUPPORTING INFRASTRUCTURE (Pages, Guides, Hubs)

**Documentation/Guide Pages:**
- `/carclever-find-my-car/` (ID 1071) — Find My Car MCP app guide (Anthropic feedback fix)
- `/carclever-guide/` (ID 1053) — Assistant-agnostic user guide (new, Anthropic requirement)
- `/tools/` (ID 452) — Tools hub (aggregates Lite, VIN Check, Deal Score, Price Check)
- `/data-guides/` (ID 899) — Data & Guides hub (vehicle profiles, buying guides)

**Blog/Educational:**
- `/blog/` (ID 300) — Blog hub
- 30+ individual blog posts (vehicle profiles, buying guides, cost analysis)
- Key posts on new vs used (financial math, depreciation, cross-shopping)

**Core Pages:**
- Homepage (ID 7) — `getcarwise.app/` — **🔴 MESSAGING: "Used Car Research & AI Deal Scoring" — outdated**
- `/try-carclever/` (ID 38) — AI assistant landing page
- `/about-getcarwise-our-story/` (ID 68) — Methodology
- `/contact-us/` (ID 64) — Support
- `/terms-of-service/` (ID 33) — Legal (VIN wording reviewed, broad, OK)
- `/privacy-policy/` (ID 3) — Legal (retention section reviewed, OK)
- `/opt-out-preferences/` (ID 115) — Compliance

---

## CURRENT MESSAGING CONFLICTS

### 🔴 HOMEPAGE (ID 7)

**Current headline:** "The Only Independent AI Evaluating **Used Cars**"

**Current FAQ:**
- "GetCarWise is an AI-powered **used car** research platform"
- "evaluate a vehicle's price against the market, flag risk factors like **title** and **accident history**"

**Conflict:** When Find My Car (new+used) goes live, or if Sky/App #3 (new+used) deploys, this is wrong.

**Messaging inventory:** Page references "used cars only" 5+ times in visible copy.

---

### 🔴 WEB APP PAGES (Deal Score, Price Check, VIN Check, CarClever Lite)

All four web-app pages (453, 527, 1023, 239) have FAQs + descriptions that assume **used-only scope**:

- "CarClever Lite is a free AI tool... that evaluates **used cars**"
- "VIN Check... decodes any vehicle VIN to reveal specs... calculate a risk gate"
- "Deal Score is an AI-powered rating system... that evaluates **used car deals**"
- "Price Check is an AI-powered tool... for **used car listings**"

**Conflict:** These web apps are currently used-only, but when messaging pivots to new+used, these pages need review.

---

### 🟡 TRY-CARCLEVER PAGE (ID 38)

**Current status message:** "⚠️ App Status: Live on ChatGPT @CarClever"

**Issue:** References old CarClever app name (@CarClever). When Find My Car becomes the primary app, this messaging needs updated.

---

## CARCLEVER LITE INTEGRATION DETAIL

**URL:** `/carclever-lite/` (ID 239)

**Backend:** CarClever Lite calls the **old CarClever (Fractal) API**

**Scope:** Used cars only (inherits from backend)

**Features:** 
- Deal score (0-100)
- Risk assessment
- True cost of ownership calculation
- No sign-up required

**Current state:** Live and functional

**Future state unclear:** When CarClever Lite is updated to support new+used, it will need to call a new+used backend (either Sky/App #3 or Find My Car, or a rewrite)

---

## WEBSITE STRUCTURE MAP

```
getcarwise.app/
├── / (homepage — ID 7) — "used cars only" messaging
├── /try-carclever/ (ID 38) — AI assistant landing
├── /carclever-lite/ (ID 239) — WEB APP: free evaluation tool
├── /tools/ (ID 452) — WEB APPS HUB
│   ├── /vin-check/ (ID 1023) — WEB APP: VIN decoder + risk
│   ├── /deal-score/ (ID 453) — WEB APP: AI deal evaluation
│   ├── /price-check/ (ID 527) — WEB APP: AI pricing
│   └── /[30+ vehicle profiles & buying guides]
├── /data-guides/ (ID 899) — Buying guides hub
├── /blog/ (ID 300) — Blog hub
│   └── [30+ blog posts including new vs used topics]
├── /carclever-guide/ (ID 1053) — Generic user guide (Anthropic)
├── /carclever-find-my-car/ (ID 1071) — Find My Car MCP guide (Anthropic)
├── /about-getcarwise-our-story/ (ID 68) — Methodology
├── /contact-us/ (ID 64) — Support
├── /terms-of-service/ (ID 33) — Legal
├── /privacy-policy/ (ID 3) — Legal
└── /opt-out-preferences/ (ID 115) — Compliance
```

---

## MCP APPS REFERENCE ON WEBSITE

**Try CarClever page (ID 38):**
- Links to ChatGPT: `@CarClever` (old app name, Fractal original)
- Links to Claude: Not explicitly clear which app (likely old CarClever or Find My Car)

**Carclever-Find-My-Car page (ID 1071):**
- Documents the new Find My Car app specifically
- Shows it's available on Claude + ChatGPT

**Carclever-Guide page (ID 1053):**
- Generic guide, doesn't name specific app, assistant-agnostic

**Issue:** The website doesn't clearly distinguish between:
- Old CarClever (Fractal, used-only, on ChatGPT)
- Sky/App #3 (Fractal, new+used, in Anthropic review)
- Find My Car (Vercel, new+used, in OpenAI+Anthropic review)

---

## WHAT NEEDS ALIGNMENT FOR PRIORITY #3

### Investigation Phase (No implementation yet)

**Scope clarifications needed:**

1. **Homepage messaging:** 
   - Current: "The Only Independent AI Evaluating Used Cars"
   - Future: Update to new+used when Find My Car goes live? Or keep used-only until confirmed?
   - Decision: André's preference stated as "prefer no change" to homepage (per TASKS.md)

2. **Web apps scope:**
   - Deal Score, Price Check: Update to new+used when backend changes? Or keep used-only?
   - CarClever Lite: Backend integration change required for new+used support
   - VIN Check: Already handles any VIN (new or used) — messaging just needs update

3. **Navigation/app clarity:**
   - How should users understand the relationship between old CarClever, Sky/App #3, Find My Car?
   - Should website link to all three, or highlight Find My Car only?
   - When old CarClever reaches EOL, how is that communicated?

4. **Platform-availability wording:**
   - Current pages say "Live on ChatGPT"
   - Need strategy for "submitted", "in review", "coming soon" copy
   - Avoid public-facing status messages per André's constraint

5. **Try CarClever page:**
   - Currently says "Live on ChatGPT @CarClever" — old app name
   - Update when Find My Car approved?

6. **Blog/educational content:**
   - New vs used blog posts (IDs 1011, 993, 666) already exist and are good
   - Do they need more prominence in navigation?

7. **Affiliate disclosure reuse:**
   - Verify affiliate/Commission Junction disclosures are consistent across all pages
   - Carclever-find-my-car page and web app pages all route to Edmunds

---

## FILES CHECKED

| File | Lines | Content |
|------|-------|---------|
| STATE.md | 1024 | Session history, website check logged |
| DECISIONS.md | 4056 | Decision history, new vs used strategy documented |
| TASKS.md | 730 | Priority #3 scope (investigation only, no implementation) |
| REFERENCE.md | 256 | MCP endpoints, no website details |
| PLAYBOOK.md | 647 | SOPs, task index |

---

## NEXT STEPS (For Priority #3 Coordinated Website Review)

**Deliverable:** Executive Recommendation + 12 numbered sections → Proposed TODO list (awaiting André's approval before implementation)

**Estimated sections needed:**
1. Executive summary (current conflicts, strategic direction)
2. Homepage messaging strategy
3. Web apps (Lite, Deal Score, Price Check, VIN Check) scope + messaging
4. MCP app clarity (how website distinguishes old/Sky/Find My Car)
5. Try CarClever page update
6. Platform-availability wording strategy
7. Navigation/information architecture review
8. Blog/educational content prominence
9. Affiliate disclosure audit
10. New vs used positioning across all pages
11. Legal/compliance (terms, privacy — already reviewed, no changes)
12. Proposed TODO list with priorities

---

**Status:** ✅ Audit complete. Ready for Priority #3 planning session.

**Prepared by:** Claude (session Aug 26, 2026)  
**For:** Priority #3 Coordinated Website Review  
**Approval needed from:** André before any implementation
