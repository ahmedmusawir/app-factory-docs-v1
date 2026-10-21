✅ PART 2 INTAKE DROP LOCATION PREPARED (STOP)

The drop folder is ready for Jarvis's ZIP. Nothing has been adopted, synced or mapped.

**Repository state**
- Branch: `factory-docs-review-astra-w-chunks`
- HEAD: `626da8d70f4db22987dc7fcc86765492072360cd`
- main = origin/main = `9c179392f79b70da099121fc357d3107ad3bb86e`
- Working tree: the R1 and R2 package edits are still uncommitted and untouched. They are 8 modified `factory-corrections/` files plus the new `DECISION_RECORD_001.md`. The 2026-10-12 bookkeeping is also uncommitted.
- This task added `factory-intake/README.md`, `session_2026-10-13.md` and this report, and updated `RECOVERY.md`. Nothing is staged.

**Drop folder:** `/home/moose/Documents/app-factory-docs-v1/factory-intake/`
- **Why not `_INBOX/`:**
  - The current skill (v0.8-DRAFT on main; this branch has an older copy) uses `_INBOX/` only for *approved* cargo at sync time.
  - When the skill runs, anything in `_INBOX/` is treated as cargo and as a RESUME signal.
  - Index §13, DECISION_RECORD_001 §3 and RECOVERY.md each rule out an `_INBOX/` drop now.
  - The skill names no location for unapproved material. I therefore made a sibling of `factory-corrections/`, outside the tier folders, `_INBOX/` and lint scope.
- **ZIP or extract:** Tony **drops the ZIP as received**, unextracted and unrenamed, together with Jarvis's SHA-256. When instructed, Claudy checks the hash, lists the archive and extracts it into a new `factory-intake/<ZIP stem>/`. If only extracted files exist, place their folder there unchanged; the as-received hash then cannot be verified.

**What Jarvis must follow** (full table with sources in README §3)
- *Required:*
  - One ZIP with one top-level folder of the same name.
  - A master index, three intake docs, and `sources/` holding unedited originals.
  - Every authored doc states DRAFT status, plus its author, date, group and the package revision it references.
  - A source register in the index: ID, path, title, origin, date or version, and kind. Sources held in Git also get repo + SHA + path.
  - Every item cites a source ID and section. Claims are labeled EVIDENCE / INFERENCE / CLAIM / GAP / QUESTION.
  - **Precedence is traced to explicit rulings** (who, when, where, text), never inferred from filenames or dates. If no ruling is found, it is a QUESTION for Tony.
  - Each item states its scope: Factory candidate · 10X (ABM/APBM) · Cyber Pharma pilot (Vibe Engineering) · project-local.
  - Item IDs are unique and stable and avoid reserved prefixes: `FC/CF/DEC`, and `IN/XB/GAP/DRIFT/QA-F`.
  - Each item is marked edit-level or intent-level. Targets use the canonical MANIFEST filename, or `NEW`.
  - The ZIP's SHA-256 travels with the delivery.
- *Preferences only.* The skill classifies by content, so **no filename is required**. Suggested conventions:
  - ZIP name `PART2_HARVEST_INTAKE_<date>.zip`
  - `FACTORY_DOCTRINE_HARVEST_INDEX_001.md` and three `0N_…_harvest.md` files
  - `HV-` item IDs and `SRC-` source IDs
  - UTF-8 with LF line endings
  - per-file hashes

**How the correction package is referenced**
- Package items are cited by ID plus file, for example `FC-051` (`05_api_commerce_corrections.md`) or `DEC-03` (`DECISION_RECORD_001.md`). They are never copied, renumbered or edited.
- The pin is R2: the uncommitted working tree over `626da8d`. It becomes a commit SHA once you commit. R1 reworded DEC-01 and DEC-05, so cite DEC meanings as worded in R2.
- Each overlap gets a relation: SAME / EXTENDS / CONFLICTS / NEW. CONFLICTS goes to Tony; the harvest does not resolve it.
- The approved DEC-01/02/03/04/16 directions are context and are not reopened. Material on an open decision, such as DEC-05, is input to that decision, not a ruling.
- The harvest is resolved before the package's intake approval (index §12). Pointing §12 at the harvest is a later, separately approved edit.

**Files**
- Created: `factory-intake/README.md`, `session_2026-10-13.md`, this report.
- Changed: `RECOVERY.md`.
- Untouched (verified): the package (9/9 hashes identical), the 100 protected files, canonical doctrine, skills, MANIFEST, CHANGELOG, lints and CI. HEAD is unchanged and nothing is staged. No sync was run and no update map was made.

**Concern:** R1 and R2 are not committed. If you want a commit SHA as the pin before Jarvis delivers, this optional block is yours to run:

```bash
git add factory-corrections/ factory-intake/README.md
git commit -m "docs(corrections): R1 revision, R2 decision record, intake staging README (draft, not approved for sync)"
git push
```

→ **STOP.** Ready for Tony's upload.

📥 Drop folder: /home/moose/Documents/app-factory-docs-v1/factory-intake/
📄 Logged: agent_docs/RESPONSES/response_2026-10-13_170824_part2-intake-drop-prepared.md
