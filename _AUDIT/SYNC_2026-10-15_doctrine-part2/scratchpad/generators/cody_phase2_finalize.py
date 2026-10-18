from pathlib import Path
import json,csv,re,collections,hashlib,colorsys,subprocess,datetime,shutil
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');O=R/'PROPOSED_CONTENT';ed=json.loads((R/'SELECTED_EXACT_EDITS.json').read_text());src={x['id']:x for x in json.loads((R/'scratchpad/fc_sources.json').read_text())}
# Retained source quotes were read in six batches (0–1200); repair choices recorded as exact edits.
# History eligibility is checked against source heading boundaries, never just a keyword.
rows=list(csv.DictReader((R/'PROPAGATION.tsv').open(),delimiter='\t'))
def history(x):
 if x['path']=='CHANGELOG.md':return True
 fence=None;head=''
 for line in Path(x['path']).read_text().splitlines()[:int(x['line'])]:
  m=re.match(r'^(`{3,}|~{3,})',line)
  if m:
   if fence is None:fence=m[1]
   elif m[1][0]==fence[0] and len(m[1])>=len(fence):fence=None
  elif fence is None and re.match(r'^#{1,6} ',line):head=line
 return bool(re.search('Version History|Changelog',head,re.I)) and bool(re.match(r'^\| \d',x['quote']))
for x in rows:
 q=x['query_id'] if 'query_id' in x else x.get('query',x.get('id',''))
 # Detect query column without guessing hidden field names.
 if q not in src and q!='WORKFLOW':
  q=next((v for v in x.values() if v in src or v=='WORKFLOW'),q)
 text=(O/x['path']).read_text()
 if x['quote'] not in text:
  x.update(disposition='CHANGE',review_state='ENGINEER REVIEWED — exact proposed replacement/withdrawal',reason='Source occurrence changed in EXECUTION_PROPOSAL.patch; ordered edit record carries full old/new text. This is propagation disposition, not runtime or finding closure.')
 elif history(x):
  x.update(disposition='HISTORY',review_state='ENGINEER REVIEWED — actual source history boundary checked',reason='Dated/version table row under the document Version History or root CHANGELOG; preserved as history, not active instructions.')
 elif q in {'FC-009','FC-041','FC-042','FC-072'} and re.search(r'kit|src/|canonical|CURRENT_APP|Mark IV|KNOWN_ISSUES|breakpoint|protectPage',x['quote'],re.I):
  x.update(disposition='OUT-OF-SCOPE',review_state='ENGINEER REVIEWED — external verification remains open',reason='Retained historical locator/interface or recon/verification instruction; no new kit fact certified. EXTERNAL_FOLLOWUPS.md names Jarvis coordination and immutable-revision evidence trigger. Unsafe callable recipes were withdrawn; full finding remains open.')
 else:
  title=src.get(q,{}).get('title','approved module workflow and QA responsibilities')
  x.update(disposition='CONSISTENT',review_state='ENGINEER REVIEWED — retained quote within selected document scope',reason='Retained heading, requirement, consumer reference, explicitly negative example or contextual field lesson does not contradict the selected correction: '+title+'. Read with current exact replacement at its governing section; no claim of verified kit/runtime behavior or campaign closure.')
with (R/'PROPAGATION.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
counts=dict(collections.Counter(x['disposition'] for x in rows));assert sum(counts.values())==2236;assert 'PENDING' not in counts
# Preserve individual quotes/IDs and give a finite account of what this review proves.
(R/'PHASE_2_SEMANTIC_REVIEW.md').write_text('''# Engineer propagation review — proposed text only

The 90 baseline searches and all 2,236 hit records are retained in SEARCH_QUERIES.json and PROPAGATION.tsv. The 1,201 unique initially retained active source lines were read in six batches; additional targeted scans covered filesystem authority, artifact ownership, Git inspection/mutation, FFM trees/boot sequences, role metadata, error handling, payment/state dependencies, deployment pinning, template provenance and actual history boundaries. Source-level findings produced additional exact replacements, including full withdrawal of unsafe code fences and their dependent recipes. This is Engineer review, not Fable’s acceptance specification or independent QA.

Final baseline-hit dispositions: '''+json.dumps(counts)+'''. Every record retains the quoted source, location, query and a disposition/reason. HISTORY is restricted to actual Version History/CHANGELOG boundaries (including 59 unique original history rows); active field lessons are not automatically history. OUT-OF-SCOPE means the named external fact remains unverified, not permission to run an unsafe example. CHANGE means the source occurrence is changed in the exact proposal; it does not mean its entire FC is resolved.

Selected safety approach: where a verified runnable replacement would require unavailable kit or project contracts, explicitly withdraw the old executable recipe and state the supported invariant. Preserve outgoing originals as history. Universal quote storage/subscription schema remain deferred. This materially reduces example code; Jarvis/Fable must assess the withdrawals and dependent references in the whole diff. No runtime examples, browsers, platforms or kit behavior were executed in this documentation preparation.

The complete diff and all new wording remain Engineer-proposed for Gate 2. Independent acceptance must examine whether a withdrawal actually contains the defect and whether any retained dependent instruction remains contradictory. Re-run search and semantic checks on the actual candidate after implementation and any repair; this review is not transferable to changed bytes without reconciliation.
''')
# Reconcile current map text, leaving verbatim intake material explicitly historical.
p=R/'UPDATE_MAP.md';m=p.read_text()
m=re.sub(r'\*\*Engineering completeness remains OPEN:\*\*[^\n]+','**Engineer preparation ready for map/spec review:** exact proposals, scope ledger, baseline-hit dispositions and integrity checks are recorded. Gate 2 is NOT approved; independent acceptance remains unwritten; operator preservation/setup is pending. See PHASE_2_SEMANTIC_REVIEW.md and PHASE_2_VERIFICATION.json.',m)
m=re.sub(r'## F\. Propagation status\n.*?(?=\n## G\.)','## F. Propagation status\n\nAll 2,236 baseline hits have Engineer dispositions: '+json.dumps(counts)+'. See PROPAGATION.tsv and PHASE_2_SEMANTIC_REVIEW.md for quotes, boundaries, retained external dependencies and limitations. This is not independent QA or full FC closure. Re-run on actual candidate bytes.\n',m,flags=re.S)
m=m.replace('Uncovered exact components are explicitly marked PENDING in SELECTED_SCOPE_LEDGER.','SELECTED_SCOPE_LEDGER maps every selected component to exact edits, new documents or derived records; external components remain explicitly tracked.')
m=m.replace('All template provenance links resolve to the committed intake snapshot after actual intake; their existence is a handoff check, not assumed today.','Template provenance links target the actual snapshot and current translation plan; byte/link checks are recorded. The snapshot is not yet committed; Tony’s preservation receipt is required.')
m=m.replace('remains a draft source until DEC-17 promotion/supersession is ruled','remains an unpromoted historical draft; RUL-14 settles current pinning without promoting this unrelated source')
m=m.replace('§K has explicit OPEN rows','§K / external ledger retain evidence-dependent components')
m=m.replace('scope split needs approval','scope split approved by RUL-08; external completion remains separate')
m=m.replace('Search evidence exists; final semantic disposition/exact selected recipe spans are part of K-MAP-FREEZE','Engineer dispositions and exact selected spans are supplied; independent review and Gate 2 approval remain required')
start=m.index('**Review request:**');m=m[:start]+'''**Review request:** Jarvis reviews the complete selected wording and scope split; Tony approves the exact map at Gate 2. Fable derives the independent LARGE acceptance specification from that approved map and standing invariants; Tony approves it at Gate 3. Obtain Tony’s preservation/setup receipts and verify baseline equivalence before Phase 3 release. Policy rulings alone approve none of those later gates.
'''
note='The source blocks below remain verbatim. Their earlier mapping-proposal/disposition annotations are retained as drafting history; SELECTED_SCOPE_LEDGER and RUL-08…15 govern current component selection, and §C exact proposals govern proposed text. No historical BLOCKED/OPEN label reopens an approved policy.'
while m.count(note)>1:
 pos=m.rfind(note);m=m[:pos]+m[pos+len(note):]
p.write_text(m)
# Numerical contrast is recalculated directly from final proposed declarations, not the old recipe.
s=(O/'05_DESIGN_SYSTEM/TOKEN_FILE.md').read_text();modes={}
for mode,selector,parent in [('Mist',':root',None),('Slate','.dark',None),('Bright','.theme-bright','Mist'),('Dark-deep','.dark.theme-deep','Slate')]:
 b=re.search(re.escape(selector)+r'\s*\{([^}]+)\}',s).group(1)
 v={k:tuple(map(float,(h,ss,ll))) for k,h,ss,ll in re.findall(r'--([\w-]+):\s*([\d.]+)\s+([\d.]+)%\s+([\d.]+)%',b)}
 modes[mode]={**(modes[parent] if parent else {}),**v}
def lum(v):
 h,ss,l=v;rgb=colorsys.hls_to_rgb(h/360,l/100,ss/100);return sum(c*w for c,w in zip([x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in rgb],[.2126,.7152,.0722]))
def ratio(a,b):lo,hi=sorted([lum(a),lum(b)]);return(hi+.05)/(lo+.05)
cr=[]
for mode,t in modes.items():
 pairs=[]
 for n in ['primary','accent','destructive','success','warning','info','role-superadmin','role-admin','role-member']:pairs +=[(n,'card'),(n,'background'),(n+'-foreground',n)]
 pairs += [('foreground','background'),('card-foreground','card'),('popover-foreground','popover'),('secondary-foreground','secondary'),('muted-foreground','muted')]
 for fg,bg in pairs:cr.append(dict(mode=mode,foreground=fg,background=bg,ratio=ratio(t[fg],t[bg])))
assert len(cr)==128 and min(x['ratio'] for x in cr)>=4.5
(R/'PHASE_2_CONTRAST_CHECK.json').write_text(json.dumps({'source':str(O/'05_DESIGN_SYSTEM/TOKEN_FILE.md'),'sha256':hashlib.sha256((O/'05_DESIGN_SYSTEM/TOKEN_FILE.md').read_bytes()).hexdigest(),'status':'ENGINEER numeric check; not rendering/accessibility certification','pairs':cr},indent=2)+'\n')
# Self-contained immutable governing skill and baseline material, sourced by read-only git show.
base='9c179392f79b70da099121fc357d3107ad3bb86e'
for rel in subprocess.check_output(['git','ls-tree','-r','--name-only',base,'_SKILLS/factory-docs-update']).decode().splitlines():
 d=R/'GOVERNING_SKILL_MAIN'/rel;d.parent.mkdir(parents=True,exist_ok=True);d.write_bytes(subprocess.check_output(['git','show',base+':'+rel]))
for rel in [*(str(p) for p in Path('.').glob('0*_*/*.md')),'MANIFEST.md','CHANGELOG.md']:
 d=R/'BASELINE_CONTENT'/rel;d.parent.mkdir(parents=True,exist_ok=True);d.write_bytes(subprocess.check_output(['git','show',base+':'+rel]))
for rel in ['astra-review/run-002/synthesis/PART1_FINDINGS_DISPOSITION.md','astra-review/run-002/synthesis/QA/PART1_CONVERGENCE_QA.md']:
 d=R/'CERTIFIED_REVIEW'/Path(rel).name;d.parent.mkdir(exist_ok=True);d.write_bytes(Path(rel).read_bytes())
print('Reviewed propagation',counts,'; actual proposed contrast 128 pairs >=4.5; main skill and baseline copies saved.')
