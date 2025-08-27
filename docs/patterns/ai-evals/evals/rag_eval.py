#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RAG/GraphRAG evaluation utilities.
Measures exact-match accuracy (EM) and citation coverage.
"""
import json
from pathlib import Path
from typing import List, Dict
from rapidfuzz import fuzz

def has_citation(answer: str, source_ids: List[str]) -> bool:
    return any(sid in answer for sid in source_ids)

def exact_match(pred: str, gold: str) -> float:
    return fuzz.ratio((pred or '').strip().lower(), (gold or '').strip().lower()) / 100.0

def evaluate_batch(examples: List[Dict]) -> Dict[str, float]:
    em_scores, cit_hits = [], []
    for ex in examples:
        em = exact_match(ex.get("answer",""), ex.get("gold",""))
        src_ids = [s.get("id","") for s in ex.get("sources",[])]
        cit = has_citation(ex.get("answer",""), src_ids)
        em_scores.append(em)
        cit_hits.append(1.0 if cit else 0.0)
    em_mean = sum(em_scores)/len(em_scores) if em_scores else 0.0
    citation_coverage = sum(cit_hits)/len(cit_hits) if cit_hits else 0.0
    return {"em_mean": round(em_mean, 4), "citation_coverage": round(citation_coverage, 4)}

def main(in_path: str, out_path: str):
    data = [json.loads(l) for l in Path(in_path).read_text().splitlines() if l.strip()]
    metrics = evaluate_batch(data)
    Path(out_path).write_text(json.dumps(metrics, indent=2))
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--golden", default="evals/datasets/golden_set.jsonl")
    ap.add_argument("--out", default="artifacts/evidence/rag_metrics.json")
    args = ap.parse_args()
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    main(args.golden, args.out)