# PART_06 — correction mapping draft

DRAFT FOR REVIEW — no execution approval. Source outcomes are not relabeled approved.

### FC-071 — Copyable portal and sidebar layouts hide navigation on mobile, contrary to Rule Zero, and bypass the kit shell

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:37`):

- **Certified record:** CF-11 · Severity HIGH · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D02 · Fable FBL-D021 (primary; also related to FC-072)
- **Evidence:** Astra C06 §7 C06-D02; Sol C06 (ACCEPT HIGH); Fable §7 FBL-D021, §9 row 13, §2 row 8.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`: Rule Zero; Sidebar usage; "Sidebar Layout (Desktop Only)"; Example 3 Members Portal; Navbar "hidden on mobile"
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md`: AppShellPage; raw app-shell anti-pattern
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md` §4 (`<Sidebar className="w-64 hidden md:block" />`)
  - Gate M consumers: `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md`, `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md`, `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`
- **Defect:** Rule Zero makes a `hidden md:block` sidebar with no trigger an automatic failure. The same manual's Sidebar usage, Desktop-Only Sidebar Layout and complete Members Portal layout use exactly that pattern, with no mobile trigger, and bypass the Registry's AppShellPage.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Every positive layout example in UI_UX and APP_ARCHITECTURE §4 keeps every navigation destination reachable at mobile widths, through an accessible mobile alternative. Any one of these qualifies:
    - the kit AppShellPage;
    - a complete, approved Sheet/drawer-triggered equivalent;
    - a desktop sidebar (which may use `hidden md:block`) paired, in the same example, with an accessible mobile trigger or alternative navigation.
  - Otherwise the example is explicitly retired.
  - **The class string is not the defect;** a hidden sidebar *without* a mobile alternative is.
- **Preserve:**
  - Rule Zero's mobile requirements and Gate M.
  - Registry drawer behavior: close-on-navigate, Esc, outside-tap.
  - Kit shell reuse.
  - Legitimate desktop-sidebar patterns that ship with a mobile alternative.
- **Likely affected docs / consumers:** UI_UX, APP_ARCHITECTURE §4, REGISTRY; FC-072; builders copying Example 3.
- **Verification intent:**
  - For each positive layout example, a reviewer confirms:
    - every navigation destination the desktop sidebar offers is reachable at mobile widths;
    - the mobile trigger or alternative is present in the example itself, operable and accessible (labeled control, keyboard operable, dismissible per the Registry drawer behavior).
  - Example 3, the Sidebar Layout, the Sidebar usage and APP_ARCHITECTURE §4 each pass that check, or are retired.
  - A live-corpus grep for `hidden md:block` is used only to *locate* candidates. Each hit is dispositioned:
    - **CONSISTENT:** the reachable mobile alternative is present;
    - **NEGATIVE EXAMPLE:** labeled as such;
    - **CHANGE.**
  - A surviving occurrence is acceptable when paired with a verified mobile alternative.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Every positive layout example keeps every navigation destination reachable at mobile widths. Consume AppShellPage or provide a complete accessible mobile trigger/drawer or equivalent navigation alongside the desktop sidebar. hidden md:block is acceptable only when that same example supplies the mobile alternative. Retire an incomplete layout as a copyable positive example.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:477` — ## Layout Components; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:839` — ## Complete Page Examples; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:408` — ## 4. Layout System; MANIFEST ← 3: ECOMMERCE_AND_PAYMENTS_MANUAL, STATE_MANAGEMENT_MANUAL, THEMING_MANUAL.

**Touch proposal:** C-071. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-071` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-072 — Rail breakpoint rules disagree across the design tier and kit docs

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-09 kit evidence. Cross-boundary component: XB-04.

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:74`):

- **Certified record:** CF-11 · Severity MEDIUM · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D04 · Fable FBL-D021 (related; primary in FC-071), FBL-D023 (related; primary in FC-073)
- **Severity divergence (recorded):** Astra MEDIUM vs Fable HIGH (Fable's whole combined finding). The certified MEDIUM stands.
- **Evidence:** Astra C06 §7 C06-D04; Sol C06; Fable §7 FBL-D021, §9 row 14.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` (sidebar → drawer below `lg`)
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Rule Zero 1024; quick reference "custom `lg` 1150px"; breakpoint table)
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` (AppShellPage `xl`/1280; quick table 768; §7)
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §6 (`xl`/1280; per-component fit)
  - `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md` (Gate M, §13.1)
  - `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` (Stage 2)
  - `05_DESIGN_SYSTEM/TOKEN_FILE.md`
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`
- **Defect:** one wide app rail is given three persistence/drawer breakpoints: `lg`/1024, `xl`/1280 and 768. The UI quick reference also calls `lg` a custom 1150px breakpoint.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One rail rule defers to the verified per-component fit contract. Fable: the AppShellPage rail is `xl` as shipped, and the Gate M threshold is the rail's declared fit breakpoint.
  - Generic tables and quick references are synchronized, and the 1150px line is corrected.
  - Verification exercises both sides of the actual transition.
- **Preserve:** the Handbook's per-component fit override; mobile drawer behavior; Gate M.
- **Likely affected docs / consumers:** the surfaces above; Gate M checks in FFM and FBP.
- **Verification intent:**
  - Every rail-breakpoint statement in live docs agrees or cites the rule.
  - Gate M cites it.
  - The documented test widths include the rail transition.
- **Open decision:** DEC-09, confirming the shipped kit value. `xl`/1280 is corroborated by the Handbook; kit source was not inspected (`XB-EXT`; GAP).
- **Proposed route:** `SYNC` (+ `XB-EXT` verification).

**Mapping proposal — ENGINEER-PROPOSED:** The rail transition follows the component’s verified fit contract, not an unrelated generic device label. Verify both sides of the actual transition. The Handbook reports xl/1280 for AppShellPage; publish that as the universal kit value only after pinned kit verification. The 1150px assertion is not a substitute for that check.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:661` — ## Responsive Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:589` — ## 7. Mobile Behavior Reference; MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:429` — ## 6. Responsive & Mobile-Nav; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md:64` — ## 5. Layout & responsive (Rule Zero); MANIFEST ← 6: DESIGNER_PLAYBOOK, COMPONENT_REGISTRY, THEME_LIBRARY, THEMING_MANUAL, TOKEN_FILE, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-072. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-072` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-073 — Positive examples present numbered Tailwind colors as convention while Rule Zero-B calls them automatic failures

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-06. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:103`):

- **Certified record:** CF-11 · Severity MEDIUM · Review CONFIRMED · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D06 · Fable FBL-D023 (primary)
- **Evidence:** Astra C06 §7 C06-D06; Sol C06; Fable §7 FBL-D023, §9 row 15.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (`Main` usage `bg-gray-50`; §10.5 "explicit dark variants"; §10.8)
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` (AppShellPage theme behavior `dark:bg-zinc-800`)
  - `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` §9 "Theme Conventions"
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` §3.4
  - `05_DESIGN_SYSTEM/TOKEN_FILE.md` §4
- **Defect:** UI_UX and the Registry positively endorse palette literals that Rule Zero-B fails and that GDSH/TOKEN_FILE treat as migration debt. The Handbook states its explicit classes as conventions, with no migration flag.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Positive examples use semantic token utilities.
  - Unmigrated kit palette literals are labeled as a surfaced migration dependency, never the target convention. Fable's wording: "LEGACY — migration task per TOKEN_FILE §4".
- **Preserve:**
  - Rule Zero-B.
  - The kit baseline: Astra is explicit that this finding does not authorize changing the kit.
  - "Match, don't invent", as scoped by the FC-005 precedence ruling.
- **Likely affected docs / consumers:** the surfaces above; FC-005, FC-077.
- **Verification intent:**
  - Positive examples contain no numbered palette classes.
  - Handbook §9 and the Registry entry carry the migration label.
- **Open decision:** DEC-06, the precedence ruling (disk-wins vs Rule Zero-B). This is the Sol C06 cross-domain item "kit authority vs token migration".
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Use semantic token utilities in positive examples. A palette literal inherited from a kit is labeled “LEGACY — migration task per TOKEN_FILE §4”; it is evidence of current state, not the target convention. Resolve a conflict through the approved question-scoped authority rule rather than silently selecting disk or Rule Zero-B.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:212` — ## Common Components; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:85` — ## 1. Common Layout Primitives (`src/components/common/`); MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:525` — ## 9. Build & Framework Notes; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-073. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-073` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-074 — The drop-in token palette fails its own AA contrast claim

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:210`):

- **Certified record:** CF-12 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D03 · Fable none
- **Evidence:** Astra C06 §7 C06-D03 (computed contrast table); Sol C06 (ACCEPT HIGH; "not a subjective palette disagreement").
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/TOKEN_FILE.md` (HSL values; "Verified in the style tile")
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` (AA requirement)
  - `05_DESIGN_SYSTEM/THEME_LIBRARY.md` (status values; brand-only list)
- **Defect:** pairs computed from the HSL values fall below the 4.5:1 ordinary-text threshold, yet TOKEN_FILE says "Verified in the style tile":
  - success on card (Mist): 3.48
  - warning: 2.21
  - info: 4.16 (Mist) and 2.95 (Slate)
  - primary-foreground on primary: 2.82
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - The failing text/fill pairs are retuned per mode, keeping their semantic meaning.
  - A computed contrast matrix covering the documented uses is kept, and any "verified" claim cites it.
  - THEME_LIBRARY values are synchronized.
  - Accessible foreground pairing is allowed for brand colors.
- **Preserve:**
  - The destructive and role colors that pass. Astra: do not replace the whole palette.
  - Per-mode tuning; identities-not-statuses role tokens.
- **Likely affected docs / consumers:** TOKEN_FILE, THEME_LIBRARY, GDSH; FC-077.
- **Verification intent:** recompute every documented text/fill pair with Astra's stated method (HSL → sRGB, linearize at 0.04045, weights 0.2126/0.7152/0.0722). Each must reach ≥ 4.5:1 for ordinary text or carry a documented large-text exception.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Do not claim AA verification without a computed contrast matrix for each documented text/fill use in light and dark modes. Retune failing semantic pairs and synchronize THEME_LIBRARY. Brand fills may use a separate accessible foreground. Record the exact token values, ratio, intended use and threshold; large-text or non-text thresholds do not justify a normal-text claim.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/TOKEN_FILE.md:14` — ## 1. Entry stylesheet (`globals.css` _or_ `globals.scss`); MANIFEST ← 3: GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/THEME_LIBRARY.md:25` — ## 2. The "Metro Warm" family (Cyber Pharma v1); MANIFEST ← 4: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL, TOKEN_FILE.
- `05_DESIGN_SYSTEM/THEME_LIBRARY.md:72` — ## 3. Adding a new theme (the repeatable process); MANIFEST ← 4: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL, TOKEN_FILE.

**Touch proposal:** C-074. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-074` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-075 — Theming handoff instructions demote required executable visual artifacts (HTML/PNG)

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:129`):

- **Certified record:** CF-11 · Severity HIGH · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D01 · Fable none
- **Evidence:** Astra C06 §7 C06-D01; Sol C06 (ACCEPT HIGH; "a real producer/consumer contract break").
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/THEMING_MANUAL.md` §§4.2–4.3, Phase 1 sequence
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` (deliverable contract; human locks)
  - Consumer check: `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md`, `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md`
- **Defect:** THEMING labels supporting deliverables "Visual Reference, Not Executable" and goes straight from the token snippet to fabrication. The GDSH and the Engineer consumer require locked, token-driven HTML/PNG plus human canonical-screen and style-tile locks.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - THEMING §4 defers to the GDSH full deliverable contract: HTML as build reference, PNG as fidelity target.
  - Its phase sequence includes or links the canonical-screen and style-tile human locks before fabrication.
- **Preserve:** the Sol C06 preservation list; the FC-018 not-applicable path for nonvisual builds.
- **Likely affected docs / consumers:** THEMING, GDSH; Designer and Engineer handshake.
- **Verification intent:**
  - THEMING no longer calls HTML/PNG non-executable or "NOT the contract".
  - Phase 1 includes both locks before fabrication.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Designer handoff follows GLOBAL_DESIGN_SYSTEM_HANDBOOK §8: executable HTML is the build reference and PNG is the fidelity target for visual interfaces. Lock the canonical screen and style tile with the human approver before fabrication. Theme notes do not replace either deliverable.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:126` — ## 4. The Designer's Deliverable; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:130` — ### 4.1 Primary Deliverable — The Tokens File; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:158` — ### 4.2 Supporting Deliverables (Visual Reference, Not Executable); MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:168` — ### 4.3 Why This Format; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:247` — ## 9. The Phase 0 / Phase 1 Discipline; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-075. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-075` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-076 — The replacement Button recipe breaks its advertised variant and `asChild` composition API

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:237`):

- **Certified record:** CF-12 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D08 · Fable none
- **Evidence:** Astra C06 §7 C06-D08; Sol C06.
- **Defect surfaces (`0a787cb`):** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` §10.1 (replacement `button.tsx`) and the public-home `<Button asChild><Link>` example.
- **Defect:** the replacement defines variants and sizes that do not include the documented `variant="primary"` / `size="md"`. It declares `asChild` but always renders `<button>`.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the manual tells builders to consume the kit Button. If its internals are taught, it uses a source-matched excerpt that keeps the actual variant names and child composition, clearly separate from any replacement instruction.
- **Preserve:** kit reuse; the documented link-composition pattern.
- **Likely affected docs / consumers:** UI_UX §10.1; FC-079 (same recipe).
- **Verification intent:** every Button usage in the docs type-checks against the documented API, and `asChild` composition yields a single link element.
- **Open decision:** none.
- **Proposed route:** `SYNC`, paired with FC-079.

**Mapping proposal — ENGINEER-PROPOSED:** Consume the kit Button, including its verified variants, sizes and asChild composition. Do not replace it with this shortened implementation. An educational internal excerpt must be source-matched and labeled as an excerpt, not installation code. Preserve Link composition through the kit API.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.

**Touch proposal:** C-076. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-076` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-077 — Token inventory and setup quick paths have not inherited the canonical token contract

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:150`):

- **Certified record:** CF-11 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D05 · Fable none
- **Evidence:** Astra C06 §7 C06-D05; Sol C06.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (token minimum; Rule Zero-B setup path)
  - `05_DESIGN_SYSTEM/THEMING_MANUAL.md` (Phase 1 checklist)
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` (canonical token set; TW3/TW4 fork)
- **Defect:**
  - The UI token minimum omits the info, chart, role and radius tokens the Handbook requires.
  - The Theming Phase 1 checklist and UI Rule Zero-B hard-code `globals.css` and `tailwind.config.ts`, whatever the kit's stylesheet or Tailwind major version.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - One canonical token inventory is referenced everywhere.
  - Setup and checklists branch on the confirmed kit stylesheet and Tailwind major version.
  - Abbreviated examples are marked as excerpts.
- **Preserve:** the GDSH token contract and its TW3/TW4 fork; TOKEN_FILE as a reference template, not the live authority.
- **Likely affected docs / consumers:** UI_UX, THEMING, GDSH; FC-073, FC-074.
- **Verification intent:**
  - Every token list in live docs is the canonical set or a labeled excerpt.
  - The setup checklist has TW3/TW4 and stylesheet branches.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** GLOBAL_DESIGN_SYSTEM_HANDBOOK §2 owns the canonical token inventory; TOKEN_FILE supplies reference values. Verify the project entry stylesheet and Tailwind major version before applying setup. Abbreviated snippets are excerpts and do not replace the full token contract, including role tokens.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md:138` — ## 11. New-project checklist (so future labs are fast); MANIFEST ← 6: DESIGNER_PLAYBOOK, COMPONENT_REGISTRY, THEME_LIBRARY, THEMING_MANUAL, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:58` — ## 3. The Token Architecture; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:60` — ### 3.1 Semantic Token Categories; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:96` — ### 3.2 The Files — Where Tokens Live; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:114` — ### 3.3 The Light / Dark / Brand Triad; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:181` — ## 5. The Quick-Swap Workflow (The Pressure-Point Win); MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:745` — ## 10. Quick Reference — "Which Primitive Should I Use?"; MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.

**Touch proposal:** C-077. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-077` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-078 — The dark-mode example creates a second theme controller beside the kit's provider

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:174`):

- **Certified record:** CF-11 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D07 · Fable none
- **Evidence:** Astra C06 §7 C06-D07; Sol C06.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` §10.5 (`src/lib/theme.ts`)
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` (ThemeToggle "don't author")
  - Supporting: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` (DO NOT BUILD)
- **Defect:** UI §10.5 proposes a controller that toggles the HTML class and writes `localStorage.theme` independently of the kit's next-themes ThemeToggle. It also mishandles a stored `system` value.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the manual teaches the existing provider/ThemeToggle API. The standalone DOM/storage controller is retired or isolated as a labeled non-kit demonstration.
- **Preserve:** kit reuse; the light/dark/system three-state model.
- **Likely affected docs / consumers:** UI_UX §10.5; REGISTRY.
- **Verification intent:** no positive example creates a second theme controller in a kit build.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Consume the existing theme provider and ThemeToggle for light, dark and system modes. Do not create a second controller that edits the HTML class or localStorage.theme independently of the provider. A standalone demonstration, if retained, must be explicitly non-kit and cannot be copied into a kit project.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.

**Touch proposal:** C-078. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-078` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-079 — The Button recipe violates the mandatory 44px target floor

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:251`):

- **Certified record:** CF-12 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D09 · Fable none
- **Evidence:** Astra C06 §7 C06-D09; Sol C06.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Rule Zero; §10.6; Button sizes)
  - Supporting: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` (`coarse:` mechanism)
- **Defect:** the copyable Button sizes are 40px, 36px and 40×40px, while Rule Zero and §10.6 require targets of at least 44px.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the recipe meets the 44px floor or keeps the kit's coarse-pointer target-floor mechanism. Any scoped exception is stated consistently, and actual hit areas are verified.
- **Preserve:** the 44px Factory floor; the kit's `coarse:` mechanism.
- **Likely affected docs / consumers:** UI_UX; FC-076.
- **Verification intent:** every documented interactive size meets 44px, or carries the coarse-pointer mechanism and a stated, verified exception.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Interactive targets meet the Factory’s 44px floor. Retain the kit’s coarse-pointer target-floor mechanism and verify the rendered hit area, including icon and compact variants. A 36px or 40px visual box alone is not evidence of a 44px target.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.

**Touch proposal:** C-079. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-079` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-080 — The proposed Grid builds utility class names Tailwind cannot reliably discover

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:267`):

- **Certified record:** CF-12 · Severity MEDIUM · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D10 · Fable none
- **Evidence:** Astra C06 §7 C06-D10; Sol C06.
- **Defect surfaces (`0a787cb`):** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Proposed Grid; the existing literal-class helper).
- **Defect:** the proposed Grid interpolates `grid-cols-${n}` and `gap-${gap}` from numeric props, with no static mapping or safelist.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Every variant the Grid offers has reliably generated CSS, produced through a documented mechanism the project's Tailwind version supports.
  - **Recommended simple implementation:** a bounded prop-to-literal mapping (the existing helper's approach). Each offered value maps to a complete literal class string that Tailwind's scanner can see.
  - Another supported mechanism, such as an explicit safelist, is acceptable only if it is documented beside the recipe and covers every offered variant.
  - Unbounded interpolation with no such mechanism is not acceptable.
- **Preserve:** the existing literal-class helper.
- **Likely affected docs / consumers:** UI_UX.
- **Verification intent:**
  - For every variant the recipe offers, the class it applies is generated through the documented mechanism. Check by literal presence in scanned source, or by the documented safelist/configuration, and confirm in the generated CSS for the documented variants.
  - No offered variant depends on a class appearing incidentally elsewhere in the codebase.
  - Interpolated class names are acceptable only where the documented mechanism provably covers every value they can produce.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Grid variants map each supported prop to a complete literal utility class string. Use a bounded lookup and reject unsupported values; do not construct unbounded Tailwind utility names by interpolation. Any alternative scanner/safelist mechanism must document the actual supported project version and cover every offered variant.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.

**Touch proposal:** C-080. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-080` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-081 — Design-tier cross-reference paths (`agent_docs/APP_FACTORY/...`) do not resolve in the DocSet

**Proposed disposition:** BLOCKED. **Authority:** certified correction YES; package outcome remains proposed. CONDITIONAL: DEC-17 project-path part. 

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:290`):

- **Certified record:** CF-13 · Severity LOW · Review PARTIAL · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D11 · Fable FBL-D010 (related; primary in FC-088)
- **Severity divergence (recorded):** Astra LOW vs Fable HIGH (whole finding; related only). The certified LOW stands.
- **Evidence:** Astra C06 §7 C06-D11; Sol C06; Fable §7 FBL-D010; register §7.3 item 1 (interpretive difference).
- **Defect surfaces (`0a787cb`):**
  - Primary: `05_DESIGN_SYSTEM/THEME_LIBRARY.md` (cross-references), `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` §11
  - QA-4 resolved set: `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`, `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md`, `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md`, `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`, `MANIFEST.md`, `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md`
- **Defect:** THEME_LIBRARY and REGISTRY cite `agent_docs/APP_FACTORY/...` paths for the Handbook, STARTER_KIT and the UI manual, and none resolves in the Hub. Astra frames these as broken DocSet links; Fable frames the same locations as inconsistent project-side landing paths.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):**
  - Doctrine cross-references resolve DocSet-relative.
  - Paths that intentionally target a downstream project are labeled as such and follow the landing-path standard FC-088 sets.
- **Preserve:** canonical basenames, which already make recovery possible.
- **Likely affected docs / consumers:** THEME_LIBRARY, REGISTRY; FC-088, FC-003.
- **Verification intent:** every `agent_docs/APP_FACTORY/...` citation in these docs resolves at the candidate SHA or carries a project-path label consistent with FC-088.
- **Open decision:** DEC-17, whether these are project-side landing paths (joint with FC-088).
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Within the Hub, reference doctrine through canonical DocSet-relative paths. Label an intentional downstream-project snapshot separately with repository, landing path and pinned revision. The project landing-path standard remains conditional on the release/pinning decision; do not make agent_docs/APP_FACTORY a universal rule by inference.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/THEME_LIBRARY.md:115` — ## Cross-References; MANIFEST ← 4: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL, TOKEN_FILE.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:775` — ## 11. Cross-References; MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:254` — ## 4. Components — Inventory; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md:684` — ## 15. Cross-References; MANIFEST ← 12: ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, API_AND_SERVICES_MANUAL, APP_ARCHITECTURE_MANUAL, AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, COMPONENT_REGISTRY, UI_UX_BUILDING_MANUAL.
- `03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md:1650` — ## 16. Bridging The FFM Into The Starter Kit; MANIFEST ← 9: APP_FACTORY_BLUEPRINT, ENGINEER_PLAYBOOK, RECON_QUESTIONNAIRE, APP_FACTORY_SKILLS_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK.

**Touch proposal:** C-081. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-081` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-082 — Blanket horizontal-scroll prohibitions conflict with prescribed tab and carousel patterns

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:191`):

- **Certified record:** CF-11 · Severity LOW · Review UNIQUE (Astra) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra C06-D12 · Fable none
- **Evidence:** Astra C06 §7 C06-D12; Sol C06.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` (tabs as a horizontal scroll strip)
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Rule Zero; §10.6 carousel)
  - `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` (checklist)
- **Defect:** the Handbook prescribes a horizontal tab strip and UI §10.6 supplies a carousel, while UI Rule Zero and the Registry checklist forbid horizontal scroll at any width.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the prohibited condition is defined as unintended viewport or content overflow. Contained scrolling is permitted, with reachable controls and keyboard behavior specified.
- **Preserve:** the no-overflow intent; the mobile transforms (tab strip, carousel).
- **Likely affected docs / consumers:** GDSH, UI_UX, REGISTRY.
- **Verification intent:** the rule text distinguishes overflow from contained scroll, and the tab and carousel patterns pass the literal checklist.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Prohibit unintended horizontal overflow of the viewport or content. A contained tab strip or carousel may scroll horizontally when all controls remain reachable and keyboard operation is defined. Test the containment and navigation at the supported widths; do not ban the very mobile transforms the design contract prescribes.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:11` — ## ⚡ RULE ZERO — MOBILE-FIRST IS THE FOUNDATIONAL POSTURE; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1339` — #### 10. Developer Experience Tools; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1481` — ## 10. Advanced Design Patterns; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1487` — ### 10.1 CVA (Class Variance Authority); MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1600` — ### 10.2 Design Tokens; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1750` — ### 10.3 Component Catalogue Pattern; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1847` — ### 10.4 Class Ordering Convention; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1899` — ### 10.5 Dark Mode Best Practices; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:1948` — ### 10.6 Touch Device Considerations; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2007` — ### 10.7 The `cn()` Utility; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2042` — ### 10.8 Quick Reference: Do's and Don'ts; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md:589` — ## 7. Mobile Behavior Reference; MANIFEST ← 5: DESIGNER_PLAYBOOK, FRONTEND_BUILD_PHASE_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md:64` — ## 5. Layout & responsive (Rule Zero); MANIFEST ← 6: DESIGNER_PLAYBOOK, COMPONENT_REGISTRY, THEME_LIBRARY, THEMING_MANUAL, TOKEN_FILE, UI_UX_BUILDING_MANUAL.

**Touch proposal:** C-082. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-082` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-083 — Cross-references cite section anchors that do not exist

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:309`):

- **Certified record:** CF-13 · Severity LOW · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D024
- **Evidence:** Fable §7 FBL-D024.
- **Defect surfaces (`0a787cb`):**
  - `05_DESIGN_SYSTEM/THEMING_MANUAL.md` §0, §7, §10
  - `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (Lesson 9; Rule Zero-B cross-reference)
  - `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md` §14 (Quick Pattern Lookup)
  - `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md`
  - Targets: `02_PIPELINE_AGENTS/HANDOFF_PACKAGE_PLAYBOOK.md`, `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`
- **Defect:**
  - THEMING cites five anchors that don't exist: "§Theming Files", "§Designer Handoff", "§Typography", "§shadcn Defaults" and "§Lucide Icons".
  - UI_UX Lesson 9 claims APP_ARCHITECTURE was cross-linked, but it never mentions THEMING.
  - SFP §14 cites a non-existent UI-UX "Component Library" section.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** every cited section anchor exists, or the citation is retargeted or removed. The THEMING ↔ APP_ARCHITECTURE pairing is made true, or the Lesson 9 claim is corrected.
- **Preserve:** the cross-reference intent.
- **Likely affected docs / consumers:** the surfaces above. Backlog FBL-S003 (an anchor lint) is optional.
- **Verification intent:** a manual or scripted anchor check over these documents finds every cited "§Name" present in its target.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** Cross-references identify the actual canonical file and live heading. Use GLOBAL_DESIGN_SYSTEM_HANDBOOK §8 for Designer deliverables, TOKEN_FILE §3 for font wiring, and COMPONENT_REGISTRY §5 for Shadcn primitives. Add the missing APP_ARCHITECTURE reference to THEMING_MANUAL for token architecture. Replace nonexistent section labels only with the verified equivalent, not a guessed anchor.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:12` — ## 0. Reader's Guide; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:218` — ## 7. What This Manual Does NOT Cover; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/THEMING_MANUAL.md:266` — ## 10. Cross-References; MANIFEST ← 5: DESIGNER_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE, UI_UX_BUILDING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:84` — ## 🎨 RULE ZERO-B — THEMING IS THE SECOND FOUNDATIONAL POSTURE; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md:2070` — ## Appendix — Run 001 Lessons That Updated This Manual; MANIFEST ← 4: FRONTEND_BUILD_PHASE_PLAYBOOK, COMPONENT_REGISTRY, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEMING_MANUAL.
- `01_CONSTITUTION/SOFTWARE_FACTORY_PLAYBOOK.md:1006` — ## 14. Manual Reference Guide; MANIFEST ← 8: APP_FACTORY_BLUEPRINT, FFM_PLAYBOOK, FRONTEND_FIRST_PLAYBOOK, TESTING_PLAYBOOK, QA_PLAYBOOK, BUG_FIX_PLAYBOOK, BIM_PLAYBOOK, FEAT_PLAYBOOK.
- `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md:783` — ## 7. Component Architecture; MANIFEST ← 3: ECOMMERCE_AND_PAYMENTS_MANUAL, STATE_MANAGEMENT_MANUAL, THEMING_MANUAL.

**Touch proposal:** C-083. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-083` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.

### FC-084 — Dangling internal reference in DESIGNER_PLAYBOOK (§5.6)

**Proposed disposition:** CHANGE. **Authority:** certified correction YES; package outcome remains proposed.  

**Source and preservation — INTAKE-VERBATIM** (`factory-corrections/06_design_frontend_corrections.md:331`):

- **Certified record:** CF-13 · Severity LOW · Review UNIQUE (Fable) · Current-main OPEN — SOURCE UNCHANGED · Correction required YES
- **Reviewer source IDs:** Astra none · Fable FBL-D013
- **Evidence:** Fable §7 FBL-D013.
- **Defect surfaces (`0a787cb`):** `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md` §7.
- **Defect:** DESIGNER §7 cites "§5.6 minimum display fields", but §5 has no 5.6.
- **Current-main status:** OPEN — SOURCE UNCHANGED.
- **Proposed outcome (PROPOSED — not approved):** the reference resolves (Fable suggests UI_SPEC §5) or is removed.
- **Preserve:** the "all required elements present" check.
- **Likely affected docs / consumers:** DESIGNER §7.
- **Verification intent:** the citation resolves at the candidate SHA, or it is gone.
- **Open decision:** none.
- **Proposed route:** `SYNC`.

**Mapping proposal — ENGINEER-PROPOSED:** - [ ] All required elements and minimum display fields in the approved UI_SPEC are present; record NOT APPLICABLE only where that contract says so.

**Verified live placements (BASE_SHA 9c179392f79b70da099121fc357d3107ad3bb86e):**
- `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md:217` — ## 7. Screen-by-Screen Discipline; MANIFEST ← 10: APP_FACTORY_BLUEPRINT, SOFTWARE_FACTORY_PLAYBOOK, ARCHITECT_PLAYBOOK, ENGINEER_PLAYBOOK, HANDOFF_PACKAGE_PLAYBOOK, APP_FACTORY_SKILLS_PLAYBOOK, FFM_PLAYBOOK, GLOBAL_DESIGN_SYSTEM_HANDBOOK, THEME_LIBRARY, TOKEN_FILE.

**Touch proposal:** C-084. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.

**Search:** query `FC-084` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.

**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.
