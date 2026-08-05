# DOCTRINE PROMOTION PACK — 2026-08-04 — "The Navbar Saga"

> **STATUS: ENCODED** — Landed in the Hub via PR #8 (branch `docs/navbar-saga-2026-08-05`,
> rebase-and-merge, 2026-08-05). Docs shipped: QA_PLAYBOOK v0.1, BUG_FIX_PLAYBOOK v0.1,
> STATE_MANAGEMENT_MANUAL v1.2, FRONTEND_BUILD_PHASE_PLAYBOOK v1.2.2, AUTH_MANUAL v1.4.
> Splits parked (NOT in PR #8): Entry 3 → `stark-frontend-first` skill repo (ANTI_PATTERNS.md);
> pack instruction #3 (`fixed inset-0` grep) → kit verification-cluster.
> This file is retained in `_AUDIT/` as the run's source record.

> **Origin:** Staging nav bug (empty menu + full-screen spinner), root-caused and fixed on
> `navbar-fix-1`, verified rock-solid on staging (Gate D passed). Lessons promoted per
> retro ritual: verified fix → doctrine, written where the next engineer will actually obey it.
> **Contains:** 4 surgical entries. Claudy lands each into its target file EXACTLY as written
> (surgical additions — no overwrites), bumps each file's version history, reports diffs.
> Operator commits. These then join the central trickle-up queue (with Gate-M split +
> commit-checkpoint gate) for the kit/central doc-stack merge.

---

## ENTRY 1 of 4 — AUTH_MANUAL.md

**Placement:** New `##` section immediately AFTER `## Server-Side Protection (RBAC)`.
**Also:** add a row to `## Version History` — `Server-Resolved Identity for UI section added (navbar race, 2026-08-04)`.

```markdown
## Server-Resolved Identity for UI (The Navbar Law)

**Identity and authorization state that UI renders from is server-resolved and passed
down as props. UI is never gated on client-resolved identity.**

If a component's render output depends on WHO the user is (nav links, role-gated
buttons, portal chrome), the answer must arrive WITH the component — resolved by the
server layout's route guard and passed as props — not fetched after mount.

### ❌ WRONG — client-resolved identity (the navbar race)

```tsx
"use client";
const [user, setUser] = useState<SupabaseUser | null>(null);   // null window
useEffect(() => {
  supabase.auth.getUser().then(({ data }) => setUser(data.user)); // network race
}, []);
const navLinks = user ? [...] : [];   // renders EMPTY during the window
```

Failure mechanism: every mount opens a `null` window while a network round-trip
resolves. Zero-latency dev masks it; deployed latency makes it visible and "random."
A failed call renders logged-out UI to an authenticated user. This shipped, broke
staging, and was invisible in dev — see BUG_FIX_PLAYBOOK (mechanism-naming) and the
2026-08-04 fix.

### ✅ CORRECT — server-resolved, props down

```tsx
// layout.tsx (SERVER component) — the guard already knows the answer
const { user, role } = await protectPage([AppRole.ADMIN]);
return <AuthedShell user={user} role={role}>{children}</AuthedShell>;

// Navbar — born holding the card; no fetch, no window, no race
const Navbar = ({ user, role }: { user: SupabaseUser; role: AppRole }) => {
  const navLinks = buildLinks(role);   // unconditional — structurally never empty
  ...
};
```

`protectPage` returns `{ user, role }` — it already computed both to guard the route;
returning them costs zero queries. The same server check that admits the user writes
the user's menu: one source, one moment, correct in the first server-rendered paint.

### Rules

1. Route guards return what they resolve (`{ user, role }`) — never compute-and-discard.
2. Client stores (Zustand) may REACT to session events (`onAuthStateChange` sign-out)
   and own interaction state — they are never the SOURCE of identity for rendering.
   (See STATE_MANAGEMENT_MANUAL §1 — Division of Labor.)
3. Persisted client role state goes stale by design (written at login, survives in
   localStorage). Any consumer treating it as truth inherits the race. (KIP-2.)
4. Invariant-test the guarantee: an authed shell component must render its full
   role-appropriate link set on FIRST render, synchronously (see Navbar.invariant).
```

---

## ENTRY 2 of 4 — STATE_MANAGEMENT_MANUAL.md

**Placement A:** Append to `## 1. Philosophy & Strategy` as a closing subsection.
**Placement B:** Add one line under `## Cross-References (Factory Doctrine)`:
`- AUTH_MANUAL — "Server-Resolved Identity for UI (The Navbar Law)": identity renders from server props, never from client stores.`
**Also:** Version History row.

```markdown
### Division of Labor: Server Props vs. Client Stores (HARD RULE)

**The server tells the UI who you are; the store helps the UI react to what you do.**

| Concern | Source | Why |
|---|---|---|
| Identity & role for RENDERING (nav links, role-gated UI, portal chrome) | Server-resolved by the route guard, passed as props | No client fetch window → no race, no empty state, no dev/deploy divergence. Re-verified server-side on every navigation. |
| Session EVENT reactions (sign-out in another tab), interaction state, UI state, in-memory domain state | Client store (Zustand) | Lives and changes in the browser during use — that is what a client store is for. |

Persisted auth state (e.g. a `role` written only at login into localStorage) is a
SNAPSHOT, not truth: it goes stale across browsers/devices/cleared storage. Rendering
from it produces "random" partial-UI bugs that dev latency hides (see AUTH_MANUAL —
The Navbar Law; origin: 2026-08-04 staging nav bug).
```

---

## ENTRY 3 of 4 — ANTI_PATTERNS.md (stark-frontend-first skill)

**Placement:** New group `## UI / Navigation Anti-Patterns` inserted BEFORE `## Process Anti-Patterns`. Two entries, matching house format.

```markdown
## UI / Navigation Anti-Patterns

### Global Navigation Overlays

```tsx
// ❌ WRONG — full-screen overlay mounted at root, covers the shell
// (v0.4.1 "Disappearing Navbar" — REBUILT and re-killed 2026-08-04)
<div className="fixed inset-0 z-40 bg-background/70 backdrop-blur-sm">
  <Spinner />
</div>   // mounted in root layout.tsx, triggered on every nav click

// ✅ CORRECT — route-scoped loading.tsx INSIDE the page directory
// src/app/owedbook/loading.tsx — only page CONTENT spins;
// navbar + sidebar stay mounted, always.
export default function Loading() { return <SpinnerLarge />; }
```

> **HARD GATE — this recurred (kit v0.4.1 → Cyber Pharma, rebuilt under new names
> `NavigationSpinner`/`useNavSpinner`).** A lesson archived in a changelog is not a
> gate. The shell (navbar/sidebar) never unmounts and is never covered.
> **Greppable enforcement:** verification-cluster greps must include
> `fixed inset-0` in any layout/nav/global component → FAIL. Loading states live in
> `loading.tsx` inside the page dir, nowhere else.

### Gating UI on Client-Resolved Identity

```tsx
// ❌ WRONG — component fetches "who am I" after mount, renders empty meanwhile
const [user, setUser] = useState(null);
useEffect(() => { supabase.auth.getUser().then(...) }, []);
const navLinks = user ? [...] : [];   // the race window

// ✅ CORRECT — server layout's guard resolves it, props carry it down
const { user, role } = await protectPage([...]);   // layout.tsx (server)
<Navbar user={user} role={role} />                  // born knowing
```

> Client stores are not identity sources either — persisted role state is a stale
> snapshot (written at login only). Full law: AUTH_MANUAL "Server-Resolved Identity
> for UI (The Navbar Law)". Invariant-test the guarantee (never-empty on first render).
```

---

## ENTRY 4 of 4 — FRONTEND_BUILD_PHASE_PLAYBOOK.md

**Placement:** In the final stage's completion checklist / stop condition (the phase-close
verification section — Claudy locates the exact checklist), append these lines.
**Also:** Version History row + version bump per filename-carries-version rule.

```markdown
- [ ] **Gate Q — Pre-Deployment Quality Gate** passed per `QA_PLAYBOOK.md` §9
      (includes production-mode verify: `npm run build && npm start` walk — dev mode
      hides latency-class and build-class bugs).
- [ ] **Gate D — Deployed-Environment Verification** passed per `QA_PLAYBOOK.md` §10:
      the smoke walk runs ON the deployed URL against the RECORDED deployed revision.
      A deploy without a passed Gate D is not done.
- [ ] Any bug fixed during this phase: mechanism named in the commit (never "small
      fix") and regression protection added, per `BUG_FIX_PLAYBOOK.md` Rules 3 & 6.
```

*(Note: Gate Q/D content lives ONLY in QA_PLAYBOOK.md — this playbook points, never
duplicates. Duplicated doctrine is how the v0.4.1 lesson died in a changelog.)*

---

## LANDING INSTRUCTIONS (for Claudy)

1. Read each target file's section structure first (recon), then land each entry as a
   surgical addition at the stated placement. NO overwrites, NO reflowing of
   surrounding content.
2. Bump each file's version history with a one-line entry citing origin
   `navbar identity race + overlay recurrence, 2026-08-04`. Apply
   filename-carries-version where the filename encodes it.
3. Add the `fixed inset-0` grep to the verification-cluster gating greps (wherever
   the C5-style grep list lives) — layout/nav/global components only.
4. Report all diffs. STOP. Operator reviews and commits (git law).
5. Flag for the central trickle-up queue: these 4 entries + QA_PLAYBOOK + 
   BUG_FIX_PLAYBOOK join the Gate-M split and commit-checkpoint gate for the
   kit/central-stack merge session (diff-and-merge, never overwrite).

🥄
