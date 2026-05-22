# Basic Function Cards v0.1

## 1. scope_lock

```text
id:"basic_fn.scope_lock.v0.1"
name:"scope_lock"
layer:"basic_function_common_layer"
status:"stable"
purpose:"Lock the current request into a bounded task scope."
input_slots:["user_request","known_context?"]
output_schema:{
  bounded_scope:"string",
  out_of_scope:"list",
  missing_slots:"list",
  stop_condition:"string"
}
failure_output:{
  ok:false,
  reason:"missing_required_input | unstable_output | execution_forbidden",
  missing_slots:"list",
  suggested_layer:"basic_function_tightening | skill | engine"
}
operation:[
  "read the visible request",
  "state the smallest executable scope",
  "list nearby work that is outside this turn",
  "expose missing slots",
  "define when this function should stop"
]
guards:[
  "do not execute the task",
  "do not add a hidden goal",
  "do not expand into project redesign"
]
forbids:[
  "implementation",
  "deep meaning judgment",
  "domain reasoning"
]
memory_policy:"none"
trace_policy:"min"
fixture_id:"fixture.scope_lock.001"
pass_if:[
  "bounded_scope exists",
  "out_of_scope exists",
  "missing_slots exists",
  "stop_condition exists"
]
fail_if:[
  "task is executed inside the function",
  "scope expands beyond user request",
  "missing slot is guessed"
]
```

## 2. route_lock

```text
id:"basic_fn.route_lock.v0.1"
name:"route_lock"
layer:"basic_function_common_layer"
status:"stable"
purpose:"Choose the first read or first execution route."
input_slots:["bounded_scope","available_routes","constraints?"]
output_schema:{
  first_route:"string",
  conditional_routes:"list",
  do_not_read_by_default:"list",
  stop_rule:"string"
}
failure_output:{
  ok:false,
  reason:"missing_required_input | no_valid_route | unstable_output | route_expansion_forbidden",
  missing_slots:"list",
  suggested_layer:"basic_function_tightening | skill | engine"
}
operation:[
  "read bounded_scope",
  "select one first_route from available_routes",
  "place optional routes behind conditions",
  "list routes that should not be read by default",
  "define the stop rule"
]
guards:[
  "choose one first route",
  "do not read all routes",
  "do not turn optional context into required context"
]
forbids:[
  "full-folder sweep by default",
  "route expansion without trigger",
  "content judgment"
]
memory_policy:"none"
trace_policy:"min"
fixture_id:"fixture.route_lock.001"
pass_if:[
  "first_route is one item",
  "conditional_routes are condition-bound",
  "do_not_read_by_default is explicit",
  "stop_rule exists"
]
fail_if:[
  "all routes are opened",
  "first_route is ambiguous",
  "stop_rule is missing"
]
```

## 3. missing_slot_detect

```text
id:"basic_fn.missing_slot_detect.v0.1"
name:"missing_slot_detect"
layer:"basic_function_common_layer"
status:"stable"
purpose:"Find missing inputs without guessing."
input_slots:["input_slots","required_slots"]
output_schema:{
  missing:"list",
  present:"list",
  assumed:"list",
  needs_user:"boolean"
}
failure_output:{
  ok:false,
  reason:"missing_required_input | required_slots_missing | unstable_output | guessing_forbidden",
  missing_slots:"list",
  suggested_layer:"basic_function_tightening | skill | engine"
}
operation:[
  "compare input_slots with required_slots",
  "list present slots",
  "list missing slots",
  "list any assumptions already made",
  "mark whether user input is needed"
]
guards:[
  "do not fill missing values",
  "separate assumed from present",
  "ask only when the missing slot blocks execution"
]
forbids:[
  "guessing",
  "inventing user preference",
  "semantic overreach"
]
memory_policy:"none"
trace_policy:"min"
fixture_id:"fixture.missing_slot_detect.001"
pass_if:[
  "missing is accurate",
  "present is accurate",
  "assumed is separated",
  "needs_user reflects blocker status"
]
fail_if:[
  "missing slot is silently filled",
  "assumption is presented as fact",
  "needs_user is true for non-blocking detail"
]
```

## 4. output_schema_bind

```text
id:"basic_fn.output_schema_bind.v0.1"
name:"output_schema_bind"
layer:"basic_function_common_layer"
status:"stable"
purpose:"Bind the expected output shape before generation."
input_slots:["task_type","output_goal","constraints?","required_fields?","forbidden_fields?"]
output_schema:{
  required_fields:"list",
  forbidden_fields:"list",
  format_rule:"string",
  pass_if:"list"
}
failure_output:{
  ok:false,
  reason:"missing_required_input | unstable_output | schema_bloat | format_goal_unclear",
  missing_slots:"list",
  suggested_layer:"basic_function_tightening | skill | engine"
}
operation:[
  "read task_type and output_goal",
  "preserve explicit required_fields and forbidden_fields when provided",
  "choose only fields needed for that output",
  "list fields that must not appear",
  "state the format rule",
  "define pass_if for the output"
]
guards:[
  "keep the schema smaller than the task",
  "do not add optional sections by default",
  "prefer explicit required fields over broad style guidance"
]
forbids:[
  "open-ended output",
  "hidden appendices",
  "format drift"
]
memory_policy:"none"
trace_policy:"min"
fixture_id:"fixture.output_schema_bind.001"
pass_if:[
  "required_fields exists",
  "forbidden_fields exists",
  "format_rule exists",
  "pass_if exists"
]
fail_if:[
  "schema is broader than output_goal",
  "forbidden fields are missing",
  "format_rule is vague"
]
```

## 5. memory_policy_check

```text
id:"basic_fn.memory_policy_check.v0.1"
name:"memory_policy_check"
layer:"basic_function_common_layer"
status:"stable"
purpose:"Decide whether a result may create memory side effects."
input_slots:["artifact_type","user_confirmed?","reuse_value?"]
output_schema:{
  memory_policy:"none|trace_only|candidate_only",
  allowed_surface:"string",
  forbidden_surface:"list",
  promotion_required:"boolean"
}
failure_output:{
  ok:false,
  reason:"missing_required_input | memory_write_forbidden | promotion_unclear | unstable_output",
  missing_slots:"list",
  suggested_layer:"basic_function_tightening | skill | engine"
}
operation:[
  "classify artifact_type",
  "check whether user confirmation exists",
  "check whether reuse_value exists",
  "choose the weakest allowed memory_policy",
  "state allowed and forbidden surfaces"
]
guards:[
  "default to none",
  "do not create canon memory directly",
  "user confirmation is required for promotion beyond candidate"
]
forbids:[
  "canon write",
  "preference write from one-off comment",
  "global rule change"
]
memory_policy:"none"
trace_policy:"structured"
fixture_id:"fixture.memory_policy_check.001"
pass_if:[
  "memory_policy is one of none, trace_only, candidate_only",
  "allowed_surface exists",
  "forbidden_surface exists",
  "promotion_required is boolean"
]
fail_if:[
  "canon memory is allowed",
  "unconfirmed content is promoted",
  "global memory side effect is implied"
]
```

## 6. trace_policy_check

```text
id:"basic_fn.trace_policy_check.v0.1"
name:"trace_policy_check"
layer:"basic_function_common_layer"
status:"stable"
purpose:"Decide the trace level required for a task."
input_slots:["task_risk","repeatability_need","debug_need"]
output_schema:{
  trace_policy:"none|min|structured",
  trace_fields:"list",
  redaction_required:"boolean"
}
failure_output:{
  ok:false,
  reason:"missing_required_input | trace_bloat | redaction_unclear | unstable_output",
  missing_slots:"list",
  suggested_layer:"basic_function_tightening | skill | engine"
}
operation:[
  "read task_risk",
  "read repeatability_need",
  "read debug_need",
  "choose the lightest sufficient trace_policy",
  "list trace fields and redaction need"
]
guards:[
  "avoid excessive logging",
  "use structured trace only when needed",
  "redact sensitive values when present"
]
forbids:[
  "trace everything by default",
  "write secrets",
  "turn trace into work journal"
]
memory_policy:"none"
trace_policy:"min"
fixture_id:"fixture.trace_policy_check.001"
pass_if:[
  "trace_policy is one of none, min, structured",
  "trace_fields exists",
  "redaction_required is boolean"
]
fail_if:[
  "trace level is heavier than needed",
  "sensitive fields are not flagged",
  "trace fields are undefined"
]
```

## 7. gate_label

```text
id:"basic_fn.gate_label.v0.1"
name:"gate_label"
layer:"basic_function_common_layer"
status:"stable"
purpose:"Label whether an operation can proceed."
input_slots:["requested_action","risk","permission_state"]
output_schema:{
  gate:"ALLOW|WARN|HOLD|BLOCK|ESCALATE",
  reason:"string",
  required_confirmation:"boolean",
  safe_next_action:"string"
}
failure_output:{
  ok:false,
  reason:"missing_required_input | permission_unclear | unsafe_action | unstable_output",
  missing_slots:"list",
  suggested_layer:"basic_function_tightening | skill | engine"
}
operation:[
  "read requested_action",
  "read risk",
  "read permission_state",
  "choose one gate label",
  "state reason, confirmation need, and safe next action"
]
guards:[
  "choose one gate label only",
  "do not bypass permission state",
  "safe_next_action must be executable or explicitly a stop"
]
forbids:[
  "silent destructive action",
  "ambiguous proceed state",
  "permission escalation without confirmation"
]
memory_policy:"none"
trace_policy:"structured"
fixture_id:"fixture.gate_label.001"
pass_if:[
  "gate is one valid label",
  "reason exists",
  "required_confirmation is boolean",
  "safe_next_action exists"
]
fail_if:[
  "multiple gates are returned",
  "required confirmation is hidden",
  "safe_next_action is vague"
]
```
