# Phase 1 — Intake & Recon Report

> **Run:** 2026-08-05 — "The Navbar Saga" doctrine promotion
> **Skill:** factory-docs-update v0.2-DRAFT
> **Timestamp:** 2026-08-05 15:13 UTC

---

## Environment Discovery

- **Location:** Doctrine Hub clone at `/home/moose/nextjs/app-factory-docs-v1`
- **Remote:** `https://github.com/ahmedmusawir/app-factory-docs-v1.git`
- **Branch:** `main` — clean, no modified tracked files
- **GitHub MCP:** Not available in this session (fine — local git is primary)
- **Lessons file:** None found (pack IS the lessons input)
- **Examples folder:** None (first validated run)

---

## Cargo Found

| Item | Status |
|---|---|
| `DOCTRINE_PROMOTION_2026-08-04_NAVBAR_SAGA.md` | Pack — 4 entries, presumptive scope |
| `QA_PLAYBOOK.md` | New doc riding in (v0.1, 2026-08-04) |
| `BUG_FIX_PLAYBOOK.md` | New doc riding in (v0.1, 2026-08-04) |

---

## Scope (per Architect's ruling + amendment)

| Entry | Target | Scope |
|---|---|---|
| Entry 1 | `AUTH_MANUAL.md` — new § after "Server-Side Protection (RBAC)" | ✅ IN |
| Entry 2 | `STATE_MANAGEMENT_MANUAL.md` — append to §1 + cross-ref line | ✅ IN |
| Entry 3 | `ANTI_PATTERNS.md` (stark-frontend-first skill) | 🔀 PARKED — different repo |
| Entry 4 | `FRONTEND_BUILD_PHASE_PLAYBOOK.md` — append to §9 checklist | ✅ IN |

---

## New Docs Entering the Hub (Ruling 2 + Architect Amendment)

| Doc | Current Tier Line | Hub Tier Line (aligned) | Landing Folder |
|---|---|---|---|
| `QA_PLAYBOOK.md` | `Engineering Process / Quality Doctrine` | `3 — Build Methodology` | `03_BUILD_METHODOLOGY/` |
| `BUG_FIX_PLAYBOOK.md` | `Engineering Process / Quality Doctrine` | `3 — Build Methodology` | `03_BUILD_METHODOLOGY/` |

Both found in clone root. Enter in this run: standard header, MANIFEST row, CHANGELOG line each. Tier line aligned to Hub taxonomy; content untouched.

---

## Placement Verification

| Entry | Stated Placement | Live Doc Match |
|---|---|---|
| Entry 1 | After `## Server-Side Protection (RBAC)` | ✅ Found at AUTH_MANUAL.md line 787. Next section is `## Role-Based Access Control` at line 880. New section lands between them. |
| Entry 2-A | Append to `## 1. Philosophy & Strategy` as closing subsection | ✅ Found at STATE_MANAGEMENT_MANUAL.md line 25. Section ends at line 98, before `## 2. Store Architecture` at line 101. |
| Entry 2-B | Add line under `## Cross-References (Factory Doctrine)` | ✅ Found at line 1530. |
| Entry 4 | "final stage's completion checklist / stop condition (the phase-close verification section)" | ✅ Found at `## 9. UI Phase Completion Checklist` (line 417). **Naming note:** pack says "phase-close verification section" — live doc calls it "UI Phase Completion Checklist." Same thing, different name. Anchoring at §9; flagging the naming. |

All placements verified. No mismatches blocking execution.

---

## Blast Radius (preliminary, from MANIFEST)

| Doc | ← Count | Referenced By |
|---|---|---|
| AUTH_MANUAL | ←4 | APP_ARCHITECTURE_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, STRIPE_SUBSCRIPTIONS_PLAYBOOK |
| STATE_MANAGEMENT_MANUAL | ←3 | APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, ECOMMERCE_AND_PAYMENTS_MANUAL |
| FRONTEND_BUILD_PHASE_PLAYBOOK | ←4 | ENGINEER_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, UI_UX_BUILDING_MANUAL |
| QA_PLAYBOOK (new) | 0 | Will be referenced by FRONTEND_BUILD_PHASE_PLAYBOOK (Entry 4) and BUG_FIX_PLAYBOOK |
| BUG_FIX_PLAYBOOK (new) | 0 | Will be referenced by FRONTEND_BUILD_PHASE_PLAYBOOK (Entry 4) and QA_PLAYBOOK |

---

## Architect Amendments Incorporated

1. **Route:** local git — standing primary (confirmed; formal decision at Phase 3).
2. **New playbooks landing folder:** `03_BUILD_METHODOLOGY/` — verified exists, contains 5 docs. Tier line aligned to `3 — Build Methodology` per Hub taxonomy.

---

## ANTI_PATTERNS — Most Relevant

- **AP-6** (guessed archive versions): every archive version read from live header at execution time.
- **AP-9** (version suffixes in refs): Hub law — canonical filenames only; pack's "filename-carries-version" instruction translates to header bump + _ARCHIVE/ copy.

---

## Next: Phase 2 — Ripple Analysis

If scope is approved, Phase 2 will produce the full ripple map: exact version bumps per doc, the complete touch list (3 edits + 2 new docs + MANIFEST + CHANGELOG + 3 archive copies), and cross-reference consistency checks.
