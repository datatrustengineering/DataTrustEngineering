---
title: Observability Patterns
---

# Design Patterns: Observability for Data & AI Trust

Observability in Data Trust Engineering (DTE) goes beyond logs and metrics. It is about **measuring trust directly**: freshness, contract violations, bias, lineage gaps, drift. These patterns treat observability as a **first-class engineering concern**.

---

## 1) Shift-Left Telemetry
**Problem:** Issues only surface in production dashboards.  
**Pattern:** Emit trust signals (freshness, nulls, contract violations) at ingestion or pipeline step. Use OpenTelemetry/Prometheus exporters.  
**Signals:** Time-to-detect ↓, MTTR ↓.  
**Artifacts:** Python client instrumentation, OTEL spans for pipeline steps.

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)
span_processor = BatchSpanProcessor(OTLPSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

with tracer.start_as_current_span("ingestion_step") as span:
    span.set_attribute("trust.freshness_seconds", 42)
    span.set_attribute("trust.contract_violations", 0)
    span.set_attribute("trust.null_rate", 0.003)
```

---

## 2) Trust SLO Dashboards
**Problem:** Teams lack clarity on acceptable error rates.  
**Pattern:** Define SLOs for trust (e.g., null rate ≤0.5%, freshness ≤60m p95). Burn error budgets before shipping new features.  
**Signals:** Fewer surprises, clearer trade-offs.  
**Artifacts:** YAML SLO spec + Superset/Metabase dashboards.

```yaml
slo:
  freshness_p95: "≤ 60m"
  null_rate: "≤ 0.5%"
  contract_violation_rate: "≤ 0.1%"
```

---

## 3) Drift & Fairness Monitors
**Problem:** AI models silently degrade.  
**Pattern:** Integrate Evidently AI or Fairlearn monitors into pipelines. Emit metrics to OTEL/Grafana.  
**Signals:** Drift detected early, fairness scores tracked.  
**Artifacts:** Drift dashboards + alerts.

```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref_df, current_data=curr_df)
print(report.as_dict())
```

---

## 4) Lineage-Aware Alerts
**Problem:** Silent blast radius.  
**Pattern:** Use OpenLineage events to trace upstream/downstream impact. Alert only affected consumers.  
**Signals:** Targeted pages, fewer false alarms.  
**Artifacts:** OpenLineage emitter + CI integration.

```python
from openlineage.client import OpenLineageClient
from openlineage.client.run import RunEvent, RunState, Run, Job

client = OpenLineageClient(url="http://localhost:5000")
event = RunEvent(
    eventType=RunState.COMPLETE,
    run=Run(runId="abcd-123")),
    job=Job(namespace="dte", name="pipeline.orders"),
    inputs=[], outputs=[]
)
client.emit(event)
```

---

## 5) Observability Budget
**Problem:** No time allocated for telemetry.  
**Pattern:** Allocate a fixed % of each sprint to observability tied to trust metrics (freshness, nulls, lineage).  
**Signals:** Fewer “unknown cause” incidents, faster MTTR.  
**Artifacts:** Metrics backlog + dashboard checklist.

---

## Minimal Metrics for DTE Observability
- Freshness (p95 latency from source → consumer)
- Null/contract violation %
- Drift & fairness scores
- Error budget burndown
- Lineage completeness (% known downstreams)

---

## Lightweight Tooling
- **OpenTelemetry** → standard tracing/metrics  
- **Superset/Metabase** → dashboards  
- **Evidently AI** → drift, explainability  
- **Fairlearn** → fairness metrics  
- **OpenLineage** → lineage + blast radius  

---

> Observability is not just *monitoring uptime*. In DTE, observability means **seeing trust itself**: is the system fresh, fair, explainable, and accountable?
