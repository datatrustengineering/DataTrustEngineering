# Data Debt Ledger

A lightweight register of **known technical/data debt** across pipelines, models, and contracts.  
Debt is tracked as **items with “principal” (effort to fix) and “interest” (ongoing cost)** so teams can prioritize repayment.  

This file is intended to live in Git, evolve with PRs, and link to GitHub Issues for detailed work.

---

## How to Use
1. Add new debt items here (or via GitHub Issues with label `debt/*`).
2. Record **impact**, **principal (fix cost)**, **interest (recurring cost)**, and a **due date** if critical.
3. Reference related use cases (contracts, lineage, dashboards, ML workflows).
4. Close/remove items once resolved.

---

## Debt Categories
- **Schema Drift**: Contracts or models not aligned with actual data.
- **Pipeline Fragility**: Jobs not idempotent, fail silently, or need manual restarts.
- **Observability Gaps**: Missing trust signals (freshness, nulls, lineage, drift).
- **Duplicate / Conflicting Entities**: Two sources of truth for the same KPI/domain.
- **Orphan Assets**: Unused tables, models, or reports inflating complexity.

---

## Ledger

| ID  | Item                            | Category            | Impact (Interest)                   | Principal (Fix Effort) | Due Date   | Status   | Notes / Links |
|-----|---------------------------------|---------------------|-------------------------------------|-------------------------|------------|----------|---------------|
| D-1 | Missing null checks on `customer_orders.total` | Schema Drift       | Risk of invalid revenue calc; manual reconciliation weekly | ~1 day | 2025-09-15 | Open     | [contracts/customer_orders.json](contracts/customer_orders.json) |
| D-2 | No lineage for `user_events` pipeline | Observability Gap  | Unknown blast radius on schema change; ~4h incident last month | ~2 days | Backlog   | Open     | Add OpenLineage emitter to DAG |
| D-3 | Duplicate KPIs: `revenue` in BI vs. ML | Conflicting Entities | Confusion in reporting; extra 2h/week debugging | ~3 days | 2025-10-01 | Open     | Needs canonical `gold.revenue` model |
| D-4 | Orphaned table `tmp_sales_2023` | Orphan Assets       | Storage + risk of misuse | ~0.5 day | 2025-08-31 | Closed   | Dropped in dbt cleanup |
| D-5 | Airflow DAG `inventory_sync` not idempotent | Pipeline Fragility | Backfills create duplicates; 1–2h manual fix monthly | ~2 days | 2025-09-30 | Open     | Add merge/upsert pattern |

---

## Minimal Metrics (Debt KPIs)
- **Contract violation rate** (% of events rejected at ingestion)  
- **Freshness p95** (minutes late vs SLA)  
- **Flaky test rate** (CI / dbt tests)  
- **Orphan asset %** (unused models/tables)  
- **Incident MTTR** (Mean Time to Recovery)  

---

## Notes
- Debt is not a failure; it’s a **budget**.  
- Prioritize repayment based on **interest cost vs. business value**.  
- Keep the ledger small and actionable — big, stale backlogs defeat the purpose.  

---

*#DTERevolution — Track debt, make it visible, and turn it into trust.*
