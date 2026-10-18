from pathlib import Path
import re,json,csv,collections,hashlib,datetime
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');O=R/'PROPOSED_CONTENT';H=R/'PLANNING_HISTORY/PRE_MC_CORRECTION_2026-10-16';ed=json.loads((R/'SELECTED_EXACT_EDITS.json').read_text());idx=json.loads((R/'EXECUTION_PROPOSAL_INDEX.json').read_text());status=json.loads((R/'POST_VERIFICATION_STATUS_TRANSITIONS.json').read_text());counts={'existing_tier':31,'new_playbooks':3,'templates':25,'outgoing_archives':31,'restored_archive':1,'infrastructure':2,'workflow_documents':4,'workflow_assets':4,'paths':len(idx),'ordered_edits':len(ed),'changelog_rows':39,'tier_docs':34,'transitions':len(status['transitions']),'transition_paths':len(set(x['path'] for x in status['transitions']))}
(R/'PROPOSAL_COUNTS.json').write_text(json.dumps(counts,indent=2)+'\n')
# Retain Fable's unaffected verification as attributable prior evidence; do not overwrite it.
rows=list(csv.DictReader((H/'PROPAGATION.tsv').open(),delimiter='\t'))
for x in rows:
 current=(O/x['path']).read_text()
 if x['quote'] not in current:
  x['disposition']='CHANGE';x['review_state']='ENGINEER MC-CORRECTED exact proposal';x['reason']='Exact source occurrence is replaced/withdrawn in the current EXECUTION_PROPOSAL.patch; MC correction IDs are in SELECTED_EXACT_EDITS and the disposition record. Not an FC closure or independent verdict.'
 elif x['disposition']=='HISTORY':x['review_state']='HISTORICAL SOURCE ROW RETAINED';x['reason']='Original dated/version log retained. RECON report/history fence boundary repaired under MC-02; current history tables are checked structurally. This records history, not current instructions.'
with (R/'PROPAGATION.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
prop=dict(collections.Counter(x['disposition'] for x in rows));assert len(rows)==2236
m=(H/'UPDATE_MAP.md').read_text()
def sec(letter,body):
 global m
 rg=re.compile(r'^## '+letter+r'\.[^\n]*\n[\s\S]*?(?=^## [A-P]\.|\Z)',re.M);m,n=rg.subn(lambda _:body.strip()+'\n\n',m,count=1);assert n==1,letter
m=m.replace('# UPDATE MAP — doctrine-part2 — Phase 2 reconciliation','# UPDATE MAP — doctrine-part2 — Phase 2 MC correction pass')
intro='''**Current revision:** MC-01…MC-14 correction pass, prepared under Tony’s explicit 2026-10-16 assignment. The earlier 16:47 handoff is superseded for current review and preserved unchanged. Fable’s review and 36-AC draft specification are preserved byte-for-byte; no independent acceptance of these corrections is claimed. Gate 2 remains unapproved, Gate 3 remains pending Fable finalization/Tony approval, Phase 3 is not released.

'''
a=m.index('## 0.');m=m[:a]+intro+m[a:]
sec('A','## A. Selected scope, rulings and actual intake\n\n'+(R/'SELECTED_SCOPE_LEDGER.md').read_text()+'\n\nActual immutable intake: INTAKE_RECEIPT.md / INTAKE_SNAPSHOT_INDEX.json, 189 files. New derivative workflow publications are authorized by Tony’s MC correction assignment; originals remain immutable. No new intake/classification process. Copy these exact selected sets into the future handoff and Gate Q accounting; SYNC_HANDOFF_DISPOSITIONS.template.md is a preparation copy, not a completed handoff or QA verdict.')
sec('C',f'''## C. Exact proposed execution content

Current full proposal: EXECUTION_PROPOSAL.patch, EXECUTION_PROPOSAL_INDEX.json and PROPOSED_CONTENT/. {len(ed)} ordered content edits replay deterministically over the pinned baseline; SELECTED_EXACT_EDITS.json includes prior 334 edits plus bounded MC corrections. SELECTED_CONTENT_INDEX.json is the pre-metadata stage; the final index is authoritative for file bytes. NEW_DOCUMENT_PROPOSALS.json / MC_NEW_DOCUMENT_EDITS.json record new-playbook integration; DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json records 31 outgoing originals and the one version bump/history-row mechanics.

Exact footprint: {len(idx)} paths = 31 revised tier documents + 3 new playbooks + 25 accepted-template translations + 31 outgoing archives + 1 historical QA restore + MANIFEST/CHANGELOG + 4 workflow documents + 4 SVG stick diagrams. Eight new derivative paths explain 93 → 101; four workflow publication rows explain CHANGELOG 35 → 39. Tier count remains 34; workflow companions are nested references under the owning playbooks, not extra tier rows. PROPOSAL_COUNTS.json and the enumerated index are the count authority.

All new words, diagrams, structural fixes and conditional closeout edits remain ENGINEER-PROPOSED for Gate 2. No approval is inferred from a generated file. Future implementation dates bind only the 151 named header/row fields in LANDING_DATE_PLAN.json; approval/source dates are preserved. Recompute execution and closeout hashes for the actual landing date and record that mechanical binding; never claim the planned 2026-10-16 was the actual landing date before it occurs.''')
sec('D','''## D. New playbooks, accepted templates and revised workflow publications

Three proposed playbooks retain DRAFT status pending actual verification. Source drafts/substitution ledger remain unchanged; RUL-01…15 supply bounded authority. Accepted v0.3 templates remain settled; PHASE_2_TEMPLATE_TRANSLATIONS.json is the sole current pre-verification translation/hash plan. TEMPLATE_INSTALL_PLAN.md/json are explicitly HISTORICAL and superseded; TEMPLATE_INSTALL_CHECKS.md preserves their eight required checks. No repeat acceptance review is requested. Actual installation remains pending.

WORKFLOW_PUBLICATION_PLAN.json enumerates four revised workflow documents under 03_BUILD_METHODOLOGY/_workflows/ and four matching SVG stick diagrams under _assets/workflows/. Each derivative references its unaltered August source in the snapshot and states exactly when it supersedes that source for current instructions. FFM creation, engineering/QA/post-FFM review, deployment/Gate D and BIM/Engine 2 are covered. SFP, Blueprint, FFM, BIM, RRM and Deployment link the relevant publications. Original diagrams remain historical; leaving them merely unreferenced is no longer the proposed outcome.

POST_VERIFICATION_STATUS_TRANSITIONS.json names 12 exact future spans on nine paths: original five spans, three matching MANIFEST rows and four workflow-document status lines. POST_VERIFICATION_PROPOSAL.patch/index and CLOSEOUT_PROPOSED_CONTENT show the exact pre/post difference. Intended commit: Tony’s bounded closeout to activate verified doctrine/workflow references and installed-template provenance after accepted product QA, actual installation verification, required cleanup acceptance and Architect closeout instructions. Its actual SHA is null/PENDING until Tony creates it; record it afterward in a subsequent receipt. Actual TEMPLATE_INSTALL_VERIFICATION.md, RUN_SUMMARY.md and CLOSEOUT_VERIFICATION.md remain PENDING and absent. EVIDENCE_TEMPLATES are forms only.

Independent QA must bound the closeout retest to AC25/27/31/32/33, all twelve spans, the actual nine-path diff, template comparison including the one README transition, and workflow reference/diagram consistency. QA Lead accepts the post-closeout evidence/verdict; a pre-transition PASS does not certify later changed bytes. Gate 2 includes this proposed sequence; nothing executes during Phase 2.''')
sec('E','''## E. Replaced and superseded material

- MC-01 replaces malformed historical-pointer lines inside their actual table/list/blockquote containers, including the FFM availability claim.
- MC-02/13 repair the RECON report-template fence boundary so its existing history is an actual table; HANDOFF uses its existing four-column Versioning table. No appended duplicate history/after-footer rows.
- MC-03 inserts all 39 current CHANGELOG rows in the Ongoing entries table. MC-09 preserves existing status suffixes; MC-10 preserves the bump-procedure pointer and CI-parked guidance.
- Blueprint phase labels and deployment/Gate D return in both flows. FFM/BIM actual lifecycle, boot/checklist and ownership/freeze wording are reconciled; a paragraph beside stale contradictory text is insufficient.
- Old August pictures remain exact historical sources. Four revised published workflow/diagram pairs supersede their instructions only after approved verified landing. Historical persona names, kit filenames and authority assumptions are not transported into the new derivatives.
- Existing unsafe-example withdrawals and dependency/deferral records remain; no full finding closure is inferred from containment. FC-085/086/097 remain NO correction.''')
sec('F',f'''## F. Propagation and MC verification

All 2,236 original baseline-hit identities/quotes remain in PROPAGATION.tsv with current Engineer dispositions: {json.dumps(prop)}. Earlier semantic checks are retained as prior Engineer evidence, not a waiver of Fable’s findings. MC_PROPAGATION.tsv and MC_PROPAGATION_QUERIES.json supply the targeted correction-pass searches and per-hit context. MC_VERIFICATION.json/raw evidence cover replay/baseline/hashes, Markdown tables/fences/containers/footers, workflow/diagram/reference agreement, current template translations and post-verification transitions. New exact wording requires independent review; no Engineer correction is Fable acceptance.''')
sec('G','''## G. Metadata, archives and conditional status rows

MANIFEST derives all 34 rows from full current headers, including meaningful status suffixes. It retains “How this stays current”, the _ARCHIVE/README.md bump pointer and the parked CI note. Only unsupported tag/universal-path assumptions are removed. Reverse dependencies and body appendix are recomputed from actual tier content. Workflow documents/diagrams are governed nested companions; CHANGELOG records their four publications. Thirty-one histories use the existing parsed table shape/order; no template/example table receives the document row. All 39 current CHANGELOG rows are inside its intended table.

Outgoing archives remain baseline-identical, restored QA v1.0 remains exact historical blob bb41260f6b6f94372a682f04b313a451f2b3c4b1. No infra archive or second version bump is proposed. After actual verification, the exact QAM/RRM/Deployment MANIFEST rows change atomically with their matching headers in the named Tony closeout commit; then bounded independent checks revalidate row/header equality. Both pre- and post-transition hashes are explicit, bound to actual implementation date at execution.''')
sec('H','''## H. Paths, links, workflows and assets

QAM canonical destination remains 03_BUILD_METHODOLOGY/_templates/QAM/ (AD-01); module QAM remains under project agent_docs with actual production exclusion verified. Snapshot/template provenance links are real. No universal project landing path is invented.

Eight new workflow paths are explicit in WORKFLOW_PUBLICATION_PLAN.json and the 101-path index. Every SVG is referenced by its matching workflow document; all workflow docs are linked by owning tier documents, cite governing sections and link preserved original sources. SVG and numbered prose sequences derive from the same step data. This replaces the previous “no new assets” scope statement under Tony’s current explicit requirement; it does not edit the historical original images or Fable’s draft AC28.

RRM §2 resolves to the SFP Phase Vocabulary table containing Engine 1, post-FFM review, Engine 2 and RRM rows. Blueprint states lifecycle Phase 0…5 including deployment/Gate D. Recon/Engineer lifecycle citations resolve; MANIFEST FFM purpose no longer describes a four-role pattern. Q9.4 stays a new stable ID and Q9.1…3 remain unchanged.''')
# K preserves attributable ruling text; append correction-pass clarifications without reopening eight votes.
kstart=m.index('## K.');kend=m.index('## L.',kstart)
k=m[kstart:kend];k+='''### Current correction-pass clarifications

Q-1 is addressed by Tony’s explicit requirement in this assignment: “Prepare revised published versions, with references and a clear supersession note”. Original RUL-07 history is preserved; new derivatives are proposed as required. Q-3 follows the same assignment: “Preserve meaningful existing status and versioning guidance unless an approved ruling supersedes it.” Status suffixes and bump/CI guidance are retained. Q-2 is concretely proposed in §D and the transition record: named Tony closeout commit after actual evidence/product verdict/cleanup acceptance, followed by bounded independent retest. Gate 2 approval must cover that exact plan; no fabricated separate ruling is asserted.

Fable’s unchanged draft AC28 says “no new assets”; Tony’s current assignment requires revised stick diagrams. Recommendation: Fable re-anchor AC28 to allow exactly the four declared SVG assets and their four workflow references, with linkage/preservation checks. Counts, history rows, traceability and closeout-span ACs also need her re-anchoring/finalization. These are independent-spec dependencies before Gate 3, not an Engineer-authored spec amendment.

''';m=m[:kstart]+k+m[kend:]
sec('M','''## M. Verification and retained evidence

Repeat only checks affected by MC changes: deterministic ordered-edit/full-tree regeneration and hashes; before-hash/baseline agreement; Markdown structure (pointers, tables, history, fences and footer placement); existing unchanged lints; cross-document lifecycle/ownership/freeze/review propagation; all four revised workflow/SVG/prose sequences and local links; 25-file source-preservation/translation replay; both pre/post-closeout MANIFEST/header equality; 97 certified dispositions plus W01…23/RUL01…15/AD01 traceability; exact 101 paths, 39 rows, 12 transitions and nine closeout paths. MC_VERIFICATION.json and raw evidence record actual preparation results only.

Retain Fable’s 429-hash/334-edit/93-path/25-template/archive/lint verification as prior independent evidence for the earlier package. Repeated checks are necessary because the proposed bytes/counts/structure changed. Accepted source hashes, original drafts, snapshot, protected originals and historical archive identities remain unchanged; no fresh template acceptance review or runtime/platform tests.

Future actual candidate checks include actual installation (not proposal replay), actual landing-date binding, original archive Git-object fidelity after Tony stages/commits, independent QA at its observed candidate, authorized repair/retest and the bounded post-transition checks. Required raw evidence includes command, cwd, exit and unfiltered safe output. No Fable verdict or completed future evidence is supplied by Cody.''')
sec('N','''## N. Execution setup, lawful run state and commits

Phase 1 COMPLETE; Phase 2 current correction pass. Tony performs ALL Git mutations. Current review branch/HEAD and proposed baseline remain as §0; no fetch or new worktree by Cody. OPERATOR_NEXT_STEPS.md provides scoped preservation/base/worktree commands. Preserve the review branch and all source work; never merge its older skill copy into main.

Expected run-state surface: this existing run’s proposals, immutable snapshot, preserved planning history, review/spec (Fable-owned, Cody read-only), verification evidence, generators, workflow proposals, inventories and delivery records; root RECOVERY/session/response bookkeeping. Existing correction/intake changes are preserved as earlier authorized work; canonical tiers/MANIFEST/CHANGELOG/_ARCHIVE/skills/CI remain untouched. MC_CORRECTION_PROTECTED.json and PRESERVATION_BASELINE.json pin protected material. OPERATOR_PRESERVATION_PATHS.nul enumerates the actual scoped preservation paths; inspect before staging.

Run-only commit plan: Tony preservation checkpoint; approved isolated execution base; one implementation commit of the agreed map (RUL-15 override); necessary metadata/publication records and bounded QA repair commits; named Tony status/provenance closeout commit under §D with independent bounded verification; eventual PR merge/local-main synchronization. No new release tag or skill rewrite. No planned commit SHA is a completed identity. CONTENT_SHA and later actual SHAs belong in handoff/RUN_SUMMARY receipts after they exist, not a frozen map.''')
sec('O','''## O. Current gates

- Phase 1 scope: approved by Tony, 2026-10-16, RUL-08…15.
- Actual intake/snapshot: 189 exact files present, unchanged; operator preservation still pending.
- Phase 2 MC corrections: Engineer-prepared and verified; MC_CORRECTION_DISPOSITIONS.md records MC-01…14. Jarvis review and Fable confirmation/finalization remain required; no acceptance claimed.
- Gate 2 exact map: NOT APPROVED. Includes all proposed wording, 101 paths, derivative workflows/diagrams, exclusions, date binding and the exact conditional closeout sequence.
- Fable’s independent 36-AC DRAFT spec: present and byte-preserved. Fable must re-anchor/finalize against the corrected approved map. Gate 3 Tony approval remains pending.
- Tony’s preservation/base/worktree receipts and execution setup verification: pending.
- Phase 3: NOT RELEASED.

Continuous execution applies within the released assignment. No future implementation, installed verification, closeout commit, independent verdict, publication or merge is fabricated. After eventual Gate 2 freeze, substantive map changes require the governing amendment process.''')
# Keep original verbatim §B and preservation constraints unchanged.
a=m.index('**Review request:**');m=m[:a]+'''**Review request:** Jarvis reviews the corrected map and every MC disposition. Fable confirms corrections and independently finalizes/re-anchors her specification; Tony approves Gate 2 and Gate 3 in the proper order, verifies preservation/execution setup receipts and releases Phase 3. No additional correction-pass go is requested.
'''
(R/'UPDATE_MAP.md').write_text(m)
# Replace stale current handoff/phase pointers; historical sources stay unchanged.
(R/'PHASE_PLAN.md').write_text('''# Six-phase status — MC correction pass

| Phase | Status | Remaining dependency |
|---|---|---|
| 1. Finalize scope | COMPLETE | Eight bounded Director rulings recorded |
| 2. Prepare execution | CORRECTION PASS PREPARED; review/operator gates pending | MC-01…14 disposition/evidence, corrected map, workflows and revised package; Jarvis/Fable review, Gate 2, Fable spec finalization/Gate 3, Tony setup receipts |
| 3. Update documents | NOT RELEASED | Approved exact map/spec, verified setup and implementation release |
| 4. Verify and repair | NOT STARTED | Actual installation/semantic checks; independent QA and bounded repair/closeout verification |
| 5. Publish and merge | NOT STARTED | Required release/verdicts; Tony Git/PR/merge |
| 6. Sync local main and close | NOT STARTED | Tony local-main synchronization, actual identity and durable closeout checks |

No canonical implementation, Git mutation, independent acceptance or completed future verification is claimed by this preparation.
''')
print('Map A/C/D/E/F/G/H/K/M/N/O reconciled; original source intent/preservation retained; current gates truthful.')
