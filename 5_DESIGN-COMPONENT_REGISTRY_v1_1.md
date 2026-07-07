# COMPONENT REGISTRY

> **Scannable primitive lookup. Decision-ready. The first stop before authoring any UI.**
>
> **🛑 BEFORE AUTHORING ANY COMPONENT, SCAN THIS REGISTRY.**
>
> If a primitive exists, you USE it. You do not author a parallel one. If a primitive is close but not quite right, surface a Kit Improvement Proposal — don't fork silently.

**Kit:** Stark SaaS Starter — Starter Kit v3 (post Kit-Perfection campaign)
**Last Updated:** 2026-06-28
**Pairs with:** `STARTER_KIT_HANDBOOK.md` (sibling file)

---

## How To Use This Registry

1. **Scan the Quick Decision Tree** below first — covers 80% of authoring questions in 30 seconds
2. **Find the primitive** in the relevant section
3. **Read its "when NOT to use"** clause — that's where most stumbles happen
4. **Check the mobile behavior** — Rule Zero applies to every primitive
5. **If nothing fits**, surface a Kit Improvement Proposal in the next phase completion report

---

## 🎯 Quick Decision Tree

```
What are you trying to build?
│
├─ A full PAGE
│   ├─ Full-bleed app shell (sidebar + main)? → AppShellPage
│   ├─ Content-flow (marketing, docs, forms)? → Page + Row + Box
│   ├─ Dense data table portal? → plain <div className="container mx-auto p-6">
│   └─ Nested section inside a page? → Container
│
├─ A LAYOUT element
│   ├─ Horizontal section grouping content? → Row
│   ├─ Generic content block (card, bubble)? → Box
│   ├─ Semantic <main>? → Main
│   ├─ Navigation sidebar (role-specific)? → Sidebar / AdminSidebar / SuperadminSidebar
│   ├─ Top navbar? → Navbar (portal) / PublicNav (marketing) / NavbarLoginReg (auth)
│   └─ Mobile slide-over drawer? → Sheet (kit-authored `ui/sheet.tsx`)
│
├─ A FORM
│   ├─ Login form? → LoginForm (already wired)
│   ├─ Register form? → RegisterForm (already wired)
│   ├─ Login + Register tabs? → AuthTabs
│   ├─ Custom form with validation? → Shadcn Form + react-hook-form + zod
│   └─ Single input? → Input + Label
│
├─ A BUTTON / ACTION
│   ├─ Standard button? → Button (Shadcn, variants available)
│   ├─ Back navigation? → BackButton
│   ├─ Pagination? → PaginationControls
│   └─ Dropdown actions? → DropdownMenu
│
├─ A FEEDBACK element
│   ├─ Success notification (transient)? → toast.success via Sonner
│   ├─ Error notification (persistent)? → Alert variant="destructive"
│   ├─ Warning callout? → Alert variant="warning"
│   ├─ Info callout? → Alert (default)
│   └─ Loading? → Spinner (lucide Loader2) or Skeleton
│
├─ A SELECTION control
│   ├─ Single-select dropdown? → Select
│   ├─ Multi-select? → Custom — not in kit yet (Kit Improvement Proposal candidate)
│   ├─ Tabs? → Tabs
│   ├─ Dialog/modal? → Dialog
│   └─ Theme toggle? → ThemeToggle (already wired)
│
├─ A TEXT element
│   ├─ Markdown content (agent responses)? → react-markdown + remark-gfm
│   ├─ Plain text (user messages)? → just JSX text
│   └─ HTML (rare, sanitized)? → html-react-parser (NEVER dangerouslySetInnerHTML)
│
└─ Something NONE of the above covers
    └─ STOP. Surface to operator with Kit Improvement Proposal format.
```

---

## 1. Common Layout Primitives (`src/components/common/`)

These are the kit's reusable building blocks. They are mobile-first by default and theme-aware.

### `Page`

**Purpose:** Responsive content-flow page wrapper

**When to use:**
- Marketing pages
- Doc pages
- Form pages
- Settings pages
- Anything content-flow (not full-bleed app shell)

**When NOT to use:**
- Full-bleed app shells (sidebar + scrolling main) → use `AppShellPage` instead
- Dense data table portals → use plain `container` div

**Props:**
```typescript
{
  children: ReactNode;
  className?: string;
  FULL?: boolean;  // true = min-w-full, false = w-11/12 mx-auto (centered)
}
```

**Mobile behavior:** Inherits responsive defaults. Use Tailwind responsive classes inside.

**Example:**
```tsx
<Page FULL={false} className="">
  <Row><h1>Page Title</h1></Row>
  <Row><p>Content</p></Row>
</Page>
```

---

### `Row`

**Purpose:** Horizontal container for grouping content with consistent padding

**When to use:**
- Stacked content sections within a Page
- Grid containers
- Flex containers for content blocks

**When NOT to use:**
- Top-level page wrapping → use `Page`
- Generic content blocks → use `Box`

**Props:**
```typescript
{
  children: ReactNode;
  className?: string;
}
```

**Default styles:** `min-w-full p-5`

**Mobile behavior:** Full-width by default. Use Tailwind classes for responsive layouts.

**Example:**
```tsx
<Row className="grid grid-cols-1 md:grid-cols-3 gap-4">
  <Box>Card 1</Box>
  <Box>Card 2</Box>
</Row>
```

---

### `Box`

**Purpose:** Generic content block — most flexible primitive

**When to use:**
- Cards
- Bubbles (message bubbles in chat)
- Content blocks within a grid
- Any container that needs custom dimensions

**When NOT to use:**
- Page-level wrapping → use `Page`
- Section grouping with padding → use `Row`

**Props:**
```typescript
{
  children: ReactNode;
  className?: string;
}
```

**Default styles:** NONE — fully customizable

**Mobile behavior:** Depends on className you pass.

**Example:**
```tsx
<Box className="w-80 p-5 rounded-lg shadow">
  <img src="..." />
  <h3>Title</h3>
</Box>
```

---

### `Container`

**Purpose:** Like `Page` but for nested sections inside a page

**When to use:**
- Sub-sections within a Page that need their own width context
- Less commonly used than `Page`

**When NOT to use:**
- Top-level page wrapping → use `Page`
- Single content blocks → use `Box`

**Props:**
```typescript
{
  children: ReactNode;
  className: string;       // REQUIRED
  FULL: boolean;
}
```

---

### `Main`

**Purpose:** Semantic `<main>` element with flex-grow

**When to use:**
- Wrapping main content in layouts where semantic `<main>` is needed
- Pages that should fill available vertical space

**When NOT to use:**
- Sidebars or non-main content
- Within a Page wrapper (Page handles its own main)

**Props:**
```typescript
{
  children: ReactNode;
  className: string;       // REQUIRED
}
```

**Default styles:** `min-w-full flex flex-grow`

---

### `AppShellPage` ⭐ NEW (Born In Run 001 Phase 5.4)

**Purpose:** Full-bleed app surface with sidebar + main column. Mobile-first built-in.

**When to use:**
- Chat interfaces
- Mission control / admin consoles
- Dashboards with persistent sidebars
- Any "app-like" surface (sidebar + scrolling main + sticky inputs)

**When NOT to use:**
- Content-flow pages (marketing, docs, forms) → use `Page + Row + Box`
- Dense data tables → use plain `container` div
- Pages without sidebars → use `Page`

**Props:**
```typescript
{
  sidebar: ReactNode;              // Sidebar content
  children: ReactNode;             // Main column content (manages own flex layout)
  mobileTitle?: string;            // Wordmark/title in mobile top bar
  mobileTopBarRight?: ReactNode;   // Right slot in mobile top bar (e.g., ThemeToggle)
}
```

**Mobile behavior (built-in) — REAL as of Gate 2/3 (Kit-Perfection):**
- Below `xl` (<1280px): sidebar becomes a hamburger-triggered slide-over (a `Sheet`,
  side="left") under a two-bar layout (the shared `Navbar` + a trigger bar). Dismiss
  via close-on-nav (`usePathname`), outside-tap, and Esc.
- `xl`+ (>=1280): sidebar persistent (`w-[25rem]`), main takes the remainder.
- `sidebar` may be a render-fn `(close) => ReactNode` so a panel can close on a
  terminal action. The 4 CP scars: close-on-nav, passable `close`, ~25rem capped to
  85vw, native dismiss.

**Theme behavior:**
- Dark mode default: `dark:bg-zinc-800` (softer than `zinc-950`)
- Light mode default: white/neutral

**Example:**
```tsx
<AppShellPage
  sidebar={<CyberizeSidebar />}
  mobileTitle="CYBERIZE"
  mobileTopBarRight={<ThemeToggle />}
>
  <div className="flex flex-col h-full">
    {/* main column content */}
  </div>
</AppShellPage>
```

**Heavy in-file JSDoc** at `src/components/common/AppShellPage.tsx` documents the decision tree, mobile behavior contract, accessibility notes, and promotion path.

---

### `BackButton`

**Purpose:** Consistent back-navigation button with arrow icon

**When to use:**
- Anywhere a user needs to navigate back to a parent route
- Detail views, edit forms

**When NOT to use:**
- Main navigation (use Sidebar)
- Form submission (use Button)

**Props:**
```typescript
{
  text: string;
  link: string;
}
```

**Example:**
```tsx
<BackButton text="Back to Users" link="/admin-portal" />
```

---

### `Spinner`

**Purpose:** Loading indicator with accessibility support

**When to use:**
- Loading states for buttons (also see lucide `Loader2`)
- Full-page loading states
- In-flight operation indicators

**When NOT to use:**
- Skeleton loading for content blocks → use Shadcn `Skeleton`
- Long operations → use `Skeleton` + progress

**Example:**
```tsx
{isLoading && <Spinner />}
```

---

### `PaginationControls`

**Purpose:** Shared pagination component with `useTransition` for smooth navigation

**When to use:**
- Any portal list view
- Tables with paginated data
- Search result lists

**When NOT to use:**
- Single-page content
- Infinite scroll patterns (not in kit)

**Behavior:**
- Uses `useRouter` and `useTransition`
- Shows `Loader2` spinner while pending
- Pagination elements are `role="button"` (NOT `role="link"`) for testing

**Example:**
```tsx
<PaginationControls
  totalPages={10}
  currentPage={1}
  baseUrl="/admin-portal"
/>
```

---

## 2. Global Components (`src/components/global/`)

Site-wide components used across all pages.

### `Navbar`

**Purpose:** Default site navbar

**Variants (actual on disk):**
- `Navbar` — authenticated portal top bar
- `NavbarLoginReg` — minimal auth-pages bar (logo + theme)
- `PublicNav` — public/marketing nav (logo + portal links + theme + auth island)
- `PublicNavAuthSection` — auth-state island consumed by `PublicNav`
- `PublicMobileNav` — hamburger + `Sheet` mobile menu for the public nav (< lg)

(`NavbarHome` / `NavbarSuperadmin` do NOT exist — removed from this registry.)

**When to use:**
- Top of public pages
- Top of portal pages (variant by portal)

---

### `ThemeToggle`

**Purpose:** Light/dark mode toggle button

**When to use:**
- Anywhere you need theme switching (typically in navbar or sidebar)

**Example:**
```tsx
<ThemeToggle />
```

---

## 3. Layout Components (`src/components/layout/`)

Navigation sidebars by role.

### `Sidebar`

**Purpose:** Default sidebar for non-portal contexts

### `AdminSidebar`

**Purpose:** Admin portal navigation
**Visible to:** Admin role

### `SuperadminSidebar`

**Purpose:** Superadmin portal navigation
**Visible to:** Superadmin role

**Pattern for new portals:**
Create a `<ProjectName>Sidebar.tsx` in `src/components/layout/` (e.g., `CyberizeSidebar`) and consume it via `<AppShellPage sidebar={<CyberizeSidebar />} />`.

---

## 4. Auth Components (`src/components/auth/`)

Pre-wired auth UI components.

### `LoginForm`

**Purpose:** Email/password login form, wired to `/api/auth/login`

**🛑 DO NOT** author a custom login form. Use this one.

---

### `RegisterForm`

**Purpose:** Email/password/full_name signup form, wired to `/api/auth/signup`

**🛑 DO NOT** author a custom signup form. Use this one.

---

### `AuthTabs`

**Purpose:** Tab switcher between login and register views

**When to use:**
- The `/auth` page
- Anywhere you offer both login and register options

---

## 5. Shadcn UI Primitives (`src/components/ui/`)

Standard Shadcn components installed and themed.

### Form Primitives

| Component | Purpose | Common Use |
|---|---|---|
| `Button` | Standard button with variants (default, destructive, outline, ghost, etc.) | Any action trigger |
| `Input` | Text input | Forms, search bars |
| `Label` | Form label (paired with Input/Textarea) | Always pair with form inputs |
| `Textarea` | Multi-line text input | Long-form content, instructions, comments |
| `Form` | Form wrapper with `react-hook-form` integration | Forms with validation |
| `Select` | Single-select dropdown | Dropdown choices |
| `Checkbox` | Checkbox input | Multi-select, boolean toggles |
| `RadioGroup` | Radio button group | Mutually exclusive choices |
| `Switch` | Toggle switch | Boolean settings |

---

### Layout & Container Primitives

| Component | Purpose | Common Use |
|---|---|---|
| `Card` | Bordered content container (Header, Content, Footer) | Information panels, stat cards |
| `Dialog` | Modal dialog | Confirmations, complex forms |
| `Sheet` | Slide-over panel (kit-authored `ui/sheet.tsx`, on Radix dialog) | Mobile menus, side details |
| `Tabs` | Tab navigation | Multi-view content within a page |
| `Separator` | Horizontal or vertical divider | Section breaks |
| `ScrollArea` | Custom-styled scrollable container | Long content lists |
| `Accordion` | Collapsible content sections | FAQ, settings, hierarchical content |

---

### Feedback Primitives

| Component | Purpose | When to use |
|---|---|---|
| `Alert` | Persistent inline callout (with variants: default, destructive, warning) | Error messages, warnings, info |
| `Sonner` (toast) | Transient notification (top-right by default) | Success confirmations |
| `Skeleton` | Loading placeholder | Content loading states |
| `Spinner` (lucide `Loader2`) | Loading indicator | Button loading, in-flight actions |
| `Progress` | Progress bar | Multi-step processes |

**Critical convention:**
- ✅ **Success → toast** (transient)
- ✅ **Failure → Alert variant="destructive"** (persistent)
- Don't mix them. Toast for failure is hard to read; Alert for success is too persistent.

---

### Selection & Action Primitives

| Component | Purpose | When to use |
|---|---|---|
| `DropdownMenu` | Dropdown menu with items | Context menus, action menus |
| `ContextMenu` | Right-click context menu | Right-click actions |
| `Tooltip` | Hover tooltip | Help text, abbreviation explanations |
| `Popover` | Floating popover | Rich tooltips, mini-forms |
| `Command` | Command palette / search | Search-as-you-type interfaces |
| `Avatar` | User avatar with fallback | User indicators in lists, headers |

---

## 6. Specialized Component Patterns

### Markdown Rendering (For Chat Assistant Responses)

**Use:** `react-markdown` + `remark-gfm`

**Why:**
- Renders headings, lists, bold, italic, code blocks, **tables (GFM)**, links, blockquotes
- Sanitizes by default (no XSS risk)

**Critical:** Always include `remark-gfm` plugin for table support. Without it, markdown tables render as raw `| header |` text.

**Example:**
```tsx
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

<ReactMarkdown remarkPlugins={[remarkGfm]}>
  {messageContent}
</ReactMarkdown>
```

**🛑 NEVER use `dangerouslySetInnerHTML`** for any content. Use `react-markdown` for markdown, `html-react-parser` if you must render raw HTML.

---

### HTML Rendering (Rare, Sanitized)

**Use:** `html-react-parser`

**When to use:** When you have HTML content from a trusted source that must render as elements (not as escaped text)

**🛑 NEVER use `dangerouslySetInnerHTML`** in this codebase. It's XSS-prone and breaks React's component model.

**Example:**
```tsx
import parse from 'html-react-parser';

<div>{parse(safeHtml)}</div>
```

---

### Code Highlighting In Markdown

**Use:** `react-syntax-highlighter` (already installed) with `oneLight` or `oneDark` theme

**When to use:** Code blocks in chat responses, documentation pages

**Example:**
```tsx
import SyntaxHighlighter from 'react-syntax-highlighter';
import { oneLight } from 'react-syntax-highlighter/dist/esm/styles/prism';

<SyntaxHighlighter style={oneLight} language={lang}>
  {code}
</SyntaxHighlighter>
```

---

## 7. Mobile Behavior Reference

Every primitive in this registry must work at the three breakpoints:

| Breakpoint | Width | Behavior |
|---|---|---|
| Mobile | 375px | Default; everything works here first |
| Tablet | 768px (`md:`) | Layouts may split; sidebars become persistent |
| Desktop | 1024px+ (`lg:`) | Multi-column layouts permitted |

### Mobile Behavior By Primitive

| Primitive | Mobile Behavior |
|---|---|
| `AppShellPage` | Sidebar → slide-over drawer; mobile top bar appears |
| `Page` | Full-width content flow; vertical stacking |
| `Row` | Tailwind-controlled (use `flex-col md:flex-row` etc.) |
| `Box` | Tailwind-controlled (use `w-full md:w-1/2` etc.) |
| `Sidebar` / `AdminSidebar` / `SuperadminSidebar` | Behavior depends on parent layout — typically hidden behind hamburger at mobile |
| `Navbar` variants | Compact at mobile, full at desktop |
| Shadcn `Sheet` | Already mobile-first (slide-over native) |
| Shadcn `Dialog` | Full-screen at mobile, centered at desktop |
| Shadcn `DropdownMenu` | Position-aware |
| Forms (`LoginForm`, `RegisterForm`) | Already mobile-first |

### Mobile-First Authoring Checklist (For New Components)

Before authoring any new UI component, answer:

- [ ] What does it look like at 375px?
- [ ] What changes at 768px?
- [ ] What changes at 1024px?
- [ ] Are all touch targets ≥ 44px?
- [ ] Does horizontal scroll occur at any width? (If yes, fix the layout)
- [ ] Is text readable at 375px without zoom? (≥ 14px body)

---

## 8. Anti-Patterns To Avoid

Patterns that look reasonable but break in this kit:

### ❌ Authoring layouts with raw flex divs when primitives exist

**Wrong:**
```tsx
<div className="flex flex-col h-screen">
  <div className="flex flex-1">
    <div className="w-64 bg-gray-100">...</div>
    <div className="flex-1">...</div>
  </div>
</div>
```

**Right:**
```tsx
<AppShellPage sidebar={<MySidebar />} mobileTitle="App">
  {/* main column */}
</AppShellPage>
```

(Lesson from Run 001 Phase 5 — see `STARTER_KIT_FEEDBACK.md` Lesson 7)

---

### ❌ Putting `*PageContent.tsx` in `src/components/`

**Wrong:**
```
src/components/chat/ChatPageContent.tsx
src/app/(cyberize)/chat/page.tsx
```

**Right (co-located):**
```
src/app/(cyberize)/chat/page.tsx
src/app/(cyberize)/chat/ChatPageContent.tsx
```

(Lesson from Run 001 Phase 5)

---

### ❌ Building parallel auth forms

**Wrong:** Authoring custom `MyLoginForm.tsx` from scratch

**Right:** Use `LoginForm` from `src/components/auth/`. If you need additional fields, surface a Kit Improvement Proposal to extend `LoginForm`.

---

### ❌ Using `dangerouslySetInnerHTML`

**Wrong:**
```tsx
<div dangerouslySetInnerHTML={{ __html: content }} />
```

**Right (for markdown):**
```tsx
<ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>
```

**Right (for sanitized HTML):**
```tsx
{parse(safeHtml)}
```

---

### ❌ Mixing success and failure feedback components

**Wrong:** Using `Alert variant="destructive"` for save success, `toast` for save failure

**Right:** Toast for success (transient), Alert variant="destructive" for failure (persistent)

---

### ❌ Skipping mobile behavior in plan

**Wrong:** Plan describes desktop layout, mobile "we'll figure out later"

**Right:** Plan opens with the 375px sketch first, then describes how it scales up

---

## 9. Kit Improvement Proposals — When To File One

If you encounter a UI need that NO primitive in this registry handles, do NOT silently author a one-off. Instead:

1. **Don't fork** — don't create a slightly-different version of an existing primitive
2. **Surface to operator** in your next phase completion report using the Kit Improvement Proposal format:
   - What I noticed
   - What the kit currently does
   - What a better pattern might be
   - Whether I'd recommend implementing it (with cost estimate)
3. **Wait for operator decision** — they may accept, defer, or reject
4. **Accepted proposals** become kit-level work that gets added to this registry
5. **Deferred proposals** land in `KIT_PROPOSALS_ARCHIVE.md`

This is how the registry grows. Every Factory run can leave the kit a little richer.

### Examples Of Things That Could Become Future Primitives

These were noted but not authored in Run 001:

- `MultiSelect` — multi-selection dropdown (currently not in kit)
- `MobileTestHarness` — utility for screenshot capture at 3 breakpoints
- `DataTable` — full-featured table primitive (currently using raw HTML tables)
- `EmptyState` — standardized empty state component
- `ErrorBoundary` — standardized error boundary with retry

If you find yourself needing any of these, you've found a Kit Improvement Proposal candidate.

---

## 10. Quick Reference — "Which Primitive Should I Use?"

| If you need to... | Use this primitive |
|---|---|
| Wrap a full chat or dashboard page | `AppShellPage` |
| Wrap a marketing or form page | `Page` |
| Group content horizontally with padding | `Row` |
| Make a card or content block | `Box` |
| Wrap nested section | `Container` |
| Add semantic `<main>` | `Main` |
| Add back navigation | `BackButton` |
| Show loading | `Spinner` or `Skeleton` |
| Paginate a list | `PaginationControls` |
| Login form | `LoginForm` (don't author) |
| Signup form | `RegisterForm` (don't author) |
| Login + Register tabs | `AuthTabs` |
| Toggle light/dark | `ThemeToggle` (don't author) |
| Show success | `toast.success()` via Sonner |
| Show error inline | `Alert variant="destructive"` |
| Show warning | `Alert variant="warning"` |
| Modal dialog | `Dialog` |
| Mobile slide-over | `Sheet` |
| Dropdown of actions | `DropdownMenu` |
| Form with validation | `Form` + `react-hook-form` + `zod` |
| Render markdown | `ReactMarkdown` + `remark-gfm` |
| Render code | `react-syntax-highlighter` |
| Sanitized HTML | `html-react-parser` |

---

## 11. Cross-References

- **`STARTER_KIT_HANDBOOK.md`** — full kit overview (sibling file)
- **`agent_docs/APP_FACTORY/UI-UX-BUILDING-MANUAL.md`** — full UI patterns deep-dive
- **`src/app/(public)/page.tsx`** — canonical page-composition example (live `Page`/`Row`/`Box` content-flow)
- **`src/components/common/AppShellPage.tsx`** — heavy in-file JSDoc with decision tree

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.1 | 2026-06-28 | Kit-Perfection reconciliation: `AppShellPage` + `Sheet` are REAL (built Gates 2–3); breakpoint `md`→`xl`, two-bar + render-fn sidebar + 4 CP scars; removed non-existent `NavbarHome`/`NavbarSuperadmin`; added real global components (`PublicNav`/`PublicNavAuthSection`/`NavbarLoginReg`/`PublicMobileNav`); re-pointed the page-composition cross-ref from the deleted `/demo` to the live home. |
| 1.0 | 2026-05-31 | Initial registry authored from kit v0.4.1 + Run 001 lessons |

---

🥄 *Part of Stark Industries — App Factory v1.1 doctrine.*
