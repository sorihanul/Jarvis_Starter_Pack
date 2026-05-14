# Session Card Template v0.1

아래 템플릿은 `Jarvis Starter Pack`에서 세션 정체성을 고정할 때 쓰는 최소 카드다.

```md
# Session Card

- session_name:
- session_type: main | orchestration | task | research | writing | coding | review
- purpose:
- current_scope:
- read_order:
- write_targets:
- do_not_touch:
- active_rules:
- handoff_to:
- close_condition:
```

## 예시 1. 메인 세션

```md
# Session Card

- session_name: starter-brain-main
- session_type: main
- purpose: 자비스 스타터 문서와 모듈을 설계하고 정리한다
- current_scope: TASKS/, 01_Modules/, 루트 문서
- read_order: START_HERE.md -> MAP.md -> POLICY.md
- write_targets: TASKS/, CAPSULES/
- do_not_touch: 00_Core~05_Scripts
- active_rules: public starter, document-first, no productization
- handoff_to: project orchestration session
- close_condition: 필요한 문서 정리와 공개판 판단 완료
```

## 예시 2. 프로젝트 오케스트레이션 세션

```md
# Session Card

- session_name: project-alpha-orchestration
- session_type: orchestration
- purpose: 프로젝트 alpha의 roster, phase, outputs를 설계한다
- current_scope: TASKS/PROJECTS/project-alpha
- read_order: START_HERE.md -> MAP.md -> POLICY.md -> project docs
- write_targets: TASKS/PROJECTS/project-alpha, LOGS/
- do_not_touch: 00_Core~05_Scripts
- active_rules: separate orchestration session, project-local planning
- handoff_to: implementation session
- close_condition: BOOT_ENTRY, MISSION, ROADMAP, ORCHESTRATOR 정리 완료
```

## 예시 3. 코딩 작업 세션

```md
# Session Card

- session_name: login-fix-task
- session_type: coding
- purpose: 로그인 오류를 분석하고 수정한다
- current_scope: 대상 코드 경로와 관련 TASKS
- read_order: START_HERE.md -> POLICY.md -> relevant code
- write_targets: TASKS/, LOGS/, 변경 파일
- do_not_touch: unrelated core files
- active_rules: bounded scope, validate before close
- handoff_to: review or validation session
- close_condition: 수정, 검증, 결과 보고 완료
```
