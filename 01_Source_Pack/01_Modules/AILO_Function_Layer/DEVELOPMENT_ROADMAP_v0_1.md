# AILO Function System Development Roadmap v0.1

## Purpose
This roadmap fixes the development paths.

There are two valid paths.

## Path A: Basic runtime route

```text
AILO function system
-> Rust-based AILO OS
```

Use this path when the goal is to prove that AILO can become a runnable operating layer.

Default core:
```text
AILO E++
```

Meaning:
- use the public/common AILO intent language as the base
- keep the function set small
- prove parser, registry, runner, trace, and CLI first
- do not require the advanced cognitive expansion kernel

This path focuses on:
- parser
- function registry
- function runner
- trace
- schema validation
- minimal CLI

It does not require full cognitive function or engine design first.

## Path B: Cognitive expansion route

```text
AILO function system
-> AILO cognitive function system
-> AILO engine system
-> Rust-based AILO OS
```

Use this path when the goal is to build the full cognitive expansion direction.

Default core:
```text
AILO cognitive expansion core
```

Meaning:
- use the advanced cognitive expansion kernel as the base
- include cognitive functionization
- include engine compilation
- include deeper memory, trace, validation, and multi-layer operating rules

This path focuses on:
- brain-local cognitive functions
- reusable thought operations
- ordered engine pipelines
- engine verification
- later Rust runtime support

## Default rule
Default to Path B for advanced cognitive expansion research.

Use Path A when the goal is an early runnable proof.

## Core assignment rule

```text
Path A
-> AILO E++ based
-> basic runtime route

Path B
-> AILO cognitive expansion based
-> cognitive expansion route
```

Do not mix the two defaults.

Path A may borrow ideas from the cognitive expansion route only after they are reduced to E++-level function contracts.

Path B may use E++ as a surface, but its source identity is cognitive expansion.

## Stage 1: AILO function system

### Goal
Make small AILO operations stable.

This stage is the common layer used by both paths.

```text
Path A
-> basic function

Path B
-> basic function
-> cognitive function expansion
```

### First flag
```text
AILO E++ based AILO function system
```

Start here before pulling in the cognitive function system.

First read:
```text
01_AILO_Functions/AILO_FUNCTION_SYSTEM_FLAG_v0_1.md
01_AILO_Functions/AILO_FUNCTION_MINIMUM_SET_v0_1.md
```

### Main target
```text
shared lower function layer
```

Jarvis v2 is the public/basic application lane for this layer.
Advanced cognitive expansion uses the same layer as the lower contract before cognitive functions.

### What belongs here
- scope lock
- route lock
- missing slot detection
- output schema binding
- memory policy check
- trace policy check
- permission label
- simple gate judgment

### Success condition
An AILO function has:
```text
name
purpose
input_slots
operation
output_schema
guards
memory_policy
trace_policy
test fixture
```

## Stage 2: AILO cognitive function system

### Goal
Make small thought operations reusable by a brain.

This is not a second basic set.
This is the expansion layer above the common basic function layer.

### Expansion bridge
Bring this layer in through:
```text
02_AILO_Cognitive_Functions/FUNCTION_TO_COGNITIVE_EXPANSION_BRIDGE_v0_1.md
```

Do not import the cognitive layer before the basic function layer has a small proof.

### Main target
```text
brain-local cognitive lane
```

### What belongs here
- hidden premise recovery
- evidence authority check
- route cost judgment
- broad verb detection
- lens extraction
- contradiction split
- source role judgment

### Success condition
A cognitive function has:
```text
brain_owner
trigger_condition
input_slots
operation
output_schema
validation
memory_policy
cost_class
```

## Stage 3: AILO engine system

### Goal
Compile functions and cognitive functions into ordered, verified structures.

### Main target
```text
brain-local engine lane
```

### What belongs here
- intent slot extraction engine
- route cost control engine
- document role/read order engine
- cognition to engine compiler
- paper to engine preprocessor
- lens to skill/engine compiler

### Success condition
An engine has:
```text
entry_rule
pipeline
module_slots
output_contract
guards
verification_gate
failure_conditions
stop_rule
test fixture
```

## Stage 4: Rust-based AILO OS

### Goal
Move from document/spec into a runnable operating layer.

### Main target
```text
implementation/runtime lane
```

### Why Rust
Rust fits the deterministic layer:
- parser
- canonical object conversion
- registry
- runner
- trace
- permission policy
- package export/import
- validation gate

### What Rust should not own
Rust should not own:
- natural language interpretation
- creative judgment
- domain reasoning
- brain identity
- prose writing

Those remain LLM/brain/document-layer work.

### Minimal prototype seed
Do not start with full OS.

Start with:
```text
parser
function registry
function runner
trace output
schema validation
small CLI
test fixture
```

This minimal seed belongs to Path A.

Full AILO OS belongs to Path B after engine proof.

### Success condition
AILO OS prototype exists only when:
```text
ailo parse
ailo fn register
ailo fn run
ailo trace show
ailo test
```

can run in a repeatable way.

## Development rule
Each path must produce proof before the next stage.

```text
Path A:
function proof
-> Rust OS prototype seed

Path B:
function proof
-> cognitive function proof
-> engine proof
-> Rust OS prototype proof
```

## One-line rule
Basic function is the common layer. Cognitive function is the expansion layer. There is a fast route from basic functions to an AILO OS prototype, and a full route from basic functions to cognitive functions to engines to AILO OS.
