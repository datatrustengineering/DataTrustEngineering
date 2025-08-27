---
title: Idempotent Backfill Patterns
type: "page"
layout: "single"
markup: "markdown"
---

# Idempotent Backfills (DTE Pattern)

## Mission

Backfills are a necessary evil in data systems — but poorly designed backfills create **duplicates, inconsistencies, and replay storms**.  
In DTE, **backfills must be idempotent**: they should produce the same result no matter how many times they are run.

This guide provides open-source patterns to implement idempotent backfills with **merge/upsert logic, natural keys, and watermarks**.

---

## Design Patterns for Backfills

### 1) Merge/Upsert Instead of Insert-Only
**Problem:** Re-running inserts creates duplicate rows.  
**Pattern:** Use SQL `MERGE` (or dbt incremental models with `unique_key`) so records are updated/replaced, not duplicated.  
**Example (dbt incremental)**:
```sql
{{ config(materialized='incremental', unique_key='order_id') }}

SELECT order_id, customer_id, order_date, total
FROM {{ source('raw', 'orders') }}
```

---

### 2) Natural Keys as Identity
**Problem:** Surrogate IDs differ across runs, making deduplication impossible.  
**Pattern:** Use **business keys** (e.g., `order_id`) as primary identifiers for reconciliation.  

```yaml
models:
  - name: orders
    columns:
      - name: order_id
        tests: [unique, not_null]
```

---

### 3) Watermarks & Timestamps
**Problem:** Full backfills reprocess all history, overloading systems.  
**Pattern:** Use **watermarking** (max timestamp processed) to backfill incrementally.  

```python
# watermark_backfill.py
import pandas as pd, sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///warehouse.db")

# Load last watermark
watermark = pd.read_sql("SELECT max(order_date) as ts FROM orders", engine).iloc[0].ts

# Load only new/changed records
df = pd.read_csv("raw_orders.csv")
df_new = df[df["order_date"] > watermark]

df_new.to_sql("orders", engine, if_exists="append", index=False)
```

---

### 4) Idempotent DAG Design
**Problem:** Pipelines replay data inconsistently across retries.  
**Pattern:** DAG tasks should be **pure functions** (same input → same output) and write to **staging tables** before final merge.  

---

### 5) Backfill Audit & Reconciliation
**Problem:** Silent mismatches between historical and current runs.  
**Pattern:** Compare backfilled output vs. golden sources.  
**Artifacts:** reconciliation queries, validation dashboards.

```sql
SELECT COUNT(*) FROM orders_backfill WHERE order_id NOT IN (SELECT order_id FROM orders_current);
```

---

## Minimal Metrics

- **Duplicate key %** (per 1k rows)  
- **Backfill runtime** (p95 duration)  
- **Watermark lag** (max timestamp processed vs. now)  
- **Mismatch count** (backfill vs. golden source)

---

## Open-Source Toolkit

- **dbt incremental models** (`unique_key`)  
- **SQL MERGE** (Snowflake, BigQuery, Postgres ≥15)  
- **Great Expectations** (validation on backfilled sets)  
- **Airflow** (orchestrated staged runs)

---

> In DTE, **backfills aren’t firefighting** — they’re repeatable, measurable, and safe.  
> Idempotence = trust.
