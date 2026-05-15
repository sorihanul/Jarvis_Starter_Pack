# Memory Map

## 목적

이 문서는 `00_Orchestrator`가 무엇을 기억 표면으로 보고, 무엇을 원천소스로만 보는지 구분한다.

메모리는 한곳에 모두 쌓는 저장소가 아니다. 다시 읽을 파일의 역할을 나눈 표면 묶음이다.

## Identity Memory

오케스트레이터의 정체성과 작업 방식이다.

- `Jarvis_Main_Brain/BRAIN.md`
- `Jarvis_Main_Brain/AILO_INTENT_LAYER.md`
- `Jarvis_Main_Brain/MODE_REGISTRY.md`
- `Jarvis_Main_Brain/BRAIN_BUILD_PROTOCOL.md`
- `Jarvis_Main_Brain/SOURCE_USAGE_RULE.md`

## Route Memory

처음 어디를 읽을지 정하는 길찾기 표면이다.

- `../START_HERE.md`
- `../MAP.md`
- `../BOOT.md`
- `Jarvis_Main_Brain/BOOT.md`
- `LOCAL_RULEBOOK.md`
- `MEMORY_MAP.md`

## Session Memory

현재 부팅 상태와 진행 흔적이다.

- `SESSION_CARD.md`
- `TASKS/CURRENT_TASK.md`
- `LOGS/SESSION_OPS_LOG.md`
- `CAPSULES/CURRENT_CAPSULE.md`

## Source Memory

필요할 때만 여는 원천소스다.

- `../01_Source_Pack/START_HERE.md`
- `../01_Source_Pack/MAP.md`
- `../01_Source_Pack/POLICY.md`
- `../01_Source_Pack/00_Core/`
- `../01_Source_Pack/01_Modules/`
- `../01_Source_Pack/02_Protocols/`
- `../01_Source_Pack/03_Memory/`
- `../01_Source_Pack/AGENTS/`
- `../01_Source_Pack/SKILLS/`

## Agent Route Memory

에이전트 카드 제작, 역할 분리, Codex 서브에이전트 운용이 필요할 때만 여는 경로다.

- `../01_Source_Pack/AGENT_INDEX.md`
- `../01_Source_Pack/TASKS/PUBLIC_AGENT_RECIPE_v0.1.md`
- `../01_Source_Pack/TASKS/PUBLIC_AILO_E_AGENT_RECIPE_v0.1.md`
- `../01_Source_Pack/TASKS/PUBLIC_AGENT_FIT_GUIDE_v0.1.md`
- `../01_Source_Pack/TASKS/PUBLIC_AGENT_SKILL_BUNDLES_v0.1.md`
- `../01_Source_Pack/01_Modules/Codex_Agent_Starter/README.md`
- `../01_Source_Pack/01_Modules/Codex_Agent_Starter/10_CODEX_AGENT_UTILIZATION_v0.1.md`
- `../01_Source_Pack/01_Modules/Codex_Agent_Starter/20_SUBAGENT_BRIEF_TEMPLATE_v0.1.md`
- `../01_Source_Pack/01_Modules/Codex_Agent_Starter/30_CODEX_FILE_SURFACE_GUIDE_v0.1.md`

## Do Not Read By Default

아래는 기본 부팅 때 읽지 않는다.

- `../01_Source_Pack/TASKS/`
- `../01_Source_Pack/LOGS/`
- `../01_Source_Pack/CAPSULES/`
- `../01_Source_Pack/05_Scripts/`
- `Agent Route Memory` 전체
- 오래된 테스트 산출물

## 읽기 원칙

- 부팅 때는 route, session, identity만 얇게 읽는다.
- 작업 요청을 받은 뒤 필요한 source만 연다.
- 현재 작업 기록은 source memory에 남기지 않는다.
- 산출물은 다시 읽을 사람이 원천소스 전체를 몰라도 이해되게 만든다.
