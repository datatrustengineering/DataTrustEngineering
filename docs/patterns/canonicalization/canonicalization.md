---
title: Canonicalization & De-duplication
type: "page"
layout: "single"
markup: "markdown"
---

# Canonicalization & De-duplication (DTE Pattern)

## Mission
In DTE, canonicalization and de-duplication reduce **data debt** caused by conflicting definitions and duplicate entities. They create **golden records** with clear provenance, enabling trust in metrics and AI outputs.

---

## Design Patterns for Canonicalization

### 1) Golden Tables
- Centralize entity resolution rules (e.g., customer, product, account).
- Emit a **canonical table** that downstreams trust.

### 2) Survivorship Rules
- Define clear precedence: “CRM beats webform,” “latest update wins.”
- Apply consistently across pipelines.

### 3) Deduplication with Keys
- Enforce natural/business keys in contracts (e.g., `order_id`).
- Deduplicate with **merge/upsert** patterns.

### 4) Provenance Metadata
- Track lineage for every resolution step with **OpenLineage** events.
- Attach metadata to golden records (source, rule applied, timestamp).

---

## Example dbt Model for Deduplication

```sql
-- models/customer_canonicalized.sql
{{ config(materialized='table') }}

with ranked as (
  select *,
         row_number() over (partition by customer_id order by updated_at desc) as rn
  from {{ source('crm', 'customers') }}
)

select customer_id, name, email, updated_at
from ranked
where rn = 1
```

---

## Tooling
- **dbt** (canonical models, dedup macros)  
- **Great Expectations** (enforce uniqueness)  
- **OpenLineage** (lineage of resolution logic)  

> Canonicalization is how DTE turns **multiple truths** into **one trusted truth**.
