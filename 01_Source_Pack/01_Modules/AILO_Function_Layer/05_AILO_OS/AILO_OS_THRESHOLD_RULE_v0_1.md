# AILO OS Threshold Rule v0.1

## Purpose
This rule prevents calling a document system an OS too early.

## Four states

```text
1. OS idea
   concept only

2. OS spec
   documents define components and contracts

3. OS prototype
   parser, registry, runner, trace, and package surface exist

4. OS runtime
   stable operation, validation, permission, memory, packaging, and replay are actually used
```

## Current naming rule

Use these names precisely:

```text
document-only
-> AILO OS concept or AILO OS spec

parser + registry only
-> AILO OS prototype seed

parser + registry + function runner + trace
-> AILO OS prototype

function runner + skill runner + engine runner + validation + permission + memory policy + releasepack
-> AILO OS runtime
```

## Minimum OS prototype
Do not call it an OS prototype unless it has:

```text
input parser
function registry
function runner
trace output
error surface
small test fixture
```

## Minimum OS runtime
Do not call it an OS runtime unless it has:

```text
parser
function registry
skill registry
engine runner
tool permission policy
validation gate
memory side-effect policy
trace or replay surface
release/package surface
acceptance tests
```

## Important boundary
Markdown can define AILO OS.

Markdown cannot be AILO OS by itself.

The OS begins when the operating path is executable, replayable, or at least reproducible by a runner.

## Failure cases
Fail the OS label when:
- there is no parser
- there is no registry
- there is no runner
- there is no trace
- memory writes are not controlled
- permission policy is only prose
- validation is only an opinion
- releasepack means only a folder copy

## Correct next step
If the current state is document-only, do not pretend it is a runtime.

Instead produce:
```text
AILO OS spec
-> minimal prototype requirements
-> first runner target
-> acceptance test
```

## One-line rule
AILO OS is allowed as a concept now, but it becomes real only when there is a runner.
