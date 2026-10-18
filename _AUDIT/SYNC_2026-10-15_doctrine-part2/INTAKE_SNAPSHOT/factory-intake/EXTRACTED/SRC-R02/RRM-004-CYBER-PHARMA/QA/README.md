# RRM-004 QA lane — the first QAM (QA Module) run

This folder is a **prepared QA body**: it knows its candidate, its environment, its stops, its plan and its outputs before anyone opens a terminal. The Director starts it with one command (below). The QA Executor runs it end to end, stopping only on an enumerated QA stop condition, and hands the QA Lead an execution report and an AC matrix — or, if something failed, a drafted `REPAIR_PROPOSAL.md` as well. The QA Lead adjudicates and certifies. Nothing here changes the acceptance standard: Gate Q is issued on the product ACs (AC-100…600) exactly as in RRM-001…003; the pilot-process ACs (AC-700) are graded separately in `QAM_PILOT_RESULTS.md`.

## Who writes what (DD-4)

| File | Author | When |
|---|---|---|
| `AGENTS.md` — the Executor's operating law | Architect draft v0.1 → **QA Lead ratifies or amends** | before DC-4 |
| `QAM_PILOT_CHARTER.md` — what the pilot measures | Architect draft v0.1 → QA Lead ratifies or amends | before DC-4 |
| `QA_ENVIRONMENT_PREFLIGHT.md` — QF rows | Architect draft v0.1 → QA Lead ratifies or amends | before DC-4; Executor runs it first |
| `QAM_MANIFEST.md` — the factual half | **Engineer** at handoff (end of P2) | facts and labeled claims only |
| `QA_TEST_PLAN.md` — the judgment half | **QA Lead** (or a QA-seat agent under the QA Lead) | after DC-3, before DC-4; never the Engineer, never the Architect |
| `AUTOMATION/` · `evidence/` · `AC_EVIDENCE_MATRIX.md` · `QA_EXECUTION_REPORT.md` · `REPAIR_PROPOSAL.md` (only on a FAIL) · `ARTIFACT_INVENTORY.json` · `QA_CLEANUP_REPORT.md` · `QAM_PILOT_RESULTS.md` | **QA Executor** | during and after the run |
| `QA_CERTIFICATION.md` | **QA Lead** | after reading the matrix and the evidence map |
| `GOVERNING/` | Engineer copies from RRM-003's at handoff with a fresh `PROVENANCE.md` | end of P2 |

Whoever built the candidate does not write the plan that tests it. The Engineer's manifest and handoff are claims; the Executor derives every expected value itself.

## The command (DC-4)

The Director confirms `git status --porcelain` is empty on `qa/phase-3-rrm004`, records `date -Is`, and gives the QA Executor exactly this:

QA EXECUTOR — RRM-004-CYBER-PHARMA QAM. Read agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/QA/AGENTS.md and run the module. Stop only on an enumerated Q-stop. Return to the QA Lead.

Nothing else is said until DC-5 (credentials in the browser) or a logged Q-stop.

## Architect risk notes (input to the QA Lead's plan, not the plan)

- The one thing a dependency bump can silently undo is RRM-003's cache header — re-capture from your own build, and check all three negative controls still say `no-store`.
- Attack the instrument: read `@img/sharp-libvips-<platform>/versions.json` on **your** platform; if your platform string differs from the Engineer's, that is a second data point, not a mismatch.
- Rebuild from the lockfile with `npm ci`, never reuse the Engineer's `node_modules/` or `.next/`. If `npm ci` complains the lockfile and `package.json` disagree, that is a finding.
- `npm audit` output depends on the registry at run time. A new advisory published after the candidate is a finding to record with its date, not a candidate defect — classify, don't fail.
- `/_next/image` is the only place sharp runs in this app. A 500 there with a 200 everywhere else is exactly what a broken native binding looks like.
- The negative host probe (`url=https://res.cloudinary.com/...`) must return `400` under DD-2 = remove; if it returns an image, the config did not apply.
- Expected image inventory per route comes from source (`Navbar*.tsx`, `HomePageContent.tsx`), not from the manifest.
- RRM-003's retained browser driver (`agent_docs/ACTIONS/RRM-003-CYBER-PHARMA/QA/evidence/browser/qa_ac107.cjs`) is a starting point for `AUTOMATION/`, not a requirement. Its Enter/Space probe is now a QF preflight row.
- One sign-in per role is the target. Ask for the Director once, at DC-5, with the browser already open on the login page.

Finding classes and statuses per the governing playbook. Bounded J-19 cleanup after Gate Q; `RECOVERY.md` and `agent_docs/SESSIONS/**` untouched.
