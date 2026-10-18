# CONVENTIONS.md — map-part drafting contract for the PART_0N forks (run SYNC_2026-10-15_doctrine-part2)

> You are a fork of the Engineer seat (Claudy/Opy), drafting ONE map part (`scratchpad/map_parts/PART_0N.md`) for the DocSet Sync UPDATE MAP. This file is your contract. Read it fully before touching anything. You write ONLY your PART file. No canonical edits, no Git commands, no other files, no deletions. Everything else is read-only.

## 1. Run facts (do not re-derive; cite as given)

| Field | Value |
|---|---|
| Run | `SYNC_2026-10-15_doctrine-part2` |
| BASE_SHA | `9c179392f79b70da099121fc357d3107ad3bb86e` (main = origin/main; the working tree is byte-identical to it over the whole canonical scope: `0?_*`, MANIFEST.md, CHANGELOG.md, `_ARCHIVE/`, lints, `.github`, `_OTHERS/`. Only `_SKILLS/` differs — an older copy; irrelevant to your greps.) |
| Propagation scope (D19) | `01_CONSTITUTION 02_PIPELINE_AGENTS 03_BUILD_METHODOLOGY 04_REFERENCE_MANUALS 05_DESIGN_SYSTEM MANIFEST.md CHANGELOG.md` — `_SKILLS/` and `_OTHERS/` read-only for AWARENESS hits only (disposition OUT-OF-SCOPE → §I/§J candidates) |
| Command shape | `grep -rn -i -E "<term>" 01_CONSTITUTION 02_PIPELINE_AGENTS 03_BUILD_METHODOLOGY 04_REFERENCE_MANUALS 05_DESIGN_SYSTEM MANIFEST.md CHANGELOG.md` |
| Lint baseline (pre-existing, §M) | 9 findings: STARTER_KIT_HANDBOOK L258/261/688/690/692 + DATABASE_MANUAL L8/156 [VERSIONED-REFS]; STARTER_KIT_HANDBOOK L1 [HEADER-PRESENCE] |
| Live-doc reality | 31 tier docs on disk; MANIFEST has 31 rows but STATES "29" (×3) and its appendix says "27 bodies" — pre-existing drift, FC-093 authorizes the recompute; this run adds 3 new docs (RRM_PLAYBOOK, QAM_PLAYBOOK, DEPLOYMENT_PLAYBOOK → 34). Do not "fix" anything; record facts. |
| New docs landing this run (RUL-06) | `03_BUILD_METHODOLOGY/RRM_PLAYBOOK.md`, `03_BUILD_METHODOLOGY/QAM_PLAYBOOK.md`, `03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md` — full drafts already exist at `_AUDIT/SYNC_2026-10-15_doctrine-part2/DRAFTS/` with their own Version History rows and cross-references (already placement-verified by the main session). Do NOT propose creating or editing them. If your FC overlaps them, say "handled by the §D draft" and reference the draft's section. |

## 2. Read order (before writing anything)

1. This file.
2. Your brief: `factory-corrections/0N_<domain>_corrections.md` — your only FC source. Quote it verbatim with line numbers.
3. `factory-corrections/FACTORY_DOCTRINE_CORRECTION_INDEX_001.md` — package authority: §4 totals, §5/§6 FC tables + routes, §7 CF families, §9 DEC ledger. Follow its routes and statuses verbatim; never re-argue a correction (D17).
4. `/tmp/opencode/skill_v08/_shared/templates/UPDATE_MAP.md` — the §B/§C row shapes you must produce.
5. `/tmp/opencode/skill_v08/_shared/references/INTAKE_TAXONOMY.md` — disposition vocabulary.
6. `MANIFEST.md` — for the ← (referenced-by) rows of your target docs.
7. The live target docs themselves — placements must be verified against ACTUAL section structure at BASE (D13): every placement you propose carries `path:line` and the real heading/anchor text. A stated placement that does not exist → report the mismatch with the nearest real anchor; never improvise.

## 3. Disposition statuses you must apply (from the planning records; do not re-adjudicate)

- **Approved (scoped, 2026-10-12):** DEC-01, DEC-02, DEC-03, DEC-04, DEC-16 (form/direction only; the package stays DRAFT).
- **Director rulings (2026-10-14, `factory-intake/PLANNING_001/DIRECTOR_RULINGS_2026-10-14.md`):** RUL-01 QAM mandatory for every newly authored module · RUL-02 continuing `qa/<module>` branch (created at the completed engineering candidate; merged into main; never abandoned) · RUL-03 cleanup checkpoint required; only abandon/transfer-back retired; module QA records under `agent_docs/` in the QAM structure; deployment exclusion of `agent_docs/**` enforced and verified · RUL-04 frozen contract, declared writable lanes, attributable amendments only · RUL-05 two review checkpoints (after FFM+QA; Engine 2 after all Engine 1 phases + QA); findings dispositioned; clean review → no RRM; each RRM includes QAM · RUL-06 placement: the three playbooks in `03_BUILD_METHODOLOGY/`; operating models fold into existing playbooks · RUL-07 boundaries: 97 FC identities/fields/totals preserved; no TRM definition; no tooling approval; ABM/APBM stay on the 10X track.
- **Architect decisions:** AD-00 consolidated-intake structure accepted; AD-01 template home `03_BUILD_METHODOLOGY/_templates/QAM/` (landing rides this run; the 25-file set is QA-Lead-accepted + Architect-verified).
- **OPEN policy decisions that GATE specific FCs — mark every affected row CONDITIONAL[<decision>] and still draft the recommended wording** (the map presents it; Gate 2 rules; drafting approves NOTHING):

| Open decision | FCs it gates (your rows stay CONDITIONAL) |
|---|---|
| D.2 (DEC-10/11/12) DATA_CONTRACT timing / UI_SPEC owner / FILE_TREE | FC-008, FC-015, FC-016, FC-017, FC-019, FC-027 |
| C.2 (DEC-18 remainder) DevOps seat / cloud matrix / staging | FC-011, FC-012, FC-088 (DEPLOYMENT_PLAYBOOK still lands with its RULED content) |
| DEC-05 commerce quote design | FC-050, FC-051, FC-060, FC-067 (land only to the certified-requirement extent) |
| DEC-17 doctrine tag / project pinning | FC-003, FC-081, FC-088 (recommended: pin by canonical name + header version + Hub commit SHA; no tag this run) |
| D.1 (DEC-07 remainder) seat glossary | FC-004, FC-006, FC-007, FC-027 (default: synonyms kept, no mass rename, glossary at SOFTWARE_FACTORY_PLAYBOOK §2) |
| D.3 (DEC-14) recon lanes / diagnostics | FC-014, FC-022, FC-023, FC-029, FC-030 |
| B.2 (RRM-09) reviewer guidance placement | FC-009 (reviewer-artifact part) |
| E (ND-07) one-shot engineering default | (no FC; affects draft sentences only) |
| DEC-06 precedence/reconciliation host | FC-001, FC-005, FC-029, FC-042, FC-073 |
| DEC-08 root CLAUDE.md status | FC-010, FC-008 (root-reference part), FC-090, FC-091, FC-094 |
| DEC-09/E-10 kit verification (no kit access) | FC-041, FC-042, FC-072 — cannot complete in this run (XB-EXT) |
| DEC-15 personal-data retention | FC-040 |
| DEC-20 QA_PLAYBOOK v1.0 archive | FC-089 |
| DEC-22 optional severity re-elevations | FC-002, FC-037, FC-052, FC-061 (certified severities kept until ruled) |
| DEC-19 remainder kits/examples/locator | FC-009 (kit part), FC-003 (locator part) |

- **Cross-boundary routes (follow the index §5/§6 route per FC; never edit those targets):** `XB-SKILL` (other `_SKILLS/*` incl. the docs-update skill's git wording), `XB-ROOT` (root `CLAUDE.md`/`AGENTS.md`), `XB-LINT/CI` (`lints/`, `.github/`), `XB-EXT` (starter-kit repo, external). These rows get disposition **SPLIT** with the target named — a short §B block (intent verbatim + target + why parked + blocking Y/N) and a §J candidate row; NO §C row, NO propagation dispositioning beyond an awareness note.
- **NO-CHANGE (FC-085, FC-086, FC-097 regression guards, or any intent you find already true):** a PROPOSAL with `path:line` + quoted evidence, valid only when Tony approves the row at Gate 2. Never state it as done.

## 4. Output format (your PART file)

Header: `# PART_0N — <domain> — map-part draft for UPDATE_MAP §B/§C` plus a 3-line summary (FCs covered, dispositions tallied from your rows, open items). Then one block per FC, in FC-number order, exactly this shape:

```markdown
### FC-0NN — <title> — <severity> — route <SYNC|XB-*> — disposition <CHANGE|NO-CHANGE (proposal)|SPLIT→<target>|CONDITIONAL[<decision>]>

- **Approved intent (verbatim):** "<exact text>" [CLAIM: factory-corrections/0N_*.md:L<nn>]
- **Must-become-true invariants (verbatim):** 1. … 2. … [CLAIM: …:L<nn>]
- **Preservation constraints (verbatim):** 1. … [CLAIM: …:L<nn>]
- **Likely affected files (from brief):** … + **MANIFEST ← rows:** <doc> ← <referencing docs from MANIFEST>
- **Propagation search (D19):**
  - Terms: `"<old wording>"`, `<name>`, `<cited filename>` …
  - Hits (rows are the count; no separate total):
    | # | Path:line | Hit (quoted ≤15 words) | Disposition (CHANGE/CONSISTENT/HISTORY/OUT-OF-SCOPE) | Drives §C/§F/§J | Label |
    |---|---|---|---|---|---|
- **Verified placements:** <path:line + real heading> — or MISMATCH: brief says X, live reality is Y (nearest real anchor Z)
- **Proposed §C rows:** for each: canonical doc · placement (path:line anchor) · proposed wording (full text for new/replaced sentences, INTAKE-VERBATIM or ENGINEER-PROPOSED per D15) · version live → new · contributing IDs · structural? · minimal-form note (D14)
- **NO-CHANGE proposal (if any):** intent already true at path:line — "<quote>"
- **CONFLICT / open questions → §K candidates:** exact question + evidence + what it blocks (type CONFLICT only for doctrine/authority collisions; mechanical details are CLARIFICATION)
- **Dependencies:** other FCs / DEC items / N-items this row depends on
```

Rules: evidence labels on every non-trivial claim (EVIDENCE path:line / INFERENCE from-what / CLAIM source / GAP looked-where / QUESTION needs-Tony). Counts derive from your enumerated rows, never maintained by hand (AP-23). Quote the brief VERBATIM — you never re-argue a correction, reword an intent, or drop a preservation constraint (D17). Any word you add beyond the brief's text is marked ENGINEER-PROPOSED (D15). Minimal diff on high-← docs (D14) — say so when you chose the minimal form.

## 5. Worked micro-example (illustrative shape only — your content comes from YOUR brief)

```markdown
### FC-XYZ — Example title — MEDIUM — route SYNC — disposition CHANGE

- **Approved intent (verbatim):** "The doc must state X before Y." [CLAIM: factory-corrections/0N_...md:L42]
- **Must-become-true invariants (verbatim):** 1. "X precedes Y in every checklist." [CLAIM: …:L43]
- **Preservation constraints (verbatim):** 1. "Do not remove the Z rule." [CLAIM: …:L44]
- **Likely affected files:** `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` · **MANIFEST ← rows:** BIM_PLAYBOOK ← FEAT_PLAYBOOK (1)
- **Propagation search:** Terms: "old term", "Old Term", "old-term". Hits:
  | 1 | 03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:77 | "old term governs…" | CHANGE | §C row 1 | EVIDENCE |
  | 2 | 01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:512 | "old term (see BIM §6)" | CHANGE | §C row 2 | EVIDENCE |
  | 3 | 03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md:601 | "old term" under Version History | HISTORY | exempt | EVIDENCE |
- **Verified placements:** BIM_PLAYBOOK.md §6 "Lifecycle" heading at L77 — matches the brief.
- **Proposed §C rows:** BIM_PLAYBOOK.md, L77 §6 intro sentence: "X governs Y." [INTAKE-VERBATIM, brief L45] — v1.0 → 1.1 — [FC-XYZ] — not structural — minimal form: one sentence replaces one sentence.
- **CONFLICT / open questions:** none.
- **Dependencies:** none.
```

## 6. Hard prohibitions

1. Write ONLY `_AUDIT/SYNC_2026-10-15_doctrine-part2/scratchpad/map_parts/PART_0N.md` (your number). 2. No edits to any other file, no `git` write commands, no deletions, no scratch files elsewhere. 3. Never re-argue, reword, or re-scope a correction (D17); a contradiction between the brief and live reality is a CONFLICT → report, do not resolve. 4. NO-CHANGE is only ever a proposal. 5. Open decisions stay OPEN — you draft recommended wording and mark it CONDITIONAL; you never approve or defer anything. 6. Do not invent placements, filenames, or section numbers; NOT FOUND is reported as NOT FOUND (D13). 7. Do not modify, "fix", or reformat the drafts, the intake, or any canonical doc — even a typo. 8. If you cannot verify something, record GAP with where you looked.