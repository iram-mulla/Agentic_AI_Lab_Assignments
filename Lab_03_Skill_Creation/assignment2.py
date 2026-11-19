article = {"title": "Low Evidence", "text": "The system is the best available solution."}

def apply_skill(text):
    lower = text.lower()
    return {
        "claim": text,
        "evidence": "not stated in source",
        "limitation": "not stated in source",
        "fabrication_detected": False,
    }

print(apply_skill(article["text"]))
