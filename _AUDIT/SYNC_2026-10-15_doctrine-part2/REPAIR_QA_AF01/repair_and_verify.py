"""QA-AF01 serialization-only repair; writes only this repair directory and /tmp.

Run from repository root with python3 -B -I. Original generators, patches,
indexes, payloads and specifications are inputs only. No Git mutation.
"""
import difflib
import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path

ROOT = Path.cwd()
RUN = ROOT / '_AUDIT/SYNC_2026-10-15_doctrine-part2'
OUT = RUN / 'REPAIR_QA_AF01'
BASE = '9c179392f79b70da099121fc357d3107ad3bb86e'
COMMANDS = []


def sha(data):
    return hashlib.sha256(data).hexdigest()


def load(path):
    return json.loads(path.read_text())


def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def command(argv, cwd=ROOT):
    result = subprocess.run(argv, cwd=cwd, capture_output=True,
                            env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
    COMMANDS.append(dict(command=argv, cwd=str(cwd), exit_code=result.returncode,
                         environment_override={'PYTHONDONTWRITEBYTECODE': '1'},
                         stdout=result.stdout.decode('utf-8'), stderr=result.stderr.decode('utf-8')))
    save('COMMANDS.json', COMMANDS)
    return result


def git_blob(path):
    result = command(['git', 'show', BASE + ':' + path])
    assert result.returncode == 0, path
    return result.stdout


def lf_lines(data):
    # Patch records are LF-delimited; preserve CR and all other content bytes.
    parts = data.split(b'\n')
    return [part + b'\n' for part in parts[:-1]] + ([parts[-1]] if parts[-1] else [])


def serialize(before, after, fromfile, tofile):
    """Emit standard unified diff, including EOF markers on +/-/context lines."""
    records = difflib.diff_bytes(difflib.unified_diff, lf_lines(before), lf_lines(after),
                                fromfile=fromfile.encode(), tofile=tofile.encode())
    return b''.join(line if line.endswith(b'\n') else
                    line + b'\n\\ No newline at end of file\n' for line in records)


def old_serialize(before, after, fromfile, tofile):
    return ''.join(difflib.unified_diff(before.decode().splitlines(True),
                                      after.decode().splitlines(True),
                                      fromfile=fromfile, tofile=tofile)).encode()


def write_tree(directory, files):
    for path, data in files.items():
        target = directory / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)


def replay_check(label, patch, before, expected, strip=0):
    with tempfile.TemporaryDirectory(prefix='cody-af01-' + label + '-') as temp:
        temp = Path(temp)
        git_tree, gnu_tree = temp / 'git-check', temp / 'gnu-replay'
        git_tree.mkdir(); gnu_tree.mkdir()
        write_tree(git_tree, before); write_tree(gnu_tree, before)
        git_check = command(['git', 'apply', '--check', '-p' + str(strip), str(patch)], git_tree)
        assert git_check.returncode == 0, (label, git_check.stderr)
        patch_result = command(['patch', '--batch', '--fuzz=0', '-p' + str(strip), '-i', str(patch)], gnu_tree)
        assert patch_result.returncode == 0, (label, patch_result.stderr)
        mismatches = [p for p, data in expected.items() if not (gnu_tree / p).is_file()
                      or (gnu_tree / p).read_bytes() != data]
        assert not mismatches, (label, mismatches)
        actual_paths = {str(p.relative_to(gnu_tree)) for p in gnu_tree.rglob('*') if p.is_file()}
        assert actual_paths == set(before) | set(expected), (label, actual_paths - set(before) - set(expected))
        return dict(label=label, git_apply_check=0, GNU_patch=0,
                    verified_outputs=len(expected), unplanned_files=0)


def main():
    protected_path = OUT / 'PROTECTED_BEFORE.json'
    if not protected_path.exists():
        listing = command(['git', 'ls-files', '-c', '-o', '--exclude-standard', '-z']).stdout
        paths = {Path(p.decode()) for p in listing.split(b'\0') if p}
        paths |= {p.relative_to(ROOT) for p in RUN.rglob('*') if p.is_file()}
        protected = {str(p): sha((ROOT / p).read_bytes()) for p in sorted(paths)
                     if (ROOT / p).is_file() and OUT not in (ROOT / p).parents
                     and str(p) not in ['RECOVERY.md', 'agent_docs/SESSIONS/session_2026-10-17.md']
                     and '__pycache__' not in p.parts}
        save('PROTECTED_BEFORE.json', protected)
        save('GIT_BEFORE.json', {name: command(args).stdout.decode() for name, args in {
            'refs': ['git', 'rev-parse', 'HEAD', 'main', 'origin/main'],
            'staging': ['git', 'diff', '--cached', '--name-status'],
            'worktrees': ['git', 'worktree', 'list', '--porcelain'],
            'status': ['git', 'status', '--porcelain']}.items()})

    base_paths = command(['git', 'ls-tree', '-r', '--name-only', BASE]).stdout.decode().splitlines()
    baseline = {p: git_blob(p) for p in base_paths
                if p.startswith(('01_', '02_', '03_', '04_', '05_', '_ARCHIVE/', 'lints/'))
                or p in ['MANIFEST.md', 'CHANGELOG.md']}
    amended = RUN / 'AMENDED_V1'
    edit_sets = {name: load(folder / 'SELECTED_EXACT_EDITS.json')
                 for name, folder in [('frozen', RUN), ('amended', amended)]}
    assert len(edit_sets['amended']) == 380 and edit_sets['amended'][:372] == edit_sets['frozen']
    variants = []
    for label, folder in [('frozen', RUN), ('amended', amended)]:
        index = load(folder / 'EXECUTION_PROPOSAL_INDEX.json')
        before, expected, records = {}, {}, []
        for row in index:
            p = row['path']; old = baseline.get(p, b'')
            target = folder / 'PROPOSED_CONTENT' / p
            if not target.is_file(): target = RUN / 'PROPOSED_CONTENT' / p
            data = target.read_bytes()
            assert sha(data) == row['proposed_sha256'] and len(data) == row['bytes'], p
            assert (sha(old) if old else None) == row['before_sha256'], p
            if row['before_sha256']: before[p] = old
            expected[p] = data
            records.append((old, data, p if row['before_sha256'] else '/dev/null', p))
        variants.append((label + '_execution', folder / 'EXECUTION_PROPOSAL.patch', records, before, expected, 0))

        stage = {}
        for edit in edit_sets[label]:
            p = edit['path']; current = stage.get(p, baseline[p].decode())
            assert current.count(edit['old']) == 1, (label, edit['sequence'])
            stage[p] = current.replace(edit['old'], edit['new'], 1)
        records, before, expected = [], {}, {}
        for row in load(folder / 'SELECTED_CONTENT_INDEX.json'):
            p = row['path']; data = stage[p].encode()
            assert sha(data) == row['proposed_sha256'], p
            before[p] = baseline[p]; expected[p] = data
            records.append((baseline[p], data, 'BASE/' + p, 'PROPOSED/' + p))
        variants.append((label + '_selected_content', folder / 'SELECTED_CONTENT_DIFF.patch', records, before, expected, 1))

    records, before, expected = [], {}, {}
    for row in load(RUN / 'POST_VERIFICATION_PROPOSAL_INDEX.json'):
        p = row['path']; old = (RUN / 'PROPOSED_CONTENT' / p).read_bytes()
        data = (RUN / 'CLOSEOUT_PROPOSED_CONTENT' / p).read_bytes()
        assert sha(old) == row['before_sha256'] and sha(data) == row['proposed_sha256']
        before[p] = old; expected[p] = data; records.append((old, data, p, p))
    variants.append(('conditional_closeout', RUN / 'POST_VERIFICATION_PROPOSAL.patch', records, before, expected, 0))

    audits = []
    for label, submitted, records, before, expected, strip in variants:
        old = b''.join(old_serialize(*record) for record in records)
        assert old == submitted.read_bytes(), ('legacy serializer identity', label)
        corrected = b''.join(serialize(*record) for record in records)
        needs_repair = corrected != old
        # Keep all original artifacts immutable; only the amended execution is active.
        if needs_repair:
            name = 'EXECUTION_PROPOSAL.corrected.patch' if label == 'amended_execution' else label + '.corrected.patch'
            destination = OUT / name; destination.write_bytes(corrected)
        else:
            destination = submitted
        result = replay_check(label, destination, before, expected, strip)
        audits.append(dict(artifact=str(submitted.relative_to(RUN)), label=label,
                           old_sha256=sha(old), corrected_sha256=sha(corrected),
                           old_bytes=len(old), corrected_bytes=len(corrected),
                           repair_required=needs_repair,
                           corrected_artifact=str(destination.relative_to(RUN)),
                           no_newline_markers=corrected.count(b'\\ No newline at end of file\n'),
                           patch_headers_strip=strip, verification=result,
                           status='active replacement proposed' if label == 'amended_execution'
                           else 'historical comparison only' if label.startswith('frozen')
                           else 'unchanged existing artifact' if not needs_repair else 'replacement proposed'))
    save('PATCH_ARTIFACT_AUDIT.json', audits)

    # Exercise the shared serializer for both sides of EOF and context-line cases.
    cases = [('add_unterminated', b'', b'new'), ('delete_unterminated', b'old', b''),
             ('both_unterminated', b'old', b'new'), ('add_final_lf', b'same', b'same\n'),
             ('remove_final_lf', b'same\n', b'same'),
             ('unterminated_context', b'old\ntail', b'new\ntail'),
             ('crlf', b'old\r\n', b'new\r\n')]
    fixture_results = []
    with tempfile.TemporaryDirectory(prefix='cody-af01-fixtures-') as temp:
        for label, old, new in cases:
            patch = Path(temp) / (label + '.patch')
            patch.write_bytes(serialize(old, new, 'fixture.txt', 'fixture.txt'))
            fixture_results.append(replay_check(label, patch, {'fixture.txt': old}, {'fixture.txt': new}))
    save('SERIALIZER_CASES.json', fixture_results)

    # Required final replay on full fresh baseline copies; no worktree/index mutations.
    execution = next(v for v in variants if v[0] == 'amended_execution')
    expected = execution[4]
    with tempfile.TemporaryDirectory(prefix='cody-af01-full-replay-') as temp:
        temp = Path(temp); gnu = temp / 'gnu'; check = temp / 'git-check'
        gnu.mkdir(); check.mkdir(); write_tree(gnu, baseline); write_tree(check, baseline)
        patch = OUT / 'EXECUTION_PROPOSAL.corrected.patch'
        result = command(['git', 'apply', '--check', '-p0', str(patch)], check)
        assert result.returncode == 0
        result = command(['patch', '--batch', '--fuzz=0', '-p0', '-i', str(patch)], gnu)
        assert result.returncode == 0
        full_hashes = []
        for p, data in expected.items():
            actual = (gnu / p).read_bytes(); assert actual == data, p
            full_hashes.append(dict(path=p, expected_sha256=sha(data), actual_sha256=sha(actual),
                                    bytes=len(actual), equal=True))
        save('REPLAY_101_HASHES.json', full_hashes)
        archive_results = []
        for archive, original in [
            ('_ARCHIVE/FRONTEND_BUILD_PHASE_PLAYBOOK_v1_2_2.md', '03_BUILD_METHODOLOGY/FRONTEND_BUILD_PHASE_PLAYBOOK.md'),
            ('_ARCHIVE/FRONTEND_FIRST_PLAYBOOK_v1_1_3.md', '03_BUILD_METHODOLOGY/FRONTEND_FIRST_PLAYBOOK.md')]:
            actual = (gnu / archive).read_bytes(); original_bytes = baseline[original]
            original_id = command(['git', 'rev-parse', BASE + ':' + original]).stdout.decode().strip()
            actual_id = command(['git', 'hash-object', '--no-filters', str(gnu / archive)]).stdout.decode().strip()
            assert actual == original_bytes and actual_id == original_id and not actual.endswith(b'\n')
            archive_results.append(dict(archive=archive, baseline_source=original,
                                       bytes=len(actual), baseline_sha256=sha(original_bytes), replay_sha256=sha(actual),
                                       baseline_blob=original_id, replay_blob=actual_id,
                                       baseline_final_newline=False, replay_final_newline=False, equal=True))
        save('ARCHIVE_FIDELITY.json', archive_results)
        lint = command(['python3', '-B', '-I', 'lints/run_all.py'], gnu)
        assert lint.returncode == 0, lint.stdout
        save('LINT_RESULT.json', dict(command=COMMANDS[-1], source='exact lints blobs from pinned BASE'))
        changed = {p for p in baseline if (gnu / p).read_bytes() != baseline[p]}
        added = {str(p.relative_to(gnu)) for p in gnu.rglob('*') if p.is_file()} - set(baseline)
        assert changed | added == set(expected), (changed | added) ^ set(expected)
        scope = dict(modified=sorted(changed), added=sorted(added), intended_paths=len(expected),
                     unexpected_paths=[], missing_paths=[])
        save('REPLAY_SCOPE.json', scope)

    protected = load(protected_path)
    changed_sources = [p for p, expected_hash in protected.items()
                       if not (ROOT / p).is_file() or sha((ROOT / p).read_bytes()) != expected_hash]
    assert not changed_sources, changed_sources
    git_before = load(OUT / 'GIT_BEFORE.json')
    for key, args in {'refs': ['git', 'rev-parse', 'HEAD', 'main', 'origin/main'],
                      'staging': ['git', 'diff', '--cached', '--name-status'],
                      'worktrees': ['git', 'worktree', 'list', '--porcelain']}.items():
        assert command(args).stdout.decode() == git_before[key], key
    save('VERIFICATION.json', dict(status='ENGINEER CHECKS PASS; independent QA retest pending',
         ordered_edits=380, indexed_output_paths=101, replayed_exact_outputs=101,
         archive_fidelity='2/2 exact bytes, Git blobs and no-final-newline state',
         lint_exit=0, active_and_historical_patches_audited=len(audits),
         serializer_cases=len(cases), protected_files_unchanged=len(protected),
         changed_protected_files=[], canonical_implementation=False, git_mutations=False,
         gate2_amendment='PENDING', gate3='PENDING', phase3='NOT RELEASED'))
    print('PASS: 101/101 replay hashes; 2/2 exact archives/blobs/EOF; full lints; '
          + str(len(audits)) + ' patch artifacts; ' + str(len(protected)) + ' protected files unchanged.')


if __name__ == '__main__':
    main()
