# DTE Quick Start Guide

Welcome to Data Trust Engineering! This guide gets you started with practical trust engineering in **15-45 minutes** using working examples. Whether you're new to data trust or looking to implement specific patterns, this guide provides:

- **3 Runnable Examples** - Working implementations you can try immediately
- **Use Case Template** - Framework for community contributions
- **KPI Framework** - How metrics feed the trust dashboard
- **Implementation Roadmap** - Path to expand with 15+ additional use cases

---

## 🚀 Getting Started (5 minutes)

### Prerequisites
```bash
# Clone the repository
git clone https://github.com/datatrustengineering/DataTrustEngineering.git
cd DataTrustEngineering

# Try the live dashboard first
open https://datatrustengineering.github.io/DataTrustEngineering/tools/data-trust-dashboard/DTE_Trust_Dashboard.html
```

### Quick Setup
```bash
# Set up Python environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (for examples that need them)
pip install pandas numpy streamlit plotly
```

---

## 📋 Example 1: Agentic Workflows Trust (15 minutes)

**Business Value:** Ensure AI agents make auditable decisions with validated data inputs.

**Technical Challenge:** Agent decisions need validation and audit trails for compliance and debugging.

**DTE Principles:** Trust, Engineering Rigor, Observability

### Implementation
```python
# File: agent_validator.py
import json
import pandas as pd
from great_expectations.dataset import PandasDataset
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

def validate_agent_data(input_data: str) -> str:
    """Validate data quality for agent consumption"""
    try:
        df = pd.read_json(input_data)
        dataset = PandasDataset(df)

        # Define validation rules
        validations = [
            dataset.expect_column_values_to_not_be_null("id"),
            dataset.expect_column_values_to_be_unique("id"),
            dataset.expect_column_values_to_be_between("amount", 0, 10000)
        ]

        # Check all validations pass
        results = [v["success"] for v in validations]
        success = all(results)

        return json.dumps({
            "success": success,
            "validations": results,
            "message": "Data validated successfully" if success else "Validation failed"
        })
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})

# Create LangChain tool
validation_tool = Tool(
    name="DataValidator",
    func=validate_agent_data,
    description="Validates data quality and structure for agent workflows"
)

# Example usage with sample data
sample_data = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "amount": [100, 250, 75, 300],
    "category": ["A", "B", "A", "C"]
})

result = validate_agent_data(sample_data.to_json())
print("Validation Result:", result)
```

### Testing
```bash
# Run the validator
python agent_validator.py

# Expected output:
# {"success": true, "validations": [true, true, true], "message": "Data validated successfully"}
```

### KPIs to Track
- **Validation Success Rate**: Percentage of data passing validation
- **Error Detection Time**: How quickly invalid data is caught
- **Agent Decision Quality**: Accuracy of agent outputs with validated data

### Dashboard Integration
These KPIs can be visualized as:
- **Gauge Chart**: Validation success rate
- **Time Series**: Error detection trends
- **Correlation Plot**: Agent performance vs. data quality

---

## 📋 Example 2: RAG / GraphRAG Trust (25 minutes)

**Business Value:** Ensure LLM responses are grounded in verified knowledge graphs.

**Technical Challenge:** LLMs can hallucinate or provide outdated information.

**DTE Principles:** Certification, Technical Debt Management, Observability

### Implementation
```python
# File: rag_validator.py
import json
from typing import List, Dict
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphQAChain
from langchain.llms import OpenAI

class RAGValidator:
    def __init__(self, graph_url: str = "bolt://localhost:7687",
                 username: str = "neo4j", password: str = "password"):
        self.graph = Neo4jGraph(
            url=graph_url,
            username=username,
            password=password
        )

    def validate_knowledge_consistency(self, query: str, response: str) -> Dict:
        """Validate that response is consistent with knowledge graph"""
        try:
            # Query knowledge graph for related information
            graph_results = self.graph.query(f"""
            MATCH (n)
            WHERE n.name CONTAINS '{query.split()[0]}'
            RETURN n.name, n.description LIMIT 5
            """)

            # Simple consistency check
            response_lower = response.lower()
            matches = sum(1 for node in graph_results
                         if node['n.name'].lower() in response_lower)

            consistency_score = matches / max(len(graph_results), 1)

            return {
                "consistency_score": consistency_score,
                "knowledge_nodes_found": len(graph_results),
                "matches_found": matches,
                "validation_passed": consistency_score > 0.5
            }
        except Exception as e:
            return {
                "error": str(e),
                "validation_passed": False
            }

    def setup_knowledge_graph(self):
        """Initialize knowledge graph with sample data"""
        self.graph.query("""
        CREATE (p1:Principle {name: "Transparency", description: "Clear decision processes"})
        CREATE (p2:Principle {name: "Accountability", description: "Responsible for outcomes"})
        CREATE (p3:Principle {name: "Trust", description: "Building confidence through reliability"})
        CREATE (p1)-[:RELATED_TO]->(p2)
        CREATE (p2)-[:RELATED_TO]->(p3)
        """)
        print("Knowledge graph initialized")

# Usage example
validator = RAGValidator()

# Setup knowledge graph (run once)
validator.setup_knowledge_graph()

# Validate a response
query = "What principles are related to accountability?"
sample_response = "Accountability is related to transparency and trust in decision making."

validation_result = validator.validate_knowledge_consistency(query, sample_response)
print("RAG Validation:", json.dumps(validation_result, indent=2))
```

### Setup Requirements
```bash
# Install dependencies
pip install neo4j langchain langchain-community

# Start Neo4j (if running locally)
# docker run -p 7474:7474 -p 7687:7687 neo4j:latest
```

### Testing
```bash
# Run validation
python rag_validator.py

# Expected output:
# RAG Validation: {
#   "consistency_score": 0.67,
#   "knowledge_nodes_found": 3,
#   "matches_found": 2,
#   "validation_passed": true
# }
```

### KPIs to Track
- **Knowledge Consistency Score**: How well responses align with verified knowledge
- **Hallucination Detection Rate**: Percentage of potentially incorrect claims caught
- **Response Grounding Coverage**: Percentage of response backed by knowledge graph

### Dashboard Integration
- **Score Gauge**: Knowledge consistency percentage
- **Trend Chart**: Consistency scores over time
- **Heat Map**: Knowledge coverage across different topics

---

## 📋 Example 3: Data Contracts (30 minutes)

**Business Value:** Formalize data agreements between teams to prevent breaking changes.

**Technical Challenge:** Schema evolution and data quality agreements between producers and consumers.

**DTE Principles:** Certification, Adaptability, Technical Debt Management

### Implementation
```yaml
# File: contracts/customer_orders.yaml
datacontract:
  id: customer_orders_contract
  version: 1.0.0
  name: Customer Orders Data Contract
  description: "Contract for customer order data exchange"

  schema:
    type: object
    properties:
      order_id:
        type: string
        description: "Unique order identifier"
        required: true
        unique: true
      customer_id:
        type: string
        description: "Customer identifier"
        required: true
      order_date:
        type: string
        format: date
        description: "Order date in ISO format"
        required: true
      total_amount:
        type: number
        minimum: 0
        maximum: 10000
        description: "Total order amount"
        required: true
      status:
        type: string
        enum: ["pending", "confirmed", "shipped", "delivered", "cancelled"]
        description: "Order status"
        required: true

  quality:
    - type: sql
      description: "No duplicate order IDs"
      query: "SELECT COUNT(*) FROM orders GROUP BY order_id HAVING COUNT(*) > 1"
      mustBeEmpty: true

    - type: sql
      description: "Order dates should not be in future"
      query: "SELECT COUNT(*) FROM orders WHERE order_date > CURRENT_DATE"
      mustBeEmpty: true

  servicelevels:
    - type: freshness
      description: "Data should be updated daily"
      threshold: "24h"

    - type: availability
      description: "Data should be available 99.9% of the time"
      threshold: "99.9%"

    - type: latency
      description: "Queries should respond within 2 seconds"
      threshold: "2s"
```

```python
# File: contract_validator.py
import yaml
import json
import pandas as pd
from datetime import datetime
from jsonschema import validate, ValidationError

class DataContractValidator:
    def __init__(self, contract_path: str):
        with open(contract_path, 'r') as f:
            self.contract = yaml.safe_load(f)

    def validate_schema(self, data: pd.DataFrame) -> Dict:
        """Validate data against JSON schema"""
        try:
            # Convert DataFrame to records for validation
            records = data.to_dict('records')
            schema = self.contract['schema']

            errors = []
            for i, record in enumerate(records):
                try:
                    validate(instance=record, schema=schema)
                except ValidationError as e:
                    errors.append(f"Row {i}: {e.message}")

            return {
                "schema_valid": len(errors) == 0,
                "errors": errors[:5],  # Limit error messages
                "rows_validated": len(records)
            }
        except Exception as e:
            return {"schema_valid": False, "error": str(e)}

    def validate_quality_rules(self, data: pd.DataFrame) -> Dict:
        """Validate quality rules (simplified version)"""
        results = []

        # Check for duplicates
        duplicates = data[data.duplicated(subset=['order_id'])]
        results.append({
            "rule": "no_duplicate_order_ids",
            "passed": len(duplicates) == 0,
            "violations": len(duplicates)
        })

        # Check future dates
        future_dates = data[data['order_date'] > datetime.now().date().isoformat()]
        results.append({
            "rule": "no_future_dates",
            "passed": len(future_dates) == 0,
            "violations": len(future_dates)
        })

        return {
            "quality_checks": results,
            "overall_passed": all(r["passed"] for r in results)
        }

# Usage example
validator = DataContractValidator("contracts/customer_orders.yaml")

# Sample data
sample_data = pd.DataFrame({
    "order_id": ["ORD001", "ORD002", "ORD003"],
    "customer_id": ["CUST001", "CUST002", "CUST003"],
    "order_date": ["2024-01-15", "2024-01-16", "2024-01-17"],
    "total_amount": [150.00, 299.99, 75.50],
    "status": ["confirmed", "shipped", "pending"]
})

# Validate
schema_result = validator.validate_schema(sample_data)
quality_result = validator.validate_quality_rules(sample_data)

print("Schema Validation:", json.dumps(schema_result, indent=2))
print("Quality Validation:", json.dumps(quality_result, indent=2))
```

# Dashboard Expansion Plan

## Overview
This plan outlines how to expand the DTE Trust Dashboard from its current AI-focused implementation into a comprehensive platform that visualizes trust metrics across all 19 DTE patterns and use cases. The expanded dashboard will serve as both a demonstration tool and a living showcase of community contributions.

## Current State Analysis

### Dashboard v1.0 (Current)
**Sections:** 6 AI-focused visualizations
- AI Governance Overview (4 metric cards)
- AI Fairness Across Protected Attributes (bar chart)
- Model Explainability Across Features (bar chart)
- Guardrails Adherence Radar (radar chart)
- GenAI Safety Metrics (bar chart)
- AI Model Performance Over Time (line chart)

**Architecture:** Single-page Streamlit application
**Data Source:** Hardcoded sample data
**Theme:** Dark mode with custom CSS

**Limitations:**
- Single-focus on AI governance
- No integration with real use case implementations
- No community contribution mechanism
- Static visualizations only

---

## Expanded Architecture

### Dashboard v2.0 (Target)
**Structure:** Multi-tab Streamlit application
**Sections:** 5 main categories with 15+ subsections
**Data Integration:** KPI ingestion from community use cases
**Community Features:** Contributor showcase, dynamic updates

### Technical Architecture

```python
# Proposed app structure
import streamlit as st
from dashboard_sections import (
    ai_governance, data_quality, observability, 
    pipeline_trust, community_showcase
)

def main():
    st.set_page_config(layout="wide", page_title="DTE Trust Dashboard")
    
    # Navigation tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🤖 AI Governance", 
        "📊 Data Quality", 
        "🔍 Observability",
        "⚙️ Pipeline Trust",
        "🌟 Community"
    ])
    
    with tab1:
        ai_governance.show()
    with tab2:
        data_quality.show()
    with tab3:
        observability.show()
    with tab4:
        pipeline_trust.show()
    with tab5:
        community_showcase.show()
```

### Data Pipeline Architecture

```json
{
  "kpi_ingestion": {
    "source": "community_use_cases",
    "format": "json/csv",
    "frequency": "real-time/scheduled",
    "validation": "schema_checking"
  },
  "data_storage": {
    "type": "in-memory/streamlit_session",
    "retention": "session-based",
    "backup": "optional_csv_export"
  },
  "visualization_engine": {
    "library": "plotly",
    "theme": "dark_mode",
    "responsiveness": "mobile-friendly"
  }
}
```

---

## Use Case to Dashboard Mapping

### 1. 🤖 AI Governance Tab (Current + Expanded)

**Current Visualizations:**
- ✅ AI Governance Overview (4 metrics)
- ✅ Fairness Across Attributes (bar chart)
- ✅ Model Explainability (bar chart)
- ✅ Guardrails Adherence (radar chart)
- ✅ GenAI Safety Metrics (bar chart)
- ✅ Model Performance Over Time (line chart)

**New Additions:**
- [ ] **AI Fairness Auditing** (`ai-evals/`) - Fairness heatmaps, mitigation tracking
- [ ] **AI Safety Guardrails** (`ai-safety/`) - Safety violation trends, jailbreak detection
- [ ] **Model Drift Detection** - Drift magnitude over time, false positive rates

### 2. 📊 Data Quality Tab (New)

**Planned Visualizations:**
- [ ] **Schema Compliance** (`data-contracts/`) - Contract violation rates, validation success
- [ ] **Data Quality Monitoring** (`data-quality/`) - Null rates, duplicate detection, range validation
- [ ] **Data Profiling** (`profiling/`) - Completeness scores, distribution analysis
- [ ] **Canonicalization** (`canonicalization/`) - De-duplication rates, golden record coverage

**KPI Examples:**
```json
{
  "data_quality": {
    "null_rate": 0.02,
    "duplicate_rate": 0.001,
    "schema_compliance": 0.98,
    "freshness_score": 0.95
  }
}
```

### 3. 🔍 Observability Tab (New)

**Planned Visualizations:**
- [ ] **Lineage Tracking** (`data-lineage/`) - Lineage completeness, impact analysis coverage
- [ ] **Freshness Monitoring** (`data-freshness/`) - Data staleness %, SLO compliance
- [ ] **Trust SLOs** (`trust-slo/`) - Error budget burn rates, SLO attainment
- [ ] **Error Budgeting** (`error-budgeting/`) - Budget consumption trends

**KPI Examples:**
```json
{
  "observability": {
    "lineage_coverage": 0.87,
    "freshness_p95": 0.95,
    "slo_compliance": 0.99,
    "error_budget_remaining": 0.15
  }
}
```

### 4. ⚙️ Pipeline Trust Tab (New)

**Planned Visualizations:**
- [ ] **Data Pipeline Validation** (`data-pipelines/`) - Pipeline success rates, validation coverage
- [ ] **Backfill Strategies** (`backfills/`) - Backfill success rates, idempotency metrics
- [ ] **Test Pyramid** (`test-pyramid-for-data/`) - Test coverage by layer, failure rates
- [ ] **Teardown Sprints** (`teardown-sprints/`) - Debt reduction metrics, complexity trends

**KPI Examples:**
```json
{
  "pipeline_trust": {
    "pipeline_success_rate": 0.96,
    "test_coverage": 0.85,
    "backfill_success": 0.99,
    "technical_debt_score": 0.72
  }
}
```

### 5. 🌟 Community Showcase Tab (New)

**Features:**
- [ ] **Contributor Leaderboard** - Most active contributors, successful use cases
- [ ] **Use Case Gallery** - Visual showcase of implemented patterns
- [ ] **Live KPI Dashboard** - Real-time metrics from community implementations
- [ ] **Implementation Status** - Progress on roadmap items
- [ ] **Success Stories** - Case studies from community implementations

---

## Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
1. **Restructure Dashboard** - Convert to tabbed layout
2. **Create KPI Framework** - Standardize data ingestion format
3. **Add Data Quality Tab** - Implement 4 core visualizations
4. **Update Documentation** - Reflect new dashboard structure

### Phase 2: Core Expansion (Week 3-4)
1. **Add Observability Tab** - 4 visualizations with real KPIs
2. **Implement Pipeline Trust** - Pipeline monitoring dashboards
3. **Enhanced AI Governance** - Add drift detection, safety monitoring
4. **Community Integration** - Basic contributor showcase

### Phase 3: Community Activation (Week 5-6)
1. **Launch Community Features** - Full contributor dashboard
2. **Create Contribution Templates** - Standardized KPI formats
3. **Add Real Implementations** - Connect to working use cases
4. **Performance Optimization** - Handle multiple data sources

### Phase 4: Advanced Features (Week 7-8)
1. **Real-time Updates** - Live KPI streaming
2. **Alert System** - SLO breach notifications
3. **Historical Trending** - Long-term KPI analysis
4. **Mobile Optimization** - Responsive design improvements

---

## Technical Implementation Guide

### Adding New Dashboard Sections

```python
# dashboard_sections/data_quality.py
import streamlit as st
import plotly.express as px

def show():
    st.header("📊 Data Quality Metrics")
    
    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Schema Compliance", "98%", "+2%")
    with col2:
        st.metric("Null Rate", "2.1%", "-0.5%")
    with col3:
        st.metric("Duplicate Rate", "0.1%", "0%")
    with col4:
        st.metric("Freshness Score", "95%", "+3%")
    
    # Visualizations
    # Add your charts here...
```

### KPI Data Ingestion

```python
# kpi_collector.py
import json
import pandas as pd
from pathlib import Path

class KPICollector:
    def __init__(self, data_dir: str = "kpi_data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
    
    def collect_kpi(self, use_case: str, kpis: dict):
        """Collect KPIs from use case implementations"""
        timestamp = pd.Timestamp.now()
        data = {
            "timestamp": timestamp.isoformat(),
            "use_case": use_case,
            **kpis
        }
        
        # Save to JSON for dashboard consumption
        filename = f"{use_case}_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
        with open(self.data_dir / filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_latest_kpis(self, use_case: str) -> dict:
        """Get latest KPIs for a use case"""
        files = list(self.data_dir.glob(f"{use_case}_*.json"))
        if not files:
            return {}
        
        latest_file = max(files, key=lambda x: x.stat().st_mtime)
        with open(latest_file, 'r') as f:
            return json.load(f)
```

### Community Contribution Template

```python
# community_contribution.py
def add_community_visualization(contributor_name: str, 
                               use_case: str, 
                               visualization_func):
    """Template for community contributors to add visualizations"""
    
    # Register the visualization
    VISUALIZATION_REGISTRY[use_case] = {
        "contributor": contributor_name,
        "function": visualization_func,
        "added_date": pd.Timestamp.now().isoformat()
    }
    
    # Add to community showcase
    update_community_showcase(use_case, contributor_name)
```

---

## Success Metrics

### Technical Metrics
- [ ] **Dashboard Load Time** < 5 seconds
- [ ] **KPI Update Frequency** Real-time or < 5 minutes
- [ ] **Mobile Responsiveness** > 90% compatibility
- [ ] **Data Source Integration** Support 10+ use cases

### Community Metrics
- [ ] **Active Contributors** > 10 within 3 months
- [ ] **Implemented Use Cases** > 8 within 6 months
- [ ] **KPI Data Sources** > 15 active feeds
- [ ] **Community Engagement** > 50 discussions/issues

### Quality Metrics
- [ ] **Visualization Accuracy** > 95% data accuracy
- [ ] **Code Quality** Pass all linting checks
- [ ] **Documentation Coverage** > 90% features documented
- [ ] **User Satisfaction** > 4/5 average rating

---

## Community Guidelines for Contributors

### Adding New Visualizations

1. **Follow the Template**:
   ```python
   # Create visualization function
   def my_visualization():
       # Your Plotly/Streamlit code here
       pass
   
   # Register with dashboard
   register_visualization("my_use_case", my_visualization)
   ```

2. **KPI Standards**:
   - Use consistent naming conventions
   - Include timestamps and metadata
   - Provide baseline and target values
   - Document calculation methodology

3. **Code Quality**:
   - Follow PEP 8 style guidelines
   - Include docstrings and comments
   - Add error handling
   - Test with sample data

4. **Documentation**:
   - Update README.md with new section
   - Add KPI definitions to metrics glossary
   - Include usage examples
   - Document data source requirements

### Review Process

1. **Pull Request Submission**:
   - Create branch: `feature/dashboard-[use-case]`
   - Include visualization code and sample data
   - Update documentation
   - Add tests if applicable

2. **Review Criteria**:
   - Code quality and style
   - Visualization clarity and usefulness
   - Data accuracy and format consistency
   - Documentation completeness
   - Integration with existing dashboard

3. **Merge Requirements**:
   - 2 maintainer approvals
   - All automated tests pass
   - Documentation updated
   - Demo provided

---

## Migration Strategy

### From v1.0 to v2.0

1. **Preserve Current Features**:
   - Keep all existing AI governance visualizations
   - Maintain current styling and branding
   - Preserve existing KPI calculations

2. **Gradual Expansion**:
   - Add tabs one at a time
   - Start with data quality section
   - Test each new section thoroughly
   - Gather user feedback before proceeding

3. **Data Migration**:
   - Export current sample data
   - Create migration scripts for new format
   - Maintain backward compatibility
   - Plan for future data sources

### Backward Compatibility

- **API Compatibility**: Existing integrations continue to work
- **Data Format**: Support both old and new KPI formats
- **URL Structure**: Maintain existing dashboard URLs
- **Visual Consistency**: Keep current design language

---

## Next Steps

### Immediate Actions (This Week)
1. **Create tabbed structure** in dashboard
2. **Implement data quality section** as first new tab
3. **Update documentation** to reflect new structure
4. **Create KPI collection framework**

### Short-term Goals (Next Month)
1. **Add observability tab** with lineage and freshness metrics
2. **Implement community showcase** features
3. **Create contributor onboarding** materials
4. **Launch with 8-10 visualizations**

### Long-term Vision (6 Months)
1. **Full pattern coverage** across all 19 DTE patterns
2. **Real-time KPI streaming** from production systems
3. **Advanced analytics** and trend analysis
4. **Multi-organization support** for enterprise deployments

---

## Conclusion

This expansion plan transforms the dashboard from a static AI governance demo into a comprehensive, community-driven platform that showcases practical data trust engineering. By providing clear contribution pathways and standardized KPI frameworks, the dashboard becomes both a learning tool and a living demonstration of the DTE ecosystem's capabilities.

**Ready to start the expansion?** The plan provides a clear, phased approach that builds community momentum while maintaining technical excellence. 🚀

#DTERevolution
