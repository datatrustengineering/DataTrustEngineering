---
title: AI Evaluations Guide
type: "page"
layout: "single"
markup: "markdown"
---

# AI Evaluations (DTE Pattern)

## Mission

In DTE, **AI evaluations are evidence, not theater**. Small, automated checks generate transparent artifacts (JSON/HTML) covering fairness, drift, robustness, and correctness. These are **non‑regulatory, risk‑tiered** signals that support certification **by use case, risk, and value**.

This guide is a **baseline**: practical, open‑source recipes you can fork and extend. It aligns with the Manifesto’s focus on **engineering rigor, observability, and AI‑readiness**.

---

## Quick Start: Evals Harness

Create a lightweight script that runs core evals and emits an **evidence pack**.

```python
# evals_harness.py
import json, pathlib, numpy as np, pandas as pd

# Fairness (Fairlearn), Drift/Perf (Evidently), Explainability (SHAP)
from fairlearn.metrics import MetricFrame, selection_rate
from evidently.report import Report
from evidently.metrics import DataDriftPreset
import shap
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

EVIDENCE_DIR = pathlib.Path("artifacts/evidence"); EVIDENCE_DIR.mkdir(parents=True, exist_ok=True)

# Toy data / model
X, y = make_classification(n_samples=2000, n_features=6, random_state=42)
X = pd.DataFrame(X, columns=[f"f{i}" for i in range(X.shape[1])])
X["gender"] = np.random.choice(["F","M"], size=len(X))
X_train, X_test, y_train, y_test = train_test_split(X.drop(columns=["gender"]), y, test_size=0.3, random_state=42)
model = RandomForestClassifier().fit(X_train, y_train)
pred = model.predict(X_test)

# 1) Fairness (selection rate by group)
mf = MetricFrame(metrics=selection_rate, y_true=y_test, y_pred=pred, sensitive_features=X.loc[y_test.index, "gender"])
fair = {"selection_rate_by_group": mf.by_group.to_dict(), "overall": mf.overall}

# 2) Drift (Evidently) — baseline vs. current (toy example uses same data twice)
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=X_train, current_data=X_test)
report.save_html(str(EVIDENCE_DIR / "drift_report.html"))

# 3) Explainability (SHAP) — summary values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test.sample(100, random_state=42).values)
import numpy as np
np.save(EVIDENCE_DIR / "shap_values.npy", shap_values, allow_pickle=True)

# Evidence index
index = {
  "fairness": fair,
  "drift_report_html": "artifacts/evidence/drift_report.html",
  "shap_values": "artifacts/evidence/shap_values.npy"
}
json.dump(index, open(EVIDENCE_DIR / "index.json", "w"), indent=2)
print("AI evals evidence pack written to artifacts/evidence/")
```

**Run**
```bash
python evals_harness.py
```

---

## Design Patterns for AI Evals

### 1) Risk‑Tiered Evals
- Scope evals by **use case risk** (e.g., customer eligibility > marketing ranker).  
- Increase coverage (fairness/robustness) for high‑stakes tiers.  

### 2) Evaluation as Code
- Evals live in repo; run in CI on model/data changes.  
- Emit versioned **evidence packs** linked from PRs.  

### 3) Grounded Outputs for RAG/Agents
- Use **retrieval coverage** and **source attribution** checks.  
- Log **hallucination rate** via curated Q&A sets.  

### 4) Degradation Budgets
- Set SLOs for eval metrics (e.g., “fairness delta ≤ 5% overall”).  
- If budget is burned, block promotion until remediated.  

### 5) Explainability for Humans
- Produce **small, interpretable** artifacts (SHAP plots, top features).  
- Attach to dashboards alongside performance and freshness.  

---

## Minimal Metrics

- **Fairness**: selection rate, TPR/PPV by group; worst‑group delta.  
- **Drift**: feature drift score (PSI/JS), target drift detection.  
- **Correctness (RAG)**: answer accuracy vs. gold set; citation coverage.  
- **Robustness**: sensitivity to small input changes; guardrail violation rate.  

---

## Open‑Source Toolkit

- **Fairlearn**, **Evidently**, **SHAP**, **MLflow** (tracking), **LangChain evals** (for LLM/RAG).

> Evals create **confidence** through transparent evidence — not promises. 

## Advanced Extensions

See `/evals/` for advanced examples:  
- Risk-tiered profiles (`eval_profiles.yml`)  
- Evidence pack schema (JSON)  
- RAG/GraphRAG evals (`rag_eval.py`)  
- Adversarial probes (`adversarial.py`)  
- CI wiring (`.github/workflows/evals.yml`)  
- PR checklist + model card templates  

