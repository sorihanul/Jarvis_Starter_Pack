# Obsidian Runtime Surface Lite Starter

이 모듈은 `Obsidian`을 자비스 스타터의 **선택형 보기면**으로 붙이는 방법을 설명한다.
즉, 본체 기능이 아니라 필요할 때만 얹는 옵션 문서다.

핵심 정의:
- Obsidian은 브레인이 아니다
- Obsidian은 에이전트 시스템을 대체하지 않는다
- Obsidian은 사람이 지식층을 읽고 탐색하고 검토하는 운영 표면이다

이 모듈이 다루는 것:
1. `raw / wiki / schema` 3층 분리
2. `index.md`, `log.md` 같은 얇은 탐색 표면
3. ingest / query / lint 루프
4. 인간과 LLM의 역할 분리
5. git-backed knowledge repo 감각

이 모듈이 전제하지 않는 것:
- Obsidian 필수 설치
- 스타터 본체 구조 변경
- 기존 `TASKS/`, `CAPSULES/`, `LOGS/` 운용 대체
- 이 저장소 안에 바로 `vault/`를 생성해야 한다는 강제

권장 읽기 순서:
1. `10_OBSIDIAN_RUNTIME_SURFACE_v0.1.md`

이 모듈은 옵션이다.
- Obsidian이 없어도 스타터는 그대로 쓸 수 있다
- 지식층이 커져서 눈으로 확인할 표면이 필요할 때만 붙인다
- 먼저 문서 개념을 읽고, 실제 vault 구조나 규칙 파일은 필요할 때 별도로 만든다

## 독립 운용

이 모듈은 특정 외부 문서를 다시 열어야만 이해되는 구조가 아니다.
필요한 정의와 사용 경계는 이 폴더 안에 둔다.
