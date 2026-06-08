# AI Work Route Lite v0.1

**Document class:** Public-safe lightweight workflow card  
**Purpose:** Help an AI task move through visible steps, checks, stop conditions, and a clear completion level.  
**Scope:** Workflow organization only. This is not a hidden reasoning request, runtime, memory system, security system, or proof of correctness.

---

## 0. Core Idea

```text
Do not ask the AI to simply "finish."
Define the visible work route and the level of evidence behind the result.
```

Simple Korean:

```text
AI에게 그냥 끝내라고 하지 말고,
작업 단계와 확인 기준, 중단 조건, 완료 주장 수준을 정한다.
```

---

## 1. Use When

Use this card when:

```text
- the task has multiple stages
- missing one stage would cause bad output
- the result needs checking
- the work may look complete without really being complete
- the final answer needs a clear evidence level
```

Skip it for simple, reversible, low-risk tasks.

---

## 2. Basic Template

```text
WorkRoute {
  purpose: "",
  target: "",
  steps: [],
  checks: [],
  stop_if: [],
  output: "",
  completion_level: ""
}
```

---

## 3. Completion Levels

Use conservative labels.

```text
draft_only:
  written but not checked

structure_checked:
  file or document structure was checked

source_checked:
  sources were read and separated from interpretation

tool_checked:
  a relevant tool, command, or test was run

runtime_checked:
  behavior was checked in a running environment

release_ready:
  ready only after required checks pass and remaining risks are acceptable
```

Rules:

```text
- Do not call a draft verified.
- Do not call a structure check runtime proof.
- Do not call a tool run successful if it failed.
- Do not hide skipped checks.
- Do not treat a report as the same thing as a working result.
```

---

## 4. Example: Research

```text
WorkRoute.Research {
  purpose: "answer from sources without overstating certainty",
  target: "question or claim",
  steps: [
    "lock the question",
    "read sources",
    "separate source statements from interpretation",
    "hold conflicts instead of merging them",
    "summarize what is known and unknown"
  ],
  checks: [
    "source exists",
    "date or freshness is noted when relevant",
    "unsupported claims are marked"
  ],
  stop_if: [
    "required source is unavailable",
    "freshness matters but current data was not checked"
  ],
  output: "short answer with evidence and uncertainty",
  completion_level: "source_checked"
}
```

---

## 5. Example: Coding

```text
WorkRoute.Coding {
  purpose: "make a code change that actually works",
  target: "repo, bug, feature, or patch",
  steps: [
    "read project rules",
    "lock the goal",
    "define scope",
    "plan a small change",
    "edit",
    "run the relevant check",
    "interpret failures",
    "report changed files and remaining risk"
  ],
  checks: [
    "no unrelated large refactor",
    "no hardcoded sample-only solution",
    "no silent fallback masking failure",
    "test/build/check result is reported honestly"
  ],
  stop_if: [
    "destructive command is required",
    "security risk appears",
    "the required change crosses the agreed scope"
  ],
  output: "changed files, check result, remaining risk",
  completion_level: "tool_checked"
}
```

---

## 6. Example: Verification

```text
WorkRoute.Verification {
  purpose: "say what is proven and what is not",
  target: "artifact, claim, patch, or release candidate",
  steps: [
    "lock target",
    "define success criteria",
    "list evidence",
    "run or inspect checks",
    "separate findings by severity",
    "assign completion level",
    "name one next action"
  ],
  checks: [
    "condition and result are separate",
    "static evidence is not called runtime evidence",
    "skipped checks are reported"
  ],
  stop_if: [
    "target is unclear",
    "success criteria are missing"
  ],
  output: "findings, evidence level, next action",
  completion_level: "structure_checked"
}
```

---

## 7. One-Line Rule

```text
For complex AI tasks, define visible steps, required checks, stop conditions, output, and completion level before claiming the work is done.
```

---

END OF AI WORK ROUTE LITE v0.1
