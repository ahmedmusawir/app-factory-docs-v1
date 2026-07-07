# REVIEW 026: 5_DESIGN-TOKEN_FILE_v1_1.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v1.1 (Cyber Pharma, Tailwind 3.4 + shadcn)
> **Tier:** 5 — Design System
> **Verdict:** KEEP — v1.2 micro (role-definition sentence, stray fence, history table); post-F-013a: mint --role-* values

---

## 1. What This Doc Is (role now official, per F-025 ruling)

The **concrete values artifact**: the complete drop-in Metro Warm token implementation for Cyber Pharma — full `:root` (Mist) / `.dark` (Slate) HSL blocks + Bright/Dark-deep one-line alternates, the `tailwind.config.ts` mapping, Saira wiring via next/font, usage rules, per-mode contrast notes with guards. **Reference snapshot + drop-in template — NOT the live token file** (that is each project's `globals.css`, GDSH §8). The D-001 pairing made flesh: THEMING_MANUAL = rules; this = the worked example with every value filled in.

## 2. Strengths

- **Portability rule fully present** (confirmed stack; match-the-kit css/scss logic; `/* */` comments only) — F-038-model compliant.
- **Token set matches the GDSH contract** (incl. --info, --chart-1..5, --radius) — concrete proof THEMING §3.1's table is the stale edge in the three-way alignment.
- Per-mode contrast notes WITH guard rails ("Do not lighten the light-mode values"); L16 Slate fixes present and annotated.
- Usage rules crisp ("Status colors are sacred"); Phase-1 migration task named; one-knob radius note.
- Values cross-check clean against THEME_LIBRARY (Mist/Slate/Bright/Dark-deep consistent).

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-043 (third witness) | — | NO `--role-*` tokens in the concrete values file. Tally: contract (GDSH) lacks them; values artifact lacks them; only THEME_LIBRARY carries them — **and only as rules, not HSL values.** F-013a's implementation therefore = contract edit (GDSH §2) + rules already written (Library §2) + **minting actual Metro Warm role values here** (superadmin/admin/member hues, AA per mode). Complete three-file plan attached to the decision. |
| F-025 (closure item) | LOW | Header line "This is the executable design system" conflates this doc with the live globals.css — the exact confusion that produced Designer Playbook §13. v1.2 adds the role sentence: "Reference values for Cyber Pharma / Metro Warm; the live file is the project's entry stylesheet." |
| Byte bug | TRIVIAL | Stray orphan ``` fence at final line. |
| F-018 (light) | LOW | No version-history table (version lives in title only). |

## 4. Required Changes for v1.2 (micro)

1. Role-definition sentence in header (closes the F-025 terminology chain).
2. Remove stray fence; add version-history table.
3. Post-F-013a: add the `--role-*` block (both modes, AA-checked) — coordinated with GDSH §2 + Library.

## 5. Cross-Doc Dependencies Noted

Pairs (D-001): THEMING_MANUAL (rules → this example). Values source for/consistent with: THEME_LIBRARY (Metro Warm). Contract: GDSH (matches; awaiting --role-* jointly). Consumed by: Designer/Claudy at Phase 1 token install; referenced by DESIGNER_PLAYBOOK §13 (post-fix).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
