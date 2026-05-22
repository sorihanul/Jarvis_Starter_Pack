# Prompt Validation Real Trials v0.1

## Purpose
This folder checks whether the manufactured prompt-validation skill skeleton can be used against small real prompt inputs.

This is still not a full prompt-validation engine.
It is a small rule-based trial to find contract gaps.

## Run
```powershell
python .\prompt_validation_real_trial_runner.py .\PROMPT_VALIDATION_REAL_TRIAL_FIXTURES_v0_1.json
```

## Boundary
This trial may:
- read small prompt fixtures
- check declared purpose
- check output contract markers
- check obvious instruction conflict
- return a compact validation report

This trial must not:
- rewrite the prompt
- call cognitive functions
- call engines
- write memory
- claim expert prompt-quality judgment

## Output
```text
PROMPT_VALIDATION_REAL_TRIAL_OUTPUT_v0_1.json
PROMPT_VALIDATION_REAL_TRIAL_REPORT_v0_1.md
```
