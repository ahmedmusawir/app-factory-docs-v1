# SOFTWARE FACTORY PLAYBOOK

> **Version:** 1.4 · **Date:** 2026-10-18 · **Status:** Active
> **Tier:** 1 — Constitution · **Pairs with:** APP_FACTORY_BLUEPRINT, DESIGNER_PLAYBOOK, TESTING_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK

> **Stark Industries Software Factory**
> *The master guide to building production-ready applications with AI assistance.*
> **Born from:** Cyberize Run 001 — operator's strategic insight on instruction-plus-example pairing

---

## Table of Contents

1. [Philosophy and Factory Seats](#1-philosophy-and-factory-seats)
2. [The Build Phases](#2-the-build-phases)
3. [Phase 1: Planning & User Stories](#3-phase-1-planning--user-stories)
4. [Phase 2: Design System](#4-phase-2-design-system)
5. [Phase 3: Database Schema](#5-phase-3-database-schema)
6. [Phase 4: API & Services](#6-phase-4-api--services)
7. [Phase 5: State Management](#7-phase-5-state-management)
8. [Phase 6: UI Implementation](#8-phase-6-ui-implementation)
9. [Phase 7: Authentication & RBAC](#9-phase-7-authentication--rbac)
10. [Phase 8: Integration & Testing](#10-phase-8-integration--testing)
11. [Phase 9: Deployment](#11-phase-9-deployment)
12. [Feature Spec Template](#12-feature-spec-template)
13. [Checklists](#13-checklists)
14. [Manual Reference Guide](#14-manual-reference-guide)

---

## 1. Philosophy and Factory Seats

Resolve authority by the question being answered: disk and recon establish what exists; approved artifacts establish what is authorized; the named domain owner defines the reusable pattern. A conflict between these is not permission to substitute one for another. Stop the affected work, record both sources and their revisions, and obtain the Director’s attributable ruling. Preserve stage-specific authority within its stated scope.

### Shared terminology

A seat defines responsibility; a persona or model name does not grant permission. Director is the human scope, access and release authority; Operator and Coordinator are contextual names for that human responsibility. Architect owns assembly and scope interpretation; Engineer owns implementation and factual handoff; QA Lead owns QA doctrine, plan approval, adjudication and certification; QA Executor independently plans and tests. Designer and deployment responsibilities remain distinct. “Architect” does not name the human approver in an authority rule.

Keep lifecycle axes separate: Blueprint phases describe the Factory pipeline; SFP implementation phases describe build disciplines; FFM sub-phases and Frontend Build Phase stages describe execution within a module; roadmap phases describe product scope. Record each stage’s parent, entry artifacts, exit evidence and approver in the module contract. Demo deployment is not Gate Q or Gate D. Engine 1 is module engineering and module QA. Engine 2 is independent system review after all Engine 1 phases and their QA are closed. The separate post-FFM review occurs after FFM and its QA. Only dispositioned findings requiring repair produce RRM work.

Schema-first, approved specifications, incremental verification and recorded changes remain required.

---

Revised workflow documents and stick diagrams: [FFM creation](../03_BUILD_METHODOLOGY/_workflows/FFM_CREATION.md), [FFM execution and post-FFM review](../03_BUILD_METHODOLOGY/_workflows/FFM_EXECUTION.md), [deployment](../03_BUILD_METHODOLOGY/_workflows/FFM_DEPLOYMENT.md), [BIM and Engine 2](../03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md). They supersede the historical August pictures when verified and published; originals are retained.

## 1.5 Doctrine Pairing Principle — Playbooks Paired With Worked Examples

> **Born from Cyberize Run 001 (May 2026).**
> Pair each methodology with an available, verified worked example. Historical external pointers below are not proof that an example is present in this Hub or in a project. Record repository, immutable revision and path before requiring it.

### The Principle

Abstract rules alone produce drift. Concrete examples alone produce cargo culting. The combination — instruction set + worked example — produces durable, transferable competence.

This is true for human architects authoring docs and reading playbooks. It is even more true for AI agents executing those playbooks. Every Factory playbook that aims to guide authoring or building should be paired with a real, complete, evidence-traceable example.

### The Pattern

| Playbook (Instruction) | Paired Example (Concrete) |
|---|---|
| `HANDOFF_PACKAGE_PLAYBOOK.md` | Historical external example (availability unverified): `agent_docs/CURRENT_APP/app-factory-frontend-first-module/_project/`. Obtain the source repository, immutable revision and path before use; do not assume this path exists locally. |
| `FRONTEND_FIRST_PLAYBOOK.md` | Cyberize Agentic Automation build (Run 001) |
| `UI-UX-BUILDING-MANUAL.md` | Cyberize screenshots in `_design/` + built screens |
| `AUTH_MANUAL.md` | Starter kit's working auth implementation |
| `APP_ARCHITECTURE_MANUAL.md` | Starter kit's actual folder structure + Run 001 module |
| `SOFTWARE_FACTORY_PLAYBOOK.md` | The Cyberize Run 001 retrospective + all surviving doctrine |

### Discipline When Authoring New Playbooks

When a new playbook is authored, it must include:

1. **Cross-reference to its paired example** — where in the repo to find the real instance
2. **"Common Authoring Mistakes" section** — evidence-based, drawn from runs where mistakes happened
3. **Versioning that traces back to runs** — "v1.0 born from Run 001" makes the lineage explicit

### Discipline When Authoring New Examples

When a new project enters the Factory:

1. **Treat the project's handoff files as a candidate worked example** — they may become the canonical reference for future runs
2. **Don't sanitize for production** — keep the operator's actual decision-history visible (e.g., "Known Discrepancies" sections that preserve quirks)
3. **Reference the playbook that governs the example** — bi-directional cross-references

### Why This Matters Strategically

Three reasons:

**One — AI performance is structurally better with examples.** This is the technical reality. Skipping examples produces worse builds regardless of how well-written the abstract playbook is.

**Two — Tacit knowledge is capturable.** Without paired examples, the "why" of factory decisions stays in the architect's head. With paired examples, the "why" is visible in the artifacts themselves.

**Three — Future architects (human or AI) can learn from precedent.** When the next project begins, the architect doesn't have to re-derive the handoff package structure. They look at the canonical example, see what worked, adapt.

### The Lifecycle Of A Worked Example

Examples are not frozen. They evolve as lessons accumulate:

1. **Born during a run** — the run's actual artifacts (handoff package, build artifacts, retrospective)
2. **Refined post-run** — lessons learned during the run get baked back into the example (with version notes)
3. **Promoted to canonical reference** — when proven across multiple runs, marked as the reference example for its category
4. **Archived but preserved** — when superseded, archived rather than deleted (preserves doctrine history)

### When To Update Examples

After each Factory run completes:

1. **Surface lessons in the retrospective**
2. **For lessons that affect the playbook → patch the playbook**
3. **For lessons that affect the example → patch the example with a clear note ("v1.1 — added Lesson X mitigation")**
4. **For lessons that affect both → patch both with cross-references**

This keeps playbook and example in sync. They evolve together. The pairing stays valid.

### Cross-Reference

- **`HANDOFF_PACKAGE_PLAYBOOK.md`** — first explicit application of this principle (instructions + Cyberize handoff as example)
- Historical external example (availability unverified): **`CURRENT_APP/app-factory-frontend-first-module/_project/`** — the inaugural historical worked example Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.

---

## 2. The Build Phases

Engine 1 denotes module engineering and module QA across the implementation phases. Review occurs after FFM completion and its QA, and again at Engine 2 after all Engine 1 phase/module engineering and QA are closed. Findings require disposition; only approved findings needing repair produce bounded RRM work, and each RRM includes QAM. A clean review produces no RRM. Module QA certification, broader review completion and deployed-system Gate D remain distinct.

Every feature follows this sequence:

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        BUILD PHASE SEQUENCE                                 │
└────────────────────────────────────────────────────────────────────────────┘

  PHASE 1          PHASE 2          PHASE 3          PHASE 4
  ────────         ────────         ────────         ────────
  Planning    ──►  Design      ──►  Database    ──►  API
  & Stories        System           Schema           Services

       │                                                  │
       │                                                  │
       ▼                                                  ▼

  PHASE 5          PHASE 6          PHASE 7          PHASE 8
  ────────         ────────         ────────         ────────
  State       ──►  UI          ──►  Auth &      ──►  Integration
  Management       Implementation   RBAC             & Testing

                                                          │
                                                          │
                                                          ▼

                                                     PHASE 9
                                                     ────────
                                                     Deployment
```

### Why This Order?

| Phase | Why It Comes Before the Next |
|-------|------------------------------|
| Planning | Can't design without knowing what to build |
| Design | Consume the Architect’s approved DATA_CONTRACT; proposed contract refinements require approved amendments before implementation. |
| Database | Can't build APIs without knowing the data shape |
| API | Can't manage state without knowing what data exists |
| State | Can't build UI without knowing where data comes from |
| UI | Can't add auth without having something to protect |
| Auth | Can't test without all pieces in place |
| Testing | Can't deploy untested code |

### Phase Vocabulary — One Canonical Map

The factory uses one canonical project-phase map: the **APP_FACTORY_BLUEPRINT lifecycle** (Phase 0 — Recon → Phase 5 — Deployment). This playbook's 9 phases are the **execution breakdown** within that lifecycle — they do not compete with it. FFM "Sub-Phases" nest inside individual build phases. Nothing is renumbered by this note.

| This Playbook (execution breakdown) | Blueprint Lifecycle (canonical) |
|---|---|
| Phase 1 — Planning & User Stories | Phase 1 — Ignition |
| Phase 2 — Design System | Phase 2 — Design |
| Phase 3 — Database Schema | Phase 3 — Engineering (spec) → Phase 4 — Fabrication (build) |
| Phases 4–8 — API / State / UI / Auth / Testing | Phase 4 — Fabrication |
| Phase 9 — Deployment | Phase 5 — Deployment |
| Engine 1 | Module engineering and independent module QA, including required certification/cleanup/closeout; complete every scoped phase/module and its QA before Engine 2. |
| Post-FFM review (checkpoint 1) | Independent review after FFM build and its independent QA finish; findings require disposition. |
| Engine 2 (checkpoint 2) | Independent system review after all Engine 1 phases/modules and their QA are closed. |
| RRM | Repair work only for approved review findings requiring repair; a clean review requires no RRM. Review does not replace Gate Q, Gate D or Director release. |

> **Phase 0 — Recon precedes everything:** no Phase 1 planning until the target repo is ground-truthed per `RECON_QUESTIONNAIRE.md` and the Recon Report is consumed (see APP_FACTORY_BLUEPRINT, Phase 0).

---

## 2.5 Module Identity & QA Handoff  *(Factory-wide — governs BIM, FIX, FEAT, and all future module types)*

### Module Identity

**Canonical ID format: `<TYPE>-<NNN>-<APP-SLUG>`** — e.g., `BIM-006-ADK-HARNESS`, `FIX-004-CYBER-PHARMA`, `FEAT-002-ADK-HARNESS`.

1. The slug comes from the application's canonical identity in its project brief / APP_BRIEF. *(A central `APP_REGISTRY.md` is a proposed future addition, pending separate Operator approval; until it exists, no document may cite it as a source of truth.)*
2. The ID appears on: the module folder name, every document header inside it, the `ACCEPTANCE_SPEC.md`, QA references, retrospectives, changelog entries, and cross-document links.
3. Casing: canonical ID UPPERCASE in documents and folder names; git branches lowercase-kebab; commit tags carry the canonical ID.
4. Rationale (stated, not assumed): module artifacts escape their folders — into QA reports, branches, search results, and handoffs. A naked `FIX-002` becomes ambiguous the day a second application mints one. Provenance travels with the artifact.
5. Legacy: modules created before this doctrine keep their unsuffixed names as LEGACY IDs — no retroactive mass-renaming. New citations append the app parenthetically: "FIX-002 (ADK-HARNESS, legacy)."

### QA Handoff — the `ACCEPTANCE_SPEC.md` Contract

1. **Every code-bearing module handoff includes `ACCEPTANCE_SPEC.md`** (exact filename locked). It is the contract from Engineering to QA — **never the QA test plan.** Engineering states the claim; QA independently designs the attack.
2. **Ownership:** acceptance criteria are **seeded from the approved module contract — Architect/Operator-defined — before implementation.** The Engineer maintains the spec in sync with approved scope and finalizes it at handoff, but may not silently add, remove, weaken, or redefine a requirement; scope changes require approval.
3. **Numbering:** acceptance requirements use **`AC1, AC2, …`** — a Factory decision effective 2026-08-10. Module-internal engineering gates keep their own ID families (`X*`, `V*`, `N*`, `P-G*` …); a gates↔AC mapping table in the spec is encouraged. Bare `A*` is reserved for recon assumption checklists. Legacy specs using gate IDs stand as legacy.
4. **Minimum contents:** canonical module ID + owning app · objective · in-scope / explicit out-of-scope · numbered ACs, testable and observable · expected behavior per AC incl. error surfaces · **environment/setup prerequisites and every manual Operator step, called out FIRST** · regression expectations · manual-only points · known limitations · follow-up work outside this contract.
5. **Authority chain:** QA owns the verdict — Factory vocabulary exactly: **PASS / PASS WITH FOLLOW-UP FINDINGS / PASS WITH KNOWN RISK / FAIL / BLOCKED.** The **Operator holds final adjudication and release authority.** The Architect advises on architectural classification and routing. An in-scope acceptance failure needs no one's permission to be a FAIL. Accepted findings reach Engineering only as approved module content.
6. **Gate Q is mandatory for all code-bearing modules.** Only documentation-only / non-runtime changes may receive a recorded Operator QA waiver.

Every newly authored module includes a complete, module-specific `QAM/` prepared by the Architect from `03_BUILD_METHODOLOGY/_templates/QAM/`. QA Lead owns the reusable playbook and standing requirements. Engineer fills factual engineering records and handoff; QA Executor performs independent Q1 recon and test planning; QA Lead approves the plan; Director releases execution; QA Executor performs Q2 and authorized retest; QA Lead adjudicates and certifies. `QAM_PLAYBOOK.md` owns this packaging and sequence. Existing modules already in flight retain their recorded sequence until an attributable amendment.

The Director commits and pushes the completed engineering candidate on the numbered product branch, then creates `qa/<module-branch>` at that exact commit. Engineer performs approved repairs and QA Executor independently tests on that same QA branch, with separate writable lanes and one active writer during repair or measurement. The QA branch continues to final integration; do not transfer work back or abandon it as the normal workflow. After the QA Lead’s verdict and required cleanup, the Architect issues closeout instructions, Engineer performs bounded closeout, and the Director performs final commits, merge and push. Preserve product, execution, evidence and closeout identities separately.

---

## 3. Phase 1: Planning & User Stories

### Objective

Transform a feature idea into actionable user stories with clear acceptance criteria.

### AI Tools for Planning

| Tool | Best For | Notes |
|------|----------|-------|
| **Gemini Pro** | Initial brainstorming | Good at exploring possibilities |
| **Claude Sonnet/Opus** | Refining specs | Better at precise requirements |
| **ChatGPT** | User story generation | Good conversational refinement |

### User Story Format

```markdown
## User Story: [Short Title]

**As a** [user role]
**I want to** [action/goal]
**So that** [benefit/reason]

### Acceptance Criteria

- [ ] Given [precondition], when [action], then [result]
- [ ] Given [precondition], when [action], then [result]
- [ ] Given [precondition], when [action], then [result]

### Out of Scope

- [What this story does NOT include]

### Dependencies

- [Other stories or systems this depends on]

### Technical Notes

- [Any known technical considerations]
```

### Example User Story

```markdown
## User Story: Admin Views Order List

**As an** Admin user
**I want to** see a paginated list of all orders
**So that** I can manage and track customer purchases

### Acceptance Criteria

- [ ] Given I am logged in as Admin, when I navigate to /orders, then I see a table of orders
- [ ] Given the orders table is displayed, when I scroll, then more orders load (pagination)
- [ ] Given an order in the table, when I click it, then I navigate to the order detail page
- [ ] Given the orders table, when I type in search, then orders filter by email or order ID

### Out of Scope

- Editing orders (separate story)
- Bulk actions (separate story)

### Dependencies

- Auth system must be in place
- Orders table must exist in database

### Technical Notes

- Use offset pagination for simplicity
- Cache order list in Zustand for client-side filtering
```

### Deliverables

- [ ] All user stories written
- [ ] Acceptance criteria defined
- [ ] Dependencies identified
- [ ] Stories prioritized (P0, P1, P2)

---

## 4. Phase 2: Design System

### Objective

Lock the design system and screen set that define the visual implementation.

### Design Execution Is Owned By The Designer

**Design execution is owned by `DESIGNER_PLAYBOOK.md`** — the token file (`globals.css`/`.scss`, all modes) is the PRIMARY deliverable, and screens are built as token-driven HTML rendered to PNG with Playwright via the **Canonical Page Method** (lock one canonical screen, clone-and-adapt the rest). This playbook does not define a competing design process.

In summary, Phase 2 runs:

1. Designer receives the approved stories/brief + Tailwind version + token well
2. Designer locks the token file (all modes) — operator gate
3. Designer builds the canonical screen: token-driven HTML → Playwright PNG (light + dark) — operator gate
4. Designer clones-and-adapts the remaining screens; ships style tile + per-screen HTML/PNG + `UI_SPEC.md` + component manifest

### Deliverables

- [ ] Token file locked (primary deliverable)
- [ ] Canonical screen approved; full screen set shipped (HTML + PNG)
- [ ] UI_SPEC.md + component manifest delivered
- [ ] Responsive breakpoint decisions

**Reference:** `DESIGNER_PLAYBOOK.md`

---

## 5. Phase 3: Database Schema

### Objective

Design and implement the database schema before any application code.

### Schema Design Process

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  User Stories   │ ──► │  Identify       │ ──► │  Design Tables  │
│  + Designs      │     │  Entities       │     │  + Columns      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Run SQL in     │ ◄── │  Add Indexes    │ ◄── │  Define         │
│  Supabase       │     │  + RLS          │     │  Relationships  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │  Generate TS    │
                                               │  Types          │
                                               └─────────────────┘
```

### Schema Spec Template

```markdown
## Table: [table_name]

### Purpose
[What this table stores]

### Columns

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| id | UUID | NO | gen_random_uuid() | Primary key |
| ... | ... | ... | ... | ... |

### Relationships

- [FK to other_table on column_name]

### Indexes

- idx_{table}_{column} on {column}

### RLS Policies

- [Policy name]: [Description]

### SQL

```sql
CREATE TABLE {table_name} (
  ...
);
```
```

### Deliverables

- [ ] Entity relationship diagram
- [ ] SQL for all tables
- [ ] Indexes defined
- [ ] RLS policies written
- [ ] TypeScript types generated
- [ ] Tables created in Supabase

**Reference:** `DATABASE_MANUAL.md`

---

## 6. Phase 4: API & Services

### Objective

Build the service layer and API routes that interact with the database and external systems.

### Service Layer Structure

```
src/
├── services/
│   ├── orderServices.ts      # Order CRUD operations
│   ├── ticketServices.ts     # Ticket operations
│   ├── userServices.ts       # User operations
│   └── crmServices.ts        # External CRM integration
└── app/
    └── api/
        ├── orders/
        │   ├── route.ts          # GET /api/orders
        │   └── [id]/route.ts     # GET /api/orders/:id
        ├── webhooks/
        │   └── crm/route.ts      # POST /api/webhooks/crm
        └── sync/
            └── route.ts          # GET /api/sync
```

### Service Function Template

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### Deliverables

- [ ] Service functions for all entities
- [ ] API routes for client-side access
- [ ] Webhook endpoints if needed
- [ ] External API integrations
- [ ] Error handling in place

**Reference:** `API_AND_SERVICES_MANUAL.md`

---

## 7. Phase 5: State Management

### Objective

Create Zustand stores that manage client-side state and connect to the service layer.

### Store Structure

```
src/
└── store/
    ├── useAuthStore.ts       # Authentication state
    ├── useOrderStore.ts      # Orders state
    ├── useTicketStore.ts     # Tickets state
    └── useSyncStore.ts       # Sync progress state
```

### Store Template

```typescript
// src/store/use{Entity}Store.ts

import { create } from 'zustand';
import type { Entity } from '@/types/database';

interface EntityState {
  // Data
  entities: Entity[];
  selectedEntity: Entity | null;
  
  // Loading states
  isLoading: boolean;
  error: string | null;
  
  // Actions
  fetchEntities: () => Promise<void>;
  selectEntity: (id: string) => void;
  clearSelection: () => void;
}

export const useEntityStore = create<EntityState>((set, get) => ({
  // Initial state
  entities: [],
  selectedEntity: null,
  isLoading: false,
  error: null,

  // Actions
  fetchEntities: async () => {
    set({ isLoading: true, error: null });
    
    try {
      const response = await fetch('/api/entities');
      const { data } = await response.json();
      set({ entities: data, isLoading: false });
    } catch (error) {
      set({ error: 'Failed to fetch entities', isLoading: false });
    }
  },

  selectEntity: (id: string) => {
    const entity = get().entities.find((e) => e.id === id);
    set({ selectedEntity: entity || null });
  },

  clearSelection: () => {
    set({ selectedEntity: null });
  },
}));
```

### Selector Pattern (Prevent Re-renders)

```typescript
// In components, use selectors:
const entities = useEntityStore((state) => state.entities);
const isLoading = useEntityStore((state) => state.isLoading);

// NOT:
const { entities, isLoading } = useEntityStore(); // ❌ Causes re-renders
```

### Deliverables

- [ ] Stores for all major data domains
- [ ] Loading and error states
- [ ] Selectors defined for components
- [ ] Persistence configured if needed

**Reference:** `STATE_MANAGEMENT_MANUAL.md`

---

## 8. Phase 6: UI Implementation

### Objective

Build React components that consume stores and render the designs.

### Component Structure

```
src/
├── app/
│   └── (admin)/
│       ├── layout.tsx
│       ├── orders/
│       │   ├── page.tsx              # Orders list page
│       │   └── [orderId]/page.tsx    # Single order page
│       └── events/
│           └── page.tsx              # Events list page
└── components/
    ├── ui/                           # shadcn primitives
    ├── common/                       # Shared components
    │   ├── Spinner.tsx
    │   └── BackButton.tsx
    └── admin/                        # Admin-specific
        ├── orders/
        │   ├── OrderTable.tsx
        │   └── OrderCard.tsx
        └── events/
            └── EventCard.tsx
```

### Page Component Pattern

```typescript
// src/app/(admin)/orders/page.tsx
'use client';

import { useEffect } from 'react';
import { useOrderStore } from '@/store/useOrderStore';
import { OrderTable } from '@/components/admin/orders/OrderTable';
import Spinner from '@/components/common/Spinner';

export default function OrdersPage() {
  const orders = useOrderStore((state) => state.orders);
  const isLoading = useOrderStore((state) => state.isLoading);
  const fetchOrders = useOrderStore((state) => state.fetchOrders);

  useEffect(() => {
    fetchOrders();
  }, [fetchOrders]);

  if (isLoading) {
    return (
      <div className="flex justify-center py-12">
        <Spinner />
      </div>
    );
  }

  return (
    <div className="p-2 sm:p-10">
      <div className="border-b-4 border-red-500 mb-8">
        <h1 className="text-2xl sm:text-4xl font-extrabold text-center py-4">
          Orders List
        </h1>
      </div>

      <OrderTable orders={orders} />
    </div>
  );
}
```

### Deliverables

- [ ] All pages implemented
- [ ] Components match designs
- [ ] Responsive design verified
- [ ] Loading/empty/error states
- [ ] Accessibility basics (labels, focus)

**Reference:** `UI-UX-BUILDING-MANUAL.md`

---

## 9. Phase 7: Authentication & RBAC

For kit-based builds, consume the existing kit authentication and authorization primitives and verify them through AUTH-WALK. Do not rebuild login pages, an auth store, metadata role flags or a client route guard. Page wrappers follow STARTER_KIT_HANDBOOK §5 and §7: resolve authorized server data before rendering the interactive client child. Generic non-kit examples do not apply when the kit supplies the capability.

The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization.

Every privileged operation authorizes its own invocation before acquiring or using elevated capability: authenticate the requester, resolve the current trusted role, authorize the operation and target, and validate input. Layout admission controls page access only. Direct unauthenticated, wrong-role and wrong-target invocations must produce no privileged side effect.

Verify authentication state, table-backed current role, object-level authorization, denied targets, session expiry, logout and first server render. The former metadata-role/auth-store checklist is withdrawn. Kit-dependent signatures require the pinned kit evidence; this containment does not close those replacements.

---

## 10. Phase 8: Integration & Testing

### Objective

Verify all components work together and meet acceptance criteria.

### Testing Checklist

#### Functional Testing

- [ ] All user stories verified against acceptance criteria
- [ ] Happy path flows work end-to-end
- [ ] Error states display correctly
- [ ] Edge cases handled (empty data, long text, etc.)

#### Auth Testing

- [ ] Login with valid credentials
- [ ] Login with invalid credentials
- [ ] Protected routes redirect unauthorized users
- [ ] Logout clears session completely
- [ ] Role-specific features visible only to correct roles

#### Data Testing

- [ ] CRUD operations work correctly
- [ ] Data persists after refresh
- [ ] Sync with external systems works
- [ ] Data validation prevents bad input

#### UI Testing

- [ ] Responsive design at all breakpoints
- [ ] Loading states display correctly
- [ ] Error states display correctly
- [ ] Empty states display correctly

#### Performance Testing

- [ ] Pages load in < 3 seconds
- [ ] No unnecessary re-renders
- [ ] Large data sets paginate correctly

### Deliverables

- [ ] All acceptance criteria verified
- [ ] Bug fixes applied
- [ ] Performance acceptable

**Reference:** `TESTING_PLAYBOOK.md` — the factory's testing bible: test doctrine, pytest/Jest patterns, verification gates. This phase executes what that playbook defines.

---

## 11. Phase 9: Deployment

### Objective

Deploy the application to production.

### Pre-Deployment Checklist

- [ ] Environment variables set in production
- [ ] Database migrations applied
- [ ] RLS policies enabled
- [ ] API keys secured (not in client code)
- [ ] Error logging configured
- [ ] Analytics configured (if needed)

### Deployment Steps

```bash
# 1. Build the application
npm run build

# 2. Test production build locally
npm run start

# 3. Deploy to Vercel/Netlify
# (Automatic via Git push or manual deploy)

# 4. Verify production
# - Check all pages load
# - Test login flow
# - Verify data displays
```

### Post-Deployment Checklist

- [ ] All pages accessible
- [ ] Auth works in production
- [ ] Database connections stable
- [ ] External integrations working
- [ ] Error monitoring active

---

## 12. Feature Spec Template

Use this template when starting any new feature:

```markdown
# Feature Spec: [Feature Name]

## Overview
[Brief description of the feature]

## User Stories
[List of user stories with acceptance criteria]

## Database Changes
[Tables, columns, relationships needed]

## API Endpoints
[New routes needed]

## State Management
[Stores to create or modify]

## UI Components
[Pages and components needed]

## Auth Requirements
[Roles that can access this feature]

## Dependencies
[Other features this depends on]

## Out of Scope
[What this feature does NOT include]

## Estimated Effort
- Phase 3 (Database): X hours
- Phase 4 (API): X hours
- Phase 5 (State): X hours
- Phase 6 (UI): X hours
- Phase 7 (Auth): X hours
- Phase 8 (Testing): X hours

## Risks & Considerations
[Known challenges or risks]
```

---

## 13. Checklists

### Feature Development Checklist

- [ ] Approved brief, applicable specifications and complete applicable screen set are identified before implementation.
- [ ] Approved ACCEPTANCE_SPEC and engineering QAM handoff are ready before independent QA.

```markdown
## Feature: [Name]

### Phase 1: Planning
- [ ] User stories written
- [ ] Acceptance criteria defined
- [ ] Dependencies identified

### Phase 2: Design
- [ ] Token file locked (Designer)
- [ ] Screen set shipped (HTML + PNG)
- [ ] UI_SPEC + component manifest documented

### Phase 3: Database
- [ ] Schema designed
- [ ] SQL written and run
- [ ] Types generated
- [ ] RLS policies applied

### Phase 4: API
- [ ] Services created
- [ ] API routes created
- [ ] Error handling added

### Phase 5: State
- [ ] Stores created
- [ ] Actions implemented
- [ ] Selectors defined

### Phase 6: UI
- [ ] Pages created
- [ ] Components built
- [ ] Responsive verified

### Phase 7: Auth
- [ ] Routes protected
- [ ] APIs protected
- [ ] Role-based UI working

### Phase 8: Testing
- [ ] Acceptance criteria verified
- [ ] Edge cases tested
- [ ] Bugs fixed

### Phase 9: Deployment
- [ ] Code merged
- [ ] Deployed to production
- [ ] Verified in production
```

### Code Review Checklist

```markdown
- [ ] Follows manual patterns
- [ ] TypeScript types correct
- [ ] Error handling present
- [ ] Loading states implemented
- [ ] No hardcoded values
- [ ] Environment variables used
- [ ] Console.logs removed (or intentional)
- [ ] No security issues (keys exposed, etc.)
```

### QA Checklist

```markdown
## Pre-Release QA

- [ ] QA Lead Gate Q verdict and Director release decision are recorded separately.
- [ ] Applicable deployed-environment Gate D is planned and verified; build success is not Gate D.

### Authentication
- [ ] Login works
- [ ] Logout works
- [ ] Session persists on refresh
- [ ] Protected routes redirect

### Data
- [ ] Create works
- [ ] Read works
- [ ] Update works
- [ ] Delete works

### UI
- [ ] Desktop layout correct
- [ ] Mobile layout correct
- [ ] Loading states show
- [ ] Error states show
- [ ] Empty states show

### Performance
- [ ] No slow pages
- [ ] No console errors
- [ ] No network errors
```

---

## 14. Manual Reference Guide

### When to Use Each Manual

| Manual | Use When |
|--------|----------|
| **UI-UX-BUILDING-MANUAL.md** | Building pages, components, layouts, styling |
| **AUTH_MANUAL.md** | Adding login, roles, protected routes, user management |
| **DATABASE_MANUAL.md** | Designing tables, writing SQL, managing data |
| **API_AND_SERVICES_MANUAL.md** | Creating services, API routes, webhooks, integrations |
| **STATE_MANAGEMENT_MANUAL.md** | Creating Zustand stores, managing client state |
| **APP_ARCHITECTURE_MANUAL.md** | Project structure, routing, rendering strategies |
| **ECOMMERCE_AND_PAYMENTS_MANUAL.md** | Stripe, cart logic, checkout flows |

### Quick Pattern Lookup

| Pattern | Manual | Section |
|---------|--------|---------|
| Page component | UI-UX | Page Building |
| Table component | UI-UX | Component Library |
| Auth flow | AUTH | Login Flow |
| RBAC | AUTH | Role-Based Access |
| SuperAdmin | AUTH | SuperAdmin User Management |
| DB schema | DATABASE | Schema Design Patterns |
| RLS | DATABASE | Row Level Security |
| JSONB | DATABASE | JSONB Patterns |
| Service layer | API | Service Layer |
| Webhook | API | Webhook Integration |
| CRM sync | API | CRM Integration |
| Zustand store | STATE | Store Architecture |
| Selectors | STATE | Selector Pattern |
| Persistence | STATE | Persistence |

---

## Summary

The Stark Software Factory Playbook ensures:

✅ **Predictable** - Same process for every feature  
✅ **Maintainable** - Code follows documented patterns  
✅ **Scalable** - Architecture supports growth  
✅ **Collaborative** — Director, Architect, Designer, Engineer and independent QA retain distinct responsibilities.

**Remember:**
1. **Plan before you build**
2. **Schema before code**
3. **Follow the manuals**
4. **Test against acceptance criteria**
5. **Document as you go**

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.4 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-001, FC-002, FC-005, FC-006, FC-007, FC-009, FC-021, FC-033, FC-036, FC-063, FC-066, MC-01, MC-05, MC-06, MC-07, RUL-01, RUL-05, RUL-07, RUL-08, RUL-09, RUL-11, RUL-12, RUL-14, W01, W23 |
| 1.3 | 2026-08-10 | Added §2.5 "Module Identity & QA Handoff" Factory-wide section (app-suffixed module IDs; mandatory ACCEPTANCE_SPEC contract; QA verdict ownership + Operator final authority; AC* numbering decision). Promoted from the ADK Harness field campaign via R1/R2 QA review and finalization pass. |
| 1.2 | 2026-07-07 | **Wave 1 (audit sync).** Standard header block adopted, version/date moved to top (F-018). Phase 2 rewritten to defer to DESIGNER_PLAYBOOK — token file primary, Canonical Page Method; obsolete Stitch/Figma design-spec workflow deleted (F-009, F-002). "Phase Vocabulary" note + mapping table added to §2: Blueprint lifecycle (incl. Phase 0 Recon) is the canonical phase map, these 9 phases are the execution breakdown, FFM Sub-Phases nest inside build phases (F-010). Phase 8 now points to TESTING_PLAYBOOK (F-035). §1.5 pairing-table refs stripped of version suffixes — canonical names only (F-011). Full mojibake sweep incl. 16 invisible U+0090 control chars left behind by the v1.1 "encoding fix" (F-012). §13 Phase-2 checklist aligned to Designer deliverables. |
| 1.1 | 2026-05-31 | Added Section 1.5 (Doctrine Pairing Principle). Born from Cyberize Run 001 operator insight on instruction+example pairing. Fixed UTF-8 encoding artifacts (incompletely — see 1.2). |
| 1.0 | 2024-12 | Initial playbook |

---

*This playbook is part of the Stark Industries Software Factory documentation suite.*

🥄 *App Factory doctrine.*
