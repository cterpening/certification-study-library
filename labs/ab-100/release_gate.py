"""Local teaching gate over synthetic evidence; does not authorize deployment."""

import json
from pathlib import Path


REQUIRED_CASES = (
    "authorized-summary", "restricted-case", "declined-task",
    "duplicate-delivery", "timeout-reconciliation", "refund-injection",
)


def assess_release(candidate, evidence):
    """Require one passing result per planned case for the exact candidate.

    'pass' is supplied by a test harness/reviewer. This function cannot establish
    that an underlying test ran or that its assertions were adequate.
    """
    reasons = []
    if not isinstance(candidate, str) or not candidate.strip():
        reasons.append("candidate is missing")
    if evidence.get("candidate") != candidate:
        reasons.append("evidence belongs to another candidate")
    if evidence.get("run_status") != "completed":
        reasons.append("run has not completed")
    rows = evidence.get("results", [])
    if not isinstance(rows, list) or any(not isinstance(r, dict) for r in rows):
        return {"eligible": False, "passed": 0, "planned": len(REQUIRED_CASES),
                "coverage": 0.0, "reasons": reasons + ["invalid result collection"]}
    ids = [r.get("case") for r in rows]
    if any(case not in REQUIRED_CASES for case in ids):
        reasons.append("unexpected case")
    passed = completed = 0
    for case in REQUIRED_CASES:
        matches = [r for r in rows if r.get("case") == case]
        if len(matches) != 1:
            reasons.append(f"{case}: expected exactly one result")
            continue
        result = matches[0]
        if result.get("status") in ("pass", "fail"):
            completed += 1
        if result.get("status") == "pass" and isinstance(result.get("trace"), str) and result["trace"].strip():
            passed += 1
        else:
            reasons.append(f"{case}: passing assertion and trace required")
    return {"eligible": not reasons, "passed": passed,
            "planned": len(REQUIRED_CASES), "coverage": completed / len(REQUIRED_CASES),
            "reasons": reasons}


def outcome_cost(credits, attempts, accepted):
    """Credits per accepted outcome are not a currency price or net ROI."""
    if any(type(n) is not int or n < 0 for n in (credits, attempts, accepted)):
        raise ValueError("use nonnegative integer counts")
    if attempts == 0 or accepted > attempts:
        raise ValueError("attempts must be positive and cover accepted outcomes")
    return {"acceptance_rate": accepted / attempts,
            "credits_per_accepted": credits / accepted if accepted else None}


if __name__ == "__main__":
    evidence = json.loads(Path(__file__).with_name("starter-evidence.json").read_text(encoding="utf-8"))
    print(json.dumps({"release": assess_release("service-case-v1", evidence),
                      "pilot_b": outcome_cost(7200, 600, 240)}, indent=2))
