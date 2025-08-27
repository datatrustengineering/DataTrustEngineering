---
title: Data Contracts Guide
type: "page"
layout: "single"
markup: "markdown"
---

# Data Contracts (DTE Pattern)

## Mission

In DTE, **data contracts are trust enforcers at ingestion**.  
They shift validation **left** — catching schema drift, quality issues, and SLA violations before they propagate downstream. Contracts are **lightweight, versioned artifacts** (YAML/JSON) that engineers can enforce in pipelines or APIs.

---

## Quick Start: Contract Example

**`contracts/customer_orders.json`**

```json
{
  "urn": "urn:product:customer_orders",
  "schema": {
    "order_id": "string",
    "customer_id": "string",
    "order_date": "date",
    "total": "decimal"
  },
  "dq_rules": {
    "order_date": "must not be in future",
    "total": "must be >= 0"
  },
  "sla": {
    "availability": "99.9%",
    "freshness": "daily by 8am"
  },
  "business_metadata": {
    "domain": "Sales",
    "description": "Captures all customer order and revenue events.",
    "product_owner": "sales-analytics@company.com",
    "tags": ["sales", "orders", "revenue"]
  }
}
```

---

## Shift-Left Validation Harness

```python
# validate_contract.py
import json, datetime
from jsonschema import validate
from great_expectations.dataset import PandasDataset
import pandas as pd

CONTRACT = json.load(open("contracts/customer_orders.json"))

def validate_event(event: dict) -> bool:
    # 1) Schema validation
    validate(instance=event, schema={
        "type": "object",
        "properties": {
            "order_id": {"type": "string"},
            "customer_id": {"type": "string"},
            "order_date": {"type": "string", "format": "date"},
            "total": {"type": "number", "minimum": 0}
        },
        "required": ["order_id", "customer_id", "order_date", "total"]
    })

    # 2) Quality rules
    if datetime.date.fromisoformat(event["order_date"]) > datetime.date.today():
        raise ValueError("order_date must not be in future")

    # 3) Great Expectations checks
    df = pd.DataFrame([event])
    ds = PandasDataset(df)
    assert ds.expect_column_values_to_not_be_null("order_id")["success"]
    return True
```

**Run**
```bash
python validate_contract.py < sample_event.json
```

---

## Design Patterns for Data Contracts

### 1) Shift-Left Governance
- Enforce schema + rules **before** data lands in pipelines.  
- Fail fast on contract violations.  

### 2) Defense in Depth
- Mirror contracts with **dbt tests** in the warehouse.  
- Keep upstream and downstream aligned.  

### 3) Versioned in Git
- Contracts live as code (`contracts/*.json`).  
- Reviewed via pull requests.  

### 4) SLA + Metadata Included
- Contracts include **freshness**, **availability**, and **domain ownership**.  
- Builds accountability across teams.  

---

## dbt Example

```yaml
# models/schema.yml
version: 2
models:
  - name: customer_orders
    description: "Customer orders aligned to contract"
    columns:
      - name: order_id
        tests: [not_null, unique]
      - name: total
        tests:
          - not_null
          - accepted_values: {values: [">=0"]}   # custom macro
```

---

## Why This Matters

- **Prevents drift** before it breaks downstream pipelines  
- **Shifts trust left** to the ingestion edge  
- **Codifies SLAs** alongside schema and DQ rules  
- **Community-friendly**: lightweight JSON/YAML contracts anyone can adopt  

---

#DTERevolution
