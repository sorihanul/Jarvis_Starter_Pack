# REENTRY CANON v1.2

## 목적

실패 시 무한 반복을 막고, 항상 같은 회귀 경로로 재진입한다.

---

## 실패 분류

- `ENV_FAIL`: PATH/인증/버전/프로세스 문제
- `SPEC_FAIL`: 요구사항/범위/가정 문제
- `IMPLEMENT_FAIL`: 코드/명령 실행 실패
- `INSPECT_FAIL`: 회귀/품질 미달

---

## 회귀 규칙

1. `ENV_FAIL` 발생
   - 즉시 `ENV_ALIGNMENT`으로 회귀
2. `SPEC_FAIL` 발생
   - `DESIGN`으로 회귀 후 `VALIDATION` 재실행
3. `IMPLEMENT_FAIL` 발생
   - 먼저 `ENV_ALIGNMENT` 확인 후 `IMPLEMENTATION` 재시도
4. `INSPECT_FAIL` 발생
   - `ENV_ALIGNMENT -> IMPLEMENTATION -> INSPECTION` 순으로 재진입

---

## 반복 제한

- 동일 실패코드 3회 반복 시 자동 중단
- 중단 시 `AGENDA_LOG`에 `HUMAN_DECISION_REQUIRED` 기록

---

## 종료 조건

- `INSPECTION=PASS` + `AGENDA_LOG` 최종 전파 완료

---

## 한 줄 원칙

실패를 바로 구현 반복으로 몰지 말고, 먼저 환경/설계 원인을 분리한 뒤 재진입한다.
