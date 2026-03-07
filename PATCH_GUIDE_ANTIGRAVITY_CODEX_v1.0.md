# PATCH GUIDE v1.0 (Antigravity + Codex)

## 목적
- 현재 `Jarvis_Starter_Pack` 구조는 유지한다.
- 실행 환경별 호환 레이어만 덧붙인다.
- 원본 코어(`00_Core~05_Scripts`)는 건드리지 않는다.

## 공통 원칙
1. 정본은 현재 워크스페이스 파일이다.
2. 패치는 "추가" 중심으로만 적용한다.
3. 실패 시 패치 레이어만 제거하면 원복된다.

## A) Antigravity 패치 (권장)
Antigravity는 `.agent` 관례를 쓰므로, 아래 레이어를 추가한다.

### A-1. 추가 구조
```text
Jarvis_Starter_Pack/
  .agent/
    agents/
      agent_research.md
      agent_critic.md
    skills/
      skill_research.md
      skill_review.md
      skill_summarize.md
    README.md
```

### A-2. 매핑 규칙
- `AGENTS/*.md` -> `.agent/agents/*.md` 복제
- `SKILLS/*.md` -> `.agent/skills/*.md` 복제
- `AGENT_INDEX.md`, `SKILL_INDEX.md`는 그대로 유지(사람/시스템 안내용)

### A-3. 운영 지시 예시
- "이 폴더의 `.agent` 레이어를 우선 읽고, 부족하면 `00_Core`를 참조해."

## B) Codex 패치 (권장)
Codex는 프로젝트 규칙 문서 우선이다.

### B-1. 추가 구조
```text
Jarvis_Starter_Pack/
  AGENTS.md
```

### B-2. AGENTS.md 최소 규칙
- First read order:
  1) `START_HERE.md`
  2) `MAP.md`
  3) `POLICY.md`
  4) `00_Core/한글 AILO-H Full-Stack v0.91 — Unified Core Specification.md`
- Task writes only to: `TASKS/`, `CAPSULES/`, `LOGS/`
- Do not mutate core files without explicit approval.

### B-3. 운영 지시 예시
- "AGENTS.md 규칙을 따르고, 이번 작업 산출은 `TASKS`와 `CAPSULES`에만 남겨."

## C) 패치 우선순위
1. Antigravity만 쓸 때: `.agent` 패치만 적용
2. Codex만 쓸 때: `AGENTS.md` 패치만 적용
3. 둘 다 쓸 때: 둘 다 적용 (코어는 동일, 레이어만 이중화)

## D) 점검 체크리스트
- [ ] `AGENTS/`와 `SKILLS/` 파일 존재
- [ ] `.agent` 레이어(선택) 존재
- [ ] `AGENTS.md`(선택) 존재
- [ ] 코어 파일(`00_Core~05_Scripts`) 무변경

## 결론
- 현재 스타터는 이미 범용 운용 가능하다.
- 이 패치는 "환경 호환성"을 보강하는 옵션이다.
- 핵심은 구조 변경이 아니라 진입 레이어 추가다.
