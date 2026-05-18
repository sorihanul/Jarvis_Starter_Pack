# Activation Rule

## Activate This Pack When

Use `Switching_Lens_Pack` when:

```text
one task needs more than one judgment posture
the model is drifting into a generic helper answer
the user asks for another angle, stricter view, simpler view, or verification view
the task needs intake before execution
the task needs review after a draft or plan
the answer must be decision-ready, not just informative
```

Common triggers:

```text
다른 관점으로 봐줘
검증 관점으로 봐줘
설계 관점으로 봐줘
사용자가 이해할 수 있게 다시 봐줘
지금 너무 퍼지는 것 같아
이걸 스킬로 할지 렌즈로 볼지 구분해줘
```

## Do Not Activate When

Do not use this pack when:

```text
one direct answer is enough
the user asked for a known skill or checklist
the task already belongs to one clear domain brain
the problem is tool permission, not viewpoint
the task is coding-specific and Switching_Coding_Pack already fits better
```

## Priority Rule

```text
viewpoint problem -> Switching_Lens_Pack
repeatable procedure problem -> relevant skill
coding role problem -> Switching_Coding_Pack
separate thread handoff problem -> Brain_Routing_and_Handoff_Pack
permission or tool risk -> Action_Permission_Pack
proof and acceptance problem -> Verification_and_Proof_Pack
```
