"""LINT a — ENCODING. The three corruption classes proven by the 2026-07 campaign:
(i)  mojibake signatures: literal U+00E2 'â' / U+00C3 'Ã' (UTF-8 double-decode residue)
(ii) C1 control chars U+0080–U+009F (the invisible U+0090 class)
(iii) quote-residue / broken-dash ("‚Äù class → '"' + U+201D) and U+FFFD replacement chars
Fenced code blocks are exempt. Exit 1 on any hit.
"""
import sys
from lint_common import live_files, iter_lines, report

LINT = "ENCODING"


def check_line(path, lineno, line):
    hits = 0
    for col, ch in enumerate(line, start=1):
        cp = ord(ch)
        if cp in (0x00E2, 0x00C3):
            report(path, lineno, LINT, f"mojibake signature {ch!r} (U+{cp:04X}) at col {col}")
            hits += 1
        elif 0x80 <= cp <= 0x9F:
            report(path, lineno, LINT, f"C1 control char U+{cp:04X} at col {col} (invisible corruption)")
            hits += 1
        elif cp == 0xFFFD:
            report(path, lineno, LINT, f"U+FFFD replacement char at col {col} (undecodable byte)")
            hits += 1
    if '"”' in line:
        report(path, lineno, LINT, "quote-residue broken-dash sequence '\"”' (F-012 class)")
        hits += 1
    return hits


def main():
    failures = 0
    for f in live_files():
        for lineno, line in iter_lines(f, skip_fences=True):
            failures += check_line(f, lineno, line)
    if failures:
        print(f"[{LINT}] FAIL — {failures} hit(s)")
        return 1
    print(f"[{LINT}] PASS — 0 hits across {len(live_files())} live docs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
