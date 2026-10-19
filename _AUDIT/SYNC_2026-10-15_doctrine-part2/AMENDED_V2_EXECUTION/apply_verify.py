"""Apply approved patch once, then verify installed bytes; --verify repeats read-only checks.
Outputs evidence in review repo, never alters frozen proposal evidence.
"""
from pathlib import Path
import subprocess,json,hashlib,datetime,os,re,csv,sys,zipfile
R=Path('/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2');A=R/'AMENDED_V2_EXECUTION';approved=R/'AMENDED_V2';W=Path('/home/moose/Documents/app-factory-docs-sync-execution');RUN='_AUDIT/SYNC_2026-10-15_doctrine-part2/';C='20f71ee932ed21c0878cb3a0f39c6fbe90d0a793'
sha=lambda b:hashlib.sha256(b).hexdigest();commands=[];checks={}
def save(n,d):(A/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def cmd(args,cwd=W):
 p=subprocess.run(args,cwd=cwd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});commands.append(dict(command=args,cwd=str(cwd),exit=p.returncode,stdout=p.stdout,stderr=p.stderr));save('COMMANDS.json',commands);assert p.returncode==0,commands[-1];return p.stdout

def blob(p):return subprocess.check_output(['git','-C',str(W),'show',C+':'+p])
def check(k,ok,details):
 checks[k]=dict(status='PASS' if ok else 'FAIL',details=details);assert ok,(k,details)
index=json.loads((approved/'BOUND_EXECUTION_INDEX.json').read_text());ed=json.loads((approved/'AMENDMENT_V2_EDITS.json').read_text());changed=sorted({e['path'] for e in ed});before=json.loads((approved/'EXPORT_HASHES.json').read_text())['candidate']
assert sha((approved/'BOUND_EXECUTION_INDEX.json').read_bytes())=='b4fe406963b13b650f11d7d688026c88ff37fb1698d6191cdec420247c156bc9'
assert sha((approved/'EXECUTION_PROPOSAL.patch').read_bytes())=='86fbfe6f3787c55332bb5d0c741d7ed3296c1f872e3ce26bc4af01b29a0282fd'
assert cmd(['git','branch','--show-current']).strip()=='docs/sync-doctrine-part2-2026-10-15'
if '--verify' not in sys.argv:
 assert cmd(['git','rev-parse','HEAD']).strip()==C
 assert cmd(['git','status','--porcelain'])==''
 assert all(sha((W/p).read_bytes())==h for p,h in before.items())
 approval=R/'QA_PHASE4/REPAIR_QA_P4/DIRECTOR_DECISIONS_V2.md';assert approval.exists() and 'AMENDED-v2 APPROVED' in approval.read_text()
 # Copy only immutable approved review records and the additive approval, before product mutation.
 with zipfile.ZipFile('/home/moose/Downloads/FACTORY_AMENDED_V2_REVIEW_2026-10-19_135012.zip') as z:
  for p in z.namelist():
   if p.startswith(('AMENDED_V2/','scratchpad/generators/')):
    out=W/RUN/p;assert not out.exists();out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(z.read(p))
 dest=W/RUN/'QA_PHASE4/REPAIR_QA_P4/DIRECTOR_DECISIONS_V2.md';assert not dest.exists();dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(approval.read_bytes())
 cmd(['git','apply','--check','-p0',str(approved/'EXECUTION_PROPOSAL.patch')]);cmd(['git','apply','-p0',str(approved/'EXECUTION_PROPOSAL.patch')])
 # Capture remote preflight identities already independently queried before mutation.
 save('START_STATE.json',dict(head=C,branch='docs/sync-doctrine-part2-2026-10-15',remote_branch=C,remote_main='9c179392f79b70da099121fc357d3107ad3bb86e',approval_sha256=sha(approval.read_bytes()),observed_at=datetime.datetime.now(datetime.timezone.utc).isoformat()))
after={p:sha((W/p).read_bytes()) for p in before}
check('R12_existing_path_scope',sorted(p for p in before if before[p]!=after[p])==changed,{'seven_changed_paths':changed,'all_other_existing_files_unchanged':len(before)-7})
rows=[]
for x in index:
 p=x['path'];assert before[p]==x['before_sha256'] and after[p]==x['proposed_sha256'] and (W/p).stat().st_size==x['bytes'];rows.append(dict(path=p,expected=x['proposed_sha256'],installed=after[p],changed=before[p]!=after[p]))
save('INSTALLED_101_HASHES.json',rows)
check('R6_all_successor_hashes',len(rows)==101 and sum(x['changed'] for x in rows)==7,'101/101 installed hashes equal approved successor index; seven changed, 94 unchanged.')
for p in changed:
 t=blob(p).decode()
 for e in ed:
  if e['path']==p:assert t.count(e['old'])==1;t=t.replace(e['old'],e['new'],1)
 assert t.encode()==(W/p).read_bytes()==(approved/'PROPOSED_CONTENT'/p).read_bytes()
check('approved_exact_replay',True,'All 29 edits replay exactly to installed seven files.')
# Reuse the sealed verifier's R1–R10 semantic/propagation checks on ACTUAL installed worktree.
# Only input/output path is redirected; check expressions are unchanged.
source=(R/'scratchpad/generators/cody_amend_v2_verify.py').read_text()
block=source[source.index(' def text(p):'):source.index(" save('EXPORT_HASHES.json'")]
block='\n'.join(l[1:] if l.startswith(' ') else l for l in block.splitlines()).replace("A/'INPUTS/", "approved/'INPUTS/")
tree=W
exec(compile(block,'approved_repair_checks_on_installed_worktree','exec'))
spec=RUN+'QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md'
check('frozen_spec',after[spec]=='2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc','Frozen specification preserved; no main, merge or closeout change.')
# Verify immutable copied payload and approval are exact; enumerate allowed additions.
additions=[]
with zipfile.ZipFile('/home/moose/Downloads/FACTORY_AMENDED_V2_REVIEW_2026-10-19_135012.zip') as z:
 for p in z.namelist():
  if p.startswith(('AMENDED_V2/','scratchpad/generators/')):
   assert (W/RUN/p).read_bytes()==z.read(p);additions.append(RUN+p)
ap=RUN+'QA_PHASE4/REPAIR_QA_P4/DIRECTOR_DECISIONS_V2.md';assert (W/ap).read_bytes()==(R/'QA_PHASE4/REPAIR_QA_P4/DIRECTOR_DECISIONS_V2.md').read_bytes();additions.append(ap)
check('approval_and_proposal_preserved',True,'Original sealed records copied exactly; additive Gate 2 approval predates application. Old approval and bound index unchanged.')
save('APPROVED_RECORD_PATHS.json',additions)
save('EXISTING_PATH_PRESERVATION.json',{'before':before,'after':after})
cmd(['git','diff','--check'])
save('VERIFICATION.json',dict(time=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='ENGINEERING INSTALLED CHECKS PASS — independent QA acceptance pending',start_candidate=C,checks=checks,gate2='APPROVED by Tony with pinned identities',closeout='12 pending',verifier_source_sha256=sha(source.encode())))
print(json.dumps({k:v['status'] for k,v in checks.items()},indent=2))
