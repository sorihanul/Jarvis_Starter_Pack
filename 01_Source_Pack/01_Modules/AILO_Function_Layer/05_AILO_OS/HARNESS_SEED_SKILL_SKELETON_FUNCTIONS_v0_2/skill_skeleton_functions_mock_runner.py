#!/usr/bin/env python3
"""Mock runner for AILO basic skill-skeleton functions v0.2.

This runner is deliberately simple:
- explicit function_id only
- no smart routing
- no cognitive functions
- no file writes
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Callable


SEED_ID = "ailo_os_harness_seed.skill_skeleton_functions"


REGISTRY: dict[str, dict[str, Any]] = {
    "basic_fn.input_contract_bind.v0.2": {
        "required_slots": ["skill_goal"],
        "output_schema": ["required_inputs", "optional_inputs", "rejected_inputs", "missing_inputs"],
        "trace_policy": "min",
    },
    "basic_fn.step_sequence_lock.v0.2": {
        "required_slots": ["skill_goal", "candidate_steps"],
        "output_schema": ["ordered_steps", "optional_steps", "forbidden_reorder", "stop_rule"],
        "trace_policy": "min",
    },
    "basic_fn.acceptance_criteria_bind.v0.2": {
        "required_slots": ["output_goal"],
        "output_schema": ["pass_if", "fail_if", "proof_required", "review_stop_rule"],
        "trace_policy": "min",
    },
    "basic_fn.fixture_contract_bind.v0.2": {
        "required_slots": ["function_or_skill_id", "input_contract", "output_contract"],
        "output_schema": ["positive_fixture_shape", "negative_fixture_shape", "required_assertions", "fixture_stop_rule"],
        "trace_policy": "min",
    },
    "basic_fn.handoff_packet_bind.v0.2": {
        "required_slots": ["current_stage", "next_stage", "artifact_summary"],
        "output_schema": ["handoff_fields", "required_artifacts", "open_items", "next_entrypoint"],
        "trace_policy": "structured",
    },
    "basic_fn.retry_policy_check.v0.2": {
        "required_slots": ["failure_reason", "attempt_count", "max_attempts"],
        "output_schema": ["retry_decision", "reason", "next_attempt_change", "stop_condition"],
        "trace_policy": "structured",
    },
    "basic_fn.cost_budget_lock.v0.2": {
        "required_slots": ["task_scope"],
        "output_schema": ["read_limit", "token_budget", "time_budget", "expansion_trigger"],
        "trace_policy": "min",
    },
    "basic_fn.dependency_check.v0.2": {
        "required_slots": ["required_dependencies", "available_dependencies"],
        "output_schema": ["satisfied", "missing", "blocked", "next_requirement"],
        "trace_policy": "min",
    },
}


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def failure(run_id: str, function_id: str | None, reason: str, missing_slots: list[str]) -> dict[str, Any]:
    return {
        "ok": False,
        "function_id": function_id,
        "reason": reason,
        "missing_slots": missing_slots,
        "suggested_layer": "basic_function_tightening",
        "final_task_executed": False,
        "memory_written": False,
        "run_id": run_id,
    }


def parse_input(raw: dict[str, Any], fallback_run_id: str) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    run_id = raw.get("run_id", fallback_run_id)
    function_id = raw.get("function_id")
    slots = raw.get("slots", {})
    if function_id not in REGISTRY:
        return None, failure(run_id, function_id, "unknown_function", [])
    if not isinstance(slots, dict):
        return None, failure(run_id, function_id, "missing_required_input", ["slots"])
    required = REGISTRY[function_id]["required_slots"]
    missing = [slot for slot in required if slot not in slots or slots[slot] in ("", None)]
    if missing:
        return None, failure(run_id, function_id, "missing_required_input", missing)
    return {"run_id": run_id, "function_id": function_id, "slots": slots}, None


def run_input_contract_bind(slots: dict[str, Any]) -> dict[str, Any]:
    raw_inputs = [str(x) for x in as_list(slots.get("raw_inputs"))]
    required = [str(x) for x in as_list(slots.get("required_candidates"))] or raw_inputs[:2]
    optional = [x for x in raw_inputs if x not in required]
    missing = [x for x in required if x not in raw_inputs] if raw_inputs else []
    return {
        "required_inputs": required,
        "optional_inputs": optional,
        "rejected_inputs": [],
        "missing_inputs": missing,
    }


def run_step_sequence_lock(slots: dict[str, Any]) -> dict[str, Any]:
    steps = [str(x) for x in as_list(slots["candidate_steps"])]
    return {
        "ordered_steps": steps,
        "optional_steps": [],
        "forbidden_reorder": steps,
        "stop_rule": "stop after locking the step order; do not execute the steps",
    }


def run_acceptance_criteria_bind(slots: dict[str, Any]) -> dict[str, Any]:
    quality = [str(x) for x in as_list(slots.get("quality_constraints"))]
    failures = [str(x) for x in as_list(slots.get("failure_constraints"))]
    return {
        "pass_if": quality or ["output matches goal", "required fields exist"],
        "fail_if": failures or ["required evidence missing", "output shape drift"],
        "proof_required": ["fixture result", "field check"],
        "review_stop_rule": "stop after pass/fail criteria are explicit",
    }


def run_fixture_contract_bind(slots: dict[str, Any]) -> dict[str, Any]:
    input_contract = [str(x) for x in as_list(slots["input_contract"])]
    output_contract = [str(x) for x in as_list(slots["output_contract"])]
    return {
        "positive_fixture_shape": {"input": input_contract, "expect": output_contract},
        "negative_fixture_shape": {"missing_input": input_contract[:1], "expect": "FAIL"},
        "required_assertions": ["ok matches expected", "required output fields exist"],
        "fixture_stop_rule": "start with one positive and one negative fixture",
    }


def run_handoff_packet_bind(slots: dict[str, Any]) -> dict[str, Any]:
    open_items = [str(x) for x in as_list(slots.get("open_items"))]
    return {
        "handoff_fields": ["current_stage", "next_stage", "artifact_summary", "open_items", "next_entrypoint"],
        "required_artifacts": [str(slots["artifact_summary"])],
        "open_items": open_items,
        "next_entrypoint": str(slots["next_stage"]),
    }


def run_retry_policy_check(slots: dict[str, Any]) -> dict[str, Any]:
    attempt_count = int(slots["attempt_count"])
    max_attempts = int(slots["max_attempts"])
    risk = str(slots.get("risk", "mid")).lower()
    if risk == "high":
        decision = "ESCALATE"
    elif attempt_count < max_attempts:
        decision = "RETRY"
    else:
        decision = "STOP"
    return {
        "retry_decision": decision,
        "reason": f"failure_reason={slots['failure_reason']}, attempt={attempt_count}/{max_attempts}, risk={risk}",
        "next_attempt_change": "reduce scope and rerun validation" if decision == "RETRY" else "do not retry without new information",
        "stop_condition": "stop when max attempts are reached or risk is high",
    }


def run_cost_budget_lock(slots: dict[str, Any]) -> dict[str, Any]:
    available = str(slots.get("available_budget", "small")).lower()
    if available == "large":
        token_budget = "medium"
        time_budget = "medium"
    else:
        token_budget = "small"
        time_budget = "small"
    return {
        "read_limit": "first route only unless expansion trigger fires",
        "token_budget": token_budget,
        "time_budget": time_budget,
        "expansion_trigger": "missing required evidence or blocked validation",
    }


def run_dependency_check(slots: dict[str, Any]) -> dict[str, Any]:
    required = [str(x) for x in as_list(slots["required_dependencies"])]
    available = set(str(x) for x in as_list(slots["available_dependencies"]))
    satisfied = [x for x in required if x in available]
    missing = [x for x in required if x not in available]
    return {
        "satisfied": satisfied,
        "missing": missing,
        "blocked": bool(missing),
        "next_requirement": missing[0] if missing else "none",
    }


RUNNERS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "basic_fn.input_contract_bind.v0.2": run_input_contract_bind,
    "basic_fn.step_sequence_lock.v0.2": run_step_sequence_lock,
    "basic_fn.acceptance_criteria_bind.v0.2": run_acceptance_criteria_bind,
    "basic_fn.fixture_contract_bind.v0.2": run_fixture_contract_bind,
    "basic_fn.handoff_packet_bind.v0.2": run_handoff_packet_bind,
    "basic_fn.retry_policy_check.v0.2": run_retry_policy_check,
    "basic_fn.cost_budget_lock.v0.2": run_cost_budget_lock,
    "basic_fn.dependency_check.v0.2": run_dependency_check,
}


def validate(function_id: str | None, result: dict[str, Any]) -> tuple[str, str | None]:
    if not result.get("ok"):
        return "FAIL", result.get("reason", "validation_failed")
    if function_id not in REGISTRY:
        return "FAIL", "unknown_function"
    output = result.get("output", {})
    if not all(key in output for key in REGISTRY[function_id]["output_schema"]):
        return "FAIL", "validation_failed"
    if result.get("memory_written") is not False:
        return "FAIL", "memory_written"
    if result.get("final_task_executed") is not False:
        return "FAIL", "execution_forbidden"
    return "PASS", None


def emit_trace(run_id: str, function_id: str | None, validation_result: str, failure_reason: str | None) -> dict[str, Any]:
    return {
        "run_id": run_id,
        "seed": SEED_ID,
        "selected_function": function_id if function_id in REGISTRY else None,
        "input_keys": ["function_id", "slots"],
        "output_keys": REGISTRY[function_id]["output_schema"] if function_id in REGISTRY else [],
        "memory_policy": "none",
        "trace_policy": REGISTRY[function_id]["trace_policy"] if function_id in REGISTRY else "min",
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
    if "retry_decision" in expect and output.get("retry_decision") != expect["retry_decision"]:
        errors.append("retry_decision mismatch")
    if "blocked" in expect and output.get("blocked") != expect["blocked"]:
        errors.append("blocked mismatch")
    return not errors, errors


def run_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    parsed, parse_failure = parse_input(fixture["input"], fixture["id"])
    if parse_failure is not None:
        validation_result, failure_reason = validate(parse_failure.get("function_id"), parse_failure)
        trace_obj = emit_trace(parse_failure["run_id"], parse_failure.get("function_id"), validation_result, failure_reason)
        passed, errors = check_fixture(parse_failure, trace_obj, fixture["expect"])
        return {"fixture_id": fixture["id"], "passed": passed, "errors": errors, "result": parse_failure, "trace": trace_obj}

    assert parsed is not None
    output = RUNNERS[parsed["function_id"]](parsed["slots"])
    result = {
        "ok": True,
        "function_id": parsed["function_id"],
        "output": output,
        "final_task_executed": False,
        "memory_written": False,
        "run_id": parsed["run_id"],
    }
    validation_result, failure_reason = validate(parsed["function_id"], result)
    trace_obj = emit_trace(parsed["run_id"], parsed["function_id"], validation_result, failure_reason)
    passed, errors = check_fixture(result, trace_obj, fixture["expect"])
    return {"fixture_id": fixture["id"], "passed": passed, "errors": errors, "result": result, "trace": trace_obj}


def main() -> int:
    fixture_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("SKILL_SKELETON_FUNCTIONS_FIXTURES_v0_2.json")
    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    results = [run_fixture(item) for item in data["fixtures"]]
    passed = sum(1 for item in results if item["passed"])
    summary = {
        "seed": SEED_ID,
        "function_count": len(REGISTRY),
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
