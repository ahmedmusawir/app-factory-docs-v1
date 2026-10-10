# 📋 PLAN — Part 1 Convergence Workspace (2026-09-27 11:52)

🔵 ENTERING PLAN MODE
Task: Create `astra-review/run-002/synthesis/PART1_FINDINGS_DISPOSITION.md`, a draft for evidence convergence only.

## Source Inventory (inspected, read-only)

| Source | Location | Size | Defect findings | Suggestions |
| --- | --- | --- | --- | --- |
| Astra C01 governance | `chunks/01_governance/ASTRA_REVIEW.md` | 182 L | 3 (D01–D03) | 3 |
| Astra C02 agents/handoffs | `chunks/02_agents_handoffs/ASTRA_REVIEW.md` | 219 L | 6 (D01–D06) | 4 |
| Astra C03 build method | `chunks/03_build_method/ASTRA_REVIEW.md` | 294 L | 14 (D01–D14) | 3 |
| Astra C04 auth/data/security | `chunks/04_auth_data_security/ASTRA_REVIEW.md` | 308 L | 17 (D01–D17) | 3 |
| Astra C05 api/commerce | `chunks/05_api_commerce/ASTRA_REVIEW.md` | 297 L | 18 (D01–D18) | 3 |
| Astra C06 design/frontend | `chunks/06_design_frontend/ASTRA_REVIEW.md` | 308 L | 12 (D01–D12) | 2 |
| Astra C07 skills/doc governance | `chunks/07_skills_doc_governance/ASTRA_REVIEW.md` | 330 L | 11 (D01–D11) | 3 |
| **Astra total** | | | **81** | **21** |
| Sol C01–C05 | `chunks/0[1-5]*/SOL_REVIEW.md` | 571–1001 L each | severity adjustments per finding | |
| Sol C06, C07 | `chunks/06*/SOL_REVIEW.md`, `chunks/07*/SOL_REVIEW.md` | **0 bytes (empty)** | none | |
| Fable whole-corpus | `git show origin/factory-docs-review-fable-001:fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md` | 743 L | **31** (FBL-D001–D031: 2 BLOCKER, HIGH / MEDIUM / LOW sets) | 14 (FBL-S001–S014) |

- The chunk-level `DISPOSITION.md` and `FABLE_REVIEW.md` files in all 7 chunks are **0-byte placeholders**, so there is nothing to read.
- Excluded on purpose, not read: the Fable branch's `SOL_REVIEW_OF_FABLE_001.md` and `FINAL_DISPOSITION.md`. Also not read: run-002 `synthesis/*` (ASTRA synthesis, SOL/FABLE synthesis reviews, FINAL_DISPOSITION), because they aren't in the evidence list.

## 📋 PLAN

1. **Read in full:** all 7 ASTRA_REVIEW files, SOL reviews 01–05, and the Fable review through `git show`. This gives the IDs, titles, severities, mechanisms and cited files for each finding.
2. **Extract ledgers:**
   - Astra: 81 rows with ID, title, Astra severity and cited docs/sections.
   - Sol: an adjustment column taken only from what Sol actually stated. Where Sol stated nothing, write "none stated". For C06/C07, write "no Sol review (file empty)".
   - Fable: 31 rows with ID, title, severity and cited docs/sections.
3. **Group into FC-### root issues** by *shared mechanism plus the same doctrine location*. The rule is conservative: findings merge only when they describe the same defect in the same doctrine surface. Findings that are only similar in theme get a cross-reference ("see also"), not a merge.
4. **Assign REVIEW BASELINE STATUS:**
   - CONFIRMED = both reviews found the same mechanism.
   - PARTIAL = overlap, but the scope or locus differs.
   - UNIQUE = only one reviewer found it.
   - CONFLICT = the reviews disagree on fact or severity direction.
5. **Fill the fixed fields:** CURRENT-MAIN STATUS = `UNKNOWN — TO BE VERIFIED`. PROPOSED DISPOSITION, FINAL SEVERITY and CORRECTION REQUIRED are left blank.
6. **Build the summary sections:** source inventory, Astra and Fable totals, an unmapped list (target: zero), cross-review contradictions, a unique-Astra list, a unique-Fable list, and a reverse index (every Astra ID and every Fable ID pointing to its FC-###) so coverage can be checked by eye.
7. **Verify mechanically:** grep the new file for all 81 Astra IDs and all 31 FBL-D IDs. Run `git status` / `git diff` read-only and show you the diff.

## FILES TO CREATE
- `astra-review/run-002/synthesis/PART1_FINDINGS_DISPOSITION.md`: the convergence draft.

## FILES I WILL NOT TOUCH
- Every ASTRA_REVIEW, SOL_REVIEW, chunk DISPOSITION/FABLE_REVIEW placeholder, all of `synthesis/*` including FINAL_DISPOSITION.md, all doctrine folders (01–05, _SKILLS, lints, MANIFEST, CHANGELOG), and the Fable branch.
- `RECOVERY.md`: out of date, but only updated on completion per protocol (see Q3).

## ASSUMPTIONS
1. **Suggestions (Astra C0x-S##, Fable FBL-S###) are out of scope for FC mapping.** "Every defect finding" means D-IDs. I'll list the suggestions in the inventory as "not mapped: suggestion class" so they're visible but don't count as unmapped.
2. **Fable §9 contradiction-table rows are not separate findings.** Each row already points to an FBL-D ID, so I use them only as evidence.
3. **Sol "severity adjustment"** = only what Sol explicitly wrote (e.g. "Provisional severity: X", "do not accept BLOCKER until disposition"). I record it word-for-word or in close paraphrase with a line reference, and I don't infer anything beyond that.
4. **Astra severity:** C03–C07 appear ranked without an explicit severity label on each heading. If a finding has no explicit severity label, I record the Astra rank plus whatever label the body gives, and never invent one.
5. **Grouping is 1-to-many in both directions.** One FBL-D can map to several FCs; for example, FBL-D001 spans C04-D01, C04-D02, C04-D08 and likely C01-D01. Every ID lands in exactly one *primary* FC, and any extra links are marked "also relates".

## ⚠️ CONFLICT TO RESOLVE BEFORE I WRITE
Your DONE criterion says: *"working tree contains only the new/updated convergence artifact."* That can't be fully true right now, for two reasons:
- **Already in the tree before this task:** 6 deleted `agent_docs/RESPONSES/response_2026-08-10_*.md` plus the untracked, empty `agent_docs/readme.md`. I won't touch them.
- **Required by CLAUDE.md, and already written:** `session_2026-09-27.md` and `agent_docs/RESPONSES/response_2026-09-27_*.md` (bootstrap report and this plan). A completion report will add one more.

→ Q1: Is it OK for the working tree to have the convergence file **plus** the session/RESPONSES logs (and the pre-existing deletions)? Or should I keep the logs outside the repo this time?
→ Q2: Confirm that suggestions are out of scope (Assumption 1).
→ Q3: Should I update RECOVERY.md on completion as protocol requires, or leave it alone so the diff stays clean?

## RISKS
- Merge judgement is the core risk. I'll lean toward UNIQUE/PARTIAL with "see also" links over forced CONFIRMED merges, and give a one-line basis for each status.
- Output size: about 60–80 FC entries, so the file will be large (roughly 1,500+ lines). Each FC block stays compact.

→ Awaiting approval before proceeding.
