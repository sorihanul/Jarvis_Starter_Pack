# Stop Rule

## stop and ask or report risk when

```text
ontology_scope_missing:true
source_material_missing:true
user_demands_asserted_without_evidence:true
frame_count_explodes:true
relation_conflict_unresolved:true
execution_instruction_enters_frame:true
full_ontology_required_beyond_mini_scope:true
```

## stop and use another pack when

```text
needs_source_research:
  Evidence_Intake_Pack

needs_validation_report:
  Verification_and_Proof_Pack

needs_full_knowledge_pack:
  Ontology_Pack + Evidence_Intake_Pack + Verification_and_Proof_Pack + Memory_Access_and_Route_Pack

needs_context_handoff:
  Context_Compression_Pack
```

## split rule

If the frame set grows beyond the useful mini range, split by domain, use case, or target brain.

Do not solve frame growth by adding more slots.
