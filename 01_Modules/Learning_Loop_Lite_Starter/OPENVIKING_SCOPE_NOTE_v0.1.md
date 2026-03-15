# OpenViking Scope Note for Ailo Starter v0.1

목적:
- `Ailo Starter`에 `OpenViking`을 얼마나 가져올지 범위를 최소한으로 고정한다.

참고 원본:
- GitHub: `https://github.com/volcengine/OpenViking`

판정:
- 스타터는 `가볍게 바로 읽히는 것`이 우선이다.
- 따라서 `OpenViking`의 전체 런타임이나 컨텍스트 DB 구조를 넣지 않는다.
- 대신 `학습 루프 Lite`와 맞닿는 최소 아이디어만 흡수한다.

## 스타터에 가져올 것

### 1. L0 / L1 / L2 사고방식
- `L0`: 이번 세션 핵심 한 줄
- `L1`: 세션 캡슐 요약
- `L2`: 원문 로그나 상세 작업물

스타터 해석:
- `L0`: 세션 종료 시 짧은 결론
- `L1`: `CAPSULES\CAPSULE_TEMPLATE.md`
- `L2`: `TASKS`, `LOGS`, 원문 작업 파일

### 2. Session Commit 관점
- 세션 종료 시 핵심 변화만 남긴다.
- 스타터에서는 이를 `SESSION_CLOSE_PROTOCOL` + `CAPSULE` 작성으로 처리한다.

## 스타터에 가져오지 않을 것

1. 별도 컨텍스트 DB
2. 임베딩/모델 의존
3. 자동 메모리 승격 엔진
4. 전면적인 자원 URI 체계

## 운영 규칙

1. 스타터는 `세션 종료 -> 캡슐 작성 -> 필요 시 승격 후보 기록`까지만 한다.
2. `OpenViking`은 이 흐름의 철학적 참고처일 뿐, 스타터 기본 런타임이 아니다.
3. 나중에 상위 시스템이 필요해지면 그때 별도 확장한다.

## 결론

- `Ailo Starter`는 `OpenViking`에서 `계층형 요약`과 `session commit 사고방식`만 흡수한다.
- 나머지는 의도적으로 넣지 않는다.
