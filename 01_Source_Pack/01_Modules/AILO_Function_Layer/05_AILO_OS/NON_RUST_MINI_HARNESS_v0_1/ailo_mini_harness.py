#!/usr/bin/env python3
"""Non-Rust mini harness for stable AILO basic functions.

This file intentionally reuses the stable mock runner.
Rust comes later, after this behavior is observed and tightened.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STABLE_SEED_DIR = ROOT / "HARNESS_SEED_STABLE_BASIC_FUNCTIONS_v0_1"
RUNNER_PATH = STABLE_SEED_DIR / "stable_basic_functions_mock_runner.py"
DEFAULT_FIXTURES = STABLE_SEED_DIR / "STABLE_BASIC_FUNCTIONS_FIXTURES_v0_1.json"
NEGATIVE_FIXTURES = STABLE_SEED_DIR / "STABLE_BASIC_FUNCTIONS_NEGATIVE_FIXTURES_v0_1.json"
SKILL_SERIES_DIR = ROOT / "HARNESS_SEED_SKILL_SKELETON_FUNCTIONS_v0_2"
SKILL_SERIES_RUNNER = SKILL_SERIES_DIR / "skill_skeleton_functions_mock_runner.py"
SKILL_SERIES_FIXTURES = SKILL_SERIES_DIR / "SKILL_SKELETON_FUNCTIONS_FIXTURES_v0_2.json"


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.name


def load_runner():
    spec = importlib.util.spec_from_file_location("stable_basic_functions_mock_runner", RUNNER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load runner: {RUNNER_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_runner_from(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load runner: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_fixtures(fixture_path: Path) -> dict[str, Any]:
    runner = load_runner()
    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    results = [runner.run_fixture(item) for item in data["fixtures"]]
    passed = sum(1 for item in results if item["passed"])
    return {
        "mode": "run-fixtures",
        "fixture_file": display_path(fixture_path),
        "total": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "overall": "PASS" if passed == len(results) else "FAIL",
        "results": results,
    }


def run_skill_series() -> dict[str, Any]:
    runner = load_runner_from(SKILL_SERIES_RUNNER, "skill_skeleton_functions_mock_runner")
    data = json.loads(SKILL_SERIES_FIXTURES.read_text(encoding="utf-8"))
    results = [runner.run_fixture(item) for item in data["fixtures"]]
    passed = sum(1 for item in results if item["passed"])
    return {
        "mode": "run-skill-series",
        "fixture_file": display_path(SKILL_SERIES_FIXTURES),
        "total": len(results),
        "passed": passed,
        "failed": len(results) - passed,
        "overall": "PASS" if passed == len(results) else "FAIL",
        "results": results,
    }


def run_one(input_path: Path) -> dict[str, Any]:
    runner = load_runner()
    raw = json.loads(input_path.read_text(encoding="utf-8"))
    fixture = {
        "id": raw.get("run_id", "run-one"),
        "input": raw,
        "expect": {
            "ok": True,
            "validation_result": "PASS",
            "required_output_keys": [],
        },
    }
    result = runner.run_fixture(fixture)
    return {
        "mode": "run-one",
        "input_file": display_path(input_path),
        "overall": "PASS" if result["trace"]["validation_result"] == "PASS" else "FAIL",
        "result": result["result"],
        "trace": result["trace"],
    }


def main() -> int:
    command = sys.argv[1] if len(sys.argv) > 1 else "run-fixtures"

    if command == "run-fixtures":
        fixture_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_FIXTURES
        summary = run_fixtures(fixture_path)
    elif command == "run-negative-fixtures":
        summary = run_fixtures(NEGATIVE_FIXTURES)
    elif command == "run-one":
        if len(sys.argv) < 3:
            raise SystemExit("run-one requires an input json path")
        summary = run_one(Path(sys.argv[2]))
    elif command == "run-skill-series":
        summary = run_skill_series()
    else:
        raise SystemExit(f"unknown command: {command}")

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["overall"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
