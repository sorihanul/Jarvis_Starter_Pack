# AILO Engine Boundary v0.1

## Purpose
This document defines what counts as an AILO engine.

It also defines what should remain a function, cognitive function, skill, or material.

## Core definition
An AILO engine is an ordered, guarded, and verified structure built from functions, cognitive functions, skills, or modules.

It exists when order matters.

```text
entry_rule
-> ordered pipeline
-> intermediate state handoff
-> guarded steps
-> output contract
-> verification gate
-> stop rule
```

## What makes it an engine
A structure becomes an engine when:

```text
several operations must run in a fixed order
wrong order creates failure
intermediate outputs feed later steps
the final output contract matters
verification is required
failure conditions are explicit
the process is reusable
```

## Difference from function

```text
function
-> one bounded operation

engine
-> ordered set of operations with verification
```

If one function is enough, do not make an engine.

## Difference from cognitive function

```text
cognitive function
-> one meaning operation

engine
-> multiple operations arranged into a stable process
```

If one thought move is enough, do not make an engine.

## Difference from material

```text
material
-> raw or semi-processed input used by functions, skills, or engines

engine
-> process that transforms material through ordered, guarded steps
```

Material may feed an engine.
Material is not an engine.

Examples of material:

```text
paper text
book summary
worldbuilding note
song prompt sample
session log
source excerpt
```

## Difference from skill

```text
skill
-> user-facing repeatable task procedure

engine
-> internal ordered mechanism with strict input/output and verification
```

A user calls a skill.
A system runs an engine.

A skill may use an engine.
An engine may be wrapped by a skill.

Do not confuse the two.

## What is not an engine
These are not engines yet:

```text
a prompt collection
a checklist
a single function
a single cognitive function
a broad workflow without stable output
a research plan
a folder of examples
a long instruction file with no verification gate
```

## Engine must stay bounded
An engine should do one kind of process.

Examples:

```text
extract intent slots
control route cost
classify document role and read order
compile cognition into engine draft
preprocess paper into engine material
```

Bad engine names:

```text
do all research
make better brain
manage every document
think like an expert
```

Good engine names should show:

```text
process target
transformation type
output type
```

Examples:

```text
IntentSlotExtractionEngine
DocumentRoleReadOrderEngine
DeepCausePreprocessEngine
CostRouteControlEngine
PaperToEngineMaterialEngine
```

## One-line rule
An AILO engine is not a bigger prompt; it is a verified order of operations.
