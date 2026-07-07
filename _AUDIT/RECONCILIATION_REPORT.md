# RECONCILIATION REPORT: DOC STACK ↔ GITHUB REPO

> **Series:** Stark Industries App Factory — Full Doc Stack Audit (interlude)
> **Author:** Architect Jarvis
> **Date:** 2026-07-03
> **Trigger:** Tony's starter-kit v3 upgrade recollection + git status screenshot showing doc renames/modifications not reflected in the audit doc stack.
> **Method:** GitHub repo synced into project knowledge; per-doc version-history comparison, stack copy vs repo copy.

---

## Headline

Between 2026-06-25 and 2026-06-29 the repo ran the **Kit Perfection Campaign** (10 gates, branch `kit-hardening`; ★ all gates closed 06-29). **Gate 10 was a docs harvest** that version-bumped six factory docs repo-side. The audit doc stack was assembled from pre-campaign copies and never received these updates. Drift window: ~June 8 → June 29.

## Per-Doc Verdicts

| Doc | Stack Copy | Repo Truth | Verdict |
|---|---|---|---|
| UI-UX-BUILDING-MANUAL | File named `v1_4`; **header says v1.2** (June 2) | `agent_docs/APP_FACTORY/UI-UX-BUILDING-MANUAL_v1_3.md` — **v1.3** (June 28): ThemeToggler→ThemeToggle sweep, orphan refs dropped, demo examples re-pointed, `next/head` → App Router metadata API | 🔴 STALE **and MISNAMED** — stack "v1_4" is v1.2 content; no v1.4 exists anywhere. Resolves F-006. |
| FRONTEND_FIRST_PLAYBOOK | v1.1.1 (June 2) | `agent_docs/APP_FACTORY/FRONTEND_FIRST_PLAYBOOK_v1.1.2.md` — **v1.1.2** (June 28): §12 reference example re-pointed from deleted `/demo` to live `(admin)/admin-portal` pair | 🔴 STALE |
| AUTH_MANUAL | v1.1 | **v1.2** per Gate 10 ledger | 🔴 STALE (bonus find — not in git status screenshot) |
| APP_ARCHITECTURE_MANUAL | v1.1 | **v1.2** per Gate 10 ledger | 🔴 STALE (bonus find) |
| COMPONENT_REGISTRY | v1.0 | **v1.1** per Gate 10 ledger (drift fixed: AppShellPage/Sheet made real; ThemeToggler renamed) | 🔴 STALE (bonus find) |
| FRONTEND_BUILD_PHASE_PLAYBOOK | v1.2 | v1.2 (rename v1.1→v1.2 committed) | 🟢 ALIGNED (spot-check pending) |
| STARTER_KIT_HANDBOOK | v1.1 (June 8, v3 reconciliation) | Matching v1.1 copy found at `_SKILLS/starter-kit-cleaner-skill/references/`; Gate 10 ledger mentions handbook harvest (`4dd8151`) | 🟡 VERIFY — content matches, but confirm canonical repo location + whether Gate 10 produced a post-June-8 revision |

## Findings Resolved by This Reconciliation

- **F-006 SOLVED:** stack `v1_4` byte-twin mystery = rename without content change; real content is v1.2; current truth is repo v1.3.
- **F-013b RESOLVED:** canonical theme toggle name is **`ThemeToggle`** — decided and shipped at Gate 10 (stale-debt purge, 06-28). No longer an open operator decision.
- **F-013a LIKELY RESOLVED:** starter-kit-cleaner skill notes role colors "pre-baked on defaults: `--role-*` tokens." Tony to confirm, then close.

## New Discoveries

1. **DOCTRINE_SYNC_MANIFEST exists in the repo**, and the Gate 10 backlog explicitly lists "canonical doctrine repo + skill-management design sessions." The central-delivery-system endgame was already on the factory's own backlog. The manifest is required reading for that design session.
2. **`_SKILLS/` ecosystem** in repo (starter-kit-cleaner, stark-repo-security, etc.) — a doc family not represented in the audit stack. Scope decision needed: are skills' CLAUDE.md files part of the 27-doc audit or a separate track?
3. **Session logs as doctrine history** (`session_2026-06-25.md` etc.) — the Gate ledger is where doc-bump truth lives. The MANIFEST design should treat session logs / commit ledger as the authoritative change feed.
4. LESSONS_BIN harvested at Gate 10 — likely related to the F-014 `STARTER_KIT_FEEDBACK.md` question.

## Root-Cause Note (for the delivery system)

This drift happened exactly as theorized: docs evolved **repo-side during a campaign** while the distribution copy (this project's stack) froze. No manifest = no diff = no alarm. The fix list already filed (MANIFEST, dependency map, canonical names, committed-or-it-doesn't-exist rule) addresses every mechanism observed here.

## Action Plan

1. **Tony:** refresh 5 stack docs from repo — UI-UX v1.3 (delete the misnamed `v1_4`), FRONTEND_FIRST v1.1.2, AUTH_MANUAL v1.2, APP_ARCHITECTURE v1.2, COMPONENT_REGISTRY v1.1.
2. **Tony:** confirm F-013a (role tokens) so it can be closed alongside F-013b.
3. **Jarvis:** verify STARTER_KIT_HANDBOOK canonical repo copy; spot-check FRONTEND_BUILD_PHASE v1.2 stack-vs-repo.
4. **Jarvis:** read DOCTRINE_SYNC_MANIFEST before the delivery-system design session.
5. **Resume audit** at ARCHITECT_QUESTIONNAIRE (Review 005) on verified-current docs.

## Impact on Completed Reviews

- REVIEW_001 (Blueprint), REVIEW_002 (SFP), REVIEW_004 (Architect Playbook): **unaffected** — no Gate 10 bumps observed for these docs.
- REVIEW_003 (Starter Kit Handbook): **provisionally unaffected**, pending the canonical-location check.

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
