#!/usr/bin/env python3
"""Canonical objective-adapter inventory and cross-surface contract checks."""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping, Sequence
from typing import TypeVar


ADAPTER_DESCRIPTIONS = {
    "aws-exam-guide": "AWS exam identity, capability summary, weighted domains, and lifecycle signals.",
    "cisco-certification": "Cisco exam topics, domain weights, version identifiers, and lifecycle signals.",
    "comptia-certification": "CompTIA exam code, lifecycle details, and weighted objective summary.",
    "cpp-institute-certification": "C/C++ Institute syllabus sections, exam metadata, and lifecycle signals.",
    "databricks-certification": "Databricks weighted coverage map, assessment details, and lifecycle signals.",
    "fortinet-certification": "Fortinet exam topics, product-version scope, delivery details, and lifecycle signals.",
    "google-cloud-certification": "Google Cloud exam-guide sections, product scope, and lifecycle signals.",
    "hashicorp-developer": "HashiCorp exam baselines, objective lists, product versions, and lifecycle signals.",
    "ibm-certification": "IBM certification API objectives, assessment metadata, and lifecycle signals.",
    "isaca-certification": "ISACA content domains, weights, exam metadata, and lifecycle signals.",
    "isc2-certification": "ISC2 domains, weights, exam outline metadata, and lifecycle signals.",
    "js-institute-certification": "JS Institute syllabus sections, exam metadata, and lifecycle signals.",
    "linux-foundation-certification": "Linux Foundation and CNCF domains, competencies, format, versions, and lifecycle signals.",
    "microsoft-learn": "Microsoft Learn skills versions, weighted objective sections, and announced changes.",
    "microsoft-office-specialist": "Microsoft Office Specialist objective groups, exam metadata, and lifecycle signals.",
    "mongodb-certification": "MongoDB public exam contracts and objective lines exposed without authentication.",
    "nvidia-certification": "NVIDIA exam topics, weights, certification metadata, and lifecycle signals.",
    "oracle-learning-path": "Oracle learning-path objectives, exam references, product scope, and lifecycle signals.",
    "palo-alto-networks-certification": "Palo Alto Networks blueprint domains, weights, versions, and lifecycle signals.",
    "python-institute-certification": "Python Institute syllabus sections, exam metadata, and lifecycle signals.",
    "red-hat-exam": "Red Hat performance tasks, tested product versions, and lifecycle signals.",
    "salesforce-certification": "Salesforce exam-guide topics, weights, credential metadata, and lifecycle signals.",
    "servicenow-certification": "ServiceNow blueprint scope, weights, delivery details, and lifecycle signals.",
    "snowflake-certification": "Snowflake exam-guide domains, weights, exam metadata, and lifecycle signals.",
    "splunk-certification": "Splunk blueprint topics, exam metadata, product versions, and lifecycle signals.",
}
OBJECTIVE_ADAPTER_NAMES = frozenset(ADAPTER_DESCRIPTIONS)
INVENTORY_START = "<!-- BEGIN GENERATED ADAPTER INVENTORY -->"
INVENTORY_END = "<!-- END GENERATED ADAPTER INVENTORY -->"


AdapterValue = TypeVar("AdapterValue")


def checked_implementations(
    implementations: Mapping[str, AdapterValue],
) -> dict[str, AdapterValue]:
    """Return implementations only when they exactly cover the canonical registry."""
    names = set(implementations)
    missing = sorted(OBJECTIVE_ADAPTER_NAMES - names)
    extra = sorted(names - OBJECTIVE_ADAPTER_NAMES)
    if missing or extra:
        details = []
        if missing:
            details.append(f"missing implementations: {', '.join(missing)}")
        if extra:
            details.append(f"unregistered implementations: {', '.join(extra)}")
        raise RuntimeError("Objective adapter registry mismatch (" + "; ".join(details) + ")")
    return dict(implementations)


def render_inventory(vendors: Sequence[object]) -> str:
    """Render the documented adapter inventory from canonical names and vendors."""
    vendors_by_adapter: dict[str, list[str]] = defaultdict(list)
    for vendor in vendors:
        if not isinstance(vendor, dict):
            continue
        adapter = vendor.get("objective_adapter")
        name = vendor.get("name")
        if isinstance(adapter, str) and isinstance(name, str) and name:
            vendors_by_adapter[adapter].append(name)

    lines = [
        INVENTORY_START,
        "| Adapter | Vendor catalog entries | Public extraction contract |",
        "| --- | --- | --- |",
    ]
    for adapter, description in sorted(ADAPTER_DESCRIPTIONS.items()):
        vendor_names = ", ".join(sorted(vendors_by_adapter.get(adapter, []))) or "_Unassigned_"
        lines.append(f"| `{adapter}` | {vendor_names} | {description} |")
    lines.append(INVENTORY_END)
    return "\n".join(lines)


def inventory_errors(vendors: Sequence[object], readme_text: str) -> list[str]:
    """Report unsupported assignments, unused adapters, and stale documentation."""
    assigned = {
        vendor.get("objective_adapter")
        for vendor in vendors
        if isinstance(vendor, dict) and isinstance(vendor.get("objective_adapter"), str)
    }
    errors = []
    unsupported = sorted(assigned - OBJECTIVE_ADAPTER_NAMES)
    unused = sorted(OBJECTIVE_ADAPTER_NAMES - assigned)
    if unsupported:
        errors.append("Vendor catalog uses unregistered adapters: " + ", ".join(unsupported))
    if unused:
        errors.append("Objective adapter registry has no vendor assignment: " + ", ".join(unused))

    expected = render_inventory(vendors)
    start = readme_text.find(INVENTORY_START)
    end = readme_text.find(INVENTORY_END)
    if start < 0 or end < start:
        errors.append("adapters/README.md is missing its generated inventory markers")
    else:
        end += len(INVENTORY_END)
        actual = readme_text[start:end].replace("\r\n", "\n")
        if actual != expected:
            errors.append("adapters/README.md adapter inventory is stale")
    return errors
