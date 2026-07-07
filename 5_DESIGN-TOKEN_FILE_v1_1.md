# TOKEN FILE — Cyber Pharma v1.1 (Tailwind 3.4 + shadcn)

> **Confirmed stack:** `tailwindcss@^3.4.1` → classic shadcn convention.
> **Format:** CSS variables in the kit's **entry stylesheet** (`globals.css` _or_ `globals.scss` — **match the kit**, e.g. `ls src/app/globals.*`; if `package.json` has `sass`, it's `.scss`) as **HSL, no `hsl()` wrapper**; mapped in `tailwind.config.ts`. Comments are `/* */` only (portable across `.css` and `.scss`); never `//`.
> **This is the executable design system.** Every screen reads these via semantic utilities (`bg-primary`, `text-destructive`, `bg-card`) — never numbered colors (`bg-slate-800`).
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
- **Migration task (Phase 1):** replace the kit's hardcoded `dark:bg-slate-800`, role `text-red-600/green-600/purple-600`, etc. with these tokens so the theme is actually centralized.

---

## 5. Notes

- Contrast: `--success` / `--destructive` were tuned per-mode (darker on light, brighter on dark) specifically so they stay legible as small numbers in the OwedBook table on both `--card` backgrounds. Verified in the style tile. Do not lighten the light-mode values.
- The four modes are one token swap each — Mist/Slate ship now; Bright/Dark-deep are catalogued for the Theme Library doc.
- `--radius: 0px` gives the Metro-flat look globally; change this one value to soften every corner at once if direction ever shifts.
```
