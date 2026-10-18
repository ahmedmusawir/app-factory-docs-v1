# AUTHENTICATION & SUPABASE INTEGRATION MANUAL

> **Version:** 1.5 · **Date:** 2026-10-18 · **Status:** Active
> **Tier:** 4 — Reference Manuals · **Pairs with:** STARTER_KIT_HANDBOOK, DATABASE_MANUAL, API_AND_SERVICES_MANUAL, FRONTEND_FIRST_PLAYBOOK, RECON_QUESTIONNAIRE, STATE_MANAGEMENT_MANUAL

> **Project:** Stark SaaS Starter Kit
> **Born from:** Cyberize Run 001 — Lesson 2 (redundant authService)
> **Purpose:** Complete guide for authentication, authorization, and Supabase integration patterns
> **Role doctrine (v1.3):** the `user_roles` TABLE is the single source of truth for authorization. See "Role-Based Access Control" + the Version History for the F-042 correction.

---

## 🛑 CRITICAL — DO NOT AUTHOR authService.ts

> **The kit already provides complete Supabase SSR authentication.**
> Authoring a custom `authService.ts` wrapper produces dead code that diverges from the kit baseline.
> **Components consume the kit's auth primitives directly. Do not wrap them.**

### What The Kit Provides (Already Complete)

| Capability | Kit Provides | How To Consume |
|---|---|---|
| Server-side auth (RLS-respecting) | `src/utils/supabase/server.ts` | `createClient()` in Server Components / API routes |
| Browser-side auth | `src/utils/supabase/client.ts` | `createClient()` in Client Components |
| Middleware session refresh | `src/utils/supabase/middleware.ts` | Already wired in `src/proxy.ts` |
| Service-role admin operations | `src/utils/supabase/admin.ts` | `createAdminClient()` for portal admin actions |
| Login endpoint | `/api/auth/login` | POST email/password |
| Logout endpoint | `/api/auth/logout` | POST to clear session |
| Signup endpoint | `/api/auth/signup` | POST email/password/full_name |
| Email confirmation | `/api/auth/confirm` | GET callback |
| User creation (admin/superadmin) | Verify named actions against pinned kit | Each invocation checks caller, current role, allowed target and privileged-target protection before elevated capability |
| Client auth state | `src/store/useAuthStore.ts` | Zustand store with user + role flags |
| Server-side page protection | `src/utils/supabase/actions.ts` | `protectPage([AppRole.X])` |
| Login form UI | `src/components/auth/LoginForm.tsx` | Pre-wired to `/api/auth/login` |
| Signup form UI | `src/components/auth/RegisterForm.tsx` | Pre-wired to `/api/auth/signup` |

### The Anti-Pattern To Avoid

🛑 **DO NOT** write code like this:

```typescript
// src/services/authService.ts  ← THIS FILE SHOULD NOT EXIST
export const authService = {
  signIn: async (email: string, password: string) => {
    // wrapping Supabase auth here...
  },
  signOut: async () => { /* ... */ },
  // ...
};
```

### The Correct Patterns

**In a Server Component:**
```typescript
import { createClient } from "@/utils/supabase/server";

export default async function SomePage() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  // ...
}
```

**For a protected route:**
**Kit-signature example withdrawn pending verification:** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

**In a Client Component:**
```typescript
import { useAuthStore } from "@/store/useAuthStore";

export function MyComponent() {
  const user = useAuthStore((s) => s.user);
  const isAdmin = useAuthStore((s) => s.isAdmin);
  // ...
}
```

**For login form submission:**
```typescript
// Already wired in LoginForm.tsx — just use the component
import { LoginForm } from "@/components/auth/LoginForm";
```

### When You Might Legitimately Need A Service

The ONLY auth-related service that might legitimately exist is for **project-specific auth extensions** that are NOT in the kit. Examples:

- ✅ A `magicLinkService.ts` for magic-link auth (kit doesn't provide this)
- ✅ An `oauthService.ts` for Google/GitHub SSO if you add it (kit doesn't provide this)
- ✅ A `mfaService.ts` for two-factor auth (kit doesn't provide this)

🛑 **NEVER** a generic `authService.ts` that wraps what the kit already does.

If you're unsure whether a service is legitimate, surface to the operator BEFORE authoring.

### Cross-Reference

- **`STARTER_KIT_HANDBOOK.md` Section "Auth — Already Wired"** — full kit auth inventory
- **`COMPONENT_REGISTRY.md` Section "Auth Components"** — LoginForm, RegisterForm, AuthTabs primitives
- **`FRONTEND_FIRST_PLAYBOOK.md` Section "0. Pre-Authoring Kit Audit"** — the audit step that catches this

---

## Table of Contents

1. [Overview & Architecture](#overview--architecture)
2. [Supabase Client Setup](#supabase-client-setup)
3. [Authentication Flow](#authentication-flow)
4. [API Routes Reference](#api-routes-reference)
5. [Client-Side Auth (Zustand Store)](#client-side-auth-zustand-store)
6. [Server-Side Protection (RBAC)](#server-side-protection-rbac)
7. [Session Management & Middleware](#session-management--middleware)
8. [Role-Based Access Control](#role-based-access-control)
9. [Auth Components](#auth-components)
10. [Common Patterns & Recipes](#common-patterns--recipes)
11. [Troubleshooting](#troubleshooting)
12. [Security Best Practices](#security-best-practices)

---

## Overview & Architecture

### Authentication Stack

**Backend:**
- Supabase Auth (PostgreSQL + JWT)
- Server-side session validation
- Cookie-based authentication

**Frontend:**
- Zustand for client state
- React Hook Form + Zod validation
- Hard page reloads for session sync

**Middleware:**
- Next.js middleware for session refresh
- Automatic cookie synchronization
- Route-level protection

### Key Principles

1. **Server-side first** - All auth checks happen on the server
2. **Session persistence** - Middleware keeps sessions alive
3. **Role-based access** - Three-tier role system (superadmin, admin, member)
4. **Hard reloads** - Force full page reload after auth changes to sync server/client state
Roles must resolve from an authoritative server-side store. Creation and mutation require verified per-call authorization and a role input that untrusted signup cannot control. The historical Mark IV transport is not a verified safe recipe for the current kit; obtain pinned trigger and caller evidence before implementation.

---

## Supabase Client Setup

### Three Client Types

We use **three different Supabase clients** depending on the context:

| Client | Location | Use Case | Async? |
|--------|----------|----------|--------|
| Server | `src/utils/supabase/server.ts` | Server Components, API Routes | ✅ Yes |
| Browser | `src/utils/supabase/client.ts` | Client Components | ❌ No |
| Middleware | `src/utils/supabase/middleware.ts` | Session refresh | ✅ Yes |

---

### 1. Server Client (Server Components & API Routes)

**File:** `src/utils/supabase/server.ts`

```typescript
import { createServerClient } from "@supabase/ssr";
import { cookies } from "next/headers";

export const createClient = async () => {
  const cookieStore = await cookies();

  return createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return cookieStore.getAll();
        },
        setAll(cookiesToSet) {
          try {
            cookiesToSet.forEach(({ name, value, options }) =>
              cookieStore.set(name, value, options)
            );
          } catch {
            // Server Component - can't set cookies
          }
        },
      },
    }
  );
};
```

**Key Points:**
- ✅ **Must be async** (Next.js 15 + React 19 requirement)
- ✅ **Must await `cookies()`** before using
- Uses `@supabase/ssr` for server-side rendering
- Handles cookie get/set operations
- Try/catch for Server Components (can't set cookies)

**Usage:**
```typescript
// In Server Component
export default async function MyPage() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  // ...
}

// In API Route
export async function POST(req: NextRequest) {
  const supabase = await createClient();
  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password
  });
  // ...
}
```

---

### 2. Browser Client (Client Components)

**File:** `src/utils/supabase/client.ts`

```typescript
import { createBrowserClient } from "@supabase/ssr";

export const createClient = () =>
  createBrowserClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
  );
```

**Key Points:**
- ❌ **Not async** - synchronous function
- Uses `@supabase/ssr` browser client
- Automatically handles browser cookies
- Use in client components only

**Usage:**
```typescript
"use client";

import { createClient } from "@/utils/supabase/client";

export default function MyComponent() {
  const supabase = createClient();
  
  const handleAction = async () => {
    const { data } = await supabase.auth.getUser();
    // ...
  };
}
```

---

### 3. Middleware Client (Session Refresh)

**File:** `src/utils/supabase/middleware.ts`

```typescript
import { createServerClient } from "@supabase/ssr";
import { NextResponse, type NextRequest } from "next/server";

export async function updateSession(request: NextRequest) {
  let supabaseResponse = NextResponse.next({
    request,
  });

  const supabase = createServerClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!,
    {
      cookies: {
        getAll() {
          return request.cookies.getAll();
        },
        setAll(cookiesToSet) {
          cookiesToSet.forEach(({ name, value, options }) =>
            request.cookies.set(name, value)
          );
          supabaseResponse = NextResponse.next({
            request,
          });
          cookiesToSet.forEach(({ name, value, options }) =>
            supabaseResponse.cookies.set(name, value, options)
          );
        },
      },
    }
  );

  // Refresh session
  const {
    data: { user },
  } = await supabase.auth.getUser();

  return supabaseResponse;
}
```

**Key Points:**
- Runs on **every request** (via Next.js middleware)
- Syncs cookies between request and response
- Calls `getUser()` to refresh session
- Prevents session expiration during active use

**Middleware Entry:** the verified framework-version entry

```typescript
import { updateSession } from "@/utils/supabase/middleware";
import { NextRequest } from "next/server";

export async function middleware(request: NextRequest) {
  return await updateSession(request);
}

export const config = {
  matcher: [
    "/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",
  ],
};
```

---

## Authentication Flow

### Complete Login Flow

```
1. User enters credentials in LoginForm
   ↓
2. LoginForm calls useAuthStore.login()
   ↓
3. Zustand store calls POST /api/auth/login
   ↓
4. API route calls supabase.auth.signInWithPassword()
   ↓
5. Supabase validates credentials & sets cookies
   ↓
6. API returns user data with metadata
   ↓
7. Store updates state with user & roles
   ↓
8. Store determines redirect based on role
   ↓
9. Store saves redirect to localStorage
   ↓
10. Store forces window.location.reload()
   ↓
11. Page reloads, middleware refreshes session
   ↓
12. LoginForm useEffect reads localStorage redirect
   ↓
13. Router navigates to role-specific portal
```

### Why Hard Reload?

**Problem:** Server and client can have different session states

**Solution:** Force full page reload after login/logout

```typescript
// In useAuthStore.ts
window.location.reload();
```

**Benefits:**
- ✅ Server and client sessions always in sync
- ✅ Middleware runs to refresh cookies
- ✅ Server Components get fresh user data
- ✅ No stale auth state

**Tradeoff:**
- ❌ Not SPA-like (full page reload)
- ❌ Loses client state
- ✅ But ensures security and consistency

---

### Complete Registration Flow

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

At the trusted public-signup boundary, allow only approved profile fields and force the member role independently of submitted metadata. The provider-side creation path must also ignore or reject public role keys, so direct provider signup cannot bypass the endpoint. Privileged role assignment uses a separately authorized protected channel. Trigger hardening and a negative direct-provider test are required before promotion: role=admin submitted publicly must not produce an admin.

---

### Logout Flow

```
1. User clicks Logout button
   ↓
2. Button calls useAuthStore.logout()
   ↓
3. Store calls POST /api/auth/logout
   ↓
4. API route calls supabase.auth.signOut()
   ↓
5. Supabase clears session cookies
   ↓
6. Store clears user state
   ↓
7. Store forces window.location.reload()
   ↓
8. Page reloads, user redirected to /auth
```

---

## API Routes Reference

All auth routes are in `src/app/api/auth/`.

### POST /api/auth/login

**Purpose:** Authenticate user with email/password

**Request:**
```typescript
{
  email: string;
  password: string;
}
```

**Response (Success):**
**Legacy response example withdrawn:** client metadata flags are not authorization or first-render identity. Use the verified server-resolved user/role contract for the pinned kit.

**Response (Error):**
```typescript
{
  error: string;
}
```

**Implementation:**
**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

---

### POST /api/auth/logout

**Purpose:** Sign out current user

**Request:** Empty body

**Response:**
```typescript
{
  message: "Logged out successfully"
}
```

**Implementation:**
```typescript
export async function POST(req: NextRequest) {
  const supabase = await createClient();
  const { error } = await supabase.auth.signOut();
  if (error) {
    return NextResponse.json(
      { message: "Remote sign-out could not be confirmed. Retry sign-out." },
      { status: 503 }
    );
  }
  return NextResponse.json(
    { message: "Logged out successfully" },
    { status: 200 }
  );
}
```

---

### POST /api/auth/signup

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

At the trusted public-signup boundary, allow only approved profile fields and force the member role independently of submitted metadata. The provider-side creation path must also ignore or reject public role keys, so direct provider signup cannot bypass the endpoint. Privileged role assignment uses a separately authorized protected channel. Trigger hardening and a negative direct-provider test are required before promotion: role=admin submitted publicly must not produce an admin.

---

### GET /api/auth/confirm

**Purpose:** Confirm email via OTP token

**Query Parameters:**
- `token_hash` - OTP token from email
- `type` - Confirmation type (usually "signup")
- `next` - Redirect URL after confirmation (optional)

**Response:** Redirects to `next` or `/error`

**Implementation:**
```typescript
export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const token_hash = searchParams.get("token_hash");
  const type = searchParams.get("type");
  const next = searchParams.get("next") ?? "/";

  if (token_hash && type) {
    const supabase = await createClient();

    const { error } = await supabase.auth.verifyOtp({
      type: type as any,
      token_hash,
    });

    if (!error) {
      const origin = new URL(request.url).origin;
      const fallback = new URL("/", origin);
      const allowedPaths = new Set(["/"]); // Extend only with approved local destinations.
      try {
        const destination = new URL(next, origin);
        if (destination.origin === origin && allowedPaths.has(destination.pathname)) {
          destination.search = "";
          destination.hash = "";
          return NextResponse.redirect(destination);
        }
      } catch {
        // Malformed destinations use the fixed safe fallback.
      }
      return NextResponse.redirect(fallback);
    }
  }

  return NextResponse.redirect(new URL("/error", request.url));
}
```

---

### User creation — server actions (no API route)

User creation is handled by **server actions** behind role-gated layouts, not a public
API route. The legacy `POST /api/auth/superadmin-add-user` route was removed (Gate 6).

- Admin → `addMember` (`(admin)/admin-portal/actions.ts`) — creates a `member`
- Superadmin → `addUser` (`(superadmin)/superadmin-portal/actions.ts`) — creates admin/member

**Authorization:** the server action itself must authenticate and authorize each invocation before any privileged client call. A route-group layout is not an action authorization boundary. Resolve roles from the authoritative server store and allow only explicitly permitted target roles. Do not use a user-writable metadata trigger to assign privilege. The historical action/trigger recipe is withdrawn pending pinned kit verification.

---

## Client-Side Auth (Zustand Store)

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Server guards control page access; server-resolved { user, role } props establish first-render identity. Retire client HOC route protection and post-mount identity fetching as authoritative patterns. Zustand handles interaction and session-event reactions, with no persisted authorization authority. Display helpers are display-only and use explicit role sets; they never authorize an operation.

---

## Server-Side Protection (RBAC)

### protectPage Function

**File:** `src/utils/supabase/actions.ts`

**Kit-signature example withdrawn pending verification:** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

**Key Points:**
- ✅ Runs on server (Server Component or layout)
- ✅ Checks authentication first
- ✅ Then checks role authorization
- ✅ Redirects to /auth if unauthorized
- ✅ Returns user object if authorized

---

### Usage in Layouts

**Members Layout:**
**Kit-signature example withdrawn pending verification:** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

**Admin Layout:**
**Kit-signature example withdrawn pending verification:** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

**Superadmin Layout:**
**Kit-signature example withdrawn pending verification:** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

---

### Multiple Roles

**Kit-signature example withdrawn pending verification:** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

---

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

**Kit-signature example withdrawn pending verification:** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

Do not assume the page guard returns `{ user, role }`; verify the pinned implementation and callers before destructuring its result.
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

---

## Role-Based Access Control

### Role Definition

**File:** `src/utils/get-user-role.ts` — the kit's canonical role-resolution path.

```typescript
export type AppRole = "superadmin" | "admin" | "member";
```

Roles must resolve from an authoritative server-side store. Creation and mutation require verified per-call authorization and a role input that untrusted signup cannot control. The historical Mark IV transport is not a verified safe recipe for the current kit; obtain pinned trigger and caller evidence before implementation.

> 📁 **The kit file on disk is the ground truth.** Read `src/utils/get-user-role.ts` and `supabase/setup.sql` in the repo you are working on (recon Q3.2/Q5.3). This manual intentionally does not carry an implementation copy that can drift — an earlier edition of this section showed a `user_metadata`-reading implementation that no longer matches the kit (F-042; corrected v1.3).

**⛔ FORBIDDEN:** any `getUserRole` variant (or ad-hoc check) that reads roles from `user_metadata` for authorization — that is the recon Q3.4 smell.

---

### Role Hierarchy

```
superadmin (highest privilege)
    ↓
  admin
    ↓
  member (lowest privilege)
```

**Access Rules:**
- Superadmin can access superadmin routes only (unless explicitly allowed)
- Admin can access admin routes only
- Member can access member routes only

**⚠️ Important:** Roles are **exclusive** by default. If you want superadmin to access admin routes, you must explicitly allow it:

**Kit-signature example withdrawn pending verification:** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

---

### Where Roles Live (v1.3 — the F-042 correction)

Roles must resolve from an authoritative server-side store. Creation and mutation require verified per-call authorization and a role input that untrusted signup cannot control. The historical Mark IV transport is not a verified safe recipe for the current kit; obtain pinned trigger and caller evidence before implementation.

Roles must resolve from an authoritative server-side store. Creation and mutation require verified per-call authorization and a role input that untrusted signup cannot control. The historical Mark IV transport is not a verified safe recipe for the current kit; obtain pinned trigger and caller evidence before implementation.

**⛔ FORBIDDEN:**
- Reading `user_metadata` for ANY authorization decision, client or server (recon Q3.4 smell).
- Writing role values to metadata outside the protected admin channel.

**Hardening note:** a kit-side hardening ticket exists for the creation-time transport channel; apply the kit's current hardening when building on it. This manual deliberately does not document the vector.

---

## Session Management & Middleware

### Middleware Flow

```
Every Request
    ↓
Next.js Middleware (verified entry for the installed framework)
    ↓
updateSession() (src/utils/supabase/middleware.ts)
    ↓
Create Supabase client with cookie handlers
    ↓
Call supabase.auth.getUser()
    ↓
Refresh session if needed
    ↓
Sync cookies between request/response
    ↓
Continue to route handler
```

### Session Lifecycle

**Session Creation:**
1. User logs in via `/api/auth/login`
2. Supabase sets session cookies
3. Cookies include access token + refresh token

**Session Refresh:**
1. Middleware runs on every request
2. Calls `getUser()` which auto-refreshes if needed
3. Updates cookies with new tokens
4. Session stays alive during active use

**Session Expiration:**
- Access token expires after 1 hour (default)
- Refresh token expires after 7 days (default)
- Middleware auto-refreshes before expiration
- User must re-login after refresh token expires

---

### Cookie Configuration

**Cookie Names:**
- `sb-<project-ref>-auth-token` - Access token
- `sb-<project-ref>-auth-token-code-verifier` - PKCE verifier

**Cookie Options:**
- HttpOnly attributes — verify against the approved kit session architecture; no blanket value is prescribed here
- `secure: true` - HTTPS only (production)
- `sameSite: 'lax'` - CSRF protection
- `path: '/'` - Available site-wide

---

## Auth Components

### AuthTabs Component

**File:** `src/components/auth/AuthTabs.tsx`

**Purpose:** Tab switcher for Login/Register forms

```typescript
const AuthTabs = () => {
  const [selectedTab, setSelectedTab] = useState("login");

  return (
    <Tabs defaultValue="login" className="w-[400px] mt-16">
      <TabsList className="grid w-full grid-cols-2">
        <TabsTrigger value="login">Login</TabsTrigger>
        <TabsTrigger value="register">Register</TabsTrigger>
      </TabsList>
      
      <TabsContent value="login">
        <LoginForm />
      </TabsContent>
      
      <TabsContent value="register">
        <RegisterForm />
      </TabsContent>
    </Tabs>
  );
};
```

**Features:**
- Two-tab interface
- Active tab highlighting
- Smooth transitions
- Dark mode support

---

### LoginForm Component

**File:** `src/components/auth/LoginForm.tsx`

**Features:**
- React Hook Form validation
- Zod schema validation
- Error handling
- Loading states
- Redirect after login

**Form Schema:**
```typescript
const formSchema = z.object({
  email: z.string().min(1, "Email is required").email("Please enter a valid email"),
  password: z.string().min(1, "Password is required"),
});
```

**Submit Handler:**
**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

**Redirect Logic:**
```typescript
useEffect(() => {
  const target = localStorage.getItem("redirectAfterLogin");
  if (target) {
    localStorage.removeItem("redirectAfterLogin");
    router.replace(target);
  }
}, [router]);
```

---

### RegisterForm Component

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

At the trusted public-signup boundary, allow only approved profile fields and force the member role independently of submitted metadata. The provider-side creation path must also ignore or reject public role keys, so direct provider signup cannot bypass the endpoint. Privileged role assignment uses a separately authorized protected channel. Trigger hardening and a negative direct-provider test are required before promotion: role=admin submitted publicly must not produce an admin.

---

### Auth Page Layout

**File:** `src/app/(auth)/layout.tsx`

```typescript
const AuthLayout = ({ children }) => {
  return (
    <>
      <NavbarLoginReg />
      <div className="h-[100vh] flex items-center justify-center relative">
        {children}
      </div>
    </>
  );
};
```

**Features:**
- Full-height centered layout
- Minimal navbar
- Clean, focused design

---

## Common Patterns & Recipes

### Pattern 1: Get Current User (Server)

```typescript
// In Server Component or API Route
import { createClient } from "@/utils/supabase/server";

export default async function MyPage() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  
  if (!user) {
    redirect("/auth");
  }
  
  return <div>Welcome, {user.email}</div>;
}
```

---

### Pattern 2: Get Current User (Client)

```typescript
"use client";

import { createClient } from "@/utils/supabase/client";
import { useEffect, useState } from "react";

export default function MyComponent() {
  const [user, setUser] = useState(null);
  const supabase = createClient();
  
  useEffect(() => {
    const getUser = async () => {
      const { data: { user } } = await supabase.auth.getUser();
      setUser(user);
    };
    getUser();
  }, []);
  
  return <div>{user?.email}</div>;
}
```

---

### Pattern 3: Protected Page (Server Component)

**Kit-signature example withdrawn pending verification:** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

---

### Pattern 4: Role-Based UI (Client)

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Server guards control page access; server-resolved { user, role } props establish first-render identity. Retire client HOC route protection and post-mount identity fetching as authoritative patterns. Zustand handles interaction and session-event reactions, with no persisted authorization authority. Display helpers are display-only and use explicit role sets; they never authorize an operation.

---

### Pattern 5: Conditional Navbar Links

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Server guards control page access; server-resolved { user, role } props establish first-render identity. Retire client HOC route protection and post-mount identity fetching as authoritative patterns. Zustand handles interaction and session-event reactions, with no persisted authorization authority. Display helpers are display-only and use explicit role sets; they never authorize an operation.

---

### Pattern 6: Fetch User-Specific Data

```typescript
// Server Component
import { createClient } from "@/utils/supabase/server";

export default async function MyPosts() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  
  if (!user) redirect("/auth");
  
  // Fetch user's posts
  const { data: posts } = await supabase
    .from("posts")
    .select("*")
    .eq("user_id", user.id);
  
  return (
    <div>
      {posts?.map(post => (
        <div key={post.id}>{post.title}</div>
      ))}
    </div>
  );
}
```

---

### Pattern 7: Update User Metadata

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

---

## Troubleshooting

### Issue 1: "cookies() should be awaited"

**Error:**
```
Error: Route "/api/auth/login" used cookies().get(...). 
cookies() should be awaited before using its value.
```

**Cause:** Next.js 15 + React 19 requires `await cookies()`

**Fix:**
```typescript
// ❌ Wrong
export const createClient = () => {
  const cookieStore = cookies();
  // ...
}

// ✅ Correct
export const createClient = async () => {
  const cookieStore = await cookies();
  // ...
}
```

**Also update all call sites:**
```typescript
// ❌ Wrong
const supabase = createClient();

// ✅ Correct
const supabase = await createClient();
```

---

### Issue 2: Session not persisting

**Symptoms:**
- User logs in but appears logged out on refresh
- Session cookies not being set

**Causes:**
1. Middleware not running
2. Cookie settings incorrect
3. HTTPS required but using HTTP

**Fixes:**
1. Check the verified framework-version entry is present and configured
2. Verify `NEXT_PUBLIC_SITE_URL` is set correctly
3. Use HTTPS in production
4. Check browser cookie settings

---

### Issue 3: Infinite redirect loop

**Symptoms:**
- Page keeps redirecting to /auth
- Browser shows "too many redirects"

**Causes:**
1. `protectPage()` in wrong place
2. Middleware interfering with auth routes
3. Role check failing

**Fixes:**
1. Only use `protectPage()` in layouts, not in /auth routes
2. Exclude /auth from middleware matcher
3. Check the user's row in `user_roles` (did the creation-time transport apply at signup?)

---

### Issue 4: Hard reload loses state

**Symptoms:**
- Client state lost after login
- Form data cleared

**This is expected behavior:**
- Hard reload is intentional for session sync
- Use localStorage for persistence if needed
- Or refactor to avoid hard reload (advanced)

---

### Issue 5: Role not recognized

**Symptoms:**
- User has role but `getUserRole()` returns null
- Access denied despite correct metadata

**Causes:**
1. No row in `user_roles` for the user (the `handle_new_user()` trigger didn't fire, or the user pre-dates it)
2. Creation-time metadata transport missing/malformed, so the trigger applied nothing
3. Role value in the table not one of the expected values

**Fixes:**
1. Check the user's row in the `user_roles` table in the Supabase dashboard
2. Verify the `handle_new_user()` trigger exists (recon Q5.3) and the creation flow used the protected channel
3. Read `src/utils/get-user-role.ts` on disk for the resolution behavior — the kit file is the ground truth

---

## Security Best Practices

### ✅ DO

1. **Always validate on server**
   - Never trust client-side auth state
   - Use `protectPage()` in layouts
   - Validate user in API routes

2. **Use environment variables**
   - Store Supabase keys in `.env.local`
   - Never commit secrets to git
   - Use different keys for dev/prod

3. **Implement RLS policies**
   - Add Row Level Security in Supabase
   - Restrict data access by user ID
   - Enforce at database level

4. **Validate all inputs**
   - Use Zod schemas
   - Sanitize user input
   - Check for SQL injection

5. **Use HTTPS in production**
   - Required for secure cookies
   - Prevents man-in-the-middle attacks

6. **Set proper cookie options**
   - HttpOnly only where compatible with the verified session architecture
   - `secure: true` (production)
   - `sameSite: 'lax'`

7. **Implement rate limiting**
   - Prevent brute force attacks
   - Limit login attempts
   - Use Supabase rate limiting or middleware

---

### ❌ DON'T

1. **Don't trust client state**
   - Client can be manipulated
   - Always verify on server

2. **Don't store sensitive data in localStorage**
   - Accessible via JavaScript
   - Use secure cookies instead

3. **Don't expose API keys**
   - Never commit to git
   - Don't log in production
   - Use environment variables

4. **Don't skip validation**
   - Validate all user input
   - Check roles on every request
   - Don't assume data is safe

5. **Don't use weak passwords**
   - Enforce password requirements
   - Consider password strength meter
   - Implement password reset

6. **Don't ignore errors**
   - Log authentication errors
   - Monitor failed login attempts
   - Alert on suspicious activity

---

### Security Checklist

**Before Production:**
- [ ] RLS policies implemented on all tables
- [ ] Environment variables secured
- [ ] HTTPS enabled
- [ ] Rate limiting configured
- [ ] Password requirements enforced
- [ ] Email verification enabled
- [ ] Session timeout configured
- [ ] Error logging implemented
- [ ] Security headers set
- [ ] CORS configured properly
- [ ] API routes protected
- [ ] User input sanitized
- [ ] SQL injection prevented
- [ ] XSS protection enabled
- [ ] CSRF tokens implemented (if needed)

---

## Advanced Topics

### Custom Email Templates

Configure in Supabase Dashboard:
1. Go to Authentication > Email Templates
2. Customize confirmation, reset, invite emails
3. Use variables: `{{ .ConfirmationURL }}`, `{{ .Token }}`

---

### Password Reset Flow

**Not currently implemented. To add:**

1. Create `/api/auth/reset-password` route
2. Call `supabase.auth.resetPasswordForEmail()`
3. User receives email with reset link
4. Create password reset page
5. Call `supabase.auth.updateUser({ password })`

---

### Email Verification

**Currently optional. To enforce:**

1. Enable in Supabase Dashboard
2. Users must confirm email before login
3. Handle unverified state in login flow
4. Show "verify email" message

---

### OAuth Providers

**To add Google/GitHub login:**

1. Configure provider in Supabase Dashboard
2. Add OAuth button to LoginForm
3. Call `supabase.auth.signInWithOAuth({ provider: 'google' })`
4. Handle callback in `/api/auth/callback`

---

### Multi-Factor Authentication

**To add 2FA:**

1. Enable in Supabase Dashboard
2. Call `supabase.auth.mfa.enroll()`
3. User scans QR code
4. Verify with `supabase.auth.mfa.verify()`
5. Require on login

---

## Quick Reference

### Import Statements

```typescript
// Server Components / API Routes
import { createClient } from "@/utils/supabase/server";
import { protectPage } from "@/utils/supabase/actions";
import { getUserRole } from "@/utils/get-user-role";

// Client Components
import { createClient } from "@/utils/supabase/client";
import { useAuthStore } from "@/store/useAuthStore";

// Middleware
import { updateSession } from "@/utils/supabase/middleware";
```

---

### Common Commands

**Kit-signature example withdrawn pending verification:** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

---

## Environment Variables

Required in `.env.local`:

```bash
NEXT_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
NEXT_PUBLIC_SITE_URL=http://localhost:3000
```

**Production:**
```bash
NEXT_PUBLIC_SITE_URL=https://yourdomain.com
```

---

## File Structure Reference

```
src/
├── app/
│   ├── (auth)/
│   │   ├── layout.tsx              # Auth page layout
│   │   └── auth/
│   │       └── page.tsx            # Login/Register page
│   └── api/
│       └── auth/
│           ├── login/route.ts      # POST login
│           ├── logout/route.ts     # POST logout
│           ├── signup/route.ts     # POST signup
│           └── confirm/route.ts    # GET email confirm
├── components/
│   └── auth/
│       ├── AuthTabs.tsx            # Tab switcher
│       ├── LoginForm.tsx           # Login form
│       ├── RegisterForm.tsx        # Register form
│       └── Logout.tsx              # Logout button
├── store/
│   └── useAuthStore.ts             # Zustand auth store
├── utils/
│   ├── get-user-role.ts            # Role derivation
│   └── supabase/
│       ├── server.ts               # Server client
│       ├── client.ts               # Browser client
│       ├── middleware.ts           # Session refresh
│       ├── actions.ts              # protectPage
│       └── fetchUserData.ts        # User data helper
└── <verified-session-entry>        # framework-version-specific entry
```

---

## 12. SuperAdmin User Management

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization.

Use the session client for identity and RLS-bound data. Acquire an isolated admin client only after independently authorizing the elevated operation. An API route is not itself a reason to bypass RLS. Do not substitute a service-role client as a general fix for denied access.

---

## 13. User Mirror Table Pattern

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization.

Use an atomic database operation for invariants inside one database. Across external boundaries, use a stable operation identity, check every forward and compensation result, and persist completed, failed or partially-completed outcomes. Partial failure creates durable reconciliation work with a recovery owner; do not report success after an unchecked compensation or deletion.

---

## 14. HOC Route Protection Pattern

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Server guards control page access; server-resolved { user, role } props establish first-render identity. Retire client HOC route protection and post-mount identity fetching as authoritative patterns. Zustand handles interaction and session-event reactions, with no persisted authorization authority. Display helpers are display-only and use explicit role sets; they never authorize an operation.

---

## Summary

This authentication system provides:

✅ **Secure** - Server-side validation, secure cookies, session management  
✅ **Simple** - Three client types, clear patterns, minimal boilerplate  
✅ **Scalable** - Role-based access, metadata-driven, extensible  
✅ **Production-ready** - Middleware, error handling, type safety  
✅ **SuperAdmin Ready** - User management APIs, mirror tables, HOC protection

**Key Takeaways:**
1. Always use server-side validation
2. Three client types for different contexts
3. Hard reload ensures session sync
4. Authorization roles resolved from the authoritative user_roles table; never from user_metadata.
5. Middleware keeps sessions alive
6. protectPage() for route protection
7. Mirror tables for custom user data
8. HOC pattern for layout-level protection
9. SuperAdmin APIs for user management

**Next Steps:**
1. Implement RLS policies in Supabase
2. Add password reset flow
3. Enable email verification
4. Add rate limiting
5. Implement audit logging
6. Consider OAuth providers

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | (original, date unknown) | Initial manual: Supabase clients, auth flows, API routes, Zustand store, protectPage RBAC, session middleware, components, patterns, troubleshooting, security practices. |
| 1.1 | Jun 2026 | Run 001 era updates (service-layer antibody groundwork). |
| 1.2 | 2026-06-28 | Removed the deleted `POST /api/auth/superadmin-add-user` route (creation via `addMember`/`addUser` server actions); documented the Mark IV `handle_new_user` trigger applying the metadata `role` + `full_name` at creation. Kit Hardening Gate 10. |
| 1.3 | 2026-07-08 | **Wave 4 — the F-042 role-doctrine correction.** Role storage doctrine corrected everywhere it lived: the `user_roles` TABLE is the single source of truth (kit `supabase/setup.sql`; server-side resolution via `get-user-role.ts`); the v1.2 "Metadata-driven roles — NOT separate tables" philosophy line was FALSE against the kit's own filesystem (RECON_WAVE0 Q1 ground-truth). Key Principle #5 rewritten; "User Metadata Schema" section → "Where Roles Live" (table home + creation-time-transport nuance + ⛔ never read authz from `user_metadata`, recon Q3.4); §8 metadata-reading `getUserRole` sample replaced with the canonical-path description + read-the-kit-on-disk pointer (no drifting code copies — D-015); legacy `is_qr_*` (QR-era) store/pattern snippets marked with advisories; troubleshooting realigned to the table model; registration flow wording corrected. Kit hardening ticket referenced without documenting the vector. Canonical cross-refs (F-032/F-011); standard header (F-018). Full code-sample resync vs the kit = queued kit-verification touch. |
| 1.4 | 2026-08-05 | **Navbar Saga promotion.** New § "Server-Resolved Identity for UI (The Navbar Law)" inserted after Server-Side Protection (RBAC): identity renders from server props, never from client stores. Four hard rules. | navbar-saga |
| 1.5 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-001, FC-021, FC-033, FC-034, FC-035, FC-036, FC-038, FC-039, FC-041, FC-042, FC-043, FC-044, FC-063, FC-066, RUL-11 |

---

**End of Manual**

*Build secure, scalable auth flows with confidence.* 🔐
