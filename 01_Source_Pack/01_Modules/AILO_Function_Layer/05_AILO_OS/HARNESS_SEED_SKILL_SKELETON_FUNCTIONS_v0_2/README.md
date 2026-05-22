# Harness Seed Skill Skeleton Functions v0.2

## Purpose
This seed implements the v0.2 basic functions used to manufacture skill skeletons.

It runs eight tested basic functions by explicit `function_id`.

It does not run cognitive functions, engines, or smart routing.

## Supported functions

```text
basic_fn.input_contract_bind.v0.2
basic_fn.step_sequence_lock.v0.2
basic_fn.acceptance_criteria_bind.v0.2
basic_fn.fixture_contract_bind.v0.2
basic_fn.handoff_packet_bind.v0.2
basic_fn.retry_policy_check.v0.2
basic_fn.cost_budget_lock.v0.2
basic_fn.dependency_check.v0.2
```

## Run

```powershell
python .\skill_skeleton_functions_mock_runner.py .\SKILL_SKELETON_FUNCTIONS_FIXTURES_v0_2.json
python .\failure_consistency_check.py
```

Expected:

```text
total:16
passed:16
failed:0
```

Failure consistency expected:

```text
failure_cases:8
passed:8
failed:0
overall:PASS
```

## Boundary

This seed may:
- bind skill inputs
- lock skill step order
- bind acceptance criteria
- bind fixture shape
- bind handoff packet shape
- decide retry policy
- lock cost budget
- check dependencies

This seed must not:
- execute the skill
- judge domain meaning
- infer hidden premise
- call an engine
- write memory
- modify files

## One-line rule
This seed turns repeated skill-building control moves into callable basic functions.
