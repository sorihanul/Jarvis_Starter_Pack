# Local Validation Checklist v0.1

## Purpose

Check whether an imported capability works inside Jarvis before treating it as stable.

## Validation Levels

```text
paper_valid:
  The rule is clear on paper.

route_valid:
  Jarvis knows when to read or skip the rule.

dry_run_valid:
  The rule works on a small simulated task.

work_valid:
  The rule helped one real task.

repeat_valid:
  The rule helped more than once without increasing confusion.
```

## Checklist

```text
purpose_clear:
  The capability has one clear purpose.

trigger_clear:
  Jarvis knows when to use it.

stop_rule_clear:
  Jarvis knows when to stop using it.

output_clear:
  The capability produces a visible result.

cost_bounded:
  It does not require loading too many files by default.

source_independent:
  It can run without reopening the outside source.

risk_bounded:
  It does not create unsafe tool calls, secret exposure, or unbounded memory capture.

conflict_checked:
  It does not override the local rulebook or core boot path.

evidence_recorded:
  There is a note showing why the capability was accepted.
```

## Failure Conditions

Reject or demote the capability if:

- It cannot explain when to use it.
- It requires broad context every time.
- It mostly repeats an existing option pack.
- It makes the default boot path heavier.
- It cannot be validated with a small task.
- It depends on source-specific names, files, or services.

## Output

```text
capability_name:
validation_level:
passed:
failed:
fix_needed:
status: candidate | adapted | deferred | rejected
```
