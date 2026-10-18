# Template placement recommendation — where `TEMPLATES/QAM/` should live in the Hub

> **PLANNING RECOMMENDATION — DRAFT / NOT APPROVED.** One concrete versioned home is recommended with its governing basis. The draft set stays in intake staging (`TEMPLATES/QAM/` beside this file) until canonical placement is authorized by the Director (DEC-19, narrowed by RUL-06) on Jarvis's advice. No skill, taxonomy, lint or CI file is modified to create a home.

| Field | Value |
|---|---|
| Prepared by | Claudy (documentation Engineer seat), 2026-10-14 |
| Question | `QAM_PLAYBOOK_v1_0.md` §5 says "Instantiate `TEMPLATES/QAM/` inside each module directory". Where does the reusable set live in the Doctrine Hub so that DocSet Sync can version it with the playbook? (COMBINED_DECISIONS N-2; dependency map E-11) |
| Hub conventions read | `MANIFEST.md` v1.0 (29 live docs = top-level `*.md` in the five tier folders); `_ARCHIVE/README.md` (DOCTRINE_HUB_DESIGN §2.3 rule); `lints/lint_common.py` (scope); `_SKILLS/factory-docs-update/_shared/references/INTAKE_TAXONOMY.md` at main `9c17939` (eleven classes, Ruling 9); family `CLAUDE.md` D15/D16; `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` (skill `templates/` convention); `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §1.5 (worked-example pairing) |

## 1. What the Hub's conventions say (evidence)

| Convention | Where | What it establishes | Consequence for a template set |
|---|---|---|---|
| Live doctrine = canonical-named `*.md` directly in a tier folder; versions live in headers and MANIFEST, never in live filenames; versioned filenames only in `_ARCHIVE/` | `_ARCHIVE/README.md`; MANIFEST "29 Live Docs" | A template file is not a doctrine document: it has no Version/Date/Status header claim of its own kind and no MANIFEST row | Templates must not sit as top-level tier `*.md` (they would be counted as live docs and lint-checked for the standard header) and must not carry version suffixes in their filenames |
| Lint scope is **non-recursive**: `glob("*.md")` per tier folder plus MANIFEST and CHANGELOG | `lints/lint_common.py` `live_files()` | A subfolder inside a tier is outside lint scope | A tier subfolder can hold templates without tripping the header lint; it also gets no lint coverage, so the sync run's QA lane must check the set explicitly |
| Ruling 9: canonical assets live in `<OWNING_TIER>/_assets/<name>.<ext>`; no MANIFEST row; the referencing doc's row and the CHANGELOG line carry the change; replaced assets go to `_ARCHIVE/<name>_<date>.<ext>` | INTAKE_TAXONOMY class 6 | The Hub already sanctions **one tier-local, underscore-prefixed subfolder** for non-doctrine files owned by a tier's documents | The nearest precedent for a tier-local, non-doctrine, versioned-with-its-owner file set |
| Class 7 supporting / non-canonical assets land in `_AUDIT/` or `_OTHERS/`: no header law, no MANIFEST row, ledger records the landing path | INTAKE_TAXONOMY class 7 | A home for things "not intended as live doctrine" | Possible but weak: the set is the instrument of a **mandatory** rule and must track the playbook's version; `_OTHERS/` is not versioned with any document |
| Skills keep their fillable structures in `<skill>/templates/*.md` | APP_FACTORY_SKILLS_PLAYBOOK; `_SKILLS/factory-docs-update/templates/` (`LESSONS_LEARNED.md`, `RIPPLE_MAP.md`) | Templates belong next to the thing that fills them | Supports a tier-local folder beside the playbook rather than a detached location; a skill folder itself is the wrong owner (the skill family is for sync, not module QA, and "do not modify skills to create a template home") |
| Worked examples pair with playbooks and live project-side (`CURRENT_APP/…/_project/`) | SOFTWARE_FACTORY_PLAYBOOK §1.5 | Examples are born in runs, not in the Hub | A kit repository (`XB-EXT`) is the Hub's existing pattern for example/kit material; its weakness is access and versioning (DEC-09 shows kit access is already a gap) |
| D15: Hub law outranks cargo conventions; mechanics are translated and every translation flagged | family `CLAUDE.md` | The playbook's `TEMPLATES/QAM/` path is a cargo convention | The Hub path may differ from the playbook's literal path; the translation is flagged in the UPDATE MAP and the playbook text's §5 cites the Hub path |
| D16 / class 11: a unit that fits no class is a QUESTION at Gate 1, never a guess | INTAKE_TAXONOMY | No class describes "a template set instantiated by a doctrine rule" | Without a prior Director ruling on the home, the set would be BLOCKED at Gate 1; a ruling now pre-answers that question. A taxonomy note is a later `XB-SKILL` job, not a prerequisite |

## 2. Options

| Option | Home | Basis | Pros | Cons |
|---|---|---|---|---|
| **A (recommended)** | `03_BUILD_METHODOLOGY/_templates/QAM/` — the set's `README.md` header carries `Template set version` and `Pinned to QAM_PLAYBOOK version`; each file carries the same set version in its header line | Ruling 9 precedent (tier-local `_`-prefixed subfolder owned by the tier's documents); `_ARCHIVE/README.md` (versions in headers, not filenames); lint scope (no header-lint conflict); D15 translation of `TEMPLATES/QAM/` → `_templates/QAM/`, flagged | Versioned with the playbook by the same sync run; one owner tier (`03_` owns the module-type playbooks); no MANIFEST drift (no new live-doc row); path is stable and lint-safe | Needs a Director ruling (DEC-19) because no taxonomy class covers it; needs an explicit QA check in the sync run since lints do not cover subfolders; superseded sets need an archive convention (proposed: copy the outgoing set to `_ARCHIVE/QAM_TEMPLATES_v<set version>/`, stamped from the set README header) |
| B | `_OTHERS/TEMPLATES/QAM/` | Class 7 landing for non-canonical material | No ruling needed beyond class 7 triage | Not versioned with the playbook; `_OTHERS/` is a parking lot for design notes and master lists, not an instrument of a mandatory rule; projects would be told to copy templates from a folder that no document owns |
| C | External kit repository, recorded as `XB-EXT`; the playbook cites the kit by version | DEC-21 / class 9 pattern; SFP §1.5 project-side examples | Keeps non-doctrine files out of the Hub | Kit access is already unverified (DEC-09, E-10); version coupling between playbook and kit must be managed by hand; a mandatory rule would depend on a repository the Hub cannot see |

## 3. Recommendation (PROPOSED)

**Option A: `03_BUILD_METHODOLOGY/_templates/QAM/`.** Governing basis: Ruling 9's tier-subfolder precedent, the archive rule that versions live in headers, the non-recursive lint scope, and D15's rule that cargo paths are translated to Hub law and flagged. What it requires, in order:

1. **QA Lead acceptance** of the draft set's QA behavior (CL-26) — independent of placement.
2. **Director ruling** (DEC-19): "`03_BUILD_METHODOLOGY/_templates/QAM/` is the home of the QAM template set; versions in the set README header, pinned to the QAM_PLAYBOOK version; superseded sets archived under `_ARCHIVE/QAM_TEMPLATES_v<version>/`; no MANIFEST row; the QAM_PLAYBOOK row's Purpose and the CHANGELOG line carry changes." The ruling pre-answers the Gate 1 class question for this unit.
3. **UPDATE MAP rows** (Gate 2): QAM_PLAYBOOK §5 cites the Hub path (flagged D15 translation); HANDOFF_PACKAGE_PLAYBOOK, ARCHITECT_PLAYBOOK and the module-type playbooks point to it; the sync run's acceptance spec includes an explicit check of the set (presence of all files, identical entry routing, no prefilled results) because lints do not cover it.
4. **Later, optional** `XB-SKILL` job: a one-line taxonomy note naming tier-local `_templates/` as a lawful landing for template sets, so the next run does not need a ruling.

Until step 2 is done the set stays here, in staging, and QAM-03 is reported incomplete.

*PLANNING RECOMMENDATION — DRAFT / NOT APPROVED. No skill, lint, CI or canonical file was modified.*
