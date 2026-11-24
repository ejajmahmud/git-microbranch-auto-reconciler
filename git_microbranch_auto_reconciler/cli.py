"""CLI for Microbranch Reconciler."""
import argparse
from .core import MicrobranchReconciler

def main():
    parser = argparse.ArgumentParser(description="Git Microbranch Auto-Reconciler CLI")
    parser.add_argument("--demo", action="store_true", help="Run reconciler demo")
    args = parser.parse_args()

    rec = MicrobranchReconciler()
    rec.create_branch("feature-login", {"login.py"})
    res = rec.reconcile_and_merge("feature-login")
    print(f"Reconcile success: {res['success']} | New Head: {res.get('new_head')}")

if __name__ == "__main__":
    main()
