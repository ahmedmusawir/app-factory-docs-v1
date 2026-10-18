from pathlib import Path
import json,hashlib,re,collections,subprocess,csv
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2')
checks=[]
def check(label,condition,detail=''):
 checks.append((label,bool(condition),detail))
base=json.loads((R/'PRESERVATION_BASELINE.json').read_text());bad=[p for p,h in base.items() if not Path(p).exists() or hashlib.sha256(Path(p).read_bytes()).hexdigest()!=h]
check('Preserved input fingerprints',not bad,f'{len(base)} files; mismatches={bad}')
src=json.loads((R/'scratchpad/fc_sources.json').read_text());m=(R/'UPDATE_MAP.md').read_text();ids=[e['id'] for e in src]
check('97 unique source findings',len(ids)==97 and len(set(ids))==97)
check('All verbatim source bodies embedded',all(e['body'] in m for e in src))
sev=collections.Counter(re.search(r'Severity (\w+)',e['body'])[1] for e in src)
check('Certified severity totals',dict(sev)==dict(BLOCKER=6,HIGH=36,MEDIUM=44,LOW=11),str(dict(sev)))
no=[e['id'] for e in src if 'Correction required NO' in e['body']]
check('Three NO correction findings',no==['FC-085','FC-086','FC-097'],str(no))
for file in ['PROPOSED_EXACT_EDITS.json','EXACT_CORRECTION_EDITS.json']:
 edits=json.loads((R/file).read_text());errors=[]
 for e in edits:
  text=Path(e['path']).read_text();lines=text.splitlines()
  # Mechanical repeated references are identified by recorded line rather than unique global count.
  if e['old'] not in '\n'.join(lines[e['start_line']-1:e['end_line']]):errors.append(e['id'])
 check(file+' source spans',not errors,f'{len(edits)} spans; errors={errors}')
placements=json.loads((R/'scratchpad/placements.json').read_text());bad=[]
for row in placements:
 for p in row['placements']:
  if Path(p['path']).read_text().splitlines()[p['line']-1]!=p['heading']:bad.append((row['id'],p))
check('Placement headings at exact recorded lines',not bad,str(bad))
plans=json.loads((R/'TEMPLATE_INSTALL_PLAN.json').read_text());bad=[]
for p in plans:
 b=Path(p['source']).read_bytes();s=b.decode()
 if hashlib.sha256(b).hexdigest()!=p['source_sha256']:bad.append(p['source'])
 for t in p['translations']:
  if s.count(t['old'])!=t['occurrences']:bad.append(p['source']+' occurrence')
  s=s.replace(t['old'],t['new'])
 if hashlib.sha256(s.encode()).hexdigest()!=p['proposed_destination_sha256']:bad.append(p['source']+' proposed hash')
check('25 proposed template translations simulate correctly',len(plans)==25 and not bad,str(bad))
check('Templates not installed',not Path('03_BUILD_METHODOLOGY/_templates/QAM').exists())
check('No inbox or claimed snapshot',not Path('_INBOX').exists())
canonical=['01_CONSTITUTION','02_PIPELINE_AGENTS','03_BUILD_METHODOLOGY','04_REFERENCE_MANUALS','05_DESIGN_SYSTEM','MANIFEST.md','CHANGELOG.md','_ARCHIVE','lints','.github','_OTHERS']
p=subprocess.run(['git','diff','--name-only','9c179392f79b70da099121fc357d3107ad3bb86e','--',*canonical],capture_output=True,text=True)
check('Canonical diff vs baseline empty',p.returncode==0 and not p.stdout,p.stdout)
p=subprocess.run(['git','diff','--cached','--name-only'],capture_output=True,text=True);check('Nothing staged',p.returncode==0 and not p.stdout,p.stdout)
p=subprocess.run(['git','rev-parse','HEAD','main','origin/main'],capture_output=True,text=True);check('Git refs unchanged',p.stdout.splitlines()==['626da8d70f4db22987dc7fcc86765492072360cd','9c179392f79b70da099121fc357d3107ad3bb86e','9c179392f79b70da099121fc357d3107ad3bb86e'])
rows=list(csv.DictReader((R/'PROPAGATION.tsv').open(),delimiter='\t'))
check('Propagation search rows recorded',bool(rows),f'{len(rows)} preliminary rows; NOT a completed semantic disposition review')
lines=['# Engineer review-draft verification','', 'This validates draft integrity and preservation, not implementation or independent QA. Recipe completeness and semantic propagation review remain open in UPDATE_MAP §K-MAP-FREEZE.','']
for label,ok,detail in checks:lines.append(f'- {"PASS" if ok else "FAIL"} — {label}: {detail}')
lines+=['','No product tests were run: only planning artifacts were created. Existing document lint baseline remains nine findings; no green-lint claim is made.']
(R/'REVIEW_DRAFT_VERIFICATION.md').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines));assert all(c[1] for c in checks)
