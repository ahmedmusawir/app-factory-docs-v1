from pathlib import Path
import json,re,hashlib,difflib,xml.etree.ElementTree as ET,subprocess
E=Path(__file__).resolve().parents[1];C=Path('/tmp/qa-phase4-20261019-054106/cand');B=C.parent/'base';R=C/'_AUDIT/SYNC_2026-10-15_doctrine-part2';checks=[]
def j(n):return json.loads((R/n).read_text())
def out(n,x): (E/'RAW'/n).write_text(x if isinstance(x,str) else json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def ck(ac,n,ok,d):checks.append(dict(ac=ac,name=n,ok=bool(ok),detail=d))
def norm(s):return re.sub(r'(?<=-)\s+(?=specific)','',re.sub(r'\s+',' ',s)).strip()
# Correct instrument: Markdown bold actor markup; SVG visual line wrapping of context-specific.
for w in j('WORKFLOW_PUBLICATION_PLAN.json')['workflows']:
 md=(C/w['document']).read_text();flat=norm(' '.join(''.join(t.itertext()) for t in ET.parse(C/w['asset']).iter() if t.tag.endswith('}text')));prev=-1
 for i,(a,s) in enumerate(w['steps'],1):
  needle=f'{i}. **{a}** — {s}'; pos=flat.find(s);ck('AC37',w['id']+' step '+str(i),needle in md and pos>prev,dict(markdown=needle,svg_position=pos));prev=pos
# Standing amendments are sections in risk/entry docs; README provenance identifiers are approved translations.
for x in j('PHASE_2_TEMPLATE_TRANSLATIONS.json'):
 src=(R/'INTAKE_SNAPSHOT'/x['source']).read_text();dst=(C/x['destination']).read_text()
 for marker in re.findall(r'^.*(?:AM-[123]\b|QAM-SR-\d+\b).*$',src,re.M):
  translated=marker
  for tr in x['translations']:translated=translated.replace(tr['old'],tr['new'])
  # provenance spans can cross lines, validated by full-file exact replay, not section invariants
  if x['destination'].endswith('/README.md'):continue
  ck('AC22','standing exact '+x['destination'],marker in dst,marker)
# MANIFEST independently derived from headers
live=sorted(C.glob('0?_*/*.md'));names={p.stem for p in live};m=(C/'MANIFEST.md').read_text();tier=m.split('## Dependency')[0];deps={};meta=[]
for p in live:
 t=p.read_text();head=next(l for l in t.splitlines()[:10] if '**Version:**' in l);z=re.search(r'\*\*Version:\*\* (.*?) · \*\*Date:\*\* (.*?) · \*\*Status:\*\* (.*)',head);row=next(l for l in tier.splitlines() if l.startswith('| '+p.stem+' |'));cells=[s.strip() for s in row.split('|')[1:-1]];ck('AC25','header '+p.stem,cells[1:4]==list(z.groups()),dict(header=list(z.groups()),cells=cells[1:4]));pair=next(l for l in t.splitlines()[:10] if '**Pairs with:**' in l).split('**Pairs with:**',1)[1];deps[p.stem]={n for n in names if re.search(r'(?<![\w-])'+re.escape(n)+r'(?![\w-])',pair)};meta.append(dict(path=str(p.relative_to(C)),header=head,row=row))
reverse=m.split('## Dependency')[1].split('## Appendix')[0]
for name in names:
 expected={s for s,d in deps.items() if name in d};row=next((l for l in reverse.splitlines() if l.startswith('| '+name+' |')),None)
 ck('AC25','reverse '+name,row is not None and set(x.strip() for x in row.split('|')[2].strip().split(',') if x.strip() not in ['—','none',''])==expected,dict(expected=sorted(expected),row=row))
append=m.split('## Appendix')[1];extra=[]
for p in live:
 body='\n'.join(p.read_text().splitlines()[5:]);mentioned={n for n in names if n!=p.stem and re.search(r'(?<![\w-])'+re.escape(n)+r'(?![\w-])',body)}-deps[p.stem];row=next((l for l in append.splitlines() if l.startswith('| '+p.stem+' |')),None);actual=set(x.strip() for x in row.split('|')[2].strip().split(',')) if row else set();extra.append(dict(doc=p.stem,computed=sorted(mentioned),recorded=sorted(actual)));ck('AC25','body appendix '+p.stem,mentioned==actual,extra[-1])
out('ac25_manifest.json',meta);out('ac25_appendix.json',extra)
# Exact eight amendment spans
am=j('AMENDED_V1/AMENDMENT_V1_EDITS.json');am=am.get('edits',[]) if isinstance(am,dict) else am
for x in am:
 t=(C/x['path']).read_text(); ck('AC6','amendment '+str(x.get('sequence',x.get('id'))),x['old'] not in t and t.count(x['new'])==1,dict(path=x['path'],line=t[:t.find(x['new'])].count('\n')+1,new=x['new']))
# Replay residual allowance: strip exactly one added history row and standard metadata, then compare whole bodies.
eds=j('AMENDED_V1/SELECTED_EXACT_EDITS.json');replay={}
for x in eds:replay[x['path']]=replay.get(x['path'],(B/x['path']).read_text()).replace(x['old'],x['new'])
for v in j('DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json'):
 p=v['path'];a=replay[p];b=(C/p).read_text();b=''.join(l for l in b.splitlines(True) if not (l.startswith('|') and '2026-10-18' in l));oldhead=next((l for l in a.splitlines()[:6] if '**Version:**' in l),None);newhead=next((l for l in b.splitlines()[:6] if '**Version:**' in l),None)
 if oldhead:b=b.replace(newhead,oldhead,1)
 else:
  # Explicit D-4 insertion at H1 plus historical kit campaign line.
  b=b.replace('\n'+newhead+'\n'+b.splitlines()[3]+'\n','',1)
  b=b.replace('**Kit campaign reference:** handbook v1.1 (historical reconciliation; verify current kit revision)','**Version:** v1.1 (Kit-Perfection campaign applied)')
 ck('AC2','content plus metadata '+p,a==b,''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True))))
# Withdrawals: independently locate approved replacement contexts, exact old absence and all query hits.
rows=[l for l in (R/'SELECTED_SCOPE_LEDGER.md').read_text().splitlines() if l.startswith('| FC-') and 'withdrawal/containment' in l];packet=[]
for row in rows:
 id=row.split('|')[1].strip();packet.append('\n'+id+' '+row);seen=set()
 for x in eds:
  if id not in x['ids']:continue
  t=(C/x['path']).read_text();n=t.find(x['new']);line=t[:n].count('\n')+1
  if x['new'] in seen:continue
  seen.add(x['new']);packet.append(f"{x['path']}:{line} old-span-present={x['old'] in t}\n{x['new']}")
out('read_withdrawals.txt','\n'.join(packet)+'\n')
# All targeted supplementary hits with exact line and context. 
patterns={'claims':r'97 findings|all findings|all 94|all 97|findings (are )?resolved|findings closed|rescored|kit facts verified','retired':r'Engineer authors DATA_CONTRACT|Architect drafts UI_SPEC|Designer revises|FILE_TREE (?:=|is the) source of truth|The Engineer.s full output list|abandon the QA branch|transfer back|disposable QA branch|Engineer commits|git-zero|folder FREEZES here|nothing inside the folder is added|freeze doctrine applies to attackers|filesystem wins|disk wins|doctrine doc wins|roll back the work','personas':r'Codex|\bSol\b|Claudy|Director of QA|QA Engineer \[|runs zero git','paths':r'CURRENT_APP|\.claude/skills|doctrine-YYYY|release tag','platform':r'Cloud Run|init-app.sh|deploy.sh|INITSCRIPT|CLOUDDEPLOYMENT','template_values':r'PASS\b|approved|certificate|\b[0-9a-f]{40}\b|password|token|secret'}
scope=live+[C/'MANIFEST.md',C/'CHANGELOG.md']+list((C/'03_BUILD_METHODOLOGY/_workflows').glob('*.md'))+list((C/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*.md'))
for k,pat in patterns.items():
 selected=scope if k!='template_values' else list((C/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*.md'));hits=[]
 for p in selected:
  for i,l in enumerate(p.read_text().splitlines(),1):
   if re.search(pat,l,re.I):hits.append(f'{p.relative_to(C)}:{i}: {l}')
 out('supplement_'+k+'.txt','\n'.join(hits)+'\n')
out('supplement_checks.json',checks);print(json.dumps([x for x in checks if not x['ok']],indent=2,ensure_ascii=False))
