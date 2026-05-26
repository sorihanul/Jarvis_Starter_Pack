# Activation Rule

## activate when

Use this pack when the user asks to make a small ontology, frame set, reusable concept map, knowledge pack, brain map, source/claim map, or v4 target-frame layer.

Also use it when mixed material contains repeated or confusion-prone targets such as:

```text
brain
function pack
policy
source
claim
evidence
verification result
repo target
patch plan
synapse target
domain concept
```

## activate examples

```text
이 자료로 미니 온톨로지 만들어줘.
브레인/팩/소스/주장을 헷갈리지 않게 구조화해줘.
AILO-N Frame으로 정리해줘.
이 도메인에서 candidate/asserted를 나눠줘.
검증 가능한 작은 지식 구조로 바꿔줘.
```

## do not activate when

```text
single_answer_enough:true
no_repeated_target:true
user_only_wants_summary:true
frame_output_would_not_change_ai_behavior:true
source_or_evidence_absent_and_user_wants_asserted_facts:true
```

## activation decision

```text
if repeated_target and structure_changes_next_action:
  activate
else:
  use Ontology_Pack or plain summary instead
```
