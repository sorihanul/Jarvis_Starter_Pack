# PHASE OUTPUT TEMPLATES v1.2

## 목적

각 단계 산출물 형식을 고정해 다음 빙의 Agent가 바로 이어받게 한다.

---

## ENV_ALIGNMENT 출력

- `status`: PASS|FAIL
- `why`: 환경 정상/비정상 원인
- `next`: DESIGN 또는 환경 복구
- `artifacts`: 버전/인증/PATH 확인 로그

---

## DESIGN 출력

- `status`: PASS|REJECT
- `requirements`: 필수 요구사항
- `scope`: 포함/제외
- `next`: VALIDATION
- `artifacts`: 설계 문서 경로

---

## VALIDATION 출력

- `status`: APPROVE|REJECT
- `blockers`: 치명 이슈 목록
- `required_fixes`: 수정 필수 항목
- `next`: IMPLEMENTATION 또는 DESIGN
- `artifacts`: 검증 체크리스트 경로

---

## IMPLEMENTATION 출력

- `status`: PASS|FAIL
- `changed_files`: 변경 파일
- `executed_commands`: 실행 명령
- `next`: INSPECTION
- `artifacts`: diff/실행 로그

---

## INSPECTION 출력

- `status`: PASS|FAIL
- `findings`: 고위험 이슈 중심
- `next`: AGENDA_LOG 또는 ENV_ALIGNMENT
- `artifacts`: 점검 리포트

---

## AGENDA_LOG 출력

- `status`: PASS
- `summary`: 단계별 결과 요약
- `next`: 종료 또는 다음 작업
- `artifacts`: AGENDA_LOG 기록 시각/라인

---

## 공통 규칙

모든 단계는 아래 4필드를 반드시 포함:
- `status`
- `why`
- `next`
- `artifacts`
