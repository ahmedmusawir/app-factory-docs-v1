from pathlib import Path
import json,re,hashlib,difflib
from markdown_it import MarkdownIt
E=Path(__file__).resolve().parents[1];C=Path('/tmp/qa-phase4-20261019-054106/cand');B=C.parent/'base';R=C/'_AUDIT/SYNC_2026-10-15_doctrine-part2';checks=[]
def ck(ac,n,ok,d):checks.append(dict(ac=ac,name=n,ok=bool(ok),detail=d))
def sha(b):return hashlib.sha256(b).hexdigest()
def out(n,x):(E/'RAW'/n).write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
q=C/'03_BUILD_METHODOLOGY/_templates/QAM'
def route(n):return re.search(r'<!-- ROUTING TEXT[^>]*-->\n(.*?)<!-- END ROUTING TEXT -->',(q/n).read_text(),re.S)[1]
ck('AC14','routing bodies excluding directional comments',route('CLAUDE.md')==route('AGENTS.md'),'Marker comments intentionally name opposite file; body exact')
state=(q/'QAM_STATE.md').read_text().split('## Current state')[0];states=re.findall(r'`([^`]+)`',state.split('## State vocabulary')[1].split('\n\n',1)[1]);dispatch=(q/'QAM_ENTRY.md').read_text();ck('AC22','nineteen states',len(states)==19 and all(s in dispatch for s in states),states)
sr=[l for l in (q/'QAM_RISK_REQUIREMENTS.md').read_text().splitlines() if re.match(r'\| SR-\d+ \|',l)];source=R/'INTAKE_SNAPSHOT/factory-intake/INTAKE_ADDENDUM_001_v0_3/TEMPLATES/QAM/QAM_RISK_REQUIREMENTS.md';ck('AC22','eleven SR rows',len(sr)==11 and all(l in source.read_text() for l in sr),sr)
# Historical site 13: mixed-case detector in initial instrument omitted FFM.
p='03_BUILD_METHODOLOGY/FFM_PLAYBOOK.md';body=(C/p).read_text();i=1997;tokens=MarkdownIt('commonmark').enable('table').parse(body);types=[t.type for t in tokens if t.map and t.map[0]<i<=t.map[1]];ck('AC20','historical site 13', 'paragraph_open' in types and 'Availability is unverified' in body.splitlines()[i-1],dict(path=p,line=i,quote=body.splitlines()[i-1],types=types))
# Bound future index: recompute both sides without applying transitions to candidate.
d=json.loads((R/'BOUND_STATUS_TRANSITIONS.json').read_text());future={}
for t in d['transitions']:
 future[t['path']]=future.get(t['path'],(C/t['path']).read_text()).replace(t['old'],t['new'])
for x in d['index']:
 pre=(C/x['path']).read_bytes();post=future[x['path']].encode() if x['path'] in future else pre;ck('AC30','future bound '+x['path'],sha(pre)==x['before_sha256'] and sha(post)==x['proposed_sha256'],dict(pre=sha(pre),post=sha(post)))
# Representative preserved domain text, exact occurrence tested against BASE independently.
specimens=[('roles','04_REFERENCE_MANUALS/DATABASE_MANUAL.md',140,156),('RLS ownership and explicit public access','04_REFERENCE_MANUALS/DATABASE_MANUAL.md',362,415),('schema first','04_REFERENCE_MANUALS/DATABASE_MANUAL.md',35,41),('Navbar invariant','04_REFERENCE_MANUALS/AUTH_MANUAL.md',636,644),('state labor','04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md',86,112),('selective persistence','04_REFERENCE_MANUALS/STATE_MANAGEMENT_MANUAL.md',501,501),('AUTH-WALK/live DB','01_CONSTITUTION/STARTER_KIT_HANDBOOK.md',508,508),('money versus permission','04_REFERENCE_MANUALS/STRIPE_SUBSCRIPTIONS_PLAYBOOK.md',38,56),('raw-body signature','04_REFERENCE_MANUALS/ECOMMERCE_AND_PAYMENTS_MANUAL.md',374,390),('private data uncached','04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md',352,355),('server secrets','04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md',396,400),('wire/UI types','04_REFERENCE_MANUALS/API_AND_SERVICES_MANUAL.md',570,574)]
proof=[]
for label,p,a,b in specimens:
 lines=(C/p).read_text().splitlines();quote='\n'.join(lines[a-1:b]);proof.append(dict(family=label,path=p,start=a,end=b,quote=quote,byte_equal_span_in_base=quote in (B/p).read_text()))
out('ac17_preservation.json',proof)
# History order relative to approved plan and historical rows; fence status.
rows=[]
for v in json.loads((R/'DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json').read_text()):
 lines=(C/v['path']).read_text().splitlines();i=next(i for i,l in enumerate(lines) if l.startswith('|') and '2026-10-18' in l);a=i;b=i
 while a and lines[a-1].startswith('|'):a-=1
 while b+1<len(lines) and lines[b+1].startswith('|'):b+=1
 table=[l for l in lines[a:b+1] if re.match(r'^\|\s*[0-9(]',l)];expected_first=v['history_order']=='newest-first';ok=lines[i]==(table[0] if expected_first else table[-1]);rows.append(dict(path=v['path'],line=i+1,order=v['history_order'],table_start=a+1,table_end=b+1,ok=ok));ck('AC27','table order '+v['path'],ok,rows[-1])
out('ac27_table_order.json',rows)
recon=(C/'02_PIPELINE_AGENTS/RECON_QUESTIONNAIRE.md').read_text();ck('AC27','recon fence parity',sum(l.startswith('```') for l in recon.splitlines())%2==0,'even raw fences')
# Template hits classified: provenance/instructions/vocabulary vs populated records, retained in output for audit.
hits=(E/'RAW/supplement_template_values.txt').read_text().splitlines();classified=[]
for l in hits:
 cat='provenance' if 'TEMPLATE SET' in l or 'Source playbook SHA' in l else 'unfilled placeholder' if 'NOT RECORDED' in l or '<<' in l else 'instruction/vocabulary'
 classified.append(dict(hit=l,classification=cat))
out('ac22_classified_hits.json',classified)
# All FC counts and no-change/outside rows independently counted.
ledger=[l for l in (R/'SELECTED_SCOPE_LEDGER.md').read_text().splitlines() if re.match(r'\| FC-\d{3} \|',l)];counts={k:sum(k in l.split('|')[3] for l in ledger) for k in ['SELECTED','OUTSIDE','NO correction']};yes=sum(l.split('|')[2].strip()=='YES' for l in ledger);ck('AC3','disposition counts',counts=={'SELECTED':89,'OUTSIDE':5,'NO correction':3} and yes==94,dict(classes=counts,yes=yes,no=97-yes));out('ac36_remainder_rows.json',[l for l in ledger if re.search(r'FC-(005|006|008|009|010|041|042|072|090|091|092|094|095|096) \|',l)])
# Source references in new workflow links are exact; asset set checked from independently captured diff.
diff=(E/'RAW/ac1_name_status.txt').read_text();assets=[l for l in diff.splitlines() if '/_assets/' in l or '/_workflows/' in l];ck('AC28','exact 8 assets/workflow docs',len(assets)==8 and all(l.startswith('A\t') for l in assets),assets)
# Avoid calling JSON.stringify inside code examples a Markdown URL.
bad=[x for x in json.loads((E/'RAW/ac28_links.json').read_text()) if not x['exists']];ck('AC28','actual relative links resolve',all(x['target'].startswith('JSON.stringify') for x in bad),dict(false_regex_matches=bad))
# Missing new-document archives, full translation span count, historical install plans.
trans=json.loads((R/'PHASE_2_TEMPLATE_TRANSLATIONS.json').read_text());ck('AC22','31 translation spans',sum(len(x['translations']) for x in trans)==31,'per-file occurrence counts authoritative; CLAUDE/AGENTS have one status occurrence')
ck('AC22','historical plans',all('HISTORICAL' in (R/n).read_text() and 'SUPERSEDED' in (R/n).read_text() for n in ['TEMPLATE_INSTALL_PLAN.md','TEMPLATE_INSTALL_PLAN.json']),'both marked')
out('reconciled_checks.json',checks)
print(json.dumps(dict(checks=len(checks),failures=[x for x in checks if not x['ok']],preservation_changed=[x['family'] for x in proof if not x['byte_equal_span_in_base']]),indent=2))
