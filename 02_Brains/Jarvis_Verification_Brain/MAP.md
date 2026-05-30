# Jarvis Verification Brain Map

## 구조

```text
Jarvis_Verification_Brain/
  START_HERE.md
  BOOT.md
  MAP.md
  LOCAL_RULEBOOK.md
  MEMORY_MAP.md
  RUNTIME_BOUNDARY.md
  SESSION_CARD.md
  BRAIN.md
  MODE_REGISTRY.md
  FUNCTION_PACKS.md
  DECISION_TABLES.md
  SOURCE_BINDINGS.md
  JARVIS_STARTER_BINDING.md
  OUTPUT_CONTRACT.md
  ACCEPTANCE_TESTS.md
  TASKS/
    PREFLIGHT_RESULT.md
    CURRENT_TASK.md
    VERIFICATION_QUEUE.md
  LOGS/
    SESSION_OPS_LOG.md
  CAPSULES/
    CURRENT_CAPSULE.md
  REPORTS/
    README.md
```

## 핵심 파일

- `START_HERE.md`: 진입 안내
- `BOOT.md`: 부팅 순서와 첫 응답
- `MAP.md`: 브레인 내부 경로와 읽기 순서
- `LOCAL_RULEBOOK.md`: 검증 운영 규칙
- `MEMORY_MAP.md`: 기억 표면 구분
- `RUNTIME_BOUNDARY.md`: 본체와 운용 기록 분리
- `SESSION_CARD.md`: 정체성 카드
- `BRAIN.md`: 역할과 금지
- `MODE_REGISTRY.md`: 검증 모드
- `FUNCTION_PACKS.md`: v3 런타임 검증 함수팩
- `DECISION_TABLES.md`: proof level, severity, revalidation, close status 판정표
- `SOURCE_BINDINGS.md`: 검증 대상과 참고 출처 범위
- `JARVIS_STARTER_BINDING.md`: Jarvis Starter Pack 검증 전용 바인딩
- `OUTPUT_CONTRACT.md`: 검증 보고 형식
- `ACCEPTANCE_TESTS.md`: 작동 검증표
- `TASKS/PREFLIGHT_RESULT.md`: 독립 브레인 판정 근거

## 기본 읽기 순서

1. `BOOT.md`
2. `MAP.md`
3. `LOCAL_RULEBOOK.md`
4. `MEMORY_MAP.md`
5. `RUNTIME_BOUNDARY.md`
6. `SESSION_CARD.md`
7. `BRAIN.md`
8. `MODE_REGISTRY.md`
9. `FUNCTION_PACKS.md`
10. `DECISION_TABLES.md`
11. `SOURCE_BINDINGS.md`
12. `JARVIS_STARTER_BINDING.md`
13. `OUTPUT_CONTRACT.md`
14. `TASKS/PREFLIGHT_RESULT.md`
15. `TASKS/CURRENT_TASK.md`

## 경계

- 이 브레인은 검증 브레인이다.
- 제작, 리팩터링, 대량 수정은 기본 역할이 아니다.
- 필요한 수정은 검증 보고의 `fixes_applied` 또는 `fixes_needed`로 분리한다.
- 구조 검증은 실제 동작 증명과 다르다.
