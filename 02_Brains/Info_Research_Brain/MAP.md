# Info Research Brain Map

## 구조

```text
Info_Research_Brain/
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
  SOURCE_REVIEW_BINDING.md
  SOURCE_POLICY.md
  OUTPUT_CONTRACT.md
  ACCEPTANCE_TESTS.md
  TASKS/
    PREFLIGHT_RESULT.md
    CURRENT_TASK.md
    RESEARCH_QUEUE.md
  LOGS/
    SESSION_OPS_LOG.md
  CAPSULES/
    CURRENT_CAPSULE.md
  NOTES/
    SOURCE_LEDGER.md
    FINDINGS_INDEX.md
    OPEN_QUESTIONS.md
```

## 핵심 파일

- `START_HERE.md`: 사람이 처음 읽는 진입면
- `BOOT.md`: 새 세션 부팅 순서와 첫 응답
- `MAP.md`: 브레인 내부 경로와 읽기 순서
- `LOCAL_RULEBOOK.md`: 조사 운영 규칙
- `MEMORY_MAP.md`: 기억 표면 구분
- `RUNTIME_BOUNDARY.md`: 브레인 본체와 운용 기록의 동기화 경계
- `SESSION_CARD.md`: 정체성, 경계, 기본 루프
- `BRAIN.md`: 브레인의 역할과 금지
- `MODE_REGISTRY.md`: 조사 모드 선택
- `FUNCTION_PACKS.md`: 조사 요청을 작게 처리하는 내부 AILO 함수팩
- `DECISION_TABLES.md`: route, evidence, freshness, conflict, memory, close 반복 판정표
- `SOURCE_BINDINGS.md`: 출처 표면과 사용 가능한 자료 경로
- `SOURCE_REVIEW_BINDING.md`: 단일 출처 검토와 원소스 source-review proof의 연결 규칙
- `SOURCE_POLICY.md`: 출처 사용 규칙
- `OUTPUT_CONTRACT.md`: 출력 형식
- `ACCEPTANCE_TESTS.md`: 작동 검증표
- `TASKS/PREFLIGHT_RESULT.md`: v3 함수팩 사전 판정 결과
- `TASKS/CURRENT_TASK.md`: 현재 조사 상태
- `TASKS/RESEARCH_QUEUE.md`: 다음 조사 후보
- `NOTES/SOURCE_LEDGER.md`: 반복 참조 출처 장부
- `NOTES/FINDINGS_INDEX.md`: 확정된 조사 결과 색인
- `NOTES/OPEN_QUESTIONS.md`: 미확인 질문 목록

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
12. `SOURCE_REVIEW_BINDING.md`
13. `SOURCE_POLICY.md`
14. `OUTPUT_CONTRACT.md`
15. `TASKS/PREFLIGHT_RESULT.md`
16. `TASKS/CURRENT_TASK.md`

## 경계

- 이 브레인은 범용 조사 브레인이다.
- 도메인 전문 지식은 조사 중 필요한 만큼만 붙인다.
- 반복되는 전문 조사 영역은 나중에 별도 도메인 브레인이나 지식팩으로 분리할 수 있다.
- `TASKS/CURRENT_TASK.md`, `LOGS`, `CAPSULES`, `NOTES`는 운용 기록이므로 원소스와 강제 동기화하지 않는다.

## context rehydration

`CONTEXT_REHYDRATION_BINDING.md` links this brain to the root v3 no-false-completion and claim-ceiling rule. It is read on trigger, not as mandatory startup bulk.
