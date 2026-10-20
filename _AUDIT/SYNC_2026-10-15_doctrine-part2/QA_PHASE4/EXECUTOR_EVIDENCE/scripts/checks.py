from pathlib import Path
import subprocess,json,hashlib,re,collections,difflib,xml.etree.ElementTree as ET
E=Path(__file__).resolve().parents[1]; S=Path('/tmp/qa-phase4-20261019-054106'); C=S/'cand'; B=S/'base'; T=S/'content'; RUN='_AUDIT/SYNC_2026-10-15_doctrine-part2'; R=C/RUN; W='/home/moose/Documents/app-factory-docs-sync-execution'; BASE='9c179392f79b70da099121fc357d3107ad3bb86e'; TIP='20f71ee932ed21c0878cb3a0f39c6fbe90d0a793'
commands=json.loads((E/'COMMANDS.json').read_text()); checks=[]
def j(p):return json.loads((R/p).read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def save(n,d): (E/'RAW'/n).write_text(d if isinstance(d,str) else json.dumps(d,indent=2,ensure_ascii=False)+'\n')
def check(ac,name,ok,detail):checks.append(dict(ac=ac,name=name,ok=bool(ok),detail=detail))
def cmd(args,cwd=W,raw=None):
 p=subprocess.run(args,cwd=cwd,capture_output=True,text=True);d=dict(cmd=args,cwd=str(cwd),exit=p.returncode,stdout=p.stdout,stderr=p.stderr);commands.append(d)
 if raw:save(raw,p.stdout+p.stderr)
 return p
idx=j('BOUND_EXECUTION_INDEX.json'); approved=j('AMENDED_V1/EXECUTION_PROPOSAL_INDEX.json'); versions=j('DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json'); dates=j('AMENDED_V1/LANDING_DATE_PLAN.json')['spans']; paths={x['path'] for x in idx}
# Every run input is independently fingerprinted, including all proposal bytes and settled records.
ident=[]
for p in sorted(R.rglob('*')):
 if p.is_file():ident.append(dict(path=str(p.relative_to(C)),sha256=sha(p.read_bytes()),bytes=p.stat().st_size))
review=E.parents[3]
for p in sorted((review/RUN/'QA_PHASE4').glob('*')):
 if p.is_file():ident.append(dict(path=str(p),sha256=sha(p.read_bytes()),bytes=p.stat().st_size))
(E/'INPUT_IDENTITIES.json').write_text(json.dumps(ident,indent=2)+'\n')
expected={'UPDATE_MAP.md':'cd291270bb6c8e537bcb050685c6464d326254f0d2a703c21f7f304dfe286931','EXECUTION_PROPOSAL_INDEX.json':'84337dcd3b60d059e8c67d1586cd8dba58827c64e14ab46d6d05ab57a611da39','AMENDED_V1/EXECUTION_PROPOSAL_INDEX.json':'69244f4edc347b30b81ed6a909bae4fbb5130864319e9f8cd84b5d5c22e59ba6','AMENDED_V1/SELECTED_EXACT_EDITS.json':'2675ffc148f49a95b688e9f252527950ce9c3f1fd61df3fb0ffb067fcc7ff687','AMENDED_V1/AMENDMENT_V1_EDITS.json':'274df38cbf0b2cefd91e05d505e71fc35d91f09cb16ca885234e80a300364893','QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md':'2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc'}
for p,h in expected.items():check('AC30','frozen identity '+p,sha((R/p).read_bytes())==h,sha((R/p).read_bytes()))
diff=cmd(['git','diff','--name-status',BASE+'..'+TIP],raw='ac1_name_status.txt').stdout
classed=[]
for line in diff.splitlines():
 status,p=line.split('\t'); category='sync' if p in paths else '10x' if p in ['10x Lab/ABM_PLAYBOOK_v1_0.md','10x Lab/APBM_PLAYBOOK_v1_0.md'] else 'run' if p.startswith(RUN+'/') else 'bookkeeping' if p=='RECOVERY.md' or p.startswith(('agent_docs/SESSIONS/','agent_docs/RESPONSES/','session_')) else 'UNAUTHORIZED';classed.append([status,p,category])
save('ac1_classification.json',classed);check('AC1','scope',not any(x[2]=='UNAUTHORIZED' for x in classed),dict(collections.Counter(x[2] for x in classed)));check('AC1','sync counts',collections.Counter(x[0] for x in classed if x[2]=='sync')=={'M':33,'A':68},'33M/68A')
protected=cmd(['git','diff','--name-only',BASE+'..'+TIP,'--','lints','.github','_SKILLS','CLAUDE.md','AGENTS.md','factory-corrections','factory-intake','_INBOX'],raw='protected_diff.txt').stdout;check('AC1','protected paths',not protected,protected)
records=[]; proposals={}
for x,a in zip(idx,approved):
 p=x['path'];assert p==a['path'];b=(C/p).read_bytes(); source=R/'AMENDED_V1/PROPOSED_CONTENT'/p
 if not source.exists():source=R/'PROPOSED_CONTENT'/p
 bprop=source.read_bytes();proposals[p]=bprop
 row=dict(path=p,installed=sha(b),bound=x['proposed_sha256'],content=sha((T/p).read_bytes()),bytes=len(b),review=sha(bprop),approved=a['proposed_sha256']);records.append(row)
 check('AC2','installed '+p,sha(b)==x['proposed_sha256']==sha((T/p).read_bytes()) and len(b)==x['bytes'],row)
 check('AC30','review '+p,sha(bprop)==a['proposed_sha256']==x['review_proposed_sha256'],row)
for d in dates:
 p=d['path'];old=d['old'].encode();new=d['new'].replace('<<ACTUAL_LANDING_DATE>>','2026-10-18').encode();n=proposals[p].count(old);check('AC30','date span '+p,n==d['occurrences'] and (C/p).read_bytes().count(new)==d['occurrences'] and old not in (C/p).read_bytes(),dict(old=d['old'],count=n));proposals[p]=proposals[p].replace(old,new)
for x in idx:check('AC30','bound replay '+x['path'],proposals[x['path']]==(C/x['path']).read_bytes(),sha(proposals[x['path']]))
save('ac2_installed_hashes.json',records)
replay={};editrows=[]
for e in j('AMENDED_V1/SELECTED_EXACT_EDITS.json'):
 p=e['path'];body=replay.get(p,(B/p).read_text());n=body.count(e['old']);check('AC2','edit '+str(e['sequence']),n==1,dict(path=p,occurrences=n));replay[p]=body.replace(e['old'],e['new']);editrows.append(dict(sequence=e['sequence'],path=p,occurrences=n))
save('ac2_edit_replay.json',editrows)
residual=[]
for p,body in replay.items():
 installed=(C/p).read_text(); d=list(difflib.unified_diff(body.splitlines(True),installed.splitlines(True),fromfile='content-stage/'+p,tofile='installed/'+p));residual+=d
save('ac2_metadata_residual.diff',''.join(residual))
# archive/blob and history metadata checks
archives=[]
for v in versions:
 p=v['path'];a=v['archive'];old=cmd(['git','rev-parse',BASE+':'+p]).stdout.strip();new=cmd(['git','rev-parse',TIP+':'+a]).stdout.strip();archives.append(dict(path=p,archive=a,base_blob=old,candidate_blob=new));check('AC23','blob '+a,old==new and (C/a).read_bytes()==(B/p).read_bytes(),archives[-1]);text=(C/p).read_text();check('AC23','header '+p,'**Version:** '+v['proposed_version'] in '\n'.join(text.splitlines()[:5]),v['proposed_version'])
 oldtext=(B/p).read_text(); rows=[l for l in text.splitlines() if l.startswith('|') and '2026-10-18' in l];check('AC27','one history row '+p,len(rows)==1 and len(rows[0].split('|'))-2==len(v['history_columns']),rows);check('AC27','history sections '+p,text.count('Version History')==oldtext.count('Version History'),[oldtext.count('Version History'),text.count('Version History')])
save('ac23_blobs.json',archives)
rest=cmd(['git','rev-parse',TIP+':_ARCHIVE/QA_PLAYBOOK_v1_0.md']).stdout.strip();check('AC24','restored blob',rest=='bb41260f6b6f94372a682f04b313a451f2b3c4b1',rest)
translations=j('PHASE_2_TEMPLATE_TRANSLATIONS.json'); template_rows=[]; eng=j('PHASE3_EXECUTION/TEMPLATE_HASHES.json');save('engineering_template_record_keys.json',list(eng[0]))
for x in translations:
 source=R/'INTAKE_SNAPSHOT'/x['source'];dest=C/x['destination'];text=source.read_text();counts=[]
 for tr in x['translations']:
  n=text.count(tr['old']);counts.append(n);check('AC22','translation '+x['destination'],n==tr['occurrences'],dict(count=n,declared=tr['occurrences']));text=text.replace(tr['old'],tr['new'])
 row=dict(path=x['destination'],source=sha(source.read_bytes()),expected_source=x['source_sha256'],translated=sha(text.encode()),expected_translated=x['proposed_destination_sha256'],installed=sha(dest.read_bytes()),counts=counts);template_rows.append(row);check('AC22','bytes '+x['destination'],row['source']==row['expected_source'] and row['translated']==row['expected_translated']==row['installed'],row)
 check('AC38','installed '+x['destination'],row['installed']==x['proposed_destination_sha256'],row)
 for label in ['AM-1','AM-2','AM-3']+[f'QAM-SR-{i:02}' for i in range(1,12)]:
  before=[l for l in source.read_text().splitlines() if label in l];after=[l for l in dest.read_text().splitlines() if label in l];check('AC22','standing '+x['destination']+' '+label,before==after,after)
actual={str(p.relative_to(C)) for p in (C/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*') if p.is_file()};check('AC22','exact 25 set',actual=={x['destination'] for x in translations} and len(actual)==25,sorted(actual));save('ac22_template_hashes.json',template_rows)
trans=j('BOUND_STATUS_TRANSITIONS.json')['transitions'];post={}
for t in trans:
 body=(C/t['path']).read_text(); n=body.count(t['old']);check('AC33','pending '+t['path'],n==t['occurrences'] and t['new'] not in body,dict(old_occurrences=n,new_occurrences=body.count(t['new']),old=t['old']));post[t['path']]=post.get(t['path'],body).replace(t['old'],t['new'])
save('ac33_post_hashes.json',[dict(path=p,pre=sha((C/p).read_bytes()),post=sha(b.encode())) for p,b in post.items()]);save('ac33_bound_fields.json',j('BOUND_STATUS_TRANSITIONS.json'))
# source preservation
snap=[]
for x in j('INTAKE_SNAPSHOT_INDEX.json')['files']:
 p=R/'INTAKE_SNAPSHOT'/x['path'];ok=sha(p.read_bytes())==x['sha256'];snap.append(dict(path=x['path'],ok=ok,sha256=sha(p.read_bytes())));check('AC32','snapshot '+x['path'],ok,x['sha256'])
save('snapshot_hashes.json',snap)
# workflows exact prose/svg order
wrows=[]
for w in j('WORKFLOW_PUBLICATION_PLAN.json')['workflows']:
 md=(C/w['document']).read_text();root=ET.parse(C/w['asset']);texts=[''.join(e.itertext()) for e in root.iter() if e.tag.endswith('}text')];flat=' '.join(texts);previous=-1;ok=True
 for i,(actor,step) in enumerate(w['steps'],1):
  needle=f'{i}. {actor}: {step}';ok &= needle in md
  pos=flat.find(step);ok &= pos>previous;previous=pos
 check('AC37','steps '+w['id'],ok,dict(step_count=len(w['steps']),svg_text=texts));check('AC37','provenance '+w['id'],w['source'] in md and 'Proposed — pending verified publication' in md,md);wrows.append(dict(id=w['id'],svg_text=texts,markdown=md))
save('ac37_workflows.json',wrows)
# ledger identities
ledgers={}
for name in ['SELECTED_SCOPE_LEDGER.md','SYNC_HANDOFF_DISPOSITIONS.template.md','UPDATE_MAP.md']:
 rows=[l for l in (R/name).read_text().splitlines() if re.match(r'\| FC-\d{3} \|',l)];ledgers[name]=rows
save('ac3_ledger_tables.json',ledgers)
sets=[set(rows) for rows in ledgers.values()];check('AC3','ledger sets',sets[0]==sets[1]==sets[2] and all(len(v)==97 for v in ledgers.values()),{k:len(v) for k,v in ledgers.items()})
coverage={id:bool(re.search(r'(?<![\w-])'+id+r'(?!\d)',(C/'CHANGELOG.md').read_text())) for id in [f'W{i:02}' for i in range(1,24)]+[f'RUL-{i:02}' for i in range(1,16)]+['AD-01']};check('AC3','ruling coverage',all(coverage.values()),coverage)
cl=(C/'CHANGELOG.md').read_text().splitlines();rows=[(i+1,l) for i,l in enumerate(cl) if l.startswith('| 2026-10-18 |')];save('ac26_rows.json',rows);check('AC26','39 contiguous rows',len(rows)==39 and rows[-1][0]-rows[0][0]==38,dict(count=len(rows),span=[rows[0][0],rows[-1][0]]))
# Git hygiene
for label,args in [('chain',['git','log',BASE+'..'+TIP,'--format=%H %P %an %cs %s%n%b']),('merges',['git','log','--merges',BASE+'..'+TIP]),('snapshot_modified',['git','log','--diff-filter=M','--format=%h',BASE+'..'+TIP,'--',RUN+'/INTAKE_SNAPSHOT']),('skills',['git','diff','--name-only',BASE+'..'+TIP,'--','_SKILLS']),('porcelain',['git','status','--porcelain']),('tree',['git','ls-tree','-r','--name-only',TIP]),('preservation',['git','cat-file','-t','e7b4a6f33e1ae2442f71d82f7f3a9d694f50da36']),('preservation_ancestor',['git','merge-base','--is-ancestor','e7b4a6f33e1ae2442f71d82f7f3a9d694f50da36',TIP])]:
 r=cmd(args,raw='ac32_'+label+'.txt')
 if label in ['merges','snapshot_modified','skills','porcelain']:check('AC32',label,r.returncode==0 and not r.stdout,r.stdout)
 if label=='preservation_ancestor':check('AC32',label,r.returncode==1,r.returncode)
 if label=='tree':check('AC32','no debris',not any(p.startswith('_INBOX/') or re.search(r'\.(orig|rej|bak|tmp)$|~$',p) for p in r.stdout.splitlines()),'tree retained')
lint=cmd(['python3','-B','-I','lints/run_all.py'],C,'ac29_lints.txt');check('AC31','lint',lint.returncode==0,lint.stdout+lint.stderr)
for n,expected_hash in [('ABM','21f8344812a385ec0a3da8ec41e144dc07c7248814a8b0a73db4f2433c5b2051'),('APBM','c12ff3f9bc4355e9bd8e1c276a3917bd443f864715ab1ffb6b84edf49beb4f93')]:
 filename=n+'_PLAYBOOK_v1_0.md';source=Path('/home/moose/Documents')/filename;installed=C/'10x Lab'/filename;check('10X-COPY',filename,sha(source.read_bytes())==sha(installed.read_bytes())==expected_hash,dict(source=sha(source.read_bytes()),installed=sha(installed.read_bytes())))
cmd(['git','log','--format=%H',BASE+'..'+TIP,'--','10x Lab'],raw='10x_commits.txt')
# Searches retained verbatim with candidate path:line, covering all supplied query families.
live=sorted(C.glob('0?_*/*.md'))+[C/'MANIFEST.md',C/'CHANGELOG.md'];scope=live+sorted((C/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*.md'))+sorted((C/'03_BUILD_METHODOLOGY/_workflows').glob('*.md'))+sorted((C/'03_BUILD_METHODOLOGY/_assets/workflows').glob('*.svg'))
for id,pattern in j('SEARCH_QUERIES.json')['queries'].items():
 hits=[]
 for p in scope:
  for i,l in enumerate(p.read_text().splitlines(),1):
   if re.search(pattern,l,re.I):hits.append(f'{p.relative_to(C)}:{i}: {l}')
 save('search_'+id+'.txt','\n'.join(hits)+'\n')
check('10X-COPY','no integration',not any(re.search(r'ABM_PLAYBOOK|APBM_PLAYBOOK|10x Lab',p.read_text()) for p in scope),'all live, templates, workflows and SVGs')
save('automated_checks.json',checks);(E/'COMMANDS.json').write_text(json.dumps(commands,indent=2)+'\n')
print(json.dumps(dict(checks=len(checks),failures=[x for x in checks if not x['ok']]),indent=2))
