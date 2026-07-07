# FACTORY DOC STACK AUDIT — FINDINGS LOG

> **Purpose:** Running, numbered list of every issue caught during the full doc stack review.
> Nothing evaporates. Resolved items stay in the log as history.
> **Started:** 2026-07-02 | **Maintainer:** Architect Jarvis | **Log revision:** 33

---

## Status Key
- 🔴 OPEN — needs action
- 🟠 DECISION — waiting on operator (Tony) call
- 🟡 FILED — deferred to central-delivery-system design phase
- 🟢 RESOLVED — fixed, kept for history

---

## Findings

| ID | Date | Status | Severity | Doc(s) Involved | Finding | Resolution |
|----|------|--------|----------|------------------|---------|------------|
| F-001 | 07-02 | 🟢 RESOLVED | HIGH | DESIGNER_PLAYBOOK (absent) | Designer Agent referenced but no Designer Playbook in stack. | Tony added it + 4 supporting docs. |
| F-002 | 07-02 | 🔴 OPEN | HIGH | BLUEPRINT ↔ ARCHITECT_PLAYBOOK ↔ ARCHITECT_QUESTIONNAIRE | Stitch (retired 9 Jun) in four places in Architect Playbook + Questionnaire Q4; §1 diagram also misstates Designer deliverable. | v2.2 sweep + diagram redraw. |
| F-003 | 07-02 | 🔴 OPEN | HIGH | APP_FACTORY_BLUEPRINT | Recon Mode missing from Blueprint. | Blueprint v2.1 adds Phase 0. |
| F-004 | 07-02 | 🟡 FILED | MEDIUM | Whole stack | No master index of the 27 docs. | MANIFEST + dependency map. |
| F-005 | 07-02 | 🟢 RESOLVED | HIGH | THEMING_MANUAL v1_0+v1_1 | Two versions coexisted. | Tony deleted v1_0. |
| F-006 | 07-02 | 🟢 RESOLVED | HIGH | UI-UX-BUILDING-MANUAL | **SOLVED via repo reconciliation:** stack file named `v1_4` contains v1.2 content (rename, no content change — hence byte-identical size). Real current version is repo v1.3 (June 28). No v1.4 exists. | Refresh stack from repo v1.3; delete misnamed v1_4. See RECONCILIATION_REPORT. **Ghost formally buried at REVIEW_023 — real v1.3 audited: MODEL DOC.** |
| F-007 | 07-02 | 🟡 FILED | LOW | APP_FACTORY_BLUEPRINT | Factory-level doc versioning undefined. | MANIFEST design. |
| F-008 | 07-02 | 🔴 OPEN | LOW | AI_APP_FACTORY_BLUEPRINT_v2_0 | Rename to APP_FACTORY_BLUEPRINT (drop "AI_"). | Bundle with Blueprint v2.1. |
| F-009 | 07-02 | 🔴 OPEN | HIGH | SFP ↔ DESIGNER_PLAYBOOK | SFP Phase 2 = stale competing design process (Stitch/Figma). | SFP v1.2 Phase 2 rewrite. |
| F-010 | 07-02 | 🔴 OPEN | HIGH | BLUEPRINT ↔ SFP ↔ STARTER_KIT_HANDBOOK | Three phase vocabularies, no bridge. | One canonical phase map. |
| F-011 | 07-02 | 🔴 OPEN | MEDIUM | Stack-wide | Versioned filenames in cross-references guarantee drift. Model fix: STARTER_KIT_HANDBOOK §13. **Reconciliation adds proof:** the "v1_4" mislabel was only possible because version lived in the filename.** | Canonical names only; MANIFEST owns versions. |
| F-012 | 07-02 | 🔴 OPEN | MEDIUM (escalated) | SFP + FRONTEND_FIRST + APP_ARCHITECTURE (3 confirmed) | UTF-8 mojibake despite claimed fixes — THIRD instance at REVIEW_015 (16 chars in a Gate-10 doc). **SYSTEMIC DIAGNOSIS: the editing/export pipeline itself is the corruption source — fixes get re-broken on save. Identify the tool before the rewrite phase.** | Tool diagnosis first, then one sweep; mojibake + char-loss lint = automation priority #1. |
| F-013a | 07-02 | 🟠 DECISION | MEDIUM | STARTER_KIT_HANDBOOK | Role colors: `--role-*` tokens vs numbered exception. Cleaner skill shows tokens "pre-baked on defaults" — likely already decided. | Tony confirms → close. |
| F-013b | 07-02 | 🟢 RESOLVED | MEDIUM | STARTER_KIT_HANDBOOK | Theme toggle canonical name. | **`ThemeToggle` — decided + shipped at Kit Hardening Gate 10 (06-28).** |
| F-014 | 07-02 | 🔴 OPEN | LOW | STARTER_KIT_HANDBOOK §13 | STARTER_KIT_FEEDBACK.md absent from stack. Gate 10 "LESSONS_BIN harvested" likely related. | Tony to confirm relationship/status. |
| F-015 | 07-02 | 🟢 RESOLVED | LOW | FFM_PLAYBOOK | Verify "doctrine says Vitest" fix landed (L8). | **RESOLVED at REVIEW_010:** zero test-runner claims in FFM v1.1 — lie removed rather than corrected (runner is recon's job to verify, not doctrine's to assert). |
| F-016 | 07-02 | 🔴 OPEN | MEDIUM | ARCHITECT_PLAYBOOK_v2.md | Filename v2 vs footer v2.1. | Fix at v2.2; F-011 rule. |
| F-017 | 07-02 | 🔴 OPEN | HIGH (escalated) | ARCHITECT_PLAYBOOK ↔ ARCHITECT_QUESTIONNAIRE | **Characterized at REVIEW_005:** not copy drift — two structurally different instruments. Standalone: 12-Q/3-phase w/ Hard Gate + Reality Rule + Planning State. Playbook §3: 15-Q/6-phase w/ none of those but unique content (constraints/deadline/integrations/risks/security). APP_BRIEF templates likewise diverged. | Questionnaire v2.2 becomes single source (absorbs playbook-only questions); playbook §3/§5 → pointers. Coordinate w/ REVIEW_004 v2.2 changes. **Fix template validated end-to-end at REVIEW_011/012 (Frontend siblings' Lesson-9 relocation confirmed on both ends).** |
| F-018 | 07-02 | 🟡 FILED | LOW | Stack-wide | Version block placement inconsistent. | Standard parseable top header. |
| F-019 | 07-03 | 🟢 RESOLVED | HIGH | Stack vs repo | **Kit Perfection Campaign (06-25→06-29) bumped 6 docs repo-side; stack froze pre-campaign.** Stale copies: UI-UX, FRONTEND_FIRST, AUTH, APP_ARCHITECTURE, COMPONENT_REGISTRY (+ THEME_LIBRARY caught in sweep, + HANDBOOK caught at F-022). | **RESOLVED 07-06:** clean-stack swap complete — 27/27 doctrine-named docs verified in project, all canonical versions (handbook = June-28 edition). Starter-kit sync disconnected. |
| F-020 | 07-03 | 🟢 RESOLVED | LOW | STARTER_KIT_HANDBOOK | Repo copy found only under cleaner-skill references (a snapshot); canonical location + Gate 10 revision were unverified. | **RESOLVED 07-06:** canonical = `agent_docs/STARTER_KIT/STARTER_KIT_HANDBOOK_v1.1.md` (June-28 Kit-Perfection edition). Now seeded in stack. Spawned F-022. |
| F-021 | 07-03 | 🟢 RESOLVED | MEDIUM | Audit scope | Skills scope split. | **✅ TONY CONFIRMED (07-07):** SKILLS_PLAYBOOK = doctrine (Hub, audited at 014); skill instances stay kit-repo-side, audited later against the playbook's activation contract. |
| F-022 | 07-06 | 🔴 OPEN | HIGH | STARTER_KIT_HANDBOOK | **Version-number collision:** TWO different handbooks both stamped v1.1 — June-8 "v3 reconciliation" edition (🔧 L-tags) vs June-28 "Kit-Perfection harvest" edition (Gate 10, commit `4dd8151` bumped from v1.0). Divergent forks of a common v1.0 ancestor. June-28 = canonical, now seeded. | REVIEW_003 flagged for REDO against canonical. Review-phase task: merge any June-8-only reconciliation content into a proper v1.2. June-8 edition → _ARCHIVE at repo creation. |
| F-023 | 07-06 | 🔴 OPEN | LOW | RECON_QUESTIONNAIRE | Internal numbering drift from two rapid renumberings: no Section 7 (jumps 6→8); §13 questions still numbered Q10.x; Recon Report Format labels out of sync ("Section 10 — Surprises" vs actual §13). | v0.5 patch: renumber + sync report format. |
| F-024 | 07-06 | 🔴 OPEN | HIGH (widened) | RECON_QUESTIONNAIRE ↔ ARCHITECT_PLAYBOOK ↔ FFM_PLAYBOOK | **Widened at REVIEW_010:** FFM v1.1 (June 18) contains ZERO recon references; §7 authoring sequence has no recon step — while the Recon doc claims to be "Stage 0 of the four-role pattern" and the Architect Playbook makes recon-before-FFM law. Three docs, one gate, one-directional knowledge. | FFM v1.2 adds Step 0 — Recon; questionnaire v0.5 + playbook v2.2 add mutual pointers. |
| F-025 | 07-06 | 🟢 ADJUDICATED | MEDIUM | DESIGNER_PLAYBOOK ↔ THEME_LIBRARY ↔ GDSH | Token-file naming split: Designer Playbook §13 listed `TOKEN_FILE.md` as "the live token values." | **SETTLED at REVIEW_022: GDSH §8 rules `globals.css` = the live token file. Designer Playbook §13 = stale outlier. TOKEN_FILE role DEFINED at REVIEW_026: reference snapshot / drop-in template for Cyber Pharma Metro Warm — NOT the live file; v1.2 adds the role sentence.** |
| F-026 | 07-06 | 🔴 OPEN | HIGH | ENGINEER_PLAYBOOK §2 ↔ DESIGNER_PLAYBOOK §10 | Handoff mismatch: Engineer expects APP_BRIEF + UI_SPEC + screenshots; Designer ships token file (PRIMARY) + style tile + HTML/PNG + UI_SPEC + component manifest. Receiving side omits the load-bearing items. | Engineer v1.2 §2 rewritten to match Designer package. **Tiebreak result (Review 009): Handoff Playbook describes a THIRD package (no Designer at all) — root cause is F-030 two-pipeline split; resolution folds into F-030.** |
| F-027 | 07-06 | 🔴 OPEN | HIGH | ENGINEER_PLAYBOOK | Doc frozen at Feb 2026 — predates recon (Claudy's recon-executor role absent from his own manual), Phase-0 handbook read, Kit Audit, FFM execution mode, all Run 001/Cyber Pharma lessons. Most stale agent doc. | v1.2 structural update (see REVIEW_008 change list). |
| F-028 | 07-06 | 🔴 OPEN | MEDIUM | ENGINEER_PLAYBOOK | Center-of-gravity mismatch: Python/pytest/CLI-pipeline spine while factory's dominant lane is the Next.js starter kit (one sentence). | v1.2 restructure: common doctrine + Kit Track / Pipeline Track. |
| F-029 | 07-06 | 🔴 OPEN | HIGH | HANDOFF_PACKAGE_PLAYBOOK ↔ ENGINEER_PLAYBOOK ↔ BLUEPRINT | DATA_CONTRACT ownership contradiction: Handoff Playbook authors it PRE-handoff (from Brain Drain evidence); Engineer Playbook + Blueprint name it the ENGINEER's deliverable. Same artifact, two authors, two moments. | Resolve per-pipeline (conversion = pre-authored; greenfield = Engineer-authored); state in all three docs. |
| F-030 | 07-06 | 🔴 OPEN | HIGH — deepest structural catch | Whole pipeline layer | **Two unacknowledged pipelines.** Conversion (Handoff Playbook): Brain Drain → 4-file package → Claudy, no Designer. Greenfield (Blueprint + agent playbooks): Architect → Designer → Engineer, token file primary. Shared artifact names, different authors/contents, no routing doc. Explains F-026 + part of F-010. **Prior art found at REVIEW_010: FFM §4 already defines Conversion vs Greenfield with a 3-question router — promote upward.** | "Which Pipeline Am I In?" preamble in Handoff Playbook v1.1 + mirror in Blueprint v2.1, sourced from FFM §4. |
| F-031 | 07-06 | 🔴 OPEN | HIGH | FFM_PLAYBOOK ↔ DESIGNER_PLAYBOOK | FFM Role 1 + `_design/` contract are pre-Designer-v2.0: "wireframes, Stitch output, style tile" (4 Stitch refs, 9 days post-retirement); no token file, token-driven HTML, Playwright, or Canonical Page Method. Downstream never updated when Designer v2.0 shipped. | FFM v1.2: rewrite Role 1 + `_design/` guides to Designer v2.0 deliverables; de-Stitch. |
| F-032 | 07-06 | 🔴 OPEN | MEDIUM | FRONTEND_FIRST_PLAYBOOK ↔ STARTER_KIT_HANDBOOK ↔ COMPONENT_REGISTRY | **Zero-hour drift record:** §0 references handbook + registry at v1.0 — the SAME Gate 10 that produced this doc's v1.1.2 bumped both to v1.1 the same day. One campaign, three docs, two stale pointers. | v1.1.3 micro-patch: canonical names, no version suffixes (also §14 refs). F-011 cure applied. **Extended at REVIEW_015, 019, 023, and 024 (THEMING v1.1: stale set + the SAME phantom `HANDOFF_PACKAGE_PLAYBOOK v1.1` — second independent citation of a nonexistent version → lost fork or copy-propagation; Tony question queued). Five docs in the class; canonical-name rule evidence conclusive.** |
| F-033 | 07-06 | 🔴 OPEN | MEDIUM | FRONTEND_BUILD_PHASE_PLAYBOOK + THEMING_MANUAL | **Metadata self-disagreement:** Build-Phase — header claims v1.1 while history/content/filename = v1.2 (header lags history). **Extended at REVIEW_024: THEMING — header claims v1.1, body carries 'added v1.1' note, but Version History records only v1.0 (history lags header — inverse symptom).** | Fix both; reinforces F-018 standard header + logged-bump discipline. |
| F-034 | 07-06 | 🔴 OPEN | MEDIUM | FRONTEND_BUILD_PHASE_PLAYBOOK | **Character-stripping corruption (new type):** characters DELETED in encoding round-trip — arrows/slashes gone ("member  admin  superadmin", "Successerror", "datasecurity"), §10 table lost its pipes (broken markdown). Silent content destruction; nastier than F-012 mojibake. | v1.2.1 character-repair pass + rebuild §10 table; lint scope expands to character-loss detection. |
| F-035 | 07-06 | 🔴 OPEN | HIGH | TESTING_PLAYBOOK ↔ whole METHOD tier | **The testing bible is an island:** zero outbound factory refs AND zero inbound (SFP Phase 8, FFM verification/, Build Phase §9 — none point here). 75KB of doctrine undiscoverable by agents executing the factory's testing phases. | v2.1 + coordinated pointers: SFP Phase 8 → here; FFM verification → here; Build Phase §9 → here; here → STARTER_KIT_HANDBOOK. **Roster: SKILLS_PLAYBOOK, STATE_MANAGEMENT, API_AND_SERVICES, DATABASE, STRIPE_SUBSCRIPTIONS (outbound-zero, Reviews 014-021). ECOMMERCE semi-connected (one ref).** |
| F-036 | 07-06 | 🔴 OPEN | LOW | TESTING_PLAYBOOK | Tail self-labels "v2.0 DRAFT" while header says Version 2.0 (no status); operating as doctrine, label stale. No version-history table. | v2.1: resolve status, add history table (D-009 — no ambient status ambiguity). |
| F-037 | 07-06 | 🔴 OPEN | MEDIUM | APP_FACTORY_SKILLS_PLAYBOOK | Pre-ecosystem time capsule (v1.0, May 5): June `_SKILLS/` ecosystem absent; launch-CWD lesson (Q6.5, skills-domain) missing; recon 0 refs; location ambiguity (`_SKILLS/` here vs `.claude/skills/` in RECON); outbound cross-refs zero. Also features "Stitch Prompting" as a specified skill example (F-002 instance, 5 refs). | v1.1: de-Stitch example → token-driven-HTML Designer skill; add CWD doctrine + June exemplars + outbound refs + header. |
| F-038 | 07-06 | 🔴 OPEN | HIGH | APP_ARCHITECTURE_MANUAL ↔ kit reality | Manual pins Next.js 15 throughout (6+ instances) while the kit runs Next.js 16 — the exact offender RECON §1 was written about (Cyber Pharma 15-vs-16 conflict). Architects consuming it replay the Discovery-gate conflict. | v1.3: de-pin version-irrelevant claims, label version-sensitive facts, add recon Q1.1 pointer, verify proxy/middleware vs Next 16. **Extended at REVIEW_020: ECOMMERCE manual pins Stripe apiVersion '2023-10-16' with a comment saying 'use latest' — self-contradicting stale pin. Pattern = stale stack/API pins, stack-wide.** |
| F-039 | 07-06 | 🔴 OPEN | HIGH | API_AND_SERVICES_MANUAL | **Unamended ROOT of Lesson 2:** blanket "all API calls through services" rule with zero kit-capability carve-out (no Kit Audit, no auth exception). Downstream docs got the antibody (FRONTEND_FIRST §0, RECON §3, handbook §11); the source doc never did — agents can still cite it to justify the authService wrapper. | v1.1: prominent exception box ("kit primitives consumed directly; kit's auth IS the service layer; Kit Audit before authoring any service"). |
| F-040 | 07-06 | 🔴 OPEN | MEDIUM | DATABASE_MANUAL ↔ FRONTEND_FIRST | Schema-first declared universal ("before writing ANY application code") with zero frontend-first/mock acknowledgment — the flagship methodology inverts this order. F-030's cousin at build-order level. | v1.1: "When Schema-First Applies" note + FRONTEND_FIRST §2 pointer. **Extended at REVIEW_020: ECOMMERCE manual is WooCommerce-only (25 refs, 0 Supabase) framed as 'THE E-commerce Module' — undeclared jurisdiction. Pattern = correct doctrine, undeclared scope.** |
| F-041 | 07-06 | 🔴 OPEN (unblocked) | HIGH (security-classed) | DATABASE_MANUAL ↔ kit + AUTH doctrine + RECON Q3.4 | §2 user-creation example WRITES role into `user_metadata` + mirrors to `app_users.role` — the forbidden pattern the factory's own Q3.4 grep hunts. Internally split: §5 RLS correctly uses `user_roles`. **The manual would fail its own factory's security grep.** | ✅ UNBLOCKED (F-042 resolved 07-07): align §2 to the TABLE model per filesystem — kit pattern (`user_roles` + `handle_new_user` + `get_user_role()`) + ⛔ forbidden box for metadata-role READS; reconcile §2 with §5. Wave 4 work item as originally planned. |
| F-042 | 07-06 | 🟢 RESOLVED (doc track) + 🔴 KIT TICKET OPEN | HIGH (security-classed) | AUTH_MANUAL ↔ RECON_QUESTIONNAIRE Q3.4 ↔ DATABASE_MANUAL | **Three-way role-doctrine conflict:** Auth Manual v1.2 (Gate-10, kit-authoritative): "Metadata-driven roles — NOT separate tables" (user_roles: 0 mentions; Mark IV trigger applies metadata role). RECON Q3.4: metadata roles = THE forbidden smell (privilege-escalation vector via updateUser unless locked down). DATABASE_MANUAL: internally split. | **✅ RESOLVED via RECON_WAVE0 (07-07):** Filesystem verdict — kit IS table-based (`user_roles` = source of truth, `get-user-role.ts` canonical, post-creation LOCKED). AUTH_MANUAL's 'metadata-driven, NOT separate tables' line is FALSE vs its own kit → AUTH v1.3 corrected; RECON Q3.4 VINDICATED (nuance added: metadata = creation-time transport only + signup-vector lesson); F-041 UNBLOCKED (table model wins). **⚠️ KIT SECURITY TICKET (separate track, kit repo): registration-time escalation — anon-key signUp with options.data.role='superadmin' honored by Mark IV trigger. Rec fix: role transport → app_metadata (client can't write it; admin createUser can) + trigger reads raw_app_meta_data; plus fix stale test README (claims metadata role 'vestigial' — false) + consolidate duplicate trigger defs (supabase/setup.sql vs docs/setup.sql). Tony to check Supabase 'Enable signups' toggle for live severity.** |
| F-043 | 07-06 | 🔴 OPEN (unblocked — F-013a confirmed) | MEDIUM | GDSH §2 ↔ THEME_LIBRARY v1.1 | Contract/catalog mismatch: Theme Library claims "the contract now includes --role-* tokens"; GDSH (the contract) lists none. Evidence (Gate 10 ThemeToggle, cleaner-skill pre-baked --role-* defaults) suggests GDSH is the stale side. **= F-013a with a blast radius.** | Tony confirms F-013a → GDSH v1.1 §2 adds --role-* set → F-013a + F-043 close together. **Payload identified at REVIEW_025 (Library §2 rules). Third witness at REVIEW_026: TOKEN_FILE v1.1 has NO --role-* values either — the Library carries rules only, no HSL anywhere. F-013a implementation = GDSH §2 contract edit + Library rules + minting actual Metro Warm role values in TOKEN_FILE (AA per mode). Three-file plan ready.** |

---

## Doctrine Worth Promoting (positive findings)

| ID | Source | Doctrine |
|----|--------|----------|
| D-001 | SOFTWARE_FACTORY_PLAYBOOK §1.5 | **Doctrine Pairing Principle** — playbook + worked example, always. |
| D-002 | STARTER_KIT_HANDBOOK v1.1 | **"Handbook is a contract, not an aspiration"** — ground-truth before trust. |
| D-003 | STARTER_KIT_HANDBOOK | **⚑ operator-decision flags** in-doc with defaults. |
| D-004 | STARTER_KIT_HANDBOOK §11 | **"Should I Author This?" verdict table.** |
| D-005 | ARCHITECT_PLAYBOOK §2 (v2.1) | **Recon Mode** — "Recon first, author second." |
| D-006 | ARCHITECT_PLAYBOOK §9 | **Bad/Good/Test anti-pattern triplets.** |
| D-007 | Repo session logs | **Gate ledger as change feed** — session logs + commit ledger are where doc-bump truth lives; MANIFEST design should consume them. |
| D-008 | Repo (Gate 10 backlog) | **DOCTRINE_SYNC_MANIFEST already exists repo-side** + "canonical doctrine repo" already on factory backlog — delivery-system endgame has prior art in the factory itself. Required reading. |
| D-009 | ARCHITECT_QUESTIONNAIRE (template §8) | **Planning State classification** — 🔒 Decision / ⚠️ Assumption / ❓ Open Question table. Epistemics as a format; candidate rule for ALL factory artifacts. Pairs with the ⛔ Hard Gate + 📌 Reality Rule patterns from the same doc. |
| D-010 | RECON_QUESTIONNAIRE (Lessons Backlog) | **Recurrence-based promotion lifecycle** — new conflict → backlog question; recurs across two runs → promoted numbered section. Explicit doctrine lifecycle; the Doctrine Hub PR flow should encode this. Question↔scar traceability (conflict table) is the same pattern at question granularity. |
| D-011 | ENGINEER_PLAYBOOK §15 | **Karpathy Protocol** — agent behavioral constitution: assumption surfacing, confusion management (STOP on ambiguity), push-back duty + anti-sycophancy, simplicity enforcement, Tony's Rule (scope discipline), dead-code hygiene, CHANGES/DIDN'T-TOUCH/CONCERNS output standard. Applies to ALL agents — extract to constitution level. |
| D-012 | ENGINEER_PLAYBOOK §16 | **Session Memory Protocol** — tool-agnostic session files as context bridges; ancestor of the Gate-ledger change-feed (D-007). |
| D-013 | FFM_PLAYBOOK §19 | **Structural-vs-project lesson split** — structural lessons promote to playbook/skill updates; project-specific lessons stay in the retrospective. The routing rule for the Doctrine Hub PR flow. FFM's "Sub-Phase" vocabulary is also the candidate convention for the canonical phase map (F-010). |
| D-014 | FRONTEND_BUILD_PHASE_PLAYBOOK §1.5 | **Pre-Phase Doctrine Refresh** — "doctrine read in Phase 0 decays by Stage 5"; structural re-injection (mandatory re-read + acknowledgment + STOP) beats willpower. Validated in Run 001 (post-5.4 phases held the line). |
| D-015 | TESTING_PLAYBOOK (Parts 3/5) | **Honesty artifacts** — companion trio (CHANGELOG, SECURITY_FINDINGS, CLEANUP_BACKLOG as standard project docs) + skip-and-document pattern (defer honestly, never fake or silently delete). Plus Principle 1.6 "source recon before test writing" (2026-05-11) = the recon DNA fossil, three weeks before recon law. |
| D-016 | STRIPE_SUBSCRIPTIONS_PLAYBOOK §1 | **Money-truth mental model** ("Stripe owns the truth about money; Supabase owns the cache; webhooks keep them in sync — Stripe speaks, Supabase listens") + **RBAC ⊥ Subscriptions orthogonality** ("never implement tiers as roles"; composable gate helpers). Boundary doctrine for F-042 regardless of outcome. |
| D-017 | GLOBAL_DESIGN_SYSTEM_HANDBOOK §7 | **Artifacts as views:** "The style tile is a view of the token file, not a separate artifact to maintain. Lock the tile = lock the tokens." No-drift-by-construction — the design-side twin of D-002. Generalizable beyond design. Also: §3's verify-then-fork version handling = the model for F-038 fixes; §12's one-paragraph-version = summarization discipline. |
| D-018 | UI_UX_BUILDING_MANUAL (Update Discipline appendix) | **In-doc maintenance doctrine:** patches at the TOP for foundational rules, at the END for evolution notes; preserve superseded sections marked, never deleted; bump version; cross-reference Run numbers. The doc teaches its own editors — feeds Doctrine Hub contribution rules directly. Gate-10 honesty verified (its changelog claims proved TRUE — unlike the F-012 class). |

---

## Review Docs Produced

| # | File | Doc Reviewed | Verdict |
|---|------|--------------|---------|
| 001 | REVIEW_001_AI_APP_FACTORY_BLUEPRINT_v2_0.md | APP_FACTORY_BLUEPRINT v2.0 | KEEP — needs v2.1 |
| 002 | REVIEW_002_SOFTWARE_FACTORY_PLAYBOOK_v1_1.md | SOFTWARE_FACTORY_PLAYBOOK v1.1 | KEEP — needs v1.2 |
| 003 | REVIEW_003_STARTER_KIT_HANDBOOK_v1_1.md | STARTER_KIT_HANDBOOK v1.1 (June-8 fork) | ⚠️ REDO REQUIRED (F-022) — reviewed the June-8 fork; canonical is June-28 edition |
| 004 | REVIEW_004_ARCHITECT_PLAYBOOK_v2.md | ARCHITECT_PLAYBOOK v2.1 | KEEP — needs v2.2 |
| 005 | REVIEW_005_ARCHITECT_QUESTIONNAIRE_v2_1.md | ARCHITECT_QUESTIONNAIRE v2.1 | KEEP — needs v2.2 (single-source merge + de-Stitch + header) |
| 006 | REVIEW_006_RECON_QUESTIONNAIRE.md | RECON_QUESTIONNAIRE v0.4 | KEEP — MODEL DOC; v0.5 patch (renumber + cross-links) |
| 007 | REVIEW_007_DESIGNER_PLAYBOOK_v2_0.md | DESIGNER_PLAYBOOK v2.0 | KEEP — cleanest agent playbook; v2.1 micro-patch (§13 refs + header) |
| 008 | REVIEW_008_ENGINEER_PLAYBOOK_v1_1.md | ENGINEER_PLAYBOOK v1.1 (Feb 2026) | KEEP doctrine — v1.2 STRUCTURAL update (handoff fix, recon/FFM roles, two-track restructure) |
| 009 | REVIEW_009_HANDOFF_PACKAGE_PLAYBOOK.md | HANDOFF_PACKAGE_PLAYBOOK v1.0 | KEEP — v1.1 (pipeline-duality preamble, F-029 ownership fix, Designer integration) |
| 010 | REVIEW_010_FFM_PLAYBOOK.md | FFM_PLAYBOOK v1.1 | KEEP — v1.2 (recon Step 0, Role 1 modernization, de-Stitch); §4 promoted upward |
| 011 | REVIEW_011_FRONTEND_FIRST_PLAYBOOK_v1_1_2.md | FRONTEND_FIRST_PLAYBOOK v1.1.2 | KEEP — v1.1.3 micro-patch (canonical refs + mojibake); §14 = F-017 fix template |
| 012 | REVIEW_012_FRONTEND_BUILD_PHASE_PLAYBOOK_v1_2.md | FRONTEND_BUILD_PHASE_PLAYBOOK v1.2 | KEEP — v1.2.1 micro-patch (header fix, character repair, tool-agnostic wording) |
| 013 | REVIEW_013_TESTING_PLAYBOOK.md | TESTING_PLAYBOOK v2.0 | KEEP — MODEL content; v2.1 (status fix, history table, end the isolation) |
| 014 | REVIEW_014_APP_FACTORY_SKILLS_PLAYBOOK.md | APP_FACTORY_SKILLS_PLAYBOOK v1.0 | KEEP — v1.1 (de-Stitch example, CWD doctrine, June exemplars, outbound refs) |
| 015 | REVIEW_015_APP_ARCHITECTURE_MANUAL_v1_2.md | APP_ARCHITECTURE_MANUAL v1.2 | KEEP — v1.3 (Next-version de-pinning, mojibake sweep, canonical refs) |
| 016 | REVIEW_016_STATE_MANAGEMENT_MANUAL.md | STATE_MANAGEMENT_MANUAL (unversioned) | KEEP — v1.1 metadata patch only; content clean (L5/L6 passed) |
| 017 | REVIEW_017_API_AND_SERVICES_MANUAL.md | API_AND_SERVICES_MANUAL (unversioned) | KEEP — v1.1 (Lesson-2 exception box, metadata, cross-refs) |
| 018 | REVIEW_018_DATABASE_MANUAL.md | DATABASE_MANUAL (unversioned) | KEEP — v1.1 CONTENT SURGERY (F-041, now blocked on F-042) + methodology bridge |
| 019 | REVIEW_019_AUTH_MANUAL_v1_2.md | AUTH_MANUAL v1.2 | KEEP — kit-auth authority + F-039 antibody source; v1.3 + F-042 adjudication |
| 020 | REVIEW_020_ECOMMERCE_AND_PAYMENTS_MANUAL.md | ECOMMERCE_AND_PAYMENTS_MANUAL (unversioned) | KEEP — v1.1 patch (scope declaration, API pin, metadata, territory cross-ref) |
| 021 | REVIEW_021_STRIPE_SUBSCRIPTIONS_PLAYBOOK.md | STRIPE_SUBSCRIPTIONS_PLAYBOOK v1.0 | KEEP — v1.1 micro (territory declaration + cross-refs); D-016 promoted |
| 022 | REVIEW_022_GLOBAL_DESIGN_SYSTEM_HANDBOOK.md | GLOBAL_DESIGN_SYSTEM_HANDBOOK (unversioned) | KEEP — MODEL DOC; v1.1 = --role-* contract addition (F-013a/F-043) + header; F-025 adjudicated |
| 023 | REVIEW_023_UI_UX_BUILDING_MANUAL_v1_3.md | UI_UX_BUILDING_MANUAL v1.3 | KEEP — MODEL DOC; v1.4 micro (canonical refs incl. phantom fix, 1-char encoding); D-018 promoted |
| 024 | REVIEW_024_THEMING_MANUAL_v1_1.md | THEMING_MANUAL v1.1 | KEEP — v1.2 patch (log the v1.1 bump, canonical refs, contract alignment post-F-043) |
| 025 | REVIEW_025_THEME_LIBRARY_v1_1.md | THEME_LIBRARY v1.1 | KEEP — MODEL DOC; cleanest in the audit; v1.2 only post-F-043 |
| 026 | REVIEW_026_TOKEN_FILE_v1_1.md | TOKEN_FILE v1.1 | KEEP — v1.2 micro (role sentence, stray fence, history); post-F-013a mint --role-* values |
| 027 | REVIEW_027_COMPONENT_REGISTRY_v1_1.md | COMPONENT_REGISTRY v1.1 | KEEP — MODEL DOC; no patch required. **CLOSES THE AUDIT.** |
| — | RECONCILIATION_REPORT.md | Stack ↔ Repo diff | 5 stack docs stale; ground truth reset |

---

## Open Questions for Tony

**F-032 archaeology: ✅ RESOLVED (Tony, 07-07):** HANDOFF v1.1 NEVER EXISTED — searched everywhere. Phantom reference confirmed; two docs cited a ghost. No recovery work; the canonical-name rule (Waves 1-5) exorcises it.

**🔥 BLOCKING — F-042:** Does the Mark IV kit protect `user_metadata.role` from client-side modification (auth hook / service-role-only writes / restricted updateUser)? Settles the three-way role doctrine; unblocks F-041.

1. F-013a: confirm role colors = `--role-*` tokens (repo suggests already decided) → close.
2. F-014: STARTER_KIT_FEEDBACK.md vs LESSONS_BIN — same thing, renamed, or separate?
3. F-021: do `_SKILLS/` CLAUDE.md doctrine files join the audit scope?

---

## Filed for the Central Delivery System (Endgame Design)

1. Git repo as single canonical home. **Prior art: DOCTRINE_SYNC_MANIFEST + "canonical doctrine repo" backlog item found in repo (D-008).**
2. MANIFEST.md — every doc, version, last-updated, status.
3. DEPENDENCY_MAP.md — doc→doc/tool/concept references.
4. Automation: retired-term lint, mojibake lint, versioned-filename lint, directive-case lint.
5. Distribution: manifest-diff delivery of the current complete set. **The Kit Perfection Campaign drift (F-019) is the canonical case study.**
6. D-001 + D-002 as first-class rules.
7. Canonical-name cross-reference rule (F-011/F-016/F-006).
8. One canonical phase map (F-010).
9. Standardized parseable version header (F-018).
10. Single-source rule — pointers over copies (F-017).
11. "Committed or it doesn't exist" — uncommitted doc edits are ghost edits.
12. Session logs / commit ledger as the authoritative change feed (D-007).
13. Redundancy nuance (from HANDOFF_PACKAGE_PLAYBOOK §5.4): doctrine docs = single source + pointers; project runtime artifacts (e.g. _project/CLAUDE.md forbidden zones) = intentional reinforcement redundancy is legitimate. Encode the distinction so the two rules never conflict.

---

## Audit Progress

🥄 **ALL TIERS COMPLETE — 27/27 DOCS AUDITED.** Tier 1: ✅ 3/3 (REVIEW_003 redo queued per F-022) | Tier 2: ✅ 6/6 | Tier 3: ✅ 5/5 | Tier 4: ✅ 7/7 | Tier 5: ✅ 6/6. Verdicts: 27 KEEP, 0 rewrite-from-scratch, 0 retire.
Tier 3: 0/5 | Tier 4: 0/7 | Tier 5: 0/6
**STATUS 07-07: 🥄 WAVE 0 COMPLETE — all 5 decisions closed (F-013a ✅, F-021 ✅, F-032-arch ✅ phantom, F-042 ✅ table model + kit security ticket opened, F-014 ✅ phantom/handbook-canon). Doctrine repo being seeded (27 docs + _AUDIT + _ARCHIVE). PARALLEL TRACK: kit security ticket (signup-vector fix — app_metadata transport rec; Tony to check 'Enable signups' toggle). NEXT: Wave 1 prompt for Claudy in the doctrine repo (Blueprint v2.1 + Handoff v1.1 + SFP v1.2). Also outstanding: REVIEW_003 redo, F-012 editing-tool diagnosis.**
