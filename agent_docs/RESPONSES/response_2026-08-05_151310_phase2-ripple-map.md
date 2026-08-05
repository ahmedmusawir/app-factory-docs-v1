# RIPPLE_MAP — Navbar Saga — 2026-08-05

> Phase 2 output of the `factory-docs-update` skill. Drafted by the Engineer (Claudy) — Architect (Jarvis) not in the loop; INFERENCE labels applied where reasoning from the dependency graph.
> Approved by the Operator at Stop Gate 2. This map — not memory, not the branch — is the single source of truth for Phase 4 execution.

## Entries in scope
| Entry/Lesson ID | One-line summary | Source (pack / lessons file) |
|-----------------|------------------|------------------------------|
| Entry 1 | AUTH_MANUAL: new § "Server-Resolved Identity for UI (The Navbar Law)" after "Server-Side Protection (RBAC)" | DOCTRINE_PROMOTION_2026-08-04_NAVBAR_SAGA.md |
| Entry 2 | STATE_MANAGEMENT_MANUAL: "Division of Labor" subsection appended to §1 + cross-ref line under Cross-References | DOCTRINE_PROMOTION_2026-08-04_NAVBAR_SAGA.md |
| Entry 4 | FRONTEND_BUILD_PHASE_PLAYBOOK: Gate Q/D checklist items appended to §9 UI Phase Completion Checklist | DOCTRINE_PROMOTION_2026-08-04_NAVBAR_SAGA.md |

## Splits parked (NOT this run — other repos)
| Entry | Target repo / location | Why parked |
|-------|------------------------|------------|
| Entry 3 | `stark-frontend-first` skill folder (separate repo) | Targets a skill's ANTI_PATTERNS.md — not a Hub doc. Named follow-up: "land Entry 3 (UI/Navigation Anti-Patterns) into stark-frontend-first skill." |
| Pack landing instruction #3 | Kit verification-cluster (separate repo) | `fixed inset-0` grep addition targets the kit's C5-style grep list — not a Hub doc. Named follow-up: "add `fixed inset-0` grep to kit verification-cluster (layout/nav/global components only)." |

## Touch list (execute lightest ← first, heaviest ← last)
| # | Doc (canonical name) | ← count (MANIFEST) | Placement (VERIFIED vs live structure) | Change summary | New version | Rename/move? |
|---|----------------------|--------------------|----------------------------------------|----------------|-------------|--------------|
| 1 | QA_PLAYBOOK (new) | 0 | N/A — new doc entering Hub | Tier line aligned to `3 — Build Methodology`; content untouched. Standard header already present (v0.1). | 0.1 | NO |
| 2 | BUG_FIX_PLAYBOOK (new) | 0 | N/A — new doc entering Hub | Tier line aligned to `3 — Build Methodology`; content untouched. Standard header already present (v0.1). | 0.1 | NO |
| 3 | STATE_MANAGEMENT_MANUAL | ←3 | ✅ Placement A: end of §1 (line 98, before §2 at line 101). ✅ Placement B: under Cross-References (line 1530). | Append "Division of Labor" subsection to §1; add AUTH_MANUAL cross-ref line. Bump header + Version History. | 1.2 | NO |
| 4 | FRONTEND_BUILD_PHASE_PLAYBOOK | ←4 | ✅ §9 UI Phase Completion Checklist (line 417). Pack says "phase-close verification section" — live doc calls it "UI Phase Completion Checklist." Same thing; anchored at §9. | Append Gate Q/D checklist items (3 lines) to §9 checklist. Bump header + Version History. | 1.2.2 | NO |
| 5 | AUTH_MANUAL | ←4 | ✅ After "Server-Side Protection (RBAC)" (line 787, before "Role-Based Access Control" at line 880). | Insert new § "Server-Resolved Identity for UI (The Navbar Law)" between existing sections. Bump header + Version History. | 1.4 | NO |

## New docs entering the Hub
| File | Standard header added? | MANIFEST row | Notes |
|------|------------------------|--------------|-------|
| QA_PLAYBOOK.md → 03_BUILD_METHODOLOGY/ | Already has standard header (v0.1, 2026-08-04, DRAFT). Tier line aligned: `Engineering Process / Quality Doctrine` → `3 — Build Methodology`. | Yes — new row in 03_BUILD_METHODOLOGY table | Pairs with: BUG_FIX_PLAYBOOK, TESTING_PLAYBOOK, SOFTWARE_FACTORY_PLAYBOOK, ENGINEER_PLAYBOOK, FFM_PLAYBOOK, RECON_QUESTIONNAIRE |
| BUG_FIX_PLAYBOOK.md → 03_BUILD_METHODOLOGY/ | Already has standard header (v0.1, 2026-08-04, DRAFT). Tier line aligned: `Engineering Process / Quality Doctrine` → `3 — Build Methodology`. | Yes — new row in 03_BUILD_METHODOLOGY table | Pairs with: QA_PLAYBOOK, TESTING_PLAYBOOK, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FFM_PLAYBOOK |

## Consistency ripples (docs NOT edited, but checked)
| Doc | Why checked | Verdict (CONSISTENT / NEEDS-TOUCH → move to touch list) |
|-----|-------------|--------------------------------------------------------|
| TESTING_PLAYBOOK | Referenced by both new playbooks (QA_PLAYBOOK pairs-with, BUG_FIX_PLAYBOOK pairs-with) | CONSISTENT — exists in 03_BUILD_METHODOLOGY/, no contradiction with new content |
| ENGINEER_PLAYBOOK | Referenced by both new playbooks (pairs-with) | CONSISTENT — exists in 02_PIPELINE_AGENTS/, no contradiction |
| RECON_QUESTIONNAIRE | Referenced by both new playbooks (pairs-with) | CONSISTENT — exists in 02_PIPELINE_AGENTS/, no contradiction |
| FFM_PLAYBOOK | Referenced by both new playbooks (pairs-with) | CONSISTENT — exists in 03_BUILD_METHODOLOGY/, no contradiction |
| SOFTWARE_FACTORY_PLAYBOOK | Referenced by QA_PLAYBOOK (pairs-with) | CONSISTENT — exists in 01_CONSTITUTION/, no contradiction |
| APP_ARCHITECTURE_MANUAL | ← AUTH_MANUAL (←4 blast radius) | CONSISTENT — references AUTH_MANUAL; new § adds server-resolved identity pattern, does not contradict APP_ARCHITECTURE's data-flow patterns |
| DATABASE_MANUAL | ← AUTH_MANUAL (←4 blast radius) | CONSISTENT — references AUTH_MANUAL; new § is UI-layer, does not touch database doctrine |
| STRIPE_SUBSCRIPTIONS_PLAYBOOK | ← AUTH_MANUAL (←4 blast radius) | CONSISTENT — references AUTH_MANUAL; new § is orthogonal to payments |
| ECOMMERCE_AND_PAYMENTS_MANUAL | ← STATE_MANAGEMENT_MANUAL (←3 blast radius) | CONSISTENT — references STATE_MANAGEMENT_MANUAL; new Division of Labor subsection reinforces existing three-layer model, does not contradict |
| FRONTEND_FIRST_PLAYBOOK | ← FRONTEND_BUILD_PHASE_PLAYBOOK (←4 blast radius) | CONSISTENT — references FRONTEND_BUILD_PHASE_PLAYBOOK; new Gate Q/D checklist items are additive, no contradiction |
| UI_UX_BUILDING_MANUAL | ← FRONTEND_BUILD_PHASE_PLAYBOOK (←4 blast radius) | CONSISTENT — references FRONTEND_BUILD_PHASE_PLAYBOOK; new items are quality-gate pointers, no contradiction |

## Structural flags
- **Renames/moves:** none — all live docs keep canonical names; new docs land in 03_BUILD_METHODOLOGY/
- **Heaviest doc touched:** AUTH_MANUAL and FRONTEND_BUILD_PHASE_PLAYBOOK, both ←4 — minimal-diff rule (D14) applies: surgical additions only, exactly as written in the pack
- **Placement mismatches found:** one naming difference — pack says "phase-close verification section" for Entry 4; live doc calls it "UI Phase Completion Checklist" (§9). Same anchor, different name. Flagged, not a blocker.
- **Hub law translations (D15):** pack's "filename-carries-version" instruction (Entry 4) translated to Hub law: canonical filename stays, version bump in header + Version History row + archive copy to _ARCHIVE/. No filename change.
- **Cross-ref closure:** all cross-references in the new content resolve within this run's touch set (AUTH_MANUAL ↔ STATE_MANAGEMENT_MANUAL cross-ref each other; FRONTEND_BUILD_PHASE_PLAYBOOK → QA_PLAYBOOK + BUG_FIX_PLAYBOOK; QA_PLAYBOOK ↔ BUG_FIX_PLAYBOOK). No dangling references.
- **Pack landing instruction #5 (trickle-up queue):** process note for the Operator — these entries join the Gate-M split + commit-checkpoint gate for the kit/central-stack merge session. Not a Hub doc change; noted for the PR description.

## Write-load tally (feeds Phase 3 estimates)
3 docs edited + 3 archive copies + 2 new docs (Tier-line alignment only) + 1 MANIFEST (5 rows: 3 version bumps + 2 new) + 1 CHANGELOG (5 entries) = **~10 writes**

## Evidence labels
- All ← counts: EVIDENCE (read from MANIFEST.md dependency map)
- All placements: EVIDENCE (verified against live doc line numbers)
- All version bumps: INFERENCE (reasoned from current header versions + semver convention: minor for new sections, patch for checklist additions)
- New doc tier alignment: EVIDENCE (03_BUILD_METHODOLOGY/ verified on disk; Tier line format confirmed from FRONTEND_BUILD_PHASE_PLAYBOOK.md and TESTING_PLAYBOOK.md headers)
- Cross-ref consistency: INFERENCE (reasoned from reading all referenced docs' headers and section structures)

## Approval
- [ ] Operator APPROVED at Stop Gate 2 on: ________
