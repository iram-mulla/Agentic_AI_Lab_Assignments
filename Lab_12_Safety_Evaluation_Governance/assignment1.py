BUDGET = 10000

def propose(cost, finance_approved=False):
    if cost is None:
        return {"rejected": True, "reason": "cost estimate omitted"}
    if cost > BUDGET and not finance_approved:
        return {"rejected": True, "reason": "cost exceeds budget without finance approval"}
    return {"approved": True}

print(propose(15000))
print(propose(None))
print(propose(15000, True))
