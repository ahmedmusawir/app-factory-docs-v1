from pathlib import Path
import json,hashlib,zipfile,subprocess,datetime
V=Path('/home/moose/Documents/app-factory-docs-v1');E=Path('/home/moose/Documents/app-factory-docs-sync-execution');RUN=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');O=V/RUN/'CLOSEOUT_EXECUTION';P=E/RUN/'PHASE5_CLEANUP';BASE='dc3b288246ea931962e889e9a88718c0daaf9c37';BR='docs/sync-doctrine-part2-2026-10-15';H=lambda b:hashlib.sha256(b).hexdigest()
def js(n,x):(O/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
cmds=[]
def run(a):
 p=subprocess.run(a,cwd=E,text=True,capture_output=True);cmds.append({'command':a,'cwd':str(E),'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode==0;return p.stdout
assert run(['git','rev-parse','HEAD']).strip()==BASE;assert run(['git','branch','--show-current']).strip()==BR;assert run(['git','status','--porcelain'])==''
package=Path('/home/moose/Downloads/FACTORY_PHASE5_CLEANUP_CLOSEOUT_REVIEW_2026-10-20_182141.zip');assert H(package.read_bytes())=='dc9544c097af7fb990153e664e95f9659c48f635bb17bc2c6db6f06aaa0fd7bd'
with zipfile.ZipFile(package) as z:
 assert z.testzip() is None
 lines=z.read('PACKAGE_SHA256SUMS.txt').decode().splitlines()
 for l in lines:
  sha,n=l.split('  ',1);assert H(z.read(n))==sha,n
 assert len(lines)==len(z.namelist())-1==1829
 for n,sha in [('CLOSEOUT.patch','127230024105899fb67b8172212d96a574dc0d9fefedf82a9f26f365f3d4fa3e'),('CLOSEOUT_SUCCESSOR_INDEX.json','d46ed5ae0f70c7ad1ea1b55a4df9fae67c2e97a53dbf8c559593e9635f651e0c')]:
  b=(P/n).read_bytes();assert H(b)==sha and b==z.read('RUN/PHASE5_CLEANUP/'+n)
 # The accepted cleanup artifacts/QA bytes must equal the reviewed package.
 for n in z.namelist():
  if n.startswith(('RUN/QA_PHASE4/','RUN/PHASE5_CLEANUP/')) and not n.endswith('/'):
   dst=E/RUN/n.removeprefix('RUN/')
   if dst.exists():assert dst.read_bytes()==z.read(n),n
idx=json.loads((P/'CLOSEOUT_SUCCESSOR_INDEX.json').read_text());cert=json.loads((E/RUN/'AMENDED_V3/BOUND_EXECUTION_INDEX.json').read_text());assert len(idx)==len(cert)==101
checks=[]
for i,c in zip(idx,cert):
 assert i['path']==c['path'];b=(E/i['path']).read_bytes();assert H(b)==i['before_sha256']==c['proposed_sha256'];checks.append({'path':i['path'],'before_sha256':H(b),'result':'PASS'})
js('BASELINE_101.json',checks)
tracked=run(['git','ls-files','-z']).rstrip('\0').split('\0');js('BASELINE_TRACKED.json',[{'path':n,'sha256':H((E/n).read_bytes())} for n in tracked])
bound=json.loads((E/RUN/'BOUND_STATUS_TRANSITIONS.json').read_text());assert len(bound['transitions'])==12
paths=sorted({t['path'] for t in bound['transitions']});assert len(paths)==9
for t in bound['transitions']:assert (E/t['path']).read_text().count(t['old'])==t['occurrences']==1
for n in ['RUN_SUMMARY.md','TEMPLATE_INSTALL_VERIFICATION.md']:
 q=O/'INPUTS'/n;q.parent.mkdir(exist_ok=True);q.write_bytes((E/RUN/n).read_bytes())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
artifacts=['CLEANUP_REPORT.md','REMOVED_PATHS.json','RETAINED_PATHS.json','EXECUTION_RETAINED_PATHS.json','INTEGRATION_PLAN.json','INTEGRATION_VERIFICATION.json','QA_EVIDENCE_MANIFEST_VALIDATION.json']
accept=f'''# Architect cleanup acceptance — recorded before activation

Recorded by Cody ENGINEER at {now}, from Tony's current explicit message conveying **JARVIS Architect acceptance**. This is an attributable record of that instruction, not a cleanup verdict authored by Cody.

Decision 1: the reviewed retention/removal inventory and preserved QA records are ACCEPTED. Reviewed package `{package.name}`, SHA-256 `{H(package.read_bytes())}`. Baseline working/remote HEAD `{BASE}`. All 870 durable QA files and the three independent verdicts remain intact; prior decisions are preserved.

Accepted artifact identities (RUN/PHASE5_CLEANUP):
'''+''.join(f'- `{n}` — `{H((P/n).read_bytes())}`\n' for n in artifacts)+'''
This cleanup acceptance is separate from the activation instruction. It does not claim post-activation independent QA acceptance. Optional follow-ups remain deferred; Tony retains PR/merge.
'''
(O/'ARCHITECT_CLEANUP_ACCEPTANCE.md').write_text(accept)
activation=f'''# Architect activation instruction — exact bounded closeout

Recorded by Cody ENGINEER at {now}, from Tony's current explicit message conveying **JARVIS Architect authorization**. Cleanup acceptance is separately recorded in ARCHITECT_CLEANUP_ACCEPTANCE.md, SHA-256 `{H(accept.encode())}`.

Decision 2: apply exactly the 12 previously approved transitions on the following nine paths, using current baseline `{BASE}` on `{BR}`:
'''+''.join('- `'+p+'`\n' for p in paths)+'''
Approved patch: RUN/PHASE5_CLEANUP/CLOSEOUT.patch
SHA-256: `127230024105899fb67b8172212d96a574dc0d9fefedf82a9f26f365f3d4fa3e`
Approved 101-path successor index: RUN/PHASE5_CLEANUP/CLOSEOUT_SUCCESSOR_INDEX.json
SHA-256: `d46ed5ae0f70c7ad1ea1b55a4df9fae67c2e97a53dbf8c559593e9635f651e0c`

Tony authorizes verification, commit and push on the existing working branch using existing agent Git authorization. Tony retains PR creation and merge. No main writes, force-push or history rewrite. No content beyond these twelve exact spans is authorized. Versions, landing dates, history, template bodies (except README provenance), workflows (except status headers), SVGs, archives, standalone 10x and frozen records must remain exact. Optional follow-ups remain deferred.

The frozen BOUND_STATUS_TRANSITIONS.json remains historical and unedited. Current applied state and actual commit identity will be recorded additively after application/commit. Independent closeout check by Fable remains PENDING.
'''
(O/'ARCHITECT_ACTIVATION_INSTRUCTION.md').write_text(activation)
js('PREFLIGHT.json',{'time':now,'baseline':BASE,'branch':BR,'clean':True,'zip_sha256':H(package.read_bytes()),'zip_inventory_verified':1829,'certified_baseline_hashes':101,'pending_before_application':12,'paths':paths,'remote_preflight':'REMOTE_PREFLIGHT.json','decision_hashes':{n:H((O/n).read_bytes()) for n in ['ARCHITECT_CLEANUP_ACCEPTANCE.md','ARCHITECT_ACTIVATION_INSTRUCTION.md']}})
js('PREFLIGHT_COMMANDS.json',cmds)
print('PASS: package inventory, approved identities, 101 baselines, 12 pending spans; separate decisions recorded in review run.')
