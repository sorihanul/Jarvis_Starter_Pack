# AI Work Quality Contract Lite v0.1

**Document class:** Public-safe lightweight work-quality contract

**Purpose:** Help an AI task stay useful, checkable, maintainable, and not more complex than needed.

**Scope:** Work-quality guidance only. This is not a hidden reasoning request, runtime, memory system, security system, benchmark, or proof of model improvement.

---

## 0. Core Idea

```text
Good AI work should fit the goal, stay within scope, show what was checked, avoid unnecessary complexity, and leave a clear next step when needed.
```

Simple Korean:

```text
좋은 AI 작업은 목표에 맞고, 범위를 넘지 않으며, 확인한 것과 확인하지 못한 것을 구분하고, 불필요하게 복잡하지 않아야 한다.
필요하면 다음 사람이 이어받을 수 있어야 한다.
```

---

## 1. Use When

Use this card when:

```text
- the task result will be reused
- the work has several possible routes
- correctness or verification matters
- the user may not know the full technical scope
- the AI may produce a polished-looking but unchecked result
- the task should leave a clear handoff
```

Skip it when the task is simple, low-risk, and already clear.

---

## 2. Quality Contract

```text
WorkQualityContract {
  goal: "",
  scope_in: [],
  scope_out: [],
  success_criteria: [],
  required_checks: [],
  unchecked_items: [],
  complexity_rule: "",
  handoff_target: "",
  stop_rule: "",
  claim_level: ""
}
```

Field meanings:

```text
goal:
  what the work must accomplish

scope_in:
  what is included in this task

scope_out:
  what is explicitly excluded

success_criteria:
  what must be true before the work can be called done

required_checks:
  checks that must pass, with recorded evidence, before completion within the declared scope

unchecked_items:
  what was not checked, could not be checked, or is only assumed

complexity_rule:
  how to keep the work no more complex than necessary

handoff_target:
  what a next worker or later session should receive

stop_rule:
  separate successful completion from a blocked stop or an incomplete handoff

claim_level:
  how strongly the result may be described
```

---

## 3. Default Quality Rules

```text
- Prefer the simplest route that satisfies the goal.
- Do not add structure that does not improve the result.
- Do not call untested work tested.
- Do not call a draft release-ready.
- Do not hide skipped checks.
- Do not expand the task scope without saying so.
- Call the work complete only when its success criteria are met and required checks have passed.
- A skipped, unavailable, or failed required check does not satisfy completion; listing it honestly does not replace verification.
- Repair a failed check within scope and run it again. If work cannot continue, report the incomplete state and the blocker or handoff.
- If the work cannot be completed honestly, name the blocker and the next possible action.
```

---

## 4. Claim Levels

Use conservative labels.

```text
draft:
  created but not checked

reviewed:
  inspected for structure, relevance, or consistency

checked:
  all required checks for the declared scope were performed, passed, and recorded

partially_checked:
  required verification is incomplete or has a failed check; the work is not complete

blocked:
  required material, permission, source, tool, or decision is missing

ready_for_next_step:
  usable for the specified next worker or task, with limits visible; not proof of overall completion
```

Rules:

```text
- Pick the weakest honest label.
- A clean explanation is not the same as proof.
- A passed checklist is only as strong as the checks that were actually done.
- If the result depends on a missing check, mark it as partially_checked or blocked.
- A failed required check cannot be reported as checked or complete.
- Scope matters: checked design documents do not prove runtime behavior, and a ready handoff does not prove a ready release.
```

---

## 5. Small Template

```text
작업 품질 계약:
- 목표:
- 포함:
- 제외:
- 완료 기준:
- 확인할 것:
- 미확인/제한:
- 복잡도 기준:
- 인계 대상:
- 중단 기준:
- 주장 수준:
```

Use the small template only when the task needs it. For simple answers, answer directly.

---

## 6. Example: Coding

```text
WorkQualityContract.Coding {
  goal: "reported issue is fixed with the smallest maintainable change",
  scope_in: ["relevant files", "necessary adjacent context", "targeted check"],
  scope_out: ["unrequested refactor", "format churn", "new architecture"],
  success_criteria: ["required behavior demonstrated", "required checks passed", "change is minimal and within scope"],
  required_checks: ["confirm the reported issue and expected outcome", "verify corrected behavior", "run required targeted regression checks"],
  unchecked_items: ["checks unavailable or not run"],
  complexity_rule: "do not add a larger design unless the small fix cannot work",
  handoff_target: "changed files, check result, remaining risk",
  stop_rule: "complete only when success criteria and required checks pass; otherwise repair and recheck, or report a partial or blocked handoff",
  claim_level: "checked only after required checks pass; otherwise partially_checked or blocked"
}
```

---

## 7. Example: Research

```text
WorkQualityContract.Research {
  goal: "answer from available sources without overstating certainty",
  scope_in: ["question", "available sources", "source date when relevant"],
  scope_out: ["unsupported certainty", "unrequested broad background"],
  success_criteria: ["source statements and interpretation are separated"],
  required_checks: ["source relevance", "freshness if the topic may change"],
  unchecked_items: ["claims not verified in this run"],
  complexity_rule: "do not add more sources than needed to answer the locked question",
  handoff_target: "next source to check or remaining gap",
  stop_rule: "stop when the supported answer and gaps are clear",
  claim_level: "checked or partially_checked"
}
```

---

## 8. Example: Design

```text
WorkQualityContract.Design {
  goal: "produce a reusable design with clear boundary and validation path",
  scope_in: ["system goal", "known constraints", "reuse target", "risks"],
  scope_out: ["runtime proof", "unbounded framework growth", "premature release claim"],
  success_criteria: ["goal, boundary, risk, and next validation are visible"],
  required_checks: ["scope check", "risk check", "claim level check"],
  unchecked_items: ["future integration assumptions", "behavior not tested"],
  complexity_rule: "add structure only when it improves operation, verification, or handoff",
  handoff_target: "next validation or implementation worker",
  stop_rule: "stop when the design is bounded and the next check is defined",
  claim_level: "reviewed or ready_for_next_step"
}
```

---

## 9. One-Line Rule

```text
For important AI work, define the goal, scope, checks, complexity limit, handoff, stop rule, and honest claim level before calling the result done.
```

---

END OF AI WORK QUALITY CONTRACT LITE v0.1
