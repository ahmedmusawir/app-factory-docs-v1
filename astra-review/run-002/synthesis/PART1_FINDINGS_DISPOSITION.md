# PART 1 — FINDINGS DISPOSITION (EVIDENCE CONVERGENCE)

**STATUS: DRAFT — EVIDENCE CONVERGENCE + SOL BASELINE ADJUDICATION + CURRENT-MAIN VERIFICATION**
**AUTHORITY: SOL + DIRECTOR ADJUDICATION REQUIRED**

- **Prepared by:** Claudy (Engineer / repo operator), 2026-09-27
- **Branch:** `factory-docs-review-astra-w-chunks`
- **Nature:** structured evidence map, carrying Sol's baseline adjudication (2026-09-27) and a read-only current-main verification against `main` @ `9c179392f79b70da099121fc357d3107ad3bb86e`. **Not** a Correction Package; there are no implementation instructions.

**Revision log**

| Pass | Date | Change |
|---|---|---|
| 1 | 2026-09-27 13:08 | Evidence convergence: 97 atomic records; all adjudication fields blank; current-main UNKNOWN |
| 2 | 2026-09-27 14:11 | Sol adjudication pass: FC renamed to Atomic Finding Convergence Record; 17 Correction Families added; Sol adjudication recorded for the 3 CONFLICTs; FINAL BASELINE SEVERITY set on all 97; CURRENT-MAIN STATUS verified; CORRECTION REQUIRED set. Evidence mappings from Pass 1 are unchanged. |

---

## 0. TERMINOLOGY

- **FC = ATOMIC FINDING CONVERGENCE RECORD.** Each `FC-###` is one traceable, atomic defect record that joins the Astra and/or Fable finding IDs describing that defect. The 97 FCs are **not** 97 independent correction programs.
- **CF = CORRECTION FAMILY.** Final repair planning happens through Correction Families **above** the FC layer (§5A.1). Each FC belongs to exactly one primary family, and cross-family "see also" links remain informational.
- **FINAL BASELINE SEVERITY** is the severity of the defect **as it existed at the review baseline** (`0a787cb`). It is never lowered because current main has changed; current-main state is recorded separately.

## 1. PURPOSE AND LIMITS

This file lines up the two independent review campaigns against the same doctrine baseline, records Sol's baseline adjudication, and records whether each atomic defect remains open on current `main`.

- `FC-###` IDs identify atomic records. They are stable and have not been renumbered since Pass 1.
- **PROPOSED DISPOSITION** remains blank. Sol's explicit conflict rulings sit in a separate **SOL ADJUDICATION** field (FC-005, FC-070, FC-096).
- **CURRENT-MAIN STATUS** comes from read-only git comparison of `0a787cb..9c17939`. No checkout of main was performed (§5A.2).
- Baseline findings remain historical evidence; current-main status never rewrites them.
- No implementation instructions are given. Reviewer recommendations are deliberately left out.

## 2. SOURCE INVENTORY

### 2.1 Authorized evidence read

| Source | Location | Defects | Suggestions |
|---|---|---:|---:|
| Astra C01 Governance | `astra-review/run-002/chunks/01_governance/ASTRA_REVIEW.md` | 3 | 3 |
| Astra C02 Agents / Handoffs | `astra-review/run-002/chunks/02_agents_handoffs/ASTRA_REVIEW.md` | 6 | 4 |
| Astra C03 Build Method | `astra-review/run-002/chunks/03_build_method/ASTRA_REVIEW.md` | 14 | 3 |
| Astra C04 Auth / Data / Security | `astra-review/run-002/chunks/04_auth_data_security/ASTRA_REVIEW.md` | 17 | 3 |
| Astra C05 API / Commerce | `astra-review/run-002/chunks/05_api_commerce/ASTRA_REVIEW.md` | 18 | 3 |
| Astra C06 Design / Frontend | `astra-review/run-002/chunks/06_design_frontend/ASTRA_REVIEW.md` | 12 | 2 |
| Astra C07 Skills / Doc Governance | `astra-review/run-002/chunks/07_skills_doc_governance/ASTRA_REVIEW.md` | 11 | 3 |
| **Astra total** | | **81** | **21** |
| Sol C01–C07 secondary reviews | `astra-review/run-002/chunks/0[1-7]_*/SOL_REVIEW.md` | rulings on all 81 | rulings on all 21 |
| Fable whole-corpus review | `git show origin/factory-docs-review-fable-001:fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md` (read-only, no checkout) | **31** (2 BLOCKER / 5 HIGH / 15 MEDIUM / 9 LOW) | **14** |

- **Sol C06 and C07:** persisted 2026-09-27 from the Director/Sol ruling, before this convergence began.
- **Sol C01–C05:** severity rulings are taken from each file's *Preliminary Sol Disposition* section, plus the rationale for any adjustment.

### 2.2 Baselines

| Review | Baseline | Evidence |
|---|---|---|
| Fable | `0a787cb826118b4a010765d60e41a449df3ce746` | Fable review header |
| Astra | Branch `factory-docs-review-astra-w-chunks`; C07 records baseline `8fcadd474156501e788edcbff620c888dd19d7e9` | Astra C07 §1 |
| Doctrine delta | `git diff --stat 0a787cb 8fcadd4 -- . ':(exclude)astra-review'` returns **no changes** | Checked 2026-09-27 13:01 |

**Both reviews therefore examined the same doctrine content.** The commits between the two baselines touch only `astra-review/`.

### 2.3 Excluded on purpose (not read)

- `fable-review/run-001/reviews/SOL_REVIEW_OF_FABLE_001.md`
- `fable-review/run-001/reviews/FINAL_DISPOSITION.md`
- `astra-review/run-002/synthesis/ASTRA_FACTORY_DOCTRINE_REVIEW_RUN_002.md`, `synthesis/SOL_REVIEW.md`, `synthesis/FABLE_REVIEW.md`, `synthesis/FINAL_DISPOSITION.md`
- The chunk-level `DISPOSITION.md` and `FABLE_REVIEW.md` files, which are 0-byte placeholders in all 7 chunks

**Consequence:** the authorized evidence contains **no Sol ruling on any Fable finding**. Fable-only FC entries record Sol as `N/A`.

## 3. METHOD

### 3.1 Grouping rule
- **Merge rule:** findings share an FC only when they describe the **same underlying defect mechanism in the same doctrine surface**.
- **Theme-only relations:** findings related only by theme stay in separate FCs and are linked with **See also**.
- **Primary FC:** every defect ID has exactly one primary FC. A finding that spans several surfaces, such as FBL-D001 and FBL-D021, is listed as *related* in the other FCs it touches.

### 3.2 Review baseline status
| Status | Meaning in this file |
|---|---|
| **CONFIRMED** | Both reviews independently identify the same defect mechanism in at least the same principal doctrine surface. Extra surfaces or sub-claims in one review are recorded as *Scope delta* and do not change the status. |
| **PARTIAL** | The reviews overlap, but their core claims differ: one core claim is only part of the other's, or they frame the same text as different defects. |
| **UNIQUE** | Only one review raises the defect. |
| **CONFLICT** | The reviews **disagree** on fact or classification. In practice, one classifies the issue as a defect and the other explicitly classifies it as a non-defect or a strength. |

**Severity divergence:** a severity disagreement between two reviews that agree on the mechanism is **not** recorded as CONFLICT. It is recorded in the FC entry and listed in §7.2. This keeps status about *whether the defect exists* separate from *how severe it is*.

### 3.3 Severity fields
- **Astra severity:** as written in the Astra finding.
- **Fable severity:** as written in the Fable finding. When a Fable finding covers several surfaces, its single severity is quoted for each FC it touches, marked "(whole finding)".
- **Sol ruling:** taken word for word or closely paraphrased from the Sol chunk review.
- **FINAL BASELINE SEVERITY (Pass 2), in order of precedence:**
  1. Sol's conflict adjudication (FC-005, FC-070, FC-096).
  2. Sol's closure of provisional severities (FC-002, 014, 026, 036, 037, 052, 061, 063).
  3. Sol's acceptance of Fable-only findings at Fable's stated severity (13 FCs).
  4. Otherwise, the existing Sol chunk ruling on the Astra ID.

  Each FC names its source.

## 4. TOTALS

| Measure | Count |
|---|---:|
| FC root issues | **97** |
| Astra defect findings represented (primary) | **81 / 81** |
| Fable defect findings represented (primary) | **31 / 31** |
| Unmapped defect findings | **0** |
| CONFIRMED | 12 |
| PARTIAL | 7 |
| UNIQUE: Astra only | 62 |
| UNIQUE: Fable only | 13 |
| CONFLICT | 3 |
| Suggestions inventoried (appendix; not mapped) | 21 Astra + 14 Fable = 35 |
| **Pass 2: Correction Families** | **17** (every FC in exactly one) |
| FINAL BASELINE SEVERITY: BLOCKER / HIGH / MEDIUM / LOW | 6 / 36 / 44 / 11 |
| CURRENT-MAIN: OPEN — SOURCE UNCHANGED | 81 |
| CURRENT-MAIN: OPEN — DEFECT REMAINS | 8 |
| CURRENT-MAIN: PARTIALLY REMEDIATED | 5 |
| CURRENT-MAIN: REMEDIATED — CURRENT MAIN | 3 |
| CURRENT-MAIN: SUPERSEDED / NO LONGER APPLICABLE | 0 |
| CURRENT-MAIN: REQUIRES RUNTIME / EXTERNAL VERIFICATION | 0 |
| CORRECTION REQUIRED: YES / NO / VERIFY BEFORE DECISION | 94 / 3 / 0 |

**Fable findings by relationship:**
- 15 overlap with Astra: 9 as primary in CONFIRMED FCs, 6 as primary in PARTIAL FCs.
- 13 are Fable-only.
- 3 are in CONFLICT.

---

## 5. FC REGISTER

### 5.A Governance / Constitution / Cross-cutting

#### FC-001 — Constitutional kit-build instructions (SFP §9 Phase 7, §8 page pattern) conflict with kit-consumption doctrine
- **CORRECTION FAMILY:** CF-01 — Constitution / roles / precedence / lifecycle
- **Astra IDs:** C01-D01 (primary)
- **Fable IDs:** FBL-D001 (related; primary in FC-033)
- **Shared mechanism:** SOFTWARE_FACTORY_PLAYBOOK §9 Phase 7 tells builders to add auth, create login pages, define role flags in `user_metadata`, and protect layouts with `withRoleCheck`. STARTER_KIT_HANDBOOK marks these items as already wired or DO NOT BUILD. The constitution and the kit authority give incompatible prescriptive instructions for the same kit-based build.
- **Astra severity:** HIGH
- **Fable severity:** BLOCKER (FBL-D001, whole finding)
- **Sol ruling:** ACCEPT — HIGH (C01 Sol §8). Sol C01 §5.A notes independent corroboration from Chunk 04 and says not to merge the finding IDs.
- **Scope delta:** Astra alone adds SFP §8's client-fetching `page.tsx` pattern against the Handbook thin-page / Server Component rules. Fable covers only the auth side of Phase 7.
- **See also:** FC-033, FC-035, FC-028
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_ARCHITECTURE_MANUAL`, `AUTH_MANUAL`, `DATABASE_MANUAL`, `MANIFEST`, `SOFTWARE_FACTORY_PLAYBOOK`, `STARTER_KIT_HANDBOOK`, `STATE_MANAGEMENT_MANUAL`, `_ARCHIVE/**`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-002 — Constitutional feature/release checklists omit required approval, acceptance and Gate Q checkpoints
- **CORRECTION FAMILY:** CF-01 — Constitution / roles / precedence / lifecycle
- **Astra IDs:** C01-D02
- **Fable IDs:** none
- **Shared mechanism:** The SFP §13 Feature Development and Pre-Release QA checklists, and the §11 deployment steps, can all be completed without recording the brief/spec/screen-set approvals, the `ACCEPTANCE_SPEC` handoff, a Gate Q verdict or an Operator release decision, even though SFP §2.5 and the Blueprint require them.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT DEFECT — provisional MEDIUM. Sol would re-elevate to HIGH if the checklist proves to be treated as the authoritative release gate. Sol C01 §5.B asks for comparison against Chunk 03.
- **See also:** FC-004 (FBL-D020, constitution lacks the QA seat), FC-013, FC-025, FC-011
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_FACTORY_BLUEPRINT`, `SOFTWARE_FACTORY_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol closure of provisional severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-003 — STARTER_KIT_HANDBOOK references and conventions do not resolve against, or conform to, Hub conventions
- **CORRECTION FAMILY:** CF-13 — Cross-reference / locator / document-structure hygiene
- **Astra IDs:** C01-D03
- **Fable IDs:** FBL-D003 (primary)
- **Shared mechanism:** The handbook, the Factory's canonical kit entry point, cites versioned or embedded-repository paths (`COMPONENT_REGISTRY_v1.1.md`, `agent_docs/APP_FACTORY/...UI-UX-BUILDING-MANUAL_v1_3.md`, and others) that do not exist in the Hub.
- **Astra severity:** MEDIUM
- **Fable severity:** MEDIUM
- **Sol ruling:** ACCEPT — MEDIUM (C01-D03). No Sol ruling on FBL-D003.
- **Scope delta:**
  - **Astra's core claim:** consumer navigation fails. Astra also covers `KNOWN_ISSUES.md` at "repo root" and says external kit contents are UNKNOWN.
  - **Fable's core claim:** the handbook was never migrated. Fable covers the §14 filename-versioning rule, which contradicts `_ARCHIVE/README.md`; the missing standard header, which is a lint miss; and the handbook's reference blast radius (←12).
  - **How Astra treated the rest:** Astra C01 lists the §14 filename-bump rule only as a DEPENDENCY for Chunk 07, not as a defect. Astra C07-D04 describes the handbook's nonstandard header as *disclosed* (see §7.3).
- **See also:** FC-088 (landing paths), FC-096 (lint hits), FC-009 (`KNOWN_ISSUES.md`), FC-081
- **REVIEW BASELINE STATUS:** PARTIAL
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `AUTH_MANUAL`, `COMPONENT_REGISTRY`, `DATABASE_MANUAL`, `MANIFEST`, `STARTER_KIT_HANDBOOK`, `STATE_MANAGEMENT_MANUAL`, `UI_UX_BUILDING_MANUAL`, `_ARCHIVE/**`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-004 — The constitution (Blueprint) predates the QA seat and the module era
- **CORRECTION FAMILY:** CF-01 — Constitution / roles / precedence / lifecycle
- **Astra IDs:** none
- **Fable IDs:** FBL-D020
- **Shared mechanism:**
  - The Blueprint's council has no QA seat or Coordinator.
  - Its router knows only CONVERSION and GREENFIELD, with no BIM/FIX/FEAT routing.
  - Its lifecycle ends at "Ship it" with no Gate Q or Gate D.
  - Meanwhile SFP §2.5, BIM, QA and FIX/FEAT define those seats and gates.
- **Astra severity:** —
- **Fable severity:** HIGH
- **Sol ruling:** N/A (no Sol ruling on Fable findings in the authorized evidence)
- **See also:** FC-002, FC-013, FC-006
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_FACTORY_BLUEPRINT`, `BIM_PLAYBOOK`, `BUG_FIX_PLAYBOOK`, `FEAT_PLAYBOOK`, `MANIFEST`, `QA_PLAYBOOK`, `SOFTWARE_FACTORY_PLAYBOOK`, `agent_docs/RESPONSES/response_2026-08-10_* (evidence)`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-005 — No Factory-wide precedence rule; individual docs each declare themselves the winner
- **CORRECTION FAMILY:** CF-01 — Constitution / roles / precedence / lifecycle
- **Astra IDs:** none as a defect. Astra C01-S01 (SUGGESTION) addresses the same subject.
- **Fable IDs:** FBL-D031
- **Shared mechanism:** Local "X wins" clauses (Rule Zero, Rule Zero-B, ENGINEER §15, DESIGNER §13, QA §5, "disk wins", FFM C.1, skill §6) exist without a tier-precedence rule. Fable cites kit reality such as numbered colors and `httpOnly: false` against doctrine as cases with no tiebreaker.
- **Astra severity:** — (C01-S01 is classified SUGGESTION. Astra states: "This is not counted as a defect: the current statements have plausible stage-specific meanings and already require escalation rather than silent reconciliation.")
- **Fable severity:** MEDIUM
- **Sol ruling:** C01-S01: ACCEPT AS SUGGESTION. No Sol ruling on FBL-D031. Sol C01 §5.C flags "source-of-truth semantics" as a possible Factory-wide theme.
- **See also:** FC-029 (C03-D13, local scope-authority conflict in FFM), FC-042, FC-073
- **REVIEW BASELINE STATUS:** CONFLICT (classification: DEFECT per Fable vs explicit non-defect SUGGESTION per Astra)
- **CURRENT-MAIN STATUS:** OPEN — DEFECT REMAINS
- **CURRENT-MAIN EVIDENCE:** Changed source: skill `CLAUDE.md` (§6). v0.8 §6 still has a local winner clause: "If this doctrine ever contradicts the Skills Playbook or the Factory's QA doctrine, the playbooks win." No Factory-wide precedence rule was added. UI_UX, ENGINEER, DESIGNER, QA, STARTER_KIT, FFM, MANIFEST and the Blueprint are unchanged.
- **SOL ADJUDICATION:** ACCEPT DEFECT (2026-09-27). Reason: Multiple live authority/precedence clauses can produce incompatible answers with no Factory-wide tiebreaker. Preserve stage-specific authority rules, but the missing reconciliation rule is a governance defect.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol conflict adjudication 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-006 — Seat vocabulary not normalized; "Architect" names both the human and an AI agent
- **CORRECTION FAMILY:** CF-01 — Constitution / roles / precedence / lifecycle
- **Astra IDs:** none
- **Fable IDs:** FBL-D007
- **Shared mechanism:** In SFP §1, ENGINEER §15 and HANDOFF §3, "Architect" means the human Operator. In FFM, the skill CLAUDE.md and BIM §2 it means the AI chat seat. The names for the human and deployment seats also vary. BIM gives the "Architect" binding advisory authority, so the ambiguity affects who holds authority.
- **Astra severity:** —
- **Fable severity:** MEDIUM
- **Sol ruling:** N/A
- **See also:** FC-027 (FBL-D014 Engineer identity), FC-004
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** OPEN — DEFECT REMAINS
- **CURRENT-MAIN EVIDENCE:** Changed source: skill `CLAUDE.md`. v0.8 §1 names "Jarvis (Architect)" and "Tony (Operator)", which is one side of the split, not a normalization. SFP §1 "HUMAN (ARCHITECT)", ENGINEER §15, HANDOFF §3 and BIM §2 are unchanged.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-007 — Lifecycle / execution-stage vocabularies lack a unifying map or crosswalk
- **CORRECTION FAMILY:** CF-01 — Constitution / roles / precedence / lifecycle
- **Astra IDs:** C03-D10
- **Fable IDs:** FBL-D008 (primary)
- **Shared mechanism:** FFM sub-phases and FRONTEND_BUILD_PHASE stages are both prescribed without an operational crosswalk. The FFM Components sub-phase is indexed as 4 in one place and 5 in another.
- **Astra severity:** MEDIUM
- **Fable severity:** MEDIUM
- **Sol ruling:** ACCEPT — MEDIUM (C03-D10). No Sol ruling on FBL-D008.
- **Scope delta:**
  - **Astra's core claim:** the FFM ↔ FBP inner execution relationship is unspecified (shared, nested or repeated gates; where demo deployment and Q/D sit).
  - **Fable's core claim:** lifecycle vocabulary proliferates Factory-wide. Its examples are Blueprint phases 0–5, SFP 1–9, FFM sub-phases, FBP stages, the HANDOFF "8 phases" vs FFM `00–07` file-count disagreement, and roadmap phases, giving "Phase 1" at least four referents.
- **See also:** Astra C01-S03 (suggestion; appendix)
- **REVIEW BASELINE STATUS:** PARTIAL
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_FACTORY_BLUEPRINT`, `ENGINEER_PLAYBOOK`, `FFM_PLAYBOOK`, `FRONTEND_BUILD_PHASE_PLAYBOOK`, `HANDOFF_PACKAGE_PLAYBOOK`, `SOFTWARE_FACTORY_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-008 — `FILE_TREE.md` is required by the Blueprint and root CLAUDE.md but no workflow produces it
- **CORRECTION FAMILY:** CF-02 — Artifact / handoff / template contracts
- **Astra IDs:** none
- **Fable IDs:** FBL-D006
- **Shared mechanism:** The Blueprint Phase 3 and root CLAUDE.md treat `FILE_TREE.md` as a source-of-truth artifact. The HANDOFF and FFM package definitions contain four files and no FILE_TREE, and ENGINEER §12 embeds file structure inside DATA_CONTRACT.
- **Astra severity:** —
- **Fable severity:** MEDIUM
- **Sol ruling:** N/A
- **See also:** FC-015 (C02-D03 lists FILE_TREE among specs requiring approval, but not as an absence defect)
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_FACTORY_BLUEPRINT`, `ENGINEER_PLAYBOOK`, `FFM_PLAYBOOK`, `HANDOFF_PACKAGE_PLAYBOOK`, `root CLAUDE.md`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-009 — Load-bearing external artifacts (skills, worked examples, issue logs) are referenced but never located
- **CORRECTION FAMILY:** CF-13 — Cross-reference / locator / document-structure hygiene
- **Astra IDs:** none
- **Fable IDs:** FBL-D011
- **Shared mechanism:** Live doctrine cites these with no locator, and none of them exist in the Hub:
  - the `stark-recon`, `brain-drain`, `stark-frontend-first`, `CLOUD_DEPLOYMENT_SKILLS` and `SUPABASE_MIGRATION_SKILL` skills;
  - the worked examples required by SFP §1.5;
  - `KNOWN_ISSUES.md`, `KIT_PROPOSALS_ARCHIVE.md`, `STARTER_KIT_FEEDBACK.md` and `agent_docs/LESSONS/`.
- **Astra severity:** —
- **Fable severity:** MEDIUM
- **Sol ruling:** N/A
- **See also:** FC-003 (C01-D03 includes the `KNOWN_ISSUES.md` absence), FC-014 (Astra C02-D02 notes `stark-recon` was not inspected; Sol C02 §6.C defers it to skills review)
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** OPEN — DEFECT REMAINS
- **CURRENT-MAIN EVIDENCE:** Changed source: `_SKILLS/` contents. On main, `_SKILLS/` still holds only `factory-docs-update/`. stark-recon, brain-drain, stark-frontend-first, CLOUD_DEPLOYMENT_SKILLS and SUPABASE_MIGRATION_SKILL are all absent. The citing docs (ARCHITECT, SFP, HANDOFF, FFM, SKILLS_PLAYBOOK, STARTER_KIT, FBP, COMPONENT_REGISTRY, BIM) are unchanged.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-010 — "Plan Mode" and root CLAUDE.md are load-bearing but sit outside the governed doc set
- **CORRECTION FAMILY:** CF-17 — Root CLAUDE / governed-instruction status
- **Astra IDs:** none
- **Fable IDs:** FBL-D018
- **Shared mechanism:**
  - Plan Mode is invoked across BIM, BUG_FIX, FFM, FBP and the skill. It is defined only in the SKILLS_PLAYBOOK (for skills) and in root CLAUDE.md.
  - Root CLAUDE.md is not in MANIFEST, is lint-exempt, carries its own version and duplicates the Karpathy protocol that ENGINEER §15 claims as canonical.
  - The FFM/FBP "root CLAUDE.md forbidden zone" pointer resolves to nothing in the Hub.
- **Astra severity:** —
- **Fable severity:** MEDIUM
- **Sol ruling:** N/A
- **See also:** FC-090 (C07-D07), FC-091 (C07-D08), FC-094 (C07-D10). All three are root CLAUDE.md content defects with different mechanisms.
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** OPEN — DEFECT REMAINS
- **CURRENT-MAIN EVIDENCE:** Changed source: skill `CLAUDE.md` D2. v0.8 D2 defines Plan Mode for skill runs only. Root `CLAUDE.md` is unchanged and still absent from MANIFEST, which is also unchanged. The BIM, BUG_FIX, FFM, FBP, ENGINEER and SKILLS_PLAYBOOK references are unchanged.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-011 — Deployment, promotion and rollback have gates and checklists but no owning doctrine
- **CORRECTION FAMILY:** CF-14 — Deployment / Git authority / doctrine distribution
- **Astra IDs:** none
- **Fable IDs:** FBL-D017
- **Shared mechanism:** Gate D requires a recorded revision and rollback readiness. BIM §6 and ENGINEER §17 reference deploy and rollback steps. No doc defines environments, promotion, revision recording or rollback for the named targets.
- **Astra severity:** —
- **Fable severity:** MEDIUM
- **Sol ruling:** N/A
- **See also:** FC-002 (C01-D02 on SFP §11 deployment lacking the release control), Astra C02-S01 (suggestion: operational custody)
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_FACTORY_BLUEPRINT`, `BIM_PLAYBOOK`, `ENGINEER_PLAYBOOK`, `QA_PLAYBOOK`, `SOFTWARE_FACTORY_PLAYBOOK`, `STRIPE_SUBSCRIPTIONS_PLAYBOOK`, `root CLAUDE.md`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-012 — Git/cloud authority differs between FFM-era and module-era doctrine without a reconciling rule
- **CORRECTION FAMILY:** CF-14 — Deployment / Git authority / doctrine distribution
- **Astra IDs:** none
- **Fable IDs:** FBL-D016
- **Shared mechanism:** In FFM Role 4 and FBP Stage 6, the Engineer deploys to staging. BIM §7 and BUG_FIX §3 say the Engineer is "git-zero / cloud-zero". Skill D5 says Claudy owns all git. TESTING §5.1 says to tag at deploy without naming an actor. No rule says the difference is intentional per context.
- **Astra severity:** —
- **Fable severity:** MEDIUM
- **Sol ruling:** N/A
- **See also:** FC-085, FC-086 (skill git sequencing; different mechanism)
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** PARTIALLY REMEDIATED
- **CURRENT-MAIN EVIDENCE:** Changed source: skill `CLAUDE.md` D5. At baseline it read "Claudy owns all git". v0.8 makes it a bounded Hub-only carve-out that "does NOT redefine the Engineer git-zero / cloud-zero doctrine that governs BIM, FIX, FEAT, TRM, and all application-module work". That reconciles the Hub-skill vs module pair. Still unchanged and still in conflict: FFM Role 4 and FBP Stage 6 (Engineer deploys to staging) against BIM §7 and BUG_FIX §3 (git-zero / cloud-zero), plus TESTING §5.1. No Factory-wide authority matrix exists.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

### 5.B Agents / Handoffs / Artifacts

#### FC-013 — Engineer-side completion/handoff doctrine does not carry the QA intake interface
- **CORRECTION FAMILY:** CF-02 — Artifact / handoff / template contracts
- **Astra IDs:** C02-D01
- **Fable IDs:** FBL-D015 (primary)
- **Shared mechanism:** The Engineer's completion contract (ENGINEER §12/§17 → Operations) does not route through, or produce what, QA intake requires. Engineering readiness and the independent QA verdict are not connected at the handoff.
- **Astra severity:** HIGH
- **Fable severity:** MEDIUM
- **Sol ruling:** ACCEPT — HIGH (C02-D01). No Sol ruling on FBL-D015. Sol C02 §6.A: related to C01-D02 but not to be merged automatically.
- **Scope delta:**
  - **Astra's core claim:** the Engineer's ready-for-Operations contract has no QA handoff, `ACCEPTANCE_SPEC`, Gate Q or Operator release interface.
  - **Fable's core claim:** QA §6 requires a 15-item Engineer completion package that no Engineer-side doctrine (BIM §4/§5/§7, ENGINEER §17) instructs anyone to produce. QA §20 artifacts (`QA_PLAN.md`, `GATE_Q_REPORT.md` and others) also have no defined location while the module folder is frozen.
- **Severity divergence:** Astra HIGH vs Fable MEDIUM
- **See also:** FC-002, FC-025, FC-026, FC-004
- **REVIEW BASELINE STATUS:** PARTIAL
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `BIM_PLAYBOOK`, `ENGINEER_PLAYBOOK`, `QA_PLAYBOOK`, `SOFTWARE_FACTORY_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-014 — Recon's operation boundary contradicts its own procedure and required output
- **CORRECTION FAMILY:** CF-03 — Recon / planning / scope-authority boundaries
- **Astra IDs:** C02-D02
- **Fable IDs:** none
- **Shared mechanism:** Recon is specified as "no file changes, no git operations", pure reading and grepping. The same doctrine instructs `npm run build` (S0.7, Q8.6) and requires a written recon report file, with no defined exception.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT DEFECT — provisional MEDIUM. Sol would elevate if recon is shown to mutate target state. Sol C02 §6.C says to cross-check against the `stark-recon` skill.
- **See also:** FC-009
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_FACTORY_BLUEPRINT`, `ARCHITECT_PLAYBOOK`, `ENGINEER_PLAYBOOK`, `RECON_QUESTIONNAIRE`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol closure of provisional severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-015 — Greenfield engineering-spec approval has no execution checkpoint before implementation
- **CORRECTION FAMILY:** CF-02 — Artifact / handoff / template contracts
- **Astra IDs:** C02-D03
- **Fable IDs:** none
- **Shared mechanism:** The Blueprint requires human approval of Engineer-produced DATA_CONTRACT, schema/API specs and FILE_TREE before Phase 4 coding. The Engineer's own "before starting" checks, its §12 "alongside working code" output and its closing checklist can all be followed without that approval step.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH. Sol C02 §6.B says this is a distinct control point from C02-D01 (pre- vs post-implementation) and not to collapse them.
- **See also:** FC-027, FC-008
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_FACTORY_BLUEPRINT`, `ENGINEER_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-016 — Artifact status vocabularies disagree between producer templates and receiving gates (LOCKED vs APPROVED)
- **CORRECTION FAMILY:** CF-02 — Artifact / handoff / template contracts
- **Astra IDs:** C02-D04
- **Fable IDs:** FBL-D012 (primary)
- **Shared mechanism:** The canonical ARCHITECT_QUESTIONNAIRE APP_BRIEF template emits `[DRAFT | REVIEW | LOCKED]`. The ARCHITECT_PLAYBOOK lifecycle and the receiving Designer/Engineer gates require APPROVED (and AMENDED), and no mapping rule connects them.
- **Astra severity:** MEDIUM
- **Fable severity:** LOW
- **Sol ruling:** ACCEPT — MEDIUM (C02-D04). No Sol ruling on FBL-D012.
- **Scope delta:** Fable extends the finding to the FFM stub `Status: LOCKED`, DATA_CONTRACT `DRAFT | APPROVED` and UI_SPEC `Status: APPROVED`.
- **Severity divergence:** Astra MEDIUM vs Fable LOW
- **See also:** FC-019
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ARCHITECT_PLAYBOOK`, `ARCHITECT_QUESTIONNAIRE`, `DESIGNER_PLAYBOOK`, `ENGINEER_PLAYBOOK`, `FFM_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-017 — Architect-seat responsibility (including the greenfield UI_SPEC draft) is assigned differently across docs
- **CORRECTION FAMILY:** CF-02 — Artifact / handoff / template contracts
- **Astra IDs:** C02-D05
- **Fable IDs:** FBL-D005 (primary)
- **Shared mechanism:** HANDOFF §5.5 and ENGINEER §3 (plus FFM §4 and GDSH §8/§11 per Fable) say the greenfield UI_SPEC is "drafted by the Architect, revised by the Designer". The Architect's own handoff and the Designer's required inputs never create or transfer such a draft.
- **Astra severity:** MEDIUM
- **Fable severity:** MEDIUM
- **Sol ruling:** ACCEPT — MEDIUM (C02-D05). No Sol ruling on FBL-D005.
- **Scope delta:**
  - **Astra's core claim:** limited to the missing UI_SPEC-draft producer/consumer step. Astra notes the Blueprint makes UI_SPEC a Designer output and does not establish an Architect-draft stage.
  - **Fable's core claim:** the Architect seat's responsibilities conflict more broadly. ARCHITECT §1 excludes UI/UX, schemas and API contracts, while the Blueprint router has the Architect pre-author DATA_CONTRACT in conversion and FFM Role 3 has the Architect author the entire FFM.
- **See also:** FC-019, FC-006
- **REVIEW BASELINE STATUS:** PARTIAL
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_FACTORY_BLUEPRINT`, `ARCHITECT_PLAYBOOK`, `DESIGNER_PLAYBOOK`, `ENGINEER_PLAYBOOK`, `FFM_PLAYBOOK`, `GLOBAL_DESIGN_SYSTEM_HANDBOOK`, `HANDOFF_PACKAGE_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-018 — Mandatory visual intake has no valid path for a supported nonvisual build
- **CORRECTION FAMILY:** CF-02 — Artifact / handoff / template contracts
- **Astra IDs:** C02-D06
- **Fable IDs:** none
- **Shared mechanism:** The Architect router supports Backend Bundle / CLI builds with little or no UI. Yet the Architect inputs, the Questionnaire Q4 and the Engineer preflight unconditionally require a visual anchor, UI_SPEC and a token/screen package, and STOP without them. There is no not-applicable branch.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT — MEDIUM. The Sol C06 cross-domain list carries "nonvisual app routing" to synthesis.
- **See also:** FC-075
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ARCHITECT_PLAYBOOK`, `ARCHITECT_QUESTIONNAIRE`, `ENGINEER_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-019 — Multiple incompatible APP_BRIEF and UI_SPEC templates coexist under a single-source claim
- **CORRECTION FAMILY:** CF-02 — Artifact / handoff / template contracts
- **Astra IDs:** none as a defect. Astra C02-S04 (SUGGESTION) concerns fields inside the canonical template, not template multiplicity.
- **Fable IDs:** FBL-D004
- **Shared mechanism:** The ARCHITECT_QUESTIONNAIRE claims to be the single APP_BRIEF template source (12 sections). HANDOFF §5.1 (14 sections) and FFM §9.1/C.2 (13 sections) define different shapes. UI_SPEC likewise appears as DESIGNER §8 (5 sections), HANDOFF §5.3 (9 sections) and FFM §9.3 (12 sections).
- **Astra severity:** —
- **Fable severity:** HIGH
- **Sol ruling:** N/A
- **See also:** FC-016, FC-017
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ARCHITECT_QUESTIONNAIRE`, `DESIGNER_PLAYBOOK`, `FFM_PLAYBOOK`, `HANDOFF_PACKAGE_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

### 5.C Build Method / Testing / QA

#### FC-020 — TESTING webhook recipe acknowledges success unconditionally, without durable processing or recovery
- **CORRECTION FAMILY:** CF-05 — Testing / evidence / environment fidelity
- **Astra IDs:** C03-D05
- **Fable IDs:** none
- **Shared mechanism:** TESTING G5 prescribes that the webhook handler always return 200 to prevent retries. The tests check call shape, not persistence outcome, and nothing requires durable capture or reconciliation before acknowledging.
- **Astra severity:** BLOCKER
- **Fable severity:** —
- **Sol ruling:** ACCEPT — BLOCKER
- **See also:** FC-052 (same mechanism in ECOM/STRIPE; separate surface), FC-059, FC-062, FC-039
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `BIM_PLAYBOOK`, `QA_PLAYBOOK`, `TESTING_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** BLOCKER — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-021 — Payment-error recipe moves sensitive error content into server logs
- **CORRECTION FAMILY:** CF-05 — Testing / evidence / environment fidelity
- **Astra IDs:** C03-D06
- **Fable IDs:** none
- **Shared mechanism:** TESTING §4.3 acknowledges that payment errors can contain card details, emails and request IDs. It then mandates logging the full error (`console.error("Stripe Error:", error)`), with no redaction and a test that checks only the response body. QA forbids PII or secrets in logs.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** FC-051 (FBL-D019's sub-claim that ECOM §3 returns Stripe `error.message` **to the client**: the response side, a different surface), FC-064 (FBL-D022, raw upstream error text propagated)
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `QA_PLAYBOOK`, `TESTING_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-022 — Mutating E2E helpers lack an enforced test-environment boundary
- **CORRECTION FAMILY:** CF-05 — Testing / evidence / environment fidelity
- **Astra IDs:** C03-D08
- **Fable IDs:** none
- **Shared mechanism:** The E2E recipe registers users, seeds subscriptions through an admin client and deletes records against whatever Supabase URL and privileged key are loaded. Nothing checks that the target is an approved test project before mutation.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** FC-069 (env-var naming)
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `QA_PLAYBOOK`, `TESTING_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-023 — Local exceptions permit implementation before scope approval
- **CORRECTION FAMILY:** CF-03 — Recon / planning / scope-authority boundaries
- **Astra IDs:** C03-D04
- **Fable IDs:** none
- **Shared mechanism:** BIM §7 (imported by FEAT, repeated in FIX) lets the Engineer step outside the enumerated writable surface when they judge it genuinely required, with ratification afterwards. TESTING §3.3 says HIGH security findings should be fixed inline. Both conflict with prior-approval rules in the SKILLS_PLAYBOOK, BUG_FIX, SFP §2.5 and ENGINEER §15.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** FC-012
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_FACTORY_SKILLS_PLAYBOOK`, `BIM_PLAYBOOK`, `BUG_FIX_PLAYBOOK`, `ENGINEER_PLAYBOOK`, `FEAT_PLAYBOOK`, `SOFTWARE_FACTORY_PLAYBOOK`, `TESTING_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-024 — E2E workaround recipe can remove a shipped failure from the system under test
- **CORRECTION FAMILY:** CF-05 — Testing / evidence / environment fidelity
- **Astra IDs:** C03-D09
- **Fable IDs:** none
- **Shared mechanism:** TESTING §§3.5–3.6 and G11 recommend aborting or neutralizing a production-present script during E2E, presented as a fix. The recipe does not require a reduced-coverage label or verification with the script enabled.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** FC-063
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `QA_PLAYBOOK`, `TESTING_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-025 — FFM (and combined-artifact allowances) omit the mandatory `ACCEPTANCE_SPEC.md` lifecycle and QA handoff
- **CORRECTION FAMILY:** CF-04 — FFM / module acceptance and freeze mechanics
- **Astra IDs:** C03-D03
- **Fable IDs:** none
- **Shared mechanism:** FFM's folder trees, file guides, handoff diagram and authoring checklist contain no `ACCEPTANCE_SPEC.md` creation or finalization step and no QA intake. QA §§6/20 accept "equivalent" artifacts, and BUG_FIX §18 allows combined documents. All three conflict with SFP §2.5's exact-filename mandate.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH. Sol says it reinforces C01-D02 and C02-D01 but should not be merged automatically.
- **See also:** FC-002, FC-013
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `BUG_FIX_PLAYBOOK`, `FFM_PLAYBOOK`, `FRONTEND_BUILD_PHASE_PLAYBOOK`, `QA_PLAYBOOK`, `SOFTWARE_FACTORY_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-026 — Whole-folder module freeze conflicts with required in-folder working artifacts
- **CORRECTION FAMILY:** CF-04 — FFM / module acceptance and freeze mechanics
- **Astra IDs:** C03-D01
- **Fable IDs:** none
- **Shared mechanism:** BIM (and FIX, and FEAT by import) freezes the module folder from Plan Mode to STOP, "nothing inside may be added or edited". The same doctrine requires the Engineer to maintain and finalize `ACCEPTANCE_SPEC.md`, which lives inside that folder.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT DEFECT — provisional MEDIUM
- **See also:** FC-013 (FBL-D015 notes QA artifacts have no home while the folder is frozen)
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `BIM_PLAYBOOK`, `BUG_FIX_PLAYBOOK`, `FEAT_PLAYBOOK`, `SOFTWARE_FACTORY_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol closure of provisional severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-027 — Greenfield DATA_CONTRACT authorship and timing are not executable as written
- **CORRECTION FAMILY:** CF-02 — Artifact / handoff / template contracts
- **Astra IDs:** C03-D07
- **Fable IDs:** FBL-D014 (primary)
- **Shared mechanism:** Doctrine assigns the greenfield DATA_CONTRACT to the Engineer (FFM §7). The execution sequence (FFM §12.4, §14, §18; Blueprint Phase 3/4) either leaves the Engineer consuming an unfinished "contract shell" or assigns authorship back to another seat. So when, and by whom, the contract is completed is undetermined.
- **Astra severity:** HIGH
- **Fable severity:** MEDIUM
- **Sol ruling:** ACCEPT — HIGH (C03-D07). Sol says this directly reinforces C02-D03. No Sol ruling on FBL-D014.
- **Scope delta:**
  - **Astra's framing:** the corrected ownership note has not propagated into the FFM recipe or checklist.
  - **Fable's framing:** Engineer seat identity is ambiguous (spec-authoring chat agent vs Claude Code). Fable cites Blueprint Phase 3 ("Engineer produces…") vs Phase 4 ("Engineer prompts Claudy") and the ENGINEER §12 "Author: Engineer Agent" header.
- **Severity divergence:** Astra HIGH vs Fable MEDIUM
- **See also:** FC-015, FC-006
- **REVIEW BASELINE STATUS:** PARTIAL
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_FACTORY_BLUEPRINT`, `ENGINEER_PLAYBOOK`, `FFM_PLAYBOOK`, `FRONTEND_FIRST_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-028 — FFM prescribes the auth-service wrapper that kit-consumption doctrine forbids
- **CORRECTION FAMILY:** CF-04 — FFM / module acceptance and freeze mechanics
- **Astra IDs:** C03-D02
- **Fable IDs:** none as primary
- **Shared mechanism:** The FFM §9.2 auth service contract and the §12.4 service sub-phase direct wrapping the kit's `getUser()` / `signInWithPassword()` in `/src/services/`. FRONTEND_FIRST §0 and FBP §1.6 prohibit redundant `authService.ts` wrappers.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** FC-033. FBL-D001 separately cites APP_ARCHITECTURE §2 listing `authServices.ts` against AUTH §0: the same wrapper prohibition on a different surface, which Astra did not review as primary.
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ENGINEER_PLAYBOOK`, `FFM_PLAYBOOK`, `FRONTEND_BUILD_PHASE_PLAYBOOK`, `FRONTEND_FIRST_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-029 — FFM gives two different documents final scope authority
- **CORRECTION FAMILY:** CF-03 — Recon / planning / scope-authority boundaries
- **Astra IDs:** C03-D13
- **Fable IDs:** none as primary
- **Shared mechanism:** FFM §9.1 makes APP_BRIEF the single source of truth for scope. The copyable root-manager stub (Appendix C.1) says `_project/CLAUDE.md` wins on scope.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT — MEDIUM
- **See also:** FC-005 (FBL-D031 cites FFM C.1's per-module order among the local "winner" clauses)
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `FFM_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-030 — Fixture discovery can publish unusable roles, and its consumer reads a different count field
- **CORRECTION FAMILY:** CF-05 — Testing / evidence / environment fidelity
- **Astra IDs:** C03-D12
- **Fable IDs:** none
- **Shared mechanism:**
  - TESTING fixture discovery labels roles without checking that they exist or meet prerequisites, so it can write "successful" JSON with empty roles.
  - The pagination consumer reads `.product_count`, but discovery preserved `.count`.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT — MEDIUM
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `TESTING_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-031 — Metadata helper cannot distinguish an absent key from a present null
- **CORRECTION FAMILY:** CF-05 — Testing / evidence / environment fidelity
- **Astra IDs:** C03-D11
- **Fable IDs:** none
- **Shared mechanism:** TESTING §4.2 requires distinguishing a missing key from a present empty value. The sample `entry ? entry.value : null` returns `null` in both cases.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT — MEDIUM
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `TESTING_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-032 — FRONTEND_BUILD_PHASE checklist points Gate Q / Gate D to the wrong QA_PLAYBOOK sections
- **CORRECTION FAMILY:** CF-13 — Cross-reference / locator / document-structure hygiene
- **Astra IDs:** C03-D14
- **Fable IDs:** FBL-D025 (primary)
- **Shared mechanism:** FBP §9 cites QA §9 (Gate Q) and §10 (Gate D). In the live QA doc those are the Engagement Lifecycle and Scope Protection sections; the gates are at §12 and §13.
- **Astra severity:** LOW
- **Fable severity:** LOW
- **Sol ruling:** ACCEPT — LOW (C03-D14). No Sol ruling on FBL-D025.
- **Scope delta:** Fable adds that the 2026-08-10 ripple map marked FBP "CONSISTENT" without checking anchors. That is process evidence from a response file deleted from the working tree by Director ruling; it existed at the review baseline.
- **See also:** FC-083, FC-087
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `FRONTEND_BUILD_PHASE_PLAYBOOK`, `QA_PLAYBOOK`, `agent_docs/RESPONSES/response_2026-08-10_* (evidence)`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** LOW — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

### 5.D Auth / Data / State / Security

#### FC-033 — AUTH_MANUAL privileged recipes authorize from `user_metadata`, recreate competing role stores and supply an app-side superadmin-creation surface
- **CORRECTION FAMILY:** CF-06 — Auth / authorization / session authority
- **Astra IDs:** C04-D01
- **Fable IDs:** FBL-D001 (primary; also related to FC-001 and FC-035)
- **Shared mechanism:**
  - AUTH §12 SuperAdmin routes check `requester.user_metadata.is_qr_superadmin` and create superadmins from the app.
  - §13 adds a `role` column to a mirror table, and the Summary says roles are stored in metadata.
  - These contradict AUTH "Where Roles Live", DATABASE §2 and STARTER_KIT §§1–2 (console-only superadmin; table-based roles).
  - The legacy advisory does not cover these privileged recipes.
- **Astra severity:** BLOCKER
- **Fable severity:** BLOCKER
- **Sol ruling:** ACCEPT — BLOCKER (C04-D01). No Sol ruling on FBL-D001.
- **Scope delta:** FBL-D001 also covers these surfaces. None was examined as primary by Astra:
  - APP_ARCHITECTURE_MANUAL §2 lists `authServices.ts` in the standard layout.
  - APP_ARCHITECTURE_MANUAL §10 middleware reads `user.user_metadata?.role`.
  - The AUTH registration flow shows `is_qr_*` default metadata.
  - The SFP Phase 7 and STATE parts of FBL-D001 are mapped in FC-001 and FC-035.
- **See also:** FC-034, FC-038, FC-036, FC-028
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_ARCHITECTURE_MANUAL`, `AUTH_MANUAL`, `DATABASE_MANUAL`, `MANIFEST`, `SOFTWARE_FACTORY_PLAYBOOK`, `STARTER_KIT_HANDBOOK`, `STATE_MANAGEMENT_MANUAL`, `_ARCHIVE/**`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** BLOCKER — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-034 — Public signup forwards caller-controlled role metadata into the role-creation trigger path
- **CORRECTION FAMILY:** CF-06 — Auth / authorization / session authority
- **Astra IDs:** C04-D03
- **Fable IDs:** none as primary
- **Shared mechanism:** The public signup endpoint forwards the request's `user_metadata` unchanged to `auth.signUp`. The described trigger reads `raw_user_meta_data.role` on every auth-user insert, and no trusted boundary forces a member role for public signup.
- **Astra severity:** BLOCKER
- **Fable severity:** —
- **Sol ruling:** ACCEPT — BLOCKER
- **See also:** FC-033 (FBL-D001 notes `is_qr_*` default metadata in the registration flow as evidence of metadata-driven roles, but does not raise caller-controlled forwarding)
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `AUTH_MANUAL`, `DATABASE_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** BLOCKER — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-035 — Active client-side recipes claim route and identity authority (HOC, post-mount Navbar, persisted auth store)
- **CORRECTION FAMILY:** CF-06 — Auth / authorization / session authority
- **Astra IDs:** C04-D08
- **Fable IDs:** FBL-D001 (related; primary in FC-033)
- **Shared mechanism:**
  - AUTH §14's `withRoleCheck` HOC gates layouts client-side on persisted role flags, and its later Navbar fetches identity after mount.
  - STATE §1 ("Zustand … route protection") and §8 persist `user.role` and export `selectIsAdmin`.
  - All of these contradict AUTH Navbar Law and STATE's own Division of Labor.
- **Astra severity:** HIGH
- **Fable severity:** BLOCKER (FBL-D001, whole finding)
- **Sol ruling:** ACCEPT (listed under HIGH, C04 Sol §10)
- **Scope delta:**
  - Astra alone adds that the HOC admits `member` for an admin layout, `selectIsAdmin` implicitly includes superadmin, and `isAuthorized` stays true on redirect.
  - Fable alone adds the APP_ARCHITECTURE §4 `'use client'` AdminLayout gated on `selectIsAdmin`.
- **Severity divergence:** Astra HIGH vs Fable BLOCKER (Fable's severity applies to its whole multi-surface finding)
- **See also:** FC-036, FC-041, FC-040
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_ARCHITECTURE_MANUAL`, `AUTH_MANUAL`, `DATABASE_MANUAL`, `MANIFEST`, `SOFTWARE_FACTORY_PLAYBOOK`, `STARTER_KIT_HANDBOOK`, `STATE_MANAGEMENT_MANUAL`, `_ARCHIVE/**`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-036 — Layout admission is presented as the authorization boundary for privileged server actions
- **CORRECTION FAMILY:** CF-06 — Auth / authorization / session authority
- **Astra IDs:** C04-D02
- **Fable IDs:** none
- **Shared mechanism:** The AUTH server-action recipe treats the route-group layout gate as the authorization for `addMember` / `addUser`, which then use a service-role client with no operation-local caller or role check. STARTER_KIT §1 repeats the dependency.
- **Astra severity:** BLOCKER
- **Fable severity:** —
- **Sol ruling:** ACCEPT DEFECT — severity pending final disposition. Sol: "Do NOT automatically accept BLOCKER severity until Factory disposition decides…"
- **See also:** FC-035, FC-057
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `AUTH_MANUAL`, `STARTER_KIT_HANDBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** BLOCKER — source: Sol closure of provisional severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-037 — Soft-delete RLS policy is an access grant, not a safely composing exclusion
- **CORRECTION FAMILY:** CF-07 — Data / RLS / state correctness and privacy
- **Astra IDs:** C04-D06
- **Fable IDs:** none
- **Shared mechanism:** The DATABASE §2 soft-delete recipe adds a permissive `USING (is_deleted = FALSE)` SELECT policy without enabling RLS. Composed with owner policies, permissive grants OR together, which can widen visibility.
- **Astra severity:** BLOCKER
- **Fable severity:** —
- **Sol ruling:** ACCEPT DEFECT — HIGH by default; BLOCKER where used as access protection for private or restricted data
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `DATABASE_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: Sol closure of provisional severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-038 — Client-capability guidance both underpowers admin calls and overgeneralizes RLS bypass
- **CORRECTION FAMILY:** CF-06 — Auth / authorization / session authority
- **Astra IDs:** C04-D05
- **Fable IDs:** none
- **Shared mechanism:** AUTH §§12–13 invoke `auth.admin.*` with the session (anon-key) client. DATABASE §5 lists "API routes" generally as a reason to bypass RLS. The session-vs-admin capability boundary is reversed on both sides.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT (HIGH)
- **See also:** FC-033
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `API_AND_SERVICES_MANUAL`, `AUTH_MANUAL`, `DATABASE_MANUAL`, `STARTER_KIT_HANDBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-039 — Multi-step persistence recipes leave compensation failures unrecoverable
- **CORRECTION FAMILY:** CF-07 — Data / RLS / state correctness and privacy
- **Astra IDs:** C04-D10
- **Fable IDs:** none
- **Shared mechanism:** The DATABASE §11 pseudo-transaction and the AUTH §§12–13 synchronized create/delete paths ignore compensation or deletion results, or continue after partial failure. There is no reconciliation state or recovery owner.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT (HIGH)
- **See also:** FC-020, FC-052
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `AUTH_MANUAL`, `DATABASE_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-040 — Persisted personal data has no enforceable account-transition lifecycle
- **CORRECTION FAMILY:** CF-07 — Data / RLS / state correctness and privacy
- **Astra IDs:** C04-D11
- **Fable IDs:** none as primary
- **Shared mechanism:** STATE persists email, names, addresses and phone in origin-wide `checkout-storage`. Logout clears only auth-store flags, and the reset guidance is optional, so account B can hydrate account A's personal data. This conflicts with the AUTH sensitive-storage advice.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT (HIGH)
- **See also:** FC-068 (FBL-D026, checkout-store shape mismatch across manuals), FC-044, FC-047
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `AUTH_MANUAL`, `STATE_MANAGEMENT_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-041 — The canonical `protectPage` recipe's call and return contract is incompatible with its documented callers
- **CORRECTION FAMILY:** CF-06 — Auth / authorization / session authority
- **Astra IDs:** C04-D07
- **Fable IDs:** none
- **Shared mechanism:**
  - AUTH `protectPage` calls `getUserRole(user)` without `await` and returns `user`.
  - The handbook specifies an async, no-argument `getUserRole()`.
  - Navbar Law destructures `{ user, role }` from the guard.
  - The `AppRole` import source differs between the recipe and the handbook.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT (HIGH)
- **See also:** FC-035
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `AUTH_MANUAL`, `STARTER_KIT_HANDBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-042 — Cookie `httpOnly` guidance contradicts the kit session model
- **CORRECTION FAMILY:** CF-06 — Auth / authorization / session authority
- **Astra IDs:** C04-D04
- **Fable IDs:** FBL-D030 (primary)
- **Shared mechanism:** AUTH "Cookie Configuration" and Security Best Practices require `httpOnly: true`. STARTER_KIT_HANDBOOK §1 says `httpOnly: false` is deliberate for client-side session access and must not be tightened.
- **Astra severity:** HIGH
- **Fable severity:** MEDIUM
- **Sol ruling:** ACCEPT (HIGH) for C04-D04. No Sol ruling on FBL-D030.
- **Scope delta:** Fable alone adds that AUTH shows `src/middleware.ts` where the kit ships `src/proxy.ts`. APP_ARCHITECTURE §10 flags this; AUTH does not.
- **Severity divergence:** Astra HIGH vs Fable MEDIUM
- **See also:** FC-005
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `AUTH_MANUAL`, `STARTER_KIT_HANDBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-043 — Email confirmation route accepts an unbounded external redirect destination
- **CORRECTION FAMILY:** CF-06 — Auth / authorization / session authority
- **Astra IDs:** C04-D09
- **Fable IDs:** none
- **Shared mechanism:** GET `/api/auth/confirm` redirects to `new URL(next, request.url)` with `next` taken from the query. There is no same-origin or allowed-path check, so absolute and network-path URLs escape the application.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT (HIGH)
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `AUTH_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-044 — Logout reports success without checking the sign-out result
- **CORRECTION FAMILY:** CF-06 — Auth / authorization / session authority
- **Astra IDs:** C04-D16
- **Fable IDs:** none
- **Shared mechanism:** POST `/api/auth/logout` discards the `signOut()` result and always returns 200 "Logged out successfully", contrary to the manual's own "don't ignore auth errors" rule.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT (MEDIUM)
- **See also:** FC-040
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `AUTH_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-045 — Timestamp-only cursor pagination silently skips tied records
- **CORRECTION FAMILY:** CF-07 — Data / RLS / state correctness and privacy
- **Astra IDs:** C04-D17
- **Fable IDs:** none
- **Shared mechanism:** The DATABASE §12 cursor orders and filters on the non-unique `created_at` alone (`.lt`, limit 20), so rows tied at a page boundary are skipped.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT (MEDIUM)
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `DATABASE_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-046 — Alternative hydration hook changes the hook invocation count
- **CORRECTION FAMILY:** CF-07 — Data / RLS / state correctness and privacy
- **Astra IDs:** C04-D13
- **Fable IDs:** none
- **Shared mechanism:** `useHydratedStore` returns early while unhydrated, then calls the store hook a second time. The comment claims it throws a promise, but the code returns null.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT (MEDIUM)
- **See also:** FC-047
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `STATE_MANAGEMENT_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-047 — Persistence readiness can become permanently false after a reset or storage failure
- **CORRECTION FAMILY:** CF-07 — Data / RLS / state correctness and privacy
- **Astra IDs:** C04-D12
- **Fable IDs:** none
- **Shared mechanism:** `reset: () => set(initialState)` resets `hasHydrated` to false, and only rehydration sets it true again. The error callback never reaches a terminal state, so gated UI can hang.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT (MEDIUM)
- **See also:** FC-046
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `STATE_MANAGEMENT_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-048 — A nonempty client store permanently overrides new server data
- **CORRECTION FAMILY:** CF-07 — Data / RLS / state correctness and privacy
- **Astra IDs:** C04-D15
- **Fable IDs:** none
- **Shared mechanism:** The STATE §7 `ProductList` initializes the store only when it is empty and renders from the store. Later server props, including an empty result, are ignored.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT (MEDIUM)
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `STATE_MANAGEMENT_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-049 — Composite-item update mutates the previous state snapshot
- **CORRECTION FAMILY:** CF-07 — Data / RLS / state correctness and privacy
- **Astra IDs:** C04-D14
- **Fable IDs:** none
- **Shared mechanism:** The STATE §3 composite-key example shallow-copies the array and then mutates `newItems[i].quantity` in place, which contradicts the manual's immutable-update rule.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT (MEDIUM)
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `STATE_MANAGEMENT_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

### 5.E API / Commerce / Payments

#### FC-050 — Public order-status mutation accepts the caller's assertion that payment succeeded
- **CORRECTION FAMILY:** CF-08 — Commerce money authority / checkout contract
- **Astra IDs:** C05-D03
- **Fable IDs:** none
- **Shared mechanism:** The browser posts `orderId`, `status: 'processing'` and any `paymentIntentId`. The route sets `set_paid = true` and forwards the change through server WooCommerce credentials with no authentication, ownership check, Stripe retrieval or transition check.
- **Astra severity:** BLOCKER
- **Fable severity:** —
- **Sol ruling:** ACCEPT — BLOCKER
- **See also:** FC-051
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ECOMMERCE_AND_PAYMENTS_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** BLOCKER — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-051 — PaymentIntent amount is computed from client-supplied prices, shipping and discount despite "never trust client"
- **CORRECTION FAMILY:** CF-08 — Commerce money authority / checkout contract
- **Astra IDs:** C05-D04
- **Fable IDs:** FBL-D019 (primary)
- **Shared mechanism:** Under the ECOM §3 comment "Recalculate total on server – never trust client", the route passes `body.items[].price`, `body.shipping.cost` and `body.coupon.discount` from the request into `calculateOrderTotal`. This contradicts the manual's own §11 checklist.
- **Astra severity:** BLOCKER
- **Fable severity:** BLOCKER
- **Sol ruling:** ACCEPT — BLOCKER (C05-D04). No Sol ruling on FBL-D019.
- **Scope delta:**
  - Astra alone adds that the order ID is caller-set in metadata, the WooCommerce total is ignored, the success webhook marks the metadata-selected order paid without an amount/currency binding, and the imported `calculateOrderTotal` is absent from the manual.
  - Fable alone adds that the same handler returns Stripe `error.message` to the client (status 400), contrary to TESTING §4.3's generic-message rule.
- **See also:** FC-050, FC-060, FC-067, FC-021
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ECOMMERCE_AND_PAYMENTS_MANUAL`, `TESTING_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** BLOCKER — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-052 — Commerce and subscription webhook acknowledgment conceals failed business persistence
- **CORRECTION FAMILY:** CF-09 — Webhook / event durability, idempotency and ordering
- **Astra IDs:** C05-D05
- **Fable IDs:** none
- **Shared mechanism:** The ECOM §9 handlers catch WooCommerce update errors and still return `{ received: true }`. The STRIPE §6 UPSERT result is not inspected, the guidance says "Always return 200", and reconciliation is only a roadmap item.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH minimum; BLOCKER candidate depending on architecture
- **See also:** FC-020 (same mechanism in TESTING G5), FC-059, FC-062, FC-054
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ECOMMERCE_AND_PAYMENTS_MANUAL`, `STRIPE_SUBSCRIPTIONS_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: Sol closure of provisional severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-053 — Checkout creation lacks the retry and concurrency identity its invariants require
- **CORRECTION FAMILY:** CF-09 — Webhook / event durability, idempotency and ordering
- **Astra IDs:** C05-D06
- **Fable IDs:** none
- **Shared mechanism:** Every initialization creates a new order and PaymentIntent with no idempotency key. The subscription flow creates Customers and Sessions without stable identity and diverts only on status `active`.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** FC-056
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ECOMMERCE_AND_PAYMENTS_MANUAL`, `STRIPE_SUBSCRIPTIONS_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-054 — Event handlers can regress newer commerce or subscription state
- **CORRECTION FAMILY:** CF-09 — Webhook / event durability, idempotency and ordering
- **Astra IDs:** C05-D07
- **Fable IDs:** none
- **Shared mechanism:** Commerce and subscription handlers apply each event's snapshot directly, with no transition, freshness or ordering rule. Out-of-order delivery can end a paid order at `failed` or restore a cancelled subscription.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** FC-052, FC-056
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ECOMMERCE_AND_PAYMENTS_MANUAL`, `STRIPE_SUBSCRIPTIONS_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-055 — Subscription bootstrap and resubscribe writes conflict with the prescribed schema
- **CORRECTION FAMILY:** CF-09 — Webhook / event durability, idempotency and ordering
- **Astra IDs:** C05-D10
- **Fable IDs:** none
- **Shared mechanism:**
  - `tier` is required with no default, `status` defaults to `active`, and `user_id` is unique.
  - Checkout must save the customer ID before payment, but no unpaid bootstrap state is defined.
  - The webhook UPSERT conflicts only on `stripe_subscription_id`, so first-subscribe and resubscribe paths collide.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** FC-053
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `STRIPE_SUBSCRIPTIONS_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-056 — Webhook deduplication neither excludes concurrent execution nor identifies events reliably
- **CORRECTION FAMILY:** CF-09 — Webhook / event durability, idempotency and ordering
- **Astra IDs:** C05-D01
- **Fable IDs:** none
- **Shared mechanism:** API §11 reads `processed_webhooks`, does the work, then inserts a marker without checking the result, keyed on `webhookId || order._id`. This is non-atomic, and the key identifies an aggregate rather than an event.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** FC-053, FC-054
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `API_AND_SERVICES_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-057 — Manual sync exposes a privileged mutation as an unprotected GET
- **CORRECTION FAMILY:** CF-10 — API trust boundaries / integration / failure semantics
- **Astra IDs:** C05-D08
- **Fable IDs:** none
- **Shared mechanism:** API §13 `/api/sync` exports `GET()` with no identity or role check, and it upserts database records. This contradicts AUTH's rule that every request is validated.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** FC-036
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `API_AND_SERVICES_MANUAL`, `AUTH_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-058 — Generic webhook verification signs reconstructed JSON and chains supposedly alternative schemes
- **CORRECTION FAMILY:** CF-10 — API trust boundaries / integration / failure semantics
- **Astra IDs:** C05-D09
- **Fable IDs:** none
- **Shared mechanism:** The API §11 validator hashes `JSON.stringify(payload)` after parsing, rather than the raw body. It also runs "Option 1" (shared-secret header) and "Option 2" (HMAC) in sequence, where they are meant to be alternatives.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `API_AND_SERVICES_MANUAL`, `ECOMMERCE_AND_PAYMENTS_MANUAL`, `STRIPE_SUBSCRIPTIONS_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-059 — Required webhook follow-up has no durable acceptance or recovery boundary
- **CORRECTION FAMILY:** CF-09 — Webhook / event durability, idempotency and ordering
- **Astra IDs:** C05-D02
- **Fable IDs:** none
- **Shared mechanism:** The API §11 "fire-and-forget" `triggerAsyncFollowUp` is not awaited. The handler returns success, and failures are only logged, with no durable job or retry.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH when the follow-up is required business work
- **See also:** FC-020, FC-052
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `API_AND_SERVICES_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH (Sol: HIGH when the follow-up is required business work) — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-060 — The displayed checkout caller cannot satisfy its order endpoint contract
- **CORRECTION FAMILY:** CF-08 — Commerce money authority / checkout contract
- **Astra IDs:** C05-D11
- **Fable IDs:** none as primary
- **Shared mechanism:**
  - `initializePayment` omits the required `shippingMethod`, which the route dereferences.
  - Email is sent as `customerEmail`, but the route reads `billing.email`.
  - Coupon state is sent to neither order creation nor intent creation.
  - `calculateOrderTotal` does not match the exported `calculateCartTotals`.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT — HIGH
- **See also:** FC-051, FC-068 (FBL-D026, checkout store shape mismatch between ECOM and STATE)
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ECOMMERCE_AND_PAYMENTS_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-061 — Revalidation secret comparison fails open when the environment variable is absent
- **CORRECTION FAMILY:** CF-10 — API trust boundaries / integration / failure semantics
- **Astra IDs:** C05-D13
- **Fable IDs:** none
- **Shared mechanism:** API §9 rejects only when `secret !== process.env.REVALIDATION_SECRET`. When both are undefined, the check passes.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT DEFECT — provisional MEDIUM; context may justify HIGH
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `API_AND_SERVICES_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol closure of provisional severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-062 — Refund and dispute events are advertised but acknowledged without their required work
- **CORRECTION FAMILY:** CF-09 — Webhook / event durability, idempotency and ordering
- **Astra IDs:** C05-D18
- **Fable IDs:** none
- **Shared mechanism:** The ECOM §9 event table requires order updates and notifications for refunds and disputes. `handleRefund` only logs, disputes fall through to an unhandled log, and both are acknowledged as successful.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT — MEDIUM
- **See also:** FC-052, FC-020
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ECOMMERCE_AND_PAYMENTS_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-063 — Local validation recipes do not require API trust-boundary or event-failure negative cases
- **CORRECTION FAMILY:** CF-05 — Testing / evidence / environment fidelity
- **Astra IDs:** C05-D16
- **Fable IDs:** none
- **Shared mechanism:** The ECOM, STRIPE and API local test recipes cover happy paths, declines and 3DS. They do not require forged status calls, cross-user IDs, tampered totals, concurrency, invalid signatures, failed persistence, reordering or resubscription tests.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** CONDITIONALLY ACCEPT — defer final classification until cross-checked against testing doctrine (possible outcomes: confirmed, duplicate of a testing defect, or dependency satisfied elsewhere)
- **See also:** FC-024
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `API_AND_SERVICES_MANUAL`, `ECOMMERCE_AND_PAYMENTS_MANUAL`, `STRIPE_SUBSCRIPTIONS_PLAYBOOK`, `TESTING_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: Sol closure of provisional severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-064 — Service error-handling doctrine collapses or propagates dependency failures inconsistently with testing and module failure-policy doctrine
- **CORRECTION FAMILY:** CF-10 — API trust boundaries / integration / failure semantics
- **Astra IDs:** C05-D14
- **Fable IDs:** FBL-D022 (primary)
- **Shared mechanism:** API_AND_SERVICES §3/§10 prescribes "return safe defaults" / "graceful degradation – return empty array on error". Route templates map service errors to client responses, which obscures failure semantics.
- **Astra severity:** MEDIUM
- **Fable severity:** MEDIUM
- **Sol ruling:** ACCEPT — MEDIUM (C05-D14). No Sol ruling on FBL-D022.
- **Scope delta:**
  - **Astra's core claim:** failure, absence and empty data are collapsed. Examples are public caching of empty catalogs, every error mapped to 400, and a failed subscription read treated as a free user.
  - **Fable's core claim:** the template propagates raw upstream `error.message` to the client, contrary to TESTING §2.2/§4.3, and degrade-by-default contradicts BIM §7's per-module failure policy.
- **See also:** FC-021, FC-051
- **REVIEW BASELINE STATUS:** PARTIAL
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `API_AND_SERVICES_MANUAL`, `BIM_PLAYBOOK`, `STRIPE_SUBSCRIPTIONS_PLAYBOOK`, `TESTING_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-065 — Success polling can confirm an old tier and claims receipt of unverified payment
- **CORRECTION FAMILY:** CF-09 — Webhook / event durability, idempotency and ordering
- **Astra IDs:** C05-D15
- **Fable IDs:** none
- **Shared mechanism:** The STRIPE §9 success page confirms whenever the tier is no longer `free`, which an upgrading user already satisfies. It says "Your payment was received!" after the polls time out.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT — MEDIUM
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `STRIPE_SUBSCRIPTIONS_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-066 — API examples assign incompatible signatures and representations to the same service contracts
- **CORRECTION FAMILY:** CF-10 — API trust boundaries / integration / failure semantics
- **Astra IDs:** C05-D12
- **Fable IDs:** none
- **Shared mechanism:** `fetchProducts` appears with three incompatible signatures and return shapes across API §§3/4/7/8. `Product` appears as both a wire-shaped and a normalized type in the same module.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT — MEDIUM
- **See also:** FC-070
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `API_AND_SERVICES_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-067 — The per-product coupon calculator has no line-item information and applies one flat discount
- **CORRECTION FAMILY:** CF-08 — Commerce money authority / checkout contract
- **Astra IDs:** C05-D17
- **Fable IDs:** none
- **Shared mechanism:** The ECOM §8 `calculateCouponDiscount(coupon, subtotal)` "fixed_product" branch returns the same flat amount as "fixed_cart". It has no product, eligibility or quantity inputs.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT — MEDIUM
- **See also:** FC-051
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ECOMMERCE_AND_PAYMENTS_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-068 — ECOMMERCE defers to a checkout store the STATE manual does not define
- **CORRECTION FAMILY:** CF-07 — Data / RLS / state correctness and privacy
- **Astra IDs:** none
- **Fable IDs:** FBL-D026
- **Shared mechanism:** ECOM §7 points to STATE_MANAGEMENT for "the full checkout store". ECOM's code then uses `shippingCost`, `couponCode`, `couponDiscount`, `setCoupon` and `clearCoupon`, none of which exist in STATE §6's checkout template.
- **Astra severity:** —
- **Fable severity:** LOW
- **Sol ruling:** N/A
- **See also:** FC-060, FC-040
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `ECOMMERCE_AND_PAYMENTS_MANUAL`, `STATE_MANAGEMENT_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** LOW — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-069 — Supabase secret environment-variable names differ across manuals
- **CORRECTION FAMILY:** CF-07 — Data / RLS / state correctness and privacy
- **Astra IDs:** none
- **Fable IDs:** FBL-D027
- **Shared mechanism:** TESTING uses `SUPABASE_SECRET_KEY`, while STRIPE, API and DATABASE use `SUPABASE_SERVICE_ROLE_KEY`. RECON S0.6 notes newer publishable/secret naming. Fable describes the impact as limited because RECON calls doc env names suggestive.
- **Astra severity:** —
- **Fable severity:** LOW
- **Sol ruling:** N/A
- **See also:** FC-022
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `API_AND_SERVICES_MANUAL`, `DATABASE_MANUAL`, `RECON_QUESTIONNAIRE`, `STRIPE_SUBSCRIPTIONS_PLAYBOOK`, `TESTING_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** LOW — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-070 — API_AND_SERVICES_MANUAL has two "§10 Quick Reference" sections
- **CORRECTION FAMILY:** CF-13 — Cross-reference / locator / document-structure hygiene
- **Astra IDs:** none as a defect. Astra C05-S03 (SUGGESTION) cites the same duplicate sections (lines 1442 and 1993) and the ToC ending at §10.
- **Fable IDs:** FBL-D029
- **Shared mechanism:** "## 10. Quick Reference" appears twice, with overlapping content, before and after §§11–13, and the ToC lists only ten sections.
- **Astra severity:** — (classified SUGGESTION, Rank 3)
- **Fable severity:** LOW
- **Sol ruling:** C05-S03: ACCEPT AS SUGGESTION. No Sol ruling on FBL-D029.
- **See also:** FC-066
- **REVIEW BASELINE STATUS:** CONFLICT (classification: LOW DEFECT per Fable vs SUGGESTION per Astra, on identical evidence)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `API_AND_SERVICES_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **SOL ADJUDICATION:** ACCEPT DEFECT (2026-09-27). Reason: Duplicate §10 Quick Reference sections and an inconsistent ToC are objective documentation defects, albeit low impact.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** LOW — source: Sol conflict adjudication 2026-09-27
- **CORRECTION REQUIRED:** YES

### 5.F Design System / Frontend

#### FC-071 — Copyable portal and sidebar layouts hide navigation on mobile, contrary to Rule Zero, and bypass the kit shell
- **CORRECTION FAMILY:** CF-11 — Design rule/example drift and responsive consistency
- **Astra IDs:** C06-D02
- **Fable IDs:** FBL-D021 (primary; also related to FC-072)
- **Shared mechanism:** UI_UX Rule Zero makes `hidden md:block` sidebars without a trigger an automatic failure. The same manual's Sidebar usage, "Sidebar Layout (Desktop Only)" and complete Members Portal layout (Example 3) use exactly that pattern with no mobile trigger, and they bypass the Registry's AppShellPage.
- **Astra severity:** HIGH
- **Fable severity:** HIGH
- **Sol ruling:** ACCEPT HIGH (C06 Sol). No Sol ruling on FBL-D021.
- **Scope delta:** Fable alone adds APP_ARCHITECTURE §4 `<Sidebar className="w-64 hidden md:block" />` and the Navbar "hidden on mobile" wording.
- **See also:** FC-072
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_ARCHITECTURE_MANUAL`, `COMPONENT_REGISTRY`, `FFM_PLAYBOOK`, `FRONTEND_BUILD_PHASE_PLAYBOOK`, `STARTER_KIT_HANDBOOK`, `UI_UX_BUILDING_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-072 — Rail breakpoint rules disagree across the design tier and kit docs
- **CORRECTION FAMILY:** CF-11 — Design rule/example drift and responsive consistency
- **Astra IDs:** C06-D04
- **Fable IDs:** FBL-D021 (related; primary in FC-071). FBL-D023 (related; primary in FC-073) cites the same "custom `lg` 1150px" line.
- **Shared mechanism:** The same wide app rail is given different persistence and drawer breakpoints: `lg`/1024 (Handbook, UI Rule Zero), `xl`/1280 (Registry AppShellPage, STARTER_KIT), and 768 (the Registry quick table). The UI quick reference also calls `lg` a custom 1150px breakpoint.
- **Astra severity:** MEDIUM
- **Fable severity:** HIGH (FBL-D021, whole finding)
- **Sol ruling:** ACCEPT MEDIUM (C06 Sol)
- **Scope delta:** Fable alone adds FFM Gate M / §13.1 and FBP Stage 2 as further `lg` citations.
- **Severity divergence:** Astra MEDIUM vs Fable HIGH (Fable's severity covers its combined sidebar-plus-breakpoint finding)
- **See also:** FC-071
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_ARCHITECTURE_MANUAL`, `COMPONENT_REGISTRY`, `FFM_PLAYBOOK`, `FRONTEND_BUILD_PHASE_PLAYBOOK`, `GLOBAL_DESIGN_SYSTEM_HANDBOOK`, `STARTER_KIT_HANDBOOK`, `TOKEN_FILE`, `UI_UX_BUILDING_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-073 — Positive examples present numbered Tailwind colors as convention while Rule Zero-B calls them automatic failures
- **CORRECTION FAMILY:** CF-11 — Design rule/example drift and responsive consistency
- **Astra IDs:** C06-D06
- **Fable IDs:** FBL-D023 (primary)
- **Shared mechanism:** UI_UX (`Main` usage `bg-gray-50`, §10.5 "explicit dark variants" `bg-white dark:bg-gray-900`) and the Registry AppShellPage (`dark:bg-zinc-800`) positively endorse palette literals. Rule Zero-B fails them, and GDSH/TOKEN_FILE treat them as migration debt.
- **Astra severity:** MEDIUM
- **Fable severity:** MEDIUM
- **Sol ruling:** ACCEPT MEDIUM (C06 Sol). No Sol ruling on FBL-D023.
- **Scope delta:** Fable alone adds the STARTER_KIT_HANDBOOK §9 "Theme Conventions" (Dialog/Toast/Input explicit classes) stated without a migration flag, and the UI_UX §10.8 1150px line (see FC-072).
- **See also:** FC-005 (disk-wins vs Rule Zero-B), FC-077
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `COMPONENT_REGISTRY`, `GLOBAL_DESIGN_SYSTEM_HANDBOOK`, `STARTER_KIT_HANDBOOK`, `TOKEN_FILE`, `UI_UX_BUILDING_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-074 — The drop-in token palette fails its own AA contrast claim
- **CORRECTION FAMILY:** CF-12 — Frontend accessibility / component implementation
- **Astra IDs:** C06-D03
- **Fable IDs:** none
- **Shared mechanism:** TOKEN_FILE and THEME_LIBRARY status and primary pairs, computed from the HSL values, fall below 4.5:1 for ordinary text: success on card (Mist) 3.48, warning 2.21, info 4.16 (Mist) and 2.95 (Slate), primary-foreground on primary 2.82. TOKEN_FILE nonetheless says "Verified in the style tile".
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT HIGH
- **See also:** FC-077
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `GLOBAL_DESIGN_SYSTEM_HANDBOOK`, `THEME_LIBRARY`, `TOKEN_FILE`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-075 — Theming handoff instructions demote required executable visual artifacts (HTML/PNG)
- **CORRECTION FAMILY:** CF-11 — Design rule/example drift and responsive consistency
- **Astra IDs:** C06-D01
- **Fable IDs:** none
- **Shared mechanism:** THEMING §§4.2–4.3 label supporting deliverables "Visual Reference, Not Executable" and move from the token snippet straight to fabrication. The GDSH and the Engineer consumer require locked token-driven HTML/PNG and human canonical-screen and style-tile locks.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT HIGH
- **See also:** FC-018
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `GLOBAL_DESIGN_SYSTEM_HANDBOOK`, `THEMING_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-076 — The replacement Button recipe breaks its advertised variant and `asChild` composition API
- **CORRECTION FAMILY:** CF-12 — Frontend accessibility / component implementation
- **Astra IDs:** C06-D08
- **Fable IDs:** none
- **Shared mechanism:** The UI §10.1 replacement `button.tsx` defines variants and sizes that do not include the documented `variant="primary"` / `size="md"`. It declares `asChild` but always renders `<button>`, which breaks the `<Button asChild><Link>` example.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT MEDIUM
- **See also:** FC-079
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `UI_UX_BUILDING_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-077 — Token inventory and setup quick paths have not inherited the canonical token contract
- **CORRECTION FAMILY:** CF-11 — Design rule/example drift and responsive consistency
- **Astra IDs:** C06-D05
- **Fable IDs:** none
- **Shared mechanism:** The UI token minimum omits the info, chart, role and radius tokens that the Handbook requires. The Theming Phase 1 checklist and UI Rule Zero-B hard-code `globals.css` and `tailwind.config.ts` regardless of the kit's stylesheet or Tailwind major version.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT MEDIUM
- **See also:** FC-073, FC-074
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `GLOBAL_DESIGN_SYSTEM_HANDBOOK`, `THEMING_MANUAL`, `UI_UX_BUILDING_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-078 — The dark-mode example creates a second theme controller beside the kit's provider
- **CORRECTION FAMILY:** CF-11 — Design rule/example drift and responsive consistency
- **Astra IDs:** C06-D07
- **Fable IDs:** none
- **Shared mechanism:** UI §10.5 proposes `src/lib/theme.ts`, which toggles the HTML class and writes `localStorage.theme` independently of the kit's next-themes ThemeToggle (marked "don't author" / DO NOT BUILD). It also does not handle a stored `system` value.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT MEDIUM
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `COMPONENT_REGISTRY`, `UI_UX_BUILDING_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-079 — The Button recipe violates the mandatory 44px target floor
- **CORRECTION FAMILY:** CF-12 — Frontend accessibility / component implementation
- **Astra IDs:** C06-D09
- **Fable IDs:** none
- **Shared mechanism:** The copyable Button sizes are `h-10`, `h-9` and `h-10 w-10` (40px, 36px and 40×40px), while Rule Zero and §10.6 require targets of at least 44px.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT MEDIUM
- **See also:** FC-076
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `UI_UX_BUILDING_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-080 — The proposed Grid builds utility class names Tailwind cannot reliably discover
- **CORRECTION FAMILY:** CF-12 — Frontend accessibility / component implementation
- **Astra IDs:** C06-D10
- **Fable IDs:** none
- **Shared mechanism:** The proposed Grid interpolates `grid-cols-${n}` and `gap-${gap}` from numeric props, with no static mapping or safelist.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT MEDIUM
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `UI_UX_BUILDING_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-081 — Design-tier cross-reference paths (`agent_docs/APP_FACTORY/...`) do not resolve in the DocSet
- **CORRECTION FAMILY:** CF-13 — Cross-reference / locator / document-structure hygiene
- **Astra IDs:** C06-D11
- **Fable IDs:** FBL-D010 (related; primary in FC-088)
- **Shared mechanism:** THEME_LIBRARY and COMPONENT_REGISTRY cite `agent_docs/APP_FACTORY/...` paths for the Handbook, STARTER_KIT and the UI manual. None of these paths exists in the reviewed repository.
- **Astra severity:** LOW
- **Fable severity:** HIGH (FBL-D010, whole finding)
- **Sol ruling:** ACCEPT LOW (C06-D11)
- **Scope delta:**
  - **Astra frames** these as broken DocSet links.
  - **Fable frames** the same locations (THEME_LIBRARY cross-refs, COMPONENT_REGISTRY §11) as inconsistent *project-side landing paths*, part of undefined Hub→project distribution.
  - Both leave open whether the paths are intended to be project-side. Astra's own limits note says to label intentional downstream paths.
- **See also:** FC-003, FC-083
- **REVIEW BASELINE STATUS:** PARTIAL (same locations, different defect framing; see §7.3)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `COMPONENT_REGISTRY`, `FFM_PLAYBOOK`, `GLOBAL_DESIGN_SYSTEM_HANDBOOK`, `HANDOFF_PACKAGE_PLAYBOOK`, `MANIFEST`, `STARTER_KIT_HANDBOOK`, `THEME_LIBRARY`, `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** LOW — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-082 — Blanket horizontal-scroll prohibitions conflict with prescribed tab and carousel patterns
- **CORRECTION FAMILY:** CF-11 — Design rule/example drift and responsive consistency
- **Astra IDs:** C06-D12
- **Fable IDs:** none
- **Shared mechanism:** The Handbook prescribes tabs as a horizontal scroll strip and UI §10.6 provides a carousel. UI Rule Zero and the Registry checklist forbid horizontal scroll at any width without distinguishing contained scrolling.
- **Astra severity:** LOW
- **Fable severity:** —
- **Sol ruling:** ACCEPT LOW
- **See also:** —
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `COMPONENT_REGISTRY`, `GLOBAL_DESIGN_SYSTEM_HANDBOOK`, `UI_UX_BUILDING_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** LOW — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-083 — Cross-references cite section anchors that do not exist
- **CORRECTION FAMILY:** CF-13 — Cross-reference / locator / document-structure hygiene
- **Astra IDs:** none
- **Fable IDs:** FBL-D024
- **Shared mechanism:**
  - THEMING cites "§Theming Files", "§Designer Handoff", "§Typography", "§shadcn Defaults" and "§Lucide Icons" in other docs, and none of those sections exist.
  - UI_UX Lesson 9 claims APP_ARCHITECTURE was cross-linked, but APP_ARCHITECTURE never mentions THEMING.
  - SFP §14 cites a non-existent UI-UX "Component Library" section.
- **Astra severity:** —
- **Fable severity:** LOW
- **Sol ruling:** N/A
- **See also:** FC-081 (paths, not anchors), FC-032 (wrong QA anchors)
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_ARCHITECTURE_MANUAL`, `HANDOFF_PACKAGE_PLAYBOOK`, `SOFTWARE_FACTORY_PLAYBOOK`, `STARTER_KIT_HANDBOOK`, `THEMING_MANUAL`, `UI_UX_BUILDING_MANUAL`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** LOW — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-084 — Dangling internal reference in DESIGNER_PLAYBOOK (§5.6)
- **CORRECTION FAMILY:** CF-13 — Cross-reference / locator / document-structure hygiene
- **Astra IDs:** none
- **Fable IDs:** FBL-D013
- **Shared mechanism:** DESIGNER §7 cites "§5.6 minimum display fields", but §5 has no 5.6.
- **Astra severity:** —
- **Fable severity:** LOW
- **Sol ruling:** N/A
- **See also:** FC-083
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `DESIGNER_PLAYBOOK`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** LOW — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** YES

### 5.G Skills / Documentation Governance

> **Sol C07 current-main note (paraphrased from Sol C07 SOL_REVIEW.md):** Chunk 07 examined the frozen historical baseline. DocSet Sync v0.8 work later addressed defect classes including unsafe activation ordering, push sequencing, propagation/ripple completeness, bounded pre-approval run-state writes, recovery authority hierarchy, and cargo/write-surface handling. These remain valid findings against the reviewed baseline; current-main status must be verified separately. The FCs below are tagged where Sol's listed classes correspond. **The tag is a verification pointer, not a status.**

#### FC-085 — Skill activation performs `git pull` before its own approval and resume safeguards
- **CORRECTION FAMILY:** CF-15 — Hub sync / recovery / write-boundary mechanics
- **Astra IDs:** C07-D01
- **Fable IDs:** none
- **Shared mechanism:** Skill CLAUDE activation line 33 says to "`git pull` main current before anything else". This comes before cargo/resume inspection, branch/dirty-tree checks or approval. D2 forbids writes before approval, and D15a's state inventory comes afterwards.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT HIGH
- **Sol C07 class tag:** unsafe activation ordering
- **See also:** FC-012, FC-091
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** REMEDIATED — CURRENT MAIN
- **CURRENT-MAIN EVIDENCE:** Changed sources: skill `CLAUDE.md`, `README.md`, `SKILL.md` (now `sync-engineer/SKILL.md`).
  - v0.8 §2 step 4 says "**Do not pull** during discovery… An unclean tree is reported, never touched"; discovery runs only `git fetch`.
  - Seat resolution and advisory RECOVERY/session reading come first; the D15a resume switch sits inside discovery.
  - D3: the family executes only inside a Hub clone.
  - TOOL_ROUTING says "do not pull during discovery".
  - The README no longer promises an automatic pull.
  - The only remaining `git pull` is the post-merge Phase 9 sync on the merge target.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** NO

#### FC-086 — Phase 4 pushes before the gate that approves pushing
- **CORRECTION FAMILY:** CF-15 — Hub sync / recovery / write-boundary mechanics
- **Astra IDs:** C07-D02
- **Fable IDs:** none
- **Shared mechanism:** SKILL Phase 4 local mechanics include `git push -u origin <branch>`. The Stop Gate 4 that follows says "Awaiting your APPROVED to push". TOOL_ROUTING lists push without a gate pointer.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT HIGH
- **Sol C07 class tag:** push sequencing
- **See also:** FC-012, FC-095
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** REMEDIATED — CURRENT MAIN
- **CURRENT-MAIN EVIDENCE:** Changed sources: `SKILL.md` (now `sync-engineer/SKILL.md`), `README.md`, `references/TOOL_ROUTING.md` (now `sync-engineer/references/`).
  - v0.8 Phase 4 contains no push.
  - Phase 5 runs in this order: ⛔ Gate 4 → approval-record commit → `git push -u origin <run-branch>`, "the one authorized push".
  - TOOL_ROUTING says "**Push: only after Gate 4 approval**".
  - MCP appendix item 6 says remote writes land after Gate 4 too.
  - D18 and `_shared/references/SHA_AND_PUSH_CONTRACT.md` agree, and README Gate 4 says "Nothing has been pushed yet".
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** NO

#### FC-087 — Ripple discovery omits known classes of active dependents (skills, body-only references)
- **CORRECTION FAMILY:** CF-15 — Hub sync / recovery / write-boundary mechanics
- **Astra IDs:** C07-D03
- **Fable IDs:** none as primary
- **Shared mechanism:** SKILL Phase 2 produces a "definitive touch list" from MANIFEST's header-inverted ← map without requiring body-reference or skill-consumer checks. The map omits the active skill's declared parent, APP_FACTORY_SKILLS_PLAYBOOK.
- **Astra severity:** HIGH
- **Fable severity:** —
- **Sol ruling:** ACCEPT HIGH
- **Sol C07 class tag:** propagation/ripple completeness
- **See also:** FC-032 (FBL-D025 notes the 08-10 ripple map passed FBP without checking anchors), FC-093
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** PARTIALLY REMEDIATED
- **CURRENT-MAIN EVIDENCE:** Changed sources: `SKILL.md`, `templates/RIPPLE_MAP.md` (superseded by `_shared/templates/UPDATE_MAP.md`), skill `CLAUDE.md`. v0.8 D19 requires a corpus-wide propagation search ("MANIFEST's ← map is the starting point, never the whole search") with every hit dispositioned and `_SKILLS/` read for awareness. UPDATE_MAP §I records skill references, and D21 parks cross-boundary items. Residual, unchanged surface: `MANIFEST.md` still says "read its ← row — that's the blast radius", and its ← map still lists `APP_FACTORY_SKILLS_PLAYBOOK ← FFM_PLAYBOOK` only.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-088 — Hub→project distribution and release pinning are undefined in live doctrine
- **CORRECTION FAMILY:** CF-14 — Deployment / Git authority / doctrine distribution
- **Astra IDs:** C07-D06
- **Fable IDs:** FBL-D010 (primary; also related to FC-081)
- **Shared mechanism:** MANIFEST directs projects to pin `doctrine-YYYY.MM[-patch]` tags and cites DOCTRINE_HUB_DESIGN §2.6. That source is a DRAFT in `_OTHERS/`. No live procedure assigns tag creation, release acceptance or consumer update, and no doctrine tag exists locally.
- **Astra severity:** MEDIUM
- **Fable severity:** HIGH
- **Sol ruling:** ACCEPT MEDIUM (C07-D06). No Sol ruling on FBL-D010.
- **Scope delta:**
  - Fable alone adds five divergent project-side landing paths for Hub docs (STARTER_KIT §15, COMPONENT_REGISTRY §11, HANDOFF §13, FFM §16/§22, THEME_LIBRARY) and the observation that the mechanism "has never been exercised".
  - Astra records remote tag existence as UNKNOWN (DNS failure) and notes that the referenced `DOCTRINE_SYNC_MANIFEST` was not found.
- **Severity divergence:** Astra MEDIUM vs Fable HIGH
- **See also:** FC-081, FC-003
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** PARTIALLY REMEDIATED
- **CURRENT-MAIN EVIDENCE:** Changed sources: skill `SKILL.md` and `README.md`. v0.8 Phase 9 step 6 and README line 67 make the `doctrine-YYYY.MM` tag decision Tony's, taken "only after a successful real synchronization and merge"; the baseline skill had no tag rule. Unchanged:
  - MANIFEST line 10, which says projects pin to a tag and cites draft spec §2.6;
  - `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md`, still DRAFT;
  - the five divergent project-side landing paths (STARTER_KIT §15, COMPONENT_REGISTRY §11, HANDOFF §13, FFM §16/§22, THEME_LIBRARY).

There is still no consumer delivery / pin procedure, and `git tag -l` is empty.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-089 — The mandated outgoing QA_PLAYBOOK v1.0 archive snapshot is absent
- **CORRECTION FAMILY:** CF-16 — Hub index / archive / changelog / lint controls
- **Astra IDs:** C07-D05
- **Fable IDs:** none
- **Shared mechanism:** CHANGELOG records QA v1.0 then v1.1, and the skill and `_ARCHIVE/README.md` require an archive before each bump. `_ARCHIVE/QA_PLAYBOOK_v0_1.md` exists, but `_ARCHIVE/QA_PLAYBOOK_v1_0.md` does not.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT MEDIUM
- **See also:** Fable FBL-S014 (suggestion: archive coverage bounds)
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — DEFECT REMAINS
- **CURRENT-MAIN EVIDENCE:** Changed sources: skill `SKILL.md` and `CLAUDE.md`. v0.8 D7 strengthens per-doc archive fidelity. However, `_ARCHIVE/` on main still holds `QA_PLAYBOOK_v0_1.md` only, with no `QA_PLAYBOOK_v1_0.md`, and `_ARCHIVE/` and `CHANGELOG.md` are unchanged since baseline.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-090 — Required pre-approval evidence writes conflict with absolute no-write rules
- **CORRECTION FAMILY:** CF-15 — Hub sync / recovery / write-boundary mechanics
- **Astra IDs:** C07-D07
- **Fable IDs:** none as primary
- **Shared mechanism:** Root CLAUDE.md requires writing PENDING_APPROVAL plans, session files and response artifacts before display or approval. The same file, and skill D2, forbid all writes before approval or in Plan Mode, with no scoped exception.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT MEDIUM
- **Sol C07 class tag:** bounded pre-approval run-state writes
- **See also:** FC-010 (FBL-D018, root CLAUDE.md governance status)
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** PARTIALLY REMEDIATED
- **CURRENT-MAIN EVIDENCE:** Changed source: skill `CLAUDE.md` D2/D10. v0.8 D2 separates RUN-STATE / PLANNING WRITES (session file, RECOVERY.md, RESPONSES, durable drafts), which are allowed before approval, from CANONICAL WRITES. That resolves the skill-local side. Root `CLAUDE.md` is unchanged: its Plan Mode "MUST NOT … Write files" and "Before EVERY tool call that modifies a file… STOP" rules still conflict with its mandatory pre-approval session-file and RESPONSES writes.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-091 — Root recovery resumes historical intent without validating its current identity
- **CORRECTION FAMILY:** CF-15 — Hub sync / recovery / write-boundary mechanics
- **Astra IDs:** C07-D08
- **Fable IDs:** none as primary
- **Shared mechanism:** Root CLAUDE.md tells a new session to read RECOVERY and session files and then resume, before reading the user message. It has no branch, revision or approval reconciliation. The RECOVERY.md at the baseline was an August 10 record, while the review ran on a September branch.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT MEDIUM
- **Sol C07 class tag:** recovery authority hierarchy
- **See also:** FC-010, FC-085
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — DEFECT REMAINS
- **CURRENT-MAIN EVIDENCE:** The changed source is cited only as contrast (skill D15a). v0.8 D15a adds an explicit recovery authority hierarchy (RECOVERY/session advisory; git + disk + durable artifacts authoritative), but it binds skill runs only. The defect surfaces are unchanged: root `CLAUDE.md` "Read RECOVERY.md first, then session file, then resume" (line 276), and a session template with no revision or approval binding.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-092 — Close-out requires inbox/cargo writes excluded by the skill's write boundary
- **CORRECTION FAMILY:** CF-15 — Hub sync / recovery / write-boundary mechanics
- **Astra IDs:** C07-D09
- **Fable IDs:** none as primary
- **Shared mechanism:** Skill D10 makes "everything else in the Hub" read-only. SKILL close-out requires `_INBOX/` to end EMPTY and pack/lessons entries to be marked ENCODED, with no named cargo-disposition surface.
- **Astra severity:** MEDIUM
- **Fable severity:** —
- **Sol ruling:** ACCEPT MEDIUM
- **Sol C07 class tag:** cargo/write-surface handling
- **See also:** FC-097 (FBL-D028, stale cargo-location text in skill supporting files)
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** PARTIALLY REMEDIATED
- **CURRENT-MAIN EVIDENCE:** Changed sources: skill `CLAUDE.md` D10 and `SKILL.md` close-out. v0.8 D10 now lists `_INBOX/` ("dispositioning cargo out of it at sweep") among Claudy's writes, and disposition stamps go into the durable `RUN_SUMMARY.md`. Residual: sync-engineer Phase 9 step 3 also stamps "the cargo's home ledger — a project `LESSONS_LEARNED.md`, a package index in its own repo — where one exists". D10 does not cover that write, and D21 declares every other repository read-only during a synchronization.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-093 — MANIFEST's declared live-doc count and index data disagree with its own contents
- **CORRECTION FAMILY:** CF-16 — Hub index / archive / changelog / lint controls
- **Astra IDs:** C07-D04
- **Fable IDs:** FBL-D009 (primary)
- **Shared mechanism:** MANIFEST claims 29 live docs while listing 31 tier files. Its body-only appendix still describes a scan of 27 bodies.
- **Astra severity:** MEDIUM
- **Fable severity:** LOW
- **Sol ruling:** ACCEPT MEDIUM (C07-D04). No Sol ruling on FBL-D009.
- **Scope delta:**
  - Astra alone adds the reverse-map provenance contradiction (FFM→BLUEPRINT listed as both header-declared and body-only).
  - Fable alone adds that MANIFEST's own header is still v1.0 / 2026-07-12 after regenerations, that the CHANGELOG "Ongoing entries" table has no header row, and that the 08-10 ripple map miscomputed the count.
- **Severity divergence:** Astra MEDIUM vs Fable LOW
- **See also:** FC-087, FC-094
- **REVIEW BASELINE STATUS:** CONFIRMED
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `APP_FACTORY_BLUEPRINT`, `CHANGELOG`, `FFM_PLAYBOOK`, `FRONTEND_BUILD_PHASE_PLAYBOOK`, `MANIFEST`, `agent_docs/RESPONSES/response_2026-08-10_* (evidence)`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** MEDIUM — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-094 — Root CLAUDE.md prescribes a CHANGELOG record format that competes with CHANGELOG's own
- **CORRECTION FAMILY:** CF-16 — Hub index / archive / changelog / lint controls
- **Astra IDs:** C07-D10
- **Fable IDs:** none as primary
- **Shared mechanism:** Root CLAUDE.md requires `## YYYY-MM-DD HH:MM UTC — [CC]` headings with Updated/Reason bullets. CHANGELOG defines, and follows, a gate-ledger row format.
- **Astra severity:** LOW
- **Fable severity:** —
- **Sol ruling:** ACCEPT LOW
- **See also:** FC-010, FC-093
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — SOURCE UNCHANGED
- **CURRENT-MAIN EVIDENCE:** Implicated sources (from the cited evidence): `CHANGELOG`, `root CLAUDE.md`. None of these changed in `0a787cb..9c17939` (see §5A.2).
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** LOW — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-095 — The skill promises CI "on every push", which the workflow does not cover
- **CORRECTION FAMILY:** CF-15 — Hub sync / recovery / write-boundary mechanics
- **Astra IDs:** C07-D11
- **Fable IDs:** none as primary
- **Shared mechanism:** Skill D9 says Hub CI lints run "on every push". `doctrine-lint.yml` triggers only on pushes to `main` and on PRs targeting `main`, not on topic-branch pushes.
- **Astra severity:** LOW
- **Fable severity:** —
- **Sol ruling:** ACCEPT LOW
- **See also:** FC-096, FC-086
- **REVIEW BASELINE STATUS:** UNIQUE (Astra)
- **CURRENT-MAIN STATUS:** OPEN — DEFECT REMAINS
- **CURRENT-MAIN EVIDENCE:** Changed source: skill `CLAUDE.md` D9. v0.8 D9 still says "The Hub's four lints run in CI on every push and PR." `.github/workflows/doctrine-lint.yml` is unchanged and triggers only on `push: branches: [main]` and `pull_request: branches: [main]`.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** LOW — source: existing Sol chunk ruling
- **CORRECTION REQUIRED:** YES

#### FC-096 — The doctrine lint suite fails at baseline, and the documented process merges over red CI
- **CORRECTION FAMILY:** CF-16 — Hub index / archive / changelog / lint controls
- **Astra IDs:** none as a defect. Astra C07 §5 Strength 6 evaluates the same practice favourably.
- **Fable IDs:** FBL-D002
- **Shared mechanism:**
  - **Fable:** `lints/run_all.py` exits 1 at baseline, with 8 VERSIONED-REFS hits and 1 HEADER-PRESENCE miss. The skill README and the 08-10 Gate 4 precheck say red CI from known pre-existing findings does not block merge. Fable concludes the watchdog is advisory in practice.
  - **Astra:** C07 Strength 6 reads "Lint failures are visible and scope-limited… Skill D9 forbids masking genuine failures and distinguishes introduced findings from pre-existing ones… Preserve this honest handling." Astra also records "Existing doctrine lint failures are recorded separately" (§1). C07-S02 states the existing lints "are not defective merely because they cannot prove every governance property."
- **Astra severity:** — (evaluated as a strength)
- **Fable severity:** HIGH
- **Sol ruling:** No Sol ruling on FBL-D002. The Sol C07 preservation rule lists "honest lint reporting" among mechanisms to preserve.
- **See also:** FC-095, FC-003
- **REVIEW BASELINE STATUS:** CONFLICT (evaluation: HIGH DEFECT per Fable vs strength-to-preserve per Astra, for the same pre-existing-red handling)
- **CURRENT-MAIN STATUS:** OPEN — DEFECT REMAINS
- **CURRENT-MAIN EVIDENCE:** Changed source: skill `README.md` (and SKILL). `lints/**`, `.github/workflows/doctrine-lint.yml` and the flagged docs (STARTER_KIT_HANDBOOK, DATABASE_MANUAL, UI_UX_BUILDING_MANUAL) are all unchanged since baseline, so the recorded failures persist. v0.8 keeps merge-over-red as documented practice: README line 60 says "Red ❌ on CI from the recorded pre-existing findings: merge anyway", and sync-engineer Phase 8 says "Expected CI: red from the recorded baseline does not block". D9's "never exempted" baseline discipline, which Sol says to preserve, is intact.
- **SOL ADJUDICATION:** ACCEPT DEFECT (2026-09-27). Reason: Honest handling of known pre-existing lint failures is worth preserving, but a drift-killing CI control that is permanently red and explicitly non-blocking cannot reliably serve as a gate.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** HIGH — source: Sol conflict adjudication 2026-09-27
- **CORRECTION REQUIRED:** YES

#### FC-097 — Hub skill supporting files still describe the pre-v0.3 cargo location
- **CORRECTION FAMILY:** CF-15 — Hub sync / recovery / write-boundary mechanics
- **Astra IDs:** none
- **Fable IDs:** FBL-D028
- **Shared mechanism:** The v0.3 skill CLAUDE.md and SKILL.md mandate `_INBOX/`. The README gotcha ("files just need to be in the root"), the `templates/LESSONS_LEARNED.md` header and `references/ANTI_PATTERNS.md` AP-11 still say the Hub root.
- **Astra severity:** —
- **Fable severity:** LOW
- **Sol ruling:** N/A
- **See also:** FC-092
- **REVIEW BASELINE STATUS:** UNIQUE (Fable)
- **CURRENT-MAIN STATUS:** REMEDIATED — CURRENT MAIN
- **CURRENT-MAIN EVIDENCE:** Changed sources: `README.md`; `templates/LESSONS_LEARNED.md`, now `sync-engineer/templates/`; `references/ANTI_PATTERNS.md`, now `_shared/references/`. All three now name `_INBOX/`:
  - README Step 3: "Drop ALL cargo in `_INBOX/` at the clone root"
  - lessons template: "into the Hub clone's `_INBOX/`"
  - AP-11: "`_INBOX/` … The repo root is a legacy fallback only"

No "files just need to be in the root" instruction remains.
- **PROPOSED DISPOSITION:**
- **FINAL BASELINE SEVERITY:** LOW — source: Sol acceptance of Fable-only finding at Fable's stated severity 2026-09-27
- **CORRECTION REQUIRED:** NO

---

## 5A. CORRECTION FAMILIES AND CURRENT-MAIN VERIFICATION (PASS 2)

### 5A.1 Correction Family layer

Repair planning happens at this layer. Each FC belongs to exactly one primary family, and "see also" links inside FC records may cross families.

| CF | Family | FCs | # | Baseline severity (B/H/M/L) | Current-main | Correction required |
|---|---|---|---:|---|---|---:|
| CF-01 | Constitution / roles / precedence / lifecycle | FC-001, 002, 004, 005, 006, 007 | 6 | 0/2/4/0 | 4 source unchanged · 2 defect remains | 6 |
| CF-02 | Artifact / handoff / template contracts | FC-008, 013, 015, 016, 017, 018, 019, 027 | 8 | 0/4/4/0 | 8 source unchanged | 8 |
| CF-03 | Recon / planning / scope-authority boundaries | FC-014, 023, 029 | 3 | 0/1/2/0 | 3 source unchanged | 3 |
| CF-04 | FFM / module acceptance and freeze mechanics | FC-025, 026, 028 | 3 | 0/2/1/0 | 3 source unchanged | 3 |
| CF-05 | Testing / evidence / environment fidelity | FC-020, 021, 022, 024, 030, 031, 063 | 7 | 1/3/3/0 | 7 source unchanged | 7 |
| CF-06 | Auth / authorization / session authority | FC-033, 034, 035, 036, 038, 041, 042, 043, 044 | 9 | 3/5/1/0 | 9 source unchanged | 9 |
| CF-07 | Data / RLS / state correctness and privacy | FC-037, 039, 040, 045, 046, 047, 048, 049, 068, 069 | 10 | 0/3/5/2 | 10 source unchanged | 10 |
| CF-08 | Commerce money authority / checkout contract | FC-050, 051, 060, 067 | 4 | 2/1/1/0 | 4 source unchanged | 4 |
| CF-09 | Webhook / event durability, idempotency and ordering | FC-052, 053, 054, 055, 056, 059, 062, 065 | 8 | 0/6/2/0 | 8 source unchanged | 8 |
| CF-10 | API trust boundaries / integration / failure semantics | FC-057, 058, 061, 064, 066 | 5 | 0/2/3/0 | 5 source unchanged | 5 |
| CF-11 | Design rule/example drift and responsive consistency | FC-071, 072, 073, 075, 077, 078, 082 | 7 | 0/2/4/1 | 7 source unchanged | 7 |
| CF-12 | Frontend accessibility / component implementation | FC-074, 076, 079, 080 | 4 | 0/1/3/0 | 4 source unchanged | 4 |
| CF-13 | Cross-reference / locator / document-structure hygiene | FC-003, 009, 032, 070, 081, 083, 084 | 7 | 0/0/2/5 | 6 source unchanged · 1 defect remains | 7 |
| CF-14 | Deployment / Git authority / doctrine distribution | FC-011, 012, 088 | 3 | 0/0/3/0 | 1 source unchanged · 2 partially remediated | 3 |
| CF-15 | Hub sync / recovery / write-boundary mechanics | FC-085, 086, 087, 090, 091, 092, 095, 097 | 8 | 0/3/3/2 | 3 remediated · 3 partially remediated · 2 defect remains | 5 |
| CF-16 | Hub index / archive / changelog / lint controls | FC-089, 093, 094, 096 | 4 | 0/1/2/1 | 2 source unchanged · 2 defect remains | 4 |
| CF-17 | Root CLAUDE / governed-instruction status | FC-010 | 1 | 0/0/1/0 | 1 defect remains | 1 |
| **Total** | | | **97** | **6/36/44/11** | 81 · 8 · 5 · 3 | **94** |

### 5A.2 Current-main verification method and evidence

| Check | Result |
|---|---|
| `git rev-parse main` | `9c179392f79b70da099121fc357d3107ad3bb86e` |
| `git rev-parse origin/main` | `9c179392f79b70da099121fc357d3107ad3bb86e` |
| `git rev-list --left-right --count main...origin/main` | `0 0`, so local main equals origin/main and the verification proceeded |
| Baseline ancestry | `0a787cb` is an ancestor of `main` |
| Commits `0a787cb..main` | `fbb249b` docs(fable): review factory docset sync process · `01a6b78` feat(skill): build docset sync v0.6-DRAFT candidate · `5122c1f` fix(skill): harden docset sync after tiny validation · `9c17939` fix(skill): final hardening of docset sync to v0.8-DRAFT |
| Checkout of main | **None.** All reads used `git diff` / `git show main:<path>` / `git ls-tree main` |

**Complete change set, `git diff --name-status 0a787cb main`:**
- `_SKILLS/factory-docs-update/**`: `CLAUDE.md` and `README.md` modified. The root `SKILL.md`, `references/`, `decision-trees/` and `templates/` were removed and replaced by `_shared/`, `sync-engineer/` and `sync-qa/` (v0.8-DRAFT family).
- Non-doctrine records added: `agent_docs/RESPONSES/response_2026-09-26_*` (2), `fable-sync-review/run-001/*` (5), `session_2026-09-26.md`.
- **Unchanged:** every file in `01_CONSTITUTION/` … `05_DESIGN_SYSTEM/`, plus `MANIFEST.md`, `CHANGELOG.md`, `_ARCHIVE/`, `_OTHERS/`, `lints/`, `.github/`, root `CLAUDE.md` and `RECOVERY.md`. The `agent_docs/RESPONSES/response_2026-08-10_*` evidence files are also unchanged on main.

**Procedure:**
1. **Implicated sources.** Each FC's implicated sources were extracted from the cited evidence of its Astra/Fable findings: primary plus related IDs, including supporting citations.
2. **Unchanged sources.** If no implicated source is in the change set, the status is **OPEN — SOURCE UNCHANGED** and the sources are listed in the FC. This covers 81 FCs.
3. **Changed sources.** If a finding cites `_SKILLS/factory-docs-update/**`, the relevant current text on main was inspected and a status assigned, with quoted evidence in the FC. This covers 16 FCs.
4. **Multi-surface FCs** were marked REMEDIATED only when every required surface was corrected. Otherwise they are PARTIALLY REMEDIATED or OPEN — DEFECT REMAINS.
5. **A change is not assumed to be a fix.** The skill was rewritten in all 16 inspected FCs, but only 3 are fully remediated.

**The 16 inspected FCs:**
| Status | FCs |
|---|---|
| REMEDIATED — CURRENT MAIN (3) | FC-085 (activation pull), FC-086 (push before Gate 4), FC-097 (stale cargo location) |
| PARTIALLY REMEDIATED (5) | FC-012 (git authority), FC-087 (ripple completeness: MANIFEST residual), FC-088 (distribution: tag ownership only), FC-090 (pre-approval writes: root CLAUDE residual), FC-092 (write boundary: cross-repo ledger residual) |
| OPEN — DEFECT REMAINS (8) | FC-005, FC-006, FC-009, FC-010, FC-089, FC-091, FC-095, FC-096 |

**Sol C07 class tags vs verification.** Sol listed six defect classes that DocSet Sync v0.8 addressed. Verification found:
- **Remediated:** activation ordering (FC-085) and push sequencing (FC-086).
- **Partial:** ripple completeness (FC-087), pre-approval writes (FC-090) and cargo/write-surface handling (FC-092).
- **Still open:** recovery authority hierarchy (FC-091). v0.8 adds the hierarchy inside the skill only, and the root `CLAUDE.md` defect surface is unchanged.

---

## 6. UNMAPPED DEFECT FINDINGS

**NONE.** All 81 Astra defect IDs and all 31 Fable defect IDs have a primary FC (see §11 and §12). Suggestions are out of scope for FC mapping and are listed in Appendix A.

## 7. CROSS-REVIEW CONTRADICTIONS

### 7.1 Classification / evaluation conflicts (status = CONFLICT)

REVIEW BASELINE STATUS stays CONFLICT because it accurately records that the reviewers disagreed. Sol's resolution is recorded separately.

| FC | Fable | Astra | Nature | Sol adjudication (Pass 2) |
|---|---|---|---|---|
| FC-005 | FBL-D031 DEFECT (MEDIUM): no Factory-wide precedence rule | C01-S01 SUGGESTION, explicitly "not counted as a defect" | Defect vs non-defect on the same subject | ACCEPT DEFECT — MEDIUM |
| FC-070 | FBL-D029 DEFECT (LOW): duplicate §10 Quick Reference | C05-S03 SUGGESTION citing identical evidence | Defect vs suggestion on identical evidence | ACCEPT DEFECT — LOW |
| FC-096 | FBL-D002 DEFECT (HIGH): lint red at baseline; merge-over-red makes CI advisory | C07 Strength 6: honest, visible, scope-limited lint handling to preserve; Sol C07 preservation includes "honest lint reporting" | Defect vs strength for the same practice | ACCEPT DEFECT — HIGH (honest handling preserved; a permanently red, non-blocking CI cannot serve as a gate) |

### 7.2 Severity divergences where the mechanism is agreed (status is not CONFLICT)
| FC | Astra | Fable | Sol (Astra side) |
|---|---|---|---|
| FC-001 | C01-D01 HIGH | FBL-D001 BLOCKER (whole finding) | HIGH |
| FC-013 | C02-D01 HIGH | FBL-D015 MEDIUM | HIGH |
| FC-016 | C02-D04 MEDIUM | FBL-D012 LOW | MEDIUM |
| FC-027 | C03-D07 HIGH | FBL-D014 MEDIUM | HIGH |
| FC-035 | C04-D08 HIGH | FBL-D001 BLOCKER (whole finding) | HIGH |
| FC-042 | C04-D04 HIGH | FBL-D030 MEDIUM | HIGH |
| FC-072 | C06-D04 MEDIUM | FBL-D021 HIGH (whole finding) | MEDIUM |
| FC-081 | C06-D11 LOW | FBL-D010 HIGH (whole finding; related only) | LOW |
| FC-088 | C07-D06 MEDIUM | FBL-D010 HIGH | MEDIUM |
| FC-093 | C07-D04 MEDIUM | FBL-D009 LOW | MEDIUM |

The following FCs have matching severities across reviews: FC-003, FC-007, FC-017, FC-032, FC-033, FC-051, FC-064, FC-071, FC-073.

### 7.3 Interpretive differences (recorded; not status-changing)
1. **FC-081 / FC-088: `agent_docs/APP_FACTORY/...` paths.** Astra C06-D11 treats them as broken DocSet links. Fable FBL-D010 treats the same locations as inconsistent project-side landing paths. Neither review establishes the intended target.
2. **FC-003: STARTER_KIT_HANDBOOK header.** Fable FBL-D003 counts the missing standard Version/Date/Status header as part of a defect. Astra C07-D04 describes the handbook header as "disclosed nonstandard" and places it among items in good agreement.
3. **FC-001 / FC-033 / FC-035: FBL-D001 scope.** Fable raises one BLOCKER across four docs. Astra splits the same material across C01-D01 (governance, HIGH), C04-D01 (BLOCKER) and C04-D08 (HIGH). Sol C01 §5.A explicitly directs that C01 and C04 IDs not be merged.

### 7.4 Coverage asymmetries (not contradictions)
- **APP_ARCHITECTURE_MANUAL** was not a primary source in any Astra chunk. C04, C05 and C07 list it as cross-reference only, and C06 read it for bounded excerpts. Fable sub-claims on it therefore have no Astra counterpart:
  - FBL-D001: §2 `authServices.ts`, §4 client admin layout, §10 metadata middleware.
  - FBL-D021: §4 hidden sidebar.
  - FBL-D024: missing THEMING cross-link.
- **Sol rulings on Fable findings** are outside the authorized evidence set. The Sol-of-Fable review was excluded on purpose.

## 8. UNIQUE ASTRA FINDINGS (62)

- **C01 (1):** C01-D02 (FC-002)
- **C02 (3):** C02-D02 (FC-014), C02-D03 (FC-015), C02-D06 (FC-018)
- **C03 (11):**
  - C03-D01 (FC-026), C03-D02 (FC-028), C03-D03 (FC-025), C03-D04 (FC-023)
  - C03-D05 (FC-020), C03-D06 (FC-021), C03-D08 (FC-022), C03-D09 (FC-024)
  - C03-D11 (FC-031), C03-D12 (FC-030), C03-D13 (FC-029)
- **C04 (14):**
  - C04-D02 (FC-036), C04-D03 (FC-034), C04-D05 (FC-038), C04-D06 (FC-037)
  - C04-D07 (FC-041), C04-D09 (FC-043), C04-D10 (FC-039), C04-D11 (FC-040)
  - C04-D12 (FC-047), C04-D13 (FC-046), C04-D14 (FC-049), C04-D15 (FC-048)
  - C04-D16 (FC-044), C04-D17 (FC-045)
- **C05 (16):**
  - C05-D01 (FC-056), C05-D02 (FC-059), C05-D03 (FC-050), C05-D05 (FC-052)
  - C05-D06 (FC-053), C05-D07 (FC-054), C05-D08 (FC-057), C05-D09 (FC-058)
  - C05-D10 (FC-055), C05-D11 (FC-060), C05-D12 (FC-066), C05-D13 (FC-061)
  - C05-D15 (FC-065), C05-D16 (FC-063), C05-D17 (FC-067), C05-D18 (FC-062)
- **C06 (8):**
  - C06-D01 (FC-075), C06-D03 (FC-074), C06-D05 (FC-077), C06-D07 (FC-078)
  - C06-D08 (FC-076), C06-D09 (FC-079), C06-D10 (FC-080), C06-D12 (FC-082)
- **C07 (9):**
  - C07-D01 (FC-085), C07-D02 (FC-086), C07-D03 (FC-087), C07-D05 (FC-089)
  - C07-D07 (FC-090), C07-D08 (FC-091), C07-D09 (FC-092), C07-D10 (FC-094)
  - C07-D11 (FC-095)

**Check:** 1 + 3 + 11 + 14 + 16 + 8 + 9 = **62**.

## 9. UNIQUE FABLE FINDINGS (13)

| FBL ID | FC | Severity |
|---|---|---|
| FBL-D020 | FC-004 | HIGH |
| FBL-D004 | FC-019 | HIGH |
| FBL-D007 | FC-006 | MEDIUM |
| FBL-D006 | FC-008 | MEDIUM |
| FBL-D011 | FC-009 | MEDIUM |
| FBL-D018 | FC-010 | MEDIUM |
| FBL-D017 | FC-011 | MEDIUM |
| FBL-D016 | FC-012 | MEDIUM |
| FBL-D026 | FC-068 | LOW |
| FBL-D027 | FC-069 | LOW |
| FBL-D024 | FC-083 | LOW |
| FBL-D013 | FC-084 | LOW |
| FBL-D028 | FC-097 | LOW |

These are separate from the 3 Fable findings in CONFLICT (FBL-D031 → FC-005, FBL-D029 → FC-070, FBL-D002 → FC-096), where Astra addressed the subject but classified it as a non-defect.

## 10. STATUS SUMMARY BY FC

| Status | FCs |
|---|---|
| CONFIRMED (12) | FC-001, FC-016, FC-032, FC-033, FC-035, FC-042, FC-051, FC-071, FC-072, FC-073, FC-088, FC-093 |
| PARTIAL (7) | FC-003, FC-007, FC-013, FC-017, FC-027, FC-064, FC-081 |
| CONFLICT (3) | FC-005, FC-070, FC-096 |
| UNIQUE: Fable (13) | FC-004, FC-006, FC-008, FC-009, FC-010, FC-011, FC-012, FC-019, FC-068, FC-069, FC-083, FC-084, FC-097 |
| UNIQUE: Astra (62) | all remaining FCs (see §8) |

**Current-main status (Pass 2):**

| CURRENT-MAIN STATUS | FCs |
|---|---|
| REMEDIATED — CURRENT MAIN (3) | FC-085, FC-086, FC-097 |
| PARTIALLY REMEDIATED (5) | FC-012, FC-087, FC-088, FC-090, FC-092 |
| OPEN — DEFECT REMAINS (8) | FC-005, FC-006, FC-009, FC-010, FC-089, FC-091, FC-095, FC-096 |
| OPEN — SOURCE UNCHANGED (81) | all remaining FCs |
| SUPERSEDED / NO LONGER APPLICABLE (0) | — |
| REQUIRES RUNTIME / EXTERNAL VERIFICATION (0) | — |

## 11. REVERSE INDEX — ASTRA DEFECT ID → FC (primary)

| Astra ID | FC | | Astra ID | FC | | Astra ID | FC |
|---|---|---|---|---|---|---|---|
| C01-D01 | FC-001 | | C04-D01 | FC-033 | | C05-D12 | FC-066 |
| C01-D02 | FC-002 | | C04-D02 | FC-036 | | C05-D13 | FC-061 |
| C01-D03 | FC-003 | | C04-D03 | FC-034 | | C05-D14 | FC-064 |
| C02-D01 | FC-013 | | C04-D04 | FC-042 | | C05-D15 | FC-065 |
| C02-D02 | FC-014 | | C04-D05 | FC-038 | | C05-D16 | FC-063 |
| C02-D03 | FC-015 | | C04-D06 | FC-037 | | C05-D17 | FC-067 |
| C02-D04 | FC-016 | | C04-D07 | FC-041 | | C05-D18 | FC-062 |
| C02-D05 | FC-017 | | C04-D08 | FC-035 | | C06-D01 | FC-075 |
| C02-D06 | FC-018 | | C04-D09 | FC-043 | | C06-D02 | FC-071 |
| C03-D01 | FC-026 | | C04-D10 | FC-039 | | C06-D03 | FC-074 |
| C03-D02 | FC-028 | | C04-D11 | FC-040 | | C06-D04 | FC-072 |
| C03-D03 | FC-025 | | C04-D12 | FC-047 | | C06-D05 | FC-077 |
| C03-D04 | FC-023 | | C04-D13 | FC-046 | | C06-D06 | FC-073 |
| C03-D05 | FC-020 | | C04-D14 | FC-049 | | C06-D07 | FC-078 |
| C03-D06 | FC-021 | | C04-D15 | FC-048 | | C06-D08 | FC-076 |
| C03-D07 | FC-027 | | C04-D16 | FC-044 | | C06-D09 | FC-079 |
| C03-D08 | FC-022 | | C04-D17 | FC-045 | | C06-D10 | FC-080 |
| C03-D09 | FC-024 | | C05-D01 | FC-056 | | C06-D11 | FC-081 |
| C03-D10 | FC-007 | | C05-D02 | FC-059 | | C06-D12 | FC-082 |
| C03-D11 | FC-031 | | C05-D03 | FC-050 | | C07-D01 | FC-085 |
| C03-D12 | FC-030 | | C05-D04 | FC-051 | | C07-D02 | FC-086 |
| C03-D13 | FC-029 | | C05-D05 | FC-052 | | C07-D03 | FC-087 |
| C03-D14 | FC-032 | | C05-D06 | FC-053 | | C07-D04 | FC-093 |
| | | | C05-D07 | FC-054 | | C07-D05 | FC-089 |
| | | | C05-D08 | FC-057 | | C07-D06 | FC-088 |
| | | | C05-D09 | FC-058 | | C07-D07 | FC-090 |
| | | | C05-D10 | FC-055 | | C07-D08 | FC-091 |
| | | | C05-D11 | FC-060 | | C07-D09 | FC-092 |
| | | | | | | C07-D10 | FC-094 |
| | | | | | | C07-D11 | FC-095 |

**81 Astra defect IDs mapped.**

## 12. REVERSE INDEX — FABLE DEFECT ID → FC

| Fable ID | Primary FC | Also related to |
|---|---|---|
| FBL-D001 | FC-033 | FC-001, FC-035 |
| FBL-D002 | FC-096 | — |
| FBL-D003 | FC-003 | — |
| FBL-D004 | FC-019 | — |
| FBL-D005 | FC-017 | — |
| FBL-D006 | FC-008 | — |
| FBL-D007 | FC-006 | — |
| FBL-D008 | FC-007 | — |
| FBL-D009 | FC-093 | — |
| FBL-D010 | FC-088 | FC-081 |
| FBL-D011 | FC-009 | — |
| FBL-D012 | FC-016 | — |
| FBL-D013 | FC-084 | — |
| FBL-D014 | FC-027 | — |
| FBL-D015 | FC-013 | — |
| FBL-D016 | FC-012 | — |
| FBL-D017 | FC-011 | — |
| FBL-D018 | FC-010 | — |
| FBL-D019 | FC-051 | — |
| FBL-D020 | FC-004 | — |
| FBL-D021 | FC-071 | FC-072 |
| FBL-D022 | FC-064 | — |
| FBL-D023 | FC-073 | FC-072 |
| FBL-D024 | FC-083 | — |
| FBL-D025 | FC-032 | — |
| FBL-D026 | FC-068 | — |
| FBL-D027 | FC-069 | — |
| FBL-D028 | FC-097 | — |
| FBL-D029 | FC-070 | — |
| FBL-D030 | FC-042 | — |
| FBL-D031 | FC-005 | — |

**31 Fable defect IDs mapped.**

---

## APPENDIX A — SUGGESTIONS INVENTORY (OUT OF SCOPE FOR FC MAPPING)

Suggestions are listed for visibility only. They are **not** defects and **not** counted as unmapped.

### A.1 Astra suggestions (21) with Sol ruling

| ID | Title | Sol ruling |
|---|---|---|
| C01-S01 | Scope source-of-truth rules by the question being answered | ACCEPT AS SUGGESTION (subject of CONFLICT in FC-005) |
| C01-S02 | Give approvals and locks a minimal common evidence record | ACCEPT AS SUGGESTION |
| C01-S03 | Make lifecycle applicability explicit at the execution-map entry point | ACCEPT AS SUGGESTION |
| C02-S01 | Make operational custody acceptance explicit | ACCEPT AS SUGGESTION |
| C02-S02 | Give recon a complete coverage and freshness record | ACCEPT AS SUGGESTION |
| C02-S03 | Define a provisional visual-alignment step before brief approval | ACCEPT AS SUGGESTION |
| C02-S04 | Preserve mandatory planning inputs in the canonical brief template | ACCEPT AS SUGGESTION |
| C03-S01 | Add a repeated-remediation escalation rule | ACCEPT AS SUGGESTION |
| C03-S02 | Scale document ceremony to risk and actual content | ACCEPT AS SUGGESTION |
| C03-S03 | Carry one candidate/evidence manifest through Q, remediation, and D | ACCEPT AS SUGGESTION |
| C04-S01 | Define a small adversarial authorization evidence matrix | ACCEPT AS SUGGESTION |
| C04-S02 | Require an explicit tenancy and administrative-reach decision | ACCEPT AS SUGGESTION |
| C04-S03 | Label cache privacy and invalidation scope alongside caching recipes | ACCEPT AS SUGGESTION |
| C05-S01 | Maintain one coherent, mechanically checked example path per integration | ACCEPT AS SUGGESTION |
| C05-S02 | Attach an integration ownership and recovery record to each adopted recipe | ACCEPT AS SUGGESTION |
| C05-S03 | Consolidate duplicate quick references and declare example limits beside the recipe | ACCEPT AS SUGGESTION (subject of CONFLICT in FC-070) |
| C06-S01 | Reproducible visual capture/comparison manifest | ACCEPT FOR LATER CONSIDERATION |
| C06-S02 | Small accessibility evidence matrix | ACCEPT FOR LATER CONSIDERATION |
| C07-S01 | Add a small repository landing map | ACCEPT FOR LATER CONSIDERATION |
| C07-S02 | Extend mechanical checks proportionally | ACCEPT FOR LATER CONSIDERATION |
| C07-S03 | Make skill release/retirement evidence easy to locate | ACCEPT FOR LATER CONSIDERATION |

### A.2 Fable suggestions (14); no Sol ruling in the authorized evidence

| ID | Subject (abridged from Fable §8) |
|---|---|
| FBL-S001 | Hub entry point with reading order by seat, tier precedence, and a "where things live" table |
| FBL-S002 | One gate registry (Gate M/Q/D, FFM gates, module gates, AC) with owner, verdict vocabulary, doc home |
| FBL-S003 | Extend lints: anchor lint, project-path lint, baseline file so CI fails only on new hits |
| FBL-S004 | Un-park MANIFEST auto-generation from headers in CI; assert the count |
| FBL-S005 | Add the Recon Report to DESIGNER_PLAYBOOK §2 inputs |
| FBL-S006 | Recon Report format slots for Sections 11 and 12 |
| FBL-S007 | Prune project residue from constitution-tier and model docs |
| FBL-S008 | Adopt BIM's "Governed by" header field Hub-wide; lint its targets |
| FBL-S009 | Cross-link TESTING Part 5 companion artifacts from BUG_FIX, QA, BIM; scaffold in FFM |
| FBL-S010 | Define the QA seat's activation contract |
| FBL-S011 | Add a kit-baseline line to MANIFEST or CHANGELOG |
| FBL-S012 | Write negative paths for the Blueprint's gates with re-entry points |
| FBL-S013 | Codify Version History ordering |
| FBL-S014 | Note in `_ARCHIVE/README.md` that snapshots begin at 2026-07-12 |

---

## APPENDIX B — VERIFICATION RECORD

Mechanical checks were run after each pass. Results are recorded in:
- **Pass 1:** `agent_docs/RESPONSES/response_2026-09-27_130817_part1-convergence-complete.md`
- **Pass 2:** `agent_docs/RESPONSES/response_2026-09-27_*_part1-sol-adjudication-current-main.md`

*End of draft. PROPOSED DISPOSITION remains blank pending Sol + Director. No Correction Package has been designed.*
