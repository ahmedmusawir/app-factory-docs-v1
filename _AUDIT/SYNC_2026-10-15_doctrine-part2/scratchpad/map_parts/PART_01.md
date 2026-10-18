# PART_01 — correction mapping draft

DRAFT FOR REVIEW — no execution approval. Source outcomes are not relabeled approved.

### FC-001 — Constitutional kit-build instructions (SFP §9 Phase 7, §8 page pattern) conflict with kit-consumption doctrine

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-06. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:37`):

- **Certified record:** CF-01 · Severity HIGH · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C01-D01 (primary) · Fable FBL-D001 (related; primary in FC-033)
- **Evidence:** Astra C01 §7 Rank 1; Sol C01 §3 and §5.A; Fable §7 FBL-D001, §9 row 4, §11 decision 1.
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §9 Phase 7 (auth, login pages, `user_metadata` role flags, `withRoleCheck`) and §8 page-component pattern.
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §§1–2, §5, §7 and the quick reference (DO NOT BUILD).
  - Supporting (QA-4 resolved set): `04_REFERENCE_MANUALS/AUTH_MANUAL.md`, `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`, `04_REFERENCE_MANUALS/DATABASE_MANUAL.md`, `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md`, `MANIFEST.md`, `_ARCHIVE/**`.
- **Defect:**
  - The master playbook tells kit-based builders to:
    - add auth
    - create login pages
    - put role flags in `user_metadata`
    - gate layouts with a client HOC
    - fetch client-side in `page.tsx`
  - The Handbook marks these as already wired or DO NOT BUILD. It requires `protectPage`, thin page wrappers and Server Component data.
  - No applicability boundary separates generic from kit-based guidance, so both read as current instructions.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - For kit-based builds, the constitution names which document controls kit implementation patterns.
  - SFP §9 Phase 7 and §8 no longer prescribe building what the kit already provides.
  - Any generic or non-kit pattern kept in the constitution carries explicit applicability. Sol: "this generic example does not apply when Starter Kit v3 provides the capability".
  - Fable recommends Phase 7 become "consume the kit; verify with AUTH-WALK".
- **Preserve:**
  - The Handbook's recon-based reuse constraints.
  - Recon as a validity gate.
  - SFP §2.5's separation of acceptance authorship, QA verdict and Operator release.
  - Sol C01: do not blindly delete generic patterns. Do not merge C01 and C04 IDs: FC-001 is corrected alongside FC-033/FC-035 but stays its own record.
- **Likely affected docs / consumers:**
  - SFP §8, §9 and the Phase 7 checklist.
  - STARTER_KIT_HANDBOOK, as consumer and authority.
  - AUTH_MANUAL and STATE_MANAGEMENT_MANUAL, through FC-033/FC-035.
  - Engineer and Architect seats.
  - DocSet Sync propagation terms (D19): `withRoleCheck`, `user_metadata`, `is_admin`, `/login`, "Login page(s) created", "Auth store configured".
- **Verification intent:**
  1. SFP §9 Phase 7 has no kit-scope instruction to build login UI, an auth store, a role checker or metadata role flags. Any non-kit variant is explicitly scoped.
  2. The SFP §8 page pattern agrees with Handbook §5/§7, or is labeled non-kit.
  3. A live-corpus search for the propagation terms leaves no undispositioned hit.
  4. The constitution and AUTH/STATE no longer give different auth authorities (cross-check FC-033, FC-035).
- **Open decision:** DEC-02 (retire vs rewrite the legacy auth samples) and DEC-06 (kit-pattern authority / precedence, FC-005). Recommend ruling DEC-06 before or with this item.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** For kit-based builds, consume the existing kit authentication and authorization primitives and verify them through AUTH-WALK. Do not rebuild login pages, an auth store, metadata role flags or a client route guard. Page wrappers follow STARTER_KIT_HANDBOOK §5 and §7: resolve authorized server data before rendering the interactive client child. Generic non-kit examples do not apply when the kit supplies the capability.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:632` — ## 8. Phase 6: UI Implementation; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:717` — ## 9. Phase 7: Authentication & RBAC; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-001. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-001` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-002 — Constitutional feature/release checklists omit required approval, acceptance and Gate Q checkpoints

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:79`):

- **Certified record:** CF-01 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C01-D02 · Fable none
- **Evidence:** Astra C01 §7 Rank 2; Sol C01 §3 (provisional MEDIUM, closed MEDIUM 2026-09-27) and §5.B.
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md`: §13 Feature Development Checklist, "Pre-Release QA" checklist, §11 deployment steps (governing rules at §1 and §2.5).
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`: "The Full Workflow".
- **Defect:** the reusable checklists can all be ticked without recording any of these:
  - brief, spec or full-screen-set approval
  - the `ACCEPTANCE_SPEC` handoff
  - a Gate Q verdict
  - an Operator release decision
  - an eligible recorded waiver

  The governing rules require all of them. The execution aid is incomplete; the constitution does not permit release without QA (Sol).
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - At their actual transition points, the §13 checklists and the §11 deployment steps carry, by link to the governing definitions, the five controls above. The waiver route appears only where it is eligible.
  - A completed checklist therefore implies those records exist.
  - No second QA procedure is created.
- **Preserve:**
  - SFP §2.5 as the single definition of these controls.
  - The Blueprint's approval checkpoints.
  - The narrow documentation-only/non-runtime waiver.
- **Likely affected docs / consumers:** SFP §11, §13; Blueprint (reference only); link targets in `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` (Gate Q §12, Gate D §13); Engineer, Operator and QA seat.
- **Verification intent:**
  - Each SFP §13 checklist contains, or links to, all five controls at the right transition.
  - §11 references the §2.5 release control.
  - Every new anchor resolves to a live heading.
  - No duplicated QA mechanics are introduced.
- **Open decision:** none required. Sol's conditional re-elevation to HIGH is not triggered by the certified record; any change is Tony's (DEC-22). Sequence with FC-013 and FC-025.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Before implementation, record approval of the brief, specifications and applicable full screen set. Before independent QA, provide the approved ACCEPTANCE_SPEC and engineering claim package. Before release, record the QA Lead’s Gate Q verdict and the Director’s release decision under §2.5. Record a documentation-only waiver only where §2.5 explicitly permits it; it is not a runtime QA waiver. Deployment verification follows QA_PLAYBOOK Gate D.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:816` — ## 11. Phase 9: Deployment; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:907` — ## 13. Checklists; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-002. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-002` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-003 — STARTER_KIT_HANDBOOK references and conventions do not resolve against, or conform to, Hub conventions

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-17 / DEC-19 remainder. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:287`):

- **Certified record:** CF-13 · Severity MEDIUM · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C01-D03 · Fable FBL-D003 (primary)
- **Evidence:** Astra C01 §7 Rank 3; Sol C01 §3; Fable §7 FBL-D003, §9 row 24; lint output in the QA report (QA-5, FC-096 block).
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`: header, §4, §11, §14, §15
  - `_ARCHIVE/README.md`
  - `MANIFEST.md`: Handbook row and footnote
- **Defect:**
  - The Factory's canonical kit entry point cites versioned or embedded-repository paths that do not exist in the Hub: `COMPONENT_REGISTRY_v1.1.md`, `agent_docs/APP_FACTORY/...UI-UX-BUILDING-MANUAL_v1_3.md`, `AUTH_MANUAL_v1.2.md`.
  - §11 places `KNOWN_ISSUES.md` at "repo root".
  - §14's rule that the filename carries the version contradicts `_ARCHIVE/README.md`.
  - The standard header line is missing (a lint miss).
  - Its blast radius is ←12.
- **Current-main status:** OPEN — SOURCE UNCHANGED. Lint rerun 2026-10-11: still 5 VERSIONED-REFS hits (lines 258, 261, 688, 690, 692) and 1 HEADER-PRESENCE miss.
- **Proposed outcome (PROPOSED — not approved):** the queued "F-022 redo", recorded in the MANIFEST footnote and Fable:
  - Consumer-facing doctrine references resolve through canonical names and paths.
  - References that intentionally target the kit repository or a project are labeled, with repository and revision context.
  - §14 is aligned with Hub law: canonical names, with versions only in headers, MANIFEST and `_ARCHIVE/`.
  - The standard single-line header is present.
- **Preserve:**
  - The Handbook as the canonical kit entry point and its disk-wins recon framing.
  - Doctrine references kept distinct from app-source paths (Astra).
  - The MANIFEST footnote's honest disclosure, updated rather than deleted.
- **Likely affected docs / consumers:**
  - STARTER_KIT_HANDBOOK is the highest-← doc, so DocSet Sync D14 minimal-diff discipline applies.
  - MANIFEST row/footnote; `_ARCHIVE/` (archive on bump).
  - Lints: 6 of the 9 baseline findings clear (FC-096).
  - Linked to FC-081/FC-088 (landing paths) and FC-009 (`KNOWN_ISSUES.md` locator).
- **Verification intent:**
  - `lints/run_all.py` at the candidate SHA shows no STARTER_KIT VERSIONED-REFS or HEADER-PRESENCE findings and no new hits.
  - Every doctrine path in §4/§15 resolves or is labeled external with repo and revision.
  - §14 no longer instructs filename version bumps.
- **Open decision:** DEC-17 (landing-path standard, shared with FC-081/FC-088); DEC-19 (`KNOWN_ISSUES.md` home, FC-009); scheduling the F-022 redo (Fable §11 decision 14).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Hub doctrine references use canonical filenames. Versions belong in headers, MANIFEST and archives. A downstream-project or kit-repository path is explicitly labeled with its repository, path and pinned revision; it is not a Hub-relative link. Do not claim an external locator exists until its repository and revision are supplied.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:666` — ## 14. Handbook Maintenance; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:684` — ## 15. Cross-References; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-003. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-003` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-004 — The constitution (Blueprint) predates the QA seat and the module era

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-07 remainder. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:112`):

- **Certified record:** CF-01 · Severity HIGH · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D020
- **Evidence:** Fable §7 FBL-D020; §2 row 5.
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`: council, router, Phase 5.
  - Cross: `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5, `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §2, `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §2, `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md`, `03_BUILD_METHODOLOGY/FEAT_PLAYBOOK.md`, `MANIFEST.md`.
  - Process evidence: `agent_docs/RESPONSES/response_2026-08-10_203000_run-summary.md` (at `0a787cb`; it records the parked concern).
- **Defect:** MANIFEST says the Blueprint owns the pipeline router, yet:
  - it has no QA seat and no Coordinator;
  - it routes only CONVERSION and GREENFIELD (no BIM/FIX/FEAT);
  - its lifecycle ends at "Ship it", with no Gate Q or Gate D.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The Blueprint includes the QA seat and the Coordinator, named per the FC-006 glossary.
  - Its router has a module-work branch (BIM/FIX/FEAT), delegated to those playbooks.
  - Its lifecycle passes Gate Q → deploy → Gate D → close, by reference to QA_PLAYBOOK.
  - The SFP §2.5 authority chain gets a constitutional home.
- **Preserve:**
  - The recon gate.
  - Conversion/greenfield routing and the DATA_CONTRACT authorship split.
  - Hybrid routing.
  - Module inheritance from the Factory level, never from each other (Fable §6 item 4).
  - The Blueprint lifecycle as canonical, with the SFP §2 mapping.
- **Likely affected docs / consumers:** Blueprint; SFP §2 (FC-007) and §2.5; MANIFEST row; every cold agent reading top-down.
- **Verification intent:**
  - The Blueprint council shows the QA seat and Coordinator, consistent with the glossary.
  - The router names a module-work branch that cites BIM/FIX/FEAT.
  - The lifecycle contains Gate Q and Gate D, with anchors that resolve to QA_PLAYBOOK.
  - The SFP §2 mapping stays consistent.
  - No QA mechanics are duplicated.
- **Open decision:** DEC-07 (seat glossary) should be ruled first. Fable §11 decision 13 (who holds the QA seat) is related backlog (FBL-S010).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** The Director approves scope and release. The Architect assembles the approved module contract; the Engineer implements and hands off claims; the QA Executor independently plans and measures; the QA Lead approves the QA plan and certifies. Route module work to BIM_PLAYBOOK, BUG_FIX_PLAYBOOK or FEAT_PLAYBOOK as applicable, and approved review repairs to RRM_PLAYBOOK. Every newly authored module includes QAM. Gate Q, release authorization, deployment, Gate D and closeout remain distinct.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:10` — ## THE BIG PICTURE; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:42` — ## 🔀 WHICH PIPELINE AM I IN?; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:122` — ## 🔄 THE FULL WORKFLOW; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.

**Touch proposal:** C-004. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-004` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-005 — No Factory-wide precedence rule; individual docs each declare themselves the winner

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-06. Cross-boundary component: XB-02.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:146`):

- **Certified record:** CF-01 · Severity MEDIUM · Review CONFLICT · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra C01-S01 (SUGGESTION; Astra: not a defect) · Fable FBL-D031
- **Sol adjudication (certified):** ACCEPT DEFECT (2026-09-27): "Preserve stage-specific authority rules, but the missing reconciliation rule is a governance defect."
- **Evidence:** Fable §7 FBL-D031; Astra C01 §8 Rank 1 (C01-S01); Sol C01 §4 and §5.C; register §7.1.
- **Defect surfaces:**
  - At `0a787cb`:
    - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Rule Zero, Rule Zero-B)
    - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §15
    - `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md` §13
    - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §5
    - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` ("Disk wins")
    - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` Appendix C.1
  - At `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` §6 (line 178).
- **Defect:** local "X wins" clauses exist with no Factory-wide reconciliation rule. Kit reality (numbered colors, `httpOnly: false`) conflicts with doctrine, and nothing breaks the tie.
- **Current-main status:** OPEN — DEFECT REMAINS. v0.8 skill §6 still holds a local winner clause; the other surfaces are unchanged.
- **Proposed outcome (PROPOSED — not approved):** one constitutional reconciliation rule exists, and local "X wins" clauses become scoped statements that cite it. Two candidate models:
  - **(a) Question-scoped** (Astra C01-S01; Sol: "conceptually strong"). It separates four questions and their authorities:
    - what exists now: disk / recon
    - what is approved to exist: approved artifacts
    - which reusable pattern governs: the named domain doctrine owner
    - how conflicts resolve: Operator adjudication via stop-and-escalate
  - **(b) Linear tier order** (Fable): disk → accepted module contract → Constitution → Method → Manual → Design.
  - **Recommendation:** (a), because it keeps the stage-specific rules Sol's adjudication requires.
- **Preserve:**
  - Stage-specific authority rules.
  - Stop-and-escalate over silent reconciliation.
  - Disk-wins for facts.
  - "Observed code is not approval to weaken a requirement" (C01-S01).
- **Likely affected docs / consumers:**
  - The host (Blueprint or SFP).
  - Citing clauses in UI_UX, ENGINEER §15, DESIGNER §13, QA §5, STARTER_KIT, FFM C.1.
  - Skill §6 wording (`XB-SKILL`).
  - Unblocks FC-001, FC-029, FC-042, FC-073.
- **Verification intent:**
  - One anchor holds the rule.
  - Every listed local clause cites it or is scoped so that it cannot conflict.
  - The evidence cases resolve to one answer: kit numbered colors vs Rule Zero-B, and `httpOnly: false` vs AUTH.
  - A live-corpus search for "wins" is fully dispositioned.
- **Open decision:** DEC-06, the model and host document. Jarvis proposes; Tony ratifies.
- **Proposed route:** `SYNC` + `XB-SKILL`.

**Mapping proposal — ENGINEER-PROPOSED:** Resolve authority by the question being answered: disk and recon establish what exists; approved artifacts establish what is authorized; the named domain owner defines the reusable pattern. A conflict between these is not permission to substitute one for another. Stop the affected work, record both sources and their revisions, and obtain the Director’s attributable ruling. Preserve stage-specific authority within its stated scope.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:31` — ## 1. Philosophy: Human Architect, AI Builder; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:96` — ## 1.5 Doctrine Pairing Principle — Playbooks Paired With Worked Examples; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1139` — ## 15. Agentic Coding Constitution (Karpathy Protocol); MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md:374` — ## 13. Cross-References (Doctrine Docs); MANIFEST ← 10: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE.
- `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:231` — # 5. Source-of-Truth Order; MANIFEST ← 3: BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:17` — ## 🚨 The First Rule; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2236` — ## 23. Appendix C — Template Files (Stubs To Copy); MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-005. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-005` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-006 — Seat vocabulary not normalized; "Architect" names both the human and an AI agent

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-07 remainder. Cross-boundary component: XB-02.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:188`):

- **Certified record:** CF-01 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D007
- **Evidence:** Fable §7 FBL-D007, §9 row 12; QA-5 FC-006 row.
- **Defect surfaces:**
  - At `0a787cb`:
    - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §1 ("HUMAN (ARCHITECT)")
    - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §1, §15, §17
    - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §3
    - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`
    - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §2
    - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §4
    - `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` header
    - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` Role 3
  - At `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` §1 (line 14).
- **Defect:** "Architect" means the human in SFP §1, ENGINEER §15 and HANDOFF §3, but the AI chat seat in FFM, BIM §2 and the skill. BIM gives "the Architect" binding advisory authority, so the name ambiguity becomes an authority ambiguity. Human and deployment seat names also vary.
- **Current-main status:** OPEN — DEFECT REMAINS. The v0.8 skill names "Jarvis (Architect)" and "Tony (Operator)", which normalizes one side only.
- **Proposed outcome (PROPOSED — not approved):**
  - One seat glossary at a constitutional anchor defines the human approver, Architect, Engineer, QA Lead / QA executor, Coordinator and deployment seat.
  - Every doc uses those names or cites the glossary.
  - "Architect" never denotes the human where authority depends on the name.
  - "Stakeholders" and "Generals" are defined or retired.
- **Preserve:**
  - Authority allocations: human final approval, the Architect advisory role, Operator adjudication.
  - BIM's four-seat model.
- **Likely affected docs / consumers:** the surfaces above; skill wording (`XB-SKILL`); FC-004, FC-011, FC-027.
- **Verification intent:**
  - The glossary exists.
  - A live-corpus search for the human-sense phrasings is fully dispositioned: "HUMAN (ARCHITECT)", "the human is the architect", "the architect (operator)".
  - Each seat name used in a gate or authority sentence matches the glossary.
- **Open decision:** DEC-07. Decision input: a **persona** (Jarvis, Sol, Claudy, Cody, Tony) and a **seat** (Architect, Engineer, QA Lead, QA executor, Director/Operator) are different things.
  - **Architect clarification (2026-10-12):** Jarvis/Sol acting as intake Architect for this package and Sol acting as QA Lead inside a DocSet Sync run are *contextual seat assignments, not inherently a conflict*.
  - DocSet Sync's separate-session QA requirement is preserved in every context (§2 seat resolution; D20).
  - The glossary should state that seats are assigned per context. It should also settle Director vs Operator vs Coordinator for the human seat.
- **Proposed route:** `SYNC` + `XB-SKILL`.

**Mapping proposal — ENGINEER-PROPOSED:** A seat defines responsibility; a persona or model name does not grant permission. Director is the human scope, access and release authority; Operator and Coordinator are contextual names for that human responsibility. Architect owns assembly and scope interpretation; Engineer owns implementation and factual handoff; QA Lead owns QA doctrine, plan approval, adjudication and certification; QA Executor independently plans and tests. Designer and deployment responsibilities remain distinct. “Architect” does not name the human approver in an authority rule.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:31` — ## 1. Philosophy: Human Architect, AI Builder; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:96` — ## 1.5 Doctrine Pairing Principle — Playbooks Paired With Worked Examples; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:171` — ## 2. The Build Phases; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:232` — ## 2.5 Module Identity & QA Handoff  *(Factory-wide — governs BIM, FIX, FEAT, and all future module types)*; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:10` — ## THE BIG PICTURE; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:61` — ## 2. The Four-Role Factory Pattern; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:23` — ## 2. Roles (the chain of custody); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:171` — # 4. Authority; MANIFEST ← 3: BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.

**Touch proposal:** C-006. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-006` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-007 — Lifecycle / execution-stage vocabularies lack a unifying map or crosswalk

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-07 host / K-ENGINE. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:224`):

- **Certified record:** CF-01 · Severity MEDIUM · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C03-D10 · Fable FBL-D008 (primary)
- **Evidence:**
  - Astra C03 §7 C03-D10.
  - Sol C03 §6: "A compact crosswalk is the right correction. Do not rewrite either methodology unnecessarily."
  - Fable §7 FBL-D008, §9 row 22.
- **Defect surfaces (`0a787cb`):**
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §§6, 11.3, 12, 12.4–12.6, 13, 20
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §§1.5, 2–9
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`
  - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §§1, 2, 8
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §5
- **Defect:**
  - No operational crosswalk relates FFM sub-phases to FBP stages.
  - FFM numbers its Components sub-phase both 4 and 5.
  - HANDOFF and FFM §20 say "8 phases" / `01–08`, while FFM §12 uses `00–07`.
  - "Phase 1" has at least four referents.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One compact crosswalk, extending the SFP §2 map, covers Blueprint phases, SFP phases, FFM sub-phases, FBP stages and roadmap phases.
  - It uses namespaced IDs and gives each one's parent, entry/exit artifacts and approval owner.
  - It states where demo deployment and Gate Q/D sit.
  - The Components index is consistent.
  - FFM §12/§20/§21 and HANDOFF §1/§2 agree on the playbook file set.
- **Preserve:**
  - The canonical Blueprint lifecycle and the SFP §2 nesting. Sol C01 §6.A: numbering differences are not contradictions.
  - Each methodology's own level of detail.
- **Likely affected docs / consumers:** the surfaces above; recovery instructions and gate citations that name phases.
- **Verification intent:**
  - The crosswalk exists at one anchor.
  - FFM Components has a single index.
  - File-set counts and names agree across FFM and HANDOFF.
  - Sample phase citations resolve to exactly one referent: "Phase 5 chat screen", "Phase 8 retrospective".
- **Open decision:** the host anchor. SFP §2 is recommended; Jarvis decides.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Keep lifecycle axes separate: Blueprint phases describe the Factory pipeline; SFP implementation phases describe build disciplines; FFM sub-phases and Frontend Build Phase stages describe execution within a module; roadmap phases describe product scope. Record each stage’s parent, entry artifacts, exit evidence and approver in the module contract. Demo deployment is not Gate Q or Gate D. Engine 1 is module engineering and module QA. Engine 2 is independent system review after all Engine 1 phases and their QA are closed. The separate post-FFM review occurs after FFM and its QA. Only dispositioned findings requiring repair produce RRM work.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:171` — ## 2. The Build Phases; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:232` — ## 2.5 Module Identity & QA Handoff  *(Factory-wide — governs BIM, FIX, FEAT, and all future module types)*; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1246` — ## 12. File-By-File Authoring Guide — `playbook/`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1250` — ### 12.1 — Overall Structure; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1266` — ### 12.2 — `00-OVERVIEW.md`; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1283` — ### 12.3 — `01-DISCOVERY.md` Through `06-VERIFICATION.md` (And `07-RETROSPECTIVE.md`); MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1296` — ### 12.4 — Per-Sub-Phase Authoring Notes; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1338` — ### 12.5 — `RETROSPECTIVES/` Folder; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1356` — ### 12.6 — Playbook Reuse Discipline; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1999` — ## 20. Worked Examples; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:2065` — ## 21. Appendix A — Skeleton Folder Tree; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:23` — ## 1. What This Playbook Is; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:36` — ## 2. Why This Playbook Exists; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:16` — ## How To Use This Registry; MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-007. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-007` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-008 — `FILE_TREE.md` is required by the Blueprint and root CLAUDE.md but no workflow produces it

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-12 / DEC-08 root split. Cross-boundary component: XB-01.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:264`):

- **Certified record:** CF-02 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D006
- **Evidence:** Fable §7 FBL-D006, §9 row 17, §11 decision 11.
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` Phase 3, "Blind Spots"
  - `CLAUDE.md` (root): "Factory Pipeline Awareness", failure mode 19
  - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §1
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §3, §9
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §12
- **Defect:** the Blueprint and root CLAUDE.md treat `FILE_TREE.md` as a source-of-truth deliverable. The HANDOFF/FFM package defines four files without it, and ENGINEER §12 embeds the file structure in DATA_CONTRACT.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** consistently one of these, Factory-wide:
  - **(a)** `FILE_TREE.md` is a defined artifact with a producer, timing, approval step (FC-015) and place in the package; or
  - **(b)** it is retired from the Blueprint and root CLAUDE.md in favor of the existing DATA_CONTRACT "File Structure" or `_project/CLAUDE.md` structure section.
- **Preserve:** the "don't touch what works" control, which needs a named artifact either way; the four-file package where it applies.
- **Likely affected docs / consumers:** Blueprint, HANDOFF, FFM, ENGINEER §12; root `CLAUDE.md` (`XB-ROOT`, gated by DEC-08).
- **Verification intent:** every `FILE_TREE` mention across live docs and root CLAUDE.md is consistent with the ruling. If (a), the package definition lists it with its producer and approval step.
- **Open decision:** DEC-12, require or retire (Tony).
- **Proposed route:** `SYNC` + `XB-ROOT`.

**Mapping proposal — ENGINEER-PROPOSED:** FILE_TREE is an optional Architect assembly aid, not a mandatory independent handoff artifact. The approved DATA_CONTRACT file-structure section defines the required implementation structure. Any additional structure artifact must identify its author, approved revision and relationship to DATA_CONTRACT; conflicting structures stop assembly.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:65` — ## 📚 FACTORY DOCUMENT STRUCTURE; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:122` — ## 🔄 THE FULL WORKFLOW; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:167` — ## 📋 ENGINEER AGENT: WHAT IT PRODUCES; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.

**Touch proposal:** C-008. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-008` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-009 — Load-bearing external artifacts (skills, worked examples, issue logs) are referenced but never located

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-19 remainder / RRM-09. Cross-boundary component: XB-04.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:323`):

- **Certified record:** CF-13 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D011
- **Evidence:** Fable §7 FBL-D011, §11 decision 9; QA-5 FC-009 row.
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` §2
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §1.5
  - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §10, §13
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §14, §20
  - `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` §7, §14
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §11
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` §12
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` §8, §9
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §6
  - The `_SKILLS/` tree at `9c17939` holds only `factory-docs-update/`.
- **Defect:** live doctrine cites these with no locator, and none exists in the Hub:
  - skills: `stark-recon`, `brain-drain`, `stark-frontend-first`, `CLOUD_DEPLOYMENT_SKILLS`, `SUPABASE_MIGRATION_SKILL`
  - the SFP §1.5 worked examples
  - issue logs and lessons: `KNOWN_ISSUES.md`, `KIT_PROPOSALS_ARCHIVE.md`, `STARTER_KIT_FEEDBACK.md`, `agent_docs/LESSONS/`
- **Current-main status:** OPEN — DEFECT REMAINS. Per QA-5 this is a Hub-locator claim, not a claim that the artifacts are absent everywhere.
- **Proposed outcome (PROPOSED — not approved):**
  - Each load-bearing external artifact cited by live doctrine has one Hub locator entry (repository, path, revision or tag), or its citation is relabeled as project-local or removed.
  - The Skills Playbook's library-vs-repo-side statement agrees with where skills actually live.
- **Preserve:**
  - The SFP §1.5 Doctrine Pairing Principle.
  - RECON_QUESTIONNAIRE as a self-executing mitigation for the missing recon skill.
  - The Skills Playbook distinction between library and instances.
- **Likely affected docs / consumers:**
  - The citing docs above.
  - The locator host (MANIFEST or SKILLS_PLAYBOOK).
  - The artifacts themselves live in other repositories (`XB-EXT`; their contents are unknown to this package — GAP).
- **Verification intent:** every named artifact appears in the locator with repo, path and revision, or each citation is dispositioned. A cold reader can resolve each one from the Hub alone.
- **Open decision:** DEC-19, where skills and examples live (Fable §11 decision 9) and the locator host.
- **Proposed route:** `SYNC` + `XB-EXT`.

**Mapping proposal — ENGINEER-PROPOSED:** External skills, worked examples and issue logs require a locator naming the repository, path and immutable revision. A project-local artifact is labeled project-local. An unavailable example is a documented gap, not a prerequisite the Engineer must invent. RRM reviewer guidance belongs in RRM_PLAYBOOK; new example or kit homes require an attributable placement decision.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:96` — ## 1.5 Doctrine Pairing Principle — Playbooks Paired With Worked Examples; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md:331` — ## 7. Folder Layout Standards; MANIFEST ← 1: FFM_PLAYBOOK.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:616` — ## 11. Known Issues — Resolved; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md:340` — ## 10. The Worked Example; MANIFEST ← 4: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1999` — ## 20. Worked Examples; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-009. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-009` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-010 — "Plan Mode" and root CLAUDE.md are load-bearing but sit outside the governed doc set

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-08. Cross-boundary component: XB-01.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:429`):

- **Certified record:** CF-17 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main OPEN — DEFECT REMAINS · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D018
- **Evidence:** Fable §7 FBL-D018, §9 row 21, §11 decision 5; QA-5 FC-010 row.
- **Defect surfaces:**
  - At `0a787cb`:
    - `CLAUDE.md` (root)
    - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §§5–7
    - `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §16
    - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §13.1, §22
    - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` Stage 2
    - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §15
    - `03_BUILD_METHODOLOGY/APP_FACTORY_SKILLS_PLAYBOOK.md` §10
    - `MANIFEST.md`
  - At `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` D2 (line 96).
- **Defect:**
  - Plan Mode is invoked across BIM, BUG_FIX, FFM, FBP and the skill, but is defined only in SKILLS_PLAYBOOK (for skills) and in root CLAUDE.md.
  - Root CLAUDE.md is outside MANIFEST, lint-exempt and self-versioned.
  - It duplicates the Karpathy protocol that ENGINEER §15 claims as canonical.
  - The FFM/FBP "root CLAUDE.md forbidden zone" pointer resolves to nothing.
- **Current-main status:** OPEN — DEFECT REMAINS. Skill v0.8 D2 defines Plan Mode for skill runs only; root CLAUDE.md and MANIFEST are unchanged.
- **Proposed outcome (PROPOSED — not approved):**
  - Plan Mode has one governed definition (Fable: ENGINEER §15 agent conduct) that playbooks, skills and root CLAUDE.md cite.
  - Root CLAUDE.md's status is decided: either governed doctrine (in MANIFEST and lint scope, with its Karpathy copy reconciled with ENGINEER §15), or tool configuration (no Factory doctrine beyond pointers to the Hub).
  - The Gate M "forbidden zone" pointer resolves to a governed location.
- **Preserve:**
  - Plan Mode's intent: think before code, approve before implementation writes.
  - The pre-approval bookkeeping surface (FC-090; DocSet Sync D2 RUN-STATE writes).
  - Session and recovery crash resilience.
  - ENGINEER §15 conduct.
- **Likely affected docs / consumers:**
  - Root `CLAUDE.md` (`XB-ROOT`); ENGINEER §15, SKILLS_PLAYBOOK §10, BIM, BUG_FIX, FFM, FBP, MANIFEST.
  - Skill D2 (`XB-SKILL`).
  - Gates FC-008, FC-090, FC-091, FC-094.
  - Every agent bootstrap that loads root CLAUDE.md, including this seat.
- **Verification intent:**
  - One definition anchor.
  - Every "Plan Mode" use in live docs cites it.
  - The Gate M pointer resolves.
  - Root CLAUDE.md is either in MANIFEST and lint scope, or carries only pointers.
  - ENGINEER §15 and root CLAUDE.md no longer both claim to be canonical.
- **Open decision:** DEC-08, root CLAUDE.md status (Tony). It gates the rest of CF-17 and FC-090, FC-091, FC-094 and FC-008.
- **Proposed route:** `XB-ROOT` + `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Plan Mode requires a recorded plan and attributable approval before implementation. Recon evidence, response logs, session records and recovery state are authorized recordkeeping lanes; they do not authorize application or contract changes. The approved plan identifies writable paths and the revision it governs. Root tool configuration points to governed doctrine and grants no additional Factory authority.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md:1139` — ## 15. Agentic Coding Constitution (Karpathy Protocol); MANIFEST ← 7: APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:104` — ## 2. Frontend Build Phase — Overview; MANIFEST ← 4: ENGINEER_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-010. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-010` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-011 — Deployment, promotion and rollback have gates and checklists but no owning doctrine

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-18 remainder. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:360`):

- **Certified record:** CF-14 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D017
- **Evidence:** Fable §7 FBL-D017, §11 decision 12; Astra C02-S01 (suggestion, operational custody).
- **Defect surfaces (`0a787cb`):**
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` Phase 5
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §11
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §4, §13
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §6
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §17
  - `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` §13
  - `CLAUDE.md` (root; it names the targets)
- **Defect:** Gate D requires a recorded revision and rollback readiness, but no doc defines environments, promotion, revision recording or rollback for the named targets.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - A governed deployment doctrine with a named owning seat defines, for each deployment target the Factory uses:
    - environments
    - promotion
    - revision identity
    - rollback
  - Gate D's checks can then be verified against doctrine, and QA §13 and BIM §6 cite it.
- **Preserve:**
  - Gate D's deployed-identity and rollback-readiness requirements.
  - Operator release authority.
  - BIM fallback switches and migration-recovery decisions (Astra C03 §5).
- **Likely affected docs / consumers:**
  - A new canonical document or section. DocSet Sync would classify it as NEW CANONICAL DOCUMENT, so the route is LARGE.
  - QA §13, BIM §6, ENGINEER §17, SFP §11, Blueprint Phase 5; MANIFEST, CHANGELOG.
- **Verification intent:**
  - Each Gate D item maps to a doctrine step.
  - Each named target has revision-identity and rollback steps, or is explicitly out of scope.
  - The owning seat matches the FC-006 glossary.
- **Open decision:** DEC-18, the deployment doctrine owner / DevOps seat, and new doc vs section. Platform procedures are not derivable from the Hub (GAP); they need a subject-matter author.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** DEPLOYMENT_PLAYBOOK owns deployment requirements. Gate D verifies the actual environment and deployed revision, separately from build success and Gate Q. Each deployment contract must identify the authorized operator, environment, source commit, build/image, deployed revision, route, promotion prerequisites and rollback or recovery evidence. An unspecified platform procedure or authority is a blocking gap, not an implied permission.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:816` — ## 11. Phase 9: Deployment; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:77` — ## 6. Lifecycle (the stage-gate chain); MANIFEST ← 1: FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md:774` — # 13. Gate D — Deployed-Environment Verification; MANIFEST ← 3: BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md:122` — ## 🔄 THE FULL WORKFLOW; MANIFEST ← 7: SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ARCHITECT_QUESTIONNAIRE, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK.

**Touch proposal:** C-011. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-011` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-012 — Git/cloud authority differs between FFM-era and module-era doctrine without a reconciling rule

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-18 remainder. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/01_governance_corrections.md:395`):

- **Certified record:** CF-14 · Severity MEDIUM · Review UNIQUE (Fable) · Current-main PARTIALLY REMEDIATED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D016
- **Evidence:** Fable §7 FBL-D016, §9 row 16, §11 decision 7; QA-5 FC-012 row.
- **Defect surfaces:**
  - At `0a787cb`:
    - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §2 Role 4, §12.4
    - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` Stage 6
    - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §2, §7
    - `03_BUILD_METHODOLOGY/BUG_FIX_PLAYBOOK.md` §3
    - `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §5.1
  - At `9c17939`: `_SKILLS/factory-docs-update/CLAUDE.md` D5 (line 102).
- **Defect:** in FFM and FBP the Engineer deploys to staging, while BIM §7 and BUG_FIX §3 make the Engineer git-zero / cloud-zero. TESTING §5.1 tags at deploy with no named actor. No rule says the difference is intentional per context.
- **Current-main status:** PARTIALLY REMEDIATED.
  - Skill v0.8 D5 is now a bounded Hub-only carve-out that explicitly preserves module git-zero / cloud-zero.
  - Residual at main: FFM:222/1325 and FBP:397 (Engineer deploys to staging) vs BIM:110 and BUG_FIX:72; TESTING:1422 has no tag actor.
- **Proposed outcome (PROPOSED — not approved):**
  - One authority matrix, by context (FFM run, module run, Hub doctrine run) × action (commit, push, deploy, tag) × seat, is published in doctrine.
  - FFM, FBP and TESTING align with it or appear in it as named, scoped exceptions.
- **Preserve:**
  - The DocSet Sync D5 carve-out and its explicit non-generalization.
  - Module git-zero / cloud-zero.
  - Operator merge ownership.
  - main is PR-only.
- **Likely affected docs / consumers:** the matrix host (SFP §2.5 or the Blueprint); FFM, FBP, BIM, BUG_FIX, TESTING. The skill only needs to cite it.
- **Verification intent:**
  - The matrix exists.
  - FFM:222/1325, FBP:397 and TESTING:1422 (main line references per QA-5) agree with it or are listed exceptions.
  - No context grants one seat opposite permissions.
- **Open decision:** DEC-18. In particular: may the Engineer deploy to staging in FFM runs? (Tony)
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Project-module Git belongs to the Director: commit and push the completed engineering candidate, create qa/<module-branch> at that exact commit, commit approved repairs there, and perform final merge and push after certification and closeout. Engineer and QA Executor have distinct writable lanes on that branch. Cloud and staging actions require explicit context-specific authority. A Hub skill exception is confined to its named Hub context and is superseded by an explicit task restriction.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:61` — ## 2. The Four-Role Factory Pattern; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.
- `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md:383` — ## 8. Stage 6 — Demo Deployment Prep (V1); MANIFEST ← 4: ENGINEER_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, UI_UX_BUILDING_MANUAL.
- `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md:1415` — ## 5.1 `CHANGELOG.md`; MANIFEST ← 11: SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, API_AND_SERVICES_MANUAL, DATABASE_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md:108` — ## 7. Standing Engineer Doctrine (bake into every manager); MANIFEST ← 1: FEAT_PLAYBOOK.

**Touch proposal:** C-012. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-012` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.
