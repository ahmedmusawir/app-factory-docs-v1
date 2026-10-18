# 04 — Auth / Data / State / Security — Correction Brief

> **DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC**

- **Package:** Factory Doctrine Correction Package 001. Index: `FACTORY_DOCTRINE_CORRECTION_INDEX_001.md`.
- **Prepared by:** Claudy (documentation Engineer seat), 2026-10-11. This is not a QA product and certifies nothing.
- **Primary entries:** FC-033 … FC-049 (17), the certified register §5.D. **Contains 3 BLOCKERs: FC-033, FC-034, FC-036.**
- **Authority:** every outcome is **PROPOSED** for Jarvis (Architect) review and Tony (Director) approval. Nothing here is approved policy.
- **Nature:** these are documentation findings about recipes and rules in the Factory manuals. Astra and Sol both bound them: no deployed application, installed trigger or live policy was examined, and none is claimed exploitable. No replacement doctrine text is written.

## Pinned sources

| Ref | Revision | Path |
|---|---|---|
| Certified register / QA | `c6210c3` = `c6210c32480558b343a27726a26822e8d959d0f7` | `astra-review/run-002/synthesis/PART1_FINDINGS_DISPOSITION.md`, `astra-review/run-002/synthesis/QA/PART1_CONVERGENCE_QA.md` |
| Astra chunk 04 / Sol chunk 04 | `c6210c3` | `astra-review/run-002/chunks/04_auth_data_security/ASTRA_REVIEW.md`, `astra-review/run-002/chunks/04_auth_data_security/SOL_REVIEW.md` |
| Fable (blind) | `39a1c6114d72b22d3550d7ff65234ec0f01418f6` (`origin/factory-docs-review-fable-001`) | `fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md` |
| Review baseline | `0a787cb` = `0a787cb826118b4a010765d60e41a449df3ce746` | defect surfaces named per entry |
| Current main | `9c17939` = `9c179392f79b70da099121fc357d3107ad3bb86e` | every surface in this brief is blob-identical to `0a787cb` (QA-4) |

Route codes are as in the index. Short manual names resolve under `04_REFERENCE_MANUALS/` unless a full path is given.

**Domain preservation (Astra C04 §5; Sol C04 §9; applies to every entry below):**
- one authoritative role table, kept separate from profiles, with only the narrow, independently authorized creation-time transport exception
- server-resolved identity on first render (Navbar Law, `{ user, role }` props, the invariant test)
- RLS-enforced user ownership with explicit public-access decisions
- schema-first modeling
- small stores with selective persistence
- behavioral evidence beyond a green build (AUTH-WALK, live DB verification)

Sol C04 §9: corrections must remove stale examples, summaries and helper signatures that contradict the newer rule. Patching one snippet in isolation is not a correction.

---

## CF-06 — Auth / authorization / session authority (FC-033, 034, 035, 036, 038, 041, 042, 043, 044 here)

### FC-033 — AUTH_MANUAL privileged recipes authorize from `user_metadata`, recreate competing role stores and supply an app-side superadmin-creation surface
- **Certified record:** CF-06 · Severity BLOCKER · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D01 · Fable FBL-D001 (primary; also related to FC-001 and FC-035)
- **Evidence:**
  - Astra C04 §7 C04-D01.
  - Sol C04 §3: "Valid BLOCKER… preserve the single-authority model rather than patch individual snippets independently."
  - Fable §7 FBL-D001, §9 rows 1–3 and 5, §11 decision 1.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: Key Principle 5, "Where Roles Live", §12 SuperAdmin routes, §13 mirror table with a `role` column, Summary, registration flow (`is_qr_*` defaults)
  - `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §2 (Roles Table, User Mirror)
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §§1–2
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`: §2 (`authServices.ts` in the standard layout), §10 (middleware reads `user.user_metadata?.role`)
  - Grep gates that should catch this: `02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md` Q3.4, `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` §3.8
- **Defect:**
  - The kit auth authority's own privileged recipes:
    - check `requester.user_metadata.is_qr_superadmin`;
    - create superadmins from the app;
    - add a `role` column to a mirror table.
  - Its Summary says roles live in metadata.
  - APP_ARCHITECTURE adds a forbidden wrapper and metadata-based middleware.
  - All of this contradicts "Where Roles Live", DATABASE §2 and STARTER_KIT §§1–2. The legacy advisory does not cover these recipes.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** every live recipe uses one role authority, the role table, so that:
  - no privileged check reads `user_metadata`;
  - no app-side superadmin-creation surface exists (creation stays console-only);
  - no profile mirror carries an authorization column;
  - the AUTH Summary states the same model;
  - APP_ARCHITECTURE §2 does not list an auth wrapper, and §10 does not authorize from metadata.

  **Two separate things are proposed:**
  - **(1) Retire the unsafe existing routes. This is required.** The current AUTH §12 `add-user` / `delete-user` / `get-users` recipes authorize from `user_metadata` and include app-side superadmin creation. They are removed, quarantined as labeled LEGACY history, or rewritten (DEC-02).
  - **(2) No blanket prohibition on future authorized operations.** Privileged list or delete operations (other than superadmin creation) stay permissible doctrine when they:
    - authorize the current requester through the trusted role authority (the role table);
    - perform operation-local authorization (DEC-04 / FC-036);
    - use the correct elevated client only after that check (FC-038);
    - allow only approved target roles;
    - protect privileged targets.

  Superadmin creation stays console-only in every case.
- **Preserve:**
  - The domain preservation list above.
  - Console-only superadmin creation.
  - Trusted (role-table) authorization.
  - Legitimate, properly authorized administrative list/delete capability.
  - Sol C01 §5.A: keep FC-001 (governance) and this record separate.
  - The existing `_ARCHIVE/` discipline if quarantine-to-archive is chosen.
- **Likely affected docs / consumers:** AUTH_MANUAL, DATABASE_MANUAL §2, STARTER_KIT_HANDBOOK §§1–2, APP_ARCHITECTURE §2/§10, MANIFEST row; FC-001, FC-034, FC-035, FC-036, FC-038, FC-039, FC-041; RECON Q3.4 and TESTING §3.8 as verification consumers.
- **Verification intent:**
  - A live-corpus grep for metadata authorization (`is_qr_superadmin`, `user_metadata?.role`, `user_metadata.is_`) leaves zero undispositioned hits; any survivor is a labeled display hint or transport case.
  - The existing metadata-authorized §12 routes no longer appear as live patterns (removed, LEGACY-quarantined or rewritten).
  - No app-side superadmin-creation route is presented as a pattern.
  - Any privileged list or delete pattern that remains (or is added) shows:
    - role-table authorization of the requester;
    - operation-local checks before the elevated client is used;
    - an approved-target-role allow-list;
    - protection of privileged targets.
  - No recipe adds `role` to a profile mirror.
  - APP_ARCHITECTURE §2 has no `authServices.ts`.
  - The RECON Q3.4 grep gate passes when run against the doctrine itself.
- **Open decision:** DEC-02, retire/archive vs rewrite (Fable §11 decision 1). Rewriting needs disk verification of the kit (`protectPage` return shape, `useAuthStore`, cookie flag), and that kit repository is outside this package (GAP).
  - **Recommendation: containment first, then correction.** Remove or quarantine the unsafe routes with a pointer to the governing rule early; rewrite or replace against the verified kit afterwards.
  - **Containment ≠ correction.** Quarantining §12 contains the risk but does **not** close FC-033 while any other listed surface still contradicts the single role authority: the Summary, the §13 mirror `role` column, APP_ARCHITECTURE §2/§10 and the registration-flow metadata. FC-033 is corrected only when every outcome bullet has landed and its verification intent passes.
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

### FC-034 — Public signup forwards caller-controlled role metadata into the role-creation trigger path
- **Certified record:** CF-06 · Severity BLOCKER · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D03 · Fable none as primary
- **Evidence:** Astra C04 §7 C04-D03; Sol C04 §3 ("The doctrine defect is valid and severe enough to remain BLOCKER"; installed trigger state UNKNOWN).
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: signup API, registration flow, "Where Roles Live"
  - `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §2 (role trigger reads `raw_user_meta_data.role`)
  - Supporting: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §§1–2 (public signup creates a member)
- **Defect:** the public signup endpoint forwards the request's `user_metadata` unchanged to `auth.signUp`. The described trigger reads `raw_user_meta_data.role` on every auth-user insert, and no trusted boundary forces a member role for public signup.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Public signup assigns the member role at a trusted boundary, independent of submitted metadata, with an allow-list of accepted profile fields.
  - Privileged creation and role assignment are separately authorized.
  - Both the app endpoint and the direct provider-signup path are covered.
  - Trigger hardening is a stated mandatory prerequisite before promotion, not "a ticket".
- **Preserve:** creation-time role transport only through a protected admin channel; table-based roles; console-only superadmin.
- **Likely affected docs / consumers:** AUTH signup and registration flow; DATABASE §2 trigger description; STARTER_KIT §§1–2; negative cases in TESTING/QA (FC-063 pattern).
- **Verification intent:**
  - No recipe forwards caller `user_metadata` wholesale into `signUp`.
  - The trigger description ignores or denies role keys arriving from the public path.
  - The doctrine states a negative case: public signup carrying `role=admin` results in a member.
- **Open decision:** trigger-side vs endpoint-side enforcement (both recommended; Jarvis).
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

### FC-035 — Active client-side recipes claim route and identity authority (HOC, post-mount Navbar, persisted auth store)
- **Certified record:** CF-06 · Severity HIGH · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D08 · Fable FBL-D001 (related; primary in FC-033)
- **Severity divergence (recorded):** Astra HIGH vs Fable BLOCKER (whole multi-surface finding). The certified HIGH stands.
- **Evidence:** Astra C04 §7 C04-D08; Sol C04 §4; Fable §7 FBL-D001, §9 row 6.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: Navbar Law, Common Patterns 2 and 5, §14 HOC Route Protection
  - `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md`: §1 (Division of Labor; table row "Zustand … route protection"), §8 Auth Store
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md` §4 (`'use client'` AdminLayout)
- **Defect:**
  - The `withRoleCheck` HOC gates layouts client-side on persisted role flags and admits `member` to an admin layout.
  - The later Navbar fetches identity after mount.
  - STATE persists `user.role` and exports `selectIsAdmin`, which implicitly includes superadmin.
  - `isAuthorized` stays true on redirect.
  - All of this contradicts Navbar Law and STATE's own Division of Labor.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Client-only route-protection recipes are withdrawn; route and identity authority comes from the verified server guard and server identity props.
  - Stores are limited to session-event reactions and interaction state: non-persisted for authority and never authoritative.
  - Every role set is explicit; any display helper is labeled display-only.
- **Preserve:**
  - Navbar Law, STATE Division of Labor and the first-render invariant test.
  - Operation-local authorization, kept independent (FC-036).
- **Likely affected docs / consumers:** AUTH, STATE §1/§8, APP_ARCHITECTURE §4; FC-041 (guard contract), FC-040 (store persistence), FC-001.
- **Verification intent:**
  - No recipe gates a layout client-side on a persisted role.
  - The STATE §1 table no longer assigns route protection to Zustand.
  - `selectIsAdmin` is absent or labeled display-only.
  - APP_ARCHITECTURE §4 uses the server guard.
- **Open decision:** DEC-02 (paired with FC-033).
- **Proposed route:** `SYNC`. Wave 1, paired with FC-033.

### FC-036 — Layout admission is presented as the authorization boundary for privileged server actions
- **Certified record:** CF-06 · Severity BLOCKER · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D02 · Fable none
- **Evidence:** Astra C04 §7 C04-D02; Sol C04 §3 (severity left to disposition); certified closure to BLOCKER on 2026-09-27; Sol C05 §7.A (the repeated "operation-local authorization" seam).
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: "User creation — server actions", "Security Best Practices"
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §1 (repeats layout-then-admin-client)
- **Defect:** the server-action recipe treats the route-group layout gate as the authorization for `addMember` / `addUser`, which then use a service-role client with no caller or role check of their own.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Before acquiring or using elevated capability, every privileged server action:
    - authenticates;
    - resolves the current role;
    - checks the allowed operation and target;
    - validates input.
  - Layout guards remain page-access controls only.
  - Negative direct-invocation tests are required.
- **Preserve:** layout guards for page access; isolation of the service-role client.
- **Likely affected docs / consumers:** AUTH server actions and best practices; STARTER_KIT §1; FC-038, FC-057 (API sync GET), FC-050.
- **Verification intent:**
  - The `addMember`/`addUser` recipes contain operation-local checks that run before the admin client.
  - STARTER_KIT §1 no longer presents layout-then-admin-client as sufficient.
  - A direct-invocation negative case is documented.
- **Open decision:** DEC-04. Adopt "every privileged operation authorizes its own invocation" as a Factory-wide invariant (Sol C05 §7.A candidate; Jarvis/Tony).
- **Proposed route:** `SYNC`. **Wave 1 BLOCKER.**

### FC-038 — Client-capability guidance both underpowers admin calls and overgeneralizes RLS bypass
- **Certified record:** CF-06 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D05 · Fable none
- **Evidence:** Astra C04 §7 C04-D05; Sol C04 §4 ("one consistent capability-selection rule").
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md` §§12–13 (`auth.admin.*` called with the session client)
  - `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §5 Service Role Bypass ("API routes")
  - Supporting: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §§1–3, `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md` §6
- **Defect:** the session-vs-admin capability boundary is reversed on both sides. Admin operations use the anon-key session client, while DATABASE lists "API routes" in general as a reason to bypass RLS.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** one capability-selection rule:
  - the session client for caller identity and RLS-bound data;
  - an isolated admin client only after independent authorization of elevated work.
  "API routes" is not a general bypass reason, and service-role substitution is prohibited as a general fix.
- **Preserve:** the handbook's client distinction; the API §6 session-client profile pattern.
- **Likely affected docs / consumers:** AUTH, DATABASE §5, STARTER_KIT, API §6; FC-033, FC-036.
- **Verification intent:**
  - The DATABASE §5 bypass list no longer contains generic "API routes".
  - Every `auth.admin.*` call in recipes uses the admin client after an operation-local check.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

### FC-041 — The canonical `protectPage` recipe's call and return contract is incompatible with its documented callers
- **Certified record:** CF-06 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D07 · Fable none
- **Evidence:** Astra C04 §7 C04-D07; Sol C04 §4.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: `protectPage`, Navbar Law
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §2 (`getUserRole` signature, `AppRole` module)
- **Defect:** `protectPage` calls `getUserRole(user)` without `await` and returns `user`. The handbook specifies an async, no-argument `getUserRole()`, Navbar Law destructures `{ user, role }`, and the `AppRole` import source differs.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One async guard signature and return shape, verified against the shipped kit exports, is used by the recipe, Navbar Law and the handbook.
  - The `AppRole` import source is correct.
  - The guard denies by default and uses only the server-resolved role.
- **Preserve:** deny-by-default; never accept a client-provided role.
- **Likely affected docs / consumers:** AUTH, STARTER_KIT §2; FC-035.
- **Verification intent:**
  - Every `protectPage` and `getUserRole` occurrence in live docs shares one signature.
  - Navbar Law's destructuring matches the return shape.
  - The kit verification evidence is cited with its repository and revision.
- **Open decision:** DEC-09, kit disk verification. The kit repository is outside this package (`XB-EXT`; GAP).
- **Proposed route:** `SYNC` (+ `XB-EXT` verification).

### FC-042 — Cookie `httpOnly` guidance contradicts the kit session model
- **Certified record:** CF-06 · Severity HIGH · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D04 · Fable FBL-D030 (primary)
- **Severity divergence (recorded):** Astra HIGH vs Fable MEDIUM. The certified HIGH stands.
- **Evidence:** Astra C04 §7 C04-D04; Sol C04 §4 ("should not be solved by selecting the more 'secure sounding' option in isolation"); Fable §7 FBL-D030, §9 row 7, §11 decision 2.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: Cookie Configuration, Security Best Practices DO 6, `src/middleware.ts` example
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §1 (`httpOnly: false` deliberate)
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md` §10 (flags `proxy.ts`)
- **Defect:**
  - AUTH requires `httpOnly: true`; the Handbook says `httpOnly: false` is deliberate for client-side session access and must not be tightened.
  - AUTH also shows `src/middleware.ts` where the kit ships `src/proxy.ts`.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The cookie/session architecture is documented once, in STARTER_KIT §1 per Fable, together with its tradeoff, and AUTH points to it.
  - The flag value follows the verified session design.
  - Login, refresh and logout verification is required.
  - AUTH notes `proxy.ts`.
- **Preserve:** the handbook's live-session-bug warning; AUTH-WALK.
- **Likely affected docs / consumers:** AUTH, STARTER_KIT §1, APP_ARCHITECTURE §10; FC-005 (precedence).
- **Verification intent:**
  - No live doc instructs a cookie flag contrary to the documented session architecture.
  - AUTH references that ruling.
  - Middleware/proxy naming is consistent.
- **Open decision:** DEC-09, the `httpOnly` ruling after kit disk verification (Tony; the kit repository is external).
- **Proposed route:** `SYNC` (+ `XB-EXT` verification).

### FC-043 — Email confirmation route accepts an unbounded external redirect destination
- **Certified record:** CF-06 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D09 · Fable none
- **Evidence:** Astra C04 §7 C04-D09; Sol C04 §4 (redirect/phishing risk only; no claim of credential disclosure).
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/AUTH_MANUAL.md`, GET `/api/auth/confirm`.
- **Defect:** the route redirects to `new URL(next, request.url)` with `next` taken from the query, with no same-origin or allowed-path check. Absolute and network-path URLs therefore leave the application.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The confirmation redirect is restricted to approved local destinations; the resolved origin and path are normalized and verified, with a safe fallback.
  - The contract covers absolute, network-path, malformed and valid local cases.
- **Preserve:** the confirmation flow itself.
- **Likely affected docs / consumers:** AUTH confirm route; any recipe reusing a `next` parameter.
- **Verification intent:** the documented cases show `https://outside.example` and `//outside.example/path` rejected, a valid local path accepted, and a stated fallback.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

### FC-044 — Logout reports success without checking the sign-out result
- **Certified record:** CF-06 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D16 · Fable none
- **Evidence:** Astra C04 §7 C04-D16; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/AUTH_MANUAL.md`, POST `/api/auth/logout` and Security Best Practices.
- **Defect:** the endpoint discards the `signOut()` result and always returns 200 "Logged out successfully", contrary to the manual's own "don't ignore auth errors" rule.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the logout recipe inspects and classifies the sign-out result, defines local cleanup and revocation expectations, returns an accurate outcome and provides retry or recovery.
- **Preserve:** the happy-path logout bounce verification.
- **Likely affected docs / consumers:** AUTH logout; FC-040 (store cleanup on logout).
- **Verification intent:** the recipe branches on the returned error, does not return success on failure, and the doctrine includes a failed-sign-out check.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

## CF-07 — Data / RLS / state correctness and privacy (FC-037, 039, 040, 045, 046, 047, 048, 049 here; FC-068 and FC-069 are in brief 05)

### FC-037 — Soft-delete RLS policy is an access grant, not a safely composing exclusion
- **Certified record:** CF-07 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D06 · Fable none
- **Evidence:** Astra C04 §7 C04-D06; Sol C04 §3 (HIGH by default; BLOCKER where used to protect private or restricted data). Certified closure: HIGH, 2026-09-27.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §2 Soft Delete Pattern; §5 own-record and admin policies.
- **Defect:** the soft-delete recipe adds a permissive `USING (is_deleted = FALSE)` SELECT policy without enabling RLS. Composed with owner policies, permissive grants combine with OR, which can widen visibility.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The recipe enables RLS explicitly and states whether the resource is public or private.
  - The active-record predicate sits inside each intended visibility condition, or in a correctly scoped restrictive policy.
  - Composed behavior is shown for anonymous, other-owner, deleted-own and privileged cases.
- **Preserve:** default-deny ownership, explicit public-access decisions and role-table lookup.
- **Likely affected docs / consumers:** DATABASE §2/§5.
- **Verification intent:**
  - The recipe contains RLS enablement.
  - No standalone permissive active-record SELECT policy is presented as an exclusion.
  - The case table shows the intended result for all four cases.
- **Open decision:** none. Sol's conditional BLOCKER for private data is noted; any re-elevation is Tony's (DEC-22).
- **Proposed route:** `SYNC`.

### FC-039 — Multi-step persistence recipes leave compensation failures unrecoverable
- **Certified record:** CF-07 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D10 · Fable none
- **Evidence:** Astra C04 §7 C04-D10; Sol C04 §4 (distinguish complete success, recoverable failure, partial completion, failed compensation and reconciliation ownership).
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §11 Pseudo-Transaction
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md` §§12–13 (synchronized create/delete)
- **Defect:** the pseudo-transaction and the synchronized create/delete paths ignore compensation or deletion results, or continue after partial failure. There is no reconciliation state and no recovery owner.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Invariants inside one database use an atomic operation.
  - Cross-boundary work defines idempotency, checked compensation results, a durable recovery owner and reconciliation.
  - Outcomes distinguish completed, failed and partially completed.
- **Preserve:** the honest "pseudo-transaction" label; explicit relational modeling.
- **Likely affected docs / consumers:** DATABASE §11; AUTH §§12–13 (scope shrinks if DEC-02 retires those recipes under FC-033); FC-020, FC-052 (the same recovery theme).
- **Verification intent:**
  - Recipes inspect compensation results.
  - A partial-completion state is named and its recovery owner stated.
- **Open decision:** none beyond DEC-02's effect on scope.
- **Proposed route:** `SYNC`.

### FC-040 — Persisted personal data has no enforceable account-transition lifecycle
- **Certified record:** CF-07 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D11 · Fable none as primary
- **Evidence:** Astra C04 §7 C04-D11; Sol C04 §4.
- **Defect surfaces (`0a787cb`):**
  - `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md`: §4 Persistence, §6 Form/Checkout Store, §8 Auth Store, §9 checklist
  - `04_REFERENCE_MANUALS/AUTH_MANUAL.md`: Security Best Practices (sensitive browser storage), logout flow
- **Defect:** STATE persists email, names, addresses and phone in origin-wide `checkout-storage`. Logout clears only the auth-store flags, and the reset guidance is optional ("when appropriate"), so account B can hydrate account A's personal data.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Doctrine decides which personal fields may persist, for how long and under which user or guest scope.
  - Sign-out and account transition trigger a coordinated reset and invalidation, including failure cases.
  - AUTH's storage rule and STATE's recipe agree.
  - Raw contact data is not retained by default without justification.
- **Preserve:** selective persistence; transient payment state kept out of persistence.
- **Likely affected docs / consumers:** STATE, AUTH; FC-044 (logout result), FC-047 (reset readiness), FC-068 (checkout store shape).
- **Verification intent:**
  - Documented walkthrough: user A signs out, user B signs in on the same browser, and the recipe yields none of A's data.
  - The reset is bound to logout, not left as an option.
- **Open decision:** DEC-15, the persisted personal-data retention policy (Tony).
- **Proposed route:** `SYNC`.

### FC-045 — Timestamp-only cursor pagination silently skips tied records
- **Certified record:** CF-07 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D17 · Fable none
- **Evidence:** Astra C04 §7 C04-D17; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` §12 Pagination Patterns.
- **Defect:** the cursor orders and filters on the non-unique `created_at` alone (`.lt`, limit 20), so rows tied at a page boundary are skipped.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the cursor uses a stable unique tie-breaker in both the order and the cursor predicate, and keeps the same filter and authorization scope across pages.
- **Preserve:** the pagination pattern's purpose.
- **Likely affected docs / consumers:** DATABASE §12; list and batch consumers.
- **Verification intent:** the documented case of 21 rows sharing one timestamp traverses every row exactly once.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

### FC-046 — Alternative hydration hook changes the hook invocation count
- **Certified record:** CF-07 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D13 · Fable none
- **Evidence:** Astra C04 §7 C04-D13; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` §5, "Alternative: Suspense-Style Loading".
- **Defect:** `useHydratedStore` returns early while unhydrated, then calls the store hook a second time. Its comment claims it throws a promise, but the code returns null.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** both subscriptions are unconditional and only the returned data is gated, or a real supported suspension strategy is documented. The explanation matches the behavior.
- **Preserve:** the hydration-gating intent.
- **Likely affected docs / consumers:** STATE §5; FC-047.
- **Verification intent:** the recipe's hook call sequence is identical before and after hydration, and the comments match the code.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

### FC-047 — Persistence readiness can become permanently false after a reset or storage failure
- **Certified record:** CF-07 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D12 · Fable none
- **Evidence:** Astra C04 §7 C04-D12; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` §5; §6 Persisted Store and Form/Checkout Store.
- **Defect:** `reset: () => set(initialState)` resets `hasHydrated` to false, and only rehydration sets it true again. The error callback never reaches a terminal state, so gated UI can hang.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** storage readiness is separated from business data, a normal reset preserves readiness, and failed hydration has an explicit terminal error and recovery path.
- **Preserve:** the readiness gate itself.
- **Likely affected docs / consumers:** STATE §5/§6; FC-040 (reset on logout).
- **Verification intent:** the documented checks cover reset-after-hydration and unavailable or invalid storage, and neither leaves the gate unresolved.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

### FC-048 — A nonempty client store permanently overrides new server data
- **Certified record:** CF-07 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D15 · Fable none
- **Evidence:** Astra C04 §7 C04-D15; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` §1 (server-state ownership table), §7 Store + Server Components, §9 freshness checklist.
- **Defect:** `ProductList` initializes the store only when it is empty and renders from the store, so later server props, including an empty result, are ignored.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** authoritative server props render directly where possible. Where a client working copy is needed, its scope, version, refresh and reconciliation with local edits are defined, including the transition to an empty dataset.
- **Preserve:** the manual's rule that product lists are server state.
- **Likely affected docs / consumers:** STATE §1/§7/§9.
- **Verification intent:** the documented refresh case shows removed records disappearing and an empty result rendering as empty.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

### FC-049 — Composite-item update mutates the previous state snapshot
- **Certified record:** CF-07 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C04-D14 · Fable none
- **Evidence:** Astra C04 §7 C04-D14; Sol C04 §5.
- **Defect surfaces (`0a787cb`):** `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` §3 Composite Key Pattern; Immutable Update Pattern.
- **Defect:** the example shallow-copies the array and then mutates `newItems[i].quantity` in place, contradicting the manual's own immutable-update rule.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the example copies the changed item as well as the container, using the manual's existing map-and-spread pattern, or is an explicit Immer-backed variant.
- **Preserve:** composite identity; the immutable-update rule.
- **Likely affected docs / consumers:** STATE §3.
- **Verification intent:** the recipe leaves the prior state's item object unchanged.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

---

*End of brief 04. Primary entries: 17 (FC-033 … FC-049). DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC.*
