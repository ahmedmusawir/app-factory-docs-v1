"""Authorized working-branch push, then independent remote identity/clean-tree checks."""
from pathlib import Path
import subprocess,json,datetime,hashlib
R=Path('/home/moose/Documents/app-factory-docs-v1/_AUDIT/SYNC_2026-10-15_doctrine-part2');E=R/'AMENDED_V3_EXECUTION';W=Path('/home/moose/Documents/app-factory-docs-sync-execution');C=json.loads((E/'COMMIT_RECEIPT.json').read_text())['commit'];commands=[]
def cmd(args):
 p=subprocess.run(args,cwd=W,capture_output=True,text=True);commands.append(dict(command=args,cwd=str(W),exit=p.returncode,stdout=p.stdout,stderr=p.stderr));(E/'PUSH_COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n');assert p.returncode==0,commands[-1];return p.stdout
assert cmd(['git','rev-parse','HEAD']).strip()==C
assert cmd(['git','branch','--show-current']).strip()=='docs/sync-doctrine-part2-2026-10-15' and cmd(['git','status','--porcelain'])==''
push=cmd(['git','push','origin','HEAD:refs/heads/docs/sync-doctrine-part2-2026-10-15'])
remote=cmd(['git','ls-remote','--heads','origin','refs/heads/docs/sync-doctrine-part2-2026-10-15','refs/heads/main']);refs={x.split()[1]:x.split()[0] for x in remote.splitlines()};assert refs['refs/heads/docs/sync-doctrine-part2-2026-10-15']==C and refs['refs/heads/main']=='9c179392f79b70da099121fc357d3107ad3bb86e'
assert cmd(['git','status','--porcelain'])==''
assert cmd(['git','rev-parse','HEAD']).strip()==C
sha=lambda b:hashlib.sha256(b).hexdigest()
for x in json.loads((R/'AMENDED_V3/BOUND_EXECUTION_INDEX.json').read_text()):assert sha((W/x['path']).read_bytes())==x['proposed_sha256']==sha(subprocess.check_output(['git','show',C+':'+x['path']],cwd=W))
prior=json.loads((E/'START_STATE.json').read_text())['candidate_path_hashes'];changed=json.loads((R/'AMENDED_V3/AMENDMENT_IDENTITIES.json').read_text())['changed_paths'];assert all(sha((W/p).read_bytes())==h for p,h in prior.items() if p not in changed)
receipt=dict(time=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PUSHED AND VERIFIED — independent QA pending',local_sha=C,remote_sha=refs['refs/heads/docs/sync-doctrine-part2-2026-10-15'],remote_main=refs['refs/heads/main'],clean_worktree=True,successor_hashes='101/101 PASS',unchanged_indexed_paths=98,all_other_original_paths='byte-identical',closeout_transitions='12 PENDING',commands_file='PUSH_COMMANDS.json',push_command=commands[3])
(E/'PUSH_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
