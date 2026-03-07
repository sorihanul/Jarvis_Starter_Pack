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

*(추가 스킬이 개발되면 여기에 인덱싱하세요)*
