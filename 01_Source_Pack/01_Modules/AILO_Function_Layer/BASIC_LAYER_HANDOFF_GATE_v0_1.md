# Basic Layer Handoff Gate v0.1

## Purpose
This gate decides what can happen after the AILO basic function layer is stable.

It prevents two mistakes:
- adding more basic functions too early
- jumping into runtime implementation when the need is actually meaning work

## Current state

```text
basic_function_layer:"PASS_STABLE"
stable_set:[
  "scope_lock",
  "missing_slot_detect",
  "route_lock",
  "output_schema_bind",
  "memory_policy_check",
  "trace_policy_check",
  "gate_label"
]
```

## First decision

After the stable basic layer, choose one route:

```text
Route A: harness seed
Route B: cognitive expansion
Route C: candidate intake
Route D: engine design
```

Do not open all routes.

## Handoff output contract

Every handoff decision must produce this shape:

```text
handoff_decision:"harness_seed | cognitive_expansion | candidate_intake | engine_design | stay_basic | hold"
reason:"why this route is the smallest correct next route"
required_next_file:"relative path to the first file to read"
blocked_routes:[
  "routes that must not be opened in this turn"
]
stop_rule:"where to stop before the task grows"
```

If the input is not enough to choose a route, return:

```text
handoff_decision:"hold"
reason:"missing target"
required_next_file:"BASIC_LAYER_HANDOFF_GATE_v0_1.md"
blocked_routes:["harness_seed","cognitive_expansion","candidate_intake","engine_design"]
stop_rule:"ask for the next target instead of guessing"
```

## Decision fixtures

### Fixture 1: prove execution

Input:

```text
basic function is stable; prove one function can run
```

Output:

```text
handoff_decision:"harness_seed"
reason:"the goal is executable proof, not new meaning work"
required_next_file:"05_AILO_OS/AILO_OS_HARNESS_SEED_EXECUTION_CONTRACT_v0_1.md"
blocked_routes:["cognitive_expansion","candidate_intake","engine_design"]
stop_rule:"stop after one-function deterministic harness contract"
```

### Fixture 2: recover hidden premise

Input:

```text
build a function that recovers unstated assumptions behind a claim
```

Output:

```text
handoff_decision:"cognitive_expansion"
reason:"the requested move interprets meaning and hidden premise"
required_next_file:"02_AILO_Cognitive_Functions/FUNCTION_TO_COGNITIVE_EXPANSION_BRIDGE_v0_1.md"
blocked_routes:["harness_seed","candidate_intake","engine_design"]
stop_rule:"define one brain-local cognitive function candidate only"
```

### Fixture 3: add new control move

Input:

```text
add a new function that selects report length
```

Output:

```text
handoff_decision:"candidate_intake"
reason:"this is a new control move and must pass the candidate gate first"
required_next_file:"01_AILO_Functions/BASIC_FUNCTION_WORKSPACE/BASIC_FUNCTION_CANDIDATE_GATE_v0_1.md"
blocked_routes:["harness_seed","cognitive_expansion","engine_design"]
stop_rule:"compare against existing stable functions before adding anything"
```

### Fixture 4: ordered process

Input:

```text
run scope, route, evidence check, report shape, and validation in a fixed order
```

Output:

```text
handoff_decision:"engine_design"
reason:"the requested structure needs ordered steps and verification gates"
required_next_file:"03_AILO_Engines/AILO_ENGINE_BOUNDARY_v0_1.md"
blocked_routes:["harness_seed","cognitive_expansion","candidate_intake"]
stop_rule:"define the engine boundary before naming an engine"
```

## Route A: harness seed

Use this when the goal is:

```text
prove that one basic function can be parsed, selected, run, traced, and validated
```

Required first read:

```text
05_AILO_OS/AILO_OS_HARNESS_SEED_TARGET_v0_1.md
05_AILO_OS/AILO_OS_HARNESS_SEED_EXECUTION_CONTRACT_v0_1.md
```

Allowed work:
- define runner object shape
- define registry object shape
- define trace object shape
- define small fixture
- implement later only after the contract is accepted

Forbidden:
- cognitive interpretation
- engine pipeline
- smart router
- memory write
- final task execution

## Route B: cognitive expansion

Use this when the goal is:

```text
handle repeated meaning work that basic functions must not perform
```

Required first read:

```text
02_AILO_Cognitive_Functions/FUNCTION_TO_COGNITIVE_EXPANSION_BRIDGE_v0_1.md
02_AILO_Cognitive_Functions/AILO_COGNITIVE_FUNCTION_BOUNDARY_v0_1.md
02_AILO_Cognitive_Functions/AILO_COGNITIVE_FUNCTION_CONTRACT_v0_1.md
```

Allowed work:
- define one brain-local cognitive function candidate
- define trigger condition
- define one meaning operation
- define output schema
- define failure output

Forbidden:
- globalize a local cognitive function immediately
- build a whole skill as one cognitive function
- run an engine
- bypass basic function wrapper

## Route C: candidate intake

Use this when a new basic-function idea appears.

Required first read:

```text
01_AILO_Functions/BASIC_FUNCTION_WORKSPACE/BASIC_FUNCTION_CANDIDATE_GATE_v0_1.md
```

Allowed work:
- record candidate
- compare against the stable seven functions
- decide merge, reject, send to cognitive layer, or keep candidate

Forbidden:
- direct promotion
- duplicate names
- adding a function because a topic sounds important

## Route D: engine design

Use this when multiple functions or cognitive functions must run in a strict order with verification gates.

Required first read:

```text
03_AILO_Engines/AILO_ENGINE_BOUNDARY_v0_1.md
03_AILO_Engines/AILO_ENGINE_CONTRACT_v0_1.md
03_AILO_Engines/AILO_ENGINEIZATION_PRINCIPLES_v0_1.md
```

Allowed work:
- define ordered pipeline
- define intermediate state handoff
- define verification gate
- define stop rule

Forbidden:
- calling a checklist an engine
- building an engine when one function is enough
- skipping output contract

## Default recommendation

If the next task is about proving execution:

```text
choose Route A
```

If the next task is about hidden premise, evidence, contradiction, lens, or reading posture:

```text
choose Route B
```

If the next task is a new small control move:

```text
choose Route C
```

If the next task needs ordered internal process:

```text
choose Route D
```

## One-line rule
After `PASS_STABLE`, do not keep polishing the basic layer by default; choose harness seed, cognitive expansion, candidate intake, or engine design by the actual next need.
