def builder(failures):
    for attempt in range(1, 3):
        if attempt > failures:
            return {"success": True, "attempts": attempt}
    return {"success": False, "attempts": 2, "escalated": True}

print(builder(1))
print(builder(2))
