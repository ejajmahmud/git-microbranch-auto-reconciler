"""Tests for MicrobranchReconciler."""
import unittest
from git_microbranch_auto_reconciler.core import MicrobranchReconciler

class TestMicrobranchReconciler(unittest.TestCase):
    def test_branch_reconciliation(self):
        rec = MicrobranchReconciler()
        rec.create_branch("b1", {"auth.py"})
        res = rec.reconcile_and_merge("b1")
        self.assertTrue(res["success"])
        self.assertIn("b1", rec.main_head)
