LOAD_LOG = [{"load_kw": 42}, {"load_kw": 48}, {"load_kw": 57}, {"load_kw": 68}]

def classify_electrical(reading):
    if reading["load_kw"] >= 65: return "ALARM"
    if reading["load_kw"] >= 55: return "WARNING"
    return "NORMAL"

def safety(condition):
    return {"action_allowed": "recommend_isolation_for_human_review", "auto_execute": False} if condition == "ALARM" else {"action_allowed": "continue_forecasting", "auto_execute": True}

latest = LOAD_LOG[-1]
condition = classify_electrical(latest)
print({"domain": "Electrical Load Forecasting", "condition": condition, "safety": safety(condition)})
