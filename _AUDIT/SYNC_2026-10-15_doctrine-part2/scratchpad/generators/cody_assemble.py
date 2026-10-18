from pathlib import Path
import json,re,collections,hashlib,subprocess,datetime
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');D=json.loads((R/'scratchpad/proposals.json').read_text());C=json.loads((R/'scratchpad/placements.json').read_text());E=json.loads((R/'scratchpad/fc_sources.json').read_text());harvest=json.loads((R/'scratchpad/harvest_sources.json').read_text());F={p.stem:p for p in Path('.').glob('0*_*/*.md')};base='9c179392f79b70da099121fc357d3107ad3bb86e';out=[]
def add(s):out.append(s.strip()+'\n')
add('''# UPDATE MAP — doctrine-part2 — 2026-10-15

**DRAFT FOR DIRECTOR / ARCHITECT REVIEW — NOT APPROVED FOR EXECUTION.** Cody is the Engineer taking over Opy’s authorized drafting. Certified findings remain 97 total, 94 correction YES and three NO (FC-085/086/097). This map does not convert a proposed correction outcome, harvest proposal or substitutions record into approval.

The proposed ledger is pre-drop planning, not completed intake. No `_INBOX/`, snapshot, preservation commit, Gate 1 approval, Gate 2 freeze or Gate 3 acceptance-spec approval is claimed. No canonical change, template installation or Git mutation was performed. Required policy and evidence decisions are in §K. Explicit review of unresolved rows is required; silence neither adopts nor defers them.

Evidence labels: EVIDENCE = locally checked; CLAIM = attributable source record; ENGINEER-PROPOSED = wording for review; GAP = missing evidence; QUESTION = decision required. Full source text in §B preserves the source’s own PROPOSED labels. **This is a review draft, not a claim that all proposed correction requirements have been implemented or independently verified.**''')
add('''## 0. Run header

| Field | Value and evidence |
|---|---|
| Active run | `_AUDIT/SYNC_2026-10-15_doctrine-part2/`; existing run reused |
| Current branch / HEAD | `factory-docs-review-astra-w-chunks` / `626da8d70f4db22987dc7fcc86765492072360cd` — EVIDENCE, read-only Git |
| Proposed execution branch | `docs/sync-doctrine-part2-2026-10-15`, created by Tony only after preservation and approval; not created |
| Proposed BASE_SHA | `9c179392f79b70da099121fc357d3107ad3bb86e`; local main and origin/main refs; canonical scope has empty working-tree diff against it. Remote not fetched in this takeover. Every placement is checked against these identical canonical bytes. |
| Merge target | main; Tony owns final Git actions |
| Execution route | Local Hub clone; explicit current instruction overrides the skill’s D5 agent-Git carve-out: ALL Git mutations are Tony-only |
| Route | LARGE; §P evidence. No docs-only QA waiver proposed |
| Seat arrangement | Director Tony; Architect Jarvis; QA Lead Fable; Engineer Cody. Independent QA Executor must be assigned in a fresh session; this Engineer cannot certify this work |
| Status | DRAFT; §O has no invented approval |
| Intake snapshot | Proposed `INTAKE_SNAPSHOT/` after approved scope and actual drop. Missing now; may not be represented as completed intake |
| Lint baseline | 9 findings, command/cwd/exit/unfiltered output in `LINT_BASELINE.txt`; eight VERSIONED-REFS and one HEADER-PRESENCE. DEC-16 authorizes the document fixes; expected candidate zero, not nine carried forward |
| Live-doc count | 31 tier documents + MANIFEST/CHANGELOG = lint’s 33 files; MANIFEST has 31 rows but states 29; appendix states 27 bodies. Three proposed new playbooks → 34 tier docs, excluding 25 template files |
| Governing skill | main at BASE_SHA, family CLAUDE.md + sync-engineer/SKILL.md v0.8-DRAFT. `DRAFT_AND_SKILL_HASHES.json` pins identities; working-tree skill is older |
| Recovery | Initial exact 33-path status in `RECOVERY_STATUS.txt`; handoff’s “28” was a miscount of its own 31 listed paths. Later additions: AGENTS.md and the 20:00 reporting response. No exact 28-path snapshot is available; no fictitious three-path delta is invented |

Relevant failure patterns: AP-16 propagation by memory; AP-22 trusting stale recovery prose; AP-23 maintaining totals independently of rows. The source archives, drafts and accepted template bytes remain preserved.''')
ledger=(R/'PHASE1_LEDGER.md').read_text();ledger=ledger.replace('`SOURCES/','`factory-intake/SOURCES/');(R/'PHASE1_LEDGER.md').write_text(ledger)
add('## A. Proposed intake ledger\n\n'+ledger.split('\n',1)[1])
add('''## B. Per-ID intent, preservation, dependencies and search

For each FC, the complete source block below preserves the certified field, evidence, proposed outcome, preservation and verification intent verbatim. **No distinct approved invariant field is invented:** the package supplies proposed outcomes and verification intent, not approved execution wording. Gate 1/2 must approve the applicable scope/wording. Domain-wide preservation in briefs 04/05 also applies (§L). Search rows are in `PROPAGATION.tsv`; query definitions and command/scope are in `SEARCH_QUERIES.json`. Exact workflow changes are incorporated in §C; broader correction wording and verified anchors remain visible below. Independent QA derives from the finally approved map, never from an Engineer’s claim of closure.''')
for p in sorted((R/'scratchpad/map_parts').glob('PART_*.md')):add(p.read_text().split('\n',3)[-1])
add('### Harvest items — IN-2026-10-15-01…36\n\nThe historical harvest is quoted intact; RUL-01…07 supersede only the stated questions. Current adoption and crosswalk follow each item. No historical record is rescored.')
for h in harvest:
 old=h['old'];where='§C shared workflow edits and corresponding FC rows' if old.startswith('WF') else '§D RRM_PLAYBOOK draft (actual §§1–14)' if old.startswith('RRM') else '§D QAM_PLAYBOOK draft and accepted template installation plan'
 add(f"#### {h['id']} — {old}: {h['title']}\n\nINTAKE-VERBATIM from `{h['path']}:{h['line']}`:\n\n{h['body']}\n\nMapping: {where}. Ruling interface: RUL-01 mandatory QAM, RUL-02 continuing candidate-based QA branch, RUL-03 required cleanup/production exclusion, RUL-04 frozen contract/writable lanes, RUL-05 two reviews with conditional RRM, RUL-06 owning documents, RUL-07 preservation/tooling boundaries. Unruled content remains conditional under §K. Search: query `WORKFLOW` plus linked FC queries. Verification: source Preserve/Verify requirements, §M and template checks. Source claims of supersession do not authenticate missing historical rulings.")
add('''### Supporting intake IN-37…67

These records are not extra correction findings. IN-37 is the Director-approved QAM source, unchanged SHA `97e111e2a495f9a3fe65f50213e6f2ba68c8e5e963f3d23493b1ee99ad35c897`; IN-38 is the 25-file accepted template set. IN-39…45 preserve separate Director, Architect, QA Lead, verification, planning and provenance records. IN-46…67 preserve all 22 original source identities/hashes from SOURCE_INVENTORY, including diagrams and historical pilot packages. Original source files and extracted pilot evidence are never rewritten. Their content is incorporated only through the explicit FC/harvest rows and attributable rulings. Old diagram flows are historical, not competing adopted policy. No new diagram asset is commissioned by this map.

P1 local check: `INTAKE_VERIFICATION.txt` establishes 35/35 addendum members + 24/24 referenced-in-place members and exact folder coverage. This is Cody’s Engineer verification, not an Architect confirmation. The 25 template members match the separately Architect-verified ZIP; the corrected QA decision provenance is preserved outside that historical ZIP.''')
add('''## C. Canonical touch proposals and exact workflow edits

Every added paragraph below is ENGINEER-PROPOSED. A shared passage is edited once with all contributing IDs; an overlap is not authorization to concatenate competing instructions. Preserve correct examples and historical entries. Exact `old`/`new` workflow spans are recorded in `PROPOSED_EXACT_EDITS.json`, checked unique against pinned bytes. Their rendered text is included below. Mechanical reference/header/token edits are in the supplemental rows. Proposed substantive replacement requirements for the remaining correction rows are given in §B at verified anchors; they require review of the corresponding recipe/contract before execution, especially where §K remains open. No row authorizes “fix anything nearby.”

**Review boundary:** The contract-level rows are proposals for reconciliation, not a blanket authorization to rewrite code examples by improvisation. Before Gate 2 freezes an executable map, every selected recipe rewrite must have its exact replacement span approved, and all propagation hits must have a final reviewed disposition. The map explicitly carries this freeze requirement in §K-MAP-FREEZE; it is not waived by the current drafting authorization.

| Row | Canonical doc / verified locations | Proposed wording | IDs | Conditional |
|---|---|---|---|---|''')
for c in C:
 paths='; '.join(f"`{p['path']}:{p['line']}` ({p['heading']})" for p in c['placements']);add('| '+c['id']+' | '+paths.replace('|','\\|')+' | '+c['text'].replace('|','\\|')+' | '+c['fc']+' | See §B / §K; all await Gate 2 |')
add((R/'EXACT_WORKFLOW_EDITS.md').read_text())
add((R/'EXACT_CORRECTION_EDITS.md').read_text())
add('''### Mechanical correction rows (ENGINEER-PROPOSED)

- C-M01 / FC-003, FC-096: STARTER_KIT_HANDBOOK adds the standard single-line header using its actual version 1.1 → proposed 1.2 and actual landing date. Replace the five versioned filename references with canonical names: COMPONENT_REGISTRY_v1.1.md → COMPONENT_REGISTRY.md; UI-UX-BUILDING-MANUAL_v1_3.md → UI_UX_BUILDING_MANUAL.md; AUTH_MANUAL_v1.2.md → AUTH_MANUAL.md. Update maintenance wording through C-003; do not generalize the project landing path while DEC-17 remains open.
- C-M02 / FC-096: DATABASE_MANUAL lines 8 and 156, `AUTH_MANUAL v1.3` → `AUTH_MANUAL`; UI_UX_BUILDING_MANUAL line 2092, `THEMING_MANUAL_v1.0.md` → `THEMING_MANUAL.md`. Do not alter historical CHANGELOG references.
- C-M03 / FC-032: FRONTEND_BUILD_PHASE_PLAYBOOK §9 Gate Q reference → QA_PLAYBOOK §12; Gate D → QA_PLAYBOOK §13; retain existing engineering checklist requirements.
- C-M04 / FC-081: COMPONENT_REGISTRY §11 Hub link to `../05_DESIGN_SYSTEM/UI_UX_BUILDING_MANUAL.md` (same-tier form `UI_UX_BUILDING_MANUAL.md` preferred); THEME_LIBRARY Cross-References to `GLOBAL_DESIGN_SYSTEM_HANDBOOK.md` and `../01_CONSTITUTION/STARTER_KIT_HANDBOOK.md`; correct Handbook Theme Conventions reference to §9. Intentional project paths remain separately labeled and conditional on DEC-17.
- C-M05 / FC-084: DESIGNER_PLAYBOOK line 232 becomes exactly `- [ ] All required elements and minimum display fields in the approved UI_SPEC are present; record NOT APPLICABLE only where that contract says so.` No nonexistent §5.6 is invented.
- C-M06 / FC-070: API_AND_SERVICES_MANUAL’s two `## 10. Quick Reference` bodies are merged at the end as `## 14. Quick Reference`; preserve every unique entry, keep sections 1–13 stable, and regenerate the ToC from actual headings. Any contradictory quick-reference recipe follows its linked correction row, not an independent alternate implementation.
- C-M07 / FC-074: exact token replacements and calculated ratios are in `FC074_CONTRAST_PROPOSAL.md`, incorporated here. Fifteen declaration changes preserve hue/meaning; 128 declared text/fill pairs across Mist, Slate, Bright and Dark-deep pass the proposed numerical 4.5:1 threshold. This is numerical proposal evidence, not browser QA. Update THEME_LIBRARY’s shared-value claim with the exact proposed sentence; remove stale hex/ratio comments for changed values.
- C-M08 / FC-089: proposed historical archive source `9ad3f3f:03_BUILD_METHODOLOGY/QA_PLAYBOOK.md`, header v1.0; blob `bb41260f6b6f94372a682f04b313a451f2b3c4b1`. Read-only history shows no intervening QA_PLAYBOOK edit before v1.1 commit 012c05d. Restore byte-for-byte only if DEC-20 chooses restoration; otherwise explicitly record the approved exception. This is separate from archiving outgoing v1.1 for this run.

### Consolidated per-document versions and archive plan

Versions below are proposals, not source facts about an installed candidate. One bump per distinct touched document; all its FC and workflow rows share that bump. Read the actual header again before archiving. Date placeholders resolve to the actual execution date, not a predicted date. New archives must equal BASE blobs. Infrastructure files receive date/content changes only.

| Document | Header at BASE → proposed | MANIFEST ← count | Archive | Structural change |
|---|---|---|---|---|''')
# Build from actual enumerated canonical placements and exact workflow changes.
exact=json.loads((R/'PROPOSED_EXACT_EDITS.json').read_text());paths=sorted({x['path'] for c in C for x in c['placements']}|{x['path'] for x in exact if not x['path'].startswith('_AUDIT/')})
vers={};rev={}
for line in Path('MANIFEST.md').read_text().splitlines():
 cs=[x.strip() for x in line.split('|')]
 if len(cs)==5 and cs[1] in F and cs[3].isdigit():rev[cs[1]]=int(cs[3])
for p in paths:
 s=Path(p).read_text();m=re.search(r'\*\*Version:\*\*\s*v?([\d.]+)',s[:1800])
 if not m:m=re.search(r'Version:?\s*v?([\d.]+)',s[:1800],re.I)
 v=m.group(1).rstrip('.') if m else 'UNRESOLVED';spl=v.split('.');nv=str(int(spl[0]))+'.'+str(int(spl[1])+1) if len(spl)==2 else (str(int(spl[0]))+'.'+str(int(spl[1])+1)+'.0' if len(spl)==3 else 'REVIEW');vers[p]=[v,nv]
 add(f'| `{p}` | {v} → {nv} | {rev.get(Path(p).stem,"GAP")} | `_ARCHIVE/{Path(p).stem}_v{v.replace(".","_")}.md` | Existing doc; bounded edits only |')
(R/'scratchpad/versions.json').write_text(json.dumps(vers,indent=2)+'\n')
add('''## D. New canonical files and accepted templates

All three existing drafts are preserved exactly and pinned in `DRAFT_AND_SKILL_HASHES.json`. The draft body plus explicit substitutions and D-* corrections in §C is the proposed text. No “Active” label inside a draft is an approval. `<<LANDING_DATE>>` is an execution-time mechanical value. Conditional sections cannot silently land as adopted doctrine.

| New file | Tier / owner | Header proposal | MANIFEST / Pairs-with / CHANGELOG | Source IDs |
|---|---|---|---|---|
| `03_BUILD_METHODOLOGY/QAM_PLAYBOOK.md` | Build methodology; QA Lead owns reusable QA doctrine | v1.0, actual landing date; Active only after approved landing | FROM draft header’s named Pairs-with; purpose “Mandatory module-specific QAM, independent planning/execution, evidence, cleanup and certification; owns reusable _templates/QAM set”; one owning CHANGELOG row includes template installation | IN-23…38; RUL-01…07; AD-01 |
| `03_BUILD_METHODOLOGY/RRM_PLAYBOOK.md` | Build methodology; bounded approved review repair | v1.0, actual landing date; adopted scope only | FROM draft header; purpose “Dispositioned review findings into bounded repair, independent QAM and closeout”; one CHANGELOG row | IN-13…22; WF-11; RUL-01…06 |
| `03_BUILD_METHODOLOGY/DEPLOYMENT_PLAYBOOK.md` | Build methodology; owning deployment doctrine, unresolved platform/authority explicitly OPEN | v1.0, actual landing date; adopted sections identified | FROM draft header; purpose “Deployment identity/exclusion, module Git flow and explicit unresolved deployment policy”; one CHANGELOG row | IN-08…10; FC-011/012/088; RUL-02/03/06 |

**QAM source adaptation:** `DRAFTS/QAM_PLAYBOOK_substitutions.json` contains 11 exact records labeled S1, S2, S3a/b, S4, S5, S6a/b/c, S7, S8. They are ENGINEER-PROPOSED integration changes, not approvals. S8 remains conditional DEC-17. S2 retroactivity and S6 cross-track/TRM wording retain RUL-07 boundaries. S3 journal provenance must remain “source reported / not supplied,” not independently authenticated. S7’s precedence-dismissal sentence is corrected by D-QAM-1. Landing claims that the rest of the corpus “was reconciled” may appear only after this run’s final verification; otherwise retain the original prospective obligation.

**Existing RRM draft:** actual reviewer guidance is §11 and optional uninterrupted run is §12; neither is adopted by RUL-05 alone. Apply D-RRM-1/2 pending the explicit §K decisions. The current source has 14 sections, not the older reported 13. The two-review cadence is ruled; no Engine 3 or mandatory RRM for a clean review.

**Existing deployment draft:** apply D-DEPLOY-1/2/3 before approval to prevent unruled cloud authority and current-main-over-pin precedence from being asserted as settled. Q9.4 currently does not exist; W17 adds it while preserving Q9.3. Platform profiles, staging promotion, monitoring and non-Next.js packages remain explicit gaps. No Cloud Run tool or command is adopted from an August example.

**Template installation:** `TEMPLATE_INSTALL_PLAN.md` and its JSON are incorporated by reference as the 25-file landing list with source and proposed destination hashes and exact status/provenance translations. Destination fixed by AD-01: `03_BUILD_METHODOLOGY/_templates/QAM/`. No separate MANIFEST row; track through the QAM_PLAYBOOK row and CHANGELOG. Explicit acceptance checks are mandatory because lints do not recurse. Acceptance of source behavior is already settled; do not reopen it. Installation and installed-byte verification are still pending.''')
add('''## E. Stale / superseded material

| Material | Proposed treatment | Authority / preservation |
|---|---|---|
| Unsafe auth and client route-guard examples | Archive outgoing canonical documents; remove/quarantine the named unsafe recipes and link governing role/operation rules; kit-specific replacement waits for verified kit evidence | DEC-02; FC-001/033/034/035/036/038/039/041/042. Containment alone does not close all these findings |
| Whole-folder freeze instructions | Replace only frozen-folder claims with frozen-contract / declared-output rules | RUL-04; W03/W04; preserve contract approval |
| Old FFM four-role release implication / handoff omitting QAM | Update complete workflow while preserving Designer/Extractor preparation responsibilities | RUL-01/06; W08…13 |
| Historical disposable QA branch / transfer-back source | Preserve as history in the input snapshot; current prose follows continuing QA line | RUL-02/03; no deletion of evidence or source packages |
| Missing historical QA_PLAYBOOK v1.0 archive | DEC-20 restoration proposal C-M08; not yet performed | Never counterfeit v1.0 from v1.1 |
| Original diagrams and pilot records | Historical input only, unchanged | RUL-07; no revised raster assets or pilot rescore |
| Source templates v0.1/v0.2/v0.3 | Preserve all source folders and verified ZIPs; first canonical installation has no predecessor canonical set to archive | AD-01; future replacement sets use `_ARCHIVE/QAM_TEMPLATES_v<version>/` |

No deletion of existing tracked/untracked work is proposed. Runtime/product debris cleanup rules concern future module execution, not permission to clean this review checkout.''')
add('''## F. Dependents checked

The quoted hit ledger supplies path:line evidence; matching text under Version History/CHANGELOG is HISTORY, active primary surfaces map to §C, and unrelated/correct uses remain quoted CONSISTENT candidates. Header-declared dependencies are retained per §B’s MANIFEST rows and are a starting set, not the whole blast radius. Re-run before candidate acceptance and reject any active contradiction.

Specific preserved interfaces: SFP §2.5 already separates acceptance contract from QA plan; BIM §3 already retains canonical IDs and legacy IDs; QA_PLAYBOOK’s verdict vocabulary and Gate Q/ Gate D purposes remain; STARTER_KIT anti-authService and Navbar Law remain; TESTING’s four-layer scope and failure evidence remain; GDSH token and visual-artifact contracts remain. These are preservation constraints, not a claim that every document needs no changes.''')
add('''## G. Infra/index effects and baseline drift

| Item | Proposed change / check |
|---|---|
| MANIFEST rows | Update every bumped row FROM landed header; add three new rows; template set represented through QAM owning row |
| Counts | Recompute from disk: baseline 31 tier docs; with all three proposed new playbooks, 34. Templates are not independent canonical tier-doc rows |
| Reverse dependencies | Recompute from actual Pairs-with/Governed-by declarations; count each edge once. MANIFEST ← count is not an exhaustive body/skill consumer count |
| Body appendix | Re-scan all actual canonical bodies, date/scope the appendix; remove duplicate FFM→BLUEPRINT classification |
| CHANGELOG | Add missing ongoing table header in existing ledger format; one row per bumped/new document with all contributing IDs; template installation rides QAM row |
| Infra dates | Actual execution date only; no infra archive/version dance |
| DRIFT-01 | 29/27 count claims stale at BASE; correction authorized by FC-093, also necessarily changed by three new docs |
| DRIFT-02 | Nine lint findings predate this run; DEC-16 explicitly authorizes their canonical document repair. No lint exemptions, script/CI edit or trigger expansion |

Partial approval changes the derived counts: re-enumerate the approved rows rather than retaining the proposed 34 unconditionally.''')
add('''## H. Paths, links and assets

- QAM source `TEMPLATES/QAM/` → Hub `03_BUILD_METHODOLOGY/_templates/QAM/` (AD-01), instantiated as module `QAM/` under project `agent_docs/`.
- Source `QAM_PLAYBOOK_v1_0.md` remains an immutable provenance identifier; live canonical citations use `QAM_PLAYBOOK.md`.
- RECON Q9.4 is an explicit new stable-ID question; Q9.3 is retained unchanged.
- New RRM §2 citation to SFP Engine 1/2 requires W23 before it resolves.
- FC-003/081/083/084 mechanical references follow actual canonical paths/headings. Do not publish a nonexistent external locator or guessed kit revision.
- All template provenance links resolve to the committed intake snapshot after actual intake; their existence is a handoff check, not assumed today.
- Original PNG/ZIP sources stay in the snapshot; no new canonical image/asset, image generation, or replacement is proposed.''')
add('''## I. Skill references — read-only awareness

Main’s DocSet Sync family is the governing workflow. The review-branch skill copy is older and cannot be used to re-open FC-085/086/097. Skills referencing FFM/BIM/QA/Engineer and deployment are consumers, not writable passengers. D5’s Git exception is overridden by Tony’s explicit instruction for this run only; no skill file is changed. The main runbook’s merge-over-red wording and CI claim belong to XB-02 (DEC-16), not this sync’s canonical file edits. `_OTHERS/DOCTRINE_HUB_DESIGN_v0_1.md` remains a draft source until DEC-17 promotion/supersession is ruled.''')
add('''## J. Cross-boundary work and evidence gaps

| ID | Target / associated FCs | Why separate | Blocking effect / recommendation |
|---|---|---|---|
| XB-01 | Root CLAUDE.md / AGENTS.md; FC-008/010/090/091/094 | Outside canonical sync surface; DEC-08/21 | Blocks full closure of root components; recommend a separately authorized root-instruction job; no change now |
| XB-02 | `_SKILLS/**`, including this family; FC-005/006/092/095/096 | Skill authoring job under Skills Playbook | Blocks closure of those skill components; does not prevent coherent canonical rows after explicit scope split; no silent “all 94 closed” |
| XB-03 | lints/, .github/, branch protection | DEC-16 approved green document fixes, not CI trigger expansion | Existing document fixes proceed; governance owner Tony must separately enforce required checks; no baseline-aware gate built |
| XB-04 | Pinned starter-kit repository and external skills/examples; FC-009/041/042/072 | Repository/revision evidence not supplied here | Blocks exact kit signature/session/breakpoint closure. Ask for named kit revision or retain explicit blocked rows; never invent verified exports |
| XB-05 | QAM validator/exporter/dispatcher/browser adapter; ABM/APBM methodology | RUL-07 boundary | Not required to install accepted document templates; separately scoped work only |
| GAP-01 | Doctrine Journal v0.3 / J-19 | CL-11 missing historical source | New Director rulings govern current branch/cleanup policy, but do not authenticate the journal; remove dangling normative dependence only through explicit map substitution |
| GAP-02 | Fully certified pilot example/evidence dossier | Harvest records are limited | No retroactive pilot completion or rescore; generic doctrine may proceed from current rulings |
| GAP-03 | Later historical 10X direction | CL-12 missing | RUL-05 governs present cadence; original historical claim remains unverified |
| GAP-04 | DevOps Architect ruling 2026-08-23 | CL-13 missing | DEC-18 remainder remains open; current source model is not permission |
| GAP-05 | Companion synchronization brief | CL-21 missing | This map supplies current planning; do not claim the missing brief was supplied |
| GAP-06 | Harvest outer-ZIP identity difference | E-8 / CL-29 | Local 75/75 file index is verified; Jarvis’s different ZIP is not reconciled by overwriting either copy; non-blocking for this drafting |

Source intent and preservation for each split FC remain verbatim in §B. “Parked” here means outside this run’s writable boundary, not a Director-approved deferral.''')
add('''## K. Unresolved decisions and recommendations

All rows below remain OPEN unless an attributable later ruling is entered. Navigation labels D.2/C.2 are shown for Tony’s convenience; DEC/ND/RRM IDs are the durable decision keys. Drafting did not approve or defer any row.

| Decision | Type | Exact choice / recommendation | Affected work | Ruling |
|---|---|---|---|---|
| DEC-10/11/12 (D.2) | CONFLICT | Rule greenfield DATA_CONTRACT producer/timing; UI_SPEC Model A or B; mandatory FILE_TREE or retirement; template multiplicity/status. Recommend Architect DATA_CONTRACT before Design, Designer UI_SPEC with Architect assembly review, optional FILE_TREE, one canonical template per artifact with pipeline sections, APPROVED/AMENDED. These are proposed changes to current text. If not ready, explicitly defer named conditional rows; no inferred deferral | FC-008/015/016/017/019/027; WF-03/04 | OPEN |
| DEC-18 remainder (C.2) | CONFLICT | Who owns DevOps, which cloud actions by context, may Engineer deploy FFM staging, and is Cloud Run one profile? Recommend retain explicit current restrictions until ruled; adopt only settled Git/exclusion content now; commission missing promotion/monitoring/platform procedures separately by named owner. A new owning doc does not close FC-011 alone | FC-011/012/088; WF-08/09/10; D-DEPLOY edits | OPEN |
| DEC-05 | CONFLICT | Choose pricing sources/tax policy/guest capability and decide whether persisted versioned quote is the design. Recommend one authorized persisted quote bound to order and payment attempt, but that design is NOT a certified requirement. Required server pricing/payment binding can be approved separately; containment cannot close FC-051 | FC-050/051/060/067; shared checkout/store contract | OPEN |
| DEC-17 | CONFLICT | Rule release owner, tag policy, standard project landing path and intentional-pin/update behavior. Recommend Director release, canonical name + header version + Hub commit SHA, no tag cut by this run; project declares its approved landing path until a universal path is ruled. Preserve intentional pins; latest main does not automatically amend project scope | FC-003/081/088; QAM S8; deployment §6 | OPEN |
| DEC-06 | CONFLICT | Question-scoped authority vs linear hierarchy and host. Recommend SFP §1 question-scoped model, preserving domain/stage rules and attributable Director conflict resolution | FC-001/005/029/042/073; D-QAM-1/D-DEPLOY-3 | OPEN |
| DEC-07 remainder | CONFLICT | Glossary host, synonyms and rename policy. Recommend SFP §2, Director with Operator/Coordinator contextual synonyms; preserve Designer; no mass persona rename. QA Executor and Director seats already ruled | FC-004/006/007/027; WF-01 | OPEN |
| DEC-08 | CONFLICT | Root tool configuration or governed doctrine? Recommend tool configuration with pointers; no root edits in this sync. Tony must rule, not the Engineer | FC-010 and XB-01 | OPEN |
| DEC-09 | CLARIFICATION / evidence dependency | Supply named starter-kit repo and immutable revision for guard exports, cookie architecture and rail breakpoint. Recommend inspect that evidence before exact kit rewrite; keep FC-041/042/072 blocked, not “resolved by prose” | XB-04; related auth/design snippets | OPEN |
| DEC-14 (D.3) | CONFLICT | Rule recon diagnostics and scope authority/emergency path. Recommend APP_BRIEF scope authority, report/bookkeeping lane, explicitly authorized diagnostic writes, no implicit emergency implementation exception | FC-014/022/023/029; WF-02; RRM-03; QAM-06 | OPEN |
| DEC-15 | CONFLICT | Fields/duration/user-vs-guest scope for personal-data persistence. Recommend no raw contact persistence by default, coordinated account-transition invalidation; any exception names duration/owner | FC-040; checkout store, logout | OPEN |
| DEC-19 remainder / RRM-09 | CONFLICT | Locator, kits, examples and reviewer-guidance host. Recommend reviewer section in RRM, locator records only for supplied repo/path/revision, no fictitious external examples. QAM template home is already settled by AD-01 | FC-003/009; RRM §11 | OPEN |
| ND-07 | CONFLICT | Default uninterrupted engineering vs optional prepared shape. Recommend optional only, with measured prerequisites/stops and total lifecycle metrics. Source pilot speed is not universal proof | RRM §12; RRM-04/08; QAM-12 | OPEN |
| DEC-20 | CONFLICT | Restore historical QA_PLAYBOOK v1.0 or record exception. Recommend restore exact discovered blob bb41260f…; evidence is available, decision is still Tony’s | FC-089, archive/CHANGELOG | OPEN |
| DEC-21 | CLARIFICATION / scope allocation | Assign owners/jobs for XB-01…05. Recommend separately authorized bounded jobs; approve explicit partial completion accounting for this sync | Split FCs, §J | OPEN |
| DEC-22 | CONFLICT if changed | Optional severity re-elevations. Recommend retain all certified severities; any change requires attributable certification governance, not this map editing the register | FC-002/037/052/061 | OPEN; unchanged |
| K-ENGINE | CLARIFICATION / wording | Approve W23’s Engine 1/2 wording consistent with RUL-05, not SRC-W11’s per-phase Engine 2 or Engine 3 | RRM §2/SFP §2 | OPEN |
| K-SUBSCRIPTION-MODEL | CONFLICT / architectural design | Choose independent customer-link storage and explicit unpaid bootstrap state; recommend separate customer identity with atomic current-subscription reconciliation. Exact schema/recipe must be reviewed before landing, not guessed from incompatible samples | FC-055/053/054 | OPEN |
| K-BIM-SCHEDULE | CONFLICT | WF-06 permits Director-selected upfront or JIT authoring; current BIM locked rule requires JIT. Recommend retain JIT unless Director explicitly approves upfront authoring with execution-baseline revalidation | WF-06 / BIM §6 | OPEN |
| K-DRAFT-INTEGRATION | CLARIFICATION / wording | Approve exact S1…S8 substitutions and D-* corrections, new Q9.4, historical-source qualification and template status/provenance translations. Acceptance of the source package does not approve these added words | §C/D/H, template installation | OPEN |
| K-MAP-FREEZE | Review completeness gate | Select/resolve conditional correction designs, approve exact recipe replacement spans and finalize per-hit dispositions before freezing an executable map. Recommend review this consolidated draft now; do not treat a contract paragraph beside an unsafe snippet as correction. No Engineer completion claim replaces this check | All selected §B/C recipe rows; propagation ledger | OPEN — Gate 2 must not be stamped prematurely |

Five scoped approvals remain untouched: DEC-01 coordinated intake direction, DEC-02 containment-first auth direction, DEC-03 two-phase webhook acknowledgment, DEC-04 operation-local authorization, DEC-16 clear nine document lints/green checks. DEC-13 is settled by RUL-04/03. Template acceptance/placement is settled; no repeat QA Lead review requested.''')
add('''## L. Preservation constraints

All per-ID Preserve bullets in §B are incorporated verbatim and remain testable obligations. Do not conflate baseline severity with later correction status, collapse distinct FC identities, or alter the certified 97/94/3 register. Raw reviews, pilot records, accepted source templates, all ZIPs and staging indexes remain unchanged.

Across auth/data: one authoritative role table; narrow independently authorized creation-time transport; server-resolved first-render identity; RLS user ownership with explicit public-access decisions; schema-first modeling; small/selectively persisted stores; behavioral AUTH-WALK/live-DB evidence beyond a green build.

Across payments/API: separate money truth, permission and entitlement; server-only subscription writers; raw-body signature verification; kit/scope boundaries; server-only secrets; private data uncached; wire/UI type separation; existing negative tests. Keep authentication versus authorization, server execution versus trusted input, authenticity versus processing, deduplication versus ordering, outbound versus inbound idempotency, and mirror versus provider truth distinct.

Preserve Designer/Extractor responsibilities, conversion/greenfield routing, module inheritance from Factory level, Plan Mode, mandatory acceptance contracts, QA independence, exact verdict vocabulary, cleanup and evidence retention, Gate D applicability, and human release authority. Required QAM packaging does not define TRM, import ABM/APBM methodology, authorize tooling or retroactively rewrite already-running modules.''')
for domain_path in ['factory-corrections/04_auth_data_security_corrections.md','factory-corrections/05_api_commerce_corrections.md']:
 raw=Path(domain_path).read_text();start=raw.index('**Domain preservation');end=raw.index('\n---',start)
 add('### Verbatim domain-wide preservation — `'+domain_path+'`\n\n'+raw[start:end])
add('''## M. Expected validation and evidence contract

1. Re-hash all immutable intake sources and compare the installed 25 templates to the approved translation plan. Current Engineer integrity checks are in INTAKE_VERIFICATION.txt; independent QA repeats against committed snapshot and candidate.
2. Check FC uniqueness/coverage: 97 records, 94 YES, FC-085/086/097 NO, certified severity B6/H36/M44/L11. Source fields remain unchanged; no source proposal becomes approved without the ruling.
3. Re-run SEARCH_QUERIES over candidate live scope; every CHANGE resolves to approved edits, every retained active hit has defensible disposition, and no new contradiction remains. Check examples, stubs, checklists, handoff/startup instructions, role tables and workflow diagrams, not just new playbooks.
4. Verify mandatory QAM in FFM/BIM/FIX/FEAT/RRM packaging; Architect preparation, Engineer facts, Executor Q1, Lead plan approval, Director release, Q2 and conditional repair/retest, required cleanup, Lead certification and Architect closeout remain distinct. Verify QA branch starts at the exact committed engineering candidate and repairs stay on it.
5. Verify module records under agent_docs and production exclusion by applicable inputs plus actual artifact inspection. The folder name alone and tsconfig alone do not prove exclusion.
6. Verify frozen requirements with declared writable output lanes; no test-plan amendment changes acceptance without approval.
7. Recompute MANIFEST totals, reverse edges and scoped body appendix; compare rows to actual headers and CHANGELOG entries. Derive write/archive counts from approved rows.
8. Run all four existing lints: expected exit 0 after DEC-16 document corrections. No script or CI exemption changes. Preserve raw baseline evidence, not a fictitious baseline PASS.
9. Archive proof: expected outgoing archive blob equals `git rev-parse BASE_SHA:path`; working/staged/committed comparisons use Git-object hashes. The optional historical v1.0 restore uses the separately identified historical blob. Tony performs all staging/commits.
10. Resolve all canonical path/heading references and snapshot/template links. Explicitly verify Q9.4 and SFP Engine definitions before new drafts cite them.
11. Recompute FC-074 contrast from landed HSL, exercise code examples/contract negative cases at the claimed level, and obtain pinned kit evidence before kit-specific closure. This drafting task does not claim runtime/vendor behavior was tested.
12. Fable derives the LARGE acceptance spec from the approved map and standing invariants; Tony approves at Gate 3. Independent fresh-session QA records its own candidate identity. Cody’s drafting checks are not an independent verdict.

Exact raw evidence records include command, working directory, exit code and unfiltered safe output; prevent secret capture at collection rather than trimming failures from the record.''')
add('''## N. Write-load tally, run-state and preservation/commit plan

Counts derive from the enumerated rows. Current proposed canonical existing-document set is in the §C version table; new tier documents = three §D rows; template destinations = 25 TEMPLATE_INSTALL_PLAN rows. Historical archive restoration = one conditional FC-089 item. Exact workflow/draft replacements = PROPOSED_EXACT_EDITS rows. MANIFEST and CHANGELOG are infrastructure, not new canonical docs. Before freeze, re-enumerate any partial approval and merge overlapping edits; never count an FC as a unique document.

**Current lawful planning writes:** this existing run folder’s map, ledger, mapping parts, exact-edit/template/contrast proposals and verification records; session_2026-10-15.md; RECOVERY.md; timestamped response files. Existing uncommitted correction/intake work and Tony’s AGENTS.md remain preserved, not newly authorized edit surfaces. RECOVERY_STATUS.txt lists the pre-takeover path set exactly; PRESERVATION_BASELINE.json checks protected file bytes. No approved map existed at takeover, so this is not falsely called a subset of a previously approved §N.

**Preserve before execution:** Tony records the review-branch work in an identifiable preservation commit (Option 1 recommendation); no merge of the review branch into main is implied. Keep all tracked/untracked material; do not stash/reset/discard to obtain a clean tree. Use an isolated execution worktree from approved BASE if Tony selects that path; transfer only the approved run/cargo artifacts after preservation, never the older skill family. Reconcile a moved main/base before creating the execution branch.

**Commit sequence, Tony executes:** preservation commit on review branch → actual approved cargo drop / Gate 1 intake snapshot → approved map and Gate 3 spec → execution branch at approved BASE / run-state checkpoint → one commit per approved canonical document (archive, header, body, history, MANIFEST/CHANGELOG, lint before commit) → derived-index update → CONTENT_SHA recorded outside frozen map → durable handoff/snapshot commit → Gate 4 publication approval → metadata-only approval commit → Tony push → independent QA / authorized repair cycles → Tony final integration. No Git mutation was run by Cody. Plain hyphens, no Co-Authored-By, one version bump per doc per unmerged run.

**Command blocks:** OPERATOR_NEXT_STEPS.md contains scoped preservation and drop commands for Tony to review and run at the appropriate gate. They are not executed by this map or by the Engineer.''')
add('''## O. Approvals and amendments

- [ ] Gate 1 — Director approves actual scope/classification, including explicit conditional/split/deferred accounting. No approval recorded.
- [ ] Actual cargo drop and immutable snapshot verified. Not performed.
- [ ] Gate 2 — Director approves the executable UPDATE MAP, exact wording, complete propagation dispositions, BASE, route, NO-CHANGE guards and explicit resolutions/deferrals. Not recorded. K-MAP-FREEZE remains a mandatory check.
- [ ] Gate 3 — independent QA Lead acceptance spec approved by Director. Not authored by this Engineer.

Current explicit authorization: Tony’s takeover instruction continues drafting through review without another go. It does not release canonical implementation. Current explicit override: all Git mutations remain Tony-only; no fetch/checkout/add/commit/push was performed. Current seats override the skill’s example persona assignments.

After Gate 2 approval this map freezes. CONTENT_SHA, Gate 4, publication and later execution records go in SYNC_HANDOFF.md / RUN_SUMMARY.md, not into this frozen map. Changes after freeze require AMENDED-v<n> and reapproval at the relevant gates.''')
add('''## P. Route evidence

| Fast-path condition | Evidence | Holds? |
|---|---|---|
| At most three intake IDs | 97 FCs plus 36 harvest items and supporting source units | NO |
| At most three touched canonical docs | §C enumerates changes across all five tiers | NO |
| No new canonical doc | Three playbooks proposed | NO |
| No Factory-wide terminology/lifecycle change | QAM, seats, branch lifecycle and Engine crosswalk | NO |
| No cross-correction dependencies | Auth, webhook, checkout, artifact ownership and workflow families overlap | NO |
| No high-risk governing rules | Authorization, money authority, QA verdict, release/Git authority | NO |
| No unresolved conflict | §K has explicit OPEN rows | NO |
| No cross-boundary requirement for complete outcome | Kit/root/skill portions remain §J; scope split needs approval | NO for full 94-finding closure |
| Bounded complete propagation before freeze | Search evidence exists; final semantic disposition/exact selected recipe spans are part of K-MAP-FREEZE | Must be satisfied; not waived |
| Docs-only waiver | Independent review requested and campaign-scale | No waiver proposed |
| **Route** | **LARGE, independent QA after approved map/spec** | **LARGE** |

**Review request:** Jarvis reviews the proposed reconciliation and recommends rulings; Tony records the policy choices and scope/classification disposition. Do not stamp Gate 2 or release implementation until K-MAP-FREEZE and intake/preservation prerequisites are actually met. No additional go was requested or needed for this drafting work.''')
(R/'UPDATE_MAP.md').write_text('\n'.join(out));print('UPDATE_MAP saved:',len('\n'.join(out).splitlines()),'lines;',len(paths),'existing-doc proposals')
