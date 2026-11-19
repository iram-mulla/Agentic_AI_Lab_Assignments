tiers = {"peer-reviewed": 3, "independent benchmark": 2, "vendor": 1}
sources = [
    {"id": "S1", "claim": "RAG reduces hallucination", "quality": "peer-reviewed"},
    {"id": "S2", "claim": "RAG is ineffective for this task", "quality": "vendor"},
]
ranked = sorted(sources, key=lambda s: tiers[s["quality"]], reverse=True)
source_ids = [source["id"] for source in ranked]
print({
    "ranked_claims": ranked,
    "quality_tiers": tiers,
    "synthesis": f"Synthesis leans toward {ranked[0]['id']} because it is peer-reviewed. The lower-tier {ranked[-1]['id']} claim is disclosed and down-weighted, not discarded.",
    "trace": source_ids,
})
