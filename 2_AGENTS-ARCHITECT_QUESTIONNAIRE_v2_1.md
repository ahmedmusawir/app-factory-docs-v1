## 🏗️ ARCHITECT QUESTIONNAIRE v2.1 (FINAL)

### Preamble (NEW)

> **Purpose:** This questionnaire is a **state transition tool**. It converts a raw idea into a machine-usable planning state that downstream agents (Designer, Engineer) can operate on **without making assumptions**.
>
> This is NOT requirements gathering. This is NOT design. This is NOT backend planning.
> This is the **anti-hallucination boundary** for the entire planning chain.

---

### Phase 1: Quick Ignition (5 questions — mandatory)

1. **Hero Action:** Complete this sentence: "When the user opens this app, they must be able to _____ in under 10 seconds."
2. **Primary User + Roles:** Single player (just you) or multiplayer (team/RBAC)?
3. **Brain Check:** Does this app require AI/Agents to function, or is it standard CRUD?
4. **Visual Anchor:** Provide a screenshot, Stitch output, or Figma link.
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

10. **Tech Stack:** Factory Standard (Next.js/Supabase/Tailwind) or exotic? If exotic, specify.
11. **Success Demo:** Describe a successful demo in exactly 3 steps.
12. **Failure Modes:** List top 3 failure modes to prevent (e.g., scope creep, lost artifacts, broken handoffs).

---

## 📄 APP_BRIEF.md TEMPLATE v2.1 (FINAL)

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
- **Auth Method:** 
- **Roles (v1):** 

## 4. Complexity Class
- **App Type:** [CRUD | Agentic | Dashboard | Utility]
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

## 9. Handoff Checklist

- [ ] Designer receives: `APP_BRIEF.md` + Visual Anchor
- [ ] Engineer receives: `APP_BRIEF.md` + Domain Concepts table
- [ ] All Open Questions resolved or explicitly deferred
```

---

### ✅ Changes Applied

| GPT Recommendation | Status |
|--------------------|--------|
| Add preamble explaining state transition purpose | ✅ Done |
| Clarify core objects = real unless marked | ✅ Added as "Reality Rule" |
| Make Out-of-Scope a hard gate | ✅ Added as "Hard Gate" warning |
| Distinguish Decision / Assumption / Open Question | ✅ New "Planning State" table in Section 8 |

---

**This is now a foundational Factory artifact.** Ready for the manual experiment when you are, Tony. 🎯