# Switching Coding Pack

## Purpose

This option pack helps Jarvis use coding roles that actually work:

```text
read the task
choose one coding lens
lock file scope
make a small patch or handoff prompt
verify against the success criteria
return a bounded report
```

It is not an automatic coding team.
It does not pretend that one brain can remotely control another brain.
It does not replace tests, repository rules, or user approval.

## Operating Idea

Coding work fails when the same model tries to be every role at once.

This pack separates the roles as temporary lenses:

```text
intake lens      -> understand the request and success criteria
implement lens   -> make the smallest useful code change
review lens      -> look for bugs, regressions, missing tests
verify lens      -> run or describe checks against success criteria
release lens     -> prepare a short user-facing summary
handoff lens     -> write a bounded prompt for another thread or agent
```

## What This Pack Does

```text
switch:
  choose the coding lens for the next step

scope:
  lock files, commands, and no-go areas

patch:
  keep implementation small and reversible

review:
  inspect behavior, tests, risks, and boundary violations

verify:
  compare result against the success criteria

handoff:
  create a prompt for a separate coding/review thread when needed
```

## What This Pack Does Not Do

```text
does not create a real autonomous coding team
does not run tools without the host environment
does not bypass approval or repository policy
does not replace dedicated project tests
does not make broad refactors by default
does not make every coding task multi-role
```

## First Read

```text
1. README.md
2. ACTIVATION_RULE.md
3. INPUT_SLOTS.md
4. OPERATING_RULE.md
5. CODING_LENS_SET.md
6. HOST_WORKSPACE_USE.md
7. TOML_ROLE_SAMPLES.md
8. HANDOFF_PROMPT_TEMPLATES.md
9. OUTPUT_CONTRACT.md
10. STOP_RULE.md
11. VALIDATION_RULE.md
12. ACCEPTANCE_TESTS.md
```

## Recommended Pairing

```text
file write, shell, browser, or network action
-> Action_Permission_Pack

must prove success or avoid regression
-> Verification_and_Proof_Pack

separate thread or brain handoff
-> Brain_Routing_and_Handoff_Pack

external code, docs, or repo pattern import
-> Source_Command_Filter_Pack + Capability_Import_Pack
```

## Completion Rule

This pack is usable when a new reader can answer:

```text
what is the coding goal?
which lens is active now?
which files are in scope?
what must not be touched?
what is the smallest valid change?
how will it be checked?
what remains risky?
```
