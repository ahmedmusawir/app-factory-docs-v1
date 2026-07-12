# Doctrine Lints — the Watchdogs

> **Version:** 1.0 · **Date:** 2026-07-12 · **Status:** Active
> **Tier:** none — repository infrastructure · **Pairs with:** MANIFEST, CHANGELOG, _ARCHIVE/README

Four checks, born from the 2026-07 Grand Audit campaign. CI runs them on every push + PR to main (`.github/workflows/doctrine-lint.yml`); any failure blocks with `FILE:LINE: [LINT-ID] message`.

## Run locally

```bash
python lints/run_all.py        # all four
python lints/encoding_lint.py  # any single lint
```

## The four lints

| ID | Catches | Why it exists |
|---|---|---|
| `ENCODING` | (i) mojibake signatures (literal `â`/`Ã` double-decode residue), (ii) invisible C1 controls U+0080–U+009F, (iii) quote-residue `"”` + U+FFFD | F-012/F-034: three corruption classes shipped repeatedly despite claimed fixes; the `â` grep alone misses classes (ii) and (iii) |
| `RETIRED-TERMS` | `stitch` (case-insensitive) in live doctrine | F-002: the retired tool survived in 6 docs for a month after its retirement |
| `VERSIONED-REFS` | (i) any `*_vN(.N)*.md` filename reference; (ii) `CANONICAL_NAME vX.Y` prose refs (MANIFEST-name-driven) | F-011/F-032: versioned cross-refs guarantee drift — including two citations of a version that never existed. THE drift-killer |
| `HEADER-PRESENCE` | missing H1 (first 3 lines) or missing `**Version:** · **Date:** · **Status:**` line (first 10) | F-018/F-033: unversioned docs and lying headers — MANIFEST regenerates from these lines |

## Scope + exemption rules

- **Live scope:** `01_CONSTITUTION/ … 05_DESIGN_SYSTEM/*.md` + `MANIFEST.md` + `CHANGELOG.md`.
- **Always exempt (by scope omission):** `_ARCHIVE/` (versioned snapshots belong there), `_AUDIT/`, `_OTHERS/`, `agent_docs/`, `lints/`, root session/RECOVERY/CLAUDE/README/MCP_RESEARCH files.
- **Section exemption** (`RETIRED-TERMS` + `VERSIONED-REFS` only): content under any heading containing *Version History*, *Changelog*, or *Versioning* — honest history is preserved, never laundered. Exemption ends at the next heading. `CHANGELOG.md` itself is exempt at file level (it is a change ledger by nature); `ENCODING` + `HEADER-PRESENCE` still apply to it.
- **Fence exemption** (`ENCODING` only): fenced code blocks are skipped (code may legitimately contain unusual bytes). Versioned refs inside fences still count — drift in a template is still drift.
- **False-positive guard** (`VERSIONED-REFS`): prose-form matching only fires on the canonical names parsed live from `MANIFEST.md`, so project identifiers (e.g. `cyber_pharma_v1_phase1_ffm`) can never trip it.

## When a lint fails

A failure is a **finding**, not an inconvenience: fix the underlying byte/reference problem (or, for genuinely historical content, move it under a Version History heading). Never add ad-hoc exemptions to make a failure disappear — that blinds the watchdog the campaign paid for.

🥄 *Part of Stark Industries — App Factory doctrine.*
