from pathlib import Path
import subprocess,json,hashlib,shutil,datetime
V=Path('/home/moose/Documents/app-factory-docs-v1');E=Path('/home/moose/Documents/app-factory-docs-sync-execution');R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');O=V/R/'CLOSEOUT_EXECUTION';D=E/R/'CLOSEOUT_EXECUTION';BASE='dc3b288246ea931962e889e9a88718c0daaf9c37';H=lambda b:hashlib.sha256(b).hexdigest();commands=[]
def run(a):
 p=subprocess.run(a,cwd=E,text=True,capture_output=True);commands.append({'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':a,'cwd':str(E),'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr});(O/'APPLY_COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n');assert p.returncode==0,commands[-1];return p.stdout
assert run(['git','rev-parse','HEAD']).strip()==BASE;assert run(['git','status','--porcelain'])==''
remote=run(['git','ls-remote','origin','refs/heads/docs/sync-doctrine-part2-2026-10-15','refs/heads/main']);assert BASE+'\trefs/heads/docs/sync-doctrine-part2-2026-10-15' in remote;assert '9c179392f79b70da099121fc357d3107ad3bb86e\trefs/heads/main' in remote
(O/'REMOTE_PREFLIGHT.json').write_text(json.dumps(commands[-1],indent=2)+'\n')
assert not D.exists();shutil.copytree(O,D)
for n,sha in json.loads((O/'PREFLIGHT.json').read_text())['decision_hashes'].items():assert H((D/n).read_bytes())==sha
receipt={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baseline':BASE,'status':'BOTH DECISIONS RECORDED IN EXECUTION RUN BEFORE PATCH APPLICATION','decisions':json.loads((O/'PREFLIGHT.json').read_text())['decision_hashes']}
for root in [O,D]:(root/'PRE_APPLICATION_DECISION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
p=E/R/'PHASE5_CLEANUP/CLOSEOUT.patch';assert H(p.read_bytes())=='127230024105899fb67b8172212d96a574dc0d9fefedf82a9f26f365f3d4fa3e'
run(['git','apply','--check',str(p)]);run(['git','apply',str(p)])
shutil.copyfile(O/'APPLY_COMMANDS.json',D/'APPLY_COMMANDS.json')
print('Approved patch applied after both separate decisions were recorded. Verification follows; not committed yet.')
