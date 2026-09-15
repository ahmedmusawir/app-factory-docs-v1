# UPDATE MAP — test-b-large — 2026-09-15

> **The approved execution source of truth for this synchronization run.** Authored by Claudy (Engineer seat), skill `factory-docs-update` v0.7-DRAFT. **APPROVED by Tony at Gate 2 on 2026-09-15, with the Operator rulings in §K/§O; AMENDED-v1 approved at Gate 2 on 2026-09-15 (TB-CP-004 wording consistency, §O). FROZEN.** Consumed by Sol (spec derivation), Cody (verification), and Claudy (execution, EXACTLY as approved).
>
> **TEST B — synthetic LARGE-path validation on a disposable branch.** No production doctrine decision is implied (package INDEX).
>
> Evidence labels: EVIDENCE (path:line / SHA / command output) · INFERENCE (from what) · CLAIM (package / Operator says) · GAP (looked where) · QUESTION (needs Tony). All path:line anchors are at BASE_SHA `dd6d496`. Canonical files at BASE_SHA are byte-identical to `origin/main` `0a787cb` (`git diff --name-only origin/main HEAD` over tiers/MANIFEST/CHANGELOG/_ARCHIVE/lints/.github is empty).

## 0. Run header

| Field | Value |
|---|---|
| Run ID | `SYNC_2026-09-15_test-b-large` (intake-ID run key `2026-09-15`) |
| Run branch | `test/docset-sync-v07-large-001`. It is the existing branch, named as-is. It already sits at BASE_SHA, so Phase 4 creates no new branch (D18). EVIDENCE: `git rev-parse --abbrev-ref HEAD`; no upstream; absent on origin (`git ls-remote --heads` empty) |
| BASE_SHA | `dd6d496a3b269a6bf83ce4e85101d8e0e6e785b9`. EVIDENCE: the launch message names it as "expected starting SHA / candidate BASE_SHA", and it equals the clean discovered HEAD. HEAD is 3 ahead / 0 behind `origin/main` `0a787cb`. The 3 commits touch only `_SKILLS/factory-docs-update/**` and `fable-sync-review/**`. Not main: main lacks the skill under validation. Every placement in this map was verified at this SHA |
| Merge target | **NONE — confirmed by Operator at Gate 2 (K-2).** This is a disposable validation branch. **There will be no PR and no merge from this TEST B run.** Phase 8 produces no compare URL. Background evidence: a PR from this branch to main would carry 3 out-of-scope commits (`fda59a8`, `a311924`, `dd6d496`: this family's own evolution plus a review folder) |
| Execution route | Local git at Hub clone (standing ruling 2026-08-05) |
| **Path** | **LARGE** (evidence §P) |
| QA arrangement | Independent QA lane (Sol / Cody); spec at `_AUDIT/SYNC_2026-09-15_test-b-large/DOCSET_SYNC_ACCEPTANCE_SPEC.md` (not authored by Claudy) |
| Status | **APPROVED (Gate 2, 2026-09-15) → AMENDED-v1 (Gate 2, 2026-09-15)** with Operator rulings K-1, K-2, K-3 and the TB-CP-004 wording amendment applied as written in §K / §O. FROZEN: any further change is AMENDED-v<n> and re-enters Gate 2 |
| Lint baseline (pre-existing) | **9** findings: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` :258, :261, :688, :690, :692 [VERSIONED-REFS]; `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` :8, :156 [VERSIONED-REFS]; `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` :2092 [VERSIONED-REFS]; `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` :1 [HEADER-PRESENCE]. ENCODING and RETIRED-TERMS pass (33 files = 31 tier docs + MANIFEST + CHANGELOG) |
| Live-doc count on disk / MANIFEST rows / MANIFEST stated (at BASE_SHA) | **31 / 31 / 29.** The mismatch is not caused by this run → §G DRIFT-2026-09-15-01 |

## A. Intake ledger

| ID | Class (INTAKE_TAXONOMY #) | Source | Gist | Disposition (proposed) | Gate state |
|---|---|---|---|---|---|
| TB-CP-001 | 1 APPROVED CORRECTION PACKAGE | `_INBOX/TEST_B_CORRECTION_PACKAGE/CORRECTION_001.md` | Add exact sentence `TEST-B-SYNTHETIC-01 …` to APP_FACTORY_SKILLS_PLAYBOOK, non-authority location | CHANGE | Gate 1 APPROVED (Operator test waiver, Q1(a)); Gate 2 APPROVED |
| TB-CP-002 | 1 | `…/CORRECTION_002.md` | Add exact sentence `TEST-B-SYNTHETIC-02 …` to ENGINEER_PLAYBOOK, non-authority location | CHANGE | Gate 1 APPROVED; Gate 2 APPROVED |
| TB-CP-003 | 1 | `…/CORRECTION_003.md` | Verify: family skill = one manager CLAUDE.md, no per-child CLAUDE.md | **NO-CHANGE** (approved Gate 2, 2026-09-15) | Gate 2 APPROVED |
| TB-CP-004 | 1 | `…/CORRECTION_004.md` | Verify: doctrine prevents Engineer self-approving a required human/Operator gate | **CHANGE** (minimum correction approved Gate 2 with Operator wording ruling K-3) | Gate 2 APPROVED |
| IN-2026-09-15-01 | 2 DOCTRINE JOURNAL / LESSON (content-first) | `_INBOX/odd_payload.md` | Add exact sentence `TEST-B-SYNTHETIC-03 …` to APP_FACTORY_SKILLS_PLAYBOOK, non-authority location | CHANGE | Gate 1 APPROVED; Gate 2 APPROVED |

**Package-level record.** `_INBOX/TEST_B_CORRECTION_PACKAGE/INDEX.md` has status "APPROVED FOR SYNTHETIC VALIDATION" and lists TB-CP-001…004.

**OPERATOR TEST WAIVER — TEST B ONLY** (Gate 1, 2026-09-15, Q1 ruling (a)). TB-CP-001 through TB-CP-004 are accepted as complete synthetic validation briefs despite missing confirmed-problem / evidence-ID / explicit-invariant fields (003/004 also lack a preservation field). The waiver:
- does not change the production Correction Package contract;
- does not establish Factory doctrine;
- does not permit future real correction packages to omit required fields;
- does not authorize the Engineer to invent missing doctrine intent.

In this map, invariants are read ONLY from each brief's own intent text, and nothing beyond it is added.

**IN-2026-09-15-01 classification evidence (D16, content-first).**
- Status is FLAGGED.
- Provenance: "Synthetic doctrine lesson for validation."
- Semantic form: one entry with target + placement class + exact content.
- Target doc exists.
- Filename `odd_payload.md` carries no LESSON/JOURNAL/PATCH/PROMOTION pattern and played no part in the class.
- GAP: no named retrospective or approver; FLAGGED is the only authority marker, and Tony approved scope at Gate 1.

**Parked:** XB none · GAP none · DRIFT §G.

## B. Per-ID sections

### TB-CP-001 — Synthetic sentence 01 (APP_FACTORY_SKILLS_PLAYBOOK)

- **Approved intent** (verbatim): "Add this exact synthetic validation sentence in an appropriate existing non-authority informational/history/notes location: TEST-B-SYNTHETIC-01 — LARGE-path synchronization validation only." [CLAIM: CORRECTION_001.md]
- **Must-become-true invariants** (read from intent only, per test waiver): 1. The exact string `TEST-B-SYNTHETIC-01 — LARGE-path synchronization validation only.` is present in `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md`, in an existing non-authority informational/history/notes location.
- **Preservation constraints** (verbatim): 1. "All existing governing rules." 2. "Do not rewrite or weaken existing doctrine." 3. "If the Engineer proposes any heading, wrapper, transition, or explanatory text, that additional wording is NOT part of this correction and must be exposed in the UPDATE MAP as ENGINEER-PROPOSED before Gate 2."
- **Likely affected files:** `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md`. MANIFEST ← row: FFM_PLAYBOOK (count 1; recomputed from disk, matches).
- **Propagation search** (D19). This item adds a non-authority validation marker and changes no governing rule, so the search proves absence/uniqueness and verifies the placement:
  - Terms: `TEST-B-SYNTHETIC` · `Version History` (placement)
  - Scope: `01_CONSTITUTION 02_PIPELINE_AGENTS 03_BUILD_METHODOLOGY 04_REFERENCE_MANUALS 05_DESIGN_SYSTEM MANIFEST.md CHANGELOG.md` (+ `_SKILLS/`, `_OTHERS/` read-only)
  - Command shape: `grep -rn "TEST-B-SYNTHETIC" <scope>` · `grep -n "Version History" 03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md`
  - Hit count: `TEST-B-SYNTHETIC` 0 in live scope, 0 in `_SKILLS/`/`_OTHERS/`. Outside scope, hits exist only in `_INBOX/` cargo and this run's `agent_docs/RESPONSES/` log. `Version History`: 3 in target.

  | # | Path:line | Hit (quoted) | Disposition | Drives | Label |
  |---|---|---|---|---|---|
  | 1 | APP_FACTORY_SKILLS_PLAYBOOK.md:30 | "17. [Version History](#17-version-history)" | CONSISTENT (TOC; unchanged) | — | EVIDENCE |
  | 2 | APP_FACTORY_SKILLS_PLAYBOOK.md:687 | "## Version History" | CONSISTENT. **Not a placement:** it sits inside a ```` ```markdown ```` example fence in §12 (L686–694) showing skill authors the table shape | — | EVIDENCE |
  | 3 | APP_FACTORY_SKILLS_PLAYBOOK.md:1143 | "## 17. Version History" | CHANGE. Verified placement (history, lint-exempt per `lints/lint_common.py:33`, non-authority) | §C-1 | EVIDENCE |

- **Touch-list rows:** §C-1 (row 1b).
- **Placement rationale (D13/D14).** The doc's existing non-authority history location is §17 Version History, whose rows are ordered **newest-last** (1.0 at L1147, 1.1 at L1148). D7 already requires one new Version History row for this bump, so the sentence rides inside that row. That is zero extra lines beyond the mandatory row: the minimal form. The alternative, `## Cross-References (Factory Doctrine)` (L1135), holds outbound doctrine pointers and is less apt for a validation marker.
- **CONFLICT / questions:** none. Version magnitude → §K-1 (CLARIFICATION).

### TB-CP-002 — Synthetic sentence 02 (ENGINEER_PLAYBOOK)

- **Approved intent** (verbatim): "Add this exact synthetic validation sentence in an appropriate existing non-authority informational/history/notes location: TEST-B-SYNTHETIC-02 — Independent Engineer-seat validation only." [CLAIM: CORRECTION_002.md]
- **Must-become-true invariants** (from intent only): 1. The exact string `TEST-B-SYNTHETIC-02 — Independent Engineer-seat validation only.` is present in `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`, in an existing non-authority informational/history/notes location.
- **Preservation constraints** (verbatim): 1. "All existing governing rules." 2. "Do not rewrite or weaken existing doctrine." 3. "Any Engineer-added wording must be identified separately before Gate 2."
- **Likely affected files:** `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`. MANIFEST ← row: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK (count 7; recomputed from disk, matches).
- **Propagation search:** terms `TEST-B-SYNTHETIC` (0 hits live scope; see TB-CP-001) · `Version History` in target:

  | # | Path:line | Hit (quoted) | Disposition | Drives | Label |
  |---|---|---|---|---|---|
  | 1 | ENGINEER_PLAYBOOK.md:1592 | "## Version History" | CHANGE. Verified placement (history, lint-exempt, non-authority) | §C-2 | EVIDENCE |

- **Touch-list rows:** §C-2 (row 2c).
- **Placement rationale.** The only existing history location is `## Version History` (L1592). This doc orders rows **newest-first** (1.2 at L1596, 1.1 at L1597, 1.0 at L1598), so the new row goes directly under the separator at L1595 (D7: follow the file's own order). There is no "Notes" section; Appendix A (L1433) is field lessons with narrative authority, which is less apt.
- **CONFLICT / questions:** none. Version magnitude → §K-1.

### TB-CP-003 — Verify single manager CLAUDE.md per family skill

- **Approved intent** (verbatim): "Verify whether the current canonical doctrine already establishes the rule that a family skill uses one manager CLAUDE.md and does not place separate CLAUDE.md files in each child skill. If the requirement is already fully true: propose NO CANONICAL CHANGE REQUIRED. If it is not fully true: report the evidence and propose the minimum correction in the UPDATE MAP. Do not guess." [CLAIM: CORRECTION_003.md]
- **Must-become-true invariants** (from intent only): 1. Canonical doctrine establishes that a family skill uses one manager CLAUDE.md. 2. Canonical doctrine establishes that child skills do not carry separate CLAUDE.md files.
- **Preservation constraints:** none stated in brief; per test waiver, "all existing governing rules" (as 001/002).
- **Likely affected files:** `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` (← FFM_PLAYBOOK).
- **Propagation search:**
  - Terms (T3a): `family skill|skill family|child skill|per-child|per-skill claude|single-claude|manager claude|one .?claude\.md|claude\.md.{0,20}manager|sub-?skill|_SKILLS/`
  - Terms (T3b): `CLAUDE\.md` (every mention, to catch any tree or template depicting a per-child CLAUDE.md)
  - Terms (T3c): `family` in FFM_PLAYBOOK (the only other doc governing an embedded skill)
  - Scope: live scope (+ `_SKILLS/`, `_OTHERS/` awareness)
  - Command shape: `grep -rniE "<term>" <scope>`
  - Hit count: T3b = 210 across 13 files (target 90, FFM 88, HANDOFF 9, THEMING 5, RECON 4, BIM 3, FRONTEND_BUILD 3, ARCHITECT 2, UI_UX 2, STARTER_KIT 1, ENGINEER 1, BUG_FIX 1, FEAT 1). T3a outside target: 4 (ARCHITECT :99, BIM :60, BIM :62, BUG_FIX :563; FEAT :20 also printed and is dispositioned). History: 1 (target :1147).

  **Rule-bearing hits in the target (quoted):**

  | # | Path:line | Hit (quoted) | Disposition | Label |
  |---|---|---|---|---|
  | 1 | SKILLS:147 | "Every skill folder that contains a SKILL.md must have a CLAUDE.md as its sibling or as the family-level CLAUDE.md if the skill belongs to a family." | CONSISTENT | EVIDENCE |
  | 2 | SKILLS:307 | "A family skill is a collection of related skills under one CLAUDE.md. The family CLAUDE.md orchestrates which child skill runs when. Each child skill has its own folder with its own SKILL.md (no per-child CLAUDE.md)." | CONSISTENT: states both invariants | EVIDENCE |
  | 3 | SKILLS:318–327 | "### The Single-CLAUDE.md Rule" · "there is exactly one CLAUDE.md per skill or skill family." · "For family skills, CLAUDE.md sits at the family root, above all child skills." · "Child skills in a family DO NOT have their own CLAUDE.md. They have only SKILL.md and references. The family's CLAUDE.md provides doctrine to all children." | CONSISTENT: governing statement of both invariants | EVIDENCE |
  | 4 | SKILLS:365, :379 | "├── CLAUDE.md ← family-level doctrine, ONE FILE for the whole family" · "Mandatory: family-level `CLAUDE.md`, one `SKILL.md` per child skill folder." (child trees L368–376 show SKILL.md only) | CONSISTENT | EVIDENCE |
  | 5 | SKILLS:767–773 | "### Anti-Pattern 4: Per-Skill CLAUDE.md In Family Skills" · "Correct pattern: Family CLAUDE.md only. Children have SKILL.md only. Doctrine inherits from family. No drift possible." | CONSISTENT | EVIDENCE |
  | 6 | SKILLS:821–836 | Exemplar 1 tree: family `CLAUDE.md` + children with `SKILL.md` only · "Children have only SKILL.md, no per-child CLAUDE.md (single-CLAUDE.md rule)" | CONSISTENT | EVIDENCE |
  | 7 | SKILLS:891 | "Family-skill author — model on Cloud Deployment Skills: family CLAUDE.md with orchestration rules, children with SKILL.md only" | CONSISTENT | EVIDENCE |
  | 8 | SKILLS:958–966 | Step 4 family scaffold: `touch CLAUDE.md` at family root; `cd <child-skill-1>` / `touch SKILL.md` only | CONSISTENT | EVIDENCE |
  | 9 | SKILLS:1053 | "Two-file core (CLAUDE.md + SKILL.md, both mandatory)" (Agent Skills, §16) | CONSISTENT: read with :147, a family child's CLAUDE.md is the family-level one; §16 also inherits "Folder layout standards" (:1055) | EVIDENCE + INFERENCE |

  **All other target hits:** SKILLS :17 :101 :103 :104 :116 :121 :123 :131 :135 :143 :150 :155 :157 :181 :203 :217 :223 :225 :255 :265 :293 :316 :320 :322 :323 :325 :339 :342 :358 :392 :400 :425 :521 :534 :536 :546 :590 :684 :712 :722 :736 :746 :753 :757 :759 :761 :763 :765 :775 :777 :779 :781 :791 :793 :795 :797 :832 :835 :839 :849 :884 :890 :940 :952 :961 :968 :970 :972 :982 :1015 :1017 :1058 :1071 :1126 :1127.
  - Disposition: **CONSISTENT**. They describe CLAUDE.md's role, contract, length, activation, single-skill layout, the Migration exemplar (single skill), AP-1/2/3/5/7, and authoring steps.
  - None depicts or permits a per-child CLAUDE.md. :181 "For family skills, this tree includes the family-level CLAUDE.md and all child skill folders"; :203 "The CLAUDE.md is responsible for orchestration — child skills do not orchestrate each other"; :536 "reads the CLAUDE.md at the skill root (single skill) or family root (family skill)".
  - SKILLS :1147 (v1.0 VH row "Specifies single skill and family skill structures") = **HISTORY**.

  **Hits outside the target:**

  | # | Path:line | Hit (quoted / summarized) | Disposition | Label |
  |---|---|---|---|---|
  | 10 | FFM_PLAYBOOK.md:293–299, :1118–1141, :2098–2101 | `skills/stark-frontend-first/` tree: `CLAUDE.md ← skill doctrine` + `SKILL.md` at the skill root | CONSISTENT: a **single** skill (SKILLS §6 Single Skill: "one CLAUDE.md and one SKILL.md at the root"), not a family child | EVIDENCE |
  | 11 | FFM_PLAYBOOK.md:467 | "**Family folder names** (for skill families): SHOUTING_SNAKE (`CLOUD_DEPLOYMENT_SKILLS`)" | CONSISTENT (naming only) | EVIDENCE |
  | 12 | FFM_PLAYBOOK.md other CLAUDE.md hits (:57 :268 :270 :271 :274 :295 :329 :344 :356–359 :433 :553 :557 :560 :569 :574 :577 :589 :618 :620 :669 :695 :706 :708 :715 :726 :728 :733 :741 :772 :900 :942 :946 :1089 :1122 :1142 :1149 :1151 :1163 :1396 :1502 :1542 :1652 :1656 :1658 :1663 :1666 :1678 :1693 :1699 :1701 :1750 :1773 :1774 :1776 :1801 :1808 :1809 :1851 :1853 :1854 :1861 :1873 :1904 :1905 :1908 :2017 :2024 :2039 :2072 :2078 :2100 :2152 :2154 :2163 :2195 :2196 :2208 :2240 :2243 :2286 :2296 :2515 :2518 :2520 :2570) | FFM module `_project/CLAUDE.md` spine, the single `stark-frontend-first/CLAUDE.md`, Brain Drain single-skill boot lines, templates | CONSISTENT: no family skill with per-child CLAUDE.md is described (T3c: the only "family" hit is #11) | EVIDENCE |
  | 13 | BIM_PLAYBOOK.md:50, :60, :62 | "## 5. The Manager File (CLAUDE.md) — one module, one manager" · "Every module folder carries exactly one `CLAUDE.md`." | CONSISTENT (module analog of the single-manager rule; modules are not skill families) | EVIDENCE |
  | 14 | BUG_FIX_PLAYBOOK.md:563 · FEAT_PLAYBOOK.md:20 | "one folder, one `CLAUDE.md` manager" · module-identity pointer | CONSISTENT (module doctrine) | EVIDENCE |
  | 15 | ARCHITECT_PLAYBOOK.md:83, :99 | `_project/CLAUDE.md` · "point the Engineer at `_SKILLS/stark-recon/CLAUDE.md`" | CONSISTENT (single skill root CLAUDE.md) | EVIDENCE |
  | 16 | HANDOFF_PACKAGE_PLAYBOOK.md :30 :211 :215 :265 :267 :276 :292 :324 :347 · RECON_QUESTIONNAIRE.md :143 :211 :298 :299 · ENGINEER_PLAYBOOK.md:164 · STARTER_KIT_HANDBOOK.md:246 · FRONTEND_BUILD_PHASE_PLAYBOOK.md :53 :65 :208 · THEMING_MANUAL.md :48 :102 :112 :260 :272 · UI_UX_BUILDING_MANUAL.md :128 :2094 | project spine `_project/CLAUDE.md` / repo-root CLAUDE.md / Rule Zero | CONSISTENT: different artifact (project instructions, not skill structure) | EVIDENCE |
  | 17 | `_SKILLS/factory-docs-update/CLAUDE.md:6, :86` | "This is the ONE CLAUDE.md for the family; children carry only SKILL.md…" · "No per-child CLAUDE.md exists or may be created (Skills Playbook Anti-Pattern 4)." `find _SKILLS _OTHERS -name CLAUDE.md` → only `_SKILLS/factory-docs-update/CLAUDE.md` | OUT-OF-SCOPE (awareness §I): CONSISTENT | EVIDENCE |

- **Touch-list rows:** none.
- **NO-CHANGE proposal:** the intent is already fully true. Governing statement at `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md:318–327` (The Single-CLAUDE.md Rule): "there is exactly one CLAUDE.md per skill or skill family … For family skills, CLAUDE.md sits at the family root, above all child skills. Child skills in a family DO NOT have their own CLAUDE.md." It is reinforced at :307, :365, :379, :767–773 (Anti-Pattern 4), :836, :891, :958–966. The search found no contradicting active guidance in live scope. **APPROVED by Operator at Gate 2, 2026-09-15.**
- **CONFLICT / questions:** none.

### TB-CP-004 — Verify Engineer cannot self-approve a required human/Operator gate

- **Approved intent** (verbatim): "Verify whether the current canonical doctrine already prevents an Engineer from self-approving a required human/Operator gate. If already fully true: propose NO CANONICAL CHANGE REQUIRED. If not: report the evidence and propose the minimum correction in the UPDATE MAP. Do not guess." [CLAIM: CORRECTION_004.md]
- **Must-become-true invariants** (from intent only): 1. Canonical doctrine prevents an Engineer from self-approving a required human/Operator gate.
- **Preservation constraints:** none stated; per test waiver, "all existing governing rules".
- **Likely affected files:** `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` (← 7 listed above).
- **Propagation search:**
  - T4a `self[- ]?approv` — 1 hit
  - T4b `self[- ]?certif` — 1
  - T4c `approve (its|his|their) own|own (gate|approval|exam)|grade (his|its|their) own|write (his|its|their) own exam` — 3
  - T4d `human approval|operator approval|human gate|operator gate|human checkpoint` — 22
  - T4e `silence is not approval|tacit silence|not approval|explicit(ly)? approv|awaiting (your )?approv|wait(s)? for (explicit )?approv|until .{0,30}approv` — 13
  - T4f (target doc, broad) `approv|gate|checkpoint|proceed|redirect|sign-?off|\bhuman\b|operator|tony` — 34 lines
  - T4g `grades his own paper|Stop means stop` — 2
  - T4h (mirror check) `executing unless you redirect|or I'll proceed` — 2, both in target
  - Scope: live scope (+ `_SKILLS/` awareness for T4a/T4b)
  - Command shape: `grep -rniE "<term>" <scope>`

  **Rule-bearing hits:**

  | # | Path:line | Hit (quoted) | Disposition | Label |
  |---|---|---|---|---|
  | 1 | QA_PLAYBOOK.md:193–201 | "## Engineer … The Engineer: … self-verifies, … provides the completion handoff, - does not self-approve release." | CONSISTENT, **partial**: covers the *release* gate only | EVIDENCE |
  | 2 | QA_PLAYBOOK.md:1634–1638 | "## Engineer Self-Certification … Not a QA verdict." | CONSISTENT, partial (QA verdict only) | EVIDENCE |
  | 3 | BIM_PLAYBOOK.md:29, :32 | "**Engineer (Claudy)** \| Plan Mode first, builds after approval …" · "The Engineer never grades his own paper." | CONSISTENT, partial (BIM modules) | EVIDENCE |
  | 4 | BIM_PLAYBOOK.md:108, :114 | "## 7. Standing Engineer Doctrine (bake into every manager)" · "**Stop means stop.** Momentum after a stage gate is the enemy; the next stage begins only on the Coordinator's plain words." | CONSISTENT, partial (module managers: BIM, and by inheritance FEAT) | EVIDENCE |
  | 5 | SOFTWARE_FACTORY_PLAYBOOK.md:250–251 | "The **Operator holds final adjudication and release authority.**" · "Only documentation-only / non-runtime changes may receive a recorded Operator QA waiver." | CONSISTENT, partial (release / QA waiver) | EVIDENCE |
  | 6 | SOFTWARE_FACTORY_PLAYBOOK.md:54, :89 | "Reviews and approves deliverables" (HUMAN) · "**Spec-Driven** \| No implementation without approved spec" | CONSISTENT: allocates approval to the human, but no explicit self-approval prohibition | EVIDENCE |
  | 7 | APP_FACTORY_BLUEPRINT.md:6, :14–15, :133, :141, :150 | "with human approval gates" · "YOU (TONY STARK) … Commander / Final Approver" · "Checkpoint: You approve APP_BRIEF ✓" … | CONSISTENT: gates are human-owned by allocation. INFERENCE only: allocation implies no self-approval; not stated | EVIDENCE + INFERENCE |
  | 8 | FFM_PLAYBOOK.md:210–213, :927 | "**With:** Operator (you) at every approval gate." · "**Approval gates explicit** — Claudy stops at each one and waits for operator approval." | CONSISTENT, partial (FFM runs; :927 is manager-authoring guidance) | EVIDENCE |
  | 9 | APP_FACTORY_SKILLS_PLAYBOOK.md:566–570, :599, :611, :615 | "The agent does NOT proceed until the operator says APPROVED" · "Tacit silence is NOT approval." · "No execution until APPROVED is on the table." | CONSISTENT, partial (skill-activated agents) | EVIDENCE |
  | 10 | HANDOFF_PACKAGE_PLAYBOOK.md:293–295 | "**Operator has explicitly approved** … Until all four files are approved, Claudy does not start Phase 0 Discovery on the build." | CONSISTENT, partial (conversion package gate) | EVIDENCE |
  | 11 | ENGINEER_PLAYBOOK.md:90–97 | "### What the Engineer Does NOT Do" · "\| Make product decisions \| Human (Tony Stark) \|" | **CHANGE** (approved): the Engineer's own role-limits table has no gate-approval row → new row owner "Required human/Operator" (K-3) | §C row 2b · EVIDENCE |
  | 12 | ENGINEER_PLAYBOOK.md:174–189 | "- [ ] APP_BRIEF is APPROVED · - [ ] UI_SPEC is APPROVED · … - [ ] Human checkpoints are identified … If any item is missing: STOP. Surface to the operator" | CONSISTENT, partial (input approvals; checkpoints identified, not an approval rule) | EVIDENCE |
  | 13 | ENGINEER_PLAYBOOK.md:1170–1173, :1185 | "1. **STOP.** Do not proceed with a guess. … 4. Wait for resolution before continuing." · "Accept their decision if they override" | CONSISTENT | EVIDENCE |
  | 14 | ENGINEER_PLAYBOOK.md:1161 | "→ Correct me now or I'll proceed with these." | CONSISTENT (assumption surfacing, not a required gate). **CONCERN** noted: proceed-by-default phrasing; unchanged (minimal form; §15 is ALL-AGENT doctrine, D-011) | EVIDENCE + INFERENCE |
  | 15 | ENGINEER_PLAYBOOK.md:1241 | "→ Executing unless you redirect." (Inline Planning Format) | CONSISTENT (inline plan for multi-step tasks, not a required gate). **CONCERN** as #14 | EVIDENCE + INFERENCE |

  **All other hits:** CONSISTENT, since none permits an Engineer to approve a gate. Two are OUT-OF-SCOPE awareness.
  - **T4a–T4e:** SFP :238, :351, :352 · ARCHITECT :324, :596 · DESIGNER :152, :177 · SKILLS :1075, :1115 · BIM :40 · BUG_FIX :324, :569, :187 · BIM :120 (Engineer "may not silently add, remove, weaken, or redefine an acceptance requirement — any scope change requires approval") · FFM :110, :120, :980, :1381, :2211, :2223 · QA :92 · GDSH :104, :122 · MANIFEST :18 · ENGINEER :1210.
  - **T4f remainder (target doc):** :82, :139, :143, :161, :171, :262–263, :277, :284, :310, :361, :579, :732, :741, :1147, :1149, :1180, :1202, :1276, :1342, :1449, :1533, :1584, :1586.
  - **Awareness (OUT-OF-SCOPE):** `_SKILLS/factory-docs-update/CLAUDE.md:22, :134` · `_shared/references/ANTI_PATTERNS.md:57` (self-certification) → §I.

- **Finding (EVIDENCE).** The intent is **NOT fully true**:
  - Canonical doctrine forbids self-approval only for specific gates or module types: release (QA :201), QA verdict (QA :1634), BIM/FEAT module stage gates (BIM :29/:32/:114), skill-activated agents (SKILLS §9–§10), and FFM gates (FFM :213/:927). It also allocates approval to the human generally (Blueprint :15; SFP :54).
  - No canonical sentence states the general rule for the Engineer, and ENGINEER_PLAYBOOK, the Engineer's own playbook and the brief's target, is silent on it.
  - Its §15 patterns (:1161, :1241) default to proceeding. They are not about required gates, but nothing in the doc distinguishes the two.
- **Approved minimum correction (Gate 2, K-3):** one table row in ENGINEER_PLAYBOOK §1 "What the Engineer Does NOT Do", placed after L96 (§C row 2b).
  - The action cell is ENGINEER-PROPOSED, approved; it comes from the brief's phrase "self-approving a required human/Operator gate".
  - The owner cell is **OPERATOR-SPECIFIED**: "Required human/Operator". It replaces the proposed "Human (Tony Stark)". Operator's reason: do not hard-code Tony as the universal gate authority.
  - No other doctrine is added.
- **Alternative NO-CHANGE:** not chosen (K-3 ruled).
- **CONFLICT:** none. The row is additive and agrees with every hit above.

### IN-2026-09-15-01 — Synthetic sentence 03 (APP_FACTORY_SKILLS_PLAYBOOK)

- **Approved intent** (verbatim): "Add this exact synthetic validation sentence in an appropriate existing non-authority informational/history/notes location: TEST-B-SYNTHETIC-03 — Content-first intake classification validation only." [CLAIM: `_INBOX/odd_payload.md`, FLAGGED]
- **Must-become-true invariants:** 1. The exact string `TEST-B-SYNTHETIC-03 — Content-first intake classification validation only.` is present in `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md`, in an existing non-authority informational/history/notes location.
- **Preservation constraints** (verbatim): 1. "All existing governing rules."
- **Propagation search:** as TB-CP-001 (`TEST-B-SYNTHETIC` 0 hits; placement §17 L1143 verified).
- **Touch-list rows:** §C-1 (row 1b, shared with TB-CP-001; one bump per doc per run, D22).
- **Cross-item note (A5):** TB-CP-001 and this entry share one placement row but not an invariant. Neither depends on or collides with the other.

## C. Touch list (lightest ← first)

`<EXEC_DATE>` = the Phase 4 execution date (YYYY-MM-DD), written identically in header, Version History row, MANIFEST row and CHANGELOG row. This is mechanical per D7. Version numbers are fixed by **Operator test ruling K-1** (TEST B only).

All rows below are **APPROVED at Gate 2**; row 2b carries the Operator's replacement owner cell.

| # | Canonical doc (path) | ← | Placement — VERIFIED at BASE_SHA | Proposed wording / exact edit (spans marked) | IDs | Version | Archive | Structural? | Minimal-form note (D14) |
|---|---|---|---|---|---|---|---|---|---|
| **1a** | `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` | 1 | L3 header line | Replace L3 with: `> **Version:** 1.2 · **Date:** <EXEC_DATE> · **Status:** Active` [MECHANICAL, D7] | TB-CP-001, IN-2026-09-15-01 | 1.1 → **1.2** (K-1 Operator test ruling) | YES → `_ARCHIVE/APP_FACTORY_SKILLS_PLAYBOOK_v1_1.md` | NO | header only |
| **1b** | same | 1 | `## 17. Version History` table: append new last row directly after L1148 (the v1.1 row), before the blank L1149. File order is newest-last | New line, exactly: `\| 1.2 \| <EXEC_DATE> \| **TEST B synthetic validation (TB-CP-001, IN-2026-09-15-01; TB-CP-003 verified — no change).** TEST-B-SYNTHETIC-01 — LARGE-path synchronization validation only. TEST-B-SYNTHETIC-03 — Content-first intake classification validation only. \|`<br>Spans: `\| 1.2 \| <EXEC_DATE> \|` and the closing ` \|` = MECHANICAL (D7 row) · `**TEST B synthetic validation (TB-CP-001, IN-2026-09-15-01; TB-CP-003 verified — no change).**` = **ENGINEER-PROPOSED** · `TEST-B-SYNTHETIC-01 — LARGE-path synchronization validation only.` = **INTAKE-VERBATIM** (TB-CP-001) · `TEST-B-SYNTHETIC-03 — Content-first intake classification validation only.` = **INTAKE-VERBATIM** (IN-2026-09-15-01) | TB-CP-001, IN-2026-09-15-01 (TB-CP-003 cited) | — | — | NO | +1 line; the mandatory D7 row carries both sentences; no body text touched |
| **2a** | `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` | 7 | L3 header line | Replace L3 with: `> **Version:** 1.3 · **Date:** <EXEC_DATE> · **Status:** Active` [MECHANICAL] | TB-CP-002, TB-CP-004 | 1.2 → **1.3** (K-1 Operator test ruling) | YES → `_ARCHIVE/ENGINEER_PLAYBOOK_v1_2.md` | NO | header only |
| **2b** | same | 7 | §1 → `### What the Engineer Does NOT Do` table (L90–97): insert one row after L96 (`\| Make product decisions \| Human (Tony Stark) \|`), before L97 (`\| Operate production systems \| Operations / SRE \|`) | New line, exactly: `\| Self-approve a required human/Operator gate \| Required human/Operator \|`<br>Spans:<br>- Action cell `Self-approve a required human/Operator gate` = **ENGINEER-PROPOSED, APPROVED** (derived from the CORRECTION_004 intent phrase).<br>- Owner cell `Required human/Operator` = **OPERATOR-SPECIFIED at Gate 2 (K-3)**. It replaces the proposed `Human (Tony Stark)`; do not hard-code Tony as the universal gate authority.<br>- Table pipes = MECHANICAL. The Operator's dash notation "gate — Required human/Operator" is rendered as the table's two cells. | TB-CP-004 | — | — | NO | +1 table row in an existing Engineer-specific table; §15 Karpathy (ALL-AGENT, D-011) deliberately untouched |
| **2c** | same | 7 | `## Version History` (L1592): insert new first data row directly after the separator L1595, above the v1.2 row L1596. File order is newest-first | New line, exactly: `\| 1.3 \| <EXEC_DATE> \| **TEST B synthetic validation (TB-CP-002, TB-CP-004).** TEST-B-SYNTHETIC-02 — Independent Engineer-seat validation only. Clarified that a required human/Operator gate may not be self-approved by the Engineer. \|`<br>Spans:<br>- `\| 1.3 \| <EXEC_DATE> \|` / ` \|` = MECHANICAL.<br>- `**TEST B synthetic validation (TB-CP-002, TB-CP-004).**` = **ENGINEER-PROPOSED, APPROVED at Gate 2**.<br>- `TEST-B-SYNTHETIC-02 — Independent Engineer-seat validation only.` = **INTAKE-VERBATIM** (TB-CP-002).<br>- `Clarified that a required human/Operator gate may not be self-approved by the Engineer.` = **OPERATOR-SPECIFIED (Gate 2 AMENDED-v1)**, using the Operator's example sentence verbatim. It replaces the struck clause `§1 "What the Engineer Does NOT Do" gains one row: self-approving a required human/Operator gate belongs to the Human (TB-CP-004).`<br>(The earlier NO-CHANGE variant of this row is void: K-3 ruled CHANGE.) | TB-CP-002, TB-CP-004 | — | — | NO | +1 line |

Totals: 2 canonical docs · 6 edit rows (+3 lines, 2 header replacements) · 2 archives.

**Lint pre-check of proposed text (INFERENCE from lint sources):**
- No versioned filename or prose reference such as `NAME_v1.2.md` or `NAME v1.2` (VERSIONED-REFS).
- No retired term; the only one is `stitch`, per `lints/retired_terms_lint.py:11`.
- The em-dashes are ordinary U+2014, as already used in both files (ENCODING).
- Header lines keep the single-line format (HEADER-PRESENCE).

## D. New canonical files

None.

## E. Stale / superseded material

None in scope.

Observation, not actioned (OUT-OF-SCOPE for this intake): `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:250` reads "Agent-conduct doctrine (the Karpathy Protocol, D-011) lands with the ENGINEER_PLAYBOOK rewrite — pointer reserved here." ENGINEER_PLAYBOOK v1.2 (§15, L1141) already landed that rewrite. It is a stale forward-reference in an untouched doc, content rather than a derived field, so it gets no DRIFT ID. It is noted for a follow-up job.

## F. Dependents checked, unchanged

| Doc / location (path:line) | Kind | Why checked | Verdict |
|---|---|---|---|
| FFM_PLAYBOOK.md:4 (sole ← of APP_FACTORY_SKILLS_PLAYBOOK) · :1114–1238 (§11 `skills/` authoring guide) | role instruction / template | TB-CP-001, IN-…-01, TB-CP-003: does FFM cite a Skills Playbook version, section, or VH? | CONSISTENT. Cites by canonical name only (:4); §11 structure matches single-skill law (:1121–1123 "CLAUDE.md ← skill doctrine (always-on)" + "SKILL.md"). No section numbers of the Skills Playbook change |
| APP_FACTORY_BLUEPRINT.md:4, :51, :96, :248, :250 | summary / router | ENGINEER_PLAYBOOK dependent; TB-CP-004 authority allocation | CONSISTENT. :96 "`ENGINEER_PLAYBOOK.md` \| How to BE the Engineer agent" · :15 "Commander / Final Approver" agrees with row 2b. (:250 stale forward-ref → §E observation) |
| DESIGNER_PLAYBOOK.md:4, :152, :177 | role instruction | ENGINEER_PLAYBOOK dependent; approval gates | CONSISTENT. "Human approval gate: lock before proceeding." |
| HANDOFF_PACKAGE_PLAYBOOK.md:4, :17, :293–295 | checklist | ENGINEER_PLAYBOOK dependent; approval gate | CONSISTENT. "Operator has explicitly approved … Until all four files are approved, Claudy does not start" |
| QA_PLAYBOOK.md:5, :193–201, :1634 | role instruction / anti-pattern | ENGINEER_PLAYBOOK dependent; TB-CP-004 | CONSISTENT. "does not self-approve release." (row 2b generalizes; no contradiction) |
| BUG_FIX_PLAYBOOK.md:5, :62–72 | role instruction | ENGINEER_PLAYBOOK dependent; Engineer role list | CONSISTENT. "The Engineer runs zero git and zero cloud commands. He builds, tests, self-verifies, and hands the Coordinator …" |
| BIM_PLAYBOOK.md:6, :29, :32, :114 | role instruction / manager doctrine | ENGINEER_PLAYBOOK dependent; TB-CP-004 | CONSISTENT. "Stop means stop … the next stage begins only on the Coordinator's plain words." |
| ENGINEER_PLAYBOOK.md:174–189 (Pre-Flight Checklist), :1552–1566 (The Engineer's Checklist) | checklist / quick reference | TB-CP-004: do the in-doc checklists restate the Engineer's limits? | CONSISTENT; no gate-approval item exists to contradict row 2b. Minimal form keeps them unchanged |
| ENGINEER_PLAYBOOK.md:1139–1276 (§15 Karpathy Protocol) | role instruction (ALL-AGENT) | TB-CP-004 | CONSISTENT, with CONCERN (:1161, :1241 proceed-by-default phrasing) → not changed; flagged at Gate 2 |
| ENGINEER_PLAYBOOK.md:11–47 (TOC) · APP_FACTORY_SKILLS_PLAYBOOK.md:12–30 (TOC) | index | row insertions don't renumber sections | CONSISTENT: no heading added, removed, or renumbered |

## G. Infra and index effects (caused by this run)

| Item | Expected change | Check at Gate 4 / AC-I |
|---|---|---|
| MANIFEST rows | `MANIFEST.md:39` APP_FACTORY_SKILLS_PLAYBOOK: Version `1.1`→`1.2`, Date `2026-07-08`→`<EXEC_DATE>`; Status, Purpose, Pairs-with unchanged. `MANIFEST.md:31` ENGINEER_PLAYBOOK: Version `1.2`→`1.3`, Date `2026-07-07`→`<EXEC_DATE>`; rest unchanged. Values FROM the new headers | header vs row equality for both docs |
| MANIFEST header | `MANIFEST.md:3` Date `2026-07-12`→`<EXEC_DATE>`; Version `1.0` unchanged; NOT archived (Ruling 7) | header Date = EXEC_DATE; no `_ARCHIVE/MANIFEST*` |
| MANIFEST live-doc count | **Unchanged.** No canonical doc added or removed. `:6`, `:12`, `:76` stay byte-equal to BASE (drift parked) | byte-equal to BASE |
| MANIFEST ← dependency map | **Unchanged.** No Pairs-with changed. Rows for both target docs recompute correctly already | byte-equal to BASE |
| MANIFEST appendix | **Unchanged** (scope not changed by this run) | byte-equal to BASE |
| CHANGELOG | Append 2 rows to "## Ongoing entries" after L34 (last row), format per `CHANGELOG.md:22` `\| date \| doc vX.Y \| one-line change \| finding/lesson IDs \|` (see exact rows below); header `CHANGELOG.md:3` Date `2026-07-12`→`<EXEC_DATE>`; NOT archived | exactly 2 new rows; IDs in last column |
| README / index files | none | — |

**CHANGELOG rows** (APPROVED at Gate 2; the one-line change text in each is **ENGINEER-PROPOSED, APPROVED**, and the IDs column is mechanical):
1. `| <EXEC_DATE> | APP_FACTORY_SKILLS_PLAYBOOK v1.2 | TEST B synthetic validation: TEST-B-SYNTHETIC-01 and -03 added in §17 Version History (non-authority); single-CLAUDE.md family rule verified already true, no change | TB-CP-001, TB-CP-003, IN-2026-09-15-01 |`
2. `| <EXEC_DATE> | ENGINEER_PLAYBOOK v1.3 | TEST B synthetic validation: TEST-B-SYNTHETIC-02 added in Version History (non-authority); §1 "What the Engineer Does NOT Do" gains row: no self-approval of a required human/Operator gate | TB-CP-002, TB-CP-004 |`
**Pre-existing / baseline drift (D7)**

| ID | Location (path:line at BASE_SHA) | Stale value vs disk truth (EVIDENCE) | Caused by this run? | Disposition |
|---|---|---|---|---|
| DRIFT-2026-09-15-01 | `MANIFEST.md:6`, `:12`, `:76` | States "29" live docs; disk `ls 0?_*/*.md` = 31; MANIFEST tables = 31 rows. Already wrong in the commit that wrote it (`ff2e772`, whose tree has 31) | NO | **PARKED → follow-up (Operator-confirmed at Gate 2: remains parked and untouched).** Not on the touch list; byte-unchanged |
| DRIFT-2026-09-15-02 | `MANIFEST.md:114` | "scanning all 27 bodies"; live bodies = 31 | NO | **PARKED → follow-up** |
| DRIFT-2026-09-15-03 | `MANIFEST.md:83` | ← row for APP_FACTORY_BLUEPRINT lists FFM_PLAYBOOK, count 7. `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:4` Pairs-with omits APP_FACTORY_BLUEPRINT (MANIFEST `:40` agrees; appendix `:125` lists it undeclared). Disk-derived set = 6 | NO | **PARKED → follow-up** |
| DRIFT-2026-09-15-04 | `MANIFEST.md:3` | Header Date `2026-07-12` (`git blame` → `228122b`) while content changed in 7 later commits (2026-08-05 … `ff2e772` 2026-08-10) | NO (stale at BASE) | **CLEARED by §G header Date bump — Operator-confirmed at Gate 2.** It may be overwritten ONLY because this approved run itself updates MANIFEST and therefore legitimately updates its header Date (D7/Ruling 7). It is not an unrelated repair |
| DRIFT-2026-09-15-05 | `CHANGELOG.md:3` | Header Date `2026-07-12` (`228122b`) while rows were appended 2026-08-05 and 2026-08-10 | NO (stale at BASE) | **CLEARED by §G header Date bump — Operator-confirmed at Gate 2** (same basis as -04: this approved run itself updates CHANGELOG) |

Not recorded as drift (observations):
- MANIFEST Status cells abbreviate three long header statuses (RECON_QUESTIONNAIRE `:33`, BUG_FIX `:44`, QA `:46`) to their lead word. INFERENCE: abbreviation convention; not touched.
- STARTER_KIT_HANDBOOK's missing header is footnoted at `:22` and in the lint baseline.

## H. Paths, links, assets

| Reference (as written) | In doc | Resolves at BASE_SHA? | Resolves after? | Asset | IDs |
|---|---|---|---|---|---|
| §1 "What the Engineer Does NOT Do" (section citation inside row 2c) | ENGINEER_PLAYBOOK VH | YES: `### What the Engineer Does NOT Do` L90 under `## 1. Role Definition` L57 | YES (no heading change) | none | TB-CP-004 |
| §17 Version History (section citation in CHANGELOG row 1) | CHANGELOG | YES: APP_FACTORY_SKILLS_PLAYBOOK L1143 | YES | none | TB-CP-001, IN-…-01 |

No backtick filenames, folder paths, or images are added.

## I. Skill references (read-only awareness)

| Skill file (path) | What it cites that this run changes | Disposition |
|---|---|---|
| `_SKILLS/factory-docs-update/CLAUDE.md:26, :86, :88, :98, :178` | Skills Playbook Anti-Pattern 1, Anti-Pattern 4, §15 step 10, naming convention, "Skills Playbook's authoring discipline" | CONSISTENT. Cited sections are unchanged by row 1b; TB-CP-003 NO-CHANGE keeps Anti-Pattern 4 as cited |
| `_SKILLS/factory-docs-update/README.md:98`; `_shared/references/ANTI_PATTERNS.md:34–35, :57` | Skills Playbook by name; self-certification | CONSISTENT |
| `_OTHERS/MASTER_DOC_LIST_v1_0_FINAL.md:41, :49` | versioned legacy names `2_AGENTS-ENGINEER_PLAYBOOK_v1_1.md`, `3_METHOD-APP_FACTORY_SKILLS_PLAYBOOK.md` | OUT-OF-SCOPE (non-canonical historical list); not edited |

## J. Parked cross-boundary / cross-repo items

None. No §J item is required for success.

## K. Unresolved Operator decisions

| ID | Type | Question (smallest necessary) | Evidence (checked on disk first) | Affects | Ruling |
|---|---|---|---|---|---|
| K-1 | CLARIFICATION — **RULED** | Version bump size: minor (Skills Playbook 1.1→**1.2**, Engineer Playbook 1.2→**1.3**, proposed) or patch (1.1.1 / 1.2.1)? | No governing rule defines magnitude (skill CLAUDE.md v0.7 VH: "Version-bump magnitude (TESTA-F03) deferred"). Hub precedent is mixed. Lesson-style promotions went minor for STATE_MANAGEMENT_MANUAL v1.1→v1.2 and AUTH_MANUAL v1.3→v1.4 (`eb08ec6`, `1b5fc42`) and for the QA_PLAYBOOK v1.0→v1.1 sync; FRONTEND_BUILD_PHASE_PLAYBOOK v1.2.1→v1.2.2 went patch (`4148df5`). Minor proposed as the majority precedent | Header/MANIFEST/CHANGELOG/VH values, archive suffixes unaffected (they come from the live headers) | **OPERATOR TEST RULING (Gate 2, 2026-09-15):** APP_FACTORY_SKILLS_PLAYBOOK 1.1 → 1.2; ENGINEER_PLAYBOOK 1.2 → 1.3, **for TEST B only**. It does NOT establish a Factory-wide rule for version-bump magnitude; **TESTA-F03 remains deferred.** |
| K-2 | CLARIFICATION — **RULED** | Confirm merge target = **NONE** (disposable validation, no PR), rather than `main`? | §0 evidence: 3 out-of-scope commits between main and BASE_SHA; launch message calls the branch disposable. The skill template expects `main` for a production sync; this run is not one | Phase 8 compare URL / whether a PR exists | **Confirmed (Gate 2): MERGE TARGET = NONE.** Disposable validation branch. **No PR or merge from this TEST B run.** |
| K-3 | Gate 2 row decision (not a CONFLICT) — **RULED** | TB-CP-004: approve the **minimum correction** (§C row 2b) or rule **NO-CHANGE**? | §B TB-CP-004 finding: the rule is explicit only for release/QA verdict/BIM-FEAT gates/skill agents/FFM gates; absent in ENGINEER_PLAYBOOK, whose §15 defaults to proceed. Claudy proposes the correction and does not adjudicate | Rows 2b, 2c text, CHANGELOG row 2; route condition A6 | **Canonical change APPROVED (Gate 2)**, with the owner cell replaced: proposed "Self-approve a required human/Operator gate — Human (Tony Stark)" → approved "Self-approve a required human/Operator gate — Required human/Operator". Reason: do not hard-code Tony as the universal gate authority. All other Engineer-proposed wording APPROVED. |

No CONFLICT rows.

## L. Preservation constraints (all IDs, consolidated)

| Constraint (verbatim) | Source ID | Where it lives (path:line at BASE_SHA) | How QA will check (AC-P) |
|---|---|---|---|
| "All existing governing rules." | TB-CP-001, TB-CP-002, IN-2026-09-15-01 (and TB-CP-003/004 per Operator test waiver) | Both target docs in full; specifically SKILLS :318–327 (Single-CLAUDE.md Rule), :767–773 (AP-4), §9–§10 (:508–642); ENGINEER :90–97 (existing rows), §15 :1139–1276, :174–189 | Diff of each target doc at candidate vs BASE contains ONLY §C rows 1a/1b/2a/2b/2c; no deleted or modified pre-existing line other than the two L3 header lines |
| "Do not rewrite or weaken existing doctrine." | TB-CP-001, TB-CP-002 | same | same, plus the quoted rule lines grep-present unchanged |
| "If the Engineer proposes any heading, wrapper, transition, or explanatory text, that additional wording is NOT part of this correction and must be exposed in the UPDATE MAP as ENGINEER-PROPOSED before Gate 2." | TB-CP-001 | this map §C | Every added span in the diff equals a §C span marked INTAKE-VERBATIM, ENGINEER-PROPOSED, or MECHANICAL |
| "Any Engineer-added wording must be identified separately before Gate 2." | TB-CP-002 | this map §C | same |
| "Do not guess." | TB-CP-003, TB-CP-004 | this map §B (evidence tables) | NO-CHANGE / correction rationale cites path:line only |

## M. Expected validation (acceptance-spec inputs for Sol)

- **Lints:** 4 lints; expected on candidate: zero new findings; baseline exactly 9 as §0 (same paths, lines, IDs).
- **Searches to re-run at candidate (verbatim from §B):**
  1. `grep -rn "TEST-B-SYNTHETIC" <live scope>` → expected **4 matching lines**:
     - 2 doc lines carrying 3 INTAKE-VERBATIM sentences: SKILLS §17 v1.2 row (01 + 03 on one line) and ENGINEER VH v1.3 row (02);
     - 2 CHANGELOG lines (the rows cite "TEST-B-SYNTHETIC-01 and -03" / "TEST-B-SYNTHETIC-02"), HISTORY.
  2. TB-CP-003 T3a / T3b / T3c. Expected: every §B hit still CONSISTENT; SKILLS :318–327, :307, :767–773 byte-unchanged (line numbers shift by 0 before L1148).
  3. TB-CP-004 T4a–T4h. Expected: all §B hits still present and CONSISTENT; the new ENGINEER row 2b present (if approved). Line numbers in ENGINEER after L96 shift +1, and after L1595 +1 more.
- **Canonical term list (AC-N):** "human/Operator gate" and "Required human/Operator" (the approved row 2b cells). The pre-existing L96 owner cell "Human (Tony Stark)" stays unchanged. Retired terms: lint list only (`stitch`). No campaign term list supplied.
- **Derived-field assertions:**
  - MANIFEST rows :31 and :39 equal their docs' new headers.
  - MANIFEST :3 and CHANGELOG :3 Date = EXEC_DATE (clears DRIFT-04/-05).
  - Count lines :6/:12/:76, ← map (incl. :83), and appendix :114 byte-unchanged from BASE (DRIFT-01/-02/-03 parked).
  - CHANGELOG +2 rows exactly.
- **Archive fidelity:** 2 archives expected: `_ARCHIVE/APP_FACTORY_SKILLS_PLAYBOOK_v1_1.md` and `_ARCHIVE/ENGINEER_PLAYBOOK_v1_2.md`, each byte-equal to `git show dd6d496:<path>`. Neither exists at BASE (`ls _ARCHIVE` has no matching name). No MANIFEST/CHANGELOG archive.
- **References to resolve (§H):** ENGINEER §1 "What the Engineer Does NOT Do"; SKILLS §17 Version History.
- **Scope assertion (AC-S):** changed paths ⊆ {2 target docs, 2 archives, `MANIFEST.md`, `CHANGELOG.md`, `_AUDIT/SYNC_2026-09-15_test-b-large/**`, `RECOVERY.md`, `session_2026-09-15.md`, `agent_docs/RESPONSES/*`}. `_INBOX/` cargo disposition is per sweep (D11).
- **Traceability (AC-T):** 5 ledger IDs. ENCODED expected for TB-CP-001, TB-CP-002, TB-CP-004 and IN-2026-09-15-01. NO-CHANGE (approved Gate 2) for TB-CP-003.
- **Merge / publication (AC-H context):** merge target NONE (K-2). No PR and no merge exist for this run, so none are expected.
- **Operator test rulings (not doctrine sources):** Q1 test waiver (§A) and K-1 version ruling apply to TEST B only. Neither is a Factory rule and neither may be cited as a standing requirement.
- **Operator test waiver:** Sol's spec must not treat the waived brief fields as sources of additional requirements. Invariants come from intent text only (§A).

## N. Write-load tally and commit plan

- Docs edited 2 + archives 2 + new docs 0 + MANIFEST + CHANGELOG = ~6 file writes (plus the durable metadata)
- Commits, in order (lightest ← first):
  1. `docs(APP_FACTORY_SKILLS_PLAYBOOK): v1.2 - TEST B synthetic validation sentences [TB-CP-001, TB-CP-003, IN-2026-09-15-01]`. Carries: archive v1_1, rows 1a/1b, MANIFEST row :39, CHANGELOG row 1.
  2. `docs(ENGINEER_PLAYBOOK): v1.3 - TEST B synthetic sentence and no self-approval of required gates [TB-CP-002, TB-CP-004]`. Carries: archive v1_2, rows 2a/2b/2c, MANIFEST row :31 + MANIFEST :3 Date, CHANGELOG row 2 + CHANGELOG :3 Date. → **CONTENT_SHA**.
  3. `chore(sync): handoff for CONTENT_SHA <short> [SYNC_2026-09-15_test-b-large]`
- Branch: none created; commits land on `test/docset-sync-v07-large-001` (§0). Push only after Gate 4, and only if this validation proceeds that far. No PR or merge in any case (K-2).
- Hygiene: plain hyphens in commit messages; no Co-Authored-By; one version bump per doc per run (D22).

## O. Approval and amendments

- [x] Gate 1 — scope + classification APPROVED by Operator 2026-09-15 (~17:50 local). Q1 ruled (a) — **OPERATOR TEST WAIVER, TEST B ONLY** (terms verbatim in §A).
- [x] Gate 2 — this map **APPROVED by Operator 2026-09-15** ("APPROVED — GATE 2"):
  - Route LARGE confirmed (no downgrade).
  - NO-CHANGE rows approved: **TB-CP-003**.
  - **K-1 — OPERATOR TEST RULING (TEST B only):** SKILLS_PLAYBOOK 1.1 → 1.2, ENGINEER_PLAYBOOK 1.2 → 1.3. Not a Factory-wide rule for bump magnitude; TESTA-F03 remains deferred.
  - **K-2:** MERGE TARGET = NONE. Disposable validation branch; no PR or merge from this TEST B run.
  - **K-3:** TB-CP-004 canonical change APPROVED. Row 2b owner cell replaced by the Operator: "Human (Tony Stark)" → "Required human/Operator" (do not hard-code Tony as the universal gate authority).
  - **All other ENGINEER-PROPOSED spans APPROVED:** row 1b bold lead-in; row 2b action cell; row 2c bold lead-in and §1 clause (clause later replaced by AMENDED-v1); both CHANGELOG one-line texts. None struck at Gate 2.
  - **Drift:** DRIFT-01/-02/-03 remain parked and untouched. DRIFT-04/-05 may be overwritten only because this approved run itself updates MANIFEST and CHANGELOG and therefore legitimately updates their header dates.
  - The Operator's rulings were applied to this file at the gate as part of the approval, not as a post-approval amendment.
  - Operator instruction: proceed to Phase 3 only; do not enter Phase 4.
- [ ] Gate 3 — spec APPROVED at `<date/time>` (LARGE; Sol)
- Amendments:
  - **AMENDED-v1 — 2026-09-15 — Gate 2 amendment APPROVED by Operator ("GATE 2 AMENDMENT APPROVED").**
    - *What changed:* TB-CP-004 wording made consistent across the map. §C row 2c's Version History clause "§1 "What the Engineer Does NOT Do" gains one row: self-approving a required human/Operator gate belongs to the Human (TB-CP-004)." is replaced by the Operator's sentence "Clarified that a required human/Operator gate may not be self-approved by the Engineer."
    - *Operator direction:* do not use the broader phrase "belongs to the Human".
    - *Why:* the Engineer concern raised at Gate 3 hand-over. Row 2b's owner cell ("Required human/Operator") and row 2c's clause expressed different authority wording.
    - *Canonical wording now, everywhere in this map:* action "Self-approve a required human/Operator gate"; owner / authority "Required human/Operator".
    - *Checked and unchanged (already the same meaning, no "Human" owner phrasing):* §C row 2b `| Self-approve a required human/Operator gate | Required human/Operator |`; §G CHANGELOG row 2 "…gains row: no self-approval of a required human/Operator gate"; §M term list.
    - *Remaining "Human (Tony Stark)" mentions* are either quotes of the pre-existing ENGINEER_PLAYBOOK L96 row (evidence, unchanged by this run) or records of the struck proposal (§B, §C 2b, §K-3, §O). None is proposed wording.
    - *Effect on route / IDs / touch list:* none.
    - *Gate 3:* no spec exists yet (not affected); Sol derives from AMENDED-v1.
  - The Gate 2 concern is resolved by AMENDED-v1.
- Overrides logged: none (the Q1 test waiver is an Operator ruling on field completeness, recorded in §A; it overrides no D-rule)
- CONTENT_SHA: `<pending Phase 4>` · Gate 4: `<pending>` · pushed: `<pending>`

## P. Route evidence

| Fast-path condition | Evidence | Holds? |
|---|---|---|
| ≤ 3 intake IDs | §A: 5 IDs with CHANGE/NO-CHANGE (TB-CP-001…004, IN-2026-09-15-01) | **NO** |
| ≤ 3 canonical touch-list docs (after §B search) | §C: 2 docs (APP_FACTORY_SKILLS_PLAYBOOK, ENGINEER_PLAYBOOK) | yes |
| no new canonical document | §D empty | yes |
| no Factory-wide terminology rename / change | no role/gate/module/artifact name changed; row 2b adds a limit, renames nothing | yes |
| no cross-correction dependency | §B: TB-CP-001 and IN-…-01 share one VH row, not an invariant; TB-CP-002 and TB-CP-004 share one VH row; no invariant depends on another | yes |
| no high-risk governing-rule change | TB-CP-004 as approved (row 2b) changes a **role authority chain** (who may approve a required gate) | **NO** (K-3 ruled correction) |
| no unresolved conflict | §K has no CONFLICT rows (K-1, K-2 CLARIFICATION; K-3 is a normal Gate 2 row decision) | yes |
| no cross-boundary change required for success | §J empty | yes |
| propagation search bounded and complete before Gate 2 | §B: every term searched over full live scope + awareness; every hit dispositioned (group dispositions list every line) | yes |
| docs-only QA waiver eligible | markdown + MANIFEST/CHANGELOG/_ARCHIVE only | yes |
| **Route** | Fails A1 (5 IDs) and A6 (approved TB-CP-004 correction). Unchanged from the provisional Phase 1 route. Baseline drift played no part | **LARGE — confirmed at Gate 2.** Operator escalation / downgrade ruling: none |
