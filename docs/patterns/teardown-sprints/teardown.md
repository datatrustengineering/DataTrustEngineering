---
title: Teardown Sprints
type: "page"
layout: "single"
markup: "markdown"
---

# Teardown Sprints (DTE Pattern)

## Mission
In DTE, **teardown sprints** are focused cycles (2–4 weeks) to pay down accumulated **data debt** by simplifying, retiring, or refactoring fragile assets. They ensure long-term agility by keeping complexity under control.

---

## Design Patterns for Teardown

### 1) Dead Code Removal
- Drop unused tables, models, and DAGs.  
- Archive in Git to allow rollback.  

### 2) Collapse Over-Abstractions
- Simplify over-engineered DAGs or dbt models.  
- Reduce model depth, merge trivial layers.  

### 3) DAG Depth Reduction
- Measure depth; aim to keep pipelines shallow.  
- Long DAGs → fragile DAGs.  

### 4) Retirement Checklist
- Track assets to decommission: owner, usage, dependencies.  
- Communicate across teams before removal.  

---

## Example: DAG Depth Metric

```sql
-- dbt model depth check
select dag_id, count(*) as depth
from lineage_graph
group by dag_id
having count(*) > 20
```

---

## Tooling
- **dbt docs** + lineage graph (identify orphans/dead models)  
- **OpenLineage** (impact analysis before teardown)  
- **Superset/Metabase** (track before/after metrics)  

> Teardown sprints restore **trust velocity** by pruning the garden of data systems.
