# RRM-004-CYBER-PHARMA — Director Actions

All YOU. Numbered, one command per block. Agents prepare; you type the git.

## DA-1 — Cut the engineering branch from post-RRM-003 main

Step 1:
```
git checkout main
```
Step 2:
```
git pull
```
Step 3:
```
git log --oneline -1
```
Must show the RRM-003 merge (`649c36d …`). Then:

Step 4:
```
git checkout -b phase-3-rrm004
```
Step 5:
```
git push -u origin phase-3-rrm004
```

## DA-2 — Place and commit the pack

Unzip so the folder lands at `agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/`. Check nothing else moved:

Step 1:
```
git status --short
```
Only `agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/` lines. Then:

Step 2:
```
git add agent_docs/ACTIONS/RRM-004-CYBER-PHARMA
```
Step 3:
```
git commit -m "30sep2026 - RRM-004 pack authored (dependencies; QAM pilot)"
```
Step 4:
```
git push
```

## DA-3 — P0 bookkeeping (docs-only)

Paste P0 from `CLAUDY_PROMPTS.md` to the Engineer. Run his staging/commit block as returned, then:

```
git push
```

## DA-4 — Clean tree, then P1

```
git status --porcelain
```
Must print nothing. Then paste P1 from `CLAUDY_PROMPTS.md` to the Engineer.

## DC-1 — After P1

Send the plan to the Architect. Rule the four decisions (the Architect's memo lists them with a recommendation each): DD-1 transitive sweep · DD-2 Cloudinary · DD-3 QA target · DD-4 authorship split. The Architect returns the P1b rows. Paste P1b to the Engineer, run his staging/commit block, push, confirm clean, then paste P2.

## DC-2 — After P2 (one commit)

Run the Engineer's single staging block exactly as returned, then:
```
git status --short
```
`node_modules` must not appear. Then his commit line, then:
```
git push
```
Then:
```
git status --porcelain
```
Then:
```
git log --oneline -1
```
Paste that line to the Architect — it is the candidate SHA.

## DC-3 — QA branch and QA Lead entry

Step 1:
```
git checkout -b qa/phase-3-rrm004
```
Step 2:
```
git push -u origin qa/phase-3-rrm004
```
Then hand the QA Lead this letter:

> QA LEAD — RRM-004-CYBER-PHARMA is on `qa/phase-3-rrm004`; candidate `<sha from DC-2>`, baseline the RRM-003 merge `649c36d`. This is the QAM pilot. The Engineer's factual half is in `agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/QA/QAM_MANIFEST.md` and `QA_HANDOFF.md`; the contract is `ACCEPTANCE_SPEC.md` with `RULINGS_ADDENDUM.md` (targets A-01/A-02, DD-1…DD-4). Before the run: (1) author `QA/QA_TEST_PLAN.md` — yours alone, header with your position and date; (2) ratify or amend `QA/AGENTS.md`, `QA/QAM_PILOT_CHARTER.md`, `QA/QA_ENVIRONMENT_PREFLIGHT.md` (fill the "Ratified by" line); (3) tell me the browser engine and the two role accounts you need verified on the DD-3 target — I confirm they exist before you start, not during. Return the three files and I commit them here. Then I start the QA Executor with the one line in `QA/README.md` and step back until DC-5. Gate Q on AC-100…600; pilot verdict on AC-700 in `QA/QAM_PILOT_RESULTS.md`, separately.

When the QA Lead returns the files:

Step 3:
```
git add agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/QA
```
Step 4:
```
git commit -m "<date> - RRM-004 QA entry: test plan, QAM law ratified"
```
Step 5:
```
git push
```

## DC-4 — The one command

Step 1:
```
git status --porcelain
```
Must print nothing. Step 2: note the time —
```
date -Is
```
Step 3: give the QA Executor exactly this line and nothing else:

> QA EXECUTOR — RRM-004-CYBER-PHARMA QAM. Read agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/QA/AGENTS.md and run the module. Stop only on an enumerated Q-stop. Return to the QA Lead.

Write the `date -Is` into `QA/QAM_PILOT_RESULTS.md` §1 later (or tell the Executor to). Then step back.

## DC-5 — During QA

When the Executor says the browser is open on the login page, you type the DD-3 target's ADMIN credentials, then later MEMBER — into the browser. Not into a file, not into chat. Aim for one sign-in per role. No spot-check unless asked; then at most one per role.

## DC-6 — If QA raises a scope or contract question

Rule it; the Architect writes the row; the Engineer applies it on the QA branch; you commit.

## After the Executor returns

The QA Lead certifies (Gate Q) and grades the pilot (AC-700). Commit the QA lane:

Step 1:
```
git add agent_docs/ACTIONS/RRM-004-CYBER-PHARMA/QA
```
Step 2:
```
git commit -m "<date> - RRM-004 QA: execution, matrix, certification, pilot results"
```
Step 3:
```
git push
```
Then send the certification and `QAM_PILOT_RESULTS.md` to the Architect for P5.

## DC-7 — After Gate Q + cleanup + Architect closeout + Engineer closeout

Step 1:
```
git checkout main
```
Step 2:
```
git pull
```
Step 3:
```
git merge --no-ff qa/phase-3-rrm004 -m "<date> - merge qa/phase-3-rrm004 - RRM-004 CLOSED (Gate Q PASS @ <candidate>) - RRM campaign complete"
```
Step 4:
```
git push
```
Step 5:
```
git log --oneline -1
```
Paste that line to the Architect. Record candidate / QA HEAD / closeout / merge SHAs separately in the scoreboard. Read `QA/QAM_PILOT_RESULTS.md` §2–§4 and fill §5: adopt, amend or drop the QAM shape for BIM-004.

## Still owed from RRM-001

Supabase "Allow new users to sign up" OFF on the dev project; curl verification per RRM-001 `DIRECTOR_ACTIONS.md` DA-2; evidence file `agent_docs/ACTIONS/RRM-001-CYBER-PHARMA/evidence/DA-2_SUPABASE_SIGNUP_DISABLED.md`. Authoring-time status: NOT YET. Nothing in RRM-004 waits on it, but the campaign closeout will say PRESENT or NOT YET in writing.
