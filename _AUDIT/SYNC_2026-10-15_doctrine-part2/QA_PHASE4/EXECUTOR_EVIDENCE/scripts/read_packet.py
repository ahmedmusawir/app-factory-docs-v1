from pathlib import Path
import re,json,sys
E=Path(__file__).resolve().parents[1];C=Path('/tmp/qa-phase4-20261019-054106/cand');R=C/'_AUDIT/SYNC_2026-10-15_doctrine-part2'
# Each packet contains exact numbered candidate lines, not paraphrases.
groups={
'ownership':['APP_FACTORY_BLUEPRINT','ARCHITECT_PLAYBOOK','DESIGNER_PLAYBOOK','ENGINEER_PLAYBOOK','HANDOFF_PACKAGE_PLAYBOOK','GLOBAL_DESIGN_SYSTEM_HANDBOOK'],
'governance':['SOFTWARE_FACTORY_PLAYBOOK','BIM_PLAYBOOK','QA_PLAYBOOK'],
'ffm':['FFM_PLAYBOOK','BUG_FIX_PLAYBOOK','FEAT_PLAYBOOK'],
'new':['RRM_PLAYBOOK','QAM_PLAYBOOK','DEPLOYMENT_PLAYBOOK'],
'security':['AUTH_MANUAL','DATABASE_MANUAL','STATE_MANAGEMENT_MANUAL','ECOMMERCE_AND_PAYMENTS_MANUAL','STRIPE_MANUAL','API_MANUAL','TESTING_PLAYBOOK'],
'indices':['MANIFEST','CHANGELOG']}
pattern=r'DATA_CONTRACT|UI_SPEC|FILE_TREE|QAM/|checkpoint|Engine [12]|source of truth|ratification|read.only|Git|cleanup|frozen|freeze|OPEN|DEFERRED|Historical external|authority|authority|Stage 5|QA Executor|Phase [0-5]|Navbar Law|RLS|schema.first|raw.body|contact|persist|withdraw|containment|recon.*writ|supersed'
for name,stems in groups.items():
 lines=[]
 for stem in stems:
  found=list(C.glob('0?_*'+'/'+stem+'.md')) or list(C.glob(stem+'.md'))
  if not found:continue
  p=found[0];body=p.read_text().splitlines(); selected=set(range(len(body))) if name in ['new','indices'] else set()
  if not selected:
   for i,l in enumerate(body):
    if re.search(pattern,l,re.I):selected.update(range(max(0,i-3),min(len(body),i+5)))
  lines.append('\nFILE '+str(p.relative_to(C)))
  last=-2
  for i in sorted(selected):
   if i!=last+1:lines.append('...')
   lines.append(f'{i+1}: {body[i]}');last=i
 (E/'RAW'/('read_'+name+'.txt')).write_text('\n'.join(lines)+'\n')
print('\n'.join(f'{p.name}: {len(p.read_text().splitlines())} lines' for p in sorted((E/'RAW').glob('read_*.txt'))))
