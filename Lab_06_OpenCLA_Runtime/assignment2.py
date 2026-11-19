from datetime import datetime

audit = []


def run_skill(skill, user):
    prior_failures = sum(
        1
        for entry in audit
        if entry["user"] == user
        and entry["skill"] == skill
        and entry["error"]
        and not entry["escalated"]
    )

    if prior_failures >= 2:
        result = {
            "escalated": True,
            "reason": f"{skill} failed twice for user {user}; human escalation required",
        }
        audit.append({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "user": user,
            "skill": skill,
            "error": None,
            "escalated": True,
            "result": result,
        })
        return result

    result = {"result": "failed", "attempt": prior_failures + 1}
    audit.append({
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "user": user,
        "skill": skill,
        "error": "simulated failure",
        "escalated": False,
        "result": result,
    })
    return result


if __name__ == "__main__":
    print("=== Same user and same skill: draft_email ===")
    for attempt in range(1, 4):
        print(f"attempt {attempt}: {run_skill('draft_email', 'uday')}")

    print("\n=== Different skill does not consume draft_email failures ===")
    print(run_skill("summarize_notes", "uday"))

    print("\n=== Audit evidence ===")
    for entry in audit:
        print(entry)

    escalation = audit[-2]["escalated"] if len(audit) >= 2 else False
