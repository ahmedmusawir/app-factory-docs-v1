# FRONTEND_FIRST_PLAYBOOK.md

**Version:** 1.1.2
**Last Updated:** June 28, 2026
**Born from:** Cyberize Run 001 lessons (Lesson 2 redundant authService, Lesson 4/7 component blindness, Lesson 7 page composition) + v1.1.1 correction (Lesson 9 — over-merged sections relocated to FRONTEND_BUILD_PHASE_PLAYBOOK)

> **Purpose:**
> This document defines **how and when we build UI before backend** in this engineering factory.
>
> It exists to maximize speed **without creating backend chaos later**.

This is a **global playbook**.
It applies to *all apps* built using this factory.

---

## 0. Pre-Authoring Kit Audit (MANDATORY BEFORE ANY CODE)

> **Born from Run 001 Lesson 2** — Claudy almost authored redundant `authService.ts` wrapping kit-provided auth. The kit's complete Supabase SSR stack would have been shadowed by a useless wrapper. This section prevents that failure mode permanently.

Before authoring ANY service, component, page, or layout — perform the Kit Audit. This is a non-negotiable step. Skipping it produces the Lesson 2 family of failures (redundant authoring of capabilities the kit already provides).

### The Audit (Three Questions)

Before authoring, answer:

1. **Does the kit already provide this?**
   Check `STARTER_KIT_HANDBOOK_v1.0.md` Section "Quick Reference — Should I Author This?". If the answer is 🛑 DO NOT BUILD, you do not build. You consume the kit's primitive directly.

2. **Does a kit primitive cover this UI need?**
   Check `COMPONENT_REGISTRY_v1.0.md` Quick Decision Tree. If a primitive exists, use it. If close-but-not-quite, surface a Kit Improvement Proposal — do NOT silently fork.

3. **Does the running code in the kit already implement this pattern?**
   When the kit's running code conflicts with stale doctrine, the running code wins. Surface the conflict to the operator; do not silently "correct" the kit.

### Why This Audit Matters

In Run 001, Claudy nearly authored `authService.ts` as a wrapper around the kit's already-complete Supabase SSR auth stack. Doctrine said "all external calls go through a service layer." Reality: the kit's auth IS the service layer. Authoring a wrapper would have produced dead code that diverged from the kit baseline.

The audit is a 30-second check that prevents this category of failure permanently.

### When You Skip The Audit

You don't. The audit is mandatory. If you find yourself about to author without performing the audit, STOP and surface to the operator.

---

## 1. Why We Use a Frontend-First Approach

We build the frontend first because it allows us to:

* See the full user flow early
* Validate UX and navigation
* Catch missing features quickly
* Get stakeholder feedback before backend work
* Avoid expensive database rework

Frontend-first is **not** a shortcut.
It is a **deliberate product discovery phase**.

---

## 2. When Frontend-First Is Allowed

Frontend-first is allowed when:

* The app is internal or early-stage
* Business rules are still evolving
* UX clarity is more important than data optimization
* We want a working demo fast

Frontend-first is **not** allowed for:

* Financial ledgers
* Compliance-heavy systems
* Systems with irreversible data writes
* Highly regulated environments

---

## 3. Mandatory Gates Before UI Work Begins

Before writing UI code with mock data, **all of the following must exist**:

### Gate 1 "” App Brief

A short document describing:

* what the app does
* who the users are
* what problem it solves

### Gate 2 "” Data Contract (REQUIRED)

A data contract document must exist that defines:

* entities
* fields
* relationships
* enums
* audit fields

UI must not invent fields outside the data contract.

### Gate 3 "” Service Layer Skeleton

A service layer must exist, even if:

* it returns hardcoded or mock data
* no backend exists yet

UI must **only** talk to the service layer.

---

## 4. Data Contract Rules

* Each app has its own data contract
* The data contract is app-specific
* Changes to UI that affect data shape **must update the data contract first**

If UI needs something not in the contract:

1. Update the contract
2. Update mock data
3. Update UI
4. Backend comes later

### Related Documents

* `CYBERBUGS_DATA_CONTRACT.md` "” defines entities, fields, and relationships for CyberBugs
* Future apps will have their own `{APPNAME}_DATA_CONTRACT.md`

---

## 5. Service Layer Rules (Non-Negotiable)

* UI never fetches data directly
* UI never imports Supabase clients
* UI never talks to mock APIs directly

All data access goes through:

* service functions
* domain-named methods (e.g. `getBugs`, `createBug`)

The service layer acts as a **swap point**:

* mock implementation today
* real backend implementation later

### Service Layer Example

```typescript
// src/services/bugService.ts

import type { Bug } from '@/types';

// During Demo Mode: returns mock data
// During Production Mode: calls Supabase

export const bugService = {
  getAll: async (): Promise<Bug[]> => {
    // Mock implementation (swap later)
    const { bugs } = await import('@/mocks/data/bugs');
    return bugs;
  },

  getById: async (id: string): Promise<Bug | null> => {
    const { bugs } = await import('@/mocks/data/bugs');
    return bugs.find(b => b.id === id) || null;
  },

  create: async (bug: Omit<Bug, 'id' | 'created_at'>): Promise<Bug> => {
    // Mock: just return with fake id
    return { ...bug, id: `bug-${Date.now()}`, created_at: new Date().toISOString() };
  }
};
```

UI components call `bugService.getAll()` "” they never know if it's mock or real.

---

## 6. Mock Data Strategy

Mock data exists to support UI development only.

### Allowed Mock Strategies (Ranked)

**Option 1 "” In-code typed mocks (Preferred)**

* mock data as plain objects
* returned by service functions
* disposable and easy to remove

**Option 2 "” Mock Service Worker (MSW)**

* intercepts API calls
* simulates real backend
* useful for realistic demos

**Option 3 "” JSON Server (Use With Discipline)**

* allowed only behind service layer
* must mirror data contract exactly
* must be disposable

If mock infrastructure slows development, it must be removed.

### Mock File Location

All mock data lives in:

```
src/
└── mocks/
    ├── data/
    │   ├── apps.ts
    │   ├── bugs.ts
    │   ├── users.ts
    │   └── index.ts
    └── services/
        ├── appService.mock.ts
        ├── bugService.mock.ts
        └── userService.mock.ts
```

When transitioning to backend:

* Delete `src/mocks/` folder
* Update service imports to use real implementations

---

## 7. What Frontend-First Must Produce

A frontend-first phase should produce:

* Fully navigable UI
* Role-based access visible in UX
* Empty, loading, and error states
* Validated user flows
* Clear backend requirements

A successful frontend-first phase ends when:

* stakeholders agree on UX
* data needs are fully understood
* backend work is unblocked

---

## 8. Transition to Backend Phase

Once UI is approved:

* service layer implementation is swapped
* Supabase tables are created
* RLS policies are added
* mock data is removed
* UI remains unchanged

This is the **key success metric** of frontend-first:

> backend can be added without rewriting UI.

---

## 9. Common Failure Modes (Avoid These)

* Building UI without a data contract
* Fetching data directly in components
* Letting mock APIs become permanent
* Inventing fields during UI work
* Skipping service layer "because it's just a demo"

Frontend-first fails when discipline is lost.

---

## 10. Summary (Rules to Remember)

* Frontend-first is a **phase**, not a shortcut
* Data contract is mandatory
* Service layer is mandatory
* Mock data is temporary
* UI must survive backend replacement unchanged

---

## 11. Frontend-First Checklist

### Before Starting UI Work

- [ ] App Brief exists
- [ ] Data Contract exists and is reviewed
- [ ] Service layer skeleton created
- [ ] Mock data matches contract
- [ ] Types defined in `src/types/`

### Before Calling UI "Done"

- [ ] All pages navigable
- [ ] RBAC visible in UI (admin sees admin stuff, tester sees tester stuff)
- [ ] Loading states implemented
- [ ] Empty states implemented
- [ ] Error states implemented
- [ ] Stakeholder feedback collected
- [ ] Mobile responsiveness verified

### Before Transitioning to Backend

- [ ] Data Contract finalized (no more changes)
- [ ] Service layer ready for real implementation swap
- [ ] Mock data documented for removal
- [ ] All UI flows approved by stakeholders

---

## 12. Page Composition Pattern (Co-Location Rule)

> **Born from Run 001 Lesson 7.**

Every Next.js App Router page in this factory follows the co-location pattern. The `page.tsx` is a thin 3-8 line wrapper. The actual content lives in a co-located `<Feature>PageContent.tsx` file IN THE SAME FOLDER.

### The Pattern

```
src/app/(group)/feature/
├── page.tsx                    ← thin wrapper (3-8 lines)
├── FeaturePageContent.tsx      ← actual page content
└── [optional subcomponents specific to this page]
```

### `page.tsx` Convention

A `page.tsx` is a thin import-and-render wrapper. Maximum 8 lines.

```typescript
import { ChatPageContent } from "./ChatPageContent";

export default function ChatPage() {
  return <ChatPageContent />;
}
```

If your `page.tsx` is doing more than this, refactor — move the logic into `<Feature>PageContent.tsx`.

### 🛑 The Critical Rule

**`*PageContent.tsx` files DO NOT live in `src/components/`.**

❌ **Wrong:**
```
src/components/chat/ChatPageContent.tsx     ← never here
src/app/(cyberize)/chat/page.tsx
```

✅ **Right (co-located):**
```
src/app/(cyberize)/chat/page.tsx
src/app/(cyberize)/chat/ChatPageContent.tsx ← co-located with page.tsx
```

`src/components/<feature>/` is for **cross-page** components ONLY. Components specific to a single page co-locate with that page.

### Reference Example

The canonical worked example of this pattern is at:
- `src/app/(admin)/admin-portal/page.tsx` (thin wrapper)
- `src/app/(admin)/admin-portal/AdminPortalPageContent.tsx` (actual content)

---

## 13. Pre-Write Check Protocol (MANDATORY For UI Files)

> **Born from Run 001 doctrine-decay pattern.** Before authoring any UI component, page, or layout file, the file's opening JSDoc MUST answer these four questions:

1. **What kit primitive(s) could I use here?** (List considered + chosen)
2. **What does the UI-UX-BUILDING-MANUAL say about this pattern?** (Cite section)
3. **What's the 375px sketch?** (1-3 sentences mobile layout)
4. **What changes at 768 and 1024?** (Breakpoint behaviors)

If you cannot answer all four, do not author the file. Surface to the operator.

### Example Opening JSDoc

```typescript
/**
 * ChatMessageList — renders the conversation message list with auto-scroll.
 *
 * Pre-Write Check:
 *   1. Primitives used: AppShellPage (page wrapper), Row (message rows), Box (bubbles).
 *      Considered: raw flex divs — rejected, kit primitives provide responsive defaults.
 *   2. Manual reference: UI-UX-BUILDING-MANUAL Rule Zero + Layouts section.
 *   3. 375 sketch: full-width column of stacked Rows, each containing a single Box bubble.
 *      Sidebar is hidden behind hamburger at this width.
 *   4. 768: sidebar becomes persistent (250px), message column takes remainder.
 *      1024: max-width container (1200px) centers the message column.
 */
```

---

## 14. Stage Execution Doctrine — See FRONTEND_BUILD_PHASE_PLAYBOOK

> **Doctrine relocated.** Stage-level execution discipline (Pre-Phase Doctrine Refresh, Kit Improvement Proposals, Stage-level Pre-Write Checks) lives in its proper home: `FRONTEND_BUILD_PHASE_PLAYBOOK_v1.2.md`.

This playbook (`FRONTEND_FIRST_PLAYBOOK`) answers **when and why** to use frontend-first.

The sibling playbook (`FRONTEND_BUILD_PHASE_PLAYBOOK`) answers **how to execute** the frontend build, stage by stage. That's where you'll find:

- **Section 1.5** — Pre-Phase Doctrine Refresh protocol (mandatory re-read at start of every stage)
- **Section 1.6** — Kit Audit (mandatory before any authoring in any stage)
- **Stage 2** — Pre-Write Check Protocol (the four mobile-first questions for every UI file)
- **Section 12** — Kit Improvement Proposals format (stage completion reports)
- **Section 13** — Run 001 Lessons appendix (Lessons 2, 4, 5, 7, plus the new Lesson 9)

### Why This Split

In v1.1 of these playbooks, doctrine was initially duplicated across both files. Operator caught the duplication in retrospective. Stage execution doctrine belongs in the build-phase playbook (which describes stages); methodology selection doctrine belongs here (which describes when to choose frontend-first).

This split is also v1.1's first explicit application of the **Doctrine Pairing Principle** (see `SOFTWARE_FACTORY_PLAYBOOK_v1.1.md` Section 1.5) — playbooks paired with each other and with worked examples, not bloated into a single mega-doc.

---

## 15. Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.1.2 | 2026-06-28 | Re-pointed the §12 co-location Reference Example from the deleted `/demo` route to the live `(admin)/admin-portal` page+content pair (preserve lesson, swap actor). Kit Hardening Gate 10. |
| 1.1.1 | 2026-06-02 | Sections 14 and 15 trimmed to cross-references. Stage execution doctrine (Pre-Phase Doctrine Refresh, Kit Improvement Proposals) relocated to its proper home in FRONTEND_BUILD_PHASE_PLAYBOOK_v1.2.md. Doctrine de-duplication. Born from Lesson 9 (speculative authoring caught in v1.1 retrospective). |
| 1.1 | 2026-05-31 | Added Section 0 (Kit Audit), Section 12 (Page Composition), Section 13 (Pre-Write Check), Section 14 (Phase Doctrine Refresh), Section 15 (Kit Improvement Proposals). Born from Cyberize Run 001 lessons 2, 4, 5, 7. Fixed UTF-8 encoding artifacts. |
| 1.0 | 2026-01-01 | Initial playbook |

---

### END OF DOCUMENT

---

🥄 *Part of Stark Industries — App Factory v1.1 doctrine.*