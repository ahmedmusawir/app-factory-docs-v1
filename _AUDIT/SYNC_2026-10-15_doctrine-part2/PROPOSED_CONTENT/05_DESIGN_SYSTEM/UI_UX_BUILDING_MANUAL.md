# UI/UX BUILDING MANUAL

> **Version:** 1.5 · **Date:** 2026-10-16 · **Status:** Active
> **Tier:** 5 — Design System · **Pairs with:** STARTER_KIT_HANDBOOK, COMPONENT_REGISTRY, THEMING_MANUAL, FRONTEND_BUILD_PHASE_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK

> **Project:** Stark SaaS Starter Kit
> **Purpose:** Standardized guide for building pages and components consistently across all projects

---

## ⚡ RULE ZERO — MOBILE-FIRST IS THE FOUNDATIONAL POSTURE

> **If you read no other section of this manual, read this one.**
> Every UI/UX deliverable from Stark Industries is mobile-first.
> This is not a feature, not a verification step, not a polish pass.
> It is the operating posture that the entire manual rests on.

### The Operating Posture

- **Design starts at 375 pixels.** The mobile experience is the canonical version of the UI. Desktop is progressive enhancement on top of mobile, never the other way around.
- **Scale UP from mobile.** Breakpoints add desktop affordances. They never strip mobile features.
- **Layouts that work at desktop but break at mobile are FAILURES**, not "polish needed." They are F-grade work by the operator's standard.
- **Mobile responsiveness is a foundation, not a verification gate.** The mobile sketch comes before the desktop sketch. The mobile breakpoint behavior is in the file's opening JSDoc BEFORE the component is written.

### Required Breakpoints (Non-Negotiable)

| Breakpoint | Width | Behavior |
|---|---|---|
| **Mobile** | 375px | Default; everything works here first |
- **Responsive rail:** determine the fit breakpoint from the pinned component and actual content. Below that breakpoint supply a reachable, keyboard-accessible drawer trigger; no vanished or untriggered sidebar. Verify on both sides of the breakpoint and at 375px. Do not infer a universal `md`, `lg` or `xl` rail rule.
- **Responsive rail:** determine the fit breakpoint from the pinned component and actual content. Below that breakpoint supply a reachable, keyboard-accessible drawer trigger; no vanished or untriggered sidebar. Verify on both sides of the breakpoint and at 375px. Do not infer a universal `md`, `lg` or `xl` rail rule.

Every UI screen MUST be verified at all three breakpoints before phase completion.

### The Grading Rule

> *Any UI/UX design gets an F if it's not mobile responsive.* — Stark

This is not a suggestion. This is the operating standard. It applies at every gate, in every phase, on every component.

### Implementation Discipline

- **Touch targets:** 44 pixels minimum on any interactive element
- **Responsive rail:** determine the fit breakpoint from the pinned component and actual content. Below that breakpoint supply a reachable, keyboard-accessible drawer trigger; no vanished or untriggered sidebar. Verify on both sides of the breakpoint and at 375px. Do not infer a universal `md`, `lg` or `xl` rail rule.
- **Type sizes:** Readable at 375px without zoom (no smaller than 14px body text)
- **Spacing:** Tap-friendly padding, not pixel-economy
- **No unintended page-level horizontal overflow** below desktop; bounded intentional tabs/carousels are permitted with accessible controls.
- **All controls reachable** at mobile (no "desktop only" UI hidden at mobile)

### What Violates Rule Zero

These are AUTOMATIC FAILURES at any phase gate:

1. **Fixed-width sidebars** (`w-64`, `w-72`) without responsive collapse to hamburger/slide-over
2. **Layouts that overflow horizontally** at 375px
3. **Touch targets smaller than 44px** on any interactive element
4. **Text or controls hidden at mobile** but available at desktop
5. **"We'll fix mobile later"** attitude — this is the deferred-violation pattern. Catch the first time, surface immediately, refuse to advance.
6. **No mobile sketch in the plan** — if the plan doesn't describe the 375px layout, the file is not authored

### How To Honor Rule Zero In Authoring

Before authoring any UI component, page, or layout, answer in the file's opening JSDoc:

1. **What's the 375px sketch?** (1-3 sentences describing the mobile layout)
2. **What changes at 768px?** (the tablet/md breakpoint behavior)
3. **What changes at 1024px?** (the desktop/lg breakpoint behavior)
4. **Are all touch targets ≥ 44px?** (yes/no with note if exceptions exist)

If you cannot answer all four, STOP — surface to the operator. The file is not authored until the mobile-first contract is explicit.

### Cross-Reference

- **`STARTER_KIT_HANDBOOK.md`** — kit primitives that are already mobile-first (AppShellPage, Sheet, etc.)
- **`COMPONENT_REGISTRY.md`** — per-primitive mobile behavior reference
- **`FRONTEND_BUILD_PHASE_PLAYBOOK.md`** — phase preambles that re-inject mobile-first at execution moments

### Why Rule Zero Supersedes Other Doctrine

If another section of this manual or another factory doc conflicts with Rule Zero, surface the conflict immediately — **Rule Zero wins**. Mobile-first is foundational, not negotiable. All other patterns and conventions in this manual are layered on top of the mobile-first foundation.

---

## 🎨 RULE ZERO-B — THEMING IS THE SECOND FOUNDATIONAL POSTURE

> **Companion to Rule Zero (mobile-first). If Rule Zero says "design for 375 pixels first," Rule Zero-B says "design tokens before pixels."**
> Every UI/UX deliverable from Stark Industries reads colors from semantic tokens, never from hardcoded values.
> This posture exists so brand iteration is a five-minute operation, not an hour-long refactor.

### The Operating Posture

- **Every color in every component reads from a semantic token.** Tokens are CSS custom properties declared in `src/app/globals.css` and mapped through `tailwind.config.ts`.
- **No hardcoded hex codes in component files.** Not in inline styles. Not in Tailwind utility classes that bypass tokens. Not in CSS files outside `globals.css`.
- **Light mode AND dark mode tokens declared from Phase 1.** Both sets coexist in the same file; the browser picks which renders.
- **The designer's executable deliverable is the tokens file, not a Figma export.** Figma is for human communication; tokens are for fabrication.

### Required Semantic Tokens (Minimum)

Every Stark project declares these tokens (matching shadcn convention so the kit ecosystem works out of the box):

`--background`, `--foreground`, `--primary`, `--primary-foreground`, `--secondary`, `--secondary-foreground`, `--accent`, `--accent-foreground`, `--muted`, `--muted-foreground`, `--card`, `--card-foreground`, `--popover`, `--popover-foreground`, `--border`, `--input`, `--ring`, `--destructive`, `--destructive-foreground`

Additional tokens (`--success`, `--warning`) may be added when a real project need surfaces. Resist token sprawl.

### What Violates Rule Zero-B

These are AUTOMATIC FAILURES at any phase gate:

1. **Hardcoded hex codes in component files** (e.g., `bg-[#3b82f6]`, `style={{ color: "#000" }}`)
2. **Tailwind color names that bypass tokens** (e.g., `bg-blue-500` instead of `bg-primary`)
3. **Light mode only** — tokens declared in `:root` with no `.dark` override set
4. **Designer delivers only a Figma file** — no executable tokens file provided
5. **Component overrides the palette silently** — fabricator bypasses a token "because it didn't fit" instead of surfacing the token as wrong

### How To Honor Rule Zero-B In Authoring

Before authoring any UI component, page, or layout:

1. **Identify which semantic tokens this component needs** (e.g., a button needs `--primary` and `--primary-foreground`)
2. **Use the token via the Tailwind utility class** (`bg-primary text-primary-foreground`)
3. **Never reach for a literal color value** — if the design calls for a color outside the current tokens, surface to the operator before bypassing the system

### Cross-Reference

- **`THEMING_MANUAL.md`** — the deep dive on token architecture, designer deliverable format, and quick-swap workflow
- **`TOKEN_FILE.md`** §1 Entry stylesheet — where the token files live in the repo
- **`GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`** §8 The Designer’s deliverables — the designer engagement spec
- Historical external example (availability unverified): **Cyberize Run 001 `_project/CLAUDE.md`** — the historical worked example of a Locked Palette table Obtain the source repository, immutable revision and path before use; do not assume this path exists locally.

### Why Rule Zero-B Supersedes Other Color Doctrine

If another section of this manual or another factory doc specifies a literal color value instead of a token reference, the conflict resolves in favor of Rule Zero-B. **Tokens are the contract.** Surface the conflict to the operator and update the other doc.

> **Note on §10.5 (Dark Mode Best Practices) and §10.8 (Do's and Don'ts):** Those sections already endorse semantic tokens and forbid hardcoded hex. Rule Zero-B promotes that guidance to foundational-posture status and makes it enforceable at every phase gate, not just a best practice.

---

## Philosophy & Approach

This manual documents the **proven patterns** used in this starter kit. The goal is to build apps **faster and better** by:

1. **Separating concerns** - Keep `page.tsx` minimal, content in dedicated files
2. **Reusing components** - Use common layout components for consistency
3. **Mobile-first responsive** - Every layout must work on all screen sizes
4. **Consistent naming** - Follow strict file and component naming conventions
5. **Composition over complexity** - Build with simple, composable pieces

**Core Principle:** If vibe coders can ship fast without deep knowledge, we as engineers should ship **faster and better** with our structured approach.

---

## Table of Contents

0. [Rule Zero — Mobile-First Is The Foundational Posture](#-rule-zero--mobile-first-is-the-foundational-posture)
0-B. [Rule Zero-B — Theming Is The Second Foundational Posture](#-rule-zero-b--theming-is-the-second-foundational-posture)
1. [Folder Structure](#folder-structure)
2. [Common Components (Reusable Building Blocks)](#common-components)
3. [Global Components (Site-Wide)](#global-components)
4. [Layout Components (Navigation)](#layout-components)
5. [Page Building Pattern](#page-building-pattern)
6. [File Naming Conventions](#file-naming-conventions)
7. [Responsive Design Patterns](#responsive-design-patterns)
8. [Complete Page Examples](#complete-page-examples)
9. [Quick Reference Checklist](#quick-reference-checklist)
10. [Suggestions for Improvement](#suggestions-for-improvement)

---

## Folder Structure

### Component Organization

```
src/components/
├── common/              # Reusable layout primitives (Page, Row, Box, etc.)
├── global/              # Site-wide components (Navbar, ThemeToggle)
├── layout/              # Navigation components (Sidebar, AdminSidebar)
├── ui/                  # shadcn/ui components (Button, Card, etc.)
├── auth/                # Authentication components
├── admin/               # Admin-specific components
├── members/             # Member-specific components
└── [feature]/           # Feature-specific components
```

### App Directory Organization

```
src/app/
├── (public)/            # Public routes (no auth required)
│   ├── page.tsx         # Minimal - imports PageContent
│   └── PageContent.tsx  # Actual content implementation
├── (auth)/              # Auth routes
├── (members)/           # Member-protected routes
│   ├── layout.tsx       # Navbar + Sidebar layout
│   └── members-portal/
│       ├── page.tsx
│       └── MembersPortalPageContent.tsx
├── (admin)/             # Admin-protected routes
│   ├── layout.tsx       # Navbar + AdminSidebar layout
│   └── admin-portal/
│       ├── page.tsx
│       └── AdminPortalPageContent.tsx
└── (superadmin)/        # Superadmin-protected routes
    ├── layout.tsx
    └── superadmin-portal/
        ├── page.tsx
        └── SuperadminPortalPageContent.tsx
```

---

## Common Components

These are your **building blocks** for every page. Located in `src/components/common/`.

### 1. Page Component

**Purpose:** Main page container with responsive width control

**File:** `src/components/common/Page.tsx`

```typescript
interface Props {
  children: ReactNode;
  FULL: boolean;           // true = full width, false = centered with margins
  className?: string;
  customYMargin?: string;  // Override default "my-10"
}
```

**Usage:**
```tsx
// Centered page with auto margins (most common)
<Page FULL={false} className="">
  {/* content */}
</Page>

// Full-width page
<Page FULL={true} className="">
  {/* content */}
</Page>

// Custom vertical margin
<Page FULL={false} customYMargin="my-20">
  {/* content */}
</Page>
```

**Responsive Behavior:**
- `FULL={false}`: Width is `w-11/12` (91%) on all screens, centered with `mx-auto`
- `FULL={true}`: Full width `min-w-full`
- Default vertical margin: `my-10`

---

### 2. Row Component

**Purpose:** Horizontal container for grouping content

**File:** `src/components/common/Row.tsx`

```typescript
interface Props {
  children: ReactNode;
  className?: string;
}
```

**Usage:**
```tsx
// Basic row
<Row className="">
  <h1>Title</h1>
  <p>Content</p>
</Row>

// Row with flex layout
<Row className="flex flex-wrap">
  <Box>Item 1</Box>
  <Box>Item 2</Box>
</Row>

// Row with grid
<Row className="grid grid-cols-1 md:grid-cols-3 gap-4">
  <Box>Card 1</Box>
  <Box>Card 2</Box>
  <Box>Card 3</Box>
</Row>
```

**Default Styles:**
- `min-w-full` - Takes full width
- `p-5` - Padding on all sides

---

### 3. Box Component

**Purpose:** Generic container for any content (most flexible)

**File:** `src/components/common/Box.tsx`

```typescript
interface Props {
  children: ReactNode;
  className?: string;
}
```

**Usage:**
```tsx
// Simple box
<Box className="p-5">
  <p>Content</p>
</Box>

// Box with fixed width (responsive cards)
<Box className="w-80 p-5">
  <img src="..." />
  <p>Card content</p>
</Box>

// Box in grid
<Box className="p-3">
  <img src="..." className="mb-3 min-w-full rounded-full" />
  <p>Text</p>
</Box>
```

**Key Points:**
- No default styles (completely customizable)
- Use for cards, content blocks, grid items
- Add your own width, padding, margins via className

---

### 4. Container Component

**Purpose:** Similar to Page but for nested sections

**File:** `src/components/common/Container.tsx`

```typescript
interface Props {
  children: ReactNode;
  className: string;       // Required
  FULL: boolean;
}
```

**Usage:**
```tsx
<Container FULL={false} className="my-8">
  {/* nested content */}
</Container>
```

**Note:** Less commonly used than Page. Use Page for top-level, Container for nested sections.

---

### 5. Main Component

**Purpose:** Semantic `<main>` wrapper with flex-grow

**File:** `src/components/common/Main.tsx`

```typescript
interface Props {
  children: ReactNode;
  className: string;       // Required
}
```

**Usage:**
```tsx
<Main className="bg-muted">
  {/* page content */}
</Main>
```

**Default Styles:**
- `min-w-full flex flex-grow` - Takes full width and grows to fill space

---

### 6. BackButton Component

**Purpose:** Consistent back navigation button

**File:** `src/components/common/BackButton.tsx`

```typescript
interface BackButtonProps {
  text: string;
  link: string;
}
```

**Usage:**
```tsx
<BackButton text="Go Back" link="/admin-portal" />
```

**Renders:** Link with arrow icon and hover effect

---

### 7. Spinner Component

**Purpose:** Loading indicator

**File:** `src/components/common/Spinner.tsx`

**Usage:**
```tsx
{isLoading && <Spinner />}
```

**Renders:** Centered animated spinner with accessibility support

---

## Global Components

Site-wide components used across all pages. Located in `src/components/global/`.

### Navbar Components

**Files:**
- `Navbar.tsx` - Default navbar (members/admin/superadmin portals)
- `PublicNav.tsx` - Public marketing navbar (with `PublicMobileNav.tsx` for the mobile sheet)
- `NavbarLoginReg.tsx` - Auth pages navbar

**Common Features:**
- User authentication state display
- Avatar dropdown with profile/logout
- Theme toggler integration
- Active link highlighting
- Responsive design (hidden on mobile, visible on md+)

**Usage in Layouts:**
**Guard-call example withdrawn pending pinned-kit verification.** The kit guard’s async signature, role lookup, AppRole import and { user, role } return contract must be verified together against the pinned kit revision before a replacement recipe is published. Deny by default and never accept a caller-supplied role. Until that evidence is supplied, do not present mismatched signatures as executable kit guidance.

---

### ThemeToggle Component

**File:** `src/components/global/ThemeToggle.tsx`

**Purpose:** Light/dark/system theme switcher (dropdown via next-themes)

**Usage:**
```tsx
import ThemeToggle from "@/components/global/ThemeToggle";

<ThemeToggle />
```

**Included on every navbar surface** (`Navbar`, `PublicNav`, `NavbarLoginReg`).

---

## Layout Components

Navigation sidebars for different user roles. Located in `src/components/layout/`.

### Sidebar Component (Members)

Every positive layout example keeps every navigation destination reachable at mobile widths. Consume AppShellPage or provide a complete accessible mobile trigger/drawer or equivalent navigation alongside the desktop sidebar. hidden md:block is acceptable only when that same example supplies the mobile alternative. Retire an incomplete layout as a copyable positive example.

The former copyable layout is withdrawn because it hid navigation on small screens or bypassed the installed shell. Use the verified responsive shell/rail/drawer contract for the pinned kit; do not invent a breakpoint or duplicate the shell. Verify reachable navigation, focus management, keyboard/escape behavior and no page overflow at every supported width.

---

### AdminSidebar Component

Every positive layout example keeps every navigation destination reachable at mobile widths. Consume AppShellPage or provide a complete accessible mobile trigger/drawer or equivalent navigation alongside the desktop sidebar. hidden md:block is acceptable only when that same example supplies the mobile alternative. Retire an incomplete layout as a copyable positive example.

The former copyable layout is withdrawn because it hid navigation on small screens or bypassed the installed shell. Use the verified responsive shell/rail/drawer contract for the pinned kit; do not invent a breakpoint or duplicate the shell. Verify reachable navigation, focus management, keyboard/escape behavior and no page overflow at every supported width.

---

## Page Building Pattern

### The Two-File Pattern

**Every page follows this structure:**

```
feature-name/
├── page.tsx              # Minimal wrapper (3-8 lines)
└── FeatureNamePageContent.tsx  # Actual implementation
```

### Step 1: Create Minimal page.tsx

**File:** `src/app/(group)/feature-name/page.tsx`

```tsx
import type { Metadata } from "next";
import FeatureNamePageContent from "./FeatureNamePageContent";

// App Router: page-level title/meta live here, NOT in a next/head inside the content.
export const metadata: Metadata = {
  title: "Feature Name",
  description: "Description of the page",
};

const FeatureName = () => {
  return <FeatureNamePageContent />;
};

export default FeatureName;
```

**Rules:**
- Keep it minimal (3-8 lines max)
- Only imports and returns the PageContent component
- Component name matches the feature (PascalCase)
- No logic, no styling, no data fetching here

---

### Step 2: Create PageContent Component

**File:** `src/app/(group)/feature-name/FeatureNamePageContent.tsx`

```tsx
import Page from "@/components/common/Page";
import Row from "@/components/common/Row";
import Box from "@/components/common/Box";
import { Button } from "@/components/ui/button";

// Title/meta live in page.tsx via `export const metadata` (App Router) — not here.
const FeatureNamePageContent = () => {
  return (
    <Page FULL={false} className="">
        <Row className="">
          <h1 className="h1">Page Title</h1>
          {/* content */}
        </Row>
        
        <Row className="flex flex-wrap">
          <Box className="w-80 p-5">
            {/* card content */}
          </Box>
        </Row>
      </Page>
  );
};

export default FeatureNamePageContent;
```

**Structure:**
1. **Page metadata** - title/description via `export const metadata` in `page.tsx`
2. **Page wrapper** - Controls page width
3. **Row sections** - Organize content horizontally
4. **Box components** - Individual content blocks

---

## File Naming Conventions

### Strict Rules

| Type | Pattern | Example |
|------|---------|---------|
| Page wrapper | `page.tsx` | `page.tsx` |
| Page content | `[FeatureName]PageContent.tsx` | `AdminPortalPageContent.tsx` |
| Layout | `layout.tsx` | `layout.tsx` |
| Component | `[ComponentName].tsx` | `BackButton.tsx` |
| Sidebar | `[Role]Sidebar.tsx` | `AdminSidebar.tsx` |
| Navbar | `Navbar[Variant].tsx` | `NavbarLoginReg.tsx` |

### Examples

**✅ Correct:**
```
admin-portal/
├── page.tsx
└── AdminPortalPageContent.tsx

members-portal/
├── page.tsx
└── MembersPortalPageContent.tsx

user-profile/
├── page.tsx
└── UserProfilePageContent.tsx
```

**❌ Incorrect:**
```
admin-portal/
├── page.tsx
└── content.tsx              # Too generic

members-portal/
├── index.tsx                # Wrong name
└── MembersPortal.tsx        # Missing "PageContent"
```

---

## Responsive Design Patterns

### Mobile-First Approach

**Always build mobile-first, then add breakpoints:**

```tsx
// Mobile: stack vertically
// Tablet+: 2 columns
// Desktop: 3 columns
<Row className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  <Box>Item 1</Box>
  <Box>Item 2</Box>
  <Box>Item 3</Box>
</Row>
```

### Tailwind Breakpoints

| Breakpoint | Min Width | Usage |
|------------|-----------|-------|
| `sm:` | 640px | Small tablets |
| `md:` | 768px | Tablets |
| `lg:` | 1024px | Laptops |
| `xl:` | 1280px | Desktops |
| `2xl:` | 1536px | Large screens |

---

### Common Responsive Patterns

#### 1. Hide/Show Elements

```tsx
// Hidden on mobile, visible on tablet+
<div className="hidden md:block">
  <Sidebar />
</div>

// Visible on mobile, hidden on tablet+
<div className="block md:hidden">
  <MobileMenu />
</div>
```

#### 2. Responsive Flexbox

```tsx
// Stack on mobile, row on desktop
<Row className="flex flex-col md:flex-row gap-4">
  <Box>Left</Box>
  <Box>Right</Box>
</Row>

// Wrap items responsively
<Row className="flex flex-wrap">
  <Box className="w-full md:w-1/2 lg:w-1/3">Item</Box>
</Row>
```

#### 3. Responsive Grid (Recommended)

```tsx
// 1 column mobile, 2 tablet, 3 laptop, 4 desktop, 5 large screens
<Row className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
  <Box className="p-3">
    <img src="..." className="mb-3 min-w-full rounded-full" />
    <p>Content</p>
  </Box>
  {/* repeat */}
</Row>
```

#### 4. Auto-Fit Grid (Plugin)

**Uses:** `@shrutibalasa/tailwind-grid-auto-fit`

```tsx
// Automatically fits items based on min-width (250px default)
<Row className="grid gap-3 grid-auto-fit p-3">
  <Box className="p-3">
    <img src="..." />
    <p>Content</p>
  </Box>
  {/* items auto-arrange */}
</Row>
```

**Benefits:**
- No breakpoint management needed
- Items automatically wrap
- Maintains consistent sizing

---

### Responsive Width Patterns

#### Fixed Width Cards

```tsx
// Cards with fixed width, wrap on overflow
<Row className="flex flex-wrap">
  <Box className="w-80 p-5">Card 1</Box>
  <Box className="w-80 p-5">Card 2</Box>
  <Box className="w-80 p-5">Card 3</Box>
</Row>
```

#### Percentage Width

```tsx
// Full width on mobile, half on tablet, third on desktop
<Box className="w-full md:w-1/2 lg:w-1/3 p-5">
  Content
</Box>
```

#### Max Width Containers

```tsx
// Prose content with max width
<Row className="prose max-w-3xl mx-auto">
  <h1>Article Title</h1>
  <p>Long form content...</p>
</Row>
```

---

### Responsive Images

```tsx
// Full width, responsive height, rounded
<img 
  src="https://picsum.photos/id/12/350/300" 
  className="mb-3 min-w-full rounded-full" 
  alt="Description"
/>

// Next.js Image component (preferred)
<Image
  src="/path/to/image.jpg"
  alt="Description"
  width={350}
  height={300}
  className="mb-3 w-full rounded-full"
/>
```

---

### Layout Patterns

#### Sidebar Layout (Desktop Only)

Every positive layout example keeps every navigation destination reachable at mobile widths. Consume AppShellPage or provide a complete accessible mobile trigger/drawer or equivalent navigation alongside the desktop sidebar. hidden md:block is acceptable only when that same example supplies the mobile alternative. Retire an incomplete layout as a copyable positive example.

The former copyable layout is withdrawn because it hid navigation on small screens or bypassed the installed shell. Use the verified responsive shell/rail/drawer contract for the pinned kit; do not invent a breakpoint or duplicate the shell. Verify reachable navigation, focus management, keyboard/escape behavior and no page overflow at every supported width.

---

## Complete Page Examples

### Example 1: Content-Flow Page (Public Home)

**File:** `src/app/(public)/page.tsx` — the kit's real marketing home, a content-flow
page built from `Page` + `Row` + `Box` (live on disk; excerpt below).

```tsx
import Link from "next/link";
import Page from "@/components/common/Page";
import Row from "@/components/common/Row";
import Box from "@/components/common/Box";
import { Button } from "@/components/ui/button";

const HomePage = () => {
  return (
    <Page FULL={false} className="">
      {/* Hero — content-flow split happens at lg (1024), not md */}
      <Row className="text-center py-12 lg:py-24">
        <h1 className="text-4xl lg:text-6xl font-bold tracking-tight">Your Product</h1>
        <p className="mt-6 text-lg text-muted-foreground max-w-2xl mx-auto">
          A neutral starter for what you&apos;re building next.
        </p>
        <div className="mt-8 flex flex-col lg:flex-row gap-3 justify-center items-center">
          <Button asChild><Link href="/auth">Get started</Link></Button>
          <Button asChild variant="outline">
            <Link href="/members-portal">Explore the portals</Link>
          </Button>
        </div>
      </Row>

      {/* Feature grid — 1 col mobile, 3 cols at lg */}
      <Row className="py-12 lg:py-16">
        <div className="grid gap-6 grid-cols-1 lg:grid-cols-3">
          <Box className="rounded-lg border border-border bg-card text-card-foreground p-6">
            <h3 className="text-lg font-semibold mb-2">Role-based access</h3>
            <p className="text-sm text-muted-foreground">Three-tier RBAC, wired end-to-end.</p>
          </Box>
          {/* …two more Box cards… */}
        </div>
      </Row>
    </Page>
  );
};

export default HomePage;
```

**Key Patterns:**
- `Page FULL={false}` for a centered content-flow column; `Row` sections stack vertically; `Box` for bordered cards
- **Token-driven colors only** (`text-muted-foreground`, `bg-card`, `border-border`) — no numbered Tailwind classes
- Responsive at `lg` (the content-flow split point; see Rule Zero / §6)
- App Router metadata via `export const metadata` — **NOT** `next/head` (that's Pages Router)

---

### Example 2: Responsive Composition Patterns (illustrative)

These are illustrative `Page` / `Row` / `Box` composition patterns — flex-wrap cards,
a responsive grid, and the auto-fit grid. They are **not a shipped route** (the kit's
old `/demo` showcase was removed in the campaign); drop any of these `Row`s into a
real `Page`.

```tsx
import Page from "@/components/common/Page";
import Row from "@/components/common/Row";
import Box from "@/components/common/Box";
import { Button } from "@/components/ui/button";

// Illustrative — compose these Rows into any Page:
const ResponsivePatterns = () => {
  return (
      
      <Page className="justify-center" FULL={false}>
        {/* Typography & Buttons Row */}
        <Row className="">
          <h1 className="h1">Main Heading</h1>
          <Button size="sm">
            Small Button
          </Button>
          <Button className="ml-3">
            Default Button
          </Button>
          <Button className="ml-3" size="lg">
            Large Button
          </Button>
          
          <h2 className="h2">Subheading</h2>
          <h3 className="h3">Smaller Heading</h3>
          <p>Body text content...</p>
        </Row>
        
        {/* Flex Wrap Cards */}
        <Row className="flex flex-wrap">
          <Box className="w-80 p-5">
            <img 
              src="https://picsum.photos/id/12/350/300" 
              className="mb-3 min-w-full rounded-full" 
              alt=""
            />
            <p>Card content with fixed width (w-80)</p>
          </Box>
          <Box className="w-80 p-5">
            <img 
              src="https://picsum.photos/id/16/350/300" 
              className="mb-3 min-w-full rounded-full" 
              alt=""
            />
            <p>Another card - wraps automatically</p>
          </Box>
        </Row>
        
        {/* Responsive Grid */}
        <Row className="min-w-full text-center prose my-5">
          <h2>Responsive Grid Example</h2>
        </Row>
        
        <Row className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-1">
          <Box className="p-3">
            <img 
              src="https://picsum.photos/id/62/350/300" 
              className="mb-3 min-w-full rounded-full" 
              alt=""
            />
            <p>Grid item - 1 col mobile, 5 cols desktop</p>
          </Box>
          {/* Repeat for more items */}
        </Row>
        
        {/* Auto-Fit Grid (Plugin) */}
        <Row className="min-w-full text-center prose my-5">
          <h2>Auto-Fit Grid (No Breakpoints)</h2>
        </Row>
        
        <Row className="grid gap-3 grid-auto-fit p-3">
          <Box className="p-3">
            <img 
              src="https://picsum.photos/id/67/350/300" 
              className="mb-3 min-w-full rounded-full" 
              alt=""
            />
            <p>Auto-arranges based on available space</p>
          </Box>
          {/* More items */}
        </Row>
      </Page>
  );
};

export default ResponsivePatterns;
```

**Demonstrates:**
- Typography hierarchy (h1, h2, h3, p)
- Button sizes (`sm` / default / `lg`) — token-themed, no numbered colors
- Fixed-width flex cards (`w-80`)
- Responsive grid (1-5 columns)
- Auto-fit grid (plugin)
- Image handling
- Proper spacing

---

### Example 3: Members Portal with Layout

Every positive layout example keeps every navigation destination reachable at mobile widths. Consume AppShellPage or provide a complete accessible mobile trigger/drawer or equivalent navigation alongside the desktop sidebar. hidden md:block is acceptable only when that same example supplies the mobile alternative. Retire an incomplete layout as a copyable positive example.

The former copyable layout is withdrawn because it hid navigation on small screens or bypassed the installed shell. Use the verified responsive shell/rail/drawer contract for the pinned kit; do not invent a breakpoint or duplicate the shell. Verify reachable navigation, focus management, keyboard/escape behavior and no page overflow at every supported width.

---

## Quick Reference Checklist

### Creating a New Page

- [ ] Create folder: `src/app/(group)/feature-name/`
- [ ] Create `page.tsx` (minimal wrapper, 3-8 lines)
- [ ] Create `FeatureNamePageContent.tsx` (actual implementation)
- [ ] Import common components: `Page`, `Row`, `Box`
- [ ] Add page metadata (`export const metadata`) in `page.tsx`
- [ ] Wrap content in `<Page FULL={false}>`
- [ ] Organize content in `<Row>` sections
- [ ] Use `<Box>` for individual content blocks
- [ ] Test responsive behavior (mobile, tablet, desktop)
- [ ] Verify layout works with sidebar (if applicable)

---

### Component Import Checklist

```tsx
// Common components (layout)
import Page from "@/components/common/Page";
import Row from "@/components/common/Row";
import Box from "@/components/common/Box";
import BackButton from "@/components/common/BackButton";
import Spinner from "@/components/common/Spinner";

// UI components (shadcn/ui)
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

// Next.js
import type { Metadata } from "next"; // page.tsx: export const metadata
import Link from "next/link";
import Image from "next/image";

// React
import React from "react";
```

---

### Responsive Testing Checklist

- [ ] Mobile (320px-640px): Content stacks vertically
- [ ] Tablet (768px-1024px): Sidebar appears, 2-3 columns
- [ ] Desktop (1280px+): Full layout, 3-5 columns
- [ ] Images scale properly
- [ ] Text remains readable
- [ ] Buttons accessible on touch
- [ ] Navigation works on all sizes
- [ ] No unintended page-level horizontal overflow; intentional bounded tabs/carousels remain usable by touch, keyboard and assistive technology.
- [ ] Proper spacing maintained

---

## Suggestions for Improvement

### Current Strengths
1. ✅ Clean separation of page.tsx and PageContent
2. ✅ Reusable common components
3. ✅ Consistent naming conventions
4. ✅ Responsive patterns established
5. ✅ Layout composition with Navbar + Sidebar

### Potential Enhancements

#### 1. Add Header Component
**Current:** No dedicated Header component in common folder

**Suggestion:** Create `src/components/common/Header.tsx`
```tsx
interface HeaderProps {
  title: string;
  subtitle?: string;
  action?: ReactNode;  // Optional action button
  className?: string;
}

const Header = ({ title, subtitle, action, className }: HeaderProps) => {
  return (
    <div className={`mb-6 ${className}`}>
      <div className="flex justify-between items-center">
        <div>
          <h1 className="h1">{title}</h1>
          {subtitle && <p className="text-muted-foreground">{subtitle}</p>}
        </div>
        {action && <div>{action}</div>}
      </div>
    </div>
  );
};
```

**Usage:**
```tsx
<Header 
  title="Admin Portal" 
  subtitle="Manage your bookings"
  action={<Button>Create Booking</Button>}
/>
```

---

#### 2. Create Section Component
**Purpose:** Semantic sections with consistent spacing

```tsx
interface SectionProps {
  children: ReactNode;
  title?: string;
  className?: string;
}

const Section = ({ children, title, className }: SectionProps) => {
  return (
    <section className={`my-8 ${className}`}>
      {title && <h2 className="h2 mb-4">{title}</h2>}
      {children}
    </section>
  );
};
```

---

#### 3. Add Grid Component
**Purpose:** Simplified responsive grid wrapper

```tsx
const mobileCols = { 1: 'grid-cols-1', 2: 'grid-cols-2', 3: 'grid-cols-3', 4: 'grid-cols-4' } as const;
const tabletCols = { 1: 'md:grid-cols-1', 2: 'md:grid-cols-2', 3: 'md:grid-cols-3', 4: 'md:grid-cols-4' } as const;
const desktopCols = { 1: 'lg:grid-cols-1', 2: 'lg:grid-cols-2', 3: 'lg:grid-cols-3', 4: 'lg:grid-cols-4' } as const;
const gaps = { 0: 'gap-0', 2: 'gap-2', 4: 'gap-4', 6: 'gap-6', 8: 'gap-8' } as const;

interface GridProps {
  children: ReactNode;
  cols?: {
    mobile?: keyof typeof mobileCols;
    tablet?: keyof typeof tabletCols;
    desktop?: keyof typeof desktopCols;
  };
  gap?: keyof typeof gaps;
  className?: string;
}

const Grid = ({ children, cols = {}, gap = 4, className = '' }: GridProps) => {
  const { mobile = 1, tablet = 2, desktop = 3 } = cols;
  if (!(mobile in mobileCols) || !(tablet in tabletCols) || !(desktop in desktopCols) || !(gap in gaps)) {
    throw new Error('Unsupported Grid variant');
  }
  return (
    <div className={`grid ${mobileCols[mobile]} ${tabletCols[tablet]} ${desktopCols[desktop]} ${gaps[gap]} ${className}`}>
      {children}
    </div>
  );
};
```

**Usage:**
```tsx
<Grid cols={{ mobile: 1, tablet: 2, desktop: 4 }} gap={4}>
  <Card>Item 1</Card>
  <Card>Item 2</Card>
</Grid>
```

---

#### 4. Component Library Documentation
**Suggestion:** Create Storybook or component showcase

- Visual documentation of all components
- Interactive props playground
- Responsive preview
- Code examples
- Accessibility notes

---

#### 5. Page Templates
**Create starter templates for common page types:**

```
src/templates/
├── DashboardPageTemplate.tsx
├── ListPageTemplate.tsx
├── DetailPageTemplate.tsx
├── FormPageTemplate.tsx
└── README.md
```

**Benefits:**
- Faster page creation
- Consistent structure
- Built-in best practices
- Copy-paste starting point

---

#### 6. Responsive Utilities
**Create helper functions for common responsive patterns:**

```typescript
// src/utils/responsive.ts

export const responsiveGrid = (cols: number) => {
  const breakpoints = {
    1: "grid-cols-1",
    2: "grid-cols-1 md:grid-cols-2",
    3: "grid-cols-1 md:grid-cols-2 lg:grid-cols-3",
    4: "grid-cols-1 sm:grid-cols-2 lg:grid-cols-4",
    5: "grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5"
  };
  return breakpoints[cols] || breakpoints[3];
};

// Usage
<Row className={`grid ${responsiveGrid(4)} gap-4`}>
```

---

#### 7. Layout Variants
**Add more layout options:**

- Full-width hero sections
- Split-screen layouts
- Masonry grid layouts
- Sticky sidebar option
- Collapsible sidebar for mobile

---

#### 8. Performance Optimizations
**Suggestions:**

1. **Lazy load images** in grid layouts
2. **Virtual scrolling** for long lists
3. **Skeleton loaders** for better perceived performance
4. **Memoize** expensive components
5. **Code split** large PageContent files

---

#### 9. Accessibility Improvements
**Add to checklist:**

- [ ] Semantic HTML (header, main, section, article)
- [ ] ARIA labels where needed
- [ ] Keyboard navigation support
- [ ] Focus indicators
- [ ] Screen reader testing
- [ ] Color contrast validation

---

#### 10. Developer Experience Tools

**CLI Tool for Page Generation:**
```bash
npm run create:page admin/users
# Creates:
# - src/app/(admin)/users/page.tsx
# - src/app/(admin)/users/UsersPageContent.tsx
```

**VS Code Snippets:**
```json
{
  "Page Content Component": {
    "prefix": "pagecontent",
    "body": [
      "import Page from '@/components/common/Page';",
      "import Row from '@/components/common/Row';",
      "",
      "// Page title/meta: set `export const metadata` in page.tsx (App Router).",
      "const ${1:ComponentName}PageContent = () => {",
      "  return (",
      "      <Page FULL={false} className=''>",
      "        <Row className=''>",
      "          <h1 className='h1'>${2:Page Title}</h1>",
      "          $0",
      "        </Row>",
      "      </Page>",
      "  );",
      "};",
      "",
      "export default ${1:ComponentName}PageContent;"
    ]
  }
}
```

---

## Questions & Discussion Points

### For Team Discussion

1. **Component Granularity:** Should we create more specialized components (Header, Section, Grid) or keep it minimal?

2. **Naming Conventions:** Are we happy with `FeatureNamePageContent.tsx` or prefer alternatives like:
   - `FeatureName.content.tsx`
   - `_content.tsx`
   - `index.content.tsx`

3. **Grid System:** Should we standardize on:
   - Manual Tailwind classes (current)
   - Grid component wrapper (proposed)
   - CSS Grid utility classes
   - Combination approach

4. **Mobile Navigation:** How should sidebar work on mobile?
   - Drawer/slide-in menu
   - Bottom navigation
   - Hamburger menu
   - Tab bar

5. **Page Templates:** Which page types should we create templates for?
   - Dashboard
   - List/Table
   - Detail/View
   - Form/Create
   - Settings
   - Profile

6. **Documentation:** How to keep this manual updated?
   - Automated from code comments
   - Manual updates per PR
   - Living Storybook
   - Wiki/Notion

---

## Final Thoughts

This manual captures the **proven patterns** from the starter kit. The approach is:

**Simple → Composable → Consistent → Fast**

By following these patterns, we can:
- ✅ Build pages in 10-15 minutes
- ✅ Maintain consistency across projects
- ✅ Onboard new developers quickly
- ✅ Scale to hundreds of pages
- ✅ Ship faster than vibe coders with better quality

**Remember:** These are guidelines, not rigid rules. Adapt as needed, but document changes here.

---

## Appendix: Common Patterns Quick Copy

### Basic Page Structure
```tsx
<Page FULL={false} className="">
  <Row className="">
    <h1 className="h1">Title</h1>
  </Row>
</Page>
```

### Card Grid
```tsx
<Row className="grid grid-cols-1 md:grid-cols-3 gap-4">
  <Box className="p-5">Card 1</Box>
  <Box className="p-5">Card 2</Box>
  <Box className="p-5">Card 3</Box>
</Row>
```

### Image Card
```tsx
<Box className="w-80 p-5">
  <img src="..." className="mb-3 min-w-full rounded-full" alt="" />
  <h3 className="h3">Title</h3>
  <p>Description</p>
</Box>
```

### Action Header
```tsx
<Row className="flex justify-between items-center mb-6">
  <h1 className="h1">Page Title</h1>
  <Button>Action</Button>
</Row>
```

### Prose Content
```tsx
<Row className="prose max-w-3xl mx-auto">
  <h1>Article Title</h1>
  <p>Long form content...</p>
</Row>
```

---

## 10. Advanced Design Patterns

This section covers advanced patterns extracted from production-grade applications built on this starter kit. These patterns enable scalable, maintainable, and consistent UI development.

---

### 10.1 CVA (Class Variance Authority)

CVA enables type-safe component variants with Tailwind CSS. Instead of conditional class logic scattered throughout components, CVA centralizes variant definitions.

#### What is CVA?

```typescript
// Without CVA: Messy conditional classes
<button
  className={`
    px-4 py-2 rounded-md
    ${variant === 'primary' ? 'bg-primary text-primary-foreground' : ''}
    ${variant === 'secondary' ? 'bg-secondary text-secondary-foreground' : ''}
    ${variant === 'ghost' ? 'bg-transparent hover:bg-accent' : ''}
    ${size === 'sm' ? 'min-h-11 min-w-11 text-sm' : ''}
    ${size === 'md' ? 'min-h-11 min-w-11 text-base' : ''}
    ${size === 'lg' ? 'h-12 text-lg' : ''}
  `}
>
  {children}
</button>

// With CVA: Clean, type-safe variants
<Button variant="default" size="default">{children}</Button>
```

#### Creating Variant Recipes

Consume the kit Button, including its verified variants, sizes and asChild composition. Do not replace it with this shortened implementation. An educational internal excerpt must be source-matched and labeled as an excerpt, not installation code. Preserve Link composition through the kit API.

Use the installed Shadcn Button as the component, retaining its verified Slot/asChild, ref and native-prop behavior. Do not replace it with the former simplified button implementation. Add a bounded variant only after verifying the installed API. All actionable sizes keep a 44×44px minimum target.

---

#### Type-Safe Props

CVA automatically generates TypeScript types from your variants:

```typescript
// These are automatically typed!
<Button variant="default" />     // ✅ Valid
<Button variant="secondary" />   // ✅ Valid
<Button variant="invalid" />     // ❌ TypeScript error

<Button size="sm" />             // ✅ Valid
<Button size="xl" />             // ❌ TypeScript error
```

#### CVA Best Practices

| Do ✅ | Don't ❌ |
|-------|---------|
| Keep variant sets small (3-5 options) | Create giant variant matrices |
| Use semantic token classes (`bg-primary`) | Hardcode hex colors |
| Co-locate recipe with component | Scatter variants across files |
| Use `cn()` for className merging | Concatenate strings manually |

---

### 10.2 Design Tokens

Design tokens are the single source of truth for visual design decisions. They're defined as CSS variables and mapped to Tailwind classes.

#### CSS Variables in globals.scss

Use the complete mode declarations in TOKEN_FILE.md §1 and the canonical token contract in GLOBAL_DESIGN_SYSTEM_HANDBOOK.md §2. The former partial CSS block is withdrawn as a drop-in setup recipe: it omitted required semantic and role tokens. Preserve every required category, foreground pairing, radius and mode override when instantiating the stylesheet.

---

#### Tailwind Token Mapping

```typescript
// tailwind.config.ts

export default {
  theme: {
    extend: {
      colors: {
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))',
        },
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
    },
  },
};
```

#### Using Tokens in Components

```tsx
// ✅ CORRECT: Use semantic tokens
<div className="bg-background text-foreground">
  <div className="bg-card text-card-foreground rounded-lg border border-border p-4">
    <h2 className="text-foreground">Title</h2>
    <p className="text-muted-foreground">Subtitle</p>
    <Button className="bg-primary text-primary-foreground">Action</Button>
  </div>
</div>

// ❌ WRONG: Hardcoded colors
<div className="bg-white text-gray-900">
  <div className="bg-gray-50 text-gray-800 rounded-lg border border-gray-200 p-4">
    <h2 className="text-gray-900">Title</h2>
    <p className="text-gray-500">Subtitle</p>
    <Button className="bg-blue-600 text-white">Action</Button>
  </div>
</div>
```

#### Dark Mode with Tokens

Because tokens use CSS variables, dark mode works automatically:

```tsx
// This component automatically adapts to dark mode
<div className="bg-background text-foreground">
  {/* In light mode: white background, dark text */}
  {/* In dark mode: dark background, light text */}
</div>

// Toggle dark mode by adding/removing class on html element
document.documentElement.classList.toggle('dark');
```

---

### 10.3 Component Catalogue Pattern

Organize components by domain and document their APIs for team consistency.

#### Domain-Based Organization

```
src/components/
├── ui/                    # Base primitives (shadcn/ui style)
│   ├── button.tsx
│   ├── input.tsx
│   ├── dialog.tsx
│   └── ...
│
├── global/                # App-wide components
│   ├── Navbar.tsx
│   ├── Footer.tsx
│   └── ...
│
├── common/                # Shared utilities
│   ├── Container.tsx
│   ├── Spinner.tsx
│   └── ...
│
├── shop/                  # E-commerce domain
│   ├── ProductList.tsx
│   ├── ProductCard.tsx
│   └── product-page/
│       ├── ProductInfo.tsx
│       └── ...
│
├── cart/                  # Cart domain
│   ├── CartSlide.tsx
│   └── CartItem.tsx
│
└── checkout/              # Checkout domain
    ├── left-pane/
    ├── right-pane/
    └── payments/
```

#### Props and APIs Documentation

Document critical component APIs:

```typescript
// src/components/shop/ProductCard.tsx

/**
 * ProductCard displays a product in a grid or list view.
 *
 * @example
 * ```tsx
 * <ProductCard
 *   product={product}
 *   variant="compact"
 *   onAddToCart={(p) => addToCart(p)}
 * />
 * ```
 */
interface ProductCardProps {
  /** The product data to display */
  product: Product;
  
  /** Display variant */
  variant?: 'default' | 'compact' | 'featured';
  
  /** Callback when add to cart is clicked */
  onAddToCart?: (product: Product) => void;
  
  /** Additional CSS classes */
  className?: string;
}

export const ProductCard = ({
  product,
  variant = 'default',
  onAddToCart,
  className,
}: ProductCardProps) => {
  // Implementation
};
```

#### Component Inventory Template

Keep a living inventory of key components:

| Component | Location | Props | Store Integration |
|-----------|----------|-------|-------------------|
| `Navbar` | `global/Navbar.tsx` | None | `useCartStore` (item count) |
| `ProductCard` | `shop/ProductCard.tsx` | `product`, `variant`, `onAddToCart` | None |
| `CartSlide` | `cart/CartSlide.tsx` | `open`, `onOpenChange` | `useCartStore` |
| `StripePaymentForm` | `checkout/payments/` | `clientSecret`, `onSuccess` | `useCheckoutStore` |

---

### 10.4 Class Ordering Convention

Consistent class ordering improves readability and reduces merge conflicts.

#### Recommended Order

1. **Layout/Display**: `container`, `flex`, `grid`, `block`, `hidden`
2. **Position/Overflow**: `relative`, `absolute`, `z-10`, `overflow-hidden`
3. **Box Model**: `w-`, `h-`, `p-`, `m-`, `gap-`, `space-`
4. **Typography**: `font-`, `text-`, `leading-`, `tracking-`
5. **Visuals**: `bg-`, `border-`, `shadow-`, `ring-`
6. **Effects/Animation**: `transition-`, `duration-`, `animate-`
7. **State Modifiers**: `hover:`, `focus:`, `disabled:`, `aria-`
8. **Responsive**: `sm:`, `md:`, `lg:`, `xl:`

#### Example

```tsx
// ✅ CORRECT: Ordered classes
<button
  className="
    inline-flex items-center justify-center
    relative
    w-full sm:w-auto px-4 py-2 gap-2
    text-sm font-medium
    bg-primary text-primary-foreground
    rounded-md border border-border shadow-sm
    transition-colors
    hover:bg-primary/90 focus-visible:ring-2
    disabled:opacity-50 disabled:pointer-events-none
    md:px-5 md:py-2.5
  "
>
  Continue
</button>

// ❌ WRONG: Random order
<button
  className="
    hover:bg-primary/90 px-4 text-sm
    bg-primary inline-flex md:px-5
    rounded-md w-full transition-colors
    font-medium py-2 items-center
    disabled:opacity-50 border-border
  "
>
  Continue
</button>
```

---

### 10.5 Dark Mode Best Practices

#### Token-Based Approach (Recommended)

```tsx
// Automatically adapts to dark mode
<div className="bg-background text-foreground">
  <div className="bg-card border-border">
    Content
  </div>
</div>
```

#### Explicit Dark Variants (When Needed)

Use semantic tokens for both modes. If a required semantic state is missing, extend the approved token contract and verify all modes; do not create a numbered-color bypass.

```tsx
<div className="bg-background text-foreground">
  <p className="text-muted-foreground">This text follows the active token mode.</p>
</div>
```

---

#### Dark Mode Toggle

Consume the existing theme provider and ThemeToggle for light, dark and system modes. Do not create a second controller that edits the HTML class or localStorage.theme independently of the provider. A standalone demonstration, if retained, must be explicitly non-kit and cannot be copied into a kit project.

---

### 10.6 Touch Device Considerations

#### Tap Target Sizing

Ensure interactive elements are at least 44×44px:

```tsx
// ✅ CORRECT: Adequate tap target
<button className="h-11 px-4 py-3">
  Click me
</button>

// ✅ CORRECT: Icon button with proper size
<button className="h-11 w-11 flex items-center justify-center">
  <Icon className="h-5 w-5" />
</button>

// ❌ WRONG: Too small for touch
<button className="h-6 px-2">
  Click me
</button>
```

#### Focus States

Don't rely solely on hover; provide visible focus states:

```tsx
<button
  className="
    bg-primary text-primary-foreground
    hover:bg-primary/90
    focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2
  "
>
  Action
</button>
```

#### Scroll and Gesture Handling

```tsx
// Horizontal scroll for carousels
<div className="overflow-x-auto scrollbar-hide">
  <div className="flex gap-4 min-w-max">
    {items.map((item) => (
      <Card key={item.id} className="w-64 flex-shrink-0" />
    ))}
  </div>
</div>

// Prevent scroll traps
<div className="overflow-y-auto max-h-[80vh]">
  {/* Scrollable content */}
</div>
```

---

### 10.7 The `cn()` Utility

The `cn()` function merges Tailwind classes intelligently, handling conflicts:

```typescript
// src/lib/utils.ts

import { type ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

#### Usage Examples

```tsx
// Merge base classes with props
<div className={cn('p-4 bg-card', className)}>

// Conditional classes
<div className={cn(
  'p-4 rounded-md',
  isActive && 'bg-primary text-primary-foreground',
  isDisabled && 'opacity-50 pointer-events-none'
)}>

// Override conflicts (twMerge handles this)
cn('p-4', 'p-6')  // Result: 'p-6' (not 'p-4 p-6')
cn('text-destructive', 'text-primary')  // Result: 'text-primary'
```

---

### 10.8 Quick Reference: Do's and Don'ts

#### Do ✅

- Use semantic tokens (`bg-primary`, `text-foreground`)
- Use CVA for components with variants
- Follow class ordering convention
- Ensure 44×44px minimum tap targets
- Use `cn()` for class merging
- Test at custom `lg` breakpoint (1150px)

#### Don't ❌

- Hardcode hex colors (`bg-[#1a1a1a]`)
- Create ad-hoc global CSS classes
- Rely solely on hover states
- Use inline styles for theming
- Duplicate variant logic across components
- Ignore dark mode compatibility

---

**End of Manual**

*Let's build better, faster, together.* 🚀

---

## Appendix — Run 001 Lessons That Updated This Manual

This manual was updated in v1.1 based on lessons learned during Cyberize Agentic Automation Run 001 (May 2026).

### Lesson 5 — The Phase 5 Mobile-First Violation

**Incident:** Phase 5 Chat screen shipped desktop-only with `w-64` fixed sidebar and no media queries. Operator caught it as F-grade work. Phase 5.4 refactor required.

**Root cause:** Mobile-first lived in section 7 of this manual. By Phase 5, the doctrine had decayed from Claudy's working memory. No structural forcing function caught the violation before code was authored.

**Fix applied to this manual:** Mobile-first promoted to Rule Zero opening section. Concrete forbidden patterns enumerated. Pre-write check questions defined. Cross-references to kit primitives and component registry added.

**Pattern to watch for in future runs:** Doctrine that lives mid-document does not survive long sessions. Anything foundational must be at the top, repeated, and enforced structurally at authoring time (pre-write check), not just at verification time.

---

### Lesson 9 — The Theming Doctrine Gap (Run 002)

**Incident:** Cyber Pharma Run 002 surfaced that the Factory had no dedicated theming doctrine. The Cyberize Run 001 Locked Palette WIN was buried in retrospective context, not promoted to evergreen methodology. The Cyber Pharma Architect identified this gap mid-Phase-0 planning when discussing how the designer should deliver the visual system.

**Root cause:** A win in Run 001 produced a real artifact (the Locked Palette table) but the Factory had no manual to formalize the *pattern* behind the artifact. Result: future projects would re-derive the lesson instead of inheriting it.

**Fix applied to this manual:** Added Rule Zero-B as the companion posture to Rule Zero. Authored `THEMING_MANUAL.md` as the standalone deep dive. Updated `APP_ARCHITECTURE_MANUAL` and `HANDOFF_PACKAGE_PLAYBOOK` with cross-references. Bumped this manual to v1.2.

**Pattern to watch for in future runs:** When a project discovers a doctrine win mid-execution and captures it in `_project/CLAUDE.md`, the Phase 8 retrospective must propose promotion to evergreen methodology. Doctrine that stays in `_project/` benefits one run; doctrine that moves to `APP_FACTORY/` benefits every future run.

---

## Manual Maintenance Discipline

This manual is a **living document**. Updates happen at three triggers:

1. **After every Factory run** — Phase 8 retrospective surfaces lessons; structural ones land here as patches
2. **When kit baseline changes** — new primitives or framework upgrades update relevant sections
3. **When the operator promotes a Kit Improvement Proposal** — accepted proposals land here

### Update Discipline

- Patches go at the TOP (like Rule Zero) for foundational rules; AT THE END (like this appendix) for evolution notes
- Preserve doctrine history — don't delete sections that are superseded, mark them as such
- Cross-reference Run numbers when adding lessons-driven content
- Bump the version number at the top when applying patches

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.5 | 2026-10-16 | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: FC-003/096, FC-009, FC-041, FC-071, FC-072, FC-073, FC-076, FC-077, FC-078, FC-079, FC-080, FC-082, FC-083, MC-01 |
| 1.4 | 2026-07-08 | **Wave 5 micro (audit sync).** Cross-references canonical-name only: the PHANTOM `HANDOFF_PACKAGE_PLAYBOOK_v1.1.md` reference killed (that version never existed — the audit's forward-dated collector's item) plus the stale handbook/registry/theming/build-phase versioned refs (F-032/F-011). Three broken-arrow mojibake sequences repaired in the component-approach line (F-012 — review counted 1; scan found 3). Standard header block adopted (F-018). Nothing else — MODEL doc; Rule Zero, Rule Zero-B, teaching examples, and the D-018 Update Discipline appendix untouched. |
| 1.3 | 2026-06-28 | Renamed `ThemeToggler` → `ThemeToggle` (the real shipped component) throughout; dropped deleted-orphan references; re-pointed deleted-demo teaching examples to live files (Example 1 → public home, Example 2 → illustrative); replaced `next/head` (Pages Router) with the App-Router `export const metadata` API in all page examples + the VS Code snippet. Kit Hardening Gate 10. |
| 1.2 | 2026-06-02 | Added Rule Zero-B (theming as the second foundational posture). Added TOC entries for Rule Zero and Rule Zero-B. Authored companion `THEMING_MANUAL.md`. Added Lesson 9 appendix. Born from Cyber Pharma Run 002. |
| 1.1 | 2026-05-31 | Added Rule Zero (mobile-first foundational posture) at top. Added Lesson 5 appendix. Fixed UTF-8 encoding artifacts throughout. Born from Cyberize Run 001. |
| 1.0 | 2025-12-30 | Initial manual authored |

---

🥄 *Part of Stark Industries — App Factory doctrine.*
