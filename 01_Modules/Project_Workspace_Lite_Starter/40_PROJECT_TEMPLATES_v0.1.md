# Project Templates v0.1

아래 템플릿은 스타터 팩 안에서 바로 복사해서 쓸 수 있는 최소 형태다.

정식 사용 위치:
- 프로젝트 작업장: `TASKS/PROJECTS/<project_id>/`
- 복사용 원본: `TASKS/PROJECTS/_TEMPLATES/`

실제 파일:
- `TASKS/PROJECTS/_TEMPLATES/BOOT_ENTRY.md`
- `TASKS/PROJECTS/_TEMPLATES/MISSION.md`
- `TASKS/PROJECTS/_TEMPLATES/ROADMAP.md`
- `TASKS/PROJECTS/_TEMPLATES/ORCHESTRATOR.md`
- `TASKS/PROJECTS/_TEMPLATES/TRACK.md`

## 1. BOOT_ENTRY

```md
# BOOT_ENTRY

- identity: 나는 이 스타터 팩 안에서 프로젝트를 정렬하고 집행하는 Jarvis 세션이다.
- workspace: 이번 세션은 특정 프로젝트 작업장을 다룬다.
- role: 현재 역할은 `orchestrator` 또는 특정 작업 역할이다.
- read_first:
  1. MISSION.md
  2. ROADMAP.md
  3. ORCHESTRATOR.md
```

## 2. MISSION

```md
# MISSION

- project_id:
- goal:
- problem:
- scope_in:
- scope_out:
- success_criteria:
```

## 3. ROADMAP

```md
# ROADMAP

## Strategic Layer
- stage_1:
- stage_2:
- stage_3:

## Execution Layer
- current_focus:
- next_step:
- blockers:
```

## 4. ORCHESTRATOR

```md
# ORCHESTRATOR

- execution_mode: sequential | review-heavy | hybrid
- participants:
  - design
  - implementation
  - review
- handoff:
  - design -> implementation
  - implementation -> review
- stop_conditions:
  - scope ambiguity
  - destructive change
  - failed validation
```

## 5. TRACK

```md
# SECURITY_TRACK

- current_focus:
- target_surface:
- checks:
- risks:
- next_action:
```
