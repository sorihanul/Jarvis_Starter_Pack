# Basic Function Test Fixtures v0.1

## fixture.scope_lock.001

Input:

```text
user_request:"기본함수부터 만들어가자고. 모든건 한 폴더에 들어있어야 하고 언제든 다시 꺼내서 구현을 이어갈 수 있도록 개발일지도 그 안에 작성하면서 진행하자"
known_context:"AILO function system already separates basic function and cognitive function."
```

Expected output:

```text
bounded_scope:"Create a single basic-function workspace folder with entry, map, contract, index, cards, fixtures, acceptance check, and development log."
out_of_scope:[
  "build execution layer",
  "build cognitive functions",
  "compile AILO engine",
  "change global rulebook"
]
missing_slots:[]
stop_condition:"workspace exists and first function proof target is named"
```

## fixture.route_lock.001

Input:

```text
bounded_scope:"Create and continue basic-function workspace."
available_routes:[
  "existing minimum set",
  "existing cognitive bridge",
  "new basic function workspace",
  "later operating-layer docs",
  "F source bank"
]
constraints:["keep all basic function development in one folder"]
```

Expected output:

```text
first_route:"new basic function workspace"
conditional_routes:[
  "existing minimum set only for seed names",
  "existing cognitive bridge only after basic proof"
]
do_not_read_by_default:[
  "later operating-layer docs",
  "F source bank"
]
stop_rule:"stop after contract, first cards, fixtures, and log are in the workspace"
```

## fixture.missing_slot_detect.001

Input:

```text
input_slots:{
  goal:"build basic functions first",
  location:"one folder",
  continuity:"development log inside the folder"
}
required_slots:[
  "goal",
  "location",
  "continuity",
  "first_function_set"
]
```

Expected output:

```text
missing:["first_function_set"]
present:["goal","location","continuity"]
assumed:["first_function_set may start with scope_lock, route_lock, missing_slot_detect based on existing minimum set"]
needs_user:false
```

## fixture.output_schema_bind.001

Input:

```text
task_type:"basic_function_proof_report"
output_goal:"close the v0.1 basic function set"
constraints:[
  "short report",
  "must include performed work",
  "must include verification result",
  "must include remaining risk"
]
```

Expected output:

```text
required_fields:[
  "performed_work",
  "verification",
  "result",
  "remaining_risk",
  "next_step"
]
forbidden_fields:[
  "new cognitive function proposal",
  "execution-layer detail",
  "global rulebook change"
]
format_rule:"flat markdown sections"
pass_if:[
  "all required fields are present",
  "forbidden fields are absent",
  "report does not expand beyond basic function proof"
]
```

## fixture.memory_policy_check.001

Input:

```text
artifact_type:"basic function development log"
user_confirmed:true
reuse_value:true
```

Expected output:

```text
memory_policy:"trace_only"
allowed_surface:"BASIC_FUNCTION_WORKSPACE/DEVELOPMENT_LOG.md"
forbidden_surface:[
  "global rulebook",
  "canon memory",
  "external workspace"
]
promotion_required:false
```

## fixture.trace_policy_check.001

Input:

```text
task_risk:"low"
repeatability_need:"medium"
debug_need:"medium"
```

Expected output:

```text
trace_policy:"min"
trace_fields:[
  "function_id",
  "fixture_id",
  "result_label",
  "notes"
]
redaction_required:false
```

## fixture.gate_label.001

Input:

```text
requested_action:"write basic function docs inside BASIC_FUNCTION_WORKSPACE"
risk:"low"
permission_state:"user requested proceed"
```

Expected output:

```text
gate:"ALLOW"
reason:"action stays inside requested workspace and does not touch global rulebook or execution-layer code"
required_confirmation:false
safe_next_action:"write or update basic function workspace files, then verify"
```
