---
title: Confidence Indicators Guide
type: "page"
layout: "single"
markup: "markdown"
---

# Confidence Indicators (DTE Pattern)

## Mission

Confidence indicators in Data Trust Engineering (DTE) transform raw metrics into **interpretable trust signals**. They answer the question: *“Can we rely on this dataset/model for its intended use?”*

Rather than abstract “data quality scores,” confidence indicators combine **observability, evaluation results, and metadata** into transparent measures that are easy to communicate.

---

## Quick Start: Confidence Score Generator

```python
# confidence_score.py
import pandas as pd, json
from ydata_profiling import ProfileReport
from great_expectations.dataset import PandasDataset

df = pd.read_csv("customer_orders.csv")

# Profile dataset (basic stats)
profile = ProfileReport(df, title="Customer Orders Profile")
profile.to_file("artifacts/confidence_profile.html")

# Great Expectations checks
dataset = PandasDataset(df)
checks = [
    dataset.expect_column_values_to_not_be_null("order_id"),
    dataset.expect_column_values_to_be_between("total", 0, None)
]

# Aggregate into a confidence score
passed = sum([1 for c in checks if c["success"]])
score = passed / len(checks)

confidence = {
    "dataset": "customer_orders",
    "confidence_score": score,
    "checks": [c["expectation_type"] for c in checks]
}
json.dump(confidence, open("artifacts/confidence.json", "w"), indent=2)
print("Confidence evidence written to artifacts/")
```

**Run**
```bash
python confidence_score.py
```

---

## Design Patterns for Confidence Indicators

### 1) Composite Confidence
- Combine multiple signals: **completeness, uniqueness, freshness, drift, lineage coverage**.  
- Weighted to reflect **use case risk** (e.g., AI eligibility vs. reporting).  

### 2) Confidence Badges
- Publish lightweight badges (✅ Trusted, ⚠️ Limited, ❌ Untrusted).  
- Attach to datasets, dashboards, and APIs.  

### 3) Evidence Packs
- Store JSON/HTML artifacts with metrics + metadata.  
- Link from dashboards and PRs for **traceability**.  

### 4) Rolling Windows
- Confidence recalculated over **time windows** (e.g., daily).  
- Provides **trend visibility** instead of static scores.  

---

## Minimal Metrics for Confidence

- **Completeness %** (not_null checks)  
- **Freshness** (last updated within SLO window)  
- **Duplicate ratio** (unique keys / total rows)  
- **Contract violation rate**  
- **Lineage completeness** (OpenLineage coverage %)  

---

## Open-Source Toolkit

- **Great Expectations** (validation)  
- **YData Profiling** (profiling + stats)  
- **OpenLineage** (lineage evidence)  
- **Superset/Metabase** (dashboard badges + trend charts)  

---

> Confidence indicators provide **explainable trust signals**, helping teams decide when data is reliable — and when to hold back.