# Basic Function Quality Review v0.1

## Result

```text
stable_v0_1
```

The seven basic functions are stable enough for the first common control layer.

Do not promote more functions yet.
AILO may keep producing function candidates, but candidates must pass the candidate gate before entering the common layer.
Use and tighten these seven first.

Basic functions control execution shape.
They do not perform the final task unless that behavior is explicitly defined in the function contract.

## Coverage

| control need | covered by | status |
| --- | --- | --- |
| define task boundary | `scope_lock` | sufficient |
| expose missing inputs | `missing_slot_detect` | sufficient |
| choose reading route | `route_lock` | sufficient |
| lock output shape | `output_schema_bind` | sufficient |
| prevent memory side effects | `memory_policy_check` | sufficient |
| choose trace weight | `trace_policy_check` | sufficient |
| decide proceed/hold/block | `gate_label` | sufficient |

## Strong points

- The set stays below cognitive-function level.
- The functions are small enough to reuse.
- Memory and trace are explicit instead of hidden.
- Gate comes after scope and policy.
- Negative fixtures now test refusal behavior.
- Real-task fixtures test actual design use.

## Weak points

These are not blocking issues for v0.1.
They are watchpoints for future use.

### 1. `scope_lock` may still become too broad
Risk:

```text
bounded_scope becomes a mini project plan
```

Tightening rule:

```text
bounded_scope must fit one current task, not the full project.
```

### 2. `route_lock` may over-read
Risk:

```text
conditional_routes become required routes
```

Tightening rule:

```text
conditional routes open only when their condition is met.
```

### 3. `missing_slot_detect` may over-ask
Risk:

```text
asks user even when the missing slot does not block work
```

Tightening rule:

```text
needs_user:true only when the missing slot blocks the next action.
```

### 4. `output_schema_bind` may over-format
Risk:

```text
schema becomes larger than the answer
```

Tightening rule:

```text
required_fields must be the minimum fields needed to satisfy output_goal.
```

### 5. `memory_policy_check` may promote too early
Risk:

```text
one-off correction becomes a durable rule
```

Tightening rule:

```text
unconfirmed one-off content stays memory_policy:"none".
```

### 6. `trace_policy_check` may create log bloat
Risk:

```text
structured trace is used when min or none is enough
```

Tightening rule:

```text
choose the lightest sufficient trace.
```

### 7. `gate_label` may hide uncertainty
Risk:

```text
ALLOW is returned even when permission state is unclear
```

Tightening rule:

```text
unclear permission state cannot produce ALLOW.
```

## New-function candidate rule

Before promoting any new basic function, prove that the need cannot be handled by:

```text
scope_lock
missing_slot_detect
route_lock
output_schema_bind
memory_policy_check
trace_policy_check
gate_label
```

If a need is meaning-based, do not add a basic function.
Send it to the cognitive-function expansion layer later.

Record new ideas in `BASIC_FUNCTION_CANDIDATE_GATE_v0_1.md` first.

Candidate states:

```text
raw_material
function_candidate
tested_basic_function
stable_basic_function
deprecated
```

If the candidate fails, record the reason with `failure_output` instead of forcing a new function name.

## Function / skill / engine split

```text
function
-> one control move

skill
-> user-facing package of several moves

engine
-> ordered internal mechanism with verification and stop rules
```

Do not create a skill when one function is enough.
Do not create an engine when order and verification do not matter.

## Next quality work

Use these seven functions in future tasks and record:

```text
which function was called
which fixture was closest
where the function was too broad
where it stopped expansion correctly
what wording must be tightened
```

Do not reopen the stable layer unless real use shows repeated failure.

## One-line rule
AILO is an infinite function source, but this common layer should grow only through candidate-gated proof.
