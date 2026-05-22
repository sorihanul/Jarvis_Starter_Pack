# Wiki Note Intake Real Trials v0.1

## Purpose
This folder checks whether the manufactured wiki-note-intake skill skeleton can handle small raw-note inputs.

This is still not a wiki engine.
It is a small rule-based trial to find contract gaps.

## Run
```powershell
python .\wiki_note_intake_real_trial_runner.py .\WIKI_NOTE_INTAKE_REAL_TRIAL_FIXTURES_v0_1.json
```

## Boundary
This trial may:
- read small raw-note fixtures
- produce candidate-only wiki packets
- check source trace
- check canon-promotion boundary

This trial must not:
- edit a real wiki
- promote canon memory
- call cognitive functions
- call engines
- write memory

## Output
```text
WIKI_NOTE_INTAKE_REAL_TRIAL_OUTPUT_v0_1.json
WIKI_NOTE_INTAKE_REAL_TRIAL_REPORT_v0_1.md
```
