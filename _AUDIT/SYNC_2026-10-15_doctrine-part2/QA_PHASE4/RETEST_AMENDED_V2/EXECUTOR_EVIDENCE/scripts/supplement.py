exec(compile(open('/tmp/qa_checks.py').read().split('idx=json.loads')[0],'/tmp/qa_checks.py','exec'))
# Persist full pinned live documents and exact edit source for reproducible manual review.
for p in json.loads((E/'RAW/live_scope.json').read_text()):
 out=E/'RAW/candidate'/p;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes((C/p).read_bytes())
idx=json.loads((C/RUN/'AMENDED_V2/BOUND_EXECUTION_INDEX.json').read_text()); changed=[x['path'] for x in idx if x['before_sha256']!=x['proposed_sha256']]
# Compare patch deltas directly against git's diff; never apply it.
def changes(text):
 d={};key=None
 for l in text.splitlines():
  if l.startswith('+++ '):key=l[4:];key=key[2:] if key.startswith('b/') else key;d[key]=[]
  elif key and l[:1] in ['+','-'] and not l.startswith('--- '):d[key].append(l)
 return d
approved=(C/RUN/'AMENDED_V2/EXECUTION_PROPOSAL.patch').read_text();actual=(E/'RAW/canonical.diff').read_text();save('RAW/patch_delta.json',dict(equal=changes(approved)==changes(actual),approved=changes(approved),actual=changes(actual)))
# Independently reconstruct exact edit effects only as strings, not a candidate or patch application.
edits=json.loads((C/RUN/'AMENDED_V2/AMENDMENT_V2_EDITS.json').read_text());delta=[]
for p in changed:
 old=(P/p).read_text(); expected=old
 for edit in [x for x in edits if x['path']==p]:
  assert expected.count(edit['old'])==1,(p,edit['sequence']);expected=expected.replace(edit['old'],edit['new'],1)
 delta.append(dict(path=p,exact_edits_account_for_entire_delta=expected==(C/p).read_text()))
save('RAW/edit_delta_accounting.json',delta)
trans=json.loads((C/RUN/'BOUND_STATUS_TRANSITIONS.json').read_text());tr=[]
for x in trans['transitions']:
 p=x['path'];text=(C/p).read_text();tr.append(dict(path=p,old=x['old'],new=x['new'],expected=x['occurrences'],count=text.count(x['old']),new_count=text.count(x['new']),unchanged=(C/p).read_bytes()==(P/p).read_bytes(),line=text[:text.index(x['old'])].count('\n')+1,status='PASS' if text.count(x['old'])==x['occurrences'] and not text.count(x['new']) else 'FAIL'))
save('RAW/transitions.json',tr)
# metadata and structural checks
meta=[];manifest=(C/'MANIFEST.md').read_text()
for p in changed:
 a=(P/p).read_text();b=(C/p).read_text();header=b.splitlines()[:5];row=[l for l in manifest.splitlines() if l.startswith('| '+Path(p).stem+' |')];ar=[l for l in a.splitlines() if l.startswith('|') and '2026-10-18' in l];br=[l for l in b.splitlines() if l.startswith('|') and '2026-10-18' in l];meta.append(dict(path=p,header=header,header_equal=header==a.splitlines()[:5],manifest=row,parent_run_rows=len(ar),candidate_run_rows=len(br),amended_rows=sum(x!=y for x,y in zip(ar,br)),history_header_counts=[a.count('## Version History'),b.count('## Version History')],row_columns_equal=[l.count('|') for l in ar]==[l.count('|') for l in br],fence_counts=[sum(l.startswith('```') for l in a.splitlines()),sum(l.startswith('```') for l in b.splitlines())]))
save('RAW/metadata.json',meta)
a=(P/'02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md').read_text();b=(C/'02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md').read_text();part=lambda t:t.split('### What Operations Needs')[1].split('## Appendix A:')[0];save('RAW/handoff_structure.json',dict(operations_and_verbal_byte_equal=part(a)==part(b),entries=[l for l in b.split('📦 ENGINEER → OPERATIONS HANDOFF')[1].split('```')[0].splitlines() if l.startswith(('├','└'))]))
archives=[]
for x in json.loads((C/RUN/'DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json').read_text()):
 if x.get('archive'):archives.append(dict(path=x['archive'],source=x['path'],base_sha256=h((B/x['path']).read_bytes()),archive_sha256=h((C/x['archive']).read_bytes()),equal=(B/x['path']).read_bytes()==(C/x['archive']).read_bytes()))
save('RAW/archive_originals.json',archives);run(['git','rev-parse',cfg['candidate']+':_ARCHIVE/QA_PLAYBOOK_v1_0.md','9ad3f3f:03_BUILD_METHODOLOGY/QA_PLAYBOOK.md'])
# protected mode/tree subsets and sealed input copies
pt=run(['git','ls-tree','-r',cfg['parent']])['stdout'];ct=run(['git','ls-tree','-r',cfg['candidate']])['stdout'];parse=lambda t:{l.split('\t',1)[1]:l.split('\t',1)[0] for l in t.splitlines()};pa=parse(pt);ca=parse(ct)
sets={'archives':'_ARCHIVE/','templates':'03_BUILD_METHODOLOGY/_templates/QAM/','workflows':'03_BUILD_METHODOLOGY/_workflows/','assets':'03_BUILD_METHODOLOGY/_assets/','10x':'10x Lab/','skills':'_SKILLS/','lints':'lints/','github':'.github/','snapshot':RUN+'/INTAKE_SNAPSHOT/','amended_v1':RUN+'/AMENDED_V1/','frozen_spec':RUN+'/QA_RETEST_AF01/'}
ps={}
for key,prefix in sets.items():
 aa={p:v for p,v in pa.items() if p.startswith(prefix)};bb={p:v for p,v in ca.items() if p.startswith(prefix)};ps[key]=dict(count=len(aa),equal=aa==bb,paths=bb)
for p in ['CLAUDE.md','AGENTS.md',RUN+'/UPDATE_MAP.md']:
 ps[p]=dict(parent=pa.get(p),candidate=ca.get(p),equal=pa.get(p)==ca.get(p))
save('RAW/protected_tree_sets.json',ps)
copychecks=[]
for p in (C/RUN/'AMENDED_V2/INPUTS').rglob('*'):
 if not p.is_file():continue
 rel=str(p.relative_to(C/RUN/'AMENDED_V2/INPUTS'))
 original= P/RUN/rel[len('candidate_run/'):] if rel.startswith('candidate_run/') else R/RUN/rel
 if p.suffix=='.zip':original=Path('/home/moose/Downloads')/p.name
 copychecks.append(dict(path=str(p.relative_to(C)),source=str(original),equal=original.exists() and original.read_bytes()==p.read_bytes()))
save('RAW/copied_inputs.json',copychecks)
source_auth=json.loads((C/RUN/'EXECUTION_SETUP/STANDALONE_10X_AUTHORIZATION.json').read_text());save('RAW/10x_authorization.json',source_auth)
save('RAW/10x_source_comparison.json',[dict(path=str(p.relative_to(C)),source=str(Path('/home/moose/Documents')/p.name),equal=(Path('/home/moose/Documents')/p.name).read_bytes()==p.read_bytes(),sha256=h(p.read_bytes())) for p in (C/'10x Lab').glob('*.md')])
staged=json.loads((R/RUN/'AMENDED_V2_EXECUTION/STAGED_SCOPE.json').read_text());scope=json.loads((E/'RAW/scope.json').read_text());save('RAW/staged_comparison.json',dict(equal=set(staged['paths'])=={x['path'] for x in scope},staged=staged))
# Withdrawal locator from original independent packet, re-evaluate candidate passages, preserve surrounding sections.
old_packet=(R/RUN/'QA_PHASE4/EXECUTOR_EVIDENCE/RAW/withdrawal_judgment_packet.txt').read_text();withdraw=[];fc=None
for line in old_packet.splitlines():
 if re.fullmatch(r'FC-\d+',line):fc=line;withdraw.append(dict(fc=fc,evidence=[]));continue
 m=re.match(r'([^:]+\.md):(\d+): (.*)',line)
 if m:
  p,_,q=m.groups();text=(C/p).read_text();n=text.find(q)
  if n>=0:
   ln=text[:n].count('\n')+1;lines=text.splitlines();start=ln-1
   while start>0 and not lines[start].startswith('#'):start-=1
   stop=ln
   while stop<len(lines) and not lines[stop].startswith('#'):stop+=1
   withdraw[-1]['evidence'].append(dict(path=p,line=ln,quote=q,section_start=start+1,section_end=stop,section_equal_parent='\n'.join(lines[start:stop]) in (P/p).read_text()))
  else:withdraw[-1]['evidence'].append(dict(path=p,quote=q,missing=True))
save('RAW/withdrawal_candidate_passages.json',withdraw)
packet=[]
for row in withdraw:
 packet.append('\n'+row['fc'])
 for x in row['evidence']:
  if 'line' in x:packet.append(f"{x['path']}:{x['line']}: {x['quote']}")
(E/'RAW/withdrawal_candidate_packet.txt').write_text('\n'.join(packet))
save('COMMANDS.json',commands);(E/'scripts/supplement.py').write_bytes(Path(__file__).read_bytes());print('metadata',[(x['path'],x['candidate_run_rows'],x['amended_rows']) for x in meta]);print('transitions',len(tr),len({x['path'] for x in tr}),all(x['status']=='PASS' for x in tr));print('archives',len(archives),all(x['equal'] for x in archives));print('copies',copychecks);print('withdrawal',len(withdraw))
