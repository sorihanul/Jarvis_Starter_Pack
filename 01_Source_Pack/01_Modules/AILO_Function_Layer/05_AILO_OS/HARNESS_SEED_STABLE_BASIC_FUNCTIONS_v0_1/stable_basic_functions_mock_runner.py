#!/usr/bin/env python3
"""Deterministic mock runner for the seven stable AILO basic functions.

This is not a smart router and not a full runtime.
Function selection is explicit through function_id.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Callable


SEED_ID = "ailo_os_harness_seed.stable_basic_functions"


REGISTRY: dict[str, dict[str, Any]] = {
    "basic_fn.scope_lock.v0.1": {
        "name": "scope_lock",
        "required_slots": ["user_request"],
        "optional_slots": ["known_context"],
        "output_schema": ["bounded_scope", "out_of_scope", "missing_slots", "stop_condition"],
        "memory_policy": "none",
        "trace_policy": "min",
    },
    "basic_fn.route_lock.v0.1": {
        "name": "route_lock",
        "required_slots": ["bounded_scope", "available_routes"],
        "optional_slots": ["constraints"],
        "output_schema": ["first_route", "conditional_routes", "do_not_read_by_default", "stop_rule"],
        "memory_policy": "none",
        "trace_policy": "min",
    },
    "basic_fn.missing_slot_detect.v0.1": {
        "name": "missing_slot_detect",
        "required_slots": ["input_slots", "required_slots"],
        "optional_slots": [],
        "output_schema": ["missing", "present", "assumed", "needs_user"],
        "memory_policy": "none",
        "trace_policy": "min",
    },
    "basic_fn.output_schema_bind.v0.1": {
        "name": "output_schema_bind",
        "required_slots": ["task_type", "output_goal"],
        "optional_slots": ["constraints", "required_fields", "forbidden_fields"],
        "output_schema": ["required_fields", "forbidden_fields", "format_rule", "pass_if"],
        "memory_policy": "none",
        "trace_policy": "min",
    },
    "basic_fn.memory_policy_check.v0.1": {
        "name": "memory_policy_check",
        "required_slots": ["artifact_type"],
        "optional_slots": ["user_confirmed", "reuse_value"],
        "output_schema": ["memory_policy", "allowed_surface", "forbidden_surface", "promotion_required"],
        "memory_policy": "none",
        "trace_policy": "structured",
    },
    "basic_fn.trace_policy_check.v0.1": {
        "name": "trace_policy_check",
        "required_slots": ["task_risk", "repeatability_need", "debug_need"],
        "optional_slots": [],
        "output_schema": ["trace_policy", "trace_fields", "redaction_required"],
        "memory_policy": "none",
        "trace_policy": "min",
    },
    "basic_fn.gate_label.v0.1": {
        "name": "gate_label",
        "required_slots": ["requested_action", "risk", "permission_state"],
        "optional_slots": [],
        "output_schema": ["gate", "reason", "required_confirmation", "safe_next_action"],
        "memory_policy": "none",
        "trace_policy": "structured",
    },
}


def failure(
    run_id: str,
    function_id: str | None,
    reason: str,
    missing_slots: list[str] | None = None,
    suggested_layer: str = "harness_contract_fix",
) -> dict[str, Any]:
    return {
        "ok": False,
        "function_id": function_id,
        "reason": reason,
        "missing_slots": missing_slots or [],
        "suggested_layer": suggested_layer,
        "final_task_executed": False,
        "memory_written": False,
        "run_id": run_id,
    }


def parse_input(raw: dict[str, Any], fallback_run_id: str) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    run_id = raw.get("run_id", fallback_run_id)
    function_id = raw.get("function_id")
    slots = raw.get("slots", {})

    if not isinstance(function_id, str) or not function_id:
        return None, failure(run_id, function_id, "missing_required_input", ["function_id"])
    if function_id not in REGISTRY:
        return None, failure(run_id, function_id, "unknown_function")
    if not isinstance(slots, dict):
        return None, failure(run_id, function_id, "missing_required_input", ["slots"])

    required = REGISTRY[function_id]["required_slots"]
    missing = [slot for slot in required if slot not in slots or slots[slot] in ("", None)]
    if missing:
        return None, failure(run_id, function_id, "missing_required_input", missing, "basic_function_tightening")

    return {"run_id": run_id, "function_id": function_id, "slots": slots}, None


def run_scope_lock(slots: dict[str, Any]) -> dict[str, Any]:
    request = str(slots["user_request"]).strip()
    out_of_scope = ["perform the final task", "write memory", "call cognitive functions", "call engines"]
    return {
        "bounded_scope": f"lock the execution scope for request: {request}",
        "out_of_scope": out_of_scope,
        "missing_slots": [],
        "stop_condition": "stop after returning scope control fields",
    }


def run_route_lock(slots: dict[str, Any]) -> dict[str, Any]:
    routes = list(slots["available_routes"])
    first_route = routes[0]
    rest = routes[1:]
    return {
        "first_route": first_route,
        "conditional_routes": [{"route": item, "when": "needed after first route"} for item in rest],
        "do_not_read_by_default": rest,
        "stop_rule": "stop after the first route unless a condition opens another route",
    }


def run_missing_slot_detect(slots: dict[str, Any]) -> dict[str, Any]:
    input_slots = slots["input_slots"]
    required_slots = list(slots["required_slots"])
    present_names = set(input_slots.keys()) if isinstance(input_slots, dict) else set(input_slots)
    missing = [item for item in required_slots if item not in present_names]
    present = [item for item in required_slots if item in present_names]
    return {
        "missing": missing,
        "present": present,
        "assumed": [],
        "needs_user": bool(missing),
    }


def run_output_schema_bind(slots: dict[str, Any]) -> dict[str, Any]:
    task_type = str(slots["task_type"])
    required_fields = slots.get("required_fields") or ["result", "evidence", "next_action"]
    forbidden_fields = slots.get("forbidden_fields") or ["hidden_appendix", "unrequested_options"]
    return {
        "required_fields": list(required_fields),
        "forbidden_fields": list(forbidden_fields),
        "format_rule": f"return a compact {task_type} with only required fields",
        "pass_if": ["required_fields exist", "forbidden_fields are absent", "format_rule is followed"],
    }


def run_memory_policy_check(slots: dict[str, Any]) -> dict[str, Any]:
    user_confirmed = bool(slots.get("user_confirmed", False))
    reuse_value = bool(slots.get("reuse_value", False))
    if user_confirmed and reuse_value:
        policy = "candidate_only"
        promotion_required = True
    elif reuse_value:
        policy = "candidate_only"
        promotion_required = True
    else:
        policy = "trace_only"
        promotion_required = False
    return {
        "memory_policy": policy,
        "allowed_surface": "candidate surface" if policy == "candidate_only" else "trace surface",
        "forbidden_surface": ["canon memory", "global rulebook", "preference memory"],
        "promotion_required": promotion_required,
    }


def run_trace_policy_check(slots: dict[str, Any]) -> dict[str, Any]:
    risk = str(slots["task_risk"]).lower()
    repeatability = str(slots["repeatability_need"]).lower()
    debug = str(slots["debug_need"]).lower()
    structured = "high" in {risk, repeatability, debug}
    policy = "structured" if structured else "min"
    return {
        "trace_policy": policy,
        "trace_fields": ["run_id", "function_id", "validation_result"] if policy == "min" else ["run_id", "function_id", "input_keys", "output_keys", "validation_result"],
        "redaction_required": risk == "high",
    }


def run_gate_label(slots: dict[str, Any]) -> dict[str, Any]:
    risk = str(slots["risk"]).lower()
    permission = str(slots["permission_state"]).lower()
    if permission in {"denied", "blocked"}:
        gate = "BLOCK"
    elif permission in {"unknown", "unclear"}:
        gate = "HOLD"
    elif risk == "high":
        gate = "ESCALATE"
    elif risk == "mid":
        gate = "WARN"
    else:
        gate = "ALLOW"
    return {
        "gate": gate,
        "reason": f"permission_state={permission}, risk={risk}",
        "required_confirmation": gate in {"WARN", "HOLD", "BLOCK", "ESCALATE"},
        "safe_next_action": "proceed" if gate == "ALLOW" else "pause and confirm boundary",
    }


RUNNERS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "basic_fn.scope_lock.v0.1": run_scope_lock,
    "basic_fn.route_lock.v0.1": run_route_lock,
    "basic_fn.missing_slot_detect.v0.1": run_missing_slot_detect,
    "basic_fn.output_schema_bind.v0.1": run_output_schema_bind,
    "basic_fn.memory_policy_check.v0.1": run_memory_policy_check,
    "basic_fn.trace_policy_check.v0.1": run_trace_policy_check,
    "basic_fn.gate_label.v0.1": run_gate_label,
}


def validate(function_id: str | None, result: dict[str, Any], selected_function: str | None) -> tuple[str, str | None]:
    if not result.get("ok"):
        return "FAIL", result.get("reason", "validation_failed")
    if function_id not in REGISTRY:
        return "FAIL", "unknown_function"
    output = result.get("output", {})
    required = REGISTRY[function_id]["output_schema"]
    if not all(key in output for key in required):
        return "FAIL", "validation_failed"
    if result.get("memory_written") is not False:
        return "FAIL", "memory_written"
    if result.get("final_task_executed") is not False:
        return "FAIL", "execution_forbidden"
    if selected_function != function_id:
        return "FAIL", "validation_failed"
    return "PASS", None


def emit_trace(run_id: str, function_id: str | None, selected_function: str | None, validation_result: str, failure_reason: str | None) -> dict[str, Any]:
    output_keys = REGISTRY[function_id]["output_schema"] if function_id in REGISTRY else []
    trace_policy = REGISTRY[function_id]["trace_policy"] if function_id in REGISTRY else "min"
    return {
        "run_id": run_id,
        "seed": SEED_ID,
        "selected_function": selected_function,
        "input_keys": ["function_id", "slots"],
        "output_keys": output_keys,
        "memory_policy": "none",
        "trace_policy": trace_policy,
        "validation_result": validation_result,
        "failure_reason": failure_reason,
    }


def check_fixture(result: dict[str, Any], trace_obj: dict[str, Any], expect: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    output = result.get("output", {})
    if result.get("ok") != expect.get("ok"):
        errors.append("ok mismatch")
    if trace_obj.get("validation_result") != expect.get("validation_result"):
        errors.append("validation_result mismatch")
    if "reason" in expect and result.get("reason") != expect["reason"]:
        errors.append("reason mismatch")
    if "missing_slots" in expect and result.get("missing_slots") != expect["missing_slots"]:
        errors.append("missing_slots mismatch")
    for key in expect.get("required_output_keys", []):
        if key not in output:
            errors.append(f"missing output key: {key}")
    if "first_route" in expect and output.get("first_route") != expect["first_route"]:
        errors.append("first_route mismatch")
    if "missing_contains" in expect and expect["missing_contains"] not in output.get("missing", []):
        errors.append("missing_contains mismatch")
    if "required_fields" in expect and output.get("required_fields") != expect["required_fields"]:
        errors.append("required_fields mismatch")
    if "memory_policy" in expect and output.get("memory_policy") != expect["memory_policy"]:
        errors.append("memory_policy mismatch")
    if "trace_policy" in expect and output.get("trace_policy") != expect["trace_policy"]:
        errors.append("trace_policy mismatch")
    if "gate" in expect and output.get("gate") != expect["gate"]:
        errors.append("gate mismatch")
    return not errors, errors


def run_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    parsed, parse_failure = parse_input(fixture["input"], fixture["id"])
    if parse_failure is not None:
        validation_result, failure_reason = validate(parse_failure.get("function_id"), parse_failure, None)
        trace_obj = emit_trace(parse_failure["run_id"], parse_failure.get("function_id"), None, validation_result, failure_reason)
        passed, errors = check_fixture(parse_failure, trace_obj, fixture["expect"])
        return {"fixture_id": fixture["id"], "passed": passed, "errors": errors, "result": parse_failure, "trace": trace_obj}

    assert parsed is not None
    function_id = parsed["function_id"]
    selected_function = function_id
    output = RUNNERS[function_id](parsed["slots"])
    result = {
        "ok": True,
        "function_id": function_id,
        "output": output,
        "final_task_executed": False,
        "memory_written": False,
    }
    validation_result, failure_reason = validate(function_id, result, selected_function)
    trace_obj = emit_trace(parsed["run_id"], function_id, selected_function, validation_result, failure_reason)
    passed, errors = check_fixture(result, trace_obj, fixture["expect"])
    return {"fixture_id": fixture["id"], "passed": passed, "errors": errors, "result": result, "trace": trace_obj}


def main() -> int:
    fixture_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("STABLE_BASIC_FUNCTIONS_FIXTURES_v0_1.json")
    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    results = [run_fixture(item) for item in data["fixtures"]]
    passed = sum(1 for item in results if item["passed"])
    summary = {
        "seed": SEED_ID,
        "stable_function_count": len(REGISTRY),
        "total": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "overall": "PASS" if passed == len(results) else "FAIL",
        "results": results,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
