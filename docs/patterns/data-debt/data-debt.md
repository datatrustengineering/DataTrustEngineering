---
title: Data Debt Guide (DTE Pattern)
type: "page"
layout: "single"
markup: "markdown"
---

# Data Debt Guide (DTE Pattern)

## Mission

In Data Trust Engineering (DTE), **data quality is reframed as technical debt** — visible, measurable, and fixable — rather than an abstract governance checkbox.
The mission of this guide is to provide **lightweight, open-source recipes** for embedding quality checks directly into pipelines and products, aligned with the [DTE Manifesto](../Manifesto.md).

The goal is not to replicate vendor platforms, but to **set a baseline**: practical, repeatable patterns that anyone can fork, extend, and adapt to their own systems.

---

## Why It Matters

- Many organizations struggle with governance complexity, often because they ignore technical debt until it becomes problematic.
- AI systems add new forms of debt: drift, bias, fairness regressions.
- Without clear **trust SLOs and error budgets**, teams ship features while debt compounds silently.

---

## Design Patterns: Technical Debt in Data & AI

Below are practical design patterns that help manage technical debt in pipelines, models, and contracts while maintaining delivery velocity. Each pattern is:
- **Lightweight** (Markdown, dbt tests, Great Expectations suites)
- **Observable** (Superset/Metabase dashboards, OpenLineage events)
- **Community-Driven** (fork and adapt, PR improvements)

> 💡 These patterns form the **baseline playbook** for DTE teams. They are not mandates, but starting points for contributors to extend.


# Design Patterns: Technical Debt in Data & AI

Technical debt isn't a moral failing; it's a budget. These patterns make debt **visible, measurable, and payable**—without halting delivery.

## 1) Data Debt Ledger
**Problem:** Invisible debt accumulates across pipelines, models, and contracts.  
**Pattern:** Maintain a lightweight, git-tracked `DATA_DEBT.md` (one per domain) listing items, impact, principal, interest (ongoing cost), and a due date.  
**Signals:** MTTR ↑, ad-hoc fixes ↑, "hero debugging" stories.  
**Artifacts:** Markdown ledger + GitHub Issues labels `debt/*`.

## 2) Contract Drift Guard (Shift-Left)
**Problem:** Producers change payloads; downstream breaks later.  
**Pattern:** Enforce **data contracts at ingestion** (jsonschema + Great Expectations). Fail fast on drift; open an issue automatically.  
**Signals:** Contract violations %, time-to-detect drift.  
**Artifacts:** `contracts/*.json`, CI step `contract-validate`.

## 3) Schema Freeze Windows
**Problem:** Breaking changes land during peak loads.  
**Pattern:** Calendarized "freeze windows" + `dbt` CI rule requiring `BREAKING_CHANGE_APPROVED=true`.  
**Signals:** Incidents during release windows, weekend pages.  
**Artifacts:** `dbt` pre-commit + release calendar.

## 4) Strangler-Fig Modernization
**Problem:** Monolithic, fragile pipelines.  
**Pattern:** Route critical slices to a **new, small, governed path**, retire old nodes incrementally.  
**Signals:** Size/complexity ↑; change failure rate ↑.  
**Artifacts:** Routing map, retirement checklist.

## 5) Trust SLOs & Error Budgets
**Problem:** Quality is subjective; tradeoffs unclear.  
**Pattern:** Define **SLOs for trust** (e.g., Freshness ≤ 60m p95, Null rate ≤ 0.5%, Contract violations ≤ 0.1%). Burn error budgets before feature work.  
**Signals:** SLO burn-down, breach frequency.  
**Artifacts:** SLO YAML + dashboard tiles.

## 6) Test Pyramid for Data
**Problem:** Only end-to-end tests; slow and flaky.  
**Pattern:** **80% unit** (dbt/gx expectations at model/column), **15% integration** (contract+lineage), **5% e2e**.  
**Signals:** Flaky test rate, time-to-signal.  
**Artifacts:** `schema.yml` tests, GE suites, a small e2e harness.

## 7) Idempotent Backfills
**Problem:** Backfills create duplicates and replays.  
**Pattern:** Design jobs to be **idempotent** (natural keys, merge/upsert, watermarking).  
**Signals:** Duplicate keys, non-deterministic counts across runs.  
**Artifacts:** Upsert macros, watermark processors.

## 8) Freshness & Staleness Budgets
**Problem:** Silent data rot.  
**Pattern:** Define freshness budgets per product; alert when exceeded; degrade gracefully (label as "stale").  
**Signals:** Freshness p95, stale-data reads.  
**Artifacts:** `dbt source freshness`, dashboard badges.

## 9) Lineage-Verified Changes
**Problem:** Hidden blast radius.  
**Pattern:** **OpenLineage** events in CI: compute impact set from lineage; require approvals when blast radius > threshold.  
**Signals:** Post-deploy breakages in "unknown" downstreams.  
**Artifacts:** OpenLineage emitter + CI guard.

## 10) Canonicalization & De-Dup
**Problem:** Divergent entity definitions inflate debt.  
**Pattern:** Centralize entity resolution (keys, survivorship rules), emit **golden tables** with provenance.  
**Signals:** Conflicting KPIs, "two truths" debates.  
**Artifacts:** Canonical model + dedupe rules in dbt.

## 11) Observability Budget
**Problem:** No time for metrics/logs/traces.  
**Pattern:** Allocate a fixed % of each story to add/upgrade **observability tied to trust indicators** (freshness, nulls, contract violations, lineage gaps).  
**Signals:** Incidents without telemetry; mean time to *know* ↑.  
**Artifacts:** Metrics spec + dashboard checklist.

## 12) Teardown Sprints (2–4 Weeks)
**Problem:** Compounded complexity; progress stalls.  
**Pattern:** Focused "teardown & simplify" sprints: remove dead code, reduce DAG depth, collapse over-abstractions, archive orphan tables.  
**Signals:** Lead time ↑, failed runs ↑, engineer sentiment ↓.  
**Artifacts:** Before/after metrics: DAG depth, model count, build time.

---

## Minimal Metrics to Track (Debt KPIs)
- **Contract violation rate** (per 1k msgs)
- **Freshness p95** / **SLO breaches**
- **MTTR** and **change failure rate**
- **Debt velocity** (new debt created vs. paid down)

---

## Quick Start: Great Expectations

Use [Great Expectations](https://github.com/great-expectations/great_expectations) to add validation at the point of ingestion or transformation.

```python
import great_expectations as ge
import pandas as pd

# Sample dataframe
df = pd.DataFrame({
    "id": [1, 2, 2, None],
    "value": [10, 20, None, 40]
})

# Wrap dataframe with Great Expectations
gdf = ge.from_pandas(df)

# Example expectations
results = [
    gdf.expect_column_values_to_be_unique("id").validate(),
    gdf.expect_column_values_to_not_be_null("value").validate()
]

print(results)
```

---

## How to Use These Patterns

1. **Pick a Pattern** → Start small (e.g., add freshness checks or contracts at ingestion).
2. **Fork & Adapt** → Use the open-source examples, swap in your stack.
3. **Contribute** → Extend a pattern or propose a new one via PR.

---

## Why This Matters

Many organizations struggle with governance complexity, often because they ignore technical debt until it becomes problematic. These patterns provide practical approaches to make debt visible, measurable, and manageable—without halting delivery.

---

## References

- Great Expectations (2025). Down with Pipeline Debt. Available at: https://greatexpectations.io/blog/down-with-pipeline-debt-introducing-great-expectations/
- Cloud Data Insights (2025). Data Pipeline Pitfalls. Available at: https://www.clouddatainsights.com/data-pipeline-pitfalls-unraveling-the-technical-debt-tangle/
- DQOps (2025). Technical Debt in Data Engineering. Available at: https://dqops.com/technical-debt-in-data-engineering/

*Built with Data Trust Engineering principles of practical collaboration.*

#DTERevolution