# Distributable Agent Skill Bundles v0.1

## Purpose

- define which distributable agent card should be paired with which skill set
- keep promotion decisions tied to tested bundles rather than isolated cards

## Bundle Rule

- distributable agent cards should not be promoted alone
- each agent card should carry a matching skill pair or trio
- the bundle should reflect actual task shape, not ideology

## Recommended Bundles

### 1. Light Intake Bundle
- agent:
  - `AGENTS/agent_distributable_intake_router.md`
- skills:
  - `SKILLS/skill_scope_lock.md`
  - `SKILLS/skill_route_lock.md`
- best for:
  - lighter intake
  - distributable-generic routing
  - quick session sorting

### 2. Structured Intake Bundle
- agent:
  - `AGENTS/agent_ailo_e_intake_chief.md`
- skills:
  - `SKILLS/skill_scope_lock.md`
  - `SKILLS/skill_route_lock.md`
- best for:
  - project-forming requests
  - escalation-heavy routing
  - stronger structure and lock discipline

### 3. Security Gate Bundle
- agent:
  - `AGENTS/security_gate_agent.md`
- skills:
  - `SKILLS/security_checklist.md`
  - `SKILLS/skill_gate_judgment.md`
- best for:
  - inbound checking
  - risky execution review
  - outbound release judgment

### 4. Distributable Research Bundle
- agent:
  - `AGENTS/agent_distributable_research_specialist.md`
- skills:
  - `SKILLS/skill_research.md`
  - `SKILLS/skill_evidence_pack.md`
- best for:
  - quick evidence gathering
  - flatter distributable language
  - low-friction research output

### 5. AILO-E Research Bundle
- agent:
  - `AGENTS/agent_ailo_e_research_specialist.md`
- skills:
  - `SKILLS/skill_research.md`
  - `SKILLS/skill_evidence_pack.md`
- best for:
  - contract-sensitive research
  - uncertainty separation
  - stronger bounded return discipline

### 6. Distributable Coding Bundle
- agent:
  - `AGENTS/agent_distributable_coding_specialist.md`
- skills:
  - `SKILLS/skill_patch_shape.md`
  - `SKILLS/skill_review.md`
- best for:
  - low-risk helper changes
  - fine-grained patch lane
  - current default distributable coding specialist shape

### 7. AILO-E Coding Worker Bundle
- agent:
  - `AGENTS/agent_ailo_e_code_worker.md`
- skills:
  - `SKILLS/skill_patch_shape.md`
  - `SKILLS/skill_review.md`
- best for:
  - blocker honesty
  - stop posture
  - bounded implementation under ambiguous conditions

### 8. Distributable Writing Bundle
- agent:
  - `AGENTS/agent_distributable_writing_specialist.md`
- skills:
  - `SKILLS/skill_brief_to_draft.md`
  - `SKILLS/skill_review.md`
- best for:
  - brief-to-draft work
  - flatter distributable output
  - compact writing tasks

## Current Default Rule

- coding specialist:
  - use `AGENTS/agent_distributable_coding_specialist.md` first
- intake with stronger structure:
  - use `AGENTS/agent_ailo_e_intake_chief.md`
- research with stronger uncertainty discipline:
  - use `AGENTS/agent_ailo_e_research_specialist.md`

## Promotion Note

- treat these bundles as operating units, not isolated cards
- prefer promotion only after repeated use confirms the bundle, not just the card
