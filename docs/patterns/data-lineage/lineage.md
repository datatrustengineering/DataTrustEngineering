---
title: Data Lineage Guide
type: "page"
layout: "single"
markup: "markdown"
---

# Data Lineage (DTE Pattern)

## Mission

Lineage is **provenance for trust**: it shows what a metric, model, or decision depends on and the **blast radius** of changes. In DTE, we use lineage to enable **impact‑aware changes, faster incident triage, and auditable evidence**—without vendor lock‑in or policy theater.

This guide is a **baseline**: practical, open‑source recipes you can fork and extend. It aligns with the Manifesto’s focus on **engineering rigor, observability, and risk‑tiered assurance** (not regulatory claims).

---

## Quick Start: Emit OpenLineage Events

Use the OpenLineage standard to describe jobs, inputs, and outputs. Collect events with a compatible backend (e.g., **Marquez**), then visualize lineage next to trust metrics.

```python
from openlineage.client import OpenLineageClient
from openlineage.client.run import RunEvent, RunState, Run, Job, Dataset
from datetime import datetime

# 1) Configure client (replace URL with your collector)
client = OpenLineageClient(url="http://localhost:5000", api_key="")

# 2) Describe the job and datasets
job = Job(namespace="dte.pipeline", name="orders_transform")
input_ds = Dataset(namespace="dte.raw", name="orders_raw")
output_ds = Dataset(namespace="dte.dw", name="orders_clean")

# 3) Emit a COMPLETE run event
event = RunEvent(
    eventType=RunState.COMPLETE,
    eventTime=datetime.utcnow().isoformat(),
    run=Run(runId="run-001"),
    job=job,
    inputs=[input_ds],
    outputs=[output_ds]
)
client.emit(event)
print("OpenLineage event emitted")
```

> Tip: Add emitters inside Airflow/Prefect/DBT tasks so lineage is produced **in flow**, not after the fact.

---

## Design Patterns for Lineage

### 1) Lineage‑Verified Changes (CI Gate)
**Problem:** Schema changes land without awareness of downstream impact.  
**Pattern:** On PRs, compute the **impact set** from lineage and require approval if the **blast radius** exceeds a threshold (e.g., >5 downstream nodes or any certified dataset).  
**Signals:** Post‑deploy breakages in “unknown” downstreams, change failure rate.  
**Artifacts:** OpenLineage emitter + CI job to query the collector and annotate PRs.

### 2) Source‑of‑Truth Annotation
**Problem:** Competing datasets create conflicting KPIs.  
**Pattern:** Mark canonical **golden tables** and **certified datasets** in lineage metadata; prefer these as model and dashboard inputs.  
**Signals:** “Two truths” debates, duplicate KPI definitions.  
**Artifacts:** Metadata tags (`canonical=true`, `certified=true`) + dashboard badges.

### 3) Incident Short‑Circuit
**Problem:** Slow triage during pipeline incidents.  
**Pattern:** Alert payloads include **upstream freshness**, **recent contract violations**, and **last successful run** for impacted nodes (derived from lineage).  
**Signals:** MTTR too high; repeated “where did this come from?” loops.  
**Artifacts:** Alert formatter pulling lineage + trust SLOs; run history links.

### 4) Evidence Packs for Certification
**Problem:** Trust claims lack concrete proof.  
**Pattern:** Export a lineage subgraph plus recent **quality checks**, **freshness**, and **contract‑violation history** as an **evidence pack** for the certified dataset. Store alongside the dataset version.  
**Signals:** Audit requests, stakeholder confidence gaps.  
**Artifacts:** JSON/HTML bundle referenced by the Trust Dashboard.

### 5) Overlay Lineage Health in the Trust Dashboard
**Problem:** Lineage is disconnected from day‑to‑day decisions.  
**Pattern:** Display **lineage coverage %**, **unknown downstreams**, and **blast radius** next to quality/fairness metrics in the dashboard. Badge datasets when lineage falls below a threshold.  
**Signals:** Teams ship without seeing provenance risk.  
**Artifacts:** Dashboard tiles fed by OpenLineage queries.

---

## Minimal Metrics (Lineage KPIs)

- **Lineage coverage %**: fraction of datasets/jobs represented in lineage.  
- **Unknown downstreams**: count of assets with incomplete/unknown consumers.  
- **Median blast radius**: median number of downstream nodes impacted per change.  
- **Certified‑path integrity**: share of certified datasets with complete upstream lineage.  

---

## Open‑Source Toolkit

- **OpenLineage** — standard client & spec for lineage events.  
- **Marquez** — OpenLineage collector & UI.  
- **dbt‑lineage** / adapters — derive job/dataset graphs from transformations.  
- **Superset/Metabase** — render lineage health in Trust Dashboard tiles.  

---

## Contribute

- Add emitters for your orchestrator (Airflow/Prefect/Spark/dbt).  
- Share CI scripts that compute blast radius and annotate PRs.  
- Propose additional KPIs or dashboard tiles for lineage health.  

> **Goal:** Make provenance **visible and actionable** so teams can change faster, with confidence.


