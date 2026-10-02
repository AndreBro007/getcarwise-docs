# CarClever OpenAI submission ZIP guide

Verified 2 October 2026, Australia/Brisbane. This guide records the workflow that successfully uploaded old CarClever's corrected package 3.0.1 and placed it in review. Approval is pending.

## Keep the two apps and numbering separate

| App | Stable package name | Current package state | Application state |
|---|---|---|---|
| Old CarClever | app-698c1e794a3481918fad0affa7757784 | 2.0.0 published; 3.0.0 rejected; 3.0.1 in review | Hosted Fractal code 3.0.0 already deployed; Recommended sort live |
| CarClever – Find My Car | app-6a85781882508191b1794888c5bbf728 | Exported/published package 1.0.0 | Application V2 approved/live; application V3 paused and unsubmitted |

Package versions label the uploaded listing/assets bundle. They need not equal hosted application releases. Start each app's update from its own export; never replace its stable name or copy the other app's listing blindly.

## What the ZIP contains

Both original downloaded exports contained only `.codex-plugin/plugin.json`. They did not contain icons, tool descriptions, annotations, MCP configuration or review materials. They are not complete application backups.

The final old-app package contains:

- `.codex-plugin/plugin.json` — identity, author, version, listing fields, links, starter prompts and release notes.
- `assets/carclever-icon.png` — André's blue square CC icon, unchanged 128 × 128 PNG.

The compatibility manifest uses root `interface.logo` and `interface.composerIcon`, both `./assets/carclever-icon.png`. Paths resolve from the plugin root, NOT from the `.codex-plugin` directory. Include actual image bytes in the ZIP. A hosted WordPress URL is not needed for these fields.

For a new portable package, use root `plugin.json`, its listing fields under `extensions.com.openai.interface`, and remote server configuration in `mcp.json`. The Python helper supports a root portable manifest or the existing compatibility manifest, but is an existing-package rebuilder, not a complete new-app generator. Mixed manifest layouts require manual review because OpenAI does not merge their settings.

## Build on Windows or another Python 3 environment

Extract this toolkit into a folder. No pip packages or API keys are required.

1. Keep the original release ZIP unchanged. Download the published release from the existing app's … → Download release ZIP, or use your maintained complete package. Include all components you intend to retain.
2. Decide the next package version. For a future old-app release after 3.0.1, 3.0.2 is a possible patch number. Use the appropriate next package version for Find My Car independently.
3. Optionally edit a listing override JSON containing only `interface` fields to change. The included `old-carclever-listing.json` is an OLD-app example; it is not a Find My Car template.
4. Supply the square icon. Reuse `assets/carclever-icon.png`, or use your approved higher-resolution square PNG.
5. Run the builder. Example for a future OLD-app package:

```powershell
py build_submission.py submitted-old-carclever-3.0.1.zip --version 3.0.2 --icon assets/carclever-icon.png --output old-carclever-3.0.2.zip
```

To add approved listing changes and release notes:

```powershell
py build_submission.py submitted-old-carclever-3.0.1.zip --version 3.0.2 --listing-json old-carclever-listing.json --icon assets/carclever-icon.png --release-notes release-notes.txt --output old-carclever-3.0.2.zip
```

To correct an unsubmitted 3.0.2 draft without changing its number:

```powershell
py build_submission.py old-carclever-3.0.2.zip --version 3.0.2 --correct-draft --icon assets/carclever-icon.png --output old-carclever-3.0.2-corrected.zip
```

`--correct-draft` permits the local build; it does not guarantee that OpenAI will overwrite a rejected or published release. Documentation does not explicitly promise rejected same-version replacement. In this session we used 3.0.1 after rejected 3.0.0; subsequent 3.0.1 ZIP uploads corrected the unsubmitted draft successfully. Do not upload changes while this review is active unless you cancel it deliberately or wait for its outcome.

Use `python3` instead of `py` on macOS/Linux. Run `py build_submission.py --help` for options. The output is a complete ZIP, not a patch. Source components are preserved. Hosted tools/code are not downloaded or modified. Omit override arguments to retain existing listing/release notes.

## Validation and submission

1. Open the EXISTING intended CarClever entry, not a new app entry.
2. Upload the generated submission ZIP, not the outer toolkit ZIP.
3. In Metadata & Skills, verify version, display name, square icon, four URLs, publisher and listing text. Wait for automated results. Resolve required issues through another complete ZIP upload.
4. In MCPs, verify the attached endpoint, authentication/domain state, tool availability and scan. For deployed server changes, Rescan checks the hosted definitions separately.
5. Check Review information → Review details: relevant test cases, demo recording, release notes, commerce/countries and reviewer access. Exports may omit these; do not assume absence in ZIP means absence in the dashboard. In our old-app draft the existing MCP stayed Configured; this is an observation, not a universal retention guarantee.
6. Submit for review and have the owner complete accurate declarations. André submitted 3.0.1 on 2 October; screenshot confirms In review.
7. Once approved, select the approved package and Publish plugin. In review is not published; 2.0.0 remains the published package until an approved update is published.

Only one review may be active per plugin. After rejection, address feedback and submit a corrected ZIP. Hosted compatible tool updates use MCP scans and can become live without a separate package upload. Cached connector descriptions in a chat are not proof of the current server definition; inspect Live definition / Held update in the portal.

## Requirements checked against official documentation

- Stable identity and semantic package version; compatible manifest at plugin root.
- Listing display name/subtitle ≤30 characters each; long description ≤4,000; developer name ≤80; at most three distinct starter prompts ≤128 characters each and no app @mentions.
- MCP listing website/support/privacy/terms URLs: public HTTPS, ≤1,024 characters, correct publisher.
- Icon paths begin `./`; reference bundled files. PNG/JPEG/WebP/SVG supported by OpenAI, ≤5 MiB each; square ≥48 × 48 and raster dimensions ≤4096. The helper deliberately accepts PNG only and checks its dimensions/header. Our 128 × 128 square icon passed actual portal validation. Prefer a higher-resolution original if available; a circular drawing on a square canvas also meets dimensional rules, but André selected blue square branding.
- Include logo and composerIcon for compatibility packages. Dark variants/screenshots optional; screenshots depend on scanned UI support.
- Initial MCP review: five positive and three negative cases, video walkthrough, release notes, production endpoint/domain verification/current scan and owner attestations. Check applicable requirements on the actual update screen.
- Explicit accurate readOnlyHint, openWorldHint and destructiveHint on each tool. Tool identifiers/descriptions must be factual, clear and explain when to use the tool without promotional comparisons or priority instructions.
- Annotation-justification wording differs across current guidelines, rejection email and submission-error reference. Retain factual justifications wherever the dashboard/reviewer requests them; do not infer a clean scan guarantees approval.
- No credentials in the ZIP. Reviewer access belongs in the secure dashboard fields. No unsupported app references or lifecycle hooks in a public-submission package.
- ZIP ≤100 MB compressed; regular files/directories only; no absolute paths, parent traversal, duplicate paths or enclosing-folder ambiguity. The helper checks core structure/asset presence and byte integrity, not every server, policy, review or portal rule.

## Session evidence and testing

Fractal reported small description changes removing priority/never-fails wording and AI-visible dealer_vdp_url suppression while preserving schemas, internal objects, Recommended sorting and affiliate resolution. Owner passed Fractal preview tests and deployed. Portal showed nine Live tools and clean scan.

Independent old-plugin calls: search returned six listings with dealer_vdp_url absent; comparison returned two with field absent; risk and affordability succeeded with no field. Garage save succeeded, populated garage-list returned dealer_vdp_url null, remove succeeded, final garage restored empty. get-vehicle-details and private resolve-dealer-url were not directly callable here; raw Fractal metadata access was HTTP 403-blocked. Do not claim independent all-nine-tool verification. No affiliate destination was clicked or lead submitted.

Initial 3.0.1 ZIP lacked icon and produced App icon required. Added bundled image plus logo/composerIcon; André selected the square design; updated draft showed No Issues, then was submitted. Final submitted ZIP is included for reference. No app code/deployment was performed by ChatGPT.

## Official sources read

- [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines) — tool descriptions, annotations and publication policy.
- [Upload and submit your plugin](https://developers.openai.com/plugins/deploy/submission) — package upload, correction, review/publish lifecycle, hosted MCP scans, manifest fields and icon requirements.
- [Package your plugin](https://developers.openai.com/plugins/build/plugins) — package formats and structure.
- [MCP review requirements](https://developers.openai.com/plugins/deploy/app-review) — review materials and MCP setup.
- [Submission error reference](https://developers.openai.com/plugins/deploy/submission-errors) — stricter final checks, missing icons, version and archive errors.

These are living documents. Recheck before a future submission. The tracked email Help Center link could not be resolved; no claim is made that its exact target was read.
