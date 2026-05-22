# Non-Rust Mini Harness v0.1

## Purpose
This is the first reusable local entrypoint for the stable AILO basic functions.

It wraps the stable basic function mock runner without starting Rust.

## Commands

Run the default fixture suite:

```powershell
python .\ailo_mini_harness.py run-fixtures
```

Run one input file:

```powershell
python .\ailo_mini_harness.py run-one .\SAMPLE_SCOPE_LOCK_INPUT_v0_1.json
```

Run the skill-skeleton function series:

```powershell
python .\ailo_mini_harness.py run-skill-series
```

## Boundary

This mini harness may:
- run the seven stable basic functions by explicit `function_id`
- run the v0.2 skill-skeleton basic functions by explicit `function_id`
- run fixture suites
- emit result and trace

It must not:
- infer which function the user meant
- call cognitive functions
- call engines
- write memory
- modify files
- become a Rust project

## One-line rule
This is the non-Rust starting point for observing stable basic function behavior.
