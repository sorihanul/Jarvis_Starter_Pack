# POSSESSION ROUTER v1.2

## 목적

요청 유형에 따라 순차 빙의 대상을 자동으로 결정한다.
한 번에 한 Agent만 활성화하는 원칙을 유지한다.

---

## 입력

- `task_type`: bugfix | feature | refactor | infra | security | docs
- `risk_level`: low | medium | high
- `change_scope`: file | module | system

---

## 라우팅 규칙 (기본)

1. 모든 작업은 `ENV_ALIGNMENT`으로 시작
2. 이후 `DESIGN -> VALIDATION` 고정
3. `VALIDATION=APPROVE`일 때만 `IMPLEMENTATION`
4. `IMPLEMENTATION` 이후 `INSPECTION` 고정
5. 종료 전 `AGENDA_LOG` 고정

---

## 라우팅 보강 (조건)

- `risk_level=high` 또는 `task_type=security`
  - `VALIDATION` 단계에서 보안 점검 항목 확장
- `change_scope=system`
  - `INSPECTION`에서 회귀 점검 항목 확장
- `docs` 단독 작업
  - `IMPLEMENTATION` 최소화, `INSPECTION`은 정합성 중심

---

## 출력 계약

- `active_agent`
- `reason`
- `next_agent`
- `gate_status`

---

## 한 줄 원칙

라우터는 실행 순서를 줄이거나 바꾸는 도구가 아니라, 누락 없이 순차 빙의를 보장하는 도구다.
