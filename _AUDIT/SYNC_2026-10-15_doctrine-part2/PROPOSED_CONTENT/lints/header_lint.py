"""LINT d — HEADER-PRESENCE. Every live doc carries the standard header block:
- an H1 title within the first 3 lines
- a '> **Version:** X · **Date:** ... · **Status:** ...' line within the first 10 lines
No exemptions inside live scope. Exit 1 on any miss.
"""
import re
import sys
from lint_common import live_files, read_lines, report

LINT = "HEADER-PRESENCE"
H1_RE = re.compile(r"^#\s+\S")
VDS_RE = re.compile(r"\*\*Version:\*\*.*\*\*Date:\*\*.*\*\*Status:\*\*")


def main():
    failures = 0
    for f in live_files():
        lines = read_lines(f)
        if not any(H1_RE.match(l) for l in lines[:3]):
            report(f, 1, LINT, "missing H1 title in the first 3 lines")
            failures += 1
        if not any(VDS_RE.search(l) for l in lines[:10]):
            report(f, 1, LINT, "missing standard 'Version / Date / Status' header line in the first 10 lines")
            failures += 1
    if failures:
        print(f"[{LINT}] FAIL — {failures} miss(es)")
        return 1
    print(f"[{LINT}] PASS — all {len(live_files())} live docs carry the standard header")
    return 0


if __name__ == "__main__":
    sys.exit(main())
