# START HERE: Jarvis Agent Workspace

환영합니다. 이 워크스페이스는 `00_Core/JARVIS_FOLDER_RECIPE_v1.0.md` 기준을 따르는 독립적인 자비스 시스템(AILO-H)입니다.

## 🧭 시작하기
어떤 작업을 수행하든, 에이전트(자비스)는 아래의 흐름을 따릅니다.

1. **MAP.md 참조**: 시스템 전체의 폴더 구조와 파일 역할을 파악합니다.
2. **Identity Layer 숙지**: 본인이 어떻게 판단하고 행동해야 하는지 결정하기 위해 `00_Core/` 내의 핵심 스펙 문서와 `POLICY.md`를 읽습니다.
3. **AGENT_INDEX.md 확인**: 본인에게 부여된 특정 역할(페르소나)과 사용 가능한 스킬(`SKILL_INDEX.md`)을 로드하여 세션 목적에 맞게 세팅합니다.
4. **Task 실행**: 현재 할당된 `TASKS/` 폴더 안의 이슈를 바탕으로 작업을 수행합니다. 작업 기록과 산출물은 `CAPSULES/`나 `LOGS/`에 보관됩니다.

### 선택 로드
초기 대화 진입을 더 안정적으로 하고 싶다면 아래 모듈을 추가로 읽습니다.
- `01_Modules/Madang_Pan_Lite_Starter/README.md`
- 프로젝트형 작업을 별도 작업장으로 정렬하고 싶다면 `01_Modules/Project_Workspace_Lite_Starter/README.md`
- 세션 종료 후 교훈과 승격 후보를 남기고 싶다면 `01_Modules/Learning_Loop_Lite_Starter/README.md`
- 메인 세션과 프로젝트 오케스트레이션 세션의 분리 원칙을 보고 싶다면 `TASKS/JARVIS_STARTER_ORCHESTRATION_METHOD_v0.1.md`
- 브라우저 사용 가능 범위를 알고 싶다면 `TASKS/BROWSER_USAGE_POLICY_v0.1.md`

`01_Modules/Madang_Pan_Lite_Starter/`는:
- 요청 분류
- 짧은 진입 브리핑
- 단일 현재 단계 유지
를 위한 경량 전면 라우터입니다.

프로젝트형 작업은 메인 세션에서 길게 끌기보다, 별도 오케스트레이션 세션을 열어 `TASKS/PROJECTS/` 작업장을 기준으로 진행하는 것을 권장합니다.

> [!IMPORTANT]
> 자비스 운영의 대원칙: **"정체성(Identity)과 작업(Task)은 완전히 분리된다."** 
> 
> 작업의 내용이나 논의, 단순 스니펫 코드는 절대 `00_Core`나 `01_Modules` 계층에 누적하지 않으며, 오직 `TASKS/`, `CAPSULES/`, `LOGS/`의 변동 레이어에만 일시적/영구적으로 기록하십시오.

## 🔧 환경 패치 안내
- Antigravity/Codex 호환 레이어는 아래 문서를 따른다.
- `PATCH_GUIDE_ANTIGRAVITY_CODEX_v1.0.md`

## 경로 원칙
- 이 스타터 팩 내부 문서 경로는 모두 현재 저장소 루트를 기준으로 한 상대경로를 우선합니다.
- 예: `04_Knowledge/IVK2_Improved/run_ivk2.bat`
