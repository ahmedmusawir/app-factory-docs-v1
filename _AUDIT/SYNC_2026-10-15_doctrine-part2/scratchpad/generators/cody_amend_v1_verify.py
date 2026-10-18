"""AMENDED-v1 Engineer verification. Read-only except AMENDED_V1/VERIFICATION.json and VERIFICATION_RAW.txt.
Independent replay uses pinned git blobs (not BASELINE_CONTENT). Lints run on an overlay copy in the scratchpad.
Engineer checks only; independent acceptance (Fable) is pending."""
from pathlib import Path
import json, hashlib, subprocess, difflib, re, os, shutil, tempfile, datetime, sys
from markdown_it import MarkdownIt
R = Path('_AUDIT/SYNC_2026-10-15_doctrine-part2'); O = R / 'PROPOSED_CONTENT'; A = R / 'AMENDED_V1'
md = MarkdownIt('commonmark').enable('table'); sha = lambda b: hashlib.sha256(b if isinstance(b, bytes) else b.encode()).hexdigest()
base_sha = '9c179392f79b70da099121fc357d3107ad3bb86e'; checks = {}; raw = []
def note(k, v): checks[k] = v; raw.append(f'{k}: {json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v}')

# 0. Frozen Gate 2 records and protected files untouched
frozen = {'UPDATE_MAP.md': 'cd291270bb6c8e537bcb050685c6464d326254f0d2a703c21f7f304dfe286931', 'EXECUTION_PROPOSAL_INDEX.json': '84337dcd3b60d059e8c67d1586cd8dba58827c64e14ab46d6d05ab57a611da39', 'DOCSET_SYNC_ACCEPTANCE_SPEC.md': '3910a62c34ff28acf1f9b956c5650deecae4ebd36872cc0072fd83e35ca19fa0'}
for n, h in frozen.items(): assert sha((R / n).read_bytes()) == h, n
for p, h in json.loads((R / 'PRESERVATION_BASELINE.json').read_text()).items(): assert sha(Path(p).read_bytes()) == h, p
# MC_CORRECTION_PROTECTED.json pins Fable's 2026-10-16 DRAFT spec; Fable herself finalized it to v1.0 (3910a62c…) on 2026-10-17. Accept that attributable successor only.
fable_successors = {'DOCSET_SYNC_ACCEPTANCE_SPEC.md': frozen['DOCSET_SYNC_ACCEPTANCE_SPEC.md']}
for p, h in json.loads((R / 'MC_CORRECTION_PROTECTED.json').read_text()).items(): assert sha((R / p).read_bytes()) in (h, fable_successors.get(p)), p
fidx = json.loads((R / 'EXECUTION_PROPOSAL_INDEX.json').read_text())
for e in fidx: assert sha((O / e['path']).read_bytes()) == e['proposed_sha256'], ('FROZEN PROPOSED_CONTENT MUTATED', e['path'])
note('frozen_gate2_map_index_spec_and_protected_files_unchanged', 'PASS — map cd291270…, index 84337dcd…, spec 3910a62c…; PRESERVATION_BASELINE and MC_CORRECTION_PROTECTED hashes hold; all 101 frozen PROPOSED_CONTENT hashes hold')

# 1. Amendment edits: exact Architect/Jarvis text, unique in BASE blob, frozen proposed and amended proposed; intended containers
am = json.loads((A / 'AMENDMENT_V1_EDITS.json').read_text()); assert [e['sequence'] for e in am] == list(range(373, 381))
D1_NEW = ("## 📋 ENGINEERING PACKAGE: APPROVED CONTRACT ARTIFACTS\n\nThe Architect assembles the approved contract artifacts below for the Engineer to implement. DATA_CONTRACT is authored before Design; FILE_TREE is optional when implementation structure and boundaries are otherwise explicit.\n")
assert am[0]['old'] == "## 📋 ENGINEER AGENT: WHAT IT PRODUCES\n\nThe Engineer's full output list:\n" and am[0]['new'] == D1_NEW
assert am[1]['old'] == '> **Author:** Engineer Agent' and am[1]['new'] == '> **Author:** Architect'
assert (am[2]['old'], am[2]['new']) == ('| Define data schemas | Engineer Agent |', '| Implement approved data schemas as migrations and models | Engineer Agent |')
assert (am[3]['old'], am[3]['new']) == ('| Define API contracts | Engineer Agent |', '| Implement approved API contracts | Engineer Agent |')
assert [e['item'] for e in am] == ['D-1', 'D-2', 'OBS-1a', 'OBS-1b', 'P-1', 'P-2', 'P-3', 'P-4']
def amended_text(rel): p = A / 'PROPOSED_CONTENT' / rel; return p.read_text() if p.exists() else (O / rel).read_text()
for e in am:
    blob = subprocess.check_output(['git', 'show', base_sha + ':' + e['path']]).decode()
    assert blob.count(e['old']) == 1 and (O / e['path']).read_text().count(e['old']) == 1, e['item']
    s = amended_text(e['path']); assert s.count(e['old']) == 0 and s.count(e['new']) == 1, e['item']
def heading_above(text, needle):
    ln = text[:text.index(needle)].count('\n'); toks = md.parse(text); heads = [(t.map[0], toks[i + 1].content) for i, t in enumerate(toks) if t.type == 'heading_open' and t.map[0] <= ln]
    inside = [t for t in toks if t.map and t.map[0] <= ln < t.map[1] and t.type in ('table_open', 'fence', 'bullet_list_open')]
    return heads[-1][1], [t.type for t in inside]
cont = {}
# D-2 inside the §12 DATA_CONTRACT template fence, below the ownership note
en = amended_text('02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md'); ln = en[:en.index('> **Author:** Architect')].count('\n')
fences = [t for t in md.parse(en) if t.type == 'fence' and t.map[0] <= ln < t.map[1]]; assert len(fences) == 1 and '# DATA_CONTRACT: [Project Name]' in fences[0].content
assert en.index('the Architect authors DATA_CONTRACT before Design') < en.index('> **Author:** Architect'); cont['E374'] = f'ENGINEER_PLAYBOOK line {ln + 1}, inside the §12 DATA_CONTRACT template fence, below the Architect-ownership note'
# D-1 heading is still an H2 heading followed by the lead paragraph and the DATA_CONTRACT H3
bl = amended_text('01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md'); toks = md.parse(bl); i = next(i for i, t in enumerate(toks) if t.type == 'heading_open' and toks[i + 1].content == '📋 ENGINEERING PACKAGE: APPROVED CONTRACT ARTIFACTS'); assert toks[i].tag == 'h2'
after = [t for t in toks[i + 3:] if t.type in ('paragraph_open', 'heading_open')][:2]; assert after[0].type == 'paragraph_open' and after[1].type == 'heading_open' and after[1].tag == 'h3'; cont['E373'] = 'Blueprint H2 heading + lead paragraph; next heading is "### **DATA_CONTRACT.md**"'
ar = amended_text('02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md')
for k, needle, exp_head, exp_c in [('E375', am[2]['new'], "What the Architect Does NOT Do", 'table_open'), ('E376', am[3]['new'], "What the Architect Does NOT Do", 'table_open'),
                                   ('E377', am[4]['new'], 'Phase 3: ENGINEERING (Architect Contract Assembly)', 'table_open'), ('E378', am[5]['new'], 'Phase 3: ENGINEERING (Architect Contract Assembly)', 'table_open'),
                                   ('E379', am[6]['new'], 'Core Responsibilities', 'table_open'), ('E380', am[7]['new'].strip(), 'Full-Stack Web App', 'bullet_list_open')]:
    text = {'E375': ar, 'E376': ar, 'E377': bl, 'E378': bl, 'E379': en, 'E380': en}[k]
    if k == 'E380':
        # ENGINEER_PLAYBOOK's §12 template fence nests ``` blocks, so markdown_it's fence parity is inverted from §12 to the end (pre-existing at BASE and Gate 2; check 7 counts it unchanged). Use line structure here.
        before = text[:text.index(needle)]; h = re.findall(r'^#{1,6} (.*)$', before, re.M)[-1]; assert h == exp_head and before.rsplit(h, 1)[1].count('**Engineer Focus:**') == 1 and needle.startswith('- '), (k, h); cont[k] = f'under "{h}" → **Engineer Focus:** bullet list (line structure; see note on fence parity)'
        continue
    h, c = heading_above(text, needle); assert h == exp_head and exp_c in c, (k, h, c); cont[k] = f'under "{h}" inside {exp_c}'
assert 'ENGINEER AGENT: WHAT IT PRODUCES' not in bl and "Engineer's full output list" not in bl and '**Author:** Engineer' not in en and 'Define data schemas' not in ar and 'Define API contracts' not in ar and '| Engineer |' not in bl and 'Define schemas, APIs' not in en and 'Database schema design' not in en
note('amendment_spans_exact_unique_and_in_intended_containers', cont)

# 2. Independent replay of 374 edits over pinned git blobs; residual per document equals the frozen residual
ed = json.loads((A / 'SELECTED_EXACT_EDITS.json').read_text()); assert len(ed) == 380 and ed[:372] == json.loads((R / 'SELECTED_EXACT_EDITS.json').read_text())
paths = sorted({e['path'] for e in ed}); state = {p: subprocess.check_output(['git', 'show', base_sha + ':' + p]).decode() for p in paths}; fstate = dict(state)
for e in ed:
    assert state[e['path']].count(e['old']) == 1, e['sequence']; state[e['path']] = state[e['path']].replace(e['old'], e['new'])
    if e['sequence'] <= 372: assert fstate[e['path']].count(e['old']) == 1; fstate[e['path']] = fstate[e['path']].replace(e['old'], e['new'])
for e in json.loads((A / 'SELECTED_CONTENT_INDEX.json').read_text()): assert sha(state[e['path']]) == e['proposed_sha256'], e['path']
def res(stage, final): return [l for l in difflib.unified_diff(stage.splitlines(True), final.splitlines(True), n=0) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
aidx = json.loads((A / 'EXECUTION_PROPOSAL_INDEX.json').read_text()); assert len(aidx) == 101
def amended_bytes(rel): p = A / 'PROPOSED_CONTENT' / rel; return p.read_bytes() if p.exists() else (O / rel).read_bytes()
shapes = {}
for p in paths:
    r_f = res(fstate[p], (O / p).read_text()); r_a = res(state[p], amended_bytes(p).decode()); assert r_f == r_a, p
    shapes[p.split('/')[-1]] = f'{sum(l.startswith("-") for l in r_a)}-/{sum(l.startswith("+") for l in r_a)}+'
assert all(v == '1-/2+' for k, v in shapes.items() if k != 'STARTER_KIT_HANDBOOK.md') and shapes['STARTER_KIT_HANDBOOK.md'] == '1-/5+'
note('replay_380_edits_over_pinned_blobs_residual_equals_frozen', {'edits': 380, 'documents': len(paths), 'residual_shape': '1 removed / 2 added (header bump + history row) for 30 docs; STARTER_KIT 1-/5+ (D-4, unchanged from Gate 2)'})

# 3. Index: 101 paths; 99 hashes identical to Gate 2; 2 amended; before-hashes = pinned blobs; canonical unchanged
changed = []
for a, f in zip(aidx, fidx):
    assert a['path'] == f['path'] and a['before_sha256'] == f['before_sha256']; b = amended_bytes(a['path']); assert sha(b) == a['proposed_sha256'] and len(b) == a['bytes'], a['path']
    g = subprocess.run(['git', 'show', base_sha + ':' + a['path']], capture_output=True); assert (sha(g.stdout) if g.returncode == 0 else None) == a['before_sha256'], a['path']
    if a['before_sha256']: assert sha(Path(a['path']).read_bytes()) == a['before_sha256'], ('CANONICAL MUTATED', a['path'])
    if a['proposed_sha256'] != f['proposed_sha256']: changed.append(a['path'])
assert changed == ['01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md', '02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md', '02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md']
note('index_101_paths_three_amended_hashes_before_hashes_pinned_canonical_untouched', {'changed': changed, 'unchanged': 101 - len(changed)})
# archives of the two docs are still the BASE bytes (amendment does not touch archives)
for arc, src in [('_ARCHIVE/APP_FACTORY_BLUEPRINT_v2_1.md', '01_CONSTITUTION/APP_FACTORY_BLUEPRINT.md'), ('_ARCHIVE/ARCHITECT_PLAYBOOK_v2_2.md', '02_PIPELINE_AGENTS/ARCHITECT_PLAYBOOK.md'), ('_ARCHIVE/ENGINEER_PLAYBOOK_v1_2.md', '02_PIPELINE_AGENTS/ENGINEER_PLAYBOOK.md')]: assert sha((O / arc).read_bytes()) == next(x['before_sha256'] for x in fidx if x['path'] == src), arc
note('outgoing_archives_of_amended_docs_still_BASE_bytes', 'PASS')

# 4. Metadata consistency: header line, history row and MANIFEST cells unchanged for the two documents
mf = (O / 'MANIFEST.md').read_text(); meta = {}
for p in changed:
    f = (O / p).read_text(); a = amended_bytes(p).decode(); hf = re.search(r'^> \*\*Version:\*\* (.*?) · \*\*Date:\*\* (.*?) · \*\*Status:\*\* (.*)$', f, re.M); ha = re.search(r'^> \*\*Version:\*\* (.*?) · \*\*Date:\*\* (.*?) · \*\*Status:\*\* (.*)$', a, re.M)
    assert hf.groups() == ha.groups(); rf = [l for l in f.splitlines() if 'Factory DocSet sync: approved workflow/security/reference corrections;' in l]; ra = [l for l in a.splitlines() if 'Factory DocSet sync: approved workflow/security/reference corrections;' in l]; assert rf == ra and len(ra) == 1
    row = next(x for x in mf.splitlines() if x.startswith('| ' + Path(p).stem + ' |')); cells = [x.strip() for x in row.split('|')][2:5]; assert cells == list(ha.groups())
    meta[Path(p).stem] = dict(version=ha[1], date=ha[2], status=ha[3])
note('headers_history_rows_MANIFEST_cells_unchanged_for_amended_docs', meta)

# 5. Landing-date plan identical spans, each occurring once in the amended overlay; transitions unaffected
ld = json.loads((A / 'LANDING_DATE_PLAN.json').read_text()); fl = json.loads((R / 'LANDING_DATE_PLAN.json').read_text()); assert ld['spans'] == fl['spans'] and ld['actual_landing_date'] is None and len(ld['spans']) == 151
sample = {}
for e in ld['spans']: s = sample.get(e['path'], amended_bytes(e['path']).decode()); assert s.count(e['old']) == e['occurrences'] == 1, e['path']; sample[e['path']] = s.replace(e['old'], e['new'].replace('<<ACTUAL_LANDING_DATE>>', '2099-01-02'))
tr = json.loads((R / 'POST_VERIFICATION_STATUS_TRANSITIONS.json').read_text()); assert not ({e['path'] for e in tr['transitions']} & set(changed)); assert tr['commit_plan']['actual_sha'] is None
post = {}
for e in tr['transitions']: s = post.get(e['path'], amended_bytes(e['path']).decode()); assert s.count(e['old']) == e['occurrences']; post[e['path']] = s.replace(e['old'], e['new'])
for e in json.loads((R / 'POST_VERIFICATION_PROPOSAL_INDEX.json').read_text()): assert sha(post[e['path']]) == e['proposed_sha256']
note('151_date_spans_unchanged_each_once_and_12_transitions_9_paths_unaffected', 'PASS — sample 2099-01-02 in memory only; actual landing date null')

# 6. Traceability and counts derived from data
tr2 = json.loads((A / 'WORKFLOW_RULING_TRACEABILITY.json').read_text()); r9 = next(e for e in tr2 if e['id'] == 'RUL-09'); assert r9['edit_ids'][-8:] == ['E%d' % i for i in range(373, 381)] and len(tr2) == 38
assert sum('amended' in e for e in tr2) == 1
c = json.loads((A / 'PROPOSAL_COUNTS.json').read_text()); assert c['ordered_edits'] == len(ed) == 380 and c['paths'] == len(aidx) == 101 and c['amendment_edits'] == 8 and c['amended_paths'] == 3 and c['changelog_rows'] == 39 and c['landing_date_spans'] == 151
ledger = (R / 'SELECTED_SCOPE_LEDGER.md').read_text(); assert len(re.findall(r'^\| FC-\d{3} \|', ledger, re.M)) == 97 and re.findall(r'^\| (FC-\d{3}) \| NO \|', ledger, re.M) == ['FC-085', 'FC-086', 'FC-097']
note('traceability_RUL09_gains_E373_E380_counts_from_data_97_FC_preserved', {'ordered_edits': 380, 'paths': 101, 'amended_paths': 3, 'changelog_rows': 39, 'date_spans': 151, 'transitions': '12 / 9'})

# 7. Unchanged lint suite on an overlay copy (frozen tree + two amended files), scratchpad only
scratch = Path(os.environ.get('CLAUDE_SCRATCH', tempfile.gettempdir())) / 'amended_v1_lint_tree'
if scratch.exists(): shutil.rmtree(scratch)
shutil.copytree(O, scratch)
for p in changed: (scratch / p).write_bytes(amended_bytes(p))
for p in Path('lints').glob('*.py'): assert p.read_bytes() == (scratch / 'lints' / p.name).read_bytes(), p
lp = subprocess.run(['python3', '-B', '-I', 'lints/run_all.py'], cwd=scratch, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}, capture_output=True, text=True)
raw.append('command: python3 -B -I lints/run_all.py\ncwd: ' + str(scratch) + '\nexit code: ' + str(lp.returncode) + '\n' + lp.stdout + lp.stderr); assert lp.returncode == 0, lp.stdout + lp.stderr
# markdown: no new unclosed fences in the three amended docs relative to frozen
for p in changed:
    for text in [amended_bytes(p).decode()]:
        lines = text.splitlines(); bad = [t.map for t in md.parse(text) if t.type == 'fence' and not lines[t.map[1] - 1].lstrip().startswith(t.markup)]; fl_ = (O / p).read_text().splitlines(); fbad = [t.map for t in md.parse((O / p).read_text()) if t.type == 'fence' and not fl_[t.map[1] - 1].lstrip().startswith(t.markup)]; assert len(bad) == len(fbad), p
shutil.rmtree(scratch)
note('unchanged_lint_suite_on_overlay_tree', 'PASS — exit 0; lint scripts byte-identical to repo lints/; no new unclosed fences in the three amended docs')

# 8. Ownership propagation sweep: every hit dispositioned (RESOLVED/RETAIN); no hit still carries an amended old span
hits = [l.split('\t') for l in (A / 'OWNERSHIP_PROPAGATION.tsv').read_text().splitlines()[1:] if l]
olds = [e['old'].strip().split('\n')[0] for e in am]
assert all(h[3].startswith(('RESOLVED', 'RETAIN')) for h in hits)
res_rows = [h for h in hits if h[3].startswith('RESOLVED')]; ret_rows = [h for h in hits if h[3].startswith('RETAIN')]
assert len(res_rows) == 8 and [h[4] for h in res_rows] == [o.strip()[:220] for o in olds]  # resolved rows cite the Gate 2 text they replace
assert not any(o in h[4] for h in ret_rows for o in olds)  # no retained live line still carries an amended old span
note('ownership_sweep_hits_all_dispositioned', {'hits': len(hits), 'resolved': 8, 'retained': sum(h[3].startswith('RETAIN') for h in hits), 'scanned': 'all live .md/.svg paths in the index excluding _ARCHIVE/ (templates and workflows included)'})

# 9. Git refs, staging and canonical worktree
assert subprocess.check_output(['git', 'rev-parse', 'HEAD', 'main', 'origin/main']).decode().split() == ['626da8d70f4db22987dc7fcc86765492072360cd', base_sha, base_sha]
assert not subprocess.check_output(['git', 'diff', '--cached', '--name-only']); assert not subprocess.check_output(['git', 'diff', base_sha, '--', '01_CONSTITUTION', '02_PIPELINE_AGENTS', '03_BUILD_METHODOLOGY', '04_REFERENCE_MANUALS', '05_DESIGN_SYSTEM', 'MANIFEST.md', 'CHANGELOG.md', '_ARCHIVE'])
note('git_refs_staging_canonical_worktree', 'Unchanged refs (HEAD 626da8d; main = origin/main = 9c17939); nothing staged; empty canonical diff; no Git mutation by Cody')

out = {'time': datetime.datetime.now().astimezone().isoformat(), 'status': 'ENGINEER CHECKS PASS — AMENDED-v1 (D-1/D-2 + OBS-1 + sweep, 8 edits, 3 documents) is a proposal; Gate 2 re-entry, Fable confirmation and Gate 3 pending; Phase 3 NOT RELEASED', 'checks': checks}
(A / 'VERIFICATION.json').write_text(json.dumps(out, indent=2, ensure_ascii=False) + '\n'); (A / 'VERIFICATION_RAW.txt').write_text('\n'.join(raw) + '\n'); print(json.dumps(out, indent=2, ensure_ascii=False))
