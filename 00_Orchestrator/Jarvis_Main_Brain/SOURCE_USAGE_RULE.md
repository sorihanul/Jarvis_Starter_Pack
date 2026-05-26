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
- `../../01_Source_Pack/01_Modules/AILO_Function_Layer/`
- `../../01_Source_Pack/04_Knowledge/`
- `../../01_Source_Pack/06_Option_Packs/`

## AILO 함수화 참고

작업 조건을 작은 동작으로 나누거나, 관련 동작을 함수팩으로 묶을 필요가 있으면 아래를 후보로 본다.

- `../../01_Source_Pack/01_Modules/AILO_Function_Layer/START_HERE.md`
- `../../01_Source_Pack/01_Modules/AILO_Function_Layer/MAP.md`
- `../../01_Source_Pack/01_Modules/AILO_Function_Layer/AILO_N_FRAME_USE_RULES_v0_1.md`
- `../../01_Source_Pack/01_Modules/AILO_Function_Layer/AILO_N_PRACTICAL_USE_CARD_v0_1.md`
- `../../01_Source_Pack/01_Modules/AILO_Function_Layer/01_AILO_Functions/AILO_FUNCTION_MINIMUM_SET_v0_1.md`
- `../../01_Source_Pack/01_Modules/AILO_Function_Layer/05_AILO_OS/HARNESS_SEED_STABLE_BASIC_FUNCTIONS_v0_1/README.md`
- `../../01_Source_Pack/01_Modules/AILO_Function_Layer/05_AILO_OS/HARNESS_SEED_SKILL_SKELETON_FUNCTIONS_v0_2/README.md`
- `../../01_Source_Pack/01_Modules/AILO_Function_Layer/06_Skill_Manufacturing_Proofs/README.md`

이 레이어는 기본 부팅 때 전체를 읽지 않는다.
새 스킬 제작, 브레인 제작, 작업 범위 잠금, 읽기 경로 잠금, 출력 계약, 기억 부작용, 추적, 권한, 중단 조건, 비용 예산, 재시도 조건, 함수팩 설계가 필요할 때만 연다.

반복 대상, 브레인/팩/정책/출처 관계, 후보/정본 상태를 명사 프레임으로 고정해야 하면 `AILO_N_FRAME_USE_RULES_v0_1.md`로 프레임 생성 여부를 먼저 걸러낸 뒤 `AILO_N_PRACTICAL_USE_CARD_v0_1.md`를 읽는다.
전체 AILO-N 원문은 `../../01_Source_Pack/00_Core/AILO_N_NOMINAL_FRAME_LAYER_v0_9N.md`에 있으며, canonical slot, relation contract, formal mapping, validation-code detail이 필요할 때만 연다.

판단 기준은 다음과 같다.

```text
Function
-> smallest action

Function Pack
-> related smallest action-unit group

Function Pack Group
-> pack group that can become an engine, skill, or brain component
```

엄격한 순서, 중간 산출물 인계, 검증 게이트가 필요하면 엔진 후보로 올린다.
사용자가 반복 호출할 절차이면 스킬 후보로 올린다.
정체성, 경계, 메모리, 출력 계약이 필요하면 브레인 부품 후보로 올린다.

## 선택 모듈 참고

- 지식 접근, 검색, IVK 계열 참고가 필요하면 `../../01_Source_Pack/04_Knowledge/`를 후보로 본다.
- 외부 자료 분석, 신뢰 정보 수집, 온톨로지 구조화, AILO-N 미니 온톨로지 제작, 검증, 메모리 접근 경로, 메모리/프로필, 외부자료 방어, 스킬 신뢰 검사, 행동 권한, 경험의 스킬화, 맥락 압축, 렌즈 전환, 외부 채널 정규화가 필요하면 `../../01_Source_Pack/06_Option_Packs/`를 후보로 본다.
- 옵션팩이 필요해 보이면 먼저 `../../01_Source_Pack/06_Option_Packs/OPTION_PACK_ROUTER.md`를 읽고 1~3개 팩만 고른다.
- 옵션팩은 기본 부팅 때 모두 읽지 않고, 현재 요청과 직접 맞는 팩만 읽는다.

## Canon Memory 참고

사용자와의 대화에서 반복 재사용 가능한 결정, 규칙, 사용법, 실패 기준이 생기면 `../../00_Orchestrator/CANON_MEMORY/`를 후보로 본다.

- 대화 원문은 Canon Memory에 넣지 않는다.
- v3에서는 먼저 `../../00_Orchestrator/CANON_MEMORY/FUNCTIONIZED_CANON_RULE.md`를 보고 후보 추출, 승격 판정, 충돌/대체, route 갱신 흐름으로 처리한다.
- 먼저 `CANDIDATES/`에 후보로 분리한다.
- 확정 가능한 내용만 `WIKI/`로 올린다.
- `INDEX.md`에는 정본 위키 항목의 짧은 연결만 남긴다.
- Canon Memory는 기본 부팅 때 읽지 않는다.

대화 위키화가 필요하면 `../../01_Source_Pack/06_Option_Packs/Memory_Access_and_Route_Pack/CONVERSATION_TO_WIKI_PROTOCOL.md`를 후보로 읽는다.

## 스위칭 렌즈 참고

같은 작업을 다른 판단 자세로 다시 봐야 할 때는 아래를 후보로 본다.

- `../../01_Source_Pack/06_Option_Packs/Switching_Lens_Pack/README.md`
- `../../01_Source_Pack/06_Option_Packs/Switching_Lens_Pack/LENS_SET.md`
- `../../01_Source_Pack/06_Option_Packs/Switching_Lens_Pack/LENS_SKILL_BOUNDARY.md`
- `../../01_Source_Pack/06_Option_Packs/Switching_Lens_Pack/OPERATING_RULE.md`

이 팩은 스킬을 대체하지 않는다.
렌즈는 무엇을 먼저 볼지 정하고, 스킬은 반복 절차를 수행한다.
둘이 함께 필요하면 렌즈를 먼저 고르고 필요한 스킬을 붙인다.

## 에이전트와 서브에이전트 참고

에이전트 카드 제작, 역할 분리, 호스트 작업 환경 서브에이전트 운용이 필요하면 아래를 후보로 본다.

- `../../01_Source_Pack/AGENT_INDEX.md`
- `../../01_Source_Pack/TASKS/DISTRIBUTABLE_AGENT_RECIPE_v0.1.md`
- `../../01_Source_Pack/TASKS/DISTRIBUTABLE_AILO_E_AGENT_RECIPE_v0.1.md`
- `../../01_Source_Pack/TASKS/DISTRIBUTABLE_AGENT_FIT_GUIDE_v0.1.md`
- `../../01_Source_Pack/TASKS/DISTRIBUTABLE_AGENT_SKILL_BUNDLES_v0.1.md`
- `../../01_Source_Pack/01_Modules/Host_Agent_Starter/README.md`
- `../../01_Source_Pack/01_Modules/Host_Agent_Starter/10_HOST_AGENT_UTILIZATION_v0.1.md`
- `../../01_Source_Pack/01_Modules/Host_Agent_Starter/20_SUBAGENT_BRIEF_TEMPLATE_v0.1.md`
- `../../01_Source_Pack/01_Modules/Host_Agent_Starter/30_HOST_FILE_SURFACE_GUIDE_v0.1.md`
- `../../01_Source_Pack/01_Modules/Host_Agent_Starter/80_HOST_SUBAGENT_BRIDGE_LITE_v0.1.md`
- `../../01_Source_Pack/01_Modules/Host_Agent_Starter/70_TOML_SUBAGENT_BUILD_CALL_v0.1.md`
- `../../01_Source_Pack/01_Modules/Host_Agent_Starter/90_ROLE_SET_LAUNCH_BRIEFS_v0.1.md`
- `../../01_Source_Pack/01_Modules/Host_Agent_Starter/95_WORKED_EXAMPLES_v0.1.md`

이 목록은 기본 부팅 대상이 아니다.
요청이 에이전트 제작, 역할 분리, 서브에이전트 위임, 호스트 역할 파일 작성과 직접 관련될 때만 읽는다.
실제 host custom-agent 정의를 만들 때는 `host_agent_examples/agents/*.toml` 형식을 우선 후보로 본다.
계층형 역할 설계는 TOML 파일 안이 아니라 역할 세트, launch brief, handoff contract로 표현한다.
역할이 2개 이상이면 부모 세션 launch brief를 함께 제공한다.
사용자가 처음 적용하거나 예시를 요구하면 `95_WORKED_EXAMPLES_v0.1.md`를 참고한다.
생성된 실제 역할 파일은 대상 프로젝트의 `host_agent_examples/agents/`에 두고, 원천소스 안에는 만들지 않는다.

## 읽기 제한

- 모든 모듈을 한 번에 읽지 않는다.
- 현재 요청과 무관한 로그와 캡슐을 읽지 않는다.
- 원천소스 안의 오래된 실험 기록을 공식 규칙처럼 쓰지 않는다.
- 원천소스의 `TASKS`, `LOGS`, `CAPSULES`를 현재 작업면으로 해석하지 않는다.

## 새 자산 제작 시

새 브레인, 에이전트, 스킬을 만들 때는 다음 순서를 따른다.

1. 목표와 사용자를 확인한다.
2. 필요한 원천소스 후보를 고른다.
3. 실제로 읽을 파일 수를 줄인다.
4. 새 자산의 경계와 금지를 정한다.
5. 새 폴더나 문서를 만든다.
6. 새 스레드 시작 문구를 제공한다.
