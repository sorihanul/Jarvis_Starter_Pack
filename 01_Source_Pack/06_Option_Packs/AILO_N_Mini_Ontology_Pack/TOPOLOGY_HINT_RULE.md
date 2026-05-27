# Topology Hint Rule

## purpose

This rule defines how `topo` may be used inside an AILO-N mini ontology.

`topo` is optional. It is not part of the default v3 practical frame shape.

## source

The full optional relation-topology source is:

```text
../../01_Modules/AILO_Function_Layer/AILO_RELATION_TOPOLOGY_PACK_v0_1.md
```

## allowed shape

```ailo
topo:{
  rel:"hub|chain|bridge|gate|loop|cut|anchor|sink",
  to:[FrameRef],
  strength:"weak|medium|strong|hard"
}
```

Only `rel` is required when `topo` is used.

## meaning

```text
identity slots
-> what the frame is

relation slots
-> how the frame relates

evidence and state slots
-> how the frame is grounded

topo
-> what structural function the frame performs inside the relation network
```

## allowed use

Use `topo` only when it improves at least one of:

```text
compression priority
validation planning
route selection
handoff clarity
project mapping
creative continuity
relation-network review
```

## preferred mini ontology subset

For v3 mini ontologies, prefer this smaller set first:

```text
anchor
gate
cut
hub
sink
```

Use `bridge`, `chain`, and `loop` only when the relation structure really needs them.

## compression priority

```text
1. anchor
2. gate
3. cut
4. hub
5. sink
6. bridge
7. chain
8. loop
```

## validation hints

```text
anchor:
  source or evidence should be visible

gate:
  rule, condition, blocks, allows, or validates should be visible

cut:
  conflict, blocks, cannot, invalidWhen, or contradicts should be visible

hub:
  connected frames should be listed or implied by relation slots

sink:
  produces, contains, stores, output, or report target should be visible
```

## forbidden use

```text
topo_replaces_actual_relation:false
topo_creates_authority:false
topo_promotes_to_asserted:false
topo_executes_action:false
topo_required_for_simple_frame:false
```

Do not use `topo` when ordinary relation slots are enough.

## one-line rule

```text
Use topo only as a thin relation-network hint for mini ontologies; never as relation, evidence, authority, or execution.
```
