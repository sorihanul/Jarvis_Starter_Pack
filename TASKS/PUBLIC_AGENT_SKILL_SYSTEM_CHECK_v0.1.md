# Public Agent Skill System Check v0.1

## Purpose

- check whether the current public-facing agent cards already have a matching skill layer
- define the minimum skill set needed before public promotion

## Current State

- the public agent cards are now ahead of the public skill layer
- `chief`, `gate`, `research specialist`, `coding specialist`, and `writing specialist` all have clearer behavioral lanes than the current `SKILLS/` set can express
- the current shared skills cover only:
  - research
  - review
  - summarize
  - security checklist

## Main Finding

- the new public agent system is structured enough to test
- but the matching skill system is still too thin
- if the starter promotes agent forms without a matching skill layer, the public system will drift back into generic helper behavior

## Minimum Public-Safe Skill Set

### 1. `skill_scope_lock.md`
- target lane:
  - chief
- use:
  - lock the bounded scope of the current request before work expands

### 2. `skill_route_lock.md`
- target lane:
  - chief
- use:
  - choose and freeze the first route and first review surface

### 3. `skill_gate_judgment.md`
- target lane:
  - gate
- use:
  - return `allow | warn | hold | block | escalate` style judgments with reasons and next action

### 4. `skill_evidence_pack.md`
- target lane:
  - research specialist
- use:
  - gather facts, uncertainty, and source paths into one bounded evidence return

### 5. `skill_patch_shape.md`
- target lane:
  - coding specialist
- use:
  - keep coding output inside a patch-shaped delivery contract
- current public bias:
  - this lane currently fits `non-AILO` better than `AILO`

### 6. `skill_brief_to_draft.md`
- target lane:
  - writing specialist
- use:
  - turn a bounded brief into one draft with stated tone and structure

## Current Matching Rule

- `chief`
  - pair with:
    - `skill_scope_lock`
    - `skill_route_lock`

- `gate`
  - pair with:
    - `security_checklist`
    - `skill_gate_judgment`

- `research specialist`
  - pair with:
    - `skill_research`
    - `skill_evidence_pack`

- `coding specialist`
  - pair with:
    - `skill_patch_shape`
    - `skill_review`

- `writing specialist`
  - pair with:
    - `skill_brief_to_draft`
    - `skill_review`

## Working Verdict

- public agent bundle refinement should continue
- but public promotion should treat agent cards and skill cards as a pair
- current baseline is:
  - stronger agent lanes first
  - then matching skill cards
  - then public module promotion
