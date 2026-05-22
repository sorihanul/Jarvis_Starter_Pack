#!/usr/bin/env python3
"""Deterministic mock runner for ailo_os_harness_seed.scope_lock.

This is not a full runtime. It proves the seed contract for one stable function.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


SEED_ID = "ailo_os_harness_seed.scope_lock"
FUNCTION_ID = "basic_fn.scope_lock.v0.1"

REGISTRY = [
    {
        "id": FUNCTION_ID,
        "name": "scope_lock",
        "layer": "basic_function_common_layer",
        "required_slots": ["user_request"],
        "optional_slots": ["known_context"],
        "output_schema": [
            "bounded_scope",
            "out_of_scope",
            "missing_slots",
            "stop_condition",
        ],
        "memory_policy": "none",
        "trace_policy": "min",
        "forbids": [
            "final_task_execution",
            "deep_meaning_judgment",
            "domain_reasoning",
        ],
    }
]


def parse_input(raw: dict[str, Any], fallback_run_id: str) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    function_id = raw.get("function_id", FUNCTION_ID)
    user_request = raw.get("user_request", "")
    known_context = raw.get("known_context", None)
    run_id = raw.get("run_id", fallback_run_id)

    if not isinstance(user_request, str) or not user_request.strip():
        return None, failure(
            run_id=run_id,
            function_id=function_id if isinstance(function_id, str) else None,
            reason="missing_required_input",
            missing_slots=["user_request"],
            suggested_layer="basic_function_tightening",
        )

    return {
        "run_id": run_id,
        "function_id": function_id,
        "slots": {
            "user_request": user_request,
            "known_context": known_context,
        },
    }, None


def registry_lookup(function_id: str) -> dict[str, Any] | None:
    matches = [item for item in REGISTRY if item["id"] == function_id]
    if len(matches) != 1:
        return None
    return matches[0]


def fixed_select(parsed: dict[str, Any], registry_record: dict[str, Any] | None) -> str | None:
    if registry_record is None:
        return None
    if parsed["function_id"] != FUNCTION_ID:
        return None
    return FUNCTION_ID


def run_scope_lock(parsed: dict[str, Any], registry_record: dict[str, Any]) -> dict[str, Any]:
    user_request = parsed["slots"]["user_request"].strip()
    out_of_scope = [
        "perform the final task",
        "modify source documents",
        "write memory",
        "call cognitive functions",
        "call engines",
    ]

    if any(token in user_request for token in ["고쳐", "수정", "반영", "작성", "만들"]):
        out_of_scope.append("perform the actual edit")

    return {
        "ok": True,
        "function_id": registry_record["id"],
        "output": {
            "bounded_scope": f"lock the execution scope for request: {user_request}",
            "out_of_scope": out_of_scope,
            "missing_slots": [],
            "stop_condition": "stop after returning the bounded scope, excluded work, missing slots, and stop condition",
        },
        "final_task_executed": False,
        "memory_written": False,
    }


def failure(
    run_id: str,
    function_id: str | None,
    reason: str,
    missing_slots: list[str],
    suggested_layer: str,
) -> dict[str, Any]:
    return {
        "ok": False,
        "function_id": function_id,
        "reason": reason,
        "missing_slots": missing_slots,
        "suggested_layer": suggested_layer,
        "run_id": run_id,
        "final_task_executed": False,
        "memory_written": False,
    }


def validate(run_id: str, result: dict[str, Any], selected_function: str | None) -> tuple[str, str | None]:
    if not result.get("ok"):
        return "FAIL", result.get("reason", "validation_failed")

    output = result.get("output", {})
    required = REGISTRY[0]["output_schema"]
    if not all(key in output for key in required):
        return "FAIL", "validation_failed"
    if result.get("memory_written") is not False:
        return "FAIL", "memory_written"
    if result.get("final_task_executed") is not False:
        return "FAIL", "execution_forbidden"
    if selected_function != FUNCTION_ID:
        return "FAIL", "unknown_function"
    return "PASS", None


def trace(run_id: str, selected_function: str | None, validation_result: str, failure_reason: str | None) -> dict[str, Any]:
    return {
        "run_id": run_id,
        "seed": SEED_ID,
        "selected_function": selected_function,
        "input_keys": ["user_request", "known_context"],
        "output_keys": REGISTRY[0]["output_schema"],
        "memory_policy": "none",
        "trace_policy": "min",
        "validation_result": validation_result,
        "failure_reason": failure_reason,
    }


def check_fixture(result: dict[str, Any], trace_obj: dict[str, Any], expect: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if result.get("ok") != expect.get("ok"):
        errors.append("ok mismatch")
    if trace_obj.get("validation_result") != expect.get("validation_result"):
        errors.append("validation_result mismatch")
    if "reason" in expect and result.get("reason") != expect["reason"]:
        errors.append("reason mismatch")
    if "suggested_layer" in expect and result.get("suggested_layer") != expect["suggested_layer"]:
        errors.append("suggested_layer mismatch")
    if "missing_slots" in expect and result.get("missing_slots") != expect["missing_slots"]:
        errors.append("missing_slots mismatch")
    if expect.get("memory_policy") and trace_obj.get("memory_policy") != expect["memory_policy"]:
        errors.append("memory_policy mismatch")
    if "required_output_keys" in expect:
        output = result.get("output", {})
        for key in expect["required_output_keys"]:
            if key not in output:
                errors.append(f"missing output key: {key}")
    if "out_of_scope_contains" in expect:
        out_of_scope = result.get("output", {}).get("out_of_scope", [])
        if expect["out_of_scope_contains"] not in out_of_scope:
            errors.append("out_of_scope_contains mismatch")
    if "final_task_executed" in expect and result.get("final_task_executed") != expect["final_task_executed"]:
        errors.append("final_task_executed mismatch")
    return not errors, errors


def run_fixture(fixture: dict[str, Any]) -> dict[str, Any]:
    parsed, parse_failure = parse_input(fixture["input"], fixture["id"])
    selected_function: str | None = None

    if parse_failure is not None:
        validation_result, failure_reason = validate(parse_failure["run_id"], parse_failure, None)
        trace_obj = trace(parse_failure["run_id"], None, validation_result, failure_reason)
        passed, errors = check_fixture(parse_failure, trace_obj, fixture["expect"])
        return {
            "fixture_id": fixture["id"],
            "passed": passed,
            "errors": errors,
            "result": parse_failure,
            "trace": trace_obj,
        }

    assert parsed is not None
    run_id = parsed["run_id"]
    registry_record = registry_lookup(parsed["function_id"])

    if registry_record is None:
        result = failure(
            run_id=run_id,
            function_id=parsed["function_id"],
            reason="unknown_function",
            missing_slots=[],
            suggested_layer="harness_contract_fix",
        )
        validation_result, failure_reason = validate(run_id, result, None)
        trace_obj = trace(run_id, None, validation_result, failure_reason)
        passed, errors = check_fixture(result, trace_obj, fixture["expect"])
        return {
            "fixture_id": fixture["id"],
            "passed": passed,
            "errors": errors,
            "result": result,
            "trace": trace_obj,
        }

    selected_function = fixed_select(parsed, registry_record)
    result = run_scope_lock(parsed, registry_record)
    validation_result, failure_reason = validate(run_id, result, selected_function)
    trace_obj = trace(run_id, selected_function, validation_result, failure_reason)
    passed, errors = check_fixture(result, trace_obj, fixture["expect"])
    return {
        "fixture_id": fixture["id"],
        "passed": passed,
        "errors": errors,
        "result": result,
        "trace": trace_obj,
    }


def main() -> int:
    fixture_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("SCOPE_LOCK_SEED_FIXTURES_v0_1.json")
    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    results = [run_fixture(item) for item in data["fixtures"]]
    passed = sum(1 for item in results if item["passed"])
    summary = {
        "seed": SEED_ID,
        "function": FUNCTION_ID,
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
