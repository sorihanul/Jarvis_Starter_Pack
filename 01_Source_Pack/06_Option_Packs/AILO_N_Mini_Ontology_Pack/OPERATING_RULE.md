# Operating Rule

## primary rule

```text
If the frame will not change future AI behavior, do not create it.
```

## behavior change test

A frame is useful only if it helps at least one of these:

```text
read less
route better
separate candidate from asserted
check source/evidence
block unsafe output or action
validate an artifact
handoff compact context
merge duplicates
discard weak knowledge
```

## asserted rule

`state:"asserted"` requires:

```text
source
evidence
assertionBasis
```

`conf` cannot satisfy this requirement.

## execution rule

Frames do not execute.

Execution belongs to:

```text
AILO verb
function pack
brain harness
protocol
tool call
```

## relation rule

Every relation must show:

```text
from
to
direction
relation type
reason
source or uncertainty
```

## density rule

Prefer fewer stronger frames.

```text
one domain starter:
  5 to 15 frames

small working ontology:
  15 to 40 frames

more than 40 frames:
  split into a domain knowledge pack or project workspace
```

## conflict rule

When two frames conflict:

```text
do not silently merge
mark conflict
keep weaker claim candidate
promote only with visible basis
report unresolved conflict
```
