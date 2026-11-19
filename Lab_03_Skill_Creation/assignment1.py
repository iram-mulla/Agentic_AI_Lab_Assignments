def apply_multi_claim(article):
    claims = [s.strip() for s in article["text"].split(".") if s.strip()]
    evidence_scores = [sum(word in claim.lower() for word in ("percent", "%", "measured", "study", "cost")) for claim in claims]
    selected = claims[evidence_scores.index(max(evidence_scores))]
    return {"selected_claim": selected, "selection_made": True, "note": "Selected the claim with the strongest explicit evidence among competing claims.", "limitation": "not stated in source"}

article = {"text": "The system cut cost by 30% in a controlled study. Accuracy improved by 15% in a pilot."}
print(apply_multi_claim(article))
