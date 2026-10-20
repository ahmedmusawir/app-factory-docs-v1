from pathlib import Path
import json,subprocess,hashlib,re,os,difflib,csv
R=Path('/home/moose/Documents/app-factory-docs-v1'); W=Path('/home/moose/Documents/app-factory-docs-sync-execution'); RUN='_AUDIT/SYNC_2026-10-15_doctrine-part2'; E=R/RUN/'QA_PHASE4/RETEST_AMENDED_V2/EXECUTOR_EVIDENCE'; cfg=json.loads((E/'RAW/environment.json').read_text()); T=Path(cfg['tmp']); C=T/'candidate'; P=T/'parent'; B=T/'base'; commands=json.loads((E/'COMMANDS.json').read_text())
def save(p,x): (E/p).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def h(b):return hashlib.sha256(b).hexdigest()
def run(a,cwd=W):
 p=subprocess.run(a,cwd=cwd,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}); d=dict(command=a,cwd=str(cwd),exit=p.returncode,stdout=p.stdout.decode(errors='replace'),stderr=p.stderr.decode(errors='replace')); commands.append(d);return d
idx=json.loads((C/RUN/'AMENDED_V2/BOUND_EXECUTION_INDEX.json').read_text()); rows=[]
for x in idx:
 p=x['path']; before=run(['git','show',cfg['parent']+':'+p]); after=run(['git','show',cfg['candidate']+':'+p]); pb=(P/p).read_bytes(); cb=(C/p).read_bytes(); wb=(W/p).read_bytes(); rows.append(dict(path=p,parent=h(pb),candidate=h(cb),installed=h(wb),bytes=len(cb),before_ok=h(pb)==x['before_sha256'],after_ok=h(cb)==h(wb)==x['proposed_sha256'],length_ok=len(cb)==x['bytes'],changed=pb!=cb,proposed_equal=(C/RUN/'AMENDED_V2/PROPOSED_CONTENT'/p).read_bytes()==cb if pb!=cb else None,blob_export_equal=before['stdout'].encode()==pb and after['stdout'].encode()==cb))
save('RAW/index_hashes.json',rows)
changed=[x['path'] for x in rows if x['changed']]; diff=run(['git','diff','--no-ext-diff','--no-renames',cfg['parent'],cfg['candidate'],'--',*changed]);(E/'RAW/canonical.diff').write_text(diff['stdout'])
full=run(['git','diff','--name-status','--no-renames',cfg['parent'],cfg['candidate']]);scope=[]
for line in full['stdout'].splitlines():
 status,p=line.split('\t'); scope.append(dict(status=status,path=p,classification='canonical approved content repair' if p in changed else 'additive '+('/'.join(p.split('/')[2:4])),additive_ok=p in changed or (status=='A' and p.startswith(RUN+'/'))))
save('RAW/scope.json',scope)
for sha in [cfg['parent'],cfg['candidate'],cfg['base']]:run(['git','ls-tree','-r',sha])
protected=[]
for p in sorted(set(x.relative_to(P).as_posix() for x in P.rglob('*') if x.is_file()) | set(x.relative_to(C).as_posix() for x in C.rglob('*') if x.is_file())):
 if p in changed:continue
 if (P/p).is_file():protected.append(dict(path=p,equal=(C/p).is_file() and (C/p).read_bytes()==(P/p).read_bytes(),sha256=h((P/p).read_bytes())))
save('RAW/preserved_existing_paths.json',protected)
for a,b in [(cfg['base'],'ef35d26d82f1904da6ed33663ad647e4ee16fe98'),('ef35d26d82f1904da6ed33663ad647e4ee16fe98',cfg['parent']),(cfg['parent'],cfg['candidate'])]:run(['git','merge-base','--is-ancestor',a,b])
run(['git','log','--format=%H %P %s',cfg['parent']+'..'+cfg['candidate']]);run(['git','show','-s','--format=fuller',cfg['candidate']]);run(['git','diff','--check',cfg['parent'],cfg['candidate'],'--',*changed]);run(['git','diff','--check',cfg['parent'],cfg['candidate']]); lint=run(['python3','-B','-I','lints/run_all.py'],C);(E/'RAW/lints.txt').write_text(lint['stdout']+lint['stderr'])
edits=json.loads((C/RUN/'AMENDED_V2/SELECTED_EXACT_EDITS.json').read_text());orig=json.loads((P/RUN/'AMENDED_V1/SELECTED_EXACT_EDITS.json').read_text()); exact=[]
for x in edits[372:]:
 txt=(C/x['path']).read_text();pt=(P/x['path']).read_text();exact.append(dict(sequence=x['sequence'],path=x['path'],new_count=txt.count(x['new']),old_count=txt.count(x['old']),parent_old_count=pt.count(x['old'])))
save('RAW/exact_spans.json',dict(original_380_preserved=edits[:380]==orig,sequence=[x['sequence'] for x in edits],spans=exact))
trans=json.loads((C/RUN/'BOUND_STATUS_TRANSITIONS.json').read_text());save('RAW/transitions_source.json',trans)
live=sorted([p for d in ['01_CONSTITUTION','02_PIPELINE_AGENTS','03_BUILD_METHODOLOGY','04_REFERENCE_MANUALS','05_DESIGN_SYSTEM'] for p in (C/d).glob('*.md')]+[C/'MANIFEST.md',C/'CHANGELOG.md']); flow=sorted((C/'03_BUILD_METHODOLOGY/_workflows').glob('*.md'))+sorted((C/'03_BUILD_METHODOLOGY/_assets/workflows').glob('*.svg')); save('RAW/live_scope.json',[str(p.relative_to(C)) for p in live+flow])
terms=['different author','filesystem wins','disk wins','hands off to Operations','seedSubscription','supabaseAdmin','appropriate for:','fetchProducts','raw contact','persist']; hits=[]
for p in live+flow:
 hist=False;fence=False;heading=''
 for i,line in enumerate(p.read_text().splitlines(),1):
  if line.startswith('#'):heading=line
  if re.match(r'^#{1,6} .*Version History',line):hist=True
  if line.startswith('```'):fence=not fence
  for term in terms:
   if term.lower() in line.lower():hits.append(dict(term=term,path=str(p.relative_to(C)),line=i,text=line,heading=heading,history=hist,fence=fence))
save('RAW/propagation_hits.json',hits)
queries=json.loads((C/RUN/'SEARCH_QUERIES.json').read_text())['queries'];ownership=[]
for fc in ['FC-008','FC-015','FC-016','FC-017','FC-019','FC-025','FC-026','FC-027']:
 pat=re.compile(queries[fc],re.I)
 for p in live+flow:
  for i,line in enumerate(p.read_text().splitlines(),1):
   if pat.search(line):ownership.append(dict(fc=fc,path=str(p.relative_to(C)),line=i,text=line))
save('RAW/ownership_hits.json',ownership)
(E/'RAW/ownership_hits.txt').write_text('\n'.join(f"{x['fc']} {x['path']}:{x['line']}: {x['text']}" for x in ownership))
(E/'RAW/propagation_hits.txt').write_text('\n'.join(f"{i} {x['term']} {x['path']}:{x['line']}: {x['text']}" for i,x in enumerate(hits)))
# Exact inputs, retained locally to make evidence reproducible.
inputs=[]
for root,names in [(C,[RUN+'/AMENDED_V2/BOUND_EXECUTION_INDEX.json',RUN+'/AMENDED_V2/EXECUTION_PROPOSAL.patch',RUN+'/QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md',RUN+'/QA_PHASE4/REPAIR_QA_P4/DIRECTOR_DECISIONS_V2.md',RUN+'/SEARCH_QUERIES.json',RUN+'/UPDATE_MAP.md',RUN+'/AMENDED_V2/AMENDMENT_V2_EDITS.json']),(R,[RUN+'/QA_PHASE4/QA_LEAD_VERDICT.md',RUN+'/QA_PHASE4/OVERRIDES_AND_ALIGNMENT.md',RUN+'/QA_PHASE4/AC_EXECUTION_CHECKLIST.md',RUN+'/QA_PHASE4/RETEST_AMENDED_V2/QA_EXECUTOR_PROMPT.md'])]:
 for p in names:
  b=(root/p).read_bytes(); inputs.append(dict(source=str(root/p),sha256=h(b))); (E/'RAW'/('input_'+Path(p).name)).write_bytes(b)
save('INPUT_IDENTITIES.json',inputs);save('COMMANDS.json',commands);(E/'scripts/checks.py').write_bytes(Path(__file__).read_bytes());print('index',len(rows),'changed',len(changed),'protected',len(protected),'scope',len(scope),'live',len(live),'hits',len(hits),'ownership',len(ownership),'lint',lint['exit']);print('bad index',[x for x in rows if not all(x[k] for k in ['before_ok','after_ok','length_ok','blob_export_equal'])]);print('spans',exact)
