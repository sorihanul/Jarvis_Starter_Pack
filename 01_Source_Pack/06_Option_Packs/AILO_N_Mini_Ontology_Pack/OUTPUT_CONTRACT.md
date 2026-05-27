# Output Contract

## required output

```text
mini_ontology_scope:
source_basis:
frame_count:
accepted_frames:
candidate_frames:
rejected_or_merged_frames:
relation_index:
topology_hints:
query_table:
validation_report:
remaining_unknowns:
next_use:
```

## accepted frame format

```ailo
Frame.Name{
  isa,
  role,
  consumes,
  produces,
  governedBy,
  blocks,
  validates,
  source,
  evidence,
  state,
  conf,
  assertionBasis,
  trace
};
```

## compact report format

```text
verdict:
frames_created:
frames_rejected:
frames_merged:
asserted_count:
candidate_count:
main_queries_supported:
queries_not_allowed:
risks:
```

## query table

Every mini ontology must include at least three usable queries.

Example:

```text
question: Which claims are not asserted?
allowed_frames: Claim.*
required_state: candidate | inferred | observed
must_check: source, evidence, assertionBasis
do_not_answer_when: frame has no source
```

## handoff packet

When the frame set is handed to another brain or thread, include:

```text
scope
top_frames
asserted_frames
candidate_frames
blocking_rules
validation_targets
unknowns
```
