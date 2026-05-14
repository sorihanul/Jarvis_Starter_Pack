# Orchestrator Tasks

이 폴더는 `Jarvis_Main_Brain`의 현재 작업면이다.

## 역할

- `CURRENT_TASK.md`: 현재 세션의 작업 상태
- `BRAIN_BUILD_REQUESTS/`: 새 브레인 제작 요청
- `PROJECT_REQUESTS/`: 프로젝트 오케스트레이션 요청

## 원칙

- 현재 오케스트레이터 작업은 여기에서 관리한다.
- `01_Source_Pack/TASKS`는 원천소스 참고면으로만 읽는다.
- 요청이 커지면 `BRAIN_BUILD_REQUESTS` 또는 `PROJECT_REQUESTS`로 분리한다.
