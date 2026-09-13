# CHUNK 06 — DESIGN / FRONTEND REVIEW

## 1. STATUS

COMPLETE — all six primary files examined; bounded references checked; findings, strengths, scores and coverage finalized.

Started 2026-09-13 12:37 UTC. Branch verified as `factory-docs-review-astra-w-chunks`; initial working tree clean. Contract read completely. Execution Plan Chunk 06 establishes `05_DESIGN_SYSTEM/` as the primary scope. No prior review conclusions are evidence.

Final verification: 12 uniquely identified defects (0 BLOCKER / 3 HIGH / 7 MEDIUM / 2 LOW), 2 uniquely identified suggestions, and five integer scores in range. All 12 required sections are present. Only the authorized report differs from the initially clean checkout; branch unchanged. No doctrine, packet, other review, telemetry, history or branch structure was modified. No commit, push or merge was performed. Unknowns and session limits are explicit in §10. Examination took approximately nine minutes (started 12:37 UTC, finalized about 12:46 UTC).

## 2. SCOPE

Objective: determine whether design intent becomes reproducible, high-fidelity, testable frontend implementation with executable Designer → Engineer contracts.

Primary files (all substantive Markdown in `05_DESIGN_SYSTEM/`):

- `GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`
- `TOKEN_FILE.md`
- `THEME_LIBRARY.md`
- `THEMING_MANUAL.md`
- `COMPONENT_REGISTRY.md`
- `UI_UX_BUILDING_MANUAL.md`

Out of scope: other chunks, whole-domain supporting reviews, prior Astra/Sol/Fable reviews, dispositions, Run 001, synthesis, and doctrine repair. Supporting reads were limited to authority or explicit dependencies and are logged below.

## 3. DOMAIN MODEL

The Architect establishes approved scope and drafts UI_SPEC; the Designer translates that intent into tokens, a human-approved canonical screen and style tile, cloned screen HTML/PNG, revised UI_SPEC, and a primitive/KIP manifest (Handbook §§8–9; Designer §§1, 8, 10; Engineer §3). Tony owns product decisions. Engineer greenfield preflight rejects missing approved brief/spec or missing artifacts. Conversion instead consumes source screenshots and Architect-authored contracts; it does not require a new Designer pass (Blueprint router; Engineer §3).

The Handbook owns token names and semantics. Each project's entry stylesheet owns live values; TOKEN_FILE is a TW3 reference template and THEME_LIBRARY catalogs value sets. Components should consume kit primitives and semantic utilities. Light/dark, 375px mobile behavior, named controls, keyboard paths and AA contrast are foundational.

Engineer kit execution uses recon and a pre-authoring kit audit, then FFM stages. Frontend completion checks functional demo flows separately from mobile collapse and desktop frame fidelity in both themes. Gate M feeds independent Gate Q; Engineer self-verification does not certify the release (Frontend Build Phase §9; QA §12).

## 4. FIVE-DIMENSION SCORECARD

Scores apply only to Chunk 06.

| Dimension | Score (1–5) | Evidence-based justification |
|---|---:|---|
| Correctness | 3 | Sound token/composition/approval model, but reference contrast fails and the Button/Grid examples have concrete technical faults (D03, D08–D10). |
| Consistency | 2 | Positive examples contradict mandatory mobile/color rules; handoff formats, token minimums and breakpoint summaries disagree (D01–D07). |
| Completeness | 3 | Five-artifact handoff, role ownership, light/dark, responsive transforms and independent QA connection exist. Reproducible visual evidence and applicability for nonvisual work remain underspecified in the bounded sources. |
| Executability | 2 | A competent reader can reconstruct the intended process, but cannot follow all copyable examples/checklists literally without rejecting or repairing them (D01–D12). |
| Maintainability | 2 | Canonical authority is named, yet independent tables, recipes and old positive examples remain unsynchronized; the maintenance rule to mark superseded content has not prevented these contradictions. |

## 5. WHAT IS STRONG

1. **An explicit, executable design contract.** Handbook §§1–3 and §8 separates the token schema from live project values and components. TOKEN_FILE lines 6–10 explicitly identifies itself as a reference template, not the live authority. Preserve this distinction and semantic status/role identities: it allows theming without component forks.
2. **The main Designer → Engineer handshake is compatible.** Handbook lines 99–109, Designer lines 243–251/311–326 and Engineer lines 139–189 agree on tokens, HTML/PNG, UI_SPEC and manifest. Engineer stops when the package is missing. Preserve this full contract while correcting the Theming side path (D01).
3. **Human design decisions have concrete lock points.** Handbook lines 115–122 makes canonical-screen and style-tile locks human approval gates; Designer lines 63–68 reserves product decisions to Tony and lines 95–99 requires an approved brief. Preserve approval before screen multiplication and real-app fabrication; do not replace it with an agent's aesthetic judgment.
4. **Mobile behavior is unusually actionable at the rule level.** Handbook lines 66–72 names table→cards, rail→drawer, KPI→2×2 and tab-strip transforms. UI Rule Zero lines 43–70 specifies reachability, touch sizes and pre-authoring sketches. Registry lines 268–275 documents drawer dismissal and close-on-navigation. Preserve these concrete requirements; fix examples and breakpoint drift rather than weakening mobile coverage.
5. **Reuse has both a lookup and an escalation mechanism.** Registry lines 8–22, its decision tree, and lines 715–727 establish scan-first, no silent fork, operator decisions and KIP disposition. Engineer lines 250–270 and Frontend First lines 22–37 add verification against the actual kit and prohibit wrappers around finished capabilities. Preserve composition, verified kit consumption and explicit gaps.
6. **Fidelity and functionality feed independent QA.** Handbook line 103 distinguishes build reference from QC target. Frontend Build Phase lines 441–450 separately checks working flows, mobile collapse, and desktop gutters/max-width against the Designer CSS in both themes. Lines 457–462 requires Gate Q and Gate D. QA lines 28–40, 690–701 and 721–760 explicitly treats Engineer reports as claims and Gate M as an input. Preserve this separation: screenshots are visual evidence, not proof that permissions, persistence or workflows work.

The TW3 HSL-no-wrapper mapping was also checked against official Tailwind guidance; the absence of an explicit `<alpha-value>` placeholder was **not** counted as a defect. The role and destructive on-card contrast pairs tested in D03 pass; the palette is not uniformly defective.

## 6. PRIORITY FINDINGS

1. **C06-D03 (HIGH):** Drop-in values fail AA for their prescribed ordinary-text uses despite a verification claim.
2. **C06-D02 (HIGH):** Complete positive portal layouts lose mobile sidebar navigation and bypass the reusable shell.
3. **C06-D01 (HIGH):** The theming engagement path demotes HTML/PNG while the main handoff and Engineer require them.
4. **C06-D04 (MEDIUM):** Conflicting rail breakpoints can cause unnecessary kit changes and incomplete verification.
5. **C06-D08 (MEDIUM):** The replacement Button recipe contradicts its own advertised API and loses `asChild` composition.

## 7. RANKED DEFECTS

Ranked by severity and operational impact. Stable IDs retain their original assignment order. Totals: **12 defects — 0 BLOCKER, 3 HIGH, 7 MEDIUM, 2 LOW.**

### C06-D03 — The drop-in token palette fails its own AA contrast claim

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files:** `05_DESIGN_SYSTEM/TOKEN_FILE.md`; `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`; `05_DESIGN_SYSTEM/THEME_LIBRARY.md`.
- **Precise evidence:** Handbook lines 79–81 requires AA contrast and per-mode status numbers on card surfaces. TOKEN_FILE lines 33–54 and 85–106 supplies the HSL values; line 221 says success/destructive were tuned for small table numbers and “Verified in the style tile.” THEME_LIBRARY lines 31–35 repeats the same status values. Fresh calculation from the HSL triplets, not approximate hex comments, gives:

  | Token usage | Mode | Contrast | Required for ordinary small text |
  |---|---|---:|---:|
  | success text on card | Mist | 3.4826:1 | 4.5:1 |
  | warning text on card | Mist | 2.2128:1 | 4.5:1 |
  | info text on card | Mist | 4.1648:1 | 4.5:1 |
  | info text on card | Slate | 2.9501:1 | 4.5:1 |
  | primary-foreground on primary | Both | 2.8232:1 | 4.5:1 |

- **Why a defect:** The mandated small-text use of success demonstrably fails despite the verification claim; ordinary primary button labels and other semantic pairs also fail. Computation converts HSL to sRGB, linearizes each channel at 0.04045, uses luminance weights 0.2126/0.7152/0.0722, then `(Llighter + .05)/(Ldarker + .05)`. The 4.5:1 threshold and use of underlying colors follow [W3C's contrast explanation](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- **Operational consequence:** Reusing the advertised drop-in palette yields inaccessible normal-sized status text and action labels; a misleading “verified” note can discourage rechecking.
- **Recommended resolution:** Retune failing text/fill pairs per mode; preserve semantic meaning, and persist a computed contrast matrix covering actual uses before retaining verification claims. Synchronize catalog values. Permit brand foreground adjustments when needed; THEME_LIBRARY line 93's brand-only list should not prevent accessible foreground pairing.
- **Confidence / limits:** High for opaque CSS color pairs, assuming the documented small-text uses. No project style tile was available or rendered, and no deployed app is alleged to use these values unchanged. Destructive and the three role colors pass the tested on-card small-text threshold in both shipping modes; do not indiscriminately replace the whole palette.

### C06-D02 — Copyable portal layouts remove mobile navigation and bypass the kit shell

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files:** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`; `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md`.
- **Precise evidence:** UI manual Rule Zero lines 43–59 explicitly fails `hidden md:block` sidebars without a trigger and requires all controls reachable. Its Sidebar usage lines 511–522, Sidebar Layout lines 814–835, and complete Members Portal layout lines 1002–1036 nevertheless use a hidden 25rem sidebar with no mobile trigger/replacement. Registry lines 243–291 documents a ready AppShellPage with a Sheet, close-on-nav, Esc and outside-tap; lines 631–648 identifies raw app-shell flex layouts as an anti-pattern.
- **Why a defect:** These are positive implementation examples, including a complete route layout, that implement the exact forbidden mobile disappearance and avoid the provided shell. The separate generic MobileMenu fragment at UI lines 694–704 does not appear in these layouts.
- **Operational consequence:** Literal implementation loses portal navigation on phones and requires corrective reconstruction despite using the manual's advertised proven pattern.
- **Recommended resolution:** Replace or explicitly retire these examples in favor of the kit shell or a complete approved equivalent retaining mobile reachability.
- **Confidence / limits:** High for the documented layouts. No actual starter-kit application was executed; an independently implemented Navbar could provide some routes, but these examples neither specify nor guarantee equivalent sidebar navigation.

### C06-D01 — Theming handoff instructions demote required executable visual artifacts

- **Classification:** DEFECT
- **Severity:** HIGH
- **Affected files:** `05_DESIGN_SYSTEM/THEMING_MANUAL.md`; `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`.
- **Precise evidence:** Theming §§4.2–4.3, lines 158–174, labels supporting deliverables “Visual Reference, Not Executable,” describes a style tile as a one-page image, and says these are “NOT the contract Claudy fabricates against.” Its Phase 1 sequence, lines 256–262, proceeds from the token snippet to fabrication. Handbook lines 88–109 requires token-driven HTML and PNG for tiles and screens and says HTML is load-bearing; lines 115–122 requires human canonical-screen and style-tile locks. Bounded consumer check: Engineer lines 139–189 requires the locked HTML/PNG set, approved UI_SPEC and manifest, and stops if missing; Designer lines 180–185 agrees.
- **Why a defect:** The supposedly standalone theming engagement specification supplies a materially smaller artifact contract than the governing handbook and actual consumer. Tokens encode values, not screen structure, responsive transformations or control behavior.
- **Operational consequence:** A Designer/operator following this engagement sequence can produce a token-only handoff that Engineer must reject, or fabricate layouts without the approved executable references.
- **Recommended resolution:** Make Theming §4 explicitly defer to the full Handbook deliverable contract, preserve HTML as build reference and PNG as fidelity target, and include or link the two human locks in its phase sequence.
- **Confidence / limits:** High; direct primary contradiction confirmed against producer and consumer. This is not a claim that the aligned Engineer preflight permits omission.

### C06-D04 — Responsive rules and acceptance references disagree on rail breakpoints

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected files:** `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`; `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`; `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md`.
- **Precise evidence:** Handbook lines 66–72 mandates sidebar→drawer below `lg`. UI Rule Zero lines 30–44 says wide rails persist at 1024; Registry AppShellPage lines 268–275 instead says below `xl` is a drawer and 1280+ is persistent. Registry's own quick table line 596 says sidebars persist at 768. UI quick reference line 2051 calls `lg` a custom 1150px breakpoint despite its table at lines 680–686 defining 1024. Bounded kit authority confirms the 1280 rail and per-component fit override at Starter Kit Handbook lines 433–436.
- **Why a defect:** A consumer cannot use all prescribed breakpoint contracts for the same wide app rail. This remains a problem even after fixing the missing mobile trigger in D02: a correct drawer could still be opened/closed at the wrong width or graded against the wrong target.
- **Operational consequence:** Unnecessary modification of a compliant kit shell, crowded intermediate layouts, or false acceptance failures. A 375/768/1024-only pass also never exercises the documented persistent AppShellPage state.
- **Recommended resolution:** Defer rail behavior to the verified per-component fit contract; synchronize generic tables and quick references, and include both sides of the actual transition in verification.
- **Confidence / limits:** High for documentary disagreement. No physical kit source was inspected; 1280 is corroborated doctrine, not a new runtime finding.

### C06-D08 — The replacement Button recipe breaks its advertised variant and composition API

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file:** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`.
- **Precise evidence:** §10.1 writes a replacement at `src/components/ui/button.tsx` (lines 1515–1572). Its variant keys are `default/destructive/outline/secondary/ghost/link` and sizes `default/sm/lg/icon` (1529–1543), while lines 1510 and 1581 call `variant="primary"` valid and line 1510 also uses `size="md"`. ButtonProps declares `asChild` (1553–1558), but the implementation always renders `<button>` and spreads the unconsumed prop (1561–1568). The public-home example uses `<Button asChild><Link ...>` at lines 863–865.
- **Why a defect:** The type-safe example supplies keys absent from its own recipe. The replacement cannot implement the documented link composition: the recipe has no conditional child-slot behavior at all.
- **Operational consequence:** Type errors when copying advertised valid calls; replacing the kit primitive also turns the linked CTA example into nested interactive elements instead of the intended single link.
- **Recommended resolution:** Consume the kit Button. If teaching its internals is necessary, use a source-matched excerpt preserving its actual variant names and child composition behavior, clearly distinguished from instructions to replace it.
- **Confidence / limits:** High by direct code inspection; no installed component library or compiler was run. This concerns the printed implementation, not an allegation about the actual kit Button.

### C06-D05 — Token inventory and setup quick paths have not inherited the canonical contract

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected files:** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`; `05_DESIGN_SYSTEM/THEMING_MANUAL.md`; `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`.
- **Precise evidence:** Handbook lines 29–37 requires the expanded set and the TW3/TW4 fork; Theming lines 85–94 explicitly aligns success/warning/info/chart/role/radius to it. UI lines 97–103 still gives the older minimum and says success/warning “may be added,” omitting info/chart/role/radius. Theming lines 105–107 and 134 require kit-matched extension/format, but its actual Phase 1 checklist at lines 257–259 selects `src/app/globals.css` and `tailwind.config.ts` unconditionally. UI Rule Zero-B lines 92–103 likewise presents the TW3 CSS/config path as universal.
- **Why a defect:** Following the operational minimum/checklist can omit required token utilities or select an unused stylesheet/config for a kit whose extension or Tailwind major differs. The explicit canonical authority prevents an authority vacuum but does not make the contradictory consumer instructions executable as written.
- **Operational consequence:** Partial semantic theming, missing role/status utilities, or token changes that do not affect the app.
- **Recommended resolution:** Reference one canonical token inventory and branch the actual setup/checklist by confirmed kit stylesheet and Tailwind major. Mark abbreviated examples as excerpts and specify completion against the contract.
- **Confidence / limits:** High for the inventory and checklist contradiction; no claim that a particular TW4 kit exists here or that all illustrative snippets must be exhaustive.

### C06-D07 — The dark-mode example creates a second controller beside the kit's theme provider

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected files:** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`; `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md`.
- **Precise evidence:** UI lines 460–473 identifies the existing light/dark/system ThemeToggle using next-themes on every navbar. Registry line 761 says ThemeToggle “don't author”; Starter Kit Handbook line 657 also says DO NOT BUILD. UI §10.5 lines 1923–1943 nevertheless proposes `src/lib/theme.ts` that toggles the HTML class and independently writes `localStorage.theme`. Its initializer handles only `dark` or an absent stored value plus OS preference; explicit stored `system` does not follow that branch.
- **Why a defect:** This is a separate state owner with no integration into the documented provider or its three-state preference model. It bypasses kit consumption and does not implement the advertised system preference behavior.
- **Operational consequence:** Theme controls and rendered mode can disagree, with different initialization behavior across reloads and system preferences.
- **Recommended resolution:** Teach the existing provider/ThemeToggle API; retire standalone DOM/storage control or clearly isolate it to a separately scoped non-kit demonstration.
- **Confidence / limits:** High for the code's missing `system` handling and competing controller. Exact provider synchronization effects were not runtime-tested.

### C06-D06 — Positive examples explicitly authorize bypassing semantic colors

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected files:** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`; `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md`.
- **Precise evidence:** UI Rule Zero-B lines 109–121 fails numbered colors and requires surfacing missing tokens. UI Main usage line 377 uses `bg-gray-50`; §10.5 lines 1912–1920 positively recommends `bg-white dark:bg-gray-900` and gray text “when tokens don't cover your needs.” Registry calls its primitives theme-aware (line 87), then AppShellPage theme behavior line 278 endorses `dark:bg-zinc-800`. Handbook lines 48–51 instead requires migration of such kit hardcoding.
- **Why a defect:** These are positive usage recommendations, not the clearly labeled negative examples elsewhere. They instruct the precise workaround the governing rule prohibits.
- **Operational consequence:** A legitimate brand/theme swap leaves components behind; Engineer must reconcile instructions or ship exceptions that fail the documented gate.
- **Recommended resolution:** Replace positive palette literals with semantic utilities; identify unmigrated kit behavior as a surfaced migration dependency, never the target convention.
- **Confidence / limits:** High for the positive primary examples. Existing kit migration ownership is separately flagged below; this finding does not authorize altering a kit baseline.

### C06-D09 — The button recipe violates the mandatory 44px target floor

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file:** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`.
- **Precise evidence:** Rule Zero lines 43 and 56 and §10.6 line 1952 require at least 44px targets. The copyable Button sizes at lines 1538–1543 specify default `h-10`, small `h-9`, and icon `h-10 w-10`: 40px, 36px and 40×40px with standard 16px rem sizing. There is no larger hit area or coarse-pointer floor in that recipe. Starter Kit Handbook lines 442–446 provides a `coarse:` mechanism and requires checking generated CSS.
- **Why a defect:** The recipe's normal sizes fail the manual's own compulsory authoring criterion. Correcting D08's prop/type behavior would not correct target geometry.
- **Operational consequence:** The supplied default and small controls are unacceptable under the Factory's mobile gate when implemented literally.
- **Recommended resolution:** Preserve the kit's appropriate target-floor mechanism or make the documented recipe meet 44px; state any scoped exception consistently and verify actual hit areas.
- **Confidence / limits:** High for this recipe at standard sizing. The 44px rule is Factory doctrine; this finding does not claim every smaller control violates every WCAG version or criterion.

### C06-D10 — Proposed Grid builds utility names Tailwind cannot reliably discover

- **Classification:** DEFECT
- **Severity:** MEDIUM
- **Affected file:** `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`.
- **Precise evidence:** Proposed Grid, lines 1215–1246, accepts numeric props and builds `grid-cols-${mobile} md:grid-cols-${tablet} lg:grid-cols-${desktop} gap-${gap}` at line 1234. No static mapping or safelist is supplied. The same manual's alternative helper, lines 1288–1296, does use complete literal class strings.
- **Why a defect:** Tailwind's source scanner does not evaluate numeric props/string interpolation. The recommended new abstraction only works incidentally when another source file already contains the required complete classes. This behavior is documented by [Tailwind's dynamic-class guidance](https://v3.tailwindcss.com/docs/content-configuration#dynamic-class-names).
- **Operational consequence:** A developer adopting this optional improvement can get missing columns/gaps in generated CSS without a TypeScript error.
- **Recommended resolution:** Use bounded prop-to-literal mappings (the existing helper demonstrates the approach) or another explicitly supported strategy, and verify generated classes for the offered variants.
- **Confidence / limits:** High for the unbounded proposed API. Classified MEDIUM, not HIGH: it is an optional enhancement, not the required page implementation path; literal classes elsewhere can mask particular cases.

### C06-D11 — Canonical cross-reference paths do not resolve in this DocSet

- **Classification:** DEFECT
- **Severity:** LOW
- **Affected files:** `05_DESIGN_SYSTEM/THEME_LIBRARY.md`; `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md`.
- **Precise evidence:** THEME_LIBRARY lines 117–118 directs readers to `agent_docs/APP_FACTORY/design-system/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` and `agent_docs/APP_FACTORY/STARTER_KIT_HANDBOOK.md`. Registry lines 777–778 calls STARTER_KIT_HANDBOOK a sibling and links `agent_docs/APP_FACTORY/UI-UX-BUILDING-MANUAL.md`. Existence checks failed for all three full paths and `05_DESIGN_SYSTEM/STARTER_KIT_HANDBOOK.md`. Current targets are under `05_DESIGN_SYSTEM/` and `01_CONSTITUTION/`.
- **Why a defect:** Explicit cross-reference locations for live governing sources cannot be followed in the repository being reviewed.
- **Operational consequence:** Failed file opens and unnecessary source rediscovery during authoring. Canonical basenames make recovery possible, limiting severity.
- **Recommended resolution:** Use resolvable DocSet-relative paths; label any intentional downstream-project paths as such and distinguish them from repository doctrine links.
- **Confidence / limits:** High for this checkout. Project-specific `_design/` and `globals.css` references were not treated as missing repository files.

### C06-D12 — Horizontal-scrolling rules prohibit the prescribed tab and carousel patterns

- **Classification:** DEFECT
- **Severity:** LOW
- **Affected files:** `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md`; `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md`; `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md`.
- **Precise evidence:** Handbook line 71 prescribes tabs as a horizontal scroll strip. UI Rule Zero line 47 forbids horizontal scroll at any width below desktop; Registry checklist line 622 says horizontal scroll at any width must be fixed. UI §10.6 lines 1989–1997 explicitly provides a horizontal carousel.
- **Why a defect:** The prohibition does not distinguish viewport overflow from intentional contained scrolling, so the documented compliant pattern can fail the literal checklist.
- **Operational consequence:** False gate failures or removal of an intended mobile navigation/content affordance.
- **Recommended resolution:** Define the prohibited condition as unintended viewport/content overflow and specify permitted contained scrolling with reachable controls and keyboard behavior.
- **Confidence / limits:** High for wording conflict; LOW because a competent reviewer may infer the intended distinction. No browser overflow was tested.

## 8. RANKED SUGGESTIONS

**2 suggestions**, ranked by value. Neither is a prerequisite inferred as a current gate.

### C06-S01 — Give visual references a reproducible capture and comparison manifest

- **Classification:** SUGGESTION
- **Affected sources:** Handbook §§7–9; Designer §5; Frontend Build Phase §9 (bounded dependency).
- **Evidence / value:** HTML/PNG roles, 2× rendering, both themes, and CSS-based frame checks already exist. A small artifact manifest could bind each screen/state to its HTML, PNG, token revision, viewport width/height, device scale, data fixture, fonts/readiness, capture command and approval record. It would make comparison repeatable and distinguish intentional reapproval from unnoticed baseline drift.
- **Recommended improvement:** Specify one compact per-project capture recipe and comparison record, including the actual component transition widths and the owner of a changed baseline. Permit manual comparison when sufficient; do not require a screenshot service or pixel-diff suite for every project.
- **Confidence / limits:** High value; no claim that pixel-diff automation is currently mandatory or that a screenshot proves functional correctness. Rendering/bundling of standalone HTML with project CSS remains UNKNOWN in this checkout.

### C06-S02 — Translate the accessibility bar into a short per-screen evidence matrix

- **Classification:** SUGGESTION
- **Affected sources:** Handbook §6; UI manual Rule Zero and §10.6; QA §12 (bounded dependency).
- **Evidence / value:** Labels, accessible names, visible focus, keyboard paths, touch size and contrast are already requirements. A small matrix assigning each check to design versus implemented-browser verification would help preserve them across handoff, including focus return, errors/status announcements, zoom/reflow and both themes where relevant.
- **Recommended improvement:** Link concrete acceptance rows and evidence owners from UI_SPEC, preserving independent QA. Distinguish the Factory's own target floor from the chosen accessibility standard/version; use an applicability decision for features the app does not contain.
- **Confidence / limits:** Improvement to existing meaningful controls, not a claim that accessibility is absent or that every suggested check is already a mandatory Factory gate.

## 9. CROSS-DOMAIN DEPENDENCIES

These are handoff records, **not additional scored defects or suggestions**.

- **DEPENDENCY — role/build ownership.** Designer §§1/8/10 and Engineer §§3/5 supply scope ownership, UI_SPEC revision, package acceptance, per-pipeline DATA_CONTRACT ownership and the recon → audit → FFM execution chain. The main package is aligned. FFM and Handoff Package playbooks were not opened for a second-domain review.
- **DEPENDENCY — independent QA and evidence.** Frontend Build Phase §9 explicitly requires Gate Q/D, and QA §12 makes Gate M a specialist input after self-verification. This refutes the hypothesis that frontend fidelity permits Engineer self-certification. Frontend Build Phase lines 458–459 still point to QA §§9/10 while current QA headings are §§12/13 (lines 684/774): **SYNTHESIS FLAG** for build/QA reference maintenance, not an added Chunk 06 path defect.
- **CONTRADICTION CANDIDATE — server data placement versus literal thin pages.** UI manual lines 571–575 bans page data fetching and allows only an eight-line wrapper, consistent with Frontend First lines 328–351 and Architecture §11 lines 1355–1371. Architecture §§5–7 instead demonstrates service fetching inside server `page.tsx` (lines 530–545, 654–674, 790–803) and client PageContent. UI's own public-home example at lines 843–884 also places composition directly in `page.tsx`, and its metadata wrapper at 554–568 exceeds the stated limit. The intended server-first/service-boundary principles are sensible, but the authoritative permitted page responsibilities and counting/exceptions need a bounded architecture/build disposition. Do not solve this by moving server-only fetching into an interactive client component.
- **CONTRADICTION CANDIDATE — kit authority versus token migration.** Handbook lines 49–51 makes migration of numbered kit colors foundational; Registry still describes a numbered AppShell default. Bounded Starter Kit Handbook line 580 also prescribes numbered backgrounds, while Frontend First lines 30–37 says verified running kit wins over stale doctrine. D06 proves the primary example conflict; the owner, approved scope and upstream/downstream lifecycle of a kit token migration need kit/build resolution. No physical kit source was reviewed.
- **CONTRADICTION CANDIDATE — desktop-only exceptions.** Handbook line 73 permits explicitly desktop-oriented consoles. Designer lines 236 and 298–300 permits an expressly desktop-only brief; UI Rule Zero lines 14–22/48–80 applies to every UI and says it wins over other doctrine. Clarify who can approve an actual mobile exemption, as distinct from a desktop-oriented design that still has mobile transforms. No deployed console defect is inferred.
- **SYNTHESIS FLAG — nonvisual routing.** Engineer lines 987–1045 explicitly supports Backend Bundle/CLI work; the primary design handbook says its five-artifact package is per project, while the bounded greenfield router assumes a Designer. An explicit nonvisual/low-visual applicability waiver was not found in the examined portions. Routing ownership must resolve this; it is not evidence that all Factory backend work is currently forced to fabricate screens.
- **DEPENDENCY — required KIPs.** Handbook lines 59–60 and Designer manifest require missing primitives to be identified for building first. Registry lines 720–727 says raise them in the next phase completion report and wait for accept/defer/reject. How to unblock a currently required primitive if deferred/rejected is not established here. Preserve operator ownership; module planning/kit owners must determine a scoped alternative or block.
- **CONTRADICTION CANDIDATE — approval recording/template defaults.** Designer's UI_SPEC template lines 255–269 starts as `APPROVED` with a `Locked` sample row, though actual human approval is required elsewhere. The bounded template does not itself record approver/date/artifact revision. This is a producer/template governance concern for disposition, not evidence that a human approval was bypassed in an actual run.

## 10. AMBIGUITIES / UNKNOWNS

- **UNKNOWN:** The actual starter-kit revision, installed package versions, component implementations and application behavior. This is a doctrine checkout review; no kit/app was installed, built, rendered or exercised. Registry prop claims (including ReactNode versus render-function sidebar) were not certified against source.
- **UNKNOWN:** A repeatable standalone design-HTML build/capture command and CSS/font linkage for a specific project. Shared token names alone do not prove two artifacts actually load the same live values. No project `_design/` artifact was available within the assigned scope.
- **UNKNOWN:** Existing project-specific visual baseline retention, change approval and regression automation. The bounded testing-playbook searches did not establish a visual-capture contract; that is not proof no other Factory resource supplies one.
- **UNKNOWN:** Nonvisual design exemption authority, desktop-only exemption authority, and the required-primitive KIP deferral path; see the explicit cross-domain records.
- **UNKNOWN:** Whether current deployed projects copied any defective example or palette unchanged. Findings are against the current printed rules/examples, not inferred incidents.
- **Session/model limits:** The session is identified as GPT-6 and the examiner was assigned Astra; an independently inspectable backend model-variant/reasoning-setting attestation is not exposed here, so the requested exact “Astra / HIGH” configuration is not independently verified. No sub-agents or other reviewers were used.
- **Tool/scope disclosure:** The unqualified `python` command was unavailable; calculations/report edits used `/usr/bin/python3`. One Execution Plan location search returned adjacent boundary context (the previous output path and the beginning of the next entry); no adjacent chunk was examined or used as evidence. Subsequent work stayed within Chunk 06 and the logged bounded references. Current primary files contain historical lesson/audit references; those sections were read to satisfy full-file coverage, but their prior conclusions were not used to establish findings. No prohibited report or disposition was opened.

## 11. COVERAGE MANIFEST

### Primary sources — complete coverage

Inventory obtained with `rg --files 05_DESIGN_SYSTEM`; six substantive Markdown files, **3,754 lines** total. All were read completely with line-numbered output; no primary read was truncated.

| Primary file | Status | Complete read coverage |
|---|---|---|
| `05_DESIGN_SYSTEM/GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` | EXAMINED | 1–164; authority, tokens, artifacts, approval, mobile, accessibility |
| `05_DESIGN_SYSTEM/TOKEN_FILE.md` | EXAMINED | 1–235; every CSS/config/font snippet and note; independently computed contrast |
| `05_DESIGN_SYSTEM/THEME_LIBRARY.md` | EXAMINED | 1–133; all modes, tenant rules, process and references |
| `05_DESIGN_SYSTEM/THEMING_MANUAL.md` | EXAMINED | 1–302; all setup, handoff, quick-swap, checklist and authority text |
| `05_DESIGN_SYSTEM/COMPONENT_REGISTRY.md` | EXAMINED | 1–400, 401–793; all primitive APIs, examples, mobile tables and KIP rules |
| `05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` | EXAMINED | 1–420, 421–900, 901–1360, 1361–1760, 1761–2127; all rules, examples, templates, checklists, appendices and history |

### Bounded supporting doctrine reads

Search results were used only to locate/verify the listed dependencies. Some broad heading/keyword output was truncated; it was **not treated as complete examination**. Full decisive excerpts were subsequently read as listed. Supporting files did not become primary scope.

| Supporting file | Status / portions consulted | Why necessary |
|---|---|---|
| `02_PIPELINE_AGENTS/DESIGNER_PLAYBOOK.md` | CROSS-REFERENCE — heading/artifact/approval searches; lines 31–101, 136–185, 217–327, 374–386 | Verify producer, human ownership, screen locks, UI_SPEC, full package, mobile exception and conflict rule |
| `02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md` | CROSS-REFERENCE — input/architecture/track searches; lines 126–189, 237–278, 987–1047 | Verify package consumer, stop conditions, conversion provenance, kit audit, DATA_CONTRACT owner and nonvisual tracks |
| `03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md` | CROSS-REFERENCE — heading/gate/visual searches; lines 419–464 | Verify fidelity versus functional completion, Gate M, independent Gate Q/D connection |
| `03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md` | CROSS-REFERENCE — heading/service/page searches; lines 18–37, 84–117, 139–154, 324–370 | Verify primary references to pre-authoring kit reuse, data prerequisites, service boundaries and co-location |
| `04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md` | CROSS-REFERENCE — heading/rendering/state/service searches; lines 523–591, 649–715, 785–823, 1340–1372 | Verify thin-page versus server/client responsibilities and client state placement; flag unresolved competing examples |
| `03_BUILD_METHODOLOGY/QA_PLAYBOOK.md` | CROSS-REFERENCE — Gate Q/visual/evidence searches; lines 22–40, 684–776 | Verify independent QA authority and actual required UI checks; verify current gate headings |
| `01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md` | CROSS-REFERENCE — pipeline/design searches; lines 40–60 | Verify constitutional greenfield/conversion routing and design provenance |
| `01_CONSTITUTION/STARTER_KIT_HANDBOOK.md` | CROSS-REFERENCE — theme/shell/target searches; lines 276–297, 429–450, 578–589, 649–659 | Verify kit rail fit, mobile primitive ownership, target-floor mechanism and existing theme-controller ownership; expose migration dependency |
| `03_BUILD_METHODOLOGY/TESTING_PLAYBOOK.md` | CROSS-REFERENCE — heading index and targeted visual/screenshot/viewport/fidelity/accessibility/contrast searches only | Check whether the explicitly referenced testing owner provided a discoverable visual-evidence contract; no substantive neighboring testing-domain review |

**Path-only checks:** The four unresolved links listed in D11 were checked for existence, without opening any substitute prior review or project artifact. Filename discovery for the named supporting authorities did not read other-domain doctrine bodies.

### Examination controls

- `astra-review/run-002/packets/CHUNK_REVIEW_CONTRACT.md` — read completely; governing method, severity, independence, write boundary and report format.
- `astra-review/run-002/packets/EXECUTION_PLAN.md` — Chunk 06 definition (lines 388–442) consulted for primary scope, permitted dependencies and output. Incidental search-boundary disclosure is recorded in §10.
- Branch, status and applicable `AGENTS.md` discovery were read-only. No applicable AGENTS file was found in repository discovery or ancestor checks.

### External technical references — bounded verification only

- [W3C contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — verify the numerical AA threshold and underlying-color computation used in D03; no external product/design recommendation imported.
- [Tailwind v3 dynamic class discovery](https://v3.tailwindcss.com/docs/content-configuration#dynamic-class-names) — verify D10 against the template's expressly supported Tailwind major.
- [Tailwind v3 CSS-variable color mapping](https://v3.tailwindcss.com/docs/customizing-colors#using-css-variables) — check and reject the suspected need for an explicit alpha placeholder; no defect raised.

No prior Astra chunk report, Sol/Fable review, disposition, Run 001 review finding, or synthesis artifact was consulted. Embedded history in assigned current doctrine was not treated as independent review evidence.

## 12. SYNTHESIS HANDOFF

- **Strongest conclusion:** The core design-to-implementation system is recognizable and substantially specified, but the current positive examples and side-path checklists are not a consistently executable expression of it. Preserve the system; reconcile its concrete instructions.
- **Most serious defect:** C06-D03 — the drop-in palette fails its stated small-text AA requirement despite claimed verification. C06-D02 and C06-D01 are the other high-priority operational failures.
- **Most important strength:** The token-driven, human-locked HTML/PNG + UI_SPEC + manifest package is compatible with the main Engineer consumer, and downstream fidelity evidence feeds independent Gate Q rather than replacing it.
- **Unresolved issue most likely to affect another domain:** The permitted server-fetching/thin-page boundary and the authority for modifying kit behavior; see §9. Do not settle those from this chunk alone.
- **Findings deserving later cross-Factory consideration:** D01 producer/consumer side-path drift, D04 kit-specific breakpoint authority, D05 duplicated canonical token requirements, and D08 copyable primitive replacement. Carry evidence forward without inferring a Factory-wide score.

This section supplies a bounded handoff only. No synthesis, disposition, doctrine repair, or Chunk 07 work was performed.
