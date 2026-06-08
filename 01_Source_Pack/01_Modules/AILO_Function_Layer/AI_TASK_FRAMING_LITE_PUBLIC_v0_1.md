# AI Task Framing Lite v0.1

**Document class:** Public-safe lightweight task-framing card  
**Purpose:** Help a user and an AI turn a broad request into a clearer task before work begins.  
**Scope:** Task clarification only. This is not a security system, runtime, memory system, hidden reasoning request, ontology, or proof of correctness.

---

## 0. Core Idea

```text
A command name is only a handle.
A task becomes clear when its purpose, target, context, constraints, and output are clear.
```

Simple Korean:

```text
명령어 이름만으로는 작업 의미가 충분하지 않다.
목적, 대상, 맥락, 제약, 산출물이 분명해야 AI가 덜 빗나간다.
```

---

## 1. Use When

Use this card when:

```text
- the request is broad or ambiguous
- the user knows the goal but not the exact method
- the work may branch into several possible tasks
- the output format matters
- the AI may answer too generally
```

Skip it when the task is simple and obvious.

---

## 2. The 8 Fields

```text
aim:
  why this task exists and what success should look like

target:
  what should be worked on

given:
  what material, context, or assumption is already provided

view:
  what angle or criteria should guide the work

steps:
  visible work order

priority:
  what matters more

limits:
  what to avoid or not change

output:
  expected final form
```

---

## 3. Basic Template

```text
TaskFrame {
  aim: "",
  target: "",
  given: "",
  view: {
    angle: "",
    criteria: []
  },
  steps: [],
  priority: {},
  limits: [],
  output: {
    form: "",
    include: []
  }
}
```

---

## 4. Example

Request:

```text
이 문서 좀 정리해줘.
```

TaskFrame:

```text
TaskFrame {
  aim: "문서를 다시 읽기 쉽게 만든다",
  target: "제공된 문서",
  given: "원문은 유지하되 구조가 흐림",
  view: {
    angle: "실사용 문서 정리",
    criteria: ["핵심 보존", "중복 제거", "읽기 순서 개선"]
  },
  steps: [
    "핵심 주장 확인",
    "중복과 흐름 문제 표시",
    "구조 재배열",
    "남은 애매함 보고"
  ],
  priority: {
    "meaning_preservation": "high",
    "clarity": "high",
    "style_polish": "medium"
  },
  limits: [
    "새 주장을 임의로 추가하지 않기",
    "원문 의도를 바꾸지 않기"
  ],
  output: {
    form: "정리본과 변경 요약",
    include: ["정리본", "주요 변경", "남은 질문"]
  }
}
```

---

## 5. Safety Notes

```text
- The frame guides the task; it does not decide the conclusion.
- Priority is not a truth score.
- Limits are not proof that mistakes cannot happen.
- Output format does not replace evidence or verification.
- If a claim needs evidence, check the evidence separately.
```

---

## 6. One-Line Rule

```text
Before asking AI to do complex work, clarify the aim, target, context, work order, limits, and output.
```

---

END OF AI TASK FRAMING LITE v0.1
