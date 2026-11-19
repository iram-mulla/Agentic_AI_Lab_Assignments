"""Parallel four-role hackathon swarm."""
from concurrent.futures import ThreadPoolExecutor

def research_agent(goal):
    return {"role": "research", "output": "Past events favored a 24-hour format with themed tracks."}

def logistics_agent(goal):
    return {"role": "logistics", "output": {"venue": "Grand Hall", "venue_cost": 45000, "date": "Saturday"}}

def budget_agent(goal):
    return {"role": "budget", "output": {"total_cap": 30000}}

def judging_agent(goal):
    return {"role": "judging", "output": "Judge on innovation, technical depth, and demo quality."}

ROLES = {
    "research": research_agent,
    "logistics": logistics_agent,
    "budget": budget_agent,
    "judging": judging_agent,
}

def run_swarm(goal):
    with ThreadPoolExecutor(max_workers=len(ROLES)) as pool:
        futures = {name: pool.submit(function, goal) for name, function in ROLES.items()}
        return {name: future.result() for name, future in futures.items()}

def merge(outputs):
    return {
        "format_notes": outputs["research"]["output"],
        "venue": outputs["logistics"]["output"]["venue"],
        "venue_cost": outputs["logistics"]["output"]["venue_cost"],
        "date": outputs["logistics"]["output"]["date"],
        "budget_cap": outputs["budget"]["output"]["total_cap"],
        "judging_criteria": outputs["judging"]["output"],
    }

def critique(draft):
    if draft["venue_cost"] > draft["budget_cap"]:
        return [{"conflict": "venue_cost exceeds budget_cap", "roles_involved": ["logistics", "budget"], "logistics_value": draft["venue_cost"], "budget_value": draft["budget_cap"]}]
    return []

def resolve(conflict):
    return {"rule_applied": "budget_over_preference", "resolution": f"Reject venue at {conflict['logistics_value']}; request an alternative under {conflict['budget_value']}."}

if __name__ == "__main__":
    outputs = run_swarm("Plan a college AI hackathon")
    draft = merge(outputs)
    conflicts = critique(draft)
    print(outputs)
    print(draft)
    print([resolve(conflict) for conflict in conflicts])
