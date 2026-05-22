# AILO OS Implementation Sequence v0.1

## Purpose
This document fixes the implementation order before Rust.

Rust is not the next step.
The next step is to make the non-Rust prototype stable enough to learn from.

## Current completed stage

```text
stage:"stable_basic_functions_mock_seed"
status:"PASS"
stable_function_count:7
fixture_total:10
fixture_failed:0
```

## Sequential implementation path

### Stage 1: one-function seed

```text
scope_lock only
status:"DONE"
proof:"05_AILO_OS/HARNESS_SEED_SCOPE_LOCK_v0_1/SCOPE_LOCK_SEED_PROOF_REPORT_v0_1.md"
```

### Stage 2: seven-function explicit seed

```text
seven stable basic functions
selection:"explicit function_id"
status:"DONE"
proof:"05_AILO_OS/HARNESS_SEED_STABLE_BASIC_FUNCTIONS_v0_1/STABLE_BASIC_FUNCTIONS_PROOF_REPORT_v0_1.md"
```

### Stage 3: negative fixture hardening

```text
goal:"prove each function fails cleanly when required input is missing"
status:"DONE"
```

This stage must prove:

```text
missing required input -> FAIL
trace still emitted
memory is not written
final task is not executed
```

### Stage 4: non-Rust mini harness

```text
goal:"provide a small reusable local entrypoint before Rust"
status:"DONE"
```

This stage may include:

```text
run-fixtures
run-one
registry inspection
trace emission
```

It must not include:

```text
smart routing
memory persistence
cognitive functions
engines
file modification
release packaging
```

### Stage 5: usage observation

```text
goal:"try several real control tasks and record what breaks"
status:"IN_PROGRESS"
```

Current usage observation:

```text
skill_manufacturing_samples:3
skill_manufacturing_failed:0
small_real_trials:3
small_real_trials_failed:0
v0_2_skill_skeleton_status:"stable_candidate"
```

This stage decides whether runner semantics are too generic.

### Stage 6: cognitive function proof

```text
goal:"only after the basic harness is stable, prove one brain-local cognitive function"
status:"LATER"
```

### Stage 7: engine proof

```text
goal:"only after function and cognitive-function proof, run ordered pipeline proof"
status:"LATER"
```

### Stage 8: Rust review

```text
goal:"consider Rust only after enough non-Rust behavior is known"
status:"NOT_NOW"
```

## One-line rule
Implement in small proof layers first; Rust begins only after the non-Rust harness shows what must be deterministic.
