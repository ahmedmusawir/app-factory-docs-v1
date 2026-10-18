# Intake Addendum 001 — v0.1 (to Harvest Package v0.1 and Correction Package 001 R3)

> **STAGING — DRAFT / NOT APPROVED FOR SYNC.** This addendum indexes material that arrived after the harvest package (the Director-approved QAM playbook, the Director rulings, the reconciled planning documents), supplies the source-register entry the harvest omitted, and stages an Engineer-drafted `TEMPLATES/QAM/` set. It replaces nothing: Harvest v0.1 keeps its files, IDs (`WF-/RRM-/QAM-`, `ND-`, `GAP-`, `SRC-`) and history; Correction Package 001 keeps its IDs (`FC-/CF-/DEC-`) and revisions R0–R3. Placing material here does not approve it; `_INBOX/` is untouched.

| Field | Value |
|---|---|
| Addendum | `factory-intake/INTAKE_ADDENDUM_001_v0_1/` — version **0.1**, 2026-10-14, Asia/Dhaka |
| Prepared by | Claudy (documentation Engineer seat), delegated by Jarvis (Architect) via Tony's instruction "CLAUDY — PREPARE THE CONSOLIDATED INTAKE AND QAM TEMPLATE DRAFT" (2026-10-14) |
| Status | DRAFT — INTAKE ADDENDUM / NOT APPROVED FOR SYNC. Awaiting Jarvis (Architect) acceptance and QA Lead review of the template draft; the DRAFT → APPROVED change is the Director's |
| Repository state | branch `factory-docs-review-astra-w-chunks` · HEAD `626da8d70f4db22987dc7fcc86765492072360cd` · main = origin/main `9c179392f79b70da099121fc357d3107ad3bb86e` · the correction package R1–R3 edits, `factory-intake/` and bookkeeping are uncommitted (nothing staged) |
| DocSet Sync revision consulted | `_SKILLS/factory-docs-update/` at main `9c17939` via `git show`: family `CLAUDE.md` v0.8-DRAFT (2026-09-26) SHA-256 `d35689b52ec19a5551372f38f9190b0c5e18ede178769ed00bb161da3a23a9fb`, `README.md` `71b80baea2ddb2f6dcf58d350f30546e9fe9c27f1b580292559c44a0417292f5`, `sync-engineer/SKILL.md` `f2a899d9c1da20b33990877b9a6d39e1c8bb762ab799057ef148840c8a79d1f8`, `_shared/references/INTAKE_TAXONOMY.md`. Not activated |
| Hashes | `ADDENDUM_FILE_INDEX.json` — SHA-256 of every file in this folder except itself, and of every in-place file this index references (playbook, ruling record, planning documents, correction package files, harvest index files, outer harvest ZIP) |

## 1. Read order

1. This index (§2 what is approved vs open; §3 source-register addendum; §4 links to the two packages).
2. `COMBINED_INTAKE_MANIFEST_001.md` — the proposed combined intake (Correction Package R3 + Harvest v0.1 + this addendum), the proposed `_INBOX/` layout, and every unresolved decision assessed individually.
3. `../QAM_PLAYBOOK_v1_0.md` — the Director-approved source (unchanged; indexed in §3 as SRC-A01).
4. `../PLANNING_001/DIRECTOR_RULINGS_2026-10-14.md` (R1.1) — the attributable ruling record, RUL-01…RUL-07.
5. `../PLANNING_001/COMBINED_DECISIONS_001.md` (R2), `../PLANNING_001/COMBINED_DEPENDENCY_MAP_001.md` (R2), `../PLANNING_001/INTAKE_CLARIFICATIONS_001.md` (R2) — the reconciled planning documents.
6. `TEMPLATE_PLACEMENT_RECOMMENDATION.md` — one recommended Hub home for the template set, with basis.
7. `TEMPLATES/QAM/README.md` then the set — **NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED**.
8. `ADDENDUM_FILE_INDEX.json` — hashes.

## 2. What is approved, what is proposed, what is deferred, what is missing

Labels follow the harvest index §2 (CURRENT SESSION DIRECTION · REPORTED DIRECTOR RULING · FIELD RESULT · PROPOSED ADOPTION · HISTORICAL · OPEN / MISSING) plus the planning vocabulary RESOLVED / NARROWED.

### 2.1 Approved rules (Director; attributable records)

| Rule | Record | Scope limit |
|---|---|---|
| `QAM_PLAYBOOK_v1_0.md` is Director-approved source material; **every newly authored module MUST include a complete, module-specific `QAM/` from initial Architect packaging; no opt-in**; five seats; Q1 → QA Lead approval → Director release → Q2; repair/retest conditional; no prefilled QA results | RUL-01 | Newly authored modules; tooling not approved; TRM undefined; ABM/APBM methodology stays on the 10X track (RUL-07) |
| **Continuing QA branch**: `<module-branch>` → Director creates `qa/<module-branch>` at the same starting commit → rework and independent testing there → certification → closeout → Director merges into `main`; no disposable branches; no transfer-back | RUL-02 | Project-module policy; DocSet Sync's Hub Git rules unchanged; no Git action authorized |
| **Necessary QA cleanup remains required** (playbook §14 preserved); only abandon/transfer-back cleanup retired; module QA records under `agent_docs/` in the QAM structure; **deployment exclusion of `agent_docs/**` must be enforced and verified** | RUL-03 | Not a third QA campaign; retention is not "keep everything" |
| **Frozen contract, writable declared lanes**; contract changes only by attributable approved amendment | RUL-04 | — |
| **Two review/RRM checkpoints** (after FFM + its QA; Engine 2 after all Engine 1 phases + QA); findings dispositioned; no manufactured repair; each RRM includes QAM; module certification ≠ review completion ≠ deployed verification | RUL-05 | Governs current drafting; does **not** authenticate the harvest's historical "later 10X" source (CL-25) |
| **Placement**: `03_BUILD_METHODOLOGY/RRM_PLAYBOOK.md`, `QAM_PLAYBOOK.md`, `DEPLOYMENT_PLAYBOOK.md`; operating models fold into existing playbooks; propagation across the named documents | RUL-06 | Template/kit homes not decided (DEC-19 narrowed) |
| Boundaries: five scoped approvals unchanged; 97 FC identities/fields/totals preserved; originals preserved; no TRM definition; no tooling approval | RUL-07 | — |
| DEC-01, DEC-02, DEC-03, DEC-04, DEC-16 — scoped directional approvals (2026-10-12) | `../../factory-corrections/DECISION_RECORD_001.md` §1 | Form/direction only; not cargo approval; package stays DRAFT |
| D.4 dual entry files (QAM-04): both `QAM/` entry files **and** parent-module Engineering/QA routing | RUL-01 via playbook §6 (CL-27) | FFM_PLAYBOOK §8.3 wording is an UPDATE MAP drafting item |

### 2.2 Unresolved proposals (need a ruling or a Gate 2 approval; details and recommendations in `COMBINED_DECISIONS_001.md` R2)

C.2 DevOps seat / Cloud Run profile / cloud matrix / staging (DEC-18 remainder; FC-011/012/088) · C.3 who runs the `XB-*` jobs (DEC-21) · D.1 seat-glossary host, synonyms, rename (DEC-07 remainder) · D.2 DATA_CONTRACT timing, UI_SPEC owner, FILE_TREE, templates (DEC-10/11/12) · D.3 recon lanes and diagnostics (DEC-14) · E one-shot engineering (ND-07) · B.2 reviewer guidance placement (RRM-09) · N-1 Engine 1/2 definitions · **N-2 `TEMPLATES/QAM/`: QA Lead acceptance of the draft + home (DEC-19)** · N-3…N-7 integration wording · Group F: DEC-05 quote design, DEC-06, DEC-08, DEC-09, DEC-15, DEC-17, DEC-20, DEC-22. Each is classified in `COMBINED_INTAKE_MANIFEST_001.md` §3 as required-before-acceptance, resolvable-in-the-UPDATE-MAP, or deferred.

### 2.3 Deferred work (outside this run; parked with IDs, never silently dropped)

`XB-SKILL` (docs-update git wording FC-005/006/096 parts; deployment skills; a later taxonomy note for the template home) · `XB-LINT/CI` (FC-096 part, DEC-16 limits) · `XB-ROOT` (CF-17, FC-090/091/094; FILE_TREE root reference) · `XB-EXT` (kit verifications FC-041/042/072; RRM/QAM kits if external; GAP-02 evidence export; QAM tooling if ever commissioned) · publication of RRM-004 as a certified worked example (needs CL-14) · revised diagrams (class 6, only if commissioned) · ABM/APBM (10X track) and Vibe Engineering (pilot-specific): out of scope by boundary, not deferred.

### 2.4 Evidence gaps (kept explicit; nothing invented)

| ID | Gap | Blocks |
|---|---|---|
| CL-11 | Doctrine Journal v0.3 (J-11, J-19) | Provenance only; RUL-02/03 rule directly; Hub text substitutes its own rules (N-5) |
| CL-12 | Historical "later 10X direction" source (no SRC ID) | Provenance only; RUL-05 governs drafting and does not authenticate it |
| CL-13 | DevOps Architect ruling 2026-08-23 | FC-011 content until C.2 is ruled afresh |
| CL-14 / HG-02 | RRM-004 QA Lead certification letter; final closeout records | Worked-example publication only |
| CL-15 / HG-03 | Original `01_EVIDENCE_DOSSIER.md` and original `TEMPLATES/` | Nothing (draft replacements exist, labeled; originals not claimed) |
| CL-16 / HG-01 | RRM campaign ledger/map (SRC-R05 empty) | Nothing |
| CL-17 | SRC-R01 nested reviewer ZIPs (declared, not extracted) | Nothing |
| CL-18 | RRM-004 post-2026-10-02 closure state | Nothing inferred |
| CL-21 | Companion synchronization brief (playbook §18) | Nothing; map §4a substitutes |
| E-8 | Jarvis's confirmation of the outer harvest ZIP hash `2b2b27e38848412143e472d98a2e4c4ffbc0ff760a95d245dab262e3837af782` | Nothing |
| E-10 | Kit repository access (DEC-09) | FC-041, FC-042, FC-072 |
| E-11 | Hub-law home for the template set | Placement of E-2 only; recommendation in `TEMPLATE_PLACEMENT_RECOMMENDATION.md` |

## 3. Source-register addendum (rows Jarvis may fold into `SOURCE_REGISTER.md` in a later revision; nothing applied there)

Register conventions follow `../SOURCE_REGISTER.md`: original bytes preserved; `SRC-R02/<member>` names a member inside that archive. **`SRC-A01` is an addendum-local ID** (prefix `A` = addendum) so it cannot collide with the harvest's `SRC-W/R/Q/C` series; Jarvis may renumber it in a harvest revision.

| ID | Packaged file / member | Original name | Date / status | SHA-256 | Kind |
|---|---|---|---|---|---|
| **SRC-A01** | `../QAM_PLAYBOOK_v1_0.md` (in place, **unchanged**; 252 lines, 30,650 bytes, UTF-8; received 2026-10-14 14:06 +0600) | `QAM_PLAYBOOK_v1_0.md` — "QAM PLAYBOOK v1.0", QA Lead / JARVIS, Director Tony Stark | 2026-10-14; **Director-approved source material (RUL-01)**; class 3 content (→ `03_BUILD_METHODOLOGY/QAM_PLAYBOOK.md` via the UPDATE MAP, substitutions N-3…N-6 flagged) + class 7 original (→ `_AUDIT/`) | `97e111e2a495f9a3fe65f50213e6f2ba68c8e5e963f3d23493b1ee99ad35c897` | ruling-backed playbook (operating model) |
| **SRC-R02/REPAIR_PROPOSAL.md.template** (the register row omitted from Harvest v0.1) | member `RRM-004-CYBER-PHARMA/QA/REPAIR_PROPOSAL.md.template` of `../SOURCES/RRM/SRC-R02_RRM004_ORIGINAL_PACK_v1_0.zip` (archive SHA-256 `c2a21b82ca4f6c1ec0e7d75dd5860ff2cf15c3a3615099c62272558db524ed2a`, = `SOURCE_INVENTORY.json`). **Not extracted** into `../EXTRACTED/SRC-R02/` (extracting would change the hashed tree); listed in `../ARCHIVE_CONTENTS.json` (SRC-R02, `file_count` 23) but absent from `../SOURCE_REGISTER.md` §SRC-R02 (22 rows) | part of `RRM-004-CYBER-PHARMA_pack_v1.0.zip` | 2026-09-30 11:02:46 (member timestamp, archive-local); 665 bytes (433 compressed); CRC32 `5faaed7e` (verified); HISTORICAL / pilot-specific blank template | `49943f04ff46cfe8de8d557b038c12a97512cd9c5dcbcfd3ce77c0747b222224` (member bytes; re-verified 2026-10-14 18:26 +0600 with Python `zipfile`, `-I`, script outside the extracted tree) | pilot lesson / blank QA Executor draft template |

Provenance of the member (verbatim phrases from the member bytes): created as `REPAIR_PROPOSAL.md` "only when at least one product AC is FAIL"; "a proposal for the QA Lead → Architect → Director chain, not a work order"; "No QA seat edits `src/`, `package.json`, `package-lock.json`, `next.config.js` or tests"; one finding table (Finding · AC(s) · Evidence path(s) · Reproduction · Suggested class · Suggested allowed files · Suggested retest scope). Evidence for QAM-09 and RRM-06. Its content informed `TEMPLATES/QAM/FINDINGS.md` §3.1 by attribution; nothing was copied as an original.

## 4. Links to the two existing packages (IDs and histories untouched)

| Package | Location | Revision pin | Status | Integrity (this addendum's check, 2026-10-14) |
|---|---|---|---|---|
| **Correction Package 001** | `../../factory-corrections/` — `FACTORY_DOCTRINE_CORRECTION_INDEX_001.md` + briefs `01_…07_*_corrections.md` + `DECISION_RECORD_001.md` (9 files) | **R3** (2026-10-14; decision-status annotations only) in the working tree over HEAD `626da8d` (R0 committed; R1–R3 uncommitted). Certified basis `c6210c3`. Hashes in `ADDENDUM_FILE_INDEX.json` | DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC; only DEC-01/02/03/04/16 approved (scoped) | 97 FC records, 17 CFs, 6/36/44/11, YES 94 / NO 3 — index §4 totals preserved; `validate.py` 0 problems |
| **Harvest Package v0.1** ("Factory Part 2 — New Doctrine Intake", Jarvis, 2026-10-13) | `../` (extracted flat; CL-03): `00_MASTER_INDEX.md`, `01_FACTORY_WORKFLOWS_INTAKE.md`, `02_RRM_INTAKE.md`, `03_QAM_INTAKE.md`, `SOURCE_REGISTER.md`, `SOURCE_INVENTORY.json`, `ARCHIVE_CONTENTS.json`, `FILE_INDEX.json`, `SOURCES/`, `EXTRACTED/` | v0.1 (not "R1", CL-01); outer ZIP `~/Downloads/FACTORY_PART2_NEW_DOCTRINE_INTAKE_v0_1.zip` SHA-256 `2b2b27e38848412143e472d98a2e4c4ffbc0ff760a95d245dab262e3837af782` (Claudy-computed; 76 members) | DRAFT FOR INTAKE RECONCILIATION | `FILE_INDEX.json` 75/75 unchanged; `SOURCE_INVENTORY.json` 22/22; no hashed file edited by this addendum |
| Planning 001 (not cargo) | `../PLANNING_001/` — decisions R2, map R2, clarifications R2, rulings R1.1 | working tree | PLANNING — DRAFT / NOT APPROVED | hashes in `ADDENDUM_FILE_INDEX.json` |

The harvest's `README.md` §4 relation vocabulary (SAME · EXTENDS · CONFLICTS · NEW) and the planning map §3 crosswalk remain the join between the two packages; this addendum adds no new relation rows.

## 5. The template draft (B) — what it is and is not

`TEMPLATES/QAM/` holds **25 files**: the 22 items the playbook §5/§13 names, plus `README.md` (ownership, Architect preparation duties, Engineer completion duties, the engagement flow), `QAM_PACKAGING.md` (§13 packaging instructions; no exporter) and `PARENT_ENTRY_ROUTING.md` (§6 parent-module routing text). Every file is labeled **NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED**, carries `<<…>>` placeholders, and leaves every result, approval, certificate, SHA and credential field unfilled (`NOT RUN` / `NOT RECORDED` / `NEEDS AUTHORING` / `PENDING`). It preserves Q1 → QA Lead approval → Director release → Q2, conditional Q4 repair/retest, the required §14 cleanup (Q5) and the continuing `qa/<module>` branch. It is an **Engineer draft, not QA-approved** (CL-26): the QA Lead reviews and accepts its QA behavior; authoring and QA ownership are different acts. It is not the pilot's original set (HG-03). It contains no validator, exporter, state dispatcher or runtime adapter (RUL-07).

## 6. What this addendum does not do

- It does not approve anything, does not change either package's status, and is not `_INBOX/` cargo.
- It does not edit `QAM_PLAYBOOK_v1_0.md`, `SOURCE_REGISTER.md`, `FILE_INDEX.json`, `SOURCE_INVENTORY.json`, `ARCHIVE_CONTENTS.json`, `SOURCES/`, `EXTRACTED/`, the correction package, canonical doctrine, MANIFEST, CHANGELOG, skills, lints or CI.
- It does not authorize a sync run, an UPDATE MAP, a canonical placement of the templates, or any Git action (the operator's global Rule Zero governs this agent; the Director executes Git).
- It does not certify the template draft; QA Lead acceptance is a separate, recorded act.

*STAGING — DRAFT / NOT APPROVED FOR SYNC. Prepared for Architect (Jarvis) and QA Lead review; Director (Tony) decides.*
