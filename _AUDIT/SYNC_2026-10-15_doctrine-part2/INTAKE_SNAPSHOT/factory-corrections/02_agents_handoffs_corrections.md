# 02 — Agents / Handoffs / Artifacts — Correction Brief

> **DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC**

- **Package:** Factory Doctrine Correction Package 001. Index: `FACTORY_DOCTRINE_CORRECTION_INDEX_001.md`.
- **Prepared by:** Claudy (documentation Engineer seat), 2026-10-11. This is not a QA product and certifies nothing.
- **Primary entries:** FC-013 … FC-019 (7), the certified register §5.B.
- **Authority:** every outcome is **PROPOSED** for Jarvis (Architect) review and Tony (Director) approval. Nothing here is approved policy.
- **Nature:** these are documentation findings, not proof that any client application has the flaw. No replacement doctrine text is written.

## Pinned sources

| Ref | Revision | Path |
|---|---|---|
| Certified register / QA | `c6210c3` = `c6210c32480558b343a27726a26822e8d959d0f7` | `astra-review/run-002/synthesis/PART1_FINDINGS_DISPOSITION.md`, `astra-review/run-002/synthesis/QA/PART1_CONVERGENCE_QA.md` |
| Astra chunk 02 / Sol chunk 02 | `c6210c3` | `astra-review/run-002/chunks/02_agents_handoffs/ASTRA_REVIEW.md`, `astra-review/run-002/chunks/02_agents_handoffs/SOL_REVIEW.md` |
| Fable (blind) | `39a1c6114d72b22d3550d7ff65234ec0f01418f6` (`origin/factory-docs-review-fable-001`) | `fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md` |
| Review baseline | `0a787cb` = `0a787cb826118b4a010765d60e41a449df3ce746` | defect surfaces named per entry |
| Current main | `9c17939` = `9c179392f79b70da099121fc357d3107ad3bb86e` | every surface in this brief is blob-identical to `0a787cb` (QA-4) |

Route codes are as in the index: `SYNC`, `XB-SKILL`, `XB-LINT/CI`, `XB-ROOT`, `XB-EXT`.

**Sol C02 §6.B (binding framing for this brief):** FC-015 is the *pre-implementation* control (spec approval before code). FC-013 is the *post-implementation* control (independent QA before release). Correct them as two distinct transitions; do not collapse them into one "missing approval" fix.

---

## CF-02 — Artifact / handoff / template contracts (FC-013, 015, 016, 017, 018, 019 here)

### FC-013 — Engineer-side completion/handoff doctrine does not carry the QA intake interface
- **Certified record:** CF-02 · Severity HIGH · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D01 · Fable FBL-D015 (primary)
- **Severity divergence (recorded):** Astra HIGH vs Fable MEDIUM. The certified HIGH stands.
- **Evidence:** Astra C02 §7 Rank 1; Sol C02 §3 and §6.A; Fable §7 FBL-D015, §9 row 18.
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §12 (readiness for Operations), §17 (Handoff to Operations)
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §2.5
  - `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` §6 (15-item Engineer completion package), §20 (QA artifacts)
  - `03_BUILD_METHODOLOGY/BIM_PLAYBOOK.md` §4, §5, §7
- **Defect:**
  - The Engineer's ready-for-Operations contract has no QA handoff, `ACCEPTANCE_SPEC`, Gate Q or Operator release interface.
  - QA §6 requires a 15-item completion package that no Engineer-side doctrine tells anyone to produce.
  - QA §20 artifacts (`QA_PLAN.md`, `GATE_Q_REPORT.md`, `GATE_D_CHECKLIST.md`, `GATE_D_REPORT.md`) have no defined home while the module folder is frozen.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The Engineer's completion contract routes through independent QA before Operations, and Engineer-side doctrine (ENGINEER §17, BIM §4/§5/§7) names:
    - the acceptance artifact and its provenance
    - one Engineer completion artifact containing every QA §6 field
    - the QA verdict reference
    - routing for findings and blockage
    - the Operator release decision
  - QA §20 artifacts have a defined location that does not contradict the module freeze (joint with FC-026).
- **Preserve:**
  - Operations' setup, environment, logging and rollback package (Astra C02 §5 item 8).
  - The constitutional documentation-only waiver eligibility.
  - QA_PLAYBOOK as the single owner of QA mechanics: link, don't duplicate.
  - The Sol C02 distinction from FC-015.
- **Likely affected docs / consumers:** ENGINEER §12/§17, BIM §4/§5/§7, QA §6/§20, SFP §2.5 (reference); QA seat intake; Operations; FC-002 and FC-025 (sequence together).
- **Verification intent:**
  - ENGINEER §17's recipient sequence is Engineering → QA (Gate Q) → Operator release → Operations.
  - A field-by-field match shows the named Engineer completion artifact covers every QA §6 item.
  - QA §20 artifacts have a stated home consistent with FC-026's freeze model.
  - No QA procedure text is duplicated in ENGINEER.
- **Open decision:** DEC-13, the QA artifact home and module freeze model. Fable proposes a `qa/` subfolder written after unfreeze; joint with FC-026.
- **Proposed route:** `SYNC`.

### FC-015 — Greenfield engineering-spec approval has no execution checkpoint before implementation
- **Certified record:** CF-02 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D03 · Fable none
- **Evidence:** Astra C02 §7 Rank 3; Sol C02 §3 ("a true pre-implementation authority boundary") and §6.B.
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`:
    - §3 (greenfield author of record)
    - "Before starting" checks
    - §12 (DATA_CONTRACT produced "alongside working code"; DRAFT/APPROVED field with no transition)
    - the closing checklist
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`: "The Full Workflow", Phase 3 → Phase 4.
- **Defect:** the Blueprint requires human approval of the Engineer-produced DATA_CONTRACT, the applicable schema/API specs and FILE_TREE before Phase 4 code. The Engineer's own sequence, §12 and closing checklist can all be followed without submitting those specs for approval.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The greenfield Engineer sequence runs in this order:
    1. author DATA_CONTRACT, plus applicable schema/API specs and FILE_TREE if retained (FC-008)
    2. submit for review
    3. human approval, recorded against the artifact revision
    4. fabrication
  - §12 and the closing checklist follow that order.
  - Later changes are amendments that need re-approval.
  - The conversion consumption path is unchanged.
- **Preserve:**
  - The per-pipeline authorship split: conversion is Architect-authored, greenfield is Engineer-authored (Astra C01 §5 item 2; C02 §5 item 5).
  - The Blueprint approval rule.
  - The distinction from FC-013.
- **Likely affected docs / consumers:** ENGINEER §3/§12 and closing checklist; Blueprint Phase 3/4; FFM §12.4/§14/§18 through FC-027; Engineer and Operator.
- **Verification intent:**
  - In ENGINEER, the spec-approval step comes before any code-writing step, in both the procedure and the closing checklist.
  - The DATA_CONTRACT DRAFT → APPROVED transition names an approver.
  - The outcome is consistent with FC-027's FFM sequence.
- **Open decision:** DEC-11, greenfield DATA_CONTRACT timing and Engineer seat identity (Fable §11 decision 6); joint with FC-027.
- **Proposed route:** `SYNC`.

### FC-016 — Artifact status vocabularies disagree between producer templates and receiving gates (LOCKED vs APPROVED)
- **Certified record:** CF-02 · Severity MEDIUM · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D04 · Fable FBL-D012 (primary)
- **Severity divergence (recorded):** Astra MEDIUM vs Fable LOW. The certified MEDIUM stands.
- **Evidence:** Astra C02 §7 Rank 4; Sol C02 §4; Fable §7 FBL-D012, §9 row 23.
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md`: template header `[DRAFT | REVIEW | LOCKED]`
  - `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md`: lifecycle DRAFT→REVIEW→APPROVED / AMENDED; handoff requires APPROVED
  - `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`: preflight; §8 UI_SPEC `Status: APPROVED`
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`: preflight; §12 `DRAFT | APPROVED`
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md`: Appendix C.2 `Status: LOCKED`
- **Defect:** the canonical APP_BRIEF template cannot express APPROVED, the state both consumers and the producer's own manual require. No mapping connects LOCKED to APPROVED, and the vocabulary also varies across other artifacts.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One artifact status vocabulary, including amendment and re-approval, is used by templates, authoring procedures and receiving gates for Factory planning artifacts.
  - If legacy LOCKED artifacts stay valid, an explicit mapping and the required approval evidence are stated. No silent relabeling.
- **Preserve:**
  - Human control of approval and unlock.
  - Re-approval after change (Astra C02 §5 item 2).
  - Revision/re-approval semantics (Sol).
- **Likely affected docs / consumers:** ARCHITECT_QUESTIONNAIRE, ARCHITECT_PLAYBOOK, DESIGNER, ENGINEER, FFM C.2; Designer and Engineer preflight gates; FC-019.
- **Verification intent:**
  - Every status enumeration in templates and gates draws from one set.
  - Every receiving gate's required state can be expressed by its producing template.
  - A corpus search for `LOCKED` as an artifact state is fully dispositioned.
- **Open decision:** DEC-10, the vocabulary. Recommend APPROVED / AMENDED, the producer playbook's and both consumers' existing set. Jarvis proposes; Tony ratifies.
- **Proposed route:** `SYNC`.

### FC-017 — Architect-seat responsibility (including the greenfield UI_SPEC draft) is assigned differently across docs
- **Certified record:** CF-02 · Severity MEDIUM · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D05 · Fable FBL-D005 (primary)
- **Evidence:** Astra C02 §7 Rank 5; Sol C02 §4 (model A or B; "Do not preserve a phantom artifact stage"); Fable §7 FBL-D005, §9 row 11, §11 decision 4.
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md` §5.5
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §3
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` §2 (Role 3), §4
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` §8, §11
  - `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` §1 ("Not Architect's Job"), §8 handoff and recipient checklist
  - `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`: required inputs, §8, §10
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md`: router, Phase 2
- **Defect:**
  - Four downstream docs say the greenfield UI_SPEC is "drafted by the Architect, revised by the Designer". The Architect's handoff and the Designer's inputs never create or transfer such a draft, and the Blueprint makes UI_SPEC a Designer output.
  - More broadly, ARCHITECT §1 excludes UI/UX, schemas and API contracts, while other docs assign the Architect conversion DATA_CONTRACT pre-authoring and full FFM authorship.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Exactly one greenfield UI_SPEC model is active, and every listed doc reflects it:
    - **(A)** the Architect produces a defined initial UI_SPEC draft and hands it off explicitly; or
    - **(B)** the Designer authors UI_SPEC from approved Architect scope.
  - ARCHITECT §1's exclusions are consistent with the Architect duties other docs assign.
- **Preserve:**
  - The conversion authorship route.
  - Designer final authorship and human approval.
  - Human ownership of product scope.
- **Likely affected docs / consumers:** the surfaces above; Designer and Engineer intake; FC-019, FC-006.
- **Verification intent:**
  - All UI_SPEC provenance statements ("drafted by the Architect", "revised by the Designer") match the chosen model.
  - Under (A), the Architect handoff package contains the draft and the Designer inputs request it; under (B), neither does.
  - ARCHITECT §1 has no exclusion contradicted elsewhere.
- **Open decision:** DEC-10, model A or B (Tony). Fable notes the majority (HANDOFF, ENGINEER, FFM, GDSH) is A; the Blueprint and DESIGNER read as B.
- **Proposed route:** `SYNC`.

### FC-018 — Mandatory visual intake has no valid path for a supported nonvisual build
- **Certified record:** CF-02 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D06 · Fable none
- **Evidence:** Astra C02 §7 Rank 6; Sol C02 §4 and §6.D; Sol C06 cross-domain item "nonvisual app routing".
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md`: router/type table (Backend Bundle, CLI), inputs and approval checks, DataSync example
  - `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md`: Q4 (STOP without a visual anchor)
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`: Part I applicability, Pipeline Track routing, preflight
- **Defect:** the router supports headless and CLI builds, but the Architect inputs, Questionnaire Q4 and Engineer preflight unconditionally require a visual anchor, UI_SPEC and the token/screen package, and STOP without them. There is no not-applicable branch.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Intake gates follow the approved interface type: visual artifacts are REQUIRED when a visual interface is approved, and explicitly recorded as NOT APPLICABLE when none is.
  - Backend and CLI builds have their own required contract and receiving checklist.
- **Preserve:**
  - The full design package wherever screens exist (Sol: do not weaken visual requirements).
  - UX work for CLIs that need it.
- **Likely affected docs / consumers:** ARCHITECT, ARCHITECT_QUESTIONNAIRE Q4, ENGINEER preflight; FC-075 (theming artifacts); the general REQUIRED / OPTIONAL / NOT APPLICABLE mechanism Sol C02 §6.D flags.
- **Verification intent:**
  - The ARCHITECT DataSync example passes Architect and Engineer gates with recorded N/A visual artifacts and no invented visuals.
  - A UI build still STOPs without a visual anchor.
- **Open decision:** a general applicability mechanism vs a local branch (Jarvis; related backlog C01-S03).
- **Proposed route:** `SYNC`.

### FC-019 — Multiple incompatible APP_BRIEF and UI_SPEC templates coexist under a single-source claim
- **Certified record:** CF-02 · Severity HIGH · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none as a defect (C02-S04 suggestion concerns fields inside the canonical template, not template multiplicity) · Fable FBL-D004
- **Evidence:** Fable §7 FBL-D004, §9 row 10, §11 decision 3; Astra C02 §8 (C02-S04).
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/ARCHITECT_QUESTIONNAIRE.md`: "SINGLE SOURCE" claim; 12-section APP_BRIEF
  - `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md`: §5.1 (14 sections), §5.3 (UI_SPEC, 9), §5.5
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md`: §9.1 / C.2 (13 sections), §9.3 (UI_SPEC, 12)
  - `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`: §8 (UI_SPEC, 5)
- **Defect:** three APP_BRIEF shapes and three UI_SPEC shapes coexist while one document claims to be the single source.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Exactly one APP_BRIEF template and one UI_SPEC template exist, or one per pipeline, explicitly declared with a "sections that differ per pipeline" table (Fable).
  - The other locations become pointers, which makes the single-source claim true.
- **Preserve:**
  - The Questionnaire as the authoring instrument.
  - Mandatory planning inputs in the canonical brief (C02-S04).
  - Real conversion/greenfield differences.
  - Uncertainty labels (Astra C02 §5 item 3).
- **Likely affected docs / consumers:** the surfaces above; checks citing "APP_BRIEF § N" (FFM §9 cross-file consistency); FC-016, FC-017.
- **Verification intent:**
  - Each artifact template is defined at one location, and all others link to it.
  - Section-number citations to APP_BRIEF and UI_SPEC across live docs resolve against the canonical template(s).
- **Open decision:** DEC-10, one template vs one per pipeline (Tony; Jarvis proposes).
- **Proposed route:** `SYNC` (multi-doc; LARGE route expected).

## CF-03 — Recon / planning / scope-authority boundaries (FC-014 here)

### FC-014 — Recon's operation boundary contradicts its own procedure and required output
- **Certified record:** CF-03 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C02-D02 · Fable none
- **Evidence:** Astra C02 §7 Rank 2; Sol C02 §3 (provisional MEDIUM, closed MEDIUM 2026-09-27) and §6.C (cross-check against `stark-recon`).
- **Defect surfaces (`0a787cb`):**
  - `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md`: "How To Use This", S0.7, Q8.6
  - `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` §2
  - `02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md` (recon consumption)
  - `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` (recon as a read-only pass)
- **Defect:** recon is specified as "no file changes, no git operations", pure reading and grepping. The same doctrine instructs `npm run build` and requires a written recon report file, with no defined exception.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** recon doctrine states one boundary, identically in all three recon documents, that separates three classes of write:
  - **(A) Report and bookkeeping writes: permitted.**
    - The recon report, at one path shared by producer and consumer.
    - The normal authorized session bookkeeping under the governing session protocol: `agent_docs/RESPONSES/`, the session file, `RECOVERY.md`.
    - These record evidence and state; they do not change the system under inspection.
  - **(B) Diagnostic-generated artifacts: permitted only inside an explicit diagnostic boundary.** If a diagnostic such as the S0.7 / Q8.6 `npm run build` is allowed, the doctrine names:
    - who authorizes it;
    - where it runs (the target checkout or a disposable copy);
    - which generated artifacts are expected (e.g. framework build output and caches);
    - how those artifacts are recorded or removed afterwards;
    - how the run confirms that no tracked application source changed.

    If a diagnostic is not authorized or not available, the recon report records the limitation instead of fabricating a result.
  - **(C) Application-source changes: prohibited.** No edits to application source, configuration, dependency manifests or lockfiles, and no state-changing operations on the target repository.
- **Preserve:**
  - Recon as a read-only validity gate and "invalid without recon" (Astra C01 §5 item 1). "Read-only" applies to class C; it must not be read as forbidding class A.
  - The named producer/consumer and freshness triggers (Astra C02 §5 item 1).
  - The normal authorized bookkeeping protocol.
- **Likely affected docs / consumers:** RECON_QUESTIONNAIRE, ENGINEER §2, ARCHITECT, Blueprint. The off-Hub `stark-recon` skill (`XB-EXT`; not inspected, FC-009) is awareness only.
- **Verification intent:**
  - The three recon documents state the same three-class boundary.
  - **Class A:** the report path is identical for producer and consumer, and no recon sentence, read literally, forbids the report or the normal bookkeeping writes (the original contradiction is gone).
  - **Class B:** S0.7 and Q8.6 are each removed, carry the full diagnostic boundary (authorizer, location, expected artifacts, post-run handling, tracked-source check), or are replaced by a recorded-limitation instruction.
  - **Class C:** the prohibition is stated, and the post-diagnostic check named under class B confirms that no tracked application source changed.
- **Open decision:** DEC-14 (Tony/Jarvis):
  - Are build diagnostics allowed during recon, and if so where do they run (target checkout or disposable copy) and which artifacts are acceptable?
  - Is read-only Git inspection permitted for the class-C check?

  Sol's elevation trigger (recon mutating target state) is not established by the certified record.
- **Proposed route:** `SYNC` (+ `XB-EXT` awareness).

---

*End of brief 02. Primary entries: 7 (FC-013 … FC-019). DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC.*
