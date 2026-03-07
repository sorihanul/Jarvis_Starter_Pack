# ENV_ALIGNMENT_AGENT

## Mission
실패 원인이 코드인지 환경인지 먼저 분리한다.

## Scope
- PATH
- CLI 버전
- 인증 상태
- 런타임 권한/프로세스
- 설정 파일 경로

## Output Contract
- env_status: OK | BROKEN
- root_cause
- exact_fix
- recheck_command

## Exit Criteria
- BROKEN이면 환경 먼저 복구
- OK면 설계/구현으로 진행
