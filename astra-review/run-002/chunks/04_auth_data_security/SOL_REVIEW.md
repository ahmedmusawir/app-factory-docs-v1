# SOL REVIEW — ASTRA CHUNK 04
# AUTH / DATA / SECURITY
# ASTRA FACTORY DOCTRINE REVIEW — RUN 002

## 1. REVIEW STATUS

COMPLETE

Reviewer:
Sol

Reviewed artifact:

astra-review/run-002/chunks/04_auth_data_security/ASTRA_REVIEW.md

Scope of this review:

This is a review of Astra's Chunk 04 examination.

It is NOT:

- a new review of the Factory corpus,
- an implementation review of a live application,
- a final disposition,
- a doctrine repair,
- or a Factory-wide synthesis.

Astra's findings remain claims until Factory disposition.

Fable's independent whole-corpus review is intentionally not consulted here.

---

## 2. OVERALL ASSESSMENT OF ASTRA'S REVIEW

Astra's Chunk 04 review is strong.

The report is bounded, evidence-oriented, explicit about uncertainty, and careful
to distinguish unsafe doctrine from claims about deployed application behavior.

The review identified:

- 4 BLOCKER defects
- 7 HIGH defects
- 6 MEDIUM defects
- 3 suggestions

The most important result is not the raw finding count.

The deeper pattern is that newer hard rules often coexist with older executable
recipes that appear to encode incompatible authority, security, or state
management behavior.

That creates a particularly dangerous doctrine failure mode:

A reader may understand the newer governing principle while an Engineer or AI
agent can still copy an older executable example that violates it.

This is highly relevant to the Factory's future DocSet synchronization work.

Astra also handled uncertainty well.

The report repeatedly distinguishes:

- doctrine defects,
- conditional consequences,
- implementation assumptions,
- and UNKNOWN live/runtime state.

That discipline should be preserved.

---

## 3. REVIEW OF BLOCKER FINDINGS

### C04-D03 — Public signup forwards caller-controlled role transport into the authority-creation path

ASTRA:
BLOCKER

SOL PRELIMINARY ASSESSMENT:
ACCEPT — BLOCKER

Reasoning:

Astra identifies a direct contradiction inside the written doctrine.

The reviewed material says creation-time role metadata is acceptable only
through a protected administrative path, while the public signup example
forwards caller-supplied user metadata.

The supporting Factory material cited by Astra says public signup should create
a member and superadmin creation should remain separately controlled.

If the written trigger behavior and public endpoint are followed together as
documented, the trust distinction required by the doctrine is not enforced.

This is exactly the type of security failure reusable Factory doctrine must not
teach.

Important limitation:

This does NOT prove a currently deployed application is exploitable.

Astra explicitly records the installed trigger/hardening state as UNKNOWN.

SOL POSITION:

The doctrine defect is valid and severe enough to remain BLOCKER pending final
Factory disposition.

---

### C04-D01 — Privileged examples still authorize from metadata and recreate competing role stores

ASTRA:
BLOCKER

SOL PRELIMINARY ASSESSMENT:
ACCEPT — BLOCKER

Reasoning:

Astra identifies incompatible authority models inside active doctrine.

The newer doctrine establishes the role table as the authorization authority and
rejects metadata/profile mirrors as privilege truth.

Older executable recipes nevertheless continue to:

- read privilege from user metadata,
- permit privileged role creation through application flows,
- and create additional role-bearing representations.

This is not merely duplicate documentation.

It creates multiple competing answers to:

"Where does authorization truth live?"

That can cause privilege drift and gives an Engineer or AI agent unsafe
copy/paste guidance.

SOL POSITION:

Valid BLOCKER.

The eventual repair should preserve the single-authority model rather than patch
individual snippets independently.

---

### C04-D02 — Layout admission is presented as authorization for privileged server actions

ASTRA:
BLOCKER

SOL PRELIMINARY ASSESSMENT:
ACCEPT DEFECT — FINAL SEVERITY REQUIRES DISPOSITION

Reasoning:

Astra's underlying security point is sound:

authorization to render or enter a protected page does not automatically prove
authorization of a separately invocable privileged mutation.

A privileged operation should defend its own boundary.

However, Astra reviewed doctrine, not the actual application implementation.

The report itself acknowledges that live application action implementations were
not examined.

SOL POSITION:

Accept the defect.

Do NOT automatically accept BLOCKER severity until Factory disposition decides
whether:

- the doctrine itself warrants BLOCKER classification, or
- the issue should be HIGH unless real implementations follow the unsafe
  pattern.

This is a severity question, not a rejection of the finding.

---

### C04-D06 — Soft-delete policy does not compose as a universal exclusion

ASTRA:
BLOCKER

SOL PRELIMINARY ASSESSMENT:
ACCEPT DEFECT — HIGH BY DEFAULT; BLOCKER WHEN APPLIED TO PRIVATE DATA

Reasoning:

Astra identifies a subtle but important RLS composition problem.

The documented soft-delete predicate is presented like a general exclusion.

When ordinary permissive access policies are combined, however, independently
true policies may expand access instead of producing the intended
owner-AND-active condition.

Astra also notes that the isolated soft-delete recipe does not independently
enable RLS.

The defect is real.

The severity depends on where the pattern is used.

On private user-owned or tenant-owned records, the resulting composition can be
security-critical.

On intentionally public resources, the same consequence may not exist.

SOL POSITION:

Accept the defect.

Provisional severity:

HIGH generally.

BLOCKER when the pattern is presented or used as protection for private,
user-scoped, tenant-scoped, or otherwise restricted data.

Final severity belongs to Factory disposition.

---

## 4. REVIEW OF HIGH FINDINGS

### C04-D05 — Confusion between user-scoped and elevated clients

SOL ASSESSMENT:
ACCEPT — HIGH

This is an important capability-boundary defect.

Running code on the server does not automatically justify service-role
privilege, and a normal session-scoped client cannot perform privileged admin
operations merely because the call occurs server-side.

The doctrine needs one consistent capability-selection rule.

---

### C04-D10 — Multi-step persistence and compensation failure

SOL ASSESSMENT:
ACCEPT — HIGH

The issue is not simply that the operations are non-atomic.

Astra correctly focuses on the absence of recovery semantics when compensation
itself fails or when execution stops between steps.

The doctrine needs to distinguish:

- complete success,
- recoverable failure,
- partial completion,
- failed compensation,
- and reconciliation ownership.

---

### C04-D11 — Persisted personal data lacks an account-transition lifecycle

SOL ASSESSMENT:
ACCEPT — HIGH

Astra identifies a concrete lifecycle gap between persisted checkout/contact data
and logout/account changes.

The issue is stronger than generic localStorage criticism.

The doctrine describes persistence and logout independently but does not define
their interaction.

A shared browser therefore has no documented guarantee that prior account data
is invalidated.

---

### C04-D08 — Client recipes conflict with server-resolved identity doctrine

SOL ASSESSMENT:
ACCEPT — HIGH

This is another example of doctrine drift.

The newer rule says server-resolved identity/role drives authoritative first
rendering and route behavior.

Older active recipes still make client stores/HOCs appear authoritative.

The danger is not merely UI flicker.

Different pieces of doctrine assign authority to different layers.

---

### C04-D07 — Route-guard contract mismatch

SOL ASSESSMENT:
ACCEPT — HIGH

Astra identifies incompatible signatures and return expectations for the same
guarding mechanism.

This is a concrete executability defect.

A competent Engineer cannot follow all cited instructions simultaneously without
repairing the contract.

---

### C04-D04 — Cookie guidance conflicts with Starter Kit session architecture

SOL ASSESSMENT:
ACCEPT — HIGH

The cited doctrine requires mutually incompatible cookie behavior.

This should not be solved by selecting the more "secure sounding" option in
isolation.

The session architecture and its browser/server requirements must determine the
cookie contract.

---

### C04-D09 — Unbounded post-confirmation redirect

SOL ASSESSMENT:
ACCEPT — HIGH

The doctrine uses externally supplied navigation input without an explicit
same-origin / allowed-path restriction.

Astra appropriately limits its claim to redirection/phishing risk and does not
claim automatic credential disclosure.

The finding is well bounded.

---

## 5. REVIEW OF MEDIUM FINDINGS

### C04-D16 — Logout ignores sign-out result

SOL ASSESSMENT:
ACCEPT — MEDIUM

The route reports success without establishing that the provider sign-out
operation actually succeeded.

This is a truthful-outcome and recovery defect.

---

### C04-D17 — Timestamp-only cursor pagination

SOL ASSESSMENT:
ACCEPT — MEDIUM

The example uses a non-unique cursor field.

Tied timestamps can cause records to be skipped.

This is a concrete correctness defect.

---

### C04-D13 — Conditional hook invocation in hydration recipe

SOL ASSESSMENT:
ACCEPT — MEDIUM

The example changes the number/order of hook invocations depending on hydration
state.

Astra also correctly notes that the implementation does not actually provide the
Suspense behavior its prose describes.

---

### C04-D12 — Hydration readiness can remain false

SOL ASSESSMENT:
ACCEPT — MEDIUM

The doctrine conflates business-state reset with persistence-readiness state.

Reset/failure paths can therefore leave dependent UI with no transition back to
ready.

---

### C04-D15 — Client store can override new server truth indefinitely

SOL ASSESSMENT:
ACCEPT — MEDIUM

The example uses store emptiness as initialization/freshness state.

That does not prove the stored dataset is still authoritative.

The defect is consistent with the doctrine's own rule that backend/server data
remains server-owned.

---

### C04-D14 — Composite-item update mutates shared object state

SOL ASSESSMENT:
ACCEPT — MEDIUM

A shallow array copy does not clone nested item objects.

The example contradicts the surrounding immutable-update rule unless explicit
Immer semantics are present.

---

## 6. REVIEW OF SUGGESTIONS

### C04-S01 — Adversarial authorization evidence matrix

SOL ASSESSMENT:
ACCEPT AS SUGGESTION

High value.

This would strengthen existing security-verification doctrine without creating a
new authority model.

---

### C04-S02 — Explicit tenancy / administrative reach decision

SOL ASSESSMENT:
ACCEPT AS SUGGESTION

Important because the reviewed manuals do not establish one universal tenant
model.

The suggestion correctly asks projects to make the isolation model explicit
rather than inventing a global Factory assumption.

---

### C04-S03 — Cache privacy / invalidation classification

SOL ASSESSMENT:
ACCEPT AS SUGGESTION

Useful maintainability/security improvement.

A reusable cache pattern should identify whether its data is:

- public,
- user-scoped,
- tenant-scoped,
- transient,
- or otherwise restricted,

and define invalidation/lifetime accordingly.

---

## 7. WHAT ASTRA DID PARTICULARLY WELL

### A. It separated doctrine defects from implementation claims

Astra repeatedly states that it did not inspect:

- deployed applications,
- live Supabase policies,
- installed triggers,
- actual service credentials,
- or external runtime state.

That is good evidence discipline.

### B. It respected chunk boundaries

Chunk 05 commerce/payment material was not broadly reviewed even when nearby
security dependencies existed.

Cross-references were bounded and recorded.

### C. It found cross-document drift rather than only isolated errors

Several major findings exist because newer governing principles coexist beside
older recipes.

That is precisely the type of problem a doctrine review should find.

### D. It preserved uncertainty

UNKNOWN and AMBIGUOUS states are used instead of invented answers.

### E. It identified strengths worth protecting

The review does not propose throwing away the domain.

It identifies strong principles such as:

- one authoritative role source,
- server-resolved identity,
- database-enforced ownership,
- schema-first integrity,
- small/selectively persisted client stores,
- and behavioral evidence beyond green builds.

Future correction should preserve those strengths.

---

## 8. WHERE SOL WOULD TEMPER ASTRA

Astra's defect discovery is strong.

Its severity classification should not automatically become Factory truth.

In particular:

- C04-D02 requires final severity adjudication.
- C04-D06 is highly context-sensitive and should not automatically remain a
  universal BLOCKER.

This reinforces an important Factory rule:

ASTRA FINDS AND ARGUES.

ASTRA DOES NOT DISPOSITION ITS OWN FINDINGS.

The independent reviewer is an examiner, not the final authority.

---

## 9. DEEPER FACTORY-LEVEL LESSON

Chunk 04 exposes a likely documentation-maintenance failure pattern:

NEW HARD RULE
+
OLD EXECUTABLE RECIPE
+
OLD SUMMARY / HELPER CONTRACT
=
MULTIPLE APPARENTLY VALID WAYS TO IMPLEMENT THE SAME SECURITY BOUNDARY

This is dangerous in an AI-operated Factory.

Humans may infer that the newer rule supersedes the older example.

An AI Engineer may instead retrieve and copy the executable example.

Therefore future DocSet synchronization work should explicitly test for:

- stale examples,
- stale summaries,
- stale helper signatures,
- duplicated authority models,
- and executable recipes that contradict newer governing rules.

This conclusion should be carried forward as a synthesis candidate.

It is NOT yet final doctrine.

---

## 10. SOL PRELIMINARY DISPOSITION SUMMARY

BLOCKERS:

C04-D03:
ACCEPT — BLOCKER

C04-D01:
ACCEPT — BLOCKER

C04-D02:
ACCEPT DEFECT — severity pending final disposition

C04-D06:
ACCEPT DEFECT — HIGH by default; BLOCKER where used as access protection for
private/restricted data

HIGH:

C04-D05:
ACCEPT

C04-D10:
ACCEPT

C04-D11:
ACCEPT

C04-D08:
ACCEPT

C04-D07:
ACCEPT

C04-D04:
ACCEPT

C04-D09:
ACCEPT

MEDIUM:

C04-D16:
ACCEPT

C04-D17:
ACCEPT

C04-D13:
ACCEPT

C04-D12:
ACCEPT

C04-D15:
ACCEPT

C04-D14:
ACCEPT

SUGGESTIONS:

C04-S01:
ACCEPT AS SUGGESTION

C04-S02:
ACCEPT AS SUGGESTION

C04-S03:
ACCEPT AS SUGGESTION

These are SOL preliminary assessments only.

FINAL_DISPOSITION / DISPOSITION.md remains reserved for Tony after the independent
review campaign and comparative analysis are complete.

---

## 11. CURRENT RECOMMENDATION

Do not repair doctrine yet.

Do not expose the Astra findings to Fable while Fable's independent whole-corpus
review remains active.

Preserve Chunk 04 as independent Astra evidence.

Continue the Astra campaign after checkpointing this chunk.

After the independent Fable review is complete:

1. compare independent overlap,
2. identify Astra-only findings,
3. identify Fable-only findings,
4. adjudicate severity,
5. reproduce/verify high-risk claims where required,
6. then build the approved doctrine-change package.

---

## 12. SOL VERDICT ON CHUNK 04

ASTRA REVIEW QUALITY:

STRONG

EVIDENCE DISCIPLINE:

STRONG

BOUNDARY DISCIPLINE:

STRONG

TECHNICAL VALUE:

HIGH

SEVERITY CALIBRATION:

GOOD, BUT REQUIRES HUMAN / FACTORY ADJUDICATION

FINAL SOL POSITION:

Chunk 04 materially justifies the Chunky Monkey review method.

The review produced a bounded, independently auditable security/data case file
containing concrete defects, explicit uncertainty, preservation targets, and
cross-domain handoffs without attempting unauthorized synthesis or repair.

Proceed to checkpoint.

Do not treat the findings as final Factory doctrine until disposition is
complete.