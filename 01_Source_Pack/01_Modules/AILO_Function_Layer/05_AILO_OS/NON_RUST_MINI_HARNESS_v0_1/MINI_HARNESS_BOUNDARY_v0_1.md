# Mini Harness Boundary v0.1

## Purpose
Define what the non-Rust mini harness is allowed to do.

## Included

```text
explicit function_id execution
stable seven-function registry
fixture test execution
single input execution
result emission
trace emission
```

## Excluded

```text
semantic routing
function recommendation
cognitive interpretation
engine pipeline
memory persistence
source file modification
Rust packaging
```

## Why this boundary exists

The goal is to observe behavior before freezing it into Rust.

If this layer becomes too smart, Rust will freeze the wrong shape.

## One-line rule
The mini harness is a testable behavior surface, not the final OS.
