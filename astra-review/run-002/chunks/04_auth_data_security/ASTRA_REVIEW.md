# CHUNK 04 — AUTH / DATA / SECURITY REVIEW

## 1. STATUS

COMPLETE — all three assigned primary manuals examined in full. The review contains 17 ranked defects (4 BLOCKER, 7 HIGH, 6 MEDIUM, 0 LOW) and 3 ranked suggestions. All twelve required sections, five integer scores, strengths, evidence fields, and coverage entries are complete. Branch verified before examination and at completion as `factory-docs-review-astra-w-chunks` on 2026-09-13.

Written incrementally only to `astra-review/run-002/chunks/04_auth_data_security/ASTRA_REVIEW.md`. Workspace file-metadata comparison against the pre-write baseline found this report to be the only changed file; the tracked working-tree diff is empty. No Factory doctrine or other file was modified. No commit, push, branch change, Chunk 05 work, disposition, or synthesis was performed. Review stops here.

## 2. SCOPE

Objective: determine whether the current Factory doctrine for identity, authority, persistence, tenancy, and data security is technically sound and internally consistent.

Before substantive examination, all seven current Markdown files in `04_REFERENCE_MANUALS/` were discovered and classified from their opening metadata and headings:

| File | Principal subject | Chunk 04 classification |
|---|---|---|
| `AUTH_MANUAL.md` | Authentication, identity, authorization, privileged user administration | PRIMARY — full examination |
| `DATABASE_MANUAL.md` | Schema, database persistence, RLS, mutation and integrity | PRIMARY — full examination |
| `STATE_MANAGEMENT_MANUAL.md` | Client state, persistence, hydration, server/client authority | PRIMARY — full examination; includes its embedded commerce-shaped examples as evidence about state doctrine |
| `APP_ARCHITECTURE_MANUAL.md` | General application structure, routing, rendering, components | Not primary; security/authority excerpts may be consulted for an explicit dependency |
| `API_AND_SERVICES_MANUAL.md` | API/service integration | Not primary; Chunk 05 territory, except a necessary explicit security/authority/data dependency check |
| `ECOMMERCE_AND_PAYMENTS_MANUAL.md` | One-time payments, checkout, orders | Not primary; Chunk 05 territory |
| `STRIPE_SUBSCRIPTIONS_PLAYBOOK.md` | Recurring billing | Not primary; Chunk 05 territory |

Exact primary set: `04_REFERENCE_MANUALS/AUTH_MANUAL.md`, `04_REFERENCE_MANUALS/DATABASE_MANUAL.md`, and `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md`.

Controls read: the full `astra-review/run-002/packets/CHUNK_REVIEW_CONTRACT.md` and only the Chunk 04 entry of `astra-review/run-002/packets/EXECUTION_PLAN.md`. Supporting references are restricted to other current doctrine needed to verify an explicit security, authority, or data dependency. Excluded: Run 001 review material, Fable/Sol reviews, dispositions, synthesis artifacts, other chunk review files, doctrine changes, implementation, commits, pushes, and Chunk 05 execution. Prior conversation is not evidence for findings; findings must be grounded in the sources examined for this chunk.

## 3. DOMAIN MODEL

The intended identity authority is the Supabase-authenticated user resolved on the server. Authorization derives from `public.user_roles`, through the kit's role helper and database policies; profile data is not a second role authority. Creation-time role metadata is an exception for transport through an authorized admin operation and the creation trigger, not an authorization-read source. Superadmin creation is console-only. Current examples conflict with those boundaries (C04-D01–D03).

User-scoped server/browser clients operate under RLS. Elevated service-role capability bypasses RLS and therefore needs its own authorized operation boundary. Layout guards admit page rendering and supply `{ user, role }` for identity-dependent UI under the Navbar Law. Client stores react to browser events and hold interaction state; they do not establish identity or privilege. Several executable examples instead use old metadata, client gating, or incompatible helper contracts.

Database doctrine starts with an explicit schema, distinguishes relational constraints from logical external relationships, enables RLS for user data, and separates own-record, privileged, and deliberately public access patterns. Database mutations carry persistence/integrity responsibilities; client caches and stores are working copies. Local persistence is selected with `partialize`, hydrated before dependent UI, and reset at relevant lifecycle boundaries. The written examples do not consistently enforce these responsibilities.

The examined sources define user ownership and global role examples. They do not establish an organization/tenant membership model or decide that every project is single-tenant. Tenant scope, privileged cross-tenant reach, and shared-cache privacy consequently remain AMBIGUOUS; no tenant policy was invented for this review.

## 4. FIVE-DIMENSION SCORECARD

These scores apply only to the assigned Chunk 04 doctrine.

| Dimension | Score | Evidence-based justification |
|---|---:|---|
| Correctness | 2 | Sound table-role and RLS principles coexist with unsafe signup/privilege paths, unsafe policy composition, and broken state/pagination recipes (C04-D01–D03, D06, D12–D17). |
| Consistency | 2 | Metadata vs. table roles, layout vs. operation authorization, contradictory cookie flags, guard signatures, and client vs. server identity cannot all be followed together (D01–D08). |
| Completeness | 3 | Auth flows, schema/RLS, integrity, browser persistence, and verification principles are broadly covered. Material failure/recovery and account-transition details remain missing; tenancy and adversarial evidence expectations are insufficiently determined (D10–D12, D16; S01–S03). |
| Executability | 2 | A competent implementer must repair canonical examples or infer undocumented prerequisites: role helper/guard mismatch, wrong admin client, stuck hydration, conditional hooks, incomplete rollback, and skipped cursor rows (D05, D07, D10, D12–D13, D17). |
| Maintainability | 2 | New hard rules were appended while older full recipes and summaries remained active. Duplicate auth/store/schema recipes now encode different contracts; explicit cross-links expose rather than resolve drift (D01, D04–D05, D07–D08). |

## 5. WHAT IS STRONG

1. **One authoritative role table, separate from profiles.** AUTH “Where Roles Live” and DATABASE §2/§5 explicitly reject authorization from user metadata and role-bearing profile mirrors. This prevents writable display data from becoming privilege. Preserve the single-role-authority principle and narrow, independently authorized creation-time transport exception while repairing contradictory examples.
2. **Server-resolved identity on the first render.** AUTH's Navbar Law and STATE §1 Division of Labor specify `{ user, role }` props and an invariant test for the first role-appropriate render. This names the latency/race mechanism and supplies an observable guarantee. Preserve the server-props contract and browser-event/store distinction; bring older recipes into compliance.
3. **Database enforcement of user ownership.** DATABASE §5 requires RLS on user data and shows own-record read/write predicates and table-based role checks. This places controls below the UI and ordinary request handlers. Preserve default-deny ownership, explicit public access decisions, and role-table lookup while correcting composition and capability selection.
4. **Schema and relational integrity are first-class inputs.** DATABASE §§1–4 distinguish schema-first production work from the discovery/UI exception, specify keys/constraints, and explicitly document logical relationships where an external system prevents a real foreign key. This exposes ownership and integrity assumptions before mutation code is written. Preserve that explicit modeling and the requirement to verify actual kit schema rather than reconstruct it from an illustrative table.
5. **Small stores with selective persistence and derived selectors.** STATE §§1–4 and §9 separate local, shared-client, and server state; keep transient loading/validation/payment state out of persistence; and compute derived values in selectors. These choices reduce stale duplicated state and unnecessary retained data. Preserve them while fixing nested mutation, freshness, and reset behavior.
6. **Behavioral evidence beyond a green build.** AUTH's Navbar invariant and its explicit kit dependency's AUTH-WALK require actual identity/session transitions; the handbook §§1–3 also requires live database application/verification and admin/member checks. This recognizes that compilation cannot prove cookies, deployed DDL, or role behavior. Preserve these checks and extend their negative cases without replacing them with build-only evidence.

## 6. PRIORITY FINDINGS

1. **C04-D03 — BLOCKER:** public signup transports caller metadata into the described role-creation trigger without an enforced trust distinction.
2. **C04-D01 — BLOCKER:** privileged recipes use forbidden metadata authority and recreate role stores/application superadmin creation.
3. **C04-D02 — BLOCKER:** layout admission is treated as authorization for an independently invocable privileged action.
4. **C04-D06 — BLOCKER:** the soft-delete policy is inactive without enablement and can widen visibility when composed as an ordinary access grant.
5. **C04-D05 — HIGH:** the manuals confuse user-scoped and elevated clients in both directions, making a simple credential replacement unsafe.

## 7. RANKED DEFECTS

Rank follows severity, then operational impact; IDs retain their original assignment. Counts: **17 defects — 4 BLOCKER, 7 HIGH, 6 MEDIUM, 0 LOW.**

### C04-D03 — Public signup forwards caller-controlled role transport into the authority-creation path

- **Classification:** DEFECT
- **Severity:** BLOCKER
- **Affected files / locations:** `AUTH_MANUAL.md`, signup API lines 547–596, registration flow, and “Where Roles Live,” lines 978–988; `DATABASE_MANUAL.md` §2, lines 153–156.
- **Evidence:** the public signup endpoint destructures `user_metadata` from the request and forwards it unchanged to `auth.signUp`. The role doctrine permits creation-time role metadata only through a protected admin channel. The cited handbook §§1–2 says public signup creates a member, while the trigger fires on every auth-user insert and reads `raw_user_meta_data.role`, defaulting only when absent. AUTH mentions a hardening ticket but supplies no enforced prerequisite or safe public-path replacement.
- **Why this is a defect:** the documented public path does not enforce the distinction on which the role-transport exception depends. A caller can supply the same role key the described trigger promotes into the authoritative table. A later table lookup cannot undo an untrusted role assignment at creation.
- **Operational consequence:** the combined documented endpoint/trigger behavior permits elevated role seeding through public registration. This is a finding about current written doctrine; actual installed trigger hardening is UNKNOWN and no live exploit was attempted.
- **Recommended resolution:** enforce public-signup member assignment at a trusted boundary independent of submitted metadata; restrict accepted profile fields; separately authorize privileged creation and role assignment. Verify the direct provider-signup path as well as the app endpoint. Make the hardening requirement discoverable and mandatory before promotion rather than relying on an unspecified ticket.

### C04-D01 — Privileged examples still authorize from user metadata and recreate competing role stores

- **Classification:** DEFECT
- **Severity:** BLOCKER
- **Affected files / locations:** `AUTH_MANUAL.md`, “Role-Based Access Control / Where Roles Live,” §§12–14, and Summary; `DATABASE_MANUAL.md` §2, Roles Table and User Mirror patterns.
- **Evidence:** AUTH lines 978–988 forbid authorization from `user_metadata`; DATABASE lines 138–156 forbid both metadata authorization and a role column on a profile mirror. AUTH §12 nevertheless checks `requester.user_metadata.is_qr_superadmin` for create/delete/list operations, lets the caller request a new superadmin, and checks the deletion target's metadata for protection. §13 adds an owner-updatable `app_users.role` column, and the Summary says roles are stored in metadata. These privileged recipes are not covered by the narrower legacy/display-hint advisory in the client-store section. The explicit supporting dependency `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §§1–2 confirms table-based roles and console-only superadmin creation.
- **Why this is a defect:** the same active manual supplies incompatible sources of privilege and an application-side creation surface forbidden by its current doctrine. Moving metadata into another writable profile column also recreates the two-authority problem. A legacy advisory for display-only snippets does not make server authorization from metadata safe.
- **Operational consequence:** authors can implement privilege checks or elevated-role creation from caller-influenced attributes. The shown admin recipes also use the wrong client (to be examined separately); this review does not claim those exact snippets currently complete privileged calls or that a deployed system was exploited.
- **Recommended resolution:** remove or quarantine the unsafe privileged recipes; authorize the current requester and protected target using the canonical role table, allow only approved target roles, preserve console-only superadmin creation, and keep profile mirrors free of authorization columns. Align the summary and HOC guidance with the same authority model.

### C04-D02 — Layout admission is presented as authorization for privileged server actions

- **Classification:** DEFECT
- **Severity:** BLOCKER
- **Affected file / location:** `AUTH_MANUAL.md`, “User creation — server actions,” lines 638–652; “Security Best Practices,” lines 1514–1581.
- **Evidence:** the action recipe says the route-group layout gates access and only then the action invokes a service-role client. Its documented authorization boundary is the layout, with no independent caller/role check in `addMember` or `addUser`. The same manual requires roles to be checked on every request. `STARTER_KIT_HANDBOOK.md` §1 repeats the layout-then-admin-client dependency.
- **Why this is a defect:** authorization to render a page is not evidence that a later independently invoked mutation is authorized. A privileged action must check its own invocation, including current caller and permitted target role. The recipe leaves that security control outside the operation it is supposed to guard.
- **Operational consequence:** implementing the documented boundary alone leaves a direct or replayed privileged action invocation without its own authorization check, including after the caller's role changes.
- **Recommended resolution:** require authentication, current role resolution, allowed-operation/target checks, and input validation inside every privileged action before acquiring/using elevated capability. Keep layout guards for page access, but do not rely on them as the mutation boundary. Require negative direct-invocation tests. Actual application action implementations were not inspected.

### C04-D06 — Soft-delete policy is an access grant, not an exclusion that composes safely

- **Classification:** DEFECT
- **Severity:** BLOCKER
- **Affected file / locations:** `DATABASE_MANUAL.md` §2, Soft Delete Pattern, lines 243–264; §5, own-record and admin policies, lines 390–450.
- **Evidence:** the soft-delete recipe creates `resources` and a plain SELECT policy `USING (is_deleted = FALSE)` under the claim “RLS policy excludes deleted records.” It does not enable RLS on that table. The separate RLS section requires enablement and teaches owner/admin access policies. Plain permissive SELECT policies combine as alternatives: applying the active-record recipe alongside an owner policy yields `is_owner OR is_active`, not `is_owner AND is_active`.
- **Why this is a defect:** following the self-contained recipe leaves its policy inactive; adding the stated RLS prerequisite still does not make the policy a general exclusion. When reused on owner-scoped data, an active row belonging to somebody else passes the active-record grant, while a deleted own row passes the ownership grant. A partial index does not enforce visibility.
- **Operational consequence:** soft-deleted data remains visible, or composing the advertised patterns grants cross-user reads. No installed policy set or live data was examined; the cross-user consequence is conditional on composing the patterns on a private table.
- **Recommended resolution:** explicitly enable RLS and specify whether the resource is public or private. Place the active predicate inside each intended visibility condition, or use a correctly scoped restrictive policy alongside the necessary access grants. Demonstrate anonymous, other-owner, deleted-own, and privileged cases against the composed policy set.

### C04-D05 — Client capability guidance both underpowers admin calls and overgeneralizes RLS bypass

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `AUTH_MANUAL.md` §§12–13; `DATABASE_MANUAL.md` §5, Service Role Bypass, lines 453–468. Supporting references: `STARTER_KIT_HANDBOOK.md` §§1–3; `API_AND_SERVICES_MANUAL.md` §6, lines 738–998.
- **Evidence:** AUTH imports the cookie/user-scoped server client and invokes `auth.admin.createUser`, `deleteUser`, and `listUsers` with it. The handbook distinguishes that anon-key session client from the service-role admin client. Conversely, DATABASE lists “API routes” generally as an appropriate reason to bypass RLS. The handbook reserves elevation for admin surfaces; the API manual's explicitly related Supabase service pattern uses the session client for ordinary profile GET/PATCH operations.
- **Why this is a defect:** execution on a server does not establish either privileged credentials or permission to bypass caller-scoped policies. The examples reverse both sides of this capability boundary. This remains independently broken after the metadata authorization defect is corrected.
- **Operational consequence:** privileged identity operations fail for lack of capability, or ordinary user routes lose their RLS boundary when an author applies the database advice. A credential swap alone would activate the unsafe checks in C04-D01.
- **Recommended resolution:** make capability selection depend on the authorized operation: session client for caller identity and ordinary RLS-bound data; isolated admin client only after independent authorization of elevated work. Reconcile both manuals and explicitly prohibit service-role substitution as a general API-route fix. The supporting API excerpt was checked only for this boundary.

### C04-D10 — Multi-step persistence recipes leave compensation failures unrecoverable

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `AUTH_MANUAL.md` §§12–13, especially lines 1826–1833 and 1977–2040; `DATABASE_MANUAL.md` §11, Pseudo-Transaction, lines 1044–1085.
- **Evidence:** the database recipe commits an order, inserts related rows, and on failure attempts a delete without inspecting its result. AUTH's synchronized creation likewise ignores failure of the compensating auth-user deletion; synchronized deletion logs a profile deletion failure and continues, or can remove a profile before auth deletion fails. The shown mirror schema has no auth-user foreign key to complete cleanup automatically. §12 even returns creation success without checking the optional mirror insert result.
- **Why this is a defect:** calling the database example a pseudo-transaction correctly admits non-atomicity, but does not handle failed compensation or interruption between steps. The advertised synchronization/rollback paths can leave a partial result with no durable reconciliation state, retry owner, or accurate completion contract.
- **Operational consequence:** accounts without expected profiles, orphaned personal data, and parent records missing their required children can persist after a reported failure or apparent success. Retrying from scratch can compound the inconsistent state.
- **Recommended resolution:** use an atomic database operation for invariants contained in one database; for cross-boundary work, define idempotency, compensation-result handling, durable recovery ownership, and reconciliation. Distinguish completed, failed, and partially completed outcomes. This is a persistence finding, not an examination of commerce fulfillment.

### C04-D11 — Persisted personal data has no enforceable account-transition lifecycle

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `STATE_MANAGEMENT_MANUAL.md` §4 Persistence, §6 Form/Checkout Store lines 938–1053, §8 Auth Store, and §9 checklist; `AUTH_MANUAL.md` Security Best Practices, sensitive browser-storage prohibition and logout flow.
- **Evidence:** STATE persists email, billing/shipping names, full addresses, and phone in the global `checkout-storage` localStorage key. Its auth-store logout clears only that store's user flags. The closing checklist says reset stores “when appropriate (logout, order complete),” but specifies no binding to logout/account switch, user scope, retention limit, or failure behavior. The storage cleanup example inspects only `cart-storage`, using a timestamp its shown cart templates do not write. AUTH advises against sensitive localStorage data without reconciling this personal-data recipe.
- **Why this is a defect:** indefinite origin-wide personal-data persistence and an optional reset reminder do not define an account boundary. The supplied pieces allow account B in the same browser to hydrate account A's contact/address data after A logs out. This does not require a remote attacker or an XSS assumption.
- **Operational consequence:** personal details can be shown or reused under the wrong account, and sign-out gives no reliable cleanup guarantee. Whether an application has added a coordinator is UNKNOWN.
- **Recommended resolution:** decide which personal fields may persist, for how long, and under what user/guest scope; require a coordinated reset/invalidation on sign-out and account transition, including failure cases. Reconcile the auth storage rule with the selected UX policy. Avoid retaining raw contact data by default where the benefit does not justify it.

### C04-D08 — Active client recipes still claim route and identity authority

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files / locations:** `AUTH_MANUAL.md`, Navbar Law; Common Patterns 2 and 5; §14 HOC Route Protection, lines 2070–2199. `STATE_MANAGEMENT_MANUAL.md` §1 Division of Labor and §8 Auth Store Pattern.
- **Evidence:** AUTH requires identity-dependent rendering from server props and authorizes the admin layout with `["admin"]`. Later, its Navbar fetches identity after mount and §14 says to protect layouts with a client HOC reading persisted role flags; its admin example accepts member as well as admin. STATE repeats the server-props rule but supplies a persisted identity/role store and `selectIsAdmin` that implicitly includes superadmin, despite AUTH's explicit-role allow-list model. The HOC also leaves `isAuthorized` true when a later missing user/role triggers a redirect.
- **Why this is a defect:** the later recipes present client snapshots and presentation checks as the route/identity mechanism the newer rule forbids. Their acceptance sets differ from the server examples. They lack a scoped advisory restricting them to non-authoritative browser-event state; the earlier legacy note does not cover these later recommendations.
- **Operational consequence:** implementers recreate stale or empty identity UI, inconsistent role admission, and a client-only access screen that cannot authorize server data. Independently secured endpoints may still deny requests; this is not evidence that an installed endpoint leaks data. C04-D02 covers a separate invocation boundary: even a correct server layout does not authorize its actions.
- **Recommended resolution:** withdraw the client-only route-protection recipe, use the verified server guard and server identity props, and restrict stores to explicit session-event reactions and interaction state. Make each permitted role set explicit; define any display helper as a display helper. Preserve operation-local authorization independently.

### C04-D07 — The canonical route-guard recipe cannot satisfy its documented callers

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected file / locations:** `AUTH_MANUAL.md`, protectPage, lines 789–824; Navbar Law, lines 906–926. Supporting `STARTER_KIT_HANDBOOK.md` §2, role-resolution signature.
- **Evidence:** `protectPage` calls `getUserRole(user)` without awaiting it, tests the result against allowed roles, and returns `user`. The handbook specifies asynchronous `await getUserRole()` with no argument. The Navbar Law instead requires the same guard to return `{ user, role }`, and its caller destructures that object. The recipe also imports `AppRole` from the role-resolution module, whereas the handbook names the separate app-role module.
- **Why this is a defect:** these are incompatible call and return contracts for the same named guard. Following the documented async resolver makes the unawaited role unsuitable for the allow-list check; following the displayed guard return leaves the Navbar caller without its required fields. This is a concrete execution failure even when the authority source is correctly chosen.
- **Operational consequence:** protected routes deny valid users or fail integration/type checks, and the server-resolved shell cannot obtain the identity props the doctrine requires.
- **Recommended resolution:** verify the shipped helper exports, publish one async guard signature and return shape, and make every usage match it. Preserve deny-by-default behavior and the server-resolved role; do not repair this by accepting a client-provided role. Actual kit implementation was not inspected.

### C04-D04 — Cookie guidance directly contradicts the required kit session model

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected file / locations:** `AUTH_MANUAL.md`, Cookie Configuration lines 1035–1045 and Security Best Practices lines 1540–1544; supporting `STARTER_KIT_HANDBOOK.md` §1, line 70.
- **Evidence:** AUTH specifies `httpOnly: true` and repeats it as a security best practice. Its browser client also needs session access. The explicitly paired kit handbook says `httpOnly: false` is deliberate for client-side session access, is preserved in the cookie adapter, and must not be tightened.
- **Why this is a defect:** two governing instructions require opposite values for the same kit session architecture. The manual does not distinguish a browser-accessible Supabase session from a separately designed server-only session architecture.
- **Operational consequence:** an author can break session synchronization by applying the manual's security checklist, or disregard it without an explicit reconciled rule.
- **Recommended resolution:** document the actual cookie/session architecture and its tradeoff, reconcile the pair, and require the relevant login/refresh/logout verification. Do not change a cookie flag independently of the browser/server session design.

### C04-D09 — Email confirmation accepts an unbounded external redirect destination

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected file / location:** `AUTH_MANUAL.md`, GET /api/auth/confirm, lines 600–633.
- **Evidence:** the route reads `next` directly from the query and, after successful OTP verification, redirects to `new URL(next, request.url)`. There is no same-origin or allowed-path check. An absolute URL or a network-path URL such as `//outside.example/path` resolves away from the application.
- **Why this is a defect:** providing a base URL resolves relative input; it does not constrain absolute or network-path destinations. An authentication completion endpoint consequently trusts caller-controlled navigation across an origin boundary.
- **Operational consequence:** a valid confirmation flow can deliver the user from the trusted application to an attacker-selected site, supporting phishing. Successful OTP verification is a prerequisite; this review does not claim session cookies or the OTP are automatically disclosed to that destination.
- **Recommended resolution:** allow approved local destinations, normalize and verify the resolved origin/path, and fall back safely when invalid. Cover absolute, network-path, malformed, and valid local destinations in the confirmation contract.

### C04-D16 — Logout reports success without checking the sign-out result

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file / locations:** `AUTH_MANUAL.md`, POST /api/auth/logout, lines 519–542; Security Best Practices, lines 1577–1580.
- **Evidence:** the endpoint awaits `supabase.auth.signOut()` but discards its result, then unconditionally returns HTTP 200 and “Logged out successfully.” The same manual says not to ignore authentication errors. Other auth examples explicitly inspect the SDK's returned error field.
- **Why this is a defect:** awaiting completion does not establish successful sign-out when failure is returned as data. The route has no truthful failure result or recovery behavior.
- **Operational consequence:** callers can show completed logout while the required sign-out effect has not been established. Whether a particular provider failure leaves local cookies or remote sessions active depends on the failure and installed SDK; the report does not assume every error retains both.
- **Recommended resolution:** inspect and classify the result, define local cleanup and revocation expectations, return an accurate outcome, and provide retry/recovery behavior. Verify failed sign-out as well as the happy-path logout bounce. This is distinct from clearing other stores' personal data in C04-D11.

### C04-D17 — Timestamp-only pagination silently skips tied records

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file / location:** `DATABASE_MANUAL.md` §12, Pagination Patterns, lines 1101–1117.
- **Evidence:** the cursor query orders solely by `created_at`, filters with `.lt('created_at', lastCreatedAt)`, and limits to 20. The documented timestamp columns are not unique. If 21 rows share a timestamp, page one takes 20 and page two excludes the remaining row together with the already-read rows.
- **Why this is a defect:** a nonunique timestamp cannot identify a unique boundary in the result order. This produces an incomplete traversal even for a static dataset, independently of concurrent writes.
- **Operational consequence:** listings or batch consumers using the supplied recipe omit valid records without an error.
- **Recommended resolution:** use a stable unique tie-breaker in both the order and cursor predicate, preserve the same filter/authorization scope across pages, and verify ties at the page boundary.

### C04-D13 — The alternative hydration hook changes hook invocation count

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file / location:** `STATE_MANAGEMENT_MANUAL.md` §5, Alternative: Suspense-Style Loading, lines 724–740.
- **Evidence:** `useHydratedStore` calls the bound store hook for `hasHydrated`, returns early while false, then calls that hook a second time for the selector only when true. Its comment says it throws a promise, but the function actually returns null.
- **Why this is a defect:** the hydration transition changes the React hook call sequence; the loading strategy violates the invariant it needs to run. Merely repairing readiness transitions in C04-D12 does not repair this separate hook-order error.
- **Operational consequence:** components following the alternative recipe can fail when hydration completes instead of displaying the persisted state; a Suspense boundary will not handle the returned null as suspension.
- **Recommended resolution:** make both subscriptions unconditional and gate only their returned data/rendering, or document and implement an actual supported suspension strategy. Match the explanation to the behavior.

### C04-D12 — Persistence readiness can become permanently false after reset or failure

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file / locations:** `STATE_MANAGEMENT_MANUAL.md` §5, lines 632–721; §6 Persisted Store, lines 802–842, and Form/Checkout Store, lines 995–1049.
- **Evidence:** the UI waits for `hasHydrated`; both templates initialize it false and implement `reset: () => set(initialState)`. Only the storage rehydration callback sets it true. Resetting an already hydrated store does not initiate another storage load. The documented error callback logs an error but never establishes a terminal failed/recovered state.
- **Why this is a defect:** business-data reset incorrectly resets storage readiness, leaving no shown transition back to a usable state. Storage failure likewise leaves the loading gate unresolved.
- **Operational consequence:** a normal reset after logout or completion, or a storage failure, leaves gated UI showing a skeleton/spinner indefinitely during that store lifetime.
- **Recommended resolution:** separate storage readiness from business data; preserve readiness on a normal reset and define an explicit terminal error/recovery path for failed hydration. Verify reset after hydration and invalid/unavailable storage.

### C04-D15 — A nonempty client store permanently overrides new server data

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file / locations:** `STATE_MANAGEMENT_MANUAL.md` §1 server-state ownership table; §7 Store + Server Components, lines 1156–1200; §9 freshness checklist.
- **Evidence:** the page fetches products on the server and passes them to `ProductList`. The client initializes the global product store only if `products.length === 0` and renders solely from that store. Subsequent server props are ignored whenever old products remain, including a new empty result. The manual assigns product lists to server state and says not to retain server state that should be fetched fresh.
- **Why this is a defect:** emptiness is used as a freshness/initialization signal with no invalidation or dataset identity. A completed server refresh therefore need not update what the user sees.
- **Operational consequence:** removed or changed records remain displayed after new server data arrives. The sample is a public catalog; this finding does not infer private-data exposure from it.
- **Recommended resolution:** render authoritative server props directly where possible. If a client working copy is needed, define scope, version, refresh, and reconciliation with local edits explicitly, including transitions to an empty dataset.

### C04-D14 — Composite-item update mutates the previous state snapshot

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file / locations:** `STATE_MANAGEMENT_MANUAL.md` §3, Composite Key Pattern, lines 389–400, and Immutable Update Pattern, lines 422–447.
- **Evidence:** the composite-item example copies only `state.items`, then increments `newItems[existingIndex].quantity`. The existing item object is shared with the prior array. The immediately following rule requires immutable updates unless Immer middleware is installed; this recipe establishes no such middleware.
- **Why this is a defect:** a shallow array copy does not copy its item objects. The example modifies the old state and preserves the changed item's reference, directly contradicting the declared update contract.
- **Operational consequence:** item-object selectors can miss a change and previous snapshots or memoized calculations become unreliable.
- **Recommended resolution:** copy the changed item as well as the container, using the manual's existing map-and-spread pattern; alternatively make an explicit Immer-backed variant. Preserve composite identity without changing prior snapshots.

## 8. RANKED SUGGESTIONS

### C04-S01 — Define a small adversarial authorization evidence matrix

- **Classification:** SUGGESTION
- **Evidence / opportunity:** AUTH's security checklist, DATABASE §5, and the supporting handbook's AUTH-WALK/admin-plus-member requirement provide useful verification, but the examined sources do not specify a reusable negative matrix.
- **Expected value:** add actor × operation × resource cases for anonymous access, another user's row, forbidden role changes, public metadata injection, direct privileged-action calls, role revocation, deleted rows, and failed sign-out. For projects with tenants, add cross-tenant actors and membership changes. Record the expected denial and evidence at the real server/database boundary. This strengthens valid existing testing practices; it does not substitute for correcting the specific defects above.

### C04-S02 — Require an explicit tenancy and administrative-reach decision

- **Classification:** SUGGESTION
- **Evidence / opportunity:** the primary manuals establish user-owned records and a global admin-all-rows example but do not say whether a project is single-tenant, user-isolated, or organization-based. No organization membership schema was established by the reviewed evidence.
- **Expected value:** document the project's selected isolation model, authoritative membership source, scope of each admin role, and who may move a resource between scopes before adapting the RLS templates. A recorded single-tenant decision is sufficient where applicable. This avoids silently treating a user ID as a tenant boundary or a tenant admin as a platform admin without asserting that an unexamined project requires tenancy.

### C04-S03 — Label cache privacy and invalidation scope alongside caching recipes

- **Classification:** SUGGESTION
- **Evidence / opportunity:** DATABASE §12 caches `events` in module-global variables and suggests memory or localStorage for static data. The example does not establish whether those rows are public or principal-filtered. STATE already distinguishes backend truth from a client working copy.
- **Expected value:** identify allowed data classification, cache lifetime, user/tenant key where required, mutation invalidation, and sign-out behavior for each reusable cache pattern. Keep a shared cache only for data explicitly safe to share. The example's actual data visibility and deployment lifetime are UNKNOWN, so this is not a claim of an existing leak.

## 9. CROSS-DOMAIN DEPENDENCIES

| Classification | Dependency / bounded evidence | Handoff |
|---|---|---|
| DEPENDENCY | AUTH/DATABASE explicitly depend on `STARTER_KIT_HANDBOOK.md` §§1–3 for client capabilities, role helper, trigger/profile ownership, and deployed RLS. | Reconcile the exact consulted contracts implicated by D03–D05 and D07; verify actual kit/database state in the domain that owns it. No kit source or live instance was examined. |
| DEPENDENCY | DATABASE's service-role advice affects API/service callers. Only `API_AND_SERVICES_MANUAL.md` §6 was opened to establish its ordinary user-scoped Supabase pattern. | C04-D05 identifies a confirmed local capability conflict. General endpoint validation, API contracts, and commerce behavior remain for their assigned review; Chunk 05 was not begun. |
| CONTRADICTION CANDIDATE | The handbook's consulted §1 still recommends store-based client email rendering and says the guard returns a user, while AUTH/STATE's newer Navbar rules require server props and `{ user, role }`. | The in-scope inconsistencies are established in D07–D08. Broader kit-consumption authority and propagation need their own domain examination; do not infer a global precedence rule here. |
| DEPENDENCY | STATE explicitly ties its three-layer model to service-layer ownership. Its server-to-store and persistence examples influence UI and data consumers. | D11–D15 concern data lifetime and state execution only; frontend architecture and commerce policy were not reviewed. |
| SYNTHESIS FLAG | Tenant isolation and administrative reach require a project/product decision not supplied by the three primary manuals (S02). | Determine where that decision is owned and evidenced across domains; no organization model or Factory-wide applicability verdict is supplied here. |
| SYNTHESIS FLAG | A repeated maintenance pattern leaves new hard rules beside incompatible recipes and summaries. | D01, D04–D05, and D07–D08 warrant eventual consideration of canonical-example ownership and synchronization. This chunk does not prescribe a Factory-wide process or perform that synthesis. |

## 10. AMBIGUITIES / UNKNOWNS

- **Actual role hardening — UNKNOWN.** No installed trigger, grants, action source, service credentials, or live policy set was inspected. The documented role-transport chain is unsafe as written; a referenced hardening ticket is not evidence of the installed control.
- **Deployed helper and session implementation — UNKNOWN.** Opposing return types, helper imports, and cookie flags were surfaced rather than silently resolved using assumed kit code. Version-specific provider defaults and request-entry behavior were not independently certified.
- **Tenant applicability and role reach — AMBIGUOUS.** No tenant/member-to-organization relation or explicit single-tenant decision was established. A global-role example does not prove that all projects intentionally permit cross-tenant administration.
- **Privacy/retention decisions — AMBIGUOUS.** The manuals do not reconcile persisted addresses/auth snapshots, shared caches, account changes, and retention. A coordinator may exist in an application; none was evidenced here.
- **Negative-test ownership and runtime evidence — UNKNOWN.** The sources provide useful behavioral checks but no complete adversarial evidence matrix for the reviewed boundaries. This review did not inspect another chunk's testing assessment or claim tests ran against a deployed kit.
- **Boundary exclusions:** the narrower legacy client snippet warning was respected; metadata snippets explicitly restricted to display hints were not independently counted as exploits. A missing explicit UPDATE `WITH CHECK` was not treated as an automatic RLS bypass. Explicit public-read/authenticated-insert product policies were not labeled wrong merely because a different product might require tighter roles. The pseudo-transaction label was respected; D10 concerns incomplete recovery, not a claim that it promises true atomicity.
- **Validation limits:** five in-memory Node assertions reproduced source-level mechanisms for external URL resolution, shallow-copy mutation, reset readiness, ignored server updates, and tied-timestamp pagination. Remaining findings were checked by direct source/contract comparison and static control-flow reasoning. No framework, Supabase SDK, database, deployed app, or external documentation was used as runtime evidence.

## 11. COVERAGE MANIFEST

| Assigned primary file | Status |
|---|---|
| `04_REFERENCE_MANUALS/AUTH_MANUAL.md` | EXAMINED — all 2,248 logical lines |
| `04_REFERENCE_MANUALS/DATABASE_MANUAL.md` | EXAMINED — all 1,240 logical lines |
| `04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md` | EXAMINED — all 1,564 logical lines |

Supporting consultations (initial classification used opening 15 lines and headings; any subsequent substantive excerpt is explicitly bounded below):

- CROSS-REFERENCE — `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`: principal-subject classification.
- CROSS-REFERENCE — `04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md`: principal-subject classification, then bounded §6 Supabase Service Pattern (lines 738–998, through the next heading) to verify the explicit database service-role/client-capability dependency. Ordinary profile services and routes use the session client. No general API/commerce review performed.
- CROSS-REFERENCE — `04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md`: principal-subject classification; one-time commerce territory excluded.
- CROSS-REFERENCE — `04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md`: principal-subject classification; recurring-commerce territory excluded.

- CROSS-REFERENCE — `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`: explicit AUTH/DATABASE dependency; targeted security/authority heading search and §§1–3 (lines 49–250), plus the proxy/middleware note (lines 421–427), read to verify client privilege boundaries, role-creation transport, current role lookup, cookie ownership, RLS expectations, and session-entry naming. Not a full handbook review.

Applicable AGENTS.md existence checks found no instruction files.

## 12. SYNTHESIS HANDOFF

- **Strongest conclusion:** the assigned domain contains valuable modern authority rules, but its active recipes cannot be followed together safely. This is a Chunk 04 conclusion, not a Factory-wide verdict.
- **Most serious defect:** C04-D03 joins an unfiltered public input to the described authority-creation trigger; C04-D01 and D02 independently undermine privileged-operation boundaries. Actual installed hardening remains unverified.
- **Most important strength to preserve:** one server/database role authority, coupled with server-resolved identity props and evidence of real session/database behavior.
- **Unresolved issue most likely to affect another domain:** the kit's deployed trigger/action/client contracts and the project's tenant/admin scope; their implementation and ownership cannot be established from these manuals alone.
- **Findings deserving eventual Factory-wide consideration:** D01–D08 for authority/example synchronization, D10–D11 for mutation recovery and personal-data lifecycle, and S01–S03 for explicit security evidence and scope decisions. These are bounded handoff candidates only; no synthesis, disposition, or doctrine repair was performed.
