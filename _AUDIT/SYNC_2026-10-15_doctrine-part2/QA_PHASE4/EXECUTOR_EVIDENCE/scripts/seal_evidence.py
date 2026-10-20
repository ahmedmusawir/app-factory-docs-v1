from pathlib import Path
import subprocess,json,hashlib,datetime,shutil
E=Path(__file__).resolve().parents[1];W='/home/moose/Documents/app-factory-docs-sync-execution';REVIEW=Path('/home/moose/Documents/app-factory-docs-v1');TIP='20f71ee932ed21c0878cb3a0f39c6fbe90d0a793';BASE='9c179392f79b70da099121fc357d3107ad3bb86e'
records=json.loads((E/'COMMANDS.json').read_text());pins=[]
for args in [['git','rev-parse','HEAD'],['git','rev-parse','--abbrev-ref','HEAD'],['git','status','--porcelain'],['git','ls-remote','--heads','origin','refs/heads/docs/sync-doctrine-part2-2026-10-15'],['git','ls-remote','origin','refs/heads/main']]:
 p=subprocess.run(args,cwd=W,capture_output=True,text=True);r=dict(cmd=args,cwd=W,exit=p.returncode,stdout=p.stdout,stderr=p.stderr);records.append(r);pins.append(r)
(E/'COMMANDS.json').write_text(json.dumps(records,indent=2)+'\n');(E/'RAW/end_pin.json').write_text(json.dumps(pins,indent=2)+'\n')
assert all(r['exit']==0 for r in pins)
assert pins[0]['stdout'].strip()==TIP and pins[1]['stdout'].strip()=='docs/sync-doctrine-part2-2026-10-15' and not pins[2]['stdout'] and pins[3]['stdout'].split()[0]==TIP and pins[4]['stdout'].split()[0]==BASE
# Record reproducible report-generation invocation with output; script itself unchanged.
args=['python3','-B','-I','finish_evidence.py'];p=subprocess.run(args,cwd=E/'scripts',capture_output=True,text=True);records.append(dict(cmd=args,cwd=str(E/'scripts'),exit=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0
(E/'COMMANDS.json').write_text(json.dumps(records,indent=2)+'\n')
now=datetime.datetime.now(datetime.timezone.utc);stamp=now.strftime('%Y-%m-%d_%H%M%S');report=(E/'EXECUTOR_REPORT.md').read_text();response=REVIEW/'agent_docs/RESPONSES'/f'response_{stamp}_qa-executor-evidence.md';response.write_text(report)
session=REVIEW/'agent_docs/SESSIONS'/f'session_{now:%Y-%m-%d}.md'
with session.open('a') as f:f.write(f'\n### [{now:%H:%M} UTC] — COMPLETE\n\n**Task:** Independent Phase4 QA at {TIP}.\n**Files changed:** QA_PHASE4/EXECUTOR_EVIDENCE/**; {response.relative_to(REVIEW)}; session log; RECOVERY.md header.\n**Tests:** All38 ACs plus10X-COPY complete:31 PASS /8 FAIL /0 BLOCKED /0 OBSERVATION. Lints pass. Candidate clean and remote tip/main unchanged at end.\n**Notes:** Fable adjudicates; no repair or closeout transitions applied. Full findings in EXECUTOR_REPORT.md.\n')
recovery=REVIEW/'RECOVERY.md';old=recovery.read_text();lines=old.splitlines(True);header=f'Last action: Independent Phase4 QA complete for {TIP}; 31 PASS /8 FAIL; Fable adjudication pending. Evidence: {E.relative_to(REVIEW)}/EXECUTOR_REPORT.md\n';recovery.write_text(lines[0]+'\n'+header+''.join(lines[1:]))
# Sealing metadata is finalized before manifest generation.
(E/'RAW/package_metadata.json').write_text(json.dumps(dict(sealed_utc=now.isoformat(),candidate=TIP,branch_unchanged=True,worktree_clean=True,main_unchanged=True,response=str(response),manifest_excludes_only_itself=True),indent=2)+'\n')
files=sorted(p for p in E.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt')
manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(E))+'\n' for p in files)
(E/'SHA256SUMS.txt').write_text(manifest)
print(json.dumps(dict(files=len(files),manifest_sha256=hashlib.sha256(manifest.encode()).hexdigest(),response=str(response)),indent=2))
