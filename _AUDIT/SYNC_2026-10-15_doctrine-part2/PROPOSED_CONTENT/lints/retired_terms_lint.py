"""LINT b — RETIRED-TERMS. Retired tool names must not appear in LIVE doctrine.
Exempt: Version History / Changelog / Versioning sections (honest history is preserved,
never laundered) and _ARCHIVE/ (out of scope entirely).
Exit 1 on any hit.
"""
import re
import sys
from lint_common import live_files, iter_lines, report

LINT = "RETIRED-TERMS"
RETIRED = [re.compile(r"stitch", re.I)]


def main():
    failures = 0
    for f in live_files():
        for lineno, line in iter_lines(f, skip_exempt_sections=True):
            for pat in RETIRED:
                m = pat.search(line)
                if m:
                    report(f, lineno, LINT, f"retired term {m.group(0)!r} in live doctrine: {line.strip()[:100]!r}")
                    failures += 1
    if failures:
        print(f"[{LINT}] FAIL — {failures} hit(s)")
        return 1
    print(f"[{LINT}] PASS — 0 hits across {len(live_files())} live docs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
