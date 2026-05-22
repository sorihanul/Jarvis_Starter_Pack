# Basic Function Skill Skeleton Series v0.2

## Purpose
This document defines the basic functions used to manufacture skills.

A skill should not be one large instruction block.
A skill can be shaped by small control functions.

## Concept

```text
basic functions
-> control the skeleton of a skill

skill
-> packages several controlled moves into a user-facing reusable workflow
```

## Function series

### 1. input_contract_bind

```text
id:"basic_fn.input_contract_bind.v0.2"
status:"stable_candidate"
purpose:"Bind required and optional inputs for a skill."
input_slots:["skill_goal","raw_inputs?","required_candidates?"]
output_schema:{
  required_inputs:"list",
  optional_inputs:"list",
  rejected_inputs:"list",
  missing_inputs:"list"
}
forbids:["guessing missing inputs","checking a live call for proceed/hold","domain judgment","execution"]
memory_policy:"none"
trace_policy:"min"
```

### 2. step_sequence_lock

```text
id:"basic_fn.step_sequence_lock.v0.2"
status:"stable_candidate"
purpose:"Lock the user-facing step order of a skill."
input_slots:["skill_goal","candidate_steps"]
output_schema:{
  ordered_steps:"list",
  optional_steps:"list",
  forbidden_reorder:"list",
  stop_rule:"string"
}
forbids:["executing steps","engine verification","semantic optimization"]
memory_policy:"none"
trace_policy:"min"
```

### 3. acceptance_criteria_bind

```text
id:"basic_fn.acceptance_criteria_bind.v0.2"
status:"stable_candidate"
purpose:"Bind pass/fail criteria before work starts."
input_slots:["output_goal","quality_constraints?","failure_constraints?"]
output_schema:{
  pass_if:"list",
  fail_if:"list",
  proof_required:"list",
  review_stop_rule:"string"
}
forbids:["quality judgment execution","replacing output_schema_bind","hidden criteria","domain truth claim"]
memory_policy:"none"
trace_policy:"min"
```

### 4. fixture_contract_bind

```text
id:"basic_fn.fixture_contract_bind.v0.2"
status:"stable_candidate"
purpose:"Define minimal positive and negative fixtures for a skill."
input_slots:["function_or_skill_id","input_contract","output_contract"]
output_schema:{
  positive_fixture_shape:"object",
  negative_fixture_shape:"object",
  required_assertions:"list",
  fixture_stop_rule:"string"
}
forbids:["running tests","inventing domain examples as facts","large fixture suite by default"]
memory_policy:"none"
trace_policy:"min"
```

### 5. handoff_packet_bind

```text
id:"basic_fn.handoff_packet_bind.v0.2"
status:"stable_candidate"
purpose:"Bind the packet handed to the next stage."
input_slots:["current_stage","next_stage","artifact_summary","open_items?"]
output_schema:{
  handoff_fields:"list",
  required_artifacts:"list",
  open_items:"list",
  next_entrypoint:"string"
}
forbids:["performing next stage","hiding open items","canon promotion"]
memory_policy:"none"
trace_policy:"structured"
```

### 6. retry_policy_check

```text
id:"basic_fn.retry_policy_check.v0.2"
status:"stable_candidate"
purpose:"Decide whether to retry, hold, stop, or escalate."
input_slots:["failure_reason","attempt_count","max_attempts","risk?"]
output_schema:{
  retry_decision:"RETRY|HOLD|STOP|ESCALATE",
  reason:"string",
  next_attempt_change:"string",
  stop_condition:"string"
}
forbids:["blind retry","changing task goal","hiding repeated failure"]
memory_policy:"none"
trace_policy:"structured"
```

### 7. cost_budget_lock

```text
id:"basic_fn.cost_budget_lock.v0.2"
status:"stable_candidate"
purpose:"Set the smallest sufficient read, token, and time budget."
input_slots:["task_scope","available_budget?","risk?"]
output_schema:{
  read_limit:"string",
  token_budget:"string",
  time_budget:"string",
  expansion_trigger:"string"
}
forbids:["choosing the live route","read everything by default","unbounded exploration","budget inflation"]
memory_policy:"none"
trace_policy:"min"
```

### 8. dependency_check

```text
id:"basic_fn.dependency_check.v0.2"
status:"stable_candidate"
purpose:"Check required prerequisites without resolving them."
input_slots:["required_dependencies","available_dependencies"]
output_schema:{
  satisfied:"list",
  missing:"list",
  blocked:"boolean",
  next_requirement:"string"
}
forbids:["installing dependencies","fetching resources","guessing availability"]
memory_policy:"none"
trace_policy:"min"
```

## Skill manufacturing pattern

```text
scope_lock
-> input_contract_bind
-> step_sequence_lock
-> output_schema_bind
-> acceptance_criteria_bind
-> fixture_contract_bind
-> memory_policy_check
-> trace_policy_check
-> gate_label
-> handoff_packet_bind
```

Use only the needed functions.
Do not force the whole chain for a small skill.

## One-line rule
The v0.2 basic series lets a skill be assembled from small control contracts instead of one large prompt.

## Stability status
The v0.2 series is currently `stable_candidate`.

It is not final stable.

See:

```text
SKILL_SKELETON_STABLE_CANDIDATE_REVIEW_v0_1.md
```
