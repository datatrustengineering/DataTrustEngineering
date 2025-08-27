#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gate promotion based on thresholds in gates.yml against evidence index.json."""
import json, sys, yaml
from pathlib import Path

def main(index_path: str, gates_path: str):
    idx = json.loads(Path(index_path).read_text())
    gates = yaml.safe_load(Path(gates_path).read_text())["gates"]

    failures = []

    # Example checks: you can extend with fairness gaps, etc.
    # Drift PSI not present in the simple baseline index; this is a placeholder for extension.
    # For demo, we only check that drift report and shap files exist:
    if not Path(idx.get("drift_report_html","")).exists():
        failures.append("Missing drift_report_html artifact")
    if not Path(idx.get("shap_values","")).exists():
        failures.append("Missing shap_values artifact")

    if failures:
        print("GATES FAILED:")
        for f in failures:
            print(" -", f)
        sys.exit(2)
    else:
        print("GATES PASSED")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: check_gates.py <evidence_index.json> <gates.yml>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])