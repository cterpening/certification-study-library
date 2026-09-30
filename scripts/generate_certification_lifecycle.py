#!/usr/bin/env python3
"""Generate the lifecycle page from dated, source-backed inventory fields."""
import json
from pathlib import Path
import sys

from certification_lifecycle import render_lifecycle_page

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    try:
        catalog = json.loads((ROOT / "config/certification-seeds.json").read_text(
            encoding="utf-8"))
        result = render_lifecycle_page(catalog)
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"Unable to generate lifecycle page: {exc}", file=sys.stderr)
        return 1
    (ROOT / "docs/CERTIFICATION-LIFECYCLE.md").write_text(result, encoding="utf-8")
    print("Wrote docs/CERTIFICATION-LIFECYCLE.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
