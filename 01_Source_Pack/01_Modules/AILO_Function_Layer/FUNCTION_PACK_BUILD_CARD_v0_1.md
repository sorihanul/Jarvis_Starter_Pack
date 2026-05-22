# Function Pack Build Card v0.1

## Purpose

Use this card when a model must create one function pack quickly without reading the whole AILO Function Layer.

This is not a function pack catalog.
It is the minimum build shape for making a purpose-specific function pack.

## Build Order

```text
1. purpose
2. use_when
3. do_not_use_when
4. input_condition
5. functions
6. output_contract
7. stop_condition
8. failure_output
9. promotion_condition
```

## Pack Shape

```text
function_pack:
  name:
  purpose:
  use_when:
  do_not_use_when:
  input_condition:
  functions:
    - name:
      action:
      input_slots:
      output:
      failure:
  output_contract:
  stop_condition:
  failure_output:
    ok:false
    reason:
    missing_slots:
    next_pack:
    stop_condition:
  promotion_condition:
```

## Pass Conditions

```text
related_actions:true
one_small_purpose:true
input_condition_defined:true
output_contract_defined:true
stop_condition_defined:true
failure_output_defined:true
fixed_inventory:false
user_facing:false
strict_order_required:false
identity_required:false
```

## Escalation

```text
strict_order_required:true
-> consider engine

user_facing:true
-> consider skill

identity_required:true or memory_surface_required:true
-> consider brain component

one_function_enough:true
-> do not create a function pack

single_use_only:true
-> do not promote the pack
```

## Anti-Bloat Rule

```text
do_not_grow_one_function_forever:true
prefer_new_purpose_pack_when_repeated:true
single_use_request_is_not_new_pack:true
stable_output_contract_required:true
stop_condition_required:true
```

## Minimal Example

```text
function_pack:
  name: Source Route Pack
  purpose: choose which source surface to read first
  use_when: task has multiple possible source surfaces
  do_not_use_when: only one obvious source exists
  input_condition:
    request:
    available_sources:
  functions:
    - name: source_candidate_list
      action: list possible source surfaces
      input_slots: [request, available_sources]
      output: candidate_sources
      failure: no_source_surface
    - name: first_source_select
      action: choose the first source to open
      input_slots: [candidate_sources, task_goal]
      output: first_source
      failure: ambiguous_priority
  output_contract:
    first_source:
    why_first:
    do_not_read_yet:
  stop_condition: no reliable source can be selected
  failure_output:
    ok:false
    reason:
    missing_slots:
    next_pack:
    stop_condition:
  promotion_condition: repeated routing need with stable source classes
```

## One-Line Rule

```text
Build one small action group with clear input, output, stop, and failure.
If it becomes a workflow, user-facing procedure, or identity surface, promote it instead of bloating the pack.
```
