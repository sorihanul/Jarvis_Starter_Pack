# Basic Function Real Task Fixtures v0.1

## Purpose
These fixtures test whether the basic functions work on real design tasks, not only clean examples.

## real.scope_lock.001

Input:

```text
user_request:"F 시스템에서 기본함수 정리하고, 다음에 인지함수도 가져오자."
known_context:"User has just corrected that basic function is the common layer and cognitive function is the expansion layer."
```

Expected output:

```text
bounded_scope:"Clarify and update the basic function common layer before starting cognitive function work."
out_of_scope:[
  "create cognitive functions now",
  "build engines",
  "change unrelated F source"
]
missing_slots:[]
stop_condition:"basic function common-layer wording is consistent"
```

## real.route_lock.001

Input:

```text
bounded_scope:"Clarify and update the basic function common layer."
available_routes:[
  "BASIC_AND_COGNITIVE_FUNCTION_CONCEPT",
  "BASIC_FUNCTION_WORKSPACE",
  "FUNCTION_TO_COGNITIVE_EXPANSION_BRIDGE",
  "DEVELOPMENT_ROADMAP"
]
constraints:["basic function first"]
```

Expected output:

```text
first_route:"BASIC_FUNCTION_WORKSPACE"
conditional_routes:[
  "BASIC_AND_COGNITIVE_FUNCTION_CONCEPT when wording conflict appears",
  "DEVELOPMENT_ROADMAP when path wording conflicts"
]
do_not_read_by_default:[
  "FUNCTION_TO_COGNITIVE_EXPANSION_BRIDGE"
]
stop_rule:"stop before creating cognitive functions"
```

## real.output_schema_bind.001

Input:

```text
task_type:"final_turn_report"
output_goal:"explain what changed and what next"
constraints:["easy Korean", "short", "include file paths", "no execution-layer drift"]
```

Expected output:

```text
required_fields:[
  "what_changed",
  "verification",
  "remaining_risk",
  "next_step"
]
forbidden_fields:[
  "execution-layer plan",
  "new cognitive function list",
  "broad roadmap"
]
format_rule:"short Korean report with file links"
pass_if:[
  "report stays about basic function quality",
  "next step is function tightening or real-task test"
]
```

## real.gate_label.001

Input:

```text
requested_action:"add more basic functions before using the first seven"
risk:"medium"
permission_state:"not requested"
```

Expected output:

```text
gate:"HOLD"
reason:"adding more functions before testing the first seven increases surface area without proof"
required_confirmation:true
safe_next_action:"test and tighten the existing seven functions first"
```
