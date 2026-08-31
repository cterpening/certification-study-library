from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_repository  # noqa: E402


class SourceCandidateValidationTests(unittest.TestCase):
    def candidate(self, **changes: object) -> dict[str, object]:
        value: dict[str, object] = {
            "id": "example-course",
            "title": "Example course",
            "url": "https://example.com/course",
            "added_on": "2026-08-31",
            "suggested_exams": ["AB-100"],
            "reason": "Potential architecture coverage.",
            "review_status": "queued",
        }
        value.update(changes)
        return value

    def validate(self, candidates: list[dict[str, object]]) -> list[str]:
        errors: list[str] = []
        validate_repository.validate_source_candidates(
            candidates,
            {"approved-source"},
            {"https://example.com/approved"},
            {"AB-100"},
            errors,
        )
        return errors

    def test_accepts_a_queued_candidate(self) -> None:
        self.assertEqual(self.validate([self.candidate()]), [])

    def test_rejects_unknown_exam_and_approved_url(self) -> None:
        errors = self.validate(
            [
                self.candidate(
                    url="https://example.com/approved",
                    suggested_exams=["UNKNOWN-100"],
                )
            ]
        )
        self.assertTrue(any("already approved" in error for error in errors))
        self.assertTrue(any("unknown exams" in error for error in errors))

    def test_rejected_candidate_needs_review_evidence(self) -> None:
        errors = self.validate([self.candidate(review_status="rejected")])
        self.assertTrue(any("needs reviewed_on" in error for error in errors))
        self.assertTrue(any("needs review_notes" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
