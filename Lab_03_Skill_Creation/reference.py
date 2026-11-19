"""Reusable research-summary skill."""
SKILL_SPEC = {
    "name": "research_summary",
    "instructions": ["identify the main claim", "list supporting evidence", "note limitations", "write an undergraduate takeaway"],
    "constraints": ["never present a hedged claim as fact", "return limitation or 'not stated in source'"],
}

ARTICLE_A = {"title": "RAG Study", "text": "RAG reduced factual hallucination by 41%. The study used 200 held-out medical questions. The evaluation was small and domain-specific."}
ARTICLE_B = {"title": "Campus Wi-Fi", "text": "A campus Wi-Fi upgrade increased peak-hour throughput by 60%. Measurements covered two weeks in the library. The report does not include measurements from other buildings."}

def apply_research_summary_skill(article):
    sentences = [sentence.strip() for sentence in article["text"].split(".") if sentence.strip()]
    claim = sentences[0]
    evidence = next((sentence for sentence in sentences[1:] if any(word in sentence.lower() for word in ("used", "study", "measurement", "test", "percent", "%"))), "not stated in source")
    limitation = next((sentence for sentence in sentences if any(word in sentence.lower() for word in ("small", "does not include", "not include", "unclear", "may not"))), "not stated in source")
    return {"claim": claim, "evidence": evidence, "limitation": limitation, "takeaway": f"Undergraduate takeaway: {claim} -- verify before generalizing."}

if __name__ == "__main__":
    a = apply_research_summary_skill(ARTICLE_A)
    b = apply_research_summary_skill(ARTICLE_B)
    print(a)
    print(b)
    print(set(a) == set(b))
