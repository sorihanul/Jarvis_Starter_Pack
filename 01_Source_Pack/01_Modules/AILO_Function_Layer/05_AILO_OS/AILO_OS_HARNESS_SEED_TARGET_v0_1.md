# AILO OS Harness Seed Target v0.1

## Purpose
This document defines the first minimal target for AILO OS harness work.

It does not start Rust work.
It defines what the first runnable seed must prove.

## Seed name

```text
ailo_os_harness_seed.scope_lock
```

## Why this target

The first seed should use a boring basic function, not a cognitive function or engine.

Use:

```text
basic_fn.scope_lock.v0.1
```

Reason:
- it has stable input slots
- it has stable output schema
- it does not require meaning judgment
- it does not need memory write
- it can prove parser, registry, runner, failure output, trace, and validation without domain complexity

## Required harness pieces

### 1. Input parser

Minimum input:

```text
user_request:"string"
known_context:"string?"
```

Parser output:

```text
parsed_input{
  user_request:"string",
  known_context:"string|null"
}
```

Fail if:

```text
user_request is empty
```

### 2. Function registry

Registry must contain one function:

```text
basic_fn.scope_lock.v0.1
```

Registry record:

```text
id
name
layer
input_slots
output_schema
memory_policy
trace_policy
pass_if
fail_if
```

Fail if:

```text
requested function id is not in registry
```

### 3. Function selector

For seed v0.1, selection is fixed:

```text
selected_function:"basic_fn.scope_lock.v0.1"
```

Do not build a smart router yet.

Fail if:

```text
selector returns multiple functions
```

### 4. Function runner

Runner must produce:

```text
bounded_scope
out_of_scope
missing_slots
stop_condition
```

The runner does not perform the user's final task.
It only controls execution shape.

Fail if:

```text
final task is executed
```

### 5. Failure output

Failure shape:

```text
failure_output{
  ok:false,
  reason:"missing_required_input | unknown_function | unstable_output | execution_forbidden",
  missing_slots:[],
  suggested_layer:"basic_function_tightening | skill | engine"
}
```

Do not return a vague prose-only error.

### 6. Trace line

Minimum trace:

```text
trace{
  run_id:"string",
  selected_function:"basic_fn.scope_lock.v0.1",
  input_keys:["user_request","known_context"],
  output_keys:["bounded_scope","out_of_scope","missing_slots","stop_condition"],
  memory_policy:"none",
  trace_policy:"min",
  validation_result:"PASS | FAIL"
}
```

### 7. Validation gate

Pass only if:

```text
selected_function exists in registry
required input exists
output has all required fields
final task is not executed
memory_policy is none
trace line exists
```

Fail if:

```text
output schema changes
missing input is guessed
scope expands into full project planning
```

## Seed fixture

Input:

```text
user_request:"지금 기본함수 문서에 후보 상태와 실패 출력을 반영해줘."
known_context:"AILO basic function workspace"
```

Expected output shape:

```text
bounded_scope:"update the basic function boundary documents for candidate state and failure output"
out_of_scope:[
  "implement Rust runner",
  "add new cognitive functions",
  "promote new functions to stable layer"
]
missing_slots:[]
stop_condition:"stop after boundary documents and re-entry capsule are updated and verified"
```

Expected trace:

```text
selected_function:"basic_fn.scope_lock.v0.1"
memory_policy:"none"
trace_policy:"min"
validation_result:"PASS"
```

## Non-goals

Do not include:
- cognitive function execution
- engine pipeline execution
- web search
- memory writing
- multi-agent state
- release packaging
- permission tiers beyond no-execution guard

## Threshold result

If this seed is implemented and passes, the system may be called:

```text
harness_seed
```

It is not yet:

```text
harness_prototype
harness_runtime
AILO OS runtime
```

## One-line rule
The first AILO OS harness seed should prove one boring basic function can be parsed, selected, run, traced, and validated without executing the user's final task.
