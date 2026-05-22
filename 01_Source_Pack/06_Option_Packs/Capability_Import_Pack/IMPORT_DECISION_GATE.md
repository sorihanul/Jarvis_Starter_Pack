# Import Decision Gate v0.1

## Purpose

Decide whether an outside pattern should become a Jarvis capability.

Do not start by asking "Can we copy this?"
Start by asking "What operating rule is worth keeping?"

## Decision Levels

```text
ignore:
  The source is not relevant, too vague, or only marketing.

note:
  The source has an interesting idea, but it is not ready for Jarvis use.

candidate:
  The source contains a reusable operating rule.

adapt:
  The rule can be rewritten as a Jarvis option-pack, skill, brain blueprint, or test rule.

defer:
  The rule is useful but needs runtime code, user approval, or more validation.

reject:
  The rule is unsafe, too costly, license-risky, or pushes Jarvis beyond its purpose.
```

## Gate Questions

```text
goal_fit:
  Does this pattern help Jarvis turn a loose user request into a useful result?

layer_fit:
  Is it a core rule, option pack, skill, brain blueprint, project workspace, or test rule?

cost_fit:
  Does it reduce future work more than it increases setup cost?

context_fit:
  Can it work without loading the whole source again?

license_fit:
  Can it be rewritten without copying code, unique wording, tests, or source structure?

safety_fit:
  Does it avoid hidden tool execution, secret exposure, and unbounded data capture?

validation_fit:
  Can we tell whether the adapted rule actually works?
```

## Default Decisions

```text
If useful but heavy:
  defer

If useful and small:
  candidate -> adapt

If useful only with external service accounts:
  note or defer

If mostly marketing:
  ignore

If it requires copying implementation:
  reject

If it changes Jarvis core behavior:
  defer unless explicitly requested
```

## Output

```text
decision:
reason:
target_layer:
absorbed_rule:
blocked_items:
validation_needed:
next_action:
```
