FAQ_DB = {"wifi": "Campus-Secure login", "password": "Use password-reset portal"}

def faq_triage(issue):
    for key, answer in FAQ_DB.items():
        if key in issue.lower(): return {"skill": "faq_triage", "resolution": "faq", "answer": answer}
    return {"resolution": "escalated"}

def password_reset_skill(issue):
    if "password" in issue.lower() or "forgot" in issue.lower():
        return {"skill": "password_reset", "resolution": "faq", "answer": FAQ_DB["password"]}
    return None

print(password_reset_skill("I forgot my password"))
print(faq_triage("How do I connect to wifi?"))
