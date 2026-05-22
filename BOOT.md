# BOOT

## 기본 부팅

이 저장소에서 사용자가 아래처럼 말하면 메인 문서형 하네스를 읽고 작업 자세를 맞춘다.

```text
부팅해.
```

## 먼저 읽을 파일

읽을 파일:

1. `START_HERE.md`
2. `MAP.md`
3. `00_Orchestrator/Jarvis_Main_Brain/BOOT.md`
4. `00_Orchestrator/LOCAL_RULEBOOK.md`
5. `00_Orchestrator/MEMORY_MAP.md`
6. `00_Orchestrator/SESSION_CARD.md`
7. `00_Orchestrator/TASKS/CURRENT_TASK.md`
8. `00_Orchestrator/Jarvis_Main_Brain/BRAIN.md`
9. `00_Orchestrator/Jarvis_Main_Brain/AILO_INTENT_LAYER.md`
10. `00_Orchestrator/Jarvis_Main_Brain/AILO_FUNCTION_LAYER.md`
11. `00_Orchestrator/Jarvis_Main_Brain/MODE_REGISTRY.md`
12. `00_Orchestrator/Jarvis_Main_Brain/BRAIN_BUILD_PROTOCOL.md`
13. 필요할 때만 `00_Orchestrator/Jarvis_Main_Brain/SOURCE_USAGE_RULE.md`

## 원칙

- `부팅해`는 이 루트에서 메인 문서형 하네스를 먼저 읽으라는 뜻이다.
- `01_Source_Pack`은 필요할 때만 확인한다.
- 모든 원천소스를 한 번에 읽지 않는다.
- 사용자의 자연어 요청은 AILO식 의도 슬롯으로 정리한다.
- v3에서는 의도 슬롯 다음에 필요한 동작을 함수로 나누고, 관련 동작을 함수팩으로 묶어 범위, 경로, 출력, 기억, 추적, 권한, 중단 조건을 먼저 구조화한다.
- 호스트 모델의 실제 능력과 도구 권한에 맞게 작업 구성을 조정한다.
- 현재 작업 기록은 `00_Orchestrator/TASKS`, `LOGS`, `CAPSULES`에 남긴다.
