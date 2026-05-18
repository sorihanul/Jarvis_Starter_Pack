# 40 Brain Route Registry Template

Use this shape for `BRAIN_ROUTE_REGISTRY.md`.

```text
registry_id:
main_brain:
target_system:
last_updated:
final_output_owner:
```

## Brain Route Entry

```text
route_name:
brain_name:
entry_files:
use_when:
do_not_use_when:
same_thread_allowed:
separate_thread_preferred:
required_inputs:
expected_output:
handoff_needed:
integration_rule:
```

## Routing Rule

```text
if_request_contains:
choose_route:
because:
mode:
  same_thread_lens | separate_thread_handoff | integration_only
stop_if:
fallback:
```

## Registry Check

```text
no_duplicate_routes:
entry_files_exist:
mode_is_declared:
final_integration_owner_visible:
```
