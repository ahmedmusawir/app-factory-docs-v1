# _ARCHIVE — Superseded Doctrine Snapshots

> **Version:** 1.0 · **Date:** 2026-07-12 · **Status:** Active
> **Tier:** none — repository infrastructure · **Pairs with:** MANIFEST, CHANGELOG

## The Rule (DOCTRINE_HUB_DESIGN §2.3)

- **Live docs carry CANONICAL names — no version suffix** (e.g. `AUTH_MANUAL.md`) — and live in the tier folders (`01_CONSTITUTION/` … `05_DESIGN_SYSTEM/`). Version + date live INSIDE each doc's header block and in `MANIFEST.md`, never in a live filename.
- **This folder holds VERSIONED SNAPSHOTS of superseded docs** (e.g. `AUTH_MANUAL_v1_2.md`) — the version suffix is stamped **from the doc's own header block at bump time**, so an archived filename can never lie about its content.

## On Every Doc Bump

1. Copy the outgoing live file into `_ARCHIVE/` with its version suffix (from its header).
2. Update the live file + its header (new version, date, Version History row).
3. Update `MANIFEST.md` and `CHANGELOG.md`.

## What This Archive Is

A **visible-history record**. Nothing here is laundered, renumbered, or rewritten; superseded versions are preserved, not deleted. Versioned filenames are allowed ONLY in this folder — anywhere else they are lint failures.

🥄 *Part of Stark Industries — App Factory doctrine.*
