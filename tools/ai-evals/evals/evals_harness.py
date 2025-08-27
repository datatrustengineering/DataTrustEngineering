#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run core AI evals and emit an evidence pack (baseline).
Includes: fairness (selection rate), drift (Evidently), SHAP summary.
"""
import json, pathlib, numpy as np, pandas as pd

from fairlearn.metrics import MetricFrame, selection_rate
from evidently.report import Report
from evidently.metrics import DataDriftPreset
import shap
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

EVIDENCE_DIR = pathlib.Path("artifacts/evidence")
EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

def main():
    # Data / model
    X, y = make_classification(n_samples=1500, n_features=6, random_state=42)
    X = pd.DataFrame(X, columns=[f"f{i}" for i in range(X.shape[1])])
    X["gender"] = np.random.choice(["F","M"], size=len(X))
    X_train, X_test, y_train, y_test = train_test_split(X.drop(columns=["gender"]), y, test_size=0.3, random_state=42)
    model = RandomForestClassifier().fit(X_train, y_train)
    pred = model.predict(X_test)

    # 1) Fairness
    mf = MetricFrame(metrics=selection_rate, y_true=y_test, y_pred=pred, sensitive_features=X.loc[y_test.index, "gender"])
    fair = {"selection_rate_by_group": mf.by_group.to_dict(), "overall": mf.overall}

    # 2) Drift
    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=X_train, current_data=X_test)
    drift_html = EVIDENCE_DIR / "drift_report.html"
    report.save_html(str(drift_html))

    # 3) SHAP
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test.sample(100, random_state=42).values)
    shap_path = EVIDENCE_DIR / "shap_values.npy"
    np.save(shap_path, shap_values, allow_pickle=True)

    # Index
    index = {
        "fairness": fair,
        "drift_report_html": str(drift_html),
        "shap_values": str(shap_path)
    }
    (EVIDENCE_DIR / "index.json").write_text(json.dumps(index, indent=2))
    print("Evidence pack written:", str(EVIDENCE_DIR))

if __name__ == "__main__":
    main()