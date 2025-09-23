"""
EMM 2.0 — OpenLineage + Neo4j Integration
----------------------------------------
Drop this file in: /tools/emm2_0/lineage_ingest.py

Usage (example):
  export OPENLINEAGE_URL="http://localhost:5000"
  export OPENLINEAGE_API_KEY="...optional..."

  python lineage_ingest.py --neo4j-uri neo4j://localhost:7687         --neo4j-user neo4j --neo4j-pass password         --job-namespace "org.datatrustengineering"         --job-name "daily_ingest"         --input "db.raw.transactions"         --output "db.curated.ledger"

Notes:
- Requires: neo4j (Python driver), openlineage-client
- The OpenLineage event structure here is a minimal, vendor-neutral example.
"""

import argparse
import os
import sys
import uuid
from datetime import datetime, timezone
from typing import List

try:
    from neo4j import GraphDatabase
except ImportError:
    raise SystemExit("Missing dependency: neo4j. Install with `pip install neo4j`")

# OpenLineage is optional at runtime, but recommended.
_openlineage_available = True
try:
    from openlineage.client import OpenLineageClient
    from openlineage.client.run import RunEvent, RunState, Run, Job, Dataset, EventTime
except Exception:
    _openlineage_available = False


def neo4j_connect(uri: str, user: str, password: str):
    driver = GraphDatabase.driver(uri, auth=(user, password))
    return driver


def ensure_dataset(tx, name: str):
    # Ensure a Dataset node exists (idempotent-ish)
    tx.run(
        "MERGE (d:Dataset {name: $name}) "
        "ON CREATE SET d.createdAt = timestamp() ",
        name=name,
    )


def create_lineage(tx, source: str, target: str):
    tx.run(
        """
        MERGE (s:Dataset {name: $source})
          ON CREATE SET s.createdAt = timestamp()
        MERGE (t:Dataset {name: $target})
          ON CREATE SET t.createdAt = timestamp()
        MERGE (s)-[r:FEEDS]->(t)
          ON CREATE SET r.createdAt = timestamp()
          ON MATCH  SET r.lastSeenAt = timestamp()
        """,
        source=source,
        target=target,
    )


def emit_openlineage_event(job_namespace: str, job_name: str, inputs: List[str], outputs: List[str]):
    if not _openlineage_available:
        print("[warn] openlineage-client not available; skipping event emission.", file=sys.stderr)
        return

    client = OpenLineageClient.from_environment()

    run_id = uuid.uuid4()
    event_time = EventTime(datetime.now(timezone.utc).isoformat())

    job = Job(namespace=job_namespace, name=job_name)

    def _mk_dataset(name: str) -> Dataset:
        # This keeps it vendor-neutral. Use namespace if you need to segment systems.
        return Dataset(namespace=job_namespace, name=name)

    input_datasets = [_mk_dataset(n) for n in inputs]
    output_datasets = [_mk_dataset(n) for n in outputs]

    event = RunEvent(
        eventType=RunState.COMPLETE,  # or START, RUNNING, FAIL
        eventTime=event_time,
        run=Run(runId=str(run_id)),
        job=job,
        inputs=input_datasets,
        outputs=output_datasets,
        producer="https://github.com/datatrustengineering/DataTrustEngineering/tools/emm2_0",
    )

    client.emit(event)
    print(f"[ok] Emitted OpenLineage event runId={run_id} job={job_namespace}.{job_name}")


def main():
    parser = argparse.ArgumentParser(description="EMM 2.0 — OpenLineage + Neo4j Integration")
    parser.add_argument("--neo4j-uri", required=True)
    parser.add_argument("--neo4j-user", required=True)
    parser.add_argument("--neo4j-pass", required=True)
    parser.add_argument("--job-namespace", required=True)
    parser.add_argument("--job-name", required=True)
    parser.add_argument("--input", action="append", dest="inputs", default=[], help="Input dataset (repeatable)")
    parser.add_argument("--output", action="append", dest="outputs", default=[], help="Output dataset (repeatable)")

    args = parser.parse_args()

    # Connect to Neo4j
    driver = neo4j_connect(args.neo4j_uri, args.neo4j_user, args.neo4j_pass)
    print("[ok] Connected to Neo4j")

    # Upsert datasets and lineage relationships
    with driver.session() as session:
        for ds in set(args.inputs + args.outputs):
            session.execute_write(ensure_dataset, ds)

        for src in args.inputs:
            for dst in args.outputs:
                session.execute_write(create_lineage, src, dst)
                print(f"[ok] Linked {src} -> {dst}")

    # Emit an OpenLineage event (optional if client is available)
    try:
        emit_openlineage_event(
            job_namespace=args.job_namespace,
            job_name=args.job_name,
            inputs=args.inputs,
            outputs=args.outputs,
        )
    finally:
        driver.close()
        print("[ok] Closed Neo4j connection")


if __name__ == "__main__":
    main()
