# Skill Trust Gate Usage Example v0.1

## Scenario

The user gives Jarvis a small external skill and says:

```text
Can we use this?
```

The skill says it summarizes Markdown files, but it also contains an optional command that can modify files.

## Step 1. Review The Source

```text
skill_name:
  Markdown Summary Skill
source_state:
  user_provided
source_limits:
  source is available, but no prior validation exists
entry_points:
  README and one script
requires_deeper_review:
  yes
reason:
  the skill claims to summarize, but it can also modify files
```

## Step 2. Map Permissions

```text
skill_name:
  Markdown Summary Skill
permission_map:
  reads_files: yes
  writes_files: optional
  runs_shell: no
  uses_network: no
  reads_secrets: no
highest_permission:
  write_local
permission_reason:
  optional file writing exists
requires_action_permission_pack:
  yes
```

## Step 3. Trust Decision

```text
skill_name:
  Markdown Summary Skill
trust_decision:
  limited_use
reason:
  useful for one task, but write behavior must be blocked first
allowed_scope:
  read-only summary of selected Markdown files
required_approval:
  yes, if writing output files
validation_needed:
  compare summary with one small test file
disable_or_rollback:
  do not add to default boot
next_action:
  run read-only review or create a local safe wrapper
```

## Step 4. Safe Enable Card

```text
skill_name:
  Markdown Summary Skill
source_state:
  user_provided
trust_decision:
  limited_use
permission_level:
  read_only for first use
allowed_scope:
  selected Markdown files only
allowed_actions:
  read and summarize
blocked_actions:
  file modification
  deletion
  network access
required_user_approval:
  any write action
validation_plan:
  inspect output against one source file
disable_path:
  do not register as default skill
owner_or_maintainer:
  current project only
review_after:
  first use
```

## Result

Jarvis does not install the skill as trusted.

Jarvis can learn the useful read-only behavior.

Any write behavior stays behind explicit approval.
