# Wiki Note Intake Skill Sample v0.1

## Purpose
This sample tests whether AILO basic functions can manufacture a wiki-note-intake skill skeleton.

It does not wikiize a real note.
It only builds the control contract for a future wiki-note-intake skill.

## Run
```powershell
cd ..\06_Skill_Manufacturing_Proofs
python .\skill_skeleton_builder.py .\WIKI_NOTE_INTAKE_SKILL_SAMPLE_v0_1\WIKI_NOTE_INTAKE_SKILL_BUILD_INPUT_v0_1.json
```

## Boundary
This sample must not:
- edit a real wiki
- promote canon memory
- call cognitive functions
- call an engine
- write memory

## One-line rule
This sample builds the skeleton of a wiki-note-intake skill; it does not perform wikiization yet.
