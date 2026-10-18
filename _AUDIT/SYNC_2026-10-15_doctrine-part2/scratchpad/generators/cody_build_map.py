from pathlib import Path
import json,re,hashlib,collections,subprocess,datetime
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');D=json.loads((R/'scratchpad/proposals.json').read_text());E=sorted(json.loads((R/'scratchpad/fc_sources.json').read_text()),key=lambda x:x['id']);F={p.stem:p for p in sorted(Path('.').glob('0*_*/*.md'))};scope=[str(p) for p in F.values()]+['MANIFEST.md','CHANGELOG.md'];A=D['aliases'];P=D['wording'];T=D['targets'];terms=D['terms'];base='9c179392f79b70da099121fc357d3107ad3bb86e'
manifest=Path('MANIFEST.md').read_text().splitlines(); reverse={}
for line in manifest:
 c=[x.strip() for x in line.split('|')]
 if len(c)==5 and c[1] in F and c[3].isdigit():reverse[c[1]]=(c[2],int(c[3]))
# Parse actual headings, excluding fenced template/code headings.
def heads(path):
 ls=path.read_text().splitlines();out=[];fence=False
 for i,l in enumerate(ls,1):
  if l.startswith('```'):fence=not fence;continue
  if not fence and re.match(r'^#{1,4} ',l):out.append((i,l))
 return out
H={str(p):heads(p) for p in F.values()};C=[];byid={};missing=[]
for e in E:
 n=str(int(e['id'][3:]));positions=[]
 for target in T.get(n,'').split(';'):
  if not target:continue
  alias,hs=target.split(':',1);path=F[A[alias]]
  for h in hs.split(','):
   hits=[(i,l) for i,l in H[str(path)] if re.sub(r'^#+ ','',l).startswith(h)]
   if not hits:missing.append((n,str(path),h));continue
   # The two API quick-reference headings are deliberately both retained in the placement evidence.
   for i,l in hits:positions.append({'path':str(path),'line':i,'heading':l})
 byid[e['id']]=positions
 if positions:C.append({'id':'C-'+e['id'][3:],'fc':e['id'],'placements':positions,'text':P[n]})
assert not missing,missing
(R/'scratchpad/placements.json').write_text(json.dumps(C,indent=2)+'\n')
# Planned source authority; conditional content remains BLOCKED, not silently deferred.
conditions={1:'DEC-06',3:'DEC-17 / DEC-19 remainder',4:'DEC-07 remainder',5:'DEC-06',6:'DEC-07 remainder',7:'DEC-07 host / K-ENGINE',8:'DEC-12 / DEC-08 root split',9:'DEC-19 remainder / RRM-09',10:'DEC-08',11:'DEC-18 remainder',12:'DEC-18 remainder',14:'DEC-14',15:'DEC-11',16:'DEC-10',17:'DEC-10',19:'DEC-10',22:'DEC-14 diagnostic authority',23:'DEC-14',27:'DEC-11',29:'DEC-14 / DEC-06',40:'DEC-15',41:'DEC-09 kit evidence',42:'DEC-09 kit evidence / DEC-06',50:'DEC-05 guest capability (required authorization still applies)',51:'DEC-05 design only (certified behavior remains required)',55:'K-SUBSCRIPTION-MODEL',60:'DEC-05',67:'DEC-05 pricing interface',72:'DEC-09 kit evidence',73:'DEC-06',81:'DEC-17 project-path part',88:'DEC-17 / DEC-18 remainder',89:'DEC-20'}
xb={5:'XB-02',6:'XB-02',8:'XB-01',9:'XB-04',10:'XB-01',41:'XB-04',42:'XB-04',72:'XB-04',90:'XB-01',91:'XB-01',92:'XB-02',94:'XB-01',95:'XB-02',96:'XB-02 / XB-03'};onlyxb={90,91,92,94,95};no={85,86,97}
def disp(n):return 'NO-CHANGE' if n in no else 'SPLIT' if n in onlyxb else 'BLOCKED' if n in conditions else 'CHANGE'
def cell(s):return str(s).replace('|','\\|').replace('\n','<br>')
# Full source/certified fields are copied unchanged; no proposed outcome is relabeled approved.
ledger=['# Phase 1 proposed intake ledger\n\nDRAFT — PRE-DROP REVIEW. No cargo has been dropped, no Gate 1 approval recorded, and no intake snapshot exists. Classification is proposed from indexed staging sources. Package 001 R3 remains DRAFT; certified correction dispositions are a separate field from approval to implement.\n\n| ID | Class | Source | Gist | Certified correction | Proposed disposition | Gate state |\n|---|---|---|---|---|---|---|']
for e in E:
 n=int(e['id'][3:]);cl='10 — regression guard' if n in no else '9 — cross-boundary' if n in onlyxb else '11 — draft correction awaiting intake approval';ledger.append(f"| {e['id']} | {cl} | `{e['source']}:{e['line']}` | {cell(e['title'])} | {'NO' if n in no else 'YES'} | {disp(n)}{' + '+xb[n] if n in xb and n not in onlyxb else ''} | Gate 1/2 pending; {cell(conditions.get(n,'source dispositions preserved; wording is proposed'))} |")
harvest=[]
for path,prefix,start in [('factory-intake/01_FACTORY_WORKFLOWS_INTAKE.md','WF',1),('factory-intake/02_RRM_INTAKE.md','RRM',13),('factory-intake/03_QAM_INTAKE.md','QAM',23)]:
 s=Path(path).read_text()
 for j,m in enumerate(re.finditer(r'^### ('+prefix+r'-\d{2}) — (.*?)\n([\s\S]*?)(?=^### |^## |\Z)',s,re.M)):
  old,title,body=m.groups();id=f'IN-2026-10-15-{start+j:02}';harvest.append(dict(id=id,old=old,title=title,body=body,path=path,line=s[:m.start()].count('\n')+1))
for h in harvest:
 conditional={'WF-01':'DEC-07 remainder','WF-02':'DEC-14','WF-03':'DEC-10/11/12','WF-08':'DEC-18 remainder','WF-09':'DEC-18 remainder','WF-10':'DEC-18 cloud part','RRM-03':'DEC-14 diagnostics','RRM-08':'ND-07','RRM-09':'RRM-09 placement'}.get(h['old'])
 ledger.append(f"| {h['id']} ({h['old']}) | 2 — intent / lesson | `{h['path']}:{h['line']}` | {h['title']} | n/a | {'BLOCKED' if conditional else 'CHANGE'} | Gate 1/2 pending; {conditional or 'RUL-01…07 control over historical proposals'} |")
extra=[('37','3 — new canonical document','factory-intake/QAM_PLAYBOOK_v1_0.md','Director-approved source QAM playbook; integrate with visible substitutions','CHANGE'),('38','7 — supporting template set (AD-01 placement)','factory-intake/INTAKE_ADDENDUM_001_v0_3/TEMPLATES/QAM/','25 accepted and verified source templates; installation not yet performed','CHANGE'),('39','7 — authority record','factory-intake/PLANNING_001/DIRECTOR_RULINGS_2026-10-14.md','RUL-01…07; preserve verbatim','NO-CHANGE'),('40','7 — authority record','factory-intake/PLANNING_001/ARCHITECT_DECISIONS_2026-10-14.md','AD-00 context / AD-01 delegated template placement','NO-CHANGE'),('41','7 — authority record','factory-intake/INTAKE_ADDENDUM_001_v0_3/QA_LEAD_DECISION_2026-10-14.md','Actual Fable decision; AM-1…3 and QAM-SR v1.0','NO-CHANGE'),('42','7 — verification record','factory-intake/INTAKE_ADDENDUM_001_v0_3/ARCHITECT_VERIFICATION_2026-10-14.md','Jarvis ZIP verification; not confirmation of regenerated local index','NO-CHANGE'),('43','7 — authority record','factory-corrections/DECISION_RECORD_001.md','Five scoped approvals, DEC-05 undecided','NO-CHANGE'),('44','7 — planning records','factory-intake/PLANNING_001/','R5 dependencies and clarification records; not policy approval','NO-CHANGE'),('45','7 — index/provenance records','factory-intake/INTAKE_ADDENDUM_001_v0_3/','Manifest/index/correction records; separate Architect instruction; no relabeling templates','NO-CHANGE')]
for num,cl,p,g,d in extra:ledger.append(f'| IN-2026-10-15-{num} | {cl} | `{p}` | {g} | n/a | {d} | Gate 1 pending; acceptance is not installation |')
si=json.loads(Path('factory-intake/SOURCE_INVENTORY.json').read_text())['sources']
for j,s in enumerate(si,46):ledger.append(f"| IN-2026-10-15-{j:02} | 8 — historical source / corroboration | `{s['package_path']}` | Preserve source bytes and original status; no independent adoption | n/a | NO-CHANGE | Gate 1 pending; source hash {s['sha256']} |")
ledger.append('\nNo DEFERRED disposition is assigned by the Engineer. A proposed BLOCKED row remains open until an attributable ruling or explicit scoped deferral. The three certified NO-correction records are FC-085, FC-086 and FC-097; source/reference NO-CHANGE rows are not extra certified findings.\n')
(R/'PHASE1_LEDGER.md').write_text('\n'.join(ledger))
# Seven parts survive independently as recoverable drafting work.
parts={i:[] for i in range(1,8)}
for e in E:
 n=int(e['id'][3:]);part=int(Path(e['source']).name[:2]);lines=[f"### {e['id']} — {e['title']}",f"\n**Proposed disposition:** {disp(n)}. **Authority:** certified correction {'NO' if n in no else 'YES'}; package outcome remains proposed. {('CONDITIONAL: '+conditions[n]+'.') if n in conditions else ''} {('Cross-boundary component: '+xb[n]+'.') if n in xb else ''}",f"\n**Source and preservation — INTAKE-VERBATIM** (`{e['source']}:{e['line']}`):\n",e['body'],f"\n**Mapping proposal — ENGINEER-PROPOSED:** {P[str(n)]}"]
 if byid[e['id']]:
  lines+=['\n**Verified live placements (BASE_SHA '+base+'):**']
  for x in byid[e['id']]:
   rev=reverse.get(Path(x['path']).stem,('not listed',0));lines.append(f"- `{x['path']}:{x['line']}` — {x['heading']}; MANIFEST ← {rev[1]}: {rev[0]}.")
  lines.append(f"\n**Touch proposal:** C-{n:03}. One merged edit per affected passage; apply shared text once, never duplicate overlapping FC proposals. Exact mechanical edits and shared workflow text are in §C. These paragraphs are proposed replacement requirements at the identified defective instruction, not permission to leave contradictory positive recipes underneath. Recipe contracts still conditional on a §K decision cannot be published as final runnable examples.")
 if n in no:lines.append('\n**Regression evidence:** main skill family (not the older review-branch copy): FC-085 family §2 says “Do not pull”; FC-086 sync-engineer Phase 4 says NO PUSH and Phase 5 gates publication; FC-097 README Step 3 and AP-11 identify `_INBOX/`. Certified severity remains unchanged; no correction proposed.')
 if n in onlyxb:lines.append('\n**No canonical touch row:** separate authorized job required; full intent and preservation retained above. This run does not close the cross-boundary finding.')
 lines.append(f"\n**Search:** query `{e['id']}` in PROPAGATION.tsv; exact pattern in SEARCH_QUERIES.json. Search covers all five canonical tiers, MANIFEST and CHANGELOG; read-only awareness is recorded separately. Every quoted hit retains a disposition and relationship to this proposal.\n\n**Verification:** use the source’s verbatim Verification intent above, the preservation constraints above, and §M; no completion or independent QA claim is made.\n")
 parts[part].append('\n'.join(lines))
mp=R/'scratchpad/map_parts';mp.mkdir(exist_ok=True)
for n,items in parts.items():(mp/f'PART_{n:02}.md').write_text(f'# PART_{n:02} — correction mapping draft\n\nDRAFT FOR REVIEW — no execution approval. Source outcomes are not relabeled approved.\n\n'+ '\n'.join(items))
(R/'scratchpad/harvest_sources.json').write_text(json.dumps(harvest,indent=2)+'\n')
print('Saved proposed Phase 1 ledger and seven mapping parts; 97 unique source blocks preserved.')
