# STARTER KIT HANDBOOK

> **Canonical answer to: "What does the kit already provide?"**
>
> **🛑 READ THIS BEFORE AUTHORING ANY SERVICE, COMPONENT, OR ROUTE.**
>
> If the kit provides what you're about to build, you DO NOT build it. You consume the kit's primitive directly.

**Kit:** Stark SaaS Starter — **Starter Kit v3** (Pro RBAC Next.js Starter Kit)
**Version:** v1.1 (Kit-Perfection campaign applied)
**Framework:** Next.js 16.2.1 (App Router) + React 19.2.4
**Last Updated:** 2026-06-28 (Gates 1–10 of the "Kit Perfection" hardening campaign)
**Maintained by:** Stark Industries — App Factory

---

## 🚨 The First Rule

**Every Factory run begins by reading this handbook in Phase 0.** No exceptions.

**Why this exists:** In Factory Run 001 (Cyberize), the agent almost authored a redundant `authService.ts` wrapping the kit's already-complete Supabase auth stack. The kit's capabilities weren't documented in one canonical place, so the agent followed the module's generic DATA_CONTRACT literally. This handbook prevents that failure mode permanently.

**The principle:** If the kit provides it as wired infrastructure, **components consume it directly**. The service layer is reserved for what the kit does NOT provide — domain operations specific to the project (chat, agent profiles, agent instructions, etc.).

**Disk wins over docs.** This handbook describes intent; the on-disk code is the source of truth. Every file/export/breakpoint named here was reconciled against disk during the Kit-Perfection campaign. If you ever find a divergence, surface it — don't average the two into a guess.

---

## Table Of Contents

1. [Auth — Already Wired](#1-auth--already-wired)
2. [RBAC & RLS — Already Wired](#2-rbac--rls--already-wired)
3. [Database — Schema & Patterns](#3-database--schema--patterns)
4. [Components — Inventory](#4-components--inventory)
5. [Routing — Conventions](#5-routing--conventions)
6. [Responsive & Mobile-Nav](#6-responsive--mobile-nav)
7. [State Management — Patterns](#7-state-management--patterns)
8. [Tests — Baseline & Conventions](#8-tests--baseline--conventions)
9. [Build & Framework Notes](#9-build--framework-notes)
10. [Common Gotchas](#10-common-gotchas)
11. [Known Issues — Resolved](#11-known-issues--resolved)
12. [What's NOT In The Kit (Build Yourself)](#12-whats-not-in-the-kit-build-yourself)
13. [Quick Reference — "Should I Author This?"](#13-quick-reference--should-i-author-this)
14. [Handbook Maintenance](#14-handbook-maintenance)
15. [Cross-References](#15-cross-references)

---

## 1. Auth — Already Wired

### 🛑 DO NOT AUTHOR

- `src/services/authService.ts` — **forbidden.** The kit's auth is complete. Components consume the kit's auth primitives directly.
- Custom session refresh logic — the proxy handles it.
- Custom login/logout API routes — they exist already.

### What The Kit Provides

The kit ships with a complete Supabase SSR auth stack. Four client types, request-level session refresh, three working portals.

**Supabase Clients (use the right one):**

| Client | File | When To Use | RLS Bypass? |
|---|---|---|---|
| Server (anon) | `src/utils/supabase/server.ts` | Server Components, API routes — own-user ops | NO — respects RLS |
| Browser | `src/utils/supabase/client.ts` | Client Components, browser auth flows | NO — respects RLS |
| Middleware | `src/utils/supabase/middleware.ts` | Session refresh, consumed by `src/proxy.ts` | NO |
| Admin (service role) | `src/utils/supabase/admin.ts` | Portal admin operations | **YES — bypasses RLS** |

**Cookie adapter (modernized — Gate 8):** all four clients use the Supabase SSR `getAll`/`setAll` cookie pattern (not the deprecated `get`/`set`/`remove`). The kit's cookie security flags — `secure`, `sameSite: 'lax'`, **`httpOnly: false`** — are deliberate and preserved in `setAll`. `httpOnly: false` is intentional ("Supabase needs client-side session access"); do NOT "tighten" it. **Modernize the mechanism, never the security behavior** — a dropped flag is a live-session bug that no build will catch.

**Auth API Routes (`src/app/api/auth/`):**

- `login/route.ts` — email/password login
- `logout/route.ts` — clears session
- `signup/route.ts` — public signup, creates `member` role; **metadata key MUST be `full_name`**
- `confirm/route.ts` — email confirmation callback

**User creation is via server actions, not an API route.** Admin → `addMember` (`(admin)/admin-portal/actions.ts`); superadmin → `addUser` (`(superadmin)/superadmin-portal/actions.ts`). Both run behind a role-gated layout (`protectPage`) and then call the service-role admin client. (The legacy `POST /api/auth/superadmin-add-user` route was a dead fossil — removed in Gate 6. Superadmins are **console-only**; see §2.)

**Client Auth State:**

- `src/store/useAuthStore.ts` — Zustand store managing current user, derived role flags, authenticated state, login/logout actions
- **Use this in client components** — do NOT create a parallel auth store

**Server-Side Page Protection:**

- `src/utils/supabase/actions.ts` exports `protectPage([AppRole.X])`
- Use as the FIRST call in any protected layout's `RootLayout` async function
- Returns the authenticated user or redirects to `/auth`

### How To Consume Auth (The Right Way)

**In a Server Component (e.g., a portal layout):** Use `protectPage([AppRole.ADMIN])` at the top of the layout. No service wrapper needed. See `src/app/(admin)/layout.tsx` for the canonical pattern.

**In a Client Component (e.g., a sidebar showing user email):** Read from `useAuthStore`. Do NOT call `supabase.auth.getUser()` from the client directly.

**In an API Route:** Create the server client via `createClient()`, call `supabase.auth.getUser()`, check the user exists, then proceed.

**For login/logout from a form:** Submit to `/api/auth/login` or `/api/auth/logout`. Use `.catch()` chains, NOT `try/catch` (see Common Gotchas).

### Auth Pattern Decision Tree

```
Need to know "is the user logged in?" in a Server Component?
  → const { data: { user } } = await supabase.auth.getUser()
  → Or use protectPage([role]) if it's a protected route

Need to know "is the user logged in?" in a Client Component?
  → useAuthStore() — read the state

Need to log in / log out?
  → POST to /api/auth/login or /api/auth/logout

Need to know the user's role?
  → Server: await getUserRole() from src/utils/get-user-role.ts
  → Client: useAuthStore() derived flags (isAdmin, isSuperadmin, isMember)
```

> **A green build proves nothing for cookie/session changes.** The real gate for any auth-touching change is the operator AUTH-WALK: login → nav-persist → hard-refresh → logout-bounce → role-resolve.

---

## 2. RBAC & RLS — Already Wired

### 🛑 DO NOT AUTHOR

- Custom role-checking logic in components — use `useAuthStore` flags or `protectPage`
- Custom RLS policies for `profiles` or `user_roles` — they exist
- New role tables — the two-table pattern is locked
- **Any app-side superadmin-creation surface** — see the console-only doctrine below

### Roles

Three roles, defined in the `AppRole` enum at `src/utils/app-role.ts` (universal — safe in client components):

- `superadmin` — full platform access
- `admin` — restricted user management
- `member` — own profile only

### 🛡️ DOCTRINE — Superadmins Are CONSOLE-ONLY

Superadmins are created in the **Supabase console ONLY**, never from the app. There must be **no app-side superadmin-creation surface** — it is a privilege-escalation attack surface. The deleted fossil route `/api/auth/superadmin-add-user` violated this and was removed in Gate 6.

Corollaries:
- A superadmin-created user landing as `member` is acceptable — promotion to superadmin happens in the console.
- The doctrine extends to **self-service**: superadmin has NO in-app profile by design. Its Profile link is hidden (render-time `isSuperadmin` gate) and the shared `/profile` route bounces superadmins via its `[ADMIN, MEMBER]` gate.

### The Two-Table Pattern (CRITICAL)

Roles and profiles live in **two sibling tables** — both FK to `auth.users(id)`, with NO direct FK between them:

```sql
public.profiles
  id         uuid PK → auth.users(id) ON DELETE CASCADE
  full_name  text
  email      text
  created_at timestamptz

public.user_roles
  id         uuid PK
  user_id    uuid → auth.users(id) ON DELETE CASCADE
  role       text  -- 'superadmin' | 'admin' | 'member'
```

**🛑 PostgREST nested selects DO NOT WORK across sibling tables.**
- ❌ NEVER use `profiles(user_roles(role))`
- ✅ ALWAYS use the two-query merge pattern (fetch profiles, then fetch roles separately, merge in JS)

### The DB Trigger (Mark IV)

`handle_new_user()` (`supabase/setup.sql`) fires atomically on every `auth.users` INSERT:

- Reads `full_name` from `raw_user_meta_data` (the key every writer writes)
- Reads `role` from `raw_user_meta_data` — applies it; defaults to `'member'` if absent
- Inserts into BOTH `user_roles` AND `profiles` (idempotent — `ON CONFLICT DO NOTHING`)

> **Mark IV is the shipped trigger as of Gate 10 Phase A**, proven live 2026-06-28. It replaced an earlier "dumb" trigger that hard-coded `'member'` and read the wrong key (`'name'`), which caused two now-RESOLVED bugs (`profiles.full_name` NULL at creation; superadmin role-drop). See §11 and `KNOWN_ISSUES.md`.

**🛑 Never manually insert into `user_roles` or `profiles` when creating users via `auth.admin.createUser()`.** The trigger handles it. Manual inserts cause duplicate-key errors. Just write `full_name` + `role` into `user_metadata` and let Mark IV apply them.

### How To Check Roles

**Server Component / API Route:**

```typescript
import { getUserRole } from "@/utils/get-user-role";
const role = await getUserRole();
if (role === AppRole.ADMIN) { /* ... */ }
```

**Client Component:**

```typescript
import { useAuthStore } from "@/store/useAuthStore";
const isAdmin = useAuthStore((s) => s.isAdmin);
```

**Protected Layout:**

```typescript
// src/app/(admin)/layout.tsx
await protectPage([AppRole.ADMIN]);
```

### Role Color Standard (Never Deviate)

```
superadmin → text-purple-600 dark:text-purple-400
admin      → text-red-600    dark:text-red-400
member     → text-green-600  dark:text-green-400
```

(In components, role colors are driven through the `--role-*` design tokens — never hardcode numbered Tailwind colors in primitives.)

---

## 3. Database — Schema & Patterns

### Tables Already In The Kit

| Table | Purpose | RLS |
|---|---|---|
| `auth.users` (Supabase managed) | All users | Supabase-managed |
| `public.profiles` | Display names, email, created_at | Per-user policies pre-applied |
| `public.user_roles` | Role assignments | Per-user policies pre-applied |

### RLS Patterns (Pre-Applied On Kit Tables)

Standard pattern — users see/edit their own data:

```sql
CREATE POLICY "Users see own profile"
ON profiles FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Users update own profile"
ON profiles FOR UPDATE USING (auth.uid() = id);
```

Service role bypasses RLS — used in admin API routes / server actions.

### When You Add New Tables (Project-Specific)

- **Always enable RLS:** `ALTER TABLE <new_table> ENABLE ROW LEVEL SECURITY;`
- **Always FK to `auth.users(id)` with `ON DELETE CASCADE`** when scoping to users
- **Always document RLS policies** in `_project/CLAUDE.md` for the run
- **Use service role client** for admin operations, anon client for user-facing
- **Test with both role contexts** (admin + member) before declaring done

> **DDL is backend state, not kit-shippable code.** The trigger + RLS live in the Supabase instance and are applied per-instance (`supabase/setup.sql`). A schema change isn't "done" until it's applied to the live DB and verified there — a green build says nothing about DB state.

---

## 4. Components — Inventory

### 🛑 BEFORE AUTHORING ANY COMPONENT

1. Check `COMPONENT_REGISTRY_v1.1.md` (sibling file) — does a primitive exist?
2. Check `src/components/common/` for layout primitives
3. Check `src/components/ui/` for Shadcn primitives
4. Check `agent_docs/APP_FACTORY/UI-UX-BUILDING-MANUAL_v1_3.md`
5. Only if NONE of those provide it, author the new component

### Common Layout Primitives (`src/components/common/`)

| Primitive | Purpose | When To Use |
|---|---|---|
| `Page` | Responsive content-flow wrapper | Marketing pages, forms, doc pages |
| `Row` | Full-width section with `p-5` padding | Stacked content sections |
| `Box` | Bare content block | Bubbles, cards, content blocks |
| `Container` | Page variant for nested sections | Sub-pages |
| `Main` | `<main>` semantic element with `flex-grow` | Wrapping main content |
| `AppShellPage` | Full-bleed app shell with sidebar + main | Chat, mission control, dashboards, ops consoles |
| `PaginationControls` | Shared pagination with `useTransition` | Any portal list view |

### AppShellPage (REAL as of Gates 2–3)

The app-shell primitive. Mobile-first built-in. Props: `{ sidebar, children, mobileTitle?, mobileTopBarRight? }`.

```typescript
<AppShellPage
  sidebar={<MySidebar />}
  mobileTitle="MY APP"
  mobileTopBarRight={<ThemeToggle />}
>
  {/* main column content */}
</AppShellPage>
```

**Mobile behavior contract (the real one):**
- Below `xl` (<1280px): the sidebar becomes a hamburger-triggered slide-over — a `Sheet` (`side="left"`) under a two-bar layout (the shared global `Navbar` + a slim trigger bar). Dismiss via close-on-nav, outside-tap, and Esc.
- `xl`+ (≥1280): the sidebar is persistent (`w-[25rem]`, `border-r`); main takes the remainder. The mobile trigger bar disappears.
- `sidebar` may be a **render-fn** `(close) => ReactNode` so a panel can close itself on a terminal action (Apply/Done).

**The 4 CP scars** (baked into the primitive): close-on-nav (`usePathname`), passable `close` to a render-fn sidebar, ~25rem width capped to 85vw, native dismiss (outside-tap + Esc).

> **🛑 AppShellPage owns the `<main>`.** A page adopting the shell must NOT bring its own `<main>` (nested `<main>` is invalid HTML). Heavy in-file JSDoc at `src/components/common/AppShellPage.tsx` documents the decision tree, the mobile contract, the breakpoint, and the scars.

### Layout Decision Tree

```
Is this a full-bleed app surface (sidebar + scrolling main / sticky input)?
  YES → AppShellPage  (chat, mission control, dashboards, ops consoles)
  NO  → Is this content-flow (marketing, doc, list, form)?
          YES → Page + Row + Box  (home, settings forms, marketing)
          NO  → Is it a dense data table portal?
                  YES → plain <div className="container mx-auto p-6">
                        (admin-portal precedent — kit allows this)
```

### Global Components (`src/components/global/`) — actual on disk

| Component | Purpose |
|---|---|
| `Navbar` | Authenticated portal top bar (members/admin/superadmin) |
| `PublicNav` | Public/marketing nav (logo + portal links + theme + auth island) |
| `PublicNavAuthSection` | Auth-state island consumed by `PublicNav` |
| `PublicMobileNav` | Hamburger + `Sheet` mobile menu for the public nav (< `lg`) |
| `NavbarLoginReg` | Minimal auth-pages bar (logo + theme) |
| `ThemeToggle` | Light/dark/system theme switcher (next-themes) |

> `NavbarHome` and `NavbarSuperadmin` do **NOT** exist — they were removed from the registry during the campaign. Don't author them back.

### Layout Components (`src/components/layout/`)

| Component | Purpose |
|---|---|
| `Sidebar` | Default sidebar |
| `AdminSidebar` | Admin portal sidebar |
| `SuperadminSidebar` | Superadmin portal sidebar |

### Auth & Profile Components

| Component | Location | Purpose |
|---|---|---|
| `LoginForm` | `src/components/auth/` | Login UI — wired to `/api/auth/login` |
| `RegisterForm` | `src/components/auth/` | Signup UI — wired to `/api/auth/signup` |
| `AuthTabs` | `src/components/auth/` | Tab switcher between login/register |
| `ProfileForm` | `src/components/profile/` | **One shared** role-aware profile form (admin + member) — see §5 |

### Shadcn UI Components (`src/components/ui/`)

Standard Shadcn primitives installed and themed: `Button`, `Input`, `Label`, `Textarea`, `Card` (+ Header/Content/Footer), `Alert`, `Dialog`, `Sheet` (kit-authored `ui/sheet.tsx` on Radix dialog), `DropdownMenu`, `Select`, `Skeleton`, `Spinner` (lucide `Loader2`), `Sonner` (toast, global), `ScrollArea`, `Separator`, `Tabs`, `Form` (`react-hook-form` + `zod`).

If you need a Shadcn primitive that's NOT installed, use `npx shadcn@latest add <name>` rather than authoring from scratch.

---

## 5. Routing — Conventions

### App Router Only

- ✅ App Router patterns exclusively
- ❌ NEVER Pages Router (`getStaticProps`, `getServerSideProps`)
- All routes in `src/app/`

### Route Groups (Current Kit Baseline)

```
src/app/
  (public)/                — Public routes
    layout.tsx             — No auth required
    page.tsx               — Home (thin) + PageContent.tsx

  (auth)/                  — Auth pages
    auth/page.tsx          — Login + register (AuthTabs)

  (account)/               — Shared account area (sidebar-less)
    layout.tsx             — protectPage([AppRole.ADMIN, AppRole.MEMBER])
    profile/               — ONE shared /profile (admin + member) → ProfileForm

  (superadmin)/            — Superadmin portal
    layout.tsx             — protectPage([AppRole.SUPERADMIN])
    superadmin-portal/     — Full CRUD user management (addUser server action)

  (admin)/                 — Admin portal
    layout.tsx             — protectPage([AppRole.ADMIN])
    admin-portal/          — Restricted CRUD (addMember server action)

  (members)/               — Member portal
    layout.tsx             — protectPage([AppRole.MEMBER])
    members-portal/        — Member dashboard

  api/auth/                — Auth API routes (login, logout, signup, confirm)
```

### Profile is ONE shared route (Gate 7)

There is no per-portal profile duplication. `/profile` lives in the `(account)` group gated `[ADMIN, MEMBER]`, backed by the single role-aware `components/profile/ProfileForm.tsx`. Superadmin has no profile (console-only; §2).

> **🛑 Shared links must match route protection.** A link shared across roles must point at a route that accepts ALL of those roles. (Live bug caught in Gate 7: the shared Navbar Profile link pointed at an admin-only route → it bounced members to `/auth`. A shared link + a narrower gate = a bounce bug.)

### Page Composition Pattern (CRITICAL)

`page.tsx` is a thin wrapper (3–8 lines). Content lives in a co-located `<Feature>PageContent.tsx`.

```typescript
// page.tsx
import { ChatPageContent } from "./ChatPageContent";
export default function ChatPage() { return <ChatPageContent />; }
```

### File Naming Conventions

| File Type | Location | Naming |
|---|---|---|
| Page wrapper | `src/app/<group>/<route>/page.tsx` | `page.tsx` |
| Page content | Same folder as `page.tsx` | `<Feature>PageContent.tsx` |
| Page-specific subcomponent | Same folder as `page.tsx` | `<Name>.tsx` |
| Shared cross-page component | `src/components/<feature>/` | `<Name>.tsx` |
| Common layout primitive | `src/components/common/` | PascalCase |

**🛑 Page-specific components co-locate with their `page.tsx`.** `src/components/<feature>/` is for **cross-page** components ONLY.

### loading.tsx Placement

Inside the portal subdirectory, not at route-group level:
- ✅ `(admin)/admin-portal/loading.tsx`
- ❌ `(admin)/loading.tsx` — wraps the entire layout including Navbar

### proxy.ts vs middleware.ts (Next.js 16)

- The kit ships `src/proxy.ts` — **correct for Next.js 16+** (the renamed middleware convention)
- Older docs may say `middleware.ts` — **on-disk code is the source of truth**
- DO NOT propose renaming `proxy.ts` → `middleware.ts` (Run 001 Lesson 1 trap)

---

## 6. Responsive & Mobile-Nav

Mobile-first is the kit's foundational posture (UI-UX Manual Rule Zero). The kit has ONE blessed way to do each responsive thing — match it, don't invent.

### Breakpoint contract — the rail vs. the nav

- **App-shell rail persists at `xl` (1280)**, not `lg`. Below `xl`, the `AppShellPage` sidebar collapses to a slide-over. `w-[25rem]` is the persistent rail width.
- **Per-component fit-breakpoints override a blanket rule.** The public nav correctly goes full-horizontal at **`lg` (1024)** — three short links fit there. `xl` is the *rail's* fit rule, not a kit-wide law. Pick the breakpoint where the actual content fits; don't cargo-cult one number everywhere.

### One mobile-menu pattern: the `Sheet`

Every mobile slide-over in the kit is the `Sheet` primitive (`ui/sheet.tsx`, Radix dialog) — both the `AppShellPage` drawer and `PublicMobileNav`. Do NOT reintroduce an older dropdown-style mobile menu. "Match, don't invent" = match the kit's *own* blessed pattern.

### Touch tap-floors: the `coarse:` variant

For touch-only tap-target floors (44px), use the registered **`coarse:` variant** (`@media (pointer: coarse)`, registered in `tailwind.config.ts`).

> **⚠️ ALWAYS verify the BUILT CSS for a variant.** `pointer-coarse:` *looks* like a real Tailwind 3.4 variant but isn't — it silently generates **zero CSS** (a phantom). The only proof a variant works is grepping the compiled output, not that the class name "looks right."

### The 4 CP scars (mobile drawer)

Any app-shell drawer carries these (already baked into `AppShellPage`): close-on-nav (`usePathname`), a passable `close` for render-fn sidebars, ~25rem capped to 85vw, native dismiss (outside-tap + Esc).

---

## 7. State Management — Patterns

### Zustand For App-Level State

- `src/store/useAuthStore.ts` — auth state (kit-provided; do NOT duplicate)
- New stores live in `src/store/use<Feature>Store.ts`
- Stores are singletons — survive across renders
- Use selectors to avoid re-renders: `useStore((s) => s.field)`

### useState For Local UI State

Form inputs (until react-hook-form), dropdown open/closed, tab selection, anything confined to one component tree.

### Server Components — Server State

Fetch DB data in Server Components, pass to Client Components via props. Don't fetch in Client Components if a Server Component could.

### When To Reach For Each

```
Auth state, current user, role flags?      → useAuthStore (kit-provided)
App-level state used by 2+ components?      → new Zustand store in src/store/
Form input values?                          → useState OR react-hook-form (preferred w/ validation)
Single-component UI state?                  → useState
DB data for initial render?                 → Server Component, pass via props
```

---

## 8. Tests — Baseline & Conventions

### Baseline (Starter Kit v3)

**76 tests, 10 suites, 0 failures.**

| Suite | Area |
|---|---|
| `actions.test.ts` | `protectPage` |
| `get-user-role.test.ts` | role resolution |
| `proxy.test.ts` | session-refresh proxy |
| `superadmin/actions.test.ts` | superadmin CRUD server actions |
| `superadmin/AddUserForm.test.tsx` | superadmin add-user form |
| `superadmin/EditUserForm.test.tsx` | superadmin edit-user form |
| `superadmin/SuperadminPortalPageContent.test.tsx` | superadmin portal |
| `admin/actions.test.ts` | admin CRUD server actions |
| `admin/AddMemberForm.test.tsx` | admin add-member form |
| `member/ProfileForm.test.tsx` | the shared `ProfileForm` |

> The old `superadmin-add-user.test.ts` was removed with its fossil route (Gate 6). The exact baseline is confirmed by `npm test`, not by summing this table from memory.

### Running Tests

```bash
npm test
```

### The Ironman Rule

> **Do not merge changes that break any test. Fix the test or fix the code — never comment out tests.**

### Test Conventions

- Tests live in `src/__tests__/` mirroring source structure
- Component tests `*.test.tsx`; logic tests `*.test.ts`; Jest + React Testing Library
- Pagination elements are `role="button"` (NOT `role="link"`)
- For impossible-to-mock APIs (clipboard, etc.), use **behavior-based assertions** (test visible UI state, not implementation)
- **Drain leaked async before asserting its absence.** A test that fires a `setTimeout`-mocked redirect can leak a `router.push` into a *later* test. Await the effect (`waitFor`) and assert on re-enabled UI, not on a bare "was not called." (Gate 9 de-flake.)
- Test intent, not implementation (Rule K9) — a test that can't fail when business logic changes is wrong

---

## 9. Build & Framework Notes

### Framework Versions

- **Next.js:** 16.2.1 (App Router)
- **React:** 19.2.4
- **TypeScript:** strict mode, no `any`

### Build Commands

```bash
npm run dev          # Development
npm test             # Run test suite
npm run build        # Production build
npx tsc --noEmit     # Type check only
```

### Verification Triad (Run Before Phase Boundaries)

1. `npx tsc --noEmit` — must exit zero
2. `npm test` — must pass all baseline + new tests
3. `npm run build` — must complete cleanly **with no env vars set** (cold build)

> A passing triad is necessary, not sufficient. Cookie/session/RBAC changes also need the operator AUTH-WALK; DB changes need live verification against the Supabase instance.

### 🛑 Stale `.next/types` cache → false tsc failures

After **deleting** a route/file, `.next/types/validator.ts` keeps referencing the dead path and tsc throws `TS2307` — indistinguishable from a real orphan. **`rm -rf .next` and re-run tsc before trusting any post-deletion type error.**

### Server / Client Component Boundary

When a `"use client"` component imports a runtime value (enum, const, function) from a module, the ENTIRE module is bundled for the client. If that module has server-only imports (`next/headers`, `supabase/server`, server actions), they leak into the client bundle and `next build` fails.

**Cross the boundary safely:** extract shared values to a server-dep-free module.
- `src/utils/get-user-role.ts` — `getUserRole()` (server-only)
- `src/utils/app-role.ts` — `AppRole` enum (universal — safe in client components)

### Typing, not casting

A needed type annotation is NOT a moved cast. Removing `(await cookies()) as any` is only real if you don't reintroduce `any` elsewhere — e.g. annotate `setAll(cookiesToSet: { name: string; value: string; options: CookieOptions }[])`, a precise type, not `any`. Verify the change with a project-wide `as any` count, not a green build.

### Login Error Handling

Use `.catch()` chains, NOT `try/catch` (Next.js dev overlay intercepts thrown errors before `try/catch`):

```typescript
login(...).catch((e) => { /* ... */ })
```

### Edit Form Redirect Pattern

`router.refresh()` BEFORE `router.push()` — else dashboards show stale data after redirect.

### Theme Conventions

Explicit Tailwind classes for theme-aware backgrounds: Dialog/Dropdown `bg-white dark:bg-slate-800`; Toast `bg-white dark:bg-zinc-900`; Input `p-6 bg-slate-100 dark:bg-slate-500 dark:text-white`.

---

## 10. Common Gotchas

### Gotcha 1: PostgREST Nested Selects Across Sibling Tables

`select("*, user_roles(role)")` silently returns empty. Use the two-query merge (fetch profiles + roles separately, merge in JS).

### Gotcha 2: Don't Manually Insert Into `user_roles` Or `profiles`

The Mark IV trigger handles it. Manual inserts cause duplicate-key errors.

### Gotcha 3: NavigationLoadingProvider — PERMANENTLY DELETED

Rendered `fixed inset-0 z-[9999] bg-white` on every `<a>` click, covering the Navbar. **Do NOT recreate.**

### Gotcha 4: Signup Metadata Key

When creating users via `auth.admin.createUser()`, the metadata key MUST be `full_name`. The Mark IV trigger reads this exact key (it also reads `role`).

### Gotcha 5: Service Role Bypasses RLS

`createAdminClient()` (service role) bypasses ALL RLS. Use ONLY server-side (API routes / server actions) that need elevated permissions. Never from the client.

### Gotcha 6: Stale Kit Docs Vs Live Code

When a doc references a file/export/route that doesn't match disk, **on-disk code is the source of truth**. Surface the doc-vs-code conflict to the operator; don't silently "fix" the code to match a stale doc.

### Gotcha 7: A Variant That Generates No CSS

`pointer-coarse:` is not a real TW3.4 variant — it compiles to nothing. Register `coarse:` and grep the BUILT CSS to prove any variant actually emits.

---

## 11. Known Issues — Resolved

The kit currently has **no open known issues.** Two bugs tracked during the campaign were fixed in **Gate 10 Phase A** (the Mark IV trigger) and **proven live 2026-06-28**:

1. `profiles.full_name` NULL at creation — trigger read the wrong key (`'name'`). Mark IV reads `'full_name'`.
2. Superadmin role-drop (silent privilege bug) — trigger hard-coded `'member'`. Mark IV applies the metadata `role`.

`KNOWN_ISSUES.md` (repo root) retains the full historical record (what was wrong, how it was fixed, the reference 2nd-step role pattern that Mark IV made unnecessary). Consult it before assuming either bug is live — both are closed.

---

## 12. What's NOT In The Kit (Build Yourself)

Project-specific; the service layer (`src/services/`) is for these:

- **Domain data services** (chat, agent profiles, products, orders, etc.)
- **Domain UI screens** (chat interface, mission control, project dashboards)
- **Project Zustand stores** (`use<Feature>Store.ts`)
- **Domain tables + RLS** (anything beyond `profiles` / `user_roles`)
- **External API integrations** (Stripe is reserved-for-payments, kept-not-wired; third-party APIs)
- **Background jobs, cron, webhooks**
- **Email** beyond Supabase auth emails
- **Real-time subscriptions** (Supabase realtime available but not wired)

---

## 13. Quick Reference — "Should I Author This?"

| If you're about to author... | The kit already provides... | Verdict |
|---|---|---|
| `authService.ts` | Complete Supabase SSR auth stack | 🛑 DO NOT BUILD |
| Custom role checker | `useAuthStore` flags + `getUserRole()` | 🛑 DO NOT BUILD |
| Custom session refresh | `src/proxy.ts` + middleware utils | 🛑 DO NOT BUILD |
| App-side superadmin creation | Console-only doctrine — forbidden surface | 🛑 NEVER BUILD |
| User CRUD | Three working portals + `addMember`/`addUser` actions | 🛑 DO NOT BUILD (extend if needed) |
| Login/signup UI | `LoginForm` / `RegisterForm` in `src/components/auth/` | 🛑 DO NOT BUILD |
| Profile form | One shared `ProfileForm` in `components/profile/` | 🛑 DO NOT BUILD |
| App shell layout | `AppShellPage` primitive | 🛑 DO NOT BUILD |
| Mobile slide-over | `Sheet` primitive | 🛑 DO NOT BUILD |
| Sidebar/navbar | `Sidebar`/`AdminSidebar`/`SuperadminSidebar`, `Navbar`/`PublicNav`/`NavbarLoginReg` | 🛑 DO NOT BUILD (extend) |
| Pagination | `PaginationControls` in `common/` | 🛑 DO NOT BUILD |
| Theme toggle | `ThemeToggle` in `global/` | 🛑 DO NOT BUILD |
| Toast notifications | Sonner pre-configured | 🛑 DO NOT BUILD |
| Form with validation | Shadcn `Form` + `react-hook-form` + `zod` | 🛑 DO NOT BUILD wrappers |
| Project chat/data service | Not in kit | ✅ Build in `src/services/` |
| Project data store | Not in kit | ✅ Build in `src/store/` |
| Project UI screens | Not in kit | ✅ Build in `src/app/<group>/` |

---

## 14. Handbook Maintenance

This handbook is a **living document**. Updates happen at three triggers:

1. **After every Factory run / hardening gate** — retrospective surfaces lessons; structural ones land here
2. **When kit baseline changes** — version bumps update relevant sections
3. **When the operator promotes a kit-level change** — accepted Kit Improvement Proposals land here

### Update Discipline

- Mark version bumps at the top with date
- Prefer adding sections over rewriting (preserve doctrine history); reconcile stale *facts* (files, breakpoints, baselines) in place against disk
- Cross-reference Run / Gate lessons in the relevant section
- If something becomes obsolete, mark it as such or move it to history (e.g. `KNOWN_ISSUES.md`) — don't quietly drop it
- **Filename carries the version.** A rewrite bumps the filename (`_v1.0` → `_v1.1`), not just the header

---

## 15. Cross-References

This handbook is the **canonical entry point** for kit knowledge. It cross-references but does NOT duplicate:

- **`agent_docs/APP_FACTORY/AUTH_MANUAL_v1.2.md`** — full auth implementation details (deep dive)
- **`agent_docs/APP_FACTORY/DATABASE_MANUAL.md`** — full DB setup, RLS policy templates
- **`agent_docs/APP_FACTORY/UI-UX-BUILDING-MANUAL_v1_3.md`** — full UI patterns, Rule Zero (mobile-first)
- **`agent_docs/APP_FACTORY/STATE_MANAGEMENT_MANUAL.md`** — Zustand patterns deeper
- **`agent_docs/STARTER_KIT/COMPONENT_REGISTRY_v1.1.md`** — scannable component lookup (sibling file)
- **`KNOWN_ISSUES.md`** (repo root) — historical record of the two now-resolved bugs

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.1 | 2026-06-28 | Kit-Perfection harvest (Gates 1–10). Reconciled to disk: removed the `superadmin-add-user` fossil; user creation documented as `addMember`/`addUser` server actions; Mark IV trigger framed as shipped + proven-live (both KNOWN_ISSUES resolved). AppShellPage `<md`→`<xl` + 4 CP scars + owns-`<main>`; real global components (`PublicNav`/`PublicNavAuthSection`/`PublicMobileNav`/`NavbarLoginReg`, dropped `NavbarHome`/`NavbarSuperadmin`); shared `(account)/profile` + `ProfileForm`; test baseline 81/11 → 76/10. NEW §6 Responsive & Mobile-Nav (xl rail vs lg nav, one-`Sheet`, `coarse:` variant + verify-built-CSS); NEW §11 Known Issues — Resolved. Cookie `getAll`/`setAll` + modernize-mechanism-not-behavior; `.next/types` cache lesson; typing-not-casting; AUTH-WALK; console-only superadmin doctrine; shared-links-match-protection. |
| 1.0 | 2026-05-31 | Initial handbook authored from Run 001 lessons + kit v0.4.1 evidence |

---

🥄 *Part of Stark Industries — App Factory v1.1 doctrine.*
