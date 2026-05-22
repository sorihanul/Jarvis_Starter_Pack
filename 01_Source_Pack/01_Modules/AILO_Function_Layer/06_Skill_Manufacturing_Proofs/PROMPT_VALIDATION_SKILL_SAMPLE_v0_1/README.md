# Prompt Validation Skill Sample v0.1

## Purpose
This sample tests whether AILO basic functions can manufacture a prompt-validation skill skeleton.

It does not validate a real prompt.
It only builds the control contract for a future prompt-validation skill.

## Run
```powershell
cd ..\06_Skill_Manufacturing_Proofs
python .\skill_skeleton_builder.py .\PROMPT_VALIDATION_SKILL_SAMPLE_v0_1\PROMPT_VALIDATION_SKILL_BUILD_INPUT_v0_1.json
```

## Boundary
This sample must not:
- rewrite the prompt
- judge prompt quality through cognitive functions
- call an engine
- write memory

## One-line rule
This sample builds the skeleton of a prompt-validation skill; it does not perform prompt validation yet.
