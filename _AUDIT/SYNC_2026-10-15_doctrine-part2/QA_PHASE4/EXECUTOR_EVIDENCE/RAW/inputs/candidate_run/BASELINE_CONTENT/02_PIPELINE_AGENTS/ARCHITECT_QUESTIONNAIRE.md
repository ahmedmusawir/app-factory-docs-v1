# 🏗️ ARCHITECT QUESTIONNAIRE

> **Version:** 2.2 · **Date:** 2026-07-07 · **Status:** Active
> **Tier:** 2 — Pipeline Agents · **Pairs with:** ARCHITECT_PLAYBOOK, APP_FACTORY_BLUEPRINT, RECON_QUESTIONNAIRE

> **This doc is the SINGLE SOURCE for the Ignition Questionnaire and the APP_BRIEF template.**
> ARCHITECT_PLAYBOOK §3 and §5 point here — do not fork this instrument.

---

### Preamble

> **Purpose:** This questionnaire is a **state transition tool**. It converts a raw idea into a machine-usable planning state that downstream agents (Designer, Engineer) can operate on **without making assumptions**.
>
> This is NOT requirements gathering. This is NOT design. This is NOT backend planning.
> This is the **anti-hallucination boundary** for the entire planning chain.

> 🔎 **Recon precedes ignition:** the Architect runs this questionnaire only AFTER a current Recon Report exists (Phase 0 — see ARCHITECT_PLAYBOOK §2 Recon Mode and RECON_QUESTIONNAIRE).

---

### Phase 1: Quick Ignition (5 questions — mandatory)

1. **Hero Action:** Complete this sentence: "When the user opens this app, they must be able to _____ in under 10 seconds."
2. **Primary User + Roles:** Single player (just you) or multiplayer (team/RBAC)?
   - Technical level: Non-technical / Semi-technical / Technical
   - Environment: OS, browser/device, network context
3. **Brain Check:** Does this app require AI/Agents to function, or is it standard CRUD?
4. **Visual Anchor:** Provide a screenshot, style tile, or Figma link. *(None available → STOP — get one before proceeding.)*
5. **Out-of-Scope Lock:** List minimum 5 things this app will NOT do in v1.

> ⛔ **HARD GATE:** If Out-of-Scope is vague, duplicated, or under 5 items, the Architect MUST pause and request clarification before proceeding.

---

### Phase 2: Data Reality (4 questions — if Brain Check = Yes)

6. **Core Objects:** What are the main "nouns"? (e.g., Agent, Session, Message, Document)
7. **Input Types:** What can users feed into v1? (text, markdown, PDF, images — pick max 3)
8. **Persistence Model:** Durable knowledge (DB) vs ephemeral uploads (session-only) — which for v1?
9. **Output Destination:** Where does agent output go? (screen only / saved artifact / GCS bucket)

> 📌 **REALITY RULE:** Core objects listed here are considered "real" (persisted, backend-managed) unless explicitly marked as UI-only or conceptual.

---

### Phase 3: Constraints & Success (3 questions — before handoff)

10. **Tech Stack:** Factory Standard (Next.js/Supabase/Tailwind) or exotic? If exotic, specify per layer: Frontend / Backend / Database / Auth / Hosting / AI-ML.
11. **Success Demo:** Describe a successful demo in exactly 3 steps.
12. **Failure Modes:** List top 3 failure modes to prevent (e.g., scope creep, lost artifacts, broken handoffs).

---

### Phase 4: Constraints Deep-Dive (5 questions — OPTIONAL)

> **Run this phase only when the project warrants it** — complex builds, external dependencies, a compliance surface, or a hard delivery date. For simple builds, Phases 1–3 are the whole instrument: 12 questions doing the work of 40. Phase 4 exists so depth is available when needed — never mandatory.
> *(Absorbed from ARCHITECT_PLAYBOOK §3 at the F-017 single-source merge.)*

13. **App Type:** Full-Stack Web App / Backend Bundle / Local-First Tool? (Feeds the ARCHITECT_PLAYBOOK §4 App Type Router.)
14. **Tech Constraints & Deadline:** Must use: ___ · Cannot use: ___ · Prefer: ___ · Hard deadline: ___
15. **External Integrations:** APIs: ___ · Services: ___ · Data sources: ___ ("None" is a valid answer — record it.)
16. **Security / Compliance:** Any security or compliance requirements? ("None identified" is a valid answer — record it.)
17. **Risks & Unknowns:** Technical risks: ___ · Dependency risks: ___ · Timeline risks: ___ · What don't we know yet: ___

> 📥 **ROUTING RULE:** every unresolved Phase 4 answer lands in the APP_BRIEF **Planning State** table (§8) as ❓ Open Question — or ⚠️ Assumption if provisionally decided. Nothing from this phase may live only in conversation.

---

## 📄 APP_BRIEF.md TEMPLATE

```markdown
# APP BRIEF: [Project Name]

> **Status:** [DRAFT | REVIEW | LOCKED]
> **Last Updated:** [Date]
> **Author:** Architect Agent

---

## 1. Mission Statement
One paragraph. What does this app DO and for WHOM?

## 2. Hero Action
The primary interaction loop, completable in <10 seconds.

## 3. User & Auth Scope
- **Target Audience:** 
- **Technical Level:** 
- **Environment:** 
- **Auth Method:** 
- **Roles (v1):** 

## 4. Complexity Class
- **App Type:** [CRUD | Agentic | Dashboard | Utility]
- **Deployment Class:** [Full-Stack Web | Backend Bundle | Local-First Tool]
- **AI Required:** [Yes | No]
- **Real-time:** [Yes | No]

## 5. Domain Concepts (Core Objects)

> Objects listed here are **real** (persisted) unless marked otherwise.

| Object | Key Fields | Lifecycle | Notes |
|--------|------------|-----------|-------|
| Agent | name, prompt, status | Static | Config-driven |
| Session | agent_id, messages[], created_at | Created → Active → Archived | |

## 6. Scope Locks

### ✅ In Scope (v1):
- 
- 

### 🚫 Out of Scope (v1): *(minimum 5 required)*
1. 
2. 
3. 
4. 
5. 

## 7. Success Definition

**Demo in 3 steps:**
1. 
2. 
3. 

**Metrics to track:**
- 

## 8. Planning State

| Item | Type | Notes |
|------|------|-------|
| [Example: Auth = Supabase] | 🔒 Decision | Locked |
| [Example: Agent count = 3] | ⚠️ Assumption | May change |
| [Example: MCP integration?] | ❓ Open Question | Needs research |

## 9. Integrations *(from Phase 4 — "None for v1" is a valid entry)*

| System | Type | Purpose |
|--------|------|---------|
| [System or "None for v1"] | API / SDK / Webhook | |

## 10. Constraints & Deadline *(from Phase 4)*

- **Must use:** 
- **Cannot use:** 
- **Prefer:** 
- **Hard deadline:** 

## 11. Risks & Unknowns *(from Phase 4)*

| Risk / Unknown | Type | Mitigation / Next Step |
|---|---|---|
| | Technical / Dependency / Timeline / Unknown | |

> Unresolved items here MUST also appear in §8 Planning State as ❓ or ⚠️.

## 12. Handoff Checklist

- [ ] Designer receives: `APP_BRIEF.md` + Visual Anchor
- [ ] Engineer receives: `APP_BRIEF.md` + Domain Concepts table
- [ ] All Open Questions resolved or explicitly deferred
```

---

## Version History

| Version | Date | Change |
|---|---|---|
| 2.2 | 2026-07-07 | **Wave 2A — F-017 single-source merge.** This doc is now the SINGLE SOURCE for the Ignition Questionnaire + APP_BRIEF template; ARCHITECT_PLAYBOOK §3/§5 shrink to pointers. Absorbed the playbook-only value: Q2 enriched (technical level, environment), Q10 enriched (per-layer exotic spec), new OPTIONAL Phase 4 — Constraints Deep-Dive (Q13 App Type, Q14 Tech Constraints & Deadline, Q15 Integrations, Q16 Security/Compliance, Q17 Risks & Unknowns → Planning State ❓ routing rule). Dropped playbook duplicates (what-building, problem-solved, done-looks-like, must-haves, out-of-scope, anchor checklist — each covered by a sharper standalone question or the template). Template gained Deployment Class line + §9 Integrations, §10 Constraints & Deadline, §11 Risks & Unknowns. De-Stitched Q4 → "screenshot, style tile, or Figma link" (F-002). Standard header (F-018); canonical refs (F-011); CRLF→LF normalized. "Changes Applied — GPT Recommendation" table retired into this history (see 2.1 row); chat-residue closing line removed. ⛔ Hard Gate, 📌 Reality Rule, and Planning State preserved untouched. |
| 2.1 | 2026 (pre-audit, undated) | Added preamble (state-transition purpose), 📌 Reality Rule, ⛔ Hard Gate, Planning State table (template §8) — applied from a GPT recommendation review; formerly logged as a "✅ Changes Applied" table (chat residue, retired at 2.2). |
| ≤2.0 | — | Earlier questionnaire iterations, pre-dating this standalone doc's version tracking. |

---

🥄 *Part of Stark Industries — App Factory doctrine.*
