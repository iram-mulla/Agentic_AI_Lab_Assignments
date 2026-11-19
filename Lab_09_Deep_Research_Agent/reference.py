"""Deep research evidence synthesis reference."""
QUESTION = "What are the demonstrated benefits and limitations of RAG for domain QA?"

SOURCES = [
    {"id": "S1", "type": "peer-reviewed paper", "date": "2026-02", "claim": "RAG reduces hallucination by 41% on domain QA.", "evidence": "200 held-out medical questions.", "limitation": "Small, single-domain evaluation.", "quality": "peer-reviewed"},
    {"id": "S2", "type": "vendor engineering blog", "date": "2026-04", "claim": "RAG improves support-ticket QA accuracy by 35%.", "evidence": "Internal A/B test over 10,000 tickets.", "limitation": "Vendor-funded, no independent replication.", "quality": "vendor"},
    {"id": "S3", "type": "independent benchmark", "date": "2026-05", "claim": "RAG adds 200-400ms latency per query.", "evidence": "Five open-source RAG pipelines.", "limitation": "Latency varies with index size.", "quality": "independent benchmark"},
]

def build_evidence_table():
    return SOURCES

def compare(sources):
    agreements = ["S1 and S2 both report accuracy or factuality improvements."]
    conflicts = ["S3 identifies latency overhead absent from S1 and S2; this is a gap, not a direct contradiction."]
    gaps = ["No source reports non-English domain QA performance."]
    return {"agreements": agreements, "conflicts": conflicts, "gaps": gaps}

def synthesize(sources, comparison):
    lines = [f"[{row['id']}] {row['claim']}" for row in sources]
    lines.extend(f"[S1,S2] {item}" for item in comparison["agreements"])
    lines.extend(f"[S1,S2,S3] {item}" for item in comparison["conflicts"])
    lines.extend(f"[gap] {item}" for item in comparison["gaps"])
    return lines

if __name__ == "__main__":
    table = build_evidence_table()
    comparison = compare(table)
    print("\n".join(synthesize(table, comparison)))
