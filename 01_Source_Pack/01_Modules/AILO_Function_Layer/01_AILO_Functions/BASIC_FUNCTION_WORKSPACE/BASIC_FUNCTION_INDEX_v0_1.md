# Basic Function Index v0.1

## Current function set

| id | name | status | role |
| --- | --- | --- | --- |
| `basic_fn.scope_lock.v0.1` | `scope_lock` | `stable` | lock current task scope |
| `basic_fn.route_lock.v0.1` | `route_lock` | `stable` | choose first route and non-read surfaces |
| `basic_fn.missing_slot_detect.v0.1` | `missing_slot_detect` | `stable` | expose missing inputs without guessing |
| `basic_fn.output_schema_bind.v0.1` | `output_schema_bind` | `stable` | bind output shape |
| `basic_fn.memory_policy_check.v0.1` | `memory_policy_check` | `stable` | decide memory side-effect policy |
| `basic_fn.trace_policy_check.v0.1` | `trace_policy_check` | `stable` | decide trace shape |
| `basic_fn.gate_label.v0.1` | `gate_label` | `stable` | label proceed / hold / block |

## Proof result

```text
basic_function_set_v0.1: stable
```

See `BASIC_FUNCTION_PROOF_REPORT_v0_1.md`.

## Promotion rule
A function can move from `fixture_ready` to `tested` only after:

```text
fixture exists
expected output shape exists
acceptance check passes
no cognitive interpretation is required
```

A function can move from `tested` to `stable` only after:

```text
failure_output exists
negative fixture exists
real-task fixture exists
no final task execution by default
memory side effects are explicit
trace shape is explicit
```

## One-line rule
The v0.1 set favors boring control functions over clever reasoning functions.
