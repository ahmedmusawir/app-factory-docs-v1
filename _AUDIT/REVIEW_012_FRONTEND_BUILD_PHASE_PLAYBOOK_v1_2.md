# REVIEW 012: 3_METHOD-FRONTEND_BUILD_PHASE_PLAYBOOK_v1_2.md

> **Review Series:** Stark Industries App Factory — Full Doc Stack Audit
> **Reviewer:** Architect Jarvis
> **Date:** 2026-07-06
> **Doc Version Reviewed:** v1.2 per version history (2026-06-25) — ⚠️ top header still claims v1.1/June 2 (F-033)
> **Tier:** 3 — Build Methodology
> **Verdict:** KEEP — v1.2.1 micro-patch (header fix + character repair + tool-agnostic wording)

---

## 1. What This Doc Is

The frontend-first execution manual: six ordered stages (Layout Skeleton → Page Fidelity → UX Polish → Subpages/Edge → Mock-Driven Functionality → Demo Deploy Prep), each with goal/activities/rules/output/stop-condition; §1.5 Pre-Phase Doctrine Refresh; §1.6 Kit Audit; Stage 2 Pre-Write Check; §9 completion checklist with the Gate M responsive block; §12 Kit Improvement Proposals loop; §13 Run 001 lessons appendix.

## 2. Verification Result (carried from Review 011)

✅ **The §14 relocation LANDED at all five promised addresses:** §1.5 Doctrine Refresh, §1.6 Kit Audit, Stage 2 Pre-Write Check, §12 KIPs, §13 Lessons (incl. Lesson 9). The F-017 de-duplication template (relocate + pointer) is now validated end-to-end across both sibling docs.

## 3. Strengths

- **§1.5 Doctrine Refresh (D-014):** "Doctrine read in Phase 0 decays by Stage 5" — a named failure mode with structural enforcement (mandatory re-read, acknowledgment block, STOP condition). Doctrine decay is fought with re-injection, not willpower.
- **§13 Lesson 9** — speculative authoring, discovered when an AI patched this very file without seeing its contents. The factory's no-speculative-writing law lives here; it governed this audit's own refusal to reconstruct repo docs from chunks.
- **Lesson 10 / Gate M "collapse ≠ frame"** — two responsive failure classes, both asserted from mockup CSS, not eyeballed.
- **§12 KIP loop** — the factory's self-improvement made explicit (AppShellPage origin story), with an archive path for rejected proposals.
- Cross-references use canonical unversioned names (F-011-correct) — notably better than its sibling doc.
- Stop conditions per stage — enforceable phase boundaries.

## 4. Findings

| ID | Severity | Finding |
|----|----------|---------|
| F-033 | MEDIUM — header/version mismatch (new type) | Top header: "Version: 1.1, Last Updated: June 2, 2026." Version history + content + filename: v1.2 (June 25, Lesson 10 + Gate M present). First header-lies case (F-016 was filename-lies). A MANIFEST generator parsing the header would misreport. Reinforces F-018 standardized-header rule. |
| F-034 | MEDIUM — character-stripping corruption (new type) | Characters DELETED (not garbled) in an encoding round-trip: "member  admin  superadmin" (arrows), "Successerror" / "datasecurity" (slashes), and §10's table lost its pipes entirely — broken markdown, silent content destruction. Nastier cousin of F-012 mojibake; lint scope expands to character-loss detection. |
| Minor | LOW | §10 "If Cascade misses any" — Windsurf-specific agent named; replace with tool-agnostic "the build agent." |
| F-010 (instance) | — | "Stages" here vs "Sub-Phases" in FFM_PLAYBOOK for the same layer. Canonical phase map should pick one term. |

## 5. Required Changes for v1.2.1 (micro-patch)

1. Fix top header to v1.2 / 2026-06-25 (and adopt the standard header block when F-018 lands).
2. Character repair pass: restore arrows/slashes, rebuild the §10 table.
3. "Cascade" → tool-agnostic wording.
4. Coordinate Stage/Sub-Phase terminology with the F-010 canonical phase map.

## 6. Cross-Doc Dependencies Noted

References (canonical names ✓): FRONTEND_FIRST_PLAYBOOK (sibling, §1), STARTER_KIT_HANDBOOK (§1.5/§1.6), COMPONENT_REGISTRY (§1.5/§1.6), UI-UX-BUILDING-MANUAL (§1.5, Pre-Write Check), FFM_PLAYBOOK §13.1 (Gate M), root CLAUDE.md (Rule Zero), KIT_PROPOSALS_ARCHIVE (referenced artifact), {APPNAME}_DATA_CONTRACT (project artifact). Validates: F-017 fix template (both ends confirmed).

---

*Part of the Factory Doc Stack Audit series. See FINDINGS_LOG.md for the running catch list.*
