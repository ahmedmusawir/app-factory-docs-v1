# APP ARCHITECTURE MANUAL

> **Version:** 1.4 · **Date:** 2026-10-18 · **Status:** Active
> **Tier:** 4 — Reference Manuals · **Pairs with:** STARTER_KIT_HANDBOOK, RECON_QUESTIONNAIRE, AUTH_MANUAL, API_AND_SERVICES_MANUAL, STATE_MANAGEMENT_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL

> **Stark Industries Software Factory**
> *The definitive guide to building scalable Next.js App Router applications.*
> **Born from:** Cyberize Run 001 — Lesson 7 (page composition) + Lesson 8 (server/client boundary)
> **Version rule (v1.3):** this manual does not pin the framework version — the repo's `package.json` is the only truth (recon Q1.1). Version-sensitive facts below are labeled with the version they apply to.

---

## Table of Contents

1. [Architecture Philosophy](#1-architecture-philosophy)
2. [Project Structure](#2-project-structure)
3. [Routing Architecture](#3-routing-architecture)
4. [Layout System](#4-layout-system)
5. [Rendering Strategies](#5-rendering-strategies)
6. [Data Flow Patterns](#6-data-flow-patterns)
7. [Component Architecture](#7-component-architecture)
8. [External Service Integration](#8-external-service-integration)
9. [Performance Patterns](#9-performance-patterns)
10. [Security Architecture](#10-security-architecture)

---

## 1. Architecture Philosophy

### Monolithic Frontend + External Services

This architecture follows a **monolithic frontend** pattern where a single Next.js application serves as the unified interface for multiple backend services.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         NEXT.JS APPLICATION                                  │
│                    (Monolithic Frontend)                                     │
│                                                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Public    │  │   Admin     │  │  Customer   │  │    API      │        │
│  │   Routes    │  │   Portal    │  │   Portal    │  │   Routes    │        │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
            ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
            │  Supabase   │ │ WooCommerce │ │   Stripe    │
            │  (Auth/DB)  │ │  (Products) │ │ (Payments)  │
            └─────────────┘ └─────────────┘ └─────────────┘
                    │               │               │
                    ▼               ▼               ▼
            ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
            │  WordPress  │ │  CRM APIs   │ │  Analytics  │
            │  (Content)  │ │ (Future)    │ │  (Future)   │
            └─────────────┘ └─────────────┘ └─────────────┘
```

### Why This Architecture

| Benefit | Description |
|---------|-------------|
| **Single Deployment** | One codebase, one deployment pipeline |
| **Unified Auth** | Supabase handles all authentication |
| **Flexible Backend** | Swap services without frontend changes |
| **SEO Optimized** | Server-side rendering for public pages |
| **Type Safety** | End-to-end TypeScript |
| **Scalable** | Add new services via API routes |

### Headless Architecture Benefits

- **Decoupled Frontend**: UI independent of backend technology
- **Best-of-Breed Services**: Use specialized tools for each domain
- **Performance**: Optimized frontend without backend constraints
- **Developer Experience**: Modern React/Next.js tooling
- **Future-Proof**: Easy to swap or add services

### Technology Stack Overview

| Layer | Technology | Purpose |
|-------|------------|---------|
| Framework | Next.js App Router (verify version per repo — recon Q1.1) | App Router, SSR, API Routes |
| Language | TypeScript 5 | Type safety |
| Styling | Tailwind CSS 3.4 | Utility-first CSS |
| Components | shadcn/ui | Accessible UI primitives |
| State | Zustand | Client-side state |
| Auth | Supabase | Authentication, RLS |
| Database | Supabase (PostgreSQL) | Data persistence |
| Forms | React Hook Form + Zod | Validation |
| Payments | Stripe | Payment processing |

---

## 2. Project Structure

### Root Directory Layout

```
project-root/
├── .env.local                    # Environment variables (git-ignored)
├── .env.example                  # Environment template
├── next.config.ts                # Next.js configuration
├── tailwind.config.ts            # Tailwind configuration
├── tsconfig.json                 # TypeScript configuration
├── package.json                  # Dependencies
├── README.md                     # Project documentation
│
├── public/                       # Static assets
│   ├── images/
│   ├── fonts/
│   └── favicon.ico
│
├── src/                          # Source code
│   ├── app/                      # App Router (pages, layouts, API)
│   ├── components/               # React components
│   ├── services/                 # Service layer (API calls)
│   ├── store/                    # Zustand stores
│   ├── lib/                      # Utilities and helpers
│   ├── types/                    # TypeScript definitions
│   ├── constants/                # Configuration constants
│   └── utils/                    # Utility functions
│
└── docs/                         # Documentation (optional)
```

### `/src/app/` - App Router

```
src/app/
├── layout.tsx                    # Root layout
├── not-found.tsx                 # Global 404
├── globals.scss                  # Global styles
├── favicon.ico
│
├── (public)/                     # Public routes (no auth required)
│   ├── page.tsx                  # Homepage (/)
│   ├── loading.tsx               # Loading state
│   ├── shop/
│   │   ├── page.tsx              # /shop
│   │   └── [slug]/
│   │       └── page.tsx          # /shop/[slug]
│   ├── blog/
│   │   ├── page.tsx              # /blog
│   │   └── [slug]/
│   │       └── page.tsx          # /blog/[slug]
│   └── ...
│
├── (admin)/                      # Admin routes (auth required)
│   ├── layout.tsx                # Admin layout with sidebar
│   ├── admin-dashboard/
│   │   └── page.tsx              # /admin-dashboard
│   └── ...
│
├── (customers)/                  # Customer routes (auth required)
│   ├── layout.tsx                # Customer layout
│   ├── customer-dashboard/
│   │   └── page.tsx              # /customer-dashboard
│   └── ...
│
├── auth/                         # Auth pages
│   ├── login/
│   │   └── page.tsx              # /auth/login
│   ├── signup/
│   │   └── page.tsx              # /auth/signup
│   └── callback/
│       └── route.ts              # OAuth callback
│
└── api/                          # API routes
    ├── auth/
    │   ├── login/route.ts
    │   ├── logout/route.ts
    │   └── signup/route.ts
    ├── create-payment-intent/
    │   └── route.ts
    ├── place-order/
    │   └── route.ts
    └── webhooks/
        └── stripe/route.ts
```

### `/src/components/` - Component Organization

```
src/components/
├── ui/                           # Base UI primitives (shadcn/ui)
│   ├── button.tsx
│   ├── input.tsx
│   ├── dialog.tsx
│   └── ...
│
├── global/                       # App-wide components
│   ├── Navbar.tsx
│   ├── Footer.tsx
│   ├── MobileNavOverlay.tsx
│   └── ...
│
├── common/                       # Shared utilities
│   ├── Container.tsx
│   ├── Page.tsx
│   ├── Spinner.tsx
│   ├── ErrorBoundary.tsx
│   └── ...
│
├── auth/                         # Auth-related components
│   ├── LoginForm.tsx
│   ├── SignupForm.tsx
│   └── ...
│
├── shop/                         # E-commerce components
│   ├── ProductList.tsx
│   ├── ProductCard.tsx
│   └── product-page/
│       ├── ProductInfo.tsx
│       └── ...
│
├── cart/                         # Cart components
│   ├── CartSlide.tsx
│   └── CartItem.tsx
│
├── checkout/                     # Checkout components
│   ├── left-pane/
│   ├── right-pane/
│   └── payments/
│
└── [domain]/                     # Domain-specific components
```

### `/src/services/` - Service Layer

```
src/services/
├── productServices.ts            # Product API calls
├── orderServices.ts              # Order API calls
├── blogServices.ts               # Blog/content API calls
├── paymentServices.ts            # Payment processing
├── supabaseServices.ts           # Supabase operations
├── <domain>Services.ts           # Approved domain logic; consume kit auth directly
└── index.ts                      # Re-exports
```

### `/src/store/` - State Management

```
src/store/
├── useAuthStore.ts               # Auth state
├── useCartStore.ts               # Cart state
├── useCheckoutStore.ts           # Checkout state
├── useUIStore.ts                 # UI state (modals, sidebars)
└── index.ts                      # Re-exports
```

### `/src/lib/` - Utilities

```
src/lib/
├── utils.ts                      # General utilities (cn, formatters)
├── stripe/
│   ├── client.ts                 # Client-side Stripe
│   └── server.ts                 # Server-side Stripe
└── supabase/
    └── ... (if not in utils/)
```

### `/src/types/` - TypeScript Definitions

```
src/types/
├── product.ts                    # Product types
├── order.ts                      # Order types
├── user.ts                       # User types
├── api-responses.ts              # External API response types
├── supabase.ts                   # Supabase generated types
└── index.ts                      # Re-exports
```

### `/src/constants/` - Configuration

```
src/constants/
├── apiEndpoints.ts               # API endpoint URLs
├── routes.ts                     # App route constants
├── config.ts                     # App configuration
└── index.ts                      # Re-exports
```

---

## 3. Routing Architecture

### File-System Based Routing

The Next.js App Router uses the file system to define routes:

| File | Purpose |
|------|---------|
| `page.tsx` | Route UI |
| `layout.tsx` | Shared layout |
| `loading.tsx` | Loading UI |
| `error.tsx` | Error UI |
| `not-found.tsx` | 404 UI |
| `route.ts` | API endpoint |

### Route Groups

Route groups `(folder)` organize routes without affecting URLs:

```
src/app/
├── (public)/           # Group: public routes
│   ├── page.tsx        # URL: /
│   └── shop/
│       └── page.tsx    # URL: /shop
│
├── (admin)/            # Group: admin routes
│   └── dashboard/
│       └── page.tsx    # URL: /dashboard (not /admin/dashboard)
│
└── (customers)/        # Group: customer routes
    └── orders/
        └── page.tsx    # URL: /orders
```

**Benefits:**
- Organize code by access level
- Share layouts within groups
- No URL pollution

### Dynamic Routes

Use `[param]` for dynamic segments:

```typescript
// src/app/(public)/shop/[slug]/page.tsx

interface Props {
  params: Promise<{ slug: string }>;
}

export default async function ProductPage({ params }: Props) {
  const { slug } = await params;  // Next.js 15+: params is a Promise
  
  const product = await fetchProductBySlug(slug);
  
  if (!product) {
    notFound();
  }
  
  return <ProductPageContent product={product} />;
}
```

### `generateStaticParams` for SSG

Pre-render dynamic routes at build time:

```typescript
// src/app/(public)/shop/[slug]/page.tsx

export async function generateStaticParams() {
  const slugs = await fetchAllProductSlugs();
  
  return slugs.map((slug) => ({
    slug,
  }));
}

// This generates:
// /shop/product-1
// /shop/product-2
// /shop/product-3
// etc.
```

### Async Route Params (Next.js 15+)

**Critical:** From Next.js 15 onward, route params are Promises:

```typescript
// ✅ CORRECT: Next.js 15+
const Page = async ({ params }: { params: Promise<{ slug: string }> }) => {
  const { slug } = await params;
  // ...
};

// ❌ WRONG: Old pattern (Next.js 14 and earlier)
const Page = ({ params }: { params: { slug: string } }) => {
  const { slug } = params;  // This will NOT work on Next.js 15+
  // ...
};
```

### Catch-All Routes

```
src/app/
├── docs/
│   └── [...slug]/
│       └── page.tsx    # Matches /docs/a, /docs/a/b, /docs/a/b/c
│
└── [[...slug]]/
    └── page.tsx        # Optional catch-all (also matches /)
```

---

## 4. Layout System

### Root Layout

Every Next.js app requires a root layout:

```typescript
// src/app/layout.tsx

import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.scss';
import { Navbar } from '@/components/global/Navbar';
import { Footer } from '@/components/global/Footer';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: {
    default: 'Stark App',
    template: '%s | Stark App',
  },
  description: 'Built with the Stark Software Factory',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="flex flex-col min-h-screen">
          <Navbar />
          <main className="flex-1">{children}</main>
          <Footer />
        </div>
      </body>
    </html>
  );
}
```

### Route Group Layouts

Each route group can have its own layout:

**Example withdrawn:** consume the verified responsive kit shell and server-resolved identity props. Client-store role hints are not page authority; navigation must remain reachable on mobile. Every positive layout example keeps every navigation destination reachable at mobile widths. Consume AppShellPage or provide a complete accessible mobile trigger/drawer or equivalent navigation alongside the desktop sidebar. hidden md:block is acceptable only when that same example supplies the mobile alternative. Retire an incomplete layout as a copyable positive example.

### Nested Layouts

Layouts nest automatically:

```
Root Layout (app/layout.tsx)
└── Admin Layout (app/(admin)/layout.tsx)
    └── Dashboard Page (app/(admin)/dashboard/page.tsx)
```

### Layout vs Template

| Feature | Layout | Template |
|---------|--------|----------|
| Re-renders on navigation | No | Yes |
| Preserves state | Yes | No |
| Use case | Persistent UI | Fresh state per page |

```typescript
// src/app/(public)/template.tsx
// Re-renders on every navigation within (public)

export default function PublicTemplate({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="animate-fadeIn">
      {children}
    </div>
  );
}
```

---

## 5. Rendering Strategies

### Server Components (Default)

By default, all components in the App Router are Server Components:

Independent rendering illustration: the `fetchProducts()` used in this section returns `Promise<Product[]>` and is not the API manual §3 typed-outcome service; a project implementing the §3 contract narrows `status === 'success'` and passes `items` to the list.

```typescript
// src/app/(public)/shop/page.tsx
// This is a Server Component (no 'use client' directive)

import { fetchProducts } from '@/services/productServices';
import { ProductList } from '@/components/shop/ProductList';

export default async function ShopPage() {
  // This runs on the server
  const products = await fetchProducts();
  
  return (
    <div className="container mx-auto py-8">
      <h1 className="text-3xl font-bold mb-6">Shop</h1>
      <ProductList products={products} />
    </div>
  );
}
```

**Server Component Benefits:**
- Direct database/API access
- Smaller client bundle
- SEO-friendly
- Secure (secrets stay on server)

### Client Components

Add `'use client'` for interactivity:

```typescript
// src/components/shop/AddToCartButton.tsx
'use client';

import { useState } from 'react';
import { useCartStore } from '@/store/useCartStore';
import { Button } from '@/components/ui/button';

export const AddToCartButton = ({ product }) => {
  const [isAdding, setIsAdding] = useState(false);
  const addItem = useCartStore((state) => state.addItem);
  
  const handleClick = () => {
    setIsAdding(true);
    addItem(product);
    setTimeout(() => setIsAdding(false), 500);
  };
  
  return (
    <Button onClick={handleClick} disabled={isAdding}>
      {isAdding ? 'Added!' : 'Add to Cart'}
    </Button>
  );
};
```

**When to Use Client Components:**
- Event handlers (onClick, onChange)
- useState, useEffect, useRef
- Browser APIs (localStorage, window)
- Zustand stores
- Third-party client libraries

### SSR vs SSG vs ISR Decision Tree

```
START: What kind of data is this?
│
├─► Static content (rarely changes)
│   └─► SSG with generateStaticParams()
│       Example: Blog posts, product pages
│
├─► Dynamic but cacheable (changes occasionally)
│   └─► ISR with revalidate
│       Example: Product catalog, pricing
│       fetch(url, { next: { revalidate: 3600 } })
│
├─► User-specific or real-time
│   └─► SSR (no caching) or Client-side
│       Example: Cart, user dashboard
│       fetch(url, { cache: 'no-store' })
│
└─► Highly interactive
    └─► Client Component with client-side fetch
        Example: Search, filters, infinite scroll
```

### Streaming and Suspense

```typescript
// src/app/(public)/shop/page.tsx

import { Suspense } from 'react';
import { ProductList } from '@/components/shop/ProductList';
import { ProductListSkeleton } from '@/components/shop/ProductListSkeleton';

export default function ShopPage() {
  return (
    <div className="container mx-auto py-8">
      <h1 className="text-3xl font-bold mb-6">Shop</h1>
      
      {/* Stream in product list */}
      <Suspense fallback={<ProductListSkeleton />}>
        <ProductListAsync />
      </Suspense>
    </div>
  );
}

// Async component that fetches data
// Same independent Promise<Product[]> illustration as the Server Component example above.
async function ProductListAsync() {
  const products = await fetchProducts();
  return <ProductList products={products} />;
}
```

---

## 6. Data Flow Patterns

### Server-First Data Fetching

Fetch data in Server Components whenever possible:

```typescript
// src/app/(public)/shop/[slug]/page.tsx

import { fetchProductBySlug } from '@/services/productServices';
import { ProductPageContent } from './ProductPageContent';
import { notFound } from 'next/navigation';

export default async function ProductPage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const product = await fetchProductBySlug(slug);
  
  if (!product) {
    notFound();
  }
  
  // Pass server data to client component
  return <ProductPageContent product={product} />;
}
```

### Client-Side Interactivity

Client components handle user interactions:

```typescript
// src/app/(public)/shop/[slug]/ProductPageContent.tsx
'use client';

import { useState } from 'react';
import { useCartStore } from '@/store/useCartStore';
import type { Product } from '@/types/product';

interface Props {
  product: Product;  // Server-fetched data passed as prop
}

export const ProductPageContent = ({ product }: Props) => {
  const [quantity, setQuantity] = useState(1);
  const [selectedVariation, setSelectedVariation] = useState(null);
  const addItem = useCartStore((state) => state.addItem);
  
  const handleAddToCart = () => {
    addItem({
      productId: product.id,
      name: product.name,
      price: product.price,
      quantity,
      variationId: selectedVariation?.id,
    });
  };
  
  return (
    <div>
      <h1>{product.name}</h1>
      {/* Interactive UI */}
    </div>
  );
};
```

### API Route Proxy Pattern

Protect credentials by proxying through API routes:

```
Client Component
      │
      ▼
API Route (src/app/api/products/route.ts)
      │ (credentials added here)
      ▼
External API (WooCommerce, Stripe, etc.)
```

```typescript
// src/app/api/products/route.ts

import { NextRequest, NextResponse } from 'next/server';

export async function GET(request: NextRequest) {
  // Credentials stay on server
  const response = await fetch(
    `${process.env.WOO_API_URL}/products`,
    {
      headers: {
        Authorization: `Basic ${Buffer.from(
          `${process.env.WOO_KEY}:${process.env.WOO_SECRET}`
        ).toString('base64')}`,
      },
    }
  );
  
  const data = await response.json();
  return NextResponse.json(data);
}
```

### State Synchronization

```
┌─────────────────────────────────────────────────────────────────┐
│                     SERVER STATE                                 │
│   (Database, External APIs)                                      │
│   Source of truth for persistent data                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
        ┌───────────────────┐ ┌───────────────────┐
        │  Server Component │ │    API Route      │
        │  (Initial fetch)  │ │  (Mutations)      │
        └───────────────────┘ └───────────────────┘
                    │                   │
                    └─────────┬─────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     CLIENT STATE                                 │
│   (Zustand stores)                                               │
│   Optimistic updates, UI state                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Component Architecture

### Page Pattern

Every page follows this structure:

```typescript
// src/app/(public)/example/page.tsx (Server Component)

import { fetchData } from '@/services/exampleServices';
import { ExamplePageContent } from './ExamplePageContent';

export const metadata = {
  title: 'Example Page',
  description: 'Example page description',
};

export default async function ExamplePage() {
  const data = await fetchData();
  return <ExamplePageContent data={data} />;
}

// src/app/(public)/example/ExamplePageContent.tsx (Client Component)
'use client';

import { useState } from 'react';

interface Props {
  data: DataType;
}

export const ExamplePageContent = ({ data }: Props) => {
  const [state, setState] = useState(initialState);
  
  return (
    <div>
      {/* Interactive content */}
    </div>
  );
};
```

### Component Organization by Domain

```
src/components/
├── shop/                         # E-commerce domain
│   ├── ProductList.tsx
│   ├── ProductCard.tsx
│   └── product-page/
│       ├── ProductInfo.tsx
│       ├── ProductGallery.tsx
│       └── AddToCartButton.tsx
│
├── blog/                         # Content domain
│   ├── PostList.tsx
│   ├── PostCard.tsx
│   └── post-page/
│       ├── PostContent.tsx
│       └── AuthorBio.tsx
│
└── dashboard/                    # Admin domain
    ├── StatsCard.tsx
    ├── RecentOrders.tsx
    └── charts/
        └── SalesChart.tsx
```

### Shared vs Feature Components

| Location | Purpose | Example |
|----------|---------|---------|
| `components/ui/` | Base primitives | Button, Input, Dialog |
| `components/common/` | Shared utilities | Container, Spinner, ErrorBoundary |
| `components/global/` | App-wide UI | Navbar, Footer, Sidebar |
| `components/[domain]/` | Feature-specific | ProductCard, CartSlide |

### Props Interface Standards

```typescript
// Always define explicit interfaces

interface ProductCardProps {
  product: Product;
  variant?: 'default' | 'compact' | 'featured';
  onAddToCart?: (product: Product) => void;
  className?: string;
}

export const ProductCard = ({
  product,
  variant = 'default',
  onAddToCart,
  className,
}: ProductCardProps) => {
  // ...
};

// Use React.ComponentProps for extending HTML elements
interface ButtonProps extends React.ComponentProps<'button'> {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
}
```

---

## 8. External Service Integration

### REST API Integration

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### GraphQL Integration

**Executable error-handling example withdrawn.** Return a generic client error. Log only an allow-listed structured record: correlation ID, operation, normalized failure class and safe provider code. Exclude raw exceptions, request bodies, credentials, payment details and personal data. A negative test plants synthetic sensitive markers and asserts that neither client output nor retained logs contain them. The Architect includes the API trust-boundary matrix in the acceptance contract; the Engineer supplies engineering results, the QA Executor derives independent checks, and the QA Lead approves and grades them. Cover unauthenticated/wrong-role/wrong-owner calls, forged payment status, tampered totals, duplicate and concurrent requests, invalid signatures, pre-acceptance persistence failure, post-acceptance worker failure, and stale/out-of-order events. Each case records status, absence of unauthorized effects, persisted final state and retry/recovery evidence. TESTING_PLAYBOOK owns the matrix; commerce, subscription and API manuals refer to it. Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results. Implement only against a verified project service contract; distinguish empty success from failure and redact internal/upstream detail from public responses and logs.

### Payment Provider Integration

See `ECOMMERCE_AND_PAYMENTS_MANUAL.md` for detailed Stripe integration.

### Environment Configuration

```typescript
// src/constants/apiEndpoints.ts

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL;

if (!BACKEND_URL) {
  throw new Error('NEXT_PUBLIC_BACKEND_URL is not defined');
}

export const API_ENDPOINTS = {
  // WooCommerce
  PRODUCTS: `${BACKEND_URL}/wp-json/wc/v3/products`,
  ORDERS: `${BACKEND_URL}/wp-json/wc/v3/orders`,
  CATEGORIES: `${BACKEND_URL}/wp-json/wc/v3/products/categories`,
  
  // WordPress
  GRAPHQL: `${BACKEND_URL}/graphql`,
  
  // Internal API routes
  CREATE_PAYMENT_INTENT: '/api/create-payment-intent',
  PLACE_ORDER: '/api/place-order',
} as const;
```

---

## 9. Performance Patterns

### Image Optimization

```typescript
// next.config.ts

import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'your-cdn.com',
        pathname: '/**',
      },
      {
        protocol: 'https',
        hostname: 'your-wordpress.com',
        pathname: '/wp-content/uploads/**',
      },
    ],
  },
};

export default nextConfig;
```

```typescript
// Usage in components
import Image from 'next/image';

<Image
  src={product.image}
  alt={product.name}
  width={400}
  height={400}
  className="object-cover"
  priority={isAboveFold}  // Preload important images
/>
```

### Code Splitting

Next.js automatically code-splits by route. For component-level splitting:

**Example withdrawn:** consume the verified responsive kit shell and server-resolved identity props. Client-store role hints are not page authority; navigation must remain reachable on mobile. Every positive layout example keeps every navigation destination reachable at mobile widths. Consume AppShellPage or provide a complete accessible mobile trigger/drawer or equivalent navigation alongside the desktop sidebar. hidden md:block is acceptable only when that same example supplies the mobile alternative. Retire an incomplete layout as a copyable positive example.

### Caching Strategies

```typescript
// Static data (SSG)
fetch(url);  // Default: cached indefinitely

// Revalidate periodically (ISR)
fetch(url, { next: { revalidate: 3600 } });  // Revalidate every hour

// No caching (SSR)
fetch(url, { cache: 'no-store' });  // Always fresh

// Tag-based revalidation
fetch(url, { next: { tags: ['products'] } });

// Revalidate by tag
import { revalidateTag } from 'next/cache';
revalidateTag('products');
```

### Bundle Optimization

```typescript
// Import only what you need
import { Button } from '@/components/ui/button';  // ✅
import * as UI from '@/components/ui';            // ❌ Imports everything

// Use barrel exports wisely
// src/components/ui/index.ts
export { Button } from './button';
export { Input } from './input';
// Only export what's commonly used together
```

---

## 10. Security Architecture

### Credential Protection

```bash
# .env.local (NEVER commit)

# Public (OK to expose)
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=xxx
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_xxx

# Private (server-only)
SUPABASE_SERVICE_ROLE_KEY=xxx
STRIPE_SECRET_KEY=sk_xxx
WOO_CONSUMER_KEY=ck_xxx
WOO_CONSUMER_SECRET=cs_xxx
```

### Route Protection

**Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.

The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization.

Every privileged operation authorizes its own invocation before acquiring or using elevated capability: authenticate the requester, resolve the current trusted role, authorize the operation and target, and validate input. Layout admission controls page access only. Direct unauthenticated, wrong-role and wrong-target invocations must produce no privileged side effect.

The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

---

### Input Validation

```typescript
// Always validate on server
import { z } from 'zod';

const OrderSchema = z.object({
  items: z.array(z.object({
    productId: z.number().positive(),
    quantity: z.number().min(1).max(100),
  })).min(1),
  email: z.string().email(),
  // ...
});

export async function POST(request: NextRequest) {
  const body = await request.json();
  
  const result = OrderSchema.safeParse(body);
  if (!result.success) {
    return NextResponse.json(
      { error: 'Invalid input', details: result.error.flatten() },
      { status: 400 }
    );
  }
  
  // Proceed with validated data
  const validatedData = result.data;
}
```

### HTTPS Requirements

- All production deployments must use HTTPS
- Payment pages require HTTPS (Stripe requirement)
- Set secure cookie options in production

Session-cookie attributes must follow the verified pinned kit’s session architecture. HTTPS and Secure transport remain required in production; do not impose an unverified HttpOnly architecture on a browser-client session model. Record the verification gap rather than guessing compatible options.

---

## Appendix: Future Considerations

### Admin Portals

When building admin interfaces:

```
src/app/(admin)/
├── layout.tsx              # Admin layout with sidebar
├── dashboard/
│   └── page.tsx            # Overview stats
├── orders/
│   ├── page.tsx            # Order list
│   └── [id]/
│       └── page.tsx        # Order detail
├── products/
│   ├── page.tsx            # Product management
│   └── [id]/
│       └── page.tsx        # Product editor
└── users/
    └── page.tsx            # User management
```

### Background Jobs

For async operations (syncs, notifications):

```typescript
// Option 1: Vercel Cron Jobs
// vercel.json
{
  "crons": [{
    "path": "/api/cron/sync-inventory",
    "schedule": "0 * * * *"  // Every hour
  }]
}

// Option 2: External job queue (Inngest, Trigger.dev)
// src/app/api/inngest/route.ts
import { serve } from 'inngest/next';
import { inngest, syncInventory } from '@/lib/inngest';

export const { GET, POST, PUT } = serve({
  client: inngest,
  functions: [syncInventory],
});
```

### CRM Integration Patterns

For future CRM integrations (GoHighLevel, HubSpot):

```typescript
// src/services/crmServices.ts

export const syncContactToCRM = async (contact: ContactData) => {
  // Same service layer pattern
  // Credentials in env vars
  // Error handling with graceful degradation
};

// src/app/api/webhooks/crm/route.ts
export async function POST(request: NextRequest) {
  // Verify webhook signature
  // Process CRM events
  // Update local state as needed
}
```

---

## 11. Page Composition Pattern (Co-Location Rule)

> **Born from Run 001 Lesson 7.**

Every Next.js App Router page in this factory follows the co-location pattern. This is non-negotiable.

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

### `<Feature>PageContent.tsx` Convention

The PageContent file contains the actual page logic and JSX. It's a Client Component if interactive, Server Component if not.

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

`src/components/<feature>/` is for **cross-page** components ONLY.

### When Components Belong In `src/components/`

| Component Type | Where It Lives |
|---|---|
| `<Feature>PageContent.tsx` (one per page) | Co-located with `page.tsx` |
| Subcomponent used by ONE page only | Co-located with `page.tsx` |
| Subcomponent used by MULTIPLE pages | `src/components/<feature>/` |
| Layout primitive used everywhere | `src/components/common/` |
| Site-wide global component | `src/components/global/` |
| Role-specific sidebar/navbar | `src/components/layout/` |

### Why This Pattern

Co-location keeps page-specific code with the page that owns it:

- When the page is deleted or renamed, the page-specific code goes with it
- When the page is edited, all related code is in one folder
- New developers can find a page's implementation by navigating to its route folder
- Refactoring `src/components/` doesn't affect page-specific code

### Reference Example

Historical external example (availability unverified): The historical worked example of this pattern is at: Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.

- `src/app/(admin)/admin-portal/page.tsx` (thin wrapper)
- `src/app/(admin)/admin-portal/AdminPortalPageContent.tsx` (actual content)

---

## 12. Server / Client Component Boundary (Next.js 16+)

> **Born from Run 001 Lesson 8 (server-only imports in client components).**

In Next.js App Router with Turbopack, the server/client boundary is enforced at the import level. If a `"use client"` component imports a runtime value (enum, const, function) from a module, the ENTIRE module gets bundled for the client.

If that module has server-only imports (`next/headers`, `supabase/server`, server actions), they leak into the client bundle and **`next build` FAILS**.

### The Pattern To Avoid

🛑 **Wrong** — `AppRole` enum mixed with server-only function in one file:

```typescript
// src/utils/get-user-role.ts
import { headers } from "next/headers";  // SERVER-ONLY

export enum AppRole {
  SUPERADMIN = "superadmin",
  ADMIN = "admin",
  MEMBER = "member",
}

export async function getUserRole() {
  const h = await headers();  // SERVER-ONLY
  // ...
}
```

When a Client Component does `import { AppRole } from "@/utils/get-user-role"`, the `headers` import gets bundled for the client and the build fails.

### The Correct Pattern

✅ **Right** — extract shared values to a server-agnostic file:

```typescript
// src/utils/app-role.ts (UNIVERSAL — safe in client or server)
export enum AppRole {
  SUPERADMIN = "superadmin",
  ADMIN = "admin",
  MEMBER = "member",
}
```

```typescript
// src/utils/get-user-role.ts (SERVER-ONLY)
import { headers } from "next/headers";
import { AppRole } from "./app-role";

export async function getUserRole(): Promise<AppRole | null> {
  // server-only logic
}
```

Now Client Components import `AppRole` from `app-role.ts` (universal). Server Components import `getUserRole` from `get-user-role.ts` (server-only).

### The Discipline

When designing utility modules:

- **Pure values (enums, consts, types)** → put in a universal file with ZERO server-only deps
- **Functions that use server-only APIs** → put in a separate file that imports from the universal file
- **Test the boundary** by attempting to import the universal file in a Client Component

### Cross-Reference

- **`STARTER_KIT_HANDBOOK.md` Section "Build & Framework Notes"** — server/client boundary details

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.4 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-001, FC-009, FC-021, FC-028, FC-033, FC-035, FC-036, FC-041, FC-042, FC-063, FC-066, FC-071, MC-01, RUL-11; QA-P4 repair: RV2-F01 (AC16/FC-066 labels) |
| 1.2 | 2026-06-28 | Re-pointed the §11 co-location Reference Example from the deleted `/demo` route to the live `(admin)/admin-portal` page+content pair (preserve lesson, swap actor). Kit Hardening Gate 10. |
| 1.3 | 2026-07-08 | **Wave 4 (audit sync).** Framework version de-pinned (F-038 — this manual was the exact offender RECON §1 was written about): subtitle + stack table + §3 intro now say "Next.js App Router"; version-sensitive facts labeled ("Next.js 15+" for params-as-Promise); header carries the version rule — `package.json` is the only truth (recon Q1.1). §10 Route Protection gains the `src/middleware.ts` vs `src/proxy.ts` (Next 16 kit convention) note with a verify-on-disk pointer (recon Q2.5). Encoding repaired: 21 mojibake sequences (▼/►/✅) + 17 invisible U+0090 C1 controls — a Gate-10 doc whose v1.1 changelog claimed the UTF-8 fix; F-012 systemic diagnosis reconfirmed a third time (the editing pipeline re-corrupts on save). Handbook cross-ref canonical (F-032). Standard header (F-018). |
| 1.1 | 2026-05-31 | Added Section 11 (Page Composition Pattern), Section 12 (Server/Client Boundary). Born from Cyberize Run 001 Lessons 7, 8. Fixed UTF-8 encoding artifacts. |
| 1.0 | (original) | Initial manual |

---

*This manual is part of the Stark Industries Software Factory documentation suite.*

🥄 *App Factory v1.2 doctrine.*
