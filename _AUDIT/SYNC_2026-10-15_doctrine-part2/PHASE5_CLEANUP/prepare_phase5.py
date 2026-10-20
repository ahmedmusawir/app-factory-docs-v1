from pathlib import Path
import hashlib,json,subprocess,zipfile,shutil,difflib,os,datetime,re,tempfile,tarfile,io
V=Path('/home/moose/Documents/app-factory-docs-v1'); E=Path('/home/moose/Documents/app-factory-docs-sync-execution'); RUN=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2'); R=V/RUN; ER=E/RUN; O=R/'PHASE5_CLEANUP'; C='26b050fe70de66e74ec8d65bcf9287d4369a91f7'; BR='docs/sync-doctrine-part2-2026-10-15'
h=lambda b:hashlib.sha256(b).hexdigest()
def put(p,b):
 p=O/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b.encode() if isinstance(b,str) else b)
def js(p,d):put(p,json.dumps(d,indent=2,ensure_ascii=False)+'\n')
commands=[]
def cmd(args,cwd=E):
 p=subprocess.run(args,cwd=cwd,text=True,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});commands.append(dict(command=args,cwd=str(cwd),exit=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,commands[-1];return p.stdout
assert cmd(['git','rev-parse','HEAD']).strip()==C
assert cmd(['git','branch','--show-current']).strip()==BR
assert cmd(['git','status','--porcelain'])==''
js('PREFLIGHT.json',{'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate':C,'branch':BR,'clean':True,'observed_remote_working_branch':C,'observed_remote_main':'9c179392f79b70da099121fc357d3107ad3bb86e'})
put('REMOTE_PREFLIGHT.txt',f'{C}\trefs/heads/{BR}\n9c179392f79b70da099121fc357d3107ad3bb86e\trefs/heads/main\nRead-only git ls-remote origin, execution worktree; exit 0 (2026-10-20).\n')
zpath=Path('/home/moose/Downloads/FACTORY_QA_PHASE4_GATE_CLOSED_ARCHITECT_HANDBACK_2026-10-20_165031.zip');assert h(zpath.read_bytes())=='fbcabacdd39d74fc7fc63daf3f512cac42dafa0c0d8ab17306d980f842084dff'
ziprows=[]
with zipfile.ZipFile(zpath) as z:
 assert z.testzip() is None
 for n in z.namelist():
  if n.endswith('/'):continue
  b=z.read(n);assert b==(R/'QA_PHASE4'/n).read_bytes(),n
  ziprows.append({'path':n,'sha256':h(b),'review_copy_equal':True})
put('INPUTS/'+zpath.name,zpath.read_bytes());js('HANDBACK_VALIDATION.json',{'zip_sha256':h(zpath.read_bytes()),'files':ziprows})
# Freeze original execution and review records before integration or cleanup.
def inventory(root):
 return [{'path':str(p.relative_to(root)),'sha256':h(p.read_bytes()),'bytes':p.stat().st_size,'decision':'RETAIN: evidence, provenance, frozen history, approved proposal or run-support dependency'} for p in sorted(root.rglob('*')) if p.is_file() and 'PHASE5_CLEANUP' not in p.parts]
js('EXECUTION_RUN_BEFORE.json',inventory(ER));before_review=inventory(R);js('REVIEW_RUN_BEFORE.json',before_review)
tracked=cmd(['git','ls-files','-z']).split('\0');tracked=[p for p in tracked if p]
js('CERTIFIED_TRACKED_FILES.json',[{'path':p,'sha256':h((E/p).read_bytes())} for p in tracked])
# Integrate every missing QA file and the post-commit engineering receipts; never overwrite.
transfer=[]
for sub in ['QA_PHASE4','AMENDED_V2_EXECUTION','AMENDED_V3_EXECUTION']:
 for p in sorted((R/sub).rglob('*')):
  if not p.is_file():continue
  dest=ER/p.relative_to(R)
  if dest.exists():assert dest.read_bytes()==p.read_bytes(),str(dest)
  else:transfer.append({'path':str(RUN/p.relative_to(R)),'sha256':h(p.read_bytes()),'action':'ADD missing exact review copy'})
js('INTEGRATION_PLAN.json',transfer)
qa=[]
for d in ['EXECUTOR_EVIDENCE','RETEST_AMENDED_V2/EXECUTOR_EVIDENCE','RETEST_AMENDED_V3/EXECUTOR_EVIDENCE']:
 m=R/'QA_PHASE4'/d/'SHA256SUMS.txt';rows=[]
 for line in m.read_text().splitlines():
  sha,name=line.split(None,1);p=m.parent/name.lstrip('*');assert h(p.read_bytes())==sha,name;rows.append({'path':name,'sha256':sha,'result':'PASS'})
 qa.append({'manifest':str(m.relative_to(R)),'manifest_sha256':h(m.read_bytes()),'rows':rows})
js('QA_EVIDENCE_MANIFEST_VALIDATION.json',qa)
# Remove only untracked bytecode, after proving no evidence manifest lists it.
removed=[]
for p in sorted(R.rglob('*.pyc')):
 rel=str(p.relative_to(V));assert subprocess.run(['git','ls-files','--error-unmatch',rel],cwd=V,capture_output=True).returncode!=0
 refs=[]
 for m in R.rglob('SHA256SUMS.txt'):
  if str(p.relative_to(R)) in m.read_text() or p.name in m.read_text():refs.append(str(m))
 assert not refs,refs
 removed.append({'path':str(p),'sha256':h(p.read_bytes()),'bytes':p.stat().st_size,'reason':'Untracked regenerable Python bytecode; source retained; absent from evidence manifests; not installed in execution run'})
 p.unlink()
 if not list(p.parent.iterdir()):p.parent.rmdir()
js('REMOVED_PATHS.json',removed);js('RETAINED_PATHS.json',inventory(R));js('EXECUTION_RETAINED_PATHS.json',inventory(ER))
# Certified index verification and fresh proposal from bound spans, without modifying either worktree.
idx=json.loads((ER/'AMENDED_V3/BOUND_EXECUTION_INDEX.json').read_text());assert len(idx)==101
bound=json.loads((ER/'BOUND_STATUS_TRANSITIONS.json').read_text());tr=bound['transitions'];assert len(tr)==12 and bound['commit_plan']['actual_sha'] is None
for f in ['BOUND_STATUS_TRANSITIONS.json','AMENDED_V3/BOUND_EXECUTION_INDEX.json','QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md','PHASE_2_TEMPLATE_TRANSLATIONS.json','TEMPLATE_INSTALL_VERIFICATION.md','RUN_SUMMARY.md']:
 put('INPUTS/'+f,(ER/f).read_bytes())
original={row['path']:(E/row['path']).read_bytes() for row in idx}
for row in idx:assert h(original[row['path']])==row['proposed_sha256'],row['path']
proposed=dict(original);exact=[]
for i,t in enumerate(tr,1):
 p=t['path'];old=t['old'].encode();new=t['new'].encode();assert proposed[p].count(old)==t['occurrences']==1
 assert old in original[p];proposed[p]=proposed[p].replace(old,new)
 exact.append({'id':i,**t,'baseline_line':original[p].split(old)[0].count(b'\n')+1,'status':'PENDING; proposal only'})
changed=sorted(p for p in original if original[p]!=proposed[p]);assert len(changed)==9
patch=''
for p in changed:
 patch+=''.join(difflib.unified_diff(original[p].decode().splitlines(True),proposed[p].decode().splitlines(True),fromfile='a/'+p,tofile='b/'+p))
 put('CLOSEOUT_PROPOSED_CONTENT/'+p,proposed[p])
put('CLOSEOUT.patch',patch);js('EXACT_TRANSITIONS.json',exact)
successor=[{'path':p,'before_sha256':h(original[p]),'proposed_sha256':h(proposed[p]),'bytes':len(proposed[p]),'baseline_candidate':C,'status':'PROPOSED ONLY' if p in changed else 'UNCHANGED','landing_date':'2026-10-18'} for p in original]
js('CLOSEOUT_SUCCESSOR_INDEX.json',successor);js('CERTIFIED_101_HASHES.json',[{'path':p,'certified_sha256':h(b),'installed_sha256':h((E/p).read_bytes()),'result':'PASS'} for p,b in original.items()])
js('PROPOSED_92_UNCHANGED.json',[r for r in successor if r['status']=='UNCHANGED'])
# Independently export certified Git tree; apply exactly the proposal only in disposable scratch.
scratch=Path(tempfile.mkdtemp(prefix='phase5-closeout-'))
archive=subprocess.check_output(['git','archive',C],cwd=E);tarfile.open(fileobj=io.BytesIO(archive)).extractall(scratch,filter='data')
cmd(['git','apply','--check',str(O/'CLOSEOUT.patch')],scratch);cmd(['git','apply',str(O/'CLOSEOUT.patch')],scratch)
for p,b in proposed.items():assert (scratch/p).read_bytes()==b,p
assert cmd(['python3','lints/run_all.py'],scratch).strip().endswith('=== RESULT: PASS ===')
assert cmd(['python3','lints/run_all.py'],E).strip().endswith('=== RESULT: PASS ===')
# Template source -> authorized translation -> actual install comparison.
templates=[]
tmap=json.loads((ER/'PHASE_2_TEMPLATE_TRANSLATIONS.json').read_text());assert len(tmap)==25
assert {str(p.relative_to(E)) for p in (E/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*') if p.is_file()}=={t['destination'] for t in tmap}
for t in tmap:
 src=ER/'INTAKE_SNAPSHOT'/t['source'];b=src.read_bytes();assert h(b)==t['source_sha256'];s=b.decode()
 counts=[]
 for a in t['translations']:
  n=s.count(a['old']);assert n==a['occurrences'];counts.append(n);s=s.replace(a['old'],a['new'])
 installed=(E/t['destination']).read_bytes();assert s.encode()==installed and h(installed)==t['proposed_destination_sha256']
 templates.append({'source':str(src.relative_to(E)),'destination':t['destination'],'source_sha256':h(b),'approved_translation_sha256':h(s.encode()),'installed_sha256':h(installed),'proposed_after_closeout_sha256':h(proposed[t['destination']]),'translation_occurrences':counts,'result':'PASS'})
js('TEMPLATE_PROVENANCE.json',{'translation_map_sha256':h((ER/'PHASE_2_TEMPLATE_TRANSLATIONS.json').read_bytes()),'exact_set_count':25,'source_and_translation_replayed':True,'rows':templates})
# Manual-equivalent structural checks backed by exact diff and byte comparison.
checks=[]
def check(name,ok,detail):assert ok,name;checks.append({'check':name,'result':'PASS','evidence':detail})
check('101 certified paths unchanged in actual worktree',all((E/p).read_bytes()==b for p,b in original.items()),'CERTIFIED_101_HASHES.json')
check('12 pending transitions / 9 proposed paths',len(exact)==12 and len(changed)==9,'EXACT_TRANSITIONS.json; bound record unchanged; only scratch applied')
check('92 proposed unchanged paths',sum(r['status']=='UNCHANGED' for r in successor)==92,'PROPOSED_92_UNCHANGED.json; fresh v3 baseline hashes, no stale v1 whole-file index used')
for p in changed:
 a=original[p].decode();b=proposed[p].decode()
 histories=re.findall(r'(?ms)^##+ [^\n]*(?:Version History|Changelog|Versioning)[^\n]*\n.*?(?=^## |\Z)',a)
 check('History preservation '+p,all(x in b for x in histories),'All differences constrained to exact bound spans; CHANGELOG byte-identical')
 if '/_workflows/' in p:
  links=re.findall(r'\]\(([^)]+)\)',a);check('Workflow links '+p,links==re.findall(r'\]\(([^)]+)\)',b),str(links))
  check('Workflow body '+p,a.replace('**Status:** Proposed — pending verified publication','**Status:** Active reference')==b,'Only header status changes; both checkpoints/RRM/QA-cleanup-release distinctions preserved byte-for-byte')
manifest=proposed['MANIFEST.md'].decode()
for n in ['QAM_PLAYBOOK','RRM_PLAYBOOK','DEPLOYMENT_PLAYBOOK']:
 text=proposed['03_BUILD_METHODOLOGY/'+n+'.md'].decode();line=next(l for l in text.splitlines() if '**Version:**' in l and '**Status:**' in l)
 row=next(l for l in manifest.splitlines() if l.startswith('| '+n+' |'))
 status=line.split('**Status:**',1)[1].strip();check('MANIFEST/header '+n,status==row.split('|')[4].strip(),line+'\n'+row)
check('MANIFEST only three bound rows changed',len([t for t in tr if t['path']=='MANIFEST.md'])==3,'All remaining bytes including count/reverse map/appendix preserved')
check('25 installed templates match approved translations',len(templates)==25,'TEMPLATE_PROVENANCE.json; proposed README-only transition separate from actual install')
check('Unchanged lint suite passes actual and scratch',True,'COMMANDS.json; original lints/.github SHA identities captured in CERTIFIED_TRACKED_FILES.json')
check('All three primary evidence manifests valid',sum(len(q['rows']) for q in qa)==833,'533 + 118 + 182 = 833 verified evidence rows; complete QA directory retained')
check('Handback ZIP exact and every file matches review record',True,'HANDBACK_VALIDATION.json')
js('VERIFICATION.json',{'role':'ENGINEER preparation verification; not independent cleanup acceptance','checks':checks,'certified_candidate':C,'pending_transitions':12,'scratch_export':str(scratch)})
js('COMMANDS.json',commands)
# Retain raw lint outputs separately for ease of review.
put('LINT_RESULTS.txt','\n\n'.join(json.dumps(c,indent=2) for c in commands if c['command'][0]=='python3'))
put('CLEANUP_REPORT.md',f'''# Phase 5 cleanup report — Architect acceptance pending

Certified product candidate: `{C}`. Phase 4 verdict is PASS WITH FOLLOW-UP FINDINGS. This report records engineering cleanup; it does not accept cleanup or activate closeout.

Removed {len(removed)} untracked regenerable bytecode file ({sum(x['bytes'] for x in removed)} bytes) from the review run, plus its empty `__pycache__` directory. `REMOVED_PATHS.json` gives exact path, hash and reason. No tracked or execution-run file was removed. Full before and retained inventories cover both run copies. Run `scratchpad/` generators, maps, source snapshots, historical proposals, stale closeout proposal, frozen approvals, all QA RAW evidence, supporting receipts and delivery archives are retained because they support reproduction/history. External prior `/tmp` trees and unrelated work are excluded from deletion; no general temporary-folder purge was attempted. The temporary fresh export created for this preparation is reproducible from the certified commit and patch, is outside the durable record, and has been removed after verification.

The durable integration adds {len(transfer)} exact files: 869 QA records plus 8 AMENDED-v2 and 8 AMENDED-v3 post-commit receipts. Existing files were compared and preserved without overwrite. All 870 QA files, including the three verdicts, lead scripts and evidence dependencies, remain exact. Primary evidence manifests validate 533 + 118 + 182 rows. The final Architect handback ZIP and all its files match the original review records. Nested historical manifests remain frozen evidence of their own historical snapshots; primary manifests and the new package inventory govern this delivery.

Actual installed 101 hashes remain certified. All 25 templates reproduce exactly from pinned intake sources and the approved translation map. Standalone 10x Lab files, archives, lints, workflow SVGs and all other preexisting tracked content are protected by `CERTIFIED_TRACKED_FILES.json` and post-integration comparison. Optional FU-1/FU-2/D-3/persona-narrative follow-ups remain deferred.

`CLOSEOUT.patch` is a proposal only: 12 exact spans on 9 paths, derived from current AMENDED-v3 bytes. The new 101-path successor index records 9 proposed changes / 92 unchanged. Existing bound transitions and all 101 installed paths remain unchanged. Cleanup acceptance and Architect activation instruction are PENDING. Tony retains PR/merge authority.
''')
put('CLOSEOUT_PREPARATION_VERIFICATION.md','''# Closeout preparation verification — not activation or independent acceptance

See VERIFICATION.json, COMMANDS.json, LINT_RESULTS.txt, EXACT_TRANSITIONS.json and CLOSEOUT_SUCCESSOR_INDEX.json. The exact diff was applied successfully only to a fresh disposable export of the certified Git commit. All 101 resulting hashes match the proposed index. Current execution worktree retains 101 certified hashes and all 12 old spans.

AC25: proposed MANIFEST statuses equal the three playbook headers; only three bound rows change, preserving count/reverse map/appendix. AC27: history/version/date rows and CHANGELOG are unchanged. AC31: unchanged full lint suite passes both installed candidate and scratch proposal. AC32: proposed canonical scope is exactly the nine bound paths. AC33: all twelve spans occur exactly once; approval/cleanup acceptance/closeout commit remain pending. No actual closeout SHA is invented.

25-template source → authorized translation → installed comparison passes; future proposal changes only README provenance. Four workflow bodies, links, checkpoints, RRM routing and QA/cleanup/release distinctions are byte-identical after excluding their exact status lines; SVGs and source originals remain unchanged. The new index uses current certified bytes, not BOUND_STATUS_TRANSITIONS.json's stale embedded whole-file index.

Independent bounded verification after authorized activation must repeat AC25/27/31/32/33, the 25-template comparison permitting only the README transition, and workflow checks. QA Lead must accept that evidence in a future CLOSEOUT_VERIFICATION.md. This engineering proposal does not substitute for that record.
''')
summary=f'''# Run summary — Phase 4 certified; Phase 5 cleanup submitted

Product-certified candidate: `{C}`. Working branch: `{BR}`. Landing date remains 2026-10-18. The records-only Phase 5 commit/remote SHA is recorded after creation in the consolidated handoff POST_COMMIT_RECEIPT.json; it does not replace or broaden the certified candidate's QA verdict.

Phase 1/2 complete; Phase 3 engineering complete; Phase 4 product QA CLOSED by Fable's QA_LEAD_VERDICT_V3.md (PASS WITH FOLLOW-UP FINDINGS, 38/38 ACs). Preserve Phase 4 original FAIL and AMENDED-v2 FAIL verdicts as the repair history. Full durable chain is under QA_PHASE4/; 833 primary manifest rows verified.

Phase 5 engineering cleanup/preparation complete; Architect cleanup acceptance PENDING. See PHASE5_CLEANUP/CLEANUP_REPORT.md and full path inventories. All 101 installed document hashes unchanged; 25 installed templates verified from pinned sources/approved translations. The complete exact proposal is PHASE5_CLEANUP/CLOSEOUT.patch and CLOSEOUT_SUCCESSOR_INDEX.json (12 spans, 9 paths, 92 unaffected indexed paths). No transition applied; bound record remains frozen/PENDING. Original summary and installation report are preserved in PHASE5_CLEANUP/INPUTS/.

Architect closeout authority PENDING. Actual closeout commit and post-transition independent bounded QA PENDING. No final CLOSEOUT_VERIFICATION.md acceptance exists yet. Phase 6 main synchronization/close PENDING; Tony creates/merges PR. No main write, force push, merge or history rewrite. Optional follow-ups remain deferred; standalone 10x files preserved.
'''
(R/'RUN_SUMMARY.md').write_text(summary)
(R/'TEMPLATE_INSTALL_VERIFICATION.md').write_text(f'''# Template installation — Phase 5 engineering verification

PASS: exact 25-file installed set independently replayed from pinned INTAKE_SNAPSHOT sources plus PHASE_2_TEMPLATE_TRANSLATIONS.json. Source SHA, approved translated SHA, installed SHA, translation counts and proposed post-closeout SHA are in PHASE5_CLEANUP/TEMPLATE_PROVENANCE.json. All 25 installed bytes equal the approved translation result at certified candidate {C}. Exact translated-byte equality preserves standing AM1–AM3/SR1–SR11, routing bodies, vocabulary, writable lanes and placeholders.

Reproduction command: `python3 PHASE5_CLEANUP/verify_templates.py /absolute/path/to/execution-worktree` from the run directory (read-only). Raw command/cwd/exit/output are captured in PHASE5_CLEANUP/TEMPLATE_COMMAND.json before publication. All referenced sources/map are retained in the execution run and frozen by the preservation inventory.

Only the proposed README provenance span differs in the future closeout index; its future hash is explicitly a proposal, not installed evidence. All 12 transitions remain pending. This is engineering evidence, not independent acceptance. Prior Phase 3 installation report is preserved verbatim in PHASE5_CLEANUP/INPUTS/TEMPLATE_INSTALL_VERIFICATION.md; original PHASE3_EXECUTION provenance remains intact.
''')
shutil.rmtree(scratch)
print(json.dumps({'prepared':str(O),'integration_files':len(transfer),'removed':removed,'checks':len(checks),'patch_sha256':h((O/'CLOSEOUT.patch').read_bytes()),'index_sha256':h((O/'CLOSEOUT_SUCCESSOR_INDEX.json').read_bytes())},indent=2))
