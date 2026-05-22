#!/usr/bin/env python3
"""Small rule-based trial for the manufactured source-review skill skeleton."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


OUT_JSON = Path(__file__).with_name("SOURCE_REVIEW_REAL_TRIAL_OUTPUT_v0_1.json")
OUT_REPORT = Path(__file__).with_name("SOURCE_REVIEW_REAL_TRIAL_REPORT_v0_1.md")


def collect_prefixed(text: str, prefix: str) -> list[str]:
    normalized = text.replace("\\n", "\n")
    items: list[str] = []
    for line in normalized.splitlines():
        if line.lower().startswith(prefix.lower()):
            items.append(line.split(":", 1)[1].strip())
    return items


def review_source(fixture: dict[str, Any]) -> dict[str, Any]:
    source_text = str(fixture["source_text"])
    claims = collect_prefixed(source_text, "Claim")
    evidence = collect_prefixed(source_text, "Evidence")
    uncertainty = collect_prefixed(source_text, "Uncertainty")

    issues: list[str] = []
    issue_evidence: list[str] = []

    if not fixture.get("source_path"):
        issues.append("source path is missing")
        issue_evidence.append("source_path is empty")

    if not claims:
        issues.append("claim is missing")
        issue_evidence.append("no Claim marker found")

    if not evidence or any(item.lower() in {"none", "no evidence"} for item in evidence):
        issues.append("supporting evidence is missing")
        issue_evidence.append("no usable Evidence marker found")

    joined_claims = " ".join(claims).lower()
    if "production ready" in joined_claims or "all prompt validation tasks" in joined_claims:
        if not evidence or any(item.lower() in {"none", "no evidence"} for item in evidence):
            issues.append("broad readiness claim is unsupported")
            issue_evidence.append("claim uses production/all-task language without evidence")

    verdict = "FAIL" if issues else "PASS"
    return {
        "fixture_id": fixture["id"],
        "verdict": verdict,
        "summary": claims[0] if claims else "No claim extracted.",
        "claims": claims,
        "evidence": evidence if evidence and evidence != ["none"] else issue_evidence,
        "uncertainty": uncertainty,
        "next_action": "keep as bounded reviewed source" if verdict == "PASS" else "repair evidence or narrow the claim",
        "issues": issues,
        "source_rewritten": False,
        "memory_written": False,
    }


def check_contract(packet: dict[str, Any], expected: str) -> tuple[bool, list[str]]:
    errors: list[str] = []
    required = ["summary", "claims", "evidence", "uncertainty", "next_action"]
    for key in required:
        if key not in packet:
            errors.append(f"missing required field: {key}")
    if packet.get("verdict") != expected:
        errors.append(f"verdict mismatch: expected {expected}, got {packet.get('verdict')}")
    if packet.get("source_rewritten") is not False:
        errors.append("source rewrite occurred")
    if packet.get("memory_written") is not False:
        errors.append("memory write occurred")
    if not packet.get("evidence"):
        errors.append("evidence is empty")
    return not errors, errors


def main() -> int:
    fixture_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("SOURCE_REVIEW_REAL_TRIAL_FIXTURES_v0_1.json")
    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    results = []
    for fixture in data["fixtures"]:
        packet = review_source(fixture)
        passed, errors = check_contract(packet, fixture["expect_verdict"])
        results.append({"fixture_id": fixture["id"], "passed": passed, "errors": errors, "packet": packet})

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
        f"- {item['fixture_id']}: {'PASS' if item['passed'] else 'FAIL'} -> {item['packet']['verdict']}"
        for item in summary["results"]
    )
    return f"""# Source Review Real Trial Report v0.1

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
The manufactured source-review skill card can be used as a small claim/evidence/uncertainty separation contract.

## What this does not prove
This does not prove deep source-review judgment.
This does not read real project files.
This does not use cognitive functions.
This does not use engines.

## Finding
The trial checks that broad claims without evidence fail while bounded claim/evidence/uncertainty packets pass.

## Next tightening target
Compare the three real-trial results and decide whether v0.2 skill-skeleton functions should become stable candidates or need another tightening pass.
"""


if __name__ == "__main__":
    raise SystemExit(main())
