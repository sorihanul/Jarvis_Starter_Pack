# Current Orchestrator Capsule

## 목적

`부팅해`로 시작한 메인 오케스트레이터가 다음 세션에서 바로 이어받을 최소 상태를 제공한다.

## 현재 구조

- live_brain: `00_Orchestrator/Jarvis_Main_Brain`
- local_rulebook: `00_Orchestrator/LOCAL_RULEBOOK.md`
- memory_map: `00_Orchestrator/MEMORY_MAP.md`
- session_card: `00_Orchestrator/SESSION_CARD.md`
- source_pack: `01_Source_Pack`
- live_tasks: `00_Orchestrator/TASKS`
- live_logs: `00_Orchestrator/LOGS`
- live_capsules: `00_Orchestrator/CAPSULES`
- ailo_intent_layer: `00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md`

## 현재 결정

- `01_Source_Pack`은 원천소스다.
- 오케스트레이터의 현재 작업 기록은 `00_Orchestrator` 내부 작업면에 둔다.
- 새 브레인과 프로젝트는 원천소스 밖에 만든다.
- 메인 브레인은 사용자의 자연어 요청을 AILO식 의도 슬롯으로 바꾼 뒤 목적, 범위, 금지, 산출물, 소환문구로 좁혀 코덱스 실행 구조를 만든다.
- 옵션팩이 필요하면 먼저 `01_Source_Pack/06_Option_Packs/OPTION_PACK_ROUTER.md`를 읽고 1~3개만 고른다.
- 복합 요청이면 `01_Source_Pack/06_Option_Packs/OPTION_PACK_COMPOSITION_FLOW.md`로 팩 순서를 잡고, 방어, 수집, 구조화, 실행, 검증 순서를 기본값으로 둔다.
- 패키지를 고친 뒤에는 루트 `ACCEPTANCE_TESTS.md`로 부팅, 원천소스 경계, 옵션팩 선택, 새 브레인 제작, 작업 적치, 공개 위생을 확인한다.

## 다음 행동

- 사용자가 요청하면 `Jarvis_Main_Brain/BOOT.md`를 기준으로 부팅한다.
- 부팅 때 `LOCAL_RULEBOOK.md`, `MEMORY_MAP.md`, `SESSION_CARD.md`, `AILO_INTENT_LAYER.md`를 함께 읽는다.
- 요청 성격에 따라 직접 처리, 브레인 제작, 프로젝트 오케스트레이션으로 분기한다.
- 외부 공개 저장소, 에이전트 시스템, 기술 문서를 자비스 능력으로 바꿀 때는 `01_Source_Pack/06_Option_Packs/Capability_Import_Pack`을 후보로 읽는다.
- 옵션팩이 필요해 보이면 먼저 `01_Source_Pack/06_Option_Packs/OPTION_PACK_ROUTER.md`를 읽고 1~3개 팩만 고른다.
- 복합 옵션팩 흐름이 필요하면 `OPTION_PACK_COMPOSITION_FLOW.md`를 먼저 보고, 완료 전 `Verification_and_Proof_Pack`으로 성공 기준과 남은 리스크를 분리한다.
