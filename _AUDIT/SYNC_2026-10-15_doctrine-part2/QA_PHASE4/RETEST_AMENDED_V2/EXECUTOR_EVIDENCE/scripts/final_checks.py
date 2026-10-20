exec(compile(open('/tmp/qa_checks.py').read().split('idx=json.loads')[0],'/tmp/qa_checks.py','exec'))
import zipfile,collections
patch=(C/RUN/'AMENDED_V2/EXECUTION_PROPOSAL.patch').read_text().splitlines();i=0;p=None;checks=[]
while i<len(patch):
 l=patch[i]
 if l.startswith('+++ '):p=l[4:]
 m=re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',l)
 if m:
  a,ac,b,bc=[int(x) if x else 1 for x in m.groups()];before=[];after=[];i+=1
  while i<len(patch) and not patch[i].startswith(('@@','--- ')):
   t=patch[i]
   if t.startswith((' ','-')):before.append(t[1:])
   if t.startswith((' ','+')):after.append(t[1:])
   i+=1
  checks.append(dict(path=p,old_line=a,new_line=b,parent_hunk_equal=(P/p).read_text().splitlines()[a-1:a-1+ac]==before,candidate_hunk_equal=(C/p).read_text().splitlines()[b-1:b-1+bc]==after));continue
 i+=1
save('RAW/approved_patch_hunks.json',dict(hunks=checks,all_equal=all(x['parent_hunk_equal'] and x['candidate_hunk_equal'] for x in checks),note='Initial line-delta sequence comparison differs because Git and difflib align blank lines differently. Exact old/new hunk slices and whole-file exact-edit delta accounting establish equality without applying patch.'))
# ZIP copied source is absent in Downloads; pinned historical delivery hash is available.
p=C/RUN/'AMENDED_V2/INPUTS/FACTORY_QA_P4_VERDICT_HANDBACK_2026-10-19_122452.zip';expected='b486cccbf29fb677c84173594bfd00c12905b81f2382ae62f9c30572b28f7e5a';z=zipfile.ZipFile(p);save('RAW/copied_zip_identity.json',dict(path=str(p),expected=expected,actual=h(p.read_bytes()),equal=h(p.read_bytes())==expected,authority='Review RECOVERY/session and QA_PHASE4/DELIVERY_RECEIPT_P4_VERDICT.json',downloads_original_present=False,members=z.namelist(),safe=all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())))
# Read original approval and receipt authority; preserve direct source bytes, no engineering helper executed.
for rel in ['QA_RETEST_AF01/DIRECTOR_DECISIONS.md','AMENDED_V2/PREPARATION_AUTHORITY.md','AMENDED_V2_EXECUTION/EXECUTION_PLAN.md','AMENDED_V2_EXECUTION/START_STATE.json','AMENDED_V2_EXECUTION/STAGED_SCOPE.json','QA_PHASE4/DELIVERY_RECEIPT_P4_VERDICT.json']:
 p=R/RUN/rel
 if p.exists():(E/'RAW'/('authority_'+p.name)).write_bytes(p.read_bytes())
# Each additional path inspected by purpose, input copies and proposed bytes separately checked.
scope=json.loads((E/'RAW/scope.json').read_text())
for x in scope:
 p=x['path'];x['sha256']=h((C/p).read_bytes())
 if x['status']=='A':
  if '/INPUTS/' in p:x['purpose']='Sealed source evidence copy; independent copy/hash checks in copied_inputs and copied_zip_identity.'
  elif '/PROPOSED_CONTENT/' in p:x['purpose']='Approved seven-file content payload; equals independently hashed installed/blob bytes.'
  elif p.endswith('DIRECTOR_DECISIONS_V2.md'):x['purpose']='Additive attributable Gate 2 approval with exact index/patch and corrected seven-path scope.'
  elif '/AMENDED_V2_EXECUTION/' in p:x['purpose']='Engineering pre-commit execution/verification record; not accepted as independent QA proof.'
  elif '/AMENDED_V2/' in p:x['purpose']='Amendment proposal, exact edit provenance, identity or preparation-check record; independently checked as appropriate.'
  else:x['purpose']='UNEXPLAINED'
 x['frozen_overwrite']=x['status']!='A' and p.startswith(RUN+'/')
save('RAW/scope.json',scope)
# Extra map queries for withdrawal rows; raw hits retain all fences and history.
rows=json.loads((E/'RAW/withdrawal_candidate_passages.json').read_text());queries=json.loads((C/RUN/'SEARCH_QUERIES.json').read_text())['queries'];live=json.loads((E/'RAW/live_scope.json').read_text());queryhits=[]
for row in rows:
 pat=re.compile(queries[row['fc']],re.I)
 for p in live:
  for n,l in enumerate((C/p).read_text().splitlines(),1):
   if pat.search(l):queryhits.append(dict(fc=row['fc'],path=p,line=n,text=l))
save('RAW/withdrawal_query_hits.json',queryhits)
# Categorize full-commit whitespace by actual offending file, preserving original diagnostic.
full=[x for x in commands if x['command']==['git','diff','--check',cfg['parent'],cfg['candidate']]][0];bad=[]
for l in full['stdout'].splitlines():
 m=re.match(r'(.+):(\d+): (.*)',l)
 if m and (C/m.group(1)).is_file() and ('trailing whitespace' in m.group(3) or 'blank line' in m.group(3) or 'space before tab' in m.group(3)):
  p,n,msg=m.groups();b=(C/p).read_bytes().splitlines(keepends=True)[int(n)-1];kind='CRLF TSV evidence' if p.endswith('.tsv') and b.endswith(b'\r\n') else 'immutable patch context' if p.endswith('.patch') else 'preserved exact source quotation';bad.append(dict(path=p,line=int(n),diagnostic=msg,category=kind,line_repr=repr(b),canonical=not p.startswith(RUN+'/')))
save('RAW/whitespace_classification.json',bad)
# compare base lints and root instructions, modes by Git trees
run(['git','diff','--name-status',cfg['base'],cfg['candidate'],'--','lints','.github','_SKILLS','CLAUDE.md','AGENTS.md'])
save('COMMANDS.json',commands);(E/'scripts/final_checks.py').write_bytes(Path(__file__).read_bytes());print('patch hunks',len(checks),all(x['parent_hunk_equal'] and x['candidate_hunk_equal'] for x in checks),'whitespace',len(bad),'withdrawal queries',len(queryhits))
