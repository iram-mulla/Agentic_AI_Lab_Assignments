def risk_level(action):
    return "high" if action == "rollback" else "low"

def execute(action):
    if risk_level(action) == "high":
        return {"status": "AWAITING HUMAN APPROVAL", "action_executed": False}
    return {"status": "AUTO_EXECUTED", "action_executed": True}

warning_action = execute("restart_single_pod")
rollback_action = execute("rollback")
print({"warning": warning_action, "rollback": rollback_action})
assert warning_action["action_executed"]
assert not rollback_action["action_executed"]
