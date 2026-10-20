"""Engineering verification of approved closeout; writes evidence only to review run."""
from pathlib import Path
import subprocess,json,hashlib,os,re,datetime
V=Path('/home/moose/Documents/app-factory-docs-v1');E=Path('/home/moose/Documents/app-factory-docs-sync-execution');R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');O=V/R/'CLOSEOUT_EXECUTION';P=E/R/'PHASE5_CLEANUP';BASE='dc3b288246ea931962e889e9a88718c0daaf9c37';H=lambda b:hashlib.sha256(b).hexdigest();commands=[]
def js(n,d):(O/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def run(a):
 p=subprocess.run(a,cwd=E,text=True,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});commands.append({'command':a,'cwd':str(E),'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode==0,commands[-1];return p.stdout
def blob(n):return subprocess.check_output(['git','show',BASE+':'+n],cwd=E)
idx=json.loads((P/'CLOSEOUT_SUCCESSOR_INDEX.json').read_text());bound=json.loads((E/R/'BOUND_STATUS_TRANSITIONS.json').read_text());tr=bound['transitions'];paths=sorted({t['path'] for t in tr});checks=[]
def check(n,ok,detail):assert ok,n;checks.append({'check':n,'result':'PASS','evidence':detail})
check('101 successor hashes',len(idx)==101 and all(H((E/r['path']).read_bytes())==r['proposed_sha256'] for r in idx),'SUCCESSOR_101.json')
js('SUCCESSOR_101.json',[{'path':r['path'],'before_sha256':r['before_sha256'],'approved_successor_sha256':r['proposed_sha256'],'installed_sha256':H((E/r['path']).read_bytes()),'result':'PASS'} for r in idx])
expected={p:blob(p).decode() for p in paths};applied=[]
for i,t in enumerate(tr,1):
 assert expected[t['path']].count(t['old'])==t['occurrences']==1;expected[t['path']]=expected[t['path']].replace(t['old'],t['new']);applied.append({'id':i,'path':t['path'],'old':t['old'],'new':t['new'],'occurrences':1,'status':'APPLIED; independent bounded QA PENDING'})
check('Exact 12 replacements on nine paths',len(tr)==12 and len(paths)==9 and all((E/p).read_bytes()==s.encode() for p,s in expected.items()),'Independent replay of frozen spans equals every installed changed byte')
check('Canonical diff exactly nine approved paths',sorted(run(['git','diff','--name-only']).splitlines())==paths,str(paths))
(O/'ACTUAL_CANONICAL.diff').write_text(run(['git','diff','--binary','--',*paths]));run(['git','diff','--check','--',*paths]);js('APPLIED_TRANSITIONS.json',applied)
unchanged=[r for r in idx if r['before_sha256']==r['proposed_sha256']];check('92 remaining indexed paths unchanged',len(unchanged)==92,'UNCHANGED_92.json');js('UNCHANGED_92.json',unchanged)
protected=[]
for r in json.loads((O/'BASELINE_TRACKED.json').read_text()):
 if r['path'] not in paths:
  assert H((E/r['path']).read_bytes())==r['sha256'],r['path'];protected.append(r)
js('PROTECTED_BASELINE_PATHS.json',protected);check('All other preexisting tracked bytes preserved',True,f'{len(protected)} paths, including full QA, frozen decisions/spec/maps, archives, 10x, lints/.github and SVGs')
# Current predecessor is still HEAD before commit; document all three template hash stages.
tmap=json.loads((E/R/'PHASE_2_TEMPLATE_TRANSLATIONS.json').read_text());actual={str(p.relative_to(E)) for p in (E/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*') if p.is_file()};check('Exact 25-template set',len(tmap)==25 and actual=={t['destination'] for t in tmap},'TEMPLATE_BEFORE_AFTER.json')
trows=[]
for t in tmap:
 src=(E/R/'INTAKE_SNAPSHOT'/t['source']).read_bytes();assert H(src)==t['source_sha256'];translated=src.decode()
 for a in t['translations']:
  assert translated.count(a['old'])==a['occurrences'];translated=translated.replace(a['old'],a['new'])
 before=blob(t['destination']);assert before==translated.encode() and H(before)==t['proposed_destination_sha256']
 after=translated
 for a in tr:
  if a['path']==t['destination']:assert after.count(a['old'])==1;after=after.replace(a['old'],a['new'])
 installed=(E/t['destination']).read_bytes();assert after.encode()==installed
 trows.append({'source':t['source'],'destination':t['destination'],'source_sha256':H(src),'approved_translation_sha256':H(translated.encode()),'before_installed_sha256':H(before),'after_installed_sha256':H(installed),'readme_only_allowance':t['destination'].endswith('/QAM/README.md'),'result':'PASS'})
js('TEMPLATE_BEFORE_AFTER.json',trows);check('25 templates source/translation/before/after',sum(t['before_installed_sha256']!=t['after_installed_sha256'] for t in trows)==1,'README exact provenance span only; all other translated bytes including AM1–3 and SR1–11 preserved')
metadata=[];workflows=[]
for p in paths:
 before=blob(p).decode();after=(E/p).read_text()
 # Exact span replay above is stronger than selective history extraction; also expose metadata/history evidence.
 versions=re.findall(r'\*\*(?:Version|Date):\*\*[^·\n]+',before);check('Versions/dates '+p,versions==re.findall(r'\*\*(?:Version|Date):\*\*[^·\n]+',after),str(versions))
 histories=re.findall(r'(?ms)^##+ [^\n]*(?:Version History|Changelog|Versioning)[^\n]*\n.*?(?=^## |\Z)',before);check('History '+p,all(s in after for s in histories),'All matched history sections exact; only frozen spans changed')
 metadata.append({'path':p,'versions_and_dates':versions,'history_section_hashes':[H(s.encode()) for s in histories]})
 if '/_workflows/' in p:
  check('Workflow body '+p,before.replace('**Status:** Proposed — pending verified publication','**Status:** Active reference')==after,'Header status only: body, both review checkpoints, RRM and QA/cleanup/release distinctions exact')
  links=re.findall(r'\]\(([^)]+)\)',before);check('Workflow links '+p,links==re.findall(r'\]\(([^)]+)\)',after),'Link text/targets preserved exactly; no link rewrite')
  workflows.append({'path':p,'links':links,'body_preserved':True})
for p in sorted((E/'03_BUILD_METHODOLOGY/_assets/workflows').glob('*.svg')):
 rel=str(p.relative_to(E));assert p.read_bytes()==blob(rel);workflows.append({'path':rel,'sha256':H(p.read_bytes()),'unchanged':True})
check('Four SVGs unchanged',sum('sha256' in r for r in workflows)==4,'WORKFLOW_PRESERVATION.json')
js('METADATA_HISTORY.json',metadata);js('WORKFLOW_PRESERVATION.json',workflows)
manifest=(E/'MANIFEST.md').read_text()
for n in ['DEPLOYMENT_PLAYBOOK','QAM_PLAYBOOK','RRM_PLAYBOOK']:
 text=(E/'03_BUILD_METHODOLOGY'/f'{n}.md').read_text();header=next(l for l in text.splitlines() if '**Version:**' in l and '**Status:**' in l);row=next(l for l in manifest.splitlines() if l.startswith('| '+n+' |'));check('MANIFEST/header '+n,header.split('**Status:**')[1].strip()==row.split('|')[4].strip(),header+'\n'+row)
check('MANIFEST count/reverse map/appendix unchanged',expected['MANIFEST.md']==manifest,'Only exact three bound MANIFEST rows changed; all other bytes identical')
lint=run(['python3','lints/run_all.py']);check('Unchanged full lint suite',lint.strip().endswith('=== RESULT: PASS ==='),lint);(O/'LINT_RESULTS.txt').write_text(lint)
js('VERIFICATION_COMMANDS.json',commands);js('ENGINEERING_VERIFICATION.json',{'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baseline':BASE,'checks':checks,'result':'PASS ENGINEERING','independent_closeout_check':'PENDING Fable','applied_transitions':12,'canonical_paths':9,'successor_paths':101,'unchanged_indexed_paths':92})
print(json.dumps({'result':'PASS ENGINEERING','checks':len(checks),'templates':trows,'successor_paths':101,'canonical_paths':9,'independent_QA':'PENDING'},indent=2))
