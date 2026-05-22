# Harness Seed Scope Lock v0.1

## Purpose
This folder contains the first executable-style AILO OS harness seed.

It proves one stable basic function can be parsed, selected, run, validated, and traced.

It does not prove the full AILO OS.

## Seed

```text
seed:"ailo_os_harness_seed.scope_lock"
function:"basic_fn.scope_lock.v0.1"
status:"mock_prototype"
```

## Files

```text
SCOPE_LOCK_SEED_PROTOTYPE_SPEC_v0_1.md
-> exact seed flow and boundaries

SCOPE_LOCK_SEED_FIXTURES_v0_1.json
-> pass and fail fixtures

scope_lock_seed_mock_runner.py
-> deterministic mock runner

SCOPE_LOCK_SEED_VALIDATION_GATE_v0_1.md
-> pass/fail rules

SCOPE_LOCK_SEED_TRACE_FORMAT_v0_1.md
-> trace contract

SCOPE_LOCK_SEED_TEST_OUTPUT_v0_1.json
-> generated test output

SCOPE_LOCK_SEED_PROOF_REPORT_v0_1.md
-> proof result
```

## Run

```powershell
python .\scope_lock_seed_mock_runner.py .\SCOPE_LOCK_SEED_FIXTURES_v0_1.json
```

Expected summary:

```text
total:4
passed:4
failed:0
```

## Boundary

This seed may:
- parse one input object
- use one function registry record
- fixed-select `basic_fn.scope_lock.v0.1`
- emit result and trace
- validate against fixtures

This seed must not:
- call cognitive functions
- call engines
- write memory
- modify source documents
- execute the user's final task
- implement smart routing

## One-line rule
This is a one-function proof seed, not a full runtime.
