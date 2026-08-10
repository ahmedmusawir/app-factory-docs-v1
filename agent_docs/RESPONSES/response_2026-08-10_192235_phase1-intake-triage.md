# Phase 1 — Intake & Recon: Cargo Triage (Gate 1)

> **Run:** Factory Module Doctrine promotion · **Date:** 2026-08-10 19:22 · **Skill:** factory-docs-update v0.3-DRAFT
> **Status:** PENDING_APPROVAL — Awaiting Operator APPROVED on scope

## Environment Discovery (EVIDENCE)

- At a Hub clone: `C:\_MY_PROJECTS\APP_FACTORY_DOCS\app-factory-docs-v1`, remote `ahmedmusawir/app-factory-docs-v1`. On `main`, pulled — already up to date.
- No `docs/*` branches local or remote — NO resume evidence. This is a fresh run, not a D15a resume.
- Housekeeping PR from the navbar-saga close-out is MERGED (commits a3613a9, b5112cc, 8df66e2, ff3cbd4 on main).
- GitHub MCP tools: PRESENT in this session (not needed on the primary route).
- MANIFEST.md read — dependency map in hand.
- Lessons file: none at repo root (GAP — not a blocker; the cargo pack is the lessons input).
- Skill v0.3-DRAFT read completely: CLAUDE.md, SKILL.md, README.md, ANTI_PATTERNS.md.

## Working-Tree Anomaly (QUESTION 1)

The skill folder was dropped in as `_SKILLS/factory-docs-update-skill/` (untracked, v0.3-DRAFT, timestamps today 12:16–12:18), while the committed `_SKILLS/factory-docs-update/` shows all 8 files DELETED (unstaged). But the skill's own docs (CLAUDE.md Home line, README activation lines) still say `_SKILLS/factory-docs-update/`.

**Options:** (a) RECOMMENDED — rename the folder back to `factory-docs-update` so disk matches doctrine; commit the v0.3 skill as housekeeping cargo in this run's close-out (same pattern as v0.2 last run). (b) Keep the `-skill` name — requires editing the skill's own docs, which is Skills-Playbook work, out of this skill's scope.

## Cargo Triage — `_INBOX/`, 7 files, per D16

| # | File | Class | Disposition |
|---|---|---|---|
| 1 | FINALIZATION_REPORT.md | PACK-manifest | Jarvis's finalization manifest for this drop — names each file's intended disposition. Not doctrine itself → `_AUDIT/` marked ENCODED at close-out (navbar-pack pattern) |
| 2 | BIM_PLAYBOOK.md (v1.0) | NEW DOC | No Hub counterpart → enters fresh at `03_BUILD_METHODOLOGY/` |
| 3 | FEAT_PLAYBOOK.md (v1.0) | NEW DOC | No Hub counterpart → enters fresh at `03_BUILD_METHODOLOGY/` |
| 4 | SFP_INSERT_KIT_MODULE_IDENTITY_QA_HANDOFF.md | PACK (insert kit) | Inserts "Module Identity & QA Handoff" section into live SOFTWARE_FACTORY_PLAYBOOK (v1.2 → v1.3) |
| 5 | QA_PLAYBOOK_v1.0_FIELD_TESTED.md | SUPERSEDING DOC | Hub counterpart: `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` at v0.1-DRAFT. Archive v0.1, land wholesale as canonical `QA_PLAYBOOK.md`. Version: cargo claims 1.0; live is 0.1; forward-consistent (its own history table carries the 0.1 row) — adopting 1.0, flagged per D16 |
| 6 | QA_PLAYBOOK_AC_SYNC_PATCH.md | PACK (patch) | 4 surgical items applied to QA_PLAYBOOK AFTER the supersession lands (see QUESTION 3) |
| 7 | BUG_FIX_PLAYBOOK_v1_0_AMENDMENTS.md | PACK (merge kit) | Targets live `BUG_FIX_PLAYBOOK.md` v0.1. Jarvis marked it BLOCKED-ON-INPUT (v0.1 base absent in HIS session) — but the base IS on disk here. Blocker is resolved (see QUESTION 2) |

## GAP check (dangling references)

- BIM/FEAT/BUG_FIX-amendments all cite `SOFTWARE_FACTORY_PLAYBOOK.md › Module Identity & QA Handoff` — a section that does NOT exist in the live SFP yet. The SFP insert kit (#4) closes this gap **in the same run**. No dangling reference if all ride together.
- All other Pairs-with citations (FFM, TESTING, ENGINEER, ARCHITECT, RECON, QA, BUG_FIX, FEAT, BIM) resolve to live Hub docs or docs entering this run. No gaps.
- `APP_REGISTRY.md` — cited only as "proposed, pending Operator approval"; verified by Jarvis's grep (0 active references). Not entering this run. Parked as a separately-approvable proposal (FINALIZATION_REPORT item 3).

## Split candidates

None. All seven files target Hub doctrine. Zero cross-repo entries.

## Hub-law translations required (D15 — will flag each at execution)

- QA v1.0 cargo header is multi-line stacked → translate to single-line `> **Version:** X · **Date:** Y · **Status:** Z` (HEADER-PRESENCE lint; bit us in PR #8).
- Cargo status strings ("ACTIVE — Field-tested…", "ACTIVE — Factory doctrine") → normalize to Hub status vocabulary (verify convention against live docs at Phase 2).
- Versioned cargo filename `QA_PLAYBOOK_v1.0_FIELD_TESTED.md` → lands as canonical `QA_PLAYBOOK.md` (AP-9).

## Anti-patterns most relevant to this job's shape

- **AP-1** (bulk over MCP): ~6 docs + 3 archives + MANIFEST + CHANGELOG ≈ 15+ file writes — bulk-shaped; local git per standing ruling.
- **AP-9** (version suffixes leaking into live names): the QA cargo filename is exactly this trap.
- **AP-11** (cargo never asked about): the `_INBOX/` scan + this triage is the counter.

## Preliminary affected-docs list (Phase 2 confirms)

1. SOFTWARE_FACTORY_PLAYBOOK v1.2 → v1.3 (insert kit; ←4 in dependency map)
2. QA_PLAYBOOK v0.1 → v1.0 (supersede) [→ v1.1 if patch lands as its own bump — QUESTION 3]
3. BUG_FIX_PLAYBOOK v0.1 → v1.0 (seamless merge per kit §D)
4. BIM_PLAYBOOK — NEW at 03_BUILD_METHODOLOGY (v1.0)
5. FEAT_PLAYBOOK — NEW at 03_BUILD_METHODOLOGY (v1.0)
6. MANIFEST.md — rows for all five + new-doc Pairs-with entries
7. CHANGELOG.md — entries
8. `_ARCHIVE/`: SOFTWARE_FACTORY_PLAYBOOK_v1_2, QA_PLAYBOOK_v0_1, BUG_FIX_PLAYBOOK_v0_1

## QUESTIONS for the Operator

1. **Skill folder rename** — rename `factory-docs-update-skill/` back to `factory-docs-update/` (recommended, matches doctrine Home) and commit v0.3 as close-out housekeeping? Or keep the new name (requires skill-doc edits, separate Skills-Playbook task)?
2. **BUG_FIX seamless merge** — Jarvis's kit says merge amendments into one seamless v1.0 at finalization; he was blocked only because the v0.1 base wasn't in his tree. It's in mine. Execute the seamless merge THIS run (recommended)? Or park the kit?
3. **QA patch versioning** — land the v1.0 supersession and the AC-sync patch as TWO version bumps (v1.0 then v1.1, two commits, cleanest audit trail — recommended) or fold the patch into the v1.0 landing with a second history row?
4. **Scope** — all seven files this run (recommended — they're one interlocked doctrine drop; the SFP section gap only closes if they ride together)?

**⛔ Stop Gate 1 — Awaiting your APPROVED on scope.**
