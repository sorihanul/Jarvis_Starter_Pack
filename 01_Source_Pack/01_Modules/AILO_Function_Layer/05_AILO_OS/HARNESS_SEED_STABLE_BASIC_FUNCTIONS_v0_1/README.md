# Harness Seed Stable Basic Functions v0.1

## Purpose
This folder expands the first one-function seed into the stable AILO basic function set.

It supports all seven stable basic functions by explicit `function_id`.

It does not implement smart routing.

## Supported functions

```text
basic_fn.scope_lock.v0.1
basic_fn.route_lock.v0.1
basic_fn.missing_slot_detect.v0.1
basic_fn.output_schema_bind.v0.1
basic_fn.memory_policy_check.v0.1
basic_fn.trace_policy_check.v0.1
basic_fn.gate_label.v0.1
```

## Files

```text
STABLE_BASIC_FUNCTIONS_SEED_SPEC_v0_1.md
STABLE_BASIC_FUNCTIONS_FIXTURES_v0_1.json
stable_basic_functions_mock_runner.py
STABLE_BASIC_FUNCTIONS_VALIDATION_GATE_v0_1.md
STABLE_BASIC_FUNCTIONS_TRACE_FORMAT_v0_1.md
STABLE_BASIC_FUNCTIONS_TEST_OUTPUT_v0_1.json
STABLE_BASIC_FUNCTIONS_PROOF_REPORT_v0_1.md
```

## Run

```powershell
python .\stable_basic_functions_mock_runner.py .\STABLE_BASIC_FUNCTIONS_FIXTURES_v0_1.json
```

Expected summary:

```text
total:10
passed:10
failed:0
```

## Boundary

This seed may:
- parse explicit `function_id`
- look up one stable function
- run the requested basic function
- validate output shape
- emit minimal trace

This seed must not:
- infer which function to use
- call cognitive functions
- call engines
- write memory
- execute final user tasks
- modify source documents

## One-line rule
This seed proves the seven stable basic functions can run by explicit function id; it is not a router.
