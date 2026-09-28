"""Expected values are taken from the written contract, not candidate output."""

import argparse
import importlib
import unittest

from reference import shipping_cents


class ShippingContract(unittest.TestCase):
    target = staticmethod(shipping_cents)

    def test_zero(self):
        self.assertEqual(self.target(0), 499)

    def test_below(self):
        self.assertEqual(self.target(4999), 499)

    def test_threshold(self):
        self.assertEqual(self.target(5000), 0)

    def test_above(self):
        self.assertEqual(self.target(5001), 0)

    def test_large(self):
        self.assertEqual(self.target(10**30), 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            self.target(-1)

    def test_non_integer(self):
        for invalid in (True, False, 50.0, "5000", None, [], {}):
            with self.subTest(value=invalid), self.assertRaises(ValueError):
                self.target(invalid)


def run_contract(module_name, stream):
    candidate = importlib.import_module(module_name)
    case = type("CandidateContract", (ShippingContract,),
                {"target": staticmethod(candidate.shipping_cents)})
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(case)
    return unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)


if __name__ == "__main__":
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument("--implementation", choices=("starter", "reference", "boolean_mutant"), default="reference")
    args = parser.parse_args()
    result = run_contract(args.implementation, sys.stderr)
    raise SystemExit(0 if result.wasSuccessful() else 1)
