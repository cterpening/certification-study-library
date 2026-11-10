#!/usr/bin/env python3
"""Rebuild or check the authored DP-900 comparison; local inputs only."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from visual_exercise import Exercise, document, paragraph, path, rect, text  # noqa: E402

PACKAGE = "examples/study-packs/dp-900-data-decisions"
UNITS = {"relational-management": "e507e0e26816ca2acd4009f4e537a9538d8638e86a399c7744edeed6db05ac22"}
NAVY = "#102b40"
INK = "#183348"
TEAL = "#0e6654"
TEAL_PALE = "#e3f3ed"
AMBER = "#704711"
AMBER_PALE = "#fff1d5"
SERVICES = (
    {
        "icon": "azure-sql-database",
        "name": "Azure SQL Database",
        "titles": (("Azure SQL", 323), ("Database", 351)),
        "scope": "PaaS · database scope",
        "cue": "Database-oriented app",
        "caution": "Check required SQL features.",
    },
    {
        "icon": "azure-sql-managed-instance",
        "name": "Azure SQL Managed Instance",
        "titles": (("Azure SQL", 323), ("Managed Instance", 351)),
        "scope": "PaaS · instance scope",
        "cue": "Instance-level dependencies",
        "caution": "Check exact compatibility.",
    },
    {
        "icon": "sql-server-on-azure-vm",
        "name": "SQL Server on Azure Virtual Machines",
        "titles": (("SQL Server on", 312), ("Azure Virtual", 338), ("Machines", 364)),
        "scope": "IaaS · OS + SQL control",
        "cue": "Guest OS + installation control",
        "caution": "Own admin; automation can help.",
    },
)
REQUIREMENTS = (
    {
        "label": "A  /  NEW APPLICATION",
        "given": "A compatible cloud app needs one database,\nwith no instance-level or guest OS dependency.",
        "candidate": "Evaluate Azure SQL Database",
        "tradeoff": "Managed platform; the app must fit its features.",
    },
    {
        "label": "B  /  EXISTING SQL WORKLOAD",
        "given": "A migration needs instance-level SQL features\nand managed OS upkeep. No OS agent needed.",
        "candidate": "Evaluate Azure SQL Managed Instance",
        "tradeoff": "Broader instance scope; verify each dependency.",
    },
    {
        "label": "C  /  VENDOR REQUIREMENT",
        "given": "The vendor requires a guest OS agent and\ncontrol over the SQL Server installation.",
        "candidate": "Evaluate SQL Server on Azure VMs",
        "tradeoff": "OS + SQL control brings more administration.",
    },
)


def layer(x: int, y: int, label: str, owner: str) -> list[str]:
    customer = owner == "CUSTOMER"
    return [
        rect(x, y, 312, 62, AMBER_PALE if customer else TEAL_PALE, radius=9),
        text(x + 14, y + 20, owner, 11, AMBER if customer else TEAL, 700),
        text(x + 14, y + 47, label, 19, INK, 700),
    ]


def comparison(exercise: Exercise) -> list[str]:
    body = []
    for index, service in enumerate(SERVICES):
        x = 56 + index * 368
        vm = index == 2
        body += [
            rect(x, 276, 352, 540, "#ffffff", "#b6c6cf", radius=16),
            exercise.icon(service["icon"], x + 20, 305, size=58),
            *[text(x + 94, y, value, 24, INK, 700) for value, y in service["titles"]],
            text(x + 20, 396, service["scope"], 16, "#496175"),
        ]
        body += layer(x + 20, 424, "App · data · access", "CUSTOMER")
        body += layer(x + 20, 505, "SQL installation + engine" if vm else "SQL engine platform", "CUSTOMER" if vm else "MICROSOFT")
        body += layer(x + 20, 576, "Guest OS + added agents" if vm else "Guest operating system", "CUSTOMER" if vm else "MICROSOFT")
        body += layer(x + 20, 658, "Azure infrastructure", "MICROSOFT")
        boundary_y = 647 if vm else 495
        body += [
            path(f"M{x + 11} {boundary_y} H{x + 341}", NAVY, 2, dash="5 4"),
            text(x + 20, 758, service["cue"], 18, INK, 700),
            text(x + 20, 790, service["caution"], 16, "#496175"),
        ]
    return body


def description(mode: str) -> str:
    labels = []
    for index, service in enumerate(SERVICES):
        vm = index == 2
        labels.append(
            f"{service['name']}. {service['scope']}. "
            "Customer: application, data and access decisions. "
            + ("Customer: SQL installation and engine; guest OS and added agents. " if vm else
               "Microsoft: SQL engine platform and guest operating system. No customer guest OS access. ")
            + f"Microsoft: Azure infrastructure. {service['cue']}. {service['caution']} "
        )
    tasks = []
    for requirement in REQUIREMENTS:
        entry = requirement["label"] + ". " + requirement["given"].replace("\n", " ")
        if mode == "study":
            entry += " " + requirement["candidate"] + ". " + requirement["tradeoff"]
        else:
            entry += " Choose a candidate, explain one tradeoff and identify a check before deployment."
        tasks.append(entry)
    return " ".join([
        "DP-900. " + mode.title() + " version. Who runs which SQL layer?",
        "Three equal columns compare responsibility, not a universal product ranking.",
        "Read each stack downward: app/data/access, SQL platform, guest OS, Azure infrastructure.",
        "The app/data/access layer represents decisions, not application hosting inside the SQL service.",
        "The dashed line marks the shift to Microsoft-managed platform layers: after the first row for the two PaaS services, after the guest OS for the VM.",
        *labels,
        "In every option the customer owns recovery requirements. Managed backups do not choose business recovery needs.",
        "VM automation can help with patching, backup and availability.",
        "Three original, invented requirements follow.", *tasks,
        "These are candidates to evaluate. VERIFY CURRENT: exact feature compatibility, vendor support and recovery configuration.",
        "Independent AI-assisted draft; human review pending. Selected objective only; accepted baseline July 21, 2026.",
        "The official DP-900 study guide is authoritative. Sources: Microsoft Learn Azure SQL comparison and DP-900 study guide.",
        "See the README for exact links and a separate answer section. No live Azure execution or vendor validation is claimed.",
    ])


def svg(exercise: Exercise, mode: str) -> str:
    study = mode == "study"
    body = [
        rect(0, 0, 1200, 174, NAVY, radius=0),
        rect(56, 34, 5, 22, "#70e0be", radius=0),
        text(74, 51, "DP-900  /  SQL DECISIONS", 16, "#bceedd", 700),
        text(56, 107, "Who runs which SQL layer?", 43, "#ffffff", 700),
        text(56, 146, "Match the management boundary to the workload.", 21, "#d7e6ef"),
        rect(943, 28, 201, 34, "#23485e", radius=17),
        text(1043, 51, mode.upper() + " VERSION", 15, "#ffffff", 700, "middle"),
        text(56, 218, "Start with the control you need", 28, INK, 700),
        rect(56, 237, 14, 14, AMBER_PALE, "#9c6a24", radius=3),
        text(80, 250, "Customer decisions / administration", 16, INK),
        rect(406, 237, 14, 14, TEAL_PALE, TEAL, radius=3),
        text(430, 250, "Microsoft platform management", 16, INK),
        path("M774 244 H820", NAVY, 2, dash="5 4"),
        text(830, 250, "Management boundary", 16, INK),
        *comparison(exercise),
        rect(56, 836, 1088, 64, "#e6edf2", radius=12),
        text(76, 862, "IN EVERY OPTION", 13, NAVY, 700),
        text(245, 862, "Own recovery requirements as well as app, data and access decisions.", 19, INK, 700),
        text(245, 886, "Managed backups do not choose your business recovery needs.", 17, "#496175"),
        text(56, 941, "Three requirements. Three reasoned starting points." if study else "Choose a candidate. Explain one tradeoff.", 26, INK, 700),
    ]
    for index, requirement in enumerate(REQUIREMENTS):
        y = 960 + index * 96
        body += [
            rect(56, y, 1088, 84, "#ffffff", "#c3d0d8", radius=12),
            text(76, y + 21, requirement["label"], 12, TEAL, 700),
            paragraph(76, y + 45, requirement["given"], width=58, size=17, line_height=23),
            path(f"M642 {y + 15} V{y + 69}", "#d1dce3", 1),
        ]
        if study:
            body += [
                text(664, y + 31, requirement["candidate"], 19, TEAL, 700),
                text(664, y + 59, requirement["tradeoff"], 16, "#496175"),
            ]
        else:
            body += [
                text(664, y + 25, "Candidate + tradeoff + check before deployment", 15, "#496175"),
                path(f"M664 {y + 47} H1122 M664 {y + 70} H1122", "#93a8b6", 1),
            ]
    body += [
        text(56, 1264, "Invented requirements · Candidates, not a universal ranking · Check the vendor's actual support policy.", 15, "#496175"),
        rect(0, 1283, 1200, 117, NAVY, radius=0),
        text(56, 1310, "VERIFY CURRENT: exact feature compatibility, vendor support and recovery configuration.", 16, "#f8dca8", 700),
        text(56, 1336, "Independent AI-assisted draft · Human review pending · Selected objective · Accepted baseline: July 21, 2026", 14, "#d7e6ef"),
        text(56, 1361, "Sources: Microsoft Learn — Azure SQL comparison; official DP-900 study guide (authoritative exam scope).", 14, "#d7e6ef"),
        text(56, 1384, "Exact source links and accessible exercise: README. No live Azure execution or vendor compatibility validation.", 14, "#d7e6ef"),
    ]
    return document("DP-900 SQL management choices — " + mode + " exercise", description(mode), body, height=1400)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare bound inputs and regenerated outputs without writing")
    args = parser.parse_args()
    try:
        exercise = Exercise(HERE, PACKAGE, UNITS, icons=tuple(service["icon"] for service in SERVICES))
        exercise.save(svg(exercise, "study"), svg(exercise, "practice"), check=args.check)
    except (OSError, ValueError, KeyError, StopIteration) as exc:
        print(f"Visual exercise error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
