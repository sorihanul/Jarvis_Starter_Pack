# Codex Agent Starter

이 모듈은 `Jarvis Starter Pack`을 **Codex 환경에서 에이전트/서브에이전트 활용까지 포함해 운용하는 방법**만 담당하는 경량 애드온이다.

목적:
- `Jarvis Starter` 본체는 모델 독립으로 유지한다.
- `Codex`의 에이전트 기능은 **호환 레이어**로만 붙인다.
- 단일 세션 응답과 역할 분화형 서브에이전트 운용의 경계를 분명히 한다.

이 모듈이 하는 일:
1. 언제 서브에이전트를 써야 하는지 기준 제시
2. 어떤 역할로 쪼개야 하는지 기본 패턴 제공
3. 서브에이전트에게 넘길 브리프 템플릿 제공
4. `AGENTS.md` 계열 문서와 `.codex/config.toml` 계열 설정의 차이 설명
5. Codex 운영 가이드를 자비스 스타터 문서 체계 안에 맞춰 설명

이 모듈이 하지 않는 일:
- `Jarvis Starter` 본체 정체성 변경
- Codex 전용 본체화
- 무제한 병렬 멀티에이전트 기본화
- 실제 Codex 커스텀 에이전트 설정 파일을 대신 생성

읽기 순서:
1. `10_CODEX_AGENT_UTILIZATION_v0.1.md`
2. `20_SUBAGENT_BRIEF_TEMPLATE_v0.1.md`
3. `30_CODEX_FILE_SURFACE_GUIDE_v0.1.md`
4. `40_CODEX_PROJECT_AGENTS_TEMPLATE_v0.1.md`
5. `50_CODEX_LOCAL_CONFIG_TEMPLATE_v0.1.toml.example`
6. `60_CODEX_STANDARD_ROLES_v0.1.md`
7. `.codex/agents/*.toml.example`

핵심 원칙:
- 본체는 `START_HERE.md`, `MAP.md`, `POLICY.md`, `00_Core/`가 유지한다.
- Codex 에이전트 기능은 작업 환경 확장일 뿐, 정체성 레이어가 아니다.
- 작은 작업은 단일 세션으로 끝내고, 분업 이득이 있을 때만 서브에이전트를 연다.
- Codex의 프로젝트 지침은 `AGENTS.md` 또는 `AGENTS.override.md` 계열로 읽힌다.
- Codex의 로컬 역할/실행 설정은 `.codex/config.toml` 계열에서 관리한다.
- 자비스 문서와 Codex 로컬 설정은 같은 것이 아니며, 표면을 분리해 두는 편이 안전하다.
- 표준 역할 카드는 설명용 `MD`가 아니라 실제 Codex 역할 설정으로 연결 가능한 `TOML` 파일로 두는 편이 맞다.
- 공개용 예시는 두 층으로 제공한다.
  - `.codex/agents/*.toml.example`: 공식 custom agent 방식
  - `roles/*.toml`: 로컬에서 참고하거나 수동 변환할 수 있는 fragment 예시
