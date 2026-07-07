# MASTER DOC LIST — v1.0 FINAL (SEED-READY)

> **Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Author:** Architect Jarvis | **Date:** 2026-07-04 | **Status:** ✅ FINAL — all 27 rows verified, zero 🔎 remaining
> **Supersedes:** MASTER_DOC_LIST_v0_1 (kept as history)
> **Purpose:** The copy-paste seed plan for the `app-factory-doctrine` repo. Every row: pull from WHERE, save as WHAT.

---

## Verification Sweep Results (closing the 7 open rows)

| Doc | Verdict | Evidence |
|---|---|---|
| SOFTWARE_FACTORY_PLAYBOOK | ✅ ALIGNED v1.1 both sides | Repo copy `SOFTWARE_FACTORY_PLAYBOOK_v1.1.md` identical to stack |
| FFM_PLAYBOOK | ✅ ALIGNED both sides | Stack + `agent_docs/APP_FACTORY/FFM_PLAYBOOK.md` chunks identical |
| RECON_QUESTIONNAIRE | ✅ Stack = truth | No campaign bump recorded; stack copy post-dates campaign |
| TESTING_PLAYBOOK | ✅ Stack = truth | No campaign bump recorded |
| STATE_MANAGEMENT_MANUAL | ✅ Stack = truth | No campaign bump recorded |
| GLOBAL_DESIGN_SYSTEM_HANDBOOK | ✅ Stack = truth (v1.1-era content) | Content matches post-reconciliation doctrine; re-verify at Tier 5 review |
| THEMING_MANUAL | ✅ Stack v1.1 = truth (NEWER than repo v1.0) | Stack v1.1 carries the entry-stylesheet portability rule |
| **THEME_LIBRARY** | 🔴 **STACK STALE — new catch** | Repo has **v1.1 (2026-06-08)**: `globals.css` correction, `--role-*` tokens, L16 fix, cross-refs. Stack copy is the prior unversioned edition. |

**Also:** repo cross-references `agent_docs/APP_FACTORY/STARTER_KIT_HANDBOOK.md` (canonical name) — largely resolves F-020.

---

## THE SEED PLAN — 27 files

Format: **New Filename** ← source. `[STACK]` = this project's doc stack copy. `[REPO]` = starter kit v3 repo (paths noted).

### 1_CONSTITUTION (3)
- **1_CONSTITUTION-APP_FACTORY_BLUEPRINT_v2_0.md** ← [STACK] `AI_APP_FACTORY_BLUEPRINT_v2_0.md` *(rename executes F-008)*
- **1_CONSTITUTION-SOFTWARE_FACTORY_PLAYBOOK_v1_1.md** ← [STACK] (aligned with repo)
- **1_CONSTITUTION-STARTER_KIT_HANDBOOK_v1_1.md** ← [STACK] (aligned with repo)

### 2_AGENTS (6)
- **2_AGENTS-ARCHITECT_PLAYBOOK_v2_1.md** ← [STACK] `ARCHITECT_PLAYBOOK_v2.md` *(filename gains true version, F-016)*
- **2_AGENTS-ARCHITECT_QUESTIONNAIRE_v2_1.md** ← [STACK]
- **2_AGENTS-RECON_QUESTIONNAIRE.md** ← [STACK]
- **2_AGENTS-DESIGNER_PLAYBOOK_v2_0.md** ← [STACK]
- **2_AGENTS-ENGINEER_PLAYBOOK_v1_1.md** ← [STACK]
- **2_AGENTS-HANDOFF_PACKAGE_PLAYBOOK.md** ← [STACK]

### 3_METHOD (5)
- **3_METHOD-FFM_PLAYBOOK.md** ← [STACK] (aligned with repo)
- **3_METHOD-FRONTEND_FIRST_PLAYBOOK_v1_1_2.md** ← 🔴 [REPO] `agent_docs/APP_FACTORY/FRONTEND_FIRST_PLAYBOOK_v1.1.2.md`
- **3_METHOD-FRONTEND_BUILD_PHASE_PLAYBOOK_v1_2.md** ← [STACK] (aligned with repo)
- **3_METHOD-TESTING_PLAYBOOK.md** ← [STACK]
- **3_METHOD-APP_FACTORY_SKILLS_PLAYBOOK.md** ← [STACK]

### 4_MANUAL (7)
- **4_MANUAL-APP_ARCHITECTURE_MANUAL_v1_2.md** ← 🔴 [REPO] `agent_docs/APP_FACTORY/` (Gate 10 bump)
- **4_MANUAL-STATE_MANAGEMENT_MANUAL.md** ← [STACK]
- **4_MANUAL-API_AND_SERVICES_MANUAL.md** ← [STACK]
- **4_MANUAL-DATABASE_MANUAL.md** ← [STACK]
- **4_MANUAL-AUTH_MANUAL_v1_2.md** ← 🔴 [REPO] `agent_docs/APP_FACTORY/` (Gate 10 bump)
- **4_MANUAL-ECOMMERCE_AND_PAYMENTS_MANUAL.md** ← [STACK]
- **4_MANUAL-STRIPE_SUBSCRIPTIONS_PLAYBOOK.md** ← [STACK]

### 5_DESIGN (6)
- **5_DESIGN-GLOBAL_DESIGN_SYSTEM_HANDBOOK.md** ← [STACK]
- **5_DESIGN-UI_UX_BUILDING_MANUAL_v1_3.md** ← 🔴 [REPO] `agent_docs/APP_FACTORY/UI-UX-BUILDING-MANUAL_v1_3.md` *(stack "v1_4" is v1.2 content — do NOT seed it)*
- **5_DESIGN-THEMING_MANUAL_v1_1.md** ← [STACK] (newer than repo v1.0)
- **5_DESIGN-THEME_LIBRARY_v1_1.md** ← 🔴 [REPO] `_SKILLS/starter-kit-cleaner-skill/references/THEME_LIBRARY_v1_1.md` *(stack copy is pre-June-8 — do NOT seed it)*
- **5_DESIGN-TOKEN_FILE_v1_1.md** ← [STACK]
- **5_DESIGN-COMPONENT_REGISTRY_v1_1.md** ← 🔴 [REPO] `agent_docs/STARTER_KIT/COMPONENT_REGISTRY.md` (Gate 10 bump to v1.1; verify path on pull)

### Repo root extras (2)
- **MANIFEST.md** — Jarvis will generate from this list (doc, version, date, status table)
- **_ARCHIVE/** — seed with the 6 superseded copies for history: old FRONTEND_FIRST v1.1.1, APP_ARCHITECTURE v1.1, AUTH v1.1, UI-UX v1.2 (the "v1_4" file, renamed honestly), THEME_LIBRARY (pre-v1.1), COMPONENT_REGISTRY v1.0

---

## Scoreboard (FINAL)

- From STACK: **21 docs**
- From REPO: **6 docs** (Frontend-First v1.1.2 · App Architecture v1.2 · Auth v1.2 · UI-UX v1.3 · Theme Library v1.1 · Component Registry v1.1)
- To _ARCHIVE: 6 superseded copies
- Impostor to discard from live set: stack `UI-UX-BUILDING-MANUAL_v1_4.md`

## Tony's Seed Checklist

- [ ] Create empty repo `app-factory-doctrine` (main branch)
- [ ] Copy 21 stack docs → rename per list
- [ ] Copy 6 repo docs → rename per list
- [ ] Create `_ARCHIVE/` with the 6 superseded copies
- [ ] Ask Jarvis for MANIFEST.md content (one message, I'll generate it)
- [ ] Commit + push + tag `doctrine-2026.07-seed`
- [ ] Swap this project's GitHub sync: starter-kit repo → `app-factory-doctrine`
- [ ] Tell Jarvis "seeded" → verification recon → audit resumes at Review 005

---

*Part of the Factory Doc Stack Audit series. Phase 2 (update/sync loop) parked in DOCTRINE_HUB_DESIGN_v0_1.*
