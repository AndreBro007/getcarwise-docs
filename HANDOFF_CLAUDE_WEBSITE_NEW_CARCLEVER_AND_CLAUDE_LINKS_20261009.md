# Claude handoff — website new CarClever defaults and Claude launch

Date: 9 October 2026 (Brisbane). Lane: ChatGPT strategy -> Claude website execution. Status: implementation READY TO REVIEW; website not changed by ChatGPT; launch article draft only. André asked ChatGPT to audit placement and prepare the complete Priority 3 website work. No need to re-ask generic permission for that requested scope. His possible blog announcement still requires a publication decision; create/review a draft before asking that decision. Keep V3/listing feedback, Auto.dev, Fractal and catalogue cutover decisions separate.

## 1. Read first
- AUDIT_CARCLEVER_WEBSITE_DIRECTORY_LINKS_AND_CLAUDE_LAUNCH_20261009.md (59-row live REST inventory, proposed actions/reasons, exact copy, measurement and limitations).
- DRAFT_CARCLEVER_FIND_MY_CAR_CLAUDE_LAUNCH_20261009.html and LAUNCH_CARCLEVER_CLAUDE_EDITORIAL_CHECKLIST_20261009.md.
- Fresh STATE.md/TASKS.md/DECISIONS.md/PLAYBOOK.md from carclever-widget before any shared write. STATE has a second archive now. ChatGPT did not change either lane's checkpoint.

## 2. Verified inventory / exact scope
All 49 published pages + 10 posts fetched via public REST, Oct 9. NEW app links: 31 pages/posts, 34 anchors. OLD app: 29 pages/posts, 32 anchors. Both: 26. No Claude directory body links. Full public inventory is in the audit.

Paired NEW Find My Car rollout on 42 EXISTING IDs: 7, 452, 738, 739, 740, 741, 742, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 769, 771, 772, 773, 774, 899, 1071, 309, 412, 513, 666, 1008, 1011, 1469, 827, 828, 829, 830, 934, 935, 936, 937, 938, 1160, 952.
Keep direct OLD app external directory links ONLY on 38 (/try-carclever/) and 1053 (/carclever-guide/). Remove the other 30 old anchors across 27 pages/posts, with context updates from the audit. Old launch 952 becomes dated history with an internal toolkit-page link and a separate current Find My Car pair; don't rewrite history as a new-app launch. Don't retire the old app or change its hosting.

The 42 existing IDs exclude the drafted new announcement. If it is later published, it adds one separately verified post.

## 3. URL gate: browser verification, not an indexing assumption
André supplied https://claude.ai/directory/carclever-find-my-car from the publish screen. Use that prepared URL, but first open it in a real normal browser and verify correct listing/Connect control, final address and logged-out behaviour. Earlier email/screenshot used /directory/connectors/carclever-find-my-car. Both direct automated calls got 403; that is NOT proof of missing listing/indexing. Record what the browser actually shows; normalise to an observed working public route. If unavailable, report and leave live links unchanged instead of publishing a broken destination. No directory discovery rank guarantees.

NEW ChatGPT identity: 6a85781882508191b1794888c5bbf728. OLD: 698c1e794a3481918fad0affa7757784. Match href identity across /apps/, /plugins/ and any actual canonical redirect. Preserve existing validated new links; don't blindly replace based on button labels.

## 4. Execution order
1. Main guide 1071: apply current intro, paired choices, setup/examples/disclosure. No fixed current listing-count claim, unverified Muse rollout claim, no separate-platform-account claim, guarantee of availability or duplicate Deal Score promise.
2. Homepage 7, Tools 452, Decision Center 1160, Data & Guides 899: make Find My Car the default conversational search route; remove duplicated old app promotions and old-toolkit assertions tied to the new CTA. Keep specialist calculators/direct Edmunds and an optional internal toolkit reference.
3. Sixteen model guides and four comparisons: paired new-app block; remove external old-app choice where present; preserve exact/model-specific Edmunds link, Shared IDs and independent guide content.
4. Nine guide gaps 827/828/829/830/934–938: add small paired block OUTSIDE the existing iframe. They currently have neither new nor old directory app anchor. No iframe migration, page 239 change, ranking/canonical/schema rewrite or experiment reset. Record an intervention on Task #78's protected cohort.
5. Six explainers 309/412/513/666/1008/1011, AI-tools post 1469 and historic launch 952: scope the CTA to new-app search, preserve historical examples and specialist tools. Keep the 1469 June-test/product distinction. Price-value Deal Score stays attributed to the calculator/toolkit, not Match Score.
6. Keep toolkit pages 38 and 1053: label old app as Used-Car Toolkit in ChatGPT; keep the worked example's original date. Correct stale cross-platform/Claude-directory instructions using an INTERNAL reference to the new-app guide, without pairing new Claude directory CTA with old app.
7. Blog announcement: create/review draft using supplied HTML and editorial checklist. Publish only once André approves that concrete draft. Link from the relevant entry pages and actual blog index after publication.

## 5. Safe WordPress update process
Use authenticated browser + cookie/nonce REST path already documented; retrieve content.raw/current modified timestamp fresh before each edit. Public content.rendered used for the audit is not an editable Gutenberg backup. Preserve raw blocks/media/classes/schema/affiliate URLs where not intentionally changed. Save rollback revision, preview before publishing, and re-fetch exact intended content after save. Refresh/close stale editor tabs and don't save one over a REST edit. SHA-guard fresh admin writes, preserve concurrent changes and verify re-fetch; no broad start-up re-audit required for this scoped task.

Do not use a global search/replace of 'CarClever', old ID or 'coming soon' without per-placement context. Authenticated navigation/template/widget coverage was not available to ChatGPT: scan those too, retaining no old-app direct promo outside the two documented pages unless explicitly reported/justified.

## 6. Measurement and functional verification
Inspect existing GA4/MonsterInsights outbound event settings; directory link clicks should be separable by source page, link URL/domain and product identity. data-* labels don't create analytics events on their own. Prefer existing capture and avoid double-firing. Confirm exactly one captured test click per platform; label test traffic. Do not create artificial Edmunds affiliate clicks or leads. Keep existing Shared IDs/disclosures. Don't pass personal chat data into affiliate tracking. Directory clicks != connections != useful buyer sessions != paid eligible Impact actions.

Representative desktop/mobile checks: 1071, homepage, Tools, Decision Center, one model guide, one of nine guide gaps, one explainer, 38/1053 and any new announcement. Both paired choices need meaningful hrefs, clear labels, keyboard focus, mobile wrapping and matching product descriptions. Old screenshots/results are not evidence of the new connector's UI.

## 7. Return required
Report WP IDs/URLs and exact changes made; before/after inventory counts; residual old-link locations; browser-observed Claude final URL; old-link replacement reasons; any shared global sources changed; copy corrections; which setup/examples/analytics were verified; screenshots/rollback references; blog draft/publish status. Explicitly mark incomplete checks. Fresh public re-scan should show old directory identity only on 38/1053 bodies, paired new links on the 42 intended existing IDs, and no changed iframe/backend/affiliate destination.

No Vercel app production branch/alias/environment change, no catalogue production deployment, no Fractal cancellation, no Meta announcement, no Anthropic email and no paid campaign are part of this website task.
