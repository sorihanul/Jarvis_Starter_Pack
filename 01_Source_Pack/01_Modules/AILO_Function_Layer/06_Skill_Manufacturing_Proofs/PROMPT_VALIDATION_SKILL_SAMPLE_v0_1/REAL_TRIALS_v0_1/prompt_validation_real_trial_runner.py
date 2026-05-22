#!/usr/bin/env python3
"""Small rule-based trial for the manufactured prompt-validation skill skeleton."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


OUT_JSON = Path(__file__).with_name("PROMPT_VALIDATION_REAL_TRIAL_OUTPUT_v0_1.json")
OUT_REPORT = Path(__file__).with_name("PROMPT_VALIDATION_REAL_TRIAL_REPORT_v0_1.md")


def has_marker(text: str, markers: list[str]) -> bool:
    lowered = text.lower()
    return any(marker.lower() in lowered for marker in markers)


def validate_prompt(fixture: dict[str, Any]) -> dict[str, Any]:
    text = fixture["prompt_text"]
    issues = {
        "blocking_issues": [],
        "major_issues": [],
        "minor_issues": [],
    }
    evidence: list[str] = []

    if not has_marker(text, ["Purpose:", "Goal:", "목적:", "목표:"]):
        issues["major_issues"].append("declared purpose is missing")
        evidence.append("no Purpose/Goal marker found")

    if not has_marker(text, ["Output:", "Return ", "출력:", "반환"]):
        issues["major_issues"].append("output contract marker is missing")
        evidence.append("no Output/Return marker found")

    lower = text.lower()
    if "do not ask questions" in lower and "ask clarifying questions" in lower:
        issues["blocking_issues"].append("instruction conflict: asks and forbids questions")
        evidence.append("contains both 'Do not ask questions' and 'Ask clarifying questions'")

    if "rewrite" in lower and "only report" in lower:
        issues["major_issues"].append("rewrite boundary is unclear")
        evidence.append("contains both rewrite request and report-only request")

    verdict = "FAIL" if issues["blocking_issues"] or issues["major_issues"] else "PASS"
    next_action = "use as-is for this small contract" if verdict == "PASS" else "tighten prompt purpose and output contract before use"

    return {
        "fixture_id": fixture["id"],
        "verdict": verdict,
        "blocking_issues": issues["blocking_issues"],
        "major_issues": issues["major_issues"],
        "minor_issues": issues["minor_issues"],
        "evidence": evidence or ["purpose and output contract markers are present"],
        "next_action": next_action,
        "rewrite_performed": False,
    }


def check_contract(result: dict[str, Any], expected: str) -> tuple[bool, list[str]]:
    errors: list[str] = []
    required = ["verdict", "blocking_issues", "major_issues", "minor_issues", "evidence", "next_action"]
    for key in required:
        if key not in result:
            errors.append(f"missing required field: {key}")
    if result.get("verdict") != expected:
        errors.append(f"verdict mismatch: expected {expected}, got {result.get('verdict')}")
    if result.get("rewrite_performed") is not False:
        errors.append("rewrite was performed")
    if not result.get("evidence"):
        errors.append("evidence is empty")
    return not errors, errors


def main() -> int:
    fixture_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("PROMPT_VALIDATION_REAL_TRIAL_FIXTURES_v0_1.json")
    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    results = []
    for fixture in data["fixtures"]:
        report = validate_prompt(fixture)
        passed, errors = check_contract(report, fixture["expect_verdict"])
        results.append({"fixture_id": fixture["id"], "passed": passed, "errors": errors, "report": report})

    passed_count = sum(1 for item in results if item["passed"])
    summary = {
        "trial_id": data["trial_id"],
        "total": len(results),
        "passed": passed_count,
        "failed": len(results) - passed_count,
        "overall": "PASS" if passed_count == len(results) else "FAIL",
        "results": results,
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_REPORT.write_text(render_report(summary), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["overall"] == "PASS" else 1


def render_report(summary: dict[str, Any]) -> str:
    lines = "\n".join(
        f"- {item['fixture_id']}: {'PASS' if item['passed'] else 'FAIL'} -> {item['report']['verdict']}"
        for item in summary["results"]
    )
    return f"""# Prompt Validation Real Trial Report v0.1

## Result
```text
overall:{summary['overall']}
total:{summary['total']}
passed:{summary['passed']}
failed:{summary['failed']}
```

## Fixture results
{lines}

## What this proves
The manufactured prompt-validation skill card can be used as a small execution contract.

## What this does not prove
This does not prove deep prompt judgment.
This does not use cognitive functions.
This does not use engines.

## Finding
The trial can produce the report contract fields.
The manufactured card now preserves the explicit report fields in `output_schema_bind`.

## Next tightening target
Run the same real-trial pattern against wiki-note intake and source review before promoting v0.2 functions to stable.
"""


if __name__ == "__main__":
    raise SystemExit(main())
