# 1. 목적 (Purpose)
진행 가능 여부를 짧고 명확한 판정으로 반환하여, 흐름을 열거나 멈추거나 상위 승인으로 넘깁니다.

# 2. 입력 (Input)
- `판정 대상`
- `판정 맥락`
- (선택사항) `제약 또는 금지 조건`

# 3. 절차 (Procedure)
1. 판정 대상이 무엇인지 확인합니다.
2. 아래 라벨 중 하나를 선택합니다.
   - `ALLOW`
   - `WARN`
   - `HOLD`
   - `BLOCK`
   - `ESCALATE`
3. 라벨 선택 근거를 1~3개로 줄입니다.
4. 다음 행동을 한 줄로 제시합니다.

# 4. 출력 (Output)
- **judgment**: [ALLOW|WARN|HOLD|BLOCK|ESCALATE]
- **reason**: [핵심 근거]
- **next_action**: [다음 행동]

# 5. 실패 처리 (Fallback)
- **근거 부족**: 위험 또는 허용을 확정하기 어렵다면 억지로 확정하지 말고 `ESCALATE`를 반환합니다.
