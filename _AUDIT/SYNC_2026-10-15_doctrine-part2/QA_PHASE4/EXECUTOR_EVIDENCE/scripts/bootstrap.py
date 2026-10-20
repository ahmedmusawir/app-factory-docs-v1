from pathlib import Path
import subprocess,json,datetime,hashlib,tarfile,io
E=Path(__file__).resolve().parents[1]; R=E.parents[3]; W=Path('/home/moose/Documents/app-factory-docs-sync-execution'); S=Path('/tmp/qa-phase4-20261019-054106'); S.mkdir(exist_ok=True)
start='2026-10-19T05:41:06Z'
plan='Execute the authorized Phase 4 checklist: pin remote/local identities; export BASE, CONTENT and candidate; independently check all 38 ACs and 10X-COPY with manual reads; retain raw evidence and scripts; report all findings without verdict; package one ZIP. Candidate and Git stay read-only; only assigned evidence and bookkeeping lanes are writable.'
session=R/'agent_docs/SESSIONS/session_2026-10-19.md'
with session.open('a') as f:f.write('\n### '+datetime.datetime.now(datetime.timezone.utc).isoformat()+' — APPROVED → IN PROGRESS\n\n**Seat:** fresh independent QA Executor, Codex; reporting to Fable.\n**Plan:** '+plan+'\n**Authorization:** current user explicitly directs execution in one pass, no routine go. Prior engineering-session blocker does not apply to this fresh conversation.\n')
(E/'RAW/execution_plan.txt').write_text(plan+'\n')
if (E/'BLOCKED.md').exists():
 (E/'RAW/prior_session_BLOCKED.md').write_bytes((E/'BLOCKED.md').read_bytes()); (E/'BLOCKED.md').unlink()
commands=[]
def run(args,cwd=W):
 p=subprocess.run(args,cwd=cwd,capture_output=True); d=dict(cmd=args,cwd=str(cwd),exit=p.returncode,stdout=p.stdout.decode(errors='replace'),stderr=p.stderr.decode(errors='replace')); commands.append(d); return d
qa={}
for label,args in [('remote_tip',['git','ls-remote','--heads','origin','refs/heads/docs/sync-doctrine-part2-2026-10-15']),('head',['git','rev-parse','HEAD']),('branch',['git','rev-parse','--abbrev-ref','HEAD']),('porcelain',['git','status','--porcelain']),('main',['git','ls-remote','origin','refs/heads/main'])]:qa[label]=run(args)
qa['session_start_utc']=start
(E/'QA_START.json').write_text(json.dumps(qa,indent=2)+'\n'); (E/'COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n')
tip='20f71ee932ed21c0878cb3a0f39c6fbe90d0a793';base='9c179392f79b70da099121fc357d3107ad3bb86e';content='ef35d26d82f1904da6ed33663ad647e4ee16fe98'
assert all(v['exit']==0 for v in qa.values() if isinstance(v,dict))
assert qa['remote_tip']['stdout'].split()[0]==tip==qa['head']['stdout'].strip();assert not qa['porcelain']['stdout'];assert qa['main']['stdout'].split()[0]==base
for a,b in [(base,content),(content,tip)]:assert run(['git','merge-base','--is-ancestor',a,b])['exit']==0
for name,sha in [('base',base),('content',content),('cand',tip)]:
 target=S/name; target.mkdir(exist_ok=True); archive=S/(name+'.tar'); d=run(['git','archive','--format=tar','--output='+str(archive),sha]);assert d['exit']==0
 with tarfile.open(archive) as t:t.extractall(target,filter='data')
(E/'COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n')
print('QA_START_SHA='+tip+'; main='+base+'; clean; ancestry verified; exported '+str(S))
