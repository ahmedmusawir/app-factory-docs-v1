# FRONTEND_BUILD_PHASE_PLAYBOOK.md

**Version:** 1.1
**Last Updated:** June 2, 2026
**Born from:** Cyberize Run 001 lessons (Lessons 2, 4, 5, 7 + Lesson 9 — speculative authoring discovered during v1.1 retrospective)

> **Purpose**
> This document defines how the Frontend Build Phase is executed in this factory.
>
> It exists to ensure:
>
> - UI-first work is disciplined
> - demo data does not become a fake backend
> - all apps reach a usable, reviewable demo state before backend work begins

This is a global playbook.
It applies to all frontend-first builds unless an alternative strategy is explicitly chosen.

---

## 1. Position in the Factory

This playbook is used when

 Frontend-First has been selected as the execution strategy
 A Data Contract already exists for the app
 Backend implementation is intentionally deferred

This playbook does not decide whether frontend-first is used.
It defines how to execute it correctly once chosen.

Related Documents
 `FRONTEND_FIRST_PLAYBOOK.md` — Defines when and why to use frontend-first
 `{APPNAME}_DATA_CONTRACT.md` — Defines the data shape for the specific app

---

## 1.5 Pre-Phase Doctrine Refresh (MANDATORY Before Every Stage)

> **Born from Run 001 Lesson 5 (mobile-first violation) and Pattern One (doctrine load decay).**

Doctrine read in Phase 0 decays by Stage 5. To prevent this, every stage opens with a mandatory re-read of relevant doctrine sources.

### The Refresh Protocol

At the START of each stage below (before any work), re-read:

1. **Root CLAUDE.md Rule Zero** — mobile-first as foundational posture
2. **UI-UX-BUILDING-MANUAL Rule Zero** — operating standard
3. **STARTER_KIT_HANDBOOK** — section relevant to this stage's work
4. **COMPONENT_REGISTRY** — Quick Decision Tree
5. **This stage's specific anti-patterns** (listed in each stage below)

### The Acknowledgment

After the refresh, produce this acknowledgment in your stage plan:

```
### Pre-Stage Doctrine Refresh Acknowledged
- ✅ Root CLAUDE.md Rule Zero re-read
- ✅ UI-UX-BUILDING-MANUAL Rule Zero re-read
- ✅ STARTER_KIT_HANDBOOK Section <X> re-read
- ✅ COMPONENT_REGISTRY Quick Decision Tree re-read
- ✅ Stage-specific anti-patterns reviewed
- ✅ 375px sketch in plan (for UI stages)
```

If any item cannot be checked, STOP. The stage is not ready to start.

### Why This Works

Doctrine load decay is a real failure mode. In Cyberize Run 001, Phase 5 shipped a desktop-only chat screen because mobile-first doctrine had decayed from working memory. After Phase 5.4 refactor and the introduction of structural re-injection, all subsequent phases held the line. This protocol is the structural enforcement of that lesson.

---

## 1.6 Kit Audit (MANDATORY Before ANY Authoring In ANY Stage)

> **Born from Run 001 Lesson 2 (redundant authService) and Pattern Two (authoring bias).**

Before authoring ANY service, component, page, or layout in ANY stage, perform the Kit Audit. This is non-negotiable. Skipping it produces the Lesson 2 family of failures — agents authoring capabilities the kit already provides.

### The Audit (Three Questions)

1. **Does the kit already provide this?**
   Check `STARTER_KIT_HANDBOOK.md` Section "Should I Author This?". If 🛑 DO NOT BUILD, consume the kit's primitive directly.

2. **Does a kit primitive cover this UI need?**
   Check `COMPONENT_REGISTRY.md` Quick Decision Tree. If close-but-not-quite, surface a Kit Improvement Proposal — do NOT silently fork.

3. **Does the running code in the kit already implement this pattern?**
   When kit's running code conflicts with stale doctrine, the running code wins. Surface the conflict; do not silently "correct" the kit.

### Why This Audit Matters

In Run 001, the agent nearly authored `authService.ts` as a wrapper around the kit's already-complete Supabase SSR auth stack. The audit is a 30-second check that prevents this category of failure permanently.

---

## 2. Frontend Build Phase — Overview

The Frontend Build Phase is broken into six ordered stages.

Each stage has

 a clear goal
 defined outputs
 explicit stop conditions

Stages must be completed in order.

```
┌─────────────────────────────────────────────────────────────┐
│                  FRONTEND BUILD PHASE                       │
├─────────────────────────────────────────────────────────────┤
│  Stage 1 Layout & Navigation Skeleton                      │
│      ↓                                                      │
│  Stage 2 Page Fidelity Pass (Design Alignment)             │
│      ↓                                                      │
│  Stage 3 UX Polish Pass (Manual Refinement)                │
│      ↓                                                      │
│  Stage 4 Subpages & Edge Screens                           │
│      ↓                                                      │
│  Stage 5 UI-Complete Functionality (Mock-Driven)           │
│      ↓                                                      │
│  Stage 6 Demo Deployment Prep (V1)                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Stage 1 — Layout & Navigation Skeleton

### Goal

Create the structural shell of the application.

No functionality. No real data behavior.

### Activities

 Implement global layout (sidebar, header, footer)
 Set up route groups (member  admin  superadmin)
 Create main pages from design (placeholders allowed)
 Add navigation links
 Add access-denied and not-found pages
 Verify RBAC redirects work

### Rules

 No business logic
 No service calls
 No mock data beyond placeholders

### Output

 Clickable navigation
 All primary routes exist
 Pages render without errors

### Stop Condition

You can navigate the entire app without hitting missing routes.

---

## 4. Stage 2 — Page Fidelity Pass (Design Alignment)

### Goal

Make pages visually match the approved design.

### 🛑 Pre-Write Check Protocol (MANDATORY for every UI file in this stage)

> **Born from Run 001 Lesson 5 (mobile-first violation).**

Before authoring ANY UI component, page, or layout file in Stage 2, the file's opening JSDoc MUST answer these four questions:

1. **What kit primitive(s) could I use here?** (List considered + chosen)
2. **What does UI-UX-BUILDING-MANUAL say about this pattern?** (Cite section)
3. **What's the 375px sketch?** (1-3 sentences mobile layout)
4. **What changes at 768 and 1024?** (Breakpoint behaviors)

If you cannot answer all four, do not author the file. Surface to the operator.

#### Example Opening JSDoc

```typescript
/**
 * ChatMessageList — renders conversation messages with auto-scroll.
 *
 * Pre-Write Check:
 *   1. Primitives used: AppShellPage (page wrapper), Row (rows), Box (bubbles).
 *      Considered: raw flex divs — rejected, kit primitives provide responsive defaults.
 *   2. Manual reference: UI-UX-BUILDING-MANUAL Rule Zero + Layouts section.
 *   3. 375 sketch: full-width column of stacked Rows, sidebar hidden behind hamburger.
 *   4. 768: sidebar persistent (250px). 1024: max-width container (1200px) centers.
 */
```

### Stage 2 Anti-Patterns

- ❌ Authoring raw flex layouts when AppShellPage / Page / Row / Box primitives exist
- ❌ Fixed-width / persistent sidebars (`w-64`, `hidden md:block`) without responsive collapse to a slide-over **below the rail's fit breakpoint** — `lg` for wide app rails (≥ ~20rem), `md` for narrow nav. A sidebar hidden below its breakpoint with NO hamburger/trigger = the rail vanishes on mobile = automatic failure (this is **Gate M** — see FFM_PLAYBOOK §13.1 / root CLAUDE.md forbidden zone).
- ❌ `*PageContent.tsx` files placed in `src/components/` instead of co-located with `page.tsx`
- ❌ Skipping the 375px sketch in the plan
- ❌ Deferring the mobile shell to a "later/responsive cluster" — the named deferred-violation pattern; build it in the SAME phase as the shell.

### Activities

 Implement Page  Row  Box layout consistently
 Build tables, cards, forms based on design
 Ensure responsive behavior is acceptable
 Replace placeholders with real UI components
 Reference Stitch designs (or equivalent) for layout

### Rules

 Still no real functionality
 Focus is visual structure, not behavior

### Output

 Pages visually resemble final product
 Layout feels consistent across the app

### Stop Condition

Design feedback is about details, not structure.

---

## 5. Stage 3 — UX Polish Pass (Manual Refinement)

### Goal

Make the app feel professional and intentional.

This stage includes manual human judgment. AI output is corrected and refined.

### Activities

 Fix spacing inconsistencies
 Improve typography hierarchy
 Normalize button styles and variants
 Add loading states
 Add empty states
 Add error states
 Add confirmation dialogs and toasts
 Improve form validation messaging
 Fix breadcrumbs (if applicable)
 Update documentation if Cascade deviated from standards

### Rules

 This is a human-driven stage
 Do not skip — AI misses polish details

### Output

 App feels usable even without real data
 No obvious rough edges in common flows

### Stop Condition

A user can navigate without confusion or friction.

---

## 6. Stage 4 — Subpages & Edge Screens

### Goal

Eliminate unfinished app gaps.

### Activities

 Detail pages (view single item)
 Edit pages (edit single item)
 Create pages (new item forms)
 Settings pages
 Profile pages
 Error screens (404, 500, access denied)
 Empty state screens
 Breadcrumb implementation (decision must be recorded)

### Rules

 No new primary features introduced here
 This stage completes navigation coverage

### Output

 All navigation paths terminate cleanly
 No dead buttons or placeholder routes

### Stop Condition

Every link leads to a real screen.

---

## 7. Stage 5 — UI-Complete Functionality (Mock-Driven)

### Goal

Validate user flows, not backend realism.

This stage makes the app feel usable using demo data.

---

### Allowed Functionality (UI Phase)

 Feature  Notes 
----------------
 Create items  In-memory only, lost on refresh 
 Edit items  In-memory only 
 Delete items  In-memory only 
 Change statusseverity  In-memory only 
 Filters  Client-side filtering of mock data 
 Search  Client-side search of mock data 
 Sorting  Client-side sorting 
 Pagination  Client-side (service returns paginated results) 
 Role-based UI gating  Hideshow actions based on role 
 Form validation  Client-side validation 
 Successerror toasts  Feedback for user actions 

---

### Explicitly Forbidden (Backend Phase Only)

 Feature  Why 
--------------
 localStorage persistence  Adds complexity, no real value for demo 
 Real concurrency simulation  Backend concern 
 Audithistory systems  Backend concern 
 File uploads to storage  Backend concern (show UI only) 
 Background jobs  Backend concern 
 WebSockets  real-time sync  Backend concern 
 Multi-user permission enforcement  RLS concern 
 DB-level pagination logic  Backend concern 
 Data integrity enforcement  Backend concern 
 Fake auth or fake permissions  Use real auth with mock data 

---

### Mock Discipline Rules (Non-Negotiable)

 UI never talks directly to mock data files
 All data access goes through the service layer
 Mock data must follow the Data Contract exactly
 Mock behavior must be deterministic (same input = same output)
 No fake auth or fake permissions systems — use real auth
 If mocking becomes complex → simplify or stop

---

### The Golden Rule

 Demo data exists to prove the UI works. It should be simple enough to delete entirely when backend is ready.

 If you find yourself debugging mock data logic or building complex state management for mocks — STOP. You've gone too far. Simplify.

---

### Output

 End-to-end flows work with demo data
 Stakeholders can use the app
 UI reveals missing requirements clearly

### Stop Condition

When further realism would require backend logic.

---

## 8. Stage 6 — Demo Deployment Prep (V1)

### Goal

Produce a stable, reviewable demo environment.

### Activities

 Seed demo data (representative, not exhaustive)
 Verify RBAC behavior (app-layer redirects)
 Test all user flows end-to-end
 Fix broken flows
 Remove debug UI and console logs
 Document known limitations (e.g., data resets on refresh, RLS not implemented yet)
 Deploy to staging (Vercel or equivalent)

### Rules

 This is not production
 Stability matters more than completeness
 Communicate limitations clearly to stakeholders

### Output

 Deployed demo app at staging URL
 Stakeholders can review and give feedback
 UI requirements are effectively frozen

### Stop Condition

Feedback shifts from UX changes to datasecurity concerns.

---

## 9. UI Phase Completion Checklist

Before declaring Frontend Build Phase complete

### Navigation & Structure
- [ ] All routes exist and render
- [ ] No dead links or placeholder buttons
- [ ] Breadcrumb decision recorded (implemented or intentionally skipped)

### States & Feedback
- [ ] Loading states implemented
- [ ] Empty states implemented
- [ ] Error states implemented
- [ ] Toast notifications working
- [ ] Form validation messages showing

### Access Control
- [ ] Role-based access verified visually
- [ ] Admin sees admin pages only
- [ ] Member sees member pages only
- [ ] Unauthorized access redirects correctly

### Functionality
- [ ] Core flows work end-to-end with demo data
- [ ] Pagination UI exists where lists are large
- [ ] Filters work (if applicable)
- [ ] Search works (if applicable)

### Responsive (Gate M) — collapse AND desktop frame
- [ ] Mobile collapse verified at 375: grids → 1-col, rows → stacked cards, tables → stacked, forms → full-width
- [ ] Desktop content frame matches the designer's container CSS: content gutter present (not flush to the sidebar) AND form screens use the mockup's max-width, **centered** — sourced from the mockup CSS (e.g. `.main` padding, `.formcard` max-width), NOT eyeballed
- [ ] Both confirmed, both themes, every screen (collapse ≠ frame — they are different failure classes; see Lesson 10)

### Documentation
- [ ] Known backend dependencies documented
- [ ] Known limitations documented
- [ ] Data Contract still accurate (update if UI revealed new needs)

If any item is unchecked, the phase is not complete.

---

## 10. Things That Should Just Work

These components should be built into every app by default. If Cascade misses any, flag it in Stage 3 (Polish).

 Component  Purpose 
--------------------
 Pagination component  Reusable across all tables 
 Breadcrumbs  Auto-generated from route (if decided yes) 
 Loading spinner  Global and inline variants 
 Empty state component  Reusable No data message 
 Error boundary  Catches React errors gracefully 
 Toast notifications  Successerror feedback 
 Mobile responsive nav  Sidebar collapses on mobile 
 Dark mode toggle  Respects system preference 
 Confirmation dialog  Are you sure for destructive actions 

---

## 11. Transition to Backend Phase

The Frontend Build Phase ends when

 UI flows are validated
 Data requirements are clear
 Demo feedback is incorporated
 Backend work is unblocked and justified

Backend implementation should begin only after this point.

The next phase will
 Create Supabase tables from Data Contract
 Implement RLS policies
 Swap mock services for real services
 Enable file uploads via Supabase Storage
 Deploy to production

---

## 12. Stage Completion Reports — Kit Improvement Proposals

> **Born from Run 001 — the AppShellPage primitive was born from accidentally surfacing a kit gap. Make it deliberate.**

At every stage completion (Stages 1 through 6), the AI agent has the OPTION to surface Kit Improvement Proposals. Format:

```
### Kit Improvement Proposals (OPTIONAL)

- **What I noticed:** [observation made during this stage]
- **What the kit currently does:** [current state / limitation]
- **Proposed improvement:** [what could be better]
- **Recommended action:** [Implement now / Defer / Archive for consideration]
```

The operator decides whether to accept. Accepted proposals become kit-level work separate from the current project. Rejected proposals go to `KIT_PROPOSALS_ARCHIVE.md` for future consideration.

If no proposals this stage, write "None this stage."

### Why This Matters

This is the Factory's self-improvement loop made explicit. The `AppShellPage` primitive came from Phase 5.4 in Run 001 — what started as a mobile-first fix became a permanent kit primitive. Every future Factory run benefits from primitives discovered this way. Don't lose those discoveries to "I'll mention it later" forgetfulness.

---

## 13. Appendix — Run 001 Lessons That Updated This Playbook

This playbook was updated in v1.1 based on lessons learned during Cyberize Agentic Automation Run 001 (May 2026).

### Lesson 2 — Almost-Authored Redundant authService

Pattern: Authoring bias produces redundant work on capabilities the kit already provides.
Fix in this playbook: Section 1.6 (Kit Audit) mandates checking STARTER_KIT_HANDBOOK before any authoring in any stage.

### Lesson 4 / 7 — Component Blindness

Pattern: Agent ignored kit primitives, authored raw flex layouts.
Fix in this playbook: Stage 2 Pre-Write Check Protocol forces primitive consideration before authoring. Stage 2 anti-patterns list raw flex as forbidden.

### Lesson 5 — The Phase 5 Mobile-First Violation

Pattern: Doctrine read in Phase 0 decays by Stage 5.
Fix in this playbook: Section 1.5 (Pre-Phase Doctrine Refresh) mandates re-read at the start of every stage. Stage 2 Pre-Write Check Protocol forces 375px sketch before authoring.

### Lesson 7 — Page Composition Pattern

Pattern: `*PageContent.tsx` placed in wrong location.
Fix in this playbook: Stage 2 anti-patterns explicitly forbid this placement.

### Lesson 9 (New) — Speculative Authoring (Discovered During v1.1 Retrospective)

Pattern: AI agent (Claude itself) wrote a v1.1 patch for this very file without having seen its contents — improvised when merge couldn't find the original.
Fix in this playbook (and broader factory doctrine): When authoring patches or merges, if a referenced file isn't available, STOP and request it. Never write speculatively. Karpathy Rule K7 — surface conflicts, don't blend them.

This lesson is a real-time addition to the retrospective discovered while authoring v1.1. It applies to AI agents doing patch/merge work in any Factory phase.

### Lesson 10 (New, Cyber Pharma v1 Phase 2.2 — Admin Portal Run 001) — Mobile Gate Checked Collapse, Not the Desktop Frame

Pattern: "Responsive" was treated as done once the layout collapsed at 375 (grid→1-col, rows→stacked, table→cards). The *desktop content frame* went unchecked — the content column shipped with no gutter (flush to the sidebar) and form screens were left-aligned in a wide void instead of centered. This is a different failure class than collapse; it fell through the mobile gate and cost an unplanned two-round eyes-on fix.

Fix in this playbook: Section 9 (UI Phase Completion Checklist) now carries a "Responsive (Gate M) — collapse AND desktop frame" block asserting BOTH (a) collapse and (b) the desktop content frame matches the designer's container CSS (content gutter present; form screens at the mockup's max-width, centered). Source both checks from the mockup CSS (e.g. `.main` padding, `.formcard` max-width), not from eyeballing.

---

## 14. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.2 | 2026-06-25 | Added Lesson 10 (the mobile gate must check the desktop content frame — gutter + centered form max-width — not just 375 collapse) + the Section 9 "Responsive (Gate M)" checklist block. Born from Cyber Pharma v1 Phase 2.2 Admin Portal retrospective. |
| 1.1 | 2026-06-02 | Added Section 1.5 (Pre-Phase Doctrine Refresh), Section 1.6 (Kit Audit), Stage 2 Pre-Write Check Protocol + anti-patterns, Section 12 (Kit Improvement Proposals), Section 13 (Run 001 Lessons appendix including new Lesson 9). Born from Cyberize Run 001 retrospective. |
| 1.0 | 2026-01-02 | Initial playbook |

---

### END OF DOCUMENT

🥄 *Part of Stark Industries — App Factory v1.1 doctrine.*