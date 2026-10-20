# DEPLOYMENT PLAYBOOK
## Deployment, Promotion, Rollback and Git / Cloud Authority — the Owning Document

> **Version:** 1.0 · **Date:** 2026-10-16 · **Status:** Active (sections marked OPEN are not doctrine until ruled)
> **Tier:** 3 — Build Methodology · **Pairs with:** `QA_PLAYBOOK.md`, `SOFTWARE_FACTORY_PLAYBOOK.md`, `BIM_PLAYBOOK.md`, `FFM_PLAYBOOK.md`, `QAM_PLAYBOOK.md`, `RRM_PLAYBOOK.md`, `RECON_QUESTIONNAIRE.md`, `APP_FACTORY_SKILLS_PLAYBOOK.md`
> **Owner:** Stark Industries App Factory
> **Provenance:** Created by the Director's placement ruling of 2026-10-14 (RUL-06) as the owning document that the Factory lacked (certified finding FC-011). Ruled content: the module Git flow (RUL-02) and the deployment-exclusion rule (RUL-03). Source material for the sections still marked OPEN: the DevOps operating model of 2026-08-24 (harvest source SRC-W07, status REVIEW; preserved in this run's intake snapshot); its claims are not adopted here.

---

## 1. Purpose and Status

This document owns deployment, staging-to-production promotion, rollback and the Git / cloud authority rules of the Factory. Before it existed, deployment gates and checklists were scattered across `QA_PLAYBOOK.md` (Gate D), `BUG_FIX_PLAYBOOK.md` §12–§13, `BIM_PLAYBOOK.md` §6–§7 and the Blueprint's Phase 5 with no owning doctrine (FC-011).

Each section below carries one of two statuses:

- **RULED** — Director-ruled doctrine, in force.
- **OPEN** — a named gap. An OPEN section records the question, its owner and what exists in the sources; it grants no authority and must not be cited as a rule. Open items are closed only by a recorded Director ruling landed through DocSet Sync.

## 2. Seats and Authority — RULED

- **Director** holds release authority and performs project-module Git mutations under RUL-02. QA seats do not mutate product or Git. Existing BIM cloud-zero restrictions remain in force in their declared context. Existing context-specific permissions, including any recorded FFM staging permission, remain intact; missing DevOps assignments and platform procedures remain OPEN under DEC-18; this section grants no new cloud permission.
- **DevOps / Deployment Operator** is the responsibility named in `QA_PLAYBOOK.md` §4: deploys the approved revision, records deployment identity, maintains rollback capability, supports environment diagnostics. One person may hold this seat together with the Director seat; the responsibilities remain distinct.
- **QA owns the verification verdict; the Director owns the release decision** (`QA_PLAYBOOK.md` §4). Gate Q (pre-deployment) and Gate D (deployed-environment) are QA verdicts with their own evidence; neither is replaced by a successful deploy command, a healthy container or a green build (`QA_PLAYBOOK.md` §13).
- **DevOps Architect seat occupant** — OPEN (see §8, O-2).

## 3. Context × Action × Seat Matrix

| Context | Action | Seat that acts | Status |
|---|---|---|---|
| Project module engineering (FFM, BIM, FIX, FEAT, RRM) | Build, test, self-verify; hand the Director file lists and suggested commit messages | Engineer (read-only Git inspection allowed; Git mutations Director-only; existing context-specific cloud permissions retained) | RULED (`BIM_PLAYBOOK.md` §7) |
| Project module engineering | Commit per concern to the module branch; push | Director | RULED (`BIM_PLAYBOOK.md` §6) |
| Project module QA | Create `qa/<module-branch>` **at the completed engineering candidate commit** after the engineering handoff; commit on it; merge it into `main`; push `main` | Director | RULED (RUL-02, 2026-10-14) |
| Project module QA | Authorized rework on `qa/<module-branch>` only when ruled; never on a transfer back to the engineering branch | Engineer | RULED (RUL-02) |
| Project module QA | Independent testing on `qa/<module-branch>`; no Git mutation | QA Executor | RULED (RUL-02; `QAM_PLAYBOOK.md` §3) |
| Project module QA | Certify the governed candidate; approve cleanup and retention | QA Lead | RULED (RUL-01, RUL-03) |
| Project module closeout | Closeout instruction; bounded closeout; commit, merge, push | Architect → Engineer → Director | RULED (RUL-02, RUL-03) |
| Doctrine Hub synchronization (`app-factory-docs-v1`) | Run branch, commits and the one authorized push inside the Hub only | Director-only Git mutations for this sync (RUL-15); read-only Git inspection is allowed. Historical Hub exceptions do not override this assignment | RULED (Operator ruling 2026-08-05, reconfirmed 2026-09-14; cited, not restated) |
| Cloud contexts beyond an existing explicit restriction | Deploy, promote, roll back, change infrastructure | Per an attributable context-specific authorization; no general grant here | OPEN under DEC-18 (§7–§8) |
| FFM runs | Retain the recorded FFM staging permission; verify its bounds before any action | — | OPEN (§8, O-1) |
| Any context | Cloud columns of this matrix (who prepares the package, who verifies readiness, who executes which phase) | — | OPEN (§8, O-1) |

Project `--no-ff` merge examples in pilot records are project policy, not Hub policy. After a merge on the remote, the Director refreshes local `main` before starting a new branch; a GitHub merge is not local synchronization (`RRM_PLAYBOOK.md` §10).

## 4. Deployment Exclusion of `agent_docs/**` — RULED

Module packs, QAM folders, QA evidence and session records live under the project's `agent_docs/` tree (RUL-03). **Their exclusion from every built and deployed artifact must be explicitly enforced and verified; the directory name alone is not proof of production exclusion** (Director ruling RUL-03, 2026-10-14).

Enforcement covers three surfaces, each verified separately:

1. **Compile and test scope** — `tsconfig` `exclude` and the test runner's scope exclude `agent_docs/**` (`RECON_QUESTIONNAIRE.md` Q9.1–Q9.2).
2. **Build and deploy inputs** — the platform's ignore rules exclude `agent_docs/**` from the build context and the deployed bundle: `.dockerignore` for container builds, `.gcloudignore` for Cloud Build, `.vercelignore` or the platform's equivalent for Vercel-style deploys (`RECON_QUESTIONNAIRE.md` Q9.4).
3. **The artifact itself** — the built image, bundle or deployed revision is inspected for any `agent_docs` path; the inspection command, working directory, exit code and output are recorded as EVIDENCE.

Where the verification is performed: at module packaging (Architect declares the exclusion mechanism in the module manager), at QA readiness (QA Executor preflight), and at Gate D (Step D1 evidence names the inspected artifact). A pack that cannot show the three surfaces excluded is not deploy-ready.

Revised [deployment workflow and stick diagram](_workflows/FFM_DEPLOYMENT.md) supersede the original August deployment picture; platform-specific procedures and new permissions remain outside this run.

## 5. Release Identity and the Gate D Interface

Gate D is defined in `QA_PLAYBOOK.md` §13 and is not restated here. Step D1 identifies the deployment (repository, branch, commit SHA, build ID, image digest, revision, environment, URL, time); Gate D verifies the actual deployed revision; Gate Q never certifies a deployed revision (`QAM_PLAYBOOK.md` §14).

RUL-10 (2026-10-16) approves the common requirements below, without granting new deployment authority: Record the identity chain repository → commit → build or image → deployed revision → environment → route/domain as applicable. Preserve the tested-product equivalence check through documentation-only successors (proved from the complete diff, not from a commit message). Do not generalize "redeploy runs the last phase only" without checking changed configuration, secrets, permissions, migrations and deployment prerequisites. A traffic rollback plus Git revert does not restore data or external effects; every deployment names a rollback or recovery plan suited to the changed surfaces, its operator and its evidence.

## 6. Hub → Project Distribution and Pinning

RUL-14 (2026-10-16): identify governing snapshots by canonical document name, header version and Hub commit. Preserve an intentional approved project pin until an attributable update. Declare the actual project location; no universal landing path or release tag is required. Route genuine conflicts to the Director with both identities recorded.

## 7. Platform Profiles — OPEN

No platform procedure is Factory doctrine yet. The August DevOps operating model (SRC-W07) proposes a Cloud Run profile (`init-app.sh`, `cloudbuild.yaml`, `Dockerfile`, `deploy.sh`, a checklist) and two platform postures; `APP_FACTORY_SKILLS_PLAYBOOK.md` §14 names the deployment skill family. These are source claims and existing tools, not adopted rules: version-sensitive commands must be verified at implementation time, and profile-specific filenames are not imposed on Vercel or Python deployments. Adoption of any profile is the Director's decision (DEC-18 remainder).

## 8. Open Items Register — OPEN (not doctrine)

| ID | Open item | Owner | Source of the gap |
|---|---|---|---|
| O-1 | DevOps authority: the cloud columns of the §3 matrix; "may the Engineer deploy to staging in FFM runs?"; Cloud Run as one platform profile | Director (Architect advises) | DEC-18 remainder; the reported DevOps Architect ruling of 2026-08-23 was not supplied (CL-13) |
| O-2 | DevOps Architect seat occupant | Director | SRC-W07 F-2 (deliberately unassigned) |
| O-3 | Staging → production promotion doctrine | Director | SRC-W07 F-1 |
| O-4 | Monitoring / incident detection after deploy | Director | SRC-W07 F-3 |
| O-5 | Non-Next.js deployment packages (Python / ADK services) | Director | SRC-W07 F-4 |
| O-6 | Gate D mapping on client platforms beyond Vercel | QA Lead / Director | SRC-W07 F-5 |

An OPEN item is closed only by a Director ruling recorded and landed through DocSet Sync; until then no module may cite this section as authority for a deployment action.

## 9. Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-16 | New doc entering Hub: owning document for deployment and Git / cloud authority (RUL-06; FC-011). Ruled content: seats and authority (§2), the context × action × seat matrix's ruled rows (§3; RUL-02; Hub D5 cited), deployment exclusion of `agent_docs/**` with three verified surfaces (§4; RUL-03). Gate D pointer (§5). Distribution and pinning (§6, RUL-14). Platform profiles and the DevOps remainder recorded as OPEN (§7–§8; DEC-18). [FC-011; FC-012; FC-088; IN-2026-10-15-08 … IN-2026-10-15-10 (WF-08, WF-09, WF-10); RUL-02; RUL-03; RUL-06]; current correction pass: MC-01…14; RUL-02, RUL-03, RUL-06, RUL-10 |
