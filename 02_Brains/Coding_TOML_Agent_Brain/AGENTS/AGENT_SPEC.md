# Agent Spec

## TOML schema

```toml
name = "example-agent"
role = "short role description"
thread_model = "single_thread"
status = "active"
stage_role = "design|implementation|verification|release|closeout"

use_when = []
do_not_use_when = []

inputs = []
outputs = []
allowed_actions = []
forbidden_actions = []
stop_conditions = []

[handoff]
required_context = []
expected_report = []
```

## required fields

```text
name
role
thread_model
use_when
do_not_use_when
inputs
outputs
stop_conditions
```

## rule

Do not create an agent that has no explicit stop condition.
