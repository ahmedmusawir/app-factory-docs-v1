# AMENDED-v1 — ownership amendment to the Gate 2-approved map (D-1 / D-2 / OBS-1 / propagation sweep)

> **Status:** ENGINEER-PROPOSED · prepared 2026-10-17 by Cody (Engineer) in two passes (13:50 D-1/D-2; 14:56 OBS-1 fold + sweep) · **re-enters Gate 2** (map §O freeze rule) · **not approved** · Gate 3 pending · Phase 3 **NOT RELEASED**
> **Authority to prepare:** Tony (Director), 2026-10-17, "CODY — PREPARE ONE BOUNDED MAP AMENDMENT" (D-1/D-2, Architect text verbatim) and "CODY — COMPLETE THE OWNERSHIP CORRECTION IN ONE PASS" (Jarvis resolves OBS-1 into this same draft; one propagation sweep; no AMENDED-v2).
> **Resolves:** `FABLE_CORRECTION_CONFIRMATION_2026-10-17.md` §5 D-1 and D-2 (spec v1.0 AC6(c)/(d) FAIL on the approved tree); OBS-1 (Cody 13:50, Jarvis-resolved); four further direct contradictions found by the sweep (P-1…P-4).
> **Policy:** applies the existing approved rule only — RUL-09 (Architect owns DATA_CONTRACT before Design; FILE_TREE optional) as restated by the Architect: **"The Architect owns the approved contract; Engineering implements it."** No new policy is proposed. The approved ownership policy is not reopened.

## 1. What this amendment is, and is not

- Eight exact ENGINEER-PROPOSED spans, E373–E380, appended after the frozen 372 ordered edits, on three already-revised documents (Blueprint, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK). No other proposed byte changes.
- The Gate 2-approved records (`UPDATE_MAP.md` SHA-256 `cd291270…6931`, `EXECUTION_PROPOSAL_INDEX.json` SHA-256 `84337dcd…da39`, `SELECTED_EXACT_EDITS.json`, `PROPOSED_CONTENT/`) are **unchanged**. This directory holds the proposed successor records side by side; neither tree is implemented.
- Version numbers, header dates, Version History rows, MANIFEST cells, CHANGELOG rows, archives, templates, workflow documents, SVGs, closeout transitions and the landing-date spans are **unchanged** (verified in `VERIFICATION.json`).
- D-3 (five punctuation sites) stays outside this amendment. D-4 is recorded in §6 as an already-approved byte transformation; no new content change.
- The earlier two-span package (`FACTORY_AMENDED_V1_REVIEW_2026-10-17_135049.zip`, SHA-256 `4feb45de…`) is superseded by this draft; it is not a separate amendment.

## 2. Exact spans (verbatim; each `old` occurs exactly once at BASE, in the frozen proposed file and in the content-stage replay)

### E373 — D-1 — `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` (lines 140–142)

Old (complete span):

```
## 📋 ENGINEER AGENT: WHAT IT PRODUCES

The Engineer's full output list:
```

New:

```
## 📋 ENGINEERING PACKAGE: APPROVED CONTRACT ARTIFACTS

The Architect assembles the approved contract artifacts below for the Engineer to implement. DATA_CONTRACT is authored before Design; FILE_TREE is optional when implementation structure and boundaries are otherwise explicit.
```

IDs: D-1, MC-07, RUL-09, FC-008, FC-017, FC-027. Authority: Architect text via Tony's first brief. Container: H2 heading → lead paragraph → existing `### **DATA_CONTRACT.md**` H3.

### E374 — D-2 — `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` (line 746, inside the §12 canonical DATA_CONTRACT template fence)

Old: `> **Author:** Engineer Agent` → New: `> **Author:** Architect`. IDs: D-2, MC-07, RUL-09, FC-027. Authority: Architect text via Tony's first brief. Container: the single fenced template beginning `# DATA_CONTRACT: [Project Name]`, below the Architect-ownership note (E356).

### E375 / E376 — OBS-1 — `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` (lines 63 and 67, table "What the Architect Does NOT Do")

Old: `| Define data schemas | Engineer Agent |` → New: `| Implement approved data schemas as migrations and models | Engineer Agent |`
Old: `| Define API contracts | Engineer Agent |` → New: `| Implement approved API contracts | Engineer Agent |`

IDs: OBS-1, MC-07, RUL-09, FC-017, FC-027. Authority: **Jarvis's exact rows**, conveyed in Tony's second brief. Container: table rows under the H3 "What the Architect Does NOT Do" (markdown_it table token).

### E377 / E378 — P-1 / P-2 — `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` (lines 87 and 88, owner table under "Phase 3: ENGINEERING (Architect Contract Assembly)")

Old: ``| `DB_SCHEMA.md` | Database tables, relationships, indexes | Engineer |`` → New: ``| `DB_SCHEMA.md` | Database tables, relationships, indexes | Architect |``
Old: ``| `API_SPEC.md` | Endpoints, methods, auth, error codes | Engineer |`` → New: ``| `API_SPEC.md` | Endpoints, methods, auth, error codes | Architect |``

IDs: P-1/P-2, OBS-1, MC-07, RUL-09, FC-008, FC-017, FC-027. Evidence: the table heading already reads "Architect Contract Assembly", its DATA_CONTRACT row already reads "Architect", and E373 states the Architect assembles the approved contract artifacts (DATA_CONTRACT, DB_SCHEMA, API_SPEC, FILE_TREE). An Engineer owner cell for two contract artifacts is a direct contradiction of the rule. **Engineer-worded under the rule; wording for Architect/Fable confirmation.**

### E379 — P-3 — `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` (line 86, "Core Responsibilities" role table)

Old: `| **Data Contracts** | Define schemas, APIs, file formats |`
New: `| **Data Contracts** | Implement the approved schemas, APIs and file formats; contract changes return to the Architect |`

IDs: P-3, OBS-1, MC-07, RUL-09, FC-027. Evidence: the playbook's own role table assigned contract *definition* to the Engineer, contradicting its §"DATA_CONTRACT Ownership" block, the §12 note, E374 and OBS-1. The return clause mirrors the Blueprint FAQ row already approved at Gate 2 ("contract changes return to the Architect and Director"). **Engineer-worded; wording for Architect/Fable confirmation.**

### E380 — P-4 — `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` (line 998, §13 "Full-Stack Web App → Engineer Focus" bullet)

Old: `- Database schema design (Supabase/Firebase)` → New: `- Implement approved database schemas as migrations and models (Supabase/Firebase)`

IDs: P-4, OBS-1, MC-07, RUL-09, FC-027. Evidence: the bullet assigned schema *design* to the Engineer; reworded with Jarvis's OBS-1 phrase. Sibling bullets ("API route implementation"; Backend Bundle "API contract implementation") already state implementation and are retained.

Full records: `AMENDMENT_V1_EDITS.json` (the eight edits with authority and evidence), `SELECTED_EXACT_EDITS.json` (all 380, frozen 1–372 byte-identical).

## 3. Before / after identities

| Object | Gate 2 (frozen, approved) | AMENDED-v1 (proposed) |
|---|---|---|
| `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` — before (pinned main) | `9b732116c6030aee4d6ae0b792272bc372dd647ef95dea522c2bf7949934af93` | same |
| … proposed_sha256 / bytes | `de0321e3b2b9220121606c5255d2ddc3d0d01ce57d69be11200d0c2aed5a2ac4` / 14,426 | `df17ac849c4035a3febcc7042329a43bf9fb2ffbf2cafbc954a01a6d0d7f6911` / 14,636 |
| `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` — before (pinned main) | `b0754979e3b24cb79234265fe146f39f03718e608a60153a702a518f34979af4` | same |
| … proposed_sha256 / bytes | `ad0712bf79a03233c6dd4799eb04113ad966d23017f26a5ba1a6f433481dce48` / 26,430 | `3ec6bc37f52ad913e06ad43e7b7344477a5804c5b205122ca8b075502d01949c` / 26,479 |
| `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` — before (pinned main) | `8d73c37a42624fa2c60729d8d2648fc96f72305a732fd5e74460cf0a614f861c` | same |
| … proposed_sha256 / bytes | `72477ec8dccc0381d6a5a4476d64b84751b376dfb78f83a49b337beb8651a1e9` / 50,878 | `b0f74569d020176a189abc47fa1ea6f27644a81ceb55efc1ccd78e4d5197a5ab` / 50,972 |
| `EXECUTION_PROPOSAL_INDEX.json` | `84337dcd3b60d059e8c67d1586cd8dba58827c64e14ab46d6d05ab57a611da39` | `69244f4edc347b30b81ed6a909bae4fbb5130864319e9f8cd84b5d5c22e59ba6` |
| `SELECTED_EXACT_EDITS.json` | `4bd81b896edc1a47925861cd1136fe01b9231d9c2a3fdb1fee796c5eb5c2c928` (372) | `2675ffc148f49a95b688e9f252527950ce9c3f1fd61df3fb0ffb067fcc7ff687` (380) |
| Other regenerated records | see `AMENDMENT_IDENTITIES.json` → `regenerated_records` | |
| Unaffected records (transitions, templates, workflow plan, version plan, new-doc proposals, archive restoration, map, Gate 2 record, Fable's files) | see `AMENDMENT_IDENTITIES.json` → `unaffected_records_sha256` | identical |

The 98 other index entries keep their Gate 2 `proposed_sha256` and byte counts exactly. Outgoing archives of all three documents remain the BASE bytes. The 13:50 two-span identities (`5ac27e0d…`, `ef3826c9…`, index `c35406fe…`) are superseded and no longer appear in any record.

## 4. Counts (derived from the regenerated records, not assumed)

| Item | Gate 2 | AMENDED-v1 |
|---|---:|---:|
| Ordered content edits | 372 | **380** |
| Proposed paths | 101 | 101 (3 hashes changed, 98 identical) |
| Amended documents / new edits | — | 3 / 8 (D-1, D-2, OBS-1a, OBS-1b, P-1…P-4) |
| Revised existing tier documents | 31 | 31 |
| CHANGELOG rows (in-table) | 39 | 39 |
| MANIFEST tier rows | 34 | 34 |
| Landing-date spans | 151 | 151 (identical spans) |
| Conditional closeout spans / paths | 12 / 9 | 12 / 9 (unaffected) |
| Templates / archives / workflow md / SVG | 25 / 32 / 4 / 4 | unchanged |
| Certified findings | 97 (94 YES / 3 NO) | unchanged; FC-008, FC-017, FC-027 evidence columns gain the new edit IDs via `SCOPE_LEDGER_SUPPLEMENT.md` |
| Ownership sweep hits | — | 39 (8 RESOLVED, 31 RETAIN with rationale) |

## 5. Verification performed (Engineer evidence; `VERIFICATION.json` / `VERIFICATION_RAW.txt`, 2026-10-17T14:56:16.091465+06:00)

1. Frozen Gate 2 map, index, Fable's v1.0 spec and all 101 frozen `PROPOSED_CONTENT/` hashes unchanged; PRESERVATION_BASELINE and MC_CORRECTION_PROTECTED hold (the protected list pins Fable's DRAFT spec; her own v1.0 successor `3910a62c…` is the only accepted difference).
2. All eight spans are byte-exact to the briefs (D-1/D-2 Architect text; OBS-1 Jarvis rows) or recorded verbatim (P-1…P-4); each is unique at BASE / frozen / amended and sits in the intended container (table rows verified with markdown_it under the named headings; E380 by line structure because ENGINEER_PLAYBOOK's nested template fences invert markdown_it fence parity from §12 onward — pre-existing at BASE, fence count 82 unchanged).
3. Independent replay of all 380 edits over the pinned `9c17939` blobs; per document, the residual against the amended proposed bytes equals the frozen residual exactly (header bump + one history row for 30 documents; STARTER_KIT's approved D-4 residual).
4. Index: 101 paths, 98 hashes identical to Gate 2, three amended; every before-hash equals the pinned blob; canonical worktree unchanged; outgoing archives of the three documents still BASE bytes.
5. Header line, history row and MANIFEST cells unchanged for the three documents (Blueprint 2.2 / ARCHITECT 2.3 / ENGINEER 1.3, 2026-10-16, Active).
6. 151 landing-date spans identical and each occurs once in the amended tree; the 12 closeout transitions on 9 paths do not touch the amended documents and still apply.
7. RUL-09 traceability row gains E373–E380; 38 traceability rows; counts from data; 97 FC rows and the three NO guards intact.
8. Unchanged lint suite (`python3 -B -I lints/run_all.py`) PASS on an overlay copy; lint scripts byte-identical; no new unclosed fences in the three amended documents.
9. Ownership sweep: 39 hits, every one dispositioned; no retained live line still carries an amended old span.
10. Two consecutive generator runs produced byte-identical output (16 generated files) — deterministic.
11. Git: HEAD 626da8d, main = origin/main = 9c17939, nothing staged, empty canonical diff, no mutation.

## 6. D-4 — STARTER_KIT_HANDBOOK metadata normalization (recorded, not changed)

`D4_STARTER_KIT_METADATA_NORMALIZATION.json` records the exact residual that `cody_mc_metadata.py` (lines 26–28) applies to `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` beyond the ordered edits: the standard two-line header block inserted after the H1, the line `**Version:** v1.1 (Kit-Perfection campaign applied)` replaced by `**Kit campaign reference:** handbook v1.1 (historical reconciliation; verify current kit revision)`, and the single history row. Content-stage SHA `02289c07…`, approved proposed SHA `29ce1d9f…` (Gate 2 = AMENDED-v1). Already-approved byte transformation; AMENDED-v1 adds no content change to that document. Fable's spec AC2 already enumerates it.

## 7. Ownership propagation sweep (`OWNERSHIP_PROPAGATION.tsv`, 39 rows)

Scope: every live `.md`/`.svg` path in the proposed index except `_ARCHIVE/` — role tables, headings, copyable templates (`_templates/`), examples, boot prompts and checklists (`_workflows/`, FFM/QAM material) included. Pattern set: the D-1/D-2 spans, "Engineer Agent", trailing `| Engineer |` owner cells, "Define data schemas / API contracts / schemas", "schema design", "Engineer Focus", "Engineer owns/produces/authors", "owned by the Engineer", "Engineering owns", and "Engineer defines/designs/writes/creates … schema/contract". The generator fails closed: a hit without a curated disposition aborts the build.

| Group | Rows | Disposition |
|---|---:|---|
| Direct contradictions of the approved rule | 8 | **RESOLVED** E373–E380 (§2) |
| Amended Architect rows re-matched by "Engineer Agent" | 2 | RETAIN — implementation now assigned to the Engineer |
| Seat/subject naming (titles, headings, mission, agentic-conduct section, Phase 4 "Prompted By", Designer "Write the production app", SFP seat split, skills authority) | 11 | RETAIN — no contract-ownership claim |
| ARCHITECT_PLAYBOOK "Type Implications for Engineer" header and ENGINEER §13 "Engineer Focus" labels | 4 | RETAIN — implementation-focus subject lists; ARCHITECT rows name "DB schema" / "API contracts" as subjects without assigning definition (parallel ENGINEER §13 "API route implementation" / "API contract implementation"); the Architect may tighten in a later pass |
| SFP §5 "Phase 3: Database Schema" process heading, build-phase checklist item, manual cross-reference row | 3 | RETAIN — implementation-phase build discipline; SFP line 39 keeps lifecycle axes separate; no seat assignment |
| Technical reference statements (DATABASE_MANUAL "Schema Design Patterns", ECOMMERCE/STRIPE "schema design is deferred", "project-approved ownership and storage contract") | 10 | RETAIN — technical scope, no seat assignment |
| STRIPE_SUBSCRIPTIONS_PLAYBOOK:535 "Schema design and migration SQL are the developer's responsibility" (DevOps Handoff Note) | 1 | RETAIN — developer-vs-DevOps operational split, not an Architect-vs-Engineer seat statement; **OBS-2, noted for the Architect, no change proposed** |

No genuine policy conflict and no required change outside the approved path set was found; nothing is escalated.

## 8. Out of scope, unchanged

D-3 punctuation sites (FRONTEND_FIRST:373, APP_ARCHITECTURE:1206, SFP:118, THEMING:268, UI_UX:128); external follow-ups; template, archive, diagram, transition and date-plan content; Fable's specification (she re-anchors it herself); canonical documents; Git.

## 9. Files in this directory

`AMENDMENT_V1.md` (this), `AMENDMENT_V1_EDITS.json`, `SELECTED_EXACT_EDITS.json`, `PROPOSED_CONTENT/` (the three amended files only), `SELECTED_CONTENT_INDEX.json`, `SELECTED_CONTENT_DIFF.patch`, `EXECUTION_PROPOSAL_INDEX.json`, `EXECUTION_PROPOSAL.patch`, `LANDING_DATE_PLAN.json`, `WORKFLOW_RULING_TRACEABILITY.json`, `SCOPE_LEDGER_SUPPLEMENT.md`, `PROPOSAL_COUNTS.json`, `AMENDMENT_IDENTITIES.json`, `D4_STARTER_KIT_METADATA_NORMALIZATION.json`, `OWNERSHIP_PROPAGATION.tsv`, `VERIFICATION.json`, `VERIFICATION_RAW.txt`, `FABLE_HANDOFF_AMENDED_V1.md`, `OPERATOR_NEXT_STEPS_SUPPLEMENT.md`, `PRESERVATION_SUPPLEMENT.txt`, `README_AMENDED_V1_REVIEW.md`. Generators: `../scratchpad/generators/cody_amend_v1.py`, `cody_amend_v1_verify.py`.
