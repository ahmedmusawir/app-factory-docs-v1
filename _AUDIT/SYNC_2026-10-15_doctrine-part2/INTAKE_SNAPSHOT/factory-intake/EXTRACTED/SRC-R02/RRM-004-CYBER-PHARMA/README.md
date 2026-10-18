# RRM-004-CYBER-PHARMA — Dependencies

Module 4 of 4 in the RRM campaign (`agent_docs/RRM_CAMPAIGN_MAP_v1_0.md` §7). **Two pilots ride on it:** the Engineering side repeats the RRM-003 one-shot shape; the QA side is the **first QAM (QA Module) run** — a prepared QA folder the Director starts with one command (QA Lead's pilot plan v0.1, Architect's QAM opinion 2026-09-29). Start at `CLAUDE.md`. Director runway in `DIRECTOR_ACTIONS.md`. Status: AUTHORED 2026-09-30.

| File | Owner |
|---|---|
| CLAUDE.md · AUTHORITY_POINTER.md · ENVIRONMENT_PREFLIGHT.md · DIRECTOR_CHECKPOINTS.md · RRM_BRIEF.md · ACCEPTANCE_SPEC.md · CLAUDY_PROMPTS.md · DIRECTOR_ACTIONS.md | Architect (frozen at handoff) |
| RULINGS_ADDENDUM.md | append-only; Engineer writes rows under Architect/Director instruction |
| EXECUTION_LOG.md (incl. §Metrics) · QA_HANDOFF.md · evidence/ · QA/QAM_MANIFEST.md (the factual half only) | Engineer |
| QA/AGENTS.md · QA/QAM_PILOT_CHARTER.md · QA/QA_ENVIRONMENT_PREFLIGHT.md · QA/QA_TEST_PLAN.md · QA/QA_CERTIFICATION.md | QA Lead (Architect supplied v0.1 drafts of the first three; the QA Lead ratifies or amends them before the run; the plan is the QA Lead's alone) |
| QA/evidence/ · QA/AUTOMATION/ · QA/AC_EVIDENCE_MATRIX.md · QA/QA_EXECUTION_REPORT.md · QA/REPAIR_PROPOSAL.md (only on a FAIL) · QA/ARTIFACT_INVENTORY.json · QA/QA_CLEANUP_REPORT.md · QA/QAM_PILOT_RESULTS.md | QA Executor |
| QA/GOVERNING/ | Engineer copies from RRM-003's at handoff with a fresh `PROVENANCE.md` |

Whoever built the candidate does not write the plan that tests it.
