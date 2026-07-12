# 🏭 APP FACTORY BLUEPRINT

> **Version:** 2.1 · **Date:** 2026-07-07 · **Status:** Active
> **Tier:** 1 — Constitution · **Pairs with:** SOFTWARE_FACTORY_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, FFM_PLAYBOOK, ARCHITECT_PLAYBOOK, DESIGNER_PLAYBOOK, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE

> *The Stark Protocol — the factory constitution: who does what, in what order, with human approval gates.*

---

## THE BIG PICTURE

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        YOU (TONY STARK)                                 │
│                    Commander / Final Approver                           │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        ▼                           ▼                           ▼
┌───────────────┐           ┌───────────────┐           ┌───────────────┐
│   ARCHITECT   │    ──►    │   DESIGNER    │    ──►    │   ENGINEER    │
└───────────────┘           └───────────────┘           └───────────────┘
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐        ┌──────────────────┐        ┌───────────────┐
│  APP_BRIEF.md │        │  Token file      │        │ DATA_CONTRACT │
│               │        │  + UI_SPEC.md    │        │ + FILE_TREE   │
│               │        │  + HTML/PNG      │        │               │
└───────────────┘        └──────────────────┘        └───────────────┘
                                    │                           │
                                    ▼                           ▼
                         ┌──────────────────────┐     ┌───────────────┐
                         │  TOKEN-DRIVEN HTML    │     │  CLAUDE CODE  │
                         │  → PLAYWRIGHT PNG     │     │  (Claudy)     │
                         └──────────────────────┘     └───────────────┘
```

> The Designer **builds the screens directly** as token-driven HTML and renders them to PNG with Playwright. There is no external UI-generation tool in the loop.

---

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

**DATA_CONTRACT ownership differs per pipeline.** In a CONVERSION run, the Architect **pre-authors** `DATA_CONTRACT.md` before handoff, from Brain Drain evidence (the API-surface extract). In a GREENFIELD run, the Engineer **authors** it from the approved `APP_BRIEF.md` + `UI_SPEC.md`. Same artifact name — different author, different moment. Know which run you're in before touching it.

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

### Phase 3: ENGINEER (Data & Code)

| Document | Purpose | Owner |
|----------|---------|-------|
| `DATA_CONTRACT.md` | All data shapes, API payloads, state objects | Engineer |
| `DB_SCHEMA.md` | Database tables, relationships, indexes | Engineer |
| `API_SPEC.md` | Endpoints, methods, auth, error codes | Engineer |
| `FILE_TREE.md` | Exact folder/file structure for codebase | Engineer |
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
- **Consumer:** the Architect reads the Recon Report BEFORE authoring the brief. Where any doc and reality disagree, **reality wins**.

> Applies to BOTH pipelines. A handoff package or brief authored without a current Recon Report is invalid.

---

## 🔄 THE FULL WORKFLOW

```
PHASE 0: RECON (Engineer, read-only)
├── Engineer runs: stark-recon per RECON_QUESTIONNAIRE on the target repo
├── Engineer produces: Recon Report
└── Checkpoint: Architect consumes the Recon Report before authoring ✓

PHASE 1: IGNITION (You + Architect)
├── You provide: Idea, constraints, vibe
├── Architect produces: APP_BRIEF.md
└── Checkpoint: You approve APP_BRIEF ✓

PHASE 2: DESIGN (You + Designer)
├── Designer receives: APP_BRIEF.md + Tailwind version + token well
├── Designer locks tokens: globals.css/scss (all modes)
├── Designer builds canonical screen: token-driven HTML → Playwright PNG (light + dark)
├── Designer clones-and-adapts: remaining screens from the canonical HTML
├── Designer produces: style tile + per-screen HTML/PNG + UI_SPEC.md + component manifest
└── Checkpoint: You approve the canonical lock, then the screen set ✓

PHASE 3: ENGINEERING (You + Engineer)
├── Engineer receives: APP_BRIEF.md + UI_SPEC.md + token file + HTML/PNG
├── Engineer produces:
│   ├── DATA_CONTRACT.md (all data shapes)
│   ├── DB_SCHEMA.md (if applicable)
│   ├── API_SPEC.md (if applicable)
│   └── FILE_TREE.md (exact structure)
└── Checkpoint: You approve all specs ✓

PHASE 4: FABRICATION (You + Engineer + Claudy)
├── Engineer prompts: Claudy with specs + the Designer's HTML/tokens
├── Claudy writes: actual code files, inheriting the token file
├── You review: in Windsurf with Cascade, PNG as the QC target
├── Iterate: fix issues, refine
└── Checkpoint: Working code ✓

PHASE 5: DEPLOYMENT (You)
├── Test locally
├── Deploy to target (Cloud Run, Vercel, local exe)
└── Ship it 🚀
```

---

## 📋 ENGINEER AGENT: WHAT IT PRODUCES

The Engineer's full output list:

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

### **FILE_TREE.md**
```
peppers_video_rig/
├── app.py                 # Streamlit entry
├── config/
│   └── defaults.py        # Default prompts, settings
├── services/
│   ├── transcriber.py     # YouTube → text
│   ├── script_writer.py   # Text → script
│   ├── metadata_gen.py    # Script → titles/desc
│   ├── audio_gen.py       # Script → MP3
│   ├── image_gen.py       # Script → images
│   └── video_composer.py  # Audio + images → MP4
├── ui/
│   ├── sidebar.py         # Navigation component
│   ├── tab_projects.py
│   ├── tab_starter.py
│   ├── tab_script.py
│   ├── tab_metadata.py
│   ├── tab_audio.py
│   ├── tab_images.py
│   └── tab_video.py
├── utils/
│   ├── file_manager.py    # Project folder ops
│   ├── state_manager.py   # config.json read/write
│   └── logger.py          # Logging utility
├── projects/              # User projects live here
├── requirements.txt
└── run.bat                # Windows launcher
```

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
| "What does the Engineer actually produce?" | DATA_CONTRACT + DB_SCHEMA + API_SPEC + FILE_TREE |
| "How does the Engineer talk to Claudy?" | Structured prompts with specs + the Designer's HTML/tokens attached |
| "Who reviews Claudy's output?" | You + Windsurf/Cascade, with the Designer's PNG as the QC target |
| "What if Claudy breaks existing code?" | FILE_TREE.md = source of truth; Engineer enforces "don't touch what works" |
| "How do we version this?" | Each project gets a `/docs` folder with all .md files; `_design/` holds versioned HTML/PNG |

---

## 🚀 IMMEDIATE NEXT STEPS

1. **You:** Work with the Designer agent — lock tokens, then the canonical screen.
2. **Designer:** Build the canonical screen as token-driven HTML, render light + dark via Playwright, bring it back for the lock gate.
3. **After the screen set locks:** Engineer produces `DATA_CONTRACT.md` + `FILE_TREE.md`.
4. **Then:** We prompt Claudy together, with the HTML + tokens in hand.

---

## Version History

| Version | Date | Change |
|---|---|---|
| (unversioned) | — | Original blueprint: 3-agent council, Stitch as the UI generator, multi-vendor agent lineup. |
| 2.0 | 9 Jun 2026 | **Stitch retired.** Pipeline diagram, doc structure, and Phase 2 workflow rebuilt around token-driven HTML → Playwright PNG. Designer deliverables corrected (token file primary; `_design/` HTML+PNG; UI_SPEC; component manifest). `STITCH_PROMPTS/` folder replaced by `_design/`. Stale vendor parentheticals dropped from the diagram (agents shown role-only). Engineer tool labeled Claudy (Claude Code). Pepper's Rig example retained as illustration. |
| 2.1 | 7 Jul 2026 | **Wave 1 (audit sync).** Standard header block adopted, version/date moved to top (F-018). Title "AI App Factory" → "App Factory" (F-008). Phase 0 — Recon added to the lifecycle + workflow diagram: Engineer ground-truths per RECON_QUESTIONNAIRE / stark-recon, Architect consumes the Recon Report (F-003). "Which Pipeline Am I In?" router promoted from FFM_PLAYBOOK §4 — Conversion vs Greenfield, ownership split: HANDOFF_PACKAGE_PLAYBOOK = conversion detail, agent playbooks = greenfield detail (F-030). Per-pipeline DATA_CONTRACT ownership stated (F-029). Karpathy Protocol pointer placeholder reserved (D-011). Cross-references canonical-name only (F-011). |
