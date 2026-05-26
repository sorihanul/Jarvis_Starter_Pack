# AILO Function System

## One-line identity
AILO Function System starts from functions, groups related actions into function packs, then promotes pack groups into cognitive functions, engines, skills, brain components, or OS-level runtime only when needed.

## Why this exists
The three concepts are related, but they should not be merged.

```text
AILO function
  one smallest callable action

AILO function pack
  related smallest action-unit group

AILO cognitive function
  one bounded meaning operation

AILO engine
  ordered set of functions or function packs with guards, output contract, intermediate handoff, and verification

AILO skill
  user-callable repeatable procedure built from functions or function packs

AILO brain component
  identity, boundary, memory, output contract, and operating rules built around function packs

AILO OS
  operating layer that actually runs, records, validates, governs, and packages functions, skills, and engines
```

Read `BASIC_AND_COGNITIVE_FUNCTION_CONCEPT_v0_1.md` before expanding a function into a cognitive function.
Read `FUNCTION_PACK_BOUNDARY_v0_1.md` before turning related functions into a skill, engine, or brain component.
Read `FUNCTION_PACK_BUILD_CARD_v0_1.md` when you need to build one purpose-specific function pack quickly.
Read `AILO_N_FRAME_USE_RULES_v0_1.md` before creating or promoting persistent frames.
Read `AILO_N_PRACTICAL_USE_CARD_v0_1.md` when repeated targets need noun-slot frames before verbs or function packs act on them.

The full AILO-N source is stored in:

```text
01_Source_Pack/00_Core/AILO_N_NOMINAL_FRAME_LAYER_v0_9N.md
```

Do not read the full AILO-N source by default.
Open it only for canonical slot disputes, relation contracts, formal mapping, validation-code details, or knowledge-pack shape.

## Research allocation

```text
AILO functions
-> shared lower function layer and function-pack layer
-> public subset may be carried by Jarvis v3

AILO cognitive functions
-> advanced cognitive expansion lane

AILO engines
-> advanced engine expansion lane
```

## Folder roles
- `01_AILO_Functions`: shared small operational functions for basic and full cognitive paths
- `02_AILO_Cognitive_Functions`: brain-local thought functions and card rules
- `03_AILO_Engines`: compiled engines and engine criteria
- `04_Research_Notes`: discussion notes, import notes, and unresolved questions
- `05_AILO_OS`: boundary between document/spec and actual operating layer
- `AILO_N_FRAME_USE_RULES_v0_1.md`: guardrails for when to create, promote, merge, or discard noun frames
- `AILO_N_PRACTICAL_USE_CARD_v0_1.md`: short runtime card for AILO-N noun-frame usage

## Boundary
This is a research and concept separation hub.

Promoted source rules remain in this package's public source layer.
This module does not require any external private source tree.
```text
01_Source_Pack
```

Reusable material remains in public source modules or option packs.
```text
01_Source_Pack/01_Modules
```

Active extraction and tests remain in package-local proof or task surfaces.
```text
01_Source_Pack/01_Modules/AILO_Function_Layer
```

## One-line rule
Function is the smallest operation, function pack is the smallest reusable action group, cognitive function is a meaning operation, engine is an ordered and verified execution structure, skill is the user-callable procedure, brain component carries identity and boundary, and OS begins only when there is a runner.
