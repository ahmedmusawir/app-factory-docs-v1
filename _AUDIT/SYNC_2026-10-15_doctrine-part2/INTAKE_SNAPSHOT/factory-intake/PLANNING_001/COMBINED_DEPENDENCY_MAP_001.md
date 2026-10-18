# Combined Dependency Map 001 — planning map for Correction Package 001 (R2) × Harvest Package v0.1

> **PLANNING DEPENDENCY MAP — DRAFT / NOT APPROVED. This is not the formal UPDATE MAP.** The UPDATE MAP is produced by DocSet Sync Phase 2 after Gate 1, from approved cargo in `_INBOX/`, with per-term propagation searches and proposed wording (D17, D19). This document proposes **which items go where, who consumes them, what class they are, and why the route is LARGE**, so the UPDATE MAP can be built quickly once the decisions in `COMBINED_DECISIONS_001.md` are ruled. Mappings that depend on a ruling are marked **CONDITIONAL** and must not land before it.
>
> **Revision R1 (2026-10-14).** The Director's rulings (`DIRECTOR_RULINGS_2026-10-14.md`, RUL-01…07) resolve groups A.1–A.4, B.1 and C.1. Three rules now hold throughout this map: **QAM is mandatory for every newly authored module (RUL-01); the QA branch is a continuing `qa/<module>` line that the Director merges into `main`, never disposable (RUL-02); the QAM §14 cleanup checkpoint is required and only abandon/transfer-back cleanup is retired (RUL-03).** The Gate and Cond. columns in §3 are updated row by row; QAM rows now cite the approved `QAM_PLAYBOOK_v1_0.md` sections as the authoring source. New: §4a propagation plan (RUL-06), §4b template inventory, §9 exact next DocSet Sync step, §10 external dependencies. CL references corrected in §7.
>
> **Revision R2 (2026-10-14, after Architect acceptance of R1).** Jarvis's corrections applied: QAM-04 row and §4a (parent-module routing is covered by playbook §6 → D.4 resolved; FFM §8.3 wording is a Gate 2 drafting item); §7 and §10 E-7 (RUL-05 governs current drafting and does not authenticate the missing historical "later 10X" source); §3.3 QAM-03, §4b, §9 P1/P4 and §10 E-2 (the template set is now **drafted by the Engineer seat** in `../INTAKE_ADDENDUM_001_v0_2/TEMPLATES/QAM/`, labeled NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED; the QA Lead accepts its QA behavior; the addendum indexes the playbook and the omitted register row).
>
> **Revision R3 (2026-10-14, after Jarvis's review).** Consolidated intake structure accepted (AD-00). **Template home decided by Architect decision AD-01** (`ARCHITECT_DECISIONS_2026-10-14.md`): `03_BUILD_METHODOLOGY/_templates/QAM/`; the placement and the D15 cargo-path translation are carried in §4a as UPDATE MAP rows; §9 P1/P4 and §10 E-2/E-8/E-11 updated; addendum now v0.2 (`../INTAKE_ADDENDUM_001_v0_2/`, v0.1 preserved). The Director-executed Git convention (P6) is established and not reopened.

> **Revision R4 (2026-10-14, after the QA Lead's decision).** The QA Lead (Fable) decided **ACCEPT WITH EXACT AMENDMENTS** on the v0.2-draft template set and adopted the standing requirements as **QAM-SR v1.0** (2026-10-14; verbatim in `../INTAKE_ADDENDUM_001_v0_3/QA_LEAD_DECISION_2026-10-14.md`). The exact amendments AM-1/AM-2/AM-3 and the adoption record are applied in **v0.3-draft** (`../INTAKE_ADDENDUM_001_v0_3/`, `TEMPLATE_CORRECTION_RECORD_002.md`; v0.1 and v0.2 preserved). N-2(a) therefore moves from "QA Lead acceptance pending" to "decision received; Architect amendment verification pending". No second QA Lead decision is implied; §3.3 QAM-03, §4b, §9 P1/P4 and §10 E-2 carry the R4 status; nothing else changes.

> **Revision R5 (2026-10-15, after the Architect's verification).** Jarvis verified `QAM_TEMPLATES_v0_3_AMENDED_FOR_ARCHITECT_2026-10-14_204903.zip` (34 files; 32 indexed members; HASH_MANIFEST 33/33; AM-1/AM-2/AM-3 and the QAM-SR v1.0 adoption confirmed applied; remaining differences bookkeeping) and accepted the amendments under the QA Lead's existing decision; no further QA Lead review for these edits; canonical installation and DocSet Sync remain pending (`../INTAKE_ADDENDUM_001_v0_3/ARCHITECT_VERIFICATION_2026-10-14.md`). **N-2(a) is SETTLED; template acceptance and placement are settled.** The QA Lead's actual decision text was supplied and is now preserved verbatim; the text previously filed under its name was the Director-relayed Architect implementation instruction and is preserved as such (`ARCHITECT_IMPLEMENTATION_INSTRUCTION_2026-10-14.md`). §9 P1/P4 and §10 E-2 carry the R5 status; no template file changed.

| Field | Value |
|---|---|
| Prepared by | Claudy (documentation Engineer seat), 2026-10-13 21:50 +0600 |
| Inputs | Correction index R2 + 7 briefs + `DECISION_RECORD_001.md`; harvest v0.1 index, register, three briefs and sources; `COMBINED_DECISIONS_001.md` (group labels A.1 … E) |
| DocSet Sync revision | `_SKILLS/factory-docs-update/` at main `9c179392f79b70da099121fc357d3107ad3bb86e` — sync-engineer `SKILL.md` v0.8-DRAFT, family `CLAUDE.md`, `INTAKE_TAXONOMY.md`, `decision-trees/route-selection.md` (read with `git show`; not activated) |
| Hub baseline for counterparts | main `9c17939`: 29 live docs per MANIFEST v1.0 (31 on disk; DRIFT per the skill's worked example); `git grep` over `0?_*/*.md` + `MANIFEST.md` |
| Relation vocabulary | from `factory-intake/README.md` §4: SAME · EXTENDS · CONFLICTS · NEW (relative to the certified FC/CF record or the live Hub text) |
| Revision | **R5 (2026-10-15 12:06 +0600):** Architect verification recorded in §9 P1/P4 and §10 E-2. **R4 (2026-10-14 20:45 +0600):** QA Lead decision recorded in §3.3/§4b/§9 P1,P4/§10 E-2; addendum v0.3. **R3 (2026-10-14 19:12 +0600):** AD-01 placement carried into §4a/§9/§10; addendum v0.2. **R2 (2026-10-14 18:45 +0600):** Jarvis's corrections (D.4, RUL-05 provenance, template authoring vs QA ownership); addendum `../INTAKE_ADDENDUM_001_v0_2/` referenced in §4b, §9, §10. **R1 (2026-10-14 15:05 +0600):** rulings RUL-01…07 applied; approved source `QAM_PLAYBOOK_v1_0.md` SHA-256 `97e111e2…5c897`; §4a/§4b/§9/§10 added. **R0 (2026-10-13 21:50):** initial map. |

---

## 1. Method

1. **Crosswalk.** Each WF/RRM/QAM item is joined to the FCs/CFs its brief cites ("Correction link / interface") and to the harvest index §3 overlap table; I added FCs only where the item's text plainly touches a certified defect surface, and say so.
2. **Owning document.** Proposed by canonical name first, content similarity second (taxonomy D16), from the Hub tree and the grep evidence in §2. "New" means no counterpart by name or content.
3. **Consumers.** From MANIFEST's "Dependency Map — Ripple Analysis (← Referenced by)" on main, plus the Appendix of body-only mentions. The ← count is the blast radius the per-doc dance uses (D7, "lightest ← first").
4. **Class.** The eleven D16 classes, applied to the *cargo as it would arrive after approval*. The harvest briefs are outcome-level proposals, not an APPROVED CORRECTION PACKAGE (class 1 requires APPROVED status and the seven fields). After approval they enter as class 2 intent-level entries (target + rule change), class 3 new canonical documents, class 5 process documents (resolving to class 3/4 mechanics), class 6/7/8 for diagrams and sources, class 9 for cross-boundary parks. The correction package stays class 1 with FC IDs as join keys.
5. **Route.** `route-selection.md` Decision A, conditions A1–A10, provisional (Phase 1 shape); final only after the Phase 2 search.
6. **CONDITIONAL** = the mapping's wording or existence depends on a Group A–E ruling. The group label names the ruling; the underlying IDs are in the decision list.

## 2. Hub counterpart evidence (main `9c17939`, tier folders + MANIFEST)

| Term | Hits | Where | Reading |
|---|---:|---|---|
| `RRM`, `Review Rework`, `REVIEWER_PLAYBOOK` | 0 | — | No counterpart → RRM_PLAYBOOK is class 3 (forces LARGE). SFP has only a "Code Review Checklist" (line 961). |
| `QAM` | 0 | — | No counterpart → QAM_PLAYBOOK is class 3. **R1: RESOLVED (RUL-01, mandatory; RUL-06 placement).** |
| `one-shot` | 0 | — | No counterpart; pattern text only (class 2). |
| `QA branch` / `disposable` / `qa/` | 0 / 2 / 0 | FRONTEND_FIRST (mock data, unrelated) | **No Hub branch-lifecycle rule exists.** R1: RUL-02 supplies the rule (continuing `qa/<module>` branch); it lands as NEW text in QA_PLAYBOOK, BIM_PLAYBOOK, RRM_PLAYBOOK and QAM_PLAYBOOK. |
| `DevOps` | 8 | QA_PLAYBOOK §4 (seat), BUG_FIX, APP_FACTORY_SKILLS, STRIPE | Seat named; no owning doctrine (FC-011 certified) → `DEPLOYMENT_PLAYBOOK` is class 3. R1: placement RESOLVED (RUL-06); content/authority still C.2. |
| `QA Executor` | 0 | — | R1: new seat by ruling (RUL-01) → SFP glossary anchor + QA_PLAYBOOK §4 (class 2, terminology → A4 fails). |
| `agent_docs` | 59 | FFM (22), RECON (11), STARTER_KIT (6), HANDOFF (5), TESTING (3), ARCHITECT, BIM, ENGINEER, SFP, SKILLS, COMPONENT_REGISTRY, THEME_LIBRARY | Counterpart for "QA records under `agent_docs/`" (RUL-03). RECON Q9.1–Q9.2 check tsconfig/test exclusion only; **deployment exclusion (RUL-03) has no counterpart** (`dockerignore`/`vercelignore`/`gcloudignore` 0 hits) → new row in DEPLOYMENT_PLAYBOOK + RECON Q9.3. |
| `TEMPLATES` | 2 | APP_FACTORY_SKILLS_PLAYBOOK | No Hub convention for doctrine-tier template folders; templates exist only under `_SKILLS/…/templates/`. Bears on N-2 (`TEMPLATES/QAM/` home). |
| `TRM` | 0 | — | No definition; RUL-07 forbids inventing one → N-6 placeholder row. |
| `Gate D` | 35 | QA_PLAYBOOK (Steps D1–D7), BIM, BUG_FIX, FRONTEND_BUILD_PHASE, DESIGNER | Gate D interface exists; WF-08/09 EXTEND it. |
| `Cloud Run` / `cloudbuild` / `deploy.sh` / `init-app.sh` | 31 / 1 / 1 / 0 | Blueprint, ARCHITECT, ENGINEER, SKILLS, BUG_FIX, FFM, QA, STRIPE | Platform mentions scattered; no package doctrine. |
| `Backend Integration Module` / `Backend Implementation Module` | 3 / 0 | BIM_PLAYBOOK header, MANIFEST | Hub expansion is "Integration" → WF-06's acronym concern resolves to NO-CHANGE on the expansion. |
| `AGENTS.md` | 14 | FFM_PLAYBOOK (12; §8.3 "AGENTS.md → redirects to CLAUDE.md"), RECON_QUESTIONNAIRE (2) | Counterpart for QAM-04 exists; EXTENDS. |
| `Operator` / `Coordinator` / `Director` | 354 / 19 / 18 | 19 docs / BIM + BUG_FIX / 8 docs | Seat vocabulary is live and heavy; D.1 is a normalization, not a rename (A4 still fails → LARGE). |
| `FILE_TREE` | 7 | APP_FACTORY_BLUEPRINT only | Matches FC-008 (no producer). |
| `ACCEPTANCE_SPEC` | 26 | SFP §2.5, BIM §8, BUG_FIX, FEAT, QA, MANIFEST | Counterpart for WF-05, RRM-02/04 (EXTENDS). |
| `Plan Mode` | 41 | ARCHITECT, HANDOFF, SKILLS, BIM, BUG_FIX, FEAT, FFM | Retained by every harvest item; no change. |
| `ABM` / `APBM` / `Vibe Engineering` | 0 | — | Out of scope; nothing proposed (RUL-07). QAM_PLAYBOOK's universality sentence covers them without importing methodology (N-4). |
| `Engine 1` / `Engine 2` | 0 / 0 | — | R1: terms used by RUL-05 → definitions needed in SFP §2 "Phase Vocabulary — One Canonical Map" (N-1; ENGINEER-PROPOSED wording at Gate 2). No "Engine 3". |

`_SKILLS/`, `_OTHERS/`, `_AUDIT/` on main: no RRM/QAM/REVIEWER/one-shot mentions (awareness scan, read-only).

## 3. Crosswalk: harvest items → corrections → owning document → consumers → class → gate

Columns: **Relation** is to the certified record / live Hub text · **Owning doc** is the proposed primary placement (canonical name; tier `03_` = `03_BUILD_METHODOLOGY/`, `02_` = `02_PIPELINE_AGENTS/`, `01_` = `01_CONSTITUTION/`) · **Consumers** are ← header-declared dependents (count) plus notable body mentions · **Class** per D16 · **Gate** = ruling in the decision list, or "RESOLVED RUL-nn" (R1) · **Cond.** = CONDITIONAL ("No" = lands with the ruling's wording; "Partly" names the remaining conditional fragment).

R1 reading aid: the Relation column keeps the R0 analysis (e.g. WF-07 "CONFLICTS with SRC-W06 §8"); the Gate column says how the conflict was resolved. For QAM rows, "v1.0 §n" means the section of the approved `QAM_PLAYBOOK_v1_0.md`, now the authoring source in place of SRC-Q03.

### 3.1 Factory Workflows (WF)

| ID | FCs / CFs touched | Relation | Owning doc (proposed) | Consumers (← count) | Class | Gate | Cond. |
|---|---|---|---|---|---|---|---|
| WF-01 Seats and human authority | FC-004, FC-006, FC-007, FC-011; CF-01 | EXTENDS DEC-07 glossary | `01_/SOFTWARE_FACTORY_PLAYBOOK` §2 vocabulary map (anchor); `01_/APP_FACTORY_BLUEPRINT`; `03_/QA_PLAYBOOK` §4 | SFP ←8, Blueprint ←7, QA ←3; body: BIM §2 roles, BUG_FIX | 2 (intent) | D.1 (NARROWED by RUL-01) | Yes — glossary host/synonyms only; "Director" and "QA Executor" land as ruled |
| WF-02 Recon lanes | FC-014, FC-023; CF-03 | EXTENDS DEC-14 | `02_/RECON_QUESTIONNAIRE`; `02_/ARCHITECT_PLAYBOOK` (recon mode); `02_/ENGINEER_PLAYBOOK` Phase 0 | RECON ←12, ARCHITECT ←6, ENGINEER ←7 | 2 | D.3 | Yes (diagnostics list) |
| WF-03 Artifact ownership and timing | FC-008, FC-015, FC-016, FC-017, FC-019, FC-027; CF-02 | EXTENDS DEC-11/12; **CONFLICTS** on UI_SPEC owner (Hub = Architect drafts) | `02_/HANDOFF_PACKAGE_PLAYBOOK`; `01_/APP_FACTORY_BLUEPRINT` artifact table; `02_/ARCHITECT_PLAYBOOK`, `02_/DESIGNER_PLAYBOOK`, `02_/ENGINEER_PLAYBOOK` §3; `02_/ARCHITECT_QUESTIONNAIRE` (APP_BRIEF template) | HANDOFF ←4, Blueprint ←7, DESIGNER ←10 | 2 | D.2 | Yes |
| WF-04 Architect assembles and freezes the FFM | FC-025, FC-026; CF-02, CF-04 | SAME (assembly already in FFM_PLAYBOOK per SRC-W05 B-3 → NO-CHANGE candidate with path:line at map time); EXTENDS freeze lanes | `03_/FFM_PLAYBOOK` | FFM ←9 | 2 (+10 for the assembly sentence) | RESOLVED RUL-04 | No |
| WF-05 Completion includes handoff | FC-013, FC-025; CF-02 | EXTENDS SFP §2.5 ACCEPTANCE_SPEC contract | `02_/ENGINEER_PLAYBOOK`; `01_/SOFTWARE_FACTORY_PLAYBOOK` §2.5; `02_/HANDOFF_PACKAGE_PLAYBOOK` | ENGINEER ←7, SFP ←8 | 2 | RESOLVED RUL-01 ("QAM manifest" is always required for new modules) | No |
| WF-06 BIM campaigns and lifecycle terminology | FC-007; CF-02 | EXTENDS SFP §2 "Phase Vocabulary — One Canonical Map"; acronym expansion → NO-CHANGE (Hub = Integration) | `03_/BIM_PLAYBOOK` §4–6; `01_/SOFTWARE_FACTORY_PLAYBOOK` §2 | BIM ←1, SFP ←8 | 2 (+10) | RESOLVED RUL-05 for the review axis (two checkpoints); acronym NO-CHANGE | No |
| WF-07 QA execution by evidence need; branch | FC-022, FC-024; CF-05; DEC-13 | **CONFLICTS** with QA_PLAYBOOK Stage 5 as a default and with SRC-W06 §8 (branch) | `03_/QA_PLAYBOOK` §4, Stage 5 | QA ←3; body: BIM §9, BUG_FIX, FEAT, FFM §7 | 2 | RESOLVED RUL-02 (branch) + RUL-03/RUL-01 (execution, cleanup) | No — lands with the ruling wording |
| WF-08 DevOps as a shared function | FC-011; CF-14; DEC-18 | NEW (no owning doctrine) | new `03_/DEPLOYMENT_PLAYBOOK` (name per C.1) | QA_PLAYBOOK Gate D / Steps D1–D7, BIM §6, Blueprint phases, APP_FACTORY_SKILLS (deploy skills) | 3 / 5 | C.1 RESOLVED (owner = DEPLOYMENT_PLAYBOOK); C.2 OPEN (content/authority) | Yes — content; placement no |
| WF-09 Deployment identity, rollback, redeploy limits | FC-011, FC-012, FC-088; CF-14; DEC-17/18 | NEW | same deployment doc; `03_/QA_PLAYBOOK` Step D1 (identity) | as above | 3 | C.1 RESOLVED (owner); C.2 OPEN | Yes — content; placement no |
| WF-10 Context × action × seat git/sync matrix | FC-012; CF-14; DEC-18/21 | EXTENDS (FC-012 partially remediated) | deployment doc (matrix) or SFP (per C.2); `03_/BIM_PLAYBOOK` §6 (Coordinator commits); `03_/FFM_PLAYBOOK` | BIM ←1, FFM ←9; `_SKILLS/factory-docs-update/CLAUDE.md` D5 read-only (XB-SKILL awareness) | 2 (+9 for skill wording) | RUL-02 (module-Git row); C.2 OPEN (cloud columns); DEC-21 | Partly — module-Git row lands |
| WF-11 Review engines, targeted repair, certification | — (no FC) | NEW process (cadence); EXTENDS QA_PLAYBOOK Gate Q/D definitions (unchanged) | `01_/SOFTWARE_FACTORY_PLAYBOOK` §2 only if cadence adopted; else RRM_PLAYBOOK "when launched" section as proposal | SFP ←8 | 5 (if adopted) / 2 | RESOLVED RUL-05 (two checkpoints; N-1 wording) | No — Engine 1/2 definitions ENGINEER-PROPOSED at Gate 2 |
| WF-12 One owning document; synchronized visuals | FC-009, FC-087, FC-093; CF-13, CF-16 | EXTENDS | `MANIFEST.md` rows + ← recompute; new docs' "Pairs with"; diagrams: originals class 8 → `_AUDIT/`; revised diagrams class 6 → `<tier>/_assets/` only if commissioned | all new-doc consumers | 3 mechanics / 6 / 8 | RESOLVED RUL-06 | No |

### 3.2 Review Rework Modules (RRM)

| ID | FCs / CFs touched | Relation | Owning doc (proposed) | Consumers (← count) | Class | Gate | Cond. |
|---|---|---|---|---|---|---|---|
| RRM-01 Route findings into a bounded module | — | NEW | new `03_/RRM_PLAYBOOK` §§1–4; crosswalk rows in `03_/QA_PLAYBOOK` Stage 7 (classes A–G) and `03_/BUG_FIX_PLAYBOOK` (FIX vs RRM boundary); `01_/SOFTWARE_FACTORY_PLAYBOOK` §2.5 (module ID `RRM-NNN-APP`) | QA ←3, BUG_FIX ←3, SFP ←8 | 3 (+2 rows) | RESOLVED RUL-05 | No |
| RRM-02 Freeze the repair contract | FC-013, FC-025, FC-026; DEC-13 | EXTENDS SFP §2.5, BIM §6 Locked Rules | RRM_PLAYBOOK §5; `01_/SOFTWARE_FACTORY_PLAYBOOK` §2.5 (restated once) | SFP ←8, BIM ←1 | 3 + 2 | RESOLVED RUL-04 | No |
| RRM-03 Baseline and preflight | FC-014, FC-022, FC-030; DEC-14 | EXTENDS RECON_QUESTIONNAIRE | RRM_PLAYBOOK §6; `02_/RECON_QUESTIONNAIRE` (preflight concept, one row) | RECON ←12 | 3 + 2 | D.3 | Yes |
| RRM-04 Prepared run and same-assignment handoff | FC-013 | EXTENDS SFP §2.5, ENGINEER_PLAYBOOK handoff | RRM_PLAYBOOK §§6–7; `02_/ENGINEER_PLAYBOOK` pointer | ENGINEER ←7 | 3 + 2 | E (continuous-execution sentence only) | Partly |
| RRM-05 Independent QA and the QAM interface | — | EXTENDS QA_PLAYBOOK §4 authority, BIM §9 | RRM_PLAYBOOK §7; `03_/QA_PLAYBOOK` §4 (QA Executor line) | QA ←3 | 3 + 2 | RESOLVED RUL-01/RUL-05 ("each RRM includes QAM"); seat per D.1 narrowed | No |
| RRM-06 Forward certification line and bounded repairs | — ; DEC-13, DEC-18 | **CONFLICTS** with SRC-W06 §8 (source vs source; no Hub rule) | RRM_PLAYBOOK §6/§8; `03_/QA_PLAYBOOK` only if Factory-wide | QA ←3, BIM ←1 | 3 | RESOLVED RUL-02 — continuing qa/<module> branch, Director-merged | No — lands with the ruling wording |
| RRM-07 Certification, cleanup, closeout, integration | DEC-13, DEC-18; CF-14 | EXTENDS QA_PLAYBOOK Gate Q / Gate D; sequence CONFLICTS between sources (Gate Q→cleanup vs cleanup→certificate) | RRM_PLAYBOOK §9; `03_/QA_PLAYBOOK` Gate Q section (sequence note); deployment doc (merge/Gate D rows) | QA ←3 | 3 + 2 | RESOLVED RUL-03 (sequence) + RUL-02 (branch); C.2 for cloud/Gate D rows | Partly — Gate D/cloud rows |
| RRM-08 One-shot engineering as a scoped option | — | NEW pattern | RRM_PLAYBOOK (optional run shape); `02_/ENGINEER_PLAYBOOK` pointer | ENGINEER ←7 | 2 | E | Yes |
| RRM-09 Reviewer playbook modernization | FC-009 (unlocated external artifacts) | NEW (no Hub reviewer doctrine) | RRM_PLAYBOOK reviewer section; standalone doc only under DEC-19 | — | 3 (section) | B.2, DEC-19 | Yes |
| RRM-10 Owning playbook, kit, references | FC-009, FC-003; CF-13; DEC-19 | NEW | RRM_PLAYBOOK + MANIFEST row + "Pairs with" (FFM, BIM, BUG_FIX, QA, TESTING, ENGINEER, ARCHITECT, HANDOFF); kit/templates → DEC-19 location or `XB-EXT` | all listed | 3 + 9 (kit if external) | RESOLVED RUL-06 (document); kit per N-2/DEC-19 | Partly — kit/template home |

### 3.3 QA Modules (QAM)

| ID | FCs / CFs touched | Relation | Owning doc (proposed) | Consumers (← count) | Class | Gate | Cond. |
|---|---|---|---|---|---|---|---|
| QAM-01 Definition and adoption boundary | — | NEW | new `03_/QAM_PLAYBOOK` from v1.0 §§1–2, §16 (scope: mandatory for every newly authored module; N-3 retroactivity line; N-4 ABM/APBM line; N-6 TRM line) | QA ←3 + links from HANDOFF, ARCHITECT, ENGINEER, BIM, FFM | 3 | RESOLVED RUL-01 | No |
| QAM-02 Authorship and five seats | FC-006, FC-025; DEC-07/13 | EXTENDS QA_PLAYBOOK §4 (adds QA Executor; DevOps already present) | `01_/SOFTWARE_FACTORY_PLAYBOOK` glossary; `03_/QA_PLAYBOOK` §4 (adds QA Executor); QAM_PLAYBOOK from v1.0 §3 | SFP ←8, QA ←3 | 2 + 3 | RESOLVED RUL-01 (seats); D.1 narrowed (host/synonyms) | Partly — glossary host only |
| QAM-03 Package readiness and ownership | DEC-13 | NEW templates (GAP-03: originals not supplied → newly authored, labeled) | QAM_PLAYBOOK from v1.0 §§5, 7; `02_/HANDOFF_PACKAGE_PLAYBOOK` link; `TEMPLATES/QAM/` per N-2 — **R2: drafted** in `../INTAKE_ADDENDUM_001_v0_2/TEMPLATES/QAM/` (Engineer draft, NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED); home per the placement recommendation | HANDOFF ←4 | 3 (+9 if templates external) | RESOLVED RUL-01/RUL-04; templates: home decided (AD-01); **R4: QA Lead accepted with exact amendments, applied in v0.3-draft (`../INTAKE_ADDENDUM_001_v0_3/`); Architect amendment verification pending** | Partly — Architect verification and landing of the set; text lands |
| QAM-04 Folder-only startup; dual entries | — | EXTENDS FFM_PLAYBOOK §8.3 (AGENTS.md redirect); NEW for "QAM folder assigns QA Executor" | `03_/FFM_PLAYBOOK` §8.3 (one reconciling sentence); `03_/BIM_PLAYBOOK` §5 manager file; QAM_PLAYBOOK from v1.0 §6 | FFM ←9, BIM ←1; RECON (2 body hits) | 2 + 3 | RESOLVED RUL-01 — **R2: playbook §6 covers the `QAM/` files and the parent-module routing (D.4 resolved)**; FFM §8.3 wording ENGINEER-PROPOSED at Gate 2 | No — wording only |
| QAM-05 Checkpoint sequence (Q1/Q1b/Q2/Q4/Q5) | DEC-13 | EXTENDS QA_PLAYBOOK Stages 1–7 (different axis → crosswalk table, not replacement) | QAM_PLAYBOOK from v1.0 §§1, 8–10 (Q1 · approval/Q1b · Q2; Q4 conditional); `03_/QA_PLAYBOOK` one crosswalk row | QA ←3 | 3 + 2 | RESOLVED RUL-01/RUL-03/RUL-02 | No |
| QAM-06 Preflight and concrete stops | FC-014, FC-022, FC-030; DEC-14 | EXTENDS QA_PLAYBOOK Stage 3 Environment Readiness | QAM_PLAYBOOK from v1.0 §8 (Q1 checks), §11 (STOP-* table); `03_/QA_PLAYBOOK` Stage 3 | QA ←3 | 3 + 2 | RESOLVED RUL-01 as source; D.3 for the diagnostics lanes sentence | Partly — diagnostics sentence |
| QAM-07 Credential and browser lifecycle | FC-021, FC-022; CF-05 | EXTENDS TESTING_PLAYBOOK (sensitive data out of logs), QA Stage 3 | QAM_PLAYBOOK from v1.0 §12, §14; `03_/TESTING_PLAYBOOK` awareness pointer | TESTING ←11 (pointer only) | 3 | RESOLVED RUL-01/RUL-03 | No; A6 high-risk (credentials) — Gate 2 scrutiny |
| QAM-08 Independent instruments; literal grading | FC-024; CF-05 | EXTENDS QA_PLAYBOOK evidence labels (EVIDENCE/INFERENCE/CLAIM/GAP/QUESTION exist) and Stage 4 | QAM_PLAYBOOK from v1.0 §§10–11 (labels, "no relabeling to PASS"); `03_/QA_PLAYBOOK` Stage 4 row | QA ←3 | 3 + 2 | RESOLVED RUL-01 | No |
| QAM-09 Finding classification and repair | — | EXTENDS QA_PLAYBOOK Stage 7 classes A–G (QAM's five classes crosswalk to them) | QAM_PLAYBOOK from v1.0 §11 (classification; repair on the QA line); `03_/QA_PLAYBOOK` Stage 7 crosswalk row | QA ←3 | 3 + 2 | RESOLVED RUL-01/RUL-02 | No |
| QAM-10 Durable evidence and certification | DEC-13 | EXTENDS QA_PLAYBOOK verdicts and Gate Q | QAM_PLAYBOOK from v1.0 §§14–15 (verdicts, cleanup, closeout, state); `03_/QA_PLAYBOOK` Gate Q (exact Lead text; sequence note) | QA ←3 | 3 + 2 | RESOLVED RUL-01/RUL-03/RUL-04 | No |
| QAM-11 Checkpoint review packages (`QAM/HANDOFFS/`, allowlist, SHA-256) | — | NEW (HANDOFF_PACKAGE_PLAYBOOK is the FFM 4-file package, a different subject) | QAM_PLAYBOOK from v1.0 §13 (`QAM/HANDOFFS/<MODULE>_<PHASE>_REVIEW_<ATTEMPT>.zip`, FILE_INDEX.json, inclusion list) | — | 3 | RESOLVED RUL-01 (source approved; the SRC-R04 Obs. 005–006 confirmation is absorbed) | No |
| QAM-12 Honest metrics; separate verdicts | — | NEW | QAM_PLAYBOOK from v1.0 §17; RRM_PLAYBOOK §10 (return learning) | — | 3 | RESOLVED RUL-01; E for the one-shot sentence | Partly — one-shot sentence |
| QAM-13 Integration with the DocSet; tooling boundary | FC-009; CF-13 | mechanics | `MANIFEST.md` row + "Pairs with" on QA_PLAYBOOK, HANDOFF, ARCHITECT, ENGINEER, BIM, FFM, BUG_FIX, FEAT, RRM; v1.0 §4, §18; tools → not approved (RUL-07) | all listed | 3 mechanics + 9 | RESOLVED RUL-06/RUL-07 | No |
| QAM-14 Portability, validation, promotion | — | NEW | QAM_PLAYBOOK from v1.0 §§16–17 (adaptation table; metrics); promotion threshold moot (mandatory) | — | 3 | RESOLVED RUL-01/RUL-07 | No |

### 3.4 The sources themselves, if they ride in as cargo

| Source | Class | Landing | Note |
|---|---|---|---|
| SRC-W05, W06, W07 operating models (REVIEW, 2026-08-24) | 7 (supporting) or 8 (historical) → `_AUDIT/` | never a live tier | "Tier 1 / canonical" labels in them are claims (harvest index §7). Not class 4: they must not replace FFM/BIM playbooks wholesale. |
| SRC-W01…W04 diagrams | 8 → `_AUDIT/` | — | Class 6 only for revised diagrams Tony commissions. |
| SRC-W08, W09, W10, W11 text diagrams | 7 → `_AUDIT/`; **W11 class 8 (superseded by RUL-05)** | — | Proposals; W10 is superseded by the installed skill; W11's three-engine model is superseded by the two-checkpoint ruling. |
| **`QAM_PLAYBOOK_v1_0.md`** (QA Lead / JARVIS, 2026-10-14; SHA-256 `97e111e2…5c897`) — R1 | **3 (new canonical document)**: its content becomes `03_/QAM_PLAYBOOK.md` via the map's proposed wording, exact text preserved except the integration substitutions N-3…N-6 (each marked ENGINEER-PROPOSED); the original rides as class 7 → `_AUDIT/` | `03_BUILD_METHODOLOGY/` | Director-approved source (RUL-01). Not yet in `FILE_INDEX.json` / `SOURCE_REGISTER.md` (N-8). Its §4 cites "Doctrine Journal v0.3" and §14 "J-19 where supplied" — unsupplied (CL-11; N-5). |
| SRC-R01 pilot ZIP (RRM_PLAYBOOK v0.1 seed, kit, reviewer candidate, change map, journal v0.1) | 7 → `_AUDIT/`; the playbook content enters as class 3 **via the map's proposed wording**, not byte-for-byte | — | Nested reviewer ZIPs stay inside (declared). |
| SRC-R02 RRM-004 original pack | 7 → `_AUDIT/` | — | Blank forms; project-specific; not a template source without re-authoring (RRM-10). |
| SRC-R03 bundle, SRC-R04 journal, SRC-Q02 journal, SRC-Q03 master draft, SRC-Q04 plan, SRC-Q05 discussion | 7 → `_AUDIT/` | — | Rulings inside R04/Q02 are evidence for class-2 entries; Q03 is the authoring source for QAM_PLAYBOOK. |
| SRC-R05 empty scaffold | 7 (inventory only) | — | GAP-01. |
| SRC-C01 | 10 (already in repo as `agent_docs/RESPONSES/response_2026-10-12_215553_…`) | no landing | Byte-identical. |

## 4. Owning documents and consumers — the combined touch surface (planning estimate)

The correction package and the harvest touch the same heavy documents. D22 allows **one version bump per doc per unmerged run**, which is the strongest argument for one campaign.

| Document (canonical) | ← | Harvest items (proposed primary or row) | Correction package FCs (primary surface, from the briefs' likely files) | Notes |
|---|---:|---|---|---|
| RECON_QUESTIONNAIRE | 12 | WF-02, RRM-03 | FC-014 (CF-03), FC-023 | lightest-first order is by ←; this is the heaviest |
| TESTING_PLAYBOOK | 11 | QAM-07 pointer | FC-020…FC-024, FC-030, FC-031, FC-063 (CF-05) | harvest adds a pointer only |
| DESIGNER_PLAYBOOK | 10 | WF-03 | FC-017, FC-075, FC-084 … (CF-02, CF-11, CF-13) | |
| FFM_PLAYBOOK | 9 | WF-04, WF-10, QAM-04 | FC-025, FC-026, FC-028, FC-029 (CF-04, CF-03) | |
| SOFTWARE_FACTORY_PLAYBOOK | 8 | WF-01, WF-05, WF-06, (WF-11), RRM-01/02, QAM-02 | FC-001, FC-002, FC-005, FC-007 (CF-01) | glossary anchor |
| APP_FACTORY_BLUEPRINT | 7 | WF-01, WF-03 | FC-004, FC-008, FC-002 (CF-01, CF-02) | |
| ENGINEER_PLAYBOOK | 7 | WF-02, WF-03, WF-05, RRM-04/08 | FC-013, FC-027 (CF-02) | |
| ARCHITECT_PLAYBOOK | 6 | WF-02, WF-03 | FC-014, FC-017 | |
| HANDOFF_PACKAGE_PLAYBOOK | 4 | WF-03, WF-05, QAM-03 | FC-016, FC-018, FC-019 (CF-02) | |
| QA_PLAYBOOK | 3 | WF-01, WF-07, RRM-01/05/06/07, QAM-02/05/06/08/09/10 | FC-013 (QA intake), FC-032 anchors | the most harvest-dense doc; DEC-20 archive question becomes timely. R1: QA Executor seat (§4), continuing-branch rule, §14 sequence note, Q1/Q2 crosswalk |
| BUG_FIX_PLAYBOOK | 3 | RRM-01 boundary row; **R1: mandatory QAM for FIX modules** (module tree, handoff) | — | |
| BIM_PLAYBOOK | 1 | WF-06, WF-10, QAM-04; **R1: mandatory QAM in the one-folder package; continuing `qa/<module>` branch; §6 Locked Rules reconciled to frozen inputs + writable lanes (RUL-04)** | FC-026 (freeze), FC-064 (§7 failure policy, awareness) | |
| FEAT_PLAYBOOK | 1 | **R1: mandatory QAM for FEAT modules** (deltas over BIM) | — | |
| ARCHITECT_QUESTIONNAIRE | — | WF-03 (APP_BRIEF template) | FC-019 | |
| **New:** RRM_PLAYBOOK | 0 | RRM-01…10, WF-11, RRM-08; R1: two checkpoints (RUL-05), continuing branch (RUL-02), includes QAM (RUL-01) | — | class 3; **RESOLVED RUL-05/RUL-06** |
| **New:** QAM_PLAYBOOK | 0 | QAM-01…14 from `QAM_PLAYBOOK_v1_0.md` | — | class 3; **RESOLVED RUL-01/RUL-06** |
| **New:** DEPLOYMENT_PLAYBOOK | 0 | WF-08, WF-09, WF-10; R1: module-Git row (RUL-02), deployment-exclusion rule (RUL-03/N-7) | FC-011, FC-012, FC-088 | class 3; placement **RESOLVED RUL-06**; content C.2 |
| MANIFEST.md | — | 3 new rows; ← recompute | FC-093, FC-087 | FC-093 is baseline drift the intake authorizes repairing (index §13) |
| CHANGELOG.md | — | one row per bumped doc | FC-094 is XB-ROOT (format) | |

Documents the harvest does **not** touch: the reference manuals (CF-06…CF-10) and the design tier (CF-11/12), apart from CF-13 locator rows. Security, auth, data, commerce and design corrections proceed on the correction package alone.

### 4a. Propagation plan required by RUL-06 (R1) — what each existing document must say after sync

RUL-06: "A new QAM playbook beside contradictory old instructions does not satisfy the requested synchronization." The rows below are the **minimum** propagation scope the UPDATE MAP must search (D19) and disposition; they are intent-level (class 2) unless marked. Wording is proposed at Gate 2.

| Document (canonical) | Mandatory QAM (RUL-01) | Continuing QA branch (RUL-02) | Cleanup retained (RUL-03) | Lanes (RUL-04) | Review checkpoints (RUL-05) | Other |
|---|---|---|---|---|---|---|
| SOFTWARE_FACTORY_PLAYBOOK §2 / §2.5 | §2.5 "Module Identity & QA Handoff" states that every module type ships `QAM/`; process spine shows Q1/Q2 | one sentence: QA runs on `qa/<module>`; Director merges | — | §2.5: frozen contract + declared lanes | Phase Vocabulary: two review checkpoints; Engine 1/2 definitions (N-1) | glossary anchor: QA Executor seat (D.1 narrowed) |
| APP_FACTORY_BLUEPRINT | pipeline router: QAM packaging at Architect handoff | — | — | — | post-FFM review checkpoint in the pipeline | role table: QA Executor |
| FFM_PLAYBOOK | folder anatomy gains `QAM/` (mandatory); §8.3 entry files route QA to QAM | FFM QA on `qa/<module>` | §14 cleanup pointer | lanes inside the FFM folder | "Review after FFM completion and its QA" | fold SRC-W05 operating-model content (intent-level) |
| BIM_PLAYBOOK | one-folder package includes `QAM/`; manager grammar routes QA | replaces any abandon-branch instruction; `qa/<module>` continuing | §14 cleanup pointer; transfer-back cleanup retired | §6 Locked Rules reconciled (frozen inputs; writable lanes) | — | fold SRC-W06 content; acronym NO-CHANGE |
| BUG_FIX_PLAYBOOK, FEAT_PLAYBOOK | FIX/FEAT modules ship `QAM/` (v1.0 §16 rows) | same branch rule | pointer | pointer | — | FIX vs RRM boundary row |
| QA_PLAYBOOK | §4 seats (QA Executor); Stage 1–7 ↔ Q1/Q2 crosswalk row | branch rule row | Gate Q section: verdict → cleanup → closeout sequence note; Gate Q ≠ cleanup acceptance ≠ Gate D | — | review completion ≠ module certification | DEC-20 archive timely |
| ARCHITECT_PLAYBOOK | "instantiate QAM from the playbook" at packaging; contract freeze; closeout instruction | — | — | declares lanes in the pack | commissions review at the two checkpoints | — |
| ENGINEER_PLAYBOOK | completion includes QAM manifest + engineering handoff (WF-05); never fills QA results | rework on `qa/<module>` only when ruled | bounded closeout | writes only to declared lanes | — | one-shot pointer (E, open) |
| HANDOFF_PACKAGE_PLAYBOOK | handoff instructions reference `QAM/HANDOFFS/` and the indexed ZIP | — | — | lanes | — | templates pointer (N-2) |
| RECON_QUESTIONNAIRE | Q1 recon is the QAM entry (pointer) | — | Q9.3 deployment exclusion of `agent_docs/**` (N-7) | — | — | diagnostics lanes (D.3, open) |
| TESTING_PLAYBOOK | awareness pointer (credentials, privacy scans) | — | — | — | — | — |
| **DEPLOYMENT_PLAYBOOK (new)** | — | module-Git row of the matrix | deployment-exclusion rule + verification (N-7) | — | — | C.2 content open |
| **RRM_PLAYBOOK (new)** | each RRM includes QAM | continuing branch | sequence | repair contract frozen; lanes | both triggers; clean review → no RRM | reviewer section (B.2, open) |
| **QAM_PLAYBOOK (new)** | source text v1.0 | v1.0 §9, §11, §14 already state it | v1.0 §14 | v1.0 §4–5 | — | integration lines N-3…N-6 |
| MANIFEST / CHANGELOG | 3 new rows; "Pairs with" on every module-type playbook; ← recompute | — | — | — | — | — |
| Module trees / startup instructions / templates (in the playbooks above) | every module tree shows `QAM/` with `CLAUDE.md` + `AGENTS.md` + `QAM_ENTRY.md`; startup text routes QA to QAM | — | — | — | — | template set itself: N-2(a) acceptance |
| **Template set landing (AD-01; R3)** — `03_BUILD_METHODOLOGY/_templates/QAM/` (25 files, accepted version) | lands only if QA Lead-accepted; otherwise DEFERRED row with QAM-03 incomplete | — | — | — | — | **D15 cargo-path translation flagged:** playbook §5 "`TEMPLATES/QAM/`" cited in the Hub text as `03_BUILD_METHODOLOGY/_templates/QAM/`; stable filenames; set version + governing playbook version in the set README; superseded sets → `_ARCHIVE/QAM_TEMPLATES_v<version>/`; no MANIFEST row — the QAM_PLAYBOOK row's Purpose/"Pairs with" and the CHANGELOG line carry the change; **explicit template verification in the sync acceptance specification** (presence of all files, identical dual-entry routing, state/permission consistency, no prefilled results/approvals/SHAs/credentials) because lints do not recurse into the folder |

### 4b. QAM companion material inventory (R1; authorized work item 7)

| Item | Referenced by | Status | Treatment |
|---|---|---|---|
| `QAM_PLAYBOOK_v1_0.md` | Director ruling RUL-01 | **SUPPLIED** (`factory-intake/`, hash in the ruling record; outside `FILE_INDEX.json`) | Approved source; preserved unchanged; integration changes described in §4a and Group N only |
| Companion synchronization brief | v1.0 §18 ("using the companion synchronization brief") | **MISSING** — not in the package, `factory-intake/` or `~/Downloads` | Non-blocking: RUL-06's propagation list + §4a serve as the plan; Jarvis may supply the brief or accept §4a as its substitute (CL-21) |
| `TEMPLATES/QAM/` — the template set v1.0 §5 instantiates: `CLAUDE.md`, `AGENTS.md`, `QAM_ENTRY.md`, `QAM_STATE.md`, `QAM_MANIFEST.md`, `HANDOFFS/ENGINEERING_HANDOFF.md`, `QAM_PREFLIGHT.md`, `QAM_RISK_REQUIREMENTS.md`, `QAM_RECON_REPORT.md`, `QAM_TEST_PLAN.md`, `QAM_APPROVAL.md`, `QAM_EXECUTION_REPORT.md`, `AC_EVIDENCE_MATRIX.md`, `FINDINGS.md`, `QAM_CLEANUP_REPORT.md`, `QAM_CERTIFICATION.md`, `GOVERNING/`, `AUTOMATION/`, `evidence/`, `HANDOFFS/` (+ `REVIEW_START_HERE.md` and `FILE_INDEX.json` per package, §13) | v1.0 §5, §13; harvest GAP-03 / HG-03 | **R2: DRAFTED** — `../INTAKE_ADDENDUM_001_v0_2/TEMPLATES/QAM/`, 25 files covering all 22 named items plus `README.md` (ownership and duties), `QAM_PACKAGING.md` (§13 instructions) and `PARENT_ENTRY_ROUTING.md` (§6 parent routing). Every file labeled **NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED**; Engineer draft, **not QA-approved**. **R4: v0.3-draft** (`../INTAKE_ADDENDUM_001_v0_3/TEMPLATES/QAM/`) — the QA Lead accepted v0.2 with exact amendments (2026-10-14) and adopted QAM-SR v1.0; AM-1/AM-2/AM-3 applied; label now states that decision and the pending Architect verification | Was MISSING (CL-20). R2: QA Lead reviews and accepts the QA behavior (ownership stays with the QA Lead; authoring was delegated to the Engineer seat); home decided by AD-01 (R3). **R4: accepted with exact amendments; applied; Architect amendment verification pending.** Still blocks QAM-03 completion until verified and placed; never blocked the playbook text |
| Nearest existing specimens (pilot-specific, HISTORICAL): RRM-004 pack `QA/` — `AGENTS.md`, `QAM_MANIFEST.md`, `QA_ENVIRONMENT_PREFLIGHT.md`, `QA_TEST_PLAN.md`, `QA_EXECUTION_REPORT.md`, `AC_EVIDENCE_MATRIX.md`, `QAM_PILOT_CHARTER.md`, `QAM_PILOT_RESULTS.md`, `README.md`, `REPAIR_PROPOSAL.md.template` (archive-only; register row now in the addendum index with its archive-member provenance) | SRC-R02 (23 members) | SUPPLIED as evidence | Not templates; Cyber Pharma names are project examples (QAM-14). Read as vocabulary evidence for the draft set, with attribution in its `README.md`; nothing copied as "the originals" |
| `01_EVIDENCE_DOSSIER.md` | SRC-Q03 | MISSING (HG-03 / CL-15) | Evidence only; blocks nothing |
| Doctrine Journal v0.3 (J-11, J-19) | v1.0 §4, §14; SRC-Q03 | MISSING (CL-11) | No longer gates a decision (RUL-02/03 rule directly); citation substitution N-5 |
| QA Playbook v1.1 | v1.0 §4 | **SUPPLIED** = Hub `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` v1.1 (2026-08-10) | Cite by canonical name |
| QAM tooling (validator, exporter, state dispatcher, runtime adapters, skills) | v1.0 §6, §13; QAM-13 | NOT SUPPLIED; **not approved** (RUL-07) | Out of scope; `XB-EXT` if ever commissioned |

## 5. Route evidence (route-selection.md Decision A, provisional)

| Condition | Evidence | Result |
|---|---|---|
| A1 ≤ 3 intake IDs | 94 corrections + 36 harvest proposals (12 + 10 + 14) | **NO** |
| A2 ≤ 3 touch-list docs | ≥ 14 live docs in §4 before the propagation search | **NO** |
| A3 no new canonical document | **R1: three new documents ruled** — RRM_PLAYBOOK, QAM_PLAYBOOK, DEPLOYMENT_PLAYBOOK (RUL-06) | **NO** (class 3 always forces LARGE) |
| A4 no Factory-wide terminology change | seat glossary (QA Executor by ruling; Director/Operator/Coordinator), new module type "RRM", Engine 1/2 (N-1), artifact status vocabulary (FC-016) | **NO** |
| A5 no cross-correction dependency | DEC-13 spans WF-04/RRM-02/QAM-03/FC-026; DEC-07 spans WF-01/QAM-02/FC-006; RUL-02 spans RRM-06/WF-07/DEC-18 | **NO** |
| A6 no high-risk governing-rule change | auth/RBAC (CF-06), payments (CF-08/09), QA verdict authority (WF-07, QAM-02), merge/git governance (WF-10, RUL-02), credentials (QAM-07) | **NO** |
| A7 no unresolved conflict | R1: the branch rule and the cleanup order are **resolved** (RUL-02, RUL-03). Still unresolved: D.2 UI_SPEC owner (source vs Hub), C.2 DevOps authority, BIM §6 freeze wording until the RUL-04 reconciliation lands | **NO** (fewer, but not zero) |
| A8 no blocking cross-boundary change | XB items (skills, lint/CI, root, kits) are non-blocking for the Hub text; DEC-21 assigns them | YES (non-blocking) |
| A9 search bounded and complete | decided at Phase 2 | provisional |
| A10 docs-only waiver eligible | new docs + possible assets; waiver not applicable | **NO** |

**Provisional route: LARGE**, with Sol's acceptance specification and Cody's QA in separate sessions (D20) and the `INTAKE_SNAPSHOT/` taken at Gate 1 (D11). No downgrade is proposed. Execution route: local git at the Hub clone (standing ruling 2026-08-05). **R1 correction to R0:** R0 said the run's Git steps would be "run by Claudy under the Hub-only carve-out (D5)". The operator's global Rule Zero ("you never run a git command that changes anything… an explicit instruction to commit or push is NOT an exception") outranks the skill's D5 carve-out for this agent. Inside a sync run, Claudy therefore prints every Git mutation (run branch, commits, archive moves, merge) as a command block for the Director to execute; see §9 prerequisite P6.

## 6. Campaign recommendation: one coordinated campaign, with named parks

**Recommendation (PROPOSED): one coordinated intake and one UPDATE MAP covering Correction Package 001 and the approved parts of Harvest v0.1**, as DEC-01's approved form already states for the corrections.

Why one campaign and not two:
1. **Shared documents, one bump each (D22).** QA_PLAYBOOK, SFP, ENGINEER, FFM, HANDOFF, Blueprint and RECON are touched by both packages (§4). Two runs mean two archive/bump cycles and two QA lanes on the same ←-heavy docs, and a second run that cannot start until the first merges.
2. **Shared decisions.** DEC-07, DEC-13, DEC-14, DEC-18 are answered partly by harvest evidence; splitting would force the same ruling to be recorded twice.
3. **One seat glossary and one lifecycle crosswalk** (CF-01 outcome; WF-01/06) cannot be landed twice without the second run rewording the first.

Justified parks and the only split worth making:
- **Park, not split (DEFERRED rows in the one map):** any CONDITIONAL item whose ruling Tony defers — ~~A.2 branch rule, B.1(b) cadence~~ (R1: both ruled), E one-shot, B.2 reviewer doc, D.2/D.3 if deferred. They stay in the ledger as DEFERRED with the ruling that is missing; the rest of the campaign proceeds.
- ~~**The one split that materially changes shape:** if A.1 rules "QAM not now", QAM-01…14 become a later run.~~ **R1: withdrawn.** QAM is mandatory (RUL-01) and every module-type playbook must say so, which makes the QAM rows inseparable from the FFM/BIM/FIX/FEAT/RRM rows. **One campaign, no split.**
- **XB track (parallel, separate jobs; DEC-21):** `XB-SKILL` (docs-update git wording; deployment skills; kits if they are skills), `XB-LINT/CI` (FC-096 part), `XB-ROOT` (CF-17, FC-090/091/094; FILE_TREE reference), `XB-EXT` (kit verifications FC-041/042/072; RRM/QAM kits and templates if external per N-2; GAP-02 evidence export; QAM tooling if ever commissioned). None blocks the Hub text.
- **Sequencing inside the run** follows index §6 waves: BLOCKERs first (unchanged), then the harvest-dense governance/QA documents in Group 3, with new documents landed before the rows that link to them. R1: land QAM_PLAYBOOK and RRM_PLAYBOOK before the module-type playbooks that must point to them; land the SFP §2 vocabulary (QA Executor, Engine 1/2, review checkpoints) before the rows that use the terms.

What blocks the formal UPDATE MAP (R1): the Director's intake approval statement (§9 P2) and Jarvis's indexing revision (P1). What no longer blocks: Groups A and B, and C.1. What does not block and is mapped CONDITIONAL for Gate 2: C.2, D.1–D.4 remainders, E, F, N-1/N-4/N-5/N-6 wording. What blocks one item's *completion* only: N-2 templates (QAM-03).

## 7. Gaps and clarifications carried

See `INTAKE_CLARIFICATIONS_001.md`: harvest GAP-01…05 crosswalk (HG-01…HG-05), J-11 / journal v0.3 (**CL-11**), the "later 10X direction" (**CL-12**; R2: RUL-05 governs current drafting but does not authenticate this historical source, which stays MISSING for provenance), the reported DevOps Architect ruling (**CL-13**), the `REPAIR_PROPOSAL.md.template` register addendum (**clarifications §3**; it has no CL ID), the outer ZIP hash (CL-02), and the R1 additions CL-19…CL-24 (QAM playbook receipt, missing templates and companion brief, numbering note). *R0 of this section cited CL-04/05/06/07 for these items; those numbers were wrong (CL-04/05 are the status clarifications; CL-06…CL-10 were never assigned) and are corrected here.*

## 8. Self-check (read-only, Engineer seat; not QA)

- Every WF-01…12, RRM-01…10, QAM-01…14 ID appears exactly once as a primary row in §3.
- Every FC cited in §3/§4 exists in index §8 (FC-001…FC-097); every CF in §7.1; every DEC in §9; every ND in harvest index §5.
- No row changes an FC's certified fields, a DEC number, a harvest ID, or the five approvals.
- No row asserts a supersession as adopted by inference; the branch rows cite the fresh ruling RUL-02 (R1).
- ABM/APBM/Vibe Engineering: not mapped (0 Hub hits; 10X / pilot-specific). TRM: placeholder only (N-6).
- R1 consistency: no row still reads "optional QAM", "disposable QA branch" or "cleanup optional" except as quoted R0 history or as a retired source rule.

## 9. Exact next DocSet Sync step and its prerequisites (R1)

**Next step (skill README Step 3 → CLAUDE.md §2 → sync-engineer Phase 1):** the approved cargo is placed in `_INBOX/` at a Hub clone on `main` (`9c17939` or its successor), and the `sync-engineer` skill is activated for **Phase 1 — Scope**: cargo scan, `INTAKE_SNAPSHOT/` (D11), classification of every item into the eleven D16 classes, ID assignment (`IN-`, `XB-`, `GAP-<run>-NN`, `DRIFT-`), and the route decision from evidence (A1–A10; expected LARGE). Phase 2 (UPDATE MAP with propagation searches and proposed wording) follows inside the same run. **None of this starts until every prerequisite below is met and the Director says "activate".**

| # | Prerequisite | Owner | State today |
|---|---|---|---|
| P1 | Intake addendum that indexes `QAM_PLAYBOOK_v1_0.md` (hash `97e111e2…5c897`), carries the ruling record, adds the `REPAIR_PROPOSAL.md.template` register row and links both packages without replacing their IDs or histories | Claudy (delegated by Jarvis, R2) → Jarvis accepts or revises | **R3: structure accepted by Jarvis (AD-00) on v0.1. R4: the current refresh is v0.3 (`../INTAKE_ADDENDUM_001_v0_3/`): corrected templates with the QA Lead's exact amendments, AD-01, correction records 001/002, the QA Lead decision record and the Engineer verification; **R5: the v0.3 package was verified by Jarvis (2026-10-14); after the 2026-10-15 bookkeeping (verification record, provenance correction) the folder index is regenerated — one line from Jarvis confirming the final folder index closes P1** (v0.1 and v0.2 preserved). The status change from DRAFT is P2 (Director) |
| P2 | Director intake approval statement: Correction Package 001 (R3) and Harvest v0.1/0.2 approved as **one coordinated intake**, naming the DEFERRED items (C.2 remainder, D.1–D.4 remainders, E, F, B.2, N-2) that ride as CONDITIONAL rows for Gate 2 | Tony | Not done. DEC-01 approved the *form* only; the decision record and index §13 forbid an `_INBOX/` drop while either package is DRAFT |
| P3 | Confirmations N-1, N-4, N-5, N-6 wording (one line each) — or an instruction to carry them ENGINEER-PROPOSED to Gate 2 | Jarvis | Not done; non-blocking if carried to Gate 2 |
| P4 | Template set: (a) QA Lead review and acceptance of the draft's QA behavior; (b) its home; **(c, R4) Architect verification of the applied amendments**. The playbook text may land before (a)/(c), with QAM-03 marked incomplete until the set is verified and landed | (a) QA Lead · (b) Jarvis under delegation · (c) Jarvis | R3: **(b) done — AD-01 `03_BUILD_METHODOLOGY/_templates/QAM/`**. **R4: (a) decision received — ACCEPT WITH EXACT AMENDMENTS (QA Lead Fable, 2026-10-14; `../INTAKE_ADDENDUM_001_v0_3/QA_LEAD_DECISION_2026-10-14.md`); AM-1/AM-2/AM-3 + QAM-SR v1.0 applied in v0.3-draft. R5: (c) done — Architect-verified 2026-10-14, accepted under the QA Lead's decision (`../INTAKE_ADDENDUM_001_v0_3/ARCHITECT_VERIFICATION_2026-10-14.md`). (a), (b), (c) all done; template acceptance and placement settled.** QAM-03 completes when the sync run lands the set |
| P5 | Working-tree hygiene before the run: the review branch's uncommitted R3 package, `factory-intake/`, planning folder and bookkeeping are either committed by the Director or left on this branch; the run itself starts from `main` at a Hub clone (skill: "Execution environment: a Hub clone"). Command blocks will be printed on request; Claudy does not run them | Tony | Open |
| P6 | Execution convention for the run's Git steps: Claudy prints each Git block; the Director runs it; the run records the executed SHAs | Tony | **Established** (Director-executed Git; confirmed in the 2026-10-14 instruction; not reopened) |
| P7 | `_INBOX/` layout for two packages in one run (correction package folder + harvest folder + ruling record) — the skill's cargo scan treats any non-empty `_INBOX/` as presumptive cargo, so nothing enters it before P1–P2 | Claudy proposes at drop time | Not started |

## 10. External dependencies, assessed individually (R1; authorized work item 6)

"Blocks" means: prevents a correction or harvest item from reaching **actual completion** (its verification intent passing), as opposed to delaying planning or wording.

| # | Dependency | Needed by | Supplied? | Blocks planning? | Blocks actual completion of… |
|---|---|---|---|---|---|
| E-1 | Companion synchronization brief (v1.0 §18) | propagation plan | No (CL-21) | No — §4a substitutes | Nothing |
| E-2 | `TEMPLATES/QAM/` set (22 items) | QAM-03; executability of the mandatory rule | **R3: drafted v0.2** (Engineer draft corrected per the Architect review; CL-20, CL-30); home decided (AD-01). **R4: v0.3-draft** (`../INTAKE_ADDENDUM_001_v0_3/TEMPLATES/QAM/`) — QA Lead accepted v0.2 with exact amendments (CL-31), applied and Engineer-verified. **R5: Architect-verified (CL-32); supplied for the run** | No | **QAM-03 and the mandatory-QAM acceptance check** until the sync run lands the set. Playbook text lands regardless |
| E-3 | `01_EVIDENCE_DOSSIER.md` | SRC-Q03 provenance | No (CL-15) | No | Nothing |
| E-4 | Doctrine Journal v0.3 (J-11, J-19) | v1.0 §4/§14 citations; A.2 history | No (CL-11) | No — RUL-02/03 rule directly | Nothing; citation substitution N-5 |
| E-5 | QA Lead certification letter for RRM-004; final closeout/merge records | worked example (RRM-10, SFP §1.5 pairing) | No (CL-14, HG-02) | No | **Publishing RRM-004 as a certified worked example** only; no FC |
| E-6 | DevOps Architect ruling 2026-08-23 | C.2 (DEC-18, FC-011) | No (CL-13) | No | **FC-011 content** (owner/authority of deployment doctrine) and WF-08/09 content until C.2 is ruled afresh; placement already exists |
| E-7 | "Later 10X direction" historical source (harvest index §5 / WF-11, no SRC ID) | B.1(b) provenance only | **No** — still unsupplied. R2: RUL-05 governs current drafting of the review cadence and does **not** authenticate this historical source (CL-12 stays MISSING for provenance; CL-22 reworded) | No | Nothing — the cadence is ruled directly |
| E-8 | Outer harvest ZIP hash confirmation by Jarvis | CL-02 | **Unconfirmed (R3, CL-29): Jarvis's locally available harvest ZIP has a different outer hash and member count from Claudy's copy (`2b2b27e3…782`, 76 members).** Neither copy is replaced; Jarvis did not confirm Claudy's copy. The 75 extracted files match `FILE_INDEX.json`, which is the integrity basis in use | No | Nothing |
| E-9 | Package revision + Director intake approval | `_INBOX/` drop | No (P1, P2) | No | **Everything** — this is the gate to the run itself, not to any single item |
| E-10 | Kit repository access and revision (DEC-09) | FC-041/042/072 | No | No | **FC-041, FC-042, FC-072** (correction package; unchanged by R1) |
| E-11 | Hub-law check: may non-doctrine template files live in a tier folder (D15/D16)? | N-2 placement | **R3: resolved for this set by AD-01** (`03_BUILD_METHODOLOGY/_templates/QAM/`; basis in `../INTAKE_ADDENDUM_001_v0_3/TEMPLATE_PLACEMENT_RECOMMENDATION.md` (unchanged since v0.1)); a taxonomy note is an optional later `XB-SKILL` job | No | Nothing |
| E-12 | SRC-R04 / SRC-Q02 rulings cited inside v1.0 (dual entries, Q5 order) | QAM-04, QAM-11 | Yes (in package) | — | Nothing — absorbed by RUL-01's approval of the playbook |

---

*PLANNING DEPENDENCY MAP — DRAFT / NOT APPROVED. Not the UPDATE MAP. No synchronization has begun. R1 reconciled to the Director rulings of 2026-10-14; R2 applies Jarvis's corrections of the same day; R3 records AD-01 and the addendum v0.2; R4 records the QA Lead decision and the addendum v0.3; R5 records the Architect verification.*
