# Fable (QA Lead) — Phase 2 map review, independent verification and Phase 3 readiness — 2026-10-16 17:55 +0600

**Seat:** QA Lead (Fable), fresh session. **Inputs:** `DELIVERY/FACTORY_PHASE2_FABLE_HANDOFF_2026-10-16_164712.zip` (SHA-256 `87d37eb0…7973`, 429/429 payload hashes OK), RUL-08…15, RUL-01…07/AD-01 (snapshot), standing invariants, pinned main `9c17939`. **No canonical edits, no Git mutations, no new intake process.** Companion: `DOCSET_SYNC_ACCEPTANCE_SPEC.md` (DRAFT).

## 1. Engineer-reported counts — independently checked

| Claim (Cody) | Fable's check | Result |
|---|---|---|
| 93 proposed paths | `EXECUTION_PROPOSAL_INDEX.json` = 93; tallied by tier | CONFIRMED: 31 revised + 3 new playbooks + 25 templates + 32 archives (31 outgoing + restored QA v1.0) + MANIFEST + CHANGELOG |
| 31 revised documents | 31 entries with `before_sha256`; all equal `git show main:<path>` and the untouched worktree | CONFIRMED |
| Three new playbooks | QAM/RRM/DEPLOYMENT exist in proposal, absent at main | CONFIRMED |
| 25 QAM templates | 25 files; source hashes match snapshot; translations replayed from `INTAKE_SNAPSHOT` → 25/25 proposed hashes match index | CONFIRMED |
| Archives and index repairs | 31 archives byte-equal to baseline; QA v1.0 restore = blob `bb41260f` (SHA-256 `32d17ef5…`) confirmed via `git cat-file`; "index repairs" = MANIFEST + CHANGELOG only (`_ARCHIVE/README.md` untouched, carries no index) | CONFIRMED with the defects in §3 |
| 334 ordered edits | replayed sequentially over baseline: 334/334 apply; residual vs proposal = header bump + one history row (+2 authorized STARTER_KIT header lines) | CONFIRMED |
| Proposal lints PASS | Fable ran the lint scripts (byte-identical to repo `lints/`) on the proposal tree: PASS, 36 docs, 0 hits | CONFIRMED |
| Refs unchanged | HEAD `626da8d`, main = origin/main `9c17939`; canonical worktree clean | CONFIRMED |

## 2. Agreement with Tony's eight approved decisions (RUL-08…15)

| Ruling | Proposal state | Gaps |
|---|---|---|
| RUL-08 scope / external tracking | Ledger 97 rows; `EXTERNAL_FOLLOWUPS.md` names owner/trigger per component; no "all resolved" claim found | none blocking |
| RUL-09 artifact ownership | Propagated to Blueprint, ARCHITECT/DESIGNER/ENGINEER/HANDOFF, FFM §2/§4/§7/§9, GDSH | MC-07 (retained contradicting sentence in ENGINEER §12; Blueprint Phase 3 heading) |
| RUL-10 deployment | DEPLOYMENT_PLAYBOOK v1.0 RULED/OPEN split; no new cloud grant | none |
| RUL-11 security/commerce | 26 withdrawal rows; dependents withdrawn; universal designs DEFERRED and labeled | AC16 manual read at QA |
| RUL-12 authority/recon | "filesystem wins" replaced in SFP/QA/ENGINEER/ARCHITECT/FFM/BIM/DESIGNER | none found |
| RUL-13 personal data | STATE/ECOMMERCE/AUTH/TESTING edits (FC-040) | none found |
| RUL-14 housekeeping | glossary in SFP; reviewer guidance RRM §11; QA v1.0 restored; release-tag text removed | MC-05, MC-10, MC-01 |
| RUL-15 execution/commits | one implementation commit, Tony-only Git, continuous execution text | MC-08 (transition commit undefined) |

## 3. Concrete map corrections required before implementation (MC)

Blocking-class = would fail an AC on the candidate as proposed.

| ID | Class | Finding (evidence) | Correction |
|---|---|---|---|
| MC-01 | Blocking | The FC-009 prefix "**Historical external example pointer — availability unverified:**" is inserted *before* the markdown structure at 13 sites, breaking a table row (SFP:60), blockquotes (HANDOFF:7, :9), bullets (SFP:116, HANDOFF:380, UI_UX:128, THEMING:268) and bold-in-bold lines (HANDOFF:131, :169); FFM:1987 keeps "Two real FFMs are available" beside "availability unverified". | Regenerate E225–E238 so the label sits inside the cell / after `> ` / after `- `; reword FFM §20 sentence. |
| MC-02 | Blocking | Duplicate "## Version History": RECON_QUESTIONNAIRE (base 1 → prop 2; original table before "Lessons Backlog" uses column "Changes"); HANDOFF_PACKAGE_PLAYBOOK (base table at ~367 has 4 columns "Version/Date/Born From/Changes"; generator appended a new section after the footer). | Append the row to the existing table (match its column shape). |
| MC-03 | Blocking | CHANGELOG: the 35 new rows are appended after `---` and the 🥄 footer, outside the "Ongoing entries" table. | Insert rows inside the table, before the footer. |
| MC-04 | Blocking | Blueprint "THE FULL WORKFLOW" block replaced; the Blueprint no longer states a Phase 5 — Deployment or any deployment/Gate D step, yet SFP "Phase Vocabulary — One Canonical Map" (167–180) still maps to "Blueprint Lifecycle Phase 0 — Recon → Phase 5 — Deployment"; RECON_QUESTIONNAIRE:8 and ENGINEER:123 cite "Phase 0 of the APP_FACTORY_BLUEPRINT lifecycle" and RECON:8 "Stage 0 of the FFM four-role pattern"; MANIFEST FFM row still says "four-role pattern". | Either keep lifecycle phase labels (incl. Phase 5/Gate D pointer) in the Blueprint flow, or re-propagate the four citations and the MANIFEST purpose cell. |
| MC-05 | Gate 2 | RRM §2 cites SFP §2 "Phase Vocabulary — One Canonical Map" for Engine 1/2 definitions; the definitions sit in SFP §1 and the §2 intro, and the vocabulary table has no Engine/review rows. | Add Engine 1 / post-FFM review / Engine 2 / RRM rows to the table, or point the citation at §1 "Shared terminology". |
| MC-06 | Blocking (Tony's explicit requirement) | FFM_PLAYBOOK and BIM_PLAYBOOK contain zero statements of the two review checkpoints (grep "Engine", "RRM", "review after" = 0 hits in both). FFM §2 text flow ends at "Director final Git actions". | Add the checkpoint line used in Blueprint/SFP to FFM §2 flow (post-FFM review) and BIM §6 lifecycle (Engine 2 after all Engine 1 phases), citing RRM §2. |
| MC-07 | Blocking | Retained contradictions: ENGINEER §12 "This is the output the Engineer produces alongside working code" right after the Architect-ownership note; BIM §6 "[folder FREEZES here]" and §9 "the freeze doctrine applies to attackers too" vs RUL-04 contract-freeze/writable lanes; BIM §6 lifecycle lacks QA-branch creation, Q1, plan approval, Q2, cleanup, closeout that BIM §9 now mandates; Blueprint "Phase 3: ENGINEER (Data & Code)" heading. | Replace or withdraw each retained sentence; extend BIM §6 flow. |
| MC-08 | Blocking (process) | `POST_VERIFICATION_STATUS_TRANSITIONS.json` has no MANIFEST row edits for the three status strings (AC-I rows = headers would fail after transition); the commit in which the five transitions land is undefined; `TEMPLATE_INSTALL_VERIFICATION.md` and the RUN_SUMMARY evidence they cite do not exist yet. | Add the three MANIFEST spans; name the commit (recommendation: Tony's closeout commit after Gate Q PASS of the pre-transition candidate, followed by a bounded retest of AC25/AC27/AC31/AC32 + the five spans) and the evidence files. |
| MC-09 | Gate 2 question | Header status suffixes stripped without a cited source: QA_PLAYBOOK "Active — field-tested (ADK Harness…)", BUG_FIX "Active — field-validated (FIX-001/002/003…)", RECON "Active (living document…)" → "Active". | Cite authority (FC-093 derived-index consistency?) or preserve the suffixes. |
| MC-10 | Gate 2 question | MANIFEST "How this stays current" removed wholesale (bump-procedure pointer to `_ARCHIVE/README.md` and the CI-parked note) — RUL-14 only removes release tag / universal landing path. | Retain the bump-procedure sentence; remove only the tag/path claims. |
| MC-11 | Execution | All 36 headers, 35 history rows, MANIFEST and CHANGELOG carry planned `2026-10-16`. | Stamp the actual landing date consistently at implementation (map already says so; AC30 grades it). |
| MC-12 | Traceability | `SELECTED_SCOPE_LEDGER.md` is FC-only; 23 edits (E2, E6–E23 = W02…W23; E146/E313/E316/E327/E331/E332 = RUL-only) have no ledger row. | Add a W01…W23 / RUL section to the ledger (or a column) so AC3 can reconcile three identical sets. |
| MC-13 | Gate 2 | New HANDOFF_PACKAGE and RECON Version History rows are appended after the document footer (🥄 line) — same root cause as MC-02. | Covered by MC-02. |
| MC-14 | Observation | `TEMPLATE_INSTALL_PLAN.md/json` (superseded by `PHASE_2_TEMPLATE_TRANSLATIONS.json`) still shows different expected hashes. | Mark the older plan HISTORICAL in the run folder to avoid two "expected" hash sets at QA. |

## 4. Questions only Tony can answer (not blocking the spec)

- **Q-1 Stick diagrams.** The four Whimsical PNGs stay intake-only and unreferenced; they contradict the approved model (QA Lead executing tests, "Director of QA", "Codex: Sol" persona, no QA Executor/QA branch/recon/Architect assembly, `INITSCRIPT.SH` filenames). RUL-07 keeps them historical. Do you want a one-line canonical note (e.g. in RRM §2 or SFP §1) stating the August diagrams are superseded by the text flows? That is new content and needs your ruling; without it the sync still passes.
- **Q-2 Transition commit.** Confirm MC-08's recommended sequence (transitions in a Tony closeout commit after Gate Q PASS, then bounded retest) or rule that the Engineer applies them inside the single implementation commit after producing `TEMPLATE_INSTALL_VERIFICATION.md`.
- **Q-3 Status suffixes (MC-09)** and **MANIFEST bump-procedure sentence (MC-10)**: keep or drop.

## 5. Readiness recommendation

**Phase 3: NOT READY.** Gate 2 should not approve the map as delivered. Mechanics (hashes, archives, replay, templates, lints) are sound; the blocking items are content/structure defects MC-01…MC-04, MC-06, MC-07 and the process gap MC-08, all of which the candidate would fail under AC7, AC10, AC11, AC20, AC26, AC27, AC33. They are bounded regeneration fixes, not policy reopenings. After Cody applies them and Jarvis reviews, Tony approves Gate 2; Fable re-anchors the spec (AMENDED-v1 only if cited rows change) for Gate 3.

## 6. Verification record (commands run read-only by Fable)

- `sha256sum -c SHA256SUMS.txt` → all OK (429 lines); ZIP SHA-256 matches RECOVERY/receipt.
- Python replay: 93 index entries vs `BASELINE_CONTENT/`, `PROPOSED_CONTENT/`, `git show main:<path>`, worktree → 0 problems; 31 archives EXACT-BASELINE; QA v1.0 DIFFERS by design (historical blob).
- `git cat-file -p bb41260f… | sha256sum` → `32d17ef5…3098e99` (matches `ARCHIVE_RESTORATION_PROPOSAL.json`).
- 334-edit sequential replay → 334 ok / 0 fail; residual classification per file: header ×2, history-row ×1 (STARTER_KIT +2 authorized header lines; HANDOFF/RECON +3 scaffold lines = MC-02).
- Template translations replay from `INTAKE_SNAPSHOT/…/TEMPLATES/QAM/` → 25/25 equal to `PHASE_2_TEMPLATE_TRANSLATIONS.json` and index hashes.
- `cmp` of the 6 lint scripts in the proposal tree vs repo `lints/` → identical; `python3 -I lints/run_all.py` in `PROPOSED_CONTENT` → PASS (36 docs); repo baseline re-run → 9 findings (8 VERSIONED-REFS + 1 HEADER-PRESENCE) as recorded.
- Header/Version-History extraction for 34 docs; MANIFEST rows = 34 = files on disk; CHANGELOG rows counted (35).
- Greps: Engine/RRM/review-after (0 in FFM/BIM); "four-role"/"Blueprint lifecycle" citations; historical-pointer sites (13); freeze wording (BIM); Git/branch instructions (live docs + templates); `2026-10-16` occurrences (36 files).
- Read: the four PNG diagrams; `01_FACTORY_WORKFLOWS_INTAKE.md`; RUL-01…07/AD-01 revisions; sync-qa SKILL, STANDING_INVARIANTS, spec template; full diffs of Blueprint, SFP, FFM, QA, ENGINEER, BIM, HANDOFF, ARCHITECT, DESIGNER; full RRM and DEPLOYMENT playbooks; QAM playbook vs draft.
