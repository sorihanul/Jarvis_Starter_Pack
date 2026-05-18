# Acceptance Tests

## Test 1. Lens Instead Of Skill

Input:

```text
이걸 스킬로 할지 렌즈로 볼지 구분해줘.
```

Pass:

```text
explains that lens changes viewpoint
explains that skill performs a repeatable move
selects one first
does not pretend lens and skill are the same
```

Fail:

```text
turns every lens into a skill
turns every skill into a lens
opens multiple packs without need
```

## Test 2. Same Task, Different Lens

Input:

```text
이 계획을 검증 관점으로 다시 봐줘.
```

Pass:

```text
active_lens: review
first_focus: defect, risk, missing proof
does not rewrite the whole plan unless needed
returns findings and next action
```

Fail:

```text
only summarizes the plan
adds unrelated ideas
creates a new brain or project
```

## Test 3. Skill Pairing

Input:

```text
이 자료는 근거가 중요해. 어떤 방식으로 처리할까?
```

Pass:

```text
active_lens: evidence
pairs with Evidence_Intake_Pack or source-check skill when needed
separates fact, inference, missing source
returns to the task goal
```

Fail:

```text
uses a writing skill first
skips source uncertainty
turns evidence review into broad research
```

## Test 4. Coding Boundary

Input:

```text
이 버그 수정은 구현, 리뷰, 검증 순서로 봐줘.
```

Pass:

```text
uses Switching_Coding_Pack first
does not keep the work in generic Switching_Lens_Pack
```

Fail:

```text
uses generic lens when coding-specific pack fits better
```
