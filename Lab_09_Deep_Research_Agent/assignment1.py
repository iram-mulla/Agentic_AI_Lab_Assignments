sources = [
    {"id": "S1", "claim": "RAG reduces hallucination by 41%", "evidence": "200 held-out medical questions", "limitation": "small, single-domain evaluation", "quality": "peer-reviewed"},
    {"id": "S4", "claim": "RAG shows no measurable hallucination improvement", "evidence": "500 questions across two enterprise documents", "limitation": "different document quality and retrieval setup", "quality": "independent benchmark"},
]

def compare(sources):
    return {
        "type": "direct contradiction",
        "sources": ["S1", "S4"],
        "reason": "different domains, datasets, retrieval setups, and evaluation methodologies",
    }

def synthesize(sources, conflict):
    return [f"[{row['id']}] {row['claim']} Evidence: {row['evidence']}. Limitation: {row['limitation']}." for row in sources] + [f"[conflict] {conflict['reason']}."]

conflict = compare(sources)
print({"comparison": conflict, "synthesis": synthesize(sources, conflict)})
