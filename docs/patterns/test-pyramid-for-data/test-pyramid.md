---
title: Test Pyramid for Data
type: "page"
layout: "single"
markup: "markdown"
---

# Test Pyramid for Data (DTE Pattern)

## Mission

In Data Trust Engineering (DTE), tests are **evidence**, not ceremony.  
The **data test pyramid** balances speed and signal: **many fast unit checks**, **some integration tests** across contracts/lineage, and **a few end‑to‑end (e2e)** scenarios to validate the happy path.  
Goal: **catch most issues early (shift‑left)** while keeping delivery velocity high.

---

## Shape & Ratios (Guideline)

- **Unit (≈80%)** — column/model‑level checks that run in seconds.  
- **Integration (≈15%)** — multi‑table/contract/lineage validations.  
- **End‑to‑End (≈5%)** — minimal full‑pipeline smoke tests on small samples.

> Ratios are guidance — tune by use case **risk & value**.

---

## Unit Tests (Fast, Local Signal)

### dbt built‑ins
```yaml
# models/schema.yml
version: 2
models:
  - name: orders_clean
    description: "Cleaned orders"
    columns:
      - name: order_id
        tests: [not_null, unique]
      - name: total
        tests:
          - not_null
          - relationships:
              to: ref('currencies')
              field: currency_code
```

### Great Expectations quick checks
```python
# tests/test_orders_clean.py
import pandas as pd
from great_expectations.dataset import PandasDataset

df = pd.read_parquet("artifacts/orders_clean.parquet")
gx = PandasDataset(df)
assert gx.expect_column_values_to_not_be_null("order_id")["success"]
assert gx.expect_column_values_to_be_between("total", min_value=0)["success"]
```

**Signals:** null %, duplicate %, bounds, referential integrity.

---

## Integration Tests (Contracts & Lineage)

### Contract conformance across hops
```python
# tests/test_contract_conformance.py
import json, pandas as pd
from jsonschema import validate

contract = json.load(open("contracts/customer_orders.json"))
df = pd.read_parquet("artifacts/warehouse/customer_orders.parquet")

# Validate a sample batch against the jsonschema contract
sample = df.sample(min(500, len(df))).to_dict(orient="records")
for rec in sample:
    validate(instance=rec, schema=contract)
```

### Lineage impact check with OpenLineage
```python
# tests/test_lineage_impact.py
from openlineage.client import OpenLineageClient
client = OpenLineageClient(url="http://localhost:5000", api_key="")

# Example: assert that downstream dataset is recorded for the job
runs = client.get_runs(job="dte.orders.pipeline")  # pseudocode: use your client helper
assert any("customer_orders_curated" in r.outputs for r in runs)
```

**Signals:** contract drift, blast radius coverage, multi‑table expectations.

---

## End‑to‑End (Minimal, Sampled)

```bash
# e2e: run on a tiny slice in CI
make e2e   SOURCE_LIMIT=500   START_TS=2025-01-01T00:00:00Z   END_TS=2025-01-01T01:00:00Z
```

```python
# e2e/e2e_smoke_test.py
import subprocess, json, pathlib

# 1) run ingestion -> transform -> publish on a time‑boxed window
subprocess.check_call(["python", "tools/ingest.py", "--limit", "500"])
subprocess.check_call(["dbt", "run", "--select", "tag:core"])

# 2) validate golden KPIs
kpis = json.load(open("artifacts/kpis.json"))
assert kpis["orders_count"] > 0
assert kpis["dup_key_rate"] < 0.001
```

**Signals:** basic system wiring, KPI sanity, env parity.

---

## CI Strategy

- **Pre‑commit**: lint SQL/Python, run ultra‑fast unit tests.  
- **Push/PR**: unit + integration + lineage impact checks; publish artifacts.  
- **Nightly**: small e2e on sampled data + drift/evals reports.  

**Fail‑fast rules:** block merge if **contract violations**, **null/dup spikes**, or **lineage coverage < threshold**.

---

## Flake & Debt Management

- Track **flaky test rate** and quarantine with an owner + due date.  
- Add failures to **DATA_DEBT.md** with principal/interest.  
- Prefer **deterministic fixtures** over live prod hits.

---

## Minimal Metrics

- Unit test duration p95  
- Integration failure rate  
- E2E mean runtime & failure rate  
- Flaky test % and time‑to‑signal  

---

## Open‑Source Toolkit

- **dbt tests** for schema & relationships  
- **Great Expectations** for expectations as code  
- **OpenLineage** for lineage impact assertions  
- **pytest** for Python harnesses; **pre‑commit** for local speed  
- **Superset/Metabase** to visualize test KPIs in the Trust Dashboard

---

> The best test pyramid **protects velocity** while **raising trust** — lots of cheap signal, a little expensive certainty.
