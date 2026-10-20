# QAM — reusable QA Module template set

> **TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC.**
> Template set **v0.3**. Governing playbook: **QAM_PLAYBOOK v1.0**. QA behavior was accepted by Fable on 2026-10-14 with three exact amendments; Jarvis verified their application. Source set v0.3-draft is preserved byte-for-byte in this run’s intake snapshot. This proposed set differs only by the status/provenance translations enumerated in this run’s `PHASE_2_TEMPLATE_TRANSLATIONS.json`; installation and translation approval remain pending; it is newly authored from the approved playbook, not the pilot’s missing original templates. Source playbook SHA-256: `97e111e2a495f9a3fe65f50213e6f2ba68c8e5e963f3d23493b1ee99ad35c897`.
> **Canonical home (Architect decision AD-01 under the Director's C.1 delegation, 2026-10-14): `03_BUILD_METHODOLOGY/_templates/QAM/`** — stable filenames; set version and governing playbook version recorded here; superseded sets archived under `_ARCHIVE/QAM_TEMPLATES_v<version>/`; changes tracked through the QAM_PLAYBOOK MANIFEST row and CHANGELOG; explicit template verification in the sync acceptance scope. **Installation provenance:** see the sync run’s template-install plan and retained acceptance records; source acceptance alone is not installation verification.

Acceptance and provenance: [QA Lead decision](../../../_AUDIT/SYNC_2026-10-15_doctrine-part2/INTAKE_SNAPSHOT/factory-intake/INTAKE_ADDENDUM_001_v0_3/QA_LEAD_DECISION_2026-10-14.md), [Architect verification](../../../_AUDIT/SYNC_2026-10-15_doctrine-part2/INTAKE_SNAPSHOT/factory-intake/INTAKE_ADDENDUM_001_v0_3/ARCHITECT_VERIFICATION_2026-10-14.md), [installation translations](../../../_AUDIT/SYNC_2026-10-15_doctrine-part2/PHASE_2_TEMPLATE_TRANSLATIONS.json).

## 1. What this set is

The playbook (§5) says: "Instantiate `TEMPLATES/QAM/` inside each module directory. The template's unfilled fields are authoring prompts, not a launch-ready pack." This folder is that template set (in the Hub its path is the one above; the playbook's literal path is a cargo convention translated under D15). Copy it to `<module>/QAM/` when the Architect packages a newly authored module (RUL-01: every newly authored module MUST include a complete, module-specific `QAM/` from initial Architect packaging), then resolve every `<<…>>` placeholder that belongs to the preparing seat.

Conventions used in every file:

| Token | Meaning |
|---|---|
| `<<LIKE_THIS>>` | Authoring placeholder. The seat named in the file's header fills it. A pack with unresolved placeholders in Architect-owned fields is not ready for engineering; one with unresolved Engineer-owned fields is not ready for Q1. |
| `NOT RUN` | A check or test that has not been executed. Never replaced by a result the owning seat did not record. |
| `NOT RECORDED` | A fact that exists but has not been written down yet by its owner. |
| `NEEDS AUTHORING` | A section the owning seat must write for this module. |
| `PENDING` | An identity that does not exist yet (for example the candidate SHA before the Director commits, playbook §7). Never replaced by an invented value. |

No file in this set carries a PASS, an approval, a certificate, a SHA, a credential or a project-specific name. Where the pilot used Cyber Pharma names, this set uses placeholders (playbook §12: "Do not hardcode Cyber Pharma's ADMIN/MEMBER or 375px into every app").

## 2. The files, their owners and when they are written

Write permissions per seat are stated once, in `QAM_ENTRY.md` §3; each file's header repeats only its owner. Where a file has an Executor-recorded part inside an Architect- or QA Lead-owned file (preflight results, Q1 risk observations, exact plan amendments), the file says so.

| File | Owner at instantiation | Written when | Playbook |
|---|---|---|---|
| `CLAUDE.md` · `AGENTS.md` | Architect (generated, identical routing text) | packaging | §6 |
| `QAM_ENTRY.md` | Architect | packaging | §5, §6 |
| `QAM_STATE.md` | Architect creates at `READY FOR ENGINEERING`; every seat appends dated entries for its own transitions | packaging, then continuously | §15 |
| `QAM_MANIFEST.md` | Engineer | as engineering finishes, before the Director commits | §7 |
| `HANDOFFS/ENGINEERING_HANDOFF.md` | Engineer | as engineering finishes | §7 |
| `QAM_PREFLIGHT.md` | Architect authors rows (expected results, owners, authorizations); QA Executor records results in Q1 and rechecks at Q2/Q4 entry | packaging / Q1 | §8 |
| `QAM_RISK_REQUIREMENTS.md` | §1 QA Lead standing requirements (QAM-SR v1.0, adopted by the QA Lead 2026-10-14; reusable without per-module re-review); §2 Architect module risks; §3 QA Executor's Q1 observations | packaging / Q1 | §7 |
| `QAM_RECON_REPORT.md` | QA Executor | Q1 | §8 |
| `QAM_TEST_PLAN.md` | QA Executor drafts; QA Lead amends and approves; Executor applies only the exact amendments | Q1 → approval | §8, §9 |
| `QAM_APPROVAL.md` | QA Lead (decision); Director (release references); attributed transcription of exact supplied text only when expressly instructed | between the shots; Q4 approvals appended | §9 |
| `QAM_EXECUTION_REPORT.md` · `AC_EVIDENCE_MATRIX.md` | QA Executor | Q2 (and Q4 retest) | §10 |
| `FINDINGS.md` | QA Executor records and proposes; QA Lead dispositions; Architect/Director route repair | Q2 onward | §11 |
| `QAM_CERTIFICATION.md` | QA Lead only (§1–§3 the product verdict after adjudication; §4 cleanup acceptance and release appended afterwards) | after adjudication; §4 after cleanup | §14 |
| `QAM_CLEANUP_REPORT.md` | QA Executor executes approved cleanup; QA Lead approves retention and accepts the cleanup | after the accepted product verdict | §14 |
| `QAM_PACKAGING.md` · `HANDOFFS/REVIEW_START_HERE.md` · `HANDOFFS/FILE_INDEX.template.json` | QA Executor builds each package | every Q1/Q2/stop/retest return | §13 |
| `GOVERNING/README.md` | Architect (snapshot + provenance) | packaging | §2, §5 |
| `AUTOMATION/README.md` · `evidence/README.md` | QA Executor (lane rules set by the Architect) | Q1 onward | §5, §10, §12 |
| `PARENT_ENTRY_ROUTING.md` | Architect pastes into the parent module's entry files | packaging | §6 |

## 3. Architect preparation duties (before engineering) — playbook §7

Instantiate the set with the module ZIP and resolve, in the files named:

1. **Identity.** Repository, module ID, engineering branch `<<MODULE_BRANCH>>`, the baseline commit, and the intended continuing QA branch `qa/<<MODULE_BRANCH>>`, which the Director creates **at the completed engineering candidate commit** after the engineering handoff (RUL-02) — `QAM_ENTRY.md` §1, `QAM_STATE.md` (initial state `READY FOR ENGINEERING`).
2. **Contract.** Module-relative link to the parent's frozen acceptance spec and its ruling/erratum lane; no duplicate contract — `QAM_ENTRY.md` §2 (RUL-04).
3. **Protections and lanes.** Protected paths; the writable lanes (`QAM/` with `HANDOFFS/`, `evidence/`, `AUTOMATION/`, `GOVERNING/`); permitted effects — `QAM_ENTRY.md` §3, `evidence/README.md`, `AUTOMATION/README.md`.
4. **Target, data, roles, toolchain.** The actual target environment and how it is resolved, test data, roles required, credential file name (declared ignored QA credential file, normally `.env.qa.local`, created by the Director), tool and runtime requirements — `QAM_PREFLIGHT.md`, `QAM_ENTRY.md` §4.
5. **Evidence outputs, blocking rules, browser coverage inputs.** `QAM_RISK_REQUIREMENTS.md` §2; `QAM_PREFLIGHT.md`; `evidence/README.md`.
6. **Completion duties and handoff destinations.** Tell the Engineer exactly which fields of `QAM_MANIFEST.md` and `HANDOFFS/ENGINEERING_HANDOFF.md` are theirs — `QAM_ENTRY.md` §7.
7. **Governing snapshot.** Versioned local snapshot of the governing bodies with source, version and hash, or an explicitly approved accessible source — `GOVERNING/README.md`.
8. **Entry validation.** Both entry files route to `QAM_ENTRY.md`; the parent module's entry files route Engineering to the implementation assignment and QA to `QAM/`; discovery validated in each supported runtime, with the one-line fallback recorded — `CLAUDE.md`, `AGENTS.md`, `PARENT_ENTRY_ROUTING.md` (§6).
9. **Module-type adaptation.** The §16 inputs for the module type (RRM, FFM, BIM, FIX/FEAT; TRM only once the Factory defines it) — `QAM_RISK_REQUIREMENTS.md` §2.

The Architect does not write Q1 findings, the test plan, the approval, Q2 results, dispositions or the certificate.

## 4. Engineer completion duties (as engineering finishes) — playbook §7

Completing the factual QAM handoff is part of the original engineering assignment. It is written **before the Director commits**, so the Engineer records in `QAM_MANIFEST.md` and `HANDOFFS/ENGINEERING_HANDOFF.md`:

1. baseline identity, and the implementation identity as `PENDING` (the candidate SHA does not exist until the Director commits; never an invented SHA);
2. the **complete change inventory at handoff**: committed changes since the baseline, staged changes, unstaged changes and untracked files (manifest §2), plus any authorized exceptions;
3. claimed behavior, self-verification commands and results, evidence links — each labeled **CLAIM** for independent QA;
4. install, build, serve and reproduction commands with their working directory;
5. environments, prerequisites, migrations, fixtures, roles and credentials **needed**, without secret values;
6. known limitations, unresolved issues, preserved paths, rollback dependencies;
7. the meaning of each engineering evidence item.

The Engineer then records `ENGINEERING COMPLETE — AWAITING QA BRANCH` in `QAM_STATE.md`. The Engineer does not fill Q1 findings, Q2 results, the QA Lead decision or a passed certification. The Engineer repairs only ruled scope, on the QA branch, when a disposition routes a repair (§11).

## 5. The engagement these files support

```
Architect packages module + QAM/ (state READY FOR ENGINEERING)
→ Engineer builds; completes manifest + handoff (ENGINEERING COMPLETE — AWAITING QA BRANCH)
→ Director commits/pushes the completed engineering candidate on <<MODULE_BRANCH>> and creates
  qa/<<MODULE_BRANCH>> at that candidate commit (READY FOR RECON)
→ Q1  QA Executor: preflight, recon (resolves the candidate from the Director's receipt and reconciles it
      against the handoff inventory), independent test plan → one indexed Q1 package → STOP for QA Lead
→ Approval checkpoint  QA Lead approves / approves with exact amendments / holds
      (Q1b = the Executor applies only the exact amendments and re-binds the plan; not a third shot)
→ Release  Director commits the records and releases the candidate for Q2
→ Q2  QA Executor executes the approved plan continuously → one indexed result package; no self-certification
→ Adjudication  QA Lead dispositions findings. Product defect? → Architect ruling → Engineer bounded repair on
      qa/<<MODULE_BRANCH>> (REPAIR RULED — AWAITING COMMIT: nobody retests yet) → Director commits → QA Lead
      approves the retest scope → Director releases (RELEASED FOR Q4) → Executor re-pins and runs Q4 (conditional)
→ Product verdict  QA Lead issues the certificate §1–§3 (VERDICT ISSUED — CLEANUP PENDING)
→ Q5 cleanup  required §14 cleanup executed by the Executor under QA Lead authority
→ Cleanup acceptance + durable records committed by the Director → certificate §4 appended
  (CLEANUP ACCEPTED — RELEASED TO CLOSEOUT)
→ Architect closeout instruction → Engineer bounded closeout → Director merges qa/<<MODULE_BRANCH>> into main (CLOSED)
```

No repair is transferred back to the engineering branch; the QA branch is not abandoned (RUL-02). Cleanup is a closure operation, not a third campaign (RUL-03). The product verdict never depends on a cleanup that itself requires that verdict.

## 6. What this set does not contain

- Validators, exporters, state dispatchers, browser adapters or any runtime (RUL-07; QAM-13). `QAM_STATE.md` and the dispatch table in `QAM_ENTRY.md` are document instructions read by the agent, not a dispatcher.
- Pilot charter / pilot results files: those belong to experiments, not to routine runs (SRC-Q03 §6, harvest QAM-03).
- A `REPAIR_PROPOSAL.md` file: the conditional repair proposal is a section of `FINDINGS.md` (§11), with the pilot's archive member recorded as evidence in the addendum index, not copied.
- ABM/APBM or TRM methodology (RUL-07).

*TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC. Installed reusable template; instantiate and resolve module-specific fields before launch.*
