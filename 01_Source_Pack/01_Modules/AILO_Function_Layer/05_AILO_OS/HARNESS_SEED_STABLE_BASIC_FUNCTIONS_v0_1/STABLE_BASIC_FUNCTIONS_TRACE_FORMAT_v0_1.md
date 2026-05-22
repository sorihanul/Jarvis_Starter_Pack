# Stable Basic Functions Trace Format v0.1

## Purpose
Define the minimum trace for the seven-function stable basic seed.

## Trace shape

```text
trace{
  run_id:"string",
  seed:"ailo_os_harness_seed.stable_basic_functions",
  selected_function:"basic_fn.<name>.v0.1|null",
  input_keys:["function_id","slots"],
  output_keys:["function output keys"],
  memory_policy:"none",
  trace_policy:"min|structured",
  validation_result:"PASS|FAIL",
  failure_reason:"string|null"
}
```

## Required constraints

```text
trace exists on pass
trace exists on fail
memory_policy stays none
trace_policy follows registry
selected_function is null on unknown function
```

## One-line rule
Trace records which stable function was explicitly selected and whether its contract passed.
