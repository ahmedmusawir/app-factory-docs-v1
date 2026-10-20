from pathlib import Path
import re,json,hashlib,subprocess,difflib,xml.etree.ElementTree as ET
from markdown_it import MarkdownIt
E=Path(__file__).resolve().parents[1]; C=Path('/tmp/qa-phase4-20261019-054106/cand');B=C.parent/'base';R=C/'_AUDIT/SYNC_2026-10-15_doctrine-part2';checks=[]
def j(n):return json.loads((R/n).read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def out(n,x): (E/'RAW'/n).write_text(x if isinstance(x,str) else json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def ck(ac,n,ok,d): checks.append(dict(ac=ac,name=n,ok=bool(ok),detail=d))
live=sorted(C.glob('0?_*/*.md')); names={p.stem for p in live};scope=live+[C/'MANIFEST.md',C/'CHANGELOG.md']+list((C/'03_BUILD_METHODOLOGY/_workflows').glob('*.md'))+list((C/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*.md'))
for p in scope:
 target=E/'RAW/candidate_text'/p.relative_to(C);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(p.read_bytes())
for w in j('WORKFLOW_PUBLICATION_PLAN.json')['workflows']:
 md=(C/w['document']).read_text();flat=re.sub(r'\s+',' ',' '.join(''.join(t.itertext()) for t in ET.parse(C/w['asset']).iter() if t.tag.endswith('}text'))).replace('context- specific','context-specific');prev=-1
 for i,(a,s) in enumerate(w['steps'],1):
  needle=f'{i}. **{a}:** {s}.';pos=flat.find(s);ck('AC37',w['id']+' step '+str(i),needle in md and pos>prev,dict(md=needle,position=pos));prev=pos
 forbidden=re.findall(r'Director of QA|Codex|\bSol\b|Claudy|INITSCRIPT|CLOUDDEPLOYMENT|QA Lead executes|QA Lead runs tests',flat);ck('AC37','actors '+w['id'],not forbidden,forbidden)
# Header dependency extraction includes the explicit Governed-by dependency as well as Pairs-with.
m=(C/'MANIFEST.md').read_text();depsec=m.split('## Dependency')[1].split('## Appendix')[0];deps={}
for p in live:
 header='\n'.join(l for l in p.read_text().splitlines()[:9] if '**Pairs with:**' in l or '**Governed by:**' in l);deps[p.stem]={n for n in names if re.search(r'(?<![\w-])'+re.escape(n)+r'(?![\w-])',header)}
for n in names:
 expected={s for s,d in deps.items() if n in d};row=next(l for l in depsec.splitlines() if l.startswith('| '+n+' |'));actual=set(x.strip() for x in row.split('|')[2].split(',') if x.strip() not in ['—','none','']);ck('AC25','derived reverse '+n,expected==actual,dict(expected=sorted(expected),actual=sorted(actual)))
app=m.split('## Appendix')[1]
for p in live:
 body='\n'.join(p.read_text().splitlines()[9:]);expected={n for n in names if n!=p.stem and re.search(r'(?<![\w-])'+re.escape(n)+r'(?![\w-])',body)}-deps[p.stem];row=next((l for l in app.splitlines() if l.startswith('| '+p.stem+' |')),None);actual=set(x.strip() for x in row.split('|')[2].split(',')) if row else set();ck('AC25','derived appendix '+p.stem,actual==expected,dict(expected=sorted(expected),actual=sorted(actual)))
# Markdown historical containers, with table extension.
md=MarkdownIt('commonmark').enable('table');sites=[]
for p in live:
 t=p.read_text();tokens=md.parse(t)
 for i,l in enumerate(t.splitlines()):
  if 'Historical external example (availability unverified)' in l or 'two historical FFM examples' in l.lower():
   spans=[dict(type=x.type,map=x.map,content=x.content) for x in tokens if x.map and x.map[0]<=i<x.map[1] and x.type in ['table_open','tr_open','td_open','blockquote_open','list_item_open','paragraph_open','inline','fence']];sites.append(dict(path=str(p.relative_to(C)),line=i+1,quote=l,containers=spans));ck('AC20','historical label '+str(p.relative_to(C))+':'+str(i+1),any(s['type'] in ['table_open','blockquote_open','list_item_open','paragraph_open'] for s in spans),spans)
out('ac20_markdown_containers.json',sites)
# Link checking with preserved unresolved targets; expected placeholders distinguished by reviewer.
links=[]
for p in scope:
 for mt in re.finditer(r'!?\[[^\]\n]*\]\(([^)\n]+)\)',p.read_text()):
  target=mt.group(1).split('#')[0];line=p.read_text()[:mt.start()].count('\n')+1
  if not target or re.match(r'https?://|mailto:',target):continue
  dest=(p.parent/target).resolve();links.append(dict(path=str(p.relative_to(C)),line=line,target=target,exists=dest.exists()))
out('ac28_links.json',links)
# Changed Hub-name tokens (only names of canonical Hub bodies, not project artifacts).
for x in j('BOUND_EXECUTION_INDEX.json'):
 p=x['path']
 if not p.endswith('.md') or p.startswith('_ARCHIVE/'):continue
 before=(B/p).read_text() if (B/p).exists() else ''; after=(C/p).read_text(); added=[l[1:] for l in difflib.unified_diff(before.splitlines(),after.splitlines()) if l.startswith('+') and not l.startswith('+++')]
 for line in added:
  for token in re.findall(r'`([^`]+\.md)`',line):
   stem=Path(token).stem
   if stem in names:ck('AC28','hub token '+token,any(v.stem==stem for v in live),dict(path=p,text=line))
# Q9 preserved entries
p='02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md'
for id in ['Q9.1','Q9.2','Q9.3']:
 a=next(l for l in (B/p).read_text().splitlines() if id in l);b=next(l for l in (C/p).read_text().splitlines() if id in l);ck('AC12',id,a==b,dict(base=a,candidate=b))
ck('AC12','Q9.4 added','Q9.4' not in (B/p).read_text() and 'Q9.4' in (C/p).read_text(),'candidate questionnaire')
# Full _SKILLS byte comparison covers named NO guards.
guards=[]
for p in (B/'_SKILLS').rglob('*'):
 if p.is_file():
  rel=p.relative_to(B);q=C/rel;guards.append(dict(path=str(rel),base=sha(p.read_bytes()),candidate=sha(q.read_bytes()),equal=p.read_bytes()==q.read_bytes()))
ck('AC35','all skills unchanged',all(x['equal'] for x in guards),len(guards));out('ac35_guard_hashes.json',guards)
# Metadata/history structure and normalization verified in prior supplement; retain new-doc draft diff.
for stem in ['QAM','RRM','DEPLOYMENT']:
 p=C/'03_BUILD_METHODOLOGY'/(stem+'_PLAYBOOK.md');t=p.read_text();ck('AC21',stem+' initial header/history','DRAFT FOR EXECUTABLE-MAP REVIEW — NOT INSTALLED' in t.splitlines()[3] and sum(l.startswith('| 1.0 | 2026-10-18 |') for l in t.splitlines())==1 and not list((C/'_ARCHIVE').glob(stem+'_PLAYBOOK*')),t.splitlines()[3])
out('ac21_qam_draft.diff',''.join(difflib.unified_diff((R/'DRAFTS/QAM_PLAYBOOK.md').read_text().splitlines(True),(C/'03_BUILD_METHODOLOGY/QAM_PLAYBOOK.md').read_text().splitlines(True))))
# Validate 25 engineering template hash records as objects under test.
for x in j('PHASE3_EXECUTION/TEMPLATE_HASHES.json'):
 actual=sha((C/x['destination']).read_bytes());ck('AC38','engineer recorded hash '+x['destination'],x.get('installed_sha256')==actual,dict(actual=actual,record=x))
# Exact state and standing-amendment content comparison in correct homes.
q=C/'03_BUILD_METHODOLOGY/_templates/QAM';src=R/'INTAKE_SNAPSHOT/factory-intake/INTAKE_ADDENDUM_001_v0_3/TEMPLATES/QAM'
for n in ['QAM_CLEANUP_REPORT.md','QAM_ENTRY.md','QAM_EXECUTION_REPORT.md','QAM_RISK_REQUIREMENTS.md']:
 a=(src/n).read_text();b=(q/n).read_text();tr=next(x for x in j('PHASE_2_TEMPLATE_TRANSLATIONS.json') if x['destination'].endswith('/'+n))
 for x in tr['translations']:a=a.replace(x['old'],x['new'])
 ck('AC22','AM/SR home '+n,a==b,'full body exact after declared provenance only')
a=(q/'CLAUDE.md').read_text().split('\n',4)[4];b=(q/'AGENTS.md').read_text().split('\n',4)[4];ck('AC14','entry routing',a==b and 'QA Executor' in a,a)
state=(q/'QAM_STATE.md').read_text();entry=(q/'QAM_ENTRY.md').read_text();out('ac22_state_and_entry.txt',state+'\n'+entry)
# Every withdrawal query independently executed earlier; retain full remaining query hits for manual classification.
ids=[l.split('|')[1].strip() for l in (R/'SELECTED_SCOPE_LEDGER.md').read_text().splitlines() if l.startswith('| FC-') and 'withdrawal/containment' in l];out('ac16_remaining_query_hits.txt','\n'.join(id+'\n'+(E/'RAW'/('search_'+id+'.txt')).read_text() for id in ids));ck('AC16','31 withdrawal rows',len(ids)==31,ids)
# Input provenance pairs: all settled records at preservation checkpoint and CONTENT are unchanged unless explicitly mutable bound/setup/handoff records.
W='/home/moose/Documents/app-factory-docs-sync-execution';log=json.loads((E/'COMMANDS.json').read_text())
for arg in [['git','log','-1','--format=%cs','ef35d26d82f1904da6ed33663ad647e4ee16fe98'],['git','diff','--name-only','356206ab293dc3a3987269636bb853c84aaf4ad3..20f71ee932ed21c0878cb3a0f39c6fbe90d0a793','--',str(R.relative_to(C))+'/AMENDED_V1',str(R.relative_to(C))+'/PROPOSED_CONTENT',str(R.relative_to(C))+'/DRAFTS',str(R.relative_to(C))+'/UPDATE_MAP.md']]:
 p=subprocess.run(arg,cwd=W,capture_output=True,text=True);log.append(dict(cmd=arg,cwd=W,exit=p.returncode,stdout=p.stdout,stderr=p.stderr))
(E/'COMMANDS.json').write_text(json.dumps(log,indent=2)+'\n');out('final_checks.json',checks)
print(json.dumps(dict(checks=len(checks),failures=[x for x in checks if not x['ok']],broken_links=[x for x in links if not x['exists']],historical_sites=len(sites)),indent=2,ensure_ascii=False))
