# Source Usage Rule v0.1

## 목적

`01_Source_Pack`을 어떻게 참고할지 정한다.

## 원천소스 정의

`01_Source_Pack`은 자비스 스타터의 원천소스다.

여기에는 기존 코어, 모듈, 프로토콜, 메모리, 스크립트, 에이전트, 스킬, 작업 문서가 들어 있다.

## 사용 원칙

- 필요한 파일만 읽는다.
- 원천소스를 작업 로그 저장소로 쓰지 않는다.
- 새 브레인과 프로젝트 산출물은 원천소스 밖에 둔다.
- 원천소스의 문서를 복제하기보다 필요한 규칙과 구조를 새 브레인에 맞게 재구성한다.
- 원천소스 변경이 필요하면 별도 유지보수 작업으로 분리한다.

## 작업면 분리

- `../../01_Source_Pack/TASKS`는 원천소스 안의 작업 참고면이다.
- `../../01_Source_Pack/LOGS`는 원천소스 안의 기록 참고면이다.
- `../../01_Source_Pack/CAPSULES`는 원천소스 안의 인수인계 참고면이다.
- 현재 오케스트레이터 작업은 `../TASKS`에 둔다.
- 현재 오케스트레이터 기록은 `../LOGS`에 둔다.
- 현재 오케스트레이터 인수인계 요약은 `../CAPSULES`에 둔다.
- 새 브레인 제작 요청은 `../TASKS/BRAIN_BUILD_REQUESTS`에 둔다.
- 프로젝트 오케스트레이션 요청은 `../TASKS/PROJECT_REQUESTS`에 둔다.

## 기본 읽기 후보

- `../../01_Source_Pack/START_HERE.md`
- `../../01_Source_Pack/MAP.md`
- `../../01_Source_Pack/POLICY.md`
- `../../01_Source_Pack/01_Modules/`
- `../../01_Source_Pack/AGENTS/`
- `../../01_Source_Pack/SKILLS/`
- `../../01_Source_Pack/TASKS/`
- `../../01_Source_Pack/04_Knowledge/`
- `../../01_Source_Pack/06_Option_Packs/`

## 선택 모듈 참고

- 지식 접근, 검색, IVK 계열 참고가 필요하면 `../../01_Source_Pack/04_Knowledge/`를 후보로 본다.
- 외부 자료 분석, 신뢰 정보 수집, 온톨로지 구조화, 검증, 메모리 접근 경로, 메모리/프로필, 외부자료 방어, 스킬 신뢰 검사, 행동 권한, 경험의 스킬화, 맥락 압축, 외부 채널 정규화가 필요하면 `../../01_Source_Pack/06_Option_Packs/`를 후보로 본다.
- 옵션팩이 필요해 보이면 먼저 `../../01_Source_Pack/06_Option_Packs/OPTION_PACK_ROUTER.md`를 읽고 1~3개 팩만 고른다.
- 옵션팩은 기본 부팅 때 모두 읽지 않고, 현재 요청과 직접 맞는 팩만 읽는다.

## 에이전트와 서브에이전트 참고

에이전트 카드 제작, 역할 분리, Codex 서브에이전트 운용이 필요하면 아래를 후보로 본다.

- `../../01_Source_Pack/AGENT_INDEX.md`
- `../../01_Source_Pack/TASKS/PUBLIC_AGENT_RECIPE_v0.1.md`
- `../../01_Source_Pack/TASKS/PUBLIC_AILO_E_AGENT_RECIPE_v0.1.md`
- `../../01_Source_Pack/TASKS/PUBLIC_AGENT_FIT_GUIDE_v0.1.md`
- `../../01_Source_Pack/TASKS/PUBLIC_AGENT_SKILL_BUNDLES_v0.1.md`
- `../../01_Source_Pack/01_Modules/Codex_Agent_Starter/README.md`
- `../../01_Source_Pack/01_Modules/Codex_Agent_Starter/10_CODEX_AGENT_UTILIZATION_v0.1.md`
- `../../01_Source_Pack/01_Modules/Codex_Agent_Starter/20_SUBAGENT_BRIEF_TEMPLATE_v0.1.md`
- `../../01_Source_Pack/01_Modules/Codex_Agent_Starter/30_CODEX_FILE_SURFACE_GUIDE_v0.1.md`

이 목록은 기본 부팅 대상이 아니다.
요청이 에이전트 제작, 역할 분리, 서브에이전트 위임, Codex 역할 파일 작성과 직접 관련될 때만 읽는다.
실제 Codex custom agent 정의를 만들 때는 `.codex/agents/*.toml` 형식을 우선 후보로 본다.

## 읽기 제한

- 모든 모듈을 한 번에 읽지 않는다.
- 현재 요청과 무관한 로그와 캡슐을 읽지 않는다.
- 원천소스 내부의 오래된 실험 기록을 공식 규칙처럼 쓰지 않는다.
- 원천소스의 `TASKS`, `LOGS`, `CAPSULES`를 현재 작업면으로 해석하지 않는다.

## 새 자산 제작 시

새 브레인, 에이전트, 스킬을 만들 때는 다음 순서를 따른다.

1. 목표와 사용자를 확인한다.
2. 필요한 원천소스 후보를 고른다.
3. 실제로 읽을 파일 수를 줄인다.
4. 새 자산의 경계와 금지를 정한다.
5. 새 폴더나 문서를 만든다.
6. 새 스레드 시작 문구를 제공한다.
