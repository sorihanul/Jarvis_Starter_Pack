# Public Agent Bundle Session Dryruns

- date: 2026-03-26
- purpose: verify that the new public agent cards still read cleanly when paired with a session card and matching skills

## Method

- use one minimal session card per lane
- assign the recommended bundle from `TASKS/PUBLIC_AGENT_SKILL_BUNDLES_v0.1.md`
- check whether the card, the skill pair, and the lane all agree on:
  - bounded scope
  - first action
  - stop boundary
  - handoff target

## Case 1. Light Intake Bundle

### Session Card

```md
# Session Card

- session_name: light-intake-demo
- session_type: task
- purpose: 짧은 요청을 어느 레인에서 먼저 처리할지 정한다
- current_scope: 현재 사용자 요청 하나
- read_order: START_HERE.md -> POLICY.md -> current request
- write_targets: LOGS/
- do_not_touch: 00_Core~05_Scripts
- active_rules: bounded scope, first-route lock
- handoff_to: research or coding or writing
- close_condition: first route and first review surface fixed
```

### Bundle

- agent: `AGENTS/agent_public_intake_router.md`
- skills:
  - `SKILLS/skill_scope_lock.md`
  - `SKILLS/skill_route_lock.md`

### Dryrun Verdict

- result: pass
- why:
  - the card reads naturally with a lightweight session card
  - the two skills complete the missing parts cleanly
  - no role collision with gate or worker behavior

## Case 2. Structured Intake Bundle

### Session Card

```md
# Session Card

- session_name: structured-intake-demo
- session_type: orchestration
- purpose: 프로젝트형 요청의 첫 구조를 잠그고 별도 세션 필요 여부를 판단한다
- current_scope: project-forming request only
- read_order: START_HERE.md -> POLICY.md -> current request
- write_targets: TASKS/PROJECTS/, LOGS/
- do_not_touch: 00_Core~05_Scripts
- active_rules: scope lock, route lock, escalation-first if needed
- handoff_to: project orchestration session
- close_condition: bounded scope and first route fixed
```

### Bundle

- agent: `AGENTS/agent_ailo_e_intake_chief.md`
- skills:
  - `SKILLS/skill_scope_lock.md`
  - `SKILLS/skill_route_lock.md`

### Dryrun Verdict

- result: strong pass
- why:
  - the card and the skill pair match almost perfectly
  - this remains the strongest bundle for project-forming or escalation-heavy intake
  - session-card framing makes the route-lock behavior even clearer

## Case 3. Security Gate Bundle

### Session Card

```md
# Session Card

- session_name: security-check-demo
- session_type: review
- purpose: 외부 코드 실행 요청을 진행 전 점검한다
- current_scope: inbound and execution safety judgment only
- read_order: POLICY.md -> current request -> relevant plan
- write_targets: LOGS/
- do_not_touch: target files before judgment
- active_rules: judgment before action
- handoff_to: chief or user approval
- close_condition: allow/warn/hold/block/escalate returned
```

### Bundle

- agent: `AGENTS/security_gate_agent.md`
- skills:
  - `SKILLS/security_checklist.md`
  - `SKILLS/skill_gate_judgment.md`

### Dryrun Verdict

- result: pass
- why:
  - `security_checklist` finds the risk surface
  - `skill_gate_judgment` compresses the final control decision
  - this bundle is now cleaner than relying on checklist alone

## Case 4. Public Research Bundle

### Session Card

```md
# Session Card

- session_name: public-research-demo
- session_type: research
- purpose: 공개 문서를 조사해 근거와 남은 불확실성을 정리한다
- current_scope: one research question
- read_order: START_HERE.md -> current request -> local docs
- write_targets: LOGS/, CAPSULES/
- do_not_touch: 00_Core~05_Scripts
- active_rules: evidence first, bounded return
- handoff_to: synthesis or writing
- close_condition: claims, evidence, uncertainty produced
```

### Bundle

- agent: `AGENTS/agent_public_research_specialist.md`
- skills:
  - `SKILLS/skill_research.md`
  - `SKILLS/skill_evidence_pack.md`

### Dryrun Verdict

- result: pass
- why:
  - this is the clean public-generic research lane
  - the new evidence pack skill prevents the card from collapsing back into generic summary mode

## Case 5. AILO-E Research Bundle

### Session Card

```md
# Session Card

- session_name: ailo-research-demo
- session_type: research
- purpose: 계약 민감도가 높은 조사 결과를 bounded하게 정리한다
- current_scope: one contract-sensitive question
- read_order: START_HERE.md -> POLICY.md -> local docs
- write_targets: LOGS/
- do_not_touch: 00_Core~05_Scripts
- active_rules: bounded claims, uncertainty separation
- handoff_to: chief or critic
- close_condition: status, claims, evidence, uncertainty fixed
```

### Bundle

- agent: `AGENTS/agent_ailo_e_research_specialist.md`
- skills:
  - `SKILLS/skill_research.md`
  - `SKILLS/skill_evidence_pack.md`

### Dryrun Verdict

- result: strong pass
- why:
  - the stronger card becomes practical once the evidence pack skill is present
  - this bundle is the cleaner choice when uncertainty reporting matters more than speed

## Case 6. Public Coding Bundle

### Session Card

```md
# Session Card

- session_name: public-coding-demo
- session_type: coding
- purpose: 저위험 보조 수정 하나를 patch-shaped output으로 정리한다
- current_scope: one small helper change
- read_order: START_HERE.md -> POLICY.md -> target file
- write_targets: LOGS/, changed file
- do_not_touch: unrelated core files
- active_rules: patch lane, bounded result
- handoff_to: validation or critic
- close_condition: intended location and patch intent fixed
```

### Bundle

- agent: `AGENTS/agent_public_coding_specialist.md`
- skills:
  - `SKILLS/skill_patch_shape.md`
  - `SKILLS/skill_review.md`

### Dryrun Verdict

- result: strong pass
- why:
  - this is the current best public coding default
  - the patch-shape skill stabilizes the lane around the bounded coding behavior this starter expects

## Case 7. AILO-E Coding Worker Bundle

### Session Card

```md
# Session Card

- session_name: ailo-code-worker-demo
- session_type: coding
- purpose: blocker honesty가 필요한 수정 요청의 진행 가능 범위를 확인한다
- current_scope: one ambiguous coding slice
- read_order: START_HERE.md -> POLICY.md -> target file
- write_targets: LOGS/
- do_not_touch: unrelated files and protected layers
- active_rules: stop posture, bounded implementation
- handoff_to: chief or public coding specialist
- close_condition: ready or blocked returned honestly
```

### Bundle

- agent: `AGENTS/agent_ailo_e_code_worker.md`
- skills:
  - `SKILLS/skill_patch_shape.md`
  - `SKILLS/skill_review.md`

### Dryrun Verdict

- result: pass
- why:
  - this lane is not the default coding specialist lane
  - but it is the right lane when environment ambiguity and blocker honesty matter more than rapid output

## Case 8. Public Writing Bundle

### Session Card

```md
# Session Card

- session_name: public-writing-demo
- session_type: writing
- purpose: 짧은 브리프를 한 번에 읽히는 초안으로 바꾼다
- current_scope: one draft only
- read_order: START_HERE.md -> current brief
- write_targets: LOGS/, TASKS/
- do_not_touch: unrelated core files
- active_rules: one draft, no over-explaining
- handoff_to: critic or user revision
- close_condition: draft and revision hint returned
```

### Bundle

- agent: `AGENTS/agent_public_writing_specialist.md`
- skills:
  - `SKILLS/skill_brief_to_draft.md`
  - `SKILLS/skill_review.md`

### Dryrun Verdict

- result: pass
- why:
  - the card and skill pair agree on output-first writing behavior
  - this remains the cleanest writing follower lane in the current bundle set

## Final Reading

- `chief` and `gate` bundles are now structurally complete
- `research` bundles are complete enough to compare public vs AILO-E lanes
- `coding` bundles now read clearly as:
  - `public coding specialist` for default patch lane
  - `AILO-E code worker` for blocker-honest bounded work
- `writing` bundle is coherent and lightweight

## Working Verdict

- the new public agent cards no longer float alone
- once the matching skills are added, the bundles read as an actual operating system layer
- next useful step:
  - run repeated session-card pilots for `public coding specialist`, `public writing specialist`, and `public intake router`
