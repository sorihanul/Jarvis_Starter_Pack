# Project Workspace Lite Starter

이 모듈은 스타터 팩 안에서 `프로젝트 하나를 어떻게 시작할지`만 담당하는 경량 작업장 모듈이다.

목적:
- 요청을 바로 작업 문서 3종으로 정렬한다.
- 장기 시스템 없이도 프로젝트를 자치적으로 굴리게 한다.
- 필요해질 때만 트랙(설계/보안/검증/디버그)으로 확장한다.
- 공개용 기준에서 프로젝트 문서 위치를 하나로 고정한다.

핵심:
1. `BOOT_ENTRY`
2. `MISSION`
3. `ROADMAP`
4. `ORCHESTRATOR`

권장 사용 순서:
1. `00_PROJECT_WORKSPACE_LITE_OVERVIEW_v0.1.md`
2. `10_BOOT_ENTRY_LITE_v0.1.md`
3. `20_PROJECT_TRIAD_v0.1.md`
4. `30_TRACK_EXPANSION_v0.1.md`
5. `40_PROJECT_TEMPLATES_v0.1.md`

운영 원칙:
- 이 모듈은 `무거운 런타임`이 아니라 `문서형 프로젝트 시작 레일`이다.
- 작은 작업은 `MISSION + ROADMAP + ORCHESTRATOR`만으로 시작한다.
- 프로젝트가 커질 때만 `TRACK`를 추가한다.
- 프로젝트 정식 위치는 `TASKS/PROJECTS/<project_id>/`다.
- 실제 복사용 템플릿은 `TASKS/PROJECTS/_TEMPLATES/`에 둔다.
