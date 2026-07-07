# FFM PLAYBOOK — Frontend-First Module Authoring Manual

> **Audience:** Future Architects (human or agent) authoring a Frontend-First Module (FFM) for any project's any phase.
> **Purpose:** A self-contained, end-to-end guide so the reader can produce a complete, working FFM without hunting through old repos or scattered docs.
> **Version:** v1.1 (2026-06-18) — added mandatory **Gate M (mobile shell)** to §13.1 + authoring checklist (Rule Zero as an enforced gate, not just spec advice; after RUN_002 missed shipping a mobile shell). Prev: v1.0 (June 2026).
> **Owner:** Stark Industries — AI App Factory
> **Pairs with:** `HANDOFF_PACKAGE_PLAYBOOK.md`, `APP_FACTORY_SKILLS_PLAYBOOK.md`, `SOFTWARE_FACTORY_PLAYBOOK.md`, `ARCHITECT_PLAYBOOK.md`, `ENGINEER_PLAYBOOK.md`

---

## Table of Contents

1. [What an FFM Is, In One Page](#1-what-an-ffm-is-in-one-page)
2. [The Four-Role Factory Pattern](#2-the-four-role-factory-pattern)
3. [FFM Anatomy — The Folder Structure](#3-ffm-anatomy--the-folder-structure)
4. [The Two FFM Variants — Conversion vs Greenfield](#4-the-two-ffm-variants--conversion-vs-greenfield)
5. [Naming Conventions](#5-naming-conventions)
6. [Phase Scoping — One FFM Per Phase](#6-phase-scoping--one-ffm-per-phase)
7. [Authoring Sequence](#7-authoring-sequence)
8. [File-By-File Authoring Guide — Root Files](#8-file-by-file-authoring-guide--root-files)
9. [File-By-File Authoring Guide — `_project/`](#9-file-by-file-authoring-guide--_project)
10. [File-By-File Authoring Guide — `_design/` and `_extraction/`](#10-file-by-file-authoring-guide--_design-and-_extraction)
11. [File-By-File Authoring Guide — `skills/`](#11-file-by-file-authoring-guide--skills)
12. [File-By-File Authoring Guide — `playbook/`](#12-file-by-file-authoring-guide--playbook)
13. [File-By-File Authoring Guide — `verification/`](#13-file-by-file-authoring-guide--verification)
14. [The Extractor Question — When To Run Brain Drain](#14-the-extractor-question--when-to-run-brain-drain)
15. [Custom Brain Drain Prompts](#15-custom-brain-drain-prompts)
16. [Bridging The FFM Into The Starter Kit](#16-bridging-the-ffm-into-the-starter-kit)
17. [Common Authoring Stumbles](#17-common-authoring-stumbles)
18. [The Authoring Checklist](#18-the-authoring-checklist)
19. [Evolution And Versioning](#19-evolution-and-versioning)
20. [Worked Examples](#20-worked-examples)
21. [Appendix A — Skeleton Folder Tree](#21-appendix-a--skeleton-folder-tree)
22. [Appendix B — Boot Prompts](#22-appendix-b--boot-prompts)
23. [Appendix C — Template Files (Stubs To Copy)](#23-appendix-c--template-files-stubs-to-copy)

---

## 1. What an FFM Is, In One Page

A **Frontend-First Module (FFM)** is a portable, self-contained folder dropped at `agent_docs/CURRENT_APP/<project>_<phase>_ffm/` inside a starter kit clone. It is the single source of truth that tells an AI coding tool (Claude Code, Codex CLI, Gemini CLI, etc.) **what to build, how to build it, and what not to touch.**

An FFM bundles:

- **Navigation** — entry-point files that route AI tools through the module
- **Doctrine** — the operating rules, forbidden zones, and conflict resolution order
- **Specification** — APP_BRIEF (scope), DATA_CONTRACT (data shapes), UI_SPEC (screens)
- **Methodology** — a frontend-first skill and a phase-by-phase playbook
- **Verification** — approval gates and a build checklist
- **Evidence** — design references and extraction artifacts (when applicable)

One FFM covers one project's one phase. When that phase closes, a new FFM is authored for the next phase, informed by the lessons of the previous run.

The FFM exists because **AI coding tools need structured context to stay on-task.** Without an FFM, a session drifts: invented data shapes, out-of-scope features, forbidden zones violated, doctrine forgotten. With an FFM, the AI reads a deterministic boot sequence, confirms understanding, and stays in scope through phase completion.

The FFM is **vendor-neutral** — Claude Code, Codex, Gemini all use the same module via different entry-point files (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`) that redirect to the same navigation contract.

---

## 2. The Four-Role Factory Pattern

The FFM lives inside a four-role pipeline. Understanding the pipeline matters because **each role's outputs feed the next role's inputs**, and skipping or reordering breaks the chain.

### The Roles

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   1. DESIGNER       2. EXTRACTOR      3. ARCHITECT     4. ENGINEER  │
│   ─────────         ─────────         ─────────        ─────────    │
│   Designer +        Claudy +          Architect        Engineer     │
│   Operator          Extractor +       (Claude in       (Claudy in   │
│                     Operator          chat)            terminal)    │
│                                                                     │
│   PRODUCES:         PRODUCES:         PRODUCES:        PRODUCES:    │
│   Brand tokens      Brain Drain       The FFM          Working code │
│   Style tile        extracts          folder           per the FFM  │
│   Wireframes        (11 evidence-                                   │
│   Stitch output     labeled docs)                                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                │                │                │
                ▼                ▼                ▼
        Feeds _design/   Feeds _extraction/   Feeds _project/
                                                       │
                                                       ▼
                                              Claudy reads FFM,
                                              builds the phase,
                                              operator reviews
                                              at each gate.
```

### Role 1 — Designer

**Who:** A visual designer (human, or a Designer Agent with Stitch).
**With:** Operator (you).
**Produces:** Design artifacts that become the visual ground truth.

**Outputs:**
- Brand tokens (primary color hex, accent colors, font choice)
- Logo files (color SVG, mono SVG, favicon)
- Style tile (typography ramp, button styles, color samples — single image or Figma export)
- Wireframes (for new screens — Stitch output or Figma frames)
- High-fidelity screen designs (if available)
- Reference screenshots of the prior version or competitor (if applicable)

**Handoff target:** `_design/` folder inside the FFM.

**Quality bar:**
- Brand tokens are concrete (hex codes, not "brand-ish blue")
- Logo files are usable as-is (right dimensions, transparent background)
- Style tile is current (not from a prior abandoned direction)
- Wireframes cover every screen in the FFM's scope

**Failure modes if Designer work is incomplete:**
- AI defaults to shadcn zinc baseline — looks generic
- Operator iterates on design AFTER components are built — rework
- Style tile drifts from final result — debt

### Role 2 — Extractor

**Who:** Claudy operating under the **Brain Drain** skill (or equivalent extraction skill).
**With:** Operator (you), providing the source repo URL or clone.
**Produces:** 11 evidence-labeled extraction documents capturing the source app's architecture.

**Outputs (the 11 docs):**

| # | Document | Content |
|---|---|---|
| 00 | REPO-PROFILE.md | Repo identity, file tree, entry points, dependencies |
| 01 | EXISTING-DOCS-REVIEW.md | Existing docs validated against actual code |
| 02 | ARCHITECTURE-MAP.md | Flow map of the source app's primary user journeys |
| 03 | AGENT-LOOP.md | Request/response lifecycles (if AI-agent app) |
| 04 | TOOL-SYSTEM.md | API surface (HTTP routes, external services) |
| 05 | CONTEXT-AND-MEMORY.md | Session state, persistence, blob storage |
| 06 | PROMPTS-AND-PERSONA.md | Screen inventory (typically the fattest doc) |
| 07 | GUARDRAILS-AND-SANDBOXING.md | Auth gates, RLS, transport security |
| 08 | ERROR-HANDLING-AND-RECOVERY.md | Try/except map, sentinels, retry patterns |
| 09 | TESTS-AND-EVALS.md | Existing tests; GAP if none |
| 10 | RAW-FINDINGS-AND-QUESTIONS.md | Drifts, dead code, top 5 discoveries |

**Handoff target:** `_extraction/` folder inside the FFM.

**Quality bar (evidence discipline):**
Every line in every extraction document is labeled:
- **EVIDENCE** — directly found in a specific file with line number citation
- **INFERENCE** — reasonable conclusion from observed structure; basis stated
- **CLAIM** — documentation or operator says it; not independently verified
- **GAP** — expected component not found; what was expected and where searched
- **QUESTION** — needs operator clarification; phrased as an explicit question

This discipline is what makes extraction trustworthy. Without it, the Architect can't tell what was verified versus guessed.

**Failure modes if Extractor work is incomplete:**
- DATA_CONTRACT invents fields the source app doesn't have
- UI_SPEC describes screens that don't match the source
- Known discrepancies get "fixed" silently during conversion
- The Architect spends time re-extracting instead of authoring

**When you might skip the Extractor:**
- Greenfield projects with no source app to convert
- Phases that build on already-extracted upstream work
- Foundation skeleton phases where the starter kit is the spec

(More on this in [Section 14](#14-the-extractor-question--when-to-run-brain-drain).)

### Role 3 — Architect

**Who:** You, Claude (in a chat session, NOT in the terminal as a coding agent).
**With:** Operator (you).
**Produces:** The complete FFM folder, ready to drop at `agent_docs/CURRENT_APP/`.

**Outputs:** Every file in the FFM folder structure (see [Section 3](#3-ffm-anatomy--the-folder-structure)).

**Handoff target:** The starter kit's `agent_docs/CURRENT_APP/` directory.

**Quality bar:**
- Every section of every file is filled (no TBDs, no placeholders)
- Forbidden zones are concrete and enforceable (Claudy can verify violations)
- Hard gates are numbered, measurable, machine-verifiable where possible
- Cross-references between files resolve (DATA_CONTRACT references match UI_SPEC references)
- Conflict resolution order is stated clearly
- The skill (`stark-frontend-first`) is bundled inside the FFM at `skills/`

**Inputs the Architect needs:**
- The locked PHASE_ROADMAP (which phase is this FFM for?)
- The locked MASTER_APP_BRIEF (what's the whole project?)
- The Designer's outputs in `_design/` (or a clear "Designer hasn't produced these yet" signal)
- The Extractor's outputs in `_extraction/` (or a clear "Greenfield — no source to extract" signal)
- The starter kit's handbook and component registry
- Any prior FFM retrospectives (lessons from past runs)

**Failure modes if Architect work is incomplete:**
- Claudy hits ambiguity mid-build and stops (best case)
- Claudy improvises and builds the wrong thing (worst case)
- Operator has to author missing files mid-run, breaking flow
- The FFM has to be patched after Claudy has already drifted

### Role 4 — Engineer

**Who:** Claudy (Claude Code in the terminal).
**With:** Operator (you) at every approval gate.
**Produces:** Working code, tests, deployed services per the FFM's playbook.

**Outputs:**
- TypeScript types per DATA_CONTRACT
- Service-layer files per service contracts
- Mock data fixtures
- Components per UI_SPEC
- Tests per the playbook
- Deployed staging URLs
- A retrospective in `playbook/RETROSPECTIVES/RUN_NNN_LESSONS.md`

**Handoff target:** Real code in the starter kit clone; deployed services; retrospective for the next FFM.

**Quality bar:**
- All hard gates from APP_BRIEF green
- Smoke walkthrough passes
- Tests pass
- Retrospective drafted honestly (not sycophantically)

**Failure modes if Engineer work is rushed:**
- "Tests pass" claimed without verification
- Phase declared "done" with red gates
- Sycophantic retrospective ("everything went great!") that buries real lessons
- RECOVERY.md not updated; next session has no entry point

### Handoff Discipline

Each role hands off to the next with explicit deliverables. **No role advances without the previous role's outputs in hand.**

```
Designer ──[ design artifacts ]──▶ Architect
Extractor ──[ 11 docs ]──▶ Architect
Architect ──[ complete FFM ]──▶ Engineer
Engineer ──[ working code + retrospective ]──▶ Operator
Operator ──[ approval ]──▶ next phase's Architect
```

If a downstream role is blocked because an upstream role's outputs are missing, **the upstream role finishes first.** No "we'll fix it later." Lessons learned with this discipline (and without it) are why this playbook exists.

### Parallel Opportunities

Designer and Extractor can work in parallel — they have independent inputs and outputs. The Architect waits for both before authoring the FFM in earnest, though the Architect can scaffold the structure and reusable parts (skill, playbook, verification) while Designer and Extractor are still working.

The Engineer cannot run until the Architect ships a complete FFM.

---

## 3. FFM Anatomy — The Folder Structure

Every FFM follows the same folder structure. Names and content vary per project; structure does not.

```
<project>_<phase>_ffm/
│
├── CLAUDE.md             ← navigation contract (entry point for Claude Code)
├── README.md             ← operator's setup guide
├── AGENTS.md             ← Codex CLI pointer → redirects to CLAUDE.md
├── GEMINI.md             ← Gemini CLI pointer → redirects to CLAUDE.md
│
├── _project/             ← PROJECT-SPECIFIC content (filled per run)
│   ├── CLAUDE.md         ← project spine (forbidden zones, tech stack, doctrine)
│   ├── APP_BRIEF.md      ← scope, hard gates, success criteria
│   ├── DATA_CONTRACT.md  ← types, service contracts, mock requirements
│   └── UI_SPEC.md        ← screens, behavior, design system
│
├── _design/              ← visual reference (filled by Designer + Operator)
│   ├── README.md         ← what goes here, what's expected
│   ├── brand-tokens.md   ← summary of colors, fonts, logo refs (or stub)
│   ├── style-tile.png    ← visual reference (when available)
│   ├── logo-color.svg    ← brand logo
│   ├── logo-mono.svg     ← single-color variant
│   └── reference/        ← optional screenshots from prior version, etc.
│
├── _extraction/          ← extraction evidence (filled by Extractor + Operator)
│   ├── README.md         ← which extracts to drop here, why
│   └── (the 11 evidence-labeled docs from Brain Drain — or repurposed)
│
├── skills/               ← REUSABLE skills (travel across runs)
│   └── stark-frontend-first/
│       ├── CLAUDE.md     ← skill doctrine
│       ├── SKILL.md      ← Anthropic v2 methodology
│       ├── workflow/     ← 6 workflow files (00-discovery → 05-verification)
│       ├── references/   ← SERVICE_LAYER_PATTERNS, MOCK_DATA_PATTERNS, etc.
│       └── templates/    ← starter files (service, mock-data, types)
│
├── playbook/             ← REUSABLE phase-by-phase build instructions
│   ├── 00-OVERVIEW.md
│   ├── 01-DISCOVERY.md
│   ├── 02-TYPES.md
│   ├── 03-SERVICES.md
│   ├── 04-MOCKS.md
│   ├── 05-COMPONENTS.md
│   ├── 06-VERIFICATION.md
│   ├── 07-RETROSPECTIVE.md
│   └── RETROSPECTIVES/   ← per-run lessons (empty until first run completes)
│
└── verification/         ← REUSABLE approval gate criteria
    ├── PHASE_GATES.md    ← all gates and their criteria
    └── BUILD_CHECKLIST.md ← operator-runnable checklist
```

### What Each Folder Is For

**Underscore-prefixed folders** (`_project/`, `_design/`, `_extraction/`) contain **per-project content** — filled per run, replaced wholesale for the next FFM.

**Non-prefixed folders** (`skills/`, `playbook/`, `verification/`) contain **reusable Factory tooling** — copied forward to every new FFM, refined over time.

**Accumulating content** lives in `playbook/RETROSPECTIVES/` — one file per run, accumulated across runs to inform future authoring.

### The Reusability Matrix

| Item | Reusable Across Runs | Replaced Per Run | Accumulates |
|---|---|---|---|
| Root `CLAUDE.md` | ✅ (with minor edits) | | |
| Root `README.md` | ✅ (with minor edits) | | |
| `AGENTS.md`, `GEMINI.md` | ✅ | | |
| `_project/` (all files) | | ✅ | |
| `_design/` | | ✅ | |
| `_extraction/` | | ✅ | |
| `skills/stark-frontend-first/` | ✅ | | |
| `playbook/00-OVERVIEW.md` through `07-*.md` | ✅ (with phase-specific tuning) | | |
| `playbook/RETROSPECTIVES/RUN_NNN_*.md` | | | ✅ |
| `verification/` | ✅ (with hard-gate updates per phase) | | |

### Why This Structure

The structure encodes three principles:

1. **Discoverability** — an AI tool opening the FFM finds the entry point (`CLAUDE.md` at root) and follows the navigation chain. No hunting.

2. **Separation of concerns** — project-specific content is isolated in underscore-prefixed folders so it can be replaced wholesale without touching the reusable parts.

3. **Compounding leverage** — the reusable parts (skill, playbook, verification) get refined with every run. By Run 4 or 5, the playbook is tight enough for autonomous overnight runs.

### Vendor Neutrality

The FFM works with any AI coding tool that reads markdown:

| Tool | Entry File | Notes |
|---|---|---|
| Claude Code | `CLAUDE.md` | Primary, fully tested |
| Codex CLI | `AGENTS.md` → redirects to `CLAUDE.md` | Compatible |
| Gemini CLI | `GEMINI.md` → redirects to `CLAUDE.md` | Compatible |
| Windsurf / Cursor / other | `CLAUDE.md` directly | Compatible |

The doctrine inside is tool-agnostic. Tool-specific steps (like installing skills to `.claude/skills/`) are documented per tool, not baked into the module.

---

## 4. The Two FFM Variants — Conversion vs Greenfield

FFMs come in two flavors based on whether a source app exists to convert from.

### Variant A — Conversion FFM

**When to use:** A working prototype exists (Streamlit, Gradio, Python app, etc.) and the goal is to convert it to a production Next.js app.

**Examples:** The original FFM v1.0 (Cyberize Agentic Automation, May 2026) converted a Streamlit prototype.

**`_design/` contains:** Screenshots of the source app (the canonical visual reference).
**`_extraction/` contains:** The 11 Brain Drain extracts from the source repo.
**DATA_CONTRACT** is authored: From the Brain Drain `04-TOOL-SYSTEM.md` (API surface).
**UI_SPEC** is authored: From the Brain Drain `06-PROMPTS-AND-PERSONA.md` (screen inventory) plus the screenshots.
**The "Known Discrepancies" section** is critical: drift between the source app and the desired Next.js version is preserved as documentation, not "fixed" silently.

### Variant B — Greenfield FFM

**When to use:** No source app exists. The build is greenfield — starting from a starter kit with no prior implementation to mirror.

**Examples:** Cyber Pharma v1 Phase 1 FFM (June 2026) — foundation skeleton with no source app.

**`_design/` contains:** Brand tokens, style tile, wireframes (the visual ground truth replaces source app screenshots).
**`_extraction/` contains:** Either (a) data-shape evidence from upstream/related repos that inform what the new build should look like, or (b) a `README.md` documenting "N/A — greenfield, no source to extract."
**DATA_CONTRACT** is authored: From operator decisions, related repos' extracts, or the starter kit's existing schema.
**UI_SPEC** is authored: From wireframes and brand tokens.
**The "Known Discrepancies" section** may not apply or may be very thin.

### What Differs Between Variants

| Aspect | Conversion FFM | Greenfield FFM |
|---|---|---|
| Source app exists | Yes | No |
| `_design/` contents | Source app screenshots | Brand tokens + style tile + wireframes |
| `_extraction/` contents | 11 Brain Drain docs | Data-shape evidence from related repos OR N/A |
| DATA_CONTRACT source | Brain Drain TOOL-SYSTEM doc | Operator decisions, related extracts |
| UI_SPEC source | Brain Drain PROMPTS-AND-PERSONA + screenshots | Wireframes |
| Known Discrepancies relevance | High | Low / N/A |
| Authoring time | Faster (evidence pre-extracted) | Slower (operator decisions take time) |
| Failure mode | Inventing fields not in source | Operator decisions drift mid-build |

### How To Identify Which Variant You're Authoring

Ask the operator three questions:

1. **Is there an existing app we're converting?**
   - Yes → Conversion variant
   - No → Greenfield variant

2. **If yes, has Brain Drain been run on the source repo?**
   - Yes → 11 extracts go in `_extraction/`
   - No → Run Brain Drain first ([Section 14](#14-the-extractor-question--when-to-run-brain-drain))

3. **If no source app, what's the design ground truth?**
   - Wireframes / Stitch output → Goes in `_design/`
   - Brand tokens only (UI improvised) → Style tile must land before screens; surface this risk
   - Nothing yet → Designer work blocks. Surface to operator.

### A Note On Variant Hybrids

Some FFMs are **hybrid**: greenfield work that inherits data shapes from a related repo's extracts. Example: Cyber Pharma v1 Phase 1 is greenfield (no source UI to convert), but uses FRANK_API extracts to inform the eventual Phase 3 data contract.

For hybrids:
- Treat structurally as Greenfield (no source app screenshots in `_design/`)
- Repurpose `_extraction/` to hold the related-repo evidence
- Document the repurpose in `_extraction/README.md` so future readers understand
- Operator decisions still go in `_project/CLAUDE.md`

---

## 5. Naming Conventions

### FFM Folder Names

Format: `<project>_<phase>_ffm`

| Example | Project | Phase |
|---|---|---|
| `cyber_pharma_v1_phase1_ffm` | Cyber Pharma v1 | Phase 1 (Foundation Skeleton) |
| `cyber_pharma_v1_phase2_ffm` | Cyber Pharma v1 | Phase 2 (Visual Fidelity) |
| `super_admin_portal_phase1_ffm` | Super Admin Portal | Phase 1 |
| `stark_reads_phase1_ffm` | Stark Reads | Phase 1 |

Rules:
- All lowercase
- Underscores between segments (no spaces, no hyphens — spaces break shell tools, hyphens collide with shadcn class conventions)
- Project name first, phase second, `_ffm` suffix last
- Phase number always present (no `cyber_pharma_v1_ffm` ambiguity)
- Keep it short — 30 chars or less when possible

### Why This Format

- **Sortable** — alphabetical order also gives chronological order within a project
- **Greppable** — `*_ffm` finds all FFMs; `cyber_pharma_*` finds all phases of one project
- **Scannable** — operator glancing at `agent_docs/CURRENT_APP/` knows immediately what's there
- **Self-documenting** — no separate registry needed

### Subfolders And Files

- **Skill folder names:** kebab-case (`stark-frontend-first`)
- **Family folder names** (for skill families): SHOUTING_SNAKE (`CLOUD_DEPLOYMENT_SKILLS`)
- **Workflow files:** zero-padded numeric prefix (`00-discovery.md`, `01-types-and-contract.md`)
- **Reference files:** descriptive names, no prefix (`ANTI_PATTERNS.md`, `SERVICE_LAYER_PATTERNS.md`)
- **Underscore-prefixed folders:** project-specific content (`_project/`, `_design/`, `_extraction/`)

### Avoiding Name Collisions

If two FFMs exist for the same starter kit clone (rare but possible — main app + dependency module), name them distinctly:

```
agent_docs/CURRENT_APP/
├── cyber_pharma_v1_phase1_ffm/           ← main app foundation
└── cyber_pharma_v1_phase1_payments_ffm/  ← payments module foundation
```

The `_ffm` suffix in both makes them recognizable as modules; the qualifier in the middle distinguishes them.

---

## 6. Phase Scoping — One FFM Per Phase

### The Rule

**One FFM scopes one phase of one project.** Not the whole project. Not multiple phases.

This is intentional. The alternative — a mega-FFM covering all 8 phases of a project — has been tried in older Factory iterations and consistently fails because:

- Scope is too large for any one AI session
- Lessons from Phase 1 can't inform Phase 2 authoring if both are authored upfront
- Operator can't approve at fine-grained boundaries
- Forbidden zones can't be tuned per phase (Phase 1 forbids schema work; Phase 3 requires it)

### Authoring Cadence

```
Phase 0 (Ignition)           → No FFM. Planning docs locked.
Phase 1 (Foundation)         → Phase 1 FFM authored. Engineer runs. Retrospective.
Phase 2 (Visual Fidelity)    → Phase 2 FFM authored, informed by Phase 1 retrospective.
Phase 3 (Schema + RLS)       → Phase 3 FFM authored, informed by Phase 2 retrospective.
... etc.
```

Each FFM is authored **after** the previous phase's retrospective is in hand. Lessons compound.

### When To Author The Next FFM

Trigger conditions:
- Previous phase has closed (all hard gates green)
- Retrospective drafted by Engineer and reviewed by Operator
- Operator confirms readiness to start next phase
- Designer outputs for next phase (if needed) are ready

Do NOT pre-author multiple FFMs in advance. The whole point of phase-scoped FFMs is to incorporate lessons.

### Archival Pattern For Completed Phases

When a phase closes, the FFM doesn't get deleted — it gets **archived**.

Suggested pattern:

```
agent_docs/
├── current_app/                          ← active FFM lives here
│   └── cyber_pharma_v1_phase2_ffm/
└── completed_phases/                     ← archived FFMs live here
    └── cyber_pharma_v1_phase1_ffm/       ← closed, kept for reference
```

The archived FFM is read-only reference material. Future architects can grep it for patterns; future engineers can read its retrospective.

Some teams prefer to keep all FFMs in `current_app/` and use git tags / branches to mark phase completion. Either approach works; the discipline is **don't delete FFMs**.

---

## 7. Authoring Sequence

### High-Level Authoring Order

The Architect authors files in this order. Each step gets the previous step's outputs as inputs.

```
1. Scaffold the folder structure (mkdir, empty files)
2. Author the root navigation files (CLAUDE.md, README.md, AGENTS.md, GEMINI.md)
3. Author _project/APP_BRIEF.md FIRST (scope must be locked)
4. Author _project/DATA_CONTRACT.md SECOND (data shapes inform UI)
5. Author _project/UI_SPEC.md THIRD (screens built from data contract)
6. Author _project/CLAUDE.md LAST (project spine informed by the above three)
7. Author _design/README.md (instructions for operator on what to drop in)
8. Author _extraction/README.md (instructions for operator on what to drop in)
9. Author skills/stark-frontend-first/* (CLAUDE.md, SKILL.md, workflow, references, templates)
10. Author playbook/* (00-OVERVIEW through 07-RETROSPECTIVE)
11. Author verification/* (PHASE_GATES, BUILD_CHECKLIST)
12. Self-check (cross-references resolve, hard gates measurable, structure complete)
13. Package (zip the folder for handoff to operator)
14. Operator fills _design/ and _extraction/ with actual content (Architect's job is done at this point)
15. Operator drops FFM at agent_docs/CURRENT_APP/, boots Claudy
```

### Why APP_BRIEF First, CLAUDE.md Last

- **APP_BRIEF.md FIRST** — scope must be locked before contracts or screens can be specified
- **DATA_CONTRACT.md SECOND** — data shapes inform what the UI needs to display
- **UI_SPEC.md THIRD** — screens are built from the data contract
- **_project/CLAUDE.md LAST** — the spine is informed by the other three

If you author UI_SPEC before DATA_CONTRACT, you'll invent data shapes that don't match the source.
If you author CLAUDE.md before the others, you won't know the conventions to encode.

### Time Budget (Rough)

| Step | Time (single FFM, by an experienced Architect) |
|---|---|
| Scaffold + root nav files | 30 min |
| APP_BRIEF | 45-60 min |
| DATA_CONTRACT | 45-60 min |
| UI_SPEC | 60-90 min |
| _project/CLAUDE.md | 30-45 min |
| _design/README + _extraction/README | 15 min |
| skills/* | 45 min (mostly copied from previous FFM, lightly adapted) |
| playbook/* | 60-90 min (mostly copied from previous FFM, phase-tuned) |
| verification/* | 30 min |
| Self-check + package | 15 min |
| **Total** | **5-7 hours** |

The first FFM is slower (you're building the patterns). Subsequent FFMs are faster (you're copying skill/playbook/verification forward and only re-authoring `_project/`).

### Inputs The Architect Needs Before Starting

Confirm these are in hand:

- [ ] Locked PHASE_ROADMAP (which phase is this FFM for?)
- [ ] Locked MASTER_APP_BRIEF (whole project scope)
- [ ] Designer outputs in hand (or operator decision: "use shadcn defaults, iterate later")
- [ ] Extractor outputs in hand (or operator decision: "greenfield, no extracts needed")
- [ ] Starter kit handbook and component registry references
- [ ] Previous FFM retrospective (for non-first FFMs)
- [ ] Operator's "go" signal

If any input is missing, the Architect surfaces and waits. Don't author with stale or missing inputs.

---

## 8. File-By-File Authoring Guide — Root Files

The root of the FFM has four files: `CLAUDE.md`, `README.md`, `AGENTS.md`, `GEMINI.md`. Each has a specific role.

### 8.1 — Root `CLAUDE.md`

**Purpose:** The navigation contract for AI tools opening the FFM. Tells them what this module is, what reading order to follow, and what the precedence rules are.

**Audience:** Claudy (primary), Codex CLI / Gemini CLI / other coding agents (secondary).

**Required sections (in order):**

1. **Frontmatter / blockquote** — one-line description of what this file is
2. **What This Module Is** — name, version, what it does, who owns it
3. **What's Different About This FFM** (for variants) — table comparing to a baseline (e.g., conversion vs greenfield)
4. **Vendor Neutrality** — which tools it works with, how they enter
5. **Reading Order (MANDATORY)** — numbered list of files to read in order
6. **Folder Map** — ASCII tree of the FFM's structure
7. **Activation Contract** — the exact boot prompt the operator should paste
8. **Forbidden Zones (Hard Stops)** — what NOT to do; categorized
9. **Skill Inventory** — what skills ship with the FFM, what skills the operator installs separately
10. **What Is Reusable vs Per-Project** — table or list
11. **Evolution Principle** — how the FFM evolves across runs
12. **Version History** — changelog

**Length:** 250-400 lines.

**Critical disciplines:**
- The reading order MUST be deterministic. No "read whatever feels relevant."
- The forbidden zones MUST be enforceable. Claudy can verify violations.
- The folder map MUST match the actual disk structure (verify before zipping).
- The activation contract MUST be copy-pasteable verbatim.

**Common authoring mistakes:**

| Mistake | Why it hurts | Fix |
|---|---|---|
| Reading order says "read whatever's relevant" | Drift on every run | Numbered list, exact order |
| Forbidden zones say "no backend stuff" | Unenforceable, interpretable | "No API routes in /app/api/ beyond starter kit defaults. No Supabase migrations. No SQL beyond starter kit migrations." |
| Folder map doesn't match disk | Confusion at boot | Always verify with `find . -type f` before publishing |
| Activation contract is wordy / unclear | Operator skips it | One paragraph max, copy-paste ready |
| No "What's Different" section for variants | Future readers confused | Always include for non-baseline FFMs |

### 8.2 — Root `README.md`

**Purpose:** The operator's setup guide. Step-by-step instructions for staging the FFM, installing skills, booting Claudy.

**Audience:** The operator (you).

**Required sections (in order):**

1. **What This Is** — brief context for the operator
2. **Quick Start** — numbered steps: stage the module, fill `_project/`, fill `_design/`, fill `_extraction/`, install skills, verify stack, open Claude Code, issue boot prompt
3. **Bridging The Module Into Your Starter Kit** — the PROJECT_POINTER.md pattern (or older "edit starter kit root CLAUDE.md" pattern, depending on the operator's setup)
4. **The Run** — overview of the sub-phases Claudy will execute
5. **Operator Cheat Sheet** — recovery prompts, forbidden zone violation handling, gate-skip recovery
6. **Troubleshooting** — common issues and fixes
7. **Sequencing Note** — reminder that this FFM is for one phase only
8. **Credits** — who designed the module, who operates it
9. **Version**

**Length:** 250-350 lines.

**Critical disciplines:**
- Quick Start should be copy-paste runnable (real bash commands, real paths)
- Troubleshooting should cover the failures actually seen in past runs
- The boot prompt should be quoted verbatim with full path

**Common authoring mistakes:**

| Mistake | Fix |
|---|---|
| Boot prompt has `<PLACEHOLDER>` requiring operator find-replace | Specify the actual FFM folder name; less risk of error |
| Troubleshooting is generic | Capture real failure modes from past runs |
| No reference to PROJECT_POINTER pattern | Document if the operator's setup uses it |
| Skills install commands skip the cleanup step | Always include `rm -rf /tmp/anthropic-skills` |

### 8.3 — `AGENTS.md`

**Purpose:** Entry point for Codex CLI. Redirects to `CLAUDE.md`.

**Length:** 5-10 lines.

**Template:**

```markdown
# AGENTS.md

> Codex CLI entry point.

This module's primary navigation contract is at `CLAUDE.md` (sibling file). All AI coding tools — Claude Code, Codex CLI, Gemini CLI, Windsurf, Cursor — read the same `CLAUDE.md`.

**Read `CLAUDE.md` next.**
```

That's it. Don't duplicate doctrine here. The redirect is the whole point.

### 8.4 — `GEMINI.md`

**Purpose:** Entry point for Gemini CLI. Redirects to `CLAUDE.md`.

**Length:** 5-10 lines.

**Template:** Same as `AGENTS.md` but with Gemini-flavored header.

```markdown
# GEMINI.md

> Gemini CLI entry point.

This module's primary navigation contract is at `CLAUDE.md` (sibling file). All AI coding tools — Claude Code, Codex CLI, Gemini CLI, Windsurf, Cursor — read the same `CLAUDE.md`.

**Read `CLAUDE.md` next.**
```

### Why These Two Redirect Files Exist

Codex CLI looks for `AGENTS.md` by convention. Gemini CLI looks for `GEMINI.md`. Both should redirect to the canonical doctrine in `CLAUDE.md` so the FFM stays single-source-of-truth regardless of which tool opens it.

If you skip these files, Codex CLI users will either fail to find the FFM or improvise their own conventions, breaking vendor neutrality.

---

## 9. File-By-File Authoring Guide — `_project/`

The `_project/` folder is the **project-specific** content of the FFM. Four files. Each has a specific purpose. Author them in order: APP_BRIEF → DATA_CONTRACT → UI_SPEC → CLAUDE.md.

### 9.1 — `_project/APP_BRIEF.md`

**Purpose:** Scope and success criteria for this phase. The single source of truth for what's in scope and out of scope.

**Audience:** Claudy (primary), Operator (review).

**Required sections (in order):**

1. **Mission Of This Phase** — what this phase exists to do
2. **Hero Outcome** — one-sentence success measure
3. **In Scope** — bulleted list of what ships in this phase
4. **Out of Scope** — bulleted list of what does NOT ship in this phase
5. **Hard Gates** — numbered, measurable criteria (G1, G2, ...) for phase closure
6. **Success Criteria Table** — criterion + how to verify
7. **Known Risks** — risk + likelihood + mitigation
8. **Common Stumbles** — what to watch for during the run
9. **Estimated Effort** — sessions count
10. **Handoff To Next Phase** — what becomes available to the next phase's FFM
11. **Constraints** — non-negotiable rules
12. **Phase Transitions** — table showing where each phase fits in the overall roadmap
13. **Changelog**

**Length:** 250-400 lines for medium phases. Foundation skeleton phases (smaller scope) ~200 lines.

**Critical disciplines:**

- **Hard gates are numbered, not bulleted.** Bullets are unscannable in conversation. "Did G7 pass?" is unambiguous; "did the error boundary one pass?" is not.
- **Hard gates are measurable.** "Both apps deploy to staging" — verify with `curl`. "Brand applied" — verify with visual diff. "Feels good" — not a gate.
- **Out of scope is more important than in scope.** Spend more authoring time on out-of-scope items. Most stumbles are scope creep, not missing scope.
- **Every claim is evidence-traceable.** For conversions: cite Brain Drain doc. For greenfield: cite operator decision and record it in `_project/CLAUDE.md` § Operator Decisions.

**Common authoring mistakes:**

| Mistake | Fix |
|---|---|
| Hard gates as bullets, not numbered | Number them G1, G2, ... |
| Vague gates ("works well") | Replace with measurable criteria |
| Out-of-scope section is one bullet | Expand; this section is the most important |
| Hero outcome describes effort, not result | "Reviewer can click through every route and trust foundation is ready" — not "we built a thing" |
| Mission of phase repeats project mission | The phase's mission is narrower; be specific |
| In-scope list is aspirational | List what WILL ship, not what would be nice |

**Example hero outcomes (from real FFMs):**

> "A reviewer can click through every route on both apps, see that every role gate holds, log in as different test users to confirm different views, and trust that the foundation is ready for product work."

> "The chat screen renders all 5 agents from config.json. User can send a message, receive a response, switch agents, and see message history correctly."

Notice both are concrete, measurable, scoped to one phase.

### 9.2 — `_project/DATA_CONTRACT.md`

**Purpose:** Every data shape, every service contract, every mock requirement. The contract that both mock implementations and real backend implementations must satisfy.

**Audience:** Claudy (primary).

**Required sections (in order):**

1. **Tables In Play For This Phase** — database tables relevant to this phase (with field-by-field tables)
2. **Tables NOT In Play** — explicit list of tables that exist in the broader project but are NOT used in this phase
3. **Trigger / Function Inventory** — DB functions inherited from the starter kit (e.g., `handle_new_user()`)
4. **TypeScript Types** — every interface needed in this phase, with code blocks
5. **Service Contracts** — every method the UI calls, signatures, mock behavior, BACKEND_SWAP_NOTES
6. **Mock Data Strategy** — what mocks are needed, where they live, what they cover
7. **Future Phase Decision Points** — questions deferred to later phases (explicitly NOT decided now)
8. **Conflict Resolution** — what happens when code wants a shape not in this contract
9. **Changelog**

**Length:** 300-600 lines for medium phases. Data-heavy phases can be longer.

**Critical disciplines:**

- **Both mock and real must satisfy the contract.** If swapping the mock for a real backend requires changing the contract, the contract is wrong.
- **Wire format conventions matter.** Snake_case for DB-derived shapes (matches Supabase / FastAPI / Pydantic conventions). CamelCase for UI-internal types.
- **No `any` types ever.** Use `unknown` with narrowing if truly unknown.
- **Enum values as string literal unions**, not `enum` keyword (better tree-shaking, no runtime cost).
- **BACKEND_SWAP_NOTES per service method** — when the real backend lands, what does this method actually do?

**Common authoring mistakes:**

| Mistake | Fix |
|---|---|
| Inventing fields not evidenced | Trace every field to Brain Drain or operator decision |
| Mixed optionality conventions | Pick `?` everywhere or nullable everywhere, document the choice |
| Forgetting edge cases | Document empty array, error sentinel, timeout patterns |
| Documenting "ideal" instead of actual source | The contract describes reality, not aspiration |
| Service methods without BACKEND_SWAP_NOTES | Add notes explaining what real backend will need to provide |
| Adding Frank-domain types in Phase 1 | Phase 1 has no Frank tables — only auth-relevant types belong |

**Example service contract:**

```typescript
// /src/services/auth.ts (CONTRACT — not implementation)

export interface AuthService {
  /**
   * Get the current authenticated user with their role.
   * Returns null if no session.
   * BACKEND_SWAP_NOTES (Phase 2): wraps starter kit's getUser() with role join.
   */
  getCurrentUser(): Promise<AuthenticatedUser | null>;

  /**
   * Sign in with email/password. Returns user on success, throws on failure.
   * BACKEND_SWAP_NOTES (Phase 2): wraps starter kit's signInWithPassword().
   * On Phase 3, audit log entry created via trigger.
   */
  signIn(email: string, password: string): Promise<AuthenticatedUser>;
}
```

### 9.3 — `_project/UI_SPEC.md`

**Purpose:** Screen-by-screen behavior. Every screen specified with layout, content, behavior, state, error handling.

**Audience:** Claudy (primary).

**Required sections (in order):**

1. **Phase Screens — The Complete List** — table of every screen with route, route group, status (NEW / INHERITED / NEW PLACEHOLDER), description
2. **Layout & Navigation** — global layout descriptions for each app
3. **Per-Screen Specs** — one section per screen with:
   - Purpose
   - Content (with element-by-element specs)
   - Behavior (event handlers, redirects, validation)
   - Forbidden zones (what NOT to add)
4. **Error Boundaries** — which route groups need them, what they show
5. **Design System Scaffolding** — brand tokens, type ramp, spacing scale, color system, component tokens
6. **Mobile Breakpoints** — `sm` 640px, `md` 768px, `lg` 1024px, `xl` 1280px, `2xl` 1536px
7. **Loading & Empty States** — patterns to apply
8. **Accessibility Baseline** — labels, contrast, keyboard nav, focus
9. **Out Of Scope For This Phase UI** — explicit list
10. **Visual References** — pointer to `_design/`
11. **Conflict Resolution**
12. **Changelog**

**Length:** 400-700 lines for medium phases.

**Critical disciplines:**

- **Every screen's mobile behavior documented** (Rule Zero — mobile-first not "fix later")
- **Required breakpoints named per screen** if behavior differs
- **Every UI element maps to a Shadcn primitive** OR a kit common primitive (Page, Row, Box, AppShellPage); if no primitive fits, surface as a Kit Improvement Proposal
- **Loading, empty, error states specified** for every data-dependent screen
- **Component inventory** at the end suggesting the file tree for components

**Common authoring mistakes:**

| Mistake | Fix |
|---|---|
| Desktop-only specs with "mobile later" | Mobile FIRST per screen, desktop as progressive enhancement |
| Hand-waving state transitions | Name exact components (Spinner, ErrorState, EmptyState) |
| Forgetting empty / loading / error states | Add for every data-dependent screen |
| Missing markdown rendering spec (when assistant responses are markdown) | Specify `react-markdown + remark-gfm` and what plugins |
| Inventing components not in UI_SPEC | If Claudy needs a new component mid-build, STOP and update spec first |
| No touch target sizing for mobile | Add `min-h-[44px]` for buttons on mobile |

### 9.4 — `_project/CLAUDE.md`

**Purpose:** The project spine. Doctrine and conventions specific to this project. Read every session.

**Audience:** Claudy (read at every session start).

**Required sections (in order):**

1. **Project Identity** — name, phase, repos, source, mission
2. **Hero Outcome** — same as APP_BRIEF § 2 (intentional redundancy)
3. **Forbidden Zones (Hard Stops)** — same as APP_BRIEF, expanded with category headers
4. **Tech Stack** — table verified against starter kit
5. **What Phase Ships** — same as APP_BRIEF § In Scope (intentional redundancy)
6. **Lessons From Previous Phase** — pulled forward from RUN_NNN_LESSONS
7. **Skills Loaded For This Project** — which custom + Anthropic skills activate
8. **Operating Rules (Inherited From Stark Global)** — Plan Mode, Karpathy Protocol, eyesight-aware, surgical changes, surface conflicts, code-over-model, fail-loud, token budget
9. **TDD Flow** — Build → Unit Test → Integrate → Block Test → System Test → Finalize
10. **Approval Gates** — sub-phase boundaries
11. **Conflict Resolution** — precedence order
12. **Version History**

**Length:** 300-500 lines.

**Critical disciplines:**

- **Intentional redundancy with APP_BRIEF on forbidden zones.** Different docs are read in different contexts. The forbidden zones must be reinforced.
- **Lessons from previous phase** are surfaced here, not buried in retrospectives. New runs benefit from old lessons.
- **Approval gates explicit** — Claudy stops at each one and waits for operator approval.

**Common authoring mistakes:**

| Mistake | Fix |
|---|---|
| Underwriting the spine (treating it as short orientation) | Treat as authoritative doctrine, ~350 lines |
| Skipping the lessons-from-previous-phase section | Pull lessons forward from `playbook/RETROSPECTIVES/` |
| Forgetting Stark global doctrine references | Include Plan Mode, Karpathy Protocol, eyesight-aware as inherited |
| Not stating approval gates explicitly | Claudy needs to know where to stop |

### Cross-File Consistency

After authoring all four `_project/` files, verify cross-file consistency:

- **Forbidden zones match** between APP_BRIEF and `_project/CLAUDE.md` (intentional redundancy — must be identical)
- **Hard gates in APP_BRIEF appear in `verification/PHASE_GATES.md`** (they're the same gates from different angles)
- **Types in DATA_CONTRACT appear in `playbook/02-TYPES.md`** (the playbook references the contract)
- **Screens in UI_SPEC appear in `playbook/05-COMPONENTS.md`** (the playbook references the spec)
- **Tech stack in APP_BRIEF matches `_project/CLAUDE.md`** (intentional redundancy — must be identical)

If anything is inconsistent, fix BEFORE shipping the FFM.

---

## 10. File-By-File Authoring Guide — `_design/` and `_extraction/`

These two folders are **operator-filled**. The Architect's job is to author a `README.md` in each folder telling the operator what to drop in, why, and how Claudy will use it.

### 10.1 — `_design/README.md`

**Purpose:** Tell the operator what design artifacts go in `_design/` and how Claudy uses them.

**Required sections (in order):**

1. **What Goes Here** — required and optional items
2. **How Claudy Uses This Folder** — when in the run Claudy reads it, what for
3. **File Naming Convention** — directory tree showing expected file names
4. **Note On Style Tile** — explicit note if operator is moving with an "assumed for now" style tile, so future readers understand the state

**Length:** 100-150 lines.

**Content distinctions per variant:**

**For Conversion FFMs:**
- Required: Screenshots of every source app screen
- Required: Captions or section headers naming what each screenshot shows
- Optional: Annotated PDFs showing UX issues to preserve vs fix
- Optional: A "Known UX Quirks" summary

**For Greenfield FFMs:**
- Required: Brand tokens summary (`brand-tokens.md`)
- Required: Logo files (`logo-color.svg`, `logo-mono.svg`, `favicon.ico`)
- Required: Style tile (single image or Figma export)
- Optional: Wireframes from designer
- Optional: Reference screenshots from related apps for visual context (NOT to build now — context only)

**Example `_design/` directory tree (greenfield):**

```
_design/
├── README.md                     ← Architect authors
├── brand-tokens.md               ← Operator fills: primary hex, font, etc.
├── style-tile.png                ← Operator drops
├── logo-color.svg                ← Operator drops
├── logo-mono.svg                 ← Operator drops
├── favicon.ico                   ← Operator drops
└── reference/                    ← Optional context screenshots
    ├── prior-version-1.png
    ├── prior-version-2.png
    └── competitor-reference.png
```

**Example `_design/` directory tree (conversion):**

```
_design/
├── README.md                     ← Architect authors
├── 01-login-screen.png           ← Source app screenshot
├── 02-chat-screen.png            ← Source app screenshot
├── 03-mission-control.png        ← Source app screenshot
├── 04-mobile-chat.png            ← Mobile variant
└── annotations/                  ← Optional UX notes
    └── known-quirks.md
```

**Failure handling:**

If operator activates Claudy with `_design/` empty:
- Claudy surfaces during Sub-Phase 0 (Discovery): "No brand tokens / screenshots found in `_design/`. Proceeding with shadcn defaults / inferring from extraction docs. Confirm or provide assets."
- Operator either provides or confirms "proceed with defaults"
- Sub-Phase 4 (Components) defaults to shadcn zinc baseline

This is graceful degradation, not failure — but ship time suffers because brand work happens after components instead of before.

### 10.2 — `_extraction/README.md`

**Purpose:** Tell the operator which extraction documents go in `_extraction/` and why.

**Required sections (in order):**

1. **What Goes Here** — required and optional items per variant
2. **How Claudy Uses This Folder** — read on demand, not at activation
3. **File Naming Convention** — directory tree showing expected file names
4. **Why This Folder For Greenfield?** — if greenfield, explain the repurpose
5. **Operator Notes** — quick instructions for filling

**Length:** 100-150 lines.

**Content distinctions per variant:**

**For Conversion FFMs:**
The 11 Brain Drain documents should land in `_extraction/`:

```
_extraction/
├── README.md                                  ← Architect authors
├── 00-REPO-PROFILE.md
├── 01-EXISTING-DOCS-REVIEW.md
├── 02-ARCHITECTURE-MAP.md
├── 03-AGENT-LOOP.md
├── 04-TOOL-SYSTEM.md
├── 05-CONTEXT-AND-MEMORY.md
├── 06-PROMPTS-AND-PERSONA.md
├── 07-GUARDRAILS-AND-SANDBOXING.md
├── 08-ERROR-HANDLING-AND-RECOVERY.md
├── 09-TESTS-AND-EVALS.md
└── 10-RAW-FINDINGS-AND-QUESTIONS.md
```

**For Greenfield FFMs:**
Repurpose the folder for data-shape evidence from upstream / related repos. Document the repurpose clearly:

```
_extraction/
├── README.md                                  ← Architect authors (explains repurpose)
├── UPSTREAM_API_00-REPO-PROFILE.md            ← from related repo's extracts
├── UPSTREAM_API_02-ARCHITECTURE-MAP.md
├── UPSTREAM_API_04-TOOL-SYSTEM.md             ← data shapes for future phases
├── PRIOR_VERSION_00-REPO-PROFILE.md           ← patterns to preserve / fix
├── PRIOR_VERSION_07-GUARDRAILS.md             ← security smells to NOT repeat
└── PRIOR_VERSION_10-RAW-FINDINGS.md           ← open issues from prior version
```

**For Greenfield FFMs with NO related extracts:**
The folder may be effectively empty. Document this in `README.md`:

```markdown
# _extraction — N/A For Greenfield

This is a greenfield Phase 1 build. There is no source app to extract from.

Operator decisions for data shapes and patterns are documented in `_project/CLAUDE.md` § Operator Decisions, which serves as the evidence base for this phase.

Future phases may add extraction docs here if related work emerges.
```

**Failure handling:**

If operator activates Claudy with `_extraction/` empty AND it should have content:
- Claudy surfaces during Sub-Phase 0: "No extraction docs found. Proceeding without source-of-truth evidence — risk of repeating known smells. Confirm or provide extracts."
- Operator either provides or confirms "proceed without"
- Risk: Sub-Phase 1 (Types) may invent fields without evidence

### Why Operator-Filled

The Architect doesn't fill `_design/` or `_extraction/` because:

1. **Designer outputs** are designer's domain — Architect doesn't author brand tokens
2. **Brain Drain extracts** require running Brain Drain — that's Extractor's job, not Architect's
3. **Operator owns the evidence chain** — only the operator knows which related repos to pull extracts from
4. **Async dependencies** — Designer and Extractor may complete after Architect; the Architect's deliverable is the skeleton, the operator fills the bodies

The Architect's job for these folders is **authoring the README to guide the operator**, not filling the folder.

---

## 11. File-By-File Authoring Guide — `skills/`

The `skills/` folder holds the **reusable methodology skill** that travels across FFM runs. For frontend-first work, this is `stark-frontend-first`.

### 11.1 — Overall Structure

```
skills/stark-frontend-first/
├── CLAUDE.md                              ← skill doctrine (always-on)
├── SKILL.md                               ← Anthropic v2 methodology
├── workflow/
│   ├── 00-discovery.md
│   ├── 01-types-and-contract.md
│   ├── 02-service-layer.md
│   ├── 03-mock-data.md
│   ├── 04-components.md
│   └── 05-verification.md
├── references/
│   ├── SERVICE_LAYER_PATTERNS.md
│   ├── MOCK_DATA_PATTERNS.md
│   ├── COMPONENT_CONVENTIONS.md
│   └── ANTI_PATTERNS.md
└── templates/
    ├── service.template.ts
    ├── mock-data.template.ts
    └── types.template.ts
```

### 11.2 — `stark-frontend-first/CLAUDE.md`

**Purpose:** The skill's always-on doctrine. Read when the skill activates.

**Required sections (in order):**

1. **Mission Brief** — what this skill is for, who runs it, when to use it
2. **When This Skill Activates** — trigger conditions (project root CLAUDE.md declares mock-data mode, etc.)
3. **Folder Layout** — what the skill folder contains
4. **Reading Order** — read CLAUDE.md first, SKILL.md second, workflow on demand
5. **Doctrine (Non-Negotiable)** — 8 rules typically: Plan Mode, service layer = sole swap point, types are contract, mocks temporary, UI survives backend swap unchanged, no backend code in this phase, eyesight-aware, surgical changes
6. **Operator Override Protocol** — what operator can override, what they can't
7. **Anti-Patterns** — list of failure signals
8. **Success Criteria** — when the skill's phase is "complete"
9. **Evolution Principle** — how the skill grows from real usage
10. **Version History**

**Length:** 200-300 lines.

### 11.3 — `stark-frontend-first/SKILL.md`

**Purpose:** The Anthropic v2 methodology. Read after CLAUDE.md.

**Required structure:**

```yaml
---
name: stark-frontend-first
description: Build the frontend of a Next.js application using a service layer with mock data as the sole swap point for later backend integration. Use this skill when a project is in frontend-first phase, when authoring a foundation skeleton (Phase 1 of a multi-phase build), or when the project's FFM declares mock-data mode. Enforces service layer discipline, mock data conventions, type-driven contracts, and forbids backend code authoring for entities not yet in scope.
---

# Stark Frontend-First Skill

(body content)
```

**Required body sections:**

1. **Role definition** — "You are building the frontend of a Next.js app..."
2. **Phase Sequence** — Discovery → Types → Services → Mocks → Components → Verification
3. **Phase 0 — Discovery** (steps, verification gate)
4. **Phase 1 — Types & Contract** (steps, verification gate)
5. **Phase 2 — Service Layer** (steps, verification gate)
6. **Phase 3 — Mock Data** (steps, verification gate)
7. **Phase 4 — Components** (steps, verification gate)
8. **Phase 5 — Verification** (steps, verification gate)
9. **Worked Example** — at least one concrete code example
10. **Anti-Patterns** — block these
11. **When You're Done** — completion criteria
12. **Version History**

**Length:** 200-300 lines.

**v2 YAML frontmatter rules:**
- `name` — kebab-case, matches the skill folder name exactly
- `description` — multi-line allowed (use `>` for folded scalar), 2-4 sentences, includes trigger phrases, distinguishes from neighboring skills
- `allowed-tools` — optional list of tools the skill is authorized to use

### 11.4 — `workflow/00-discovery.md` Through `workflow/05-verification.md`

**Purpose:** Concise per-phase workflows that mirror the playbook's sub-phases.

**Required structure per file:**

1. **Goal** — one sentence
2. **Steps** — numbered, terse
3. **Gate** — verification criteria
4. **Notes** — gotchas if any

**Length:** 20-50 lines each. Workflow files are intentionally terse — the playbook has the long-form version.

### 11.5 — `references/`

Four reference files:

- **`SERVICE_LAYER_PATTERNS.md`** — examples of correct service-layer wrapping; the "sole swap point" doctrine
- **`MOCK_DATA_PATTERNS.md`** — how to author mock data; deletability discipline
- **`COMPONENT_CONVENTIONS.md`** — Shadcn primitive mapping, Tailwind conventions, server vs client components, brand token usage
- **`ANTI_PATTERNS.md`** — failure modes with code examples (security smells, layering violations, scope creep)

**Length:** 100-200 lines each.

### 11.6 — `templates/`

Three template files:

- **`types.template.ts`** — starter type definition with comments showing what to replace
- **`service.template.ts`** — starter service file with comments
- **`mock-data.template.ts`** — starter mock data file with the DELETABLE comment header

**Length:** 30-80 lines each.

### 11.7 — Reuse Discipline

The skill is **mostly the same across FFMs**. Don't re-author from scratch. When starting a new FFM:

1. Copy `skills/stark-frontend-first/` from the previous FFM
2. Only edit phase-specific notes (e.g., "For Cyber Pharma v1 Phase 1, backend is forbidden zone for Frank-domain entities")
3. Bump the version (e.g., `v1.0-cp1` for Cyber Pharma run 1)

The skill compounds value by being mostly stable across runs. Tuning is per-FFM but lightweight.

---

## 12. File-By-File Authoring Guide — `playbook/`

The `playbook/` folder holds the **phase-by-phase build instructions** Claudy follows during the run.

### 12.1 — Overall Structure

```
playbook/
├── 00-OVERVIEW.md
├── 01-DISCOVERY.md
├── 02-TYPES.md
├── 03-SERVICES.md
├── 04-MOCKS.md
├── 05-COMPONENTS.md
├── 06-VERIFICATION.md
├── 07-RETROSPECTIVE.md
└── RETROSPECTIVES/             ← per-run lessons
    └── RUN_001_LESSONS.md      ← created after run completes
```

### 12.2 — `00-OVERVIEW.md`

**Purpose:** The phase-by-phase build plan.

**Required sections:**

1. **The Phases** — flow diagram
2. **Sub-Phase Summary** — table: sub-phase, what ships, estimated time, approval gate
3. **Skill Activation Per Sub-Phase** — which Anthropic skills trigger when
4. **Approval Gate Protocol** — what the structured completion summary looks like
5. **Recovery Protocol** — how to resume after interruption
6. **Tests Per Sub-Phase** — what tests get written when
7. **Sequencing With Stark Repo Security** — confirmation that audit is clean before phase starts
8. **Cross-Reference** — where to find what

**Length:** 100-200 lines.

### 12.3 — `01-DISCOVERY.md` Through `06-VERIFICATION.md` (And `07-RETROSPECTIVE.md`)

Each playbook file follows a consistent structure:

1. **Goal** — what this sub-phase produces
2. **What This Sub-Phase Does** — context
3. **Steps** — numbered, detailed
4. **Verification Gate** — operator-checkable criteria
5. **Common Stumbles** — what to watch for
6. **Anti-Patterns** — code examples of WRONG vs CORRECT

**Length:** 150-300 lines each.

### 12.4 — Per-Sub-Phase Authoring Notes

**`01-DISCOVERY.md`**
- Claudy reads everything in order, summarizes back, proposes Sub-Phase 1 plan
- Produces NO code in this sub-phase — read-only
- Includes the structured acknowledgment format Claudy outputs

**`02-TYPES.md`**
- Claudy creates TypeScript types from DATA_CONTRACT § 4
- Verifies `npx tsc --noEmit` clean
- Verifies no Supabase imports in `/src/types/`

**`03-SERVICES.md`**
- Claudy wraps starter kit's data access in `/src/services/`
- Critical: read roles from `user_roles` table only (security)
- Verifies no Supabase imports in components

**`04-MOCKS.md`**
- Minimal mock data for Phase 1; expands for later phases
- Document each mock file as DELETABLE
- Verify no component imports `/src/mocks/`

**`05-COMPONENTS.md`**
- This is the biggest sub-phase
- Break into discrete steps: design system → brand tokens → public marketing → auth screens → portals → role gates → error boundaries → tests → brand other app
- Mini-gates between steps; operator approves each before advancing

**`06-VERIFICATION.md`**
- Runs all tests
- Deploys to staging
- Manual smoke walkthrough
- Env var fail-closed verification
- Security smell greps
- Hard gates checklist
- Update RECOVERY.md

**`07-RETROSPECTIVE.md`**
- Draft `RUN_001_LESSONS.md` honestly
- Capture what worked, what stumbled, what should change
- Identify structural lessons (apply to all future FFM runs) vs project-specific
- Identify lessons that should feed the NEXT phase's FFM authoring

### 12.5 — `RETROSPECTIVES/` Folder

Starts empty. After each run completes, a `RUN_NNN_LESSONS.md` file lands here.

**Required structure for retrospective files:**

1. **What Worked** — be specific
2. **What Stumbled** — be honest (not sycophantic)
3. **What Should Change For Next FFM** — broken into Structural, Project-Specific, Phase-N-Specific
4. **Surprises** — anything unexpected
5. **Time Estimates vs Actual** — calibration data
6. **Anti-Patterns Observed** — propose additions to skill's `ANTI_PATTERNS.md`
7. **New Patterns That Worked** — propose additions to skill's references
8. **Open Questions For Next FFM**
9. **Verdict** — one-sentence overall assessment

**Length:** 150-300 lines.

### 12.6 — Playbook Reuse Discipline

Like the skill, the playbook is **mostly stable across FFMs**. When authoring a new FFM:

1. Copy `playbook/` from the previous FFM
2. Tune phase-specific content (e.g., "For Phase 1, this sub-phase produces only auth-related types")
3. Update sub-phase 5 (Components) heavily — this is the most phase-specific
4. Leave 01-04 mostly intact (Types / Services / Mocks discipline is consistent across phases)

---

## 13. File-By-File Authoring Guide — `verification/`

The `verification/` folder holds the **approval gate criteria** and the **operator-runnable build checklist**.

### 13.1 — `verification/PHASE_GATES.md`

**Purpose:** Approval gate criteria for each sub-phase.

**Required structure:**

For each sub-phase (0 through 6):

1. **Criteria** — checkbox list of what must pass
2. **Failure Mode** — what indicates the gate is red
3. **Operator Approval Required** — explicit statement

Plus a final section:

- **Master Sign-Off** — all gates green, operator gut-check, both apps deployed

**MANDATORY cross-cutting gate — Gate M, Mobile Shell (every FFM, every UI-bearing sub-phase):**

Rule Zero is a build-time GATE, not spec-authoring advice. Every `PHASE_GATES.md` MUST carry a **Gate M**, verified in the SAME sub-phase that builds any shell/screen — NOT a late "responsive" cluster:

- Authed/app shell has mobile nav: navbar → hamburger; the sidebar / app-rail is reachable via a hamburger + slide-over below its fit breakpoint (`lg` for wide rails ≥ ~20rem) — never `hidden md:block` (or fixed-width) with no trigger.
- No control is desktop-only; no horizontal overflow at 375px; touch targets ≥ 44px.
- Verified at 375 / tablet / desktop, both themes.
- **Failure mode — refuse to advance:** "we'll fix mobile in a later cluster" (the named deferred-violation pattern).

Source of truth: root `CLAUDE.md` forbidden zone + `UI-UX-BUILDING-MANUAL` Rule Zero. (Added after a missed mobile shell shipped past the gates — RUN_002. Rule Zero existed as authoring advice but wasn't an enforced gate; this closes that.)

**Length:** 200-400 lines.

### 13.2 — `verification/BUILD_CHECKLIST.md`

**Purpose:** Operator-runnable verification checklist. The operator walks this checklist before declaring phase complete.

**Required sections:**

1. **Pre-Build Checks** — what must be true before activating Claudy
2. **Build Verification (After Each Sub-Phase)** — checkboxes per sub-phase
3. **Final Pass: All Hard Gates** — walk through APP_BRIEF § Hard Gates
4. **Final Operator Gut Check** — three questions ("does foundation feel solid?")
5. **Sign-Off** — table for operator and Claudy to confirm

**Length:** 200-300 lines.

### 13.3 — Authoring Discipline

The hard gates in `APP_BRIEF.md § 5` appear in `verification/PHASE_GATES.md § Gate 5` and `verification/BUILD_CHECKLIST.md § Final Pass`. **Same gates, three different angles.** This intentional redundancy keeps the gates visible at every approval cycle.

If you change a hard gate in APP_BRIEF, update both verification files. Use grep to catch this.

---

## 14. The Extractor Question — When To Run Brain Drain

Brain Drain is the **Extractor Skill** — a Stark Skill that reads any source repo and produces 11 evidence-labeled extraction documents. The question is: when do you run it?

### Decision Tree

```
Does the FFM's phase have a source app to convert?
│
├─ YES → Run Brain Drain on the source. 11 docs → _extraction/
│         Then Architect authors DATA_CONTRACT from extracts.
│
└─ NO → Is the FFM building on patterns from a related repo?
    │
    ├─ YES → Pull relevant extracts from that repo's prior Brain Drain
    │         (or run Brain Drain on it now, custom-scoped to data shapes)
    │         Extracts → _extraction/
    │         Architect authors DATA_CONTRACT from operator decisions + extracts
    │
    └─ NO → Greenfield with no patterns to inherit.
              _extraction/ may stay empty (with README documenting "N/A")
              DATA_CONTRACT authored from operator decisions only
              Risk: more drift between authoring and reality
```

### When To Run Brain Drain — The Clearest Cases

**Always run Brain Drain when:**
- Converting an existing prototype (Streamlit, Gradio, internal tool) to a production Next.js app
- Inheriting a system from another team and need to understand what's there
- Auditing a vibe-coded codebase before refactoring
- The operator says "I built this and forgot how it works"

**Skip Brain Drain when:**
- Greenfield project with no related repos
- Foundation skeleton phases where the starter kit IS the spec
- Operator decisions cover all data shape questions
- Phase doesn't touch new entities (Phase 1 foundation skeleton has no Frank-domain work)

**Maybe run Brain Drain when:**
- Greenfield but building on a related team's API
- Security audit of an existing repo to inform new work
- Documentation drift suspected (docs don't match code)

### What Brain Drain Produces (The 11 Docs Reminder)

| # | Document | Content |
|---|---|---|
| 00 | REPO-PROFILE.md | Repo identity, file tree, entry points, dependencies, build/run commands |
| 01 | EXISTING-DOCS-REVIEW.md | Existing docs validated against actual code; drift flagged |
| 02 | ARCHITECTURE-MAP.md | Flow map of the source app's primary user journeys |
| 03 | AGENT-LOOP.md | Request/response lifecycles (if AI-agent app) |
| 04 | TOOL-SYSTEM.md | API surface — HTTP routes, external services, integrations |
| 05 | CONTEXT-AND-MEMORY.md | Session state, persistence, blob storage patterns |
| 06 | PROMPTS-AND-PERSONA.md | Screen inventory (the fattest doc — every screen, every element) |
| 07 | GUARDRAILS-AND-SANDBOXING.md | Auth gates, RLS policies, transport security, secret management |
| 08 | ERROR-HANDLING-AND-RECOVERY.md | Try/except map, sentinels, retry patterns, failure modes |
| 09 | TESTS-AND-EVALS.md | Existing tests; GAP if none |
| 10 | RAW-FINDINGS-AND-QUESTIONS.md | Drifts, dead code, security smells, top 5 discoveries |

### How Brain Drain Uses Evidence Discipline

Every line in every extraction document carries one of these labels:

- **EVIDENCE** — directly found in a specific file with line number citation
- **INFERENCE** — reasonable conclusion from observed structure; basis stated
- **CLAIM** — documentation or operator says it; not independently verified
- **GAP** — expected component not found; what was expected and where searched
- **QUESTION** — needs operator clarification; phrased as an explicit question

Without these labels, the Architect can't tell what's verified versus guessed. With them, the Architect can author DATA_CONTRACT with confidence.

### How To Trigger Brain Drain

Brain Drain is a Stark Skill. The operator:

1. Clones the source repo locally
2. Drops the Brain Drain skill folder at `.claude/skills/brain-drain/` (or wherever the skill lives)
3. Adds a `_EXTRACTIONS/` folder at the repo root for outputs
4. Boots Claudy in that repo's directory
5. Pastes the boot prompt: *"Read the CLAUDE.md at `.claude/skills/brain-drain/CLAUDE.md` and follow it. Extract this repo into `_EXTRACTIONS/`. Use evidence labels throughout."*
6. Claudy reads, plans, asks for approval, then produces the 11 docs

Output ends up at `<source-repo>/_EXTRACTIONS/`. Operator copies the relevant docs into the FFM's `_extraction/`.

### Time Budget For Brain Drain

| Repo Size | Brain Drain Time |
|---|---|
| Small (< 5K LOC) | 1-2 hours |
| Medium (5-20K LOC) | 2-4 hours |
| Large (20-50K LOC) | 4-8 hours, often multiple sessions |
| Very large (50K+ LOC) | Custom scoping recommended; targeted Brain Drain on specific subsystems |

For very large repos, run targeted Brain Drain on the specific subsystems you need rather than the whole repo. (More on this in [Section 15](#15-custom-brain-drain-prompts).)

---

## 15. Custom Brain Drain Prompts

The standard Brain Drain skill produces 11 generic docs. Sometimes you need targeted evidence on specific questions. That's where **custom Brain Drain prompts** come in.

### When To Use Custom Prompts

**Use a custom prompt when:**

- Standard 11 docs are too broad for the question (e.g., you only need data shapes, not the whole architecture)
- You need extra emphasis on one area (e.g., security audit deep dive)
- The repo is too large for a full extraction in one pass
- You've run standard Brain Drain and need to drill deeper on specific findings

### How To Write A Custom Brain Drain Prompt

The custom prompt **augments** the standard Brain Drain skill, not replaces it. It tells Claudy what extra emphasis to apply.

**Structure:**

```
You are running Brain Drain on the source repo at <path>.

Follow the standard Brain Drain skill at .claude/skills/brain-drain/CLAUDE.md
for evidence discipline and the 11-document structure.

ADDITIONALLY, apply this custom focus:

[1-3 paragraphs describing what extra emphasis to apply]

Specifically:
- [Bullet 1: extra detail wanted]
- [Bullet 2: extra detail wanted]
- [Bullet 3: extra detail wanted]

Skip or shrink these sections (they're not needed for this run):
- [Section to deprioritize]
- [Section to deprioritize]

Surface any gaps or questions during the run. Plan Mode before each document.
```

### Example Custom Prompts

**Example 1 — Security Audit Focus**

```
You are running Brain Drain on the source repo at <path>.
Follow the standard Brain Drain skill...

ADDITIONALLY, apply security-audit focus:

Document 07 (GUARDRAILS-AND-SANDBOXING) gets EXTRA depth.

Specifically:
- Every auth check, RLS policy, JWT validation, role check — with file:line citation
- Every secret accessed in code (env vars, config files, etc.) — with how it's read
- Every external service called — with what credentials are used
- Every input that crosses a trust boundary — request bodies, query params, file uploads
- Every "TODO security" or "FIXME auth" comment

Skip or shrink these sections:
- Document 06 (PROMPTS-AND-PERSONA) — UI inventory not needed
- Document 03 (AGENT-LOOP) — only if no AI agents in app
```

**Example 2 — Data Shapes Only**

```
You are running Brain Drain on the source repo at <path>.
Follow the standard Brain Drain skill...

ADDITIONALLY, apply data-shapes-only focus:

This run is for FFM authoring. We only need the data contract evidence.

Specifically:
- Document 04 (TOOL-SYSTEM) gets EXTRA depth — every API endpoint with request/response shapes
- Document 05 (CONTEXT-AND-MEMORY) gets EXTRA depth — database schemas, session shapes
- Document 10 (RAW-FINDINGS) — flag any data shape oddities (snake_case vs camelCase, optionality inconsistencies)

Skip or shrink these sections:
- Document 02 (ARCHITECTURE-MAP) — high-level flow not needed
- Document 06 (PROMPTS-AND-PERSONA) — UI inventory not needed
- Document 08 (ERROR-HANDLING) — error patterns not needed for this run
```

**Example 3 — Targeted Subsystem**

```
You are running Brain Drain on the source repo at <path>.
Follow the standard Brain Drain skill...

ADDITIONALLY, scope to ONE subsystem:

This run extracts ONLY the authentication subsystem. Ignore other subsystems.

Specifically:
- Document 02 (ARCHITECTURE-MAP) — auth flows only (login, logout, session, password reset)
- Document 04 (TOOL-SYSTEM) — auth endpoints only
- Document 07 (GUARDRAILS-AND-SANDBOXING) — full coverage
- All other docs — auth-related portions only

Surface anything outside auth scope as INFERENCE labeled "not in scope for this run."
```

### Custom Prompt Discipline

- **Don't replace the skill** — the custom prompt augments
- **Don't skip Plan Mode** — Claudy still plans before each doc
- **Don't lose evidence discipline** — even targeted runs use the 5-label system
- **Output to a clearly-named folder** — `_EXTRACTIONS_security_audit/` not just `_EXTRACTIONS/` so it doesn't overwrite the standard one
- **Document what you skipped** — so the next reader knows what's NOT in the extract

### Storing Custom Prompts

Keep a library of useful custom prompts in your factory's `agent_docs/app_factory/brain-drain-prompts/`:

```
agent_docs/app_factory/brain-drain-prompts/
├── security-audit-focus.md
├── data-shapes-only.md
├── auth-subsystem-only.md
├── api-surface-only.md
└── README.md  ← when to use which
```

Each prompt is a starter — operator adapts per use.

---

## 16. Bridging The FFM Into The Starter Kit

The FFM lives at `agent_docs/CURRENT_APP/<project>_<phase>_ffm/`. The starter kit's root `CLAUDE.md` needs to know it's there.

### Two Bridging Patterns

**Pattern A — Edit Starter Kit Root `CLAUDE.md` (older convention)**

The operator adds a pointer paragraph to the starter kit's root `CLAUDE.md`:

```markdown
## Active Project Module

The current project's Factory module lives at `agent_docs/CURRENT_APP/<ffm_folder_name>/`. Read `CLAUDE.md` in that folder for project-specific direction, doctrine, and the phase-by-phase playbook. All work for the current project follows that module.
```

Claudy reads root CLAUDE.md first on session start, sees the pointer, follows it to the FFM.

**Pattern B — `PROJECT_POINTER.md` (newer, cleaner convention)**

Create a separate file at the starter kit root called `PROJECT_POINTER.md`:

```markdown
# PROJECT_POINTER.md — Active Project Module

The current project's Factory module lives at:
**`agent_docs/CURRENT_APP/<ffm_folder_name>/`**

On session start, read `CLAUDE.md` in that folder. That file is the project's navigation contract. It tells you which project we're building, what's in scope, what's forbidden, what phase we're in, and where to find the project handoff docs (APP_BRIEF, DATA_CONTRACT, UI_SPEC).

Before starting the FFM's Discovery sub-phase, also read these kit-level references:
- `agent_docs/starter-kit/starter-kit-handbook.md` — kit conventions and what's pre-wired
- `agent_docs/starter-kit/COMPONENT_REGISTRY.md` (if it exists) — primitive mapping

All work for the current build follows the module's doctrine and playbook. This pointer is **active until this phase completes**. After completion, this file gets updated to point at the next phase's FFM.
```

The operator's boot prompt then becomes one line:

> Read `PROJECT_POINTER.md` at project root. Follow it. STOP and wait for my approval after the FFM's Discovery sub-phase summary.

### Why Pattern B Is Cleaner

- **No global doctrine pollution** — the universal Stark CLAUDE.md stays project-agnostic
- **Self-documenting** — new collaborators see `PROJECT_POINTER.md` immediately
- **Per-repo state** — each starter kit clone has its own pointer, no syncing across repos
- **Survives session resets** — no need to remember to paste a long prompt; just point at the file
- **Easy phase transitions** — when Phase 1 closes, update one file to point at Phase 2 FFM

### Pattern B's Companion: Global CLAUDE.md Precedence Block

If using Pattern B, the operator's global CLAUDE.md should still mention precedence:

```markdown
## Project Module Precedence

When working in any project that uses a Factory Module (FFM), follow this precedence:

- For project-specific decisions (scope, types, screens, forbidden zones): the FFM's docs win
- For universal Stark doctrine (Plan Mode, disaster recovery, communication style, TDD flow): this file wins
- When in doubt, surface to operator

Project entry point is always `PROJECT_POINTER.md` at the project root (when present). It names the active FFM.
```

This says "FFMs exist, here's how they win" without naming any specific FFM.

### Which Pattern To Use

For new FFM authoring: **use Pattern B**. It's the cleaner architecture.

For existing FFMs already using Pattern A: keep going with Pattern A until phase completion, then migrate to Pattern B at the next FFM.

---

## 17. Common Authoring Stumbles

These are stumbles observed across multiple FFM runs. Avoid them.

### Stumble 1 — Vague Forbidden Zones

❌ "No backend stuff" — interpretable, unenforceable
✅ "No API routes in `/app/api/` beyond starter kit defaults. No Supabase migrations. No SQL beyond starter kit migrations. No RLS policy authoring."

Claudy needs concrete prohibitions it can verify before acting.

### Stumble 2 — Inventing Mock Data Shapes

❌ Author DATA_CONTRACT with shapes that "feel right"
✅ Author DATA_CONTRACT from Brain Drain extraction evidence OR explicit operator decisions

Every field traces to evidence. If you can't trace it, STOP and surface.

### Stumble 3 — Skipping The Mobile Layout

❌ Document UI_SPEC as desktop-first, mention mobile in passing
✅ Document mobile sketch FIRST per screen, desktop as progressive enhancement

If the spec describes desktop, the build will be desktop. Rule Zero is mobile-first.

### Stumble 4 — Underwriting `_project/CLAUDE.md`

❌ Treat the project spine as a short orientation doc
✅ Treat it as authoritative doctrine, ~350 lines, intentionally redundant with APP_BRIEF

The spine is read every session. It must hold across sessions.

### Stumble 5 — No "Known Discrepancies" Section (For Conversions)

❌ Silently fix bugs/quirks in the source app during conversion
✅ Document quirks in "Known Discrepancies" section; preserve unless explicitly flagged

In FFM v1.0, Mission Control hardcoded 4 agents vs Chat dropdown's 5 was preserved deliberately. Documenting it prevented Claudy from "fixing" it during build.

### Stumble 6 — Cross-File Drift

❌ Edit APP_BRIEF hard gates without updating `verification/PHASE_GATES.md`
✅ Treat hard gates as ONE source, three views. Update all three when changing.

Grep is your friend: `grep -rn "G1" _project/ verification/` to find every reference.

### Stumble 7 — Authoring Out Of Order

❌ Author CLAUDE.md first because "it's the most important"
✅ Author APP_BRIEF → DATA_CONTRACT → UI_SPEC → CLAUDE.md, in order

CLAUDE.md is informed by the other three. Author it last with everything else in hand.

### Stumble 8 — Skipping The Folder READMEs (`_design/`, `_extraction/`)

❌ Leave `_design/` and `_extraction/` as empty folders
✅ Author `README.md` in each, telling the operator what to drop in

The Architect's job for these folders is the README. Operator fills the body.

### Stumble 9 — Authoring An FFM Before Designer / Extractor Outputs Land

❌ "I'll author the FFM now and update `_design/` when designer is done"
✅ Wait for upstream outputs (or get explicit operator confirmation to proceed without them)

Authoring with stale or missing inputs causes rework when the real inputs land.

### Stumble 10 — Forgetting Cross-Repo Implications

❌ FFM assumes one repo when the project has two (main app + superadmin app)
✅ Decide upfront: same FFM staged in both repos, OR separate FFMs per repo

For Cyber Pharma v1: Phase 1 FFM is staged in BOTH main app and superadmin app repos (same content, two stagings). Decide before authoring.

### Stumble 11 — Folder Tree Doesn't Match Disk

❌ FFM's `CLAUDE.md` folder map shows `playbook/05-LOGIN.md` but actual file is `05-COMPONENTS.md`
✅ Always run `find . -type f | sort` and compare to the folder map before publishing

Folder map drift is the #1 source of confusion when Claudy tries to read a referenced file.

### Stumble 12 — Activation Contract Requires Placeholder Substitution

❌ "Read the CLAUDE.md at `agent_docs/CURRENT_APP/<FFM_FOLDER>/CLAUDE.md`"
✅ "Read the CLAUDE.md at `agent_docs/CURRENT_APP/cyber_pharma_v1_phase1_ffm/CLAUDE.md`"

The operator should be able to copy-paste the boot prompt without find-replace. Substitute the actual folder name during authoring.

### Stumble 13 — Sycophantic Retrospectives

❌ "Everything went great, no issues!"
✅ "Sub-Phase 3 took 2 attempts because the mock auth fixture didn't satisfy the AuthenticatedUser type — root cause was undocumented optionality in DATA_CONTRACT."

Honest retrospectives compound. Sycophantic ones decay the system.

### Stumble 14 — Authoring While Tired

The FFM is a multi-thousand-line artifact. Authoring it in one sprint at the end of a long day produces sloppy work that has to be redone.

Pace it: morning for `_project/` files (highest cognitive load), afternoon for `skill/playbook/verification` (copy-forward work).

---

## 18. The Authoring Checklist

Use this checklist when authoring a new FFM. Walk it top to bottom. Don't skip steps.

### Pre-Authoring (Inputs Confirmation)

- [ ] PHASE_ROADMAP is locked; this FFM is for phase N
- [ ] MASTER_APP_BRIEF is locked
- [ ] Designer outputs in hand (or operator confirmed "use defaults")
- [ ] Extractor outputs in hand (or operator confirmed "greenfield, N/A")
- [ ] Starter kit handbook and component registry available
- [ ] Previous FFM retrospective read (for non-first FFMs)
- [ ] Operator's "go" signal received

### Scaffold

- [ ] Create FFM folder named `<project>_<phase>_ffm` (lowercase, underscores)
- [ ] Create subfolders: `_project/`, `_design/`, `_extraction/`, `skills/stark-frontend-first/`, `playbook/RETROSPECTIVES/`, `verification/`
- [ ] Create skill subfolders: `skills/stark-frontend-first/workflow/`, `references/`, `templates/`

### Root Files

- [ ] `CLAUDE.md` — 12 required sections, accurate folder map, copy-pasteable activation contract
- [ ] `README.md` — 9 required sections, runnable bash, real folder name in boot prompt
- [ ] `AGENTS.md` — redirect to CLAUDE.md
- [ ] `GEMINI.md` — redirect to CLAUDE.md

### `_project/` (Author In Order)

- [ ] `APP_BRIEF.md` — mission, hero outcome, in/out of scope, numbered hard gates, success criteria, risks, stumbles, effort estimate, handoff, constraints, phase transitions, changelog
- [ ] `DATA_CONTRACT.md` — tables in/out of play, triggers, TypeScript types, service contracts, mock strategy, future decision points, conflict resolution, changelog
- [ ] `UI_SPEC.md` — screen list, layouts, per-screen specs, error boundaries, design system, breakpoints, states, a11y, out of scope, references, changelog
- [ ] `CLAUDE.md` — project identity, hero, forbidden zones (redundant w/ APP_BRIEF), tech stack, ships, lessons-from-previous, skills, operating rules, TDD flow, gates, conflict resolution, version

### `_design/`

- [ ] `README.md` authored (operator instructions, expected files, how Claudy uses)

### `_extraction/`

- [ ] `README.md` authored (which extracts to drop, repurpose note if greenfield)

### `skills/stark-frontend-first/`

- [ ] `CLAUDE.md` (skill doctrine — mission, activation, doctrine, anti-patterns)
- [ ] `SKILL.md` (Anthropic v2 frontmatter, phase sequence, worked example)
- [ ] `workflow/00-discovery.md` through `05-verification.md` (6 terse files)
- [ ] `references/SERVICE_LAYER_PATTERNS.md`
- [ ] `references/MOCK_DATA_PATTERNS.md`
- [ ] `references/COMPONENT_CONVENTIONS.md`
- [ ] `references/ANTI_PATTERNS.md`
- [ ] `templates/types.template.ts`
- [ ] `templates/service.template.ts`
- [ ] `templates/mock-data.template.ts`

### `playbook/`

- [ ] `00-OVERVIEW.md` (phase flow, sub-phase table, gate protocol, recovery, tests, cross-references)
- [ ] `01-DISCOVERY.md`
- [ ] `02-TYPES.md`
- [ ] `03-SERVICES.md`
- [ ] `04-MOCKS.md`
- [ ] `05-COMPONENTS.md` (typically the biggest playbook file)
- [ ] `06-VERIFICATION.md`
- [ ] `07-RETROSPECTIVE.md`
- [ ] `RETROSPECTIVES/` folder exists (empty, accumulates over runs)

### `verification/`

- [ ] `PHASE_GATES.md` (Gate 0 through Gate 6, **Gate M — mobile shell**, master sign-off)
- [ ] `BUILD_CHECKLIST.md` (pre-build checks, per-sub-phase checks, hard gates pass, **mobile shell at 375/tablet**, gut check, sign-off)

### Self-Check

- [ ] Hard gates in APP_BRIEF match gates in PHASE_GATES.md and BUILD_CHECKLIST.md
- [ ] Tech stack in APP_BRIEF matches tech stack in `_project/CLAUDE.md`
- [ ] Forbidden zones in APP_BRIEF match forbidden zones in `_project/CLAUDE.md`
- [ ] Types in DATA_CONTRACT match types referenced in `playbook/02-TYPES.md`
- [ ] Screens in UI_SPEC match screens referenced in `playbook/05-COMPONENTS.md`
- [ ] Folder map in root `CLAUDE.md` matches `find . -type f` output
- [ ] Activation contract uses real folder name, no placeholders
- [ ] All cross-references between files resolve

### Package

- [ ] `zip -r <ffm_name>.zip <ffm_folder>/`
- [ ] Verify zip structure (top-level folder, no extra wrapper)
- [ ] Hand off zip to operator

### Operator Hands Back

When operator returns the filled FFM (with `_design/` and `_extraction/` populated):

- [ ] Confirm `_design/` is populated (or operator confirms defaults)
- [ ] Confirm `_extraction/` is populated (or operator confirms N/A)
- [ ] Architect role is done; Engineer takes over

---

## 19. Evolution And Versioning

The FFM is not static. Each run produces lessons that should feed the next.

### Versioning Convention

- `v1.0` — first instance of this FFM type (e.g., FFM v1.0 = original Cyberize conversion FFM)
- `v1.1` — refinement after a run (e.g., FFM v1.0-cp1 = adapted for Cyber Pharma run 1)
- `v2.0` — significant restructure (e.g., FFM v2.0 = new variant pattern emerged)

Track versions in each file's bottom Version History table.

### Evolution Loop

```
Run completes
    ↓
Retrospective drafted (engineer)
    ↓
Operator reviews and edits
    ↓
Structural lessons identified (apply to all future FFM runs)
    ↓
Project-specific lessons stay in retrospective
    ↓
Phase-N+1 lessons feed Phase-N+1 FFM authoring
    ↓
Structural lessons promote to:
    - playbook updates (sub-phase steps)
    - skill updates (anti-patterns, patterns)
    - FFM_PLAYBOOK updates (this document)
    ↓
Next FFM is authored sharper
```

### What Counts As "Structural" vs "Project-Specific"

**Structural** (applies to all FFMs):
- New anti-pattern observed in code (add to skill's ANTI_PATTERNS.md)
- New verification step that saved a stumble (add to BUILD_CHECKLIST template)
- A consistent ordering issue between sub-phases (update 00-OVERVIEW)
- A new role discovery (update this playbook's role descriptions)

**Project-Specific** (stays in retrospective):
- Frank's brand color hex was wrong on the first attempt
- Cloud Run IAM took 20 min to resolve
- Stripe CLI auth needed re-doing on the new VM

The distinction matters. Promoting project-specifics to structural creates noise. Leaving structurals in retrospectives means the next FFM repeats the same stumbles.

### When To Update This Playbook (FFM_PLAYBOOK.md)

Update this playbook when:
- A new structural lesson surfaces
- The pattern itself evolves (e.g., new variant emerges, new sub-phase needed)
- The Designer / Extractor / Architect / Engineer role boundaries shift
- A new common stumble is identified

Don't update for:
- Single-run anomalies
- Project-specific debugging
- Personal authoring preferences

### Versioning This Playbook

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-06-03 | Initial playbook authored from FFM v1.0 (Cyberize conversion) + Cyber Pharma v1 Phase 1 FFM (greenfield foundation). Captures four-role factory pattern, two FFM variants (conversion + greenfield), full file-by-file authoring guides, custom Brain Drain prompts. |

---

## 20. Worked Examples

This playbook describes the pattern abstractly. Two real FFMs are available as worked examples.

### Example 1 — Conversion FFM v1.0 (Cyberize Agentic Automation, May 2026)

**Location:** `agent_docs/CURRENT_APP/app-factory-frontend-first-module/` (in the Cyberize starter kit clone)

**Variant:** Conversion

**Source app:** A Streamlit prototype for an AI agent harness (Google ADK + N8N hybrid)

**Phase scope:** Full app conversion (login, chat, mission control)

**What to study:**
- `_project/APP_BRIEF.md` — 200+ lines, 15 hard gates, success criteria table, known discrepancies preserved
- `_project/DATA_CONTRACT.md` — 500+ lines, 12 types, 4 service contracts, mock data requirements, Phase 2 decision points
- `_project/UI_SPEC.md` — 600+ lines, 3 screens with full per-screen specs, Shadcn primitive mapping, mobile breakpoints
- `_project/CLAUDE.md` — 350+ lines, forbidden zones repeated, tech stack, operating rules, approval gates
- `playbook/01-DISCOVERY.md` through `08-VERIFICATION.md` — the full sub-phase playbook
- `skills/stark-frontend-first/` — the skill that travels with the module

**What it taught us:**
- The folder structure that works
- The reading order discipline
- The intentional redundancy between APP_BRIEF and `_project/CLAUDE.md`
- The "Known Discrepancies" section pattern
- The reusable-vs-per-project separation

### Example 2 — Greenfield FFM (Cyber Pharma v1 Phase 1, June 2026)

**Location:** `agent_docs/CURRENT_APP/cyber_pharma_v1_phase1_ffm/` (in both main app and superadmin app starter kit clones)

**Variant:** Greenfield (foundation skeleton)

**Source app:** None — building from audited starter kit clone

**Phase scope:** Phase 1 of 8 in the Cyber Pharma v1 roadmap (foundation skeleton only)

**What to study:**
- `CLAUDE.md` — adapted for greenfield, includes "What's Different About This FFM" section
- `_project/APP_BRIEF.md` — 15 hard gates including design system scaffolding (greenfield-specific)
- `_project/DATA_CONTRACT.md` — minimal types (auth.users, user_roles only), Frank-domain tables explicitly out of scope
- `_project/UI_SPEC.md` — placeholder pages + inherited starter kit screens, design system spec
- `_design/README.md` — operator-fills instructions for brand tokens and style tile
- `_extraction/README.md` — repurposed for data-shape evidence from Frank API + TONY_DEMO extracts

**What it taught us:**
- The greenfield variant pattern
- How `_extraction/` is repurposed for related-repo evidence
- How `_design/` shifts from screenshots to brand tokens + style tile
- How phase scoping works (one FFM per phase, not mega-modules)
- The naming convention: `<project>_<phase>_ffm`

### Reading Order For Worked Examples

If you're authoring your first FFM, read in this order:

1. **This playbook end-to-end** — understand the pattern
2. **Greenfield FFM (Example 2)** — simpler, smaller scope
3. **Conversion FFM (Example 1)** — fuller, conversion-specific patterns
4. **Both FFMs' retrospectives** (when available) — what actually went well/poorly
5. **Start authoring your FFM**

---

## 21. Appendix A — Skeleton Folder Tree

The complete folder structure to scaffold, with file purposes:

```
<project>_<phase>_ffm/
│
├── CLAUDE.md                          # Navigation contract for AI tools
├── README.md                          # Operator's setup guide
├── AGENTS.md                          # Codex CLI pointer
├── GEMINI.md                          # Gemini CLI pointer
│
├── _project/                          # PROJECT-SPECIFIC content
│   ├── CLAUDE.md                      # Project spine, forbidden zones, tech stack
│   ├── APP_BRIEF.md                   # Scope, hard gates, success criteria
│   ├── DATA_CONTRACT.md               # Types, service contracts, mocks
│   └── UI_SPEC.md                     # Screens, behavior, design system
│
├── _design/                           # OPERATOR-FILLED visual artifacts
│   ├── README.md                      # What goes here (Architect authors)
│   ├── brand-tokens.md                # (operator) primary hex, font, etc.
│   ├── style-tile.png                 # (operator) visual reference
│   ├── logo-color.svg                 # (operator) brand logo
│   ├── logo-mono.svg                  # (operator) single-color variant
│   ├── favicon.ico                    # (operator) favicon
│   └── reference/                     # (operator) optional context screenshots
│
├── _extraction/                       # OPERATOR-FILLED evidence
│   ├── README.md                      # What goes here (Architect authors)
│   └── (11 Brain Drain docs OR repurposed evidence)
│
├── skills/
│   └── stark-frontend-first/          # REUSABLE skill
│       ├── CLAUDE.md
│       ├── SKILL.md
│       ├── workflow/
│       │   ├── 00-discovery.md
│       │   ├── 01-types-and-contract.md
│       │   ├── 02-service-layer.md
│       │   ├── 03-mock-data.md
│       │   ├── 04-components.md
│       │   └── 05-verification.md
│       ├── references/
│       │   ├── SERVICE_LAYER_PATTERNS.md
│       │   ├── MOCK_DATA_PATTERNS.md
│       │   ├── COMPONENT_CONVENTIONS.md
│       │   └── ANTI_PATTERNS.md
│       └── templates/
│           ├── service.template.ts
│           ├── mock-data.template.ts
│           └── types.template.ts
│
├── playbook/                          # REUSABLE sub-phase build instructions
│   ├── 00-OVERVIEW.md
│   ├── 01-DISCOVERY.md
│   ├── 02-TYPES.md
│   ├── 03-SERVICES.md
│   ├── 04-MOCKS.md
│   ├── 05-COMPONENTS.md
│   ├── 06-VERIFICATION.md
│   ├── 07-RETROSPECTIVE.md
│   └── RETROSPECTIVES/                # Per-run lessons accumulate here
│
└── verification/                      # REUSABLE approval gate criteria
    ├── PHASE_GATES.md
    └── BUILD_CHECKLIST.md
```

**Total file count (skeleton):** ~30 files across ~12 folders.

**Per-FFM file count (after operator fills):** ~35-50 files including extracts and design assets.

---

## 22. Appendix B — Boot Prompts

Three boot prompt templates the operator uses to activate Claudy.

### B.1 — First Session (Fresh Boot)

```
You are Claudy, working on the <PROJECT_NAME> build under <OPERATOR_NAME>.

BOOT SEQUENCE — read in this exact order, then STOP:

1. Read your global CLAUDE.md (universal Stark doctrine).

2. Read this repo's root CLAUDE.md (starter kit conventions).

3. Read PROJECT_POINTER.md at repo root. It names the active FFM folder.

4. Read the kit-level references listed in PROJECT_POINTER.md:
   - agent_docs/starter-kit/starter-kit-handbook.md
   - agent_docs/starter-kit/COMPONENT_REGISTRY.md (if exists; skip if not)

5. Read the active FFM's navigation contract:
   - agent_docs/CURRENT_APP/<FFM_FOLDER>/CLAUDE.md
   
   Then follow that file's "Reading Order" section exactly.

6. Confirm required skills are present in .claude/skills/:
   - frontend-design
   - skill-creator
   - webapp-testing
   - stark-frontend-first
   If any are missing, surface — operator will install before proceeding.

7. Produce a structured Sub-Phase 0 Discovery summary per
   playbook/01-DISCOVERY.md Step 5.

8. STOP. Wait for "approved" before doing anything else.

Hard constraints during boot:
- Do NOT write any code
- Do NOT modify any files
- Do NOT advance past Sub-Phase 0
- Plan Mode applies even to reading
- Eyesight-aware: explanations before any code blocks

Karpathy Protocol applies: you are the hands, I am the architect. Move fast
but never faster than I can verify.

Go.
```

### B.2 — Resume Session (After Interruption)

```
Read RECOVERY.md at project root, then read the CLAUDE.md at
`agent_docs/CURRENT_APP/<FFM_FOLDER>/CLAUDE.md`, then continue from where
we left off.

Report the last completed sub-phase and propose the next sub-phase before
doing any work. STOP after the proposal.
```

### B.3 — Forbidden Zone Violation Recovery

```
STOP. You touched a forbidden zone.

Read `_project/CLAUDE.md` again and tell me which zone you violated.
Then we recover.

Do NOT continue executing until I approve the recovery plan.
```

### B.4 — Phase Boundary Skipped Recovery

```
STOP. You skipped a sub-phase boundary without my approval.

Roll back the work that wasn't approved.

Read the playbook for the current sub-phase and re-propose.

Do NOT advance until I approve.
```

### B.5 — Session-End Discipline

```
Update RECOVERY.md with the current state and the next action.

Don't start anything new. We end here.
```

---

## 23. Appendix C — Template Files (Stubs To Copy)

Use these as starting points when authoring a new FFM. Copy the stub, adapt to your project.

### C.1 — Root `CLAUDE.md` Stub

```markdown
# CLAUDE.md — <PROJECT_NAME> / <PHASE_NAME> FFM

> **You are reading the entry point to a portable Factory module.**
> This file is the navigation contract for any AI coding tool that opens this folder.
> Read this first. Everything else is referenced from here.

---

## What This Module Is

This is the **<PROJECT_NAME> — Phase <N> Frontend-First Module (FFM)**.

A portable, reusable Factory artifact instantiated for Phase <N> (<PHASE_LABEL>) of the <PROJECT_NAME> build. Based on the App Factory Frontend-First Module pattern, adapted for <variant> Phase <N> work.

**Born from:** <previous FFM or pattern reference>.
**Adapted for:** <project specifics>.
**Owner:** <organization>.
**Operator:** <name + alias>.
**License:** Internal Factory tooling.

---

## What's Different About This FFM (vs the baseline pattern)

| Aspect | Baseline FFM | This FFM |
|---|---|---|
| ... | ... | ... |

(Document the variant differences.)

---

## Vendor Neutrality

This module is **tool-agnostic**...

(Copy the vendor neutrality section from a previous FFM.)

---

## Reading Order (MANDATORY)

1. **This file** — navigation contract
2. **`_project/CLAUDE.md`** — project spine
3. **`_project/APP_BRIEF.md`** — scope, hard gates
4. **`_project/DATA_CONTRACT.md`** — data shapes
5. **`_project/UI_SPEC.md`** — screen behavior
6. **`playbook/00-OVERVIEW.md`** — build plan
7. **Each phase file under `playbook/`** — on demand
8. **Skills** under `skills/` — auto-activate when triggers fire
9. **`_extraction/`** — referenced on demand for ambiguity
10. **`_design/`** — visual reference

Conflict resolution: `DATA_CONTRACT.md` wins on data shapes, `UI_SPEC.md` wins on UI behavior, `_project/CLAUDE.md` wins on scope, this file wins on module structure. If two sources still conflict, STOP and surface to the operator.

---

## Folder Map

(Insert the actual folder map for this FFM.)

---

## Activation Contract

When the operator stages this module into the <starter kit> and opens an AI tool, the first prompt should be:

> *(Insert the boot prompt with the actual FFM folder name.)*

---

## Forbidden Zones (Hard Stops)

(List concrete, enforceable prohibitions specific to this phase.)

---

## Skill Inventory

(List skills that ship with this FFM and skills the operator installs separately.)

---

## What Is Reusable vs Per-Project

(Reuse table from a previous FFM, adapted.)

---

## Evolution Principle

(Copy from a previous FFM.)

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | <date> | Initial FFM for <project> <phase>. |
```

### C.2 — `_project/APP_BRIEF.md` Stub

```markdown
# APP BRIEF — <PROJECT_NAME> / Phase <N>: <PHASE_LABEL>

> **Status:** LOCKED
> **Phase:** <N> of <TOTAL>
> **Predecessor:** Phase <N-1>
> **Successor:** Phase <N+1>
> **Author:** Architect Agent (Claude) for <operator>

---

## 1. Mission Of This Phase

(One paragraph: what this phase exists to do.)

---

## 2. Hero Outcome

> **(One sentence: what success looks like, observably.)**

---

## 3. In Scope (Phase <N> Only)

- ...
- ...

---

## 4. Out of Scope (Phase <N>)

- ❌ ... (Phase <X>)
- ❌ ... (Phase <Y>)

---

## 5. Hard Gates

| Gate | Verification |
|---|---|
| **G1** ... | ... |
| **G2** ... | ... |
...

---

## 6. Success Criteria Table

| Criterion | How to verify |
|---|---|
| ... | ... |

---

## 7. Known Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| ... | ... | ... |

---

## 8. Common Stumbles (Watch For These)

| Stumble | Why it happens | Fix |
|---|---|---|
| ... | ... | ... |

---

## 9. Estimated Effort

**<N> sessions** per the locked PHASE_ROADMAP.

---

## 10. Handoff To Next Phase

(What becomes available to Phase <N+1>.)

---

## 11. Constraints

(Non-negotiable rules.)

---

## 12. Phase Transitions

(Where each phase fits in the roadmap.)

---

## 13. Changelog

| Version | Date | Changes |
|---|---|---|
| 1.0 | <date> | Initial. |
```

### C.3 — `_design/README.md` Stub

```markdown
# _design/ — Operator Fills

> This folder is the canonical visual reference for Phase <N>.

## What Goes Here

### Required

1. **Brand tokens summary** — `brand-tokens.md` with primary hex, font, logo refs
2. **Logo files** — color SVG, mono SVG, favicon
3. **Style tile** — visual reference image

### Optional

4. **Reference screenshots** for visual context
5. **Wireframes** from designer

## How Claudy Uses This Folder

(Copy from a previous FFM, adapt.)

## File Naming Convention

(Copy the directory tree from a previous FFM, adapt.)

## Operator Notes

(Brief instructions for filling.)
```

### C.4 — `_extraction/README.md` Stub

```markdown
# _extraction/ — Operator Fills

> This folder holds **evidence-labeled extracts** that informed Phase <N>'s authoring.

## What Goes Here

### For This Phase

(List the specific extraction docs the operator should drop in.)

## How Claudy Uses This Folder

Claudy reads `_extraction/` **on demand**, not at activation.

(Document when in the run.)

## File Naming Convention

(Directory tree.)

## Why `_extraction/` For Greenfield?

(If greenfield, explain the repurpose.)

## Operator Notes

(Brief instructions for filling.)
```

### C.5 — `_project/CLAUDE.md` Stub (Project Spine)

```markdown
# _project/CLAUDE.md — <PROJECT_NAME> / Phase <N> / Project Spine

> **Project-specific direction.** Read AFTER the module root `CLAUDE.md`.

---

## Project Identity

**Project:** <name>
**Phase:** <N> of <TOTAL> — <label>
**Repos in scope:** <list>
**Source:** <starter kit details>
**Mission of this phase:** <one paragraph>

---

## Hero Outcome

> **(Same as APP_BRIEF § 2 — intentional redundancy.)**

---

## Forbidden Zones (Hard Stops — Phase <N> Specific)

(Same as APP_BRIEF § Forbidden Zones — expanded with category headers.)

---

## Tech Stack (Phase <N>)

(Table matching APP_BRIEF.)

---

## What Phase <N> Ships

(Same as APP_BRIEF § In Scope — intentional redundancy.)

---

## Lessons From Previous Phase

(Pull forward from `playbook/RETROSPECTIVES/RUN_<N-1>_LESSONS.md`.)

---

## Skills Loaded For This Project

(List skills + activation triggers.)

---

## Operating Rules (Inherited from Stark Global CLAUDE.md)

(Plan Mode, Karpathy Protocol, eyesight-aware, surgical changes, surface conflicts, code-over-model, fail-loud, token budget.)

---

## TDD Flow (Stark Standard)

Build → Unit Test → Integrate → Block Test → System Test → Finalize

---

## Approval Gates

(Sub-phase boundaries.)

---

## Conflict Resolution

(Precedence order.)

---

## Version History
```

### C.6 — `skills/stark-frontend-first/SKILL.md` Frontmatter Stub

```yaml
---
name: stark-frontend-first
description: Build the frontend of a Next.js application using a service layer with mock data as the sole swap point for later backend integration. Use this skill when a project is in frontend-first phase, when authoring a foundation skeleton (Phase 1 of a multi-phase build), or when the project's FFM declares mock-data mode. Enforces service layer discipline, mock data conventions, type-driven contracts, and forbids backend code authoring for entities not yet in scope.
---

# Stark Frontend-First Skill

(Body content per Section 11.3.)
```

---

## Closing Doctrine

> **Build the FFM once per phase. Operate it forever. The Architect's only job is to remember where the pattern lives.**

This playbook is that pattern.

If you author an FFM that:
- Requires the operator to remember more than where the FFM folder lives
- Skips Plan Mode or eyesight-aware communication
- Modifies files it shouldn't
- Lets Claudy drift into forbidden zones
- Buries lessons in sycophantic retrospectives

The FFM has failed its purpose.

Use this playbook. Study the worked examples. Author the FFM with discipline. Test it with a real run. Update the playbook with what you learn.

The factory compounds. Every FFM run sharpens the next. Every retrospective surfaces a lesson worth promoting. Every Architect who reads this playbook starts from a stronger baseline than the one before.

🛡️ **End of FFM Playbook v1.0.**
