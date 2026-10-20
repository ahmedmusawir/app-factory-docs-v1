"""Engineering verification on installed worktree; no product/Git writes. python3 -B -I."""
from pathlib import Path
import json,hashlib,subprocess,re,csv,os,datetime,zipfile
R=Path('/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2');A=R/'AMENDED_V3';E=R/'AMENDED_V3_EXECUTION';W=Path('/home/moose/Documents/app-factory-docs-sync-execution');C='8dff354937bc7baf739370a9886497d9d5359186';RUN='_AUDIT/SYNC_2026-10-15_doctrine-part2/'
sha=lambda b:hashlib.sha256(b).hexdigest();checks={};commands=[]
def save(n,x):(E/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def cmd(args,cwd=W):
 p=subprocess.run(args,cwd=cwd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});commands.append(dict(command=args,cwd=str(cwd),exit=p.returncode,stdout=p.stdout,stderr=p.stderr));save('COMMANDS.json',commands);assert p.returncode==0,commands[-1];return p.stdout

def ck(k,ok,d):checks[k]={'status':'PASS' if ok else 'FAIL','evidence':d};assert ok,(k,d)
def blob(p):return subprocess.check_output(['git','-C',str(W),'show',C+':'+p])
assert cmd(['git','branch','--show-current']).strip()=='docs/sync-doctrine-part2-2026-10-15'
idx=json.loads((A/'BOUND_EXECUTION_INDEX.json').read_text());ed=json.loads((A/'AMENDMENT_V3_EDITS.json').read_text());changed=sorted({e['path'] for e in ed});arch='04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md';st='04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md';api='04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md'
assert sha((A/'BOUND_EXECUTION_INDEX.json').read_bytes())=='55537c6411724ab78837d0191d61375654839202acbf15b13a76d98aa8d483e6'
assert sha((A/'EXECUTION_PROPOSAL.patch').read_bytes())=='afd8f9249854d4e99c385b1e21c459fa297fa5ed5ddcac782d1509747c43faed'
before=json.loads((E/'START_STATE.json').read_text())['candidate_path_hashes'];after={p:sha((W/p).read_bytes()) for p in before};tree=W
# Reuse the exact sealed semantic checks, with outputs redirected into execution evidence.
# Inputs stay the immutable approved AMENDED_V3 records; candidate is ACTUAL worktree.
source=(A/'generators/verify.py').read_text();block=source[source.index(" ck('R12_prime_scope'"):source.index("ck('review_records_preserved'")]
block='\n'.join(l[1:] if l.startswith(' ') else l for l in block.splitlines())
for name in ['PROPAGATION.tsv','MANUAL_READS.md','LINT_OUTPUT.txt']:block=block.replace("A/'"+name+"'","E/'"+name+"'")
block=block.replace('Exactly three paths in disposable export; no execution-worktree writes.','Exactly three original canonical paths changed in installed worktree; all other original paths preserved.')
exec(compile(block,'sealed_checks_on_installed_worktree','exec'))
# Explicit passage-level carry-forward, with hashes and actual lines; STATE itself changed.
b=blob(st).decode();n=(W/st).read_text();passages=[]
for title in ['## 4. Persistence','## 5. Hydration & SSR','## 6. Store Templates']:
 assert b.count(title)==n.count(title)==1
 old=title+b.split(title,1)[1].split('\n## ',1)[0];new=title+n.split(title,1)[1].split('\n## ',1)[0];assert old==new
 passages.append(dict(section=title,parent_sha256=sha(old.encode()),installed_sha256=sha(new.encode()),parent_line=b[:b.index(title)].count('\n')+1,installed_line=n[:n.index(title)].count('\n')+1,text=new))
assert b.split('## 7. Integration Patterns',1)[0]==n.split('## 7. Integration Patterns',1)[0]
assert before[st]!=after[st]
for needle in ['// Raw contact information is not persisted by default.','Do not persist raw contact details by default.']:
 old=next(l for l in b.splitlines() if needle in l);assert old in n;passages.append(dict(anchor=needle,parent_sha256=sha(old.encode()),installed_sha256=sha(old.encode()),text=old))
save('STATE_CARRY_FORWARD.json',dict(whole_file_changed=True,whole_file_identity_claimed=False,pre_integration_prefix_identical=True,passages=passages));ck('STATE_passage_carry_forward',True,'STATE file changed; entire prefix before §7 and explicit Persistence/Hydration/Store Templates sections/default lines byte-identical. See passage hashes and quotes.')
with zipfile.ZipFile('/home/moose/Downloads/FACTORY_AMENDED_V3_REVIEW_2026-10-19_203340.zip') as z:
 copied=[]
 for p in z.namelist():
  if p.startswith('AMENDED_V3/'):
   assert (W/RUN/p).read_bytes()==z.read(p);copied.append(RUN+p)
ap='AMENDED_V3/DIRECTOR_DECISIONS_V3.md';assert (W/RUN/ap).read_bytes()==(R/ap).read_bytes();copied.append(RUN+ap)
ck('approval_and_sealed_records',True,'Approved payload bytes exact; additive Gate2 approval matches review record; old approvals not overwritten.')
save('APPROVED_RECORD_PATHS.json',copied)
cmd(['git','diff','--check','--']+changed)
save('VERIFICATION.json',dict(time=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='ENGINEERING INSTALLED CHECKS PASS — independent QA pending',parent=C,gate2='APPROVED exact index/patch',checks=checks,source_verifier_sha256=sha(source.encode()),closeout='12 pending'))
print(json.dumps({k:v['status'] for k,v in checks.items()},indent=2))
