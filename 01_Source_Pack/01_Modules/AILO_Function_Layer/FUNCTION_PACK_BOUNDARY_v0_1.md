# Function Pack Boundary v0.1

## Purpose

This file defines the middle layer between a single AILO function and larger structures such as skills, engines, and brain components.

## Core Definitions

```text
Function
= one smallest action

Function Pack
= related smallest action-unit group

Function Pack Group
= multiple function packs combined for a larger purpose
```

## Function

A function does one small action.
It is not limited to a fixed inventory.

Existing functions are seeds and examples.
New functions may be created when the action is small, bounded, and has an input/output contract.

Examples:

```text
goal_lock
scope_lock
route_lock
output_shape_lock
evidence_check
uncertainty_split
permission_gate
stop_condition_define
```

A function should not try to become a workflow.

## Function Pack

A function pack groups related small actions.

It is still smaller than a skill or an engine.
It is not a copied list from a global catalog.
It is designed for the current brain, skill, engine, or task surface.

Examples:

```text
Goal Lock Pack
-> goal_lock
-> scope_lock
-> success_criteria_bind

Evidence Check Pack
-> claim_extract
-> evidence_check
-> uncertainty_split

Issue Label Pack
-> issue_detect
-> severity_label
-> blocking_reason_bind
```

The pack is useful when the same small actions are often used together.

## Function Pack Group

A function pack group combines packs for a larger job.

The same group may become different things depending on use.

```text
strict order + intermediate handoff + verification gate
-> Engine

user-callable repeatable procedure
-> Skill

identity + boundary + memory + output contract + operating rules
-> Brain component
```

## Hierarchy

```text
Function
-> Function Pack
-> Function Pack Group
   -> Engine
   -> Skill
   -> Brain component
-> Brain
```

## Difference From Skill

A function pack is not what the user calls directly.

A skill is user-facing.
A function pack is model-facing construction material.

```text
User calls a skill.
Model assembles or uses function packs.
```

## Difference From Engine

A function pack is a group.
An engine is an ordered mechanism.

If the order is optional, it is not an engine.
If the order is strict and each step feeds the next step, it may become an engine.

## Difference From Brain Component

A brain component needs identity and operating boundary.

A function pack only contains actions.

If it starts carrying memory policy, output contract, local rule, or role identity, it is becoming a brain component.

## Promotion Gate

A function pack may be created when:

```text
related_actions:true
repeated_together:true
single_function_insufficient:true
user_facing:false
strict_order_required:false
identity_required:false
```

If `strict_order_required:true`, consider an engine.
If `user_facing:true`, consider a skill.
If `identity_required:true`, consider a brain component.

## Creation Rule

Create a new function only when:

```text
one_small_action:true
input_slots_defined:true
output_schema_defined:true
failure_output_defined:true
existing_function_insufficient:true
```

Create a new function pack only when:

```text
related_actions:true
use_condition_defined:true
output_contract_defined:true
stop_condition_defined:true
fixed_inventory:false
```

Do not treat the seed functions as the full system.
The reusable part is the making rule, not a closed function list.

## Anti-bloat Rule

Do not create a function pack when one function is enough.

Do not create a skill or engine when a function pack is enough.

Do not create a brain component when the work has no identity, memory, or boundary requirement.

## One-line Rule

Function pack is the smallest reusable action group; it is designed from the current purpose and becomes engine, skill, or brain component only when use conditions require that higher layer.
