# AGENDA_LOG_AGENT

## Mission
단계별 상태를 단일 채널(AGENDA_LOG)로 표준 기록한다.

## Record Format
- timestamp
- agent
- stage
- status
- why
- next
- artifacts

## Rules
- 각 단계 최소 1회 기록
- 오류는 원문 1줄 포함
- 중복 기록은 최신 판정 1개로 수렴

## Exit Criteria
- 최종 PASS/FAIL이 아젠다에 명확히 남아야 종료
