🔵 PART 2 — CORRECTION PACKAGE DRAFT: PLAN (authorized by the instruction; proceeding)

**Verified state matches the Director's**
- Branch `factory-docs-review-astra-w-chunks`, HEAD `c6210c32480558b343a27726a26822e8d959d0f7`.
- main = origin/main = `9c179392f79b70da099121fc357d3107ad3bb86e`, divergence 0/0.
- Working tree is clean apart from this session's three bootstrap bookkeeping files (RECOVERY.md, session_2026-10-11.md, one RESPONSES file).
- Certified register and QA report are byte-identical to c6210c3. QA verdict: PASS, 0 findings.
- Fable source was read through `origin/factory-docs-review-fable-001` (`39a1c61`, blob `55dd3e9`).
- DocSet Sync CLAUDE.md and README.md were read from main via `git show`, without activating the skill.

**Plan**
1. **One primary entry per FC.** Each FC goes in the brief matching its certified register §5 subsection: 5.A→01 (12), 5.B→02 (7), 5.C→03 (13), 5.D→04 (17), 5.E→05 (21), 5.F→06 (14), 5.G→07 (13). That totals 97.
2. **IDs stay as certified.** Correction ID = FC ID, and the CF is the planning unit. Mappings, severities and statuses are copied from the register, never re-derived.
3. **Every entry carries the same fields:**
   - IDs and pinned sources
   - the defect and its current-main status
   - a PROPOSED outcome
   - what to preserve
   - likely affected documents and consumers
   - verification intent
   - open decisions
   - a proposed delivery route: DocSet Sync, or cross-boundary per DocSet Sync §1 (skills, lints/CI, root CLAUDE.md, external)
4. **The index** gives:
   - totals
   - the six BLOCKERs first
   - the 17-family table
   - a 97-row master table
   - a prioritized decision list for Jarvis/Tony
   - the 35 suggestions as an optional backlog
   - the newer-doctrine harvest, kept separate and PENDING
5. **Validation:**
   - parse all 8 files against the register
   - check pinned paths exist at their revision
   - rerun lints and compare to the baseline
   - re-hash the protected inputs
   - confirm write scope

**Assumptions**
1. "Primary brief" follows the certified register section, not the CF. CF membership appears in every entry and in the index.
2. No replacement doctrine text. Outcomes say what must become true.
3. The three remediated FCs (085, 086, 097) get "no new correction" entries with a regression guard only.

**Boundaries:** no canonical doctrine, MANIFEST, CHANGELOG or skill edits; no Git writes; no subagents; no sync.

📄 Logged: agent_docs/RESPONSES/response_2026-10-11_213059_part2-correction-package-plan.md
