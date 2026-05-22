# Code as Agent Harness Reading Note v0.1

## Source
- arXiv: `2605.18747`
- Title: `Code as Agent Harness`
- URL: `https://arxiv.org/abs/2605.18747`
- Type: survey / framing paper

## Why this matters here
This paper gives an outside vocabulary for the AILO expansion direction.

The useful point is not that every AI system must become code.
The useful point is that a reliable agent needs a harness around the model.

In this paper, code is treated as the harness medium because code can be:

```text
executable
inspectable
stateful
governed
```

This matches the AILO expansion route:

```text
AILO function
-> AILO cognitive function
-> AILO engine
-> AILO OS
```

## Core interpretation

The paper's central move:

```text
code is not only model output
code is also the operating substrate around the model
```

Translated into this system:

```text
prompt/document
-> describes desired behavior

harness
-> makes behavior runnable, inspectable, stateful, and governed
```

## Three-layer taxonomy

### 1. Harness Interface

Code connects the model to:

```text
reasoning
acting
environment modeling
```

System translation:

```text
reasoning
-> executable reasoning artifact

acting
-> tool/action/program surface

environment modeling
-> state, trace, repository, simulator, test, or log surface
```

### 2. Harness Mechanisms

The harness needs:

```text
planning
memory
tool use
execution feedback
control
optimization
```

System translation:

```text
basic function
-> control surface

cognitive function
-> meaning operation

engine
-> ordered verified mechanism

OS
-> runner + registry + trace + permission + validation + memory policy
```

### 3. Scaling the Harness

Multi-agent systems need shared state.

The paper's useful warning:

```text
shared logs are not enough
shared state must preserve assumptions, versions, read/write sets, conflicts, and verification obligations
```

System translation:

```text
multi-agent orchestration without shared-state contract
-> drift risk

shared state with read/write/assumption/version/verification records
-> harness-grade coordination
```

## Strongest takeaways for AILO expansion

### 1. AILO OS needs a runner

Documents can define the system.
They are not the OS by themselves.

AILO OS begins when:

```text
parser
registry
runner
trace
permission
validation
memory policy
package/release surface
```

exist as runnable or reproducible surfaces.

### 2. Verification must declare scope

Executable feedback can mislead.

```text
green test
!= full correctness
```

Every verifier should declare:

```text
what it checks
what it cannot check
what confidence it gives
what assumptions remain
```

This supports the existing `failure_output`, `validation`, `trace_policy`, and `memory_policy` direction.

### 3. Harness mutation must carry a change contract

Self-improving harness work is risky unless each change states:

```text
changed_component
target_failure
predicted_improvement
preserved_invariants
falsification_test
rollback_path
```

This should guide future AILO OS runner evolution.

### 4. Shared state must be transactional enough

For multi-agent or multi-thread work, each action should eventually record:

```text
read_set
write_set
assumptions
version_dependencies
verifier_obligations
conflict_policy
```

This is not needed for every document now.
It becomes relevant when AILO moves from document design to executable harness.

### 5. Safety is harness state

Human approval should not be only a chat interruption.
High-risk approvals or rejections should become durable state.

Minimum future shape:

```text
proposed_action
evidence_shown
risk_surface
approval_or_rejection
responsibility_boundary
future_policy_effect
```

## What not to import

Do not import the paper's full survey taxonomy as a new folder structure.

Do not rename the AILO expansion path around this paper.

Do not treat code harness as mandatory for every brain.

This note is a lens for the AILO OS threshold, not a replacement for AILO function / cognitive function / engine boundaries.

## Placement in current system

```text
Basic function
-> controls execution shape

Cognitive function
-> interprets meaning surface

Engine
-> orders guarded operations with verification

AILO OS
-> makes those operations runnable, inspectable, stateful, and governed
```

## One-line rule
Code-as-agent-harness supports the AILO expansion path by clarifying that AILO OS starts only when AILO functions, cognitive functions, and engines become runnable, inspectable, stateful, and governed.
