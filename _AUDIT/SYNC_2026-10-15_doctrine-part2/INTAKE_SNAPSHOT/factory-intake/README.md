# Factory Intake — Pre-Intake Staging

> **STAGING — PRE-INTAKE SOURCE MATERIAL / NOT APPROVED FOR SYNC**
> Whatever is placed here is source material for review. Placing it here does not approve it for adoption, and DocSet Sync does not treat it as cargo.

| Field | Value |
|---|---|
| Purpose | Drop location for Jarvis's consolidated Part 2 harvest ZIP. It covers App Factory workflows and operating models, the RRM playbook with its pilot packages and campaign lessons, and the QAM proposals with their later rulings and pilot lessons. |
| Prepared by | Claudy (documentation Engineer seat), 2026-10-13 |
| Repository state | branch `factory-docs-review-astra-w-chunks`, HEAD `626da8d70f4db22987dc7fcc86765492072360cd`; main = origin/main = `9c179392f79b70da099121fc357d3107ad3bb86e` |
| Skill consulted | DocSet Sync `_SKILLS/factory-docs-update/` v0.8-DRAFT at main `9c17939`, read with `git show`. The skill was not activated. |

---

## 1. Why the drop location is here and not in `_INBOX/`

The DocSet Sync skill names one intake location: `_INBOX/` at the clone root (README Step 3). That bay is reserved for **approved** cargo that is about to be synced. When the skill activates, it treats every file in `_INBOX/` as cargo (CLAUDE.md §2). A non-empty `_INBOX/` also counts as a RESUME signal. The skill names no location for material that has not yet been approved.

This delivery has not been approved, so it cannot go into `_INBOX/`. Three existing records already rule that out:
- Correction index §13: DRAFT material must not be placed in `_INBOX/`.
- `DECISION_RECORD_001.md` §3: no `_INBOX/` drop is authorized.
- `RECOVERY.md`: no `_INBOX/` drop.

`factory-intake/` sits beside `factory-corrections/`, outside the five canonical tier folders and outside lint scope (`lints/lint_common.py` scans only the tier folders plus `MANIFEST.md` and `CHANGELOG.md`). The skill does not scan it, and nothing in it is cargo. No existing folder suited this purpose:
- `factory-corrections/` belongs to the correction package itself.
- `_AUDIT/` holds landed records and sync run folders.
- `_OTHERS/` holds landed non-canonical assets.

## 2. How Tony places the delivery

1. **Drop the ZIP here exactly as received. Do not extract it and do not rename it.** It goes at `factory-intake/<ZIP name>.zip`.
2. **Give Claudy the ZIP's SHA-256 as Jarvis stated it.** Paste it into the instruction, or include Jarvis's delivery note.
3. **When you instruct it, Claudy unpacks the ZIP.** Claudy first checks the hash, lists the archive and rejects any absolute or `..` paths. The contents are then extracted into a new, empty `factory-intake/<ZIP stem>/`. Neither the ZIP nor the extracted files are edited afterwards; they are the as-received record.

**Fallback:** if you only have the extracted files, put their top-level folder at `factory-intake/<folder name>/` unchanged. Without the ZIP, the as-received hash cannot be verified, and the report will say so.

**Git note:** the Hub has no `.gitignore`, so the ZIP will show as untracked. Whether a binary ZIP is committed is your decision.

## 3. What Jarvis's delivery must follow

The skill classifies material by its content, not its name (D16), so it requires **no particular filenames**. All filenames below are preferences. The requirements come from the sources named in each row.

### 3.1 Required

| # | Requirement | Source |
|---|---|---|
| R1 | One ZIP containing one top-level folder, named the same as the ZIP. | INTAKE_TAXONOMY "Cargo units": a folder is one unit. |
| R2 | A master index, three intake documents (one per material group) and a `sources/` folder. Sources are the original files, unedited. A transcription or excerpt is labeled as such. | Director instruction; D11 ("byte-for-byte as received"); D13. |
| R3 | Every authored document states its status at the top as DRAFT / not approved for sync. No document claims APPROVED unless Tony approved it, and then it cites that approval. | D16 (status decides the class); taxonomy class 1 requires APPROVED; "uploads are source material, not adoption approval". |
| R4 | Every authored document carries its author or seat, date, material group, and the package revision it references (§4). | D16 (provenance and authority). |
| R5 | The master index holds a **source register**, one row per source: source ID, path inside the ZIP, original title, origin (author, project or repo), original date or version, and kind (workflow or operating model · proposal · ruling · pilot lesson · campaign record). For a source held in Git, add repo + commit SHA + path. | D16 (provenance and authority); D11 (`REFERENCE.md` form). |
| R6 | Every harvested item cites its sources by source ID and section or heading. Each claim is labeled EVIDENCE, INFERENCE, CLAIM, GAP or QUESTION. | D12, D13. |
| R7 | **Precedence is traced, not inferred.** Where a later document (for example QAM) is said to supersede an older workflow, cite the explicit ruling: who ruled, when, where it is recorded, and the ruling text. Filename or date order alone is not evidence. If no ruling is found, the precedence is a QUESTION for Tony. | Director instruction; D16 (content-first); D17 (conflicts → Tony). |
| R8 | Every item states its scope: Factory DocSet candidate · **10X track** (ABM/APBM, outside Factory scope) · **Cyber Pharma pilot-specific** (Vibe Engineering, not proposed for the Factory) · other project-local. | Director boundaries; correction index §12. |
| R9 | Item IDs are stable, unique and never reused. They must not use a reserved prefix: `FC-`, `CF-` or `DEC-` (correction package), or `IN-`, `XB-`, `GAP-`, `DRIFT-` or `QA-F` (minted by DocSet Sync). | D16 (the ID is the join key); INTAKE_TAXONOMY "IDs". |
| R10 | Every item states its level. **Edit-level** gives the target doc, placement and exact proposed wording. **Intent-level** gives the rule that must become true. Targets use canonical filenames as listed in `MANIFEST.md` on main, or `NEW`. | Taxonomy classes 1–2; D15 (approved wording lands verbatim). |
| R11 | Where an item overlaps the correction package, it cites the package by ID and states the relation (§4). It does not copy, renumber or restate package content. | D16, D17; Director instruction. |
| R12 | The ZIP's SHA-256 travels with the delivery. | Verification of the as-received bytes (§2). |

### 3.2 Preferred (convenience; not blocking)

- **ZIP name:** `PART2_HARVEST_INTAKE_<YYYY-MM-DD>.zip`.
- **Filenames:** named after the correction package's files:
  - `FACTORY_DOCTRINE_HARVEST_INDEX_001.md`
  - `01_workflows_operating_models_harvest.md`
  - `02_rrm_harvest.md`
  - `03_qam_harvest.md`
  - `sources/01_workflows/…`, `sources/02_rrm/…`, `sources/03_qam/…`
- **ID prefixes:** item IDs `HV-WF-01`, `HV-RRM-01`, `HV-QAM-01`; source IDs `SRC-WF-01`, `SRC-RRM-01`, `SRC-QAM-01`.
- **Status phrase:** "DRAFT — HARVEST INTAKE / NOT APPROVED FOR SYNC".
- **Formats:** Markdown, UTF-8 without BOM, LF line endings; ASCII filenames without spaces.
- **Checksums:** a per-file SHA-256 list in the master index.

## 4. How the harvest references Correction Package 001

- **One home.** `factory-corrections/` remains the only home of the 97 FCs, the 17 CFs and DEC-01 … DEC-22. The harvest does not copy, replace, renumber or edit them.
- **Cite by ID plus file.** For example, `FC-051` (`factory-corrections/05_api_commerce_corrections.md`) or `DEC-03` (`factory-corrections/DECISION_RECORD_001.md`). FC and CF IDs and their certified records are identical across R0–R2. DEC-01 … DEC-22 keep their numbers, but R1 reworded DEC-01 and DEC-05, so cite DEC meanings as worded in R2.
- **Revision pin: R2.** That is the working tree over HEAD `626da8d`; R1 and R2 are not committed yet. Once Tony commits them, that commit SHA becomes the pin.
- **Relation per overlapping item** (suggested vocabulary):
  - `SAME`: an FC already covers it, and the harvest adds evidence only.
  - `EXTENDS`: it adds scope beyond the FC.
  - `CONFLICTS`: it is incompatible with an FC outcome or an approved direction. This is a QUESTION for Tony, not resolved by the harvest.
  - `NEW`: no FC covers it.
- **Approved directions are context, not reopened.** These are DEC-01, DEC-02, DEC-03, DEC-04 and DEC-16, all scoped (`DECISION_RECORD_001.md` §1). Material bearing on an open decision, such as DEC-05's quote design, is cited as input to that decision, not as a ruling.
- **Order.** Per correction index §12, the harvest is resolved before the package's intake approval. Pointing index §12 at the harvest is a later, separately approved edit.
- **IDs at sync time.** If Tony approves the harvest as a correction package, its item IDs are kept. Otherwise DocSet Sync mints `IN-…` IDs at intake and records the harvest IDs beside them.

## 5. What this folder does not authorize

It does not authorize any of the following:
- adoption of any material;
- an `_INBOX/` drop or a DocSet Sync run;
- an UPDATE MAP;
- edits to canonical doctrine, the correction package, skills, `MANIFEST.md`, `CHANGELOG.md`, lints or CI;
- Git mutations.

Moving approved material into `_INBOX/` is a later step that Tony approves separately.
