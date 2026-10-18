"""QA-AF01 independent retest — Fable, QA Lead, 2026-10-17.
Read-only against the repository and the run; writes only under RUN/QA_RETEST_AF01/. Disposable BASE copies are exported
from read-only Git blobs (git archive) into the scratch directory given by QA_SCRATCH. No branch/worktree/index mutation.
Oracle = the unchanged amended index (AMENDED_V1/EXECUTION_PROPOSAL_INDEX.json) and pinned Git blobs — not Engineer output."""
from pathlib import Path
import json, hashlib, subprocess, os, shutil, sys, datetime, zipfile, difflib
RUN = Path('_AUDIT/SYNC_2026-10-15_doctrine-part2'); Q = RUN / 'QA_RETEST_AF01'; BASE = '9c179392f79b70da099121fc357d3107ad3bb86e'
SCR = Path(os.environ['QA_SCRATCH']) / 'qa_af01'; ZIP = Path('/home/moose/Downloads/FACTORY_QA_AF01_REPAIR_2026-10-17_173649.zip')
sha = lambda b: hashlib.sha256(b).hexdigest(); R = {}; raw = []; cmds = []
def run(args, cwd, env=None):
    p = subprocess.run(args, cwd=str(cwd), capture_output=True, text=True, env=env); rec = dict(cmd=args, cwd=str(cwd), exit=p.returncode, stdout=p.stdout, stderr=p.stderr); cmds.append(rec); return p
def note(k, v): R[k] = v; raw.append(f'{k}: {json.dumps(v, ensure_ascii=False)}'); print(k, '->', json.dumps(v, ensure_ascii=False)[:300])
if SCR.exists(): shutil.rmtree(SCR)
SCR.mkdir(parents=True)

# 0. Git state before (read-only)
refs = subprocess.check_output(['git', 'rev-parse', 'HEAD', 'main', 'origin/main']).decode().split(); staged = subprocess.check_output(['git', 'diff', '--cached', '--name-only']).decode()
assert refs[1] == refs[2] == BASE and refs[0] == '626da8d70f4db22987dc7fcc86765492072360cd' and not staged
note('git_before', dict(HEAD=refs[0], main=refs[1], origin_main=refs[2], staged=0))

# 1. Repair ZIP: hash, CRC, inventory, payload equals run directory
assert sha(ZIP.read_bytes()) == '9782260ccbd12fd6b76a844c0439e69796d8e6904e6912c9c78631215fdcf4ed'
zx = SCR / 'zip'; zx.mkdir()
with zipfile.ZipFile(ZIP) as z:
    assert z.testzip() is None; names = z.namelist(); assert all(not n.startswith('/') and '..' not in n for n in names); z.extractall(zx)
inv = [l.split('  ', 1) for l in (zx / 'SHA256SUMS.txt').read_text().splitlines() if l.strip()]
assert len(inv) == 45 and len(names) == 46
for h, p in inv: assert sha((zx / p).read_bytes()) == h, p
mism = []
for h, p in inv:
    local = RUN / p if p.startswith('REPAIR_QA_AF01/') else (RUN / p[len('CONTEXT/'):] if p.startswith('CONTEXT/') else None)
    if local is not None and sha(local.read_bytes()) != h: mism.append(p)
assert not mism, mism
note('repair_zip', dict(sha256='9782260c…', members=46, inventory=45, inventory_ok=True, payload_equals_run_dir=True))

# 2. Input identities and the exact serialization delta
corr = RUN / 'REPAIR_QA_AF01/EXECUTION_PROPOSAL.corrected.patch'; sub = RUN / 'AMENDED_V1/EXECUTION_PROPOSAL.patch'
idx_p = RUN / 'AMENDED_V1/EXECUTION_PROPOSAL_INDEX.json'; ed_p = RUN / 'AMENDED_V1/SELECTED_EXACT_EDITS.json'
cb, sb = corr.read_bytes(), sub.read_bytes()
assert sha(cb) == 'cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d' and len(cb) == 1906921
assert sha(sb) == 'ce4528d8db1183699ea8a90aaed266e91c991fe59b01747d4aa51e70acb3d58c' and len(sb) == 1906863
assert sha(idx_p.read_bytes()) == '69244f4edc347b30b81ed6a909bae4fbb5130864319e9f8cd84b5d5c22e59ba6' and sha(ed_p.read_bytes()) == '2675ffc148f49a95b688e9f252527950ce9c3f1fd61df3fb0ffb067fcc7ff687'
marker = b'\n\\ No newline at end of file\n'; assert cb.count(marker) == 2 and sb.count(b'\\ No newline') == 0
assert cb.replace(marker, b'\n', 2) != sb  # naive replacement is not the delta; verify the precise structure instead
# locate the two markers; each must follow the spoon footer line and precede the next file header
pos = [i for i in range(len(cb)) if cb.startswith(marker, i)]; where = []
for i in pos:
    before = cb[:i].rsplit(b'\n', 1)[1]; after = cb[i + len(marker):i + len(marker) + 13]
    assert before == '+🥄 *Part of Stark Industries — App Factory doctrine.*'.encode() and after == b'--- /dev/null', (before, after)
    where.append(cb[:i].count(b'\n') + 1)
# removing only the 29-byte sequence "\n\ No newline at end of file\n" minus the LF that must remain → reconstruct submitted
recon = cb.replace(marker, b'', 2); assert len(cb) - len(recon) == 58
assert recon == sb, 'removing the two inserted sequences must reproduce the submitted patch byte-for-byte'
note('serialization_delta', dict(inserted_sequences=2, bytes_added=58, marker_lines=where, removing_them_reproduces_submitted_patch=True, old_marker_count_in_submitted=0))

# 3. Fresh disposable BASE copies from read-only git archive
def export(name):
    d = SCR / name; d.mkdir(); p = subprocess.run(f'git archive {BASE} | tar -x -C {d}', shell=True, capture_output=True, text=True); assert p.returncode == 0, p.stderr; return d
A, B, C = export('apply_check'), export('gnu_patch'), export('closeout_and_content')
base_files = {str(p.relative_to(A)) for p in A.rglob('*') if p.is_file()}
pa = run(['git', 'apply', '--check', '-p0', str(corr.resolve())], A); assert pa.returncode == 0 and not pa.stderr.strip(), pa.stderr
note('git_apply_check_corrected_patch', dict(exit=pa.returncode, stderr=pa.stderr, cwd='fresh BASE export (no .git)'))
pa_old = run(['git', 'apply', '--check', '-p0', str(sub.resolve())], A)
note('git_apply_check_submitted_patch_control', dict(exit=pa_old.returncode, stderr=pa_old.stderr.strip()[:200]))
pb = run(['patch', '--batch', '--fuzz=0', '-p0', '-i', str(corr.resolve())], B); assert pb.returncode == 0, pb.stdout + pb.stderr
assert 'rej' not in pb.stdout and 'fuzz' not in pb.stdout.lower() and 'offset' not in pb.stdout.lower()
note('gnu_patch_replay', dict(exit=pb.returncode, hunks_reported=pb.stdout.count('patching file'), rejects_or_fuzz=False))

# 4. 101 outputs vs the unchanged amended index; exact scope; no stray files
idx = json.loads(idx_p.read_text()); assert len(idx) == 101
hashes = {}; bad = []
for e in idx:
    b = (B / e['path']).read_bytes(); hashes[e['path']] = dict(sha256=sha(b), bytes=len(b), expected=e['proposed_sha256'], expected_bytes=e['bytes'])
    if sha(b) != e['proposed_sha256'] or len(b) != e['bytes']: bad.append(e['path'])
assert not bad, bad
after_files = {str(p.relative_to(B)) for p in B.rglob('*') if p.is_file()}
added = sorted(after_files - base_files); modified = sorted(p for p in base_files if (B / p).read_bytes() != (A / p).read_bytes())
exp_added = sorted(e['path'] for e in idx if not e['before_sha256']); exp_mod = sorted(e['path'] for e in idx if e['before_sha256'])
assert added == exp_added and modified == exp_mod and len(added) == 68 and len(modified) == 33, (len(added), len(modified))
assert not [p for p in after_files if p.endswith(('.rej', '.orig')) or '__pycache__' in p]
for e in idx:
    if e['before_sha256']: assert sha(subprocess.check_output(['git', 'show', f"{BASE}:{e['path']}"])) == e['before_sha256'] == sha((A / e['path']).read_bytes())
(Q / 'REPLAY_101_HASHES.json').write_text(json.dumps(hashes, indent=1) + '\n')
note('outputs_vs_index', dict(exact=101, of=101, modified=33, added=68, stray_files=0, before_hashes_equal_pinned_blobs=33))

# 5. Archive fidelity: bytes, blob IDs (hash-object without -w), absent final LF
arch = {}
for a, src, blob, size in [('_ARCHIVE/FRONTEND_BUILD_PHASE_PLAYBOOK_v1_2_2.md', '03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md', '3edb88c3149a9a6d9a7c760471f30956053c9d60', 23578),
                           ('_ARCHIVE/FRONTEND_FIRST_PLAYBOOK_v1_1_3.md', '03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md', 'c8516c8b8b3950e4b2d08d0bb2c112d7136d8f30', 15043)]:
    rb = (B / a).read_bytes(); src_blob = subprocess.check_output(['git', 'rev-parse', f'{BASE}:{src}']).decode().strip()
    rep_blob = subprocess.check_output(['git', 'hash-object', '--no-filters', str(B / a)]).decode().strip()
    assert src_blob == blob == rep_blob and len(rb) == size and rb == subprocess.check_output(['git', 'show', f'{BASE}:{src}']) and rb[-1:] != b'\n'
    arch[a] = dict(source=src, blob=blob, replayed_blob=rep_blob, bytes=len(rb), final_LF=False, equals_base_bytes=True)
(Q / 'ARCHIVE_BLOBS.json').write_text(json.dumps(arch, indent=1) + '\n'); note('archive_fidelity', {k: 'exact' for k in arch})
# all 31 outgoing archives equal their BASE source blobs (carry-forward of AC23 on the replayed tree)
plan = json.loads((RUN / 'DOCUMENT_VERSION_AND_ARCHIVE_PLAN.json').read_text())
n_arch = 0
for e in idx:
    if e['path'].startswith('_ARCHIVE/') and e['path'] != '_ARCHIVE/QA_PLAYBOOK_v1_0.md':
        src = next((x['path'] for x in idx if x['before_sha256'] and Path(x['path']).stem == e['path'].split('/')[1].rsplit('_v', 1)[0]), None); assert src, e['path']
        assert (B / e['path']).read_bytes() == subprocess.check_output(['git', 'show', f'{BASE}:{src}']); n_arch += 1
assert n_arch == 31; note('all_outgoing_archives_equal_BASE_sources', n_arch)

# 6. Pinned lint suite on the replayed tree; lint scripts identical to repo; no bytecode left behind
for p in Path('lints').glob('*.py'): assert p.read_bytes() == (B / 'lints' / p.name).read_bytes()
pl = run(['python3', '-B', '-I', 'lints/run_all.py'], B, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}); assert pl.returncode == 0, pl.stdout + pl.stderr
assert not list(B.rglob('__pycache__')); (Q / 'LINT_RAW.txt').write_text(f'cwd: {B}\nexit: {pl.returncode}\n' + pl.stdout + pl.stderr)
note('lint_suite_on_replayed_tree', dict(exit=0, tail=pl.stdout.strip().splitlines()[-1] if pl.stdout.strip() else ''))

# 7. Other patch artifacts: conditional closeout patch applies on the replayed tree; selected-content diff applies on BASE
pc = run(['git', 'apply', '--check', '-p0', str((RUN / 'POST_VERIFICATION_PROPOSAL.patch').resolve())], B); assert pc.returncode == 0, pc.stderr
tr = json.loads((RUN / 'POST_VERIFICATION_STATUS_TRANSITIONS.json').read_text()); post = {}
for t in tr['transitions']: s = post.get(t['path'], (B / t['path']).read_text()); assert s.count(t['old']) == t['occurrences']; post[t['path']] = s.replace(t['old'], t['new'])
for e in json.loads((RUN / 'POST_VERIFICATION_PROPOSAL_INDEX.json').read_text()): assert sha(post[e['path']].encode()) == e['proposed_sha256']
ps = run(['git', 'apply', '--check', '-p1', str((RUN / 'AMENDED_V1/SELECTED_CONTENT_DIFF.patch').resolve())], C); assert ps.returncode == 0, ps.stderr
note('other_patch_artifacts', dict(closeout_patch_git_apply_check_exit=pc.returncode, closeout_12_spans_replay_to_post_index=True, selected_content_diff_git_apply_check_exit=ps.returncode))

# 8. Carry-forward: 380 ordered edits replay from pinned blobs to the amended content index; 3 amended docs equal the replayed tree after metadata residual
ed = json.loads(ed_p.read_text()); assert len(ed) == 380
state = {}
for e in ed:
    s = state.get(e['path']) or subprocess.check_output(['git', 'show', f"{BASE}:{e['path']}"]).decode(); assert s.count(e['old']) == 1, e['sequence']; state[e['path']] = s.replace(e['old'], e['new'])
for e in json.loads((RUN / 'AMENDED_V1/SELECTED_CONTENT_INDEX.json').read_text()): assert sha(state[e['path']].encode()) == e['proposed_sha256'], e['path']
for p in ['01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md', '02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md', '02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md']:
    assert (B / p).read_bytes() == (RUN / 'AMENDED_V1/PROPOSED_CONTENT' / p).read_bytes()
    res = [l for l in difflib.unified_diff(state[p].splitlines(True), (B / p).read_text().splitlines(True), n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    assert sum(l.startswith('-') for l in res) == 1 and sum(l.startswith('+') for l in res) == 2, p
note('carry_forward_380_edits_to_content_index_and_amended_docs', dict(edits=380, content_index_docs=31, amended_docs_in_replayed_tree=3, residual='header bump + history row'))

# 9. Map / spec / source / review identities unchanged
fixed = {'UPDATE_MAP.md': 'cd291270bb6c8e537bcb050685c6464d326254f0d2a703c21f7f304dfe286931', 'DOCSET_SYNC_ACCEPTANCE_SPEC.md': '3910a62c34ff28acf1f9b956c5650deecae4ebd36872cc0072fd83e35ca19fa0',
         'QA_AMENDED_V1/DOCSET_SYNC_ACCEPTANCE_SPEC_AMENDED_V1.md': '103c7ede8a03e7bd0ea64f482e9d0b5a646b7720b8ae7f07729ea3482c9b8bd3', 'AMENDED_V1/AMENDMENT_V1.md': '655e24edf2c53b8ca89563a66ada54ab6df09b930eb80a7a2743216dc1153764',
         'AMENDED_V1/AMENDMENT_V1_EDITS.json': '274df38cbf0b2cefd91e05d505e71fc35d91f09cb16ca885234e80a300364893'}
for p, h in fixed.items(): assert sha((RUN / p).read_bytes()) == h, p
rev = json.loads((RUN / 'QA_AMENDED_V1/REVIEW_IDENTITIES.json').read_text())
for p, v in rev['amendment_records'].items(): assert sha((RUN / 'AMENDED_V1' / p).read_bytes()) == v['sha256'], p
for p, h in json.loads((RUN / 'PRESERVATION_BASELINE.json').read_text()).items(): assert sha(Path(p).read_bytes()) == h, p
for e in json.loads((RUN / 'EXECUTION_PROPOSAL_INDEX.json').read_text()): assert sha((RUN / 'PROPOSED_CONTENT' / e['path']).read_bytes()) == e['proposed_sha256']
note('identities_unchanged', dict(fixed=list(fixed), amended_v1_records=len(rev['amendment_records']), preservation_baseline=True, frozen_proposed_content=101))

# 10. Git state after
refs2 = subprocess.check_output(['git', 'rev-parse', 'HEAD', 'main', 'origin/main']).decode().split(); assert refs2 == refs and not subprocess.check_output(['git', 'diff', '--cached', '--name-only'])
assert not subprocess.check_output(['git', 'diff', BASE, '--', '01_CONSTITUTION', '02_PIPELINE_AGENTS', '03_BUILD_METHODOLOGY', '04_REFERENCE_MANUALS', '05_DESIGN_SYSTEM', 'MANIFEST.md', 'CHANGELOG.md', '_ARCHIVE', 'lints'])
note('git_after', dict(refs_unchanged=True, staged=0, canonical_diff_vs_BASE='empty', worktrees_or_branches_created=False))
shutil.rmtree(SCR)
out = dict(time=datetime.datetime.now().astimezone().isoformat(timespec='seconds'), seat='Fable, QA Lead', verdict='QA-AF01 CLOSED — PASS on independent retest of corrected patch cf6413c9…; 101/101 exact; both archives blob-exact; Git check 0; GNU patch 0; lints 0',
           corrected_patch_sha256='cf6413c9340c80f5c1bf53a55385876470e9b3aad364bc8963f52a68580f2a6d', amended_index_sha256='69244f4edc347b30b81ed6a909bae4fbb5130864319e9f8cd84b5d5c22e59ba6', checks=R)
(Q / 'RETEST_VERIFICATION.json').write_text(json.dumps(out, indent=2, ensure_ascii=False) + '\n'); (Q / 'RETEST_RAW.txt').write_text('\n'.join(raw) + '\n'); (Q / 'RETEST_COMMANDS.json').write_text(json.dumps(cmds, indent=1, ensure_ascii=False) + '\n')
print('RETEST PASS')
