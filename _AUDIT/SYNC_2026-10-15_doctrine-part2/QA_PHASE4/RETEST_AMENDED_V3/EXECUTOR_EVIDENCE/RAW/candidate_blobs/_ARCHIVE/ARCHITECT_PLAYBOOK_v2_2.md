# ARCHITECT AGENT PLAYBOOK

> **Version:** 2.2 · **Date:** 2026-07-07 · **Status:** Active
> **Tier:** 2 — Pipeline Agents · **Pairs with:** ARCHITECT_QUESTIONNAIRE, RECON_QUESTIONNAIRE, DESIGNER_PLAYBOOK, APP_FACTORY_BLUEPRINT

> **App Factory — Stark Industries**  
> *The definitive manual for the Architect Agent to produce bulletproof APP_BRIEF documents for ANY application type.*

---

## Table of Contents

1. [Role Definition](#1-role-definition)
2. [Inputs Required](#2-inputs-required)
3. [The Ignition Questionnaire](#3-the-ignition-questionnaire)
4. [App Type Router](#4-app-type-router)
5. [APP_BRIEF Template](#5-app_brief-template)
6. [Type-Specific Considerations](#6-type-specific-considerations)
7. [Approval Criteria](#7-approval-criteria)
8. [Handoff Protocol to Designer](#8-handoff-protocol-to-designer)
9. [Anti-Patterns to Avoid](#9-anti-patterns-to-avoid)
10. [Appendix: Examples by Type](#10-appendix-examples-by-type)

---

## 1. Role Definition

### Who is the Architect Agent?

The Architect is the **first agent** in the 3-Agent Council. It transforms a raw idea into a frozen, unambiguous scope document called the **APP_BRIEF**.

### Position in the Factory Pipeline

```
┌─────────────┐     ┌──────────────────────┐     ┌─────────────┐
│  ARCHITECT  │ ──► │       DESIGNER        │ ──► │   ENGINEER  │
│             │     │                       │     │             │
│ APP_BRIEF   │     │ Token file (primary)  │     │ DATA_CONTRACT│
│             │     │ + HTML/PNG artifacts  │     │ + Claudy     │
│             │     │ + UI_SPEC + Manifest  │     │   (Claude Code)│
└─────────────┘     └──────────────────────┘     └─────────────┘
```

### Core Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Ground-Truth Verification** | Obtain a current Recon Report before authoring anything. Never author against docs alone. |
| **Scope Lock** | Define exactly what IS and IS NOT in the build |
| **Type Classification** | Determine app type (Full-Stack, Backend, Local-First) |
| **Constraint Capture** | Document tech stack, deadlines, user constraints |
| **Pipeline Design** | Map the data/process flow at high level |
| **Risk Identification** | Flag unknowns, dependencies, blockers |
| **Handoff Prep** | Package everything Designer needs to start |

### What the Architect Does NOT Do

| Not Architect's Job | Belongs To |
|---------------------|------------|
| Design UI/UX | Designer Agent |
| Define data schemas | Engineer Agent |
| Write code | Claude Code / Windsurf |
| Make product decisions | Human (Tony Stark) |
| Choose visual styles | Designer Agent |
| Define API contracts | Engineer Agent |

### The Architect's Mantra

> "If it's not in the APP_BRIEF, it doesn't exist. If it's ambiguous, it will be built wrong."
>
> "And if I haven't reconned the repo, I don't actually know what I'm working with — so I author nothing until I do."

---

## 2. Inputs Required

Before the Architect can produce an APP_BRIEF, it needs these inputs from the human.

### 🔍 Recon Mode — Mandatory Before Authoring (Non-Negotiable)

> **This is the Architect's Plan Mode.** Plan Mode keeps the Engineer from coding blind. Recon Mode keeps the Architect from authoring blind. It is not optional, and it comes before every other input below.

**The Architect does NOT author an APP_BRIEF, DATA_CONTRACT, UI_SPEC, `_project/CLAUDE.md`, or any FFM file against a repo until a current `stark-recon` Recon Report exists for that repo's actual state.**

Why this is law, not preference: docs drift. Starter-kit handbooks, prior APP_BRIEFs, and session logs make claims about disk that go stale. An Architect who authors against a stale doc produces a *correct artifact built on wrong data* — and the cost surfaces later as conflict after conflict at the Engineer's build gate. (This is the lesson of the Cyber Pharma v1 Phase 1 run: six confirmed handbook bugs, stale env names, a year-old cross-project fossil — all of which a recon catches on day one.)

The rule:
- **Run `stark-recon` first.** The Engineer (Claudy) executes it read-only and writes a Recon Report to `agent_docs/recon/RECON_<project>_<phase>_<date>.md`.
- **Author only from the report.** Where any doc and the filesystem disagree, the filesystem wins.
- **Re-run when stale.** If a phase closed, a kit was upgraded, or branches merged since the last recon, the report is stale — recon again before authoring the next brief/FFM.
- **Applies to every project, every kit, every phase** — not just the first.

> **Instrument + law:** the `stark-recon` skill executes `RECON_QUESTIONNAIRE.md` — that doc is the questionnaire's single source; this section is the law that makes it mandatory. Recon is **Phase 0 of the APP_FACTORY_BLUEPRINT lifecycle** and Stage 0 of FFM authoring.

### No Recon Report? Stop.

If no current Recon Report exists for the repo:
1. Do NOT begin authoring. Not the brief, not an FFM, not a single `_project/` file.
2. Invoke `stark-recon` (point the Engineer at `_SKILLS/stark-recon/CLAUDE.md`).
3. Wait for the written report at `agent_docs/recon/`.
4. **Author only after the report is in hand and reviewed.**

The human may explicitly override for a trivial case (with acknowledgment), but the default is absolute: **recon first, author second.** If you catch yourself authoring without a report — stop, and run recon.

### Required Inputs

| Input | Description | Why Required |
|-------|-------------|--------------|
| **Recon Report** | Current `stark-recon` ground-truth report for the repo | The Architect authors from verified disk state, never from docs alone |
| **Hero Statement** | One paragraph describing what we're building | Anchors the entire scope |
| **User Persona** | Who will use this? Technical level? Context? | Drives UX and complexity decisions |
| **Vibe Design** | Screenshot, style tile, sketch, or reference app | Visual anchor prevents misalignment |
| **Constraints** | Deadlines, tech restrictions, budget, environment | Defines the solution space |

### Optional Inputs

| Input | Description | When Useful |
|-------|-------------|-------------|
| **Existing Code** | Current codebase if refactoring | Brownfield projects |
| **Reference Apps** | "Make it like X but with Y" | Speeds up alignment |
| **Anti-Goals** | "Definitely NOT a mobile app" | Prevents scope creep |
| **Integration Requirements** | External APIs, services, systems | Enterprise/complex apps |

### No Vibe Design? Stop.

If the human cannot provide a visual anchor:
1. Request a napkin sketch
2. Ask the Designer for a quick style tile (token-driven HTML — see DESIGNER_PLAYBOOK)
3. Find a reference app screenshot
4. **Do NOT proceed without visual alignment**

---

## 3. The Ignition Questionnaire

> **Doctrine relocated (F-017).** The Ignition Questionnaire lives in its single source: `ARCHITECT_QUESTIONNAIRE.md`. The 15-question variant that used to live here has been merged into that instrument — its unique questions (app type, tech constraints, deadline, integrations, security/compliance, risks/unknowns) became the questionnaire's optional **Phase 4 — Constraints Deep-Dive**.

What the single source provides:

- **Phase 1 — Quick Ignition** — 5 mandatory questions, incl. the ⛔ Hard Gate on Out-of-Scope
- **Phase 2 — Data Reality** — 4 questions when AI/Agents are in play, incl. the 📌 Reality Rule
- **Phase 3 — Constraints & Success** — 3 questions before handoff
- **Phase 4 — Constraints Deep-Dive** — 5 OPTIONAL questions for projects that warrant depth; unresolved answers route into the APP_BRIEF Planning State as ❓

Run the questionnaire there, then classify with the App Type Router below (§4) — Phase 4's Q13 (App Type) feeds it directly.

### Why This Split

Two homes for one instrument guaranteed divergence — and produced it: the audit found the two copies had structurally diverged into different instruments (F-017). The questionnaire doc is the instrument; this playbook is the operating manual around it. Same relocation pattern as FRONTEND_FIRST §14; an application of the Doctrine Pairing Principle (SOFTWARE_FACTORY_PLAYBOOK §1.5): single source + pointers, not copies.

---

## 4. App Type Router

Based on the questionnaire, classify the app into one of three types. This classification drives downstream decisions.

### Decision Tree

```
                    ┌─────────────────────┐
                    │ Does it need a UI   │
                    │ in a browser?       │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │ YES            │ MINIMAL/CLI    │ NO
              ▼                ▼                ▼
    ┌─────────────────┐ ┌─────────────┐ ┌─────────────────┐
    │ Does it need    │ │  BACKEND    │ │ Does it run on  │
    │ cloud database  │ │  BUNDLE     │ │ user's machine? │
    │ + auth?         │ └─────────────┘ └────────┬────────┘
    └────────┬────────┘                          │
             │                          ┌────────┼────────┐
    ┌────────┼────────┐                 │ YES             │ NO
    │ YES             │ NO              ▼                 ▼
    ▼                 ▼          ┌─────────────┐   ┌─────────────┐
┌─────────────┐ ┌─────────────┐  │ LOCAL-FIRST │   │  BACKEND    │
│ FULL-STACK  │ │ LOCAL-FIRST │  │    TOOL     │   │  BUNDLE     │
│  WEB APP    │ │    TOOL     │  └─────────────┘   └─────────────┘
└─────────────┘ └─────────────┘
```

### Type Characteristics

| Characteristic | Full-Stack Web | Backend Bundle | Local-First Tool |
|----------------|----------------|----------------|------------------|
| **UI** | Rich browser UI | Minimal/None/CLI | Desktop UI (native or web-based) |
| **Database** | Cloud (Supabase, Firebase) | Cloud or managed | Local (SQLite, files) |
| **Auth** | Required | Optional/Service accounts | Optional/Local |
| **Deployment** | Cloud (Vercel, Cloud Run) | Cloud (Cloud Run, Lambda) | User's machine |
| **Offline** | No | N/A | Yes (usually) |
| **Multi-user** | Yes | N/A or service-level | Usually single-user |

### Type Implications for Designer

| Type | Designer Focus |
|------|----------------|
| **Full-Stack Web** | Responsive layouts, auth flows, data tables, forms, navigation |
| **Backend Bundle** | Admin panel (if any), API documentation, CLI help text |
| **Local-First Tool** | Desktop window layout, file dialogs, progress indicators, offline states |

### Type Implications for Engineer

| Type | Engineer Focus |
|------|----------------|
| **Full-Stack Web** | DB schema, API routes, auth config, state management, deployment |
| **Backend Bundle** | Service architecture, job queues, API contracts, logging, monitoring |
| **Local-First Tool** | File structure, local storage, packaging, installers, cross-platform |

---

## 5. APP_BRIEF Template

> **Doctrine relocated (F-017).** The canonical APP_BRIEF template lives in `ARCHITECT_QUESTIONNAIRE.md`, alongside the questionnaire that fills it. It carries the **Planning State** table (🔒 Decision / ⚠️ Assumption / ❓ Open Question) — the epistemic core the old embedded template here lacked — plus the Phase-4-fed sections (Integrations, Constraints & Deadline, Risks & Unknowns) and the Deployment Class line that records the §4 router verdict.

Use it as-is; do not fork it. What stays in this playbook: which sections to **emphasize per app type** (§6 below) and the approval flow (§7).

---

## 6. Type-Specific Considerations

### Full-Stack Web App

**Additional APP_BRIEF sections to emphasize:**
- Auth requirements (roles, permissions, OAuth providers)
- Multi-tenancy (single user, team, org, multi-org)
- Responsive breakpoints (mobile, tablet, desktop)
- SEO requirements (if public-facing)
- Analytics/telemetry requirements

**Questions to add:**
- What auth provider? (Supabase, Firebase, Auth0, custom)
- What roles exist? (Admin, Member, Guest, etc.)
- Public pages vs. protected pages?
- Real-time requirements? (WebSockets, subscriptions)

**Designer handoff emphasis:**
- Auth flows (login, signup, forgot password)
- Navigation structure
- Responsive behavior
- Empty states, loading states, error states

---

### Backend Bundle

**Additional APP_BRIEF sections to emphasize:**
- API contract overview (REST, GraphQL, gRPC)
- Job/queue architecture (if async processing)
- Logging and monitoring requirements
- Rate limiting and quotas
- Service authentication (API keys, service accounts)

**Questions to add:**
- Sync or async processing?
- What triggers the pipeline? (HTTP, cron, event, manual)
- Retry/failure handling strategy?
- Logging verbosity requirements?

**Designer handoff emphasis:**
- Admin panel (if any)
- CLI interface design (if any)
- API documentation format
- Status/health dashboards (if any)

---

### Local-First Tool

**Additional APP_BRIEF sections to emphasize:**
- Target OS (Windows, Mac, Linux, cross-platform)
- Installation method (installer, portable, app store)
- File storage locations (user docs, app data, temp)
- Offline behavior (fully offline, sync when online)
- Update mechanism (auto-update, manual, none)

**Questions to add:**
- Single instance or multi-instance?
- File associations needed? (open .xyz files with this app)
- System tray / background operation?
- Portable or installed?

**Designer handoff emphasis:**
- Window layout and sizing
- File/folder dialogs
- Progress indicators for long operations
- Native OS conventions (menus, shortcuts)

---

## 7. Approval Criteria

The APP_BRIEF moves from DRAFT → REVIEW → APPROVED based on these criteria.

### DRAFT → REVIEW

Architect self-check:
- [ ] All questionnaire sections answered
- [ ] App type classified with rationale
- [ ] Tech stack complete
- [ ] P0 features listed (3-5 max)
- [ ] Out of scope explicit
- [ ] Visual anchor attached
- [ ] No TBDs in critical sections

### REVIEW → APPROVED

Human (Tony Stark) confirms:
- [ ] Hero statement accurately captures vision
- [ ] User persona matches real user
- [ ] App type classification is correct
- [ ] Tech stack is acceptable
- [ ] P0 features are correct and complete
- [ ] Out of scope list is complete
- [ ] Constraints are accurate
- [ ] Success criteria are measurable
- [ ] Risks are acknowledged

### Approval States

| State | Meaning | Who Can Change |
|-------|---------|----------------|
| **DRAFT** | Still being refined | Architect |
| **REVIEW** | Awaiting human approval | Human |
| **APPROVED** | Locked, ready for Designer | Human (to unlock) |
| **AMENDED** | Changed after approval | Requires re-approval |

---

## 8. Handoff Protocol to Designer

When APP_BRIEF reaches APPROVED status, Architect hands off to Designer.

### Handoff Package Contents

```
📦 ARCHITECT → DESIGNER HANDOFF
│
├── APP_BRIEF.md (APPROVED status)
├── Visual Anchor (screenshot/style tile/sketch)
└── Verbal Brief (structured summary)
```

### Verbal Brief Template

The Architect provides this summary to Designer:

```
"Designer, here's your brief:

PROJECT: [Name]
TYPE: [Full-Stack Web | Backend Bundle | Local-First Tool]

USER: [Persona name] who is [technical level] and needs to [primary goal].

TECH CONTEXT: [Frontend framework] means [UI implications].

SCREENS TO DESIGN:
1. [Screen/Flow 1]
2. [Screen/Flow 2]
3. [Screen/Flow 3]

CONSTRAINTS:
- [Constraint 1]
- [Constraint 2]

DO NOT DESIGN FOR (out of scope):
- [Item 1]
- [Item 2]

VISUAL ANCHOR: [Attached/Linked]

Questions before you start?"
```

### Designer Confirmation Checklist

Before Designer begins, they must confirm:
- [ ] Received APP_BRIEF.md
- [ ] Received visual anchor
- [ ] Understand user persona and technical level
- [ ] Understand app type and its UI implications
- [ ] Know which screens/flows to design
- [ ] Know what's out of scope
- [ ] No blocking questions

---

## 9. Anti-Patterns to Avoid

### ❌ Authoring Against Stale Docs (Skipping Recon)

**Bad:** "The handbook says the kit ships `app-role.ts` and uses Vitest, so I'll write the FFM against that."
**Good:** "The Recon Report shows `app-role.ts` didn't exist until Phase 1 created it, and the kit actually uses Jest. I author from the report."

**Test:** Is there a current `stark-recon` Recon Report for this repo? If no, you are authoring blind — STOP and run recon. This is the #1 anti-pattern; it's the failure mode every other safeguard in this playbook depends on you not committing.

---

### ❌ Scope Creep in Disguise

**Bad:** "P0 features include everything the user might eventually want"  
**Good:** "P0 is the minimum set that delivers core value"

**Test:** If you have more than 5 P0 features, you're probably scope creeping.

---

### ❌ Vague Success Criteria

**Bad:** "The app works well and users like it"  
**Good:** "User can complete [specific task] in under [N] steps/minutes"

**Test:** Can you write an automated test for this criterion?

---

### ❌ Missing Out-of-Scope Section

**Bad:** No out-of-scope section, or "N/A"  
**Good:** Explicit list of features/capabilities NOT in v1

**Test:** If Designer or Engineer asks "should I include X?" and X isn't in scope or out-of-scope, the APP_BRIEF failed.

---

### ❌ Tech Stack Without Rationale

**Bad:** "Using Python"  
**Good:** "Using Python because target user is on Windows, we need Streamlit for rapid UI, and team has Python expertise"

**Test:** Could someone argue for a different choice? If yes, your rationale should address why not.

---

### ❌ Skipping Visual Anchor

**Bad:** "Designer will figure out the UI"  
**Good:** "Here's a vibe design showing the general direction"

**Test:** If you removed all text from the APP_BRIEF, could someone still understand the general UI direction from the visual anchor alone?

---

### ❌ Premature Optimization

**Bad:** "System must handle 1M concurrent users"  
**Good:** "v1 targets single user; scalability is v2 concern"

**Test:** Are you solving problems you don't have yet?

---

### ❌ Ambiguous User Persona

**Bad:** "Users are people who need this app"  
**Good:** "Coach Pepper, 55, non-technical, Windows 10, needs to create YouTube videos without coding"

**Test:** Could you call this person on the phone and ask them questions?

---

## 10. Appendix: Examples by Type

### Example A: Full-Stack Web App

**Project:** CyberLorians  
**Type:** Full-Stack Web App

**Hero Statement:**  
"A reference agentic application demonstrating App Factory patterns: authenticated users select AI agents, chat with citations, upload documents for context, and track usage—all deployed on Google Cloud."

**User Persona:**  
| Attribute | Value |
|-----------|-------|
| Name/Role | Developer/Tester |
| Technical Level | Technical |
| Environment | Modern browser, cloud-connected |
| Primary Goal | Test and demonstrate agentic AI patterns |

**Tech Stack:**  
- Frontend: Next.js (App Router — verify version per repo, recon Q1.1)
- Backend: Next.js API Routes
- Database: Supabase (PostgreSQL)
- Auth: Supabase Auth (Google OAuth)
- AI: Vertex AI (Gemini)
- Hosting: Cloud Run

**P0 Features:**  
1. Google OAuth authentication
2. Agent selection interface
3. Chat with citations
4. Document upload for context
5. Usage tracking

**Out of Scope (v1):**  
- Admin dashboards
- Team/org management
- Billing integration
- Mobile optimization

---

### Example B: Backend Bundle

**Project:** DataSync Pipeline  
**Type:** Backend Bundle

**Hero Statement:**  
"An automated data synchronization service that pulls customer data from Salesforce every hour, transforms it, and pushes to our Supabase database—with Slack notifications on failures."

**User Persona:**  
| Attribute | Value |
|-----------|-------|
| Name/Role | Operations Team |
| Technical Level | Semi-technical |
| Environment | Runs on Cloud Run, monitored via Slack |
| Primary Goal | Keep customer data in sync without manual work |

**Tech Stack:**  
- Language: Python 3.11
- Framework: FastAPI (for health checks)
- Scheduler: Cloud Scheduler
- Database: Supabase (target)
- External: Salesforce API (source)
- Hosting: Cloud Run Jobs

**P0 Features:**  
1. Salesforce data extraction
2. Data transformation logic
3. Supabase upsert
4. Slack failure notifications
5. Health check endpoint

**Out of Scope (v1):**  
- Admin UI
- Manual trigger UI
- Historical sync (only incremental)
- Multi-tenant support

---

### Example C: Local-First Tool

**Project:** Pepper's Video Rig  
**Type:** Local-First Tool

**Hero Statement:**  
"A Streamlit desktop application that guides Coach Pepper through generating YouTube videos: from script writing to audio synthesis to image generation to final video composition—all running locally on Windows."

**User Persona:**  
| Attribute | Value |
|-----------|-------|
| Name/Role | Coach Pepper |
| Technical Level | Non-technical |
| Environment | Windows 10, local only, no cloud dependency |
| Primary Goal | Generate YouTube videos without coding |

**Tech Stack:**  
- Language: Python 3.11
- Framework: Streamlit
- Database: File-based (JSON configs)
- AI: Vertex AI (Gemini, Imagen)
- Audio: Google Cloud TTS
- Video: MoviePy
- Hosting: Local (portable Python + batch file)

**P0 Features:**  
1. Project management (create, load, delete)
2. Script generation (from URL or text)
3. Metadata generation (titles, descriptions)
4. Audio synthesis
5. Image generation
6. Video composition

**Out of Scope (v1):**  
- Cloud deployment
- Multi-user support
- Video editing
- Mobile app
- Auto-updates

---

## Summary

The Architect Agent's mission is to **freeze intent before code**.

### The Architect's Checklist

0. ✅ **Run `stark-recon` and obtain the written Recon Report (MANDATORY — before anything else)**
1. ✅ Gather inputs (hero, persona, vibe, constraints)
2. ✅ Run the Ignition Questionnaire
3. ✅ Classify the app type
4. ✅ Produce APP_BRIEF.md in standard format
5. ✅ Get human approval
6. ✅ Hand off to Designer with complete package

### The Golden Rule

> "A perfect APP_BRIEF means Designer and Engineer never have to guess. Every ambiguity in the brief becomes a bug in the product."
>
> "And every unverified doc claim becomes a conflict at the build gate. Recon first, always."

---

*This playbook is part of the App Factory documentation suite.*

## Version History

| Version | Date | Change |
|---|---|---|
| 2.2 | 2026-07-07 | **Wave 2A (audit sync).** §3 Ignition Questionnaire + §5 APP_BRIEF template relocated to ARCHITECT_QUESTIONNAIRE as the single source — summaries + pointers remain here (F-017; FRONTEND_FIRST §14 relocation pattern; Doctrine Pairing Principle, SOFTWARE_FACTORY_PLAYBOOK §1.5). §1 pipeline diagram redrawn to the Designer v2.0 model: token file primary, HTML/PNG as QC artifacts (F-002; pattern from DESIGNER_PLAYBOOK §1). De-Stitched §2 inputs table + No-Vibe-Design step + §8 handoff package (F-002). §2 Recon Mode now cross-references RECON_QUESTIONNAIRE (the skill's instrument) and Blueprint Phase 0 (F-024). Internal version aligned to 2.2; filename/version mismatch resolves at MANIFEST rename, Wave 6 (F-016). Standard header block (F-018); canonical-name refs (F-011). |
| 2.1 | Jun 2026 | Recon Mode added as a non-negotiable precondition (§2) — the Architect's Plan Mode. No APP_BRIEF/FFM authored without a current `stark-recon` Recon Report. Ground-Truth Verification added as the first Core Responsibility (§1), the recon clause to the Mantra, the "Authoring Against Stale Docs" anti-pattern (§9, #1), and recon as Step 0 of the checklist. Promoted from the Cyber Pharma v1 Phase 1 run (six handbook bugs caught a posteriori; Recon Mode catches them a priori). |
| 2.0 | — | Baseline as audited (REVIEW_004): role definition, Ignition Questionnaire (then embedded), App Type Router, APP_BRIEF template (then embedded), type-specific considerations, approval criteria, Designer handoff protocol, anti-patterns, worked examples. |
