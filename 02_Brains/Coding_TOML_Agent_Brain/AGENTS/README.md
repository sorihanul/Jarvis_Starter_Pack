# Agents

## purpose

This folder holds TOML role agents for a single-thread coding task.

Agents are not sub-brain threads.
They are temporary role contracts used sequentially in one conversation.

## folders

```text
ACTIVE/
  agents currently used by this task

CANDIDATES/
  repeated agent patterns worth reviewing

ARCHIVE/
  completed or discarded task agents
```

## rule

Default to no agents.
Create an agent only when its role boundary, inputs, outputs, and stop condition are clear.
