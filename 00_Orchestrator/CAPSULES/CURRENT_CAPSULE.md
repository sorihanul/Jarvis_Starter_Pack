# Current Orchestrator Capsule

## 목적

이 캡슐은 `부팅해` 이후 메인 오케스트레이터가 이어받을 최소 상태만 제공한다.

이 파일은 변경 이력이 아니다.
현재 재진입에 필요한 짧은 인계 상태만 남긴다.

## 현재 상태

- status: `initial_ready`
- active_user_task: `none`
- latest_session_log: `none`
- active_capsule_scope: `initial_orchestrator_state`

## 런타임 표면

- main_brain: `00_Orchestrator/Jarvis_Main_Brain`
- local_rulebook: `00_Orchestrator/LOCAL_RULEBOOK.md`
- memory_map: `00_Orchestrator/MEMORY_MAP.md`
- session_card: `00_Orchestrator/SESSION_CARD.md`
- current_task: `00_Orchestrator/TASKS/CURRENT_TASK.md`
- session_log: `00_Orchestrator/LOGS/SESSION_OPS_LOG.md`
- current_capsule: `00_Orchestrator/CAPSULES/CURRENT_CAPSULE.md`
- source_pack: `01_Source_Pack`

## 기본 규칙

- `01_Source_Pack`은 원천소스다. 현재 작업 폴더로 쓰지 않는다.
- 현재 사용자 작업은 `00_Orchestrator/TASKS`, `00_Orchestrator/LOGS`, `00_Orchestrator/CAPSULES`에 둔다.
- 원천소스를 열기 전에는 `Jarvis_Main_Brain/SOURCE_USAGE_RULE.md`를 확인한다.
- 옵션팩이 필요해 보이면 `01_Source_Pack/06_Option_Packs/OPTION_PACK_ROUTER.md`를 먼저 본다.
- 여러 옵션팩이 필요하면 `01_Source_Pack/06_Option_Packs/OPTION_PACK_COMPOSITION_FLOW.md`로 순서를 잡는다.
- 대화 원문 전체를 기억으로 저장하지 않는다.
- 다시 쓸 결정, 규칙, 사용법, 실패 기준만 Canon Memory 후보가 될 수 있다.
- 이 캡슐은 짧게 유지한다. 자세한 세션 이력은 `LOGS/SESSION_OPS_LOG.md`로 보낸다.

## 다음 행동

사용자가 `부팅해`로 시작하면:

1. `Jarvis_Main_Brain/BOOT.md`를 읽는다.
2. 현재 요청을 확인한다.
3. 아래 중 하나로 분기한다.
   - 직접 처리
   - 브레인 제작
   - 프로젝트 작업장
   - 정보 수집
   - 리뷰 또는 검증
4. 해당 분기에 필요한 원천소스만 연다.
5. 현재 작업 흔적은 오케스트레이터 작업 표면에 남기고 `01_Source_Pack`에는 남기지 않는다.
