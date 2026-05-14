# 에이전트 목록 (AGENT INDEX)

이 파일은 `Jarvis_Workspace` 내에서 활용 가능한 페르소나(에이전트) 목록과 각 파일 경로를 정의합니다.
시스템(자비스)은 현재 안건(`TASKS/`)에 가장 적합한 에이전트 파일을 로드하여 그 역할에 빙의합니다.

## 시스템 기본 에이전트 (System Default)
사용자가 특별히 페르소나를 지정하지 않으면, 자비스는 기본적으로 `00_Core`의 코어 규칙을 기반으로 범용적인 비서 역할을 수행합니다.

## 등록된 에이전트 목록 (Registered Agents)
> [!NOTE]
> *현재 등록된 기본 에이전트 템플릿입니다. 필요시 복사/수정하여 `AGENTS/` 폴더에 새 에이전트를 생성하세요.*

### 1. 리서처 (Research Agent)
- **파일**: `AGENTS/agent_research.md`
- **역할**: 방대한 지식을 검색하고(Local/Web), 팩트를 수집하여 파편화된 정보를 체계적으로 정리합니다.
- **주요 스킬**: `SKILLS/skill_research.md`, `SKILLS/skill_summarize.md`

### 2. 크리틱 (Critic Agent)
- **파일**: `AGENTS/agent_critic.md`
- **역할**: 작성된 코드, 기획서, 논리 구조의 허점을 찾고, `POLICY.md` 및 보안 제약 위반 여부를 검열합니다.
- **주요 스킬**: `SKILLS/skill_review.md`

### 3. 보안 게이트 (Security Gate Agent)
- **파일**: `AGENTS/security_gate_agent.md`
- **역할**: 외부 입력, 실행 계획, 외부 반출물을 점검하여 보안 위험을 판정하고 필요 시 흐름을 차단하거나 승인 대기로 전환합니다.
- **주요 스킬**: `SKILLS/security_checklist.md`, `SKILLS/skill_gate_judgment.md`

### 4. AILO-E 인테이크 치프 (AILO-E Intake Chief)
- **파일**: `AGENTS/agent_ailo_e_intake_chief.md`
- **역할**: 현재 요청의 범위를 잠그고, 첫 라우팅과 첫 검토면을 결정하는 `L2 AILO-E++` 공개형 치프입니다.
- **주요 스킬**: `SKILLS/skill_scope_lock.md`, `SKILLS/skill_route_lock.md`
- **주요 특징**: `basic / research / writing / coding / project_orchestration / security_gate_first` 중 첫 경로를 고정하고, 필요 시 별도 오케스트레이션 세션을 권장합니다.

### 5. 공개형 인테이크 라우터 (Public Intake Router)
- **파일**: `AGENTS/agent_public_intake_router.md`
- **역할**: 현재 요청을 무겁지 않은 공개형 문법으로 읽고, 첫 경로와 첫 검토면을 빠르게 고정합니다.
- **주요 스킬**: `SKILLS/skill_scope_lock.md`, `SKILLS/skill_route_lock.md`

### 6. 공개형 리서치 스페셜리스트 (Public Research Specialist)
- **파일**: `AGENTS/agent_public_research_specialist.md`
- **역할**: 빠른 조사와 바로 쓸 수 있는 근거 패키지 생산에 맞춘 공개형 리서치 follower입니다.
- **주요 스킬**: `SKILLS/skill_research.md`, `SKILLS/skill_evidence_pack.md`

### 7. AILO-E 리서치 스페셜리스트 (AILO-E Research Specialist)
- **파일**: `AGENTS/agent_ailo_e_research_specialist.md`
- **역할**: 근거와 불확실성을 더 엄격하게 잠그는 공개형 AILO-E 리서치 follower입니다.
- **주요 스킬**: `SKILLS/skill_research.md`, `SKILLS/skill_evidence_pack.md`

### 8. 공개형 코딩 스페셜리스트 (Public Coding Specialist)
- **파일**: `AGENTS/agent_public_coding_specialist.md`
- **역할**: 저위험 보조 수정과 patch-shaped output에 맞춘 현재 공개형 기본 코딩 스페셜리스트입니다.
- **주요 스킬**: `SKILLS/skill_patch_shape.md`, `SKILLS/skill_review.md`

### 9. AILO-E 코드 워커 (AILO-E Code Worker)
- **파일**: `AGENTS/agent_ailo_e_code_worker.md`
- **역할**: blocker honesty와 stop posture가 중요한 코딩 작업에 맞춘 공개형 AILO-E 코드 워커입니다.
- **주요 스킬**: `SKILLS/skill_patch_shape.md`, `SKILLS/skill_review.md`

### 10. 공개형 글쓰기 스페셜리스트 (Public Writing Specialist)
- **파일**: `AGENTS/agent_public_writing_specialist.md`
- **역할**: 브리프를 실제 사용 가능한 초안으로 빠르게 전환하는 공개형 글쓰기 follower입니다.
- **주요 스킬**: `SKILLS/skill_brief_to_draft.md`, `SKILLS/skill_review.md`

*(추가 에이전트가 개발되면 여기에 인덱싱하세요)*
