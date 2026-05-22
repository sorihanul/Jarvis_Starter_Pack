# Scope Lock Seed Trace Format v0.1

## Purpose
Define the minimum trace emitted by the scope-lock harness seed.

Trace is not a work journal.
Trace only proves what was selected, what was checked, and whether validation passed.

## Trace shape

```text
trace{
  run_id:"string",
  seed:"ailo_os_harness_seed.scope_lock",
  selected_function:"basic_fn.scope_lock.v0.1|null",
  input_keys:["user_request","known_context"],
  output_keys:["bounded_scope","out_of_scope","missing_slots","stop_condition"],
  memory_policy:"none",
  trace_policy:"min",
  validation_result:"PASS|FAIL",
  failure_reason:"string|null"
}
```

## Required even on failure

Trace must exist when:

```text
user_request is missing
unknown function is requested
validation fails
```

## What trace must not contain

```text
full conversation history
hidden reasoning
large source text
memory write content
domain interpretation
final task output
```

## One-line rule
Trace records harness control facts only.
