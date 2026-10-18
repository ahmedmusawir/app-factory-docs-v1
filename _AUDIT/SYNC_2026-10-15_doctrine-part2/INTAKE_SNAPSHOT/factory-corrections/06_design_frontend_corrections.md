# 06 — Design System / Frontend — Correction Brief

> **DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC**

- **Package:** Factory Doctrine Correction Package 001. Index: `FACTORY_DOCTRINE_CORRECTION_INDEX_001.md`.
- **Prepared by:** Claudy (documentation Engineer seat), 2026-10-11. This is not a QA product and certifies nothing.
- **Primary entries:** FC-071 … FC-084 (14), the certified register §5.F.
- **Authority:** every outcome is **PROPOSED** for Jarvis (Architect) review and Tony (Director) approval. Nothing here is approved policy.
- **Nature:** these are documentation findings about design-tier rules and copyable examples. No starter-kit application was run and no kit source was inspected (Astra C06 limits). No replacement doctrine text is written.

## Pinned sources

| Ref | Revision | Path |
|---|---|---|
| Certified register / QA | `c6210c3` = `c6210c32480558b343a27726a26822e8d959d0f7` | `astra-review/run-002/synthesis/PART1_FINDINGS_DISPOSITION.md`, `astra-review/run-002/synthesis/QA/PART1_CONVERGENCE_QA.md` |
| Astra chunk 06 / Sol chunk 06 | `c6210c3` | `astra-review/run-002/chunks/06_design_frontend/ASTRA_REVIEW.md`, `astra-review/run-002/chunks/06_design_frontend/SOL_REVIEW.md` |
| Fable (blind) | `39a1c6114d72b22d3550d7ff65234ec0f01418f6` (`origin/factory-docs-review-fable-001`) | `fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md` |
| Review baseline | `0a787cb` = `0a787cb826118b4a010765d60e41a449df3ce746` | defect surfaces named per entry |
| Current main | `9c17939` = `9c179392f79b70da099121fc357d3107ad3bb86e` | every surface in this brief is blob-identical to `0a787cb` (QA-4) |

Route codes are as in the index. Short names: UI_UX = `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`; REGISTRY = `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md`; GDSH = `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`.

**Sol C06 preservation rule (binding framing for this brief):** do not weaken the strong design contract while correcting drift. Preserve:
- semantic-token discipline
- human design lock points
- mobile reachability
- kit reuse
- HTML as build reference and PNG as fidelity target
- independent QA separation

Sol C06's root patterns: canonical rule vs copyable-example drift, duplicated executable truth tables, inconsistent enforcement of kit consumption, and verification claims stronger than their evidence.

---

## CF-11 — Design rule/example drift and responsive consistency (FC-071, 072, 073, 075, 077, 078, 082)

### FC-071 — Copyable portal and sidebar layouts hide navigation on mobile, contrary to Rule Zero, and bypass the kit shell
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

### FC-072 — Rail breakpoint rules disagree across the design tier and kit docs
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

### FC-073 — Positive examples present numbered Tailwind colors as convention while Rule Zero-B calls them automatic failures
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

### FC-075 — Theming handoff instructions demote required executable visual artifacts (HTML/PNG)
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

### FC-077 — Token inventory and setup quick paths have not inherited the canonical token contract
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

### FC-078 — The dark-mode example creates a second theme controller beside the kit's provider
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

### FC-082 — Blanket horizontal-scroll prohibitions conflict with prescribed tab and carousel patterns
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

## CF-12 — Frontend accessibility / component implementation (FC-074, 076, 079, 080)

### FC-074 — The drop-in token palette fails its own AA contrast claim
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

### FC-076 — The replacement Button recipe breaks its advertised variant and `asChild` composition API
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

### FC-079 — The Button recipe violates the mandatory 44px target floor
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

### FC-080 — The proposed Grid builds utility class names Tailwind cannot reliably discover
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

## CF-13 — Cross-reference / locator / document-structure hygiene (FC-081, 083, 084 here)

### FC-081 — Design-tier cross-reference paths (`agent_docs/APP_FACTORY/...`) do not resolve in the DocSet
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

### FC-083 — Cross-references cite section anchors that do not exist
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

### FC-084 — Dangling internal reference in DESIGNER_PLAYBOOK (§5.6)
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

---

*End of brief 06. Primary entries: 14 (FC-071 … FC-084). DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC.*
