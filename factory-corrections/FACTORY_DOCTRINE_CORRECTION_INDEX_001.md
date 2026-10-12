# Factory Doctrine Correction Package 001 — Index

> **DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC**

| Field | Value |
|---|---|
| Package | Factory Doctrine Correction Package 001 (intake preparation, Part 2) |
| Prepared by | Claudy (documentation Engineer seat), 2026-10-11 |
| Starting state | branch `factory-docs-review-astra-w-chunks` at HEAD `c6210c32480558b343a27726a26822e8d959d0f7` · main = origin/main = `9c179392f79b70da099121fc357d3107ad3bb86e` (0/0) |
| Certified basis | `astra-review/run-002/synthesis/PART1_FINDINGS_DISPOSITION.md` at `c6210c3`, with QA verdict **PASS** (QA-1…QA-8; 0 findings) in `astra-review/run-002/synthesis/QA/PART1_CONVERGENCE_QA.md` |
| Status | **DRAFT.** Not approved and not certified. Not DocSet Sync cargo until Tony approves it. |
| Seats | Jarvis/Sol: Architect review · Tony: Director approval · Claudy: Engineer (author; cannot certify) |

**What this package is.** It converts the 97 certified Part 1 findings (FCs) in 17 Correction Families (CFs) into a reviewable correction intake. For each finding it gives:
- what the correction must achieve (a **PROPOSED** outcome);
- what it must preserve;
- what it likely touches;
- how it can be verified;
- which Architect or Director decisions it waits on.

**What this package is not.**
- It is not approved policy. Every outcome is labeled PROPOSED; recommendations are marked as recommendations.
- It contains no replacement doctrine text, and no canonical doctrine, MANIFEST, CHANGELOG or skill file was edited.
- It is not a DocSet Sync UPDATE MAP. Placements and wording are DocSet Sync's job after approval (D17).
- It is not QA or certification.
- These are documentation findings about Factory doctrine text. **They are not proof that any client application has these flaws.** The reviewers examined doctrine, not deployed apps, installed triggers, live policies or kit source.

---

## 1. Package contents

| File | Primary entries | Register section |
|---|---:|---|
| `FACTORY_DOCTRINE_CORRECTION_INDEX_001.md` | (index; cross-references only) | — |
| `01_governance_corrections.md` | 12 (FC-001 … FC-012) | §5.A |
| `02_agents_handoffs_corrections.md` | 7 (FC-013 … FC-019) | §5.B |
| `03_build_method_corrections.md` | 13 (FC-020 … FC-032) | §5.C |
| `04_auth_data_security_corrections.md` | 17 (FC-033 … FC-049) | §5.D |
| `05_api_commerce_corrections.md` | 21 (FC-050 … FC-070) | §5.E |
| `06_design_frontend_corrections.md` | 14 (FC-071 … FC-084) | §5.F |
| `07_skills_doc_governance_corrections.md` | 13 (FC-085 … FC-097) | §5.G |
| **Total** | **97** | |

## 2. Pinned sources

| Source | Revision | Path / ref |
|---|---|---|
| Certified register (authoritative Pass 2) | `c6210c3` | `astra-review/run-002/synthesis/PART1_FINDINGS_DISPOSITION.md` |
| Certified QA | `c6210c3` | `astra-review/run-002/synthesis/QA/PART1_CONVERGENCE_QA.md` |
| Astra reviews, chunks 01–07 | `c6210c3` | `astra-review/run-002/chunks/0N_*/ASTRA_REVIEW.md` |
| Sol reviews, chunks 01–07 | `c6210c3` | `astra-review/run-002/chunks/0N_*/SOL_REVIEW.md` |
| Fable blind review | `origin/factory-docs-review-fable-001` = `39a1c6114d72b22d3550d7ff65234ec0f01418f6`; blob `55dd3e92bf466b1873b724c501a8bf5660737456` | `fable-review/run-001/reviews/FABLE_FACTORY_DOCTRINE_REVIEW_001.md` (read with `git show`) |
| Review baseline (defect surfaces) | `0a787cb826118b4a010765d60e41a449df3ce746` | doctrine paths per entry |
| Current main (status) | `9c179392f79b70da099121fc357d3107ad3bb86e` | for the 81 OPEN — SOURCE UNCHANGED FCs, every cited surface is blob-identical to the baseline (QA-4) |
| DocSet Sync (intake fit) | `9c17939` | `_SKILLS/factory-docs-update/CLAUDE.md`, `_SKILLS/factory-docs-update/README.md` (read with `git show`; the skill was not activated) |

Excluded on purpose (as in Part 1): `SOL_REVIEW_OF_FABLE_001.md`, the Fable and Astra `FINAL_DISPOSITION.md`, the Astra synthesis files and the empty chunk-level placeholders.

## 3. How to read the package

- **Correction ID = certified FC ID** (`FC-001` … `FC-097`). FC numbers, reviewer-ID mappings, severities, review statuses, current-main statuses and correction-required values are copied from the certified register. They are not re-derived and not renumbered. The validator in §13 checks them mechanically.
- **The CF is the planning unit.** Per the register's §0, the 97 FCs are atomic records, not 97 programs; repair planning happens per Correction Family. Every entry names its CF, and §6 gives the family view.
- **Primary entry rule.** Each FC has exactly one primary entry, in the brief that matches its certified register §5 subsection (§5.A → `01_…` … §5.G → `07_…`). Cross-references between briefs and from this index are allowed and are not primary entries.
- **Fields per primary entry:**
  - certified record and reviewer source IDs;
  - evidence pointers (Astra/Sol section, Fable section);
  - defect surfaces, with paths at the pinned revision;
  - the defect and its certified current-main status;
  - **Proposed outcome (PROPOSED — not approved)**;
  - **Preserve** (invariants);
  - likely affected docs and consumers;
  - **Verification intent**;
  - open decision;
  - proposed route.
- **Verification intent is input, not acceptance criteria.** Under DocSet Sync D20, Sol derives the acceptance spec from the approved package and map. These intents are written to make that derivation possible; they are not the ACs.
- **Route codes (PROPOSED):**

  | Code | Target | Owner of the change |
  |---|---|---|
  | `SYNC` | five tier folders, `MANIFEST.md`, `CHANGELOG.md`, `_ARCHIVE/` | DocSet Sync run (Claudy), after approval |
  | `XB-SKILL` | `_SKILLS/**` (including the docs-update family itself) | separate Skills Playbook authoring job; DocSet Sync §1 declines it |
  | `XB-LINT/CI` | `lints/`, `.github/` | separate approved job (DocSet Sync §1, D21) |
  | `XB-ROOT` | root `CLAUDE.md` (outside the synchronized DocSet) | separate approved job; gated by DEC-08 |
  | `XB-EXT` | other repositories (starter kit, project repos, off-Hub skills) | external verification or change; Hub records the result |

## 4. Certified totals (preserved)

| Measure | Certified | In this package |
|---|---:|---:|
| FC records | 97 | 97 primary entries, 97 unique |
| Astra defect IDs mapped (primary) | 81 / 81 | carried in "Reviewer source IDs" |
| Fable defect IDs mapped (primary) | 31 / 31 | carried in "Reviewer source IDs" |
| Correction Families | 17 | 17 |
| BLOCKER / HIGH / MEDIUM / LOW | 6 / 36 / 44 / 11 | 6 / 36 / 44 / 11 |
| OPEN — SOURCE UNCHANGED | 81 | 81 |
| OPEN — DEFECT REMAINS | 8 | 8 |
| PARTIALLY REMEDIATED | 5 | 5 |
| REMEDIATED — CURRENT MAIN | 3 | 3 (FC-085, FC-086, FC-097) |
| CORRECTION REQUIRED YES / NO / VERIFY | 94 / 3 / 0 | 94 corrections · 3 "NO NEW CORRECTION" regression guards |
| Suggestions (not defects) | 21 Astra + 14 Fable | §11, optional backlog only |

Review-status mix (certified): CONFIRMED 12 · PARTIAL 7 · UNIQUE (Astra) 62 · UNIQUE (Fable) 13 · CONFLICT 3. The three CONFLICT records (FC-005, FC-070, FC-096) carry Sol's certified ACCEPT DEFECT adjudication verbatim in their entries.

---

## 5. BLOCKER priority (6 of 97)

All six are **OPEN — SOURCE UNCHANGED** on current main.

| # | FC | Certified title | CF | Brief | Coupled items (same correction surface) | Gating decisions |
|---|---|---|---|---|---|---|
| 1 | FC-033 | AUTH_MANUAL privileged recipes authorize from `user_metadata`, recreate competing role stores and supply an app-side superadmin-creation surface | CF-06 | 04 | FC-035, FC-038, FC-041, FC-001 (governance twin; kept separate per Sol C01 §5.A) | DEC-02 |
| 2 | FC-034 | Public signup forwards caller-controlled role metadata into the role-creation trigger path | CF-06 | 04 | FC-033 (role authority) | DEC-02 |
| 3 | FC-036 | Layout admission is presented as the authorization boundary for privileged server actions | CF-06 | 04 | FC-038, FC-057 (same seam) | DEC-04 |
| 4 | FC-050 | Public order-status mutation accepts the caller's assertion that payment succeeded | CF-08 | 05 | FC-051, FC-054, FC-063 | DEC-04, DEC-05 |
| 5 | FC-051 | PaymentIntent amount is computed from client-supplied prices, shipping and discount despite "never trust client" | CF-08 | 05 | FC-060, FC-067, FC-021 | DEC-05 |
| 6 | FC-020 | TESTING webhook recipe acknowledges success unconditionally, without durable processing or recovery | CF-05 | 03 | FC-052 (same mechanism in ECOM/STRIPE), FC-059, FC-062 | DEC-03 |

**Recommendation (PROPOSED): containment before rewrite.** For each BLOCKER, the first correction removes or quarantines the unsafe copyable recipe and points to the governing rule that already exists (the role table, server quote authority, the operation-local authorization principle, the acknowledgment contract). A full rewrite against the verified kit or payment architecture can follow in a later wave. This shrinks the window in which agents can copy the unsafe recipe without waiting on external verification (the kit repository is outside this package). Choosing containment vs immediate rewrite is DEC-02 (Tony).

**Severity note.** The package keeps every certified severity. Sol's conditional re-elevations are recorded in their entries and parked under DEC-22: FC-037 (BLOCKER on private data), FC-052 (BLOCKER candidate), FC-061 (HIGH when material), FC-002 (HIGH if the checklist is the de-facto gate). None is applied.

## 6. Proposed delivery waves (PROPOSED; for Tony's sequencing decision)

DocSet Sync routes each run TINY or LARGE from evidence (D3). Every wave below touches several documents, so each is expected to be a LARGE run with Sol's acceptance spec and Cody's QA.

| Wave | Content | Prerequisites |
|---|---|---|
| 0 | Decisions DEC-01 … DEC-05 (§9) | none |
| 1 — BLOCKER containment | FC-033, FC-034, FC-036, FC-050, FC-051, FC-020, with tightly coupled FC-035, FC-038, FC-060, FC-052 | DEC-01–05 |
| 1b — optional early hygiene | Lint stragglers outside STARTER_KIT (FC-096: DATABASE ×2, UI_UX ×1), MANIFEST recompute (FC-093 + FC-087) | DEC-16 (lint policy) |
| 2 — security / integrity remainder | Rest of CF-05, CF-06, CF-07, CF-08, CF-09, CF-10 | Wave 1; DEC-09, DEC-15 |
| 3 — governance foundation and artifact contracts | CF-01, CF-02, CF-03, CF-04, CF-14 (FC-011, FC-012) | DEC-06, DEC-07, DEC-10–14, DEC-18 |
| 4 — design tier | CF-11, CF-12, and the design CF-13 items (FC-081, FC-083, FC-084) | DEC-06 (FC-073), DEC-09 (FC-072) |
| 5 — Hub hygiene and distribution | Remaining CF-13 (FC-003, FC-009, FC-032, FC-070), FC-088, FC-089 | DEC-17, DEC-19, DEC-20 |
| XB track (parallel, separate jobs) | CF-17 + FC-090/091/094 (root CLAUDE.md); FC-092/095 and the skill wording in FC-005/006/096 (docs-update family); FC-096 lint/CI part; `XB-EXT` kit verifications (FC-041, FC-042, FC-072) | DEC-08, DEC-21 |

**STARTER_KIT_HANDBOOK note.** This doc has a ←12 blast radius, and DocSet Sync D22 allows one version bump per doc per unmerged run. Wave 1 touches Handbook §§1–2 (FC-034/FC-036), so consider landing FC-003 (the F-022 redo, 6 of the 9 lint findings) in the same run to avoid a second bump of the highest-blast-radius doc.

---

## 7. Correction Families

### 7.1 Certified family layer (generated from the briefs; matches register §5A.1)

| CF | Family (certified name) | Members | # | B/H/M/L | Current-main | YES | Primary brief(s) |
|---|---|---|---:|---|---|---:|---|
| CF-01 | Constitution / roles / precedence / lifecycle | FC-001, FC-002, FC-004, FC-005, FC-006, FC-007 | 6 | 0/2/4/0 | 4 unchanged · 2 defect remains | 6 | 01 |
| CF-02 | Artifact / handoff / template contracts | FC-008, FC-013, FC-015, FC-016, FC-017, FC-018, FC-019, FC-027 | 8 | 0/4/4/0 | 8 unchanged | 8 | 01, 02, 03 |
| CF-03 | Recon / planning / scope-authority boundaries | FC-014, FC-023, FC-029 | 3 | 0/1/2/0 | 3 unchanged | 3 | 02, 03 |
| CF-04 | FFM / module acceptance and freeze mechanics | FC-025, FC-026, FC-028 | 3 | 0/2/1/0 | 3 unchanged | 3 | 03 |
| CF-05 | Testing / evidence / environment fidelity | FC-020, FC-021, FC-022, FC-024, FC-030, FC-031, FC-063 | 7 | 1/3/3/0 | 7 unchanged | 7 | 03, 05 |
| CF-06 | Auth / authorization / session authority | FC-033, FC-034, FC-035, FC-036, FC-038, FC-041, FC-042, FC-043, FC-044 | 9 | 3/5/1/0 | 9 unchanged | 9 | 04 |
| CF-07 | Data / RLS / state correctness and privacy | FC-037, FC-039, FC-040, FC-045, FC-046, FC-047, FC-048, FC-049, FC-068, FC-069 | 10 | 0/3/5/2 | 10 unchanged | 10 | 04, 05 |
| CF-08 | Commerce money authority / checkout contract | FC-050, FC-051, FC-060, FC-067 | 4 | 2/1/1/0 | 4 unchanged | 4 | 05 |
| CF-09 | Webhook / event durability, idempotency and ordering | FC-052, FC-053, FC-054, FC-055, FC-056, FC-059, FC-062, FC-065 | 8 | 0/6/2/0 | 8 unchanged | 8 | 05 |
| CF-10 | API trust boundaries / integration / failure semantics | FC-057, FC-058, FC-061, FC-064, FC-066 | 5 | 0/2/3/0 | 5 unchanged | 5 | 05 |
| CF-11 | Design rule/example drift and responsive consistency | FC-071, FC-072, FC-073, FC-075, FC-077, FC-078, FC-082 | 7 | 0/2/4/1 | 7 unchanged | 7 | 06 |
| CF-12 | Frontend accessibility / component implementation | FC-074, FC-076, FC-079, FC-080 | 4 | 0/1/3/0 | 4 unchanged | 4 | 06 |
| CF-13 | Cross-reference / locator / document-structure hygiene | FC-003, FC-009, FC-032, FC-070, FC-081, FC-083, FC-084 | 7 | 0/0/2/5 | 6 unchanged · 1 defect remains | 7 | 01, 03, 05, 06 |
| CF-14 | Deployment / Git authority / doctrine distribution | FC-011, FC-012, FC-088 | 3 | 0/0/3/0 | 2 partial · 1 unchanged | 3 | 01, 07 |
| CF-15 | Hub sync / recovery / write-boundary mechanics | FC-085, FC-086, FC-087, FC-090, FC-091, FC-092, FC-095, FC-097 | 8 | 0/3/3/2 | 3 remediated · 3 partial · 2 defect remains | 5 | 07 |
| CF-16 | Hub index / archive / changelog / lint controls | FC-089, FC-093, FC-094, FC-096 | 4 | 0/1/2/1 | 2 defect remains · 2 unchanged | 4 | 07 |
| CF-17 | Root CLAUDE / governed-instruction status | FC-010 | 1 | 0/0/1/0 | 1 defect remains | 1 | 01 |

### 7.2 Family-level outcomes and invariants (PROPOSED)

| CF | Family outcome: what must become true (PROPOSED) | Invariants to preserve | Key decisions |
|---|---|---|---|
| CF-01 | The constitution matches the module era. It has one reconciliation (precedence) rule, one seat glossary and one lifecycle crosswalk; its checklists carry the governing gates by link; its kit-based examples defer to kit authority. | SFP §2.5 separation of acceptance authorship / QA verdict / Operator release; recon gate; conversion/greenfield routing; Operator final authority | DEC-06, DEC-07, DEC-02 |
| CF-02 | Each planning artifact has one template, one status vocabulary, a named producer and consumer, and an approval step at a defined time. The Engineer→QA interface is explicit. Visual artifacts are conditional on interface type. | Human approval; pipeline-specific authorship; recipient-side rejection; uncertainty labels | DEC-10, DEC-11, DEC-12, DEC-13 |
| CF-03 | Approval precedes action. Recon has an explicit write/diagnostic boundary. One artifact holds scope authority. | Recon read-only gate; stop-and-escalate; urgent security escalation | DEC-14 |
| CF-04 | FFM carries the ACCEPTANCE_SPEC lifecycle and QA handoff. The module freeze separates immutable inputs from authorized outputs. FFM consumes kit auth directly. | Freeze purpose; exact-filename rule; Kit Exception | DEC-13 |
| CF-05 | Test recipes prove the behavior they claim, keep sensitive data out of logs, mutate only approved test targets, label reduced coverage and include API negative cases. | TESTING truth principles (1.3, 1.4, 1.10), `retries: 0`, defensive assertions; QA one-test-at-a-time and final reset | DEC-03 |
| CF-06 | One role authority (the role table). Server-resolved identity. Every privileged operation authorizes its own invocation. One guard contract, one session/cookie architecture, safe redirects, truthful logout. | Console-only superadmin; Navbar Law and the first-render invariant; AUTH-WALK; narrow creation-time transport exception | DEC-02, DEC-04, DEC-09 |
| CF-07 | RLS recipes compose safely. Multi-step persistence has recovery. Persisted personal data has an account-transition lifecycle. State recipes obey their own invariants. One store shape and one env-name table. | Default-deny RLS; schema-first; selective persistence; "verify env names on disk" | DEC-15 |
| CF-08 | Payment truth comes only from verified server evidence bound to an authoritative server quote. One checkout contract. Coupon logic is line-item aware. | "Never trust client" principle; server-held credentials; raw-body verification | DEC-04, DEC-05 |
| CF-09 | Webhook success means durable completion or durable acceptance. Creation is idempotent, application converges in order, dedup is atomic. Handlers are complete or explicitly incomplete. UI confirmation is honest. | Signature-first verification; Stripe truth vs mirror separation; restricted subscription write boundary | DEC-03 |
| CF-10 | Privileged endpoints authorize their own invocation on non-safe methods. Webhook verification runs on raw bytes with one scheme. Secrets fail closed. Error contracts are typed. Service signatures are consistent. | Secrets server-only; wire vs UI types; BIM §7 per-module failure policy | DEC-04 |
| CF-11 | Positive examples obey Rule Zero / Zero-B. One rail-breakpoint rule. Theming defers to the full HTML/PNG deliverable contract. One token inventory, one theme controller, defined contained scrolling. | Sol C06 preservation list (semantic tokens, human locks, mobile reachability, kit reuse, HTML build reference, PNG fidelity target, QA separation) | DEC-06, DEC-09 |
| CF-12 | Tokens meet AA, with computed evidence behind any "verified" claim. The Button recipe matches the kit API and the 44px floor. The Grid uses discoverable classes. | Passing palette pairs; per-mode tuning; kit reuse | — |
| CF-13 | Every doctrine reference resolves (path or anchor) or is labeled external with repository and revision. One Quick Reference per manual. Load-bearing external artifacts are located. | Canonical names; Hub law (D15); doctrine vs app-source path distinction | DEC-17, DEC-19 |
| CF-14 | A governed deployment doctrine, a context × action × seat authority matrix, and a release/consumption procedure with a named owner. | DocSet Sync D5 bounded carve-out; module git-zero / cloud-zero; Tony owns tags and merges | DEC-17, DEC-18 |
| CF-15 | MANIFEST's ← map is scoped as a starting set. Root CLAUDE.md has a pre-approval run-state surface and evidence-first recovery. The skill close-out stays inside its write boundary. CI wording is accurate. Three items are already remediated: regression guard only. | D2 / D10 / D15a / D18 / D19 / D21 as on main | DEC-08, DEC-16, DEC-21 |
| CF-16 | MANIFEST counts and edges are true. The missing archive is reconciled. One CHANGELOG format. CI is a gate with honest baseline handling. | Archive discipline; honest lint reporting; no exemption masking | DEC-16, DEC-20 |
| CF-17 | Root CLAUDE.md is either governed doctrine (MANIFEST + lint scope) or tool configuration that points into the Hub. Plan Mode is defined once. | Crash-recovery bookkeeping; Plan Mode intent | DEC-08 |

---

## 8. Master register (generated from the briefs; every row verified against the certified register)

| FC | Title (certified) | CF | Severity | Review status | Current-main | Corr. | Proposed route | Primary brief |
|---|---|---|---|---|---|---|---|---|
| FC-001 | Constitutional kit-build instructions (SFP §9 Phase 7, §8 page pattern) conflict with kit-consumption doctrine | CF-01 | HIGH | CONFIRMED | OPEN — SOURCE UNCHANGED | YES | SYNC | `01_governance_corrections.md` |
| FC-002 | Constitutional feature/release checklists omit required approval, acceptance and Gate Q checkpoints | CF-01 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `01_governance_corrections.md` |
| FC-003 | STARTER_KIT_HANDBOOK references and conventions do not resolve against, or conform to, Hub conventions | CF-13 | MEDIUM | PARTIAL | OPEN — SOURCE UNCHANGED | YES | SYNC | `01_governance_corrections.md` |
| FC-004 | The constitution (Blueprint) predates the QA seat and the module era | CF-01 | HIGH | UNIQUE (Fable) | OPEN — SOURCE UNCHANGED | YES | SYNC | `01_governance_corrections.md` |
| FC-005 | No Factory-wide precedence rule; individual docs each declare themselves the winner | CF-01 | MEDIUM | CONFLICT | OPEN — DEFECT REMAINS | YES | SYNC + XB-SKILL | `01_governance_corrections.md` |
| FC-006 | Seat vocabulary not normalized; "Architect" names both the human and an AI agent | CF-01 | MEDIUM | UNIQUE (Fable) | OPEN — DEFECT REMAINS | YES | SYNC + XB-SKILL | `01_governance_corrections.md` |
| FC-007 | Lifecycle / execution-stage vocabularies lack a unifying map or crosswalk | CF-01 | MEDIUM | PARTIAL | OPEN — SOURCE UNCHANGED | YES | SYNC | `01_governance_corrections.md` |
| FC-008 | `FILE_TREE.md` is required by the Blueprint and root CLAUDE.md but no workflow produces it | CF-02 | MEDIUM | UNIQUE (Fable) | OPEN — SOURCE UNCHANGED | YES | SYNC + XB-ROOT | `01_governance_corrections.md` |
| FC-009 | Load-bearing external artifacts (skills, worked examples, issue logs) are referenced but never located | CF-13 | MEDIUM | UNIQUE (Fable) | OPEN — DEFECT REMAINS | YES | SYNC + XB-EXT | `01_governance_corrections.md` |
| FC-010 | "Plan Mode" and root CLAUDE.md are load-bearing but sit outside the governed doc set | CF-17 | MEDIUM | UNIQUE (Fable) | OPEN — DEFECT REMAINS | YES | XB-ROOT + SYNC | `01_governance_corrections.md` |
| FC-011 | Deployment, promotion and rollback have gates and checklists but no owning doctrine | CF-14 | MEDIUM | UNIQUE (Fable) | OPEN — SOURCE UNCHANGED | YES | SYNC | `01_governance_corrections.md` |
| FC-012 | Git/cloud authority differs between FFM-era and module-era doctrine without a reconciling rule | CF-14 | MEDIUM | UNIQUE (Fable) | PARTIALLY REMEDIATED | YES | SYNC | `01_governance_corrections.md` |
| FC-013 | Engineer-side completion/handoff doctrine does not carry the QA intake interface | CF-02 | HIGH | PARTIAL | OPEN — SOURCE UNCHANGED | YES | SYNC | `02_agents_handoffs_corrections.md` |
| FC-014 | Recon's operation boundary contradicts its own procedure and required output | CF-03 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC + XB-EXT | `02_agents_handoffs_corrections.md` |
| FC-015 | Greenfield engineering-spec approval has no execution checkpoint before implementation | CF-02 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `02_agents_handoffs_corrections.md` |
| FC-016 | Artifact status vocabularies disagree between producer templates and receiving gates (LOCKED vs APPROVED) | CF-02 | MEDIUM | CONFIRMED | OPEN — SOURCE UNCHANGED | YES | SYNC | `02_agents_handoffs_corrections.md` |
| FC-017 | Architect-seat responsibility (including the greenfield UI_SPEC draft) is assigned differently across docs | CF-02 | MEDIUM | PARTIAL | OPEN — SOURCE UNCHANGED | YES | SYNC | `02_agents_handoffs_corrections.md` |
| FC-018 | Mandatory visual intake has no valid path for a supported nonvisual build | CF-02 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `02_agents_handoffs_corrections.md` |
| FC-019 | Multiple incompatible APP_BRIEF and UI_SPEC templates coexist under a single-source claim | CF-02 | HIGH | UNIQUE (Fable) | OPEN — SOURCE UNCHANGED | YES | SYNC | `02_agents_handoffs_corrections.md` |
| FC-020 | TESTING webhook recipe acknowledges success unconditionally, without durable processing or recovery | CF-05 | BLOCKER | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-021 | Payment-error recipe moves sensitive error content into server logs | CF-05 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-022 | Mutating E2E helpers lack an enforced test-environment boundary | CF-05 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-023 | Local exceptions permit implementation before scope approval | CF-03 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-024 | E2E workaround recipe can remove a shipped failure from the system under test | CF-05 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-025 | FFM (and combined-artifact allowances) omit the mandatory `ACCEPTANCE_SPEC.md` lifecycle and QA handoff | CF-04 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-026 | Whole-folder module freeze conflicts with required in-folder working artifacts | CF-04 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-027 | Greenfield DATA_CONTRACT authorship and timing are not executable as written | CF-02 | HIGH | PARTIAL | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-028 | FFM prescribes the auth-service wrapper that kit-consumption doctrine forbids | CF-04 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-029 | FFM gives two different documents final scope authority | CF-03 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC + XB-EXT | `03_build_method_corrections.md` |
| FC-030 | Fixture discovery can publish unusable roles, and its consumer reads a different count field | CF-05 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-031 | Metadata helper cannot distinguish an absent key from a present null | CF-05 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-032 | FRONTEND_BUILD_PHASE checklist points Gate Q / Gate D to the wrong QA_PLAYBOOK sections | CF-13 | LOW | CONFIRMED | OPEN — SOURCE UNCHANGED | YES | SYNC | `03_build_method_corrections.md` |
| FC-033 | AUTH_MANUAL privileged recipes authorize from `user_metadata`, recreate competing role stores and supply an app-side superadmin-creation surface | CF-06 | BLOCKER | CONFIRMED | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-034 | Public signup forwards caller-controlled role metadata into the role-creation trigger path | CF-06 | BLOCKER | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-035 | Active client-side recipes claim route and identity authority (HOC, post-mount Navbar, persisted auth store) | CF-06 | HIGH | CONFIRMED | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-036 | Layout admission is presented as the authorization boundary for privileged server actions | CF-06 | BLOCKER | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-037 | Soft-delete RLS policy is an access grant, not a safely composing exclusion | CF-07 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-038 | Client-capability guidance both underpowers admin calls and overgeneralizes RLS bypass | CF-06 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-039 | Multi-step persistence recipes leave compensation failures unrecoverable | CF-07 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-040 | Persisted personal data has no enforceable account-transition lifecycle | CF-07 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-041 | The canonical `protectPage` recipe's call and return contract is incompatible with its documented callers | CF-06 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC + XB-EXT | `04_auth_data_security_corrections.md` |
| FC-042 | Cookie `httpOnly` guidance contradicts the kit session model | CF-06 | HIGH | CONFIRMED | OPEN — SOURCE UNCHANGED | YES | SYNC + XB-EXT | `04_auth_data_security_corrections.md` |
| FC-043 | Email confirmation route accepts an unbounded external redirect destination | CF-06 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-044 | Logout reports success without checking the sign-out result | CF-06 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-045 | Timestamp-only cursor pagination silently skips tied records | CF-07 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-046 | Alternative hydration hook changes the hook invocation count | CF-07 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-047 | Persistence readiness can become permanently false after a reset or storage failure | CF-07 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-048 | A nonempty client store permanently overrides new server data | CF-07 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-049 | Composite-item update mutates the previous state snapshot | CF-07 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `04_auth_data_security_corrections.md` |
| FC-050 | Public order-status mutation accepts the caller's assertion that payment succeeded | CF-08 | BLOCKER | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-051 | PaymentIntent amount is computed from client-supplied prices, shipping and discount despite "never trust client" | CF-08 | BLOCKER | CONFIRMED | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-052 | Commerce and subscription webhook acknowledgment conceals failed business persistence | CF-09 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-053 | Checkout creation lacks the retry and concurrency identity its invariants require | CF-09 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-054 | Event handlers can regress newer commerce or subscription state | CF-09 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-055 | Subscription bootstrap and resubscribe writes conflict with the prescribed schema | CF-09 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-056 | Webhook deduplication neither excludes concurrent execution nor identifies events reliably | CF-09 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-057 | Manual sync exposes a privileged mutation as an unprotected GET | CF-10 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-058 | Generic webhook verification signs reconstructed JSON and chains supposedly alternative schemes | CF-10 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-059 | Required webhook follow-up has no durable acceptance or recovery boundary | CF-09 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-060 | The displayed checkout caller cannot satisfy its order endpoint contract | CF-08 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-061 | Revalidation secret comparison fails open when the environment variable is absent | CF-10 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-062 | Refund and dispute events are advertised but acknowledged without their required work | CF-09 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-063 | Local validation recipes do not require API trust-boundary or event-failure negative cases | CF-05 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-064 | Service error-handling doctrine collapses or propagates dependency failures inconsistently with testing and module failure-policy doctrine | CF-10 | MEDIUM | PARTIAL | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-065 | Success polling can confirm an old tier and claims receipt of unverified payment | CF-09 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-066 | API examples assign incompatible signatures and representations to the same service contracts | CF-10 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-067 | The per-product coupon calculator has no line-item information and applies one flat discount | CF-08 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-068 | ECOMMERCE defers to a checkout store the STATE manual does not define | CF-07 | LOW | UNIQUE (Fable) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-069 | Supabase secret environment-variable names differ across manuals | CF-07 | LOW | UNIQUE (Fable) | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-070 | API_AND_SERVICES_MANUAL has two "§10 Quick Reference" sections | CF-13 | LOW | CONFLICT | OPEN — SOURCE UNCHANGED | YES | SYNC | `05_api_commerce_corrections.md` |
| FC-071 | Copyable portal and sidebar layouts hide navigation on mobile, contrary to Rule Zero, and bypass the kit shell | CF-11 | HIGH | CONFIRMED | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-072 | Rail breakpoint rules disagree across the design tier and kit docs | CF-11 | MEDIUM | CONFIRMED | OPEN — SOURCE UNCHANGED | YES | SYNC + XB-EXT | `06_design_frontend_corrections.md` |
| FC-073 | Positive examples present numbered Tailwind colors as convention while Rule Zero-B calls them automatic failures | CF-11 | MEDIUM | CONFIRMED | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-074 | The drop-in token palette fails its own AA contrast claim | CF-12 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-075 | Theming handoff instructions demote required executable visual artifacts (HTML/PNG) | CF-11 | HIGH | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-076 | The replacement Button recipe breaks its advertised variant and `asChild` composition API | CF-12 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-077 | Token inventory and setup quick paths have not inherited the canonical token contract | CF-11 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-078 | The dark-mode example creates a second theme controller beside the kit's provider | CF-11 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-079 | The Button recipe violates the mandatory 44px target floor | CF-12 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-080 | The proposed Grid builds utility class names Tailwind cannot reliably discover | CF-12 | MEDIUM | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-081 | Design-tier cross-reference paths (`agent_docs/APP_FACTORY/...`) do not resolve in the DocSet | CF-13 | LOW | PARTIAL | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-082 | Blanket horizontal-scroll prohibitions conflict with prescribed tab and carousel patterns | CF-11 | LOW | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-083 | Cross-references cite section anchors that do not exist | CF-13 | LOW | UNIQUE (Fable) | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-084 | Dangling internal reference in DESIGNER_PLAYBOOK (§5.6) | CF-13 | LOW | UNIQUE (Fable) | OPEN — SOURCE UNCHANGED | YES | SYNC | `06_design_frontend_corrections.md` |
| FC-085 | Skill activation performs `git pull` before its own approval and resume safeguards | CF-15 | HIGH | UNIQUE (Astra) | REMEDIATED — CURRENT MAIN | NO | none (no correction) | `07_skills_doc_governance_corrections.md` |
| FC-086 | Phase 4 pushes before the gate that approves pushing | CF-15 | HIGH | UNIQUE (Astra) | REMEDIATED — CURRENT MAIN | NO | none (no correction) | `07_skills_doc_governance_corrections.md` |
| FC-087 | Ripple discovery omits known classes of active dependents (skills, body-only references) | CF-15 | HIGH | UNIQUE (Astra) | PARTIALLY REMEDIATED | YES | SYNC | `07_skills_doc_governance_corrections.md` |
| FC-088 | Hub→project distribution and release pinning are undefined in live doctrine | CF-14 | MEDIUM | CONFIRMED | PARTIALLY REMEDIATED | YES | SYNC | `07_skills_doc_governance_corrections.md` |
| FC-089 | The mandated outgoing QA_PLAYBOOK v1.0 archive snapshot is absent | CF-16 | MEDIUM | UNIQUE (Astra) | OPEN — DEFECT REMAINS | YES | SYNC | `07_skills_doc_governance_corrections.md` |
| FC-090 | Required pre-approval evidence writes conflict with absolute no-write rules | CF-15 | MEDIUM | UNIQUE (Astra) | PARTIALLY REMEDIATED | YES | XB-ROOT | `07_skills_doc_governance_corrections.md` |
| FC-091 | Root recovery resumes historical intent without validating its current identity | CF-15 | MEDIUM | UNIQUE (Astra) | OPEN — DEFECT REMAINS | YES | XB-ROOT | `07_skills_doc_governance_corrections.md` |
| FC-092 | Close-out requires inbox/cargo writes excluded by the skill's write boundary | CF-15 | MEDIUM | UNIQUE (Astra) | PARTIALLY REMEDIATED | YES | XB-SKILL | `07_skills_doc_governance_corrections.md` |
| FC-093 | MANIFEST's declared live-doc count and index data disagree with its own contents | CF-16 | MEDIUM | CONFIRMED | OPEN — SOURCE UNCHANGED | YES | SYNC | `07_skills_doc_governance_corrections.md` |
| FC-094 | Root CLAUDE.md prescribes a CHANGELOG record format that competes with CHANGELOG's own | CF-16 | LOW | UNIQUE (Astra) | OPEN — SOURCE UNCHANGED | YES | XB-ROOT | `07_skills_doc_governance_corrections.md` |
| FC-095 | The skill promises CI "on every push", which the workflow does not cover | CF-15 | LOW | UNIQUE (Astra) | OPEN — DEFECT REMAINS | YES | XB-SKILL + XB-LINT/CI | `07_skills_doc_governance_corrections.md` |
| FC-096 | The doctrine lint suite fails at baseline, and the documented process merges over red CI | CF-16 | HIGH | CONFLICT | OPEN — DEFECT REMAINS | YES | SYNC + XB-LINT/CI + XB-SKILL | `07_skills_doc_governance_corrections.md` |
| FC-097 | Hub skill supporting files still describe the pre-v0.3 cargo location | CF-15 | LOW | UNIQUE (Fable) | REMEDIATED — CURRENT MAIN | NO | none (no correction) | `07_skills_doc_governance_corrections.md` |

---

## 9. Decisions requiring Jarvis (Architect) or Tony (Director), prioritized

None of these is decided by this package. Where a recommendation appears it is **PROPOSED** only.

**Priority 1: gates Wave 1 (BLOCKERs)**

| ID | Decision | Owner | Affects | Recommendation (PROPOSED) |
|---|---|---|---|---|
| DEC-01 | Adopt the package structure: Correction ID = FC ID; CF as planning unit; primary brief per register §5; route codes; wave plan. Approve as DocSet Sync cargo (in whole or by wave). | Tony | all | Approve structure; release cargo per wave, starting with Wave 1. |
| DEC-02 | Legacy auth recipes: delete, quarantine as LEGACY history (archive), or rewrite against the verified kit (Fable §11 decision 1). | Tony (Jarvis advises) | FC-033, FC-035, FC-001, FC-039 (AUTH part), FC-034 | Containment first (remove/quarantine + pointer to the governing rule); rewrite later, after kit verification. |
| DEC-03 | The Factory webhook acknowledgment contract: when success may be returned, retryable-failure semantics, reconciliation owner. | Jarvis designs → Tony approves | FC-020, FC-052, FC-059, FC-062 | "Success = the required transition completed or was durably accepted for recovery" (Sol C05 §7.B candidate). |
| DEC-04 | Adopt "every privileged operation authorizes its own invocation" as a Factory-wide invariant. | Jarvis → Tony | FC-036, FC-057, FC-050, FC-038 | Adopt (Sol C05 §7.A candidate). |
| DEC-05 | Commerce quote authority: server quote source, tax policy, quote versioning, guest-order capability. | Jarvis → Tony | FC-050, FC-051, FC-060, FC-067 | Single persisted server quote bound to the order and the PaymentIntent. |

**Priority 2: foundational; each unblocks several FCs**

| ID | Decision | Owner | Affects | Recommendation (PROPOSED) |
|---|---|---|---|---|
| DEC-06 | Factory precedence / reconciliation model and its host doc. Question-scoped (Astra C01-S01) vs linear tier order (Fable). | Jarvis → Tony | FC-005, FC-001, FC-029, FC-042, FC-073 | Question-scoped model; preserves stage-specific rules per Sol's adjudication. |
| DEC-07 | Seat glossary: names for the human seat (Director / Operator / Coordinator), Architect, Engineer, QA Lead / executor, deployment seat; seat vs persona naming. The Part 2 instruction says "Jarvis/Sol is Architect" while DocSet Sync v0.8 seats Sol as QA Lead. | Tony | FC-006, FC-004, FC-011, FC-027 | One glossary at a constitutional anchor; personas mapped to seats per context. |
| DEC-08 | Is root `CLAUDE.md` governed doctrine (MANIFEST + lint scope) or tool configuration (pointers only)? (Fable §11 decision 5) | Tony | FC-010, FC-008, FC-090, FC-091, FC-094 | No recommendation; needs Tony's intent for the root file. |
| DEC-09 | Kit disk verification: `httpOnly` flag and session architecture, the `protectPage` / `getUserRole` contract, the shipped rail breakpoint. | Tony (needs access to the kit repo) | FC-042, FC-041, FC-072 | Verify against a named kit repository and revision; record the evidence in the Hub. |
| DEC-21 | Who executes the `XB-*` items, and in which job (Skills Playbook authoring for `_SKILLS/**`; a lint/CI job; a root-instruction job). | Tony | FC-005, FC-006, FC-090, FC-091, FC-092, FC-094, FC-095, FC-096, CF-17 | Separate small jobs, each with its own approval; not passengers in a DocSet Sync run (D21). |

**Priority 3: artifact and process contracts**

| ID | Decision | Owner | Affects |
|---|---|---|---|
| DEC-10 | One APP_BRIEF / UI_SPEC template or one per pipeline (FC-019); status vocabulary, recommend APPROVED / AMENDED (FC-016); greenfield UI_SPEC model A (Architect drafts) or B (Designer authors) (FC-017). | Tony (Jarvis proposes) | FC-016, FC-017, FC-019 |
| DEC-11 | Is the Engineer = Claudy in every context, and when is the greenfield DATA_CONTRACT completed and approved? | Tony | FC-015, FC-027 |
| DEC-12 | `FILE_TREE.md`: require it (with producer and approval) or retire it. | Tony | FC-008 |
| DEC-13 | Module freeze model (immutable inputs vs authorized outputs) and the home of QA artifacts. | Jarvis → Tony | FC-026, FC-013 |
| DEC-14 | FFM scope-authority artifact (recommend APP_BRIEF); whether recon may run build diagnostics; whether to define a bounded emergency-change procedure now. | Tony | FC-029, FC-014, FC-023 |
| DEC-15 | Persisted personal-data retention policy (fields, duration, guest vs user scope). | Tony | FC-040 |

**Priority 4: Hub governance and distribution**

| ID | Decision | Owner | Affects |
|---|---|---|---|
| DEC-16 | End merge-over-red (clear the 9 findings, require green) vs adopt a reviewed baseline file; fix the CI wording vs extend triggers. | Tony | FC-096, FC-095 |
| DEC-17 | Doctrine distribution: cut a first doctrine tag now?; the standard project-side landing path; the release owner. | Tony | FC-088, FC-081, FC-003 |
| DEC-18 | Deployment doctrine owner / DevOps seat; ratify the git/cloud authority matrix (may the Engineer deploy to staging in FFM runs?). | Tony (Jarvis advises) | FC-011, FC-012 |
| DEC-19 | Where skills, worked examples and issue logs live, and where the locator is hosted. | Tony | FC-009, FC-003 |
| DEC-20 | QA_PLAYBOOK v1.0 archive: restore from Git history vs documented exception. | Tony | FC-089 |
| DEC-22 | Optional: apply any of Sol's conditional severity re-elevations (FC-002, FC-037, FC-052, FC-061). The package keeps certified severities until Tony rules. | Tony | FC-002, FC-037, FC-052, FC-061 |

## 10. Already remediated on current main (no new correction)

| FC | Certified title | Evidence on main (QA-5) | Package treatment |
|---|---|---|---|
| FC-085 | Skill activation performs `git pull` before its own approval and resume safeguards | v0.8 §2 "Do not pull" during discovery; the only pull is post-merge | Regression guard only |
| FC-086 | Phase 4 pushes before the gate that approves pushing | v0.8 Phase 4 has no push; push only after Gate 4 (D18) | Regression guard only |
| FC-097 | Hub skill supporting files still describe the pre-v0.3 cargo location | README, LESSONS_LEARNED and AP-11 all name `_INBOX/` | Regression guard only |

These keep their certified baseline severity (HIGH, HIGH, LOW). Severity is never lowered for a later repair (register §0).

## 11. Optional backlog: suggestions (not defects, not mandatory)

The certified register's Appendix A inventories 35 suggestions. **They are optional backlog, not defects and not part of the 94 required corrections.** Some entries cite one as context: for example C01-S01 informs DEC-06, and FBL-S003 (anchor lint) could support FC-083. Adopting any suggestion is a separate decision. Copied from the certified register:

#### A.1 Astra suggestions (21) with Sol ruling

| ID | Title | Sol ruling |
|---|---|---|
| C01-S01 | Scope source-of-truth rules by the question being answered | ACCEPT AS SUGGESTION (subject of CONFLICT in FC-005) |
| C01-S02 | Give approvals and locks a minimal common evidence record | ACCEPT AS SUGGESTION |
| C01-S03 | Make lifecycle applicability explicit at the execution-map entry point | ACCEPT AS SUGGESTION |
| C02-S01 | Make operational custody acceptance explicit | ACCEPT AS SUGGESTION |
| C02-S02 | Give recon a complete coverage and freshness record | ACCEPT AS SUGGESTION |
| C02-S03 | Define a provisional visual-alignment step before brief approval | ACCEPT AS SUGGESTION |
| C02-S04 | Preserve mandatory planning inputs in the canonical brief template | ACCEPT AS SUGGESTION |
| C03-S01 | Add a repeated-remediation escalation rule | ACCEPT AS SUGGESTION |
| C03-S02 | Scale document ceremony to risk and actual content | ACCEPT AS SUGGESTION |
| C03-S03 | Carry one candidate/evidence manifest through Q, remediation, and D | ACCEPT AS SUGGESTION |
| C04-S01 | Define a small adversarial authorization evidence matrix | ACCEPT AS SUGGESTION |
| C04-S02 | Require an explicit tenancy and administrative-reach decision | ACCEPT AS SUGGESTION |
| C04-S03 | Label cache privacy and invalidation scope alongside caching recipes | ACCEPT AS SUGGESTION |
| C05-S01 | Maintain one coherent, mechanically checked example path per integration | ACCEPT AS SUGGESTION |
| C05-S02 | Attach an integration ownership and recovery record to each adopted recipe | ACCEPT AS SUGGESTION |
| C05-S03 | Consolidate duplicate quick references and declare example limits beside the recipe | ACCEPT AS SUGGESTION (subject of CONFLICT in FC-070) |
| C06-S01 | Reproducible visual capture/comparison manifest | ACCEPT FOR LATER CONSIDERATION |
| C06-S02 | Small accessibility evidence matrix | ACCEPT FOR LATER CONSIDERATION |
| C07-S01 | Add a small repository landing map | ACCEPT FOR LATER CONSIDERATION |
| C07-S02 | Extend mechanical checks proportionally | ACCEPT FOR LATER CONSIDERATION |
| C07-S03 | Make skill release/retirement evidence easy to locate | ACCEPT FOR LATER CONSIDERATION |

#### A.2 Fable suggestions (14); no Sol ruling in the authorized evidence

| ID | Subject (abridged from Fable §8) |
|---|---|
| FBL-S001 | Hub entry point with reading order by seat, tier precedence, and a "where things live" table |
| FBL-S002 | One gate registry (Gate M/Q/D, FFM gates, module gates, AC) with owner, verdict vocabulary, doc home |
| FBL-S003 | Extend lints: anchor lint, project-path lint, baseline file so CI fails only on new hits |
| FBL-S004 | Un-park MANIFEST auto-generation from headers in CI; assert the count |
| FBL-S005 | Add the Recon Report to DESIGNER_PLAYBOOK §2 inputs |
| FBL-S006 | Recon Report format slots for Sections 11 and 12 |
| FBL-S007 | Prune project residue from constitution-tier and model docs |
| FBL-S008 | Adopt BIM's "Governed by" header field Hub-wide; lint its targets |
| FBL-S009 | Cross-link TESTING Part 5 companion artifacts from BUG_FIX, QA, BIM; scaffold in FFM |
| FBL-S010 | Define the QA seat's activation contract |
| FBL-S011 | Add a kit-baseline line to MANIFEST or CHANGELOG |
| FBL-S012 | Write negative paths for the Blueprint's gates with re-entry points |
| FBL-S013 | Codify Version History ordering |
| FBL-S014 | Note in `_ARCHIVE/README.md` that snapshots begin at 2026-07-12 |

## 12. Newer-doctrine harvest: SEPARATE AND PENDING

- **Status: not part of this package. Pending.** Any harvest of newer doctrine is a separate intake, decided by Tony.
- **Boundaries stated by the Director (CLAIM, from the Part 2 instruction):** ABM/APBM remain **10X-only**; Vibe Engineering remains **project-local**. Nothing here proposes promoting either into the Factory DocSet.
- **GAP:** `git grep` for "ABM", "APBM" and "Vibe Engineering" over `c6210c3` and main `9c17939` (2026-10-11) finds no occurrence in the Hub. This package therefore contains no content from them and makes no proposal about them.

## 13. DocSet Sync intake fit, and validation

**How this becomes sync cargo (after approval only):**
- **Classification.** Once Tony approves it (whole or per wave), the approved package folder is dropped into `_INBOX/` and classified **APPROVED CORRECTION PACKAGE** (D16). While it carries the DRAFT label it is not approved intake and must not be placed in `_INBOX/`.
- **ID join key.** Corrections keep the IDs the package assigned (D16), so `FC-###` becomes the join key through the UPDATE MAP, Version History rows, commit messages, CHANGELOG, handoff, QA evidence and Gate Q.
- **D17 field mapping.** D17 says an approved package defines WHAT MUST BECOME TRUE. The fields map as:

  | D17 element | This package's field |
  |---|---|
  | confirmed problem | Defect + certified record |
  | evidence IDs | Reviewer source IDs + Evidence |
  | approved intent | Proposed outcome, **only once approved** |
  | invariants / preservation constraints | Preserve |
  | likely files | Likely affected docs / consumers |
  | constraints | Open decision + route |

  Claudy proposes WHERE and HOW in the UPDATE MAP at Gate 2. Nothing in this package is a placement or wording decision.
- **Baseline drift.** Pre-existing stale index values (FC-093) are baseline drift that DocSet Sync parks unless approved intake authorizes repair (D7). Approving FC-093 is that authorization.
- **Cross-boundary items.** `XB-*` items are parked by DocSet Sync with IDs (D21) and need their own jobs (DEC-21).
- **Location.** `factory-corrections/` sits outside the synchronized DocSet and outside lint scope (`lints/lint_common.py` scans only the tier folders plus MANIFEST and CHANGELOG).

**Validation.** Read-only checks, run by Claudy. This is self-checking, not QA certification. Full results are in `agent_docs/RESPONSES/response_2026-10-11_*_part2-correction-package-draft.md`.
- Complete and unique primary coverage of FC-001 … FC-097, each in the brief matching its register section.
- For all 97 entries, the certified CF, severity, review status, current-main status, correction value, reviewer-ID set and title match the register at `c6210c3`.
- Family membership and totals recomputed from the briefs equal register §5A.1 and the QA totals.
- Every one of the 94 corrections has a PROPOSED outcome, verification intent and route. Each of the 3 NO entries says NO NEW CORRECTION.
- Every pinned path resolves at its stated revision. The exceptions are deliberately cited absent paths: the missing QA v1.0 archive, the broken `agent_docs/APP_FACTORY` links, the unlocated `agent_docs/LESSONS` and a `_SKILLS` glob.
- Protected inputs are byte-identical before and after (SHA-256).
- The lint baseline is unchanged.
- Writes stayed inside `factory-corrections/` plus bookkeeping.

---

*DRAFT — CORRECTION INTAKE / NOT APPROVED FOR SYNC. Prepared for Architect (Jarvis) and Director (Tony) review. No synchronization has begun.*
