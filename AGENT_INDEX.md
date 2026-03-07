# 에이전트 목록 (AGENT INDEX)

이 파일은 `Jarvis_Workspace` 내에서 활용 가능한 페르소나(에이전트) 목록과 각 파일 경로를 정의합니다.
시스템(자비스)은 현재 안건(`TASKS/`)에 가장 적합한 에이전트 파일을 로드하여 그 역할에 빙의합니다.

## 시스템 기본 에이전트 (System Default)
사용자가 특별히 페르소나를 지정하지 않으면, 자비스는 기본적으로 `00_Core`의 AILO-H 엔진 규칙을 기반으로 범용적인 비서 역할을 수행합니다.

## 등록된 에이전트 목록 (Registered Agents)
> [!NOTE]
> *현재 등록된 기본 에이전트 템플릿입니다. 필요시 복사/수정하여 `AGENTS/` 폴더에 새 에이전트를 생성하세요.*

### 1. 리서처 (Research Agent)
- **파일**: `AGENTS/agent_research.md`
- **역할**: 방대한 지식을 검색하고(Local/Web), 팩트를 수집하여 파편화된 정보를 체계적으로 정리합니다.
- **주요 스킬**: `skill_research.md`, `skill_summarize.md`

### 2. 크리틱 (Critic Agent)
- **파일**: `AGENTS/agent_critic.md`
- **역할**: 작성된 코드, 기획서, 논리 구조의 허점을 찾고, `POLICY.md` 및 보안 제약 위반 여부를 검열합니다.
- **주요 스킬**: `skill_review.md`

*(추가 에이전트가 개발되면 여기에 인덱싱하세요)*
