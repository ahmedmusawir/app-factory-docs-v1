"""LINT c — VERSIONED-REFS (the drift-killer). Live docs must reference other docs by
CANONICAL NAME ONLY. Two patterns:
(i)  any versioned .md filename reference:  SOMETHING_v1_2.md / SOMETHING_v1.2.md
     (catches real refs AND phantoms — versions never exist in live filenames)
(ii) '<CANONICAL_NAME> vX.Y' prose refs — MANIFEST-name-driven, so project identifiers
     like cyber_pharma_v1_phase1_ffm can never false-positive.
Exempt: Version History / Changelog / Versioning sections; _ARCHIVE/ by scope.
Exit 1 on any hit.
"""
import re
import sys
from lint_common import ROOT, live_files, iter_lines, report

LINT = "VERSIONED-REFS"
FILENAME_REF = re.compile(r"[A-Za-z0-9_\-]+_v\d+(?:[._]\d+)*\.md")
NAME_ROW = re.compile(r"^\|\s*([A-Z][A-Z0-9_]{3,})\s*\|")


def canonical_names():
    manifest = ROOT / "MANIFEST.md"
    names = set()
    if manifest.exists():
        for line in manifest.read_text(encoding="utf-8", errors="replace").splitlines():
            m = NAME_ROW.match(line)
            if m:
                names.add(m.group(1))
    return sorted(names)


def main():
    names = canonical_names()
    if not names:
        print(f"[{LINT}] ERROR — no canonical names parsed from MANIFEST.md")
        return 1
    prose_pats = [(n, re.compile(rf"{n}\s+v\d+\.\d+")) for n in names]
    failures = 0
    for f in live_files():
        for lineno, line in iter_lines(f, skip_exempt_sections=True):
            for m in FILENAME_REF.finditer(line):
                report(f, lineno, LINT, f"versioned filename reference {m.group(0)!r}")
                failures += 1
            for name, pat in prose_pats:
                m = pat.search(line)
                if m:
                    report(f, lineno, LINT, f"versioned prose reference {m.group(0)!r} — canonical names only")
                    failures += 1
    if failures:
        print(f"[{LINT}] FAIL — {failures} hit(s)")
        return 1
    print(f"[{LINT}] PASS — 0 hits across {len(live_files())} live docs ({len(names)} canonical names loaded)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
