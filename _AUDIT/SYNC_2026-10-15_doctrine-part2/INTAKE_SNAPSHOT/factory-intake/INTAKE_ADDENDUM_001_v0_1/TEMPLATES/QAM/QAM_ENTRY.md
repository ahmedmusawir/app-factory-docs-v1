# QAM_ENTRY — `<<MODULE_ID>>`

> NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED. Template `QAM/QAM_ENTRY.md` v0.1-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §§2, 5, 6, 7. **Owner: Architect** (resolves every `<<…>>` at packaging). This file is the canonical entry both `CLAUDE.md` and `AGENTS.md` point to. It references authority; it grants none.

## 1. Module identity

| Field | Value |
|---|---|
| Module ID / type | `<<MODULE_ID>>` / `<<MODULE_TYPE: RRM · FFM · BIM · FIX · FEAT · other defined type>>` |
| Repository | `<<REPO_NAME>>` (`<<REPO_URL_OR_PATH>>`) |
| Module directory (repo-relative) | `<<MODULE_DIR>>` — this QAM lives at `<<MODULE_DIR>>/QAM/` |
| Engineering branch | `<<MODULE_BRANCH>>` |
| QA branch (continuing; Director-created at the engineering start commit; Director-merged into `main`) | `qa/<<MODULE_BRANCH>>` |
| Baseline commit (full SHA) | `<<BASELINE_SHA>>` |
| Candidate (tested product identity) | `PENDING` — resolved by the QA Executor in Q1 from the Director's commit receipt / read-only Git evidence; never invented |
| Playbook governing this QAM | QAM_PLAYBOOK `<<VERSION>>` — snapshot and hash in `GOVERNING/README.md` |

## 2. Governing contract (linked, not duplicated)

| Item | Module-relative path | Identity |
|---|---|---|
| Frozen acceptance spec | `<<../ACCEPTANCE_SPEC.md or equivalent>>` | version / hash: `<<…>>` |
| Ruling / erratum lane (append-only; attributable approved amendments only) | `<<../RULINGS_ADDENDUM.md or equivalent>>` | `<<…>>` |
| Implementation assignment (Engineering entry) | `<<../CLAUDE.md>>` | — |
| Other governing bodies (QA_PLAYBOOK, module-type playbook, project policies) | `GOVERNING/README.md` | per-source version + hash |

Frozen AC text is never changed by a plan edit (RUL-04). A contract question is a `STOP-CONTRACT` for the Architect/Director, not a reinterpretation.

## 3. Seats and lanes

| Seat | May write | May not |
|---|---|---|
| QA Executor | `QAM/evidence/`, `QAM/AUTOMATION/`, `QAM/HANDOFFS/`, and the Executor-owned files (`QAM_RECON_REPORT.md`, `QAM_TEST_PLAN.md` draft, `QAM_EXECUTION_REPORT.md`, `AC_EVIDENCE_MATRIX.md`, `FINDINGS.md` records/proposals, `QAM_CLEANUP_REPORT.md`, its own `QAM_STATE.md` entries) | product code, tests, contract files, Engineer evidence, `QAM_APPROVAL.md`, `QAM_CERTIFICATION.md`; any Git mutation; any deployment |
| Engineer | `QAM_MANIFEST.md`, `HANDOFFS/ENGINEERING_HANDOFF.md`, its own `QAM_STATE.md` entries; ruled repair paths on `qa/<<MODULE_BRANCH>>` only | QA results, plan approval, certificate |
| QA Lead | `QAM_APPROVAL.md`, dispositions in `FINDINGS.md`, retention decision in `QAM_CLEANUP_REPORT.md`, `QAM_CERTIFICATION.md`, standing section of `QAM_RISK_REQUIREMENTS.md` | product changes; inventing evidence |
| Architect | this file, `QAM_PREFLIGHT.md` rows, module section of `QAM_RISK_REQUIREMENTS.md`, `GOVERNING/`, closeout instruction | QA results; substituting an engineering-green result for independent QA |
| Director | release references in `QAM_APPROVAL.md`; credentials file `<<QA_CREDENTIAL_FILE, normally .env.qa.local>>`; all Git actions; risk decisions | — (does not have to perform repeatable UI checks) |

Protected paths (never written by any QA seat): `<<PROTECTED_PATHS, e.g. src/**, package.json, lockfile, next.config.*, tests/**, RECOVERY.md, agent_docs/SESSIONS/**>>`.
Permitted effects on the target: `<<PERMITTED_EFFECTS: read-only · bounded login/logout probes · declared transient setup · named writes>>`. Anything else is `STOP-AUTHORITY`.

Authority rule (playbook §6): being pointed at this folder and asked to start authorizes **Q1 only**, within the declared scope. A folder path by itself never authorizes Q2, product repair, certification, Git mutation or deployment; those require the approval and release recorded in `QAM_APPROVAL.md`, the dispositions in `FINDINGS.md`, and the Director's own actions.

## 4. Target and prerequisites (summary; executable rows in `QAM_PREFLIGHT.md`)

| Item | Value |
|---|---|
| Target environment and how it is resolved | `<<TARGET: local served build · main-dev · scratch · replica — module-specific approval, never by habit>>` |
| Roles / identities required | `<<ROLES by role name only>>` — existence verified by `<<Director / date>>` |
| Test data | `<<FIXTURES / DATA STATE>>` |
| Toolchain | `<<RUNTIME + VERSIONS, package manager, browser driver>>` |
| Credential file (ignored, untracked; Director creates; values never recorded) | `<<QA_CREDENTIAL_FILE>>` with keys `<<KEY NAMES ONLY>>` |

## 5. Read order and phase dispatch

Read, in order: `QAM_STATE.md` → this file → the contract and ruling lane (§2) → `GOVERNING/README.md` → `QAM_RISK_REQUIREMENTS.md` → `QAM_MANIFEST.md` + `HANDOFFS/ENGINEERING_HANDOFF.md` (claims) → `QAM_PREFLIGHT.md` → the phase file for the recorded state.

| Recorded state in `QAM_STATE.md` | Do |
|---|---|
| READY FOR RECON | Introduce the QA Executor role briefly; run `QAM_PREFLIGHT.md`; write `QAM_RECON_REPORT.md`; draft `QAM_TEST_PLAN.md`; build the Q1 package (`QAM_PACKAGING.md`); stop for the QA Lead. |
| Q1 COMPLETE — AWAITING QA LEAD REVIEW | Return the existing Q1 package and the decision needed. Do not rerun Q1. |
| APPROVED — NOT RELEASED | Name the missing Director release (`QAM_APPROVAL.md` §3). Do not start Q2. |
| RELEASED FOR Q2 | Verify the approval ↔ candidate binding (`QAM_APPROVAL.md`), full HEAD, product identity, target; recheck changeable readiness rows; execute the approved plan; build the Q2 package. |
| STOPPED (`STOP-*`) | Report the recorded stop, owner and required resolution. Resume only from the recorded safe resume point after its resolution. |
| REPAIR RULED — AWAITING COMMIT / RELEASED FOR Q4 | Re-pin the repaired candidate from the Director's receipt; run the Q4 retest scope in `QAM_TEST_PLAN.md` §7; package. |
| CLEANUP APPROVED | Execute `QAM_CLEANUP_REPORT.md` under the recorded authority. |
| CERTIFIED / CLOSED | Show the verdict and the next owner. Do not restart testing or cleanup. |
| Wrong folder / wrong role | Explain the correct module-relative entry (`PARENT_ENTRY_ROUTING.md`); ask only if intent remains ambiguous. |

## 6. Outputs and return

Every Q1 return, Q2 return, material stop and repair/retest return produces one indexed ZIP at `HANDOFFS/<<MODULE_ID>>_<PHASE>_REVIEW_<ATTEMPT>.zip` per `QAM_PACKAGING.md`, with its absolute path, member count, SHA-256 and the exact decision requested. Repository-required response/session records stay at their governed paths and are indexed, not moved.

## 7. Engineer completion duties (pointer)

The Engineer completes `QAM_MANIFEST.md` and `HANDOFFS/ENGINEERING_HANDOFF.md` as part of the original engineering assignment (playbook §7) and records `ENGINEERING COMPLETE — MANIFEST + HANDOFF RECORDED` in `QAM_STATE.md`. The Engineer fills no QA result, decision or certificate.

*NEWLY AUTHORED DRAFT — QA LEAD REVIEW REQUIRED.*
