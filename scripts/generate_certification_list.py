#!/usr/bin/env python3
"""Generate certification query seeds from config/certification-seeds.json."""

from __future__ import annotations

import json
import sys

from validate_repository import CERTIFICATION_LIST_PATH, ROOT, render_certification_list


def main() -> int:
    catalog_path = ROOT / "config/certification-seeds.json"
    try:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to read {catalog_path}: {exc}", file=sys.stderr)
        return 1

    certifications = (
        catalog.get("certifications") if isinstance(catalog, dict) else None
    )
    if not isinstance(certifications, list) or not certifications:
        print(
            "config/certification-seeds.json must contain a non-empty "
            "certifications array",
            file=sys.stderr,
        )
        return 1

    CERTIFICATION_LIST_PATH.write_text(
        render_certification_list(certifications), encoding="utf-8"
    )
    print(
        f"Wrote {len(certifications)} certifications to "
        f"{CERTIFICATION_LIST_PATH.relative_to(ROOT)}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
