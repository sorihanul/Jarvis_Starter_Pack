#!/usr/bin/env python3
"""Small rule-based trial for the manufactured wiki-note-intake skill skeleton."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


OUT_JSON = Path(__file__).with_name("WIKI_NOTE_INTAKE_REAL_TRIAL_OUTPUT_v0_1.json")
OUT_REPORT = Path(__file__).with_name("WIKI_NOTE_INTAKE_REAL_TRIAL_REPORT_v0_1.md")


def load_card_contract(card_path: Path) -> str:
    return card_path.read_text(encoding="utf-8")


def line_after(text: str, prefix: str) -> str | None:
    for line in text.splitlines():
        if line.lower().startswith(prefix.lower()):
            return line.split(":", 1)[1].strip()
    return None


def extract_claims(text: str) -> list[str]:
    claims: list[str] = []
    for line in text.splitlines():
        if line.lower().startswith("claim:"):
            claims.append(line.split(":", 1)[1].strip())
    return claims


def validate_wiki_intake(fixture: dict[str, Any], card_text: str) -> dict[str, Any]:
    raw_text = str(fixture["raw_note_text"]).replace("\\n", "\n")
    source = line_after(raw_text, "Source")
    claims = extract_claims(raw_text)
    uncertainty = [line_after(raw_text, "Uncertainty")] if line_after(raw_text, "Uncertainty") else []
    lower = raw_text.lower()

    major_issues: list[str] = []
    evidence: list[str] = []

    if "candidate_status" not in card_text:
        major_issues.append("skill card output contract lacks candidate_status")
        evidence.append("candidate_status not found in skill card")

    if not fixture.get("raw_note_path"):
        major_issues.append("raw source path is missing")
        evidence.append("raw_note_path is empty")

    if not source:
        major_issues.append("source trace is missing")
        evidence.append("no Source marker found")

    if "promote directly to canon" in lower or "permanent rule immediately" in lower:
        major_issues.append("canon promotion boundary violation")
        evidence.append("raw note requests direct canon promotion")

    verdict = "FAIL" if major_issues else "PASS"
    candidate_title = Path(fixture["raw_note_path"]).stem.replace("-", " ").title()
    packet = {
        "fixture_id": fixture["id"],
        "verdict": verdict,
        "candidate_title": candidate_title,
        "candidate_status": "candidate_only",
        "summary": claims[0] if claims else "No reusable claim extracted.",
        "source_trace": {
            "raw_note_path": fixture.get("raw_note_path"),
            "source": source,
        },
        "claims": claims,
        "uncertainty": [item for item in uncertainty if item],
        "links_to_create": suggest_links(claims),
        "next_action": "keep as candidate" if verdict == "PASS" else "repair source trace or remove canon-promotion request",
        "major_issues": major_issues,
        "evidence": evidence or ["raw path, source marker, candidate boundary are present"],
        "canon_promoted": False,
        "memory_written": False,
    }
    return packet


def suggest_links(claims: list[str]) -> list[str]:
    links: list[str] = []
    joined = " ".join(claims).lower()
    if "conversation" in joined:
        links.append("[[Conversation Memory]]")
    if "candidate" in joined:
        links.append("[[Canon Candidate]]")
    return links


def check_contract(packet: dict[str, Any], expected: str) -> tuple[bool, list[str]]:
    errors: list[str] = []
    required = [
        "candidate_title",
        "candidate_status",
        "summary",
        "source_trace",
        "claims",
        "uncertainty",
        "links_to_create",
        "next_action",
    ]
    for key in required:
        if key not in packet:
            errors.append(f"missing required field: {key}")
    if packet.get("verdict") != expected:
        errors.append(f"verdict mismatch: expected {expected}, got {packet.get('verdict')}")
    if packet.get("candidate_status") != "candidate_only":
        errors.append("candidate_status is not candidate_only")
    if packet.get("canon_promoted") is not False:
        errors.append("canon promotion occurred")
    if packet.get("memory_written") is not False:
        errors.append("memory write occurred")
    return not errors, errors


def main() -> int:
    fixture_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("WIKI_NOTE_INTAKE_REAL_TRIAL_FIXTURES_v0_1.json")
    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    card_path = (fixture_path.parent / data["skill_card"]).resolve()
    card_text = load_card_contract(card_path)

    results = []
    for fixture in data["fixtures"]:
        packet = validate_wiki_intake(fixture, card_text)
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
    return f"""# Wiki Note Intake Real Trial Report v0.1

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
The manufactured wiki-note-intake skill card can be used as a small candidate-only intake contract.

## What this does not prove
This does not prove full wikiization quality.
This does not write a real wiki note.
This does not use cognitive functions.
This does not use engines.

## Finding
The trial checks that candidate status, source trace, and canon-promotion boundary are explicit.

## Next tightening target
Run source-review real trial, then decide whether v0.2 skill-skeleton functions are ready for a stronger stable-candidate review.
"""


if __name__ == "__main__":
    raise SystemExit(main())
