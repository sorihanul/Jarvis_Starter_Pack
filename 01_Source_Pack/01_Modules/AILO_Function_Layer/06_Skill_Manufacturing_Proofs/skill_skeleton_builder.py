#!/usr/bin/env python3
"""Generic AILO skill-skeleton builder.

This composes existing mock runners.
It does not execute the target skill.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STABLE_RUNNER = ROOT / "05_AILO_OS" / "HARNESS_SEED_STABLE_BASIC_FUNCTIONS_v0_1" / "stable_basic_functions_mock_runner.py"
SKILL_RUNNER = ROOT / "05_AILO_OS" / "HARNESS_SEED_SKILL_SKELETON_FUNCTIONS_v0_2" / "skill_skeleton_functions_mock_runner.py"


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.name


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


stable = load_module(STABLE_RUNNER, "stable_basic_functions_mock_runner")
skill = load_module(SKILL_RUNNER, "skill_skeleton_functions_mock_runner")


def call(module, fixture_id: str, function_id: str, slots: dict[str, Any]) -> dict[str, Any]:
    registry = module.REGISTRY[function_id]
    fixture = {
        "id": fixture_id,
        "input": {
            "run_id": fixture_id,
            "function_id": function_id,
            "slots": slots,
        },
        "expect": {
            "ok": True,
            "validation_result": "PASS",
            "required_output_keys": registry["output_schema"],
        },
    }
    result = module.run_fixture(fixture)
    if not result["passed"]:
        raise RuntimeError(f"{fixture_id} failed: {result['errors']}")
    return result


def main() -> int:
    if len(sys.argv) < 2:
        raise SystemExit("usage: skill_skeleton_builder.py <build_input.json>")

    input_path = Path(sys.argv[1]).resolve()
    build_input = json.loads(input_path.read_text(encoding="utf-8"))
    sample_dir = input_path.parent
    prefix = build_input["output_prefix"]

    skill_id = build_input["skill_id"]
    skill_goal = build_input["skill_goal"]
    required_inputs = build_input["required_inputs"]
    optional_inputs = build_input["optional_inputs"]
    output_contract = build_input["output_contract"]

    calls: list[dict[str, Any]] = []

    chain = [
        (
            stable,
            "sample.scope_lock",
            "basic_fn.scope_lock.v0.1",
            {
                "user_request": f"Build {skill_id}: {skill_goal}",
                "known_context": build_input.get("known_context", "AILO skill manufacturing sample"),
            },
        ),
        (
            skill,
            "sample.input_contract_bind",
            "basic_fn.input_contract_bind.v0.2",
            {
                "skill_goal": skill_goal,
                "raw_inputs": required_inputs + optional_inputs,
                "required_candidates": required_inputs,
            },
        ),
        (
            skill,
            "sample.dependency_check",
            "basic_fn.dependency_check.v0.2",
            {
                "required_dependencies": build_input["required_dependencies"],
                "available_dependencies": build_input["available_dependencies"],
            },
        ),
        (
            skill,
            "sample.cost_budget_lock",
            "basic_fn.cost_budget_lock.v0.2",
            {
                "task_scope": skill_goal,
                "available_budget": build_input.get("available_budget", "small"),
                "risk": build_input.get("risk", "low"),
            },
        ),
        (
            skill,
            "sample.step_sequence_lock",
            "basic_fn.step_sequence_lock.v0.2",
            {
                "skill_goal": skill_goal,
                "candidate_steps": build_input["candidate_steps"],
            },
        ),
        (
            stable,
            "sample.output_schema_bind",
            "basic_fn.output_schema_bind.v0.1",
            {
                "task_type": build_input["task_type"],
                "output_goal": build_input["output_goal"],
                "constraints": build_input["output_constraints"],
                "required_fields": output_contract,
                "forbidden_fields": build_input.get("forbidden_output_fields", ["hidden_appendix", "unrequested_options"]),
            },
        ),
        (
            skill,
            "sample.acceptance_criteria_bind",
            "basic_fn.acceptance_criteria_bind.v0.2",
            {
                "output_goal": build_input["output_goal"],
                "quality_constraints": build_input["acceptance"]["pass_if"],
                "failure_constraints": build_input["acceptance"]["fail_if"],
            },
        ),
        (
            skill,
            "sample.fixture_contract_bind",
            "basic_fn.fixture_contract_bind.v0.2",
            {
                "function_or_skill_id": skill_id,
                "input_contract": required_inputs,
                "output_contract": output_contract,
            },
        ),
        (
            stable,
            "sample.memory_policy_check",
            "basic_fn.memory_policy_check.v0.1",
            {
                "artifact_type": build_input.get("artifact_type", "skill_card"),
                "user_confirmed": build_input.get("user_confirmed", False),
                "reuse_value": build_input.get("reuse_value", True),
            },
        ),
        (
            stable,
            "sample.trace_policy_check",
            "basic_fn.trace_policy_check.v0.1",
            {
                "task_risk": build_input.get("task_risk", "low"),
                "repeatability_need": build_input.get("repeatability_need", "high"),
                "debug_need": build_input.get("debug_need", "mid"),
            },
        ),
        (
            stable,
            "sample.gate_label",
            "basic_fn.gate_label.v0.1",
            {
                "requested_action": build_input.get("requested_action", "create skill skeleton sample"),
                "risk": build_input.get("risk", "low"),
                "permission_state": build_input.get("permission_state", "allowed"),
            },
        ),
        (
            skill,
            "sample.handoff_packet_bind",
            "basic_fn.handoff_packet_bind.v0.2",
            {
                "current_stage": build_input.get("current_stage", "skill_skeleton_build"),
                "next_stage": build_input.get("next_stage", "real_skill_trial"),
                "artifact_summary": f"{skill_id} skeleton created from basic functions",
                "open_items": build_input.get("open_items", ["runner outputs are generic and need real-use tightening"]),
            },
        ),
    ]

    for item in chain:
        calls.append(call(*item))

    outputs = {item["fixture_id"]: item["result"]["output"] for item in calls}
    traces = {item["fixture_id"]: item["trace"] for item in calls}

    skill_card = {
        "skill_id": skill_id,
        "goal": skill_goal,
        "inputs": outputs["sample.input_contract_bind"],
        "dependencies": outputs["sample.dependency_check"],
        "budget": outputs["sample.cost_budget_lock"],
        "steps": outputs["sample.step_sequence_lock"],
        "output_schema": outputs["sample.output_schema_bind"],
        "report_contract": output_contract,
        "acceptance": outputs["sample.acceptance_criteria_bind"],
        "fixtures": outputs["sample.fixture_contract_bind"],
        "memory": outputs["sample.memory_policy_check"],
        "trace": outputs["sample.trace_policy_check"],
        "gate": outputs["sample.gate_label"],
        "handoff": outputs["sample.handoff_packet_bind"],
    }

    proof = {
        "sample": build_input["sample_id"],
        "function_calls": len(calls),
        "passed": len(calls),
        "failed": 0,
        "overall": "PASS",
        "skill_card": skill_card,
        "function_outputs": outputs,
        "traces": traces,
    }

    out_json = sample_dir / f"{prefix}_BUILD_OUTPUT_v0_1.json"
    out_card = sample_dir / f"{prefix}_CARD_v0_1.md"
    out_report = sample_dir / f"{prefix}_PROOF_REPORT_v0_1.md"
    out_json.write_text(json.dumps(proof, ensure_ascii=False, indent=2), encoding="utf-8")
    out_card.write_text(render_card(skill_card, build_input), encoding="utf-8")
    out_report.write_text(render_report(proof, build_input), encoding="utf-8")

    print(json.dumps({"overall": "PASS", "function_calls": len(calls), "output": display_path(out_json)}, ensure_ascii=False, indent=2))
    return 0


def render_card(card: dict[str, Any], build_input: dict[str, Any]) -> str:
    lines = {
        "required_inputs": "\n".join(f"- {item}" for item in card["inputs"]["required_inputs"]),
        "optional_inputs": "\n".join(f"- {item}" for item in card["inputs"]["optional_inputs"]),
        "steps": "\n".join(f"- {item}" for item in card["steps"]["ordered_steps"]),
        "report_contract": "\n".join(f"- {item}" for item in card["report_contract"]),
        "pass_if": "\n".join(f"- {item}" for item in card["acceptance"]["pass_if"]),
        "fail_if": "\n".join(f"- {item}" for item in card["acceptance"]["fail_if"]),
    }
    return f"""# {build_input['card_title']}

## Identity

```text
skill_id:"{card['skill_id']}"
goal:"{card['goal']}"
status:"sample_skeleton"
```

## Required inputs

{lines['required_inputs']}

## Optional inputs

{lines['optional_inputs']}

## Steps

{lines['steps']}

## Output shape

```text
required_fields:{card['output_schema']['required_fields']}
forbidden_fields:{card['output_schema']['forbidden_fields']}
format_rule:"{card['output_schema']['format_rule']}"
```

## Report contract

{lines['report_contract']}

## Acceptance

Pass if:

{lines['pass_if']}

Fail if:

{lines['fail_if']}

## Memory

```text
memory_policy:"{card['memory']['memory_policy']}"
allowed_surface:"{card['memory']['allowed_surface']}"
```

## Trace

```text
trace_policy:"{card['trace']['trace_policy']}"
trace_fields:{card['trace']['trace_fields']}
```

## Gate

```text
gate:"{card['gate']['gate']}"
safe_next_action:"{card['gate']['safe_next_action']}"
```

## Handoff

```text
next_entrypoint:"{card['handoff']['next_entrypoint']}"
open_items:{card['handoff']['open_items']}
```

## Boundary
This skill card is a manufactured skeleton. It does not perform the real domain task yet.
"""


def render_report(proof: dict[str, Any], build_input: dict[str, Any]) -> str:
    trace_lines = "\n".join(
        f"- {fixture_id}: {trace['selected_function']} -> {trace['validation_result']}"
        for fixture_id, trace in proof["traces"].items()
    )
    return f"""# {build_input['report_title']}

## Result
```text
overall:{proof['overall']}
function_calls:{proof['function_calls']}
passed:{proof['passed']}
failed:{proof['failed']}
```

## What was tested
This sample tested whether `{proof['skill_card']['skill_id']}` can be manufactured by composing AILO basic functions.

It did not test real domain quality.
It did not call cognitive functions.
It did not call engines.
It did not write memory.

## Function trace
{trace_lines}

## Pass condition
```text
all function calls return PASS
all required output fields exist
no final task execution
no memory write
skill card generated
```

## Remaining risk
The generated skeleton is structurally valid, but the actual skill still needs a real-use trial against real inputs.
"""


if __name__ == "__main__":
    raise SystemExit(main())
