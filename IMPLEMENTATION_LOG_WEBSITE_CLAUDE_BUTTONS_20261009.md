# IMPLEMENTATION LOG — “Find My Car on Claude” buttons on the GetCarWise website

Date: Oct 9, 2026 (Brisbane). Lane: Claude, Engineering. Approved by André in chat (task relayed from ChatGPT). Status: **pages DONE and verified**; GA4/MonsterInsights click capture NOT tested; four protected pages deliberately NOT edited (decision pending).

## 1. Scope and the instruction that overrides the audit
Add the Claude directory listing beside every existing NEW Find My Car ChatGPT button (app ID `6a85781882508191b1794888c5bbf728`), keep the existing description once beneath the pair, add Claude setup to `/carclever-find-my-car/`, and use paired buttons on pages without one only where a vehicle-search CTA fits. **André and ChatGPT revised the audit: the blanket removal of old CarClever links is superseded.** OLD app buttons (`698c1e794a3481918fad0affa7757784`) and their toolkit descriptions were preserved; no Claude button was placed in an old-app group. Deployments, MCP addresses, subscriptions, Edmunds links, Shared IDs, embeds, calculators and page URLs were not changed. The Claude launch blog stays a draft; the Anthropic email stays parked.

## 2. Reads before editing
Read in full: `AUDIT_CARCLEVER_WEBSITE_DIRECTORY_LINKS_AND_CLAUDE_LAUNCH_20261009.md`, the Claude handoff, STATE/TASKS/DECISIONS/PLAYBOOK (fresh, after the second STATE archive). Fresh AUTHENTICATED read of the raw editor source of all 59 pages/posts (49 + 10, all published) plus 12 templates, 4 template parts, 6 navigation menus, 5 widgets and 0 reusable blocks. Result matched the audit exactly: NEW-app anchors on 31 sources (34 anchors; 33 `/plugins/…` and 1 `/apps/…` shape), OLD-app anchors 32, no claude.ai link anywhere. No template, template part or widget contains either app link; the sidebar menu (navigation “Menu”) contains an OLD-app item “@CarClever on ChatGPT”, left unchanged. The live header (Blog, Tools, Data & Guides, …) links correctly (an earlier worry from the stored menu data was a misread).

## 3. Claude listing URL (checked in André’s Chrome)
`https://claude.ai/directory/carclever-find-my-car` loads the listing (title “CarClever - Find My Car”, Community badge, “Sign-in: Not required”, tools `find_matching_vehicle` and `resolve_dealer_url`, connector URL, Documentation/Support/Privacy links). `https://claude.ai/directory/connectors/carclever-find-my-car` redirects to it. A made-up slug shows “This connector doesn’t exist or is no longer available”. **Used on the site: the short URL.** NOT verifiable: the logged-out view (the browser session was André’s) and the Connect button label for non-owners (André’s view shows “Connected by default”). Current Claude path verified in the interface: **Customize → Connectors**, tabs Yours / Discover, button Add.

## 4. Method and safeguards
Authenticated WordPress REST (the admin application password from the project instructions), one page at a time: fresh read, abort if the page changed since my read, POST only `content`, read back and compare byte for byte, confirm the rendered output holds the Claude link(s). Backup of the original raw source of every edited page: `getcarwise_pages_backup_before_claude_buttons_20261009.zip` (given to André in chat; not committed to GitHub because of its size). The first bulk run hit the 300-second command limit after 30 pages; a state check then showed every page was either exactly the old or exactly the new content (no partial writes, no concurrent edits by anyone else) and the remaining seven were applied. Page 1071 was saved twice (content, then image sizing).

## 5. Copy and design used
- Button: “Find My Car on Claude”, same inline style as the page’s own ChatGPT button (blue pill; white variant in the dark CTA boxes of five posts; the homepage hero style with its hover script), same new-tab behaviour (the site adds `target="_blank" rel="noopener"` to all external links), plus `margin: 8px 0 0 8px` so wrapped buttons separate.
- Description kept once beneath each pair: “New or Used – Find My Car. Search it all. Find your perfect match.”
- New module on pages without a link (829, 935, 936, 937, 938, 1160): heading “Find matching cars in the assistant you already use”, the two buttons, the description, then small print: budget/ZIP prompt, Edmunds affiliate disclosure (“Vehicle links open on Edmunds via affiliate links; CarClever may earn a commission, and results are not ranked by commission.”), no separate CarClever account but ChatGPT or Claude account and platform access still apply, link to the guide.
- `/carclever-find-my-car/` section “Connect in Claude”: three steps (open the listing or Customize → Connectors → Discover; review and connect; ask Claude with budget and ZIP), example “Use CarClever – Find My Car to find a Honda CR-V under $30,000 near 90210.” (a prompt, not a promise of inventory), a Community-connector note (Anthropic: automatically reviewed, not verified), account/plan/administrator note, “results may look different between Claude and ChatGPT”, and the affiliate disclosure. Only features visible in the live listing and tool list are described.

## 6. Pages changed (37 of 59)
Rollback revision = the WordPress revision saved just before my first edit (restore it in the page’s Revisions panel).

| WP ID | Type | Title | Path | Change | Rollback revision |
|---|---|---|---|---|---|
| 7 | page | Car Research &amp; Deal Scoring | / | homepage hero + second group paired | 1366 |
| 452 | page | Car Research Tools - AI-Powered Evaluation | /tools/ | two groups paired; old @CarClever group untouched | 1470 |
| 738 | page | 2023 Honda CR-V: Reliable Compact SUV for Growing Families | /tools/2023-honda-crv-reliable-compact-suv/ | Claude button beside the ChatGPT button | 1460 |
| 739 | page | 2022 Nissan Altima: Fuel-Efficient Midsize Sedan with Strong R | /tools/2022-nissan-altima-fuel-efficient-sedan/ | Claude button beside the ChatGPT button | 1457 |
| 740 | page | 2022 Toyota Camry: Mid-Size Reliability Champion with Proven L | /tools/2022-toyota-camry-reliable-midsize-sedan/ | Claude button beside the ChatGPT button | 1458 |
| 741 | page | 2021 Ford F-150: America's Most Popular Truck with Modern Tech | /tools/2021-ford-f150-popular-pickup-truck/ | Claude button beside the ChatGPT button | 1452 |
| 742 | page | 2021 Honda Civic: Efficient Compact Car with Engaging Driving  | /tools/2021-honda-civic-efficient-compact-car/ | Claude button beside the ChatGPT button | 1453 |
| 749 | page | 2020 Toyota RAV4: Dependable SUV with Strong Resale Value | /tools/2020-toyota-rav4-dependable-suv-resale/ | Claude button beside the ChatGPT button | 1450 |
| 750 | page | 2023 Honda Accord Gas Mileage | /tools/2023-honda-accord-fuel-efficient-sedan-comfort/ | Claude button beside the ChatGPT button | 1459 |
| 751 | page | 2022 Chevrolet Silverado: Heavy-Duty Workhorse Truck for Deman | /tools/2022-chevrolet-silverado-heavy-duty-truck/ | Claude button beside the ChatGPT button | 1455 |
| 752 | page | 2021 Mazda CX-5: Stylish Compact SUV with Smooth Driving Exper | /tools/2021-mazda-cx5-stylish-compact-suv/ | Claude button beside the ChatGPT button | 1454 |
| 753 | page | 2023 Subaru Outback: Adventure-Ready Crossover with All-Wheel  | /tools/2023-subaru-outback-adventure-crossover-awd/ | Claude button beside the ChatGPT button | 1463 |
| 754 | page | 2023 Toyota Highlander: Three-Row Family SUV with Proven Relia | /tools/2023-toyota-highlander-three-row-family-suv/ | Claude button beside the ChatGPT button | 1464 |
| 755 | page | 2020 Chevrolet Equinox: Affordable Compact SUV for Budget Buye | /tools/2020-chevrolet-equinox-affordable-compact-suv/ | Claude button beside the ChatGPT button | 1449 |
| 756 | page | 2022 Honda CR-V: Versatile Compact SUV with Spacious Interior | /tools/2022-honda-crv-versatile-compact-suv-spacious/ | Claude button beside the ChatGPT button | 1456 |
| 757 | page | 2021 Ford Escape: Agile Compact SUV with Modern Tech | /tools/2021-ford-escape-agile-compact-suv-modern-tech/ | Claude button beside the ChatGPT button | 1451 |
| 758 | page | 2023 Kia Sportage: Korean Compact SUV with Premium Features | /tools/2023-kia-sportage-korean-compact-suv-premium/ | Claude button beside the ChatGPT button | 1462 |
| 769 | page | 2023 Hyundai Tucson: Korean Compact SUV with Strong Warranty C | /tools/2023-hyundai-tucson-korean-compact-suv-warranty/ | Claude button beside the ChatGPT button | 1461 |
| 771 | page | Best Compact SUV Under $25K: CR-V vs RAV4 vs Tucson vs CX-5 vs | /tools/best-compact-suv-under-25k-comparison/ | edit invisible: public URL 301-redirects to /tools/best-compact-suv-under-25000/ (pre-existing Rank Math redirect) | 1348 |
| 772 | page | Best Midsize Sedan Under $30K: Accord vs Camry vs Altima Compa | /tools/best-midsize-sedan-under-30k-comparison/ | Claude button beside the ChatGPT button | 1347 |
| 773 | page | Best Full-Size Truck for Towing: F-150 vs Silverado Head-to-He | /tools/best-full-size-truck-towing-f150-silverado/ | Claude button beside the ChatGPT button | 1346 |
| 774 | page | Vehicles Comparable to Toyota Highlander | /tools/best-3-row-suv-families-highlander/ | Claude button beside the ChatGPT button | 1345 |
| 829 | page | Best Full-Size Truck Under $35,000: F-150 vs Silverado vs Ram | /tools/best-full-size-truck-under-35000/ | new paired module | 1191 |
| 899 | page | Data & Guides | /data-guides/ | list item: label 'Find My Car' -> 'Find My Car on ChatGPT', Claude link added | 1368 |
| 935 | page | Best Sedans Under $15,000 (2026): Reliable Picks Ranked | /tools/best-sedan-under-15000/ | new paired module | 1467 |
| 936 | page | Best Hybrid SUVs Under $20,000 (2026): Value & Efficiency | /tools/best-hybrid-suv-under-20000/ | new paired module | 1465 |
| 937 | page | Best Used Plug-In Hybrids in 2026: Which PHEV Fits You? | /tools/best-used-phev-plug-in-hybrid/ | new paired module | 1501 |
| 938 | page | Best Used Electric Cars (EV) 2026: Top Value Picks | /tools/best-used-electric-car-ev/ | new paired module | 1466 |
| 1071 | page | CarClever - Find My Car | /carclever-find-my-car/ | button pair + new 'Connect in Claude' section; 'or Muse' removed; 4 screenshots made responsive (two saves) | 1325 |
| 1160 | page | CarClever Decision Center | /carclever-decision-center/ | new paired module | 1502 |
| 309 | post | How to Read a Used Car Listing: 5 Red Flags | /how-to-read-a-used-car-listing-5-red-flags-that-cost-buyers-5000/ | Claude button beside the ChatGPT button | 1474 |
| 412 | post | The CarClever Deal Score Explained | /the-carclever-deal-score-explained/ | Claude button beside the ChatGPT button | 1485 |
| 513 | post | True Cost of Ownership Explained | /true-cost-of-ownership-explained/ | Claude button beside the ChatGPT button | 1486 |
| 666 | post | Used vs. New: The Depreciation Cliff & 0% APR Trap | /used-vs-new-depreciation-cliff-apr-trap-2/ | Claude button beside the ChatGPT button | 1414 |
| 1008 | post | Used Car Title Brands: Salvage, Rebuilt & Flood - What Buyers  | /used-car-title-brands-salvage-rebuilt-flood/ | Claude button beside the ChatGPT button | 1410 |
| 1011 | post | New vs Used: The Financial Math — Why Total Cost Matters More  | /new-vs-used-financial-math/ | Claude button beside the ChatGPT button | 1409 |
| 1469 | post | Best AI Tools for Buying a Used Car in 2026 | /best-ai-tools-for-buying-a-used-car-2026/ | two prose links; 'identifies' -> 'identify' | none: this post had no earlier revision (my save created its first); restore from the backup zip |

## 7. Deliberately NOT changed (22)
- **Protected Task #78 cohort — 827, 828, 830, 934:** Sep 28 hold and the Oct 7 handoff say never to edit them during the observation window; 934 is also the planned Google test landing page. ChatGPT’s audit proposed a block here; held for André’s explicit decision. Adding one would be a documented intervention.
- **Old-toolkit pages 38 and 1053, historical launch post 952:** old-app buttons and descriptions preserved; no Claude button added beside the old app; history not rewritten. (The audit’s edits to their text were superseded.)
- **Specialist and tool pages 239, 453, 527, 539, 540, 541, 1023,** legal/contact/opt-out/blog index/about pages (3, 33, 64, 115, 300, 68), posts 809 and 993: no search CTA fits naturally or the page is a protected specialist route.

## 8. Verification
- Stored source of all 59 pages equals the intended content; all still published. OLD-app anchors 32 → 32 identical; NEW-app anchors 34 → 40 (+6 from the new modules); claude.ai links 41; Edmunds affiliate links 88 identical; iframes 17/17; scripts 23/23; no Claude button follows an old-app button.
- Public (logged-out) fetch of every changed page: 36 of 37 show the Claude link; 771 is invisible because of the redirect above.
- Layout in a real 1280px and 390px frame on 13 pages (model guide, main guide, homepage, Tools, Data & Guides, sedan and truck and PHEV and hybrid guides, red-flags post, AI-tools post, Decision Center): desktop pair on one row (gap 11–13px); phone buttons stack and stay in view; same colours as the ChatGPT button; description directly beneath; no new horizontal overflow. A screenshot of the 2023 CR-V guide confirmed it visually.

## 9. Unresolved issues and assumptions
1. Page 937 (PHEV guide): its existing 427px comparison table overflows on phones (pre-existing; no wrapper).
2. Page 1071 still says “3.3+ million active U.S. listings” (twice): unverified, left unchanged; ChatGPT’s guidance is to avoid a millions claim unless freshly sourced.
3. I removed “or Muse” from 1071’s How-to-Use sentence because Muse availability is unverified; revert if André wants it back.
4. 899: label change “Find My Car” → “Find My Car on ChatGPT”; 1469: “identifies” → “identify”.
5. Page 771 is a redirected duplicate of 934’s URL.
6. Not tested: GA4/MonsterInsights outbound-click capture (no test clicks made); the logged-out Claude listing view; the non-owner Connect button wording.
7. The audit’s other items (launch blog, measurement plan) are unchanged and out of this task.

## 10. Method notes
The browser (Claude in Chrome) was used only to verify the listing and layout; edits went through REST. This log was written with the GitHub PAT because it is a long generated table (documented fallback); it contains no credentials.
