# Prompt Validation Skill Card v0.1

## Identity

```text
skill_id:"skill.prompt_validation.v0.1"
goal:"validate one prompt against its declared purpose and output contract"
status:"sample_skeleton"
```

## Required inputs

- prompt_text
- validation_goal

## Optional inputs

- target_model
- must_avoid
- expected_output_shape

## Steps

- lock validation scope
- read prompt text
- identify declared purpose
- check instruction conflict
- check output contract
- produce bounded validation report
- emit handoff packet

## Output shape

```text
required_fields:['verdict', 'blocking_issues', 'major_issues', 'minor_issues', 'evidence', 'next_action']
forbidden_fields:['hidden_appendix', 'unrequested_options']
format_rule:"return a compact prompt_validation_report with only required fields"
```

## Report contract

- verdict
- blocking_issues
- major_issues
- minor_issues
- evidence
- next_action

## Acceptance

Pass if:

- prompt purpose is named
- findings cite prompt evidence
- rewrite is not performed unless requested

Fail if:

- vague critique
- unsupported issue
- unrequested rewrite

## Memory

```text
memory_policy:"candidate_only"
allowed_surface:"candidate surface"
```

## Trace

```text
trace_policy:"structured"
trace_fields:['run_id', 'function_id', 'input_keys', 'output_keys', 'validation_result']
```

## Gate

```text
gate:"ALLOW"
safe_next_action:"proceed"
```

## Handoff

```text
next_entrypoint:"real_prompt_validation_trial"
open_items:['real prompt validation quality still needs prompt fixtures']
```

## Boundary
This skill card is a manufactured skeleton. It does not perform the real domain task yet.
