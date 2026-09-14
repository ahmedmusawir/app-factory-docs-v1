# UPDATE MAP — test-a-tiny — 2026-09-14

> **The approved execution source of truth for this synchronization run** (supersedes RIPPLE_MAP since skill v0.6). Authored by Claudy (Engineer seat). Approved by Tony at Gate 2. Consumed by Sol (spec derivation), Cody (verification), and Claudy (execution, EXACTLY as approved). This file — not memory, not the branch — is what execution follows and what QA measures against. Lives at `_AUDIT/SYNC_2026-09-14_test-a-tiny/UPDATE_MAP.md`.
>
> Evidence labels on every non-trivial cell: EVIDENCE (path:line / SHA / command output) · INFERENCE (from what) · CLAIM (package / Operator says) · GAP (looked where) · QUESTION (needs Tony).
>
> **VALIDATION CONTEXT:** produced during TEST A (independent validation of skill v0.6-DRAFT) on disposable branch `test/docset-sync-v06-tiny-001`. Cargo is synthetic. Run stops at Gate 2 — Phase 4 is NOT executed in this test.

## 0. Run header

| Field | Value |
|---|---|
| Run ID | `SYNC_2026-09-14_test-a-tiny` |
| Branch | `docs/sync-test-a-tiny-2026-09-14` (NOT created — test stops at Gate 2) |
| BASE_SHA | pending (P4 branch creation). Discovery reference: origin/main = `0a787cb` [EVIDENCE: `git log --oneline -1 origin/main`]; session HEAD = `a311924040026f5cd7b4c35017c2283e30f09eda` on the test branch |
| Execution route | Local git at Hub clone (standing ruling 2026-08-05) [EVIDENCE: `git remote -v` → ahmedmusawir/app-factory-docs-v1] |
| **Path** | **TINY** — evidence in §P |
| QA arrangement | TINY: "Docs-only QA waiver per SOFTWARE_FACTORY_PLAYBOOK §2.5 item 6 — Operator, <date/time>." (PROPOSED — awaiting Gate 2) |
| Status | DRAFT |
| Lint baseline (pre-existing) | 9 findings: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:258/261/688/690/692 [VERSIONED-REFS]`, `04_REFERENCE_MANUALS/DATABASE_MANUAL.md:8/156 [VERSIONED-REFS]`, `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2092 [VERSIONED-REFS]`, `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:1 [HEADER-PRESENCE]` [EVIDENCE: `py lints/run_all.py` 2026-09-14 21:1x, exit 1; ENCODING PASS, RETIRED-TERMS PASS over 33 live files] |
| Live-doc count on disk / MANIFEST rows / MANIFEST stated | 31 / 31 / **29** [EVIDENCE: `ls 0?_*/*.md \| wc -l` = 31; MANIFEST §"The 29 Live Docs" row count = 31, `comm` disk vs rows = no difference; MANIFEST.md:6, :12, :76 say 29; MANIFEST.md:114 says "27 bodies"] — PRE-EXISTING drift (AP-12) |

## A. Intake ledger

| ID | Class (INTAKE_TAXONOMY #) | Source (file / package path) | Gist (one line) | Disposition | Gate state |
|---|---|---|---|---|---|
| IN-2026-09-14-01 | 2 — DOCTRINE JOURNAL / LESSON | `_INBOX/TEST_A_TINY_LESSONS.md` Entry 1 | Add note "TEST-A-SYNTHETIC-01 — Tiny-path routing validation only." under an existing non-authority informational/history section of UI_UX_BUILDING_MANUAL | CHANGE | Gate 1 APPROVED 21:20 |
| IN-2026-09-14-02 | 2 — DOCTRINE JOURNAL / LESSON | `_INBOX/TEST_A_TINY_LESSONS.md` Entry 2 | Add note "TEST-A-SYNTHETIC-02 — Propagation-map validation only." in the same doc, same kind of section | CHANGE | Gate 1 APPROVED 21:20 |

Class evidence: filename contains `LESSONS`; entries carry `Status: FLAGGED`, a target doc, required wording, and preservation lines (taxonomy class 2 recognition). Target has a Hub counterpart by canonical name: `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (header v1.4). Both entries are **intent-level placement + edit-level wording**: wording lands exactly; placement is proposed here. The file's "Synthetic validation cargo. Not real Factory doctrine." line is read as describing content, not as a request to stay out of the doc [INFERENCE; classification approved at Gate 1].

## B. Per-ID sections

### IN-2026-09-14-01 — TEST-A-SYNTHETIC-01 note

- **Approved intent** (verbatim): "Add one harmless synthetic validation note beneath an EXISTING appropriate non-authority informational/history section in the target document." [CLAIM: `_INBOX/TEST_A_TINY_LESSONS.md` Entry 1]
- **Required wording** (verbatim): "TEST-A-SYNTHETIC-01 — Tiny-path routing validation only."
- **Must-become-true invariants:** none stated beyond the intent. Derived from intent: the exact wording is present once in the target doc, inside a non-authority informational/history section [INFERENCE from intent text].
- **Preservation constraints** (verbatim; mirrored in §L): 1. "All existing doctrine behavior and wording." 2. "Do not delete or rewrite existing rules."
- **Likely affected files:** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (named TARGET). MANIFEST ← row: UI_UX_BUILDING_MANUAL ← FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL = 4 [EVIDENCE: MANIFEST.md:98].
- **Propagation search:** shared with IN-2026-09-14-02 — see "Shared propagation search" below.
- **Touch-list rows implementing this ID:** §C #1.
- **NO-CHANGE proposal:** none — wording absent from live scope (0 hits).
- **CONFLICT / open questions:** none for the note itself. §K-1 concerns infra derived fields (§G), not this ID's intent.

### IN-2026-09-14-02 — TEST-A-SYNTHETIC-02 note

- **Approved intent** (verbatim): "Add a second harmless synthetic validation note in the SAME target document, using an existing appropriate non-authority informational/history section." [CLAIM: `_INBOX/TEST_A_TINY_LESSONS.md` Entry 2]
- **Required wording** (verbatim): "TEST-A-SYNTHETIC-02 — Propagation-map validation only."
- **Must-become-true invariants:** none stated. Derived: exact wording present once in the SAME doc as IN-…-01, in a non-authority informational/history section [INFERENCE].
- **Preservation constraints** (verbatim): 1. "All existing doctrine behavior and wording." 2. "Do not delete or rewrite existing rules."
- **Likely affected files:** same as IN-2026-09-14-01.
- **Relationship to IN-…-01:** co-located by the intake's own instruction ("SAME target document"). Not a cross-correction dependency: neither note's truth depends on or alters the other's; both are additive, no shared passage is rewritten [INFERENCE from intent text].
- **Touch-list rows implementing this ID:** §C #1.
- **NO-CHANGE proposal:** none. **CONFLICT:** none.

### Shared propagation search (D19) — both IDs

Neither entry changes a governing rule; the search is still mandatory for class 2 (INTAKE_TAXONOMY "What the taxonomy is NOT"). It proves (a) the new wording does not already exist or collide, (b) no live document cites the placement sections in a way the insertion would break, (c) every live reference to the target doc stays true after the change.

- **Terms:**
  1. `TEST-A-SYNTHETIC` (new wording ID prefix)
  2. `Tiny-path routing validation` (new wording, entry 1)
  3. `Propagation-map validation` (new wording, entry 2)
  4. `synthetic validation` (intent phrase)
  5. `Run 001 Lessons That Updated This Manual` (cited section title — proposed placement anchor)
  6. `Manual Maintenance Discipline` (adjacent section title — rejected placement candidate)
  7. `Update Discipline` (adjacent subsection title — governs where evolution notes go)
  8. `UI_UX_BUILDING_MANUAL|UI-UX-BUILDING-MANUAL|UI/UX Building Manual` (target filename, hyphen variant, title)
- **Scope:** `01_CONSTITUTION 02_PIPELINE_AGENTS 03_BUILD_METHODOLOGY 04_REFERENCE_MANUALS 05_DESIGN_SYSTEM MANIFEST.md CHANGELOG.md` (+ `_SKILLS/`, `_OTHERS/` read-only for awareness)
- **Command shape:** `grep -rn -i -E "<term>" 01_CONSTITUTION 02_PIPELINE_AGENTS 03_BUILD_METHODOLOGY 04_REFERENCE_MANUALS 05_DESIGN_SYSTEM MANIFEST.md CHANGELOG.md`
- **Hit count per term:** T1 0 · T2 0 · T3 0 · T4 0 · T5 1 · T6 1 · T7 4 · T8 41 → **47 hit lines** (46 active / 1 history). No line appears under two terms except none (T5–T7 and T8 sets are disjoint).

| # | Path:line | Hit (quoted, abridged) | Disposition | Drives | Label |
|---|---|---|---|---|---|
| 1 | 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2070 | `## Appendix — Run 001 Lessons That Updated This Manual` | CONSISTENT — placement anchor; heading itself unchanged | §C #1 placement | EVIDENCE |
| 2 | 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2098 | `## Manual Maintenance Discipline` | CONSISTENT — unchanged; rejected as placement (normative: "Updates happen at three triggers") | — | EVIDENCE |
| 3 | 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2106 | `### Update Discipline` | CONSISTENT — L2108 "AT THE END (like this appendix) for evolution notes" supports the appendix placement; unchanged | §F #1 | EVIDENCE |
| 4 | 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2119 | `\| 1.4 \| 2026-07-08 \| **Wave 5 micro (audit sync).** … D-018 Update Discipline appendix untouched.` | HISTORY — under `## Version History` | — | EVIDENCE |
| 5 | 01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:674 | `### Update Discipline` | CONSISTENT — homonym section in a different doc; not about this manual | — | EVIDENCE |
| 6 | 02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:230 | `12. **Disaster Recovery** — RECOVERY.md format and update discipline` | CONSISTENT — unrelated homonym | — | EVIDENCE |
| 7 | 01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:74 | `• UI-UX-BUILDING-MANUAL.md` (diagram) | CONSISTENT — name reference; filename/sections unaffected | — | EVIDENCE |
| 8 | 01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:113 | `` `UI-UX-BUILDING-MANUAL.md` \| Cyberize screenshots… `` | CONSISTENT — name reference | — | EVIDENCE |
| 9 | 01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:713 | `**Reference:** `UI-UX-BUILDING-MANUAL.md`` | CONSISTENT — name reference | — | EVIDENCE |
| 10 | 01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:1012 | `\| **UI-UX-BUILDING-MANUAL.md** \| Building pages, components, layouts, styling \|` | CONSISTENT — manual roster summary still true | §F #2 | EVIDENCE |
| 11 | 01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:261 | ``4. Check `agent_docs/APP_FACTORY/UI-UX-BUILDING-MANUAL_v1_3.md` `` | OUT-OF-SCOPE — pre-existing baseline lint finding [VERSIONED-REFS]; stale path/version; not touched by this run (D9) | §M baseline | EVIDENCE |
| 12 | 01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:690 | ``- **`agent_docs/APP_FACTORY/UI-UX-BUILDING-MANUAL_v1_3.md`** — full UI patterns, Rule Zero`` | OUT-OF-SCOPE — pre-existing baseline lint finding; not touched (D9, D14 ←12 doc) | §M baseline | EVIDENCE |
| 13 | 03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1396 | `Source of truth: root CLAUDE.md forbidden zone + UI-UX-BUILDING-MANUAL Rule Zero` | CONSISTENT — Rule Zero unchanged | — | EVIDENCE |
| 14 | 03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:4 | `**Pairs with:** … UI-UX-BUILDING-MANUAL …` | CONSISTENT — header declaration; ← unchanged (known hyphen variant, MANIFEST.md:49 footnote) | §G ← map | EVIDENCE |
| 15 | 03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:54 | `2. **UI-UX-BUILDING-MANUAL Rule Zero** — operating standard` | CONSISTENT — Rule Zero unchanged | §F #3 | EVIDENCE |
| 16 | 03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:66 | `- ✅ UI-UX-BUILDING-MANUAL Rule Zero re-read` (checklist) | CONSISTENT — checklist item still true | §F #3 | EVIDENCE |
| 17 | 03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:184 | `2. **What does UI-UX-BUILDING-MANUAL say about this pattern?** (Cite section)` | CONSISTENT — generic pre-write check | §F #3 | EVIDENCE |
| 18 | 03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:199 | `2. Manual reference: UI-UX-BUILDING-MANUAL Rule Zero + Layouts section.` (template) | CONSISTENT — Rule Zero + Layout sections unchanged | §F #3 | EVIDENCE |
| 19 | 03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md:384 | `2. **What does the UI-UX-BUILDING-MANUAL say about this pattern?** (Cite section)` | CONSISTENT — generic | §F #4 | EVIDENCE |
| 20 | 03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md:399 | `2. Manual reference: UI-UX-BUILDING-MANUAL Rule Zero + Layouts section.` | CONSISTENT | §F #4 | EVIDENCE |
| 21 | 05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:4 | `**Pairs with:** STARTER_KIT_HANDBOOK, UI_UX_BUILDING_MANUAL, …` | CONSISTENT — header declaration | §G ← map | EVIDENCE |
| 22 | 05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:778 | ``- **`agent_docs/APP_FACTORY/UI-UX-BUILDING-MANUAL.md`** — full UI patterns deep-dive`` | CONSISTENT for this run (description still true). NOTE: pre-existing stale kit path (not a lint finding) — follow-up awareness only, not touched | §F #5 | EVIDENCE |
| 23 | 05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md:4 | `**Pairs with:** … UI_UX_BUILDING_MANUAL, COMPONENT_REGISTRY` | CONSISTENT — header declaration | §G ← map | EVIDENCE |
| 24 | 05_DESIGN_SYSTEM/THEMING_MANUAL.md:4 | `**Pairs with:** … UI_UX_BUILDING_MANUAL, APP_ARCHITECTURE_MANUAL` | CONSISTENT — header declaration | §G ← map | EVIDENCE |
| 25 | 05_DESIGN_SYSTEM/THEMING_MANUAL.md:8 | `**Parent doctrine:** UI-UX-BUILDING-MANUAL (Rule Zero — mobile-first)` | CONSISTENT | — | EVIDENCE |
| 26 | 05_DESIGN_SYSTEM/THEMING_MANUAL.md:16 | `- **UI-UX-BUILDING-MANUAL** — mentions theming briefly, points here for depth` | CONSISTENT | — | EVIDENCE |
| 27 | 05_DESIGN_SYSTEM/THEMING_MANUAL.md:222 | `- **Typography scale** — see UI-UX-BUILDING-MANUAL §Typography` | CONSISTENT for this run (not affected). NOTE: PRE-EXISTING dangling section citation — target has no `Typography` heading [EVIDENCE: `grep -n -i typography` target → only L913, L992, L1856, none a heading]. Follow-up awareness, not touched | §F #6 | EVIDENCE |
| 28 | 05_DESIGN_SYSTEM/THEMING_MANUAL.md:225 | `- **Mobile-first responsive behavior** — see UI-UX-BUILDING-MANUAL Rule Zero` | CONSISTENT | — | EVIDENCE |
| 29 | 05_DESIGN_SYSTEM/THEMING_MANUAL.md:268 | `- **UI-UX-BUILDING-MANUAL** §Theming and Design Tokens — the operating doctrine that points here` | CONSISTENT for this run. NOTE: PRE-EXISTING dangling section citation — target has `### 10.2 Design Tokens` (L1600), no "Theming and Design Tokens" heading. Follow-up awareness, not touched | §F #6 | EVIDENCE |
| 30 | 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1 | `# UI/UX BUILDING MANUAL` | CONSISTENT — title unchanged | — | EVIDENCE |
| 31 | MANIFEST.md:41 | FRONTEND_BUILD_PHASE_PLAYBOOK row, Pairs-with `… UI_UX_BUILDING_MANUAL² …` | CONSISTENT — not this doc's row | — | EVIDENCE |
| 32 | MANIFEST.md:49 | `² *Header carries the hyphen variant UI-UX-BUILDING-MANUAL — normalized here…*` | CONSISTENT | — | EVIDENCE |
| 33 | MANIFEST.md:67 | COMPONENT_REGISTRY row (Pairs-with mentions target) | CONSISTENT | — | EVIDENCE |
| 34 | MANIFEST.md:68 | GLOBAL_DESIGN_SYSTEM_HANDBOOK row | CONSISTENT | — | EVIDENCE |
| 35 | MANIFEST.md:70 | THEMING_MANUAL row | CONSISTENT | — | EVIDENCE |
| 36 | MANIFEST.md:72 | `\| UI_UX_BUILDING_MANUAL \| 1.4 \| 2026-07-08 \| Active \| …` | **CHANGE** — Version/Date updated FROM the bumped header (D7 step 3) | §G row 1 | EVIDENCE |
| 37 | MANIFEST.md:80 | ← row STARTER_KIT_HANDBOOK (lists target) | CONSISTENT — target's Pairs-with unchanged → no ← recompute effect | §G ← map | EVIDENCE |
| 38 | MANIFEST.md:87 | ← row GLOBAL_DESIGN_SYSTEM_HANDBOOK | CONSISTENT (same reason) | §G | EVIDENCE |
| 39 | MANIFEST.md:90 | ← row COMPONENT_REGISTRY | CONSISTENT | §G | EVIDENCE |
| 40 | MANIFEST.md:91 | ← row THEMING_MANUAL | CONSISTENT | §G | EVIDENCE |
| 41 | MANIFEST.md:95 | ← row FRONTEND_BUILD_PHASE_PLAYBOOK | CONSISTENT | §G | EVIDENCE |
| 42 | MANIFEST.md:98 | `\| UI_UX_BUILDING_MANUAL \| FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL \| 4 \|` | CONSISTENT — recomputed from headers (hits #14, #21, #23, #24) = 4 | §G | EVIDENCE |
| 43 | MANIFEST.md:125 | appendix row FFM_PLAYBOOK (mentions target) | CONSISTENT for this run; appendix scope → §K-1 | §G / §K-1 | EVIDENCE |
| 44 | MANIFEST.md:127 | appendix row FRONTEND_FIRST_PLAYBOOK | CONSISTENT; appendix scope → §K-1 | §K-1 | EVIDENCE |
| 45 | MANIFEST.md:129 | appendix row SOFTWARE_FACTORY_PLAYBOOK | CONSISTENT; appendix scope → §K-1 | §K-1 | EVIDENCE |
| 46 | MANIFEST.md:130 | appendix row STARTER_KIT_HANDBOOK | CONSISTENT; appendix scope → §K-1 | §K-1 | EVIDENCE |
| 47 | MANIFEST.md:133 | `\| UI_UX_BUILDING_MANUAL \| APP_ARCHITECTURE_MANUAL, HANDOFF_PACKAGE_PLAYBOOK \|` | CONSISTENT — the new notes add no canonical-name mentions | §K-1 | EVIDENCE |

**Undispositioned hits: 0.** CHANGELOG.md: 0 hits for all terms.

**Awareness scope (read-only):**
- `_SKILLS/` excluding this family: 0 hits. `_SKILLS/factory-docs-update/sync-engineer/SKILL.md:158` — worked-example prose naming the doc in a lint baseline → §I CONSISTENT.
- `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md:33,34`, `_OTHERS/MASTER_DOC_LIST_v1_0_FINAL.md:62,79` — non-canonical design notes citing hyphen/versioned names → OUT-OF-SCOPE (non-canonical; no action).

## C. Touch list (execute lightest ← first, heaviest last)

| # | Canonical doc (path) | ← count (MANIFEST) | Placement — VERIFIED against live structure | Proposed wording / exact edit intent | Contributing IDs | Version: live → new | Archive expected | Structural? | Minimal-form note (D14) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` | 4 [EVIDENCE MANIFEST.md:98] | **Inside `## Appendix — Run 001 Lessons That Updated This Manual` (L2070), as its final subsection: insert after L2094 (last line of `### Lesson 9`, "Pattern to watch for…") and before the `---` at L2096 that closes the appendix.** Verified at session HEAD a311924 (target, MANIFEST, CHANGELOG identical on origin/main [EVIDENCE: `git diff --stat origin/main HEAD -- 05_DESIGN_SYSTEM MANIFEST.md CHANGELOG.md` empty; the 2 test-branch commits touch only `_SKILLS/` (22 files) and `fable-sync-review/` (3 files)]). Why this section: it is the only non-authority history/informational section in the doc; `## Manual Maintenance Discipline` (L2098) is normative; `## Version History` (L2115) is reserved for the version row (D7). The doc's own `### Update Discipline` L2108 places evolution notes "AT THE END (like this appendix)". **Placement caveat (D13, flagged for approval):** the appendix title says "Run 001 Lessons" and already hosts a Run 002 lesson; the synthetic notes are not run lessons. Nearest real anchor; no better one exists. | Insert exactly (blank line, separator, blank line, then):<br><br>`---`<br><br>`### Synthetic Validation Notes (TEST A, 2026-09-14)`<br><br>`TEST-A-SYNTHETIC-01 — Tiny-path routing validation only.`<br><br>`TEST-A-SYNTHETIC-02 — Propagation-map validation only.`<br><br>The two note lines are the cargo's required wording VERBATIM (em-dash preserved as in cargo). The `---` separator mirrors the doc's own separator between Lesson 5 and Lesson 9 (L2084). The `###` heading is a Claudy-authored wrapper (NOT cargo wording) — flagged translation (D15) so the notes do not read as part of Lesson 9; Tony may strike it. No existing line is edited, moved, or reflowed. **Header:** L3 → `> **Version:** 1.5 · **Date:** <P4 execution date> · **Status:** Active`. **Version History:** new row ABOVE the 1.4 row (the table is newest-first, L2119–2123): `\| 1.5 \| <P4 date> \| Synthetic validation notes TEST-A-SYNTHETIC-01/02 appended to the Run-lessons appendix (TEST A — docs-sync skill v0.6 validation cargo; no doctrine change) [IN-2026-09-14-01, IN-2026-09-14-02]. \|` | IN-2026-09-14-01, IN-2026-09-14-02 | 1.4 → **1.5** [INFERENCE: the doc's own history increments by 0.1 (1.1→1.2→1.3→1.4); skill does not fix bump magnitude — approve or name another] | YES → `_ARCHIVE/UI_UX_BUILDING_MANUAL_v1_4.md` (no existing UI_UX archive in `_ARCHIVE/` [EVIDENCE: `ls _ARCHIVE`]; suffix format per `AUTH_MANUAL_v1_3.md` precedent) | NO | Additive only: ~7 inserted lines + 1 header line changed + 1 VH row. Pre-existing lint finding at L2092 (inside Lesson 9, 2 lines above the insertion) is NOT touched (D9). |

## D. New canonical files

None.

## E. Stale / superseded material

None.

## F. Dependents checked, unchanged

| # | Doc / location | Kind | Why checked | Verdict |
|---|---|---|---|---|
| 1 | 05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2106–2111 | role instruction (maintenance rules) | placement governance (T7) | CONSISTENT: "Patches go … AT THE END (like this appendix) for evolution notes"; "Bump the version number at the top when applying patches" — honored by §C #1 |
| 2 | 01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:1012 | summary (manual roster) | T8 | CONSISTENT: "Building pages, components, layouts, styling" |
| 3 | 03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:54, 66, 184, 199 | checklist / pre-write template | T8 | CONSISTENT: cite Rule Zero + Layouts — both unchanged |
| 4 | 03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md:384, 399 | pre-write template | T8 | CONSISTENT (same) |
| 5 | 05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:778 | quick reference | T8 | CONSISTENT for this run; pre-existing stale kit path noted (§K none; follow-up awareness) |
| 6 | 05_DESIGN_SYSTEM/THEMING_MANUAL.md:222, 268 | cross-reference | T8 | CONSISTENT for this run; PRE-EXISTING dangling section cites (`§Typography`, `§Theming and Design Tokens`) — follow-up awareness, not in scope, not touched |

## G. Infra and index effects

| Item | Expected change | Check at Gate 4 / AC-I |
|---|---|---|
| MANIFEST rows | Row L72 UI_UX_BUILDING_MANUAL: `1.4 \| 2026-07-08` → `1.5 \| <P4 date>` FROM the bumped header; MANIFEST header L3 Date → `<P4 date>`, Version stays 1.0; NOT archived (Ruling 7) | header vs row equality |
| MANIFEST live-doc count | **Recompute from disk: 31.** D7 mandates derived-field recompute every run. Current text says 29 at MANIFEST.md:6 ("all 29 live doctrine docs"), :12 ("## The 29 Live Docs"), :76 ("inverting the 29 Pairs-With → lists") → change each "29" → "31". **This corrects PRE-EXISTING drift (AP-12) because the skill's D7 requires it — not a "while I'm in here" fix. Flagged for explicit approval.** | count 31 = disk 31 = rows 31 |
| MANIFEST ← dependency map | No Pairs-with change in this run → no row changes. Target ← = 4 re-verified from headers (§B #42) | spot-check UI_UX row |
| MANIFEST appendix scope note (L114) | "scanning all 27 bodies … (41 total)" is stale (31 docs exist). Resolution → **§K-1** (QUESTION) | per ruling |
| CHANGELOG | Append ONE row under `## Ongoing entries`, format per CHANGELOG.md:22: `\| <P4 date> \| UI_UX_BUILDING_MANUAL v1.5 \| TEST A synthetic validation notes TEST-A-SYNTHETIC-01/02 appended to the Run-lessons appendix (skill v0.6 validation cargo; no doctrine change) \| IN-2026-09-14-01, IN-2026-09-14-02 \|`; CHANGELOG header L3 Date → `<P4 date>`; NOT archived | 1 row = 1 bumped doc; IDs present |
| README / index files | none (`_ARCHIVE/README.md` unchanged — adding a file needs no README edit [INFERENCE; to be checked at P4]) | — |

## H. Paths, links, assets

| Reference | In doc | Resolves at BASE? | Resolves after? | Asset | IDs |
|---|---|---|---|---|---|
| none added | — | — | — | none | — |

The inserted text contains no filenames, paths, section citations, or images.

## I. Skill references (read-only awareness)

| Skill file | What it cites | Disposition |
|---|---|---|
| `_SKILLS/factory-docs-update/sync-engineer/SKILL.md:158` | UI_UX_BUILDING_MANUAL named in worked-example lint baseline prose | CONSISTENT — illustrative, unaffected |

## J. Parked cross-boundary / cross-repo items

None.

## K. Unresolved Operator decisions (BLOCKED)

| ID | Question (exact) | Evidence | What it blocks | Ruling (filled by Tony) |
|---|---|---|---|---|
| K-1 | D7 requires MANIFEST's "undeclared-dependencies appendix scope note" to be current every run. The note (MANIFEST.md:114) says the appendix was built by "scanning all 27 bodies … (41 total)", but 31 docs now exist and nobody rescanned. Which do you want: **(a)** amend only the note to state its true basis — e.g. "Found by scanning the 27 bodies live at 2026-07-12 … (41 total); not recomputed for docs added since" — (1 line, keeps TINY minimal); or **(b)** rescan all 31 bodies and regenerate the appendix table (larger infra diff; still docs-only)? **Engineer recommendation: (a).** | MANIFEST.md:114; disk count 31; appendix rows L116–133 | §G appendix row only; the two notes do not depend on it | |

No other open items.

## L. Preservation constraints (all IDs, consolidated)

| Constraint (verbatim) | Source ID | Where it lives (path:line at BASE) | How QA will check (AC-P) |
|---|---|---|---|
| "All existing doctrine behavior and wording." | IN-2026-09-14-01, IN-2026-09-14-02 | Whole doc `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (L1–2127) — esp. Rule Zero L11–82, Rule Zero-B L84–136, appendix L2070–2094, Maintenance Discipline L2098–2111 | `git diff <base>..<cand> -- <path>` shows only: header L3 version/date, added lines after L2094, one added VH row; zero `-` lines other than L3 |
| "Do not delete or rewrite existing rules." | IN-2026-09-14-01, IN-2026-09-14-02 | same | same diff: no removed/modified content lines except the header line |

## M. Expected validation

- Lints: 4 lints; expected on candidate: zero new findings; baseline 9 unchanged — `STARTER_KIT_HANDBOOK.md:258,261,688,690,692 [VERSIONED-REFS]`, `DATABASE_MANUAL.md:8,156 [VERSIONED-REFS]`, `UI_UX_BUILDING_MANUAL.md:2092 [VERSIONED-REFS]` (line number stays 2092 — insertion is below it), `STARTER_KIT_HANDBOOK.md:1 [HEADER-PRESENCE]`.
- Propagation searches to re-run at the candidate (verbatim from §B): T1–T8 with the command shape above. Expected: T1 `TEST-A-SYNTHETIC` = **4 hits** (note-01 and note-02 lines = 2 active; UI_UX Version History row + CHANGELOG row = 2 HISTORY); T2 = 1 active; T3 = 1 active; T4 `synthetic validation` (case-insensitive) = **3 hits** (the `### Synthetic Validation Notes` heading = 1 active; VH row + CHANGELOG row = 2 HISTORY); T5–T8 hit sets as §B, with MANIFEST.md:72 showing 1.5 and the UI_UX line numbers below L2094 shifted by the insertion.
- Canonical term list / retired-term list (AC-N): no terminology change; lint retired-term list only.
- Derived-field assertions: MANIFEST count 31 (L6, L12, L76), rows 31, disk 31; ← map unchanged; appendix note per K-1 ruling.
- Archive fidelity: 1 archive — `git show <BASE_SHA>:05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md | diff - _ARCHIVE/UI_UX_BUILDING_MANUAL_v1_4.md` empty.
- References/assets to resolve: none.

## N. Write-load tally and commit plan

- Docs edited 1 + archives 1 + new docs 0 + MANIFEST + CHANGELOG (+ assets 0) = ~4 writes
- Commits, in order: `docs(UI_UX_BUILDING_MANUAL): v1.5 - TEST A synthetic validation notes [IN-2026-09-14-01, IN-2026-09-14-02]` (carries archive, MANIFEST row + derived fields, CHANGELOG row); then `chore(sync): run metadata [SYNC_2026-09-14_test-a-tiny]`
- Hygiene: plain hyphens in commit messages; no Co-Authored-By; one version bump per doc per run (D22)
- **NOT executed in TEST A** (stops at Gate 2).

## O. Approval and amendments

- [x] Gate 1 — scope + classification APPROVED by Operator at 2026-09-14 21:20 ("APPROVED")
- [ ] Gate 2 — this map APPROVED by Operator at `<date/time>` (route TINY confirmed; NO-CHANGE rows approved: none; TINY waiver line: "Docs-only QA waiver per SOFTWARE_FACTORY_PLAYBOOK §2.5 item 6 — Operator, <date/time>."; K-1 ruling: `<a/b>`; LARGE → TINY downgrade ruling: N/A)
- [ ] Gate 3 — N/A (TINY, waiver)
- Amendments: none
- Overrides logged: none
- CONTENT_SHA: pending (P4 not executed in TEST A) · Gate 4: pending · pushed: no

## P. Route evidence (TINY / LARGE decision record)

| Fast-path condition (route-selection.md) | Evidence | Holds? |
|---|---|---|
| A1 ≤ 3 intake IDs | §A: 2 IDs (IN-2026-09-14-01, -02) | YES |
| A2 ≤ 3 canonical touch-list docs (after §B search) | §C: 1 doc; §B 47 hits → 1 CHANGE hit (MANIFEST.md:72, infra, not canonical) | YES |
| A3 no new canonical document | §D empty | YES |
| A4 no Factory-wide terminology rename / change | Notes introduce no role/gate/module/lifecycle/artifact names; T1–T4 absent from corpus; no retired term | YES |
| A5 no cross-correction dependency | Both notes additive, independent passages; "SAME document" is co-location, not invariant dependency (§B IN-…-02) | YES |
| A6 no high-risk governing-rule change | Target is a Tier-5 UI/UX design manual; insertion is in a history appendix; no auth / RBAC / tenant / PHI / payments / subscriptions / QA verdict / git-merge / role-authority content | YES |
| A7 no unresolved conflict (§K empty or ruled) | §K has K-1 — an infra-note QUESTION, not a doctrine conflict; condition satisfied once Tony rules at Gate 2 (either option stays docs-only) | YES on ruling |
| A8 no cross-boundary change required (§J blocking = none) | §J empty; `_SKILLS/`, `lints/`, `.github/` untouched | YES |
| A9 propagation search bounded and complete before Gate 2 | 8 terms × full live scope; 47 hits, 47 dispositioned, 0 undispositioned; small enough to present aloud | YES |
| A10 docs-only QA waiver eligible | Changes confined to one live-scope .md + MANIFEST + CHANGELOG + one `_ARCHIVE/` addition; no assets, lints, CI, skills; Tony has not disallowed waivers | YES |
| **Route** | TINY only if ALL hold; else LARGE | **TINY** — provisional route (Gate 1) unchanged. Operator escalation / downgrade ruling: none |

**Pre-existing discrepancies observed and deliberately NOT repaired** (none change the route): lint baseline 9 findings; RECOVERY.md stale (2026-08-10, "29 live docs", pending housekeeping merge); THEMING_MANUAL.md:222/268 dangling section cites into the target; COMPONENT_REGISTRY.md:778 and STARTER_KIT_HANDBOOK.md:261/690 stale `agent_docs/APP_FACTORY/` kit paths; STARTER_KIT_HANDBOOK missing standard header. The MANIFEST count "29" is the one pre-existing drift the run WOULD correct — because D7 mandates derived-field recompute, not by Engineer choice (§G).
