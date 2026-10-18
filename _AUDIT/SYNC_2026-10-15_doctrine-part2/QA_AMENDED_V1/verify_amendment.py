"""Independent read-only source checks; disposable replay/lint trees in /tmp.

Run from repository root: python3 -B -I <run>/QA_AMENDED_V1/verify_amendment.py
Writes evidence only beside this script. Executes no Engineer generator.
"""
import csv
import difflib
import hashlib
import json
import re
import subprocess
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path.cwd()
RUN = ROOT / '_AUDIT/SYNC_2026-10-15_doctrine-part2'
QA = RUN / 'QA_AMENDED_V1'
AMEND = RUN / 'AMENDED_V1'
BASE = '9c179392f79b70da099121fc357d3107ad3bb86e'
ZIP = Path('/home/moose/Downloads/FACTORY_AMENDED_V1_REVIEW_2026-10-17_145858.zip')
EXPECTED_ZIP = '711914a986cd64071f4372e0c428249ba27c6eba8ace160918c312d098b34f60'
scratch = Path(tempfile.mkdtemp(prefix='cody-qa-amended-v1-'))
checks = []


def digest(content):
    return hashlib.sha256(content).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def check(name, condition, detail):
    checks.append({'check': name, 'result': 'PASS' if condition else 'FAIL', 'detail': detail})
    print(f'{checks[-1]["result"]}: {name}: {detail}', flush=True)
    if not condition:
        save()
        raise AssertionError(name)


def save():
    (QA / 'VERIFICATION.json').write_text(json.dumps({
        'reviewer': 'Cody — QA Lead (Tony assignment 2026-10-17)',
        'time_utc': datetime.now(timezone.utc).isoformat(), 'base_sha': BASE,
        'source_zip': str(ZIP), 'source_zip_sha256': digest(ZIP.read_bytes()),
        'scratch': str(scratch), 'checks': checks,
        'scope': 'Amendment proposal confirmation; not installed-candidate Gate Q',
    }, indent=2) + '\n')


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


check('ZIP identity', digest(ZIP.read_bytes()) == EXPECTED_ZIP, EXPECTED_ZIP)
with zipfile.ZipFile(ZIP) as archive:
    members = archive.namelist()
    safe = len(members) == len(set(members)) and all(
        not Path(n).is_absolute() and '..' not in Path(n).parts and
        (archive.getinfo(n).external_attr >> 16) & 0o170000 != 0o120000 for n in members)
    check('ZIP integrity and safe paths', safe and archive.testzip() is None, f'{len(members)} members')
    inventory = [line.split('  ', 1) for line in archive.read('SHA256SUMS.txt').decode().splitlines() if line]
    check('Inventory completeness', len(inventory) == 27 and {p for _, p in inventory} == set(members) - {'SHA256SUMS.txt'}, '27 payload entries')
    for expected, path in inventory:
        assert digest(archive.read(path)) == expected, path
        if path.startswith('AMENDED_V1/'):
            assert archive.read(path) == (RUN / path).read_bytes(), path
        elif path.startswith('generators/'):
            assert archive.read(path) == (RUN / 'scratchpad' / path).read_bytes(), path
        else:
            assert archive.read(path) == (AMEND / path if path.startswith('README_') else RUN / path).read_bytes(), path
    check('Payload hashes and disk equality', True, '27/27 hashes and local counterparts')
    extract = scratch / 'source_zip'
    extract.mkdir()
    archive.extractall(extract)

frozen_edits = read_json(RUN / 'SELECTED_EXACT_EDITS.json')
edits = read_json(AMEND / 'SELECTED_EXACT_EDITS.json')
extra = read_json(AMEND / 'AMENDMENT_V1_EDITS.json')
check('Edit prefix and sequence', len(edits) == 380 and len(frozen_edits) == 372 and edits[:372] == frozen_edits and edits[372:] == extra and [e['sequence'] for e in edits] == list(range(1,381)), '372 unchanged + E373–E380')
index = read_json(AMEND / 'EXECUTION_PROPOSAL_INDEX.json')
frozen_index = read_json(RUN / 'EXECUTION_PROPOSAL_INDEX.json')
check('Path set', len(index) == 101 and [r['path'] for r in index] == [r['path'] for r in frozen_index], '101 unchanged paths')
composed = {}
changed = []
for row, old in zip(index, frozen_index):
    path = row['path']
    source = AMEND / 'PROPOSED_CONTENT' / path
    if not source.exists():
        source = RUN / 'PROPOSED_CONTENT' / path
    content = source.read_bytes()
    assert digest(content) == row['proposed_sha256'] and len(content) == row['bytes'], path
    assert row['before_sha256'] == old['before_sha256'], path
    if row['before_sha256']:
        assert digest(git('show', f'{BASE}:{path}')) == row['before_sha256'], path
    if row != old:
        changed.append(path)
    composed[path] = content
check('Composed hashes and baseline hashes', len(changed) == 3 and set(changed) == {e['path'] for e in extra}, '101/101 bytes and sizes; 33 before-hashes; only 3 documents differ')

replayed = {}
frozen_replayed = {}
for edit in edits:
    path = edit['path']
    if path not in replayed:
        replayed[path] = git('show', f'{BASE}:{path}').decode()
    assert replayed[path].count(edit['old']) == 1, (edit['sequence'], path)
    replayed[path] = replayed[path].replace(edit['old'], edit['new'], 1)
    if edit['sequence'] <= 372:
        frozen_replayed[path] = replayed[path]
for row in read_json(AMEND / 'SELECTED_CONTENT_INDEX.json'):
    assert digest(replayed[row['path']].encode()) == row['proposed_sha256'], row['path']
check('Independent ordered replay', True, f'380/380 old spans unique at their application step; {len(replayed)} content-stage hashes exact')

def residual(before, after):
    return [line for line in difflib.ndiff(before.splitlines(keepends=True), after.splitlines(keepends=True)) if line.startswith(('+ ', '- '))]

residuals = {}
for path, content in replayed.items():
    old_final = (RUN / 'PROPOSED_CONTENT' / path).read_text()
    new_final = composed[path].decode()
    old_residual = residual(frozen_replayed[path], old_final)
    new_residual = residual(content, new_final)
    assert old_residual == new_residual, path
    residuals[path] = new_residual
(QA / 'REPLAY_METADATA_RESIDUALS.json').write_text(json.dumps(residuals, indent=2) + '\n')
check('Metadata residual preservation', True, '31/31 residuals equal frozen proposal; D-4 adds no change')
for path in changed:
    content = (RUN / 'PROPOSED_CONTENT' / path).read_text()
    for edit in extra:
        if edit['path'] == path:
            assert content.count(edit['old']) == 1
            content = content.replace(edit['old'], edit['new'], 1)
    assert content.encode() == composed[path]
check('Eight edits over frozen proposed files', True, '3/3 amended files reproduced byte-exactly')

identities = read_json(AMEND / 'AMENDMENT_IDENTITIES.json')
for path, identity in identities['regenerated_records'].items():
    assert digest((RUN / path).read_bytes()) == identity['gate2_sha256'], path
    assert digest((AMEND / path).read_bytes()) == identity['amended_sha256'], path
for path, expected in identities['unaffected_records_sha256'].items():
    assert digest((RUN / path).read_bytes()) == expected, path
check('Regenerated and unaffected identities', True, '8 paired records and 13 unaffected records match')
for row in identities['amended_documents']:
    path = row['path']
    assert digest(composed[path]) == row['amended_proposed_sha256']
    assert len(composed[path]) == row['amended_bytes']
check('Amendment document identity table', True, '3/3 hashes and byte sizes match')

# Apply the distributed patch to a disposable pinned tree, with no Git mutation.
tree = scratch / 'composed'
tree.mkdir()
for path in git('ls-tree', '-r', '--name-only', BASE).decode().splitlines():
    if path.startswith(('01_', '02_', '03_', '04_', '05_', '_ARCHIVE/', 'lints/')) or path in ('MANIFEST.md', 'CHANGELOG.md'):
        target = tree / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(git('show', f'{BASE}:{path}'))
patch_command = ['patch', '--batch', '--fuzz=0', '-p0', '-i', str(AMEND / 'EXECUTION_PROPOSAL.patch')]
patched = subprocess.run(patch_command, cwd=tree, capture_output=True, text=True)
(QA / 'PATCH_REPLAY_RAW.txt').write_text(f'Command: {patch_command!r}\nWorking directory: {tree}\nExit: {patched.returncode}\n{patched.stdout}{patched.stderr}')
check('Distributed patch applies', patched.returncode == 0, 'patch --batch --fuzz=0 -p0 on disposable BASE tree')
patch_mismatches = []
for path, content in composed.items():
    actual = (tree / path).read_bytes()
    if actual != content:
        patch_mismatches.append({'path': path, 'expected_sha256': digest(content),
            'actual_sha256': digest(actual), 'expected_bytes': len(content), 'actual_bytes': len(actual),
            'diff': ''.join(difflib.unified_diff(content.decode().splitlines(True), actual.decode().splitlines(True), fromfile='expected', tofile='patch-output'))})
(QA / 'PATCH_MISMATCHES.json').write_text(json.dumps(patch_mismatches, indent=2) + '\n')
checks.append({'check': 'Distributed patch output', 'result': 'FAIL' if patch_mismatches else 'PASS',
    'detail': f'{len(composed)-len(patch_mismatches)}/101 match; details in PATCH_MISMATCHES.json'})
print(f'{checks[-1]["result"]}: Distributed patch output: {checks[-1]["detail"]}', flush=True)
# Continue unaffected confirmation checks; preserve the failing patch tree as evidence.
lint_command = ['python3', '-B', '-I', 'lints/run_all.py']
lint = subprocess.run(lint_command, cwd=tree, capture_output=True, text=True)
(QA / 'LINT_RAW.txt').write_text(f'Command: {lint_command!r}\nWorking directory: {tree}\nExit: {lint.returncode}\n{lint.stdout}{lint.stderr}')
check('Full pinned lint suite', lint.returncode == 0, '36 live documents; pinned lint files unchanged')

rows = list(csv.DictReader((AMEND / 'OWNERSHIP_PROPAGATION.tsv').open(), delimiter='\t'))
retained = [row for row in rows if row['disposition'].startswith('RETAIN')]
for row in retained:
    line = composed[row['path']].decode().splitlines()[int(row['line'])-1]
    assert line.startswith(row['text']), (row['path'], row['line'])
    assert row['match'].lower() in line.lower(), row
check('Retained ownership hit locations', len(rows) == 39 and len(retained) == 31, '39 dispositions; 31 retained locations verified; semantic review recorded separately')
sweep_pattern = (r"ENGINEER AGENT: WHAT IT PRODUCES|Engineer's full output list|\*\*Author:\*\* Engineer|Engineer Agent|\| *Engineer *\|? *$"
    r"|Define data schemas|Define API contracts|Define schemas|schema design|Engineer Focus|Engineer owns|Engineer produces|Engineer authors"
    r"|owned by the Engineer|Engineering owns|Engineer (defines|designs|writes|creates) [^.]*(schema|contract|API_SPEC|DB_SCHEMA|DATA_CONTRACT)")
sweep = re.compile(sweep_pattern, re.I)
hits = []
for path, content in composed.items():
    if path.startswith('_ARCHIVE/') or Path(path).suffix not in ('.md', '.svg'):
        continue
    for n, line in enumerate(content.decode().splitlines(), 1):
        if sweep.search(line):
            hits.append({'path': path, 'line': n, 'text': line})
assert {(h['path'], h['line']) for h in hits} == {(r['path'], int(r['line'])) for r in retained}
(QA / 'OWNERSHIP_SWEEP_REPLAY.json').write_text(json.dumps({'pattern': sweep_pattern, 'hits': hits}, indent=2) + '\n')
check('Ownership sweep replay', True, '31/31 live hits dispositioned; no additional hit')

workflow_plan = read_json(RUN / 'WORKFLOW_PUBLICATION_PLAN.json')
actors = sorted({actor for workflow in workflow_plan['workflows'] for actor, _ in workflow['steps']})
workflow_evidence = []
for workflow in workflow_plan['workflows']:
    svg = ElementTree.fromstring(composed[workflow['asset']])
    text_nodes = [''.join(node.itertext()) for node in svg.iter() if node.tag.split('}')[-1] == 'text']
    joined_text = ' '.join(' '.join(text_nodes).split()).replace('- ', '-')
    document = composed[workflow['document']].decode()
    positions = []
    for actor, step in workflow['steps']:
        assert actor in actors and actor in text_nodes and step in joined_text
        assert actor in document and step in document
        positions.append(joined_text.index(step))
    assert positions == sorted(positions)
    for banned in ['Director of QA', 'Codex', 'Sol', 'Claudy', 'INITSCRIPT', 'CLOUDDEPLOYMENT', 'QA Lead executes', 'QA Lead runs tests']:
        assert not any(banned in node for node in text_nodes), (workflow['id'], banned)
    workflow_evidence.append({'id': workflow['id'], 'step_count': len(positions), 'actors': sorted({a for a, _ in workflow['steps']})})
(QA / 'WORKFLOW_ACTOR_EVIDENCE.json').write_text(json.dumps({'source': 'WORKFLOW_PUBLICATION_PLAN.json', 'sha256': digest((RUN / 'WORKFLOW_PUBLICATION_PLAN.json').read_bytes()), 'permitted_actor_labels': actors, 'workflows': workflow_evidence}, indent=2) + '\n')
check('AC37 source-derived actors and steps', True, f'{actors}; 7/18/8/24 steps; forbidden labels absent')

protected = read_json(QA / 'PROTECTED_BEFORE.json')
assert all((ROOT / path).exists() and digest((ROOT / path).read_bytes()) == sha for path, sha in protected.items())
check('Protected files unchanged', True, f'{len(protected)} source/canonical/skill/lint/intake/run files')
current_git = git('rev-parse', 'HEAD', 'main', 'origin/main') + git('diff', '--cached', '--name-status')
check('Git refs and staging unchanged', current_git.decode() == (QA / 'GIT_BEFORE.txt').read_text(), 'HEAD/main/origin-main unchanged; nothing staged')
save()
print(f'Evidence saved in {QA}; disposable tree {tree}')
raise SystemExit(1 if any(c['result'] == 'FAIL' for c in checks) else 0)
