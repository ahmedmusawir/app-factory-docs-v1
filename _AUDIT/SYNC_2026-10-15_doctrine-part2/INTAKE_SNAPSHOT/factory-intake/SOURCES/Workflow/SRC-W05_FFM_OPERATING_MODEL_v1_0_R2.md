# APP FACTORY — FFM OPERATING MODEL
## Loop 1: FFM Creation → Execution → QA → Deployment

> **Version:** 1.0 (working revision **R2**) · **Date:** 2026-08-24
> **Status:** REVIEW — Operator rulings ratified; full operating-model doctrine reconciliation pending final Operator approval.
> **Tier:** 1 — Factory Operating Model · **Owner:** Stark Industries App Factory
> **Provenance:** Field-derived from the FFM/10x Lab proving run plus two real-world FFM deliveries that reached Google Cloud staging (three completed FFM runs in total), with the independent QA model additionally hardened through the ADK Harness BIM campaign. Ratified inputs: six Operator rulings issued 2026-08-23 against the three-part process diagrams.
> **Companion visuals:** APP FACTORY PART 1–3 diagrams (Whimsical). The diagrams are simplified process maps; **this document is the full contract. Diagram omission does not mean process omission.** Where they differ, this document wins.

---

## 1. Executive Explanation — What Loop 1 Is

Loop 1 is the factory's **CREATE loop**: the governed path by which a raw application idea becomes a deployed, independently certified frontend running on cloud staging that a client can click.

It answers one question: *"Can we transform an idea into something a client can actually see and use?"*

Loop 1 is one of three factory loops (Loop 2 — MATURE: backend, integrations, security; Loop 3 — OPERATE: production support). This document covers **Loop 1 only**. The other loops appear solely where a boundary must be explained.

The delivery vehicle of Loop 1 is the **FFM — Frontend First Module**: a portable, self-contained folder that tells an AI coding agent what to build, how to build it, and what not to touch.

**The service seam.** Project-specific domain/backend data is built behind the approved service seam — a service layer whose mock implementations can later be replaced by real backend implementations (Loop 2's job) without rewriting the UI. **Kit-provided infrastructure primitives are the exception:** where the starter kit already provides a complete infrastructure primitive (e.g., kit auth), it is consumed directly per the Starter Kit Handbook and Kit Audit — never wrapped in a redundant project service. *(This preserves the seam doctrine without resurrecting the historical `authService.ts` failure mode.)*

Loop 1's lifecycle, in full:

| Stage | Name | Question answered |
|---|---|---|
| 0 | Recon | What is actually on disk before anyone authors anything? |
| 1 | FFM Creation | How does an idea become a complete, buildable module? |
| 2 | FFM Execution & QA | How is the module built, and how is the claim of completion independently certified? |
| 3 | FFM Deployment | How does a certified module reach client-visible cloud staging? |

*(The three companion diagrams cover Stages 1–3; Recon is a mandatory prerequisite even where omitted from the simplified visuals.)*

The system's first principle: **AI performs specialist work; it does not own authority.** Every department is headed by a human Director. Every release decision is human.

---

## 2. The Human Control Model — Directors

**Each department combines human authority with specialist AI intelligence. Execution may be AI-driven or human-operated depending on the nature of the work.** Not every department requires three AI seats. The three department patterns in Loop 1:

```text
DEVELOPMENT                     QA (FFM, canonical v1.0)        DEVOPS

Director of Development         Director of QA                  Director of DevOps
        +                               +                               +
Software Architect (AI)         QA Lead — GPT "Sol" (AI)        DevOps Architect (AI)
        ↓                               ↓                               ↓
Engineer — Claude Code          Sol designs the attack          DevOps Engineer (AI)
"Claudy" (AI executes)          → Director of QA performs
                                  manual/browser execution
                                → Sol adjudicates evidence
                                  (AI verdict)
```

The Director is **not** another AI agent and is never automated away. The Director:

- communicates with the department's AI seats and carries context between departments
- approves scope and plans; resolves ambiguity; adjudicates flagged conflicts
- can personally execute work (and in canonical FFM QA, does — see §6)
- holds the department's human approval authority

Operating philosophy, ruled: **an Engineer is never unleashed unsupervised.** Every execution seat — AI or human — works under a Director plus an Architect-class advisor.

> Terminology note: existing playbooks use **Operator / Coordinator** for the human authority. The Director model refines this into per-department seats. Today one person (the Operator) holds all Director chairs; the seats are defined so they can later be held by different people. See Amendment Ledger, item C-1.

---

## 3. Stage 0 — Recon (mandatory prerequisite)

Factory law, restated as part of this full contract: **no current Recon Report → no APP_BRIEF, no FFM authoring.**

```text
APP IDEA
    ↓
Target repo / starter kit identified
    ↓
PHASE 0 — RECON
Engineer (Claudy) performs read-only ground-truth inspection (stark-recon)
    ↓
RECON REPORT — agent_docs/recon/RECON_<project>_<phase>_<date>.md
    ↓
Director of Development + Software Architect review verified ground
    ↓
FFM Creation begins
```

Rules:

- Recon is **read-only**. Nothing is created, fixed, or improved during recon.
- The **Engineer is the ground-truth instrument**; the report follows `RECON_QUESTIONNAIRE.md`.
- **Where docs and disk disagree, disk wins.**
- The Architect authors **from the current Recon Report**, never from documentation alone (`ARCHITECT_PLAYBOOK.md` §2, Recon Mode).
- *Simplified in diagram; full contract defined here* — the Part 1 diagram begins at the idea/discussion step by design.

---

## 4. Stage 1 — FFM Creation

### 4.1 Flow

```text
RECON REPORT reviewed (Stage 0 complete)
   ↓  (discussion)
Director of Development  ⇄  SOFTWARE ARCHITECT
   ↓
Architect deliverables: APP_BRIEF.md · DATA_CONTRACT.md · _project/CLAUDE.md · other FFM files
   ↓
Director carries APP_BRIEF + DATA_CONTRACT (+ reference visuals, context) to the DESIGNER
   ↓
Designer works the DESIGNER_PLAYBOOK, iterating with the Director until approval
   ↓
Designer deliverables: token file (primary) · style tile · screen artifacts · UI_SPEC.md · component manifest
   ↓
ALL deliverables RETURN to the SOFTWARE ARCHITECT
   ↓
Architect ASSEMBLES + VERIFIES the integrated FFM · package FREEZES
   ↓
COMPLETE FFM → Engineer
```

### 4.2 FFM Assembly — the ruling (simplified in diagram; full contract here)

**The Software Architect is the final assembler and verifier of the FFM.** The Part 1 diagram shows Architect and Designer streams flowing directly into the FFM tree; that is visual shorthand. The actual contract:

```text
Architect deliverables ─────┐
Designer deliverables ──────┼──► SOFTWARE ARCHITECT ──► assemble + verify integrated FFM
Other required evidence ────┘                            ↓
                                                  freeze package → Engineer
```

No FFM reaches Engineering except through Architect assembly and verification. Existing doctrine already recognizes the Architect as producer of the complete FFM (`FFM_PLAYBOOK.md`: "Architect ──[ complete FFM ]──▶ Engineer"), **but** the playbook's detailed authoring sequence has the Operator filling `_design/` and `_extraction/` after Architect authoring — that sequence requires upstream amendment so all streams return to the Architect for final assembly, verification, and freeze. See Amendment Ledger, item B-3.

### 4.3 Designer input — the ruling

The Designer receives **both** `APP_BRIEF.md` **and** `DATA_CONTRACT.md`, plus any reference UI images and context the Director supplies.

**The Designer designs against approved contract data shapes — never ad-hoc fields invented during design.** `DATA_CONTRACT.md` is authoritative for the shapes available to the frontend; those shapes may initially be represented by typed mock data behind the service seam. The Designer must not invent fields outside the approved contract. Loop 2 later makes the real backend satisfy that same contract. *(Operator ruling amending prior greenfield doctrine — see Amendment Ledger, item B-1.)*

### 4.4 The FFM package (field-proven anatomy)

```text
<project>_<phase>_ffm/
├── CLAUDE.md / README.md / AGENTS.md / GEMINI.md     ← entry points
├── _project/    CLAUDE.md · APP_BRIEF.md · DATA_CONTRACT.md · UI_SPEC.md
├── _design/     tokens/ · style-tile/ · screens/ · COMPONENT_MANIFEST.md · logos · reference/
├── _extraction/ evidence docs (when an extraction source exists; else "N/A — greenfield" README)
├── skills/      stark-frontend-first (service-seam + mock-data doctrine)
├── playbook/    00-OVERVIEW → 07-RETROSPECTIVE · RETROSPECTIVES/
└── verification/ BUILD_CHECKLIST.md · PHASE_GATES.md
```

One FFM covers **one phase of one project** — no mega-FFMs. The folder freezes at Engineer handoff.

---

## 5. Stage 2 — FFM Execution

### 5.1 Flow

```text
COMPLETE FFM
   ↓
ENGINEER (Claude Code "Claudy") — Plan Mode first; builds only after approval
   ↑ supervision throughout:
   Director of Development (approvals & directions)
   Software Architect (verification & advisory)
   ↓
Internal build stages (Development gates, self-testing, approvals)
   ↓
Engineering declares the FFM complete + self-verified
   ↓
ACCEPTANCE_SPEC.md finalized
   ↓
Handoff to QA department
```

### 5.2 Rules of execution

- The Engineer runs **zero git and zero cloud commands** — those belong to the Director.
- The Engineer's scope is intentionally narrow; global vision is withheld by design. The Director and Architect hold the map; the Engineer holds the task.
- Internal stage gates during the build are **Development gates** — supervision instruments, not QA. They must never be confused with Gate Q.
- The Architect does not disappear at handoff; it remains the architectural verifier for the whole run.

### 5.3 QA cadence — the ruling

Independent QA engages **once, at module close** — not after every internal phase. The Part 2 diagram's "Phase 1 Complete → QA" is visual compression of the completion handoff. One module-level `ACCEPTANCE_SPEC.md` covers the completed FFM.

---

## 6. The Acceptance Contract

`ACCEPTANCE_SPEC.md` is the contract handed from Engineering to QA. **It is not the QA test plan.**

- Criteria are **seeded from the approved module contract** (Architect/Operator-defined) before implementation.
- The Engineer **maintains and finalizes** the spec at handoff, synchronized with approved scope — and may not silently add, remove, weaken, or redefine a requirement.
- Requirements are numbered `AC1, AC2, …`, testable and observable. "Works correctly" is a banned phrasing.
- Environment/setup prerequisites are called out **first**.
- The spec states in-scope, out-of-scope, regression expectations, manual-only acceptance points, and known limitations.

Principle: *the Engineer does not grade his own paper, and does not write his own exam either.*

---

## 7. Stage 2 — Independent QA and Gate Q

**Canonical QA source:** `QA_PLAYBOOK.md` is the factory-wide QA doctrine — QA independence, Gate Q, Gate D, verdict vocabulary, QA-vs-Engineering separation, and deployed-environment verification are defined there. Module classes (FFM, BIM, FIX, FEAT) **apply** that doctrine within their class; BIM doctrine is an implementation of it, not its source.

```text
QA_PLAYBOOK.md → factory-wide QA doctrine
BIM / FFM / FIX / FEAT → apply that doctrine within their module class
```

### 7.1 The Red Team model

```text
BLUE TEAM builds.                RED TEAM verifies.

Director of Development          Director of QA
+ Software Architect             + QA Lead — GPT "Sol"
↓                                ↓
Claudy → BUILD                   attack design → human-executed evidence → AI-adjudicated VERDICT
```

Sol is a **separate, independent GPT-class session** — never the build-side Architect or Engineer context wearing a QA hat. Epistemic independence is the point: the module's blind spots must not become the QA plan's blind spots.

### 7.2 Canonical FFM QA flow — the ruling

```text
ACCEPTANCE_SPEC.md
   ↓
QA Lead (Sol) designs the independent attack:
   QA plan · test cases · happy paths · negative paths · transitions
   ↓
Director of QA performs the required manual/browser test operations
   ↓
Evidence returns to Sol
   ↓
Sol adjudicates the evidence and issues the QA verdict + report
   ↓
FAIL → Engineering (fix under Development supervision) → QA retest
PASS → GATE Q → CERTIFIED READY FOR DEPLOYMENT
```

**Codex is not part of canonical FFM QA v1.0.** FFM QA is predominantly frontend/browser/user-flow verification, where the highest-value evidence is human visual interaction. Codex remains a **reserve technical QA execution agent** for module classes where CLI work, scripts, database inspection, or machine-verifiable commands justify it (e.g., BIM). *(Ruled.)*

### 7.3 Gate Q — the certification boundary (per `QA_PLAYBOOK.md` §12)

- Gate Q sits **after Engineer self-verification and before release approval**; it is the full pre-deployment QA verdict — mandatory for all code-bearing modules. Only documentation-only, non-runtime changes may receive a recorded Operator QA waiver.
- QA reviews **completed, frozen** work only.
- Evidence bar is symmetric: claims and findings cite reproducible steps, payloads, or file:line; findings without evidence are returned unread.
- Verdict vocabulary (factory-wide, no local dialects): **PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED.**
- A Gate D plan exists **before** deployment (Gate Q checklist requirement).

Nothing deploys without Gate Q.

---

## 8. Stage 3 — FFM Deployment

### 8.1 The DevOps department (new doctrine introduced by Loop 1)

```text
Director of DevOps  ⇄  DEVOPS ARCHITECT (pre-deployment verification & advisory)
        ↓
DEVOPS ENGINEER (authors the deployment package)
```

The **DevOps Architect** is a distinct factory function — the DevOps counterpart of the Software Architect. It: performs pre-deployment architectural verification; reviews deployment readiness; identifies risks and missing prerequisites; advises the Director of DevOps; prepares precise instructions for the DevOps Engineer; reviews the Engineer's proposed execution plan; helps verify the resulting package. It does **not** independently authorize infrastructure changes. No permanent model/vendor is assigned in v1.0 — the responsibility is defined, not the vendor. *(Ruled; new doctrine — Amendment Ledger D-1.)*

### 8.2 Flow

```text
GATE Q PASS — FFM repo complete, certified ready for deployment
   ↓
Final release authorization (Operator authority — §9)
   ↓
DevOps Architect: pre-deployment verification → READY
   ↓
DevOps Engineer authors the deployment package:
   init-app.sh · cloudbuild.yaml · Dockerfile · deploy.sh
   ↓  (commands hand-off & verification)
Director of DevOps — hands on keyboard:
   runs commands in Cloud CLI · executes deploy.sh
   sets up DNS (DigitalOcean) · SSL verification
   ↓
DEPLOYED FFM — Google Cloud (Cloud Run) staging
   ↓
GATE D (§8.4)
```

### 8.3 Canonical deployment filenames — the ruling

```text
init-app.sh · cloudbuild.yaml · Dockerfile · deploy.sh
```

Exactly these. Diagram spellings `initscript.sh` and `clouddeployment.yaml` are retired as naming drift.

### 8.4 Gate D — deployed-environment verification (per `QA_PLAYBOOK.md` §13)

A successful deploy command is not Gate D. A healthy container is not Gate D. A green build is not Gate D. **Gate D verifies the actual deployed revision.** Local development proves code behavior; production build proves packaging; the deployed environment proves the system.

Gate D preserves the same QA responsibility model as Gate Q:

```text
DEPLOYED STAGING REVISION
        ↓
QA Lead (Sol) designs the Gate D verification
        ↓
Director of QA performs required manual/browser/environment checks
        ↓
DevOps provides deployment identity and technical evidence
   (repo → branch → commit → image → Cloud Run revision → environment → DNS → HTTPS; rollback path maintained)
        ↓
Evidence returns to Sol
        ↓
Sol adjudicates → GATE D VERDICT
```

Sol may inspect technical evidence directly where tools permit, but for canonical FFM browser/UI verification the **Director performs the hands-on steps; Sol owns the independent QA reasoning and verdict.** A deploy-requiring module is never CLOSED before its Gate D (no deployment in scope → recorded "Gate D: N/A — reason").

---

## 9. Release Authority — the separation of powers

Factory law: **QA owns the verification verdict. Human authority owns the release decision.** And: **departmental approval is not the same thing as final product release authorization.**

| Seat | Owns |
|---|---|
| QA Lead (Sol) | The QA verdict — Gate Q and Gate D adjudication |
| Director of QA | QA operations: manual execution, evidence collection, human QA oversight |
| **Operator as final release authority** | The human decision to move an approved revision forward |
| Director of DevOps | Execution of the *authorized* deployment |

A Gate Q PASS certifies quality; it does not itself release. Today one human occupies Development, QA, DevOps, and final Operator authority simultaneously — the responsibilities nevertheless remain separate seats so the factory stays scalable when different humans hold them later.

---

## 10. Full Role Roster

| Seat | Kind | Department | Duty in Loop 1 |
|---|---|---|---|
| Director of Development | Human | Development | Approves scope & plans; directs the run; owns git; carries context |
| Software Architect | AI advisory | Development | Authors APP_BRIEF, DATA_CONTRACT, `_project/CLAUDE.md` from the Recon Report; assembles + verifies + freezes the FFM; verifies during execution |
| Designer | AI specialist | Development (design function) | Produces the design package from APP_BRIEF + DATA_CONTRACT under the Designer Playbook |
| Engineer ("Claudy", Claude Code) | AI execution | Development | Runs Stage 0 recon (read-only); Plan Mode → build → self-verify → finalize ACCEPTANCE_SPEC → retrospective; zero git/cloud |
| Director of QA | Human | QA | Drives the QA run; performs the manual/browser test execution; collects evidence |
| QA Lead ("Sol", GPT-class) | AI advisory | QA | Independent attack design; evidence adjudication; owns the QA verdict (Gate Q + Gate D) |
| Codex | AI execution (reserve) | QA | Not in canonical FFM QA v1.0; reserve for CLI/script-heavy classes (e.g., BIM) |
| Director of DevOps | Human | DevOps | Runs all cloud commands, deploy.sh, DNS, SSL; executes the authorized deployment |
| DevOps Architect | AI advisory | DevOps | Pre-deployment verification; readiness review; instructions for the DevOps Engineer |
| DevOps Engineer | AI execution | DevOps | Authors init-app.sh, cloudbuild.yaml, Dockerfile, deploy.sh |
| Operator (final release authority) | Human | Factory | Authorizes release beyond departmental approvals; final adjudication |

Boundary law: **Directors decide. Architects advise and verify. Engineers execute within the approved plan.** One person may hold multiple chairs; the responsibilities never merge.

---

## 11. Artifact Registry — canonical filenames

| Artifact | Canonical filename | Produced by | Consumed by |
|---|---|---|---|
| Recon Report | `agent_docs/recon/RECON_<project>_<phase>_<date>.md` | Engineer (read-only recon) | Architect, Director of Development |
| Application brief | `APP_BRIEF.md` | Software Architect | Designer, Engineer, QA |
| Data contract | `DATA_CONTRACT.md` | Software Architect *(greenfield — ruled; see B-1)* | Designer, Engineer |
| Project spine | `_project/CLAUDE.md` | Software Architect | Engineer |
| UI specification | `UI_SPEC.md` | Designer *(final ownership: proposed — see E-1)* | Architect (assembly), Engineer |
| Token file (primary design artifact) | `globals.css` + Tailwind map | Designer | Engineer |
| Style tile | HTML + PNG | Designer | Director approval, Engineer |
| Screen artifacts | HTML + PNG per screen | Designer | Engineer (HTML builds, PNG QCs) |
| Component manifest | `COMPONENT_MANIFEST.md` *(naming: open item F-2)* | Designer | Engineer |
| Acceptance contract | `ACCEPTANCE_SPEC.md` | Seeded by contract; Engineer finalizes | QA Lead |
| QA plan | `QA_PLAN.md` | QA Lead (Sol) | Director of QA |
| QA verdict/report | Per `QA_PLAYBOOK.md` | QA Lead (Sol) | Directors, Operator |
| Retrospective | `RETROSPECTIVE.md` / `RUN_NNN_LESSONS.md` | Engineer | Next module's Architect |
| Deployment package | `init-app.sh` · `cloudbuild.yaml` · `Dockerfile` · `deploy.sh` | DevOps Engineer | Director of DevOps |

---

## 12. Amendment Ledger

**A — Existing doctrine already aligned (no change needed)**

- A-1 · Stage 0 Recon law: mandatory, read-only, disk-wins, Architect authors from the report — `ARCHITECT_PLAYBOOK.md` §2 (Recon Mode), `RECON_QUESTIONNAIRE.md`, `APP_FACTORY_BLUEPRINT.md` Phase 0.
- A-2 · QA doctrine: independence, Gate Q (§12), Gate D (§13), verdict vocabulary, Engineer-self-verification → QA intake → Gate Q → deploy → Gate D — **`QA_PLAYBOOK.md` is the canonical factory-wide source.** BIM doctrine restates it as a module-class implementation.
- A-3 · Engineer conduct: Plan Mode, zero git/cloud, narrow scope, retrospectives — `ENGINEER_PLAYBOOK.md`, `FFM_PLAYBOOK.md`.
- A-4 · Designer deliverable set + HTML/PNG rule — `GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` §8.
- A-5 · QA cadence at module close with one module-level `ACCEPTANCE_SPEC.md` — aligned with `QA_PLAYBOOK.md` / BIM-derived practice.

**B — Operator rulings requiring upstream doctrine amendment**

- B-1 · **Greenfield `DATA_CONTRACT.md` ownership → Software Architect, authored before Design.** Conflicts with: `ENGINEER_PLAYBOOK.md` §3 (F-029 box); `APP_FACTORY_BLUEPRINT.md` line 95 (artifact table), line 259, line 271; `HANDOFF_PACKAGE_PLAYBOOK.md` §5.2 line 131; `ARCHITECT_PLAYBOOK.md` §1 diagram. Note: `ARCHITECT_PLAYBOOK.md` §2 already lists DATA_CONTRACT as Architect-authorable — the playbook is internally inconsistent and needs reconciliation both ways.
- B-2 · **Designer receives DATA_CONTRACT as a primary input** (with APP_BRIEF). Amends the same sections as B-1 plus the Blueprint's Phase 2 input description.
- B-3 · **FFM final assembly — PARTIALLY ALIGNED / UPSTREAM AMENDMENT REQUIRED.** Existing doctrine already recognizes the Architect as producer of the complete FFM (`FFM_PLAYBOOK.md` handoff discipline). However, the detailed authoring sequence and anatomy annotations (`FFM_PLAYBOOK.md` §5 — `_design/`/`_extraction/` "filled by Designer + Operator"; §6 handoff-completeness signals; §7 Authoring Sequence; §10 file-by-file guide) describe the Operator filling those folders after Architect authoring. Amend so Designer/evidence outputs **return to the Architect for final assembly, verification, and freeze** before Engineer handoff.

**C — Operator rulings that clarify (terminology/positioning, low-risk edits)**

- C-1 · **Director model** refines Operator/Coordinator into per-department human seats. Existing docs keep "Coordinator/Operator" validly; new Tier-1 docs use Director language with this mapping stated.
- C-2 · **Diagram doctrine:** the three Part diagrams are simplified process maps; this document is the governing contract. Diagram omission ≠ process omission.

**D — Newly introduced doctrine (first formalized here)**

- D-1 · **DevOps Architect seat** (§8.1) — exists in no prior playbook; future DevOps doctrine must adopt it.
- D-2 · **Sol as named independent QA Lead; Codex as reserve QA execution agent** with the FFM-vs-BIM applicability rule (§7.2). Canonical FFM QA execution is human (Director of QA).
- D-3 · **Canonical deployment filenames** (§8.3) — to be encoded in the deploy skills' docs where drift exists.

**E — Proposed reconciliation pending Operator ratification**

- E-1 · **`UI_SPEC.md` final ownership → Designer.** Proposed model: Architect owns product intent (APP_BRIEF); Designer owns the final screen + interaction specification; Architect reviews/verifies UI_SPEC during final FFM assembly. Architecturally coherent and compatible with portions of current Designer/Blueprint doctrine — but **not an Operator ruling**. Current doctrine language ("drafted by Architect, revised by Designer" — `GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` §8; `HANDOFF_PACKAGE_PLAYBOOK.md`) stands until Tony ratifies or rejects.

**F — Open items** → §13.

---

## 13. Open Items (fenced — NOT v1.0 doctrine)

- F-1 · **`FILE_TREE.md` vs `FOLDER_TREE` — naming and ownership.** Blueprint assigns `FILE_TREE.md` to the Engineer; the notebook flow places a folder tree with the Architect at creation time. Unruled. Until ruled, `FILE_TREE.md` (Engineer) remains doctrine.
- F-2 · **Component artifact naming.** `COMPONENT_MANIFEST.md` (per-project, in-FFM) vs "Components Registry" usage vs the factory-level `COMPONENT_REGISTRY.md` doc. Proposed distinction (registry = factory doctrine; manifest = project output) awaits ruling.
- F-3 · **Staging → production promotion doctrine** — undefined; Loop 1 ends at certified staging.
- F-4 · **BIM package upgrades** (standing `verification/` folder; example payload fixtures) — logged for `BIM_PLAYBOOK` v1.1, evidence pass over BIM-001…005 first.
- F-5 · **Loop 2/Loop 3 positioning artifacts** (FFM→BIM canonical visual, TRM evidence from DockBloxx) — outside Loop 1 scope, tracked at factory level.

*(Former O-6 — QA doctrine source sync — CLOSED: `QA_PLAYBOOK.md` is available and canonical; see A-2.)*

---

## 14. Definition of Done — Loop 1, per module

- [ ] **Stage 0:** current Recon Report exists and was reviewed before any authoring
- [ ] FFM assembled, verified, and frozen by the Software Architect
- [ ] Engineer build complete; internal Development gates green; self-verification recorded
- [ ] `ACCEPTANCE_SPEC.md` finalized (AC-numbered, testable, prerequisites first)
- [ ] Independent QA engaged: Sol designed the attack; Director of QA executed; Sol adjudicated
- [ ] **Gate Q: PASS** — certified ready for deployment; Gate D plan exists
- [ ] Final release authorization given (Operator authority)
- [ ] DevOps Architect pre-deployment verification: READY
- [ ] Deployment package authored (`init-app.sh`, `cloudbuild.yaml`, `Dockerfile`, `deploy.sh`)
- [ ] Director of DevOps executed deploy; DNS + SSL live; staging URL up
- [ ] **Gate D:** Sol-designed verification executed by Director of QA against staging; release identity recorded; rollback path confirmed; verdict issued
- [ ] Retrospective written honestly; lesson candidates flagged for doctrine promotion

**Done looks like:** a reader who has never seen our conversations can trace an idea through recon, into an assembled FFM, through supervised engineering, into an independent QA certification at Gate Q, and through DevOps onto Gate-D-verified Google Cloud staging — knowing who owns every decision and which artifact crosses every boundary.

---

## 15. Version History

| Version | Date | Change |
|---|---|---|
| 1.0 (draft) | 2026-08-23 | Initial synthesis: three-part diagrams, six Operator rulings, Director model, drift review. |
| 1.0 **R2** | 2026-08-24 | Surgical doctrine-reconciliation pass. Stage 0 Recon restored to the full contract; FFM assembly reclassified as partially aligned with upstream amendment (B-3); `QA_PLAYBOOK.md` made canonical QA source and O-6 closed; human-control model corrected (execution may be human or AI per department); Gate D restated with Sol-designs / Director-executes / Sol-adjudicates; release authority separated from departmental approval; "real data shapes" → "approved contract data shapes"; service-seam rule qualified with the Kit Audit exception; provenance tightened to evidence; UI_SPEC ownership moved to E (pending ratification); status set to REVIEW pending full Operator approval. |
