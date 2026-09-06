import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import objective_adapter_registry as registry  # noqa: E402


class ObjectiveAdapterRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.vendors = json.loads(
            (ROOT / "data/vendors.json").read_text(encoding="utf-8")
        )["vendors"]

    def test_vendor_assignments_and_documentation_match_registry(self) -> None:
        readme = (ROOT / "adapters/README.md").read_text(encoding="utf-8")
        self.assertEqual([], registry.inventory_errors(self.vendors, readme))

    def test_implementation_contract_rejects_missing_and_extra_adapters(self) -> None:
        implementations = {name: object() for name in registry.OBJECTIVE_ADAPTER_NAMES}
        self.assertEqual(implementations, registry.checked_implementations(implementations))

        implementations.pop(next(iter(implementations)))
        implementations["unregistered"] = object()
        with self.assertRaisesRegex(RuntimeError, "missing implementations"):
            registry.checked_implementations(implementations)
