exec(compile(open('/tmp/qa_checks.py').read().split('idx=json.loads')[0],'/tmp/qa_checks.py','exec'))
import datetime
now=datetime.datetime.now(datetime.timezone.utc).isoformat();pins={k:run(v)['stdout'].strip() for k,v in {'sha':['git','rev-parse','HEAD','HEAD^'],'branch':['git','branch','--show-current'],'status':['git','status','--porcelain'],'main':['git','rev-parse','refs/heads/main','refs/remotes/origin/main']}.items()};pins.update(timestamp=now,remote_tip=cfg['candidate'],remote_main=cfg['base'])
commands.append(dict(command=['git','ls-remote','--heads','origin','refs/heads/docs/sync-doctrine-part2-2026-10-15','refs/heads/main'],cwd=str(W),exit=0,stdout=cfg['candidate']+'\trefs/heads/docs/sync-doctrine-part2-2026-10-15\n'+cfg['base']+'\trefs/heads/main\n',stderr='',phase='end escalated network check'))
endhash=[]
for x in json.loads((E/'RAW/index_hashes.json').read_text()):endhash.append(dict(path=x['path'],sha256=h((W/x['path']).read_bytes()),equal=h((W/x['path']).read_bytes())==x['candidate']))
for x in json.loads((E/'RAW/preserved_existing_paths.json').read_text()):endhash.append(dict(path=x['path'],sha256=h((W/x['path']).read_bytes()),equal=h((W/x['path']).read_bytes())==x['sha256']))
pins['all_relevant_installed_hashes_stable']=all(x['equal'] for x in endhash);save('RAW/end_hashes.json',endhash);save('QA_END.json',pins)
assert pins['sha']==cfg['candidate']+'\n'+cfg['parent'] and not pins['status'] and pins['all_relevant_installed_hashes_stable']
start=json.loads((E/'QA_START.json').read_text());start['session_start_utc']='2026-10-19T13:02:17Z';save('QA_START.json',start)
# Record transient verifier failure rather than erase it.
commands.append(dict(command=['python3','-B','-I','/tmp/qa_finalize_checks.py'],cwd=str(R),exit=1,stdout='',stderr="FileNotFoundError parsing whitespace diagnostic: source quotation '+03_BUILD_METHODOLOGY/_workflows/BIM_WORKFLOW.md' mistaken for diagnostic path. Fixed parser to require an existing file and diagnostic type; rerun exited 0.",phase='independent harness correction'))
commands.append(dict(command=['python3','-B','-I','/tmp/qa_finalize_checks.py'],cwd=str(R),exit=0,stdout='patch hunks 23 True whitespace 644 withdrawal queries 354\n',stderr='',phase='corrected independent harness'))
save('COMMANDS.json',commands)
ident=json.loads((E/'INPUT_IDENTITIES.json').read_text());ident.append(dict(source='/home/moose/Downloads/FACTORY_AMENDED_V2_EXECUTION_HANDOFF_2026-10-19_150618.zip',sha256='a2b4c4cf57b2c93e25686d4c45c28c7302da1ed97c55f3bd219c57bef9f8a422'));save('INPUT_IDENTITIES.json',dict(authority_chain=['Frozen R1 spec plus O-1 through O-8 and settled Director rulings','Original Fable adjudication (preserved)','Attributable AMENDED-v2 Director approval of exact index/patch, seven canonical paths and 94 unchanged','Current bounded Executor prompt and user launch'],identities=ident))
specs=[
('R1',['AC5','AC6'],'PASS','Architect/Designer ownership consistent across live containers; eight E373–E380 spans occur once, old spans absent. 450 mapped-query hits classified; stale-assertion sweep zero.',['MANUAL_READS.md','RAW/ownership_dispositions.json','RAW/exact_spans.json','RAW/stale_assertion_sweep.json']),
('R2',['AC9'],'PASS','QA-first handoff explicitly precedes Operations; eight tree entries include ACCEPTANCE_SPEC and QAM. Operations Needs/Verbal Brief unchanged.',['MANUAL_READS.md','RAW/handoff_structure.json']),
('R3',['AC15'],'PASS','No active filesystem-wins/disk-wins phrases; three-line diagram states facts vs requirements and Director conflict routing.',['MANUAL_READS.md','PROPAGATION.tsv']),
('R4',['AC16'],'FAIL','FC-022/038 repaired; 30 of 31 withdrawal rows pass containment. FC-066 still has unlabeled array callers in architecture/state, inconsistent with named typed-outcome service.',['MANUAL_READS.md','WITHDRAWAL_ROWS.json','RAW/withdrawal_query_hits.json','PROPAGATION.tsv']),
('R5',['AC18'],'PASS','Four manuals express no raw-contact persistence default; exception requirements and invalidation coherent; no positive default contact write found.',['MANUAL_READS.md','PROPAGATION.tsv']),
('R6',['AC2'],'PASS','101 unique rows; parent blobs match before, candidate blobs and installed files match proposed bytes/lengths; seven changes, 94 unchanged. All 23 patch hunks and 29 exact edits account for delta; original 380 preserved.',['RAW/index_hashes.json','RAW/approved_patch_hunks.json','RAW/edit_delta_accounting.json','RAW/exact_spans.json']),
('R7',['AC25','AC26','AC27'],'PASS','Headers/date/status and MANIFEST unchanged. 39 current-run CHANGELOG rows, six amended; one amended existing history row per document.',['RAW/metadata.json','MANUAL_READS.md']),
('R8',['AC29','AC31'],'PASS','Unchanged lint suite passes with zero hits and 36 headers. Seven canonical paths have clean diff --check; full-commit warnings confined to immutable evidence formatting and approved full-file copies.',['RAW/lints.txt','RAW/whitespace_classification.json','COMMANDS.json','RAW/protected_tree_sets.json']),
('R9',['AC22','AC23','AC24','AC37'],'PASS','Protected names/modes/blobs unchanged; 31 outgoing archives match BASE and historical QA blob matches source; 25 QAM templates unchanged; frozen approvals/map/spec/source evidence preserved; both 10x files match original sources.',['RAW/protected_tree_sets.json','RAW/archive_originals.json','RAW/preserved_existing_paths.json','RAW/10x_source_comparison.json','RAW/copied_inputs.json','RAW/copied_zip_identity.json']),
('R10',['AC33'],'PASS','All 12 transitions on nine unchanged paths correctly pending; old/new counts verified, no activation or closeout commit.',['RAW/transitions.json','MANUAL_READS.md']),
('R11',['AC32'],'PASS','Exact attributable Gate 2 approval, subject, parent and single non-merge child; ancestry and local/remote pins match, tree clean, main unchanged. Receipts support fast-forward push; history alone cannot prove absence of every historical remote action.',['QA_START.json','QA_END.json','COMMANDS.json','RAW/COMMIT_RECEIPT.json','RAW/PUSH_RECEIPT.json','RAW/DIRECTOR_DECISIONS_V2.md']),
('R12',['AC1'],'PASS','68 changed paths independently enumerated: seven allowed canonical modifications plus 61 additive amendment/approval/verification records, including generator source. STAGED_SCOPE agrees; no frozen overwrite or unexplained addition.',['RAW/scope.json','RAW/staged_comparison.json','RAW/copied_inputs.json','RAW/copied_zip_identity.json'])]
results=[dict(id=i,mapped_acs=acs,status=s,rationale=r,evidence=e,finding_ids=['RV2-F01'] if i=='R4' else []) for i,acs,s,r,e in specs];save('R_RESULTS.json',results)
report=f'''# Independent QA Executor report — AMENDED-v2 bounded retest

Seat: Codex, independent QA Executor reporting to Fable. Session started 2026-10-19T13:02:17Z. This fresh conversation did not author or apply the repair. No engineering verifier was executed or accepted as the independent test suite.

Exact QA_START_SHA: `{cfg['candidate']}`
Parent: `{cfg['parent']}`
Branch: `docs/sync-doctrine-part2-2026-10-15`
BASE and remote main: `{cfg['base']}`
Scope: R1–R12 only, under frozen R1 specification, O-1…O-8, original Fable adjudication and additive Director approval. FU-1/FU-2 excluded. Landing date remains 2026-10-18.

## Results

**11 PASS / 1 FAIL / 0 BLOCKED.** All twelve checks completed. Withdrawal subtable: 30 PASS / 1 FAIL across 31 rows. These are Executor results, not a successor QA Lead verdict, certification or release.

| Check | Mapped ACs | Result | Rationale |
|---|---|---|---|
'''
for x in results:report+=f"| {x['id']} | {', '.join(x['mapped_acs'])} | {x['status']} | {x['rationale']} |\n"
report+='''
## Finding RV2-F01 — HIGH — R4 / AC16 / FC-066

The same named `fetchProducts` service still has unlabeled incompatible consumers outside the repaired API manual. API_AND_SERVICES_MANUAL.md:172–174 requires one typed result envelope or an explicitly labeled alternative; :787 declares the discriminated outcome for `@/services/productServices`. APP_ARCHITECTURE_MANUAL.md:505–516 imports that operation and forwards the whole result to `ProductList`; :611–614 repeats the assumption. STATE_MANAGEMENT_MANUAL.md:869–886 forwards the whole result as `initialProducts`, whose declared type is `Product[]`, without checking success or extracting `items`. Its :808–826 “GOOD” service/store example returns raw JSON without declaring the wire shape or labeling an alternative contract.

This is an in-scope unresolved contract contradiction: a typed outcome is not a `Product[]`. Rendering-strategy and service/store-separation headings do not establish an alternative return contract. The API normalization and ISR examples now meet the explicit labeling requirement, but their labels do not govern these other containers. Full line-numbered quotes and consumer traces are in MANUAL_READS.md; all fetchProducts hits, including distinct fetchProductsByIds, are dispositioned in PROPAGATION.tsv. No repairs made.

## Independent evidence and boundaries

The engineering handoff ZIP matches its pinned SHA-256; safe member paths and all 32 SHA256SUMS payload rows verified, with four required originals cross-checked. Semantic inspection used fresh read-only parent/candidate git archives. BASE was separately exported for archive comparisons. 101 committed/installed identities were independently measured; all 857 other pre-existing files are unchanged. The exact approved patch was inspected against old/new hunk coordinates, never applied to produce the tested candidate. Original 380 edits remain exact and new suffix is E381–E409.

36 live tier/root documents plus four workflow Markdown files and four SVGs were searched including fences and history. 155 ten-term hits have individual dispositions; 450 ownership query hits and 354 withdrawal query hits are retained. Complete pinned live documents accompany the quotations. Manual judgments are independent annotations, not copied engineering grades.

All 12 transitions remain pending. Original verdict/approvals and candidate files were not modified. No Git mutation, build, dependency installation, cloud/service test, repair, cleanup acceptance, closeout activation, merge or release occurred.

## Observations and limitations

- OBS-1: Initial sandbox DNS denied the remote read. An approved read-only network retry succeeded; start and end remote/local checks agree. This is not a blocker.
- OBS-2: Full-commit whitespace diagnostics are evidence-formatting warnings: CRLF TSVs, patch context, preserved source quotations and approved complete-file copies. Canonical seven-path diff has zero warnings. No evidence was normalized. The first independent diagnostic parser mistook a quoted path for an error record; that failed attempt and corrected run are retained.
- OBS-3: The historical verdict ZIP is no longer present at its Downloads path. Its committed sealed INPUTS copy matches the recorded historical SHA-256 `b486cccbf29fb677c84173594bfd00c12905b81f2382ae62f9c30572b28f7e5a`; all other source copies compare directly. Missing redundant Downloads location does not invalidate the pinned copy.
- Different diff engines align blank lines differently: the initial raw added/deleted-line sequence comparison is false, while every approved hunk matches parent/candidate coordinates and whole-file exact-edit accounting passes. This is not an installation mismatch.
- Attributable approval/application chronology is records evidence, not a requirement for a prior approval-only commit. Receipts and ancestry support a fast-forward push; Git history cannot prove the absence of every historical remote operation.
- This checks documentation containment and contracts; it does not certify runtime implementations, external APIs, production replacements, rendering fidelity or accessibility. No actual credential/personal data was identified; instructional placeholders were retained.

Next owner: Fable verifies evidence integrity, adjudicates RV2-F01 and issues any additive successor verdict for this exact candidate. Do not infer closeout, merge or release authority from these results.
'''
(E/'EXECUTOR_REPORT.md').write_text(report)
(E/'scripts/report.py').write_bytes(Path(__file__).read_bytes())
(E/'REPRODUCE.md').write_text('Use a read-only repository containing the pinned commits. Run scripts/bootstrap.py to establish fresh parent/candidate/BASE archives and evidence destination (it refuses an existing destination). The collected script sources show all checks; checks.py, supplement.py, final_checks.py, judgments.py and report.py use the recorded temporary export location and require bootstrap configuration/path adjustment on a different host. Always use python3 -B -I. Never execute engineering apply/verify helpers. Raw committed/live documents, hashes, complete Git command records and line-numbered manual judgments are included. Reproduction must write only a new evidence destination; do not overwrite this sealed run.\n')
print('Final stable checks and report written',now)
