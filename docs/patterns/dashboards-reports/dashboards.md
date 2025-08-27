---
title: Dashboards & Reports Guide
type: "page"
layout: "single"
markup: "markdown"
---

# Dashboards & Reports (DTE Pattern)

## Mission

Dashboards and reports are **trust surfaces** — where data meets decision-makers. In DTE, dashboards must be **transparent, lineage‑aware, and annotated with trust indicators**, not just pretty charts.  
They should answer: *“Can I trust this number?”* as much as *“What is this number?”*.

---

## Quick Start: Dashboard with Lineage Metadata

Example: Push engagement metrics into [Metabase](https://github.com/metabase/metabase) and emit lineage to [OpenLineage](https://github.com/OpenLineage/OpenLineage).

```python
from openlineage.client import OpenLineageClient
from openlineage.client.run import RunEvent, RunState, Run, Job, Dataset
from datetime import datetime
import pandas as pd

# Initialize OpenLineage client
client = OpenLineageClient(url="http://localhost:5000", api_key="")

# Define job and dataset
job = Job(namespace="dte.dashboard", name="engagement_report")
dataset = Dataset(namespace="dte.dashboard", name="engagement_metrics")

# Emit lineage event
event = RunEvent(
    eventType=RunState.COMPLETE,
    eventTime=datetime.utcnow().isoformat(),
    run=Run(runId="abc-123"),
    job=job,
    inputs=[dataset],
    outputs=[dataset]
)
client.emit(event)

print("Lineage emitted for engagement_report job")
```

---

## Design Patterns for Trusted Dashboards

### 1) Annotated Metrics
- Every chart shows **trust badges** (freshness, quality score, lineage).  
- Example: “Data last refreshed 27m ago; null rate <0.5%”.  

### 2) Lineage‑Linked Reports
- Embed OpenLineage links in dashboard tooltips.  
- Let users trace metrics to source systems in one click.  

### 3) Guardrail Overlays
- Visualize adherence to **DTE principles** (trust, certification, observability) as radar/score overlays.  
- Use these to communicate gaps proactively.  

### 4) Evidence‑Attached Dashboards
- Attach **AI eval artifacts** (fairness, drift, SHAP plots) next to KPIs.  
- Numbers without evidence aren’t trusted numbers.  

### 5) Trust‑as‑Default UX
- Treat trust signals as first‑class citizens in the UI.  
- Don’t bury lineage/quality in a separate tab — show inline.  

---

## Minimal Metrics to Display

- **Freshness**: “Data updated at X; SLA = Y”  
- **Completeness**: % non‑nulls per key field  
- **Lineage Coverage**: % upstream/downstream mapped  
- **Contract Violations**: Count or % flagged at ingestion  
- **AI Evals** (if model output): fairness delta, drift score  

---

## Open‑Source Toolkit

- **Metabase** or **Superset** — lightweight dashboards  
- **OpenLineage** — lineage events  
- **YData Profiling** — profiling overlays  
- **Evidently AI** — attach eval reports  

---

> Dashboards should not just visualize KPIs — they must **communicate trustworthiness**.  
