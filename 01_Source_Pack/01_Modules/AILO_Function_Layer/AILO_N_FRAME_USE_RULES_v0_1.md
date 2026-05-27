# AILO-N Frame Use Rules v0.1

## purpose

This card defines the operating limits for AILO-N frames in Jarvis v3.

Use it before creating or promoting a persistent frame.

## v3 and v4 role

In v3, AILO-N is a light target-framing rule for brains, function packs, sources, claims, repo targets, patch plans, and validation objects.

In v4, it can become the target-fixing device for cognitive-function synapses.

```text
cognitive synapse
-> what to judge, when to stop, where to hand off

AILO-N
-> what exact target the judgment is about
```

One-line relationship:

```text
synapse fixes the judgment movement; AILO-N fixes the judgment target.
```

## five rules

```text
1. Use Frame only for repeated targets.
2. conf has no authority.
3. asserted is forbidden without visible basis.
4. Execution stays outside the Frame.
5. When frames multiply, merge or discard them.
```

## minimal v3 frame contract

Use the full AILO-N source only when canonical slot disputes, relation contracts, formal mapping, validation-code details, or knowledge-pack shape are needed.

For v3 operations, prefer this minimum practical contract:

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

Do not expand the slot set just because the source contains more slots.

Optional `topo` relation-network hints belong to mini ontology use, not default frame use.

## rule details

### 1. Use Frame only for repeated targets

Create a frame only when the target will be reused, routed, validated, merged, or handed off.

Do not create a frame for a one-off note, a simple answer, a transient thought, or a plain task log.

```text
allowed:
  repeated brain
  reusable function pack
  policy object
  source object
  claim object
  repo target
  patch plan
  validation target

not_allowed:
  one-time chat answer
  temporary wording idea
  simple todo line
  note that will not be reused
```

### 2. conf has no authority

`conf` is only `confidence_hint`.

It cannot replace `source`, `evidence`, `assertionBasis`, review, validation, or user confirmation.

```text
conf:0.95
-> still not asserted
-> still not verified
-> still not executable authority
```

### 3. asserted is forbidden without visible basis

`state:"asserted"` is allowed only when the frame shows why it is accepted in the current system context.

```text
required_for_asserted:
  source
  evidence
  assertionBasis
```

If these are missing, keep the frame as `candidate`, `observed`, or `inferred`.

### 4. Execution stays outside the Frame

A frame names and constrains a target.

It does not execute the work.

```text
Frame
-> target identity, relation, state, evidence, validation target

AILO verb / function pack / brain harness
-> action, edit, verify, run, route, report
```

Wrong:

```ailo
Patch.Plan{
  isa:Artifact,
  run_tests:true
};
```

Right:

```ailo
Patch.Plan{
  isa:Artifact,
  validates:[Test.Required],
  state:"candidate"
};

verify{
  obj:Patch.Plan,
  rule:{check:[source, assertionBasis, validates]},
  to:"verification_report"
}!
```

### 5. When frames multiply, merge or discard them

Frames are not a note-taking format.

If many frames describe the same target, merge them into one stronger frame or discard weak candidates.

```text
merge_when:
  same target
  same role
  overlapping source/evidence
  same validation purpose

discard_when:
  no reuse
  no source
  no route
  no validation role
  duplicates a stronger frame
```

## promotion gate

Before a frame becomes persistent, answer:

```text
repeated_target?
source_visible?
evidence_visible?
assertionBasis_visible?
execution_outside_frame?
merge_or_discard_checked?
```

If any answer fails, the frame stays temporary or is removed.

## expected failure modes

### slot overload

When the slot list grows too large, the model tries to fill every field and creates document debt.

Use the minimum practical contract first.

### frame overproduction

If every note becomes a frame, the system becomes harder to read.

Only repeated or confusion-prone targets get frames.

### fake precision from conf

`conf:0.91` can look like evidence even when it is only decoration.

Authority must stay with `state + evidence + assertionBasis`.

### asserted misuse

Do not let plausibility become `state:"asserted"`.

Asserted requires visible basis and a promotion reason.

### execution leakage

Do not put `execute:true`, `run`, `fix`, `edit`, or similar action intent inside a noun frame.

Actions belong to AILO verbs, protocols, function packs, or brain harnesses.

### name over meaning

Do not infer meaning from names like `Brain.Builder` alone.

The meaning is determined by slots, relations, state, source, evidence, and assertion basis.

### verification burden

A persistent frame creates obligations: state transition, source tracking, conflict handling, merge, discard, and trace.

If the obligation is not worth it, do not create the frame.

### topology hint overuse

`topo` can help relation-network compression and validation, but it can also become a decorative label.

Use it only in mini ontologies when ordinary relation slots are not enough.

## useful when

AILO-N helps when v3 or v4 needs to separate:

```text
Source vs reference note
candidate vs asserted
brain vs pack
pack vs synapse
claim vs evidence
verification target vs verification result
consumes vs produces
blocks vs validates
```

## one-line rule

```text
AILO-N fixes judgment targets; used well it reduces confusion, used broadly it becomes document debt.
```
