# Skill Manufacturing Proofs

## Purpose
This folder tests whether AILO basic functions can manufacture reusable skill skeletons.

The goal is not to prove domain quality.
The goal is to prove the control skeleton:

```text
basic functions -> skill input contract -> step order -> output contract -> acceptance -> fixture -> handoff
```

## Current samples
```text
SOURCE_REVIEW_SKILL_SAMPLE_v0_1/
PROMPT_VALIDATION_SKILL_SAMPLE_v0_1/
WIKI_NOTE_INTAKE_SKILL_SAMPLE_v0_1/
```

## Shared builder
```powershell
python .\skill_skeleton_builder.py .\PROMPT_VALIDATION_SKILL_SAMPLE_v0_1\PROMPT_VALIDATION_SKILL_BUILD_INPUT_v0_1.json
python .\skill_skeleton_builder.py .\WIKI_NOTE_INTAKE_SKILL_SAMPLE_v0_1\WIKI_NOTE_INTAKE_SKILL_BUILD_INPUT_v0_1.json
python .\run_all_skill_manufacturing_proofs.py
python .\run_all_real_trials.py
```

## Boundary
This folder may:
- compose stable basic functions
- compose tested v0.2 skill-skeleton functions
- generate skill cards
- generate proof reports

This folder must not:
- call cognitive functions
- call engines
- use Rust
- use smart routing
- execute the real domain task
- write memory

## Pass condition
Each sample must show:

```text
overall: PASS
function_calls: 12
failed: 0
```

Each real trial must show:

```text
overall: PASS
failed: 0
```
