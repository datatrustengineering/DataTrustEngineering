---
title: Data Pipelines Guide
type: "page"
layout: "single"
markup: "markdown"
---

# Data Pipelines (DTE Pattern)

## Mission

Pipelines are the arteries of data systems. In DTE, they must be **observable, testable, and certifiable by use case, risk, and value**. This guide provides baseline patterns and open‑source recipes for trustworthy data pipelines.

---

## Design Patterns for Trusted Pipelines

### 1) Shift‑Left Validation
- Validate data at ingestion (schema + DQ rules).  
- Fail fast before polluting downstream.  

**Artifact:** `jsonschema` + Great Expectations.

### 2) Pipeline Contracts
- Define expectations as data contracts (schemas, SLAs).  
- Enforce violations in CI/CD or Airflow DAGs.  

**Artifact:** `contracts/*.json` + dbt tests.  

### 3) Observability by Default
- Emit lineage and trust metrics during pipeline runs.  
- Monitor freshness, nulls, contract violations.  

**Artifact:** OpenLineage client events + Superset dashboards.  

### 4) Idempotent Backfills
- Design backfill jobs to be deterministic and merge‑safe.  
- Prevent duplicates or replays.  

**Artifact:** dbt incremental models + upsert macros.  

### 5) Trust SLOs in DAGs
- Add SLAs for freshness and quality in orchestration layer.  
- Burn error budgets before feature tasks.  

**Artifact:** Airflow SLA + GE validation.

---

## Minimal Metrics to Track

- **Freshness p95**  
- **Null rate**  
- **Contract violation %**  
- **Pipeline failure MTTR**  
- **Backfill idempotency errors**  

---

## Example: Airflow + Great Expectations

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from great_expectations.dataset import PandasDataset

def ingest_and_validate():
    df = pd.read_csv("user_events.csv")
    dataset = PandasDataset(df)
    result = dataset.expect_column_values_to_not_be_null("event_id")
    with open("pipeline_validation.json", "a") as f:
        f.write(str(result))

with DAG("data_trust_pipeline", start_date=datetime(2025,1,1), schedule_interval="@daily") as dag:
    ingest_task = PythonOperator(
        task_id="ingest_and_validate",
        python_callable=ingest_and_validate
    )
```

---

## Example: OpenLineage Integration

```python
from openlineage.client import OpenLineageClient
from openlineage.client.run import RunEvent, RunState, Run, Job, Dataset
from datetime import datetime

client = OpenLineageClient(url="http://localhost:5000", api_key="")

job = Job(namespace="dte.pipelines", name="orders_pipeline")
dataset = Dataset(namespace="dte.pipelines", name="orders_raw")

event = RunEvent(
    eventType=RunState.COMPLETE,
    eventTime=datetime.utcnow().isoformat(),
    run=Run(runId="abcd-1234"),
    job=job,
    inputs=[dataset],
    outputs=[dataset]
)

client.emit(event)
print("Lineage event emitted to OpenLineage for orders_pipeline")
```

---

## Why It Matters

Traditional pipelines fail silently or only show health at the infrastructure level. DTE pipelines surface **trust signals** (contracts, SLOs, lineage) at every step. This ensures data delivered is not just “on time,” but **fit for use and AI‑ready**.

---
