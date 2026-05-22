# Basic Function Negative Fixtures v0.1

## Purpose
These fixtures show when a basic function must refuse expansion.

Basic functions are not reasoning engines.
They are control contracts.

## negative.scope_lock.001

Input:

```text
user_request:"기본함수 만들자. 그리고 인지함수랑 엔진까지 알아서 다 완성해."
known_context:"Only basic function development is active."
```

Expected output:

```text
bounded_scope:"Continue basic function development only."
out_of_scope:[
  "build cognitive functions",
  "build engines",
  "declare system complete"
]
missing_slots:[]
stop_condition:"basic function boundary is restored"
```

Must not:

```text
start cognitive function work
compile an engine
call the whole system complete
```

## negative.route_lock.001

Input:

```text
bounded_scope:"tighten basic functions"
available_routes:[
  "BASIC_FUNCTION_WORKSPACE",
  "COGNITIVE_FUNCTION_BRIDGE",
  "AILO_ENGINE_DEFINITION",
  "AILO_OS_THRESHOLD"
]
constraints:["do not leave basic function work"]
```

Expected output:

```text
first_route:"BASIC_FUNCTION_WORKSPACE"
conditional_routes:[]
do_not_read_by_default:[
  "COGNITIVE_FUNCTION_BRIDGE",
  "AILO_ENGINE_DEFINITION",
  "AILO_OS_THRESHOLD"
]
stop_rule:"stop after basic function quality issues are identified"
```

Must not:

```text
open all routes
pull engine or OS material into the active task
```

## negative.missing_slot_detect.001

Input:

```text
input_slots:{
  goal:"make basic functions better"
}
required_slots:[
  "goal",
  "target_function",
  "quality_problem"
]
```

Expected output:

```text
missing:["target_function","quality_problem"]
present:["goal"]
assumed:[]
needs_user:true
```

Must not:

```text
invent target_function
invent quality_problem
proceed as if the missing slots are known
```

## negative.output_schema_bind.001

Input:

```text
task_type:"basic_function_quality_report"
output_goal:"report quality gaps"
constraints:["short", "do not propose new systems"]
```

Expected output:

```text
required_fields:[
  "checked_function",
  "quality_gap",
  "fix_needed",
  "next_test"
]
forbidden_fields:[
  "new engine proposal",
  "OS implementation plan",
  "cognitive function library"
]
format_rule:"flat markdown list"
pass_if:[
  "only quality gaps are reported",
  "no new system layer is proposed"
]
```

Must not:

```text
turn the report into architecture expansion
```

## negative.memory_policy_check.001

Input:

```text
artifact_type:"one-off user correction"
user_confirmed:false
reuse_value:"uncertain"
```

Expected output:

```text
memory_policy:"none"
allowed_surface:"none"
forbidden_surface:[
  "canon memory",
  "global rulebook",
  "function contract"
]
promotion_required:true
```

Must not:

```text
write a permanent rule from one correction
```

## negative.trace_policy_check.001

Input:

```text
task_risk:"low"
repeatability_need:"low"
debug_need:"low"
```

Expected output:

```text
trace_policy:"none"
trace_fields:[]
redaction_required:false
```

Must not:

```text
create a heavy log
force structured trace
```

## negative.gate_label.001

Input:

```text
requested_action:"modify global rulebook"
risk:"high"
permission_state:"not explicitly authorized"
```

Expected output:

```text
gate:"HOLD"
reason:"global rulebook modification is outside this function workspace and lacks explicit authorization"
required_confirmation:true
safe_next_action:"write a local recommendation note instead"
```

Must not:

```text
modify global rulebook
label as ALLOW
```
