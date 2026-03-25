# 1. 목적 (Purpose)
요청을 가장 먼저 어디로 보낼지와, 어떤 검토면을 먼저 읽을지를 고정합니다.

# 2. 입력 (Input)
- `현재 요청`
- (선택사항) `bounded_scope`
- (선택사항) `관련 세션 카드 또는 프로젝트 문서`

# 3. 절차 (Procedure)
1. 요청 신호를 `basic | research | writing | coding | project_orchestration | security_gate_first` 중 하나 또는 최우선 하나로 분류합니다.
2. 혼합 신호가 있으면 작업형 신호보다 게이트/오케스트레이션 신호를 우선합니다.
3. 첫 검토면을 `security_gate | validation | policy_or_review | orchestration_method | approval_or_policy` 중 하나로 잠급니다.
4. 라우팅 근거를 한 줄로 요약합니다.

# 4. 출력 (Output)
- **first_route**: [첫 경로]
- **first_review_surface**: [첫 검토면]
- **reason**: [이 경로를 고른 이유]

# 5. 실패 처리 (Fallback)
- **신호 충돌**: 둘 이상이 강하게 충돌하면 더 상위의 게이트/오케스트레이션 경로를 우선 잠그고 이유를 남깁니다.
