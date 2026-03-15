# TASKS/PROJECTS

이 폴더는 프로젝트형 작업의 정식 위치다.

규칙:
- 각 프로젝트는 `TASKS/PROJECTS/<project_id>/`에 둔다.
- 작은 프로젝트도 최소한 아래 4문서로 시작한다.
  - `BOOT_ENTRY.md`
  - `MISSION.md`
  - `ROADMAP.md`
  - `ORCHESTRATOR.md`
- 팀 분화가 필요할 때만 `TRACK` 문서를 추가한다.

빠른 시작:
1. `TASKS/PROJECTS/_TEMPLATES/`의 파일을 복사한다.
2. 새 폴더 `TASKS/PROJECTS/<project_id>/`를 만든다.
3. `BOOT_ENTRY.md`, `MISSION.md`, `ROADMAP.md`, `ORCHESTRATOR.md`를 채운다.

예:
- `TASKS/PROJECTS/my_first_project/`

주의:
- 프로젝트 내용은 `TASKS` 레이어 안에만 둔다.
- `00_Core`나 `01_Modules`에 작업 산출물을 누적하지 않는다.
