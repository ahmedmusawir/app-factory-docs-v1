# HANDOFF PACKAGE PLAYBOOK

> **The instruction set for authoring project handoff packages.**
> Paired with the Cyberize Agentic Automation handoff as the canonical worked example.

**Version:** 1.0
**Born from:** Cyberize Agentic Automation Run 001 (May 2026) — first successful Factory frontend conversion
**Pairs with example:** `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/`

---

## 1. What This Playbook Is

This is the playbook for authoring the four canonical documents that drive every Factory build:

1. **APP_BRIEF.md** — scope, success criteria, forbidden zones
2. **DATA_CONTRACT.md** — types, service contracts, mock requirements
3. **UI_SPEC.md** — screen-by-screen behavior, primitive mapping
4. **_project/CLAUDE.md** — project spine, doctrine, tech stack

Together these four documents constitute a **handoff package**. When the package is complete and approved, Claudy can execute the build through 8 supervised phases with minimal operator intervention.

---

## 2. Why This Playbook Exists

In Cyberize Run 001, the handoff package worked. The four documents drove a successful build through 8 phases with 121 tests passing, 21 routes building clean, and a deployed product in three days. The reason it worked is the specific structure, level of detail, and discipline applied during authoring.

Without a playbook, that success is hard to replicate. Each future project would re-derive the structure from scratch, possibly missing things that made Run 001 work. This playbook captures the tacit knowledge so the next project starts from a proven template.

🎯 **The strategic move:** instruction set + worked example. AI agents perform dramatically better with concrete examples anchoring abstract rules. This playbook gives the rules; the Cyberize handoff gives the worked example.

---

## 3. When To Author A Handoff Package

A handoff package is authored when:

- ✅ A new project enters the Factory (Streamlit conversion, fresh build, prototype-to-production)
- ✅ Brain Drain extraction has been completed on the source app (when applicable)
- ✅ The operator has decided to commit to building this project
- ✅ Before any code is written in the new project's repo

A handoff package is NOT authored:

- ❌ For exploratory spikes or research-only work
- ❌ For projects where the architect (operator) intends to author code directly without delegating to Claudy
- ❌ For projects that haven't passed initial feasibility / scope review

---

## 4. Prerequisites Before Authoring

Before writing the handoff package, these inputs must exist:

| Input | Source | Purpose |
|---|---|---|
| Project scope decision | Operator | Confirms this is worth building |
| Source app (if conversion) | Existing app | Reference for behavior to preserve |
| Brain Drain extraction (if conversion) | `_extraction/` folder | Evidence-labeled source code analysis |
| Screenshots (if visual app) | `_design/` folder | Canonical visual reference |
| Starter kit identified | Operator | Knowing which kit the build runs on |
| Stack decisions locked | Operator | Framework, UI library, state, auth |

If any of these are missing, STOP. Surface to operator. Do not attempt to author a handoff package with incomplete inputs.

---

## 5. The Four Canonical Files — Authoring Rules

### 5.1 APP_BRIEF.md

**Purpose:** What we're building, what's in scope, what's forbidden.

**Canonical example:** `_project/APP_BRIEF.md` in the Cyberize module.

**Required sections (in order):**

1. **App Type** — internal tool, public product, prototype, etc.
2. **One-Sentence Purpose** — single sentence describing the build
3. **Who Uses This** — primary user, secondary users, NOT for
4. **Why We're Building It** — strategic context
5. **In Scope (Phase 1)** — screens, features, integrations included
6. **Out Of Scope (Phase 1) — HARD GATES** — explicit forbidden zones, numbered list, no ambiguity
7. **Success Criteria** — checkboxes that define "done"
8. **Tech Stack** — table format with layer + technology
9. **Source-Of-Truth Artifacts** — reading order, conflict resolution rules
10. **Known Discrepancies** — quirks of the source app preserved deliberately
11. **Constraints** — non-functional requirements
12. **Risks** — what could go wrong, mitigations
13. **Phase Transitions** — what's Factory work vs operator work
14. **Changelog** — version history

**Length expectation:** 200-300 lines. More than 400 means too much detail; reconsider scope.

**The hardest part:** Section 6 (forbidden zones). MUST be specific, numbered, non-negotiable. Examples from Cyberize:

- ❌ "No backend code authoring"
- ❌ "No real wrapper calls. All `/run_agent` and `/get_history` are mocked"
- ❌ "No new features not present in the source"
- ❌ "No 'improvements' to the original's behavior"

If forbidden zones are vague, Claudy will drift. If they're explicit and numbered, Claudy holds the line.

**Authoring discipline:**
- Every claim in the brief should be evidence-traceable to Brain Drain or operator decision
- Hard gates should be numbered (1, 2, 3...) not bulleted — easier to reference in conversations
- Out-of-scope is more important than in-scope; spend more authoring time there
- Success criteria should be machine-verifiable where possible (e.g., "npm run build succeeds")

---

### 5.2 DATA_CONTRACT.md

**Purpose:** Every data shape, every service contract, every mock requirement.

**Canonical example:** `_project/DATA_CONTRACT.md` in the Cyberize module.

**Required sections (in order):**

1. **Type-by-Type Reference** — every interface, every enum, every type
2. **Service Method Contracts** — every method the UI calls, its signature, its mock behavior, its BACKEND_SWAP_NOTES
3. **Mock Data Requirements** — what realistic mocks look like, what edge cases to cover
4. **Known Discrepancies** (if conversion) — drift between source app and contract
5. **Phase 2 Decision Points** — questions deferred to backend wiring phase
6. **Field-By-Field Mapping** (if conversion) — source-app fields to TypeScript fields
7. **Verification Checklist** — how to validate the contract is complete
8. **Changelog** — version history

**Length expectation:** 400-600 lines for medium projects. More for data-heavy projects.

**The critical discipline:**

- **Both mock and real must satisfy the contract.** If you wouldn't be able to swap the mock for a real backend without changing the contract, the contract is wrong.
- **Wire format conventions matter.** Snake_case for wire shapes (matches FastAPI/Pydantic convention typically); camelCase for UI-internal types.
- **No `any` types ever.** Use `unknown` with narrowing if truly unknown.
- **Enum values as string literal unions**, not `enum` keyword.
- **BACKEND_SWAP_NOTES per service method** — explicit instructions for Phase 2 wiring.

**Common authoring mistakes:**

- Inventing fields that aren't in the source — STOP, only document what's evidenced
- Mixing optionality (`?` vs nullable) inconsistently — pick one convention per type
- Forgetting edge cases (empty arrays, error sentinels, timeout patterns)
- Documenting the "ideal" rather than the actual source behavior

---

### 5.3 UI_SPEC.md

**Purpose:** Screen-by-screen behavior, Shadcn primitive mapping, state machines.

**Canonical example:** `_project/UI_SPEC.md` in the Cyberize module.

**Required sections (in order):**

1. **Screens Overview** — table of all screens, routes, auth requirements
2. **Global Layout** — app shell, sidebar conventions, theme, responsive behavior
3. **Per-Screen Sections** (one section per screen) with:
   - Layout sketch (ASCII or text description)
   - Element-by-element specification (Shadcn primitive + content + behavior)
   - State table (initial, loading, error, success states)
   - Interactions table (trigger → effect)
   - State management notes (Zustand store shape)
   - Data sources (which service methods feed this screen)
4. **Cross-Cutting Behaviors** — auth gates, sidebar nav, error conventions, loading states, markdown rendering
5. **Component Inventory** — suggested file tree for components
6. **Out Of UI_SPEC Scope** — explicit list of things considered and excluded
7. **Reference Screenshots** — mapping screenshot files to screens
8. **Verification Checklist**
9. **Changelog**

**Length expectation:** 500-700 lines for medium projects with 3-5 screens. Scale with screen count.

**The Rule Zero discipline (from Run 001):**

- **Every screen's mobile behavior is documented** before its desktop behavior
- **Required breakpoints (375/768/1024) named per screen**
- **Touch target sizes specified** for interactive elements
- **Mobile-specific patterns identified** (slide-over sidebars, hamburger menus)

**The kit primitive discipline:**

- Every UI element maps to a specific Shadcn primitive OR a kit common primitive (Page, Row, Box, AppShellPage)
- If no primitive fits, surface as a Kit Improvement Proposal candidate
- Reference `COMPONENT_REGISTRY.md` for primitive lookup

**Common authoring mistakes:**

- Describing UI as desktop-only with "we'll do mobile later" — Lesson 5 violation
- Hand-waving state transitions ("show loading...") instead of naming exact components
- Forgetting the empty state, loading state, or error state for each screen
- Missing the markdown rendering specification when assistant responses are markdown

---

### 5.4 _project/CLAUDE.md (Project Spine)

**Purpose:** The doctrine and conventions specific to this project. Read by Claudy on every session.

**Canonical example:** `_project/CLAUDE.md` in the Cyberize module.

**Required sections (in order):**

1. **Project Identity** — name, origin, phase, goal
2. **Forbidden Zones** — repeated from APP_BRIEF for emphasis (intentional redundancy)
3. **What You ARE Building** — top-level summary of in-scope items
4. **Tech Stack** — table (matches APP_BRIEF)
5. **Project Structure (Expected)** — folder tree
6. **Source of Truth (Reading Order)** — order to read docs in
7. **Skills Loaded For This Project** — which custom + Anthropic skills activate
8. **Operating Rules (Inherited From Global)** — Plan Mode, Karpathy Protocol, eyesight-aware communication
9. **TDD Flow** — Build → Unit Test → Integrate → Block Test → System Test → Finalize
10. **Project-Specific Conventions** — naming, service layer discipline, state management
11. **Approval Gates** — phase boundary discipline
12. **Disaster Recovery** — RECOVERY.md format and update discipline
13. **Known Discrepancies** — preserve, don't fix
14. **Phase Transitions** — Phase 1 (Factory) vs Phase 2+ (operator manual work)
15. **On Completion** — what happens when Phase 1 success criteria are met

**Length expectation:** 250-350 lines.

**The critical discipline:**

- This file is INTENTIONALLY REDUNDANT with APP_BRIEF on forbidden zones. The redundancy is a feature — different docs are read in different contexts and the forbidden zones must be reinforced.
- Mobile-first / Rule Zero language should be present here, not just in UI_SPEC.
- The "Active Project Module" pointer must reference the module's location.

---

## 6. Authoring Order

Author the files in this order:

1. **APP_BRIEF.md FIRST** — scope must be locked before contracts or screens can be specified
2. **DATA_CONTRACT.md SECOND** — data shapes inform what the UI needs to display
3. **UI_SPEC.md THIRD** — screens are built from the data contract
4. **_project/CLAUDE.md LAST** — the spine is informed by the other three

If you author UI_SPEC before DATA_CONTRACT, you'll invent data shapes that don't match the source. If you author CLAUDE.md before the others, you won't know the conventions to encode.

---

## 7. Evidence Traceability

Every claim in the handoff package must be traceable to evidence:

- **For conversions:** Brain Drain extraction docs in `_extraction/` are the evidence base
- **For greenfield builds:** Operator decisions are the evidence base (capture in `_project/CLAUDE.md` Section "Operator Decisions")
- **For screenshots:** `_design/` folder is the canonical visual reference

If you can't trace a claim to evidence, surface to operator. Don't invent.

In Run 001, every type in DATA_CONTRACT traced to a specific section of `04-TOOL-SYSTEM.md` (the Brain Drain API surface doc). Every screen in UI_SPEC traced to `06-PROMPTS-AND-PERSONA.md` (the screen inventory) and the screenshots. This traceability is why the handoff package was airtight.

---

## 8. Approval Gates

The handoff package is approved when:

1. **Operator has read APP_BRIEF in full** and confirmed scope
2. **Operator has read DATA_CONTRACT in full** and confirmed shapes match expectations
3. **Operator has read UI_SPEC in full** and confirmed screen behavior matches intent
4. **Operator has read _project/CLAUDE.md** and confirmed doctrine is right
5. **Operator has explicitly approved** — "this package is ready to hand to Claudy"

Until all four files are approved, Claudy does not start Phase 0 Discovery on the build.

---

## 9. Common Authoring Mistakes

From Run 001 experience, watch for these:

### Mistake 1 — Vague Forbidden Zones

❌ "No backend stuff"
✅ "No backend code authoring. No new API routes beyond what the starter kit provides for auth callbacks. No database migrations. No schema authoring. No backend SDK calls in components."

The difference: enforceability. Claudy can verify whether it's about to violate the second; the first is interpretable.

### Mistake 2 — Inventing Mock Data Shapes

❌ Author DATA_CONTRACT with shapes that "feel right"
✅ Author DATA_CONTRACT from Brain Drain extraction evidence

In Run 001, every field in `RunAgentRequest` and `RunAgentResponse` traced to specific line numbers in the source `chat.py`. No invention.

### Mistake 3 — Skipping The Mobile Layout

❌ Document UI_SPEC as desktop-first, mention mobile in passing
✅ Document mobile sketch FIRST per screen, desktop as progressive enhancement

This is the structural lesson from Lesson 5. If the spec describes desktop, the build will be desktop.

### Mistake 4 — Underwriting CLAUDE.md

❌ Treat the project spine as a short orientation doc
✅ Treat it as the authoritative source of project doctrine, equal in weight to the other three

The spine is read every session. The other three may be read once and decay. The spine is doctrine that must hold across sessions.

### Mistake 5 — No Known Discrepancies Section

❌ Silently fix bugs/quirks in the source app during conversion
✅ Document quirks in "Known Discrepancies" section; preserve unless explicitly flagged

In Run 001, the Mission Control hardcoded 4 agents vs Chat dropdown's 5 was preserved deliberately. Documenting it prevented Claudy from "fixing" it during build.

---

## 10. The Worked Example

The canonical worked example is `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/`. Read all four files there to see what "good" looks like:

- **`APP_BRIEF.md`** — 200+ lines, 15 hard gates, success criteria table, known discrepancies preserved
- **`DATA_CONTRACT.md`** — 500+ lines, 12 types, 4 service contracts, mock data requirements, Phase 2 decision points
- **`UI_SPEC.md`** — 600+ lines, 3 screens with full per-screen specs, Shadcn primitive mapping, mobile breakpoints
- **`_project/CLAUDE.md`** — 350+ lines, forbidden zones repeated, tech stack, operating rules, approval gates

When authoring a new handoff package, use these files as direct templates. Copy the structure. Adapt the content to the new project.

---

## 11. After The Build — Lessons Promotion

After each Factory run completes, the retrospective surfaces lessons. Some lessons inform the next handoff package:

- **Doctrine gaps** → patch this playbook with the missing rule
- **Authoring mistakes** → add to Section 9 (Common Authoring Mistakes)
- **New required sections** → add to Section 5 (the four canonical files)

The playbook evolves through use. Each run leaves it sharper for the next.

---

## 12. Versioning

| Version | Date | Born From | Changes |
|---|---|---|---|
| 1.0 | 2026-05-31 | Cyberize Run 001 | Initial playbook authored from Run 001 worked example |

---

## 13. Cross-References

- **Worked example:** `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/`
- **Frontend playbook:** `FRONTEND_FIRST_PLAYBOOK.md` (mandatory gates BEFORE handoff package authoring)
- **Build phases:** `FRONTEND_BUILD_PHASE_PLAYBOOK.md` (what happens AFTER handoff package is approved)
- **Kit reference:** `agent_docs/STARTER_KIT_HANDBOOK.md` (what the starter kit provides)
- **Component reference:** `agent_docs/COMPONENT_REGISTRY.md` (which primitives map to UI elements)
- **Software Factory meta:** `SOFTWARE_FACTORY_PLAYBOOK.md` (factory-wide methodology)

---

🥄 *Part of Stark Industries — App Factory v1.1 doctrine.*
