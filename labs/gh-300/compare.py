"""Verify that the independent oracle detects each intentional mutation."""

import io
import json

from test_contract import run_contract


expected = {"reference": [], "starter": ["test_threshold"],
            "boolean_mutant": ["test_non_integer", "test_non_integer"]}
report = {}
for module, expected_failures in expected.items():
    output = io.StringIO()
    result = run_contract(module, output)
    failures = sorted(test.id().split(".")[-1].split(" ")[0] for test, _ in result.failures)
    if result.errors or result.testsRun != 7 or failures != expected_failures:
        print(output.getvalue())
        raise SystemExit(f"Unexpected contract result for {module}")
    report[module] = {"tests_run": result.testsRun, "failed_assertions": failures,
                      "errors": len(result.errors), "matches_expected": True,
                      "output": output.getvalue()}
print(json.dumps(report, indent=2))
