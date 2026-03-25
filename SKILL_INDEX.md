# 스킬 목록 (SKILL INDEX)

이 파일은 `Jarvis_Workspace` 내의 에이전트들이 공용으로 호출할 수 있는 함수형 작업(스킬) 목록과 경로를 정의합니다.
에이전트는 정체성(`AGENT`)을 유지한 채, 특정 반복 작업이 필요할 때 해당 스킬 파일(`SKILLS/*.md`)의 절차를 따릅니다.

## 등록된 스킬 목록 (Registered Skills)
> [!NOTE]
> *현재 등록된 기본 스킬 템플릿입니다. 필요시 복사/수정하여 `SKILLS/` 폴더에 새 스킬을 생성하세요.*

### 1. 심층 검색 (Deep Research)
- **파일**: `SKILLS/skill_research.md`
- **목적**: 특정 키워드나 주제에 대해 로컬 IVK 문서 및 외부 웹을 조회하여, 3단락 이내의 팩트 요약본을 생성.
- **입출력**: `주제(Input) -> 요약 및 출처(Output)`

### 2. 코드/문서 리뷰 (Review & Audit)
- **파일**: `SKILLS/skill_review.md`
- **목적**: 대상 파일(코드/문서)을 읽고, 버그, 비효율성, 오타, 규칙(`POLICY.md`) 위반을 잡아내어 보고서 작성.
- **입출력**: `대상 파일 경로(Input) -> 취약점 레포트(Output)`

### 3. 세션 요약 (Summarize Session)
- **파일**: `SKILLS/skill_summarize.md`
- **목적**: 현재까지 진행된 대화 및 조치 내역을 압축하여 `CAPSULES/` 폴더에 인수인계용 메모로 보관.
- **입출력**: `대화 로그(Input) -> 캡슐 파일(Output)`

### 4. 보안 체크리스트 (Security Checklist)
- **파일**: `SKILLS/security_checklist.md`
- **목적**: 외부 입력, 실행 계획, 최종 출력물을 빠르게 점검해 보안 위험을 판정하고 적절한 조치를 제안.
- **입출력**: `점검 단계 + 대상(Input) -> 판정 및 권장 조치(Output)`

### 5. 범위 잠금 (Scope Lock)
- **파일**: `SKILLS/skill_scope_lock.md`
- **목적**: 현재 요청의 범위를 한 문장 단위로 잠그고, 세션 팽창을 막음.
- **입출력**: `현재 요청(Input) -> bounded_scope 및 out_of_scope(Output)`

### 6. 라우트 잠금 (Route Lock)
- **파일**: `SKILLS/skill_route_lock.md`
- **목적**: 첫 경로와 첫 검토면을 고정해, 요청을 어디서 다룰지 빨리 결정.
- **입출력**: `현재 요청(Input) -> first_route 및 first_review_surface(Output)`

### 7. 게이트 판정 (Gate Judgment)
- **파일**: `SKILLS/skill_gate_judgment.md`
- **목적**: 진행 가능 여부를 `ALLOW | WARN | HOLD | BLOCK | ESCALATE`로 짧게 판정.
- **입출력**: `판정 대상(Input) -> judgment 및 next_action(Output)`

### 8. 근거 패키지 (Evidence Pack)
- **파일**: `SKILLS/skill_evidence_pack.md`
- **목적**: 리서치 결과를 근거 경로와 불확실성을 가진 bounded evidence return으로 정리.
- **입출력**: `조사 주제(Input) -> claims, evidence_paths, uncertainty(Output)`

### 9. 패치 형태 유지 (Patch Shape)
- **파일**: `SKILLS/skill_patch_shape.md`
- **목적**: 코딩 결과를 작은 패치형 산출로 유지하여 과도한 완성품 드리프트를 줄임.
- **입출력**: `수정 목표(Input) -> intended_file_location, patch_intent, implementation_slice(Output)`

### 10. 브리프→초안 (Brief To Draft)
- **파일**: `SKILLS/skill_brief_to_draft.md`
- **목적**: 짧은 브리프를 빠르게 실제 사용 가능한 단일 초안으로 전환.
- **입출력**: `브리프(Input) -> tone_lock 및 draft(Output)`

*(추가 스킬이 개발되면 여기에 인덱싱하세요)*
