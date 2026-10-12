✅ PART 2 — FACTORY DOCTRINE CORRECTION PACKAGE 001: DRAFT DELIVERED (STOP for Architect/Director review)

I wrote the draft correction package: an index plus seven briefs covering all 97 certified findings. All checks pass. Every file is labeled DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC. Nothing is approved, nothing is synced, and nothing is committed.

**Starting state (verified before writing; matched the Director's)**

| Item | Value |
| --- | --- |
| Branch | `factory-docs-review-astra-w-chunks` |
| Starting HEAD | `c6210c32480558b343a27726a26822e8d959d0f7` (unchanged at finish) |
| main / origin/main | `9c179392f79b70da099121fc357d3107ad3bb86e` / same, divergence 0/0 |
| Dirty at start | only this session's 3 bootstrap bookkeeping files |

**Output files (`factory-corrections/`)**

| File | Primary FCs |
| --- | ---: |
| `FACTORY_DOCTRINE_CORRECTION_INDEX_001.md` | index |
| `01_governance_corrections.md` | 12 (FC-001 … 012) |
| `02_agents_handoffs_corrections.md` | 7 (FC-013 … 019) |
| `03_build_method_corrections.md` | 13 (FC-020 … 032) |
| `04_auth_data_security_corrections.md` | 17 (FC-033 … 049) |
| `05_api_commerce_corrections.md` | 21 (FC-050 … 070) |
| `06_design_frontend_corrections.md` | 14 (FC-071 … 084) |
| `07_skills_doc_governance_corrections.md` | 13 (FC-085 … 097) |

**Coverage**
- **All 97 FCs:** one primary entry each, no duplicates. Each sits in the brief matching its certified register section.
- **All 17 Correction Families:** the membership and severity mix recomputed from the briefs match the register's family table exactly.
- **Certified totals preserved:**
  - severity: 6 BLOCKER, 36 HIGH, 44 MEDIUM, 11 LOW;
  - current main: 81 source unchanged, 8 defect remains, 5 partial, 3 remediated;
  - correction required: 94 yes, 3 no.
- **The three remediated FCs** (085, 086, 097) carry "NO NEW CORRECTION" and a regression guard only.
- **Every correction entry** has a PROPOSED outcome, what to preserve, affected documents, verification intent, open decisions and a proposed route.
- **Route counts:**
  - 89 FCs go through DocSet Sync.
  - Some FCs also, or only, need cross-boundary work that DocSet Sync won't do:
    - skills: 5 FCs
    - root CLAUDE.md: 5 FCs
    - external repositories: 6 FCs
    - lints/CI: 2 FCs
  - Five FCs are cross-boundary only: 090, 091, 092, 094, 095.
- **Suggestions:** all 35 are listed as an optional backlog, not as defects.
- **Newer-doctrine harvest:** kept separate and pending. ABM/APBM stay 10X-only and Vibe Engineering stays project-local. None of them appears in the Hub (that gap is recorded).

**Validation (my own read-only checks; not independent QA)**
- **Register cross-check:** 0 problems. Every entry's family, severity, review status, current-main status, correction value, title and reviewer IDs match the register at c6210c3.
- **Pinned paths:** 98 path references resolve at their stated revisions, including the index's pointer to this report. Six don't, and all six are deliberately cited missing paths:
  - `_ARCHIVE/QA_PLAYBOOK_v1_0.md` (the FC-089 defect)
  - `agent_docs/APP_FACTORY` paths (FC-003, FC-081)
  - `agent_docs/LESSONS` (FC-009)
- **Document checks:** 0 problems across all 8 files (UTF-8, line endings, table structure, headings, DRAFT label).
- **Lints:** output is byte-identical before and after. The suite still exits 1, but only on the 9 pre-existing findings (8 versioned references + 1 missing header). Those are recorded as FC-096. I did not fix them.
- **Protected inputs:** all 100 tracked files are byte-identical; all 12 Git refs are unchanged; nothing is staged.
- **Write scope:** only the 8 package files plus bookkeeping.

**BLOCKERs, prioritized (index §5)**
1. **FC-033:** auth recipes authorize from user metadata, plus an app-side superadmin creation route.
2. **FC-034:** public signup forwards role metadata.
3. **FC-036:** a layout check is treated as authorization for privileged actions.
4. **FC-050:** the browser can assert that an order is paid.
5. **FC-051:** the payment amount comes from client-supplied prices.
6. **FC-020:** webhooks always return 200.

My recommendation (proposed only): contain each one first (remove or quarantine the unsafe recipe and point to the rule that already governs it), then rewrite against the verified kit later.

**Decisions needed from Jarvis/Tony (index §9 has the full list)**
- **Priority 1, gates the BLOCKER wave:**
  - DEC-01: adopt the package structure and the sync cargo plan.
  - DEC-02: retire or rewrite the legacy auth recipes.
  - DEC-03: the webhook acknowledgment rule.
  - DEC-04: "every privileged operation authorizes its own invocation."
  - DEC-05: where the commerce quote comes from.
- **Priority 2, foundational:**
  - DEC-06: precedence model.
  - DEC-07: seat glossary.
  - DEC-08: whether root CLAUDE.md is governed doctrine.
  - DEC-09: kit verification (cookie flag, page guard, rail breakpoint).
  - DEC-21: who runs the cross-boundary jobs.
- **Priority 3–4:** DEC-10 … DEC-20 and DEC-22, covering artifacts, process, distribution, lint policy and optional severity re-elevation.

**Things I didn't touch**
- No canonical doctrine, MANIFEST, CHANGELOG (left unchanged per your instruction), skills, lints, CI or root CLAUDE.md.
- The certified register, the QA report, the 14 chunk reviews and the Fable branch are all unchanged.
- No Git writes, no subagents, no DocSet Sync activation or `_INBOX/` drop.

**Potential concerns**
- **Brief placement follows the register sections, not the families.** A few FCs sit outside their family's usual brief (FC-008, FC-010, FC-063, FC-088). Index §7 gives the family view. Regrouping by family would be a reshuffle, not a content change.
- **Some outcomes need evidence the Hub doesn't hold:**
  - the kit repository (FC-041, FC-042, FC-072);
  - deployment-platform procedures (FC-011);
  - the commit that carried QA v1.0 (FC-089);
  - the skills that live outside the Hub (FC-009).

  These are marked as gaps.
- **Seat naming is inconsistent.** Your instruction names Sol as Architect; DocSet Sync v0.8 seats Sol as QA Lead. I logged it as input to DEC-07.
- **This is self-checked, not independently verified.** I authored the package, so independent QA needs a different seat.
- **The validation scripts are in my session scratchpad, not the repo.** They may not survive. Adding them to the repo would need your approval.

**Final git status**
```text
 M RECOVERY.md
?? agent_docs/RESPONSES/response_2026-10-11_212534_session-bootstrap.md
?? agent_docs/RESPONSES/response_2026-10-11_213059_part2-correction-package-plan.md
?? agent_docs/RESPONSES/response_2026-10-11_215527_part2-correction-package-draft.md
?? factory-corrections/01_governance_corrections.md
?? factory-corrections/02_agents_handoffs_corrections.md
?? factory-corrections/03_build_method_corrections.md
?? factory-corrections/04_auth_data_security_corrections.md
?? factory-corrections/05_api_commerce_corrections.md
?? factory-corrections/06_design_frontend_corrections.md
?? factory-corrections/07_skills_doc_governance_corrections.md
?? factory-corrections/FACTORY_DOCTRINE_CORRECTION_INDEX_001.md
?? session_2026-10-11.md
```

**Change summary:** 8 new package files (263,832 bytes, 3,101 lines), 3 new RESPONSES files, a new session file, and RECOVERY.md updated. HEAD is unchanged and nothing is staged.

**Optional: checkpoint the draft** (only if you choose to; no agent runs this; per the standing rule there is no Co-Authored-By line):
```bash
git add factory-corrections/ session_2026-10-11.md RECOVERY.md agent_docs/RESPONSES/response_2026-10-11_*.md
git commit -m "docs(corrections): draft factory doctrine correction package 001 (not approved for sync)"
git push
```

→ **STOP.** The draft is waiting for Architect/Director review. No synchronization has begun.

📄 Logged: agent_docs/RESPONSES/response_2026-10-11_215527_part2-correction-package-draft.md
