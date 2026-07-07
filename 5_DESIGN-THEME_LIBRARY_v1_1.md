# THEME LIBRARY — Cyber Pharma (and the factory pattern)

> **Reader:** Designer (me, in future labs) + Claudy.
> **Pairs with:** the **Global Design System Handbook** (defines the token *contract*) and each project's **token file** (`globals.css` — the live values). This doc is the *catalog*: named themes that each satisfy the contract.
> **Mental model:** the Handbook says *which tokens must exist*; `globals.css` holds *the active values*; this library is the *menu* of complete value-sets you can drop in. Adding a theme never touches the contract — only values.
>
> **v1.1 reconciliation note (2026-06-08):** Two changes only. (1) The live token file is **`globals.css`**, not `TOKEN_FILE.md` — references corrected throughout (the Global Design System Handbook §8 names `globals.css` as the primary deliverable; this aligns to it). (2) The contract now includes **role identity tokens** (`--role-*`) — see §2. Theme content is otherwise unchanged.

---

## 1. How a theme entry works

A theme = **one complete semantic token set** (every token the Handbook requires), in HSL-no-wrapper, activated by a class on `<html>`. Components never change; only the variables behind `bg-primary`, `bg-card`, etc. resolve differently. That's the whole "change values, not code" promise.

- **Light-base themes** live on `:root` (or a `.theme-*` override).
- **Dark-base themes** live on `.dark` (or `.dark.theme-*`).
- Full values for the two defaults are in `globals.css` (`:root` + `.dark`); the alternates are the small `.theme-*` override blocks there.

---

## 2. The "Metro Warm" family (Cyber Pharma v1)

Shared across **all four** (these never change between modes — brand + meaning + identity hold):

| | Value |
|---|---|
| Primary (brand) | coral `#f9704f` → `12 93% 64%` |
| Success (recovered) | green — `131 54% 40%` light / `142 69% 58%` dark |
| Destructive (money lost) | red — `2 67% 51%` light / `351 95% 71%` dark |
| Info (neutral count) | blue `#2f7ce0` → `214 74% 53%` |
| Warning (pending) | amber `#e8a008` → `41 93% 47%` |
| Role — superadmin | identity hue, distinct from brand & status *(set per family; AA on `--card`)* |
| Role — admin | identity hue — **must not reuse the destructive red** |
| Role — member | identity hue — may align with `--success` |
| Typeface | Saira |
| Radius | `0` (Metro flat) |
| Labels | uppercase, tracked |

> **Role tokens (added v1.1):** roles are identities, not statuses. They hold their hue across all four modes just like the semantic four. The only hard rule: `--role-admin` must read as visually distinct from `--destructive` so an admin badge never looks like an error. Tune each role's lightness per mode and contrast-check on the style tile.

What changes between modes is **only the neutral surface stack**:

### 🟫 Mist — *default light*
- **Base:** light · **Background:** `#e2e5ea` (`217 16% 90%`) · **Surface:** `#ffffff`
- **Activate:** `:root` (default — no class)
- **Best for:** the everyday daytime view. Muted, easy on the eyes, looks intentional rather than glaring. **This is the recommended default.**

### 🌑 Slate — *default dark*
- **Base:** dark · **Background:** `#1d212a` (`222 18% 14%`) · **Surface (card):** `#2e3440` (`220 16% 22%`)
- **Activate:** `class="dark"`
- **Best for:** low-light work, long sessions. Sophisticated gunmetal; coral pops hardest here.
- **Readability note (L16):** background sits *below* the card so panels elevate; `--muted-foreground` is lifted (`221 17% 71%`) and `--border` firmed (`218 13% 33%`). This is the v1.1 real-screen fix — keep it; do not flatten background and card to the same value.

### ⬜ Bright — *alternate light*
- **Base:** light · **Background:** `#ffffff` · **Surface:** `#ffffff`
- **Activate:** `class="theme-bright"`
- **Best for:** maximum contrast, print/export views, screenshots for decks. Crisp but can glare on big screens.

### ⬛ Dark-deep — *alternate dark*
- **Base:** dark · **Background:** `#191c24` (`224 18% 12%`) · **Surface:** `#23262f`
- **Activate:** `class="dark theme-deep"`
- **Best for:** OLED / focus mode / demo drama. Near-black; reserve for when you want the charts to glow.

**Phase 1 ships Mist + Slate** wired to the theme toggle. Bright and Dark-deep are catalogued and ready, not yet wired.

---

## 3. Adding a new theme (the repeatable process)

1. **Pick the neutral direction** — only the surface stack changes (background, card, muted, border, secondary). Brand + semantic + role stay fixed.
2. **Derive the full set** — every token the Handbook lists, light *and*/or dark base. Don't ship a partial theme.
3. **Contrast-check** — run `success`/`destructive` (and the `--role-*` colors) as small text against the new `card`; tune lightness until all clear WCAG AA. (This is the step a 4-color palette can't give you.)
4. **Add as a class** — a `.theme-*` override block in `globals.css`. Nothing else changes.
5. **Catalog it here** — name, base, background, "best for", activation class.
6. **Render the style tile in it** — eyeball light + dark, then a real-screen pass, before locking.

A new theme is ~30 minutes and zero component changes. That's the payoff.

---

## 4. Per-tenant brand themes (multi-tenant, future)

Cyber Pharma is multi-tenant. When a client wants their own brand color, it's the same mechanism scoped to a class:

```css
.theme-acme { --primary: <acme hsl>; --ring: <acme hsl>; --accent: <acme hsl>; }
```

- Swap **only** `--primary` / `--accent` / `--ring`. **Never** the semantic four or the role tokens — underpaid must read red, and an admin must read like an admin, for every client.
- Apply the class at the tenant boundary (layout reads the org's theme).
- This keeps a per-pharmacy brand a one-line addition, not a fork.

> Defer building this until multi-tenant brand theming is actually scoped (it's Phase 7-ish). The architecture above means it costs nothing to add later.

---

## 5. Quick reference — activation

| Theme | Class on `<html>` |
|---|---|
| Mist (light default) | *(none)* |
| Slate (dark default) | `dark` |
| Bright | `theme-bright` |
| Dark-deep | `dark theme-deep` |
| Tenant brand (future) | `theme-<tenant>` (+ `dark` if dark base) |

Full token values: `globals.css`. Visual proof of all modes: the style tile + the OwedBook Mist/Slate/Dark artifacts in `_design/`.

---

## Cross-References

- **`agent_docs/APP_FACTORY/design-system/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`** — the token contract this library satisfies.
- **`agent_docs/APP_FACTORY/STARTER_KIT_HANDBOOK.md`** — kit primitives; its §8 Theme Conventions and §2 Role Colors defer to these tokens.
- **`globals.css`** — the live token file (per project).

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.1 | 2026-06-08 | Corrected `TOKEN_FILE.md` → `globals.css` as the live token file (aligns with GDSH §8); added `--role-*` tokens to the Metro Warm family + the add-a-theme contrast step + the multi-tenant rule; folded the L16 Slate readability fix into the Slate entry; added cross-references. Theme values unchanged. |
| (prior) | — | Initial Theme Library (Mist / Slate / Bright / Dark-deep). |

---

🥄 *Part of Stark Industries — App Factory doctrine. The Handbook defines the contract; this is the menu.*
