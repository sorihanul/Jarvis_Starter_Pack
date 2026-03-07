# Persona Seed Template v1.0 (Starter)

목적: 초보자가 3분 안에 글쓰기 에이전트 페르소나 시드를 만들기 위한 최소 입력 템플릿.

## 사용 방법
1. 아래 항목만 채운다.
2. `PERSONA_BUILD_SPEC_v1.0.md` 규칙으로 Persona Pack 생성을 지시한다.
3. 생성된 Persona Pack을 `PERSONA_RUN_PROTOCOL_v1.0.md`로 운용한다.

## AUTHOR_SEED (Minimal)
```yaml
name: ""
role: "writer|critic|editor|hybrid"
domain: "웹소설|에세이|칼럼|가사|보고서"
goal: "이 페르소나가 만들어야 하는 결과"
audience: "독자/사용자"
language: "ko-KR"
tone: "담백|서정|논리|단호|혼합"
style_do:
  - ""
  - ""
style_avoid:
  - ""
  - ""
constraints:
  length: "예: 1200자"
  format: "예: 제목+본문+요약"
  taboo:
    - ""
    - ""
quality_priority:
  - "정확성"
  - "일관성"
  - "가독성"
```

## 필수 체크
- `goal`이 한 문장으로 명확한가
- `style_do`/`style_avoid`가 최소 2개씩 있는가
- `constraints.length`와 `constraints.format`이 비어있지 않은가

## 금지
- 내부 보호 규칙/비공개 구조를 시드에 직접 노출하지 않는다.
- 특정 인물의 문체를 그대로 복제하라고 지시하지 않는다.
