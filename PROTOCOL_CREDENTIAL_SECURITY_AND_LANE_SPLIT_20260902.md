# Credential Security & Lane-Split Protocol — Sep 2, 2026

**Status:** Implemented same session. Cross-referenced in `carclever-widget` STATE.md,
TASKS.md, DECISIONS.md, WORKFLOW_ARCHITECTURE.md, TOOL_STACK_REFERENCE.md.

---

## What triggered this

A GitHub PAT with full account access (`carclever-automation`) had been exposed multiple
times in Claude chat transcripts across this and prior sessions — both directly in prose
and repeated in visible bash command output. André asked to rotate it and restrict scope
going forward, then separately asked whether ChatGPT (currently read-only on GitHub) could
get its own write access so strategy decisions (like the Auto.dev renewal call) don't need
manual relay through Claude every time.

## What was done

### 1. Claude's GitHub PAT rotated and scoped down
- Old token: full account access, no expiry set, exposed multiple times — pending revoke.
- New token: `claude-carclever-restricted`, fine-grained, exactly 3 repos
  (`carclever-widget`, `carclever-find-my-car`, `getcarwise-docs`), Contents + Pull
  requests Read/write only. **Expires Nov 30, 2026.**
- Verified with a real write test (create + delete a test file) before trusting it, not
  just a read-only check.
- Cross-checked for other places the old token might be referenced before revoking:
  GitHub Actions (both repos — none), Vercel env vars (all 3 projects, all environments,
  team-wide shared — none), Fractal env vars (both projects, both environments — none),
  Drive-wide search for the literal token value (zero hits). Confirmed the token exists
  in exactly one place: the Drive secrets doc.

### 2. ChatGPT given its own repo-scoped write token (separate task, in progress)
- New PAT, scoped to `carclever-widget` ONLY, Contents Read/write.
- Stored in a separate Drive doc (`SECRETS_CHATGPT_GITHUB_WIDGET_PAT_PRIVATE`) from
  Claude's token, so a leak of one doesn't compromise the other.
- Deliberately NOT given access to `carclever-find-my-car` (the actual application code)
  — enforced structurally via GitHub's fine-grained repo selection, not a rule either AI
  has to remember to follow.
- `WORKFLOW_ARCHITECTURE.md` §2a updated with the full reasoning and a standing
  cross-check rule: both AIs make mistakes (confirmed twice same session — a stale Reddit
  row ChatGPT presented as current, and this PAT exposure on Claude's side), so direct
  write access doesn't remove the need to spot-check the other AI's recent commits at the
  start of a session.

### 3. Real transcript-exposure limitation acknowledged, not glossed over
Every credential Claude uses via bash/tool calls appears in the visible transcript — no
channel exists to use a secret without it passing through something readable. Scoping and
short expiry limit blast radius; they don't eliminate the exposure. Two real fixes
identified, not yet built/set up:
- **Near-term:** Claude's first-party GitHub Integration connector (Settings → Connectors
  → GitHub, OAuth-based, same model as existing Drive/Gmail connectors) — credential would
  live in Anthropic's infrastructure, never in a transcript. Known risk: real bug reports
  (Jul 2026) of this connector failing writes with 403 errors even when authorized —
  needs testing before being trusted, not assumed to work. Logged as `TASKS.md` #55.
- **Fallback if the connector proves unreliable:** a Vercel serverless function holding
  the credential server-side, called with just content (never the token). Not built.

### 4. `getcarwise-docs` repo gap discovered and partially fixed
This repo — designed Aug 26 as persistent storage for session documentation, meant to be
fetched at the start of every session alongside `carclever-widget` — was never actually
fetched by this session, or apparently any session since Aug 26. Root cause: the
session-launch instructions given to Claude at conversation start only listed
`carclever-widget` files; `getcarwise-docs` wasn't mentioned, even though `PLAYBOOK.md`
(inside `carclever-widget`) correctly specifies fetching both. The launch instructions
(which live outside GitHub, in Claude's own project/session configuration) are stale
relative to `PLAYBOOK.md` and need updating by André — Claude cannot edit its own launch
instructions from inside a session.

Also found and fixed: `SESSION_END_PROTOCOL_V2.md` (in `carclever-widget`) had the OLD,
now-rotated GitHub PAT hardcoded in plaintext, committed to git history — a second,
independent exposure predating today's session, unrelated to the chat-transcript issue.
Fixed to reference fetching fresh from the Drive doc instead, matching the discipline
`REFERENCE.md` already uses.

## What's still open

- André has not yet revoked the old broad-access PAT — held open deliberately until
  ChatGPT's separate token is also fully set up and verified.
- ChatGPT's `carclever-widget`-only PAT: not yet created.
- `TASKS.md` #55 (GitHub connector investigation) not yet started.
- The launch-instructions gap (this repo not being fetched) needs a permanent fix by
  André outside GitHub — Claude can only flag it, not correct it directly.
- Old git history in `SESSION_END_PROTOCOL_V2.md` still technically contains the exposed
  PAT in past commits even after this fix — moot once that token is revoked, but worth
  knowing git history isn't retroactively clean.
