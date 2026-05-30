# Decision Tables

## purpose

Keep repeated ontology brain design decisions stable without forcing all domain ontology brains into one identical shape.

## shared rules

```text
do_not_merge_early:true
connector_over_direct_mutation:true
domain_ontology_brain_owns_domain:true
search_result_is_candidate:true
asserted_requires_source_evidence_basis:true
```

## build_or_not_decision

| condition | decision |
|---|---|
| one-time concept extraction only | do not create ontology brain |
| repeated domain ontology management needed | create domain ontology brain |
| only output conversion is needed | create export procedure, not brain |
| existing ontology brain can own it | hand off or extend connector |
| new domain boundary and maintenance needed | create new domain ontology brain |

## ontology_scope_decision

| condition | decision |
|---|---|
| domain has multiple unrelated subdomains | split projects |
| terms share material source and use case | keep one ontology brain |
| relations cross domains but ownership differs | use bridge connector |
| domain boundary unknown | keep candidate scope |

## material_decision

| material | handling |
|---|---|
| raw documents | store in input/raw surface |
| DB export | store in input/db surface and derive schema candidates |
| search results | source candidate only |
| user notes | source candidate unless confirmed |
| existing glossary | concept candidate source |

## merge_decision

| condition | decision |
|---|---|
| same label, different role | do not merge |
| same concept, same evidence, same use | merge candidate |
| same term, different source definitions | conflict ledger |
| alias without proof | alias candidate |
| synonym confirmed by source/user | synonym link |

## connector_decision

| consumer | read surfaces |
|---|---|
| Info Research Brain | source ledger, concepts, relations, question index |
| Verification Brain | rules, exceptions, evidence bindings, conflicts |
| Coding Brain | attributes, enums, validation schema, JSON export |
| Domain Brain | domain packet, question index, connector note |

## AILO_N_decision

| condition | decision |
|---|---|
| simple ontology tables are enough | do not use AILO-N |
| repeated target relations are confusing | use AILO-N frame export |
| relation-network compression is needed | optional `topo` |
| every item requested as frame | warn about cost |

## close_decision

| condition | close status |
|---|---|
| boot path, project template, connector, and tests present | ready |
| missing source binding | blocked |
| no connector surface | incomplete |
| no acceptance tests | incomplete |
| domain scope too broad | split_required |
