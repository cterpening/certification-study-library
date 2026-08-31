#!/usr/bin/env python3
"""Generate certification query seeds from config/exams.json."""

from __future__ import annotations

import json
import sys

from validate_repository import CERTIFICATION_LIST_PATH, ROOT, render_certification_list


def main() -> int:
    catalog_path = ROOT / "config/exams.json"
    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to read {catalog_path}: {exc}", file=sys.stderr)
        return 1

    exams = catalog.get("exams") if isinstance(catalog, dict) else None
    if not isinstance(exams, list) or not exams:
        print("config/exams.json must contain a non-empty exams array", file=sys.stderr)
        return 1

    CERTIFICATION_LIST_PATH.write_text(
        render_certification_list(exams), encoding="utf-8"
    )
    print(
        f"Wrote {len(exams)} certifications to "
        f"{CERTIFICATION_LIST_PATH.relative_to(ROOT)}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
