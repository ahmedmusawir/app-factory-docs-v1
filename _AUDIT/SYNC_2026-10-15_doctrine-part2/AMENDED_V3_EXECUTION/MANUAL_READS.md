# FC-066 complete container review

Engineer semantic review, not independent QA acceptance. Each sweep hit points to one full container below. Unknown contexts fail closed; totals are observations, not acceptance criteria.

## 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:178

````text
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

````

## 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:577

````text
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

// Independent normalization-step example: fetchProducts() returns Promise<Product[]>.
// This array-returning step is not the typed-outcome service used by the route below.
export const fetchProducts = async (): Promise<Product[]> => {
  const response = await fetch(API_ENDPOINTS.PRODUCTS);
  const wooProducts: WooCommerceProduct[] = await response.json();
  
  // Transform each product to internal format
  return wooProducts.map(normalizeProduct);
};
```

````

## 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:785

````text
### Graceful Degradation Pattern

This caller uses the §3 typed-outcome contract: `fetchProducts()` returns a discriminated outcome with `status` equal to `success`, `not-found`, `unavailable`, `invalid` or `forbidden`; only `success` carries `items: Product[]`. This example assumes a project-approved public-catalog failure policy permitting the generic empty-state UI on non-success; this is not an entitlement decision or a cached successful result. It does not call the independent array-returning normalization example.

```typescript
// src/app/(public)/shop/page.tsx

import { fetchProducts } from '@/services/productServices';
import { ProductList } from '@/components/shop/ProductList';
import { EmptyState } from '@/components/common/EmptyState';

export default async function ShopPage() {
  const outcome = await fetchProducts();

  // Apply the declared public-catalog failure policy; do not treat failure as success.
  if (outcome.status !== 'success' || outcome.items.length === 0) {
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

  return <ProductList products={outcome.items} />;
}
```

````

## 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:856

````text
### ISR and Revalidation

Independent ISR example: this `fetchProducts()` returns the endpoint’s raw JSON payload, with no normalization or typed-outcome envelope; it is not the §3 service or the caller above. The project must declare and validate that endpoint’s wire contract and failure/cache policy before implementation; this example only illustrates the revalidation option.

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

````

## 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:942

````text
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

````

## 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:981

````text
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

````

## 04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:1175

````text
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

````

## 04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:497

````text
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

````

## 04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:590

````text
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

````

## 04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:624

````text
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

````

## 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:232

````text
### Action Naming Conventions

| Action Type | Prefix | Example |
|-------------|--------|---------|
| Add/Create | `add`, `create` | `addItem`, `createOrder` |
| Remove/Delete | `remove`, `delete` | `removeItem`, `deleteAddress` |
| Update/Set | `update`, `set` | `updateQuantity`, `setShippingMethod` |
| Toggle | `toggle` | `toggleSidebar`, `toggleDarkMode` |
| Clear/Reset | `clear`, `reset` | `clearCart`, `resetCheckout` |
| Fetch/Load | `fetch`, `load` | `fetchProducts`, `loadMore` |

---

````

## 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:793

````text
### Store + Service Layer

**Keep network calls in services, not stores.** Stores manage state; services fetch data.

```typescript
// ❌ BAD: Network call inside store
const useProductStore = create((set) => ({
  products: [],
  fetchProducts: async () => {
    const response = await fetch('/api/products'); // Network call in store!
    const data = await response.json();
    set({ products: data });
  },
}));

// ✅ GOOD: Service handles network, store handles state
// src/services/productServices.ts — independent store/service-separation illustration
// this local fetchProducts() returns the route's raw JSON array; it is not the API manual §3 typed-outcome service
export const fetchProducts = async () => {
  const response = await fetch('/api/products');
  return response.json();
};

// src/store/useProductStore.ts
export const useProductStore = create((set) => ({
  products: [],
  setProducts: (products) => set({ products }),
}));

// Component orchestrates both
const ProductPage = () => {
  const setProducts = useProductStore((state) => state.setProducts);
  
  useEffect(() => {
    fetchProducts().then(setProducts);
  }, []);
};
```

````

## 04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:864

````text
### Store + Server Components

Server Components cannot use hooks, but they can pass initial data to Client Components: This illustration's `fetchProducts()` returns `Promise<Product[]>` (hence `initialProducts: Product[]`) and is not the API manual §3 typed-outcome service; under that contract, narrow `status === 'success'` and pass `outcome.items`.

```typescript
// src/app/(public)/shop/page.tsx (Server Component)
import { fetchProducts } from '@/services/productServices';
import { ProductList } from '@/components/shop/ProductList';

export default async function ShopPage() {
  const products = await fetchProducts();
  
  // Pass server data to client component
  return <ProductList initialProducts={products} />;
}

// src/components/shop/ProductList.tsx (Client Component)
'use client';

import { useEffect } from 'react';
import { useProductStore, selectProducts } from '@/store/useProductStore';

interface Props {
  initialProducts: Product[];
}

export const ProductList = ({ initialProducts }: Props) => {
  const products = useProductStore(selectProducts);
  const setProducts = useProductStore((state) => state.setProducts);
  
  // Initialize store with server data on mount
  useEffect(() => {
    setProducts(initialProducts);
  }, [initialProducts, setProducts]);
  
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};
```

````

