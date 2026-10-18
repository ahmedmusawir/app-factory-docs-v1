from pathlib import Path
import subprocess,hashlib,json,datetime
scriptdir=Path(__file__).resolve().parent
r=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');logs=[];bindings=['SELECTED_EXACT_EDITS.json','SELECTED_CONTENT_INDEX.json','EXECUTION_PROPOSAL_INDEX.json','DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json','WORKFLOW_PUBLICATION_PLAN.json','POST_VERIFICATION_STATUS_TRANSITIONS.json','POST_VERIFICATION_PROPOSAL_INDEX.json','LANDING_DATE_PLAN.json','SELECTED_SCOPE_LEDGER.md','WORKFLOW_RULING_TRACEABILITY.json']
def run(cmd):
 p=subprocess.run(cmd,capture_output=True,text=True);logs.append('command: '+' '.join(cmd)+'\ncwd: '+str(Path.cwd())+'\nexit code: '+str(p.returncode)+'\n'+p.stdout+p.stderr)
 if p.returncode:(r/'MC_REBUILD_RAW.txt').write_text('\n'.join(logs));raise SystemExit(p.returncode)
def hashes():return {n:hashlib.sha256((r/n).read_bytes()).hexdigest() for n in bindings}
for n in ['correct','metadata','records']:run(['python3',str(scriptdir/('cody_mc_'+n+'.py'))])
a=hashes()
for n in ['correct','metadata','records']:run(['python3',str(scriptdir/('cody_mc_'+n+'.py'))])
b=hashes();assert a==b,[(n,a[n],b[n]) for n in bindings if a[n]!=b[n]]
(r/'MC_REBUILD_RAW.txt').write_text('\n'.join(logs));(r/'MC_DETERMINISTIC_REBUILD.json').write_text(json.dumps({'time':datetime.datetime.now().astimezone().isoformat(),'status':'PASS — two full fresh dependent rebuilds produced identical index/plan bytes','bindings':a},indent=2)+'\n');print('PASS: two complete rebuilds produced identical exact edits, before/after hashes, metadata, workflows, transitions and date binding.')
