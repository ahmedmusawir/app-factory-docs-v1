# APP FACTORY — DEVOPS OPERATING MODEL
## Cross-Cutting: Certified Revision → Deployment → Gate D Evidence

> **Version:** 1.0 · **Date:** 2026-08-24
> **Status:** REVIEW — pending final Operator approval.
> **Tier:** 1 — Factory Operating Model · **Owner:** Stark Industries App Factory
> **Scope:** DevOps is a **cross-cutting department** serving all module classes — FFM (Loop 1 staging), BIM (Loop 2 backend/integration deploys), TRM (Loop 3 production promotions). One department, one contract, every loop.
> **Provenance:** Field-derived from the factory's Cloud Run deployment record (FFM staging deliveries; ADK Harness Cloud Run services) codified in the two-skill deployment package (`next-deploy-generate`, `next-deploy-execute`), the DockBloxx client-platform promotions (`TRM_PLAYBOOK.md` §9), and the DevOps Architect ruling (2026-08-23).
> **Companion visual:** APP FACTORY PART 3: FFM DEPLOYMENT diagram (Whimsical) — the FFM-flavored instance of this department. Simplified process map; **this document is the full contract.** Logged diagram edits: filenames `initscript.sh` → `init-app.sh`, `clouddeployment.yaml` → `cloudbuild.yaml`.
> **Sibling docs:** FFM / BIM / TRM operating models. Canonical QA source: `QA_PLAYBOOK.md`.

---

## 1. Executive Explanation — What DevOps Is in This Factory

**DevOps is not "the last command." It is a first-class engineering department** with its own advisory seat, execution seat, contract, and gates.

Its charter: take an **independently certified revision** (Gate Q PASS + release authorization) and make it **verifiably live** in the target environment — with a recorded identity and a maintained rollback path — then supply the technical evidence for **Gate D**.

Why the department exists (paid-for lessons): local development proves code behavior; production build proves packaging; **the deployed environment proves the system.** Latency, cookies, IAM, secrets, DNS, SSL, external-service timing, environment values, and session behavior only reveal themselves after deploy. No Jest test covers them.

```text
GATE Q PASS + release authorization
        ↓
DEVOPS DEPARTMENT
   pre-deployment verification → package → execution → identity + rollback
        ↓
DEPLOYED REVISION
        ↓
GATE D (QA adjudicates; DevOps supplies technical evidence)
```

---

## 2. The Human Control Model — the DevOps Department

```text
Director of DevOps (human)  ⇄  DEVOPS ARCHITECT (AI advisory)
            ↓
    DEVOPS ENGINEER (AI execution — authors the package)
            ↓
    Director of DevOps — hands on keyboard, runs every command
```

- **Director of DevOps** — the only seat that touches the cloud. Runs all commands in the Cloud CLI, executes `deploy.sh`, sets up DNS, verifies SSL. Owns execution of the *authorized* deployment. Human, always.
- **DevOps Architect** (ruled 2026-08-23) — the DevOps counterpart of the Software Architect: pre-deployment verification, readiness review, risk and missing-prerequisite identification, precise instructions for the DevOps Engineer, plan and package review. **Never independently authorizes infrastructure changes.** No permanent model/vendor assigned — responsibility over occupant.
- **DevOps Engineer** — authors the deployment package from a structured intake. Never executes against the cloud.

**Guidance-only law** (from the execute skill, promoted here to doctrine): the AI seats **provide exact commands and verification steps; the human runs them.** The AI never assumes permissions, never invents service accounts, never skips verification, always states which identity is acting, and stops after each phase until the Director confirms success.

Current instruments: `next-deploy-generate` (Engineer-seat authoring skill) and `next-deploy-execute` (Architect-seat walkthrough skill). Skills are instruments; the seats are doctrine.

---

## 3. The Intake Boundary — what DevOps accepts

DevOps deploys **identified, certified revisions only**:

- **Gate Q: PASS** recorded (or documented Operator QA waiver for doc-only changes).
- **Release authorization** given by the Operator (departmental approval ≠ release authorization).
- The exact revision identified: repo, branch, commit SHA. **Certified-revision law:** the revision QA certified must be the revision that ships.
- A **Gate D plan exists** (Gate Q checklist requirement) before any deploy.

Uncertified or unidentified work is refused back to its department. No exceptions, no "quick pushes."

---

## 4. The Deployment Package (Engineer deliverable)

Canonical files (ruled 2026-08-23) plus checklist:

```text
init-app.sh                 ← one-time app setup: APIs, secrets, service accounts
cloudbuild.yaml             ← build definition
Dockerfile                  ← container definition
deploy.sh                   ← repeatable deploy
DEPLOYMENT_CHECKLIST.md     ← pre-filled run record
```

The package is generated from a **structured intake** — never from memory:

1. **Identity:** app name (lowercase, hyphenated — prefix for all naming), GCP project ID, region.
2. **URLs:** backend URL (if any), custom domain — or the two-deploy pattern when the domain is undecided.
3. **Secrets:** every env var, each classified on two axes: **build-time vs runtime vs both**, and **public (`NEXT_PUBLIC_`, safe in client JS) vs secret (server-side only, Secret Manager)**. Misclassification here is the classic silent deploy-breaker.
4. **Confirmation:** the full collection summarized back in a table before a single file is generated. Generated files are ready-to-run — no placeholder editing.

---

## 5. The Identity Model — who is acting (promoted to doctrine)

Every command in a deployment names its actor:

```text
Actor A — the human operator (Director of DevOps): runs scripts, owns gcloud auth
Actor B — the build service account: executes cloudbuild.yaml
Actor C — the runtime service account: what the deployed service runs as
```

Rules: verify IAM state before proceeding, never assume permissions, reference only service accounts created by `init-app.sh`, and record which actor performed each phase. Most "deploy worked yesterday" mysteries are actor-identity mysteries.

---

## 6. Execution Flow

```text
Certified revision + release authorization (§3)
   ↓
DevOps Architect: pre-deployment verification → READY
   ↓
DevOps Engineer: package authored/confirmed current (§4)
   ↓  commands hand-off & verification
Director of DevOps executes, phase by phase, verifying each:
   Phase 1  chmod + ./init-app.sh          (first deploy only — APIs, secrets, SAs)
   Phase 2  IAM / permissions verification
   Phase 3  ./deploy.sh                    (build → image → Cloud Run revision)
   Phase 4  DNS setup (DigitalOcean)       (first deploy on a domain)
   Phase 5  domain mapping + SSL verification
   Phase 6  smoke verification of the live URL
   ↓
Release identity recorded + rollback path confirmed (§7)
   ↓
Gate D evidence package → QA (§8)
```

**Redeployment path:** an existing service updating to a new certified revision runs **Phase 3 only** (plus Phase 6 smoke). This is the standard path for BIM and TRM deploys into already-mapped services.

---

## 7. Release Identity & Rollback (per deploy, no exceptions)

Recorded in the deployment checklist:

```text
repo → branch → commit SHA → image → Cloud Run revision → environment → DNS → HTTPS
```

- **Rollback path maintained:** previous known-good revision identified before the new one goes live; rollback = re-route serving to the prior revision (platform-level instant rollback) + `git revert` for bookkeeping. **Never history rewrites** — absolute law in client repos.
- **Client-platform promotions** (TRM evidence): three-layer chain DEV → PROD-mirror → client platform; the lock is law (`npm ci` downstream); bookmark the current production deployment before the final push; full production build after any lock regeneration.

---

## 8. The Gate D Interface — DevOps ↔ QA

Gate D belongs to QA (`QA_PLAYBOOK.md` §13). DevOps's contract at Gate D:

- Supply the **release identity chain** (§7) and technical evidence: revision serving, domain mapped, SSL valid, env values present, service healthy.
- A successful deploy command, a healthy container, and a green build are **not** Gate D — they are DevOps evidence *inputs* to Gate D.
- QA Lead designs the Gate D verification; execution splits per module class (Director-manual for browser/UI, QA-Engineer scripts for machine-verifiable); QA Lead adjudicates and issues the verdict.
- A deploy-requiring module is never CLOSED before its Gate D verdict.

---

## 9. Platform Families

| Family | Examples | DevOps posture |
|---|---|---|
| **Factory-owned Cloud Run** | FFM staging, BIM services, ADK agents | Full package (§4), phases 1–6, DigitalOcean DNS, domain mapping + managed SSL |
| **Client-owned platforms** | DockBloxx on Vercel (TRM) | Three-layer promotion chain; client-repo law (git status review before every commit, never rewrite history); platform-native rollback bookmarked; Gate D mapped onto the final push |

One department, two postures — the contract (§3, §7, §8) is identical in both.

---

## 10. Full Role Roster (DevOps)

| Seat | Kind | Duty |
|---|---|---|
| Director of DevOps | Human | Runs every command; DNS + SSL; executes the authorized deployment; confirms each phase |
| DevOps Architect | AI advisory | Pre-deployment verification; readiness + risk review; instructions and plan review; never self-authorizes |
| DevOps Engineer | AI execution | Authors the deployment package from structured intake; maintains it across redeploys |
| Operator (final release authority) | Human | Authorizes the release that DevOps executes |

---

## 11. Artifact Registry (DevOps)

| Artifact | Canonical filename | Produced by | Consumed by |
|---|---|---|---|
| Deployment package | `init-app.sh` · `cloudbuild.yaml` · `Dockerfile` · `deploy.sh` | DevOps Engineer | Director of DevOps |
| Deployment checklist / run record | `DEPLOYMENT_CHECKLIST.md` | DevOps Engineer (pre-filled) → Director (completed) | Gate D, audit |
| Release identity record | in checklist (§7 chain) | Director of DevOps | QA (Gate D), rollback |
| Gate D evidence package | per `QA_PLAYBOOK.md` | Director of DevOps + DevOps Architect | QA Lead |
| Secrets inventory | intake table (§4.3) → Secret Manager | DevOps Engineer + Director | init-app.sh, audits |

---

## 12. Amendment Ledger

**A — Existing doctrine already aligned**

- A-1 · Canonical filenames (ruled 2026-08-23) — encoded in the deploy skills.
- A-2 · Gate D definition and DevOps evidence duty — `QA_PLAYBOOK.md` §13.
- A-3 · Client-platform promotion/rollback law — `TRM_PLAYBOOK.md` §9.
- A-4 · DevOps Architect seat — ruled 2026-08-23 (FFM operating model D-1); this doc is its department charter.

**D — Newly introduced doctrine (first formalized at Tier 1 here)**

- D-1 · **DevOps as a cross-cutting department** with one contract across FFM/BIM/TRM and the two platform postures (§9).
- D-2 · **Intake boundary law** (§3): certified-and-identified revisions only; refusal is mandatory.
- D-3 · **Guidance-only law** (§2) and the **Actor A/B/C identity model** (§5), promoted from skill practice to doctrine.
- D-4 · **Redeployment path** (§6): Phase-3-only standard for existing services.

**F — Open items** → §13.

---

## 13. Open Items (fenced — NOT v1.0 doctrine)

- F-1 · **Staging → production promotion doctrine** for factory-owned apps (Cloud Run staging → client-facing production) — still the factory's biggest undefined seam; carried from the factory ledger.
- F-2 · **DevOps Architect occupant** — deliberately unassigned (responsibility over vendor); assignment when field runs demand it.
- F-3 · **Monitoring / incident detection** post-deploy (feeds Loop 3 intake before a ticket exists) — undefined; carried from the factory seam list.
- F-4 · **Non-Next.js deployment packages** (Python/ADK services deploy today via project-specific scripts) — fold into the package doctrine when a second generator skill exists.
- F-5 · **Gate D mapping on client platforms beyond Vercel** — confirm per new client platform.

---

## 14. Definition of Done — per deployment

- [ ] Intake boundary satisfied: Gate Q PASS · release authorized · revision identified · Gate D plan exists
- [ ] DevOps Architect pre-deployment verification: READY
- [ ] Package current; secrets classified (build/runtime × public/secret) and present
- [ ] Director executed phases with per-phase verification; actor identity stated throughout
- [ ] DNS + SSL live (or platform-native equivalent); smoke verification green
- [ ] Release identity chain recorded; rollback path confirmed and bookmarked
- [ ] Gate D evidence package delivered to QA; Gate D verdict issued
- [ ] Checklist archived as the run record

**Done looks like:** a reader who has never seen our conversations can trace a certified revision from the intake boundary through package, phased human-executed deployment, and identity recording — to a Gate-D-verified live environment with a one-step rollback path, knowing which seat owned every action and which artifact crossed every boundary.

---

## 15. Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-08-24 | Initial operating model. Charters DevOps as the cross-cutting fourth department: DevOps Architect seat, intake boundary law, canonical package + structured intake, Actor A/B/C identity model, guidance-only law, phased execution with redeploy path, release identity + rollback, Gate D interface, two platform postures. Status REVIEW pending Operator ratification. |
