# Source Review Skill Sample v0.1

## Purpose
This sample proves the idea:

```text
basic functions -> skill skeleton
```

It builds a `source_review_skill` skeleton by composing stable basic functions and v0.2 skill-skeleton functions.

It does not execute the skill.
It only manufactures the skill contract.

## Skill target

```text
skill_id:"skill.source_review.v0.1"
goal:"review one source file and produce a bounded evidence-backed report"
```

## Function chain

```text
scope_lock
input_contract_bind
dependency_check
cost_budget_lock
step_sequence_lock
output_schema_bind
acceptance_criteria_bind
fixture_contract_bind
memory_policy_check
trace_policy_check
gate_label
handoff_packet_bind
```

## Run

```powershell
cd ..\06_Skill_Manufacturing_Proofs
python .\skill_skeleton_builder.py .\SOURCE_REVIEW_SKILL_SAMPLE_v0_1\SOURCE_REVIEW_SKILL_BUILD_INPUT_v0_1.json
```

## Outputs

```text
SOURCE_REVIEW_SKILL_BUILD_INPUT_v0_1.json
SOURCE_REVIEW_SKILL_BUILD_OUTPUT_v0_1.json
SOURCE_REVIEW_SKILL_CARD_v0_1.md
SOURCE_REVIEW_SKILL_PROOF_REPORT_v0_1.md
```

## Boundary

This sample may:
- assemble a skill skeleton
- produce a skill card
- show each function output
- verify required sections

It must not:
- review a real source file
- call cognitive functions
- call an engine
- write memory
- modify outside this sample folder

## One-line rule
This sample builds the skeleton of a skill from basic functions; it does not perform the skill's real work.
