# Input Slots

Before coding, fill only the slots that matter.

```yaml
coding_request:
  goal: ""
  current_problem: ""
  success_criteria: []
  repo_or_folder: ""
  files_in_scope: []
  files_out_of_scope: []
  commands_allowed: []
  commands_to_avoid: []
  change_limit: "small_patch | review_only | design_only | handoff_only"
  active_lens: "intake | implement | review | verify | release | handoff"
  user_approval_needed: "yes | no | unknown"
  risk_notes: []
```

## Missing Slot Rule

If a missing slot blocks safe action, stop and ask or produce a handoff note.

Do not guess:

```text
target repository
files in scope
destructive command permission
API keys or secrets
production deployment intent
```
