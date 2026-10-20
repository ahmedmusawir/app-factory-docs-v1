# PARENT_ENTRY_ROUTING — text for the parent module's entry files

> TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC. Template `QAM/PARENT_ENTRY_ROUTING.md` v0.3-draft (2026-10-14), from `QAM_PLAYBOOK_v1_0.md` §6 ("At the parent module, both entry conventions must route Engineering to the implementation assignment and QA to QAM"). **Owner: Architect.** This file is not read by the QA Executor; it is the snippet the Architect pastes into the parent module's `CLAUDE.md` and `AGENTS.md` (and `GEMINI.md` where the module ships one) so that both entry conventions route the same way. Delete this file from the instantiated `QAM/` once pasted, or keep it as the record of what was pasted.

## Snippet (same wording in every parent entry file)

```markdown
## Role routing

- **Engineering** (implementing `<<MODULE_ID>>`): your assignment is `<<MODULE_DIR>>/<<IMPLEMENTATION_ENTRY, e.g. CLAUDE.md §Assignment or README.md>>`. The acceptance contract is `<<MODULE_DIR>>/<<ACCEPTANCE_SPEC>>` (frozen; amendments only through `<<RULINGS_LANE>>`). Completing `QAM/QAM_MANIFEST.md` and `QAM/HANDOFFS/ENGINEERING_HANDOFF.md` is part of this assignment.
- **QA** (independent verification of `<<MODULE_ID>>`): go to `<<MODULE_DIR>>/QAM/` and read `QAM_ENTRY.md`. Both `QAM/CLAUDE.md` and `QAM/AGENTS.md` assign the QA Executor seat and point there. A folder path authorizes Q1 only.
- Wrong seat or wrong folder: say so and name the correct entry above; do not switch branches, reset, repair or restart anything.
```

## Where the FFM convention already has a redirect

Where the parent module follows FFM_PLAYBOOK §8.3 (`AGENTS.md` → redirects to `CLAUDE.md`), the redirect form is acceptable as long as the redirected-to body contains the routing above: the playbook requires that both entry conventions **route** correctly, and that `QAM/`'s own two files carry **identical** routing text. The exact Hub wording for FFM_PLAYBOOK §8.3 is proposed in the UPDATE MAP (ENGINEER-PROPOSED at Gate 2), not here.

## Architect validation checklist (§6)

- [ ] Parent `CLAUDE.md` contains the snippet (or redirects to a body that contains it).
- [ ] Parent `AGENTS.md` contains the snippet (or redirects to that body).
- [ ] `QAM/CLAUDE.md` and `QAM/AGENTS.md` routing text byte-identical (diff the region between the markers).
- [ ] Discovery validated in each supported runtime: `<<runtime: loaded automatically? Y/N; fallback instruction recorded>>`.
- [ ] No long custom kickoff prompt exists anywhere that contains operating rules missing from `QAM_ENTRY.md`.

*TEMPLATE SET v0.3 — QA LEAD ACCEPTED WITH EXACT AMENDMENTS (Fable, 2026-10-14); AMENDMENTS ARCHITECT-VERIFIED; INSTALLATION REQUIRES THE APPROVED DOCSET SYNC.*
