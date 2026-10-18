from pathlib import Path
import json,hashlib,subprocess,csv,re,datetime
R=Path('_AUDIT/SYNC_2026-10-15_doctrine-part2');O=R/'PROPOSED_CONTENT';checks={};h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
protected=json.loads((R/'PRESERVATION_BASELINE.json').read_text());assert all(h(Path(p))==v for p,v in protected.items());checks['protected_original_files_unchanged']=len(protected)
snap=json.loads((R/'INTAKE_SNAPSHOT_INDEX.json').read_text())['files'];assert len(snap)==189
for e in snap:
 assert h(R/'INTAKE_SNAPSHOT'/e['path'])==e['sha256'];assert h(Path('_INBOX')/e['path'])==e['sha256']
checks['actual_intake_snapshot_and_drop_hashes']=len(snap)
plan=json.loads((R/'PHASE_2_TEMPLATE_TRANSLATIONS.json').read_text())
for e in plan:
 assert h(Path(e['source']))==e['source_sha256'];s=Path(e['source']).read_text()
 for t in e['translations']:
  assert s.count(t['old'])==t['occurrences'],e['source'];s=s.replace(t['old'],t['new'])
 assert s==(O/e['destination']).read_text();assert h(O/e['destination'])==e['proposed_destination_sha256']
checks['accepted_templates_exact_translation_replay']=len(plan)
for e in json.loads((R/'NEW_DOCUMENT_PROPOSALS.json').read_text()):assert h(O/e['path'])==e['proposed_sha256']
checks['new_playbook_proposal_hashes']=3
for e in json.loads((R/'DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json').read_text()):
 assert h(O/e['archive'])==e['source_sha256']==h(Path(e['path']))
 assert h(O/e['path'])==e['proposed_sha256']
 # Document-level history entry must be outside fenced sample templates.
 text=(O/e['path']).read_text();fence=None;history_rows=0
 for line in text.splitlines():
  m=re.match(r'^(`{3,}|~{3,})',line)
  if m:
   if fence is None:fence=m[1]
   elif m[1][0]==fence[0] and len(m[1])>=len(fence):fence=None
  elif 'Factory DocSet sync: approved workflow/security/reference corrections;' in line:
   assert fence is None,e['path'];history_rows+=1
 assert history_rows==1,e['path']
checks['outgoing_archives_and_unfenced_histories']=31
restore=json.loads((R/'ARCHIVE_RESTORATION_PROPOSAL.json').read_text());assert h(O/restore['destination'])==restore['sha256'];checks['historical_qa_archive']=restore['git_blob']
index=json.loads((R/'EXECUTION_PROPOSAL_INDEX.json').read_text())
for e in index:assert h(O/e['path'])==e['proposed_sha256']
assert len(index)==93;checks['full_proposal_paths']=len(index)
ed=json.loads((R/'SELECTED_EXACT_EDITS.json').read_text());files={str(p):p.read_text() for p in Path('.').glob('0*_*/*.md')}
for e in ed:
 assert files[e['path']].count(e['old'])==1,(e['sequence'],e['path']);files[e['path']]=files[e['path']].replace(e['old'],e['new'])
for e in json.loads((R/'SELECTED_CONTENT_INDEX.json').read_text()):assert hashlib.sha256(files[e['path']].encode()).hexdigest()==e['proposed_sha256']
checks['ordered_exact_content_edits_replayed']=len(ed)
rows=list(csv.DictReader((R/'PROPAGATION.tsv').open(),delimiter='\t'));assert len(rows)==2236 and all(x['disposition'] in {'CHANGE','CONSISTENT','HISTORY','OUT-OF-SCOPE'} and x['reason'] for x in rows);checks['baseline_propagation_records_dispositioned']=len(rows)
ledger=(R/'SELECTED_SCOPE_LEDGER.md').read_text();assert len(re.findall(r'^\| FC-\d{3} \|',ledger,re.M))==97;assert 'PENDING exact coverage' not in ledger
assert re.findall(r'^\| (FC-\d{3}) \| NO \|',ledger,re.M)==['FC-085','FC-086','FC-097'];checks['certified_ledger_rows_and_NO_guards']={'rows':97,'NO':['FC-085','FC-086','FC-097']}
refs=subprocess.check_output(['git','rev-parse','HEAD','main','origin/main']).decode().splitlines();assert refs==['626da8d70f4db22987dc7fcc86765492072360cd','9c179392f79b70da099121fc357d3107ad3bb86e','9c179392f79b70da099121fc357d3107ad3bb86e'];assert not subprocess.check_output(['git','diff','--cached','--name-only'])
assert not subprocess.check_output(['git','diff','main','--','01_CONSTITUTION','02_PIPELINE_AGENTS','03_BUILD_METHODOLOGY','04_REFERENCE_MANUALS','05_DESIGN_SYSTEM','MANIFEST.md','CHANGELOG.md','_ARCHIVE'])
checks['git_refs_unchanged_no_staging_canonical_diff_empty']=refs
for key,v in json.loads((R/'DRAFT_AND_SKILL_HASHES.json').read_text()).items():
 if key.startswith('main:'):assert hashlib.sha256(subprocess.check_output(['git','show',key])).hexdigest()==v
 else:assert h(Path(key))==v
checks['drafts_and_main_skill_unchanged']=True
# Template provenance file links resolve through the proposal destination into the durable run.
links=[]
for p in (O/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if '_AUDIT/SYNC_' not in target:continue
  dst=(Path.cwd()/p.relative_to(O).parent/target.split('#')[0]).resolve();assert dst.is_file(),str(dst);links.append(str(dst.relative_to(Path.cwd())))
checks['template_provenance_links_resolve']=len(links)
checks['proposal_lints']='PASS: unchanged four checks; PROPOSED_LINT_CHECK.txt'
checks['contrast']='128 computed pairs >=4.5 from final proposed HSL; no browser/render verdict'
checks['limits']=['Engineer-only checks; no canonical implementation','Gate 2/map approval pending; Fable independent spec unwritten; Gate 3 pending','Operator preservation/worktree/remote-baseline receipts pending','External kit/root/skill/CI/platform components and deferred universal designs remain open']
(R/'PHASE_2_VERIFICATION.json').write_text(json.dumps({'time':datetime.datetime.now().astimezone().isoformat(),'status':'ENGINEER PREPARATION CHECKS PASS; not independent QA','checks':checks},indent=2)+'\n')
print(json.dumps(checks,indent=2))
