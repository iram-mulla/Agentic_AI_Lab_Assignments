draft = {
    "venue_cost": 45000,
    "budget_cap": 30000,
    "marketing_cost": 8000,
    "venue_preference": "Grand Hall",
    "judging_criteria": ["innovation", "technical depth", "demo quality"],
}

role_critiques = {
    "research": [],
    "logistics": [],
    "budget": [],
    "judging": [],
}

if draft["venue_preference"] == "Grand Hall":
    role_critiques["research"].append(
        "Verify that Grand Hall capacity and format support the proposed 24-hour event."
    )

if draft["venue_cost"] > draft["budget_cap"]:
    role_critiques["logistics"].append(
        "Propose an alternative venue under the 30000 budget."
    )
    role_critiques["budget"].append(
        "Venue cost 45000 exceeds the 30000 total budget cap."
    )

if draft["marketing_cost"] > 5000:
    role_critiques["budget"].append(
        "Marketing cost 8000 exceeds the role's 5000 planned allocation."
    )

if not draft["judging_criteria"]:
    role_critiques["judging"].append(
        "Judging criteria are missing from the merged draft."
    )
else:
    role_critiques["judging"].append(
        "Confirm that judging criteria remain consistent with venue and format constraints."
    )

conflict_log = []
for role, objections in role_critiques.items():
    for objection in objections:
        conflict_log.append({"raised_by": role, "objection": objection})

print({"role_critiques": role_critiques, "conflict_log": conflict_log})
