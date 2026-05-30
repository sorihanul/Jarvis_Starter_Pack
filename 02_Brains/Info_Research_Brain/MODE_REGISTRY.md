# Mode Registry

## `quick_brief`

짧은 조사 답변이 필요할 때 사용한다.

## `deep_research`

여러 출처를 비교하고 근거표가 필요할 때 사용한다.

## `local_folder_scan`

로컬 폴더, 문서 묶음, 저장소를 먼저 읽어야 할 때 사용한다.

## `source_audit`

출처의 신뢰도, 주장, 누락, 위험을 검토할 때 사용한다.

## `comparison`

여러 대상의 차이, 장단점, 선택 기준을 비교할 때 사용한다.

## `decision_brief`

사용자의 선택이나 실행 전 판단을 돕는 보고서를 만들 때 사용한다.

## `route_builder`

큰 자료 묶음에서 먼저 읽을 경로를 잡을 때 사용한다.

## `conflict_check`

출처 간 주장이 충돌할 때 날짜, 버전, 권위, 문맥을 나눠 본다.

## `freshness_check`

최신성이 중요한 정보의 현재 확인 필요성을 판단한다.

## `memory_candidate`

조사 중 반복 재사용할 출처, 기준, 경로가 생겼을 때 사용한다.

## 선택 규칙

- 단순 질문은 `quick_brief`를 쓴다.
- 로컬 경로가 있으면 `local_folder_scan`을 먼저 쓴다.
- 신뢰도 판단이 중요하면 `source_audit`을 붙인다.
- 선택이 목적이면 `decision_brief`를 쓴다.
- 자료가 크면 `route_builder`로 시작한다.
- 출처가 충돌하면 `conflict_check`를 붙인다.
- 최신성이나 고위험성이 있으면 `freshness_check`를 붙인다.
