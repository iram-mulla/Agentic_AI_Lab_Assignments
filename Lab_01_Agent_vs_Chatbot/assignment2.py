import json

def build_plan(unavailable, busy_days):
    conflicts = sorted(set(unavailable) & set(busy_days))
    if conflicts:
        return {"status": "CONFLICT", "conflicts": conflicts, "message": f"Selected unavailable days conflict with busy days: {', '.join(conflicts)}"}
    return {"status": "OK", "plan": ["Monday", "Tuesday", "Thursday", "Friday"]}

result = build_plan(["Sunday", "Wednesday"], ["Wednesday", "Saturday"])
print(json.dumps(result, indent=2))
assert result["status"] == "CONFLICT"
