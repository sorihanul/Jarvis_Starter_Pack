# Conservative Operation Loop

## purpose

This document defines the default repair loop for coding work.
The loop is not a product claim, a shortcut, or proof that the template has been validated in real projects.
It is a conservative procedure for checking whether a program fits its stated purpose and actually works.

## core question

```text
primary_question:
  Does the program work properly for the purpose it was built for?
```

## loop

```text
1_purpose_fit:
  compare the result against the locked final goal
  check whether the program still matches the intended user flow and outcome

2_run_or_render:
  run the program, command, report, UI, chart, or main output when feasible
  if it cannot be run, record the blocker instead of claiming completion

3_detect_abnormality:
  check errors, broken output, missing data, misleading output, failing tests, and goal mismatch

4_locate_cause:
  identify the file, function, data path, dependency, configuration, or design choice causing the abnormality

5_apply_minimal_fix:
  make the smallest maintainable change that addresses the cause
  do not add agents, loops, or automation unless they improve correctness, verification, or maintenance

6_rerun:
  run the relevant check again after the fix
  do not close on an unverified fix

7_repeat_or_stop:
  repeat only while there is meaningful progress and scope still allows it
  stop with a blocker if the same failure repeats without new evidence

8_record:
  record what was checked, what failed, what changed, what now passes, and what risk remains
```

## priority order

```text
priority_order:
  1_original_purpose_fit
  2_actual_working_behavior
  3_verifiable_evidence
  4_maintainability
  5_loop_agent_or_automation_structure
```

## abnormality examples

```text
abnormality:
  program does not start
  data does not load
  output is blank or misleading
  user-facing flow exposes implementation details
  result is technically generated but does not satisfy the locked goal
  tests pass but the primary user flow fails
  placeholder data is presented as real behavior
  fix creates unnecessary maintenance burden
```

## stop conditions

```text
stop_with_blocker:
  required behavior cannot be run or inspected
  required data, permission, or environment is unavailable
  repeated failure has no new diagnosis path
  fix would exceed locked scope
  safe rollback or maintenance path is unclear

stop_with_done:
  purpose fit is checked
  actual behavior is checked
  abnormalities are absent or recorded as residual risk
  rerun after fix passed
  maintainability remains acceptable
  verification evidence is recorded honestly
```

## forbidden claims

```text
forbidden:
  claim done because a loop ran
  claim done because code was edited
  claim done because tests passed while the main purpose was not checked
  add agents to avoid understanding the program
  add automation that makes the program harder to maintain
```

