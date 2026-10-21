✅ DIRECTOR RULINGS RECONCILED — PLANNING 001 R1 + INDEX R3 (STOP for Architect review)

Planning and bookkeeping only. No canonical edit, no source modification, no skill/lint/CI change, no `_INBOX/` drop, no Git mutation, no sync activation. The five scoped approvals (DEC-01/02/03/04/16), all 97 FC identities, fields and totals, and every supplied source file are unchanged.

**State**
- Start and end: branch `factory-docs-review-astra-w-chunks`, HEAD `626da8d70f4db22987dc7fcc86765492072360cd`, main = origin/main `9c179392f79b70da099121fc357d3107ad3bb86e`; nothing staged; existing R1/R2 edits, `factory-intake/` and bookkeeping preserved.
- DocSet Sync read from main `9c17939` with `git show`: family `CLAUDE.md` v0.8-DRAFT (2026-09-26) SHA-256 `d35689b5…a9fb`, `README.md` `71b80bae…92f5`, `sync-engineer/SKILL.md` `f2a899d9…1f8`. Not activated.
- New source received: `factory-intake/QAM_PLAYBOOK_v1_0.md` (QA Lead / JARVIS, 2026-10-14; 252 lines) SHA-256 `97e111e2a495f9a3fe65f50213e6f2ba68c8e5e963f3d23493b1ee99ad35c897`. Preserved unchanged; not yet in `FILE_INDEX.json`.

**Rulings recorded and conflicts resolved** — `factory-intake/PLANNING_001/DIRECTOR_RULINGS_2026-10-14.md` (RUL-01…07, each linked to its DEC/ND/WF/RRM/QAM IDs; A.1 etc. kept as navigation labels only)
- RUL-01 mandatory QAM → ND-01 RESOLVED; QAM-01…14 adoption resolved; five seats; Q1/Q2; DEC-07 NARROWED ("Director", "QA Executor" in use; glossary host/synonyms open).
- RUL-02 continuing `qa/<module>` branch → A.2 RESOLVED by fresh decision; SRC-W06 §8 disposable rule retired for module QA; RRM-06/WF-07/QAM-09 land; DEC-18 NARROWED (module-Git row ruled; cloud/staging open). J-11 no longer gates anything.
- RUL-03 cleanup retained → ND-04 RESOLVED; playbook §14 preserved; only abandon/transfer-back cleanup retired; QA records under `agent_docs/` QAM structure; **new requirement**: deployment exclusion of `agent_docs/**` enforced and verified (no Hub counterpart today; RECON Q9 covers tsconfig/tests only).
- RUL-04 frozen contract + writable lanes → DEC-13 RESOLVED; FC-013/FC-026 unblocked; BIM_PLAYBOOK §6 "outputs OUTSIDE" to be reconciled.
- RUL-05 two review/RRM checkpoints → ND-02 RESOLVED; RRM adopted; SRC-W11 three-engine draft superseded; the unsourced "later 10X direction" is now sourced (it is this ruling); each RRM includes QAM.
- RUL-06 placement → ND-05 RESOLVED: `03_BUILD_METHODOLOGY/RRM_PLAYBOOK.md`, `QAM_PLAYBOOK.md`, `DEPLOYMENT_PLAYBOOK.md`; operating models folded; DEC-19 NARROWED (templates/kits home open); DEC-17 unchanged.
- RUL-07 boundaries → ABM/APBM 10X-only, Vibe pilot-specific, no TRM definition, no tooling approval, FC/approvals preserved.
- Consistency: the mandatory-QAM, continuing-branch and retained-cleanup rules are applied through all four planning documents; R0 wording ("optional", "two named patterns", "QAM later run") survives only as marked, superseded history.

**Planning documents revised (R1)**
- `COMBINED_DECISIONS_001.md` (239 lines): A.1–A.4, B.1, C.1 RESOLVED; C.2, D.1 NARROWED; D.4 split (QAM/ resolved, parent entries CONFIRM); B.2, C.3, D.2, D.3, E, F unchanged OPEN; new **Group N** (N-1 Engine 1/2 definitions, N-2 `TEMPLATES/QAM/` author/home, N-3 retroactivity, N-4 ABM/APBM wording, N-5 unresolvable journal citations, N-6 TRM row, N-7 deployment-exclusion owner, N-8 package indexing); §3 status column; §5 ruling sheet with a Ruling column.
- `COMBINED_DEPENDENCY_MAP_001.md` (270 lines): all 36 crosswalk rows re-gated (QAM rows now cite v1.0 sections as the authoring source); §2 new counterpart rows (QA Executor, agent_docs, TEMPLATES, TRM, Engine 1/2); §3.4 QAM playbook as class 3 + class 7; **§4a propagation plan** per RUL-06 (16 documents × the five rules); **§4b companion/template inventory** (supplied / missing / proposed newly authored); §5 route still LARGE, A7 narrowed; §6 one campaign, QAM split withdrawn; §7 CL references corrected; **§9 exact next sync step + P1–P7**; **§10 external dependencies E-1…E-12** with what each actually blocks.
- `INTAKE_CLARIFICATIONS_001.md` (106 lines): CL-05 closed by RUL-02; new §1a CL-19…CL-24 (playbook receipt + hash, templates missing, companion brief missing, CL-12 sourced, CL-11 no longer gating, numbering note); §4/§5/§6 updated.
- **CL correction:** R0 cited CL-04/05/06/07 for J-11, the 10X direction, the DevOps ruling and the register addendum; correct references are CL-11, CL-12, CL-13 and clarifications §3. CL-06…CL-10 stay unassigned.

**Correction index R3** (`FACTORY_DOCTRINE_CORRECTION_INDEX_001.md`, decision-status annotations only): DEC-13 RESOLVED; DEC-07, DEC-18, DEC-19 NARROWED; §12 status note; Revision line R3. Briefs 01–07 and `DECISION_RECORD_001.md` untouched. The package stays DRAFT.

**Proposed propagation (map §4a, summary)**: SFP §2/§2.5 (QAM in module identity; Q1/Q2; QA Executor; Engine 1/2; two checkpoints) · Blueprint (router, role table, post-FFM review) · FFM/BIM/BUG_FIX/FEAT playbooks (mandatory `QAM/` in every module tree; `qa/<module>` branch; §14 cleanup pointer; BIM §6 lanes) · QA_PLAYBOOK (seat, crosswalk, sequence note) · ARCHITECT/ENGINEER/HANDOFF (instantiate, complete, never prefill; `QAM/HANDOFFS/`) · RECON (Q9.3 deploy exclusion) · new RRM/QAM/DEPLOYMENT playbooks · MANIFEST/CHANGELOG. Template set: 22 items proposed newly authored by the QA Lead (N-2).

**Remaining genuine decisions (plain-English recommendations)**
- N-2 `TEMPLATES/QAM/`: QA Lead authors, labeled newly authored; host beside the playbook if Hub law allows, else `XB-EXT`. **Only item that blocks a correction's actual completion (QAM-03).**
- C.2 DevOps seat / Cloud Run profile / cloud matrix / staging: seat by responsibility, profile yes, matrix yes with D5 as one row.
- D.1 remainder: keep Operator/Coordinator as synonyms, no mass rename. D.2: confirm B-1/B-2; UI_SPEC model B; retire FILE_TREE as mandatory. D.3: three recon lanes. D.4 parent entries: keep FFM §8.3 redirect. E: no one-shot default. B.2: reviewer section in RRM_PLAYBOOK. C.3 and Group F: unchanged.
- Wording confirmations for Jarvis: N-1 (Engine 1/2 definitions in SFP §2, no Engine 3), N-4, N-5, N-6.

**Missing supporting material and whether it blocks (map §10)**
- Blocks completion: `TEMPLATES/QAM/` (QAM-03); the DevOps Architect ruling 2026-08-23 (FC-011 content); kit repo access (FC-041/042/072, unchanged).
- Blocks the run, not an item: Jarvis's package revision indexing the playbook + the Director's intake approval statement.
- Blocks nothing: companion synchronization brief (map §4a substitutes), Doctrine Journal v0.3 / J-11 / J-19 (ruled directly; citation substitution N-5), evidence dossier, RRM-004 certification letter (worked example only), outer ZIP hash confirmation.

**Exact next DocSet Sync step (map §9)**: approved cargo into `_INBOX/` at a Hub clone on `main`, then activate `sync-engineer` **Phase 1 — Scope** (cargo scan, `INTAKE_SNAPSHOT/`, D16 classification, route decision; expected LARGE), Phase 2 UPDATE MAP in the same run. Prerequisites: P1 Jarvis's harvest revision (indexes the playbook, carries the rulings, register row, status change) · P2 Director intake approval of both packages as one coordinated intake naming the DEFERRED items · P3 N-1/N-4/N-5/N-6 confirmations or "carry to Gate 2" · P4 template-home decision (blocks QAM-03 only) · P5 working-tree hygiene on this branch (Director's call) · **P6 Git execution convention: the operator's global Rule Zero outranks the skill's D5 carve-out for this agent, so inside the run Claudy prints every Git mutation as a command block for the Director** (R0's "run by Claudy under D5" is corrected) · P7 `_INBOX/` layout for two packages.

**Validation (read-only self-check, not QA)**
- Package: `validate.py` 0 problems (94 YES / 3 NO; 17 CFs; routes unchanged); `doccheck.py` 0 problems on the 9 package files; one new unresolved path token `03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md` in the index (expected: the document is ruled, not yet created).
- Planning: 36/36 harvest IDs one primary row each; 45 FCs, 13 CFs, DEC-01…22, ND-01…07 resolve; RUL-01…07 all cited; no CL-04…07 misreferences; no "reopen" of the five approvals; "v0.1-R1" only inside CL-01; UTF-8/LF/no BOM; one H1 each; table columns consistent.
- Hashes: FILE_INDEX 75/75 unchanged; 8/9 package files unchanged (the index changed by design); protected 100/100; `QAM_PLAYBOOK_v1_0.md` and staging README unchanged.
- Lints (`lints/run_all.py`): output identical to the pre-task baseline (the 9 known findings; DEC-16). Unrelated to this task; `factory-*` is outside lint scope.

**Changed paths**: `factory-intake/PLANNING_001/DIRECTOR_RULINGS_2026-10-14.md` (new), `COMBINED_DECISIONS_001.md`, `COMBINED_DEPENDENCY_MAP_001.md`, `INTAKE_CLARIFICATIONS_001.md`, `factory-corrections/FACTORY_DOCTRINE_CORRECTION_INDEX_001.md` (R3 annotations), this response, `session_2026-10-14.md` (new), `RECOVERY.md`, one ZIP in `~/Downloads/`. Nothing else.

**Review ZIP**: `~/Downloads/RULINGS_RECONCILIATION_001_2026-10-14_145435.zip` — the four planning documents, the correction index (R3), `DECISION_RECORD_001.md`, this response and `HASH_MANIFEST.sha256`. The ZIP's own SHA-256 is printed on screen and recorded in the session file and `RECOVERY.md` (it cannot be inside this file, which the ZIP contains).

→ **STOP** for Architect review.

📄 Logged: agent_docs/RESPONSES/response_2026-10-14_145435_rulings-reconciliation-001.md
