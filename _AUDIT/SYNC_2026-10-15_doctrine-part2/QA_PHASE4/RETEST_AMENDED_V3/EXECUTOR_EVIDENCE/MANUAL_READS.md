# Independent semantic reads — AMENDED-v3

Candidate: `26b050fe70de66e74ec8d65bcf9287d4369a91f7`; parent: `8dff354937bc7baf739370a9886497d9d5359186`. Quotes below are numbered from the candidate export, which was checked against committed blobs. These are Executor readings, not engineering conclusions.

## Four repaired containers

### V3-1 — Server Components

`04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:495–528`

V3-1 explicitly makes fetchProducts() an independent Promise<Product[]> rendering illustration and excludes the API §3 typed-outcome service. ShopPage awaits that array and passes products directly to ProductList. The same paragraph explains how a project using §3 instead narrows success and passes items. No return-envelope mismatch remains in this container.

````text
495: ## 5. Rendering Strategies
496: 
497: ### Server Components (Default)
498: 
499: By default, all components in the App Router are Server Components:
500: 
501: Independent rendering illustration: the `fetchProducts()` used in this section returns `Promise<Product[]>` and is not the API manual §3 typed-outcome service; a project implementing the §3 contract narrows `status === 'success'` and passes `items` to the list.
502: 
503: ```typescript
504: // src/app/(public)/shop/page.tsx
505: // This is a Server Component (no 'use client' directive)
506: 
507: import { fetchProducts } from '@/services/productServices';
508: import { ProductList } from '@/components/shop/ProductList';
509: 
510: export default async function ShopPage() {
511:   // This runs on the server
512:   const products = await fetchProducts();
513:   
514:   return (
515:     <div className="container mx-auto py-8">
516:       <h1 className="text-3xl font-bold mb-6">Shop</h1>
517:       <ProductList products={products} />
518:     </div>
519:   );
520: }
521: ```
522: 
523: **Server Component Benefits:**
524: - Direct database/API access
525: - Smaller client bundle
526: - SEO-friendly
527: - Secure (secrets stay on server)
528: 
````

### V3-2 — Streaming and Suspense

`04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:590–619`

V3-2 is present at line 613. Its 'Same independent Promise<Product[]> illustration' comment explicitly points to V3-1, whose scope says 'in this section' and excludes the §3 service. ProductListAsync awaits an array and passes it to ProductList. The label changes no import or executable statement. The illustrative fence is not certified as a standalone compiling module.

````text
590: ### Streaming and Suspense
591: 
592: ```typescript
593: // src/app/(public)/shop/page.tsx
594: 
595: import { Suspense } from 'react';
596: import { ProductList } from '@/components/shop/ProductList';
597: import { ProductListSkeleton } from '@/components/shop/ProductListSkeleton';
598: 
599: export default function ShopPage() {
600:   return (
601:     <div className="container mx-auto py-8">
602:       <h1 className="text-3xl font-bold mb-6">Shop</h1>
603:       
604:       {/* Stream in product list */}
605:       <Suspense fallback={<ProductListSkeleton />}>
606:         <ProductListAsync />
607:       </Suspense>
608:     </div>
609:   );
610: }
611: 
612: // Async component that fetches data
613: // Same independent Promise<Product[]> illustration as the Server Component example above.
614: async function ProductListAsync() {
615:   const products = await fetchProducts();
616:   return <ProductList products={products} />;
617: }
618: ```
619: 
````

### V3-3 — Store + Service Layer

`04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:791–830`

The BAD store-local network example stays explicitly negated (line 798). The GOOD service block is separately labelled at 809–810 as an independent store/service-separation illustration returning a raw JSON array, not the §3 typed outcome. response.json() is passed through fetchProducts().then(setProducts); setProducts assigns that array to products. This demonstrates state placement with a stated illustrative array contract; it does not claim that arbitrary endpoint JSON has been runtime-validated.

````text
791: ## 7. Integration Patterns
792: 
793: ### Store + Service Layer
794: 
795: **Keep network calls in services, not stores.** Stores manage state; services fetch data.
796: 
797: ```typescript
798: // ❌ BAD: Network call inside store
799: const useProductStore = create((set) => ({
800:   products: [],
801:   fetchProducts: async () => {
802:     const response = await fetch('/api/products'); // Network call in store!
803:     const data = await response.json();
804:     set({ products: data });
805:   },
806: }));
807: 
808: // ✅ GOOD: Service handles network, store handles state
809: // src/services/productServices.ts — independent store/service-separation illustration
810: // this local fetchProducts() returns the route's raw JSON array; it is not the API manual §3 typed-outcome service
811: export const fetchProducts = async () => {
812:   const response = await fetch('/api/products');
813:   return response.json();
814: };
815: 
816: // src/store/useProductStore.ts
817: export const useProductStore = create((set) => ({
818:   products: [],
819:   setProducts: (products) => set({ products }),
820: }));
821: 
822: // Component orchestrates both
823: const ProductPage = () => {
824:   const setProducts = useProductStore((state) => state.setProducts);
825:   
826:   useEffect(() => {
827:     fetchProducts().then(setProducts);
828:   }, []);
829: };
830: ```
````

### V3-4 — Store + Server Components

`04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:864–909`

V3-4 explicitly declares Promise<Product[]> and excludes the §3 service. The server passes products to initialProducts; the client Props interface requires initialProducts: Product[], initializes the store with it, and maps the resulting products. The label also says a §3 consumer must narrow success and pass outcome.items. The local declared shape and consumer agree.

````text
864: ### Store + Server Components
865: 
866: Server Components cannot use hooks, but they can pass initial data to Client Components: This illustration's `fetchProducts()` returns `Promise<Product[]>` (hence `initialProducts: Product[]`) and is not the API manual §3 typed-outcome service; under that contract, narrow `status === 'success'` and pass `outcome.items`.
867: 
868: ```typescript
869: // src/app/(public)/shop/page.tsx (Server Component)
870: import { fetchProducts } from '@/services/productServices';
871: import { ProductList } from '@/components/shop/ProductList';
872: 
873: export default async function ShopPage() {
874:   const products = await fetchProducts();
875:   
876:   // Pass server data to client component
877:   return <ProductList initialProducts={products} />;
878: }
879: 
880: // src/components/shop/ProductList.tsx (Client Component)
881: 'use client';
882: 
883: import { useEffect } from 'react';
884: import { useProductStore, selectProducts } from '@/store/useProductStore';
885: 
886: interface Props {
887:   initialProducts: Product[];
888: }
889: 
890: export const ProductList = ({ initialProducts }: Props) => {
891:   const products = useProductStore(selectProducts);
892:   const setProducts = useProductStore((state) => state.setProducts);
893:   
894:   // Initialize store with server data on mount
895:   useEffect(() => {
896:     setProducts(initialProducts);
897:   }, [initialProducts, setProducts]);
898:   
899:   return (
900:     <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
901:       {products.map((product) => (
902:         <ProductCard key={product.id} product={product} />
903:       ))}
904:     </div>
905:   );
906: };
907: ```
908: 
909: ### Store + Client Components
````

The full parent→candidate diff has only these label/prose insertions, the one replaced service-path comment, and the history clauses. RAW/edit_accounting.json reverses only the eight declared spans in memory and recovers the parent bytes exactly. RAW/code_preservation.json separately compares every fenced non-line-comment byte and every import in both manuals. No service implementation, import path or executable behavior changed.

## Propagation context

### API §3 invariant and naming vocabulary

`04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:166–185`

The invariant requires one named contract or an explicitly labelled alternative. The naming table has no result shape. This is the authority against which the four repaired containers and every literal hit were read.

````text
166: ## 3. Service Layer Implementation
167: 
168: ### Creating a Service File
169: 
170: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
171: 
172: Services return an explicit typed outcome: success, not-found, unavailable, invalid or forbidden. Routes map it to the approved HTTP/UI behavior with generic client messages and no upstream error text. Do not cache failures as successful public data. Degrade or fail closed according to the module’s approved failure policy; an unavailable entitlement read is not confirmed absence.
173: 
174: Declare wire and internal types separately and normalize once at the service boundary. A named operation uses one parameter signature and typed result envelope in its service, route and client examples. Any independent alternative is explicitly labeled with its own contract; callers do not silently mix array, paginated and wrapped results.
175: 
176: ---
177: 
178: ### Function Naming Conventions
179: 
180: | Action | Prefix | Example |
181: |--------|--------|---------|
182: | Read single | `fetch{Resource}` | `fetchProductBySlug()` |
183: | Read multiple | `fetch{Resources}` or `fetchAll{Resources}` | `fetchProducts()`, `fetchAllProductSlugs()` |
184: | Create | `create{Resource}` | `createOrder()` |
185: | Update | `update{Resource}` | `updateOrderStatus()` |
````

### Independent normalization example

`04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:577–622`

Category (b): the normalization fence explicitly labels its Promise<Product[]> result at 613–614 as independent of the typed-outcome service. Its return maps the external array into Product objects. The module-path comment at 582 belongs to that same labelled fence.

````text
577: ### Normalizing External Responses
578: 
579: External APIs often return data in formats that don't match your internal types. Transform at the service layer:
580: 
581: ```typescript
582: // src/services/productServices.ts
583: 
584: import type { Product } from '@/types/product';
585: import type { WooCommerceProduct } from '@/types/api-responses';
586: 
587: /**
588:  * Transforms WooCommerce product to internal Product type
589:  */
590: const normalizeProduct = (wooProduct: WooCommerceProduct): Product => ({
591:   id: wooProduct.id,
592:   name: wooProduct.name,
593:   slug: wooProduct.slug,
594:   price: parseFloat(wooProduct.price) || 0,
595:   regularPrice: parseFloat(wooProduct.regular_price) || 0,
596:   salePrice: wooProduct.sale_price ? parseFloat(wooProduct.sale_price) : null,
597:   description: wooProduct.description,
598:   shortDescription: wooProduct.short_description,
599:   images: wooProduct.images.map((img) => ({
600:     id: img.id,
601:     src: img.src,
602:     alt: img.alt || wooProduct.name,
603:   })),
604:   categories: wooProduct.categories.map((cat) => ({
605:     id: cat.id,
606:     name: cat.name,
607:     slug: cat.slug,
608:   })),
609:   inStock: wooProduct.stock_status === 'instock',
610:   stockQuantity: wooProduct.stock_quantity,
611: });
612: 
613: // Independent normalization-step example: fetchProducts() returns Promise<Product[]>.
614: // This array-returning step is not the typed-outcome service used by the route below.
615: export const fetchProducts = async (): Promise<Product[]> => {
616:   const response = await fetch(API_ENDPOINTS.PRODUCTS);
617:   const wooProducts: WooCommerceProduct[] = await response.json();
618:   
619:   // Transform each product to internal format
620:   return wooProducts.map(normalizeProduct);
621: };
622: ```
````

### Typed-outcome caller

`04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:785–815`

Category (a): the caller declares the §3 outcome contract at 787, short-circuits on non-success before accessing success items, and passes outcome.items to ProductList. The project-approved public-catalog fallback is explicit.

````text
785: ### Graceful Degradation Pattern
786: 
787: This caller uses the §3 typed-outcome contract: `fetchProducts()` returns a discriminated outcome with `status` equal to `success`, `not-found`, `unavailable`, `invalid` or `forbidden`; only `success` carries `items: Product[]`. This example assumes a project-approved public-catalog failure policy permitting the generic empty-state UI on non-success; this is not an entitlement decision or a cached successful result. It does not call the independent array-returning normalization example.
788: 
789: ```typescript
790: // src/app/(public)/shop/page.tsx
791: 
792: import { fetchProducts } from '@/services/productServices';
793: import { ProductList } from '@/components/shop/ProductList';
794: import { EmptyState } from '@/components/common/EmptyState';
795: 
796: export default async function ShopPage() {
797:   const outcome = await fetchProducts();
798: 
799:   // Apply the declared public-catalog failure policy; do not treat failure as success.
800:   if (outcome.status !== 'success' || outcome.items.length === 0) {
801:     return (
802:       <EmptyState
803:         title="No products available"
804:         description="Please check back later or try refreshing the page."
805:         action={{
806:           label: 'Refresh',
807:           href: '/shop',
808:         }}
809:       />
810:     );
811:   }
812: 
813:   return <ProductList products={outcome.items} />;
814: }
815: ```
````

### Independent ISR example

`04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:854–869`

Category (b): the ISR illustration states raw JSON payload, excludes normalization and the §3 service, and returns response.json(). It supplies no consumer asserting an incompatible array/envelope shape; the wire/failure/cache contract is explicitly left to the project.

````text
854: ## 9. Performance Patterns
855: 
856: ### ISR and Revalidation
857: 
858: Independent ISR example: this `fetchProducts()` returns the endpoint’s raw JSON payload, with no normalization or typed-outcome envelope; it is not the §3 service or the caller above. The project must declare and validate that endpoint’s wire contract and failure/cache policy before implementation; this example only illustrates the revalidation option.
859: 
860: ```typescript
861: // Static generation with revalidation
862: export const fetchProducts = async () => {
863:   const response = await fetch(API_ENDPOINT, {
864:     next: { 
865:       revalidate: 3600, // Revalidate every hour
866:     },
867:   });
868:   return response.json();
869: };
````

### Distinct batch operation

`04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md:942–955`

Category (e): fetchProductsByIds has its own ids: number[] parameter and Promise<Product[]> signature. It is a distinct batch operation, not a conflicting fetchProducts() definition.

````text
942: ### Batch Operations
943: 
944: ```typescript
945: // Batch multiple IDs into single request
946: export const fetchProductsByIds = async (ids: number[]): Promise<Product[]> => {
947:   if (ids.length === 0) return [];
948:   
949:   // WooCommerce supports include parameter
950:   const response = await fetch(
951:     `${API_ENDPOINT}/products?include=${ids.join(',')}`
952:   );
953:   
954:   return response.json();
955: };
````

### Distinct single-product import

`04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:623–650`

Category (e), the assignment's named fetchProductBySlug exception: this is a single-slug lookup, called with slug from params: Promise<{ slug: string }>. The caller checks absence then passes one product to ProductPageContent. The import does not import fetchProducts. This evidence establishes the distinct named operation and explicit caller parameter shape; it does not claim a service return-type declaration exists in this container.

````text
623: 
624: ### Server-First Data Fetching
625: 
626: Fetch data in Server Components whenever possible:
627: 
628: ```typescript
629: // src/app/(public)/shop/[slug]/page.tsx
630: 
631: import { fetchProductBySlug } from '@/services/productServices';
632: import { ProductPageContent } from './ProductPageContent';
633: import { notFound } from 'next/navigation';
634: 
635: export default async function ProductPage({
636:   params,
637: }: {
638:   params: Promise<{ slug: string }>;
639: }) {
640:   const { slug } = await params;
641:   const product = await fetchProductBySlug(slug);
642:   
643:   if (!product) {
644:     notFound();
645:   }
646:   
647:   // Pass server data to client component
648:   return <ProductPageContent product={product} />;
649: }
650: ```
````

## Metadata

### ARCH header

`04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:1–4`

Header remains v1.4, 2026-10-18, Active, exactly equal to the parent.

````text
1: # APP ARCHITECTURE MANUAL
2: 
3: > **Version:** 1.4 · **Date:** 2026-10-18 · **Status:** Active
4: > **Tier:** 4 — Reference Manuals · **Pairs with:** STARTER_KIT_HANDBOOK, RECON_QUESTIONNAIRE, AUTH_MANUAL, API_AND_SERVICES_MANUAL, STATE_MANAGEMENT_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL
````

### STATE header

`04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:1–4`

Header remains v1.3, 2026-10-18, Active, exactly equal to the parent.

````text
1: # STATE MANAGEMENT MANUAL
2: 
3: > **Version:** 1.3 · **Date:** 2026-10-18 · **Status:** Active
4: > **Tier:** 4 — Reference Manuals · **Pairs with:** STARTER_KIT_HANDBOOK, AUTH_MANUAL, FRONTEND_FIRST_PLAYBOOK, APP_ARCHITECTURE_MANUAL
````

### ARCH history

`04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:1285–1293`

Exactly one existing history row, at 1289, gains the RV2-F01 clause. History-row count and every other row remain unchanged.

````text
1285: ## Version History
1286: 
1287: | Version | Date | Changes |
1288: |---|---|---|
1289: | 1.4 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-001, FC-009, FC-021, FC-028, FC-033, FC-035, FC-036, FC-041, FC-042, FC-063, FC-066, FC-071, MC-01, RUL-11; QA-P4 repair: RV2-F01 (AC16/FC-066 labels) |
1290: | 1.2 | 2026-06-28 | Re-pointed the §11 co-location Reference Example from the deleted `/demo` route to the live `(admin)/admin-portal` page+content pair (preserve lesson, swap actor). Kit Hardening Gate 10. |
1291: | 1.3 | 2026-07-08 | **Wave 4 (audit sync).** Framework version de-pinned (F-038 — this manual was the exact offender RECON §1 was written about): subtitle + stack table + §3 intro now say "Next.js App Router"; version-sensitive facts labeled ("Next.js 15+" for params-as-Promise); header carries the version rule — `package.json` is the only truth (recon Q1.1). §10 Route Protection gains the `src/middleware.ts` vs `src/proxy.ts` (Next 16 kit convention) note with a verify-on-disk pointer (recon Q2.5). Encoding repaired: 21 mojibake sequences (▼/►/✅) + 17 invisible U+0090 C1 controls — a Gate-10 doc whose v1.1 changelog claimed the UTF-8 fix; F-012 systemic diagnosis reconfirmed a third time (the editing pipeline re-corrupts on save). Handbook cross-ref canonical (F-032). Standard header (F-018). |
1292: | 1.1 | 2026-05-31 | Added Section 11 (Page Composition Pattern), Section 12 (Server/Client Boundary). Born from Cyberize Run 001 Lessons 7, 8. Fixed UTF-8 encoding artifacts. |
1293: | 1.0 | (original) | Initial manual |
````

### STATE history

`04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:1104–1111`

Exactly one existing history row, at 1111, gains the RV2-F01 clause. History-row count and every other row remain unchanged.

````text
1104: ## Version History
1105: 
1106: | Version | Date | Changes |
1107: |---|---|---|
1108: | 1.0 | (original, date unknown) | Initial manual: three-layer state model, when-to-use table, store architecture, core patterns, persistence, SSR hydration, templates, integration patterns, common stores, best practices. Unversioned until the 2026-07 audit. |
1109: | 1.1 | 2026-07-08 | **Wave 4 metadata patch (audit sync).** Standard header block — this doc was the F-018 worst-case specimen (no version, date, or history anywhere). Cross-References section added — outbound isolation ended (F-035). This history table (D-018). ZERO content changes — the audit verified the doctrine clean (no derived-flag fictions, no `: any`, service-layer-consistent). |
1110: | 1.2 | 2026-08-05 | **Navbar Saga promotion.** Division of Labor subsection appended to §1 (server props vs. client stores hard rule — identity renders from server, stores react to browser events). Cross-ref to AUTH_MANUAL Navbar Law added. | navbar-saga |
1111: | 1.3 | 2026-10-18 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-035, FC-040, FC-046, FC-046-heading, FC-047, FC-048, FC-049, FC-055, FC-067, FC-068, RUL-11, RUL-13; QA-P4 repair: RV2-F01 (AC16/FC-066 labels) |
````

### CHANGELOG amended rows and surrounding prior clauses

`CHANGELOG.md:53–60`

Only rows 56 and 60 gain the RV2-F01 clause. The six AMENDED-v2 clauses at 43,54,55,57,58,59 remain exact; all 39 current-run rows remain in the same table and every other line is unchanged. MANIFEST is byte-identical.

````text
53: | 2026-10-18 | QA_PLAYBOOK v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass | FC-005, FC-025, RUL-03, RUL-12, W14, W15, W16 |
54: | 2026-10-18 | TESTING_PLAYBOOK v2.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | DEC-03, FC-020, FC-021, FC-022, FC-023, FC-024, FC-030, FC-031, FC-040, FC-063, RUL-11, RUL-12, RUL-13 |
55: | 2026-10-18 | API_AND_SERVICES_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-021, FC-056, FC-057, FC-058, FC-059, FC-061, FC-063, FC-064, FC-066, FC-070, RUL-11 |
56: | 2026-10-18 | APP_ARCHITECTURE_MANUAL v1.4 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: RV2-F01 (AC16/FC-066 labels) | FC-001, FC-009, FC-021, FC-028, FC-033, FC-035, FC-036, FC-041, FC-042, FC-063, FC-066, FC-071, MC-01, RUL-11 |
57: | 2026-10-18 | AUTH_MANUAL v1.5 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-001, FC-021, FC-033, FC-034, FC-035, FC-036, FC-038, FC-039, FC-041, FC-042, FC-043, FC-044, FC-063, FC-066, RUL-11 |
58: | 2026-10-18 | DATABASE_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-001, FC-003/096, FC-033, FC-034, FC-036, FC-037, FC-038, FC-039, FC-045, RUL-11 |
59: | 2026-10-18 | ECOMMERCE_AND_PAYMENTS_MANUAL v1.2 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: F01–F05 (AC5/6/9/15/16/18) | FC-047, FC-050, FC-051, FC-052, FC-053, FC-054, FC-055, FC-059, FC-060, FC-062, FC-063, FC-067, FC-068, RUL-11 |
60: | 2026-10-18 | STATE_MANAGEMENT_MANUAL v1.3 | Factory DocSet sync; preserved outgoing original; MC correction pass; QA-P4 repair: RV2-F01 (AC16/FC-066 labels) | FC-035, FC-040, FC-046, FC-046-heading, FC-047, FC-048, FC-049, FC-055, FC-067, FC-068, RUL-11, RUL-13 |
````

## R5′ exact-passage carry-forward

### STATE §4 Persistence

`04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:475–620`

Exact bytes and line numbers match parent git-show output. The persistence example's partialize excludes raw contact fields; line 519 states the default and 520 requires a field/purpose/retention/owner exception. This retains the previously accepted AC18 surface.

````text
475: ## 4. Persistence
476: 
477: ### The `persist` Middleware
478: 
479: Zustand's `persist` middleware automatically saves state to storage and rehydrates on page load.
480: 
481: ```typescript
482: import { create } from 'zustand';
483: import { persist, createJSONStorage } from 'zustand/middleware';
484: 
485: export const useCartStore = create<CartState>()(
486:   persist(
487:     (set, get) => ({
488:       items: [],
489:       addItem: (item) => set((state) => ({ items: [...state.items, item] })),
490:     }),
491:     {
492:       name: 'cart-storage',                              // localStorage key
493:       storage: createJSONStorage(() => localStorage),   // Storage engine
494:     }
495:   )
496: );
497: ```
498: 
499: ### `partialize` - What to Persist
500: 
501: **Never persist everything.** Use `partialize` to select only UX-critical state:
502: 
503: ```typescript
504: export const useCheckoutStore = create<CheckoutState>()(
505:   persist(
506:     (set) => ({
507:       // Persisted
508:       billingAddress: null,
509:       shippingAddress: null,
510:       
511:       // NOT persisted (transient)
512:       isProcessing: false,
513:       validationErrors: {},
514:       paymentIntent: null,
515:     }),
516:     {
517:       name: 'checkout-storage',
518:       partialize: (state) => ({
519:         // Raw contact information is not persisted by default.
520:         // An approved exception must name fields, purpose, retention and owner.
521:         // DO NOT persist: isProcessing, validationErrors, paymentIntent
522:       }),
523:     }
524:   )
525: );
526: ```
527: 
528: #### What to Persist vs What NOT to Persist
529: 
530: | Persist ✅ | Don't Persist ❌ |
531: |-----------|-----------------|
532: | Cart items | Loading states |
533: | User preferences | Validation errors |
534: | Form drafts | API responses |
535: | Selected filters | Temporary UI state |
536: | Theme preference | Payment intents |
537: | Recently viewed | Session tokens |
538: 
539: ### localStorage vs IndexedDB Decision
540: 
541: | Storage | Use When | Limit |
542: |---------|----------|-------|
543: | localStorage | Small data (<5MB), simple values | ~5MB |
544: | IndexedDB (localforage) | Large data, complex objects, offline-first | ~50MB+ |
545: 
546: ```typescript
547: // For large data, use localforage (IndexedDB wrapper)
548: import localforage from 'localforage';
549: import { createJSONStorage } from 'zustand/middleware';
550: 
551: // Configure localforage
552: localforage.config({
553:   name: 'stark-app',
554:   storeName: 'app_state',
555: });
556: 
557: // Custom storage adapter
558: const indexedDBStorage = createJSONStorage(() => ({
559:   getItem: async (name) => {
560:     const value = await localforage.getItem(name);
561:     return value as string | null;
562:   },
563:   setItem: async (name, value) => {
564:     await localforage.setItem(name, value);
565:   },
566:   removeItem: async (name) => {
567:     await localforage.removeItem(name);
568:   },
569: }));
570: 
571: export const useProductCacheStore = create<ProductCacheState>()(
572:   persist(
573:     (set) => ({
574:       products: [],
575:       // ... actions
576:     }),
577:     {
578:       name: 'product-cache',
579:       storage: indexedDBStorage,
580:     }
581:   )
582: );
583: ```
584: 
585: ### Storage Size Considerations
586: 
587: ```typescript
588: // Utility to check storage usage
589: export const getStorageUsage = () => {
590:   let total = 0;
591:   for (const key in localStorage) {
592:     if (localStorage.hasOwnProperty(key)) {
593:       total += localStorage[key].length * 2; // UTF-16 = 2 bytes per char
594:     }
595:   }
596:   return {
597:     bytes: total,
598:     kb: (total / 1024).toFixed(2),
599:     mb: (total / (1024 * 1024)).toFixed(2),
600:   };
601: };
602: 
603: // Clear old/stale data periodically
604: export const cleanupStorage = () => {
605:   const maxAge = 7 * 24 * 60 * 60 * 1000; // 7 days
606:   const now = Date.now();
607: 
608:   // Check each persisted store for staleness
609:   const cartData = localStorage.getItem('cart-storage');
610:   if (cartData) {
611:     const parsed = JSON.parse(cartData);
612:     if (parsed.state?.lastUpdated && now - parsed.state.lastUpdated > maxAge) {
613:       localStorage.removeItem('cart-storage');
614:     }
615:   }
616: };
617: ```
618: 
619: ---
620: 
````

### STATE §5 Hydration & SSR

`04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:621–658`

Exact bytes and line numbers match. Withdrawn hydration examples stay withdrawn; readiness/error recovery remains separate from normal reset. No changed line affects these accepted passages.

````text
621: ## 5. Hydration & SSR
622: 
623: ### The Hydration Problem
624: 
625: In Next.js with SSR, the server renders HTML without access to localStorage. When the client hydrates, there's a mismatch between server-rendered content and client state.
626: 
627: ```
628: Server Render: Cart shows 0 items (no localStorage on server)
629: Client Hydrate: Cart shows 3 items (localStorage has data)
630: Result: Hydration mismatch error!
631: ```
632: 
633: ### Hydration Flags
634: 
635: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
636: 
637: Keep hydration readiness outside the resettable business state. A normal reset preserves readiness. Hydration finishes in ready or error; an error exposes bounded recovery and never leaves an indefinite loading state. Verify reset after hydration, invalid stored data and unavailable storage.
638: 
639: ---
640: 
641: ### `onRehydrateStorage` Callback
642: 
643: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
644: 
645: Keep hydration readiness outside the resettable business state. A normal reset preserves readiness. Hydration finishes in ready or error; an error exposes bounded recovery and never leaves an indefinite loading state. Verify reset after hydration, invalid stored data and unavailable storage.
646: 
647: ---
648: 
649: ### Gating UI on Hydration State
650: 
651: **Dependent executable example withdrawn.** Use a project-approved state/payment contract with explicit hydration errors, server-authoritative pricing, authenticated ownership and recovery. The removed example’s missing contract is still tracked; no universal quote/subscription schema is introduced.
652: 
653: ### Alternative: Hydration-Gated Selection
654: 
655: **Dependent executable example withdrawn.** Use a project-approved state/payment contract with explicit hydration errors, server-authoritative pricing, authenticated ownership and recovery. The removed example’s missing contract is still tracked; no universal quote/subscription schema is introduced.
656: 
657: ---
658: 
````

### STATE §6 Store Templates and RUL-13

`04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:659–790`

Exact bytes and line numbers match. At 779–786 the form/checkout implementation stays withdrawn, raw contact persistence is off by default, and account/sign-out invalidation and payment/authorization exclusions remain. The raw-contact line 519 and the entire 779–786 range were additionally hashed separately.

````text
659: ## 6. Store Templates
660: 
661: ### Basic Store Template
662: 
663: ```typescript
664: // src/store/useBasicStore.ts
665: 
666: import { create } from 'zustand';
667: 
668: interface BasicState {
669:   value: string;
670:   setValue: (value: string) => void;
671:   reset: () => void;
672: }
673: 
674: const initialState = {
675:   value: '',
676: };
677: 
678: export const useBasicStore = create<BasicState>((set) => ({
679:   ...initialState,
680:   setValue: (value) => set({ value }),
681:   reset: () => set(initialState),
682: }));
683: 
684: // Selectors
685: export const selectValue = (state: BasicState) => state.value;
686: ```
687: 
688: ### Persisted Store Template
689: 
690: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
691: 
692: Keep hydration readiness outside the resettable business state. A normal reset preserves readiness. Hydration finishes in ready or error; an error exposes bounded recovery and never leaves an indefinite loading state. Verify reset after hydration, invalid stored data and unavailable storage.
693: 
694: ---
695: 
696: ### Pagination Store Template
697: 
698: ```typescript
699: // src/store/usePaginationStore.ts
700: 
701: import { create } from 'zustand';
702: 
703: // Cursor-based pagination (GraphQL style)
704: interface CursorPaginationState {
705:   endCursor: string | null;
706:   hasNextPage: boolean;
707:   isLoadingMore: boolean;
708:   
709:   setEndCursor: (cursor: string | null) => void;
710:   setHasNextPage: (hasNext: boolean) => void;
711:   setIsLoadingMore: (loading: boolean) => void;
712:   reset: () => void;
713: }
714: 
715: export const useCursorPaginationStore = create<CursorPaginationState>((set) => ({
716:   endCursor: null,
717:   hasNextPage: true,
718:   isLoadingMore: false,
719: 
720:   setEndCursor: (endCursor) => set({ endCursor }),
721:   setHasNextPage: (hasNextPage) => set({ hasNextPage }),
722:   setIsLoadingMore: (isLoadingMore) => set({ isLoadingMore }),
723:   reset: () => set({ endCursor: null, hasNextPage: true, isLoadingMore: false }),
724: }));
725: 
726: // Page-number pagination (REST style)
727: interface PagePaginationState {
728:   currentPage: number;
729:   totalPages: number;
730:   perPage: number;
731:   isLoading: boolean;
732:   
733:   setCurrentPage: (page: number) => void;
734:   setTotalPages: (total: number) => void;
735:   setPerPage: (perPage: number) => void;
736:   setIsLoading: (loading: boolean) => void;
737:   nextPage: () => void;
738:   prevPage: () => void;
739:   reset: () => void;
740: }
741: 
742: export const usePagePaginationStore = create<PagePaginationState>((set, get) => ({
743:   currentPage: 1,
744:   totalPages: 1,
745:   perPage: 12,
746:   isLoading: false,
747: 
748:   setCurrentPage: (currentPage) => set({ currentPage }),
749:   setTotalPages: (totalPages) => set({ totalPages }),
750:   setPerPage: (perPage) => set({ perPage, currentPage: 1 }),
751:   setIsLoading: (isLoading) => set({ isLoading }),
752:   
753:   nextPage: () => {
754:     const { currentPage, totalPages } = get();
755:     if (currentPage < totalPages) {
756:       set({ currentPage: currentPage + 1 });
757:     }
758:   },
759:   
760:   prevPage: () => {
761:     const { currentPage } = get();
762:     if (currentPage > 1) {
763:       set({ currentPage: currentPage - 1 });
764:     }
765:   },
766:   
767:   reset: () => set({ currentPage: 1, totalPages: 1, isLoading: false }),
768: }));
769: 
770: // Selectors
771: export const selectCurrentPage = (state: PagePaginationState) => state.currentPage;
772: export const selectTotalPages = (state: PagePaginationState) => state.totalPages;
773: export const selectCanGoNext = (state: PagePaginationState) => 
774:   state.currentPage < state.totalPages;
775: export const selectCanGoPrev = (state: PagePaginationState) => 
776:   state.currentPage > 1;
777: ```
778: 
779: ### Form/Checkout Store Template
780: 
781: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
782: 
783: Do not persist raw contact details by default. Any approved personal-data persistence declares permitted fields, retention duration and user or guest scope. Sign-out and account transition reset and invalidate every affected store even when remote logout fails; a new account must not hydrate the previous account’s data. Payment and authorization state remain outside persistence. Storage readiness is separate from business-data reset.
784: 
785: Keep hydration readiness outside the resettable business state. A normal reset preserves readiness. Hydration finishes in ready or error; an error exposes bounded recovery and never leaves an indefinite loading state. Verify reset after hydration, invalid stored data and unavailable storage.
786: 
787: The checkout interaction contract includes shippingCost and couponDiscount as display estimates, couponCode, setCoupon(code) and clearCoupon(), alongside the existing checkout fields. The server revalidates shipping and coupons. STATE_MANAGEMENT_MANUAL owns the shared store shape; ECOMMERCE_AND_PAYMENTS_MANUAL refers to it. Personal fields follow the approved account-transition and retention policy.
788: 
789: ---
790: 
````

STATE as a whole is changed. Its first differing line is 809; lines 1–808 are byte-identical with unchanged numbering. TESTING_PLAYBOOK, AUTH_MANUAL and ECOMMERCE_AND_PAYMENTS_MANUAL are whole-file byte-identical to the parent. R5′ is PASS by exact passage, not a false whole-file carry.

## Withdrawal surfaces in changed documents

Other withdrawal rows use the accepted prior manifest and exact document identity. For rows touching ARCH or STATE, the previously graded sections below were located by their actual bytes, re-read and compared; no whole-file identity is claimed.

### Preserved withdrawal section — FC-033

`04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:1012–1023`

This previously accepted withdrawal section is byte-identical at its new location. Re-reading confirms the same containment: role authority and invocation checks, verified session-cookie architecture, responsive navigation, or hydration/contact safeguards remain explicit as applicable. The added fetchProducts labels do not reintroduce a withdrawn implementation.

````text
1012: ### Route Protection
1013: 
1014: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
1015: 
1016: The role table is the only authorization authority. Never authorize from user_metadata or a profile mirror. Superadmin creation is console-only; no app-side superadmin creation route is provided. Retire the metadata-authorized add-user, delete-user and get-users recipes. Future privileged list/delete operations remain possible only with trusted current-role lookup, operation-local authorization before elevated capability, an approved target-role allowlist and privileged-target protection. Profile mirrors contain profile data, not authorization columns. Registration metadata is not authorization.
1017: 
1018: Every privileged operation authorizes its own invocation before acquiring or using elevated capability: authenticate the requester, resolve the current trusted role, authorize the operation and target, and validate input. Layout admission controls page access only. Direct unauthenticated, wrong-role and wrong-target invocations must produce no privileged side effect.
1019: 
1020: The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.
1021: 
1022: ---
1023: 
````

### Preserved withdrawal section — FC-035

`04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:452–457`

This previously accepted withdrawal section is byte-identical at its new location. Re-reading confirms the same containment: role authority and invocation checks, verified session-cookie architecture, responsive navigation, or hydration/contact safeguards remain explicit as applicable. The added fetchProducts labels do not reintroduce a withdrawn implementation.

````text
452: ### Route Group Layouts
453: 
454: Each route group can have its own layout:
455: 
456: **Example withdrawn:** consume the verified responsive kit shell and server-resolved identity props. Client-store role hints are not page authority; navigation must remain reachable on mobile. Every positive layout example keeps every navigation destination reachable at mobile widths. Consume AppShellPage or provide a complete accessible mobile trigger/drawer or equivalent navigation alongside the desktop sidebar. hidden md:block is acceptable only when that same example supplies the mobile alternative. Retire an incomplete layout as a copyable positive example.
457: 
````

### Preserved withdrawal section — FC-042

`04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:1055–1064`

This previously accepted withdrawal section is byte-identical at its new location. Re-reading confirms the same containment: role authority and invocation checks, verified session-cookie architecture, responsive navigation, or hydration/contact safeguards remain explicit as applicable. The added fetchProducts labels do not reintroduce a withdrawn implementation.

````text
1055: ### HTTPS Requirements
1056: 
1057: - All production deployments must use HTTPS
1058: - Payment pages require HTTPS (Stripe requirement)
1059: - Set secure cookie options in production
1060: 
1061: Session-cookie attributes must follow the verified pinned kit’s session architecture. HTTPS and Secure transport remain required in production; do not impose an unverified HttpOnly architecture on a browser-client session model. Record the verification gap rather than guessing compatible options.
1062: 
1063: ---
1064: 
````

### Preserved withdrawal section — FC-047

`04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:633–640`

This previously accepted withdrawal section is byte-identical at its new location. Re-reading confirms the same containment: role authority and invocation checks, verified session-cookie architecture, responsive navigation, or hydration/contact safeguards remain explicit as applicable. The added fetchProducts labels do not reintroduce a withdrawn implementation.

````text
633: ### Hydration Flags
634: 
635: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
636: 
637: Keep hydration readiness outside the resettable business state. A normal reset preserves readiness. Hydration finishes in ready or error; an error exposes bounded recovery and never leaves an indefinite loading state. Verify reset after hydration, invalid stored data and unavailable storage.
638: 
639: ---
640: 
````

### Preserved withdrawal section — FC-047

`04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md:779–790`

This previously accepted withdrawal section is byte-identical at its new location. Re-reading confirms the same containment: role authority and invocation checks, verified session-cookie architecture, responsive navigation, or hydration/contact safeguards remain explicit as applicable. The added fetchProducts labels do not reintroduce a withdrawn implementation.

````text
779: ### Form/Checkout Store Template
780: 
781: **Executable example withdrawn.** The previous example is not an approved implementation. The outgoing archived document preserves it as history. Replacement code requires the project’s approved contract, verified dependency interfaces and behavioral evidence. This withdrawal contains the misleading recipe; it does not certify the underlying finding resolved.
782: 
783: Do not persist raw contact details by default. Any approved personal-data persistence declares permitted fields, retention duration and user or guest scope. Sign-out and account transition reset and invalidate every affected store even when remote logout fails; a new account must not hydrate the previous account’s data. Payment and authorization state remain outside persistence. Storage readiness is separate from business-data reset.
784: 
785: Keep hydration readiness outside the resettable business state. A normal reset preserves readiness. Hydration finishes in ready or error; an error exposes bounded recovery and never leaves an indefinite loading state. Verify reset after hydration, invalid stored data and unavailable storage.
786: 
787: The checkout interaction contract includes shippingCost and couponDiscount as display estimates, couponCode, setCoupon(code) and clearCoupon(), alongside the existing checkout fields. The server revalidates shipping and coupons. STATE_MANAGEMENT_MANUAL owns the shared store shape; ECOMMERCE_AND_PAYMENTS_MANUAL refers to it. Personal fields follow the approved account-transition and retention policy.
788: 
789: ---
790: 
````

