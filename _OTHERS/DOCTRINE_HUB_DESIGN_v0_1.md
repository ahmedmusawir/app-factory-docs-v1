# DOCTRINE HUB — CENTRAL DELIVERY SYSTEM DESIGN

> **Series:** Stark Industries App Factory — Full Doc Stack Audit (endgame design, pulled forward)
> **Author:** Architect Jarvis (organizing Tony's design input, 2026-07-04)
> **Status:** DRAFT v0.1 — awaiting Tony's approval on the two decisions below
> **Prior art:** Repo backlog item "canonical doctrine repo + skill-management design sessions"; `DOCTRINE_SYNC_MANIFEST` (propagation checklist to MissionControl/CP-v1); this audit's FINDINGS_LOG "Filed for Central Delivery System" items 1–12.

---

## 1. The Problem (evidence-backed)

Docs evolve inside project repos during runs (correct — that's where lessons happen), but distribution copies elsewhere silently freeze. Proven cases: the Kit Perfection Campaign bumped 6 docs repo-side while this audit's stack froze (F-019); MissionControl/CP-v1 need a manual sync manifest; the `v1_4` filename impostor (F-006). Root causes: no single canonical home, no manifest, versions in filenames, copies instead of pointers.

## 2. The System

### 2.1 One canonical repo: `app-factory-doctrine`
Docs only. No app code. Everything else in the ecosystem holds *copies of a tagged release* of this repo.

### 2.2 Structure (day one — five tiers from the audit)
```
app-factory-doctrine/
├── MANIFEST.md                  ← every doc: canonical name, version, date, status
├── CHANGELOG.md                 ← Gate-ledger style change feed (D-007 pattern)
├── 01_CONSTITUTION/             ← Blueprint, SFP, Starter Kit Handbook
├── 02_PIPELINE_AGENTS/          ← Architect/Designer/Engineer playbooks, questionnaires, handoff
├── 03_BUILD_METHODOLOGY/        ← FFM, Frontend-First, Build Phase, Testing, Skills playbook
├── 04_REFERENCE_MANUALS/        ← Auth, DB, API, State, Architecture, Ecommerce, Stripe
├── 05_DESIGN_SYSTEM/            ← GDSH, UI-UX Manual, Theming, Theme Library, Tokens, Component Registry
└── _ARCHIVE/                    ← superseded snapshots, versioned filenames allowed here
```

### 2.3 Naming + versioning rules
- **Live docs: canonical names, no version suffix** (`UI-UX-BUILDING-MANUAL.md`). Version + date live in a standardized top header block (F-018) and in MANIFEST.
- **Archive: versioned snapshots** (`_ARCHIVE/UI-UX-BUILDING-MANUAL_v1_2.md`) — Tony's visible-history requirement, satisfied without stale cross-references.
- **Cross-references always use canonical names** (F-011; model = STARTER_KIT_HANDBOOK §13).
- On every doc bump: copy old live file into `_ARCHIVE/` with its version suffix, update live file + header, update MANIFEST + CHANGELOG. (One future script; manual at first.)

### 2.4 The sync loop (one-directional circle)
- **Hub → Project (at project start):** pull the latest tagged release into the project's `agent_docs/`. Record the tag in the project (e.g., `agent_docs/DOCTRINE_VERSION` file). 
- **Project → Hub (at retrospective/gates):** lessons that changed local docs go back as a **PR to the Hub**. PR description cites run + lesson numbers (existing convention).
- **Never project → project.** Cross-project propagation happens only via the Hub.

### 2.5 Roles
- **Claudy (via GitHub MCP):** authors Hub PRs directly from lesson context — drafts the diff, the archive move, the MANIFEST/CHANGELOG updates.
- **Tony:** reviews + merges. No AI writes to main. (Matches the campaign standing rule: "operator owns git." Human gate preserved.)

### 2.6 Releases
- Git tags: `doctrine-YYYY.MM[-patch]`. Projects pin to a tag; "which doc set is this project on?" = one command.
- The old per-project drift question becomes a manifest diff between the project's pinned tag and Hub HEAD.

## 3. Later Phases (parked — do not build yet)
- CI lints on Hub PRs: retired-term grep (e.g., "Stitch"), mojibake detection, versioned-filename cross-ref detection, header-block presence.
- Auto-generated MANIFEST from header blocks.
- Doctrine-sync automation to running projects (supersedes DOCTRINE_SYNC_MANIFEST manual process).
- `_SKILLS/` doctrine migration into the Hub (own design session per repo backlog).

## 4. Sequencing With the Audit
1. Tony creates the empty Hub repo.
2. Jarvis produces the exact seed list (source → hub path → version), sourced from the RECONCILIATION_REPORT, not memory.
3. Tony seeds, pushes, tags `doctrine-2026.07-seed`.
4. This project's GitHub sync swaps from starter-kit repo → Hub (leaner capacity, docs-only truth).
5. Audit resumes (Review 005). All accepted fixes from reviews land as Hub commits/PRs — the audit's output becomes merged doctrine, not recommendations.

## 5. Decisions Needed From Tony
| # | Decision | Jarvis recommendation |
|---|----------|----------------------|
| 1 | Naming: canonical live names + versioned archive (hybrid above) vs versioned live filenames | Hybrid — the v1_4 impostor is the case against versioned live names |
| 2 | Claudy write access: PR-only vs direct-to-main | PR-only; Tony merges |

## 6. Findings This Design Closes (once implemented)
F-004 (master index), F-007 (factory versioning), F-011/F-016 (versioned filenames), F-018 (header standard), F-019-class drift (release tags + manifest diff), and provides the F-017 single-source mechanism.

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md and RECONCILIATION_REPORT.md.*
