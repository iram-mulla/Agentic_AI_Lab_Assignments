from copy import deepcopy
import json

plan = {"Monday": {"subject": "DS", "time": "17:00-19:00"}, "Tuesday": {"subject": "OS", "time": "17:00-19:00"}, "Wednesday": {"subject": "AI", "time": "20:00-22:00"}, "Thursday": {"subject": "DS", "time": "17:00-19:00"}, "Friday": {"subject": "OS", "time": "17:00-19:00"}}
log = []

def revise(feedback):
    log.append({"iteration": len(log) + 1, "action": "revise_existing_plan", "feedback": feedback, "regenerated": False})
    if "tuesday" in feedback.lower() and "evening" in feedback.lower():
        plan["Tuesday"]["time"] = "20:00-22:00"
    if "friday" in feedback.lower() and ("shorter" in feedback.lower() or "one hour" in feedback.lower()):
        plan["Friday"]["time"] = "17:00-18:00"
    log.append({"iteration": len(log) + 1, "action": "revision_applied", "plan": deepcopy(plan), "regenerated": False})

revise("Move Tuesday's session to the evening.")
revise("Also make Friday's session shorter, only one hour.")
print(json.dumps({"plan": plan, "log": log}, indent=2))
assert log[-1]["plan"] is not plan
