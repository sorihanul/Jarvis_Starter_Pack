# Workflow Separation

## core rule

Design, implementation, and verification must be separated.

They may run inside one coding case workspace, or be delegated to different sub-brain threads, but they must not collapse into one unverified narrative.

## why

LLMs naturally continue plausible context.
Without separation, a model can design, edit, and declare success in the same fluent answer without proving that the result works.

## stages

### design stage

```text
purpose:
  decide what should be changed before changing files
required_outputs:
  task_scope
  allowed_changes
  forbidden_changes
  acceptance_conditions
  verification_plan
  role_split_decision
stop_condition:
  scope or verification is unclear
```

### implementation stage

```text
purpose:
  change files only inside the locked scope
required_outputs:
  changed_files
  implementation_notes
  scope_drift_check
  verification_request
stop_condition:
  change requires scope expansion or cross-role decision
```

### verification stage

```text
purpose:
  decide whether the implementation satisfies the design contract
required_outputs:
  checks_run
  pass_fail
  failure_interpretation
  residual_risk
  close_or_rework_decision
stop_condition:
  required checks are failing, missing, or inconclusive
```

## multi-thread interpretation

```text
design_can_be_main_thread:true
implementation_can_be_sub_brain_threads:true
verification_can_be_separate_sub_brain_thread:true
closeout_owned_by_Coding_Meta_Brain:true
```

## forbidden collapse

```text
forbidden:
  design_and_edit_without_scope_lock
  edit_and_claim_done_without_verification
  verification_by_assertion_only
  implementation_thread_self_approves_high_risk_change
```
