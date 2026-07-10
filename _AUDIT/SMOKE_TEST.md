# SMOKE TEST — GitHub MCP Write Path

> **Version:** 1.0 · **Date:** 2026-07-10 (ordered 2026-07-09) · **Status:** DISPOSABLE — delete after verification
> **Tier:** none — test artifact, not doctrine · **Pairs with:** nothing

## What This Is

A disposable smoke test proving the GitHub MCP write path end-to-end:

**branch → commit → PR → operator merge**

- Created by Claude Code via the official GitHub MCP server (`create_branch` → `create_or_update_file` → `create_pull_request`).
- `main` was never written to directly; `merge_pull_request` was never called — merging is the operator's, in the GitHub UI.
- **To be deleted (file AND branch) after verification.**

🥄 *Not part of the App Factory doctrine. If you find this file on main after 2026-07, someone forgot to clean up.*
