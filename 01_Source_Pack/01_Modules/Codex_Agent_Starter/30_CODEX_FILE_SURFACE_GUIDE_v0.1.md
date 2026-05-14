# Codex File Surface Guide v0.1

이 문서는 `Jarvis Starter` 문서와 `Codex` 로컬 설정 파일의 표면을 분리해서 설명한다.

## 핵심 구분

1. `Jarvis Starter` 문서 표면
- 확장자: `.md`
- 역할: 작업 규칙, 오케스트레이션 방식, 브리프, 템플릿
- 예: `START_HERE.md`, `AGENTS.md`, `TASKS/...`

2. `Codex` 로컬 설정 표면
- 확장자: `.toml`
- 역할: Codex 실행 설정, 로컬 역할 정의, 멀티에이전트 파라미터
- 예: `.codex/config.toml`, `.codex/agents/*.toml`

즉 `자비스는 문서로 설명`하고, `Codex는 설정으로 호출`한다.

## 권장 배치

1. 저장소 루트 또는 프로젝트 루트
- `AGENTS.md`
- 필요 시 `AGENTS.override.md`

2. 로컬 설정 폴더
- `.codex/config.toml`

3. 자비스 스타터 내부 참고 모듈
- `01_Modules/Codex_Agent_Starter/`

## 권장 운용

1. 먼저 `AGENTS.md`로 프로젝트 규칙을 정한다.
2. 그 다음 `.codex/config.toml`에서 로컬 역할과 실행 폭을 조정한다.
3. 큰 작업은 별도 오케스트레이션 세션에서 roster를 설계한다.
4. 메인 세션은 항상 통합과 최종 판단을 유지한다.

## 주의

- `AGENTS.md`는 Codex가 읽는 작업 지침 파일이다.
- `.codex/config.toml`은 Codex가 읽는 로컬 설정 파일이다.
- `.codex/agents/*.toml`은 Codex가 읽는 custom agent 파일이다.
- 둘은 목적이 다르므로 하나로 합치지 않는 편이 안전하다.
- 스타터는 예시를 제공하지만, 실제 `.codex/config.toml`은 사용자의 로컬 환경에서 관리하는 편이 좋다.

## 표준 역할 파일 원칙

- 프로젝트 지침은 `MD`여도 된다.
- 그러나 실제 Codex 표준 역할 파일은 `MD`가 아니라 `TOML`로 두는 편이 맞다.
- 공개용 기본 예시는 `.codex/agents/*.toml.example`처럼 standalone custom agent 파일로 제공하는 편이 가장 이해하기 쉽다.
- `roles/*.toml`은 로컬에서 수동 조합하거나 참고할 수 있는 fragment 예시다.
- 이 fragment 방식은 Codex 공개 문서의 기본 표면은 아니므로, 프로젝트별로 직접 조정해서 쓰는 편이 안전하다.
- 따라서 이 모듈은 두 표면을 함께 제공한다.
  - 공식 표면: `.codex/agents/*.toml.example`
  - 고급 표면: `roles/*.toml`
