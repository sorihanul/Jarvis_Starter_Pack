# Session Logging Guide v0.1

이 문서는 `Jarvis Starter Pack`에서 세션 흔적을 어디에 남겨야 하는지 설명한다.

핵심 원칙:
- 사소한 대화까지 전부 로그로 만들지 않는다.
- 작업 중간의 원시 흔적은 `LOGS/`에 남긴다.
- 끝난 세션의 압축된 교훈은 `CAPSULES/`에 남긴다.
- 아직 진행 중인 안건과 다음 행동은 `TASKS/`에 남긴다.
- 세션 정체성 자체는 `세션 카드`로 먼저 고정하고, 로그는 그 뒤에 남긴다.

## 1. 무엇을 어디에 남기는가

1. `TASKS/`
- 현재 진행 중인 안건
- 프로젝트 오케스트레이션 설계
- 다음 액션
- 운영 방법론 문서

2. `LOGS/`
- 원시 실행 흔적
- 실패 기록
- 검증 결과 원본
- 보안 경고
- 오케스트레이션 세션 진행 기록

3. `CAPSULES/`
- 세션 종료 요약
- 핵심 결정
- 재사용 가능한 교훈
- 다음에 참고할 압축된 패턴

## 2. 메인 세션과 프로젝트 세션 차이

1. 메인 세션
- 스타터 설계, 모듈 정리, 공개판 판단을 다룬다.
- 긴 실행 로그보다는 `TASKS/` 문서와 필요한 최소 `CAPSULES/` 중심이 맞다.

2. 프로젝트 오케스트레이션 세션
- 프로젝트 목적, roster, phase, 산출 흐름을 설계한다.
- 진행 중 판단 흔적과 실행 관련 메모는 `LOGS/`에 남기는 편이 좋다.
- 종료 시 압축본은 `CAPSULES/`로 옮긴다.

## 2A. 세션 카드와의 차이

- `세션 카드`는 이 세션이 누구인지 정한다.
- `로그`는 이 세션에서 어떤 일이 있었는지 남긴다.
- 둘을 같은 문서로 섞지 않는 편이 좋다.

## 3. 언제 로그를 만들지 말아야 하는가

- 단순 질의응답 한 번
- 구조 설명만 듣고 끝난 세션
- 반복 가치가 거의 없는 짧은 잡담
- 코어 문서 읽기만 하고 아무 판단도 남기지 않은 경우

## 4. 최소 생산 흐름

1. 작업 시작
- 필요하면 `TASKS/SESSION_CARD_TEMPLATE_v0.1.md` 기준으로 세션 카드를 먼저 만든다.
- 현재 안건은 `TASKS/`에 둔다.

2. 작업 중
- 원시 메모, 실패 흔적, 검증 흔적은 `LOGS/`에 둔다.

3. 작업 종료
- 핵심 결정과 교훈만 `CAPSULES/`에 압축한다.

4. 승격 후보 발견
- 재사용 가치가 있으면 `TASKS/PROMOTION_CANDIDATE_TEMPLATE.md` 기준으로 후보를 남긴다.

## 5. 최소 템플릿

### LOGS

```md
# Session Log

- date:
- session type: main | orchestration | task
- focus:
- key actions:
- failures or warnings:
- next step:
```

### CAPSULES

```md
# Capsule

- scope:
- final decision:
- what worked:
- what failed:
- reusable lesson:
```

## 결론

`Jarvis Starter`에서 로그는 많이 남기는 것이 목적이 아니다. `원시 흔적은 LOGS`, `진행 안건은 TASKS`, `압축된 교훈은 CAPSULES`로 분리해 남기는 것이 목적이다.
