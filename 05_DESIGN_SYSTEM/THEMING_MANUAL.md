# THEMING MANUAL

> **Version:** 1.2 · **Date:** 2026-07-08 · **Status:** Active
> **Tier:** 5 — Design System · **Pairs with:** GLOBAL_DESIGN_SYSTEM_HANDBOOK, TOKEN_FILE, THEME_LIBRARY, UI_UX_BUILDING_MANUAL, APP_ARCHITECTURE_MANUAL

> **Project:** Stark Industries App Factory
> **Born from:** Cyber Pharma Run 002 (June 2026) — evergreen doctrine, applies to ALL projects
> **Parent doctrine:** UI-UX-BUILDING-MANUAL (Rule Zero — mobile-first), APP_ARCHITECTURE_MANUAL (Theming Files section)

---

## 0. Reader's Guide

This manual is **standalone but interlocking**. It is referenced by three other Factory manuals:

- **UI-UX-BUILDING-MANUAL** — mentions theming briefly, points here for depth
- **APP_ARCHITECTURE_MANUAL** — mentions file locations, points here for the *why*
- **HANDOFF_PACKAGE_PLAYBOOK** — mentions designer deliverable format, points here for the spec

Read this manual when:
1. Setting up a new project's visual identity (Phase 0 or Phase 1)
2. Engaging a designer (human or agent) for a new project
3. Onboarding a new designer to the Factory pattern
4. Needing to quickly re-theme a deployed project for stakeholder demos
5. Diagnosing visual inconsistency across a project

---

## 1. The Core Principle — Tokens Before Pixels

> **Design tokens are the brand contract. The variables file is the executable artifact.**

Every Stark Industries project is built on a foundation of **semantic color tokens** declared as CSS custom properties. These tokens — not hardcoded hex codes — are referenced by every component, every page, every layout in the project.

This means:

- **Changing the brand = changing one file.** A designer (or operator) updates the token values; the entire app re-themes on next page load.
- **No component file hardcodes a color.** Every color reads from a semantic token (`--primary`, `--background`, `--muted-foreground`, etc.).
- **Light mode, dark mode, and brand themes** all coexist in the same token file. The browser picks which set renders based on user preference.
- **The starter kit's shadcn components inherit automatically.** Every shadcn `Button`, `Card`, `Input`, `Dialog`, etc. reads from the same semantic tokens.

**This is the WordPress global SCSS pattern, but better.** Same single-file source-of-truth discipline, with runtime swappability instead of compile-step recompilation, plus mobile-first plus dark mode plus brand themes all in one place.

---

## 2. Why This Doctrine Exists (Born From Run 001 Lesson)

Cyberize Run 001 produced an unplanned doctrine win known as the **Locked Palette WIN**. Mid-project, the operator authored an 11-token hex color palette directly into `_project/CLAUDE.md`. This concrete artifact — specific hex values mapped to specific roles — survived across multiple sessions where abstract guidance ("use a coherent palette") had previously decayed.

**The lesson:** Concrete doctrine survives. Abstract doctrine decays.

**The promotion to Factory doctrine:** Every project gets a concrete theming token file from Phase 0 onward, declared as evergreen methodology rather than discovered ad-hoc per project.

This manual is the formalization of that lesson.

---

## 3. The Token Architecture

### 3.1 Semantic Token Categories

Every Stark project declares tokens in these categories. Names match shadcn convention so the entire shadcn ecosystem works out of the box.

| Token | Purpose | Example Use |
|---|---|---|
| `--background` | Default page background | `<body>`, page wrappers |
| `--foreground` | Default text color | Body text, headings |
| `--primary` | Brand primary action color | Primary CTA buttons, key links |
| `--primary-foreground` | Text on primary surfaces | Button labels on primary buttons |
| `--secondary` | Secondary action / surface | Less prominent buttons, secondary cards |
| `--secondary-foreground` | Text on secondary surfaces | Labels on secondary buttons |
| `--accent` | Highlight / hover affordance | Hovered list items, accent surfaces |
| `--accent-foreground` | Text on accent surfaces | Hover-state labels |
| `--muted` | Subtle background, less prominent | Disabled inputs, secondary cards |
| `--muted-foreground` | Captions, labels, secondary text | Form labels, helper text, timestamps |
| `--card` | Card surface background | Card components, panels |
| `--card-foreground` | Text on cards | Card titles, card body text |
| `--popover` | Popover / dropdown background | Menus, popovers, tooltips |
| `--popover-foreground` | Text inside popovers | Menu items, tooltip text |
| `--border` | Default border color | Component borders, dividers |
| `--input` | Input field border / surface | Form inputs, selects |
| `--ring` | Focus ring color | `:focus-visible` outlines |
| `--destructive` | Danger / error color | Delete buttons, error states |
| `--destructive-foreground` | Text on destructive surfaces | Error button labels |
| `--success(-foreground)` | Success state color — fixed meaning | Confirmation toasts, recovered/good values |
| `--warning(-foreground)` | Warning state color — fixed meaning | Caution callouts, pending states |
| `--info(-foreground)` | Neutral informational color | Neutral counts, info badges |
| `--chart-1..5` | Data-viz / KPI series colors | Charts, KPI tiles |
| `--role-superadmin(-foreground)` | Role identity (not a status) | Superadmin badges/labels |
| `--role-admin(-foreground)` | Role identity — never the destructive red | Admin badges/labels |
| `--role-member(-foreground)` | Role identity — may align with success | Member badges/labels |
| `--radius` | One knob for corner language | `0` = Metro flat |

**Discipline:** Only add tokens beyond this list if a real project need surfaces. Resist token sprawl. *(This table matches the GLOBAL_DESIGN_SYSTEM_HANDBOOK §2 canonical contract — that doc is the contract authority; role rules detail in THEME_LIBRARY §2, minted values in TOKEN_FILE.)*

### 3.2 The Files — Where Tokens Live

```
project-root/
├── tailwind.config.ts           # Maps semantic tokens to Tailwind utility classes
├── src/app/globals.{css|scss}   # Token values — match the kit's extension
└── _project/CLAUDE.md           # (Optional) — locks the chosen palette in plain language
```

**The kit's entry stylesheet** (`globals.css` _or_ `globals.scss`) is the executable source of truth. It declares two token sets — one for light mode (`:root`) and one for dark mode (`.dark`). The browser activates the right set based on `prefers-color-scheme` or an app-level toggle.

> **🔧 Entry-stylesheet rule (portability) — added v1.1:** This file is **`globals.css` _or_ `globals.scss`** depending on the kit — **match whatever the kit ships** (`ls src/app/globals.*`; if `package.json` lists `sass`, it's `.scss`). The token content is identical either way. Write it **extension-agnostic**: use `/* */` comments only — never `//`, which is SCSS-only and breaks in `.css`. The extension is a per-kit fact, not doctrine; confirm it up front alongside the Tailwind version.


**`tailwind.config.ts`** maps the CSS custom properties to Tailwind utility names. This is what lets Claudy write `className="bg-primary text-primary-foreground"` and have it resolve to the actual brand color.

**`_project/CLAUDE.md` (the Locked Palette section)** is the human-readable record of what the tokens mean. It cites which hex values were chosen and why. This is the artifact that survives sessions — when Claudy re-reads `_project/CLAUDE.md` at the start of every phase, the palette stays in working memory.

### 3.3 The Light / Dark / Brand Triad

All three coexist in one file:

- **Light mode:** Default `:root` token values
- **Dark mode:** `.dark` class override token values
- **Brand themes (optional):** Additional class overrides like `.theme-frank` or `.theme-cyberize` that swap the primary palette while keeping structural tokens (`--background`, `--foreground`) intact

For most projects, **light + dark is enough**. Brand themes are a Phase 2+ refinement.

---

## 4. The Designer's Deliverable

> **The designer (human or agent) does NOT deliver a Figma file as the primary artifact. They deliver the executable variables file.**

### 4.1 Primary Deliverable — The Tokens File

The designer's binding output is a **filled-in entry-stylesheet snippet** (`globals.css` _or_ `globals.scss` — match the kit; `/* */` comments only) with concrete hex (or HSL) values for every semantic token, for both `:root` (light) and `.dark` (dark).

> **TW3/TW4 format fork:** the value format follows the kit's Tailwind major — confirm in `package.json` (GDSH §2): **TW3** = HSL triplets, no `hsl()` wrapper, mapped in `tailwind.config.ts` (the format shown below); **TW4** = `@theme inline` block, usually OKLCH, `--color-*` naming. The extension AND the format are per-kit facts, not doctrine.

**Format:**

```css
:root {
  --background: 0 0% 100%;           /* white */
  --foreground: 222 47% 11%;         /* near-black */
  --primary: 217 91% 60%;            /* brand blue */
  --primary-foreground: 0 0% 100%;   /* white on blue */
  /* ... all tokens declared ... */
}

.dark {
  --background: 222 47% 11%;
  --foreground: 0 0% 100%;
  --primary: 217 91% 70%;            /* lighter blue for dark mode contrast */
  --primary-foreground: 222 47% 11%;
  /* ... all tokens declared ... */
}
```

Values are typically in **HSL space without the `hsl()` wrapper** — this matches shadcn's convention and lets Tailwind compose with alpha modifiers cleanly.

### 4.2 Supporting Deliverables (Visual Reference, Not Executable)

These help humans understand the designer's intent but are NOT the contract Claudy fabricates against:

- **Style tile** — a one-page image showing the palette, typography, button styles, form fields
- **Screen mockups** — annotated reference screens showing the tokens in real composition
- **Brand rationale** — a one-page document explaining why these tokens were chosen for this brand

These are valuable for stakeholder review and human alignment, but they are **secondary**. The tokens file is primary.

### 4.3 Why This Format

A Figma file is a static artifact that requires translation. CSS variables ARE the translation, pre-done. When the designer delivers tokens directly:

- Claudy reads them and fabricates without interpretation drift
- The operator can swap tokens in five minutes for stakeholder iteration
- The mobile-first plus dark mode behavior is captured in the same artifact
- Future projects can reference past tokens files as starting points

**This is why we don't pay full design agency rates for Figma alone.** Figma is communication; tokens are execution.

---

## 5. The Quick-Swap Workflow (The Pressure-Point Win)

The single biggest operational win this manual enables: **fast brand iteration during stakeholder review.**

**Scenario:** Stakeholder sees the staging deploy and says "the blue feels too cold for a healthcare brand, can we try something warmer?"

**Workflow:**

1. Operator opens the kit's entry stylesheet (`src/app/globals.css` or `globals.scss`)
2. Designer (or operator) updates the `--primary` and `--primary-foreground` tokens to warmer values
3. Commit, push, redeploy (or hot-reload in dev)
4. Stakeholder sees the new palette within minutes, not hours

**This is impossible in projects where colors are hardcoded throughout components.** It is trivial in projects that follow this manual.

---

## 6. Brand Themes (Phase 2+ Refinement)

For multi-tenant projects (like Cyber Pharma with multiple pharmacy subscribers) or projects where the same product ships under multiple brands, **brand themes** are an extension of this manual.

A brand theme is an additional class override in `globals.css`:

```css
.theme-frank {
  --primary: 142 70% 45%;           /* Frank's green */
  --primary-foreground: 0 0% 100%;
  /* selectively override only what differs from default */
}
```

Activated by setting the class on the `<html>` or `<body>` element via app logic. The structural tokens (`--background`, `--foreground`, `--border`) stay constant; only the brand identity tokens swap.

**Discipline:** Brand themes are not Phase 1 scope. Set up the token architecture in Phase 1; layer brand themes in Phase 2 when the real need surfaces.

---

## 7. What This Manual Does NOT Cover

Out of scope for this manual; covered elsewhere:

- **Typography scale** — see UI-UX-BUILDING-MANUAL §Typography
- **Spacing units** — Tailwind defaults; project-specific overrides in `tailwind.config.ts`
- **Component variants** (Button sizes, Card padding) — see COMPONENT_REGISTRY
- **Mobile-first responsive behavior** — see UI-UX-BUILDING-MANUAL Rule Zero
- **Animation tokens** — Phase 2+ concern; not in v1.0 of this manual
- **Icon systems** — see STARTER_KIT_HANDBOOK §Lucide Icons

---

## 8. Anti-Patterns

These are AUTOMATIC FAILURES at any phase gate. Surface immediately if observed.

| Anti-Pattern | What It Looks Like | Why It Fails |
|---|---|---|
| **Hardcoded hex in a component** | `className="bg-[#3b82f6]"` | Breaks theming; brand swap requires search-and-replace across the codebase |
| **Inline color styles** | `style={{ backgroundColor: "#fff" }}` | Same as above, harder to find |
| **Tailwind color names** | `className="bg-blue-500"` | Bypasses semantic tokens; locks brand to Tailwind palette |
| **Designer delivers ONLY a Figma file** | No `globals.css` snippet provided | Forces translation step that introduces drift |
| **Light mode only** | Tokens declared in `:root`, no `.dark` set | Dark mode users see broken contrast |
| **Token sprawl** | 40+ tokens declared, most unused | Cognitive load + maintenance burden; resist beyond §3.1 list |
| **Component overrides palette without surfacing** | A component hardcodes a color "because the token didn't fit" | The token is wrong — surface and update it, don't bypass it |

---

## 9. The Phase 0 / Phase 1 Discipline

When setting up a new project, theming is sequenced as follows:

**Phase 0 (IGNITION):**
- Designer brief explicitly requests the tokens file format (cite this manual)
- Token list confirmed (does this project need beyond §3.1?)
- Light + dark mode confirmed as Phase 1 scope; brand themes deferred to Phase 2 unless explicitly required

**Phase 1 (Foundation Skeleton):**
- Designer delivers the filled `globals.css` snippet
- Operator drops it into `src/app/globals.css`
- `tailwind.config.ts` mapping verified (usually no change needed; shadcn template handles this)
- `_project/CLAUDE.md` updated with the Locked Palette table (the human-readable record)
- Claudy fabricates all Phase 1 UI using semantic tokens only — no hardcoded colors permitted
- Phase 1 verification gate checks for hardcoded color violations via grep

---

## 10. Cross-References

- **UI-UX-BUILDING-MANUAL** §Theming and Design Tokens — the operating doctrine that points here
- **APP_ARCHITECTURE_MANUAL** §Theming Files — the file location convention
- **HANDOFF_PACKAGE_PLAYBOOK** §Designer Handoff — the designer engagement spec
- **STARTER_KIT_HANDBOOK** §shadcn Defaults — what the kit provides out of the box
- **Cyberize Run 001 `_project/CLAUDE.md`** — the canonical worked example of a Locked Palette table

---

## 11. Why This Matters For The Factory

Every future Stark Industries project inherits this doctrine. The Cyberize Locked Palette WIN that emerged accidentally in Run 001 becomes deliberate doctrine in Run 002 (Cyber Pharma) and every run that follows.

**The compounding payoff:**

- Stakeholder demo cycles compress from hours to minutes
- Designer engagement costs drop because the deliverable format is sharper
- Multi-tenant projects (multiple brands on one platform) become trivial instead of expensive
- Cross-project visual consistency emerges because every project speaks the same token language
- New team members onboard faster because the visual identity is in code, not in tribal knowledge

**This is the Stark Industries pattern.** Real artifacts, born of real need. Concrete doctrine, not abstract. Compounding factory IP.

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-06-02 | Initial manual. Born from Cyber Pharma Run 002. Promotes the Cyberize Run 001 Locked Palette WIN into evergreen Factory doctrine. |
| 1.1 | Jun 2026 | **(Entry restored 2026-07-08 — the bump was applied to the header/body but never logged here; F-033 inverse-symptom.)** Added the entry-stylesheet portability rule to §3.2: `globals.css` OR `globals.scss` per kit, extension-agnostic `/* */` comments, per-kit fact not doctrine (L14 institutionalized as verify-then-fork). |
| 1.2 | 2026-07-08 | **Wave 5 (audit sync).** Missing v1.1 history entry restored above — metadata honesty (F-033). Cross-references canonical-name only, §0 + §10: the PHANTOM `HANDOFF_PACKAGE_PLAYBOOK v1.1` (a version that never existed) killed at both sites, plus the stale UI-UX/APP_ARCHITECTURE/handbook versioned refs (F-032/F-011). §3.1 token table aligned to the GDSH §2 canonical contract: success/warning no longer "optional", info/chart-1..5/radius added, the three `--role-*` identity tokens added with their rules one-liners (F-043 consumer alignment). §4.1 gains the TW3/TW4 format fork note (GDSH §2 model). Standard header block (F-018); footer suite label de-versioned. |

---

🥄 *Part of Stark Industries — App Factory doctrine.*
