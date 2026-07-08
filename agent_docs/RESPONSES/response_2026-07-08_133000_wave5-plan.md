# 📋 WAVE 5 PLAN — Design Tier Sync (6 docs) + the --role-* three-file gate

> Status: PENDING_APPROVAL · 2026-07-08 · Gate = --role-* consistency across GDSH (contract) + THEME_LIBRARY (rules) + TOKEN_FILE (values).

## Required reading completed

F-013a (CONFIRMED YES) / F-043 / F-025 / F-032-phantom / F-033 / F-011 / F-012 / F-018 / D-017 ✓ · REVIEW_022–027 ✓ · THEME_LIBRARY §2 rules payload ✓ · GDSH §2 + TOKEN_FILE read in full ✓

## Pre-plan scan

All six docs: C1 = 0, CR = 0, broken-dash = 0. UI-UX carries **3** `â` chars (REVIEW_023 said 1 — will characterize at execution and repair all). Phantom `HANDOFF_PACKAGE_PLAYBOOK v1.1` located: THEMING lines 17 + 261; UI-UX line 126. Stale versioned refs: THEMING ×6 more (lines 7, 15–16, 259–260, 262), UI-UX ×5 more (73–75, 124–125). UI-UX lines 2091/2119 are history/appendix narrative — exempt (D-018 honest record).

---

## THE MINT (before/after gate)

### GDSH §2 — contract addition (AFTER)

Canonical set line gains: `--role-superadmin(-foreground)` `--role-admin(-foreground)` `--role-member(-foreground)`

New rules bullet:
> - **Role identity tokens** (v1.1, F-013a): roles are **identities, not statuses** — each holds its hue across all modes like the semantic four. `--role-admin` must never read as the destructive red (an admin badge is not an error); `--role-member` may align with `--success`. Contrast-check every role as small text on `--card` per mode (AA — verify on the style tile). Multi-tenant theming swaps brand tokens only — **never** the semantic four or the role tokens. Rules detail: Theme Library §2 · minted reference values: TOKEN_FILE.

### TOKEN_FILE — minted Metro Warm values (AFTER; AA figures computed against the file's own --card values)

`:root` (Mist — light; card = #ffffff):
```css
    /* role identity — identities, not statuses; hue holds across modes */
    --role-superadmin: 262 52% 47%;     /* #6d48b7 purple — 6.4:1 on card */
    --role-superadmin-foreground: 0 0% 100%;
    --role-admin: 189 65% 32%;          /* #1d7987 teal — 5.1:1 on card; NOT the destructive red */
    --role-admin-foreground: 0 0% 100%;
    --role-member: 131 40% 33%;         /* #33763f green (aligns w/ success) — 5.5:1 on card */
    --role-member-foreground: 0 0% 100%;
```

`.dark` (Slate; card = #2e3440):
```css
    /* role identity — same hues, lightness tuned for dark card */
    --role-superadmin: 262 70% 74%;     /* #b28eeb — 4.7:1 on card */
    --role-superadmin-foreground: 222 20% 13%;
    --role-admin: 189 60% 60%;          /* #5cc4d6 — 6.1:1 on card */
    --role-admin-foreground: 222 20% 13%;
    --role-member: 131 55% 65%;         /* #75d787 — 7.0:1 on card */
    --role-member-foreground: 222 20% 13%;
```

+ `tailwind.config.ts` mapping rows (`role: { superadmin/admin/member: hsl(var(--role-*)) , *-foreground }` styled like the file's existing entries) + a note: **Bright/Dark-deep alternates need no role overrides** (they swap surface tokens only; role values inherit from :root/.dark and stay AA on both alternate cards — Dark-deep's darker card only improves contrast) + §4 usage line (role badges read `--role-*`; the Phase-1 migration line's hardcoded role reds/greens/purples now map here) + the F-025 role sentence in the header + stray-fence removal + history table.

**Hue rationale (consistency proof):** superadmin 262° purple (distinct from brand coral 12°, all four statuses, and charts); admin 189° teal (≠ destructive 2°/351° red — the hard rule; ≠ info 214° azure by 25° + different family); member 131° = the success hue (explicitly permitted by Library §2). Identities hold hue across modes; only lightness tunes. Labeled REFERENCE VALUES (Cyber Pharma / Metro Warm) per the F-025 role sentence.

---

## Per-doc plans (2–6)

- **DOC 3 THEMING → v1.2:** missing v1.1 history entry ADDED (entry-stylesheet portability rule, 2026-06; F-033 inverse-symptom fix); 8 versioned refs → canonical incl. phantom ×2 (F-032/F-011); §3.1 token table aligned to the GDSH contract (success/warning no longer "optional"; add info/chart-1..5/radius/role rows); §4.1 gains the TW3/TW4 verify-then-fork pointer (GDSH §2 model); standard header; v1.2 row.
- **DOC 4 UI-UX → v1.4 (micro):** 6 versioned refs → canonical incl. THE PHANTOM (F-032); 3 mojibake chars repaired; standard header block; v1.4 history row. Nothing else (MODEL doc; D-018 appendix untouched).
- **DOC 5 THEME_LIBRARY → v1.2:** v1.1 note's "the contract now includes --role-*" → "defined in the contract (GDSH §2), rules here (§2), reference values in TOKEN_FILE" (the one-sided reconciliation is now two-sided); standard header line added above the existing blockquote; title scope note generalized ("first family: Metro Warm (Cyber Pharma); further families append"); v1.2 row. Content otherwise untouched (cleanest doc in the audit).
- **DOC 6 REGISTRY → v1.1 content-tag (optional enrichments):** formal Version line in header (F-018); ONE decision-tree row: "Role badge → styled Badge reading `--role-*` tokens (GDSH §2) — do not hardcode role colors"; v1.1 note appended to its reconciliation changelog. Nothing else.
- **DOC 1 GDSH → v1.1** as above + standard header + version-history table (was unversioned; v1.0 "(original, date unknown)").
- **DOC 2 TOKEN_FILE → v1.2** as above.

## Order & gates

GDSH → TOKEN_FILE → THEMING → UI-UX → THEME_LIBRARY → REGISTRY (contract first, values second, consumers after). One suggested commit per doc; stop each time. Gates: three-file consistency (same 3 role names, same rules, values satisfy rules); phantom grep → 0 across the six; `_v`/versioned refs live → 0; 3-class encoding → 0 ×6; headers + history rows 6/6; per-doc CHANGES/DIDN'T TOUCH/CONCERNS.

## Files I will NOT touch

STARTER_KIT_HANDBOOK (its §2 Role Colors defer-line is repo-side reality — kit-verification touch), all Tier 1–4 docs, _AUDIT/, _OTHERS/. AA figures are computed (WCAG relative-luminance), not eyeballed — but the style-tile render remains the operator's visual confirmation (noted in CONCERNS).
