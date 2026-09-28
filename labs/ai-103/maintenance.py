"""Synthetic retrieval and work-order contracts, with no Azure/network calls."""

from dataclasses import dataclass
import json
from pathlib import Path


def retrieval_metrics(retrieved, relevant, authorized):
    """Measure unique documents and expose access breaches before filtering."""
    retrieved, relevant, authorized = map(set, (retrieved, relevant, authorized))
    if not relevant <= authorized:
        raise ValueError("ground truth must contain only authorized relevant IDs")
    hits = len(retrieved & relevant)
    breaches = sorted(retrieved - authorized)
    return {"precision": hits / len(retrieved) if retrieved else 0.0,
            "recall": hits / len(relevant) if relevant else None,
            "unauthorized_ids": breaches,
            "eligible_context": sorted(retrieved & relevant) if not breaches else [],
            "abstain": bool(breaches) or hits == 0}


@dataclass(frozen=True)
class Proposal:
    operation_id: str
    asset: str
    description: str


class WorkOrders:
    """Single-process teaching model: approvals and idempotency are in memory.

    Callers are trusted test identities, not authenticated credentials. Production
    storage must enforce authorization and atomic, durable uniqueness itself.
    """

    def __init__(self):
        self.permissions = {"technician": {"P-104"}}
        self.approvers = {"supervisor"}
        self.approvals = set()
        self.records = {}

    def approve(self, proposal, reviewer):
        if reviewer not in self.approvers:
            raise PermissionError("reviewer cannot approve")
        self.approvals.add(proposal)

    def submit(self, proposal, caller, expected_asset, lose_response=False):
        if proposal.asset != expected_asset:
            raise ValueError("proposed asset differs from requested asset")
        if proposal.asset not in self.permissions.get(caller, set()):
            raise PermissionError("caller cannot access asset")
        if any(not isinstance(v, str) or not v.strip() for v in
               (proposal.operation_id, proposal.asset, proposal.description)):
            raise ValueError("proposal fields must be nonempty strings")
        if proposal not in self.approvals:
            raise PermissionError("exact proposal is not approved")
        existing = self.records.get(proposal.operation_id)
        if existing is not None and existing != proposal:
            raise ValueError("operation ID already belongs to different content")
        self.records[proposal.operation_id] = proposal
        if lose_response:
            raise TimeoutError("response lost; reconcile before retrying")
        return {"status": "created" if existing is None else "existing",
                "operation_id": proposal.operation_id, "asset": proposal.asset}

    def status(self, operation_id):
        # The teaching harness's authoritative observation, not a public API.
        return self.records.get(operation_id)


if __name__ == "__main__":
    cases = json.loads(Path(__file__).with_name("retrieval-cases.json").read_text(encoding="utf-8"))
    print(json.dumps({case["name"]: retrieval_metrics(case["retrieved"], case["relevant"], case["authorized"])
                      for case in cases}, indent=2))
    orders = WorkOrders()
    proposal = Proposal("synthetic-operation-01", "P-104", "Inspect the noisy pump; do not close an existing order.")
    orders.approve(proposal, "supervisor")
    try:
        orders.submit(proposal, "technician", "P-104", lose_response=True)
    except TimeoutError:
        print("Timeout: outcome unknown to caller until status lookup.")
    print("Reconciled:", orders.status(proposal.operation_id))
    print("Replay:", orders.submit(proposal, "technician", "P-104"))
    print("Destination records:", len(orders.records))
