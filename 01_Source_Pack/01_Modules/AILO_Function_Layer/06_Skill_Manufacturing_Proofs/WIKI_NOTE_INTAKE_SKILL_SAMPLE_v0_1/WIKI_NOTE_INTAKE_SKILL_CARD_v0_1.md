# Wiki Note Intake Skill Card v0.1

## Identity

```text
skill_id:"skill.wiki_note_intake.v0.1"
goal:"turn one raw note into a bounded wiki candidate note with trace"
status:"sample_skeleton"
```

## Required inputs

- raw_note_path
- wiki_goal

## Optional inputs

- source_context
- target_index
- linking_style

## Steps

- lock intake scope
- read raw note path
- extract reusable claims
- separate source trace and interpretation
- draft wiki candidate note
- mark non-canon status
- emit handoff packet

## Output shape

```text
required_fields:['candidate_title', 'candidate_status', 'summary', 'source_trace', 'claims', 'uncertainty', 'links_to_create', 'next_action']
forbidden_fields:['hidden_appendix', 'unrequested_options']
format_rule:"return a compact wiki_note_intake_packet with only required fields"
```

## Report contract

- candidate_title
- candidate_status
- summary
- source_trace
- claims
- uncertainty
- links_to_create
- next_action

## Acceptance

Pass if:

- raw source path is named
- candidate status is explicit
- source trace and interpretation are separated

Fail if:

- canon promotion
- source trace missing
- unbounded folder scan

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
gate:"WARN"
safe_next_action:"pause and confirm boundary"
```

## Handoff

```text
next_entrypoint:"real_wiki_note_intake_trial"
open_items:['real wiki note quality still needs raw-note fixtures']
```

## Boundary
This skill card is a manufactured skeleton. It does not perform the real domain task yet.
