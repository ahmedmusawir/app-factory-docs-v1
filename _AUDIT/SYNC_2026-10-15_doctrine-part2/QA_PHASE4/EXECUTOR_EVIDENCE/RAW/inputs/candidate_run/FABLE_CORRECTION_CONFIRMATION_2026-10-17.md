# Fable correction confirmation — MC-01…MC-14 against the corrected Phase 2 map

**Seat:** Fable, QA Lead · **Recorded:** 2026-10-17T11:26:40+06:00 · **Run:** `_AUDIT/SYNC_2026-10-15_doctrine-part2/` · **Scope:** Tony's 2026-10-17 assignment "GATE 2 APPROVED; FINALIZE THE INDEPENDENT SPECIFICATION", items 1–2 and 4. Read-only on canonical files; no Git mutation; no intake restarted; template source acceptance not repeated.

## 1. Result

**Correction confirmation: CONFIRMED WITH TWO RETAINED CONTRADICTIONS (D-1, D-2).** All fourteen MC items are addressed as Cody dispositioned them. Two sentences the correction pass did not reach still assert Engineer authorship of DATA_CONTRACT and therefore fail AC6 of the finalized specification as the approved tree stands. They are bounded, two-span map amendments (AMENDED-v1), not a policy question and not a reason to withhold Gate 3 on the specification itself. Two further items (D-3 cosmetic, D-4 process) are recorded and need no acceptance change.

## 2. Package and map identity (assignment item 1)

| Check | Result |
|---|---|
| ZIP `/home/moose/Downloads/FACTORY_PHASE2_MC_CORRECTED_REVIEW_2026-10-16_184920.zip` | SHA-256 `29a835c18aa517d354bf49f39203013b0a772a15ee5c72556d201ea2d01b8b3f` — matches Tony's brief; 512 members |
| `sha256sum -c SHA256SUMS.txt` inside the ZIP | 510 / 510 OK |
| ZIP payload vs local run directory | every one of the 510 payload files byte-identical to `<run>/`; local-only extras are `DELIVERY/` receipts and the earlier ZIP, plus the two inventory files that cannot list themselves |
| `UPDATE_MAP.md` before recording Gate 2 | SHA-256 `fae2981242a49a496e06876323ef53d8e6203c931f9508eef54dcb752609f2ae` — matches brief |
| `EXECUTION_PROPOSAL_INDEX.json` | SHA-256 `84337dcd3b60d059e8c67d1586cd8dba58827c64e14ab46d6d05ab57a611da39` — matches brief |
| Gate 2 record written | `UPDATE_MAP.md` §O, "Gate 2 — APPROVED (recorded by Fable, QA Lead, 2026-10-17T11:19:57+06:00)"; the only change is the 9-line insertion after the §O status paragraph; reviewed wording above it untouched |
| Approved map identity after the record | SHA-256 `cd291270bb6c8e537bcb050685c6464d326254f0d2a703c21f7f304dfe286931` — see `GATE2_APPROVAL_RECORD_2026-10-17.md` |

## 3. Independent replay of the corrected proposal (not Cody's evidence)

| Check | Fable result |
|---|---|
| Index: 101 paths; `proposed_sha256` and byte length vs `PROPOSED_CONTENT/` | 101 / 101 match. 33 modified (31 tier + MANIFEST + CHANGELOG) with `before_sha256` = `git show 9c17939:<path>` for all 33; 68 new (3 playbooks, 25 templates, 32 archives, 4 workflow docs, 4 SVGs), none existing at BASE |
| `SELECTED_EXACT_EDITS.json` sequential replay over BASE for 31 docs | 372 / 372 apply exactly once; residual per document = header bump + one history row only, except STARTER_KIT (see D-4) |
| Templates: `PHASE_2_TEMPLATE_TRANSLATIONS.json` replay from snapshot sources with declared occurrence counts | 25 / 25 destination hashes match the plan and the proposed files; 31 spans; source hashes unchanged |
| Archives | 31 outgoing archives byte-identical to `git show 9c17939:<live path>` (incl. the three my first regex missed: FRONTEND_BUILD_PHASE v1_2_2, FRONTEND_FIRST v1_1_3, STARTER_KIT v1_1); `_ARCHIVE/QA_PLAYBOOK_v1_0.md` = blob `bb41260f6b6f94372a682f04b313a451f2b3c4b1` |
| Headers | 31 bumped once; statuses preserved byte-for-byte incl. the three suffixes (MC-09); three new playbooks at `DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED` |
| MANIFEST | 34 tier rows; 34 / 34 Version/Date/Status cells equal their headers; "How this stays current" and the `_ARCHIVE/README.md` pointer present (MC-10); no workflow/template rows |
| CHANGELOG | 39 rows dated 2026-10-16, contiguous table lines 36–74 inside "Ongoing entries", separator at 76, footer after (MC-03); every W01…W23 and RUL-01…15 named; AD-01 named |
| Version History placement (MC-02/13) | one new row per document in the existing table and its own column shape/order: HANDOFF four-column "## 12. Versioning" newest-first; RECON fence closed (28 fences, even) and row in its table; BIM/BUG_FIX/FEAT/FRONTEND_*/QA/FFM rows in their numbered history sections; no second "Version History" heading anywhere |
| Transitions | 12 spans on 9 paths; every `old` occurs exactly once in the proposed file; `CLOSEOUT_PROPOSED_CONTENT/` holds exactly the `new` text; `actual_sha` null; required evidence files absent and marked PENDING (as they must be) |
| Landing date | 151 spans (40 headers, 111 current rows: 38 history + 39 CHANGELOG + 34 MANIFEST) each occur once; `actual_landing_date` null |
| Workflows | 4 md + 4 SVG present; SVG well-formed XML; all plan steps (7/18/8/24) found in both md and SVG text; md status "Proposed — pending verified publication"; md cites source PNG and supersession; each md embeds its SVG; owners link the md (SFP, Blueprint, FFM, BIM, RRM, DEPLOYMENT) |
| Lints | `python3 -B -I lints/run_all.py` in `PROPOSED_CONTENT/`: PASS, 36 live docs, 0 hits on all four; lint scripts byte-identical to repo `lints/` |
| Ledger | 97 FC rows = 58 + 27 + 3 + 1 SELECTED (89) + 5 OUTSIDE + 3 NO; W 23, RUL 15, AD 1 rows present (MC-12) |
| `TEMPLATE_INSTALL_PLAN.md/json` | marked HISTORICAL — SUPERSEDED (MC-14) |

## 4. Disposition-by-disposition confirmation (assignment item 2)

| Item | Cody's disposition | Fable confirmation | Evidence read |
|---|---|---|---|
| MC-01 | CORRECTED | **Confirmed.** 13 sites now carry "Historical external example (availability unverified):" inside their own container: SFP:62 table cell; SFP:118, HANDOFF:381, UI_UX:128, THEMING:268 bullets; HANDOFF:7, :9 blockquotes; HANDOFF:131, :169, :346, FRONTEND_FIRST:373, APP_ARCHITECTURE:1206 paragraphs; FFM:1997 "two historical FFM examples … Availability is unverified". Zero nested-bold artefacts; "Two real FFMs are available" absent. See D-3 for punctuation. | raw reads of all 13 sites vs BASE |
| MC-02 / MC-13 | CORRECTED | **Confirmed.** RECON: one "## Version History", fence closed before it, row at 558 in its table. HANDOFF: four-column row at 373 under "## 12. Versioning", newest-first; no appended section. | parse + read |
| MC-03 | CORRECTED | **Confirmed.** 39 rows inside the Ongoing table before the separator. | CHANGELOG lines 19–79 |
| MC-04 | CORRECTED | **Confirmed.** Blueprint both flows state Phase 0…5 incl. "Phase 5 — Deployment" and Gate D; SFP vocabulary cites the Blueprint lifecycle; RECON:8 "Stage 0 of FFM module preparation"; ENGINEER:123 resolves; "four-role" only in history rows; MANIFEST FFM row corrected. | grep + reads |
| MC-05 | CORRECTED | **Confirmed.** SFP lines 180–183 add Engine 1 / Post-FFM review (checkpoint 1) / Engine 2 (checkpoint 2) / RRM rows; RRM §2 line 24 cites SFP §2 "Phase Vocabulary — One Canonical Map" without a competing definition. | SFP 171–183; RRM 24 |
| MC-06 | CORRECTED / PUBLICATIONS ADDED | **Confirmed.** FFM §2 flow 80–82, completion checklist 1830–1831, boot prompt 2161–2163; BIM §6 97–99 and 102; four workflow docs + SVGs; owners link them; originals unchanged in snapshot. | reads; XML parse; step diff |
| MC-07 | CORRECTED | **Confirmed for the named sites** — ENGINEER §12 "produces alongside working code" absent; Blueprint Phase 3 heading now "ENGINEERING (Architect Contract Assembly)"; DESIGNER row 69 "Define DATA_CONTRACT before Design — Architect"; BIM §6 full lifecycle (83–99); "FREEZES"/"freeze doctrine"/"attackers" absent. **Two same-family sites were not reached: D-1 and D-2 below.** | reads + grep |
| MC-08 | CORRECTED PROPOSAL; CONDITIONS PENDING | **Confirmed.** 12 spans / 9 paths incl. 3 MANIFEST rows and 4 workflow status lines; commit named by purpose with SHA null; required evidence listed and absent; closeout content matches. Graded by AC33/AC38. | transitions JSON; CLOSEOUT_PROPOSED_CONTENT |
| MC-09 | CORRECTED BY PRESERVATION | **Confirmed.** Three suffixes preserved in headers and MANIFEST cells. | header table |
| MC-10 | CORRECTED BY PRESERVATION | **Confirmed.** "How this stays current" and `_ARCHIVE/README.md` pointer present in MANIFEST. | MANIFEST read |
| MC-11 | PREPARED; DATE PENDING | **Confirmed as a plan.** 151 spans resolve once each; actual date null. Graded by AC30. | LANDING_DATE_PLAN replay |
| MC-12 | CORRECTED | **Confirmed.** Ledger W/RUL/AD rows; CHANGELOG names every W and RUL. | ledger counts; grep |
| MC-14 | CORRECTED | **Confirmed.** Historical banner present; translations JSON is the sole hash authority. | file heads |
| Q-1 / Q-2 / Q-3 | answered by Tony's 2026-10-16 assignment (map §K) | **Accepted as recorded.** Revised derivatives satisfy Q-1; the named closeout commit after evidence satisfies Q-2; preserved suffixes/bump guidance satisfy Q-3. Not reopened. | MAP §K, §D |

## 5. Concrete defects remaining (assignment item 4)

| ID | Exact location (approved tree) | Defect | Acceptance impact | Bounded correction (for Cody to propose, Jarvis to review, Tony to approve as AMENDED-v1) |
|---|---|---|---|---|
| **D-1** | `PROPOSED_CONTENT/01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` lines 140–142: `## 📋 ENGINEER AGENT: WHAT IT PRODUCES` / `The Engineer's full output list:` followed by `### **DATA_CONTRACT.md**`, DB_SCHEMA, API_SPEC, FILE_TREE | Retained baseline heading (BASE line 167, listed in map §B FC-008 placements) asserts the Engineer produces DATA_CONTRACT; contradicts RUL-09 and the corrected Phase 3 heading 58 lines above. Not a search term in PROPAGATION.tsv, so undispositioned. | **FAILS AC6(c)** on the approved tree; AC5 manual read also catches it. | Two ENGINEER-PROPOSED spans: re-word the heading and lead line to describe the Architect-assembled artifact list the Engineer consumes (e.g. "ENGINEERING PACKAGE: WHAT THE APPROVED CONTRACT CONTAINS" / "The approved package the Engineer implements:"). Adds 1–2 edits (372 → 373/374); changes Blueprint `proposed_sha256` and its landing-date span bytes. |
| **D-2** | `PROPOSED_CONTENT/02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` line 746: `> **Author:** Engineer Agent` inside the canonical DATA_CONTRACT template fence, ten lines below the new Architect-ownership note (736–738) | Copyable template names the Engineer as author of the artifact the Architect now owns. | **FAILS AC6(d)**; a fresh Architect copying the template inherits the contradiction. | One ENGINEER-PROPOSED span: `> **Author:** Architect` (or "Architect — approved by Director"). Adds 1 edit; changes ENGINEER `proposed_sha256`. |
| D-3 | FRONTEND_FIRST:373 and APP_ARCHITECTURE:1206 ("…is at: Obtain the source repository…" — the path that followed the colon at BASE was withdrawn, the colon remains); SFP:118, THEMING:268, UI_UX:128 (description runs into "Obtain" with no full stop) | Readability only; markdown structure correct. | None — AC20 passes; recorded as Follow-Up Finding. | Optional: fold five punctuation fixes into AMENDED-v1. |
| D-4 | `PROPOSED_CONTENT/01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` lines 3–4 (standard header inserted), 13 (`**Kit campaign reference:** handbook v1.1 (historical reconciliation; verify current kit revision)` replacing `**Version:** v1.1 (Kit-Perfection campaign applied)`), and the removed `**Last Updated:**` / `**Maintained by:**` lines | Applied by `scratchpad/generators/cody_mc_metadata.py` line 28, not written out as a §C / `SELECTED_EXACT_EDITS.json` span (E116 old and new both still contain the v1.1 line). Approved as bytes through the index hash; D15 asks every added word to be a visible ENGINEER-PROPOSED span. | None on pass/fail — AC2 now enumerates the residual exactly so the QA Executor cannot mis-grade the replay. | Optional: AMENDED-v1 ledgers the span; or Tony records acceptance of the generator normalization in the Gate 3 approval line. |

**Not defects:** SVGs carry no supersession text of their own (the workflow document does; map §D/§H require it of the derivative pair) — recorded as a limitation in spec §6. Owning playbooks link the workflow documents, not the SVGs directly — consistent with map §H.

## 6. Preserved earlier evidence and settled items

Fable's 2026-10-16 verification of the 16:47 package (429 hashes, 334-edit replay, 25-template replay, 31 archives, lints) stands as history for that superseded package; every check was re-run above because bytes changed. Template source acceptance (QA Lead 2026-10-14; Architect verification 2026-10-14) is settled and was not repeated — only the translation replay was. The certified register (97 findings, 94 YES / 3 NO) is unchanged. Tony's approved policy decisions (RUL-01…15, AD-01) were not reopened.

## 7. Recommendation

- **Gate 3:** approve `DOCSET_SYNC_ACCEPTANCE_SPEC.md` v1.0 (SHA-256 in the Gate 3 ZIP inventory). AC6 already grades D-1/D-2; the spec needs only a count re-anchor (AC1/AC2 cells) once AMENDED-v1 lands, which Fable will issue as spec AMENDED-v1.
- **Before Phase 3 release:** Cody proposes AMENDED-v1 for D-1 and D-2 (two or three spans, two paths, regenerated index/patch/landing spans), Jarvis reviews, Tony approves the amendment at Gate 2; otherwise the first Gate Q verdict is a known FAIL on AC6.
- **Operator receipts** (unchanged): preservation commit incl. today's files (`FABLE_GATE3_PRESERVATION_SUPPLEMENT.txt`), remote baseline, execution worktree checkpoint.
