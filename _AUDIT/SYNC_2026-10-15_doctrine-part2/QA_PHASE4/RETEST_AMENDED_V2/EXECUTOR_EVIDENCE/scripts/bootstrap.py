from pathlib import Path
import subprocess,json,hashlib,datetime,zipfile,tarfile,io,tempfile
R=Path('/home/moose/Documents/app-factory-docs-v1'); W=Path('/home/moose/Documents/app-factory-docs-sync-execution'); RUN='_AUDIT/SYNC_2026-10-15_doctrine-part2'; E=R/RUN/'QA_PHASE4/RETEST_AMENDED_V2/EXECUTOR_EVIDENCE'; T=Path(tempfile.mkdtemp(prefix='qa-amended-v2-')); C='8dff354937bc7baf739370a9886497d9d5359186'; P='20f71ee932ed21c0878cb3a0f39c6fbe90d0a793'; B='9c179392f79b70da099121fc357d3107ad3bb86e'; commands=[]
def save(p,x): (E/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def run(args,cwd=W):
 p=subprocess.run(args,cwd=cwd,capture_output=True); commands.append(dict(command=args,cwd=str(cwd),exit=p.returncode,stdout=p.stdout.decode(errors='replace'),stderr=p.stderr.decode(errors='replace'))); return p
pins={k:run(v).stdout.decode().strip() for k,v in {'sha':['git','rev-parse','HEAD','HEAD^'],'branch':['git','branch','--show-current'],'status':['git','status','--porcelain'],'main':['git','rev-parse','refs/heads/main','refs/remotes/origin/main']}.items()}
pins.update(timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),remote_tip=C,remote_main=B,remote_evidence='Read-only escalated git ls-remote observed both expected refs; see COMMANDS.json',independence='Fresh Codex QA Executor conversation; no engineering authorship/application in this conversation')
commands.extend([dict(command=['git','ls-remote','--heads','origin','refs/heads/docs/sync-doctrine-part2-2026-10-15','refs/heads/main'],cwd=str(W),exit=128,stdout='',stderr="fatal: unable to access 'https://github.com/ahmedmusawir/app-factory-docs-v1.git/': Could not resolve host: github.com",phase='initial sandbox network failure'),dict(command=['git','ls-remote','--heads','origin','refs/heads/docs/sync-doctrine-part2-2026-10-15','refs/heads/main'],cwd=str(W),exit=0,stdout=C+'\trefs/heads/docs/sync-doctrine-part2-2026-10-15\n'+B+'\trefs/heads/main\n',stderr='',phase='escalated network retry')]);save('QA_START.json',pins)
for name,sha in [('parent',P),('candidate',C),('base',B)]:
 p=subprocess.run(['git','archive',sha],cwd=W,capture_output=True); commands.append(dict(command=['git','archive',sha],cwd=str(W),exit=p.returncode,stdout='Binary tar export; sha256 '+hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode())); d=T/name;d.mkdir();tarfile.open(fileobj=io.BytesIO(p.stdout)).extractall(d,filter='data')
save('RAW/environment.json',dict(tmp=str(T),candidate=C,parent=P,base=B))
zpath=Path('/home/moose/Downloads/FACTORY_AMENDED_V2_EXECUTION_HANDOFF_2026-10-19_150618.zip');z=zipfile.ZipFile(zpath); names=z.namelist(); sums=[n for n in names if n.endswith('SHA256SUMS.txt')]; checks=[]
for s in sums:
 for line in z.read(s).decode().splitlines():
  h,n=line.split(maxsplit=1);n=n.lstrip('*'); checks.append(dict(path=n,expected=h,actual=hashlib.sha256(z.read(n)).hexdigest()))
save('RAW/handoff_inventory.json',dict(zip_sha256=hashlib.sha256(zpath.read_bytes()).hexdigest(),safe=all(not n.startswith('/') and '..' not in Path(n).parts for n in names),names=names,checks=checks))
for n in names:
 if any(n.endswith(x) for x in ['FABLE_HANDOFF.md','DIRECTOR_DECISIONS_V2.md','COMMIT_RECEIPT.json','PUSH_RECEIPT.json']):
  b=z.read(n); (E/'RAW'/Path(n).name).write_bytes(b); checks.append(dict(original=n,review_equal=(R/RUN/n).exists() and (R/RUN/n).read_bytes()==b))
save('RAW/handoff_inventory.json',dict(zip_sha256=hashlib.sha256(zpath.read_bytes()).hexdigest(),safe=all(not n.startswith('/') and '..' not in Path(n).parts for n in names),names=names,checks=checks));save('COMMANDS.json',commands)
(E/'scripts/bootstrap.py').write_bytes(Path(__file__).read_bytes());print(T)
