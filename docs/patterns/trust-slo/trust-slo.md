---
title: Trust SLOs & Error Budgets
type: "page"
layout: "single"
markup: "markdown"
---

# Trust SLAs / SLOs & Error Budgets (DTE Pattern)

## Mission

In Data Trust Engineering (DTE), **trust must be measurable**. Service Level Objectives (SLOs) and error budgets translate abstract notions of quality (freshness, null rates, contract violations) into quantifiable, actionable thresholds. This pattern aligns directly with DTE’s principle of **engineering rigor**: trust is not subjective — it is observable, enforced, and budgeted.

---

## Design Patterns for Trust SLOs

### 1) Define Trust SLOs
- **Freshness**: Data must be updated ≤ 60 minutes p95.  
- **Null Rate**: ≤ 0.5% of key fields may be null.  
- **Contract Violations**: ≤ 0.1% of records may violate schema/DQ rules.  

These should be tailored by **use case, risk, and value** — high-stakes AI training requires stricter SLOs than exploratory BI.

### 2) Error Budgets
- Each SLO violation consumes a portion of the error budget.  
- Teams may **burn error budget** temporarily but must remediate before shipping new features.  
- This ensures trust trade-offs are explicit and documented.  

### 3) Automation & Observability
- Track SLOs in **dashboards** (Superset, Metabase).  
- Alert on SLO breaches with **Prometheus/Grafana** or equivalent.  
- Use **OpenLineage** to track contract violations tied to pipeline runs.  

### 4) Governance-In-Flow
- Embed SLO checks into **CI/CD pipelines**.  
- Block merges or promotions when SLOs are breached.  
- Provide clear evidence packs for review (JSON/HTML).  

---

## Example: SLO YAML

```yaml
trust_slos:
  - metric: freshness_minutes_p95
    objective: 60
    error_budget: 5% of runs
  - metric: null_rate_percent
    objective: 0.5
    error_budget: 2% of records
  - metric: contract_violation_rate
    objective: 0.1
    error_budget: 1% of records
```

---

## Minimal Metrics to Track
- Freshness p95  
- Null % by column  
- Contract violation rate  
- SLO breach count & burn rate  

---

## Open-Source Tooling
- **dbt source freshness** for freshness budgets  
- **Great Expectations** for contract violations  
- **Superset/Metabase** for SLO dashboards  
- **OpenLineage** for blast radius tracking  

---

> Trust SLOs make **trust engineering explicit**: they quantify, budget, and enforce quality at scale, turning governance ideals into operational reality.