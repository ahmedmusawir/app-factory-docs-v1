# 🏭 APP FACTORY BLUEPRINT

> **Version:** 2.2 · **Date:** 2026-10-16 · **Status:** Active
> **Tier:** 1 — Constitution · **Pairs with:** SOFTWARE_FACTORY_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, ARCHITECT_PLAYBOOK, DESIGNER_PLAYBOOK, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE

> *The Stark Protocol — the factory constitution: who does what, in what order, with human approval gates.*

---

## THE BIG PICTURE

```text
Phase 0 — Recon: Engineer inspects facts and records the current target state.
Phase 1 — Ignition: Architect authors APP_BRIEF and DATA_CONTRACT before Design; Director approves scope.
Phase 2 — Design: Designer authors UI_SPEC and the visual package; Architect reconciles assembly.
Phase 3 — Engineering (spec): Architect completes the module, ACCEPTANCE_SPEC and prepared QAM; FILE_TREE optional.
Phase 4 — Fabrication (build): Director releases Engineering; Engineer builds and completes factual handoff.
  Director commits/pushes the completed numbered product candidate; QA branch starts at that exact commit.
  QA Executor Q1 recon and plan → QA Lead approval → Director release → QA Executor Q2.
  Conditional authorized Engineer repair and independent retest remain on the continuing QA branch.
  QA Lead product verdict → required cleanup and QA Lead cleanup acceptance → Architect closeout.
  Engineer bounded closeout → Director final commits, merge and push; retain candidate and evidence identities.
  Review checkpoint 1: after FFM build and its independent QA finish; disposition findings; RRM only for approved repairs.
  Complete remaining Engine 1 phases/modules and their QA; include Gate D before closing deployment-requiring work.
Phase 5 — Deployment: authorized operator deploys only within existing context-specific permissions.
  QA independently verifies the deployed revision at Gate D; production confirmation/recovery as applicable.
  Review checkpoint 2: Engine 2 after all Engine 1 phases/modules and their QA are closed.
  Disposition findings; RRM only for approved repairs; a clean review requires no RRM.
  Review, Gate Q, cleanup acceptance, Gate D and Director release remain separate decisions.
```

Engine and review vocabulary: `SOFTWARE_FACTORY_PLAYBOOK.md` §2, “Phase Vocabulary — One Canonical Map”. Deployment requirements: `DEPLOYMENT_PLAYBOOK.md`; Gate D: `QA_PLAYBOOK.md` §13.

Revised workflow documents and stick diagrams: [FFM creation](../03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md), [FFM execution and post-FFM review](../03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md), [deployment](../03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md), [BIM and Engine 2](../03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md). They supersede the historical August pictures when verified and published; originals are retained.

## 🔀 WHICH PIPELINE AM I IN?

The factory runs **two pipelines**. Route every project before any authoring begins. (Router source: `FFM_PLAYBOOK.md` §4 — the detailed variant doctrine lives there.)

| | **CONVERSION** | **GREENFIELD** |
|---|---|---|
| **When** | A working source app exists (Streamlit, Gradio, prototype) | No source app — a new build on a starter kit |
| **Flow** | Brain Drain → 4-file handoff package → Engineer (Claudy) | Architect → Designer → Engineer |
| **Designer?** | No — visuals come from source-app screenshots in `_design/` | Yes — the token file is the PRIMARY design deliverable |
| **Detail owned by** | `HANDOFF_PACKAGE_PLAYBOOK.md` | The agent playbooks (`ARCHITECT_PLAYBOOK.md`, `DESIGNER_PLAYBOOK.md`, `ENGINEER_PLAYBOOK.md`) |

**The operator router (condensed from FFM_PLAYBOOK §4):**

1. **Is there an existing app we're converting?** Yes → CONVERSION. No → GREENFIELD.
2. **If converting: has Brain Drain been run on the source repo?** No → run Brain Drain first; the 11 extracts are the package's evidence base.
3. **If greenfield: what is the design ground truth?** Wireframes / Designer output → goes in `_design/`. Brand tokens only → the style tile must land before screens. Nothing yet → Designer work blocks; surface to operator.

Hybrids (a greenfield build that inherits data shapes from a related repo's extracts) are treated structurally as GREENFIELD, with `_extraction/` repurposed for the related-repo evidence.

**Artifact ownership:** the Architect owns DATA_CONTRACT before Design. The Designer owns UI_SPEC. The Architect reconciles the assembled package and Engineering consumes its approved revision. Conversion evidence informs those contracts; greenfield does not transfer authorship to Engineering. FILE_TREE is optional; implementation structure and boundaries must remain explicit in the approved package.

---

## 📚 FACTORY DOCUMENT STRUCTURE

### Phase 1: ARCHITECT (Scope & Constraints)

| Document | Purpose | Owner |
|----------|---------|-------|
| `APP_BRIEF.md` | What we're building, why, constraints, pipeline | Architect |
| `ARCHITECT_PLAYBOOK.md` | How to BE the Architect agent | Factory |

---

### Phase 2: DESIGNER (UX & Visuals)

| Document | Purpose | Owner |
|----------|---------|-------|
| `globals.css` / `globals.scss` (+ Tailwind map) | The token file — executable system, all modes. **Primary deliverable.** | Designer |
| `UI_SPEC.md` | Component hierarchy, layout, gating, states, UX rules | Designer |
| `_design/` | Versioned folder of design artifacts: style tile + per-screen **HTML + PNG** | Designer |
| `COMPONENT_MANIFEST.md` | Primitives per screen + KIPs to build first | Designer |
| `DESIGNER_PLAYBOOK.md` | How to BE the Designer agent (token-driven HTML workflow + Canonical Page Method) | Factory |

---

### Phase 3: ENGINEERING (Architect Contract Assembly)

| Document | Purpose | Owner |
|----------|---------|-------|
| `DATA_CONTRACT.md` | All data shapes, API payloads, state objects; approved before Design | Architect |
| `DB_SCHEMA.md` | Database tables, relationships, indexes | Architect |
| `API_SPEC.md` | Endpoints, methods, auth, error codes | Architect |
| `FILE_TREE.md` (optional) | Supplementary structure view; approved package still states implementation structure and boundaries | Architect assembly |
| `ENGINEER_PLAYBOOK.md` | How to BE the Engineer agent | Factory |

---

### Phase 4: IMPLEMENTATION (Code Execution)

| Tool | Role | Prompted By |
|------|------|-------------|
| **Claude Code (Claudy)** | Writes code from specs; builds from the Designer's HTML, verifies against the PNG | Engineer Agent |
| **Windsurf/Cascade** | Reviews, refactors, catches issues | You + Engineer |

---

## 🔎 PHASE 0: RECON (BEFORE ANY AUTHORING)

Every run starts with recon. No APP_BRIEF, no design work, no specs until the target repo is ground-truthed.

- **Who:** the Engineer — a read-only pass over the target repo / starter kit.
- **How:** per `RECON_QUESTIONNAIRE.md` (the `stark-recon` skill).
- **Output:** a **Recon Report** — what the kit actually provides: versions, auth model, existing primitives, schema reality.
- **Consumer:** the Architect reads the Recon Report before authoring the brief. Disk establishes implementation facts; approved briefs govern scope and governing documents control their subjects. Route genuine conflicts to the Director.

> Applies to BOTH pipelines. A handoff package or brief authored without a current Recon Report is invalid.

---

## 🔄 THE FULL WORKFLOW

```text
Phase 0 — Recon: Engineer inspects facts and records the current target state.
Phase 1 — Ignition: Architect authors APP_BRIEF and DATA_CONTRACT before Design; Director approves scope.
Phase 2 — Design: Designer authors UI_SPEC and the visual package; Architect reconciles assembly.
Phase 3 — Engineering (spec): Architect completes the module, ACCEPTANCE_SPEC and prepared QAM; FILE_TREE optional.
Phase 4 — Fabrication (build): Director releases Engineering; Engineer builds and completes factual handoff.
  Director commits/pushes the completed numbered product candidate; QA branch starts at that exact commit.
  QA Executor Q1 recon and plan → QA Lead approval → Director release → QA Executor Q2.
  Conditional authorized Engineer repair and independent retest remain on the continuing QA branch.
  QA Lead product verdict → required cleanup and QA Lead cleanup acceptance → Architect closeout.
  Engineer bounded closeout → Director final commits, merge and push; retain candidate and evidence identities.
  Review checkpoint 1: after FFM build and its independent QA finish; disposition findings; RRM only for approved repairs.
  Complete remaining Engine 1 phases/modules and their QA; include Gate D before closing deployment-requiring work.
Phase 5 — Deployment: authorized operator deploys only within existing context-specific permissions.
  QA independently verifies the deployed revision at Gate D; production confirmation/recovery as applicable.
  Review checkpoint 2: Engine 2 after all Engine 1 phases/modules and their QA are closed.
  Disposition findings; RRM only for approved repairs; a clean review requires no RRM.
  Review, Gate Q, cleanup acceptance, Gate D and Director release remain separate decisions.
```

Engine and review vocabulary: `SOFTWARE_FACTORY_PLAYBOOK.md` §2, “Phase Vocabulary — One Canonical Map”. Deployment requirements: `DEPLOYMENT_PLAYBOOK.md`; Gate D: `QA_PLAYBOOK.md` §13.

## 📋 ENGINEERING PACKAGE: APPROVED CONTRACT ARTIFACTS

The Architect assembles the approved contract artifacts below for the Engineer to implement. DATA_CONTRACT is authored before Design; FILE_TREE is optional when implementation structure and boundaries are otherwise explicit.

### **DATA_CONTRACT.md**
```markdown
# Data Contract: Pepper's Video Rig

## State Objects

### ProjectState
{
  project_name: string
  profile: "youtube_standard" | "youtube_shorts" | ...
  created_at: ISO timestamp
  stages: {
    starter: { status, input_method, input_text }
    script: { status, content, word_count, approved }
    metadata: { status, titles[], description, hashtags, approved }
    audio: { status, file_path, duration_seconds, approved }
    images: { status, count, paths[], approved }
    video: { status, file_path, size_mb }
  }
}

### Config.json (per project)
{
  project_name: string
  profile: string
  approvals: { script: bool, audio: bool, images: bool }
  paths: { ... }
}
```

### **DB_SCHEMA.md** (if needed)
For Pepper's Rig = NOT NEEDED (file-based)
For CyberLorians = YES (Supabase tables)

### **API_SPEC.md** (if needed)
For Pepper's Rig = NOT NEEDED (local only)
For CyberLorians = YES (REST/GraphQL endpoints)

### **FILE_TREE.md** (optional)

The Architect may include a structure view when useful. The approved package must still define implementation structure and boundaries. Root tool-instruction alignment is separately tracked; an older required-FILE_TREE statement does not change the Director-approved artifact model.

---

## 📄 PLAYBOOK DOCS

| Playbook | Contents |
|----------|----------|
| `ARCHITECT_PLAYBOOK.md` | Questionnaire, output template, approval criteria, handoff checklist |
| `DESIGNER_PLAYBOOK.md` | Token-driven HTML workflow, Canonical Page Method, deliverables, handoff |
| `ENGINEER_PLAYBOOK.md` | Data contract template, file tree rules, Claudy prompting strategy, review protocol |

> Agent-conduct doctrine (the Karpathy Protocol, D-011) lands with the ENGINEER_PLAYBOOK rewrite — pointer reserved here.

---

## 🎯 YOUR BLIND SPOTS (COVERED)

| Blind Spot | Solution |
|------------|----------|
| "What does the Designer actually produce?" | Token file (primary) + style tile + per-screen HTML/PNG + UI_SPEC + component manifest |
| "What does the Engineer actually produce?" | Implementation and factual handoff against approved contracts; contract changes return to the Architect and Director |
| "How does the Engineer talk to Claudy?" | Structured prompts with specs + the Designer's HTML/tokens attached |
| "Who reviews Claudy's output?" | You + Windsurf/Cascade, with the Designer's PNG as the QC target |
| "What if Claudy breaks existing code?" | Approved scope and structure boundaries govern; stop, report the regression, and repair only within authorization |
| "How do we version this?" | Record the project-declared artifact locations and governing canonical names, header versions and Hub commit; preserve intentional pins until an authorized update. No universal `/docs` landing path. |

---

## 🚀 IMMEDIATE NEXT STEPS

1. **You:** Work with the Designer agent — lock tokens, then the canonical screen.
2. **Designer:** Build the canonical screen as token-driven HTML, render light + dark via Playwright, bring it back for the lock gate.
3. **Before Design:** Architect prepares DATA_CONTRACT. After the Designer authors UI_SPEC and the screen set is approved, the Architect reconciles the full package. FILE_TREE is optional; structure and boundaries remain explicit.
4. **Then:** We prompt Claudy together, with the HTML + tokens in hand.

---

## Version History

| Version | Date | Change |
|---|---|---|
| (unversioned) | — | Original blueprint: 3-agent council, Stitch as the UI generator, multi-vendor agent lineup. |
| 2.0 | 9 Jun 2026 | **Stitch retired.** Pipeline diagram, doc structure, and Phase 2 workflow rebuilt around token-driven HTML → Playwright PNG. Designer deliverables corrected (token file primary; `_design/` HTML+PNG; UI_SPEC; component manifest). `STITCH_PROMPTS/` folder replaced by `_design/`. Stale vendor parentheticals dropped from the diagram (agents shown role-only). Engineer tool labeled Claudy (Claude Code). Pepper's Rig example retained as illustration. |
| 2.1 | 7 Jul 2026 | **Wave 1 (audit sync).** Standard header block adopted, version/date moved to top (F-018). Title "AI App Factory" → "App Factory" (F-008). Phase 0 — Recon added to the lifecycle + workflow diagram: Engineer ground-truths per RECON_QUESTIONNAIRE / stark-recon, Architect consumes the Recon Report (F-003). "Which Pipeline Am I In?" router promoted from FFM_PLAYBOOK §4 — Conversion vs Greenfield, ownership split: HANDOFF_PACKAGE_PLAYBOOK = conversion detail, agent playbooks = greenfield detail (F-030). Per-pipeline DATA_CONTRACT ownership stated (F-029). Karpathy Protocol pointer placeholder reserved (D-011). Cross-references canonical-name only (F-011). |
| 2.2 | 2026-10-16 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-004, FC-008, FC-017, FC-027, MC-04, MC-06, MC-07, RUL-01, RUL-05, RUL-07, RUL-09, RUL-10, RUL-12, RUL-14 |
