from pathlib import Path
import json,re,hashlib,difflib,subprocess,shutil
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');out=R/'PROPOSED_CONTENT';versions=json.loads((R/'scratchpad/versions.json').read_text());ed=json.loads((R/'SELECTED_EXACT_EDITS.json').read_text());date='2026-10-16';records=[]
versions['03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md']=['1.1.3','1.2.0']
for path in sorted({e['path'] for e in ed}):
 p=out/path;s=p.read_text();old,new=versions[path];ids=sorted({id for e in ed if e['path']==path for id in e['ids']});stem=Path(path).stem;b=Path(path).read_bytes();arch=f'_ARCHIVE/{stem}_v{old.replace(".","_")}.md'
 if Path(arch).exists():assert Path(arch).read_bytes()==b,('ARCHIVE COLLISION',arch)
 a=out/arch;a.parent.mkdir(parents=True,exist_ok=True);a.write_bytes(b)
 header=f'> **Version:** {new} · **Date:** {date} · **Status:** Active'
 if stem=='STARTER_KIT_HANDBOOK':
  s=s.replace('# STARTER KIT HANDBOOK\n','# STARTER KIT HANDBOOK\n\n'+header+'\n> **Tier:** 1 — Constitution · **Pairs with:** AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, UI_UX_BUILDING_MANUAL, COMPONENT_REGISTRY\n',1)
  s=s.replace('**Version:** v1.1 (Kit-Perfection campaign applied)','**Kit campaign reference:** handbook v1.1 (historical reconciliation; verify current kit revision)')
 else:s,n=re.subn(r'(?m)^> \*\*Version:\*\*.*$',header,s,count=1);assert n==1,path
 # Find the actual document history outside fenced example/template bodies.
 offset=0;fence=None;heads=[]
 for line in s.splitlines(True):
  fm=re.match(r'^(`{3,}|~{3,})',line)
  if fm:
   token=fm[1]
   if fence is None:fence=token
   elif token[0]==fence[0] and len(token)>=len(fence):fence=None
  elif fence is None and re.match(r'^#{1,6} .*Version History',line,re.I):heads.append((offset,offset+len(line)))
  offset+=len(line)
 row=f'| {new} | {date} | Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: '+', '.join(ids)+' |\n'
 if heads:
  begin=heads[-1][1];sep=re.search(r'(?m)^\|[- :|]+\|[ \t]*$',s[begin:]);assert sep,path
  table_start=begin+sep.end();tail=s[table_start:];match=re.match(r'\n((?:\|[^\n]*\n)+)',tail);assert match,path
  oldrows=[x for x in match[1].splitlines() if re.match(r'^\| \d',x)];assert oldrows,path;first=re.search(r'\d+(?:\.\d+)*',oldrows[0]);last=re.search(r'\d+(?:\.\d+)*',oldrows[-1]);asc=tuple(map(int,first[0].split('.'))) <= tuple(map(int,last[0].split('.')))
  at=table_start+len(match[0]) if asc else table_start+1
  s=s[:at]+row+s[at:]
 else:s+='\n## Version History\n\n| Version | Date | Change |\n|---|---|---|\n'+row
 p.write_text(s);records.append(dict(path=path,old_version=old,proposed_version=new,archive=arch,source_sha256=hashlib.sha256(b).hexdigest(),proposed_sha256=hashlib.sha256(s.encode()).hexdigest(),ids=ids))
for p in Path('.').glob('0*_*/*.md'):
 if not (out/p).exists():(out/p).parent.mkdir(parents=True,exist_ok=True);(out/p).write_bytes(p.read_bytes())
for name in ['QAM_PLAYBOOK','RRM_PLAYBOOK','DEPLOYMENT_PLAYBOOK']:
 p=out/'03_BUILD_METHODOLOGY'/f'{name}.md';p.write_text(p.read_text().replace('<<LANDING_DATE>>',date))
purposes={}
for line in Path('MANIFEST.md').read_text().splitlines():
 c=[x.strip() for x in line.split('|')]
 if len(c)==8:purposes[c[1]]=c[5]
purposes.update(QAM_PLAYBOOK='Mandatory module QAM and accepted _templates/QAM set',RRM_PLAYBOOK='Bounded approved review repair with QAM and reviewer guidance',DEPLOYMENT_PLAYBOOK='Common release identity, exclusion, verification and recovery; retained context permissions')
live=sorted(out.glob('0*_*/*.md'));names={p.stem for p in live};entries={}
for p in live:
 s=p.read_text();m=re.search(r'^> \*\*Version:\*\* (.*?) · \*\*Date:\*\* (.*?) · \*\*Status:\*\* (.*)$',s,re.M);assert m,p;header='\n'.join(s.splitlines()[:12]);pairs=set()
 for f in re.finditer(r'\*\*(?:Pairs with|Governed by):\*\*([^\n]+)',header,re.I):pairs.update(n for n in names if re.search(r'(?<![A-Z_])'+re.escape(n)+r'(?![A-Z_])',f[1]))
 entries[p.stem]=dict(path=p,version=m[1],date=m[2],status=m[3],pairs=sorted(pairs),text=s)
lines=['# MANIFEST — App Factory Doctrine Index','',f'> **Version:** 1.0 · **Date:** {date} · **Status:** Active','> **Tier:** none — repository infrastructure · **Pairs with:** CHANGELOG, _ARCHIVE/README','',f'Master index of {len(live)} live tier documents. QAM template files are governed through QAM_PLAYBOOK, not separate tier rows.','', 'Identify snapshots by canonical document name, header version and Hub commit. Preserve intentional pins until an authorized update. No universal project-copy path or release tag is required. Regenerate derived values from the actual approved headers.','',f'## The {len(live)} Live Docs']
for tier in sorted({p.parent.name for p in live}):
 lines+=['',f'### {tier}','','| Canonical Name | Version | Date | Status | Purpose | Pairs With → |','|---|---|---|---|---|---|']
 for name,e in entries.items():
  if e['path'].parent.name==tier:lines.append('| '+' | '.join([name,e['version'],e['date'],e['status'],purposes[name],', '.join(e['pairs'])])+' |')
lines+=['','## Dependency Map — Ripple Analysis (Referenced by ←)','','Header dependencies are a starting set, not the complete blast radius. Inspect body references, templates, examples, checklists and skills; route external changes separately.','','| Doc | ← Referenced by (header-declared) | Count |','|---|---|---|']
for name in sorted(entries):
 refs=sorted(k for k,v in entries.items() if name in v['pairs']);lines.append(f'| {name} | '+', '.join(refs)+f' | {len(refs)} |')
lines+=['','## Appendix — Undeclared Dependencies (body-mention only)','',f'Scanned {len(live)} tier-document bodies on {date}. Historical/example mentions are included; candidate edges require review before adoption.','','| Mentioning doc | Mentions (undeclared) |','|---|---|']
for name,e in sorted(entries.items()):
 body='\n'.join(e['text'].splitlines()[12:]);refs=sorted(n for n in names-{name}-set(e['pairs']) if re.search(r'(?<![A-Z_])'+re.escape(n)+r'(?![A-Z_])',body))
 if refs:lines.append('| '+name+' | '+', '.join(refs)+' |')
(out/'MANIFEST.md').write_text('\n'.join(lines)+'\n')
cl=Path('CHANGELOG.md').read_text();cl=re.sub(r'(?m)^> \*\*Version:\*\*.*$',f'> **Version:** 1.0 · **Date:** {date} · **Status:** Active',cl,count=1);at=cl.index('| 2026-08-05 | QA_PLAYBOOK v0.1');cl=cl[:at]+'| Date | Document | Change | Finding / ruling IDs |\n|---|---|---|---|\n'+cl[at:]+'\n'
for e in records:cl+=f"| {date} | {Path(e['path']).stem} v{e['proposed_version']} | Factory DocSet sync; preserved outgoing original | "+', '.join(e['ids'])+' |\n'
for name in ['QAM_PLAYBOOK','RRM_PLAYBOOK','DEPLOYMENT_PLAYBOOK']:cl+=f'| {date} | {name} v1.0 | New owning doctrine'+('; accepted template translations verified separately' if name=='QAM_PLAYBOOK' else '')+' | RUL-01…15; AD-01 |\n'
cl+=f'| {date} | Historical QA_PLAYBOOK v1.0 | Exact historical restoration; not active instructions | FC-089; RUL-14 |\n';(out/'CHANGELOG.md').write_text(cl)
(R/'DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json').write_text(json.dumps(records,indent=2)+'\n');diff=[];index=[]
for p in sorted(out.rglob('*')):
 if not p.is_file() or 'lints' in p.parts:continue
 rel=p.relative_to(out);old=Path(rel).read_bytes() if Path(rel).exists() else b'';b=p.read_bytes()
 if b==old:continue
 index.append(dict(path=str(rel),before_sha256=hashlib.sha256(old).hexdigest() if old else None,proposed_sha256=hashlib.sha256(b).hexdigest(),bytes=len(b)))
 diff.extend(difflib.unified_diff(old.decode().splitlines(True),b.decode().splitlines(True),fromfile=str(rel) if old else '/dev/null',tofile=str(rel)))
(R/'EXECUTION_PROPOSAL_INDEX.json').write_text(json.dumps(index,indent=2)+'\n');(R/'EXECUTION_PROPOSAL.patch').write_text(''.join(diff));shutil.copytree('lints',out/'lints',dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__'))
proc=subprocess.run(['python3','lints/run_all.py'],cwd=out,capture_output=True,text=True);(R/'PROPOSED_LINT_CHECK.txt').write_text('ENGINEER PROPOSAL CHECK — not canonical or independent QA\ncommand: python3 lints/run_all.py\ncwd: '+str(out.resolve())+'\nexit code: '+str(proc.returncode)+'\n'+proc.stdout+proc.stderr)
print(len(records),'bumped proposals;',len(live),'tier docs;',len(index),'changed paths; simulated lint exit',proc.returncode);print(proc.stdout[-2500:])

plan=json.loads((R/'NEW_DOCUMENT_PROPOSALS.json').read_text())
for e in plan:e['proposed_sha256']=hashlib.sha256((out/e['path']).read_bytes()).hexdigest()
(R/'NEW_DOCUMENT_PROPOSALS.json').write_text(json.dumps(plan,indent=2)+'\n')
