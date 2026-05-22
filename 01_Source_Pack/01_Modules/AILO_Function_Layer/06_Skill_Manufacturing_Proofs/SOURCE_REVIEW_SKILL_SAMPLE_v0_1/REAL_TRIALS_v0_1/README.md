# Source Review Real Trials v0.1

## Purpose
This folder checks whether the manufactured source-review skill skeleton can handle small source-review inputs.

This is still not a source-review engine.
It is a small rule-based trial to find contract gaps.

## Run
```powershell
python .\source_review_real_trial_runner.py .\SOURCE_REVIEW_REAL_TRIAL_FIXTURES_v0_1.json
```

## Boundary
This trial may:
- read small fixture text
- separate claims, evidence, and uncertainty
- return a bounded review packet

This trial must not:
- read arbitrary folders
- rewrite the source
- call cognitive functions
- call engines
- write memory

## Output
```text
SOURCE_REVIEW_REAL_TRIAL_OUTPUT_v0_1.json
SOURCE_REVIEW_REAL_TRIAL_REPORT_v0_1.md
```
