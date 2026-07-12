# TOKEN FILE — Cyber Pharma / Metro Warm (Tailwind 3.4 + shadcn)

> **Version:** 1.2 · **Date:** 2026-07-08 · **Status:** Active
> **Tier:** 5 — Design System · **Pairs with:** GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, THEMING_MANUAL, DESIGNER_PLAYBOOK

> **Role of this doc (F-025):** **reference values for Cyber Pharma / Metro Warm — a drop-in template.** The LIVE token file is each project's entry stylesheet (`globals.css`/`.scss`), not this doc (GDSH §8 ruling).
> **Confirmed stack:** `tailwindcss@^3.4.1` → classic shadcn convention.
> **Format:** CSS variables in the kit's **entry stylesheet** (`globals.css` _or_ `globals.scss` — **match the kit**, e.g. `ls src/app/globals.*`; if `package.json` has `sass`, it's `.scss`) as **HSL, no `hsl()` wrapper**; mapped in `tailwind.config.ts`. Comments are `/* */` only (portable across `.css` and `.scss`); never `//`.
> Every screen reads these via semantic utilities (`bg-primary`, `text-destructive`, `bg-card`) — never numbered colors (`bg-slate-800`).
> Hex in comments is human reference only; the HSL triplet is the source of truth.

---

## 1. Entry stylesheet (`globals.css` _or_ `globals.scss`)

Drop into the kit's entry stylesheet (match its extension). Replace the existing `:root` / `.dark` token blocks with these. **`:root` = Mist (default light), `.dark` = Slate (default dark)** — the two modes Phase 1 ships. Bright and Dark-deep are included as optional alternates (Theme Library) — wire to a switcher later.

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  /* ── LIGHT · "Mist" (default) ───────────────────────────── */
  :root {
    --background: 217 16% 90%;          /* #e2e5ea */
    --foreground: 219 16% 17%;          /* #252a33 */
    --card: 0 0% 100%;                  /* #ffffff */
    --card-foreground: 219 16% 17%;
    --popover: 0 0% 100%;
    --popover-foreground: 219 16% 17%;

    --primary: 12 93% 64%;              /* #f9704f coral */
    --primary-foreground: 0 0% 100%;
    --secondary: 220 19% 94%;           /* #eceef2 panel */
    --secondary-foreground: 219 16% 17%;
    --muted: 222 15% 87%;               /* #d9dce3 */
    --muted-foreground: 218 12% 42%;    /* #5f6878 */
    --accent: 12 93% 64%;               /* coral */
    --accent-foreground: 0 0% 100%;

    --border: 220 12% 75%;              /* #b8bdc7 */
    --input: 220 12% 75%;
    --ring: 12 93% 64%;                 /* coral focus */

    /* semantic — FIXED MEANING across all themes */
    --destructive: 2 67% 51%;           /* #d6322c underpaid/lost */
    --destructive-foreground: 0 0% 100%;
    --success: 131 54% 40%;             /* #2f9e44 recovered */
    --success-foreground: 0 0% 100%;
    --warning: 41 93% 47%;              /* #e8a008 pending */
    --warning-foreground: 0 0% 100%;
    --info: 214 74% 53%;                /* #2f7ce0 neutral counts */
    --info-foreground: 0 0% 100%;

    /* data-viz / KPI tiles */
    --chart-1: 2 67% 51%;               /* red */
    --chart-2: 214 74% 53%;             /* blue */
    --chart-3: 131 54% 40%;             /* green */
    --chart-4: 359 63% 42%;             /* maroon */
    --chart-5: 12 93% 64%;              /* coral */

    /* role identity — identities, not statuses; hue holds across modes (GDSH §2) */
    --role-superadmin: 262 52% 47%;     /* #6d48b7 purple — 6.4:1 on card */
    --role-superadmin-foreground: 0 0% 100%;
    --role-admin: 189 65% 32%;          /* #1d7987 teal — 5.1:1 on card; NOT the destructive red */
    --role-admin-foreground: 0 0% 100%;
    --role-member: 131 40% 33%;         /* #33763f green (aligns w/ success) — 5.5:1 on card */
    --role-member-foreground: 0 0% 100%;

    --radius: 0px;                      /* Metro flat */
  }

  /* ── DARK · "Slate" (default dark) ──────────────────────── */
  /* v1.1 readability pass: background dropped below card so panels
     elevate; muted-foreground lifted; borders firmed. */
  .dark {
    --background: 222 18% 14%;          /* #1d212a — page (now darker than card) */
    --foreground: 222 26% 93%;          /* #e7eaf1 */
    --card: 220 16% 22%;                /* #2e3440 — elevated surface */
    --card-foreground: 222 26% 93%;
    --popover: 220 16% 22%;
    --popover-foreground: 222 26% 93%;

    --primary: 12 93% 64%;              /* coral holds across modes */
    --primary-foreground: 0 0% 100%;
    --secondary: 221 16% 27%;           /* #3a4150 */
    --secondary-foreground: 222 26% 93%;
    --muted: 220 16% 19%;               /* #282d37 */
    --muted-foreground: 221 17% 71%;    /* #a9b1c2 — readable secondary text/placeholders */
    --accent: 12 93% 64%;
    --accent-foreground: 0 0% 100%;

    --border: 218 13% 33%;              /* #49515f — firmer edges */
    --input: 218 13% 33%;
    --ring: 12 93% 64%;

    /* semantic — brightened for dark surfaces, same meaning */
    --destructive: 351 95% 71%;         /* #fb7185 */
    --destructive-foreground: 222 20% 13%;
    --success: 142 69% 58%;             /* #4ade80 */
    --success-foreground: 222 20% 13%;
    --warning: 41 93% 47%;              /* #e8a008 */
    --warning-foreground: 222 20% 13%;
    --info: 214 74% 53%;
    --info-foreground: 0 0% 100%;

    --chart-1: 351 95% 71%;
    --chart-2: 214 74% 53%;
    --chart-3: 142 69% 58%;
    --chart-4: 359 63% 42%;
    --chart-5: 12 93% 64%;

    /* role identity — same hues as light, lightness tuned for the dark card */
    --role-superadmin: 262 70% 74%;     /* #b28eeb — 4.7:1 on card (tightest cell: eyeball this FIRST on the style tile) */
    --role-superadmin-foreground: 222 20% 13%;
    --role-admin: 189 60% 60%;          /* #5cc4d6 — 6.1:1 on card */
    --role-admin-foreground: 222 20% 13%;
    --role-member: 131 55% 65%;         /* #75d787 — 7.0:1 on card */
    --role-member-foreground: 222 20% 13%;
  }

  /* ── OPTIONAL ALTERNATES (Theme Library) ────────────────── */
  /* Bright: pure-white light. Apply class on <html>: class="theme-bright" */
  .theme-bright { --background: 0 0% 100%; --secondary: 220 19% 96%; --muted: 220 16% 94%; }
  /* Dark-deep: near-black dark. Apply within dark: class="dark theme-deep" */
  .dark.theme-deep { --background: 224 18% 12%; --card: 225 16% 16%; --popover: 225 16% 16%; }
}

@layer base {
  * { @apply border-border; }
  body { @apply bg-background text-foreground font-brand; }
}
```

---

## 2. `tailwind.config.ts` (mapping)

Merge into the existing config's `theme.extend`. This is what turns `--primary` into the `bg-primary` utility. **No numbered palette is referenced — that's intentional.**

```ts
import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        card: { DEFAULT: "hsl(var(--card))", foreground: "hsl(var(--card-foreground))" },
        popover: { DEFAULT: "hsl(var(--popover))", foreground: "hsl(var(--popover-foreground))" },
        primary: { DEFAULT: "hsl(var(--primary))", foreground: "hsl(var(--primary-foreground))" },
        secondary: { DEFAULT: "hsl(var(--secondary))", foreground: "hsl(var(--secondary-foreground))" },
        muted: { DEFAULT: "hsl(var(--muted))", foreground: "hsl(var(--muted-foreground))" },
        accent: { DEFAULT: "hsl(var(--accent))", foreground: "hsl(var(--accent-foreground))" },
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        // semantic (fixed meaning)
        destructive: { DEFAULT: "hsl(var(--destructive))", foreground: "hsl(var(--destructive-foreground))" },
        success: { DEFAULT: "hsl(var(--success))", foreground: "hsl(var(--success-foreground))" },
        warning: { DEFAULT: "hsl(var(--warning))", foreground: "hsl(var(--warning-foreground))" },
        info: { DEFAULT: "hsl(var(--info))", foreground: "hsl(var(--info-foreground))" },
        // data-viz / KPI tiles
        chart: {
          1: "hsl(var(--chart-1))", 2: "hsl(var(--chart-2))", 3: "hsl(var(--chart-3))",
          4: "hsl(var(--chart-4))", 5: "hsl(var(--chart-5))",
        },
        // role identity (identities, not statuses — GDSH §2)
        role: {
          superadmin: { DEFAULT: "hsl(var(--role-superadmin))", foreground: "hsl(var(--role-superadmin-foreground))" },
          admin: { DEFAULT: "hsl(var(--role-admin))", foreground: "hsl(var(--role-admin-foreground))" },
          member: { DEFAULT: "hsl(var(--role-member))", foreground: "hsl(var(--role-member-foreground))" },
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      fontFamily: {
        brand: ["var(--font-brand)", "system-ui", "sans-serif"],
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
};

export default config;
```

---

## 3. Font wiring (`next/font`, not a CDN link)

In the root layout:

```ts
import { Saira } from "next/font/google";
const saira = Saira({ subsets: ["latin"], weight: ["300","400","500","600","700","800"], variable: "--font-brand" });
// <html lang="en" className={`${saira.variable}`}> ... (add "dark" for Slate default)
```

---

## 4. Usage rules (the discipline that keeps it swappable)

- **Use:** `bg-primary`, `text-destructive`, `bg-card`, `border-border`, `text-muted-foreground`, `bg-chart-1`, `text-success`.
- **Never:** `bg-slate-800`, `text-red-600`, `dark:bg-zinc-900`, or any numbered Tailwind color. They ignore the token file and silently break theming.
- **Status colors are sacred:** `success` = recovered, `destructive` = money-lost, `info` = neutral count. Never repaint them per theme; never use `primary` (coral) for a status.
- **Role badges read the role tokens:** `bg-role-admin text-role-admin-foreground` (or `text-role-superadmin` on `--card`). Roles are identities, not statuses — never style an admin badge with `destructive`.
- **Migration task (Phase 1):** replace the kit's hardcoded `dark:bg-slate-800` and role `text-red-600/green-600/purple-600` with these tokens — the role colors now have their own `--role-*` homes, so the theme is actually centralized.

---

## 5. Notes

- Contrast: `--success` / `--destructive` were tuned per-mode (darker on light, brighter on dark) specifically so they stay legible as small numbers in the OwedBook table on both `--card` backgrounds. Verified in the style tile. Do not lighten the light-mode values.
- **Role-token contrast (v1.2, computed — style-tile render pending):** all six role values clear WCAG AA as small text on their mode's `--card`. The tightest cell is `--role-superadmin` dark at **4.7:1** — eyeball that one FIRST when the style tile renders. Admin (189° teal) is deliberately far from the destructive red; member shares the success hue by design (Theme Library §2 rules).
- **Bright / Dark-deep alternates need no role overrides:** they swap surface tokens only; the role values inherit from `:root`/`.dark`. Dark-deep's darker card only improves role contrast; Bright's card stays white.
- The four modes are one token swap each — Mist/Slate ship now; Bright/Dark-deep are catalogued for the Theme Library doc.
- `--radius: 0px` gives the Metro-flat look globally; change this one value to soften every corner at once if direction ever shifts.

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | (original) | Initial Metro Warm token file for Cyber Pharma (Mist/Slate + alternates, Tailwind map, Saira wiring, usage rules). |
| 1.1 | Jun 2026 | Slate readability pass (L16): background dropped below card, muted-foreground lifted, borders firmed; per-mode contrast notes + guards. |
| 1.2 | 2026-07-08 | **Wave 5 — the role mint (F-013a/F-043) + F-025 closure.** Role sentence added to the header: this doc = REFERENCE VALUES / drop-in template; the live file is the project's entry stylesheet (GDSH §8). Minted `--role-superadmin/admin/member(-foreground)` for both shipping modes, AA-computed on each mode's `--card` (superadmin 262° purple 6.4:1/4.7:1 · admin 189° teal — NOT destructive red — 5.1:1/6.1:1 · member 131° success-aligned 5.5:1/7.0:1); hues hold across modes per THEME_LIBRARY §2 / GDSH §2. Tailwind `role.*` mapping added; usage rule + migration task updated (kit's hardcoded role colors → these tokens); alternates-need-no-overrides note. Stray orphan code fence at EOF removed; standard header + this history table (F-018/D-018). |
