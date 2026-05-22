# Function Pack Promotion Matrix v0.1

## Purpose

This file explains when function packs stay as packs, and when they should become an engine, skill, or brain component.

## Base Rule

```text
Function Pack
= related small actions

Engine
= ordered mechanism with intermediate handoff and verification

Skill
= user-callable repeatable procedure

Brain Component
= identity, boundary, memory, output contract, and operating rules
```

## Stay As Function Pack

Keep it as a function pack when:

```text
one small action group is enough
user does not need to call it by name
no strict step order is required
no persistent identity is required
no live memory surface is required
```

Example:

```text
User: "이 요청 범위만 잠가줘."
Use: Goal and Scope Pack
Do not create: full verification skill or new brain
```

## Promote To Engine

Promote to engine when:

```text
strict_order_required:true
intermediate_handoff_required:true
verification_gate_required:true
wrong_order_breaks_result:true
```

Example:

```text
Goal and Scope Pack
-> Read Route Pack
-> Evidence and Uncertainty Pack
-> Output Contract Pack
-> verification gate

Result:
Source Review Engine
```

Why:
The output of each pack becomes the input of the next pack.
If the order changes, the result becomes less reliable.

## Promote To Skill

Promote to skill when:

```text
user_calls_it_repeatedly:true
procedure_name_needed:true
examples_needed:true
acceptance_tests_needed:true
```

Example:

```text
Goal and Scope Pack
-> Output Contract Pack
-> Evidence and Uncertainty Pack

Result:
Prompt Validation Skill
```

Why:
The user wants a repeatable named procedure, not just internal construction material.

## Promote To Brain Component

Promote to brain component when:

```text
identity_required:true
boundary_required:true
memory_surface_required:true
output_contract_required:true
operating_rule_required:true
```

Example:

```text
Goal and Scope Pack
-> Read Route Pack
-> Output Contract Pack
-> Permission and Stop Pack

Result:
Research Brain Intake Component
```

Why:
The component becomes part of how a brain behaves every time it starts work.

## Do Not Promote

Do not promote when:

```text
one_function_is_enough:true
single_use_only:true
no_repeated_pattern:true
no_test_fixture:true
```

Example:

```text
User: "짧게 요약해줘."
Use: direct response or one output shape function
Do not create: summary pack, summary engine, or summary brain
```

## Decision Table

```text
Is it one action?
-> Function

Are several small actions usually used together?
-> Function Pack

Does order matter and each step feed the next?
-> Engine

Will the user call it as a named procedure?
-> Skill

Does it need identity, memory, boundary, and output contract?
-> Brain Component
```

## One-line Rule

Function packs are construction material; promotion happens only when the use case requires order, user-callability, or identity.
