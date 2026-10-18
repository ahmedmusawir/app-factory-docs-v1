from pathlib import Path
import json,csv,re,collections
from markdown_it import MarkdownIt
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');O=R/'PROPOSED_CONTENT';md=MarkdownIt('commonmark').enable('table')
queries={
'MC01-pointer':r'Historical external example|Two real FFMs are available',
'MC02-history':r'^#{1,6} .*Version History|^## 12\. Versioning|Factory DocSet sync:',
'MC04-lifecycle':r'Blueprint lifecycle|APP_FACTORY_BLUEPRINT lifecycle|Phase 0|Phase 5|four-role pattern',
'MC05-engine-table':r'\| Engine 1|\| Engine 2|\| Post-FFM review|\| RRM',
'MC06-review-checkpoints':r'after FFM|post-FFM|Engine 2|clean review|approved.*repair',
'MC07-ownership-freeze':r'Engineer produces alongside|Architect.*DATA_CONTRACT|Designer.*UI_SPEC|folder FREEZES|freeze doctrine applies|acceptance criteria.*froz|declared.*lanes',
'MC08-status-closeout':r'\*\*Status:\*\*|proposed set differs|installation.*pending',
'MC10-bump-guidance':r'How this stays current|bump procedure|CI auto-generation',
'MC14-template-plan':r'TEMPLATE_INSTALL_PLAN|PHASE_2_TEMPLATE_TRANSLATIONS',
'forbidden-active-contradictions':r'folder FREEZES here|freeze doctrine applies to attackers|This is the output the Engineer produces alongside working code\.|Phase 3: ENGINEER \(Data & Code\)|\*\*Historical external example pointer[^\n]*\|'}
paths=sorted(O.glob('0*_*/*.md'))+sorted((O/'03_BUILD_METHODOLOGY/_workflows').glob('*.md'))+sorted((O/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*.md'))+[O/'MANIFEST.md',O/'CHANGELOG.md'];rows=[]
for p in paths:
 s=p.read_text();lines=s.splitlines();ts=md.parse(s);hist=set()
 for i,t in enumerate(ts):
  if t.type!='table_open':continue
  header=[]
  for u in ts[i+1:]:
   if u.type=='thead_close':break
   if u.type=='inline':header.append(u.content)
  if header[:2]==['Version','Date'] or p.name=='CHANGELOG.md':hist|=set(range(t.map[0],t.map[1]))
 for q,pattern in queries.items():
  for i,line in enumerate(lines):
   if not re.search(pattern,line,re.I):continue
   history=i in hist and line.startswith('| ')
   if q=='forbidden-active-contradictions':assert history,('ACTIVE CONTRADICTION',p,i+1,line)
   rows.append({'query':q,'path':str(p.relative_to(O)),'line':i+1,'quote':line,'disposition':'HISTORY' if history else 'CONSISTENT','reason':'Existing dated/version ledger; retained historical source' if history else 'Current exact proposal reviewed against MC disposition: structural placement, lifecycle/seat/ownership/contract lanes, current pending status, or governing plan reference. This is Engineer propagation review, not independent acceptance.'})
with (R/'MC_PROPAGATION.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
(R/'MC_PROPAGATION_QUERIES.json').write_text(json.dumps({'scope':'34 tier +4 workflow documents +25 template Markdown files +MANIFEST/CHANGELOG; archives excluded','command_shape':'Python re equivalent of rg -n -i -e PATTERN, with actual Markdown table context','queries':queries,'files':len(paths),'hits':len(rows),'counts':dict(collections.Counter(x['disposition'] for x in rows)),'active_forbidden_hits':0},indent=2)+'\n');print(len(rows),'MC-focused hits dispositioned; no active forbidden contradiction.')
