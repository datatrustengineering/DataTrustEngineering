---
title: Data Trust Engineering Use Cases
type: "page"
layout: "single"
markup: "markdown"
---

## Data Trust Engineering (DTE) Use Cases and Trust Dashboard

Welcome to the **Data Trust Engineering (DTE) Use Cases** and **Trust Dashboard**, flagship artifacts of the Data Trust Engineering movement. These open-source tools and examples embody DTE’s principles of trust, engineering rigor, and AI-readiness as outlined in the [Data Trust Manifesto](../Manifesto.md).
---

## Mission for Examples & Design Patterns

The examples in this guide are designed as **illustrations, not end-to-end products**. Each one shows how DTE principles can be applied in practice using open-source components. Think of them as **recipes** that teams can fork, adapt, and extend—not polished systems.

Over time, these examples will also evolve into a library of **design patterns for Trust Engineering**.  
- Patterns for **shift-left quality** (contracts at ingestion)  
- Patterns for **lineage and observability** (OpenLineage integration, monitoring pipelines in real time)  
- Patterns for **AI trust** (fairness, explainability, drift checks)  
- Patterns for **AI evaluations** (systematic LLM/RAG evals, confidence scoring, guardrail testing)  
- Patterns for **observability** (metrics, logging, tracing tied to trust indicators)  
- Patterns for **technical debt management** (dbt tests, Great Expectations)  

The goal is to provide **starting points** and **reusable patterns** that make trust engineering approachable, repeatable, and community-driven.

---

## Purpose of the Use Cases

These use cases are not full-blown projects or attempts to rebuild the entire ecosystem of governance and AI tools. The ecosystem is already too large and fragmented. Instead, the purpose is to act as a guide with examples, showing how open-source components can be applied to real trust problems.

- **Baseline, not best-in-class**: The goal is not to compete with enterprise tools, but to set a baseline reference that’s easy to understand and extend.  
- **Trust Dashboard as MVP**: This is the anchor artifact — a lightweight starting point that demonstrates DTE principles (trust, rigor, AI-readiness) in a tangible way.  
- **Examples, not platforms**: Each use case is a recipe (e.g., data contracts at ingestion, lineage with OpenLineage, fairness checks with Fairlearn), not a production-ready service.  
- **Community-first**: The structure invites contributions, but the priority is to show how to start, not to provide a polished ecosystem out of the gate.  



## The DTE Trust Dashboard

The **DTE Trust Dashboard** is a practical, open-source artifact that visualizes real-time trust metrics. It empowers teams to build trusted, scalable systems for high-stakes use cases such as AI training, regulatory reporting, and GenAI safety.

### Implementations
- **HTML Version (`DTE_Trust_Dashboard.html`)**  
  Built with Chart.js for lightweight, static visualization.  
- **Streamlit Version (`app.py`)**  
  Built with Streamlit and Plotly for interactive, Python-based visualization.  

Both versions monitor key metrics:  
- **AI Fairness** (Fairlearn) — fairness scores across protected attributes (e.g., gender, age).  
- **Model Explainability** (Evidently AI) — feature importance visualization.  
- **Guardrails Adherence** — radar chart showing adherence to DTE principles: trust, certification by use case/risk/value, observability.  
- **GenAI Safety** (Evidently AI) — metrics for toxicity, bias, hallucination, privacy leakage, factual accuracy.  
- **Model Performance** (MLflow) — accuracy, F1, AUC-ROC over time.  

### DTE Principles in Action
- **Trust**: Transparent, real-time metrics build confidence for enterprises, users, and AI systems.  
- **Engineering Rigor**: Robust implementation with lightweight open-source tools (Chart.js, Plotly, Superset).  
- **Collaboration**: Open, extensible design inviting community contributions.  

### Getting Started
**HTML Version**
```bash
# Open in browser
open tools/data-trust-dashboard/DTE_Trust_Dashboard.html
# Or host via GitHub Pages or a simple web server
```

**Streamlit Version**
```bash
cd tools/data-trust-dashboard
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
# Access at http://localhost:8501
```

**Extend the Dashboard**
- **Data Quality**: Integrate Great Expectations.  
- **Lineage**: Connect Apache Atlas.  
- **AI Governance**: Add Fairlearn, Evidently AI, MLflow, or SDV.  

---

## Practical Use Cases for DTE

The following **use cases** demonstrate how to implement DTE principles with open-source code. Each includes a description, its alignment with DTE, and a code artifact.

---

### 1. Trust Dashboard
See **The DTE Trust Dashboard** above — the flagship artifact.  

---

### 2. Agentic Workflows Trust
Validate agent decisions with logged outputs for auditability.  
**Artifact**: [LangChain](https://github.com/langchain-ai/langchain) + [Great Expectations](https://github.com/great-expectations/great_expectations).  

```python
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from great_expectations.dataset import PandasDataset
import pandas as pd, json

def validate_data(input_data: str) -> str:
    df = pd.read_json(input_data)
    dataset = PandasDataset(df)
    result = dataset.expect_column_values_to_be_unique("id").to_json_dict()
    return json.dumps({"success": result["success"], "details": result["result"]})

tools = [Tool(name="DataValidator", func=validate_data, description="Validates uniqueness")]
llm = OpenAI(model="gpt-3.5-turbo", api_key="your-openai-key")
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")

data = pd.DataFrame({"id": [1, 2, 2, 4]}).to_json()
result = agent.run(f"Validate this data for uniqueness: {data}")
```

---

### 3. RAG / GraphRAG
Ground LLMs in trusted knowledge graphs.  
**Artifact**: [Neo4j](https://github.com/neo4j/neo4j) + LangChain.  

```python
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphQAChain
from langchain.llms import OpenAI

graph = Neo4jGraph(url="bolt://localhost:7687", username="neo4j", password="password")
graph.query("""
CREATE (p:Principle {name: "Transparency"})
CREATE (p2:Principle {name: "Accountability"})
CREATE (p)-[:RELATED_TO]->(p2)
""")

llm = OpenAI(model="gpt-3.5-turbo", api_key="your-openai-key")
chain = GraphQAChain.from_llm(llm, graph=graph)
print(chain.run("What principles are related to Transparency?"))
```

---

### 4. Data Products with Contracts
Formalize schemas and SLAs.  
**Artifact**: [dbt](https://github.com/dbt-labs/dbt-core) + [Open Data Contract Standard](https://github.com/datacontract/datacontract-specification).  

```yaml
# datacontract.yaml
datacontract:
  id: user_analytics
  version: 1.0.0
  schema:
    fields:
      - name: user_id
        type: string
        required: true
        unique: true
      - name: event_timestamp
        type: timestamp
        required: true
```

```sql
-- dbt model: models/user_analytics.sql
{{ config(materialized='table') }}
SELECT user_id, event_timestamp, COUNT(*) as event_count
FROM {{ source('raw', 'user_events') }}
GROUP BY user_id, event_timestamp
```

---

### 5. Data Models
Define consistent schemas and validate them with **dbt tests** (open-source).  
**Artifacts**: [Apache Avro](https://github.com/apache/avro) for portable schemas + **dbt** for validation.

**Avro schema**
```json
{
  "type": "record",
  "name": "ConsentRecord",
  "fields": [
    {"name": "user_id", "type": "string"},
    {"name": "consent_given", "type": "boolean"},
    {"name": "timestamp", "type": "string"}
  ]
}
```

**dbt model + tests**
```sql
-- models/consent_records.sql
{{ config(materialized='table') }}
SELECT
  user_id,
  consent_given,
  timestamp
FROM {{ source('raw', 'consent_events') }}
```

```yaml
# models/schema.yml
version: 2
models:
  - name: consent_records
    description: "Normalized consent records"
    columns:
      - name: user_id
        tests:
          - not_null
      - name: consent_given
        tests:
          - not_null
      - name: timestamp
        tests:
          - not_null
```

Run dbt validations:
```bash
dbt run --select consent_records
dbt test --select consent_records
```

---

### 6. ML Workflows
Integrate validation + explainability.  
**Artifact**: [MLflow](https://github.com/mlflow/mlflow) + [SHAP](https://github.com/slundberg/shap).  

```python
import mlflow, shap
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=4, random_state=42)
with mlflow.start_run():
    model = RandomForestClassifier().fit(X, y)
    mlflow.sklearn.log_model(model, "churn_model")
    mlflow.log_metric("accuracy", model.score(X, y))
```

---

### 7. Data Pipelines
Embed trust checks into DAGs.  
**Artifact**: [Apache Airflow](https://github.com/apache/airflow) + Great Expectations.  

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from great_expectations.dataset import PandasDataset

def ingest_data():
    df = pd.read_csv("user_events.csv")
    dataset = PandasDataset(df)
    result = dataset.expect_column_values_to_not_be_null("event_id")
    with open("pipeline_validation.json", "a") as f:
        f.write(str(result))

with DAG("data_trust_pipeline", start_date=datetime(2025,1,1), schedule_interval="@daily") as dag:
    ingest_task = PythonOperator(task_id="ingest_and_validate", python_callable=ingest_data)
```

---

### 8. Dashboards & Reports
Visualize metrics with lineage.  
**Artifact**: [Metabase](https://github.com/metabase/metabase) + [OpenLineage](https://github.com/OpenLineage/OpenLineage).  

```python
from openlineage.client import OpenLineageClient
from openlineage.client.run import RunEvent, RunState, Run, Job, Dataset
from datetime import datetime

# Initialize OpenLineage client
client = OpenLineageClient(url="http://localhost:5000", api_key="")

# Define a job and dataset
job = Job(namespace="dte.trust.dashboard", name="user_events_pipeline")
dataset = Dataset(namespace="dte.trust.dashboard", name="user_events")

# Create lineage event
event = RunEvent(
    eventType=RunState.COMPLETE,
    eventTime=datetime.utcnow().isoformat(),
    run=Run(runId="1234-5678-90"),
    job=job,
    inputs=[dataset],
    outputs=[dataset]
)

# Emit lineage event
client.emit(event)

print("Lineage event emitted to OpenLineage for user_events_pipeline")


---

### 9. Certification (Practical, Non-Regulatory)
Automated trust checks and evidence packs for **risk-tiered assurance** (not legal compliance).  
**Artifact**: Great Expectations + [DataHub](https://github.com/datahub-project/datahub).  

---

### 10. Evaluations, Profiling & Confidence Indicators
Quantify trust levels with transparent metrics.  
**Artifact**: [YData Profiling](https://github.com/ydataai/ydata-profiling).  

---

## Data Contracts: Shift-Left Trust at Ingestion

Traditional governance tries to “fix” data **after** it hits the warehouse. By then, it’s too late. **Shift-left** means enforcing standards **at ingestion**, not retroactively in BI tools or catalogs. This ensures quality from the start and prevents downstream breakage.

**Shift-left enforcement pattern (InfoLibrarian example)**  
✅ Enforce **schema validation at ingestion**  
✅ Apply **DQ rules before data hits pipelines**  
✅ Track **SLA and lineage from the start**  
✅ Catch **contract violations** before they cascade downstream

**Anatomy of a Data Contract (example)**  
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

**Open-source enforcement at ingestion**  
- **jsonschema** validation in a lightweight Python service (e.g., API, Kafka consumer)  
- **Great Expectations** rules executed pre-landing  
- **Registry** (git-backed) for versioned contracts

```python
# validate_contract.py: jsonschema + Great Expectations at ingestion
import json, datetime
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from great_expectations.dataset import PandasDataset
import pandas as pd

CONTRACT = json.load(open("contracts/customer_orders.json"))

def validate_event(event: dict) -> bool:
    # 1) Schema validation
    validate(instance=event, schema={"type": "object", "properties": {
        "order_id": {"type": "string"},
        "customer_id": {"type": "string"},
        "order_date": {"type": "string", "format": "date"},
        "total": {"type": "number", "minimum": 0}
    }, "required": ["order_id", "customer_id", "order_date", "total"]})

    # 2) DQ rules (shift-left)
    if datetime.date.fromisoformat(event["order_date"]) > datetime.date.today():
        raise ValueError("order_date must not be in future")

    df = pd.DataFrame([event])
    ds = PandasDataset(df)
    assert ds.expect_column_values_to_not_be_null("order_id")["success"]
    return True
```

```bash
# Run ingestion-time checks
python validate_contract.py < sample_event.json
```

**dbt + Contracts (warehouse guardrails)**  
Even with shift-left, keep **defense-in-depth** with dbt tests that mirror the contract.

```yaml
# models/schema.yml (contract-aligned tests)
version: 2
models:
  - name: customer_orders
    description: "Customer orders aligned to data contract"
    columns:
      - name: order_id
        tests: [not_null, unique]
      - name: customer_id
        tests: [not_null]
      - name: order_date
        tests:
          - not_null
      - name: total
        tests:
          - not_null
          - accepted_values:
              values: [">=0"]   # implement as custom test macro
```

---

## Notes for Contributors

- **Extend Artifacts**: Fork and adapt artifacts for your own use cases.  
- **Alignment with DTE**: Ensure contributions align with manifesto principles: transparency, reliability, interoperability.  
- **Vendor Neutral**: Use open-source tools; avoid vendor lock-in.  
- **Collaborate**: Propose new use cases via Issues before submitting PRs.  

---

## License
MIT License — see [LICENSE.md](../LICENSE.md).

---

## Acknowledgments
The DTE Trust Dashboard and these use cases are cornerstones of the Data Trust Manifesto, driving a collaborative, engineering-first approach to trusted data systems. Thanks to the DTE community for inspiring and contributing to the #DTERevolution.  

#DTERevolution
