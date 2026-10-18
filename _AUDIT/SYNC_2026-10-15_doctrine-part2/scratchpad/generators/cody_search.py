from pathlib import Path
import re,json,csv,subprocess,collections
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');d=json.loads((R/'scratchpad/proposals.json').read_text());placements=json.loads((R/'scratchpad/placements.json').read_text());pby={x['fc']:x for x in placements};files=sorted(Path('.').glob('0*_*/*.md'))+[Path('MANIFEST.md'),Path('CHANGELOG.md')]
queries={f'FC-{int(k):03}':v for k,v in d['terms'].items()}
queries['WORKFLOW']=r'QAM|QA Lead|QA Executor|abandon.*branch|disposable.*branch|transfer.back|four.role|folder.*freez|nothing inside|Gate Q|Gate D|ACCEPTANCE_SPEC|AGENTS.md|agent_docs|Engine [123]|QA.*handoff|engineering.*handoff'
rows=[]
# Classifications are review proposals, never represented as final semantic QA.
for id,pattern in queries.items():
 direct={x['path'] for x in pby.get(id,{}).get('placements',[])}
 if id=='WORKFLOW':direct={str(p) for p in files if p.parts[0] in ['01_CONSTITUTION','02_PIPELINE_AGENTS','03_BUILD_METHODOLOGY']}
 for path in files:
  hist=False;fenced=False;heading='document header'
  for no,line in enumerate(path.read_text().splitlines(),1):
   if line.startswith('```'):fenced=not fenced
   if not fenced and re.match(r'^#{1,4} ',line):
    heading=line
    hist=bool(re.search(r'Version History|Changelog|CHANGELOG|Field Lessons',line,re.I))
   if not re.search(pattern,line,re.I):continue
   if path.name=='CHANGELOG.md' or hist:status='HISTORY';reason='Historical record retained; not current positive instruction';target='§E/§L'
   elif str(path) in direct:status='CHANGE';reason='Primary owning/consumer document is on the touch list; reconcile this occurrence with the linked row, retaining already-correct constraints';target='§C/W01–W23' if id=='WORKFLOW' else 'C-'+id[3:]
   elif path.name=='MANIFEST.md':status='CHANGE';reason='Derived index/consumer row recomputed from approved headers';target='§G'
   else:status='CONSISTENT';reason='Retained comparison/dependent occurrence; quoted text must remain consistent with the linked governing change';target='§F; final review required'
   rows.append(dict(query=id,path=str(path),line=no,heading=heading,quote=line,disposition=status,drives=target,reason=reason,review_state='ENGINEER-PROPOSED'))
with (R/'PROPAGATION.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
(R/'SEARCH_QUERIES.json').write_text(json.dumps({'base_sha':'9c179392f79b70da099121fc357d3107ad3bb86e','scope':['01_CONSTITUTION','02_PIPELINE_AGENTS','03_BUILD_METHODOLOGY','04_REFERENCE_MANUALS','05_DESIGN_SYSTEM','MANIFEST.md','CHANGELOG.md'],'command_shape':'rg -n -i -e PATTERN <scope>; path:line hits including matching line retained; Python re equivalent used to attach heading/ID dispositions','queries':queries,'hit_rows':len(rows),'note':'Rows are disposition proposals for review, not an independent QA result. Final semantic review remains a Gate 2 requirement.'},indent=2)+'\n')
# Main skill/awareness searches use main blobs rather than the older checkout.
aw=[]
paths=subprocess.check_output(['git','ls-tree','-r','--name-only','main','_SKILLS','_OTHERS'],text=True).splitlines()
pat=re.compile(r'QAM|RRM|FFM_PLAYBOOK|BIM_PLAYBOOK|QA_PLAYBOOK|ENGINEER_PLAYBOOK|_INBOX|merge anyway|every push|pull',re.I)
for p in paths:
 if not p.endswith('.md'):continue
 for i,l in enumerate(subprocess.check_output(['git','show','main:'+p],text=True).splitlines(),1):
  if pat.search(l):aw.append(dict(path='main:'+p,line=i,quote=l,disposition='OUT-OF-SCOPE',drives='§I / XB-02; awareness only'))
(R/'SKILL_AWARENESS.json').write_text(json.dumps(aw,indent=2)+'\n')
print(len(rows),'propagation rows;',len(queries),'queries;',len(aw),'read-only main awareness hits')
print(dict(collections.Counter(x['disposition'] for x in rows)))
