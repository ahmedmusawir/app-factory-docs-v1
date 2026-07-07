# REVIEW 024: 5_DESIGN-THEMING_MANUAL_v1_1.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v1.1 per header — ⚠️ Version History table records only v1.0 (F-033 extension)
> **Tier:** 5 — Design System
> **Verdict:** KEEP — v1.2 patch (record v1.1 history entry, canonical refs, contract-table alignment post-F-043)

---

## 1. What This Doc Is

The token-architecture deep dive: tokens-before-pixels, the Locked Palette WIN origin (Run 001 → evergreen doctrine), semantic token categories + file locations, the v1.1 entry-stylesheet portability rule (css/scss per kit, extension-agnostic comments), designer's tokens-file-primary deliverable spec, quick-swap workflow, brand themes (Phase 2+), anti-patterns table, Phase 0/1 discipline with grep-verified gate. Closes the F-005 arc (the v1.0/v1.1 duplicate that opened this audit).

## 2. Strengths

- **§7 explicit out-of-scope with pointers** — the territory declaration every Tier 4 manual lacked (F-040's cure, demonstrated in-house).
- **v1.1 entry-stylesheet rule** — L14 institutionalized as verify-then-fork ("a per-kit fact, not doctrine; confirm up front") — F-038-model compliant.
- §2 origin story keeps the tier thesis consistent ("concrete doctrine survives, abstract decays"); "Figma is communication; tokens are execution."
- §8 anti-patterns as automatic failures; §9 grep-verified phase gate; §0 Reader's Guide with when-to-read triggers.
- Proper top header (version/born-from/status/parent doctrine).

## 3. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-033 (extension — inverse symptom) | MEDIUM | Header claims v1.1; §3.2 carries an "added v1.1" note; Version History table records ONLY v1.0. The bump was applied but never logged. (Build-Phase: header lagged history; here: history lags header.) Fix: add the v1.1 entry (entry-stylesheet rule, date). |
| F-032 (5th extension — PHANTOM RECURS) | MEDIUM | Stale/versioned refs in header/§0/§10: UI-UX v1.2 (→v1.3), STARTER_KIT_HANDBOOK v1.0, APP_ARCHITECTURE v1.2 (versioned) — and **`HANDOFF_PACKAGE_PLAYBOOK v1.1` AGAIN** (same phantom as UI-UX manual; Handoff is v1.0). Two independent citations of a nonexistent version → either a lost v1.1 fork (F-022-style) or copy-propagation. **Tony question queued: did Handoff ever have a v1.1?** |
| F-043 (alignment note) | LOW | §3.1 token table marks success/warning optional, omits info/chart-*/radius — GDSH's canonical contract includes them. Edges disagree between contract and deep-dive. Align §3.1 to the contract when F-043/F-013a settle (+ add TW4-fork pointer; §4.1 assumes TW3 HSL convention). |

## 4. Required Changes for v1.2

1. Add the missing v1.1 Version History entry (metadata honesty).
2. Canonical-name cross-references (kills the phantom + stale set).
3. Align §3.1 token table to GDSH contract post-F-043; add TW3/TW4 fork pointer to §4.1.

## 5. Cross-Doc Dependencies Noted

Parent/pointing docs: UI-UX-BUILDING-MANUAL (Rule Zero-B companion — authored this doc at its v1.2), APP_ARCHITECTURE_MANUAL, HANDOFF_PACKAGE_PLAYBOOK (phantom v1.1 — recurrence), STARTER_KIT_HANDBOOK. Contract authority: GDSH §2 (F-043 alignment pending). Consistent with: F-025 settled ruling (tokens file = globals.css/scss primary deliverable).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
