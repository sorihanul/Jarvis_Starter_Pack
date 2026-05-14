# Verification and Proof Usage Example v0.1

## Scenario

Jarvis added a new option-pack document and needs to verify whether the package still works.

## Step 1. Success Criteria

```text
goal:
  The new document is connected to the option pack and does not leak private or source-specific material.

success_criteria:
  - The required files exist.
  - The pack README lists the new file.
  - No internal local path appears in the public package.
  - No outside project name or URL appears in the public package.
  - The text has no trailing whitespace.

failure_conditions:
  - A required file is missing.
  - The new file is not reachable from README.
  - Private paths or source-specific names remain.

evidence_needed:
  - file existence check
  - text scan
  - whitespace check

out_of_scope:
  - real runtime automation
```

## Step 2. Proof Level

```text
claim:
  The package is structurally valid.
proof_level:
  static_checked
evidence:
  required file check and text scan
limits:
  This does not prove runtime automation.
can_call_complete:
  yes, for document package structure
```

## Step 3. Findings

```text
finding:
  no required file missing
severity:
  note
evidence:
  required file check returned zero missing files
why_it_matters:
  the pack can be found by a reader
fix_needed:
  no
```

## Step 4. Revalidation

```text
revalidation:
original_failure:
  none
fix_applied:
  none
checks_rerun:
  required file check, text scan, whitespace check
new_result:
  passed
remaining_risk:
  runtime automation was not tested
close_status:
  complete
```

## Step 5. Report

```text
target:
  selected option pack
goal:
  confirm document-package integrity
success_criteria:
  required files, README connection, no private/source-specific leakage
proof_level:
  static_checked
checks_run:
  file existence, text scan, whitespace scan
findings:
  no blocking or major issue
fixes_applied:
  none
revalidation:
  passed
remaining_risks:
  no runtime automation test
close_status:
  complete
next_action:
  run a dry-use example if runtime confidence is needed
```
