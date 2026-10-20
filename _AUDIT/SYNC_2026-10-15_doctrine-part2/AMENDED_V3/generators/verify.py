"""Independent mechanical replay + Engineer contextual review checks; not QA acceptance."""
from pathlib import Path
import json,hashlib,subprocess,tempfile,tarfile,re,csv,os,datetime
A=Path(__file__).resolve().parents[1];R=A.parent;W=Path('/home/moose/Documents/app-factory-docs-sync-execution');C='8dff354937bc7baf739370a9886497d9d5359186';RUN='_AUDIT/SYNC_2026-10-15_doctrine-part2/'
sha=lambda b:hashlib.sha256(b).hexdigest();checks={};commands=[]
def save(n,x):(A/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def cmd(args,cwd=W):
 p=subprocess.run(args,cwd=cwd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});commands.append(dict(command=args,cwd=str(cwd),exit=p.returncode,stdout=p.stdout,stderr=p.stderr));save('COMMANDS.json',commands);assert p.returncode==0,commands[-1];return p.stdout

def ck(k,ok,d):checks[k]={'status':'PASS' if ok else 'FAIL','evidence':d};assert ok,(k,d)
def blob(p):return subprocess.check_output(['git','-C',str(W),'show',C+':'+p])
refs=cmd(['git','show-ref']);assert cmd(['git','rev-parse','HEAD']).strip()==C and cmd(['git','status','--porcelain'])==''
# Frozen review source files: snapshot before verification and verify again at end.
protected={str(p.relative_to(R)):sha(p.read_bytes()) for p in R.rglob('*') if p.is_file() and 'AMENDED_V3' not in p.relative_to(R).parts}
idx=json.loads((A/'BOUND_EXECUTION_INDEX.json').read_text());ed=json.loads((A/'AMENDMENT_V3_EDITS.json').read_text());changed=sorted({e['path'] for e in ed});arch='04_REFERENCE_MANUALS/APP_ARCHITECTURE_MANUAL.md';st='04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md';api='04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md'
with tempfile.TemporaryDirectory(prefix='amended-v3-') as tmp:
 s=Path(tmp);tar=s/'candidate.tar';cmd(['git','archive','--format=tar','--output='+str(tar),C]);tree=s/'tree';tree.mkdir()
 with tarfile.open(tar) as t:t.extractall(tree,filter='data')
 before={str(p.relative_to(tree)):sha(p.read_bytes()) for p in tree.rglob('*') if p.is_file()}
 cmd(['git','apply','--check','-p0',str(A/'EXECUTION_PROPOSAL.patch')],tree);cmd(['git','apply','-p0',str(A/'EXECUTION_PROPOSAL.patch')],tree)
 after={str(p.relative_to(tree)):sha(p.read_bytes()) for p in tree.rglob('*') if p.is_file()}
 ck('R12_prime_scope',set(before)==set(after) and sorted(p for p in before if before[p]!=after[p])==changed==sorted([arch,st,'CHANGELOG.md']),'Exactly three paths in disposable export; no execution-worktree writes.')
 for p in changed:
  t=blob(p).decode()
  for e in ed:
   if e['path']==p:assert t.count(e['old'])==1;t=t.replace(e['old'],e['new'],1)
  assert t.encode()==(tree/p).read_bytes()==(A/'PROPOSED_CONTENT'/p).read_bytes()
 ck('exact_replay',True,'Eight edits replay exactly; patch applies -p0 and yields exact three proposed contents.')
 rows=[]
 for x in idx:
  p=x['path'];assert before[p]==x['before_sha256'] and after[p]==x['proposed_sha256'] and len((tree/p).read_bytes())==x['bytes'];rows.append(dict(path=p,before=before[p],proposed=after[p],changed=before[p]!=after[p]))
 save('PATH_VERIFICATION.json',rows);ck('R6_prime',len(rows)==101 and len({x['path'] for x in rows})==101 and sum(not x['changed'] for x in rows)==98,'101/101 exact;98 unchanged hashes;candidate before hashes independently derived.')
 prior=json.loads(blob(RUN+'AMENDED_V2/SELECTED_EXACT_EDITS.json'));selected=json.loads((A/'SELECTED_EXACT_EDITS.json').read_text());ck('prior_edits',selected[:409]==prior and selected[409:]==ed and [x['sequence'] for x in ed]==list(range(410,418)),'Original409 records preserved;E410–E417 appended.')
 def text(p):return (tree/p).read_text()
 def fences(t):return re.findall(r'^```[^\n]*\n(.*?)^```\s*$',t,re.M|re.S)
 code={}
 for p in [arch,st]:
  old=fences(blob(p).decode());new=fences(text(p));assert len(old)==len(new)
  strip=lambda c:'\n'.join(l for l in c.splitlines() if not l.lstrip().startswith('//'))
  assert [strip(x) for x in old]==[strip(x) for x in new]
  assert re.findall(r'^import .*$',blob(p).decode(),re.M)==re.findall(r'^import .*$',text(p),re.M)
  code[p]={'fences':len(old),'non_line_comment_fence_content_sha256':sha('\n'.join(map(strip,new)).encode()),'imports_unchanged':True}
 save('CODE_PRESERVATION.json',code);ck('labels_only',True,code)
 meta=[]
 for p in [arch,st]:
  old=blob(p).decode();new=text(p);header=re.search(r'^> \*\*Version:.*$',old,re.M).group();assert header in new
  a=[l for l in old.splitlines() if l.startswith('|') and '2026-10-18' in l];b=[l for l in new.splitlines() if l.startswith('|') and '2026-10-18' in l];assert len(a)==len(b)==1 and '; QA-P4 repair: RV2-F01 (AC16/FC-066 labels)' in b[0]
  assert re.findall(r'\d{4}-\d{2}-\d{2}',old)==re.findall(r'\d{4}-\d{2}-\d{2}',new)
  meta.append(dict(path=p,header=header,history=b[0]))
 rowscl=[l for l in text('CHANGELOG.md').splitlines() if l.startswith('| 2026-10-18 |')];assert len(rowscl)==39 and sum('RV2-F01 (AC16/FC-066 labels)' in l for l in rowscl)==2
 ck('R7_prime',before['MANIFEST.md']==after['MANIFEST.md'],'Headers/all dates unchanged; MANIFEST unchanged;39 run CHANGELOG rows, two amended; one existing history row amended per doc.');save('METADATA.json',meta)
 # Complete live-scope scan: every match must resolve to an inspected section and explicit contract.
 live=sorted([p for d in tree.glob('0[1-5]_*') for p in d.glob('*.md')]+[tree/'MANIFEST.md',tree/'CHANGELOG.md']);assert len(live)==36
 hits=[];contexts={}
 for f in live:
  rel=str(f.relative_to(tree));lines=f.read_text().splitlines();head='';start=0
  for i,line in enumerate(lines):
   if re.match(r'^#{1,6} ',line):head=line;start=i
   terms=[term for term in ['fetchProducts','services/productServices'] if term.lower() in line.lower()]
   if not terms:continue
   end=next((j for j in range(i+1,len(lines)) if re.match(r'^#{1,6} ',lines[j])),len(lines));context='\n'.join(lines[start:end]);category=None;rationale=None
   if line.startswith('|'):
    assert 'fetchProducts' in line and 'services/productServices' not in line
    category='VOCABULARY';rationale='Naming or layer-summary vocabulary; no result-shape assertion.'
   elif rel==api:
    if head=='### Normalizing External Responses':
     assert 'Independent normalization-step example' in context and 'Promise<Product[]>' in context and 'return wooProducts.map(normalizeProduct)' in context
     category='LABELLED_ALTERNATIVE';rationale='Explicit independent array-normalization label in this fence; named module and function return Product[] via map(normalizeProduct).'
    elif head=='### Graceful Degradation Pattern':
     assert 'only `success` carries `items: Product[]`' in context and "outcome.status !== 'success'" in context and 'products={outcome.items}' in context
     category='DECLARED_CONTRACT';rationale='Typed-outcome contract labelled before fence; success narrowed before passing items; no array/envelope mixing.'
    elif head=='### ISR and Revalidation':
     assert 'Independent ISR example' in context and 'raw JSON payload' in context and 'return response.json()' in context
     category='LABELLED_ALTERNATIVE';rationale='Explicit independent raw-JSON ISR contract; no consumer claims normalized array or typed envelope; project wire validation remains required.'
    elif head=='### Batch Operations':
     assert 'fetchProductsByIds' in line and 'ids: number[]): Promise<Product[]>' in context
     category='DISTINCT_OPERATION';rationale='fetchProductsByIds(ids) has its own explicit Product[] batch contract; not zero-argument fetchProducts.'
   elif rel==arch:
    if head=='### Server Components (Default)':
     assert 'Independent rendering illustration' in context and 'returns `Promise<Product[]>`' in context and 'products={products}' in context
     category='LABELLED_ALTERNATIVE';rationale='V3-1 explicitly scopes independent Product[] contract to rendering section; unchanged import/caller passes array to ProductList, not typed outcome.'
    elif head=='### Streaming and Suspense':
     assert '// Same independent Promise<Product[]> illustration as the Server Component example above.' in context and 'products={products}' in context
     category='LABELLED_ALTERNATIVE';rationale='V3-2 explicit fence comment binds streaming caller to the independent Product[] rendering illustration; array consumer agrees.'
    elif 'fetchProductBySlug' in line:
     assert 'const product = await fetchProductBySlug(slug)' in context and 'if (!product)' in context and 'product={product}' in context
     category='DISTINCT_OPERATION';rationale='Service-module match imports fetchProductBySlug, not fetchProducts; local single-product/not-found consumer consistent. No fetchProducts shape claim.'
   elif rel==st:
    if head=='### Store + Service Layer':
     good=next(j for j in range(start,end) if '// ✅ GOOD:' in lines[j])
     if i<good:
      assert '// ❌ BAD: Network call inside store' in context
      category='NEGATIVE_EXAMPLE';rationale='Explicit BAD store-network-call example before GOOD boundary; not endorsed service-contract guidance.'
     else:
      assert "// this local fetchProducts() returns the route's raw JSON array; it is not the API manual §3 typed-outcome service" in context and 'fetchProducts().then(setProducts)' in context and 'setProducts: (products) => set({ products })' in context
      category='LABELLED_ALTERNATIVE';rationale='V3-3 explicit local raw-JSON-array contract before definition; unchanged .then(setProducts) consumes same array. GOOD label alone is not relied on.'
    elif head=='### Store + Server Components':
     assert "This illustration's `fetchProducts()` returns `Promise<Product[]>`" in context and 'initialProducts: Product[];' in context and 'initialProducts={products}' in context
     category='LABELLED_ALTERNATIVE';rationale='V3-4 explicitly declares independent Product[]; both caller and prop type agree; typed-outcome narrowing guidance is separate.'
   assert category and rationale,('UNDISPOSITIONED',rel,i+1,head,line)
   contexts[rel+':'+str(start+1)]=context
   for term in terms:hits.append(dict(path=rel,line=i+1,term=term,disposition='RETAIN',category=category,rationale=rationale,text=line,container=head,context_start=start+1,context_end=end))
 with (A/'PROPAGATION.tsv').open('w',newline='') as f:
  writer=csv.DictWriter(f,fieldnames=list(hits[0]),delimiter='\t',lineterminator='\n');writer.writeheader();writer.writerows(hits)
 (A/'MANUAL_READS.md').write_text('# FC-066 complete container review\n\nEngineer semantic review, not independent QA acceptance. Each sweep hit points to one full container below. Unknown contexts fail closed; totals are observations, not acceptance criteria.\n\n'+''.join('## '+k+'\n\n````text\n'+v+'\n````\n\n' for k,v in contexts.items()))
 ck('R4_prime',bool(hits) and all(x['rationale'] for x in hits),{'scope_documents':len(live),'term_hits':len(hits),'unique_hit_lines':len({(x['path'],x['line']) for x in hits}),'reviewed_containers':len(contexts),'method':'Every occurrence mapped to full container; explicit contract/alternative/negative/vocabulary or distinct-operation rationale; no expected-count pass condition.'})
 # All prior changed files other than CHANGELOG stay byte-identical; its old repair rows stay intact.
 v2=json.loads(blob(RUN+'AMENDED_V2/AMENDMENT_IDENTITIES.json'))['changed_paths'];assert all(before[p]==after[p] for p in v2 if p!='CHANGELOG.md')
 assert [l for l in blob('CHANGELOG.md').decode().splitlines() if 'QA-P4 repair: F01–F05' in l]==[l for l in text('CHANGELOG.md').splitlines() if 'QA-P4 repair: F01–F05' in l]
 # STATE participates in R5, so do not claim whole-document byte identity. Compare actual RUL-13 surfaces.
 for needle in ['// Raw contact information is not persisted by default.','Do not persist raw contact details by default.']:
  oldline=next(l for l in blob(st).decode().splitlines() if needle in l);assert oldline in text(st)
 for heading in ['## 4. Persistence','## 6. Templates']:
  old=blob(st).decode()
  if heading in old:
   part=old.split(heading,1)[1].split('\n## ',1)[0];assert part==text(st).split(heading,1)[1].split('\n## ',1)[0]
 ck('carry_forward',True,'98 indexed paths byte-identical; all prior six repaired docs exact and six CHANGELOG repair clauses preserved. STATE changed only unrelated §7 labels/history: R5 persistence/default passages preserved, not a false whole-document identity claim.')
 transitions=json.loads(blob(RUN+'BOUND_STATUS_TRANSITIONS.json'));tr=transitions['transitions'];evidence=[]
 for e in tr:
  assert text(e['path']).count(e['old'])==e['occurrences'] and before[e['path']]==after[e['path']];evidence.append(dict(path=e['path'],old=e['old'],status='PENDING'))
 save('CLOSEOUT_TRANSITIONS.json',evidence);ck('R10_prime',len(evidence)==12 and len({x['path'] for x in evidence})==9,'Twelve pre-transition spans and nine paths unchanged.')
 l=cmd(['python3','-B','-I','lints/run_all.py'],tree);(A/'LINT_OUTPUT.txt').write_text(l);ck('R8_prime','RESULT: PASS' in l and l.count('0 hits')==3,'Unchanged full suite PASS;zero hits across36 live docs;headers PASS.')
 save('PRESERVATION_HASHES.json',{'candidate':before,'proposed':after});ck('protected_files',all(before[p]==after[p] for p in before if p not in changed),'All other candidate-export files byte-identical, including archives/templates/workflows/10x/spec/approvals/prior repair records.')
 ck('frozen_spec',after[RUN+'QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md']=='2a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc','Frozen specification untouched.')
ck('review_records_preserved',all(sha((R/p).read_bytes())==h for p,h in protected.items()),{'files_checked':len(protected)})
ck('R11_prime_preparation_boundary',cmd(['git','show-ref'])==refs and cmd(['git','status','--porcelain'])=='' and cmd(['git','rev-parse','HEAD']).strip()==C,'Execution clean and unchanged; no Git mutation. Actual Gate2/application/commit/push and independent R11′ retest PENDING.')
save('VERIFICATION.json',dict(time=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='ENGINEER PREPARATION CHECKS PASS — NOT independent acceptance',checks=checks,candidate=C,gate2='PENDING exact-patch approval',future_retest='R4′/R6′/R7′/R8′/R10′/R11′/R12′ and bounded carry-forward'))
print(json.dumps({k:v['status'] for k,v in checks.items()},indent=2))
