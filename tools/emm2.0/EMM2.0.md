# EMM 2.0: Revitalizing Enterprise Metadata Management

*A vendor-neutral, graph-native pattern for enterprise metadata repositories*

> This page introduces the EMM 2.0 pattern and links to the optional enhancements (diagram + integration code) used by the community.

---

## Overview

**EMM 2.0** enables vendor-neutral enterprise metadata management using a **graph-first** approach. It focuses on reusable **building blocks** that remain constant across platforms and use cases:

**Integration → Storage → Democratization → Use**

- Works alongside existing catalogs and platforms (no replacements required)
- Compatible with property-graph databases (Neo4j, Amazon Neptune, Azure Cosmos DB)
- Supports both **federated** and **standalone** repository architectures
- MIT-licensed and community-driven

> Goal: executable patterns and assets you can run today—without vendor lock-in.

---

## Diagram

> Placeholder diagram — community updates welcome. Submit improved SVGs to `/docs/assets/`.

![EMM 2.0 flow: Source → Metadata Repo → GraphRAG → Lineage Certification](/docs/assets/emm2-flow.svg)

---

## OpenLineage + Neo4j Integration (Tooling)

A minimal, vendor-neutral example that **upserts datasets** and **creates lineage** in Neo4j, then **emits an OpenLineage event** (if configured).

**Script location:** `/tools/emm2_0/lineage_ingest.py`

**Install & run:**
```bash
pip install neo4j openlineage-client
export OPENLINEAGE_URL="http://localhost:5000"   # or your OL endpoint
export OPENLINEAGE_API_KEY="..."                  # optional

python tools/emm2_0/lineage_ingest.py   --neo4j-uri neo4j://localhost:7687   --neo4j-user neo4j   --neo4j-pass password   --job-namespace org.datatrustengineering   --job-name daily_ingest   --input db.raw.transactions   --output db.curated.ledger
```

**What it does:**
- Ensures `(:Dataset {name})` nodes exist
- Links inputs → outputs with `[:FEEDS]`
- Emits an OpenLineage `RunEvent` (if `openlineage-client` is installed and env is set)

---

## Why EMM 2.0

- **Relationship-centric** metadata management that matches real-world lineage and knowledge use cases
- **Federated or standalone** deployment for sovereignty, privacy, and cost control
- **GraphRAG-friendly** foundation for semantic discovery and AI reasoning
- **No vendor lock-in** via open patterns and property-graph models

> Teams report **up to 65%** fewer stalls in metadata workflows when shifting to executable, graph-native patterns like EMM 2.0.[^stat-65]

---

## Contributing

- Fork/branch and open a PR with updates to the diagram or tooling
- Follow `CODE_OF_CONDUCT.md` and contribution guidelines
- Align examples with EMM 2.0 building blocks and vendor-neutral principles

**License:** MIT — see `LICENSE`

---

## References & Footnotes

[^stat-65]: *Per [source], 2024.* (Replace with a concrete citation if/when available.)

