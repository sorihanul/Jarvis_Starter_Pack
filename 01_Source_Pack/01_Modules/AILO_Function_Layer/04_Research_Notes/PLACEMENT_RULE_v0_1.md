# Placement Rule v0.1

## Purpose
This note decides where a classified AILO operation should go.

Classification alone is not enough.
After classification, the artifact must be placed in the correct lane.

## Placement map

```text
AILO function
-> shared lower function layer
-> lightweight control contract
-> slot, format, route, policy, gate, trace

AILO cognitive function
-> brain-local cognitive lane
-> bounded thought operation
-> owned by a specific brain grain

AILO engine
-> brain-local engine lane
-> ordered execution structure
-> guards, output contract, verification, stop rule

AILO OS
-> implementation/runtime lane
-> parser, registry, runner, trace, permission, validation, memory policy, release surface
```

## AILO function placement

Place here when the operation is small and control-facing:
```text
scope lock
route lock
missing slot detection
schema binding
memory policy check
trace policy check
permission gate label
```

Primary target:
```text
shared AILO function set
```

Reason:
- it is the common layer used before both the basic runtime route and the cognitive expansion route
- it keeps public harness operation light when used by Jarvis v2
- it reduces model interpretation drift
- it does not require engine machinery

Jarvis v2 may carry a public/basic subset.
Advanced cognitive expansion may reuse the same lower contract before adding cognitive functions.

Do not promote a simple AILO function into an engine unless order, verification, and reusable output contract are required.

## AILO cognitive function placement

Place here when the operation changes how a model reads, judges, or transforms meaning.

Primary target:
```text
individual F brain local function set
```

Reason:
- each brain has its own evidence standard, output standard, and grain
- the same operation name can mean different things in different brains
- a global cognitive function warehouse becomes hard to route

Promote the making rule to the public source layer only when it becomes generally useful.
Do not promote every local function itself into the public source layer.

## AILO engine placement

Place here when several functions or skills must run in a stable order.

Primary target:
```text
brain-local engines/
```

Possible source promotion:
```text
01_Source_Pack/01_Modules/AILO_Function_Layer/03_AILO_Engines
```

Only promote to the public engine layer when the engine is useful as a general source pattern.

## Skill boundary

Make a skill when:
- several functions are repeatedly used together
- the user-facing task is clear
- the output is stable enough to test

Make an engine when:
- ordering matters
- wrong order creates failure
- verification and stop rules are required

Call it AILO OS only when:
- a runner exists
- functions can be registered or selected
- execution leaves trace
- permission and memory side effects are governed
- validation is part of the operating path

## Workbench rule

Unproven artifacts start in:
```text
package-local proof or task surfaces
```

Source material stays in:
```text
public source modules or option packs
```

Promoted rules or general engines go to:
```text
public source layer
```

## One-line rule
Classify the operation first, then place it by cost, depth, owner, and verification requirement.
