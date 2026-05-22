# Basic Function Use Order v0.1

## Purpose
This file defines the default order for using the seven basic functions.

This is not an engine.
This is a use order for the common control layer.

## Default order

```text
1. scope_lock
2. missing_slot_detect
3. route_lock
4. output_schema_bind
5. memory_policy_check
6. trace_policy_check
7. gate_label
```

## Why this order

### 1. scope_lock
First decide what this turn is actually doing.

Without scope, every later function can expand the task.

### 2. missing_slot_detect
Before choosing route or output shape, expose missing inputs.

If a missing slot blocks the task, stop or ask.
If it does not block the task, record it as a non-blocking assumption.

### 3. route_lock
Choose what to read or touch first.

Route comes after missing-slot detection because route choice can change when a required slot is missing.

### 4. output_schema_bind
Lock what the answer or artifact must look like.

This prevents the model from adding broad explanation, extra modules, or unrelated proposals.

### 5. memory_policy_check
Decide whether any result may leave memory side effects.

This must happen before trace or gate because memory side effects change the risk.

### 6. trace_policy_check
Choose the lightest sufficient trace.

Do not log heavily by default.

### 7. gate_label
Finally decide whether the operation may proceed.

Gate comes last because it depends on scope, missing slots, route, output shape, memory policy, and trace policy.

## Stop points

Stop after `missing_slot_detect` when:

```text
required slot is missing
needs_user:true
```

Stop after `route_lock` when:

```text
no valid first_route exists
available_routes are outside scope
```

Stop after `memory_policy_check` when:

```text
requested memory side effect is not allowed
```

Stop after `gate_label` when:

```text
gate:"HOLD"
gate:"BLOCK"
gate:"ESCALATE"
```

## Minimal use

For small tasks, use only:

```text
scope_lock
missing_slot_detect
gate_label
```

## Full use

For document or system design tasks, use:

```text
scope_lock
missing_slot_detect
route_lock
output_schema_bind
memory_policy_check
trace_policy_check
gate_label
```

## One-line rule
Scope first, gate last.
