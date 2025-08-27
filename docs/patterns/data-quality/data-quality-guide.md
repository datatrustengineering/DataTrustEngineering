---
title: Data Quality Guide
type: "page"
layout: "single"
markup: "markdown"
---

# Data Quality Guide (DTE Pattern)

## Mission

In Data Trust Engineering (DTE), **data quality is reframed as technical debt** — visible, measurable, and fixable — rather than an abstract governance checkbox.  
The mission of this guide is to provide **lightweight, open-source recipes** for embedding quality checks directly into pipelines and products, aligned with the [DTE Manifesto](../Manifesto).  

The goal is not to replicate vendor platforms, but to **set a baseline**: practical, repeatable patterns that anyone can fork, extend, and adapt to their own systems.  

---

## Design Patterns for Data Quality

### 1. Shift-Left Validation
- **Enforce schema + expectations at ingestion** (e.g., Kafka consumer, API layer).  
- Catch issues before they propagate downstream.  

### 2. Defense in Depth
- Mirror contracts with **dbt tests** in the warehouse (`not_null`, `unique`).  
- Keep upstream + downstream aligned.  

### 3. Trust SLOs
- Track **null rate, freshness, and contract violation %** as error budgets.  
- Burn error budget before new feature work.  

### 4. Confidence Indicators
- Profile datasets with **[YData Profiling](https://github.com/ydataai/ydata-profiling)**.  
- Publish metrics alongside dashboards (completeness %, duplication %, freshness).  


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
