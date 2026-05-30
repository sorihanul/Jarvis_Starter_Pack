# Function Packs

## purpose

This file defines the design-time function packs used to produce domain ontology brains.

## runtime flow

```text
request
-> Domain Scope Lock Pack
-> Material Surface Pack
-> Ontology Brain Role Pack
-> Ontology Project Template Pack
-> Schema Contract Pack
-> Connector Contract Pack
-> Validation and Handoff Pack
-> Launch Report Pack
```

## function use principles

```text
materials_before_structure:true
minimal_skeleton_before_customization:true
connectors_before_global_standard:true
candidate_asserted_split_required:true
source_binding_required:true
domain_maintenance_separate:true
```

## packs

### Domain Scope Lock Pack

```text
use_when:
  any ontology brain or ontology project is requested
functions:
  domain_name_bind
  domain_boundary_bind
  excluded_scope_bind
  target_user_or_brain_bind
output:
  domain_scope_packet
stop_condition:
  domain is too broad or target use is unknown
```

### Material Surface Pack

```text
use_when:
  materials, docs, DBs, search results, or notes are available
functions:
  material_type_detect
  source_ledger_plan
  raw_vs_processed_surface_split
  search_gap_policy_bind
output:
  material_surface_plan
stop_condition:
  no usable material and user requests asserted ontology
```

### Ontology Brain Role Pack

```text
use_when:
  a domain ontology brain skeleton must be produced
functions:
  ontology_manager_role_bind
  maintenance_boundary_bind
  candidate_asserted_policy_bind
  conflict_exception_policy_bind
output:
  domain_ontology_brain_contract
stop_condition:
  role overlaps with an existing specialist brain without a connector boundary
```

### Ontology Project Template Pack

```text
use_when:
  the ontology needs a project workspace
functions:
  input_surface_design
  work_surface_design
  ontology_surface_design
  export_surface_design
  index_surface_design
output:
  ontology_project_layout
stop_condition:
  project would store raw material, candidate work, and asserted ontology in one surface
```

### Schema Contract Pack

```text
use_when:
  concepts, relations, attributes, rules, conflicts, or exports need stable formats
functions:
  concept_schema_bind
  relation_schema_bind
  attribute_schema_bind
  conflict_schema_bind
  export_packet_schema_bind
output:
  schema_contract
stop_condition:
  schema forces domain-specific fields into all domains
```

### Connector Contract Pack

```text
use_when:
  another brain must use ontology results
functions:
  consumer_brain_detect
  read_surface_bind
  use_for_bind
  do_not_use_for_bind
  update_permission_bind
output:
  connector_contract
stop_condition:
  connector allows consumer brain to mutate ontology internals by default
```

### AILO-N Mini Ontology Pack

```text
use_when:
  complex target/relation structure needs frame stabilization
functions:
  frame_candidate_select
  frame_use_guard
  optional_topo_hint_bind
  frame_export_bind
output:
  optional_ailo_n_frame_export
stop_condition:
  user wants AILO-N as default format for every ontology item
```

### Validation and Handoff Pack

```text
use_when:
  before closing any produced brain/project design
functions:
  acceptance_test_bind
  launch_phrase_bind
  first_task_bind
  handoff_packet_bind
output:
  validation_and_handoff_report
stop_condition:
  produced brain has no boot path, no source binding, or no connector surface
```

### Launch Report Pack

```text
use_when:
  after a produced brain/project/connector design passes validation
functions:
  produced_asset_summary
  source_basis_report
  candidate_asserted_policy_report
  conflict_policy_report
  connector_surface_report
  handoff_packet_location_report
  launch_phrase_report
output:
  produced_brain_report
stop_condition:
  output would omit source basis, candidate/asserted policy, conflict policy, connector surface, or launch phrase
```

## default combinations

```text
new_domain_ontology_brain:
  Domain Scope Lock Pack
  Material Surface Pack
  Ontology Brain Role Pack
  Ontology Project Template Pack
  Schema Contract Pack
  Connector Contract Pack
  Validation and Handoff Pack
  Launch Report Pack

existing_ontology_connector:
  Domain Scope Lock Pack
  Connector Contract Pack
  Validation and Handoff Pack
  Launch Report Pack

mini_ontology_export:
  Domain Scope Lock Pack
  Schema Contract Pack
  AILO-N Mini Ontology Pack
  Validation and Handoff Pack
  Launch Report Pack
```

## failure output

```text
ok:false
reason:
missing_slots:
blocked_pack:
next_action:
```

## promotion rule

Create a new sub-template only when repeated need appears across more than one ontology brain build.
