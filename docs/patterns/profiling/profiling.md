---
title: Profiling Guide
type: "page"
layout: "single"
markup: "markdown"
---

# Data Profiling (DTE Pattern)

## Mission

Profiling is how **hidden risks become visible**. In Data Trust Engineering (DTE), profiling is not a one‑off audit—it’s a lightweight, continuous signal that feeds confidence indicators and trust dashboards.

---

## Quick Start: Profile a Dataset

```python
# profiling.py
import pandas as pd
from ydata_profiling import ProfileReport

# Load dataset
df = pd.read_csv("user_data.csv")

# Generate profile
profile = ProfileReport(df, title="User Data Profiling")
profile.to_file("artifacts/profiling/user_data_profile.html")

print("Profile written to artifacts/profiling/user_data_profile.html")
```

Run:
```bash
python profiling.py
```

---

## Design Patterns for Profiling

### 1) Confidence Indicators
- Derive trust metrics from profiling: completeness %, duplication %, freshness.  
- Publish indicators alongside dashboards.

### 2) Continuous Profiling
- Run profiling as part of CI/CD (sampled data).  
- Store artifacts (`.html`, `.json`) in evidence packs.

### 3) Profiling as Baseline
- Use profiles as reference points for drift detection.  
- Compare current vs. baseline profiles.

### 4) Lightweight Metrics
- Track only a few critical metrics: null %, cardinality, skewness.  
- Avoid full audits in every run.

---

## Minimal Metrics to Capture

- **Completeness %** — non‑null values per column.  
- **Duplication %** — duplicate rows or keys.  
- **Freshness** — max timestamp age.  
- **Skewness** — distribution anomalies.

---

## Open‑Source Toolkit

- [YData Profiling](https://github.com/ydataai/ydata-profiling)  
- [Great Expectations](https://github.com/great-expectations/great_expectations)  
- [dbt source freshness](https://docs.getdbt.com/docs/build/sources#freshness)  

---

> Profiling feeds **confidence indicators**, enabling teams to see problems before they erode trust.
