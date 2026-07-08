# 📋 WAVE 3 PLAN — Method Tier Sync (5 docs) + required before/afters

> Status: PENDING_APPROVAL · Session 2026-07-07 · Mirrors CLI presentation.

## Required reading completed

FINDINGS F-002/F-010/F-011/F-012/F-024/F-029/F-031/F-032/F-033/F-034/F-035/F-036/F-037 + D-019 ✓ · REVIEW_010–014 ✓ · DESIGNER §1+§10 ✓ · RECON v0.5 ✓ · Target docs read/scanned (FFM 104KB targeted-read; Frontend-First + Build-Phase full; Testing head/ToC/tail; Skills full-outline + affected regions) ✓

## Pre-plan scan facts

| Doc | ctrl/CR | mojibake | stitch | `_v[0-9]` |
|---|---|---|---|---|
| FFM | 0/0 | 0 | 4 (lines 79/95/103/406) | 9 — ALL project folder names (`cyber_pharma_v1_*`) = identifiers, NOT doc refs → exempt |
| FRONTEND_FIRST | 0/0 | **8× `"”` (broken em-dash — invisible to the `â` grep)** | 0 | 4 live doc refs to strip |
| BUILD_PHASE | 0/0 | 0 visible; **F-034 = DELETED chars** (inventory below) | **1 (line 214 — unlisted in REVIEW_012)** | 0 |
| TESTING | 0/0 | 0 | 0 | 0 |
| SKILLS | 0/0 | 0 | 6 (§2 line 81 + §16 block) | 0 |

---

## DOC 1 — FFM_PLAYBOOK → v1.2

1. **Header** → standard block (Tier 3 — Build Methodology; pairs gain RECON_QUESTIONNAIRE + DESIGNER_PLAYBOOK); audience/purpose/owner lines kept; version prose → new Version History table at doc end (v1.2/v1.1/v1.0).
2. **§2 four-role diagram — BEFORE→AFTER (required approval):**

BEFORE (excerpt): Role 1 column produces `Brand tokens / Style tile / Wireframes / Stitch output`; no recon anywhere.

AFTER:
```
                    0. RECON (STAGE 0 — before all roles)
                    Engineer (Claudy) answers RECON_QUESTIONNAIRE read-only
                    → Recon Report → the Architect authors from verified facts
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   1. DESIGNER       2. EXTRACTOR      3. ARCHITECT     4. ENGINEER  │
│   ─────────         ─────────         ─────────        ─────────    │
│   Designer +        Claudy +          Architect        Engineer     │
│   Operator          Extractor +       (Claude in       (Claudy in   │
│                     Operator          chat)            terminal)    │
│                                                                     │
│   PRODUCES:         PRODUCES:         PRODUCES:        PRODUCES:    │
│   Token file        Brain Drain       The FFM          Working code │
│   (PRIMARY)         extracts          folder           per the FFM  │
│   Style tile        (11 evidence-                                   │
│   HTML+PNG          labeled docs)                                   │
│   Screen HTML+PNG                                                   │
│   Comp. manifest                                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```
(Feeds-row below the box unchanged.)

3. **Role 1 rewrite — AFTER text (required approval):**
> **Who:** the Designer Agent per `DESIGNER_PLAYBOOK.md` (token-driven HTML + Playwright method). **With:** Operator.
> **Produces:** the Designer v2.0 package — the visual ground truth.
> **Outputs:** Token file (`globals.css`/`.scss`, all modes — THE PRIMARY DELIVERABLE) · Style tile (HTML + PNG) · Per-screen HTML + PNG via the Canonical Page Method (lock one canonical screen, clone-and-adapt) · Component manifest · Logo files · Reference screenshots (if applicable).
> **Quality bar:** tokens concrete + complete (all modes, light + dark verified on real screens); canonical screen locked at an operator gate before clone-out; screen set covers every screen in FFM scope; HTML consumes tokens only (no hardcoded colors).
> **Failure modes:** unchanged (generic-zinc default; post-build design iteration; style-tile drift) — plus: screens hand-painted instead of token-driven = un-swappable debt.
4. **§4:** add pointer line ("constitution-level router now lives in APP_FACTORY_BLUEPRINT 'Which Pipeline Am I In?'; this section remains the detailed source"); line 406 de-Stitch ("Wireframes / Designer screen HTML → goes in `_design/`"); Variant B `_design/` contents + differs-table row + UI_SPEC-sourcing line updated to Designer v2.0 deliverables.
5. **§7:** prepend `0. RECON — confirm a current Recon Report exists (RECON_QUESTIONNAIRE / stark-recon); no authoring without it` (existing steps keep their numbers, D-019); inputs checklist gains `[ ] Current Recon Report`; add **F-029 ownership note** after "Why APP_BRIEF First": conversion FFM = Architect pre-authors DATA_CONTRACT from Brain Drain; greenfield = the Engineer is author-of-record from APP_BRIEF + UI_SPEC (the FFM ships the contract shell/evidence pointers) — consistent with Blueprint/Handoff/Engineer.
6. **§10.1:** greenfield required list + example tree → Designer v2.0 package (token file, style tile HTML+PNG, screen HTML+PNG, component manifest, logos); conversion side unchanged.
7. **§18 checklist:** Pre-Authoring gains recon item; `_design/` items aligned if wireframe-era.
8. Version History table + footer normalization.

## DOC 2 — FRONTEND_FIRST → v1.1.3 (micro)

1. Standard header (born-from kept). 2. §0: `STARTER_KIT_HANDBOOK_v1.0.md`/`COMPONENT_REGISTRY_v1.0.md` → canonical (F-032). 3. §14: `FRONTEND_BUILD_PHASE_PLAYBOOK_v1.2.md`, `SOFTWARE_FACTORY_PLAYBOOK_v1.1.md` → canonical. 4. **8× `"”` → `—`** (Gate headers ×3 + lines 131/181/191/197/203) (F-012). 5. One-line recon pointer in §0. 6. History row v1.1.3; footer suite label de-versioned.

## DOC 3 — BUILD_PHASE → v1.2.1 (micro + repairs) — table rebuilds (required approval)

1. Standard header v1.2.1 (kills the F-033 v1.1 header lie; history row records it).
2. **F-034 repair inventory:** restore "- " bullets on ~20 de-bulleted lists (§1, §2, Stages 1–6 activity/rule/output lists, §9 intro, §11); arrows: `member → admin → superadmin`, `Page → Row → Box`; slashes: `status/severity`, `Hide/show`, `Success/error` ×2, `Audit/history`, `WebSockets / real-time sync`, `data/security`; quotes: `"No data"`, `"Are you sure"`; Golden Rule lines → `> ` blockquote; **rebuild 3 de-piped tables**:

§7 Allowed (AFTER):
```
| Feature | Notes |
|---|---|
| Create items | In-memory only, lost on refresh |
| Edit items | In-memory only |
| Delete items | In-memory only |
| Change status/severity | In-memory only |
| Filters | Client-side filtering of mock data |
| Search | Client-side search of mock data |
| Sorting | Client-side sorting |
| Pagination | Client-side (service returns paginated results) |
| Role-based UI gating | Hide/show actions based on role |
| Form validation | Client-side validation |
| Success/error toasts | Feedback for user actions |
```
§7 Forbidden (AFTER):
```
| Feature | Why |
|---|---|
| localStorage persistence | Adds complexity, no real value for demo |
| Real concurrency simulation | Backend concern |
| Audit/history systems | Backend concern |
| File uploads to storage | Backend concern (show UI only) |
| Background jobs | Backend concern |
| WebSockets / real-time sync | Backend concern |
| Multi-user permission enforcement | RLS concern |
| DB-level pagination logic | Backend concern |
| Data integrity enforcement | Backend concern |
| Fake auth or fake permissions | Use real auth with mock data |
```
§10 (AFTER):
```
| Component | Purpose |
|---|---|
| Pagination component | Reusable across all tables |
| Breadcrumbs | Auto-generated from route (if decided yes) |
| Loading spinner | Global and inline variants |
| Empty state component | Reusable "No data" message |
| Error boundary | Catches React errors gracefully |
| Toast notifications | Success/error feedback |
| Mobile responsive nav | Sidebar collapses on mobile |
| Dark mode toggle | Respects system preference |
| Confirmation dialog | "Are you sure" for destructive actions |
```
3. **Phase-0 collision:** §1.5 line "Doctrine read in Phase 0 decays by Stage 5" → "Doctrine read at build Stage 0 (Discovery) decays by Stage 5" + naming note: build **Stage 0 = Discovery** (FFM's "Sub-Phase 0") ≠ lifecycle **Phase 0 = Recon** (APP_FACTORY_BLUEPRINT); terms per SFP §2 Phase Vocabulary (F-010-coordinated).
4. "Cascade" → "the build agent" (lines 251 §5 + 456 §10).
5. Line 214 de-Stitch: "Reference Stitch designs (or equivalent) for layout" → "Reference the Designer's screen HTML/PNG (or equivalent) for layout" (F-002 — hit not listed in REVIEW_012; found by scan).
6. §9 Documentation block gains `TESTING_PLAYBOOK.md` pointer (F-035 inbound leg).
7. History row v1.2.1; footer de-versioned.

## DOC 4 — TESTING → v2.1

1. Standard header (v2.1 · Tier 3; provenance lines kept). 2. Tail "END OF TESTING PLAYBOOK v2.0 DRAFT" → "END OF TESTING PLAYBOOK" + **Version History table** (2.1 / 2.0 / 1.0) (F-036). 3. New **"Where This Doc Sits"** section after the header: outbound → STARTER_KIT_HANDBOOK (kit runner/config ground truth) + RECON_QUESTIONNAIRE (Q1.7 runner check); inbound note → SFP Phase 8, FFM verification/, FRONTEND_BUILD_PHASE §9 reference this doc (F-035). 4. New **§3.8 "Run-Verification Rituals (Run 001)"** in Part 3 — absorbs L17 grep-at-close, L25 rm `.next` between deletion batches, L26 fresh test baseline, credited "promoted from RECON_QUESTIONNAIRE §12"; canonical home = here. 5. Nothing else touched (75KB model doc).

## DOC 5 — SKILLS → v1.1

1. Standard header (Tier 3; authoritative blockquote kept). 2. §2 line 81 + §16 block: "Stitch Prompting Discipline" → **"Token-Driven HTML Screen Discipline (for Designer Agents)"** — token-inheritance rules (screens consume `globals.css` vars, no hardcoded colors), Canonical Page Method (lock canonical screen → clone-and-adapt), Playwright render loop (light + dark PNG), quality gates before operator review; activation when the Designer is asked to produce screens (F-002/F-037). 3. §7 gains **"Where Skills Live + The Launch-CWD Rule"**: `_SKILLS/` = operator's authoring library; `.claude/skills/` = repo-side install Claude Code auto-discovers (what RECON Q6.1 checks); skills resolve relative to the LAUNCH directory (RECON Q6.5) — document launch CWD in RECOVERY.md; activation contract presumes correct CWD (F-037). 4. §14 gains **Exemplar 3: stark-recon** (Single Stark Skill, June 2026) case study + June ecosystem note (stark-recon, starter-kit-cleaner, repo-security) — described, not imported. 5. New **Cross-References** section before §17: FFM_PLAYBOOK §11 (FFM skills/ pairing), RECON_QUESTIONNAIRE §6, DESIGNER_PLAYBOOK (F-035). 6. §17 v1.1 row; closing "End of Playbook v1.0" de-versioned.

## Gates (per doc + wave)

stitch live 0 (history exempt) · `_v[0-9]` doc-refs 0 (FFM folder-name identifiers exempt — they are project artifacts, not references) · mojibake incl. `"”` 0 · C1 0 · headers + history rows 5/5 · FFM Step 0 + diagram ✓ · Build-Phase tables render ✓ · Testing DRAFT gone ✓ · Skills Stitch-free ✓ · per-doc CHANGES/DIDN'T TOUCH/CONCERNS.

## Sequencing & method

Doc order: FFM → Frontend-First → Build-Phase → Testing → Skills; one suggested commit per doc, stop for operator each time. All edits via targeted Edit calls (no full-file rewrites anticipated; if one becomes necessary, Wave-2B-style byte-faithful carry proof applies).

## Files I will NOT touch

RECON_QUESTIONNAIRE (its §12→Testing pointer-back is a later touch — CONCERNS), STARTER_KIT_HANDBOOK, all Tier 1/2/4/5 docs, _AUDIT/, _OTHERS/.
