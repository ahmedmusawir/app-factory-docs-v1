# API AND SERVICES MANUAL

> **Version:** 1.2 · **Date:** 2026-10-16 · **Status:** Active
> **Tier:** 4 — Reference Manuals · **Pairs with:** FRONTEND_FIRST_PLAYBOOK, STARTER_KIT_HANDBOOK, DATABASE_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL, TESTING_PLAYBOOK

> **Stark Industries Software Factory**
> *The definitive guide to building scalable, maintainable service layers for any external API integration.*

---

## Table of Contents

1. [Philosophy & Architecture](#1-philosophy--architecture)
2. [Folder Structure](#2-folder-structure)
3. [Service Layer Implementation](#3-service-layer-implementation)
4. [API Route Patterns](#4-api-route-patterns)
5. [External API Integration](#5-external-api-integration)
6. [Supabase Service Pattern](#6-supabase-service-pattern)
7. [Data Transformation](#7-data-transformation)
8. [Error Handling Strategy](#8-error-handling-strategy)
9. [Performance Patterns](#9-performance-patterns)
10. [Quick Reference](#10-quick-reference)

---

## 1. Philosophy & Architecture

### The Service Layer Pattern

The Service Layer is the **single most important architectural decision** in this codebase. It enforces a strict separation between UI components and data-fetching logic.

**The Rule:** Components render. Services fetch.

> 🛑 **THE KIT EXCEPTION (Run 001, Lesson 2 — read before authoring ANY service):**
> **Kit primitives are consumed directly — the kit's auth IS the service layer.** The rule above governs *project-specific domain logic*; it does NOT license wrapping capabilities the starter kit already provides complete (the Run 001 near-miss: an `authService.ts` wrapper specced around the kit's finished Supabase SSR auth). Before authoring any service, run the **Kit Audit** (`FRONTEND_FIRST_PLAYBOOK.md` §0) against `STARTER_KIT_HANDBOOK.md`'s "Should I Author This?" verdict table — if the kit provides it, consume the primitive; do not wrap it. (Full doctrine: `AUTH_MANUAL.md` §0.)

```
┌─────────────────────────────────────────────────────────────────┐
│                        UI COMPONENTS                            │
│   (React components only handle rendering and user interaction) │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       SERVICE LAYER                             │
│   (All API calls, data transformation, error handling)          │
│   Location: src/services/                                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       API ROUTES                                │
│   (Next.js API routes act as secure middleware/proxy)           │
│   Location: src/app/api/                                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    EXTERNAL SERVICES                            │
│   (WooCommerce, Stripe, WordPress, Supabase, CRM APIs, etc.)    │
└─────────────────────────────────────────────────────────────────┘
```

### Why This Matters

1. **Testability**: Services can be unit tested without rendering components
2. **Reusability**: Multiple components can share the same service functions
3. **Maintainability**: API changes only require updates in one place
4. **Security**: Credentials never leak to the client
5. **Type Safety**: Response types are defined once and enforced everywhere

### Server vs Client Data Fetching Decision Tree

```
START: Where does this data come from?
│
├─► External API with credentials (API keys, secrets)
│   └─► ALWAYS use API Route → Service Layer (Server-side)
│
├─► Supabase with RLS (Row Level Security)
│   └─► Can use Client OR Server depending on context
│       ├─► Server Component → Use server createClient
│       └─► Client Component → Use browser createClient
│
├─► Public data (no auth required)
│   └─► Server Component with direct fetch (SSR/SSG)
│
└─► User-triggered action (button click, form submit)
    └─► Client Component → API Route → Service Layer
```

### API Route as Proxy Pattern

**Never expose credentials to the client.** API routes act as a secure proxy:

```typescript
// ❌ WRONG: Credentials in client code
const response = await fetch('https://api.external.com/data', {
  headers: { 'Authorization': `Bearer ${process.env.NEXT_PUBLIC_API_KEY}` }
});

// ✅ CORRECT: Credentials stay on server
// Client calls our API route
const response = await fetch('/api/external-data');

// API route handles credentials
// src/app/api/external-data/route.ts
export async function GET() {
  const data = await externalService.fetchData(); // Uses server-only env vars
  return NextResponse.json(data);
}
```

---

## 2. Folder Structure

### Standard Layout

```
src/
├── app/
│   └── api/                          # API route handlers
│       ├── create-payment-intent/
│       │   └── route.ts
│       ├── place-order/
│       │   └── route.ts
│       ├── sync-contact/             # Future: CRM sync endpoints
│       │   └── route.ts
│       └── [resource]/
│           └── route.ts
│
├── services/                         # Service layer functions
│   ├── productServices.ts            # Product-related API calls
│   ├── orderServices.ts              # Order-related API calls
│   ├── blogServices.ts               # Blog/content API calls
│   ├── paymentServices.ts            # Payment processing
│   ├── supabaseServices.ts           # Supabase data operations
│   └── crmServices.ts                # Future: CRM integrations
│
├── constants/
│   └── apiEndpoints.ts               # Centralized endpoint definitions
│
├── types/
│   ├── product.ts                    # Product type definitions
│   ├── order.ts                      # Order type definitions
│   ├── api-responses.ts              # External API response types
│   └── supabase.ts                   # Supabase-generated types
│
└── lib/
    └── utils.ts                      # Shared utilities (cn, formatters)
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Service file | `{domain}Services.ts` | `productServices.ts` |
| Service function | `fetch{Resource}`, `create{Resource}`, `update{Resource}` | `fetchProductBySlug()` |
| API route folder | `kebab-case` | `create-payment-intent/` |
| Type file | `{domain}.ts` | `product.ts` |
| Constant file | `camelCase.ts` | `apiEndpoints.ts` |

---

## 3. Service Layer Implementation

### Creating a Service File

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Services return an explicit typed outcome: success, not-found, unavailable, invalid or forbidden. Routes map it to the approved HTTP/UI behavior with generic client messages and no upstream error text. Do not cache failures as successful public data. Degrade or fail closed according to the module’s approved failure policy; an unavailable entitlement read is not confirmed absence.

Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results.

---

### Function Naming Conventions

| Action | Prefix | Example |
|--------|--------|---------|
| Read single | `fetch{Resource}` | `fetchProductBySlug()` |
| Read multiple | `fetch{Resources}` or `fetchAll{Resources}` | `fetchProducts()`, `fetchAllProductSlugs()` |
| Create | `create{Resource}` | `createOrder()` |
| Update | `update{Resource}` | `updateOrderStatus()` |
| Delete | `delete{Resource}` | `deleteCartItem()` |
| Validate | `validate{Resource}` | `validateCoupon()` |
| Sync | `sync{Resource}` | `syncContactToCRM()` |

### TypeScript Interface Patterns

Define response types that match your service return values:

```typescript
// src/types/product.ts

export interface Product {
  id: number;
  name: string;
  slug: string;
  price: string;
  regular_price: string;
  sale_price: string;
  description: string;
  short_description: string;
  images: ProductImage[];
  categories: ProductCategory[];
  attributes: ProductAttribute[];
  variations: number[];
  stock_status: 'instock' | 'outofstock' | 'onbackorder';
}

export interface ProductImage {
  id: number;
  src: string;
  alt: string;
}

export interface ProductCategory {
  id: number;
  name: string;
  slug: string;
}

export interface ProductAttribute {
  id: number;
  name: string;
  options: string[];
}

// Response wrapper for paginated data
export interface ProductsResponse {
  items: Product[];
  totalPages: number;
  totalItems: number;
}
```

### Error Handling Template

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Services return an explicit typed outcome: success, not-found, unavailable, invalid or forbidden. Routes map it to the approved HTTP/UI behavior with generic client messages and no upstream error text. Do not cache failures as successful public data. Degrade or fail closed according to the module’s approved failure policy; an unavailable entitlement read is not confirmed absence.

Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results.

---

### Return Type Consistency

Always return the same shape, even on error:

```typescript
// ✅ CORRECT: Consistent return shape
interface ServiceResponse<T> {
  data: T | null;
  error: string | null;
  success: boolean;
}

export const fetchUser = async (id: string): Promise<ServiceResponse<User>> => {
  try {
    const user = await db.users.findUnique({ where: { id } });
    return { data: user, error: null, success: true };
  } catch (error) {
    return { data: null, error: 'Failed to fetch user', success: false };
  }
};

// ❌ WRONG: Inconsistent returns
export const fetchUser = async (id: string) => {
  try {
    return await db.users.findUnique({ where: { id } }); // Returns User
  } catch (error) {
    throw error; // Throws Error - different shape!
  }
};
```

---

## 4. API Route Patterns

### GET Route Template

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Services return an explicit typed outcome: success, not-found, unavailable, invalid or forbidden. Routes map it to the approved HTTP/UI behavior with generic client messages and no upstream error text. Do not cache failures as successful public data. Degrade or fail closed according to the module’s approved failure policy; an unavailable entitlement read is not confirmed absence.

Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results.

---

### POST Route Template

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### Request Validation with Zod

```typescript
// src/types/order.ts

import { z } from 'zod';

export const OrderCreateSchema = z.object({
  customer: z.object({
    email: z.string().email(),
    firstName: z.string().min(1),
    lastName: z.string().min(1),
    phone: z.string().optional(),
  }),
  billing: z.object({
    address1: z.string().min(1),
    city: z.string().min(1),
    state: z.string().min(2).max(2),
    postcode: z.string().min(5),
    country: z.string().default('US'),
  }),
  items: z.array(z.object({
    productId: z.number(),
    quantity: z.number().min(1),
    variationId: z.number().optional(),
  })).min(1),
  paymentMethod: z.enum(['stripe', 'paypal', 'cod']),
});

export type OrderCreateInput = z.infer<typeof OrderCreateSchema>;
```

### Response Formatting Standards

```typescript
// Success responses
{ data: T }                           // Single resource
{ items: T[], total: number }         // Collection with count
{ success: true, message: string }    // Action confirmation

// Error responses
{ error: string }                     // Simple error
{ error: string, code: string }       // Error with code
{ error: string, details: object }    // Validation errors
```

### Caching Headers

```typescript
// Static data (products, categories)
headers: {
  'Cache-Control': 'public, s-maxage=3600, stale-while-revalidate=86400',
}

// User-specific data (cart, orders)
headers: {
  'Cache-Control': 'private, no-cache, no-store, must-revalidate',
}

// Real-time data (inventory, prices)
headers: {
  'Cache-Control': 'no-store',
}
```

---

## 5. External API Integration

### REST API Pattern

For REST APIs like WooCommerce, payment gateways, or CRM systems:

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### GraphQL Pattern

For GraphQL APIs like WordPress/WPGraphQL:

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### Authentication Handling

**Server-side only.** Never expose API keys to the client.

```typescript
// src/constants/apiEndpoints.ts

// Base URL from environment
const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL;

// Public endpoints (safe for client)
export const API_ENDPOINTS = {
  PRODUCTS: `${BACKEND_URL}/wp-json/wc/v3/products`,
  CATEGORIES: `${BACKEND_URL}/wp-json/wc/v3/products/categories`,
  GRAPHQL: `${BACKEND_URL}/graphql`,
};

// Server-only credentials (never import in client components)
export const getServerCredentials = () => {
  if (typeof window !== 'undefined') {
    throw new Error('Server credentials accessed on client!');
  }
  
  return {
    wooConsumerKey: process.env.WOOCOM_CONSUMER_KEY!,
    wooConsumerSecret: process.env.WOOCOM_CONSUMER_SECRET!,
    stripeSecretKey: process.env.STRIPE_SECRET_KEY!,
    crmApiKey: process.env.CRM_API_KEY!,
  };
};
```

### Environment Variable Management

```bash
# .env.local

# Public (exposed to browser via NEXT_PUBLIC_ prefix)
NEXT_PUBLIC_BACKEND_URL=https://api.example.com
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_xxx

# Private (server-only, no NEXT_PUBLIC_ prefix)
WOOCOM_CONSUMER_KEY=ck_xxx
WOOCOM_CONSUMER_SECRET=cs_xxx
STRIPE_SECRET_KEY=sk_test_xxx
CRM_API_KEY=xxx
SUPABASE_SERVICE_ROLE_KEY=xxx
```

---

## 6. Supabase Service Pattern

This section documents how to integrate Supabase within the service layer architecture, using the existing `createClient` utilities from this starter kit.

### Client Types Recap

```typescript
// Browser client - for client components
import { createClient } from '@/utils/supabase/client';

// Server client - for server components, API routes, server actions
import { createClient } from '@/utils/supabase/server';
```

### Supabase Service File Structure

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### Client-Side Supabase Service

For operations that need to run in client components (real-time subscriptions, user-triggered actions):

```typescript
// src/services/supabaseClientServices.ts
'use client';

import { createClient } from '@/utils/supabase/client';
import type { RealtimeChannel } from '@supabase/supabase-js';

/**
 * Subscribe to real-time changes on a table
 * Client-side only
 */
export const subscribeToTable = (
  table: string,
  callback: (payload: unknown) => void
): RealtimeChannel => {
  const supabase = createClient();
  
  const channel = supabase
    .channel(`${table}_changes`)
    .on(
      'postgres_changes',
      { event: '*', schema: 'public', table },
      callback
    )
    .subscribe();

  return channel;
};

/**
 * Unsubscribe from a channel
 */
export const unsubscribeFromChannel = async (channel: RealtimeChannel) => {
  const supabase = createClient();
  await supabase.removeChannel(channel);
};
```

### Using Supabase Services in API Routes

```typescript
// src/app/api/profiles/[id]/route.ts

import { NextRequest, NextResponse } from 'next/server';
import { fetchProfile, updateProfile } from '@/services/supabaseServices';

export async function GET(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params;
  
  const result = await fetchProfile(id);
  
  if (result.error) {
    return NextResponse.json({ error: result.error }, { status: 400 });
  }
  
  if (!result.data) {
    return NextResponse.json({ error: 'Profile not found' }, { status: 404 });
  }
  
  return NextResponse.json({ profile: result.data });
}

export async function PATCH(
  request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
) {
  const { id } = await params;
  const body = await request.json();
  
  const result = await updateProfile(id, body);
  
  if (result.error) {
    return NextResponse.json({ error: result.error }, { status: 400 });
  }
  
  return NextResponse.json({ profile: result.data });
}
```

### Using Supabase Services in Server Components

```typescript
// src/app/(public)/profile/page.tsx

import { fetchProfile } from '@/services/supabaseServices';
import { createClient } from '@/utils/supabase/server';
import { redirect } from 'next/navigation';

export default async function ProfilePage() {
  const supabase = await createClient();
  const { data: { user } } = await supabase.auth.getUser();
  
  if (!user) {
    redirect('/auth/login');
  }
  
  const { data: profile, error } = await fetchProfile(user.id);
  
  if (error || !profile) {
    return <div>Error loading profile</div>;
  }
  
  return (
    <div>
      <h1>Welcome, {profile.full_name}</h1>
      {/* Profile content */}
    </div>
  );
}
```

---

## 7. Data Transformation

### Wire-Format Conventions (Factory Standard)

- **Wire shapes are `snake_case`** (matches FastAPI/Pydantic and most REST payloads — e.g. `regular_price`, `stock_status`).
- **UI-internal types are `camelCase`** (e.g. `regularPrice`, `inStock`).
- **The service layer owns the translation** — the normalize functions below are where the case boundary lives. UI code never sees wire casing; wire payloads never see UI casing.
- These conventions are the DATA_CONTRACT discipline (`HANDOFF_PACKAGE_PLAYBOOK.md` §5.2) — the contract documents both shapes; both mock and real backends satisfy it.

### Normalizing External Responses

External APIs often return data in formats that don't match your internal types. Transform at the service layer:

```typescript
// src/services/productServices.ts

import type { Product } from '@/types/product';
import type { WooCommerceProduct } from '@/types/api-responses';

/**
 * Transforms WooCommerce product to internal Product type
 */
const normalizeProduct = (wooProduct: WooCommerceProduct): Product => ({
  id: wooProduct.id,
  name: wooProduct.name,
  slug: wooProduct.slug,
  price: parseFloat(wooProduct.price) || 0,
  regularPrice: parseFloat(wooProduct.regular_price) || 0,
  salePrice: wooProduct.sale_price ? parseFloat(wooProduct.sale_price) : null,
  description: wooProduct.description,
  shortDescription: wooProduct.short_description,
  images: wooProduct.images.map((img) => ({
    id: img.id,
    src: img.src,
    alt: img.alt || wooProduct.name,
  })),
  categories: wooProduct.categories.map((cat) => ({
    id: cat.id,
    name: cat.name,
    slug: cat.slug,
  })),
  inStock: wooProduct.stock_status === 'instock',
  stockQuantity: wooProduct.stock_quantity,
});

export const fetchProducts = async (): Promise<Product[]> => {
  const response = await fetch(API_ENDPOINTS.PRODUCTS);
  const wooProducts: WooCommerceProduct[] = await response.json();
  
  // Transform each product to internal format
  return wooProducts.map(normalizeProduct);
};
```

### Mapping to Internal Types

```typescript
// src/types/api-responses.ts

// External API response (what the API returns)
export interface WooCommerceProduct {
  id: number;
  name: string;
  slug: string;
  price: string;           // WooCommerce returns strings
  regular_price: string;
  sale_price: string;
  description: string;
  short_description: string;
  stock_status: 'instock' | 'outofstock' | 'onbackorder';
  stock_quantity: number | null;
  images: Array<{
    id: number;
    src: string;
    alt: string;
  }>;
  categories: Array<{
    id: number;
    name: string;
    slug: string;
  }>;
}

// src/types/product.ts

// Internal type (what your app uses)
export interface Product {
  id: number;
  name: string;
  slug: string;
  price: number;           // Converted to number
  regularPrice: number;
  salePrice: number | null;
  description: string;
  shortDescription: string;
  inStock: boolean;        // Simplified boolean
  stockQuantity: number | null;
  images: ProductImage[];
  categories: ProductCategory[];
}
```

### Pagination Handling

#### Cursor-Based Pagination (GraphQL style)

```typescript
export interface CursorPaginatedResponse<T> {
  items: T[];
  hasNextPage: boolean;
  endCursor: string | null;
}

export const fetchWithCursor = async <T>(
  endpoint: string,
  cursor: string | null,
  limit: number
): Promise<CursorPaginatedResponse<T>> => {
  const params = new URLSearchParams({
    first: limit.toString(),
    ...(cursor && { after: cursor }),
  });

  const response = await fetch(`${endpoint}?${params}`);
  const data = await response.json();

  return {
    items: data.nodes,
    hasNextPage: data.pageInfo.hasNextPage,
    endCursor: data.pageInfo.endCursor,
  };
};
```

#### Page-Number Pagination (REST style)

```typescript
export interface PagedResponse<T> {
  items: T[];
  currentPage: number;
  totalPages: number;
  totalItems: number;
}

export const fetchWithPagination = async <T>(
  endpoint: string,
  page: number,
  perPage: number
): Promise<PagedResponse<T>> => {
  const response = await fetch(
    `${endpoint}?page=${page}&per_page=${perPage}`
  );

  const items: T[] = await response.json();
  
  return {
    items,
    currentPage: page,
    totalPages: parseInt(response.headers.get('X-WP-TotalPages') || '1'),
    totalItems: parseInt(response.headers.get('X-WP-Total') || '0'),
  };
};
```

---

## 8. Error Handling Strategy

### Client-Side Error Boundaries

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### Server-Side Error Logging

```typescript
// src/lib/logger.ts

type LogLevel = 'info' | 'warn' | 'error';

interface LogEntry {
  level: LogLevel;
  message: string;
  context?: Record<string, unknown>;
  timestamp: string;
}

export const logger = {
  info: (message: string, context?: Record<string, unknown>) => {
    log('info', message, context);
  },
  warn: (message: string, context?: Record<string, unknown>) => {
    log('warn', message, context);
  },
  error: (message: string, context?: Record<string, unknown>) => {
    log('error', message, context);
  },
};

const log = (level: LogLevel, message: string, context?: Record<string, unknown>) => {
  const entry: LogEntry = {
    level,
    message,
    context,
    timestamp: new Date().toISOString(),
  };

  if (process.env.NODE_ENV === 'development') {
    console[level](JSON.stringify(entry, null, 2));
  } else {
    // In production, send to logging service
    console[level](JSON.stringify(entry));
  }
};
```

### Graceful Degradation Pattern

```typescript
// src/app/(public)/shop/page.tsx

import { fetchProducts } from '@/services/productServices';
import { ProductList } from '@/components/shop/ProductList';
import { EmptyState } from '@/components/common/EmptyState';

export default async function ShopPage() {
  const { items: products, error } = await fetchProducts();

  // Graceful degradation: show empty state instead of crashing
  if (error || products.length === 0) {
    return (
      <EmptyState
        title="No products available"
        description="Please check back later or try refreshing the page."
        action={{
          label: 'Refresh',
          href: '/shop',
        }}
      />
    );
  }

  return <ProductList products={products} />;
}
```

### User-Friendly Error Messages

```typescript
// src/lib/errorMessages.ts

export const ERROR_MESSAGES = {
  // Network errors
  NETWORK_ERROR: 'Unable to connect. Please check your internet connection.',
  TIMEOUT: 'The request took too long. Please try again.',
  
  // Auth errors
  UNAUTHORIZED: 'Please log in to continue.',
  FORBIDDEN: 'You do not have permission to perform this action.',
  
  // Validation errors
  INVALID_INPUT: 'Please check your input and try again.',
  REQUIRED_FIELD: 'This field is required.',
  
  // Resource errors
  NOT_FOUND: 'The requested item could not be found.',
  ALREADY_EXISTS: 'This item already exists.',
  
  // Payment errors
  PAYMENT_FAILED: 'Payment could not be processed. Please try again.',
  CARD_DECLINED: 'Your card was declined. Please use a different payment method.',
  
  // Generic
  UNKNOWN: 'Something went wrong. Please try again later.',
} as const;

export const getErrorMessage = (code: string): string => {
  return ERROR_MESSAGES[code as keyof typeof ERROR_MESSAGES] || ERROR_MESSAGES.UNKNOWN;
};
```

---

## 9. Performance Patterns

### ISR and Revalidation

```typescript
// Static generation with revalidation
export const fetchProducts = async () => {
  const response = await fetch(API_ENDPOINT, {
    next: { 
      revalidate: 3600, // Revalidate every hour
    },
  });
  return response.json();
};

// On-demand revalidation (for admin updates)
// src/app/api/revalidate/route.ts
import { revalidatePath, revalidateTag } from 'next/cache';
import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  const { path, tag, secret } = await request.json();

  // Verify secret
  const expectedSecret = process.env.REVALIDATION_SECRET;
  if (!expectedSecret || typeof secret !== 'string' || secret !== expectedSecret) {
    return NextResponse.json({ error: 'Invalid secret' }, { status: 401 });
  }

  if (path) {
    revalidatePath(path);
  }
  
  if (tag) {
    revalidateTag(tag);
  }

  return NextResponse.json({ revalidated: true });
}
```

### Response Caching

```typescript
// Tag-based caching for granular invalidation
export const fetchProduct = async (slug: string) => {
  const response = await fetch(`${API_ENDPOINT}/${slug}`, {
    next: { 
      tags: ['products', `product-${slug}`],
      revalidate: 3600,
    },
  });
  return response.json();
};

// Invalidate specific product
revalidateTag(`product-${slug}`);

// Invalidate all products
revalidateTag('products');
```

### Selective Field Fetching

```typescript
// GraphQL: Only request needed fields
const MINIMAL_PRODUCT_QUERY = `
  query GetProducts {
    products {
      id
      name
      slug
      price
      images(first: 1) {
        src
      }
    }
  }
`;

// REST: Use _fields parameter if supported
const response = await fetch(
  `${API_ENDPOINT}/products?_fields=id,name,slug,price,images`
);
```

### Batch Operations

```typescript
// Batch multiple IDs into single request
export const fetchProductsByIds = async (ids: number[]): Promise<Product[]> => {
  if (ids.length === 0) return [];
  
  // WooCommerce supports include parameter
  const response = await fetch(
    `${API_ENDPOINT}/products?include=${ids.join(',')}`
  );
  
  return response.json();
};

// Parallel fetching for independent data
export const fetchPageData = async (slug: string) => {
  const [product, relatedProducts, reviews] = await Promise.all([
    fetchProductBySlug(slug),
    fetchRelatedProducts(slug),
    fetchProductReviews(slug),
  ]);

  return { product, relatedProducts, reviews };
};
```

---

## 10. Quick Reference

### Service Function Template

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### API Route Template

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### Common Patterns Cheat Sheet

| Pattern | When to Use | Example |
|---------|-------------|---------|
| Service Layer | All external API calls | `fetchProducts()` |
| API Route Proxy | Protecting credentials | `/api/create-payment-intent` |
| ISR | Static data that changes occasionally | Products, blog posts |
| No-cache | User-specific or real-time data | Cart, inventory |
| Graceful Degradation | Any data fetch | Return empty array on error |
| Type Transformation | External API responses | `normalizeProduct()` |
| Batch Fetching | Multiple independent calls | `Promise.all([...])` |
| Cursor Pagination | GraphQL, infinite scroll | `after: endCursor` |
| Page Pagination | REST APIs, numbered pages | `page=2&per_page=12` |

---

## 11. Webhook Integration Patterns

Webhooks allow external systems to push data to your application in real-time.

### Webhook Endpoint Structure

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Capture the raw request body once. Select exactly one provider-specific signature scheme with its documented header and encoding, verify before parsing, and reject missing or invalid headers. Do not sign reconstructed JSON or chain alternative schemes as cumulative requirements. Test signed whitespace-bearing bodies and malformed or absent signatures.

Distinguish optional telemetry from required follow-up. Complete required work retry-safely or durably enqueue it before acknowledgment. Failed or unconfirmed enqueue returns retryable failure. A later worker failure uses bounded durable retry, visible failed-work state and a named recovery owner. Inspect non-success HTTP responses from follow-up targets; a resolved fetch is not proof of success.

---

### Data Extraction Pattern

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### Webhook Security

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Capture the raw request body once. Select exactly one provider-specific signature scheme with its documented header and encoding, verify before parsing, and reject missing or invalid headers. Do not sign reconstructed JSON or chain alternative schemes as cumulative requirements. Test signed whitespace-bearing bodies and malformed or absent signatures.

---

### Async Follow-Up Pattern (Fire-and-Forget)

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Distinguish optional telemetry from required follow-up. Complete required work retry-safely or durably enqueue it before acknowledgment. Failed or unconfirmed enqueue returns retryable failure. A later worker failure uses bounded durable retry, visible failed-work state and a named recovery owner. Inspect non-success HTTP responses from follow-up targets; a resolved fetch is not proof of success.

---

### Idempotency for Webhooks

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Use the provider’s stable event ID, never a random fallback. Atomically claim each event with in-progress, completed and retryable states; inspect persistence results. Make effects idempotent or transactional. A bounded lease/recovery process reclaims abandoned work and reconciles partial external success without duplicating completed effects.

---

## 12. CRM Integration Patterns

### CRM Service Layer

```typescript
// src/services/crmServices.ts

const CRM_BASE_URL = 'https://services.leadconnectorhq.com';
const CRM_TOKEN = process.env.CRM_ACCESS_TOKEN;
const LOCATION_ID = process.env.CRM_LOCATION_ID;

const crmHeaders = {
  'Authorization': `Bearer ${CRM_TOKEN}`,
  'Content-Type': 'application/json',
  'Version': '2021-07-28',
};

// Fetch all contacts
export const fetchCRMContacts = async (): Promise<Contact[]> => {
  const response = await fetch(
    `${CRM_BASE_URL}/contacts/?locationId=${LOCATION_ID}`,
    { headers: crmHeaders }
  );

  if (!response.ok) {
    throw new Error(`CRM API error: ${response.statusText}`);
  }

  const data = await response.json();
  return data.contacts;
};

// Get single contact
export const fetchCRMContact = async (contactId: string): Promise<Contact> => {
  const response = await fetch(
    `${CRM_BASE_URL}/contacts/${contactId}`,
    { headers: crmHeaders }
  );

  if (!response.ok) {
    throw new Error(`CRM API error: ${response.statusText}`);
  }

  return response.json();
};

// Update contact with custom field
export const updateCRMContactField = async (
  contactId: string,
  fieldId: string,
  value: string
): Promise<void> => {
  const response = await fetch(
    `${CRM_BASE_URL}/contacts/${contactId}`,
    {
      method: 'PUT',
      headers: crmHeaders,
      body: JSON.stringify({
        customFields: [{ id: fieldId, value }],
      }),
    }
  );

  if (!response.ok) {
    throw new Error(`Failed to update CRM contact: ${response.statusText}`);
  }
};
```

### Field Mapping Table Pattern

Map external product IDs to CRM field IDs:

```typescript
// Get field mapping from database
export const getFieldMapping = async (productId: string) => {
  const { data, error } = await supabase
    .from('crm_field_mappings')
    .select('field_id, field_name')
    .eq('product_id', productId)
    .single();

  if (error || !data) {
    throw new Error(`No field mapping found for product: ${productId}`);
  }

  return data;
};

// Usage in webhook processing
const processOrderWebhook = async (data: ExtractedWebhookData) => {
  // 1. Get field mapping for this product
  const fieldMapping = await getFieldMapping(data.productId);

  // 2. Generate asset (QR code, PDF, etc.)
  const assetUrl = await generateAsset(data.orderId);

  // 3. Update CRM contact with asset
  await updateCRMContactField(
    data.contactId,
    fieldMapping.field_id,
    assetUrl
  );
};
```

---

## 13. Data Synchronization Patterns

### Manual Sync with Progress Tracking

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Manual synchronization is an authenticated, role-authorized POST operation with explicit tenant scope. Apply the context’s CSRF protection, rate and concurrency controls. Job acceptance, progress reads and retries enforce the same authorization boundary. GET is read-only and cannot initiate synchronization.

---

### Upsert Pattern for Sync

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### Client-Side Sync Monitoring

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

Manual synchronization is an authenticated, role-authorized POST operation with explicit tenant scope. Apply the context’s CSRF protection, rate and concurrency controls. Job acceptance, progress reads and retries enforce the same authorization boundary. GET is read-only and cannot initiate synchronization.

---

## 14. Integration Quick Reference

### API Route Template

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### Common Patterns Cheat Sheet

| Pattern | When to Use | Example |
|---------|-------------|---------|
| Service Layer | All external API calls | `fetchProducts()` |
| API Route Proxy | Protecting credentials | `/api/create-payment-intent` |
| ISR | Static data that changes occasionally | Products, blog posts |
| No-cache | User-specific or real-time data | Cart, inventory |
| Graceful Degradation | Any data fetch | Return empty array on error |
| Type Transformation | External API responses | `normalizeProduct()` |
| Batch Fetching | Multiple independent calls | `Promise.all([...])` |
| Cursor Pagination | GraphQL, infinite scroll | `after: endCursor` |
| Page Pagination | REST APIs, numbered pages | `page=2&per_page=12` |
| Webhook Endpoint | Receiving external events | `/api/webhooks/stripe` |
| Field Mapping | External system integration | `crm_field_mappings` table |
| Upsert Sync | Data synchronization | `onConflict: 'external_id'` |
| Durable asynchronous work | Required webhook follow-up | Acknowledge only after verified durable acceptance; no unawaited fire-and-forget promise |

---

## Cross-References (Factory Doctrine)

- **`FRONTEND_FIRST_PLAYBOOK.md`** — §0 Kit Audit (MANDATORY before authoring any service — see the Kit Exception in §1) + §5 service-layer law + mock strategy.
- **`STARTER_KIT_HANDBOOK.md`** — the "Should I Author This?" verdict table + the kit's shipped auth (the thing you must not wrap).
- **`AUTH_MANUAL.md`** — §0: the anti-authService doctrine in full.
- **`DATABASE_MANUAL.md`** — the schemas these services consume; RLS interplay.
- **`ECOMMERCE_AND_PAYMENTS_MANUAL.md`** — the WooCommerce/Stripe integration patterns built on this manual's service rules.
- **`TESTING_PLAYBOOK.md`** — unit/integration testing of services (mock-at-the-boundary patterns).

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | (original, date unknown) | Initial manual: service-layer philosophy, folder structure, implementation, API route patterns, external integration, Supabase pattern, transformation, error handling, performance, quick reference, webhooks, CRM integration, data sync. Unversioned until the 2026-07 audit. |
| 1.1 | 2026-07-08 | **Wave 4 (audit sync).** THE KIT EXCEPTION box added at §1 — the Lesson-2 antibody at its root: kit primitives consumed directly, the kit's auth IS the service layer, Kit Audit before authoring any service (F-039 — the blanket rule that produced the Run 001 authService near-miss is now amended at the source). §7 gained the factory wire-format conventions (snake_case wire / camelCase UI; service layer owns the boundary — HANDOFF DATA_CONTRACT discipline). Cross-References section added — outbound-zero ended (F-035). Standard header (F-018) + this history table (D-018). |
| 1.2 | 2026-10-16 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-021, FC-056, FC-057, FC-058, FC-059, FC-061, FC-063, FC-064, FC-066, FC-070, RUL-11 |

---

*This manual is part of the Stark Industries Software Factory documentation suite.*
