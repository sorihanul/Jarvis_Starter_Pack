# Action Permission Usage Example v0.1

## Scenario

The user says:

```text
Continue improving the option packs.
```

Jarvis decides it needs to add a small Markdown rule file inside an approved package folder.

## Step 1. Classify The Action

```text
action:
  create one Markdown file
risk_level:
  create
allowed_now:
  yes
approval_needed:
  no
why:
  The user explicitly asked to continue, and the file is inside the current package boundary.
scope:
  one option-pack folder
stop_condition:
  stop if the change requires deleting, moving, or changing global policy.
```

## Step 2. Execution Card

```text
target:
  selected option-pack folder
action:
  add a usage example
risk_level:
  create
purpose:
  make the package easier to use
scope:
  public starter package only
affected_files_or_systems:
  one new Markdown file
approval_state:
  covered by user "continue" instruction
rollback_possible:
  yes
validation_plan:
  check required files, public wording, internal path leaks, and whitespace
stop_condition:
  no deletion, no global rule change, no external side effect
```

## Step 3. Report After Work

```text
performed_action:
  added one usage example
changed_files:
  one Markdown file
validation_result:
  passed
problems_found:
  none
problems_fixed:
  none
remaining_risk:
  example is documentation only, not a tested runtime
next_step:
  run a real dry run later if needed
```

## Counterexample

If the same task required deleting old files:

```text
risk_level:
  destructive
approval_needed:
  yes
next_action:
  stop and ask for explicit deletion approval
```
