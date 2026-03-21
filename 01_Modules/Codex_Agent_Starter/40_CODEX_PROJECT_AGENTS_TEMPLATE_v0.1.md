# Codex Project AGENTS Template v0.1

이 파일은 `Codex`에서 읽히는 프로젝트 지침 템플릿이다.

실사용할 때는 이 문서를 참고해 저장소 루트의 `AGENTS.md` 또는 프로젝트 전용 `AGENTS.override.md`로 다시 두는 것을 권장한다.

## 템플릿

```md
# AGENTS.md

## Jarvis Starter Codex Rules

- Read `START_HERE.md`, `MAP.md`, and `POLICY.md` before substantial work.
- Treat `00_Core/` through `05_Scripts/` as protected by default.
- Leave working outputs in `TASKS/`, `CAPSULES/`, and `LOGS/`.
- Keep the main session as the final integrator.
- Use sub-agents only when role split clearly improves quality or speed.
- Prefer a separate orchestration session for large project work.

## Default Role Split

- `research`: read docs, inspect structure, return facts and paths
- `implementation`: make bounded changes with clear file ownership
- `validation`: verify behavior, tests, and remaining risks
- `synthesis`: combine results into the final user-facing report

## Do Not

- Do not hand off core identity decisions to sub-agents.
- Do not let sub-agents edit protected core paths casually.
- Do not open sub-agents for trivial work.
- Do not treat parallelism itself as the goal.
```

## 프로젝트 전용 오버라이드 예시

```md
# AGENTS.override.md

## Project Orchestration Rules

- This project uses a separate orchestration session before implementation.
- Confirm the role roster before opening parallel sub-agents.
- Keep validation read-only unless the main session explicitly reassigns it.
```
