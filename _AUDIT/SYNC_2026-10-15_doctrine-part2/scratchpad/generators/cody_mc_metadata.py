from pathlib import Path
import re,json,hashlib,difflib,subprocess,os
from markdown_it import MarkdownIt
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');O=R/'PROPOSED_CONTENT';H=R/'PLANNING_HISTORY/PRE_MC_CORRECTION_2026-10-16';date='2026-10-16';md=MarkdownIt('commonmark').enable('table');ed=json.loads((R/'SELECTED_EXACT_EDITS.json').read_text());oldplans=json.loads((H/'DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json').read_text());versions={e['path']:(e['old_version'],e['proposed_version']) for e in oldplans};sha=lambda b:hashlib.sha256(b).hexdigest();records=[]
# Concrete ruling consumers. These establish provenance, not new rulings.
ruldocs={1:['SOFTWARE_FACTORY_PLAYBOOK','FFM_PLAYBOOK','BIM_PLAYBOOK','QAM_PLAYBOOK'],2:['BIM_PLAYBOOK','DEPLOYMENT_PLAYBOOK'],3:['QA_PLAYBOOK','BIM_PLAYBOOK','DEPLOYMENT_PLAYBOOK'],4:['BIM_PLAYBOOK','QAM_PLAYBOOK'],5:['SOFTWARE_FACTORY_PLAYBOOK','FFM_PLAYBOOK','BIM_PLAYBOOK','RRM_PLAYBOOK'],6:['QAM_PLAYBOOK','RRM_PLAYBOOK','DEPLOYMENT_PLAYBOOK'],7:['SOFTWARE_FACTORY_PLAYBOOK','FFM_PLAYBOOK'],8:['SOFTWARE_FACTORY_PLAYBOOK'],9:['ARCHITECT_PLAYBOOK','DESIGNER_PLAYBOOK','ENGINEER_PLAYBOOK','HANDOFF_PACKAGE_PLAYBOOK'],10:['DEPLOYMENT_PLAYBOOK'],11:['AUTH_MANUAL','ECOMMERCE_AND_PAYMENTS_MANUAL'],12:['ENGINEER_PLAYBOOK','RECON_QUESTIONNAIRE'],13:['STATE_MANAGEMENT_MANUAL'],14:['SOFTWARE_FACTORY_PLAYBOOK','RRM_PLAYBOOK'],15:['FFM_PLAYBOOK','BIM_PLAYBOOK','RRM_PLAYBOOK']}
def idsfor(path):
 ids={id for e in ed if e['path']==path for id in e['ids']}
 stem=Path(path).stem
 ids|={f'RUL-{n:02}' for n,names in ruldocs.items() if stem in names}
 return sorted(ids)
def tables(s):
 ts=md.parse(s);out=[]
 for i,t in enumerate(ts):
  if t.type!='table_open':continue
  cells=[]
  for u in ts[i+1:]:
   if u.type=='thead_close':break
   if u.type=='inline':cells.append(u.content)
  out.append((t.map,cells))
 return out
for path in sorted(versions):
 p=O/path;s=p.read_text();b=(R/'BASELINE_CONTENT'/path).read_bytes();old,new=versions[path];ids=idsfor(path);stem=Path(path).stem;arch=f'_ARCHIVE/{stem}_v{old.replace(".","_")}.md';a=O/arch;a.parent.mkdir(parents=True,exist_ok=True);a.write_bytes(b)
 # MC-09: preserve meaningful status suffixes exactly; only version/date change.
 m=re.search(r'^> \*\*Version:\*\* (.*?) · \*\*Date:\*\* (.*?) · \*\*Status:\*\* (.*)$',(R/'BASELINE_CONTENT'/path).read_text(),re.M);status=m[3] if m else 'Active';header=f'> **Version:** {new} · **Date:** {date} · **Status:** {status}'
 if stem=='STARTER_KIT_HANDBOOK':
  s=s.replace('# STARTER KIT HANDBOOK\n','# STARTER KIT HANDBOOK\n\n'+header+'\n> **Tier:** 1 — Constitution · **Pairs with:** AUTH_MANUAL, DATABASE_MANUAL, STATE_MANAGEMENT_MANUAL, UI_UX_BUILDING_MANUAL, COMPONENT_REGISTRY\n',1)
  s=s.replace('**Version:** v1.1 (Kit-Perfection campaign applied)','**Kit campaign reference:** handbook v1.1 (historical reconciliation; verify current kit revision)')
 else:s,n=re.subn(r'(?m)^> \*\*Version:\*\*.*$',header,s,count=1);assert n==1,path
 histories=[(span,cells) for span,cells in tables(s) if len(cells)>=3 and cells[0]=='Version' and cells[1]=='Date'];assert histories,('NO REAL HISTORY TABLE',path)
 span,cells=histories[-1];lines=s.splitlines(True);bodyrows=lines[span[0]+2:span[1]];assert bodyrows,path
 bodyrows=[line for line in bodyrows if re.match(r'^\| \d',line)];assert bodyrows,path
 nums=[tuple(map(int,re.search(r'\d+(?:\.\d+)*',line.split('|')[1])[0].split('.'))) for line in bodyrows];asc=nums[0]<=nums[-1]
 desc='Factory DocSet sync: approved workflow/security/reference corrections; preserved original; explicit exclusions per doctrine-part2 map. IDs: '+', '.join(ids)
 vals=[new,date,'doctrine-part2 sync',desc] if len(cells)==4 else [new,date,desc];assert len(vals)==len(cells)
 row='| '+' | '.join(vals)+' |\n';at=span[1] if asc else span[0]+2;lines.insert(at,row);s=''.join(lines);p.write_text(s)
 records.append(dict(path=path,old_version=old,proposed_version=new,archive=arch,source_sha256=sha(b),proposed_sha256=sha(s.encode()),ids=ids,status_preserved=status,history_columns=cells,history_order='newest-last' if asc else 'newest-first'))
# New playbooks preserve existing source-based row and add bounded MC provenance to that row.
for name in ['QAM_PLAYBOOK','RRM_PLAYBOOK','DEPLOYMENT_PLAYBOOK']:
 p=O/'03_BUILD_METHODOLOGY'/(name+'.md');s=p.read_text();span,cells=[x for x in tables(s) if x[1][0]=='Version' and x[1][1]=='Date'][-1];lines=s.splitlines(True);row=lines[span[0]+2];assert len(lines[span[0]+2:span[1]])==1
 row=row.rstrip('\n').rstrip('|').rstrip()+'; current correction pass: MC-01…14; '+', '.join(idsfor(str(p.relative_to(O))))+' |\n';lines[span[0]+2]=row;p.write_text(''.join(lines))
# MANIFEST uses actual full headers and retains the existing bump-procedure/CI note (MC-10).
purposes={}
for line in (R/'BASELINE_CONTENT/MANIFEST.md').read_text().splitlines():
 c=[x.strip() for x in line.split('|')]
 if len(c)==8:purposes[c[1]]=c[5]
purposes.update(FFM_PLAYBOOK='Module preparation, artifact ownership, prepared QAM, engineering and post-FFM review; revised workflow references',QAM_PLAYBOOK='Mandatory module QAM and accepted _templates/QAM set',RRM_PLAYBOOK='Approved review repairs with QAM; post-FFM and Engine 2 checkpoints',DEPLOYMENT_PLAYBOOK='Common identity, exclusion, verification and recovery; context-specific permissions retained')
live=sorted(O.glob('0*_*/*.md'));names={p.stem for p in live};entries={}
for p in live:
 s=p.read_text();m=re.search(r'^> \*\*Version:\*\* (.*?) · \*\*Date:\*\* (.*?) · \*\*Status:\*\* (.*)$',s,re.M);assert m,p;pairs=set();head='\n'.join(s.splitlines()[:12])
 for x in re.finditer(r'\*\*(?:Pairs with|Governed by):\*\*([^\n]+)',head,re.I):pairs|={n for n in names if re.search(r'(?<![A-Z_])'+re.escape(n)+r'(?![A-Z_])',x[1])}
 entries[p.stem]=dict(path=p,version=m[1],date=m[2],status=m[3],pairs=sorted(pairs),text=s)
lines=['# MANIFEST — App Factory Doctrine Index','',f'> **Version:** 1.0 · **Date:** {date} · **Status:** Active','> **Tier:** none — repository infrastructure · **Pairs with:** CHANGELOG, _ARCHIVE/README','',f'Master index of {len(live)} live tier documents. QAM templates and the four workflow references/eight workflow files are governed by their owning playbooks and are not separate tier rows.','','## How this stays current','','Regenerated from the doc header blocks on **every doc bump** (bump procedure: `_ARCHIVE/README.md` — archive the outgoing version, update the live header, update this file + CHANGELOG). CI auto-generation remains parked; the cited DOCTRINE_HUB_DESIGN is an unpromoted design reference, not operational authority.','','Identify governing snapshots by canonical document name, header version and Hub commit. Preserve intentional pins until an authorized update; no universal project landing path or release tag is required.','',f'## The {len(live)} Live Docs']
for tier in sorted({p.parent.name for p in live}):
 lines+=['',f'### {tier}','','| Canonical Name | Version | Date | Status | Purpose | Pairs With → |','|---|---|---|---|---|---|']
 for name,e in entries.items():
  if e['path'].parent.name==tier:lines.append('| '+' | '.join([name,e['version'],e['date'],e['status'],purposes[name],', '.join(e['pairs'])])+' |')
lines+=['','## Dependency Map — Ripple Analysis (Referenced by ←)','','Header dependencies are a starting set, not the complete blast radius. Inspect body references, templates, examples, checklists, workflow documents/diagrams and skills; route external changes separately.','','| Doc | ← Referenced by (header-declared) | Count |','|---|---|---|']
for name in sorted(entries):
 refs=sorted(k for k,v in entries.items() if name in v['pairs']);lines.append(f'| {name} | '+', '.join(refs)+f' | {len(refs)} |')
lines+=['','## Appendix — Undeclared Dependencies (body-mention only)','',f'Scanned {len(live)} tier-document bodies on {date}. Historical/example mentions are included; candidate edges require review before adoption.','','| Mentioning doc | Mentions (undeclared) |','|---|---|']
for name,e in sorted(entries.items()):
 body='\n'.join(e['text'].splitlines()[12:]);refs=sorted(n for n in names-{name}-set(e['pairs']) if re.search(r'(?<![A-Z_])'+re.escape(n)+r'(?![A-Z_])',body))
 if refs:lines.append('| '+name+' | '+', '.join(refs)+' |')
(O/'MANIFEST.md').write_text('\n'.join(lines)+'\n')
# MC-03: insert rows inside the existing Ongoing entries ledger, before its separator/footer.
cl=(R/'BASELINE_CONTENT/CHANGELOG.md').read_text();cl=re.sub(r'(?m)^> \*\*Version:\*\*.*$',f'> **Version:** 1.0 · **Date:** {date} · **Status:** Active',cl,count=1);at=cl.index('| 2026-08-05 | QA_PLAYBOOK v0.1');cl=cl[:at]+'| Date | Document | Change | Finding / ruling IDs |\n|---|---|---|---|\n'+cl[at:]
rows=[]
for e in records:rows.append(f"| {date} | {Path(e['path']).stem} v{e['proposed_version']} | Factory DocSet sync; preserved outgoing original; MC correction pass | "+', '.join(e['ids'])+' |')
for name in ['QAM_PLAYBOOK','RRM_PLAYBOOK','DEPLOYMENT_PLAYBOOK']:rows.append(f'| {date} | {name} v1.0 | New owning playbook'+('; accepted template installation verified separately' if name=='QAM_PLAYBOOK' else '')+' | '+', '.join(idsfor('03_BUILD_METHODOLOGY/'+name+'.md'))+'; RUL-01…15; AD-01 |')
rows.append(f'| {date} | Historical QA_PLAYBOOK v1.0 | Exact historical restoration; not active instructions | FC-089; RUL-14 |')
for w in json.loads((R/'WORKFLOW_PUBLICATION_PLAN.json').read_text())['workflows']:rows.append(f"| {date} | {w['id']} workflow v1.0 | Revised reference and SVG stick diagram; original retained as superseded history | MC-06; W01–W23; RUL-01–RUL-15; Tony 2026-10-16 correction assignment |")
# Locate the ledger table's end using parsed table boundaries.
target=next(span for span,cells in tables(cl) if cells==['Date','Document','Change','Finding / ruling IDs']);ls=cl.splitlines(True);ls[target[1]:target[1]]=[x+'\n' for x in rows];(O/'CHANGELOG.md').write_text(''.join(ls));assert len(rows)==39
(R/'DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json').write_text(json.dumps(records,indent=2)+'\n')
# Update final metadata for new docs and all final bytes. Workflow assets extend 93 ->101 paths.
plan=json.loads((R/'NEW_DOCUMENT_PROPOSALS.json').read_text())
for e in plan:e['proposed_sha256']=sha((O/e['path']).read_bytes());e['label']='ENGINEER-PROPOSED new playbook; MC corrections recorded; not installed'
(R/'NEW_DOCUMENT_PROPOSALS.json').write_text(json.dumps(plan,indent=2)+'\n')
index=[];diff=[]
for p in sorted(O.rglob('*')):
 if not p.is_file() or 'lints' in p.parts:continue
 rel=p.relative_to(O);old=(R/'BASELINE_CONTENT'/rel).read_bytes() if (R/'BASELINE_CONTENT'/rel).exists() else b'';b=p.read_bytes()
 if b==old:continue
 index.append(dict(path=str(rel),before_sha256=sha(old) if old else None,proposed_sha256=sha(b),bytes=len(b)))
 diff.extend(difflib.unified_diff(old.decode().splitlines(True),b.decode().splitlines(True),fromfile=str(rel) if old else '/dev/null',tofile=str(rel)))
assert len(index)==101,len(index)
(R/'EXECUTION_PROPOSAL_INDEX.json').write_text(json.dumps(index,indent=2)+'\n');(R/'EXECUTION_PROPOSAL.patch').write_text(''.join(diff))
p=subprocess.run(['python3','-B','-I','lints/run_all.py'],cwd=O,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True)
(R/'MC_PROPOSED_LINT_CHECK.txt').write_text('command: python3 -B -I lints/run_all.py\ncwd: '+str(O.resolve())+'\nexit code: '+str(p.returncode)+'\n'+p.stdout+p.stderr);assert p.returncode==0,p.stdout+p.stderr
print('31 header/status/history proposals; 34 tier rows; 39 in-table CHANGELOG rows; 101 proposed paths; unchanged lints PASS.')
