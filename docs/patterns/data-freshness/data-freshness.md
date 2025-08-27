---
title: Data Freshness Guide
type: "page"
layout: "single"
markup: "markdown"
---

# Data Freshness (DTE Pattern)

## Mission

In Data Trust Engineering (DTE), **freshness is trust**. Stale data undermines decision-making and model reliability.  
This guide shows how to set **budgets, monitors, and graceful degradation paths** for freshness.

---

## Design Patterns for Data Freshness

### 1) Freshness & Staleness Budgets
- **Problem**: Silent data rot goes unnoticed.  
- **Pattern**: Define freshness thresholds per dataset (e.g., "≤ 1h p95 latency").  
- **Practice**: Alert when exceeded, label stale data in dashboards.  

```yaml
# dbt source freshness
version: 2
sources:
  - name: raw
    tables:
      - name: customer_orders
        loaded_at_field: created_at
        freshness:
          warn_after: {count: 2, period: hour}
          error_after: {count: 6, period: hour}
```

---

### 2) Trust SLOs on Freshness
- Define **SLOs** (e.g., 95% of events ingested within 30m).  
- Track breaches as **error budgets**.  

**Artifact**: Dashboard tiles with freshness SLO burndown.

---

### 3) Degrade Gracefully
- **Pattern**: If freshness budget is burned, mark data as "STALE" instead of silently serving it.  
- **Practice**: Add metadata badges in dashboards/reports.  

```sql
SELECT *, 
  CASE 
    WHEN updated_at < NOW() - INTERVAL '1 hour' 
    THEN 'STALE' ELSE 'FRESH' END as freshness_status
FROM customer_orders;
```

---

### 4) Observability Hooks
- Emit freshness metrics into Prometheus / OpenTelemetry.  
- Example: **lag_seconds** gauge for streaming pipelines.  

```python
# Python: Emit freshness lag metric
import time, prometheus_client as prom

freshness_gauge = prom.Gauge("customer_orders_lag_seconds", "Freshness lag in seconds")
def record_lag(event_timestamp):
    lag = time.time() - event_timestamp.timestamp()
    freshness_gauge.set(lag)
```

---

## Minimal Metrics to Track
- **p95 freshness** (load latency).  
- **% stale rows** beyond threshold.  
- **Error budget burndown** for freshness SLOs.  

---

## Open-Source Toolkit
- **dbt source freshness**  
- **Great Expectations** freshness checks  
- **Prometheus / Grafana** for monitoring  
- **Superset / Metabase** for labeling stale data  

---

> Freshness is not binary. In DTE, it’s **observable, budgeted, and explicit** — a trust signal users can rely on.