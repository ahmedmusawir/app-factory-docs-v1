# RECON_WAVE0 — Ground-Truth Pass

> **Mission:** Wave 0 factory recon. Read-only. Filesystem wins over docs.
> **Date:** 2026-07-07 · **Branch:** main · **Method:** evidence-first (path:line + quoted snippets).
> **Scope note:** No files were changed except this report. No commits.

---

## QUESTION 1 — Role-storage security (F-042)

### 1a. `handle_new_user` trigger — where is a new user's role written?

**File:** `supabase/setup.sql` (the only live trigger definition; no `supabase/migrations/` folder exists — `docs/setup.sql` and `docs/migration_add_profiles.sql` are secondary copies).

The role is written to the **`public.user_roles` table** by the trigger, and the value is **read from `user_metadata.role`** ("Mark IV smart trigger"):

```sql
-- supabase/setup.sql:97-110
DECLARE
  assigned_role public.app_role;
BEGIN
  -- Use the metadata role if provided, otherwise default to 'member'
  IF NEW.raw_user_meta_data ->> 'role' IS NOT NULL THEN
    assigned_role := (NEW.raw_user_meta_data ->> 'role')::public.app_role;
  ELSE
    assigned_role := 'member'::public.app_role;
  END IF;

  -- Insert role row (skip if one already exists)
  INSERT INTO public.user_roles (user_id, role)
  VALUES (NEW.id, assigned_role)
  ON CONFLICT (user_id) DO NOTHING;
```

- Authoritative role store: **`public.user_roles` table** (`setup.sql:24-30`), described in-file as _"the source of truth for authorization — NOT user_metadata"_ (`setup.sql:21-22`).
- `profiles` gets only `email` + `full_name` — **no role column** (`setup.sql:50-55`, insert at `113-119`).
- Trigger fires **`AFTER INSERT` only** on `auth.users` (`setup.sql:129-132`) — it does **not** fire on UPDATE.
- **Key exposure:** the assigned role is taken verbatim from client-supplied `raw_user_meta_data ->> 'role'` (`setup.sql:101-102`). `'superadmin'` is a valid enum value (`setup.sql:15`), so the trigger will honor a metadata role of `superadmin` at creation.

### 1b. Grep of `src/` for `updateUser` / `user_metadata` / `app_metadata` / `raw_user_meta_data`

**Non-test production hits:**

| path:line                                                   | Context                                                                                                          |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `src/components/profile/ProfileForm.tsx:45`                 | `user.user_metadata?.full_name` — **read only**, display name fallback                                           |
| `src/components/profile/ProfileForm.tsx:67`                 | `supabase.auth.updateUser({ password })` — **password only, no `data`/role**                                     |
| `src/app/(superadmin)/superadmin-portal/actions.ts:138`     | `user_metadata: { full_name, role }` — inside `addUser`, **server action, admin client**                         |
| `src/app/(superadmin)/superadmin-portal/actions.ts:172-175` | `adminClient.auth.admin.updateUserById(... { user_metadata: { full_name } })` — **admin client**, name-sync only |
| `src/app/(admin)/admin-portal/actions.ts:129-132`           | `adminClient.auth.admin.updateUserById(... { user_metadata: { full_name } })` — **admin client**, name-sync only |
| `src/app/(admin)/admin-portal/actions.ts:185`               | `user_metadata: { full_name, role }` — inside `addUser`, **server action, admin client**                         |

- `app_metadata` / `raw_user_meta_data`: **zero** hits in `src/` (only appears in `supabase/setup.sql` and docs).
- All remaining hits are under `src/__tests__/**` (mocks/assertions), not runtime code.

**Role writes to `user_roles` from app code** are all through the **admin (service-role) client** in server actions:
`superadmin-portal/actions.ts:194` (`editUser`) and `admin-portal/actions.ts:102`. The admin client is server-only (`src/utils/supabase/admin.ts`).

### 1c. Is there a client-reachable path for a user to modify their own role?

**Role reads for authz** come from the **`user_roles` table**, never metadata:

- `src/utils/get-user-role.ts:18-22` — _"canonical source of truth for authorization"_, selects `role` from `user_roles`.
- `src/app/api/auth/login/route.ts:33-37` — resolves role from `user_roles` at login.

**Post-creation (already logged-in user): LOCKED.**

- The only client `updateUser` call is password-only (`ProfileForm.tsx:67`) — no `{ data }` metadata write anywhere in `src/`.
- RLS on `user_roles` grants authenticated users **SELECT on their own row only** (`setup.sql:35-39`); there is **no INSERT/UPDATE policy** for users — writes are service-role only (`setup.sql:41`).
- Even if a user could edit their own `user_metadata`, the trigger is **AFTER INSERT only**, so it would never re-sync into `user_roles`. Metadata role is inert _after_ creation.

**At account creation: a CLIENT-REACHABLE ESCALATION VECTOR EXISTS.**

- The app's own signup route is safe — it hardcodes metadata and never forwards a role:
  ```ts
  // src/app/api/auth/signup/route.ts:6-17
  const { email, password, name } = await req.json(); // note: no `role` destructured
  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: { data: { full_name: name || null } }, // role NOT included
  });
  ```
  `RegisterForm.tsx:75-79` likewise sends only `{ email, password, name }`.
- **But** `supabase.auth.signUp({ options: { data: { role: 'superadmin' } } })` is callable directly from any browser using the public anon key/URL (`NEXT_PUBLIC_*`), bypassing this route entirely. Supabase writes that object into `raw_user_meta_data`, and the Mark IV trigger (`setup.sql:101-102`) then honors it — minting a `superadmin` row in `user_roles` at signup.
- This is a **registration-time privilege escalation**, not a "logged-in user edits own role" path. It is contingent on the Supabase project having **public signups enabled** (cannot be verified from the filesystem, but the presence of the signup route + `RegisterForm` strongly implies it is on).

### 1d. VERDICT

**(B) CLIENT-WRITABLE** — a privilege-escalation path exists, scoped precisely:

- ✅ **Post-creation role changes are LOCKED** (RLS service-role-only; no client metadata write; trigger is INSERT-only).
- ❌ **Creation-time is NOT safe**: the Mark IV trigger trusts client-supplied `user_metadata.role`, and `supabase.auth.signUp` with attacker-chosen `options.data.role` is anon-key reachable from the browser, bypassing the safe API route. An unauthenticated actor can self-register directly as `superadmin`.
- The "metadata roles safe" clause of verdict (A) is therefore **false** as written.
- **Single unverifiable dependency:** whether Supabase Auth "Enable signups" is toggled on. If signups are disabled server-side, the vector collapses to (A). This is the one thing filesystem recon cannot confirm — flagged, not assumed.

---

## QUESTION 2 — Feedback file canon (F-014)

### Evidence

| Candidate                                        | Exists?                                                                                                                                       | Last commit                 |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `STARTER_KIT_FEEDBACK.md` (any casing, any path) | **NO** — not in working tree, not in `git ls-files`, **never added in full history** (`git log --all --diff-filter=A` name search: zero hits) | — (phantom)                 |
| `LESSONS_BIN.md` (repo root)                     | **YES**                                                                                                                                       | `2026-06-28 16:32:10 +0800` |

- No `LESSONS_BIN` **folder** exists — it is a single root-level file, `LESSONS_BIN.md`.

**Content of `LESSONS_BIN.md`** (2 lines): It is a Gate-1→8 running lesson collection for the Starter Kit v3 "Kit Perfection" campaign, and its header banner (`LESSONS_BIN.md:3-9`) records it was **already HARVESTED on 2026-06-28 into `agent_docs/STARTER_KIT/STARTER_KIT_HANDBOOK_v1.1.md`** — i.e. it is retained as a harvest record, its content now folded into the v1.1 handbook.

### Overlap assessment (2 lines)

There is **no overlap to reconcile**: `STARTER_KIT_FEEDBACK.md` does not and never did exist, so `LESSONS_BIN.md` has no competing twin. `LESSONS_BIN.md`'s substance already lives on in `STARTER_KIT_HANDBOOK_v1.1.md`, making the bin a point-in-time harvest log rather than live canon.

**Recommendation:** Treat **`agent_docs/STARTER_KIT/STARTER_KIT_HANDBOOK_v1.1.md` as canonical** doctrine; keep `LESSONS_BIN.md` as the frozen harvest record it already declares itself to be. `STARTER_KIT_FEEDBACK.md` is a **phantom filename** — any doc/ticket referencing it as a real artifact (F-014) should be corrected to point at `LESSONS_BIN.md` / the v1.1 handbook. _(No file action taken — recon only.)_

---

## QUESTION 3 — Handoff v1.1 archaeology (F-032)

### Evidence

- Working tree: only `agent_docs/APP_FACTORY/HANDOFF_PACKAGE_PLAYBOOK.md`, header **`**Version:** 1.0`** (`HANDOFF_PACKAGE_PLAYBOOK.md:6`).
- `git log --all --oneline --follow -- '*HANDOFF*'` → **one commit only**: `1a611c3 "Starter Kit v3 — clean ancestor"`.
- Version string across **every historical blob** of the playbook:
  ```
  1a611c3: **Version:** 1.0
  ```
  (single distinct value — the file has only ever been v1.0).
- Commits touching the file: **`1a611c3` only** (`git log --all --oneline -- .../HANDOFF_PACKAGE_PLAYBOOK.md`).
- Sibling playbooks _do_ carry versioned filenames (e.g. `ENGINEER_PLAYBOOK_v1.1.md`, `SOFTWARE_FACTORY_PLAYBOOK_v1.1.md`, `UI-UX-BUILDING-MANUAL_v1_3.md`), which is likely the source of a false "there must be a Handoff v1.1" expectation — but no `*HANDOFF*v1.1*` file or "Version: 1.1" handoff blob exists anywhere in history.

### VERDICT

**(B) Never existed — phantom reference.** The Handoff Package Playbook has only ever been **v1.0** (born Cyberize Run 001, May 2026). No v1.1 was ever committed, renamed, or drafted in the git history. F-032's "Handoff v1.1" is a phantom.

---

## SURPRISES

1. **🔴 Stale test-suite doctrine directly contradicts the live trigger (security-relevant).**
   `src/__tests__/superadmin/README.md:124-129` asserts the trigger _"does **NOT** read"_ the metadata role and that _"The `role` key in `user_metadata` is currently **vestigial**"_ (repeated at line 241). This is **false against the live `supabase/setup.sql`** (Mark IV), which explicitly honors `raw_user_meta_data ->> 'role'` at INSERT (`setup.sql:101-102`). A maintainer trusting the README would believe metadata role is inert — exactly the false-safety that makes the Q1 signup vector easy to miss. Filesystem (setup.sql) wins; the README is stale.

2. **Two `handle_new_user` copies drift risk.** The trigger is defined in `supabase/setup.sql` **and** `docs/setup.sql` (+ `docs/migration_add_profiles.sql`). No `supabase/migrations/` directory exists, so there is no single migration lineage — the "canonical" trigger is a hand-run SQL file with a docs duplicate that can silently diverge.

3. **`LESSONS_BIN.md` Gate-6 entry already names this exact class of bug.** `LESSONS_BIN.md:39-45` records the doctrine _"superadmins are CONSOLE-ONLY … No app-side superadmin-creation surface should ever exist — it's an attack / privilege-escalation surface"_ and notes a deleted fossil route `/api/auth/superadmin-add-user`. The Q1 signup vector is the same doctrine violated from a different door (direct `signUp` + trusting-trigger), suggesting the "console-only" guarantee is only enforced at the app-UI layer, not at the DB-trigger layer.

4. **Q2 premise was inverted.** The mission framed F-014 as reconciling `STARTER_KIT_FEEDBACK.md` vs `LESSONS_BIN`. In reality only one side exists — `STARTER_KIT_FEEDBACK.md` is a phantom, so there is no "canon war," just a broken reference.

---

_End of Wave 0 recon. No fixes, refactors, or commits performed — findings only._
