# Response 2026-10-15 20:00 +0600 — AGENTS.md search result; reporting convention adopted

**Seat:** Claudy (Engineer) · **Trigger:** Tony's instruction (2026-10-15, ~19:5x): "read your Agents.md file to learn how to report your response; at every on-screen report present the location of your latest response file or any other .zip deliverables, and a note on Next Steps."

---

## 1. What you asked

1. Read my `AGENTS.md` to learn how to report.
2. New standing format: every on-screen report ends with (a) the location of my latest response file, (b) any `.zip`-type deliverables, (c) a Next Steps note — because you are running many projects in parallel.

## 2. Finding: there is no AGENTS.md governing this session

Searched: repo root, `agent_docs/`, repo-wide glob (incl. hidden), parent `~/Documents/`, `~/.config/opencode/`. **No governing `AGENTS.md` exists anywhere this session reads.**

The only `AGENTS.md` files in the repo are four inside intake packages, none of which instruct the Engineer seat:

| Path | What it is |
|---|---|
| `factory-intake/INTAKE_ADDENDUM_001_v0_1/TEMPLATES/QAM/AGENTS.md` | QAM dual-entry routing template (byte-identical routing to the kit's `CLAUDE.md`) |
| `factory-intake/INTAKE_ADDENDUM_001_v0_2/TEMPLATES/QAM/AGENTS.md` | same, v0.2-draft (preserved) |
| `factory-intake/INTAKE_ADDENDUM_001_v0_3/TEMPLATES/QAM/AGENTS.md` | same, v0.3-draft — part of the Architect-verified set (ZIP `25a6ffe5…553d`); read-only |
| `factory-intake/EXTRACTED/SRC-R02/RRM-004-CYBER-PHARMA/QA/AGENTS.md` | harvested source evidence; read-only |

## 3. What actually governs my reporting (in force since before the harness change)

`CLAUDE.md` — **RESPONSE LOGGING PROTOCOL (v1.0)**:

- Every substantive artifact (plans, reports, verification results, rulings, handoffs) is written to `agent_docs/RESPONSES/response_<YYYY-MM-DD>_<HHMMSS>_<slug>.md` **BEFORE** printing to screen.
- The file mirrors the on-screen output exactly. Conversational replies and short confirmations are exempt.
- Session state lives in `session_2026-10-15.md` + `RECOVERY.md`.

This response file is the first one written under the combined rule (protocol + your footer format). Note: the 19:36 bootstrap read-back was logged in the session file but carried no response file (borderline-conversational; logged read-only verification only). Going forward, every report gets one — when you say "log it", I write the missing file immediately, per the protocol's recovery cue.

## 4. Adopted, effective now: the report footer

Every on-screen report ends with:

```
📄 Response file: <path to the file backing this report>
📦 Deliverables: <ZIPs/artifacts + SHA-256, or "none this report">
➡️  Next steps: <who does what next>
```

## 5. One decision needed from you: root AGENTS.md for OpenCode

OpenCode reads a root `AGENTS.md` as its project-instruction file — the same role `CLAUDE.md` plays for Claude Code. None exists, so the OpenCode harness is **not** auto-loading our conventions; I follow them because I read `CLAUDE.md` and the session files at bootstrap.

Options (clarifying question presented on screen alongside this report):

- **(a) Draft one for your approval** (recommended): a minimal root `AGENTS.md` pointing to `CLAUDE.md` as the governing protocol + restating the reporting/footer rules. I draft → you approve → I write. No other content invented.
- **(b) Skip the file:** I keep applying `CLAUDE.md` manually (it is working — this bootstrap proves it).
- **(c) It lives elsewhere:** you point me to the `AGENTS.md` you meant, and I read it.

Not writing anything to the repo root without your approval (root is shared ground; Plan Mode).

## 6. State (unchanged since the 19:36 bootstrap)

Branch `factory-docs-review-astra-w-chunks`, HEAD `626da8d`, nothing staged; all four sync DRAFTS preserved; no `UPDATE_MAP.md`, no map parts, no `_INBOX/`. The 31-vs-28 porcelain delta from the handoff remains flagged for your confirmation (composition matches the handoff exactly).

## 7. Next steps

1. You: pick an AGENTS.md option (a)/(b)/(c) — question on screen.
2. You: confirm the 31-vs-28 porcelain delta is just the checkpoint's own bookkeeping (closes the flag).
3. On your instruction: resume the approved 15:01 sync plan at UPDATE_MAP drafting step 1 (handoff §6) — intake integrity verification first, then Gates 1–2, then STOP for review. Pending before/at approval: D.2, C.2, DEC-05, DEC-17 rulings; P1 (Jarvis, non-blocking); P2 approval statement; P5 branch hygiene.