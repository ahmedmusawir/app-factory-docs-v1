"""Shared plumbing for the doctrine lints.

LIVE SCOPE: the five tier folders (01_* .. 05_*) *.md + MANIFEST.md + CHANGELOG.md.
ALWAYS EXEMPT (by scope omission): _ARCHIVE/, _AUDIT/, _OTHERS/, agent_docs/, lints/,
and root session/RECOVERY/CLAUDE/README/MCP_RESEARCH files.
"""
import re
import sys
from pathlib import Path

# Windows consoles default to cp1252 — doctrine is UTF-8; never crash on report output.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent

# Files that are ALL honest history by nature — exempt from the section-based lints
# (retired-terms, versioned-refs) at file level. The encoding + header lints still apply.
HISTORY_FILES = {"CHANGELOG.md"}

TIER_DIRS = [
    "01_CONSTITUTION",
    "02_PIPELINE_AGENTS",
    "03_BUILD_METHODOLOGY",
    "04_REFERENCE_MANUALS",
    "05_DESIGN_SYSTEM",
]

ROOT_LIVE = ["MANIFEST.md", "CHANGELOG.md"]

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)")
# Sections whose CONTENT is honest history — exempt from retired-terms + versioned-refs.
EXEMPT_SECTION_RE = re.compile(r"version\s+history|changelog|versioning", re.I)
FENCE_RE = re.compile(r"^\s*```")


def live_files():
    files = []
    for d in TIER_DIRS:
        p = ROOT / d
        if p.is_dir():
            files.extend(sorted(p.glob("*.md")))
    for name in ROOT_LIVE:
        p = ROOT / name
        if p.exists():
            files.append(p)
    return files


def read_lines(path):
    # errors='replace' → undecodable bytes become U+FFFD, which the encoding lint flags.
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def iter_lines(path, skip_fences=False, skip_exempt_sections=False):
    """Yield (lineno, line) honoring the requested exemptions."""
    if skip_exempt_sections and path.name in HISTORY_FILES:
        return  # the whole file is a change ledger — honest history, exempt
    in_fence = False
    in_exempt = False
    for i, line in enumerate(read_lines(path), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        m = HEADING_RE.match(line)
        if m and not in_fence:
            in_exempt = bool(EXEMPT_SECTION_RE.search(m.group(2)))
        if skip_fences and in_fence:
            continue
        if skip_exempt_sections and in_exempt:
            continue
        yield i, line


def rel(path):
    return path.relative_to(ROOT).as_posix()


def report(path, lineno, lint_id, msg):
    print(f"{rel(path)}:{lineno}: [{lint_id}] {msg}")
