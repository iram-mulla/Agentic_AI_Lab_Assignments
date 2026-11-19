from reference import run_swarm, merge

def marketing_agent(_):
    return {"role": "marketing", "output": {"publicity_plan": "campus ambassadors and social posts", "cost": 35000}}

outputs = run_swarm("hackathon")
outputs["marketing"] = marketing_agent("hackathon")
draft = merge(outputs)
draft["marketing_cost"] = outputs["marketing"]["output"]["cost"]
conflicts = []
if draft["marketing_cost"] > draft["budget_cap"]:
    conflicts.append({"conflict": "marketing_cost exceeds budget_cap", "roles": ["marketing", "budget"], "rule": "budget_over_preference"})
print({"draft": draft, "conflicts": conflicts})
