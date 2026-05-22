# AILO OS Harness Seed Execution Contract v0.1

## Purpose
This document turns the first harness seed target into an implementation-ready contract.

It is still not runtime code.
It is the contract a future runner must satisfy.

## Contract target

```text
seed:"ailo_os_harness_seed.scope_lock"
function:"basic_fn.scope_lock.v0.1"
state:"harness_seed_contract"
```

## Operating boundary

This seed runs one basic function only.

It must not:
- infer hidden meaning
- call a cognitive function
- call an engine
- write memory
- perform the user's final task
- choose among multiple functions
- modify source documents

## Minimal input object

```text
input{
  run_id:"string?",
  function_id:"basic_fn.scope_lock.v0.1?",
  user_request:"string",
  known_context:"string?"
}
```

Default values:

```text
function_id:"basic_fn.scope_lock.v0.1"
known_context:null
```

Reject when:

```text
user_request is empty
function_id is not supported
```

## Parsed object

```text
parsed{
  run_id:"string",
  function_id:"basic_fn.scope_lock.v0.1",
  slots:{
    user_request:"string",
    known_context:"string|null"
  }
}
```

Parser responsibilities:
- preserve the visible user request
- normalize missing optional fields to `null`
- do not rewrite intent
- do not add hidden goals

## Registry record

The seed registry contains exactly one function:

```text
registry[
  {
    id:"basic_fn.scope_lock.v0.1",
    name:"scope_lock",
    layer:"basic_function_common_layer",
    required_slots:["user_request"],
    optional_slots:["known_context"],
    output_schema:["bounded_scope","out_of_scope","missing_slots","stop_condition"],
    memory_policy:"none",
    trace_policy:"min",
    forbids:["final_task_execution","deep_meaning_judgment","domain_reasoning"]
  }
]
```

Fail if:

```text
registry has zero functions
registry has more than one function
registry output_schema does not match the function card
```

## Selector contract

For v0.1, selector is fixed.

```text
select(parsed, registry)
-> "basic_fn.scope_lock.v0.1"
```

Do not build:
- semantic router
- intent classifier
- function ranking
- fallback function selection

Fail if:

```text
selected_function != "basic_fn.scope_lock.v0.1"
```

## Runner contract

Runner input:

```text
parsed
selected_function
registry_record
```

Runner output:

```text
result{
  ok:true,
  function_id:"basic_fn.scope_lock.v0.1",
  output:{
    bounded_scope:"string",
    out_of_scope:["string"],
    missing_slots:["string"],
    stop_condition:"string"
  }
}
```

Runner rules:
- produce the four required output fields
- keep scope to the current request
- list nearby work that is explicitly out of scope
- expose missing slots instead of guessing
- define stop condition
- do not execute the final task

## Failure contract

All failures use the same shape:

```text
failure_output{
  ok:false,
  function_id:"basic_fn.scope_lock.v0.1|null",
  reason:"missing_required_input | unknown_function | unstable_output | execution_forbidden | registry_invalid | validation_failed",
  missing_slots:[],
  suggested_layer:"basic_function_tightening | skill | engine | harness_contract_fix"
}
```

Do not return:
- prose-only error
- partial success without `ok`
- guessed missing slot
- final task result disguised as scope output

## Trace contract

Every run returns one trace object.

```text
trace{
  run_id:"string",
  seed:"ailo_os_harness_seed.scope_lock",
  selected_function:"basic_fn.scope_lock.v0.1",
  input_keys:["user_request","known_context"],
  output_keys:["bounded_scope","out_of_scope","missing_slots","stop_condition"],
  memory_policy:"none",
  trace_policy:"min",
  validation_result:"PASS | FAIL",
  failure_reason:"string|null"
}
```

Trace must be present even on failure.

## Validation contract

Validation passes when:

```text
registry contains exactly one supported function
required slot user_request is present
selected function is basic_fn.scope_lock.v0.1
output contains all four required fields
memory_policy is none
trace object exists
final task was not executed
```

Validation fails when:

```text
user_request is missing
unknown function_id is requested
output schema is incomplete
scope expands into a project plan
missing slot is guessed
memory is written
trace is missing
```

## Acceptance fixtures

### Fixture 1: pass

Input:

```text
user_request:"지금 기본함수 문서에 후보 상태와 실패 출력을 반영해줘."
known_context:"AILO basic function workspace"
```

Expected:

```text
ok:true
selected_function:"basic_fn.scope_lock.v0.1"
output_keys:["bounded_scope","out_of_scope","missing_slots","stop_condition"]
memory_policy:"none"
validation_result:"PASS"
```

### Fixture 2: missing input

Input:

```text
user_request:""
known_context:"AILO basic function workspace"
```

Expected:

```text
ok:false
reason:"missing_required_input"
missing_slots:["user_request"]
validation_result:"FAIL"
```

### Fixture 3: unknown function

Input:

```text
function_id:"basic_fn.hidden_premise_extract.v0.1"
user_request:"숨은 전제를 찾아줘."
```

Expected:

```text
ok:false
reason:"unknown_function"
suggested_layer:"harness_contract_fix"
validation_result:"FAIL"
```

### Fixture 4: execution forbidden

Input:

```text
user_request:"이 문서를 실제로 고쳐줘."
known_context:"scope_lock seed test"
```

Expected:

```text
ok:true
bounded_scope:"lock the scope for editing the document"
out_of_scope includes:"perform the actual edit"
validation_result:"PASS"
```

The runner may define the scope.
It must not perform the edit.

## Implementation hint

Any language may implement this seed later.

For now, the implementation target is:

```text
parse(input)
-> select(parsed, registry)
-> run_scope_lock(parsed, registry_record)
-> validate(result)
-> emit(result, trace)
```

No smart routing.
No cognitive interpretation.
No memory write.

## One-line rule
The first AILO OS harness seed is a deterministic contract for running one basic function and proving that the system can parse, select, run, validate, and trace without doing the user's final task.
