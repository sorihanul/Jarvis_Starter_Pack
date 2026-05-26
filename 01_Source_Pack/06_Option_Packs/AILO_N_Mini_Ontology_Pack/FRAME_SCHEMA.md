# Frame Schema

## practical shape

Use the v3 AILO-N practical shape:

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

## minimum shape

Use this when the frame is only a candidate:

```ailo
Frame.Name{
  isa,
  role,
  source,
  state
};
```

## slot meanings

```text
isa:
  what kind of object this is

role:
  what this object does in the target system

consumes:
  what this object receives or depends on as input

produces:
  what this object emits as output

governedBy:
  policies, rules, or constraints that control this object

blocks:
  actions, claims, or states this object prevents

validates:
  targets, criteria, or outputs this object checks

source:
  source material used to create the frame

evidence:
  direct or indirect support for the frame

state:
  observed | candidate | asserted | inferred | deprecated | rejected

conf:
  confidence_hint only, no authority

assertionBasis:
  visible reason why the frame is accepted

trace:
  where the frame came from or how it was transformed
```

## relation index shape

```text
from:
relation:
to:
direction:
reason:
source:
evidence:
state:
```

## query table shape

```text
question:
allowed_frames:
required_state:
must_check:
do_not_answer_when:
```
