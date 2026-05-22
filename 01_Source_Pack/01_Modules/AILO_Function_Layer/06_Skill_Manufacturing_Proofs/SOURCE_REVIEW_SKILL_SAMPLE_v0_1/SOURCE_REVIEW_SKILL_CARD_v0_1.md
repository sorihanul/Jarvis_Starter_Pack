# Source Review Skill Card v0.1

## Identity

```text
skill_id:"skill.source_review.v0.1"
goal:"review one source file and produce a bounded evidence-backed report"
status:"sample_skeleton"
```

## Required inputs

- source_path
- review_goal

## Optional inputs

- source_role
- output_style

## Steps

- lock scope
- read source path
- extract claims
- separate evidence and uncertainty
- produce bounded report
- emit handoff packet

## Output shape

```text
required_fields:['summary', 'claims', 'evidence', 'uncertainty', 'next_action']
forbidden_fields:['hidden_appendix', 'unrequested_options']
format_rule:"return a compact source_review_report with only required fields"
```

## Report contract

- summary
- claims
- evidence
- uncertainty
- next_action

## Acceptance

Pass if:

- source path is named
- claims and evidence are separated
- uncertainty is visible

Fail if:

- no source path
- unsupported claim
- unbounded rewrite

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
next_entrypoint:"real_skill_trial"
open_items:['runner outputs are generic and need real-use tightening']
```

## Boundary
This skill card is a manufactured skeleton. It does not perform the real domain task yet.
