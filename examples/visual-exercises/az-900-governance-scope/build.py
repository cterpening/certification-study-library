#!/usr/bin/env python3
"""Build or check an authored Azure scope exercise without network or AI calls."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from visual_exercise import Exercise, document, path, rect, text  # noqa: E402

PACKAGE = "examples/study-packs/az-900-governance"
UNIT = "permissions-and-policy"
UNIT_SHA256 = "b582037da541e60d1f129e28eaf634a9cd3962a227f98dbcfb2e334847b3f68f"
ICONS = ("azure-resource-group", "azure-policy", "azure-virtual-machine")
NAVY = "#102b40"
TEAL = "#0e6654"
AMBER = "#85500a"


def lines(x, y, rows, size=24, color="#334e63", step=34, weight=400):
    return "\n".join(text(x, y + index * step, row, size, color, weight)
                     for index, row in enumerate(rows))


def diagram(exercise, mode):
    study = mode == "study"
    description = (
        f"AZ-900 {mode} version. Why is this VM request blocked? Original invented scenario. "
        "The identity app-deploy has permission to create the requested virtual machine at "
        "resource group rg-research. The map places that resource group inside subscription "
        "learning-sub. A role assignment associates principal app-deploy, a role permitting "
        "VM creation, and scope rg-research. A separate Azure Policy assignment at subscription "
        "scope applies to this request: its allowed location is East US and its effect is deny. "
        "No exclusion or exemption applies in this scenario. An arrow from app-deploy points "
        "to a proposed Azure Virtual Machine create request inside the target resource group: "
        "vm-study, location West US. The dashed request box represents requested configuration, "
        "not a deployed resource. Lines connect assignments to their applicable scope; they "
        "do not represent an order of Azure checks. "
    )
    if study:
        description += (
            "Explanation: permission is granted, but West US does not meet the East US requirement. "
            "The applicable deny blocks this request. Inspect the error and applicable Policy "
            "assignment, then use an approved location or seek an approved exception. "
            "Broader RBAC permission does not resolve this stated Policy denial. "
        )
    else:
        description += (
            "Practice: which given explains the block? Justify your answer using the requested "
            "location and the applicable assignment. What evidence would you inspect next? "
            "Would a broader role resolve the stated issue? Explain and propose a next step. "
        )
    description += (
        "Simplified scope map; other checks can affect real requests. VERIFY CURRENT: actual "
        "assignments, effects, exclusions and exemptions. Selected objectives only. "
        "Independent AI-assisted draft; human review pending. Accepted baseline July 20, 2026. "
        "The official AZ-900 blueprint is authoritative. Original Microsoft icons embedded "
        "unchanged; Microsoft terms apply. Exact sources and the text exercise are in README."
    )
    out = [
        rect(0, 0, 1200, 166, NAVY, radius=0),
        rect(64, 33, 5, 22, "#70e0be", radius=0),
        text(82, 51, "AZ-900  /  SCOPE DETECTIVE", 16, "#bceedd", 700),
        rect(936, 27, 200, 35, "#23485e", radius=18),
        text(1036, 51, mode.upper() + " VERSION", 15, "#ffffff", 700, "middle"),
        text(64, 108, "Why is this VM request blocked?", 43, "#ffffff", 700),
        text(64, 145, "Read the scope map. Separate permission from requirements.", 24, "#d7e6ef"),
        rect(64, 190, 1072, 90, "#fff1d5", "#bd8432", 14),
        text(86, 218, "INVENTED CASE  /  GIVEN", 15, "#68430e", 700),
        text(86, 255, "app-deploy has VM-create permission at rg-research.", 27, "#513612", 700),

        # A subscription boundary and a nested resource-group boundary show scope.
        rect(310, 310, 826, 610, "#edf3f6", "#7794a8", 18, 2),
        text(335, 347, "Subscription · learning-sub", 26, NAVY, 700),
        rect(340, 650, 766, 244, "#f0faf6", TEAL, 14, 3),
        exercise.icon("azure-resource-group", 363, 667, 48),
        text(426, 701, "Resource group · rg-research", 26, TEAL, 700),

        # Original person geometry, deliberately separate from service artwork.
        rect(64, 371, 220, 160, "#ffffff", "#a6bac7", 14),
        text(84, 401, "REQUESTER", 16, NAVY, 700),
        '<circle cx="106" cy="439" r="14" fill="#23485e"/>',
        path("M82 483 Q82 460 106 460 Q130 460 130 483 Z", NAVY, 1, fill="#23485e"),
        text(143, 455, "app-deploy", 23, NAVY, 700),
        text(84, 511, "Identity / principal", 22),

        # Role association is not a request-processing step.
        path("M284 448 H340", "#7794a8", 2),
        '<circle cx="310" cy="448" r="5" fill="#7794a8"/>',
        rect(340, 371, 340, 207, "#ffffff", "#a6bac7", 14),
        text(364, 400, "ROLE ASSIGNMENT", 16, TEAL, 700),
        text(364, 438, "Azure RBAC", 29, NAVY, 700),
        lines(364, 479, ["Principal: app-deploy", "Role: permits VM create", "Scope: rg-research"], 24, step=34),
        path("M510 578 V650", TEAL, 3),
        rect(418, 598, 184, 32, "#edf3f6", radius=0),
        text(510, 621, "Role scope", 23, TEAL, 700, "middle"),

        # Independent Policy assignment applies from subscription scope.
        rect(718, 371, 388, 207, "#ffffff", "#bd8432", 14),
        text(742, 400, "POLICY ASSIGNMENT", 16, AMBER, 700),
        text(742, 438, "Azure Policy", 29, NAVY, 700),
        exercise.icon("azure-policy", 1025, 393, 55),
        lines(742, 479, ["Scope: subscription", "Allowed: East US", "Effect: deny"], 24, step=34),
        path("M913 578 V650", AMBER, 3, dash="7 5"),
        rect(809, 598, 208, 32, "#edf3f6", radius=0),
        text(913, 621, "Applicable here", 23, AMBER, 700, "middle"),

        # Dashed boundary means a proposed request, never a deployed VM.
        rect(371, 733, 705, 136, "#ffffff", "#7794a8", 12, 2, dash="8 6"),
        exercise.icon("azure-virtual-machine", 395, 768, 64),
        text(480, 774, "Azure Virtual Machine", 28, NAVY, 700),
        text(480, 812, "vm-study · requested location: West US", 24, NAVY),
        text(480, 847, "Proposed create request", 24, "#526d80"),
        path("M174 531 V803 H371", "#668093", 3, arrow=True),
        rect(82, 655, 184, 67, "#f3f6f7", radius=0),
        lines(174, 682, ["Create", "request"], 24, NAVY, step=30).replace('text-anchor="start"', 'text-anchor="middle"'),
        text(64, 954, "Scope associations shown; this is not an order of Azure checks.", 22, "#526d80"),
    ]

    if study:
        out += [
            rect(64, 981, 524, 237, "#ffffff", "#b6c6cf", 14),
            text(88, 1016, "READ THE EVIDENCE", 18, TEAL, 700),
            text(88, 1057, "Permission is granted.", 28, NAVY, 700),
            lines(88, 1098, ["West US does not meet", "the East US requirement.", "The deny blocks this request."], 26),
            rect(612, 981, 524, 237, "#ffffff", "#b6c6cf", 14),
            text(636, 1016, "CHECK + CORRECT", 18, TEAL, 700),
            lines(636, 1057, ["Inspect the error and applicable", "Policy assignment.", "Use East US, or seek an", "approved exception."], 26, step=36),
            text(64, 1254, "Broader RBAC permission does not resolve this stated Policy denial.", 24, NAVY, 700),
        ]
    else:
        out += [
            rect(64, 981, 524, 237, "#ffffff", "#b6c6cf", 14),
            text(88, 1016, "JUSTIFY THE CAUSE", 18, TEAL, 700),
            lines(88, 1057, ["Which given explains the block?", "Use the location and assignment", "to support your reasoning."], 26, step=36),
            path("M88 1163 H564 M88 1193 H564", "#a6bac7", 1),
            rect(612, 981, 524, 237, "#ffffff", "#b6c6cf", 14),
            text(636, 1016, "CHOOSE THE NEXT CHECK", 18, TEAL, 700),
            lines(636, 1057, ["What evidence would you inspect?", "Would a broader role resolve it?", "Explain and propose a next step."], 26, step=36),
            path("M636 1163 H1112 M636 1193 H1112", "#a6bac7", 1),
            text(64, 1254, "Explain your reasoning before opening the study version.", 24, NAVY, 700),
        ]
    out += [
        path("M64 1280 H1136", "#b6c6cf", 1),
        text(64, 1305, "Simplified scope map · Other checks can affect real requests. VERIFY CURRENT: assignments, effects and exceptions.", 18),
        text(64, 1334, "Independent AI-assisted draft · Human review pending · Selected objectives · Baseline: July 20, 2026", 17),
        text(64, 1360, "Microsoft Learn sources and text exercise: README. Official AZ-900 blueprint is authoritative. No Azure execution.", 17),
        text(64, 1386, "Original Microsoft icons embedded unchanged · Microsoft terms apply; see README and third-party notices.", 17),
    ]
    return document(f"AZ-900 governance scope — {mode} exercise", description, out, height=1400)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify current inputs and outputs without writing")
    args = parser.parse_args()
    try:
        exercise = Exercise(HERE, PACKAGE, {UNIT: UNIT_SHA256}, icons=ICONS)
        exercise.save(diagram(exercise, "study"), diagram(exercise, "practice"), check=args.check)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Visual exercise error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
