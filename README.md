# Jarvis Starter Pack (Prebuilt Edition)

이 폴더는 **이미 구성된 스타터 팩**입니다.  
폴더를 열고 에이전트에게 읽히면 바로 작업을 시작할 수 있으며, 스크립트 기능을 쓰려면 로컬에 Python 3 실행 환경이 필요합니다.

## 빠른 시작 (1분)
1. `START_HERE.md`를 먼저 읽으세요.
2. 환경별 호환이 필요하면 `PATCH_GUIDE_ANTIGRAVITY_CODEX_v1.0.md`를 적용하세요.
3. 작업은 `TASKS/`, `CAPSULES/`, `LOGS/` 레이어에서만 진행하세요.

## 이 팩의 성격
- 목적: 범용 자비스 워크스페이스의 즉시 사용
- 상태: 프리빌트(Prebuilt) / 문서 즉시 사용 가능 / 스크립트는 Python 3 필요
- 원칙: 코어는 유지하고, 환경 패치는 레이어로 추가

## 폴더 개요
- `00_Core`: 정체성/코어 스펙
- `01_Modules`: 모듈 명세
  - 선택 모듈: `01_Modules/Persona_Agent_Starter/` (글쓰기 페르소나 구성)
  - 선택 모듈: `01_Modules/Codex_Agent_Starter/` (Codex 환경에서 선택적으로 역할 분화형 에이전트를 붙이고, `AGENTS.md` 및 `.codex/config.toml` 표면을 분리해 설명하는 경량 애드온)
  - 선택 모듈: `01_Modules/Madang_Pan_Lite_Starter/` (전면 대화 라우터/브리핑 경량판)
  - 선택 모듈: `01_Modules/Project_Workspace_Lite_Starter/` (프로젝트 작업장 시작 레일)
  - 선택 모듈: `01_Modules/Learning_Loop_Lite_Starter/` (세션 종료 학습/승격 후보 기록)
- `02_Protocols`: 운영 프로토콜
- `03_Memory`: 메모리 구현
- `04_Knowledge`: 지식/검색
- `05_Scripts`: 보조 스크립트
- `AGENTS`, `SKILLS`, `TASKS`, `CAPSULES`, `LOGS`: 작업 레이어

## 선택형 운영 문서
- `TASKS/JARVIS_STARTER_ORCHESTRATION_METHOD_v0.1.md`: 메인 세션과 프로젝트 오케스트레이션 세션을 어떻게 나눠 쓰는지 설명하는 방법론
- `TASKS/SEMI_AUTO_PRESET_v0.1.md`: 완전 자동이 아닌 반자동 운영 개념 프리셋
- `TASKS/BROWSER_USAGE_POLICY_v0.1.md`: 브라우저 사용을 필수 기능이 아닌 선택형 보조 능력으로 설명하는 정책 문서
- `TASKS/SESSION_LOGGING_GUIDE_v0.1.md`: `TASKS`, `CAPSULES`, `LOGS`를 언제 어떻게 남기는지 설명하는 생산 안내
- `TASKS/SESSION_CARD_GUIDE_v0.1.md`: 여러 세션을 병행할 때 세션 정체성을 어떻게 고정하는지 설명하는 가이드
- `TASKS/PUBLIC_AGENT_FIT_GUIDE_v0.1.md`: 어떤 작업에 어떤 공개형 에이전트 형식이 맞는지 정리한 적합도 가이드
- `TASKS/PUBLIC_AGENT_SKILL_BUNDLES_v0.1.md`: 공개형 에이전트 카드와 스킬을 어떤 묶음으로 읽어야 하는지 정리한 번들 가이드
- `TASKS/PUBLIC_AGENT_BUNDLE_SESSION_SAMPLES_v0.1.md`: 세션 카드와 함께 읽는 공개형 번들 샘플
- `TASKS/PUBLIC_AGENT_RECIPE_v0.1.md`: 공개형 일반 에이전트 카드를 어떻게 만드는지 정리한 제작 레시피
- `TASKS/PUBLIC_AILO_E_AGENT_RECIPE_v0.1.md`: 공개형 AILO-E 에이전트를 언제 어떻게 만드는지 정리한 제작 레시피
- `TASKS/PUBLIC_SKILL_RECIPE_v0.1.md`: 공개형 스킬 카드를 어떻게 만드는지 정리한 제작 레시피

## 환경 호환
- Antigravity: `.agent` 레이어 패치 권장
- Codex: `AGENTS.md` 레이어 패치 권장
- 둘 다 사용 가능 (코어 공통, 패치 레이어만 추가)

## 실행 전제
- 문서/프로토콜 기반 사용: 추가 설치 없이 가능
- Python 스크립트 사용: `python` 또는 `py -3` 실행 가능 환경 필요
- 대표 스크립트:
  - `03_Memory/Jarvis_Memory.py`
  - `04_Knowledge/IVK2_Improved/run_ivk2.bat`
  - `05_Scripts/AGENDA_Flow_Template.ps1`

## 핵심 규칙
1. 코어(`00_Core~05_Scripts`)를 작업 중 임의 수정하지 마세요.
2. 임시 산출물은 작업 레이어에만 남기세요.
3. 문제가 생기면 코어 수정보다 패치 레이어부터 점검하세요.
4. 공개형 에이전트 카드는 가능하면 대응 스킬과 번들 단위로 함께 읽으세요.

## 시작 파일
- `START_HERE.md`
- `MAP.md`
- `POLICY.md`
- `PATCH_GUIDE_ANTIGRAVITY_CODEX_v1.0.md`
