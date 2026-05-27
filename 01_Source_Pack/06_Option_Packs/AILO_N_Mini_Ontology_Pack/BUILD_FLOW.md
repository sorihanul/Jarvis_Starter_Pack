# Build Flow

## sequence

```text
1. scope_lock
2. source_split
3. target_candidate_extract
4. frame_worth_check
5. minimal_frame_write
6. relation_bind
7. optional_topology_hint
8. state_and_basis_assign
9. merge_or_discard
10. query_table_write
11. validation_report
```

## 1. scope_lock

Define:

```text
domain:
main_use_case:
what_this_mini_ontology_must_help_the_ai_do:
what_it_must_not_cover:
```

## 2. source_split

Split source material into:

```text
entity
property
relation
event
action
control_rule
evidence
unknown
```

This step comes from `Ontology_Pack`.

## 3. target_candidate_extract

Extract repeated or confusion-prone targets.

Do not frame every sentence.

## 4. frame_worth_check

A candidate becomes a frame only when at least one is true:

```text
will_be_reused
will_be_routed
will_be_validated
will_block_action
will_be_handed_off
will_reduce_candidate_asserted_confusion
```

## 5. minimal_frame_write

Write the smallest useful frame first.

Do not fill optional slots just to make the frame look complete.

## 6. relation_bind

Bind only useful relations:

```text
is_a
part_of
depends_on
supports
contradicts
updates
used_for
consumes
produces
governedBy
blocks
validates
```

## 7. optional_topology_hint

Add `topo` only when relation-network structure improves compression, validation, routing, or handoff.

Prefer:

```text
anchor
gate
cut
hub
sink
```

Do not use `topo` to replace relation slots.

## 8. state_and_basis_assign

Use:

```text
observed:
  extracted from source

candidate:
  proposed but not verified

asserted:
  source, evidence, and assertionBasis are visible

inferred:
  derived by rule, not directly sourced

rejected:
  failed validation
```

## 9. merge_or_discard

Merge frames with the same target and role.

Discard frames that have no reuse, route, evidence, validation role, or behavior change.

## 10. query_table_write

Create questions the AI can safely answer from the frame set.

Also create questions it must not answer.

## 11. validation_report

Run `VALIDATION_RULE.md`.
