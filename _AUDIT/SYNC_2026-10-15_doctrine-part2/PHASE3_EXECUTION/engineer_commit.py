from pathlib import Path
exec(Path('/tmp/factory_phase3.py').read_text().split("if sys.argv[-1]=='apply':")[0])
import shutil
commands=js(ev/'COMMANDS.json');links=[]
for f in [*(root/'03_BUILD_METHODOLOGY/_templates/QAM').rglob('*.md'),*(root/'03_BUILD_METHODOLOGY/_workflows').glob('*.md')]:
 for link in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if '://' in link or link.startswith('#') or '<<' in link:continue
  target=(f.parent/link.split('#')[0]).resolve();assert target.exists(),(f,link);links.append({'file':str(f.relative_to(root)),'link':link,'exists':True})
snapshot=js(r/'INTAKE_SNAPSHOT_INDEX.json')['files'];assert len(snapshot)==189
for row in snapshot:assert sha((r/'INTAKE_SNAPSHOT'/row['path']).read_bytes())==row['sha256']
save(ev/'SUPPLEMENTARY_CHECKS.json',{'snapshot_files':189,'links':links,'template_state_owner_tables':'Installed bytes equal approved translations exactly; accepted semantics carried forward','independent_qa':'PENDING'})
shutil.copyfile('/tmp/factory_phase3.py',ev/'engineer_apply_verify.py');shutil.copyfile('/tmp/factory_phase3_commit.py',ev/'engineer_commit.py')
idx=js(r/'BOUND_EXECUTION_INDEX.json');paths=[v['path'] for v in idx];(ev/'IMPLEMENTATION_PATHS.nul').write_bytes(b'\0'.join(p.encode() for p in paths)+b'\0')
cmd(['git','add','--pathspec-from-file='+str(ev/'IMPLEMENTATION_PATHS.nul'),'--pathspec-file-nul'])
staged=git('diff','--cached','--name-status','--no-renames').decode();save(ev/'IMPLEMENTATION_PATHS.txt',staged)
assert set(line.split('\t')[1] for line in staged.splitlines())==set(paths)
assert sum(l.startswith('M\t') for l in staged.splitlines())==33
assert sum(l.startswith('A\t') for l in staged.splitlines())==68
for row in idx:assert sha(git('show',':'+row['path']))==row['proposed_sha256'],row['path']
cmd(['git','commit','-m','docs(sync): apply approved 101-path doctrine update [FC/W/RUL/AD-01; AMENDED-v1 380 edits]'])
content=git('rev-parse','HEAD').decode().strip();date=js(ev/'LANDING_DATE.json')['date'];assert git('show','-s','--format=%cs',content).decode().strip()==date
save(ev/'CONTENT_RECEIPT.json',{'content_sha':content,'setup_sha':setup,'base_sha':base,'landing_date':date,'paths':101,'modified':33,'added':68,'ordered_edits':380,'date_fields':151,'conditional_transitions_applied':0})
for row in idx:assert sha(git('show',content+':'+row['path']))==row['proposed_sha256']
receipt=js(r/'EXECUTION_SETUP/SETUP_RECEIPT.json');receipt.update(setup_head=setup,phase3_release='APPROVED — PHASE3_EXECUTION/DIRECTOR_RELEASE.md',status='Phase3 implementation complete; independent QA pending',waiting_on='Independent QA and conditional closeout',content_sha=content);save(r/'EXECUTION_SETUP/SETUP_RECEIPT.json',receipt)
save(r/'SYNC_HANDOFF.md',f'''# Engineering handoff — Phase3 complete; independent QA pending

## 0. Identities

CONTENT_SHA: `{content}`
BASE_SHA: `{base}`
SETUP_SHA: `{setup}`
Branch: `docs/sync-doctrine-part2-2026-10-15`
Destination: `https://github.com/ahmedmusawir/app-factory-docs-v1.git`
Preservation: `e7b4a6f33e1ae2442f71d82f7f3a9d694f50da36`; preparation checkpoint: `356206ab293dc3a3987269636bb853c84aaf4ad3`; standalone10x: `4ec73a40ce2ad91f0ed99b85638efc7fe375140d`.

## Scope and engineering evidence

All101 approved paths committed (33M/68A);380 ordered edits replayed; only151 declared fields bound to {date}. Bound execution and conditional indexes live at run root. All101 committed hashes verified. Frozen map, amendment, R1 specification and source records untouched; two10x files unchanged. Raw commands/cwd/exit/unfiltered output in PHASE3_EXECUTION/COMMANDS.json and VERIFY_RAW.txt. Supplementary snapshot/link checks and reproducible scripts included. First two verifier attempts are retained: routing-marker comparison and Python path-expression errors were verifier-only; no product changes resulted.

31 outgoing archives exact including EOF/blob state; historicalQA archive exact.25 installed templates source/translation/installed hashes recorded in TEMPLATE_INSTALL_VERIFICATION.md and PHASE3_EXECUTION/TEMPLATE_HASHES.json. Four workflows/SVGs follow approved7/18/8/24 steps.34MANIFEST rows equal headers. All four pinned lints PASS.189 intake snapshot hashes retained.641 protected run/reference files unchanged before new bookkeeping. Installed content equals reviewed proposal except declared date fields; previous independent proposal review is retained, not represented as candidate acceptance.

## Independent QA entry

Launch a fresh QA Executor session under Fable. Consume QA_RETEST_AF01/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1_R1.md read-only (SHA2562a3867cacef11c6bb0419a4c71229479efe703cee9fbcc1e4f71c0ac8e63f0fc). Record actual remote tip as QA_START_SHA and verify CONTENT_SHA ancestry. Re-run installed candidate checks, including manual semantic/Markdown judgment checks. Engineer evidence is not a GateQ verdict.

Authority alignment: Gate2/Gate3 actual approvals remain in QA_RETEST_AF01/DIRECTOR_DECISIONS.md. Later Phase3/Git/publication ruling is PHASE3_EXECUTION/DIRECTOR_RELEASE.md. It supersedes AC32's historical Tony-only Git wording; the separate two-file10x authorization extends AC1 scope. QA Lead owns any specification clarification; Engineer did not edit the contract.

## Dispositions and pending gates

97certified findings retain94YES/3NO dispositions;89selected canonical components implemented,5OUTSIDE and3NO preserved. Do not claim all97 resolved. SELECTED_SCOPE_LEDGER.md and EXTERNAL_FOLLOWUPS.md retain component owners/triggers, including kit/root/skill/CI, missing sources, platform permissions and deferred commerce designs. ABM/APBM standalone references are additive scope, not methodology integration.

All12 conditional transitions on9paths remain PENDING. No independent QA verdict, cleanup acceptance or Architect closeout exists for this candidate. New-document/workflow DRAFT/Proposed labels intentionally remain as approved. BOUND_STATUS_TRANSITIONS.json is a future plan, not completion evidence. Require independent product verdict, required cleanup/acceptance, Architect instruction and bounded closeout/retest before activation. Tony creates PR and merges; no main write or force push.

## Publication authorization

Tony explicitly authorized completed payload plus preparation,10x and verification/handoff records to the exact branch/destination above. Push follows this metadata commit. Remote tip will be recorded in delivery receipt after push; never preclaim own containing commit SHA.
''')
save(r/'RUN_SUMMARY.md',f'# Run summary — Phase3 implemented, QA pending\n\nCody ENGINEER. CONTENT_SHA {content}. Full handoff: SYNC_HANDOFF.md. Phase1/2 complete; Phase3 engineering complete. Phase4 independent QA/repair pending; Phase5 final approval/PR/merge pending; Phase6 main synchronization/close pending. Publication authorized by current Director release.12 conditional transitions pending; all97 findings are not claimed resolved. No QA/cleanup/closeout certification. EXTERNAL_FOLLOWUPS.md preserves exclusions.\n')
save(r/'OPERATOR_NEXT_STEPS.md','# Current next steps\n\nCody completed released Phase3. See SYNC_HANDOFF.md and PHASE3_EXECUTION/DIRECTOR_RELEASE.md for exact authority and identities. After verified normal branch push, Tony launches fresh independent QA under Fable against actual remote tip. QA Lead owns verdict/spec alignment; no routine Git commands required from Tony. Following independent QA and required cleanup/Architect closeout, apply only authorized conditional transitions and bounded retest. Tony creates PR and merges through GitHub; main sync/close follows. Never merge the old review branch.\n')
save(root/'RECOVERY.md',f'# Recovery State\n\nCody ENGINEER. Phase3 implemented at {content}; metadata handoff being prepared. Worktree {root}. Branch docs/sync-doctrine-part2-2026-10-15. Independent QA pending;12 conditional transitions unapplied. Publication authorized to named GitHub repo. Read {r}/SYNC_HANDOFF.md; frozen R1 spec consumed read-only.\n')
with (root/'agent_docs/SESSIONS/session_2026-10-18.md').open('a') as f:f.write(f'\n### Phase3 engineering COMPLETE\n\nCONTENT_SHA {content};101paths/380edits/151date bindings. Archives/templates/workflows/lints pass; frozen records and10x unchanged.12transitions pending. Next handoff commit and authorized push; then independent QA. Cody ENGINEER.\n')
print('CONTENT_SHA',content)
