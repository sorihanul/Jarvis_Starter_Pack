# Classification Decision Note v0.1

## Decision
Use three layers:

```text
AILO function
AILO cognitive function
AILO engine
AILO OS
```

## Allocation

### AILO function
Primary lane:
```text
Jarvis v2
```

Reason:
- small control functions stabilize document harness behavior
- good for public, lightweight, low-cost systems

### AILO cognitive function
Primary lane:
```text
brain-local cognitive lane
```

Reason:
- cognitive functions become brain-local thought parts
- each brain should collect functions matching its own grain

### AILO engine
Primary lane:
```text
brain-local engine lane
```

Reason:
- engines are compiled from functions, cognitive functions, or skills
- they attach specialized capability to brains

### AILO OS
Primary lane:
```text
implementation/runtime
```

Reason:
- OS is no longer just a document or classification layer
- OS requires parser, registry, runner, trace, permission, validation, memory policy, and packaging
- document-only systems should be called OS specs, not OS runtimes

## Important decision
Do not build one giant global cognitive-function warehouse by default.

Instead:
```text
The source layer provides the making rules.
Each brain owns its functions, skills, and engines.
```

## One-line conclusion
AILO functions support v2 stability; AILO cognitive functions and engines support brain specialization; AILO OS begins only when there is a runnable operating layer.
