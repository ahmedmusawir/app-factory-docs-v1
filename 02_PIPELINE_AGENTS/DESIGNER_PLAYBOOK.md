# DESIGNER AGENT PLAYBOOK

> **Version:** 2.1 · **Date:** 2026-07-07 · **Status:** Active
> **Tier:** 2 — Pipeline Agents · **Pairs with:** GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, THEMING_MANUAL, COMPONENT_REGISTRY, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK

> **App Factory — Stark Industries**
> *The definitive manual for the Designer Agent to produce consistent, implementation-ready UI for ANY application type.*
>
> **Core thesis:** *concrete artifacts survive, abstract intentions decay.* The Designer's output is **code that runs** (token-driven HTML + a tokens file), not a picture of a brand and not a prompt for an external tool.

---

## Table of Contents

1. [Role Definition](#1-role-definition)
2. [Inputs Required](#2-inputs-required)
3. [Design Modes](#3-design-modes)
4. [The Canonical Page Method](#4-the-canonical-page-method)
5. [The Production Method: Token-Driven HTML + Playwright](#5-the-production-method-token-driven-html--playwright)
6. [Common UI Patterns (Field Tested)](#6-common-ui-patterns-field-tested)
7. [Screen-by-Screen Discipline](#7-screen-by-screen-discipline)
8. [Deliverables + UI_SPEC Template](#8-deliverables--ui_spec-template)
9. [Type-Specific Considerations](#9-type-specific-considerations)
10. [Handoff Protocol to Claudy (Engineer)](#10-handoff-protocol-to-claudy-engineer)
11. [Anti-Patterns to Avoid](#11-anti-patterns-to-avoid)
12. [Appendix: Lessons from the Field](#12-appendix-lessons-from-the-field)
13. [Cross-References (Doctrine Docs)](#13-cross-references-doctrine-docs)

---

## 1. Role Definition

### Who is the Designer Agent?

The Designer is the **second agent** in the 3-Agent Council. It transforms the APP_BRIEF into a running, token-driven visual system that locks screen intent, user flows, and interaction patterns before Claudy writes the real app.

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
| **Token authorship** | Define/inherit the semantic token set (all modes) — the executable system |
| **Visual translation** | Convert APP_BRIEF scope into token-driven HTML screens |
| **Consistency enforcement** | Maintain visual coherence via the canonical screen + clone-and-adapt |
| **Flow definition** | Map user journeys through the interface |
| **Intent locking** | Freeze what each screen DOES before code |
| **Constraint surfacing** | Expose bad assumptions through real, rendered visuals |
| **Handoff prep** | Package HTML (build ref) + PNG (QC target) + tokens + spec + manifest |

### What the Designer Does NOT Do

| Not Designer's Job | Belongs To |
|--------------------|------------|
| Define app scope | Architect Agent |
| Write the production app | Engineer Agent / Claudy |
| Define data schemas | Engineer Agent |
| Make product decisions | Human (Tony Stark) |
| Invent components the kit can compose | Flag a KIP instead |

### The Designer's Mantra

> "One good screen is worth more than five inconsistent ones. The tokens are the system; the canonical screen proves them. Visuals expose what docs hide."

---

## 2. Inputs Required

Before the Designer can work, it needs these inputs.

### Required Inputs

| Input | Source | Why Required |
|-------|--------|--------------|
| **APP_BRIEF.md** | Architect | Defines scope, features, constraints, hard gates |
| **Tailwind major version** | `package.json` | Decides token format (TW3 = HSL in `globals.css`/`globals.scss`; TW4 = `@theme inline` OKLCH) |
| **Token well / theme** | Theme Library + token file | The palette to inherit or extend (don't reinvent) |
| **Visual anchor (if any)** | Architect / brainstorm | IA/layout reference only — repaint in our tokens, never visually copy |
| **App type + persona** | APP_BRIEF | Drives complexity and UX decisions |
| **P0 features** | APP_BRIEF | What screens must exist |

### Pre-Flight Checklist

Before starting, the Designer confirms:
- [ ] APP_BRIEF status is APPROVED
- [ ] Kit's Tailwind version confirmed in `package.json`
- [ ] The token set to inherit/extend is identified (Theme Library)
- [ ] P0 features + out-of-scope hard gates are listed
- [ ] The canonical screen candidate is chosen

---

## 3. Design Modes

### Mode 1: Demo / Prototype Mode (The Default)

**Purpose:** Rapid visualization for validation and backend guidance.

| Characteristic | Value |
|----------------|-------|
| **Goal** | Functional clarity |
| **Fidelity** | Low to medium |
| **Polish** | Minimal |
| **Consistency** | Token discipline + layout reuse mandatory |
| **Output** | Token-driven HTML + PNG renders |

**Mindset:**
> "Does this communicate intent, on real tokens? Ship it."

### Mode 2: Production Mode

**Purpose:** Polished, scalable UI for end users.

| Characteristic | Value |
|----------------|-------|
| **Goal** | User-experience excellence |
| **Fidelity** | High |
| **Polish** | Full |
| **Consistency** | Full token + component system |
| **Output** | Token file, component manifest, full HTML/PNG set, specs |

> Both modes produce the **same kind** of artifact (token-driven HTML). Demo Mode simply accepts lower polish. Polish is a dial, not a different tool.

---

## 4. The Canonical Page Method

### The Problem

Without a single locked reference, multi-screen design drifts — spacing, color, and layout wander screen to screen. (This was true of external generators; it is equally true of any screen built from scratch each time.)

### The Solution: Canonical Page Method (tool-agnostic)

#### Step 1: Build ONE Perfect Screen
- Identify the most representative screen (often the home/dashboard or the dominant content pattern, e.g. a card-grid directory).
- Build it as **token-driven HTML**. Iterate until it's right.
- This becomes the **Canonical Screen**.

#### Step 2: Lock the Canonical Screen
- Render it to PNG with Playwright (light **and** dark).
- The canonical **HTML + PNG** is now the anchor for everything that follows.
- Human approval gate: lock before proceeding.

#### Step 3: Clone, Don't Re-Create
- **Do NOT design new screens from a blank file.**
- **DO copy the canonical HTML and adapt it** — change the *content region*, keep the *structure* (shell, grid, spacing, type scale).
- Other themes/modes are pure token swaps — never hand-edited per screen.

---

## 5. The Production Method: Token-Driven HTML + Playwright

> This section replaces the retired external-tool protocol. The Designer **builds the screens directly**; there is no third-party generator in the loop.

### Why HTML, not an external generator

- **No diversity drift.** The Designer controls every element, so the canonical layout holds.
- **Executable, not a picture.** The HTML reads the same semantic tokens Claudy will use, so what you see is what gets built.
- **One source of truth.** The canonical HTML is edited and cloned — not regenerated — so structure never wanders.

### The Render Loop

1. **Tokens first.** Inherit or author the semantic token set (all modes) in `globals.css` (in the Cyber Pharma kit this file is `globals.scss` — confirm per kit; TW 3.4 → HSL-no-wrapper).
2. **Write the canonical screen** as token-driven HTML — semantic utilities only (`bg-primary`, `text-destructive`, `bg-card`, `border-border`). Never numbered palette classes (`bg-slate-800`).
3. **Render to PNG with Playwright** at **2x device scale**, in light and dark.
4. **Review** both modes against the brief; tune tokens (not hardcoded values) where contrast or elevation fails.
5. **Lock** at the human approval gate.
6. **Clone-and-adapt** the remaining screens from the canonical HTML.

### What ships, and what each artifact is for

- **HTML is load-bearing for Claudy** — it is the literal build reference.
- **PNG is the QC target** — the human/at-a-glance proof and the thing Claudy verifies against.
- Always ship **both** for the style tile and every screen.
- **Tokens are the contract.** If a screen needs a color outside the token set, the token set is wrong — surface it, don't bypass it.

---

## 6. Common UI Patterns (Field Tested)

These patterns are tool-agnostic and validated in real builds. Express each in kit primitives + semantic tokens.

### Pattern A: The "One-of-N" Selector
**Use Case:** User must choose *one* option from a set (e.g. selecting a title).

- **Do Not Use:** Plain bullet points (ambiguous).
- **Do Use:** **Radio Cards** (cards that behave as a radio group).
- **Visual State:** One option always shown selected (brand-token border / filled radio) to signal interactivity.
- **Build note:** selected state reads from `--ring`/`--primary`; never a hardcoded accent.

### Pattern B: The Utility List
**Use Case:** Output is meant for *external use* (e.g. copying text elsewhere).

- **Do Not Use:** Selection circles.
- **Do Use:** **Copy-Ready List** — clean rows with a right-aligned copy action.
- **UX:** Implies a utility ("copy to clipboard"), not a decision gate.

### Pattern C: The Media Player
**Use Case:** Displaying audio or video results.

- **Do Not Use:** Static loading bars or empty placeholders.
- **Do Use:** The **"Ready State" Player** — play/pause, progress/waveform, timestamp, volume.
- **Grouping:** Place configuration (e.g. voice select) directly *above* the player to show cause-and-effect.

---

## 7. Screen-by-Screen Discipline

### The Rule
**One screen per step. One purpose per screen. Lock before moving on.**

### The Sequence
1. **Identify all screens** from APP_BRIEF P0 features.
2. **Order them** by user flow (not importance).
3. **Build the canonical screen** → render → review light+dark → lock.
4. **Clone-and-adapt** the next screen → render → review → lock.
5. **Repeat** until all screens are complete.

### Screen Locking Checklist
Before moving on:
- [ ] Purpose is clear
- [ ] All required elements present (per §5.6 minimum display fields, if defined)
- [ ] Matches the canonical structure (shell, grid, spacing, type)
- [ ] Tokens only — zero hardcoded color
- [ ] Light + dark render captured (Playwright PNG)
- [ ] 375px holds (or desktop-orientation explicitly declared)
- [ ] Notes documented in UI_SPEC

---

## 8. Deliverables + UI_SPEC Template

### The Designer's Deliverables (per project)

| # | Deliverable | What it is |
|---|---|---|
| 1 | **Token file** (`globals.css`/`globals.scss` + Tailwind map) | The executable system — all modes. **Primary deliverable.** |
| 2 | **Style tile** (HTML + PNG) | The visual contract / live contrast proof |
| 3 | **Screen artifacts** (HTML + PNG) | Each screen in the canonical theme; HTML = build ref, PNG = QC |
| 4 | **UI_SPEC.md** | Hierarchy, gating, empty/loading/error states, responsive rules, checkpoints |
| 5 | **Component manifest** | Primitives per screen + KIPs to build first |

### UI_SPEC Template

```markdown
# UI_SPEC: [Project Name]

> **Version:** 1.0
> **Status:** APPROVED
> **Design Mode:** Demo

## 1. Design Overview
**Canonical Screen:** [Which screen is the anchor]
**Token theme:** [e.g. Metro Warm — Mist/Slate]

## 2. Screen Inventory
| # | Screen Name | Pattern | Status |
|---|-------------|---------|--------|
| 1 | [name] | [card grid / form / table] | Locked |

## 3. Visual System (reads from the token file)
- **Layout:** [Sidebar + content, etc.]
- **Type:** [typeface, scale]
- **Radius:** [--radius value]
- **Active/selected state:** [token-driven description]

## 4. Responsive Rules
- Base target 375px; transforms: sidebar→drawer, table→cards, KPI→2×2.
- (Ops consoles: state desktop-orientation explicitly if applicable.)

## 5. Screen Specifications (repeat per screen)
### Screen X: [Name]
- **Purpose:** [Description]
- **Elements:** [buttons/inputs/cards]
- **Gating Logic:** [what enables the primary action]
- **Empty / Loading / Error states:** [each defined]
- **Human-in-the-loop checkpoints:** [confirmations, typed confirms]
```

---

## 9. Type-Specific Considerations

### Full-Stack Web App
- Focus: auth flows, tables, dashboards, card grids.
- Reflow discipline: wide tables become stacked cards at 375px.

### Operations / Admin Console (e.g. superadmin)
- May be **desktop-oriented** — but say so explicitly in the UI_SPEC.
- Still honor mobile transforms unless the brief declares desktop-only.
- Hard-gate discipline: forbidden controls do not render **even disabled**.

### Local-First Tool (Cyberize Style)
- Focus: sidebar navigation, file inputs, progress steps.
- **Key Lesson:** keep the layout a *tool*, not a SaaS landing page.

---

## 10. Handoff Protocol to Claudy (Engineer)

### Handoff Package Contents

1. **APP_BRIEF.md** (approved)
2. **Token file** (`globals.css`/`globals.scss` + Tailwind map)
3. **Style tile** (HTML + PNG)
4. **Screen artifacts** (HTML + PNG, the locked set)
5. **UI_SPEC.md** (approved)
6. **Component manifest** (primitives + KIPs)

### What Claudy Actually Needs

- **HTML to build from** (structure + token usage, verbatim).
- **PNG to verify against** (the QC target).
- **Tokens to inherit** (the contract — no reinterpretation).
- **Locked screen intent** (what each control does).
- **Gating logic** (when actions are enabled) and **dependency order**.

---

## 11. Anti-Patterns to Avoid

### ❌ "Design all the screens at once"
**Why:** Structure drifts. **Fix:** Canonical screen first, then clone-and-adapt — one screen per step.

### ❌ "Make it modern / beautiful"
**Why:** Ambiguous; invites inconsistency. **Fix:** "Match the canonical structure exactly; colors come from tokens."

### ❌ Numbered Tailwind colors in markup (`bg-slate-800`, `text-red-600`)
**Why:** Bypasses the token file and silently breaks theming. **Fix:** Semantic utilities only (`bg-card`, `text-destructive`).

### ❌ Brand color used as a status color
**Why:** Semantic collision. **Fix:** Keep `--primary` for brand; status reads `--success`/`--destructive`/`--warning`/`--info`.

### ❌ A partial theme (light only, or missing semantic tokens)
**Why:** Dark mode and contrast break later. **Fix:** Declare light + dark, full token set, from day one.

### ❌ Desktop-first "make it responsive later"
**Why:** 375px breaks. **Fix:** Rule Zero — design 375 first.

### ❌ Inventing a component the kit can compose
**Why:** Parallel component library. **Fix:** Compose from shadcn primitives; flag genuine gaps as a KIP.

### ❌ Letting the canonical HTML drift from the tokens
**Why:** The "change one file, re-theme everything" promise dies. **Fix:** Edit tokens, not screens, for visual change.

---

## 12. Appendix: Lessons from the Field

**1. Visuals Expose Bad Assumptions**
The dual-input design (URL + text) on the video tool emerged *visually* — the docs missed it. Design is where scope gets corrected.

**2. Consistency Comes From the Canonical, Not Re-Generation**
Coherence is achieved by editing and cloning one locked canonical screen — never by rebuilding each screen from scratch and hoping it matches.

**3. Demo Mode is Liberating**
Accepting "functional clarity only" removes polish pressure and accelerates validation. Polish is a later dial.

**4. Tokens Are the Real Deliverable**
A pretty screen on hardcoded colors is a dead end. A modest screen on a clean token set re-themes in minutes and hands to Claudy without translation. Ship the system, not the screenshot.

---

## 13. Cross-References (Doctrine Docs)

This playbook is the *how-to-be-the-Designer* manual. It sits on top of the stable doctrine:

- **GLOBAL_DESIGN_SYSTEM_HANDBOOK.md** — the token contract, theming method, responsive transforms, accessibility bar, deliverables, and the Canonical Page workflow.
- **THEME_LIBRARY.md** — named, complete token value-sets (e.g. the Metro Warm family: Mist / Slate / Bright / Dark-deep).
- **THEMING_MANUAL.md** — token architecture, designer deliverable format, the quick-swap workflow.
- **TOKEN_FILE.md** — a **reference snapshot / drop-in template** (Cyber Pharma Metro Warm values) — NOT the live file. The live token values for the current project are **`globals.css`/`globals.scss`** in the project repo (ruling: GLOBAL_DESIGN_SYSTEM_HANDBOOK §8).
- **COMPONENT_REGISTRY / manifest** — primitive mapping + KIPs.

**Conflict rule:** if this playbook and a doctrine doc disagree on tokens or method, the doctrine doc wins — surface the conflict and update this playbook.

---

*This playbook is part of the App Factory documentation suite.*

## Version History

| Version | Date | Change |
|---|---|---|
| 1.4 | 5 Feb 2026 | Stitch "Batch Protocol", selection/utility patterns, media-player strategy integrated. |
| 2.0 | 9 Jun 2026 | **Stitch retired.** §5 "Stitch Protocol" replaced by "The Production Method: Token-Driven HTML + Playwright." Designer now builds canonical screens directly as token-driven HTML and renders to PNG via Playwright; clone-and-adapt operates on HTML, not tool prompts. Deliverables aligned to the Handbook (token file primary; HTML+PNG artifacts; UI_SPEC; component manifest). Removed Batch & Order image protocol, "re-upload anchor" rule, `[CONTEXT][CONSTRAINTS]…` prompt format, and all Stitch keywords. Anti-patterns + field lessons reframed; doctrine cross-references added. |
| 2.1 | 2026-07-07 | **Wave 2A micro-patch (audit sync).** §13 token-file reference corrected per the F-025 ruling: `TOKEN_FILE.md` = reference snapshot / drop-in template, NOT the live file — live token values are `globals.css`/`globals.scss` per GLOBAL_DESIGN_SYSTEM_HANDBOOK §8 (the doc's §5 was already correct; §13 was the stale outlier). THEMING_MANUAL reference de-versioned — canonical names only (F-011). Standard header block at top, version/date moved out of footer (F-018); "AI App Factory" → "App Factory". No structural or content changes — Tier 2 gold standard preserved. |
