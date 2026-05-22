# AILO OS Harness Criteria v0.1

## Purpose
This document defines what must be true before AILO OS is treated as a harness rather than a document system.

## Core rule

```text
AILO OS is not the existence of AILO documents.
AILO OS begins when AILO operations become runnable, inspectable, stateful, and governed.
```

## Four criteria

### 1. Executable

The system can run a defined operation.

Minimum:

```text
input parser
function registry
function runner
error output
small fixture
```

Pass if:

```text
same input
-> same function selection
-> same output schema
```

Fail if:

```text
behavior depends only on the model rereading prose
```

### 2. Inspectable

The system exposes what happened.

Minimum:

```text
selected function
input slots
output schema
failure output
trace line
validation result
```

Pass if a later reader can reconstruct:

```text
what was called
why it was called
what it produced
what failed
```

Fail if:

```text
only final answer remains
```

### 3. Stateful

The system preserves task-relevant state without uncontrolled memory writes.

Minimum:

```text
trace policy
memory policy
candidate write surface
no direct canon write by default
```

Pass if:

```text
memory side effects are explicit
```

Fail if:

```text
every useful output becomes memory
or
memory writes depend on hidden model preference
```

### 4. Governed

The system controls side effects and high-risk actions.

Minimum:

```text
permission policy
gate label
validation gate
rollback or stop rule
human escalation rule
```

Pass if:

```text
unsafe or unclear operations can return HOLD / BLOCK / ESCALATE
```

Fail if:

```text
the model can execute because it sounds confident
```

## Verification stack requirement

Do not treat one green signal as full correctness.

Each verifier should declare:

```text
verifier_name
checks
does_not_check
confidence
remaining_risk
```

Example:

```text
unit_test
-> checks expected examples
-> does not check full specification

schema_check
-> checks output shape
-> does not check truth

human_review
-> checks judgment fit
-> does not guarantee repeatability
```

## Harness mutation rule

Changing the harness is a high-risk change.

Every harness mutation should carry:

```text
changed_component
target_failure
predicted_improvement
preserved_invariants
falsification_test
rollback_path
```

Do not accept a harness change only because it looks cleaner.

## Shared-state rule

If multiple agents, threads, or runners share the same operating surface, actions should eventually expose:

```text
read_set
write_set
assumptions
version_dependencies
verifier_obligations
conflict_policy
```

This is not required for document-only design work.
It becomes required when AILO OS moves into runtime or multi-agent execution.

## Threshold labels

```text
document_spec
-> criteria described but not runnable

harness_seed
-> executable + inspectable minimum exists

harness_prototype
-> executable + inspectable + stateful exists

harness_runtime
-> executable + inspectable + stateful + governed exists and is used repeatedly
```

## One-line rule
AILO OS is harness-grade only when it can run, expose, preserve, and govern AILO operations.
