#!/usr/bin/env python3
"""Check failure-output consistency for skill-skeleton basic functions v0.2."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "skill_skeleton_functions_mock_runner.py"
FIXTURES = ROOT / "SKILL_SKELETON_FUNCTIONS_FIXTURES_v0_2.json"
OUTPUT = ROOT / "SKILL_SKELETON_FAILURE_CONSISTENCY_OUTPUT_v0_2.json"

EXPECTED_FUNCTIONS = {
    "basic_fn.input_contract_bind.v0.2",
    "basic_fn.step_sequence_lock.v0.2",
    "basic_fn.acceptance_criteria_bind.v0.2",
    "basic_fn.fixture_contract_bind.v0.2",
    "basic_fn.handoff_packet_bind.v0.2",
    "basic_fn.retry_policy_check.v0.2",
    "basic_fn.cost_budget_lock.v0.2",
    "basic_fn.dependency_check.v0.2",
}

REQUIRED_FAILURE_KEYS = {
    "ok",
    "function_id",
    "reason",
    "missing_slots",
    "suggested_layer",
    "final_task_executed",
    "memory_written",
    "run_id",
}

REQUIRED_TRACE_KEYS = {
    "run_id",
    "seed",
    "selected_function",
    "input_keys",
    "output_keys",
    "memory_policy",
    "trace_policy",
    "validation_result",
    "failure_reason",
}


def load_runner_output() -> dict[str, Any]:
    run = subprocess.run(
        [sys.executable, str(RUNNER), str(FIXTURES)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if run.returncode != 0:
        return {
            "runner_ok": False,
            "runner_returncode": run.returncode,
            "runner_stderr": run.stderr.strip(),
            "runner_stdout": run.stdout.strip(),
        }
    return {"runner_ok": True, "runner_output": json.loads(run.stdout)}


def check_failure_item(item: dict[str, Any]) -> dict[str, Any]:
    result = item.get("result", {})
    trace = item.get("trace", {})
    errors: list[str] = []

    missing_failure_keys = sorted(REQUIRED_FAILURE_KEYS - set(result))
    if missing_failure_keys:
        errors.append(f"missing failure keys: {missing_failure_keys}")

    missing_trace_keys = sorted(REQUIRED_TRACE_KEYS - set(trace))
    if missing_trace_keys:
        errors.append(f"missing trace keys: {missing_trace_keys}")

    if result.get("ok") is not False:
        errors.append("ok is not false")
    if result.get("reason") != "missing_required_input":
        errors.append("reason is not missing_required_input")
    if not isinstance(result.get("missing_slots"), list) or not result.get("missing_slots"):
        errors.append("missing_slots is not a non-empty list")
    if result.get("suggested_layer") != "basic_function_tightening":
        errors.append("suggested_layer is not basic_function_tightening")
    if result.get("final_task_executed") is not False:
        errors.append("final_task_executed is not false")
    if result.get("memory_written") is not False:
        errors.append("memory_written is not false")

    if trace.get("validation_result") != "FAIL":
        errors.append("trace validation_result is not FAIL")
    if trace.get("failure_reason") != "missing_required_input":
        errors.append("trace failure_reason is not missing_required_input")
    if trace.get("memory_policy") != "none":
        errors.append("trace memory_policy is not none")
    if trace.get("run_id") != result.get("run_id"):
        errors.append("trace run_id does not match failure run_id")

    return {
        "fixture_id": item.get("fixture_id"),
        "function_id": result.get("function_id"),
        "passed": not errors,
        "errors": errors,
        "failure_keys": sorted(result.keys()),
        "trace_keys": sorted(trace.keys()),
    }


def main() -> int:
    loaded = load_runner_output()
    if not loaded["runner_ok"]:
        OUTPUT.write_text(json.dumps(loaded, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(loaded, ensure_ascii=False, indent=2))
        return 1

    runner_output = loaded["runner_output"]
    failure_items = [
        item
        for item in runner_output.get("results", [])
        if item.get("result", {}).get("ok") is False
    ]
    checks = [check_failure_item(item) for item in failure_items]
    covered_functions = {item["function_id"] for item in checks if item.get("function_id")}
    missing_functions = sorted(EXPECTED_FUNCTIONS - covered_functions)
    unexpected_functions = sorted(covered_functions - EXPECTED_FUNCTIONS)

    passed = sum(1 for item in checks if item["passed"])
    summary = {
        "check": "SKILL_SKELETON_FAILURE_CONSISTENCY_v0_2",
        "failure_cases": len(checks),
        "passed": passed,
        "failed": len(checks) - passed,
        "expected_function_count": len(EXPECTED_FUNCTIONS),
        "covered_function_count": len(covered_functions),
        "missing_functions": missing_functions,
        "unexpected_functions": unexpected_functions,
        "overall": "PASS"
        if passed == len(checks) and not missing_functions and not unexpected_functions
        else "FAIL",
        "checks": checks,
    }
    OUTPUT.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
